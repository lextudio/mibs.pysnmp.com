# SNMP MIB module (EXPRESSGS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/EXPRESSGS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:41:13 2024
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

_Intel_ObjectIdentity = ObjectIdentity
intel = _Intel_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 343)
)
_Mib2ext_ObjectIdentity = ObjectIdentity
mib2ext = _Mib2ext_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 343, 6)
)
_EsGigaSwitch_ObjectIdentity = ObjectIdentity
esGigaSwitch = _EsGigaSwitch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 343, 6, 13)
)
_ExpressGSAgent_ObjectIdentity = ObjectIdentity
expressGSAgent = _ExpressGSAgent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 343, 6, 13, 1)
)
_ExpressGSAgentGen_ObjectIdentity = ObjectIdentity
expressGSAgentGen = _ExpressGSAgentGen_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 343, 6, 13, 1, 1)
)


class _ExpressGSAgentMIBVersion_Type(DisplayString):
    """Custom type expressGSAgentMIBVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_ExpressGSAgentMIBVersion_Type.__name__ = "DisplayString"
_ExpressGSAgentMIBVersion_Object = MibScalar
expressGSAgentMIBVersion = _ExpressGSAgentMIBVersion_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 13, 1, 1, 1),
    _ExpressGSAgentMIBVersion_Type()
)
expressGSAgentMIBVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    expressGSAgentMIBVersion.setStatus("mandatory")
_ExpressGSAgentMgrIndex_Type = Integer32
_ExpressGSAgentMgrIndex_Object = MibScalar
expressGSAgentMgrIndex = _ExpressGSAgentMgrIndex_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 13, 1, 1, 2),
    _ExpressGSAgentMgrIndex_Type()
)
expressGSAgentMgrIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    expressGSAgentMgrIndex.setStatus("mandatory")
_ExpressGSAgentCommunity_ObjectIdentity = ObjectIdentity
expressGSAgentCommunity = _ExpressGSAgentCommunity_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 343, 6, 13, 1, 2)
)
_ExpressGSCommunityTable_Object = MibTable
expressGSCommunityTable = _ExpressGSCommunityTable_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 13, 1, 2, 1)
)
if mibBuilder.loadTexts:
    expressGSCommunityTable.setStatus("mandatory")
_ExpressGSCommunityEntry_Object = MibTableRow
expressGSCommunityEntry = _ExpressGSCommunityEntry_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 13, 1, 2, 1, 1)
)
expressGSCommunityEntry.setIndexNames(
    (0, "EXPRESSGS-MIB", "expressGSCommunityIndex"),
)
if mibBuilder.loadTexts:
    expressGSCommunityEntry.setStatus("mandatory")
_ExpressGSCommunityIndex_Type = Integer32
_ExpressGSCommunityIndex_Object = MibTableColumn
expressGSCommunityIndex = _ExpressGSCommunityIndex_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 13, 1, 2, 1, 1, 1),
    _ExpressGSCommunityIndex_Type()
)
expressGSCommunityIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    expressGSCommunityIndex.setStatus("mandatory")


class _ExpressGSCommunityString_Type(DisplayString):
    """Custom type expressGSCommunityString based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_ExpressGSCommunityString_Type.__name__ = "DisplayString"
_ExpressGSCommunityString_Object = MibTableColumn
expressGSCommunityString = _ExpressGSCommunityString_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 13, 1, 2, 1, 1, 2),
    _ExpressGSCommunityString_Type()
)
expressGSCommunityString.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    expressGSCommunityString.setStatus("mandatory")


class _ExpressGSCommunityAddressType_Type(Integer32):
    """Custom type expressGSCommunityAddressType based on Integer32"""
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


_ExpressGSCommunityAddressType_Type.__name__ = "Integer32"
_ExpressGSCommunityAddressType_Object = MibTableColumn
expressGSCommunityAddressType = _ExpressGSCommunityAddressType_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 13, 1, 2, 1, 1, 3),
    _ExpressGSCommunityAddressType_Type()
)
expressGSCommunityAddressType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    expressGSCommunityAddressType.setStatus("mandatory")
_ExpressGSCommunityAddress_Type = IpAddress
_ExpressGSCommunityAddress_Object = MibTableColumn
expressGSCommunityAddress = _ExpressGSCommunityAddress_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 13, 1, 2, 1, 1, 4),
    _ExpressGSCommunityAddress_Type()
)
expressGSCommunityAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    expressGSCommunityAddress.setStatus("mandatory")


class _ExpressGSCommunityAccess_Type(Integer32):
    """Custom type expressGSCommunityAccess based on Integer32"""
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


_ExpressGSCommunityAccess_Type.__name__ = "Integer32"
_ExpressGSCommunityAccess_Object = MibTableColumn
expressGSCommunityAccess = _ExpressGSCommunityAccess_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 13, 1, 2, 1, 1, 5),
    _ExpressGSCommunityAccess_Type()
)
expressGSCommunityAccess.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    expressGSCommunityAccess.setStatus("mandatory")


class _ExpressGSCommunityTrapReceiver_Type(Integer32):
    """Custom type expressGSCommunityTrapReceiver based on Integer32"""
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


_ExpressGSCommunityTrapReceiver_Type.__name__ = "Integer32"
_ExpressGSCommunityTrapReceiver_Object = MibTableColumn
expressGSCommunityTrapReceiver = _ExpressGSCommunityTrapReceiver_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 13, 1, 2, 1, 1, 6),
    _ExpressGSCommunityTrapReceiver_Type()
)
expressGSCommunityTrapReceiver.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    expressGSCommunityTrapReceiver.setStatus("mandatory")


class _ExpressGSCommunitySecurityLevel_Type(Integer32):
    """Custom type expressGSCommunitySecurityLevel based on Integer32"""
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


_ExpressGSCommunitySecurityLevel_Type.__name__ = "Integer32"
_ExpressGSCommunitySecurityLevel_Object = MibTableColumn
expressGSCommunitySecurityLevel = _ExpressGSCommunitySecurityLevel_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 13, 1, 2, 1, 1, 7),
    _ExpressGSCommunitySecurityLevel_Type()
)
expressGSCommunitySecurityLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    expressGSCommunitySecurityLevel.setStatus("mandatory")
_ExpressGSCommunityStatus_Type = RowStatus
_ExpressGSCommunityStatus_Object = MibTableColumn
expressGSCommunityStatus = _ExpressGSCommunityStatus_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 13, 1, 2, 1, 1, 8),
    _ExpressGSCommunityStatus_Type()
)
expressGSCommunityStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    expressGSCommunityStatus.setStatus("mandatory")
_ExpressGSAgentWeb_ObjectIdentity = ObjectIdentity
expressGSAgentWeb = _ExpressGSAgentWeb_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 343, 6, 13, 1, 3)
)


class _ExpressGSAgentWebServerURL_Type(DisplayString):
    """Custom type expressGSAgentWebServerURL based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_ExpressGSAgentWebServerURL_Type.__name__ = "DisplayString"
_ExpressGSAgentWebServerURL_Object = MibScalar
expressGSAgentWebServerURL = _ExpressGSAgentWebServerURL_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 13, 1, 3, 1),
    _ExpressGSAgentWebServerURL_Type()
)
expressGSAgentWebServerURL.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    expressGSAgentWebServerURL.setStatus("mandatory")


class _ExpressGSAgentWebServerHelpDirectory_Type(DisplayString):
    """Custom type expressGSAgentWebServerHelpDirectory based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_ExpressGSAgentWebServerHelpDirectory_Type.__name__ = "DisplayString"
_ExpressGSAgentWebServerHelpDirectory_Object = MibScalar
expressGSAgentWebServerHelpDirectory = _ExpressGSAgentWebServerHelpDirectory_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 13, 1, 3, 2),
    _ExpressGSAgentWebServerHelpDirectory_Type()
)
expressGSAgentWebServerHelpDirectory.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    expressGSAgentWebServerHelpDirectory.setStatus("mandatory")
_ExpressGSChassis_ObjectIdentity = ObjectIdentity
expressGSChassis = _ExpressGSChassis_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 343, 6, 13, 3)
)
_ExpressGSChassisGen_ObjectIdentity = ObjectIdentity
expressGSChassisGen = _ExpressGSChassisGen_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 343, 6, 13, 3, 1)
)


class _ExpressGSChassisType_Type(Integer32):
    """Custom type expressGSChassisType based on Integer32"""
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


_ExpressGSChassisType_Type.__name__ = "Integer32"
_ExpressGSChassisType_Object = MibScalar
expressGSChassisType = _ExpressGSChassisType_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 13, 3, 1, 1),
    _ExpressGSChassisType_Type()
)
expressGSChassisType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    expressGSChassisType.setStatus("mandatory")
_ExpressGSChassisSlots_Type = Integer32
_ExpressGSChassisSlots_Object = MibScalar
expressGSChassisSlots = _ExpressGSChassisSlots_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 13, 3, 1, 2),
    _ExpressGSChassisSlots_Type()
)
expressGSChassisSlots.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    expressGSChassisSlots.setStatus("mandatory")
_ExpressGSInventory_ObjectIdentity = ObjectIdentity
expressGSInventory = _ExpressGSInventory_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 343, 6, 13, 3, 2)
)
_ExpressGSInventoryTable_Object = MibTable
expressGSInventoryTable = _ExpressGSInventoryTable_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 13, 3, 2, 1)
)
if mibBuilder.loadTexts:
    expressGSInventoryTable.setStatus("mandatory")
_ExpressGSInventoryEntry_Object = MibTableRow
expressGSInventoryEntry = _ExpressGSInventoryEntry_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 13, 3, 2, 1, 1)
)
expressGSInventoryEntry.setIndexNames(
    (0, "EXPRESSGS-MIB", "expressGSInventoryResourceType"),
    (0, "EXPRESSGS-MIB", "expressGSInventoryResourceIndex"),
)
if mibBuilder.loadTexts:
    expressGSInventoryEntry.setStatus("mandatory")
_ExpressGSInventoryResourceType_Type = ResourceType
_ExpressGSInventoryResourceType_Object = MibTableColumn
expressGSInventoryResourceType = _ExpressGSInventoryResourceType_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 13, 3, 2, 1, 1, 1),
    _ExpressGSInventoryResourceType_Type()
)
expressGSInventoryResourceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    expressGSInventoryResourceType.setStatus("mandatory")
_ExpressGSInventoryResourceIndex_Type = ResourceId
_ExpressGSInventoryResourceIndex_Object = MibTableColumn
expressGSInventoryResourceIndex = _ExpressGSInventoryResourceIndex_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 13, 3, 2, 1, 1, 2),
    _ExpressGSInventoryResourceIndex_Type()
)
expressGSInventoryResourceIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    expressGSInventoryResourceIndex.setStatus("mandatory")


class _ExpressGSInventoryModelNumber_Type(DisplayString):
    """Custom type expressGSInventoryModelNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_ExpressGSInventoryModelNumber_Type.__name__ = "DisplayString"
_ExpressGSInventoryModelNumber_Object = MibTableColumn
expressGSInventoryModelNumber = _ExpressGSInventoryModelNumber_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 13, 3, 2, 1, 1, 3),
    _ExpressGSInventoryModelNumber_Type()
)
expressGSInventoryModelNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    expressGSInventoryModelNumber.setStatus("mandatory")


class _ExpressGSInventorySerialNumber_Type(DisplayString):
    """Custom type expressGSInventorySerialNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_ExpressGSInventorySerialNumber_Type.__name__ = "DisplayString"
_ExpressGSInventorySerialNumber_Object = MibTableColumn
expressGSInventorySerialNumber = _ExpressGSInventorySerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 13, 3, 2, 1, 1, 4),
    _ExpressGSInventorySerialNumber_Type()
)
expressGSInventorySerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    expressGSInventorySerialNumber.setStatus("mandatory")


class _ExpressGSInventoryVersion_Type(DisplayString):
    """Custom type expressGSInventoryVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_ExpressGSInventoryVersion_Type.__name__ = "DisplayString"
_ExpressGSInventoryVersion_Object = MibTableColumn
expressGSInventoryVersion = _ExpressGSInventoryVersion_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 13, 3, 2, 1, 1, 5),
    _ExpressGSInventoryVersion_Type()
)
expressGSInventoryVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    expressGSInventoryVersion.setStatus("mandatory")


class _ExpressGSInventoryManufactureInfo_Type(DisplayString):
    """Custom type expressGSInventoryManufactureInfo based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_ExpressGSInventoryManufactureInfo_Type.__name__ = "DisplayString"
_ExpressGSInventoryManufactureInfo_Object = MibTableColumn
expressGSInventoryManufactureInfo = _ExpressGSInventoryManufactureInfo_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 13, 3, 2, 1, 1, 6),
    _ExpressGSInventoryManufactureInfo_Type()
)
expressGSInventoryManufactureInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    expressGSInventoryManufactureInfo.setStatus("mandatory")


class _ExpressGSInventoryScratchPad_Type(DisplayString):
    """Custom type expressGSInventoryScratchPad based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_ExpressGSInventoryScratchPad_Type.__name__ = "DisplayString"
_ExpressGSInventoryScratchPad_Object = MibTableColumn
expressGSInventoryScratchPad = _ExpressGSInventoryScratchPad_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 13, 3, 2, 1, 1, 7),
    _ExpressGSInventoryScratchPad_Type()
)
expressGSInventoryScratchPad.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    expressGSInventoryScratchPad.setStatus("mandatory")
_ExpressGSPowerSystems_ObjectIdentity = ObjectIdentity
expressGSPowerSystems = _ExpressGSPowerSystems_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 343, 6, 13, 3, 3)
)
_ExpressGSPowerSupplies_ObjectIdentity = ObjectIdentity
expressGSPowerSupplies = _ExpressGSPowerSupplies_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 343, 6, 13, 3, 3, 1)
)
_ExpressGSPowerSupplyTable_Object = MibTable
expressGSPowerSupplyTable = _ExpressGSPowerSupplyTable_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 13, 3, 3, 1, 1)
)
if mibBuilder.loadTexts:
    expressGSPowerSupplyTable.setStatus("mandatory")
_ExpressGSPowerSupplyEntry_Object = MibTableRow
expressGSPowerSupplyEntry = _ExpressGSPowerSupplyEntry_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 13, 3, 3, 1, 1, 1)
)
expressGSPowerSupplyEntry.setIndexNames(
    (0, "EXPRESSGS-MIB", "expressGSPowerSupplyIndex"),
)
if mibBuilder.loadTexts:
    expressGSPowerSupplyEntry.setStatus("mandatory")
_ExpressGSPowerSupplyIndex_Type = ResourceId
_ExpressGSPowerSupplyIndex_Object = MibTableColumn
expressGSPowerSupplyIndex = _ExpressGSPowerSupplyIndex_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 13, 3, 3, 1, 1, 1, 1),
    _ExpressGSPowerSupplyIndex_Type()
)
expressGSPowerSupplyIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    expressGSPowerSupplyIndex.setStatus("mandatory")


class _ExpressGSPowerSupplyType_Type(Integer32):
    """Custom type expressGSPowerSupplyType based on Integer32"""
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


_ExpressGSPowerSupplyType_Type.__name__ = "Integer32"
_ExpressGSPowerSupplyType_Object = MibTableColumn
expressGSPowerSupplyType = _ExpressGSPowerSupplyType_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 13, 3, 3, 1, 1, 1, 2),
    _ExpressGSPowerSupplyType_Type()
)
expressGSPowerSupplyType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    expressGSPowerSupplyType.setStatus("mandatory")


class _ExpressGSPowerSupplyStatus_Type(Integer32):
    """Custom type expressGSPowerSupplyStatus based on Integer32"""
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


_ExpressGSPowerSupplyStatus_Type.__name__ = "Integer32"
_ExpressGSPowerSupplyStatus_Object = MibTableColumn
expressGSPowerSupplyStatus = _ExpressGSPowerSupplyStatus_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 13, 3, 3, 1, 1, 1, 3),
    _ExpressGSPowerSupplyStatus_Type()
)
expressGSPowerSupplyStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    expressGSPowerSupplyStatus.setStatus("mandatory")


class _ExpressGSPowerSupplyInputStatus_Type(Integer32):
    """Custom type expressGSPowerSupplyInputStatus based on Integer32"""
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


_ExpressGSPowerSupplyInputStatus_Type.__name__ = "Integer32"
_ExpressGSPowerSupplyInputStatus_Object = MibTableColumn
expressGSPowerSupplyInputStatus = _ExpressGSPowerSupplyInputStatus_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 13, 3, 3, 1, 1, 1, 4),
    _ExpressGSPowerSupplyInputStatus_Type()
)
expressGSPowerSupplyInputStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    expressGSPowerSupplyInputStatus.setStatus("mandatory")


class _ExpressGSPowerSupplyOutputStatus_Type(Integer32):
    """Custom type expressGSPowerSupplyOutputStatus based on Integer32"""
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


_ExpressGSPowerSupplyOutputStatus_Type.__name__ = "Integer32"
_ExpressGSPowerSupplyOutputStatus_Object = MibTableColumn
expressGSPowerSupplyOutputStatus = _ExpressGSPowerSupplyOutputStatus_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 13, 3, 3, 1, 1, 1, 5),
    _ExpressGSPowerSupplyOutputStatus_Type()
)
expressGSPowerSupplyOutputStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    expressGSPowerSupplyOutputStatus.setStatus("mandatory")
_ExpressGSPowerSupplyOutputCapacity_Type = Integer32
_ExpressGSPowerSupplyOutputCapacity_Object = MibTableColumn
expressGSPowerSupplyOutputCapacity = _ExpressGSPowerSupplyOutputCapacity_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 13, 3, 3, 1, 1, 1, 6),
    _ExpressGSPowerSupplyOutputCapacity_Type()
)
expressGSPowerSupplyOutputCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    expressGSPowerSupplyOutputCapacity.setStatus("mandatory")
_ExpressGSPowerMgmtGen_ObjectIdentity = ObjectIdentity
expressGSPowerMgmtGen = _ExpressGSPowerMgmtGen_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 343, 6, 13, 3, 3, 2)
)
_ExpressGSPowerCapacity_Type = Integer32
_ExpressGSPowerCapacity_Object = MibScalar
expressGSPowerCapacity = _ExpressGSPowerCapacity_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 13, 3, 3, 2, 1),
    _ExpressGSPowerCapacity_Type()
)
expressGSPowerCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    expressGSPowerCapacity.setStatus("mandatory")
_ExpressGSPowerUsed_Type = Integer32
_ExpressGSPowerUsed_Object = MibScalar
expressGSPowerUsed = _ExpressGSPowerUsed_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 13, 3, 3, 2, 2),
    _ExpressGSPowerUsed_Type()
)
expressGSPowerUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    expressGSPowerUsed.setStatus("mandatory")
_ExpressGSPowerMgmtCtl_ObjectIdentity = ObjectIdentity
expressGSPowerMgmtCtl = _ExpressGSPowerMgmtCtl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 343, 6, 13, 3, 3, 3)
)
_ExpressGSPowerControlTable_Object = MibTable
expressGSPowerControlTable = _ExpressGSPowerControlTable_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 13, 3, 3, 3, 1)
)
if mibBuilder.loadTexts:
    expressGSPowerControlTable.setStatus("mandatory")
_ExpressGSPowerControlEntry_Object = MibTableRow
expressGSPowerControlEntry = _ExpressGSPowerControlEntry_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 13, 3, 3, 3, 1, 1)
)
expressGSPowerControlEntry.setIndexNames(
    (0, "EXPRESSGS-MIB", "expressGSModuleIndex"),
)
if mibBuilder.loadTexts:
    expressGSPowerControlEntry.setStatus("mandatory")
_ExpressGSPowerControlUsed_Type = Integer32
_ExpressGSPowerControlUsed_Object = MibTableColumn
expressGSPowerControlUsed = _ExpressGSPowerControlUsed_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 13, 3, 3, 3, 1, 1, 1),
    _ExpressGSPowerControlUsed_Type()
)
expressGSPowerControlUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    expressGSPowerControlUsed.setStatus("mandatory")


class _ExpressGSPowerControlPriority_Type(Integer32):
    """Custom type expressGSPowerControlPriority based on Integer32"""
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


_ExpressGSPowerControlPriority_Type.__name__ = "Integer32"
_ExpressGSPowerControlPriority_Object = MibTableColumn
expressGSPowerControlPriority = _ExpressGSPowerControlPriority_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 13, 3, 3, 3, 1, 1, 2),
    _ExpressGSPowerControlPriority_Type()
)
expressGSPowerControlPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    expressGSPowerControlPriority.setStatus("mandatory")


class _ExpressGSPowerControlMode_Type(Integer32):
    """Custom type expressGSPowerControlMode based on Integer32"""
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


_ExpressGSPowerControlMode_Type.__name__ = "Integer32"
_ExpressGSPowerControlMode_Object = MibTableColumn
expressGSPowerControlMode = _ExpressGSPowerControlMode_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 13, 3, 3, 3, 1, 1, 3),
    _ExpressGSPowerControlMode_Type()
)
expressGSPowerControlMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    expressGSPowerControlMode.setStatus("mandatory")
_ExpressGSTemperature_ObjectIdentity = ObjectIdentity
expressGSTemperature = _ExpressGSTemperature_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 343, 6, 13, 3, 4)
)
_ExpressGSTempTable_Object = MibTable
expressGSTempTable = _ExpressGSTempTable_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 13, 3, 4, 1)
)
if mibBuilder.loadTexts:
    expressGSTempTable.setStatus("mandatory")
_ExpressGSTempEntry_Object = MibTableRow
expressGSTempEntry = _ExpressGSTempEntry_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 13, 3, 4, 1, 1)
)
expressGSTempEntry.setIndexNames(
    (0, "EXPRESSGS-MIB", "expressGSTempIndex"),
)
if mibBuilder.loadTexts:
    expressGSTempEntry.setStatus("mandatory")
_ExpressGSTempIndex_Type = ResourceId
_ExpressGSTempIndex_Object = MibTableColumn
expressGSTempIndex = _ExpressGSTempIndex_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 13, 3, 4, 1, 1, 1),
    _ExpressGSTempIndex_Type()
)
expressGSTempIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    expressGSTempIndex.setStatus("mandatory")
_ExpressGSTempValue_Type = Integer32
_ExpressGSTempValue_Object = MibTableColumn
expressGSTempValue = _ExpressGSTempValue_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 13, 3, 4, 1, 1, 2),
    _ExpressGSTempValue_Type()
)
expressGSTempValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    expressGSTempValue.setStatus("mandatory")
_ExpressGSTempUpperLimit_Type = Integer32
_ExpressGSTempUpperLimit_Object = MibTableColumn
expressGSTempUpperLimit = _ExpressGSTempUpperLimit_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 13, 3, 4, 1, 1, 3),
    _ExpressGSTempUpperLimit_Type()
)
expressGSTempUpperLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    expressGSTempUpperLimit.setStatus("mandatory")
_ExpressGSTempUpperWarning_Type = Integer32
_ExpressGSTempUpperWarning_Object = MibTableColumn
expressGSTempUpperWarning = _ExpressGSTempUpperWarning_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 13, 3, 4, 1, 1, 4),
    _ExpressGSTempUpperWarning_Type()
)
expressGSTempUpperWarning.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    expressGSTempUpperWarning.setStatus("mandatory")
_ExpressGSTempLowerWarning_Type = Integer32
_ExpressGSTempLowerWarning_Object = MibTableColumn
expressGSTempLowerWarning = _ExpressGSTempLowerWarning_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 13, 3, 4, 1, 1, 5),
    _ExpressGSTempLowerWarning_Type()
)
expressGSTempLowerWarning.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    expressGSTempLowerWarning.setStatus("mandatory")
_ExpressGSTempLowerLimit_Type = Integer32
_ExpressGSTempLowerLimit_Object = MibTableColumn
expressGSTempLowerLimit = _ExpressGSTempLowerLimit_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 13, 3, 4, 1, 1, 6),
    _ExpressGSTempLowerLimit_Type()
)
expressGSTempLowerLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    expressGSTempLowerLimit.setStatus("mandatory")
_ExpressGSModules_ObjectIdentity = ObjectIdentity
expressGSModules = _ExpressGSModules_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 343, 6, 13, 3, 5)
)
_ExpressGSModuleTable_Object = MibTable
expressGSModuleTable = _ExpressGSModuleTable_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 13, 3, 5, 1)
)
if mibBuilder.loadTexts:
    expressGSModuleTable.setStatus("mandatory")
_ExpressGSModuleEntry_Object = MibTableRow
expressGSModuleEntry = _ExpressGSModuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 13, 3, 5, 1, 1)
)
expressGSModuleEntry.setIndexNames(
    (0, "EXPRESSGS-MIB", "expressGSModuleIndex"),
)
if mibBuilder.loadTexts:
    expressGSModuleEntry.setStatus("mandatory")
_ExpressGSModuleIndex_Type = ResourceId
_ExpressGSModuleIndex_Object = MibTableColumn
expressGSModuleIndex = _ExpressGSModuleIndex_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 13, 3, 5, 1, 1, 1),
    _ExpressGSModuleIndex_Type()
)
expressGSModuleIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    expressGSModuleIndex.setStatus("mandatory")


class _ExpressGSModuleName_Type(DisplayString):
    """Custom type expressGSModuleName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_ExpressGSModuleName_Type.__name__ = "DisplayString"
_ExpressGSModuleName_Object = MibTableColumn
expressGSModuleName = _ExpressGSModuleName_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 13, 3, 5, 1, 1, 2),
    _ExpressGSModuleName_Type()
)
expressGSModuleName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    expressGSModuleName.setStatus("mandatory")


class _ExpressGSModuleType_Type(Integer32):
    """Custom type expressGSModuleType based on Integer32"""
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


_ExpressGSModuleType_Type.__name__ = "Integer32"
_ExpressGSModuleType_Object = MibTableColumn
expressGSModuleType = _ExpressGSModuleType_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 13, 3, 5, 1, 1, 3),
    _ExpressGSModuleType_Type()
)
expressGSModuleType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    expressGSModuleType.setStatus("mandatory")


class _ExpressGSModuleBaseType_Type(Integer32):
    """Custom type expressGSModuleBaseType based on Integer32"""
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


_ExpressGSModuleBaseType_Type.__name__ = "Integer32"
_ExpressGSModuleBaseType_Object = MibTableColumn
expressGSModuleBaseType = _ExpressGSModuleBaseType_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 13, 3, 5, 1, 1, 4),
    _ExpressGSModuleBaseType_Type()
)
expressGSModuleBaseType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    expressGSModuleBaseType.setStatus("mandatory")
_ExpressGSModuleSlotWidth_Type = Integer32
_ExpressGSModuleSlotWidth_Object = MibTableColumn
expressGSModuleSlotWidth = _ExpressGSModuleSlotWidth_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 13, 3, 5, 1, 1, 5),
    _ExpressGSModuleSlotWidth_Type()
)
expressGSModuleSlotWidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    expressGSModuleSlotWidth.setStatus("mandatory")
_ExpressGSModuleSlotOffset_Type = Integer32
_ExpressGSModuleSlotOffset_Object = MibTableColumn
expressGSModuleSlotOffset = _ExpressGSModuleSlotOffset_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 13, 3, 5, 1, 1, 6),
    _ExpressGSModuleSlotOffset_Type()
)
expressGSModuleSlotOffset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    expressGSModuleSlotOffset.setStatus("mandatory")
_ExpressGSModulePorts_Type = Integer32
_ExpressGSModulePorts_Object = MibTableColumn
expressGSModulePorts = _ExpressGSModulePorts_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 13, 3, 5, 1, 1, 7),
    _ExpressGSModulePorts_Type()
)
expressGSModulePorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    expressGSModulePorts.setStatus("mandatory")
_ExpressGSPorts_ObjectIdentity = ObjectIdentity
expressGSPorts = _ExpressGSPorts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 343, 6, 13, 3, 6)
)
_ExpressGSPortMgt_ObjectIdentity = ObjectIdentity
expressGSPortMgt = _ExpressGSPortMgt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 343, 6, 13, 3, 6, 1)
)
_ExpressGSPortTable_Object = MibTable
expressGSPortTable = _ExpressGSPortTable_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 13, 3, 6, 1, 1)
)
if mibBuilder.loadTexts:
    expressGSPortTable.setStatus("mandatory")
_ExpressGSPortEntry_Object = MibTableRow
expressGSPortEntry = _ExpressGSPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 13, 3, 6, 1, 1, 1)
)
expressGSPortEntry.setIndexNames(
    (0, "EXPRESSGS-MIB", "expressGSPortIndex"),
)
if mibBuilder.loadTexts:
    expressGSPortEntry.setStatus("mandatory")
_ExpressGSPortIndex_Type = ResourceId
_ExpressGSPortIndex_Object = MibTableColumn
expressGSPortIndex = _ExpressGSPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 13, 3, 6, 1, 1, 1, 1),
    _ExpressGSPortIndex_Type()
)
expressGSPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    expressGSPortIndex.setStatus("mandatory")


class _ExpressGSPortName_Type(DisplayString):
    """Custom type expressGSPortName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_ExpressGSPortName_Type.__name__ = "DisplayString"
_ExpressGSPortName_Object = MibTableColumn
expressGSPortName = _ExpressGSPortName_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 13, 3, 6, 1, 1, 1, 2),
    _ExpressGSPortName_Type()
)
expressGSPortName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    expressGSPortName.setStatus("mandatory")


class _ExpressGSPortType_Type(Integer32):
    """Custom type expressGSPortType based on Integer32"""
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


_ExpressGSPortType_Type.__name__ = "Integer32"
_ExpressGSPortType_Object = MibTableColumn
expressGSPortType = _ExpressGSPortType_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 13, 3, 6, 1, 1, 1, 3),
    _ExpressGSPortType_Type()
)
expressGSPortType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    expressGSPortType.setStatus("mandatory")


class _ExpressGSPortBaseType_Type(Integer32):
    """Custom type expressGSPortBaseType based on Integer32"""
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


_ExpressGSPortBaseType_Type.__name__ = "Integer32"
_ExpressGSPortBaseType_Object = MibTableColumn
expressGSPortBaseType = _ExpressGSPortBaseType_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 13, 3, 6, 1, 1, 1, 4),
    _ExpressGSPortBaseType_Type()
)
expressGSPortBaseType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    expressGSPortBaseType.setStatus("mandatory")


class _ExpressGSPortMode_Type(Integer32):
    """Custom type expressGSPortMode based on Integer32"""
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


_ExpressGSPortMode_Type.__name__ = "Integer32"
_ExpressGSPortMode_Object = MibTableColumn
expressGSPortMode = _ExpressGSPortMode_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 13, 3, 6, 1, 1, 1, 5),
    _ExpressGSPortMode_Type()
)
expressGSPortMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    expressGSPortMode.setStatus("mandatory")


class _ExpressGSPortStatus_Type(Integer32):
    """Custom type expressGSPortStatus based on Integer32"""
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


_ExpressGSPortStatus_Type.__name__ = "Integer32"
_ExpressGSPortStatus_Object = MibTableColumn
expressGSPortStatus = _ExpressGSPortStatus_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 13, 3, 6, 1, 1, 1, 6),
    _ExpressGSPortStatus_Type()
)
expressGSPortStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    expressGSPortStatus.setStatus("mandatory")


class _ExpressGSPortConnector_Type(Integer32):
    """Custom type expressGSPortConnector based on Integer32"""
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


_ExpressGSPortConnector_Type.__name__ = "Integer32"
_ExpressGSPortConnector_Object = MibTableColumn
expressGSPortConnector = _ExpressGSPortConnector_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 13, 3, 6, 1, 1, 1, 7),
    _ExpressGSPortConnector_Type()
)
expressGSPortConnector.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    expressGSPortConnector.setStatus("mandatory")


class _ExpressGSPortSpeedState_Type(Integer32):
    """Custom type expressGSPortSpeedState based on Integer32"""
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


_ExpressGSPortSpeedState_Type.__name__ = "Integer32"
_ExpressGSPortSpeedState_Object = MibTableColumn
expressGSPortSpeedState = _ExpressGSPortSpeedState_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 13, 3, 6, 1, 1, 1, 8),
    _ExpressGSPortSpeedState_Type()
)
expressGSPortSpeedState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    expressGSPortSpeedState.setStatus("mandatory")


class _ExpressGSPortDuplexState_Type(Integer32):
    """Custom type expressGSPortDuplexState based on Integer32"""
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


_ExpressGSPortDuplexState_Type.__name__ = "Integer32"
_ExpressGSPortDuplexState_Object = MibTableColumn
expressGSPortDuplexState = _ExpressGSPortDuplexState_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 13, 3, 6, 1, 1, 1, 9),
    _ExpressGSPortDuplexState_Type()
)
expressGSPortDuplexState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    expressGSPortDuplexState.setStatus("mandatory")
_ExpressGSPortGroupBinding_Type = ResourceId
_ExpressGSPortGroupBinding_Object = MibTableColumn
expressGSPortGroupBinding = _ExpressGSPortGroupBinding_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 13, 3, 6, 1, 1, 1, 10),
    _ExpressGSPortGroupBinding_Type()
)
expressGSPortGroupBinding.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    expressGSPortGroupBinding.setStatus("mandatory")
_ExpressGSPortFlowControlMgt_ObjectIdentity = ObjectIdentity
expressGSPortFlowControlMgt = _ExpressGSPortFlowControlMgt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 343, 6, 13, 3, 6, 2)
)
_ExpressGSPortFlowControlTable_Object = MibTable
expressGSPortFlowControlTable = _ExpressGSPortFlowControlTable_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 13, 3, 6, 2, 1)
)
if mibBuilder.loadTexts:
    expressGSPortFlowControlTable.setStatus("mandatory")
_ExpressGSPortFlowControlEntry_Object = MibTableRow
expressGSPortFlowControlEntry = _ExpressGSPortFlowControlEntry_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 13, 3, 6, 2, 1, 1)
)
expressGSPortFlowControlEntry.setIndexNames(
    (0, "EXPRESSGS-MIB", "expressGSPortIndex"),
)
if mibBuilder.loadTexts:
    expressGSPortFlowControlEntry.setStatus("mandatory")


class _ExpressGSPortFlowControlMode_Type(Integer32):
    """Custom type expressGSPortFlowControlMode based on Integer32"""
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


_ExpressGSPortFlowControlMode_Type.__name__ = "Integer32"
_ExpressGSPortFlowControlMode_Object = MibTableColumn
expressGSPortFlowControlMode = _ExpressGSPortFlowControlMode_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 13, 3, 6, 2, 1, 1, 21),
    _ExpressGSPortFlowControlMode_Type()
)
expressGSPortFlowControlMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    expressGSPortFlowControlMode.setStatus("mandatory")
_ExpressGSPortDuplexMgt_ObjectIdentity = ObjectIdentity
expressGSPortDuplexMgt = _ExpressGSPortDuplexMgt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 343, 6, 13, 3, 6, 3)
)
_ExpressGSPortDuplexTable_Object = MibTable
expressGSPortDuplexTable = _ExpressGSPortDuplexTable_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 13, 3, 6, 3, 1)
)
if mibBuilder.loadTexts:
    expressGSPortDuplexTable.setStatus("mandatory")
_ExpressGSPortDuplexEntry_Object = MibTableRow
expressGSPortDuplexEntry = _ExpressGSPortDuplexEntry_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 13, 3, 6, 3, 1, 1)
)
expressGSPortDuplexEntry.setIndexNames(
    (0, "EXPRESSGS-MIB", "expressGSPortIndex"),
)
if mibBuilder.loadTexts:
    expressGSPortDuplexEntry.setStatus("mandatory")


class _ExpressGSPortDuplexMode_Type(Integer32):
    """Custom type expressGSPortDuplexMode based on Integer32"""
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


_ExpressGSPortDuplexMode_Type.__name__ = "Integer32"
_ExpressGSPortDuplexMode_Object = MibTableColumn
expressGSPortDuplexMode = _ExpressGSPortDuplexMode_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 13, 3, 6, 3, 1, 1, 31),
    _ExpressGSPortDuplexMode_Type()
)
expressGSPortDuplexMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    expressGSPortDuplexMode.setStatus("mandatory")
_ExpressGSPortSpeedMgt_ObjectIdentity = ObjectIdentity
expressGSPortSpeedMgt = _ExpressGSPortSpeedMgt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 343, 6, 13, 3, 6, 4)
)
_ExpressGSPortSpeedTable_Object = MibTable
expressGSPortSpeedTable = _ExpressGSPortSpeedTable_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 13, 3, 6, 4, 1)
)
if mibBuilder.loadTexts:
    expressGSPortSpeedTable.setStatus("mandatory")
_ExpressGSPortSpeedEntry_Object = MibTableRow
expressGSPortSpeedEntry = _ExpressGSPortSpeedEntry_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 13, 3, 6, 4, 1, 1)
)
expressGSPortSpeedEntry.setIndexNames(
    (0, "EXPRESSGS-MIB", "expressGSPortIndex"),
)
if mibBuilder.loadTexts:
    expressGSPortSpeedEntry.setStatus("mandatory")


class _ExpressGSPortSpeedMode_Type(Integer32):
    """Custom type expressGSPortSpeedMode based on Integer32"""
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


_ExpressGSPortSpeedMode_Type.__name__ = "Integer32"
_ExpressGSPortSpeedMode_Object = MibTableColumn
expressGSPortSpeedMode = _ExpressGSPortSpeedMode_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 13, 3, 6, 4, 1, 1, 41),
    _ExpressGSPortSpeedMode_Type()
)
expressGSPortSpeedMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    expressGSPortSpeedMode.setStatus("mandatory")
_ExpressGSPortAutoNegotiationMgt_ObjectIdentity = ObjectIdentity
expressGSPortAutoNegotiationMgt = _ExpressGSPortAutoNegotiationMgt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 343, 6, 13, 3, 6, 5)
)
_ExpressGSPortAutoNegotiationTable_Object = MibTable
expressGSPortAutoNegotiationTable = _ExpressGSPortAutoNegotiationTable_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 13, 3, 6, 5, 1)
)
if mibBuilder.loadTexts:
    expressGSPortAutoNegotiationTable.setStatus("mandatory")
_ExpressGSPortAutoNegotiationEntry_Object = MibTableRow
expressGSPortAutoNegotiationEntry = _ExpressGSPortAutoNegotiationEntry_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 13, 3, 6, 5, 1, 1)
)
expressGSPortAutoNegotiationEntry.setIndexNames(
    (0, "EXPRESSGS-MIB", "expressGSPortIndex"),
)
if mibBuilder.loadTexts:
    expressGSPortAutoNegotiationEntry.setStatus("mandatory")


class _ExpressGSPortAutoNegotiationMode_Type(Integer32):
    """Custom type expressGSPortAutoNegotiationMode based on Integer32"""
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


_ExpressGSPortAutoNegotiationMode_Type.__name__ = "Integer32"
_ExpressGSPortAutoNegotiationMode_Object = MibTableColumn
expressGSPortAutoNegotiationMode = _ExpressGSPortAutoNegotiationMode_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 13, 3, 6, 5, 1, 1, 51),
    _ExpressGSPortAutoNegotiationMode_Type()
)
expressGSPortAutoNegotiationMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    expressGSPortAutoNegotiationMode.setStatus("mandatory")


class _ExpressGSPortAutoNegotiationSpeedAdvertisement_Type(Integer32):
    """Custom type expressGSPortAutoNegotiationSpeedAdvertisement based on Integer32"""
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


_ExpressGSPortAutoNegotiationSpeedAdvertisement_Type.__name__ = "Integer32"
_ExpressGSPortAutoNegotiationSpeedAdvertisement_Object = MibTableColumn
expressGSPortAutoNegotiationSpeedAdvertisement = _ExpressGSPortAutoNegotiationSpeedAdvertisement_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 13, 3, 6, 5, 1, 1, 52),
    _ExpressGSPortAutoNegotiationSpeedAdvertisement_Type()
)
expressGSPortAutoNegotiationSpeedAdvertisement.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    expressGSPortAutoNegotiationSpeedAdvertisement.setStatus("mandatory")


class _ExpressGSPortAutoNegotiationDuplexAdvertisement_Type(Integer32):
    """Custom type expressGSPortAutoNegotiationDuplexAdvertisement based on Integer32"""
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


_ExpressGSPortAutoNegotiationDuplexAdvertisement_Type.__name__ = "Integer32"
_ExpressGSPortAutoNegotiationDuplexAdvertisement_Object = MibTableColumn
expressGSPortAutoNegotiationDuplexAdvertisement = _ExpressGSPortAutoNegotiationDuplexAdvertisement_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 13, 3, 6, 5, 1, 1, 53),
    _ExpressGSPortAutoNegotiationDuplexAdvertisement_Type()
)
expressGSPortAutoNegotiationDuplexAdvertisement.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    expressGSPortAutoNegotiationDuplexAdvertisement.setStatus("mandatory")
_ExpressGSPortRateLimitMgt_ObjectIdentity = ObjectIdentity
expressGSPortRateLimitMgt = _ExpressGSPortRateLimitMgt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 343, 6, 13, 3, 6, 6)
)
_ExpressGSPortRateLimitTable_Object = MibTable
expressGSPortRateLimitTable = _ExpressGSPortRateLimitTable_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 13, 3, 6, 6, 1)
)
if mibBuilder.loadTexts:
    expressGSPortRateLimitTable.setStatus("mandatory")
_ExpressGSPortRateLimitEntry_Object = MibTableRow
expressGSPortRateLimitEntry = _ExpressGSPortRateLimitEntry_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 13, 3, 6, 6, 1, 1)
)
expressGSPortRateLimitEntry.setIndexNames(
    (0, "EXPRESSGS-MIB", "expressGSPortIndex"),
)
if mibBuilder.loadTexts:
    expressGSPortRateLimitEntry.setStatus("mandatory")


class _ExpressGSPortRateLimitMode_Type(Integer32):
    """Custom type expressGSPortRateLimitMode based on Integer32"""
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


_ExpressGSPortRateLimitMode_Type.__name__ = "Integer32"
_ExpressGSPortRateLimitMode_Object = MibTableColumn
expressGSPortRateLimitMode = _ExpressGSPortRateLimitMode_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 13, 3, 6, 6, 1, 1, 61),
    _ExpressGSPortRateLimitMode_Type()
)
expressGSPortRateLimitMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    expressGSPortRateLimitMode.setStatus("mandatory")


class _ExpressGSPortRateLimitRate_Type(Integer32):
    """Custom type expressGSPortRateLimitRate based on Integer32"""
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


_ExpressGSPortRateLimitRate_Type.__name__ = "Integer32"
_ExpressGSPortRateLimitRate_Object = MibTableColumn
expressGSPortRateLimitRate = _ExpressGSPortRateLimitRate_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 13, 3, 6, 6, 1, 1, 62),
    _ExpressGSPortRateLimitRate_Type()
)
expressGSPortRateLimitRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    expressGSPortRateLimitRate.setStatus("mandatory")


class _ExpressGSPortRateLimitBurstSize_Type(Integer32):
    """Custom type expressGSPortRateLimitBurstSize based on Integer32"""
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


_ExpressGSPortRateLimitBurstSize_Type.__name__ = "Integer32"
_ExpressGSPortRateLimitBurstSize_Object = MibTableColumn
expressGSPortRateLimitBurstSize = _ExpressGSPortRateLimitBurstSize_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 13, 3, 6, 6, 1, 1, 63),
    _ExpressGSPortRateLimitBurstSize_Type()
)
expressGSPortRateLimitBurstSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    expressGSPortRateLimitBurstSize.setStatus("mandatory")
_ExpressGSPortPacePriorityMgt_ObjectIdentity = ObjectIdentity
expressGSPortPacePriorityMgt = _ExpressGSPortPacePriorityMgt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 343, 6, 13, 3, 6, 7)
)
_ExpressGSPortPacePriorityTable_Object = MibTable
expressGSPortPacePriorityTable = _ExpressGSPortPacePriorityTable_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 13, 3, 6, 7, 1)
)
if mibBuilder.loadTexts:
    expressGSPortPacePriorityTable.setStatus("mandatory")
_ExpressGSPortPacePriorityEntry_Object = MibTableRow
expressGSPortPacePriorityEntry = _ExpressGSPortPacePriorityEntry_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 13, 3, 6, 7, 1, 1)
)
expressGSPortPacePriorityEntry.setIndexNames(
    (0, "EXPRESSGS-MIB", "expressGSPortIndex"),
)
if mibBuilder.loadTexts:
    expressGSPortPacePriorityEntry.setStatus("mandatory")


class _ExpressGSPortPacePriorityMode_Type(Integer32):
    """Custom type expressGSPortPacePriorityMode based on Integer32"""
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


_ExpressGSPortPacePriorityMode_Type.__name__ = "Integer32"
_ExpressGSPortPacePriorityMode_Object = MibTableColumn
expressGSPortPacePriorityMode = _ExpressGSPortPacePriorityMode_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 13, 3, 6, 7, 1, 1, 71),
    _ExpressGSPortPacePriorityMode_Type()
)
expressGSPortPacePriorityMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    expressGSPortPacePriorityMode.setStatus("mandatory")
_ExpressGSPortCategoryMgt_ObjectIdentity = ObjectIdentity
expressGSPortCategoryMgt = _ExpressGSPortCategoryMgt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 343, 6, 13, 3, 6, 8)
)
_ExpressGSPortCategoryTable_Object = MibTable
expressGSPortCategoryTable = _ExpressGSPortCategoryTable_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 13, 3, 6, 8, 1)
)
if mibBuilder.loadTexts:
    expressGSPortCategoryTable.setStatus("mandatory")
_ExpressGSPortCategoryEntry_Object = MibTableRow
expressGSPortCategoryEntry = _ExpressGSPortCategoryEntry_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 13, 3, 6, 8, 1, 1)
)
expressGSPortCategoryEntry.setIndexNames(
    (0, "EXPRESSGS-MIB", "expressGSPortIndex"),
)
if mibBuilder.loadTexts:
    expressGSPortCategoryEntry.setStatus("mandatory")


class _ExpressGSPortCategoryMode_Type(Integer32):
    """Custom type expressGSPortCategoryMode based on Integer32"""
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


_ExpressGSPortCategoryMode_Type.__name__ = "Integer32"
_ExpressGSPortCategoryMode_Object = MibTableColumn
expressGSPortCategoryMode = _ExpressGSPortCategoryMode_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 13, 3, 6, 8, 1, 1, 81),
    _ExpressGSPortCategoryMode_Type()
)
expressGSPortCategoryMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    expressGSPortCategoryMode.setStatus("mandatory")
_ExpressGSBufferMgt_ObjectIdentity = ObjectIdentity
expressGSBufferMgt = _ExpressGSBufferMgt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 343, 6, 13, 3, 7)
)
_ExpressGSBufferTable_Object = MibTable
expressGSBufferTable = _ExpressGSBufferTable_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 13, 3, 7, 1)
)
if mibBuilder.loadTexts:
    expressGSBufferTable.setStatus("mandatory")
_ExpressGSBufferEntry_Object = MibTableRow
expressGSBufferEntry = _ExpressGSBufferEntry_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 13, 3, 7, 1, 1)
)
expressGSBufferEntry.setIndexNames(
    (0, "EXPRESSGS-MIB", "expressGSBufferIndex"),
)
if mibBuilder.loadTexts:
    expressGSBufferEntry.setStatus("mandatory")
_ExpressGSBufferIndex_Type = ResourceId
_ExpressGSBufferIndex_Object = MibTableColumn
expressGSBufferIndex = _ExpressGSBufferIndex_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 13, 3, 7, 1, 1, 1),
    _ExpressGSBufferIndex_Type()
)
expressGSBufferIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    expressGSBufferIndex.setStatus("mandatory")
_ExpressGSBufferFabricPort_Type = ResourceId
_ExpressGSBufferFabricPort_Object = MibTableColumn
expressGSBufferFabricPort = _ExpressGSBufferFabricPort_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 13, 3, 7, 1, 1, 2),
    _ExpressGSBufferFabricPort_Type()
)
expressGSBufferFabricPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    expressGSBufferFabricPort.setStatus("mandatory")


class _ExpressGSBufferFabricPortDirection_Type(Integer32):
    """Custom type expressGSBufferFabricPortDirection based on Integer32"""
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


_ExpressGSBufferFabricPortDirection_Type.__name__ = "Integer32"
_ExpressGSBufferFabricPortDirection_Object = MibTableColumn
expressGSBufferFabricPortDirection = _ExpressGSBufferFabricPortDirection_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 13, 3, 7, 1, 1, 3),
    _ExpressGSBufferFabricPortDirection_Type()
)
expressGSBufferFabricPortDirection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    expressGSBufferFabricPortDirection.setStatus("mandatory")
_ExpressGSBufferSwitchPort_Type = ResourceId
_ExpressGSBufferSwitchPort_Object = MibTableColumn
expressGSBufferSwitchPort = _ExpressGSBufferSwitchPort_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 13, 3, 7, 1, 1, 4),
    _ExpressGSBufferSwitchPort_Type()
)
expressGSBufferSwitchPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    expressGSBufferSwitchPort.setStatus("mandatory")
_ExpressGSBufferMemory_Type = Integer32
_ExpressGSBufferMemory_Object = MibTableColumn
expressGSBufferMemory = _ExpressGSBufferMemory_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 13, 3, 7, 1, 1, 5),
    _ExpressGSBufferMemory_Type()
)
expressGSBufferMemory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    expressGSBufferMemory.setStatus("mandatory")


class _ExpressGSBufferAgeTimer_Type(Integer32):
    """Custom type expressGSBufferAgeTimer based on Integer32"""
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


_ExpressGSBufferAgeTimer_Type.__name__ = "Integer32"
_ExpressGSBufferAgeTimer_Object = MibTableColumn
expressGSBufferAgeTimer = _ExpressGSBufferAgeTimer_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 13, 3, 7, 1, 1, 6),
    _ExpressGSBufferAgeTimer_Type()
)
expressGSBufferAgeTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    expressGSBufferAgeTimer.setStatus("mandatory")


class _ExpressGSBufferPriorityServicing_Type(Integer32):
    """Custom type expressGSBufferPriorityServicing based on Integer32"""
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


_ExpressGSBufferPriorityServicing_Type.__name__ = "Integer32"
_ExpressGSBufferPriorityServicing_Object = MibTableColumn
expressGSBufferPriorityServicing = _ExpressGSBufferPriorityServicing_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 13, 3, 7, 1, 1, 7),
    _ExpressGSBufferPriorityServicing_Type()
)
expressGSBufferPriorityServicing.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    expressGSBufferPriorityServicing.setStatus("mandatory")


class _ExpressGSBufferPriorityAllocation_Type(Integer32):
    """Custom type expressGSBufferPriorityAllocation based on Integer32"""
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


_ExpressGSBufferPriorityAllocation_Type.__name__ = "Integer32"
_ExpressGSBufferPriorityAllocation_Object = MibTableColumn
expressGSBufferPriorityAllocation = _ExpressGSBufferPriorityAllocation_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 13, 3, 7, 1, 1, 8),
    _ExpressGSBufferPriorityAllocation_Type()
)
expressGSBufferPriorityAllocation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    expressGSBufferPriorityAllocation.setStatus("mandatory")


class _ExpressGSBufferPriorityThreshold_Type(Integer32):
    """Custom type expressGSBufferPriorityThreshold based on Integer32"""
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


_ExpressGSBufferPriorityThreshold_Type.__name__ = "Integer32"
_ExpressGSBufferPriorityThreshold_Object = MibTableColumn
expressGSBufferPriorityThreshold = _ExpressGSBufferPriorityThreshold_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 13, 3, 7, 1, 1, 9),
    _ExpressGSBufferPriorityThreshold_Type()
)
expressGSBufferPriorityThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    expressGSBufferPriorityThreshold.setStatus("mandatory")


class _ExpressGSBufferCongestion_Type(Integer32):
    """Custom type expressGSBufferCongestion based on Integer32"""
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


_ExpressGSBufferCongestion_Type.__name__ = "Integer32"
_ExpressGSBufferCongestion_Object = MibTableColumn
expressGSBufferCongestion = _ExpressGSBufferCongestion_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 13, 3, 7, 1, 1, 10),
    _ExpressGSBufferCongestion_Type()
)
expressGSBufferCongestion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    expressGSBufferCongestion.setStatus("mandatory")
_ExpressGSBufferHighOverflowDrops_Type = Counter32
_ExpressGSBufferHighOverflowDrops_Object = MibTableColumn
expressGSBufferHighOverflowDrops = _ExpressGSBufferHighOverflowDrops_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 13, 3, 7, 1, 1, 11),
    _ExpressGSBufferHighOverflowDrops_Type()
)
expressGSBufferHighOverflowDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    expressGSBufferHighOverflowDrops.setStatus("mandatory")
_ExpressGSBufferLowOverflowDrops_Type = Counter32
_ExpressGSBufferLowOverflowDrops_Object = MibTableColumn
expressGSBufferLowOverflowDrops = _ExpressGSBufferLowOverflowDrops_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 13, 3, 7, 1, 1, 12),
    _ExpressGSBufferLowOverflowDrops_Type()
)
expressGSBufferLowOverflowDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    expressGSBufferLowOverflowDrops.setStatus("mandatory")
_ExpressGSBufferHighStaleDrops_Type = Counter32
_ExpressGSBufferHighStaleDrops_Object = MibTableColumn
expressGSBufferHighStaleDrops = _ExpressGSBufferHighStaleDrops_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 13, 3, 7, 1, 1, 13),
    _ExpressGSBufferHighStaleDrops_Type()
)
expressGSBufferHighStaleDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    expressGSBufferHighStaleDrops.setStatus("mandatory")
_ExpressGSBufferLowStaleDrops_Type = Counter32
_ExpressGSBufferLowStaleDrops_Object = MibTableColumn
expressGSBufferLowStaleDrops = _ExpressGSBufferLowStaleDrops_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 13, 3, 7, 1, 1, 14),
    _ExpressGSBufferLowStaleDrops_Type()
)
expressGSBufferLowStaleDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    expressGSBufferLowStaleDrops.setStatus("mandatory")
_ExpressGSBufferCongestionDrops_Type = Counter32
_ExpressGSBufferCongestionDrops_Object = MibTableColumn
expressGSBufferCongestionDrops = _ExpressGSBufferCongestionDrops_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 13, 3, 7, 1, 1, 16),
    _ExpressGSBufferCongestionDrops_Type()
)
expressGSBufferCongestionDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    expressGSBufferCongestionDrops.setStatus("mandatory")
_ExpressGSSwitching_ObjectIdentity = ObjectIdentity
expressGSSwitching = _ExpressGSSwitching_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 343, 6, 13, 5)
)
_ExpressGSSwitchingLayerII_ObjectIdentity = ObjectIdentity
expressGSSwitchingLayerII = _ExpressGSSwitchingLayerII_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 343, 6, 13, 5, 1)
)
_ExpressGSSwitchGen_ObjectIdentity = ObjectIdentity
expressGSSwitchGen = _ExpressGSSwitchGen_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 343, 6, 13, 5, 1, 1)
)


class _ExpressGSSwitchSTPConfig_Type(Integer32):
    """Custom type expressGSSwitchSTPConfig based on Integer32"""
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


_ExpressGSSwitchSTPConfig_Type.__name__ = "Integer32"
_ExpressGSSwitchSTPConfig_Object = MibScalar
expressGSSwitchSTPConfig = _ExpressGSSwitchSTPConfig_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 13, 5, 1, 1, 1),
    _ExpressGSSwitchSTPConfig_Type()
)
expressGSSwitchSTPConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    expressGSSwitchSTPConfig.setStatus("mandatory")


class _ExpressGSSwitchAgingTime_Type(Integer32):
    """Custom type expressGSSwitchAgingTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 1000000),
    )


_ExpressGSSwitchAgingTime_Type.__name__ = "Integer32"
_ExpressGSSwitchAgingTime_Object = MibScalar
expressGSSwitchAgingTime = _ExpressGSSwitchAgingTime_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 13, 5, 1, 1, 2),
    _ExpressGSSwitchAgingTime_Type()
)
expressGSSwitchAgingTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    expressGSSwitchAgingTime.setStatus("mandatory")


class _ExpressGSSwitchSuperAgingTime_Type(Integer32):
    """Custom type expressGSSwitchSuperAgingTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 30),
    )


_ExpressGSSwitchSuperAgingTime_Type.__name__ = "Integer32"
_ExpressGSSwitchSuperAgingTime_Object = MibScalar
expressGSSwitchSuperAgingTime = _ExpressGSSwitchSuperAgingTime_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 13, 5, 1, 1, 3),
    _ExpressGSSwitchSuperAgingTime_Type()
)
expressGSSwitchSuperAgingTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    expressGSSwitchSuperAgingTime.setStatus("mandatory")
_ExpressGSBridgeMgmt_ObjectIdentity = ObjectIdentity
expressGSBridgeMgmt = _ExpressGSBridgeMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 343, 6, 13, 5, 1, 2)
)
_ExpressGSBridgeTable_Object = MibTable
expressGSBridgeTable = _ExpressGSBridgeTable_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 13, 5, 1, 2, 1)
)
if mibBuilder.loadTexts:
    expressGSBridgeTable.setStatus("mandatory")
_ExpressGSBridgeEntry_Object = MibTableRow
expressGSBridgeEntry = _ExpressGSBridgeEntry_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 13, 5, 1, 2, 1, 1)
)
expressGSBridgeEntry.setIndexNames(
    (0, "EXPRESSGS-MIB", "expressGSBridgeIndex"),
)
if mibBuilder.loadTexts:
    expressGSBridgeEntry.setStatus("mandatory")
_ExpressGSBridgeIndex_Type = ResourceId
_ExpressGSBridgeIndex_Object = MibTableColumn
expressGSBridgeIndex = _ExpressGSBridgeIndex_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 13, 5, 1, 2, 1, 1, 1),
    _ExpressGSBridgeIndex_Type()
)
expressGSBridgeIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    expressGSBridgeIndex.setStatus("mandatory")


class _ExpressGSBridgeType_Type(Integer32):
    """Custom type expressGSBridgeType based on Integer32"""
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


_ExpressGSBridgeType_Type.__name__ = "Integer32"
_ExpressGSBridgeType_Object = MibTableColumn
expressGSBridgeType = _ExpressGSBridgeType_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 13, 5, 1, 2, 1, 1, 2),
    _ExpressGSBridgeType_Type()
)
expressGSBridgeType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    expressGSBridgeType.setStatus("mandatory")


class _ExpressGSBridgeMode_Type(Integer32):
    """Custom type expressGSBridgeMode based on Integer32"""
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


_ExpressGSBridgeMode_Type.__name__ = "Integer32"
_ExpressGSBridgeMode_Object = MibTableColumn
expressGSBridgeMode = _ExpressGSBridgeMode_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 13, 5, 1, 2, 1, 1, 3),
    _ExpressGSBridgeMode_Type()
)
expressGSBridgeMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    expressGSBridgeMode.setStatus("mandatory")


class _ExpressGSBridgeStatus_Type(Integer32):
    """Custom type expressGSBridgeStatus based on Integer32"""
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


_ExpressGSBridgeStatus_Type.__name__ = "Integer32"
_ExpressGSBridgeStatus_Object = MibTableColumn
expressGSBridgeStatus = _ExpressGSBridgeStatus_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 13, 5, 1, 2, 1, 1, 4),
    _ExpressGSBridgeStatus_Type()
)
expressGSBridgeStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    expressGSBridgeStatus.setStatus("mandatory")


class _ExpressGSBridgeStpPriority_Type(Integer32):
    """Custom type expressGSBridgeStpPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_ExpressGSBridgeStpPriority_Type.__name__ = "Integer32"
_ExpressGSBridgeStpPriority_Object = MibTableColumn
expressGSBridgeStpPriority = _ExpressGSBridgeStpPriority_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 13, 5, 1, 2, 1, 1, 5),
    _ExpressGSBridgeStpPriority_Type()
)
expressGSBridgeStpPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    expressGSBridgeStpPriority.setStatus("mandatory")
_ExpressGSBridgeStpTimeSinceTopologyChange_Type = TimeTicks
_ExpressGSBridgeStpTimeSinceTopologyChange_Object = MibTableColumn
expressGSBridgeStpTimeSinceTopologyChange = _ExpressGSBridgeStpTimeSinceTopologyChange_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 13, 5, 1, 2, 1, 1, 6),
    _ExpressGSBridgeStpTimeSinceTopologyChange_Type()
)
expressGSBridgeStpTimeSinceTopologyChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    expressGSBridgeStpTimeSinceTopologyChange.setStatus("mandatory")
_ExpressGSBridgeStpTopChanges_Type = Counter32
_ExpressGSBridgeStpTopChanges_Object = MibTableColumn
expressGSBridgeStpTopChanges = _ExpressGSBridgeStpTopChanges_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 13, 5, 1, 2, 1, 1, 7),
    _ExpressGSBridgeStpTopChanges_Type()
)
expressGSBridgeStpTopChanges.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    expressGSBridgeStpTopChanges.setStatus("mandatory")
_ExpressGSBridgeStpDesignatedRoot_Type = BridgeId
_ExpressGSBridgeStpDesignatedRoot_Object = MibTableColumn
expressGSBridgeStpDesignatedRoot = _ExpressGSBridgeStpDesignatedRoot_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 13, 5, 1, 2, 1, 1, 8),
    _ExpressGSBridgeStpDesignatedRoot_Type()
)
expressGSBridgeStpDesignatedRoot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    expressGSBridgeStpDesignatedRoot.setStatus("mandatory")
_ExpressGSBridgeStpRootCost_Type = Integer32
_ExpressGSBridgeStpRootCost_Object = MibTableColumn
expressGSBridgeStpRootCost = _ExpressGSBridgeStpRootCost_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 13, 5, 1, 2, 1, 1, 9),
    _ExpressGSBridgeStpRootCost_Type()
)
expressGSBridgeStpRootCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    expressGSBridgeStpRootCost.setStatus("mandatory")
_ExpressGSBridgeStpRootPort_Type = Integer32
_ExpressGSBridgeStpRootPort_Object = MibTableColumn
expressGSBridgeStpRootPort = _ExpressGSBridgeStpRootPort_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 13, 5, 1, 2, 1, 1, 10),
    _ExpressGSBridgeStpRootPort_Type()
)
expressGSBridgeStpRootPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    expressGSBridgeStpRootPort.setStatus("mandatory")
_ExpressGSBridgeStpMaxAge_Type = Timeout
_ExpressGSBridgeStpMaxAge_Object = MibTableColumn
expressGSBridgeStpMaxAge = _ExpressGSBridgeStpMaxAge_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 13, 5, 1, 2, 1, 1, 11),
    _ExpressGSBridgeStpMaxAge_Type()
)
expressGSBridgeStpMaxAge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    expressGSBridgeStpMaxAge.setStatus("mandatory")
_ExpressGSBridgeStpHelloTime_Type = Timeout
_ExpressGSBridgeStpHelloTime_Object = MibTableColumn
expressGSBridgeStpHelloTime = _ExpressGSBridgeStpHelloTime_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 13, 5, 1, 2, 1, 1, 12),
    _ExpressGSBridgeStpHelloTime_Type()
)
expressGSBridgeStpHelloTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    expressGSBridgeStpHelloTime.setStatus("mandatory")
_ExpressGSBridgeStpHoldTime_Type = Integer32
_ExpressGSBridgeStpHoldTime_Object = MibTableColumn
expressGSBridgeStpHoldTime = _ExpressGSBridgeStpHoldTime_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 13, 5, 1, 2, 1, 1, 13),
    _ExpressGSBridgeStpHoldTime_Type()
)
expressGSBridgeStpHoldTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    expressGSBridgeStpHoldTime.setStatus("mandatory")
_ExpressGSBridgeStpForwardDelay_Type = Timeout
_ExpressGSBridgeStpForwardDelay_Object = MibTableColumn
expressGSBridgeStpForwardDelay = _ExpressGSBridgeStpForwardDelay_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 13, 5, 1, 2, 1, 1, 14),
    _ExpressGSBridgeStpForwardDelay_Type()
)
expressGSBridgeStpForwardDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    expressGSBridgeStpForwardDelay.setStatus("mandatory")


class _ExpressGSBridgeStpBridgeMaxAge_Type(Timeout):
    """Custom type expressGSBridgeStpBridgeMaxAge based on Timeout"""
    subtypeSpec = Timeout.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(600, 4000),
    )


_ExpressGSBridgeStpBridgeMaxAge_Type.__name__ = "Timeout"
_ExpressGSBridgeStpBridgeMaxAge_Object = MibTableColumn
expressGSBridgeStpBridgeMaxAge = _ExpressGSBridgeStpBridgeMaxAge_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 13, 5, 1, 2, 1, 1, 15),
    _ExpressGSBridgeStpBridgeMaxAge_Type()
)
expressGSBridgeStpBridgeMaxAge.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    expressGSBridgeStpBridgeMaxAge.setStatus("mandatory")


class _ExpressGSBridgeStpBridgeHelloTime_Type(Timeout):
    """Custom type expressGSBridgeStpBridgeHelloTime based on Timeout"""
    subtypeSpec = Timeout.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(100, 1000),
    )


_ExpressGSBridgeStpBridgeHelloTime_Type.__name__ = "Timeout"
_ExpressGSBridgeStpBridgeHelloTime_Object = MibTableColumn
expressGSBridgeStpBridgeHelloTime = _ExpressGSBridgeStpBridgeHelloTime_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 13, 5, 1, 2, 1, 1, 16),
    _ExpressGSBridgeStpBridgeHelloTime_Type()
)
expressGSBridgeStpBridgeHelloTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    expressGSBridgeStpBridgeHelloTime.setStatus("mandatory")


class _ExpressGSBridgeStpBridgeForwardDelay_Type(Timeout):
    """Custom type expressGSBridgeStpBridgeForwardDelay based on Timeout"""
    subtypeSpec = Timeout.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(400, 3000),
    )


_ExpressGSBridgeStpBridgeForwardDelay_Type.__name__ = "Timeout"
_ExpressGSBridgeStpBridgeForwardDelay_Object = MibTableColumn
expressGSBridgeStpBridgeForwardDelay = _ExpressGSBridgeStpBridgeForwardDelay_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 13, 5, 1, 2, 1, 1, 17),
    _ExpressGSBridgeStpBridgeForwardDelay_Type()
)
expressGSBridgeStpBridgeForwardDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    expressGSBridgeStpBridgeForwardDelay.setStatus("mandatory")
_ExpressGSBridgePortMgmt_ObjectIdentity = ObjectIdentity
expressGSBridgePortMgmt = _ExpressGSBridgePortMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 343, 6, 13, 5, 1, 3)
)
_ExpressGSBridgePortTable_Object = MibTable
expressGSBridgePortTable = _ExpressGSBridgePortTable_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 13, 5, 1, 3, 1)
)
if mibBuilder.loadTexts:
    expressGSBridgePortTable.setStatus("mandatory")
_ExpressGSBridgePortEntry_Object = MibTableRow
expressGSBridgePortEntry = _ExpressGSBridgePortEntry_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 13, 5, 1, 3, 1, 1)
)
expressGSBridgePortEntry.setIndexNames(
    (0, "EXPRESSGS-MIB", "expressGSBridgePortIndex"),
)
if mibBuilder.loadTexts:
    expressGSBridgePortEntry.setStatus("mandatory")
_ExpressGSBridgePortIndex_Type = ResourceId
_ExpressGSBridgePortIndex_Object = MibTableColumn
expressGSBridgePortIndex = _ExpressGSBridgePortIndex_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 13, 5, 1, 3, 1, 1, 1),
    _ExpressGSBridgePortIndex_Type()
)
expressGSBridgePortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    expressGSBridgePortIndex.setStatus("mandatory")


class _ExpressGSBridgePortPriority_Type(Integer32):
    """Custom type expressGSBridgePortPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_ExpressGSBridgePortPriority_Type.__name__ = "Integer32"
_ExpressGSBridgePortPriority_Object = MibTableColumn
expressGSBridgePortPriority = _ExpressGSBridgePortPriority_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 13, 5, 1, 3, 1, 1, 2),
    _ExpressGSBridgePortPriority_Type()
)
expressGSBridgePortPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    expressGSBridgePortPriority.setStatus("mandatory")


class _ExpressGSBridgePortState_Type(Integer32):
    """Custom type expressGSBridgePortState based on Integer32"""
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


_ExpressGSBridgePortState_Type.__name__ = "Integer32"
_ExpressGSBridgePortState_Object = MibTableColumn
expressGSBridgePortState = _ExpressGSBridgePortState_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 13, 5, 1, 3, 1, 1, 3),
    _ExpressGSBridgePortState_Type()
)
expressGSBridgePortState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    expressGSBridgePortState.setStatus("mandatory")


class _ExpressGSBridgePortEnable_Type(Integer32):
    """Custom type expressGSBridgePortEnable based on Integer32"""
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


_ExpressGSBridgePortEnable_Type.__name__ = "Integer32"
_ExpressGSBridgePortEnable_Object = MibTableColumn
expressGSBridgePortEnable = _ExpressGSBridgePortEnable_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 13, 5, 1, 3, 1, 1, 4),
    _ExpressGSBridgePortEnable_Type()
)
expressGSBridgePortEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    expressGSBridgePortEnable.setStatus("mandatory")


class _ExpressGSBridgePortPathCost_Type(Integer32):
    """Custom type expressGSBridgePortPathCost based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_ExpressGSBridgePortPathCost_Type.__name__ = "Integer32"
_ExpressGSBridgePortPathCost_Object = MibTableColumn
expressGSBridgePortPathCost = _ExpressGSBridgePortPathCost_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 13, 5, 1, 3, 1, 1, 5),
    _ExpressGSBridgePortPathCost_Type()
)
expressGSBridgePortPathCost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    expressGSBridgePortPathCost.setStatus("mandatory")
_ExpressGSBridgePortDesignatedRoot_Type = BridgeId
_ExpressGSBridgePortDesignatedRoot_Object = MibTableColumn
expressGSBridgePortDesignatedRoot = _ExpressGSBridgePortDesignatedRoot_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 13, 5, 1, 3, 1, 1, 6),
    _ExpressGSBridgePortDesignatedRoot_Type()
)
expressGSBridgePortDesignatedRoot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    expressGSBridgePortDesignatedRoot.setStatus("mandatory")
_ExpressGSBridgePortDesignatedCost_Type = Integer32
_ExpressGSBridgePortDesignatedCost_Object = MibTableColumn
expressGSBridgePortDesignatedCost = _ExpressGSBridgePortDesignatedCost_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 13, 5, 1, 3, 1, 1, 7),
    _ExpressGSBridgePortDesignatedCost_Type()
)
expressGSBridgePortDesignatedCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    expressGSBridgePortDesignatedCost.setStatus("mandatory")
_ExpressGSBridgePortDesignatedBridge_Type = BridgeId
_ExpressGSBridgePortDesignatedBridge_Object = MibTableColumn
expressGSBridgePortDesignatedBridge = _ExpressGSBridgePortDesignatedBridge_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 13, 5, 1, 3, 1, 1, 8),
    _ExpressGSBridgePortDesignatedBridge_Type()
)
expressGSBridgePortDesignatedBridge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    expressGSBridgePortDesignatedBridge.setStatus("mandatory")


class _ExpressGSBridgePortDesignatedPort_Type(OctetString):
    """Custom type expressGSBridgePortDesignatedPort based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_ExpressGSBridgePortDesignatedPort_Type.__name__ = "OctetString"
_ExpressGSBridgePortDesignatedPort_Object = MibTableColumn
expressGSBridgePortDesignatedPort = _ExpressGSBridgePortDesignatedPort_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 13, 5, 1, 3, 1, 1, 9),
    _ExpressGSBridgePortDesignatedPort_Type()
)
expressGSBridgePortDesignatedPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    expressGSBridgePortDesignatedPort.setStatus("mandatory")
_ExpressGSBridgePortForwardTransitions_Type = Counter32
_ExpressGSBridgePortForwardTransitions_Object = MibTableColumn
expressGSBridgePortForwardTransitions = _ExpressGSBridgePortForwardTransitions_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 13, 5, 1, 3, 1, 1, 10),
    _ExpressGSBridgePortForwardTransitions_Type()
)
expressGSBridgePortForwardTransitions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    expressGSBridgePortForwardTransitions.setStatus("mandatory")


class _ExpressGSBridgePortFastStart_Type(Integer32):
    """Custom type expressGSBridgePortFastStart based on Integer32"""
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


_ExpressGSBridgePortFastStart_Type.__name__ = "Integer32"
_ExpressGSBridgePortFastStart_Object = MibTableColumn
expressGSBridgePortFastStart = _ExpressGSBridgePortFastStart_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 13, 5, 1, 3, 1, 1, 11),
    _ExpressGSBridgePortFastStart_Type()
)
expressGSBridgePortFastStart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    expressGSBridgePortFastStart.setStatus("deprecated")


class _ExpressGSBridgePortSetDefault_Type(Integer32):
    """Custom type expressGSBridgePortSetDefault based on Integer32"""
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


_ExpressGSBridgePortSetDefault_Type.__name__ = "Integer32"
_ExpressGSBridgePortSetDefault_Object = MibTableColumn
expressGSBridgePortSetDefault = _ExpressGSBridgePortSetDefault_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 13, 5, 1, 3, 1, 1, 12),
    _ExpressGSBridgePortSetDefault_Type()
)
expressGSBridgePortSetDefault.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    expressGSBridgePortSetDefault.setStatus("mandatory")


class _ExpressGSBridgePortEnableChangeDetection_Type(Integer32):
    """Custom type expressGSBridgePortEnableChangeDetection based on Integer32"""
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


_ExpressGSBridgePortEnableChangeDetection_Type.__name__ = "Integer32"
_ExpressGSBridgePortEnableChangeDetection_Object = MibTableColumn
expressGSBridgePortEnableChangeDetection = _ExpressGSBridgePortEnableChangeDetection_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 13, 5, 1, 3, 1, 1, 13),
    _ExpressGSBridgePortEnableChangeDetection_Type()
)
expressGSBridgePortEnableChangeDetection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    expressGSBridgePortEnableChangeDetection.setStatus("mandatory")
_ExpressGSL2AddrMgmt_ObjectIdentity = ObjectIdentity
expressGSL2AddrMgmt = _ExpressGSL2AddrMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 343, 6, 13, 5, 1, 4)
)
_ExpressGSL2AddrDatabaseMgt_ObjectIdentity = ObjectIdentity
expressGSL2AddrDatabaseMgt = _ExpressGSL2AddrDatabaseMgt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 343, 6, 13, 5, 1, 4, 1)
)
_ExpressGSL2AddressTable_Object = MibTable
expressGSL2AddressTable = _ExpressGSL2AddressTable_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 13, 5, 1, 4, 1, 1)
)
if mibBuilder.loadTexts:
    expressGSL2AddressTable.setStatus("mandatory")
_ExpressGSL2AddressEntry_Object = MibTableRow
expressGSL2AddressEntry = _ExpressGSL2AddressEntry_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 13, 5, 1, 4, 1, 1, 1)
)
expressGSL2AddressEntry.setIndexNames(
    (0, "EXPRESSGS-MIB", "expressGSL2AddressIndex"),
)
if mibBuilder.loadTexts:
    expressGSL2AddressEntry.setStatus("mandatory")
_ExpressGSL2AddressIndex_Type = Integer32
_ExpressGSL2AddressIndex_Object = MibTableColumn
expressGSL2AddressIndex = _ExpressGSL2AddressIndex_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 13, 5, 1, 4, 1, 1, 1, 1),
    _ExpressGSL2AddressIndex_Type()
)
expressGSL2AddressIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    expressGSL2AddressIndex.setStatus("mandatory")
_ExpressGSL2AddressTableIndex_Type = Integer32
_ExpressGSL2AddressTableIndex_Object = MibTableColumn
expressGSL2AddressTableIndex = _ExpressGSL2AddressTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 13, 5, 1, 4, 1, 1, 1, 2),
    _ExpressGSL2AddressTableIndex_Type()
)
expressGSL2AddressTableIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    expressGSL2AddressTableIndex.setStatus("mandatory")
_ExpressGSL2AddressMacAddress_Type = MacAddress
_ExpressGSL2AddressMacAddress_Object = MibTableColumn
expressGSL2AddressMacAddress = _ExpressGSL2AddressMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 13, 5, 1, 4, 1, 1, 1, 3),
    _ExpressGSL2AddressMacAddress_Type()
)
expressGSL2AddressMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    expressGSL2AddressMacAddress.setStatus("mandatory")
_ExpressGSL2AddressPortBinding_Type = ResourceId
_ExpressGSL2AddressPortBinding_Object = MibTableColumn
expressGSL2AddressPortBinding = _ExpressGSL2AddressPortBinding_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 13, 5, 1, 4, 1, 1, 1, 4),
    _ExpressGSL2AddressPortBinding_Type()
)
expressGSL2AddressPortBinding.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    expressGSL2AddressPortBinding.setStatus("mandatory")


class _ExpressGSL2AddressBindingValid_Type(Integer32):
    """Custom type expressGSL2AddressBindingValid based on Integer32"""
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


_ExpressGSL2AddressBindingValid_Type.__name__ = "Integer32"
_ExpressGSL2AddressBindingValid_Object = MibTableColumn
expressGSL2AddressBindingValid = _ExpressGSL2AddressBindingValid_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 13, 5, 1, 4, 1, 1, 1, 5),
    _ExpressGSL2AddressBindingValid_Type()
)
expressGSL2AddressBindingValid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    expressGSL2AddressBindingValid.setStatus("mandatory")
_ExpressGSL2AddressVlanID_Type = Integer32
_ExpressGSL2AddressVlanID_Object = MibTableColumn
expressGSL2AddressVlanID = _ExpressGSL2AddressVlanID_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 13, 5, 1, 4, 1, 1, 1, 6),
    _ExpressGSL2AddressVlanID_Type()
)
expressGSL2AddressVlanID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    expressGSL2AddressVlanID.setStatus("mandatory")


class _ExpressGSL2AddressPriority_Type(Integer32):
    """Custom type expressGSL2AddressPriority based on Integer32"""
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


_ExpressGSL2AddressPriority_Type.__name__ = "Integer32"
_ExpressGSL2AddressPriority_Object = MibTableColumn
expressGSL2AddressPriority = _ExpressGSL2AddressPriority_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 13, 5, 1, 4, 1, 1, 1, 7),
    _ExpressGSL2AddressPriority_Type()
)
expressGSL2AddressPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    expressGSL2AddressPriority.setStatus("mandatory")


class _ExpressGSL2AddressForward_Type(Integer32):
    """Custom type expressGSL2AddressForward based on Integer32"""
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


_ExpressGSL2AddressForward_Type.__name__ = "Integer32"
_ExpressGSL2AddressForward_Object = MibTableColumn
expressGSL2AddressForward = _ExpressGSL2AddressForward_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 13, 5, 1, 4, 1, 1, 1, 8),
    _ExpressGSL2AddressForward_Type()
)
expressGSL2AddressForward.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    expressGSL2AddressForward.setStatus("mandatory")


class _ExpressGSL2AddressCopy_Type(Integer32):
    """Custom type expressGSL2AddressCopy based on Integer32"""
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


_ExpressGSL2AddressCopy_Type.__name__ = "Integer32"
_ExpressGSL2AddressCopy_Object = MibTableColumn
expressGSL2AddressCopy = _ExpressGSL2AddressCopy_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 13, 5, 1, 4, 1, 1, 1, 9),
    _ExpressGSL2AddressCopy_Type()
)
expressGSL2AddressCopy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    expressGSL2AddressCopy.setStatus("mandatory")


class _ExpressGSL2AddressPersistence_Type(Integer32):
    """Custom type expressGSL2AddressPersistence based on Integer32"""
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


_ExpressGSL2AddressPersistence_Type.__name__ = "Integer32"
_ExpressGSL2AddressPersistence_Object = MibTableColumn
expressGSL2AddressPersistence = _ExpressGSL2AddressPersistence_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 13, 5, 1, 4, 1, 1, 1, 10),
    _ExpressGSL2AddressPersistence_Type()
)
expressGSL2AddressPersistence.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    expressGSL2AddressPersistence.setStatus("mandatory")


class _ExpressGSL2AddressStatus_Type(Integer32):
    """Custom type expressGSL2AddressStatus based on Integer32"""
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


_ExpressGSL2AddressStatus_Type.__name__ = "Integer32"
_ExpressGSL2AddressStatus_Object = MibTableColumn
expressGSL2AddressStatus = _ExpressGSL2AddressStatus_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 13, 5, 1, 4, 1, 1, 1, 11),
    _ExpressGSL2AddressStatus_Type()
)
expressGSL2AddressStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    expressGSL2AddressStatus.setStatus("mandatory")
_ExpressGSL2AddrSummaryMgt_ObjectIdentity = ObjectIdentity
expressGSL2AddrSummaryMgt = _ExpressGSL2AddrSummaryMgt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 343, 6, 13, 5, 1, 4, 2)
)
_ExpressGSL2AddrSummaryTable_Object = MibTable
expressGSL2AddrSummaryTable = _ExpressGSL2AddrSummaryTable_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 13, 5, 1, 4, 2, 1)
)
if mibBuilder.loadTexts:
    expressGSL2AddrSummaryTable.setStatus("mandatory")
_ExpressGSL2AddrSummaryEntry_Object = MibTableRow
expressGSL2AddrSummaryEntry = _ExpressGSL2AddrSummaryEntry_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 13, 5, 1, 4, 2, 1, 1)
)
expressGSL2AddrSummaryEntry.setIndexNames(
    (0, "EXPRESSGS-MIB", "expressGSL2AddressIndex"),
)
if mibBuilder.loadTexts:
    expressGSL2AddrSummaryEntry.setStatus("mandatory")


class _ExpressGSL2AddrSummary_Type(OctetString):
    """Custom type expressGSL2AddrSummary based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(20, 4096),
    )


_ExpressGSL2AddrSummary_Type.__name__ = "OctetString"
_ExpressGSL2AddrSummary_Object = MibTableColumn
expressGSL2AddrSummary = _ExpressGSL2AddrSummary_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 13, 5, 1, 4, 2, 1, 1, 1),
    _ExpressGSL2AddrSummary_Type()
)
expressGSL2AddrSummary.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    expressGSL2AddrSummary.setStatus("mandatory")
_ExpressGSL2AddrControlMgt_ObjectIdentity = ObjectIdentity
expressGSL2AddrControlMgt = _ExpressGSL2AddrControlMgt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 343, 6, 13, 5, 1, 4, 3)
)
_ExpressGSL2AddressControlTable_Object = MibTable
expressGSL2AddressControlTable = _ExpressGSL2AddressControlTable_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 13, 5, 1, 4, 3, 1)
)
if mibBuilder.loadTexts:
    expressGSL2AddressControlTable.setStatus("mandatory")
_ExpressGSL2AddressControlEntry_Object = MibTableRow
expressGSL2AddressControlEntry = _ExpressGSL2AddressControlEntry_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 13, 5, 1, 4, 3, 1, 1)
)
expressGSL2AddressControlEntry.setIndexNames(
    (0, "EXPRESSGS-MIB", "expressGSAgentMgrIndex"),
)
if mibBuilder.loadTexts:
    expressGSL2AddressControlEntry.setStatus("mandatory")
_ExpressGSL2AddressControlIndex_Type = Integer32
_ExpressGSL2AddressControlIndex_Object = MibTableColumn
expressGSL2AddressControlIndex = _ExpressGSL2AddressControlIndex_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 13, 5, 1, 4, 3, 1, 1, 1),
    _ExpressGSL2AddressControlIndex_Type()
)
expressGSL2AddressControlIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    expressGSL2AddressControlIndex.setStatus("mandatory")
_ExpressGSL2AddressControlMacAddress_Type = MacAddress
_ExpressGSL2AddressControlMacAddress_Object = MibTableColumn
expressGSL2AddressControlMacAddress = _ExpressGSL2AddressControlMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 13, 5, 1, 4, 3, 1, 1, 2),
    _ExpressGSL2AddressControlMacAddress_Type()
)
expressGSL2AddressControlMacAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    expressGSL2AddressControlMacAddress.setStatus("mandatory")
_ExpressGSL2AddressControlPortBinding_Type = ResourceId
_ExpressGSL2AddressControlPortBinding_Object = MibTableColumn
expressGSL2AddressControlPortBinding = _ExpressGSL2AddressControlPortBinding_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 13, 5, 1, 4, 3, 1, 1, 3),
    _ExpressGSL2AddressControlPortBinding_Type()
)
expressGSL2AddressControlPortBinding.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    expressGSL2AddressControlPortBinding.setStatus("mandatory")
_ExpressGSL2AddressControlVlanID_Type = Integer32
_ExpressGSL2AddressControlVlanID_Object = MibTableColumn
expressGSL2AddressControlVlanID = _ExpressGSL2AddressControlVlanID_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 13, 5, 1, 4, 3, 1, 1, 4),
    _ExpressGSL2AddressControlVlanID_Type()
)
expressGSL2AddressControlVlanID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    expressGSL2AddressControlVlanID.setStatus("mandatory")


class _ExpressGSL2AddressControlPriority_Type(Integer32):
    """Custom type expressGSL2AddressControlPriority based on Integer32"""
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


_ExpressGSL2AddressControlPriority_Type.__name__ = "Integer32"
_ExpressGSL2AddressControlPriority_Object = MibTableColumn
expressGSL2AddressControlPriority = _ExpressGSL2AddressControlPriority_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 13, 5, 1, 4, 3, 1, 1, 5),
    _ExpressGSL2AddressControlPriority_Type()
)
expressGSL2AddressControlPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    expressGSL2AddressControlPriority.setStatus("mandatory")


class _ExpressGSL2AddressControlPersistence_Type(Integer32):
    """Custom type expressGSL2AddressControlPersistence based on Integer32"""
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


_ExpressGSL2AddressControlPersistence_Type.__name__ = "Integer32"
_ExpressGSL2AddressControlPersistence_Object = MibTableColumn
expressGSL2AddressControlPersistence = _ExpressGSL2AddressControlPersistence_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 13, 5, 1, 4, 3, 1, 1, 6),
    _ExpressGSL2AddressControlPersistence_Type()
)
expressGSL2AddressControlPersistence.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    expressGSL2AddressControlPersistence.setStatus("mandatory")


class _ExpressGSL2AddressControlStatus_Type(Integer32):
    """Custom type expressGSL2AddressControlStatus based on Integer32"""
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


_ExpressGSL2AddressControlStatus_Type.__name__ = "Integer32"
_ExpressGSL2AddressControlStatus_Object = MibTableColumn
expressGSL2AddressControlStatus = _ExpressGSL2AddressControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 13, 5, 1, 4, 3, 1, 1, 7),
    _ExpressGSL2AddressControlStatus_Type()
)
expressGSL2AddressControlStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    expressGSL2AddressControlStatus.setStatus("mandatory")
_ExpressGSL2AddrChangeMgt_ObjectIdentity = ObjectIdentity
expressGSL2AddrChangeMgt = _ExpressGSL2AddrChangeMgt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 343, 6, 13, 5, 1, 4, 4)
)
_ExpressGSL2AddressChangeLast_Type = Integer32
_ExpressGSL2AddressChangeLast_Object = MibScalar
expressGSL2AddressChangeLast = _ExpressGSL2AddressChangeLast_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 13, 5, 1, 4, 4, 1),
    _ExpressGSL2AddressChangeLast_Type()
)
expressGSL2AddressChangeLast.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    expressGSL2AddressChangeLast.setStatus("mandatory")
_ExpressGSL2AddressChangeWraps_Type = Counter32
_ExpressGSL2AddressChangeWraps_Object = MibScalar
expressGSL2AddressChangeWraps = _ExpressGSL2AddressChangeWraps_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 13, 5, 1, 4, 4, 2),
    _ExpressGSL2AddressChangeWraps_Type()
)
expressGSL2AddressChangeWraps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    expressGSL2AddressChangeWraps.setStatus("mandatory")


class _ExpressGSL2AddressChangeMaxEntries_Type(Integer32):
    """Custom type expressGSL2AddressChangeMaxEntries based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1024, 4096),
    )


_ExpressGSL2AddressChangeMaxEntries_Type.__name__ = "Integer32"
_ExpressGSL2AddressChangeMaxEntries_Object = MibScalar
expressGSL2AddressChangeMaxEntries = _ExpressGSL2AddressChangeMaxEntries_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 13, 5, 1, 4, 4, 3),
    _ExpressGSL2AddressChangeMaxEntries_Type()
)
expressGSL2AddressChangeMaxEntries.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    expressGSL2AddressChangeMaxEntries.setStatus("mandatory")
_ExpressGSL2AddressChangeTable_Object = MibTable
expressGSL2AddressChangeTable = _ExpressGSL2AddressChangeTable_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 13, 5, 1, 4, 4, 4)
)
if mibBuilder.loadTexts:
    expressGSL2AddressChangeTable.setStatus("mandatory")
_ExpressGSL2AddressChangeEntry_Object = MibTableRow
expressGSL2AddressChangeEntry = _ExpressGSL2AddressChangeEntry_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 13, 5, 1, 4, 4, 4, 1)
)
expressGSL2AddressChangeEntry.setIndexNames(
    (0, "EXPRESSGS-MIB", "expressGSL2AddressChangeWrapCount"),
    (0, "EXPRESSGS-MIB", "expressGSL2AddressChangeIndex"),
)
if mibBuilder.loadTexts:
    expressGSL2AddressChangeEntry.setStatus("mandatory")
_ExpressGSL2AddressChangeWrapCount_Type = Integer32
_ExpressGSL2AddressChangeWrapCount_Object = MibTableColumn
expressGSL2AddressChangeWrapCount = _ExpressGSL2AddressChangeWrapCount_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 13, 5, 1, 4, 4, 4, 1, 1),
    _ExpressGSL2AddressChangeWrapCount_Type()
)
expressGSL2AddressChangeWrapCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    expressGSL2AddressChangeWrapCount.setStatus("mandatory")
_ExpressGSL2AddressChangeIndex_Type = Integer32
_ExpressGSL2AddressChangeIndex_Object = MibTableColumn
expressGSL2AddressChangeIndex = _ExpressGSL2AddressChangeIndex_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 13, 5, 1, 4, 4, 4, 1, 2),
    _ExpressGSL2AddressChangeIndex_Type()
)
expressGSL2AddressChangeIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    expressGSL2AddressChangeIndex.setStatus("mandatory")
_ExpressGSL2AddressChangeIndexChanged_Type = Integer32
_ExpressGSL2AddressChangeIndexChanged_Object = MibTableColumn
expressGSL2AddressChangeIndexChanged = _ExpressGSL2AddressChangeIndexChanged_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 13, 5, 1, 4, 4, 4, 1, 3),
    _ExpressGSL2AddressChangeIndexChanged_Type()
)
expressGSL2AddressChangeIndexChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    expressGSL2AddressChangeIndexChanged.setStatus("mandatory")


class _ExpressGSL2AddressChangeSummary_Type(OctetString):
    """Custom type expressGSL2AddressChangeSummary based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(20, 20),
    )


_ExpressGSL2AddressChangeSummary_Type.__name__ = "OctetString"
_ExpressGSL2AddressChangeSummary_Object = MibTableColumn
expressGSL2AddressChangeSummary = _ExpressGSL2AddressChangeSummary_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 13, 5, 1, 4, 4, 4, 1, 4),
    _ExpressGSL2AddressChangeSummary_Type()
)
expressGSL2AddressChangeSummary.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    expressGSL2AddressChangeSummary.setStatus("mandatory")
_ExpressGSSwitchPortMgt_ObjectIdentity = ObjectIdentity
expressGSSwitchPortMgt = _ExpressGSSwitchPortMgt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 343, 6, 13, 5, 2)
)
_ExpressGSSwitchPortTable_Object = MibTable
expressGSSwitchPortTable = _ExpressGSSwitchPortTable_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 13, 5, 2, 1)
)
if mibBuilder.loadTexts:
    expressGSSwitchPortTable.setStatus("mandatory")
_ExpressGSSwitchPortEntry_Object = MibTableRow
expressGSSwitchPortEntry = _ExpressGSSwitchPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 13, 5, 2, 1, 1)
)
expressGSSwitchPortEntry.setIndexNames(
    (0, "EXPRESSGS-MIB", "expressGSSwitchPortIndex"),
)
if mibBuilder.loadTexts:
    expressGSSwitchPortEntry.setStatus("mandatory")
_ExpressGSSwitchPortIndex_Type = ResourceId
_ExpressGSSwitchPortIndex_Object = MibTableColumn
expressGSSwitchPortIndex = _ExpressGSSwitchPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 13, 5, 2, 1, 1, 1),
    _ExpressGSSwitchPortIndex_Type()
)
expressGSSwitchPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    expressGSSwitchPortIndex.setStatus("mandatory")


class _ExpressGSSwitchPortSTAPMode_Type(Integer32):
    """Custom type expressGSSwitchPortSTAPMode based on Integer32"""
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


_ExpressGSSwitchPortSTAPMode_Type.__name__ = "Integer32"
_ExpressGSSwitchPortSTAPMode_Object = MibTableColumn
expressGSSwitchPortSTAPMode = _ExpressGSSwitchPortSTAPMode_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 13, 5, 2, 1, 1, 2),
    _ExpressGSSwitchPortSTAPMode_Type()
)
expressGSSwitchPortSTAPMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    expressGSSwitchPortSTAPMode.setStatus("mandatory")


class _ExpressGSSwitchPortConvertToStatic_Type(Integer32):
    """Custom type expressGSSwitchPortConvertToStatic based on Integer32"""
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


_ExpressGSSwitchPortConvertToStatic_Type.__name__ = "Integer32"
_ExpressGSSwitchPortConvertToStatic_Object = MibTableColumn
expressGSSwitchPortConvertToStatic = _ExpressGSSwitchPortConvertToStatic_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 13, 5, 2, 1, 1, 3),
    _ExpressGSSwitchPortConvertToStatic_Type()
)
expressGSSwitchPortConvertToStatic.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    expressGSSwitchPortConvertToStatic.setStatus("mandatory")


class _ExpressGSSwitchPortLearningMode_Type(Integer32):
    """Custom type expressGSSwitchPortLearningMode based on Integer32"""
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


_ExpressGSSwitchPortLearningMode_Type.__name__ = "Integer32"
_ExpressGSSwitchPortLearningMode_Object = MibTableColumn
expressGSSwitchPortLearningMode = _ExpressGSSwitchPortLearningMode_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 13, 5, 2, 1, 1, 4),
    _ExpressGSSwitchPortLearningMode_Type()
)
expressGSSwitchPortLearningMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    expressGSSwitchPortLearningMode.setStatus("mandatory")
_ExpressGSSwitchPortHuntGroup_Type = Integer32
_ExpressGSSwitchPortHuntGroup_Object = MibTableColumn
expressGSSwitchPortHuntGroup = _ExpressGSSwitchPortHuntGroup_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 13, 5, 2, 1, 1, 5),
    _ExpressGSSwitchPortHuntGroup_Type()
)
expressGSSwitchPortHuntGroup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    expressGSSwitchPortHuntGroup.setStatus("mandatory")
_ExpressGSSwitchPortPhysicalPort_Type = ResourceId
_ExpressGSSwitchPortPhysicalPort_Object = MibTableColumn
expressGSSwitchPortPhysicalPort = _ExpressGSSwitchPortPhysicalPort_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 13, 5, 2, 1, 1, 6),
    _ExpressGSSwitchPortPhysicalPort_Type()
)
expressGSSwitchPortPhysicalPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    expressGSSwitchPortPhysicalPort.setStatus("mandatory")


class _ExpressGSSwitchPortKnownMode_Type(Integer32):
    """Custom type expressGSSwitchPortKnownMode based on Integer32"""
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


_ExpressGSSwitchPortKnownMode_Type.__name__ = "Integer32"
_ExpressGSSwitchPortKnownMode_Object = MibTableColumn
expressGSSwitchPortKnownMode = _ExpressGSSwitchPortKnownMode_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 13, 5, 2, 1, 1, 7),
    _ExpressGSSwitchPortKnownMode_Type()
)
expressGSSwitchPortKnownMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    expressGSSwitchPortKnownMode.setStatus("mandatory")


class _ExpressGSSwitchPortMappingMethod_Type(Integer32):
    """Custom type expressGSSwitchPortMappingMethod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("port-based", 1)
    )


_ExpressGSSwitchPortMappingMethod_Type.__name__ = "Integer32"
_ExpressGSSwitchPortMappingMethod_Object = MibTableColumn
expressGSSwitchPortMappingMethod = _ExpressGSSwitchPortMappingMethod_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 13, 5, 2, 1, 1, 8),
    _ExpressGSSwitchPortMappingMethod_Type()
)
expressGSSwitchPortMappingMethod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    expressGSSwitchPortMappingMethod.setStatus("mandatory")


class _ExpressGSSwitchPortTrunkingMode_Type(Integer32):
    """Custom type expressGSSwitchPortTrunkingMode based on Integer32"""
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


_ExpressGSSwitchPortTrunkingMode_Type.__name__ = "Integer32"
_ExpressGSSwitchPortTrunkingMode_Object = MibTableColumn
expressGSSwitchPortTrunkingMode = _ExpressGSSwitchPortTrunkingMode_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 13, 5, 2, 1, 1, 9),
    _ExpressGSSwitchPortTrunkingMode_Type()
)
expressGSSwitchPortTrunkingMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    expressGSSwitchPortTrunkingMode.setStatus("mandatory")


class _ExpressGSSwitchPortVlanBindingMethod_Type(Integer32):
    """Custom type expressGSSwitchPortVlanBindingMethod based on Integer32"""
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


_ExpressGSSwitchPortVlanBindingMethod_Type.__name__ = "Integer32"
_ExpressGSSwitchPortVlanBindingMethod_Object = MibTableColumn
expressGSSwitchPortVlanBindingMethod = _ExpressGSSwitchPortVlanBindingMethod_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 13, 5, 2, 1, 1, 10),
    _ExpressGSSwitchPortVlanBindingMethod_Type()
)
expressGSSwitchPortVlanBindingMethod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    expressGSSwitchPortVlanBindingMethod.setStatus("mandatory")


class _ExpressGSSwitchPortIgnoreTag_Type(Integer32):
    """Custom type expressGSSwitchPortIgnoreTag based on Integer32"""
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


_ExpressGSSwitchPortIgnoreTag_Type.__name__ = "Integer32"
_ExpressGSSwitchPortIgnoreTag_Object = MibTableColumn
expressGSSwitchPortIgnoreTag = _ExpressGSSwitchPortIgnoreTag_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 13, 5, 2, 1, 1, 11),
    _ExpressGSSwitchPortIgnoreTag_Type()
)
expressGSSwitchPortIgnoreTag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    expressGSSwitchPortIgnoreTag.setStatus("mandatory")
_ExpressGSSwitchPortVlanID_Type = Integer32
_ExpressGSSwitchPortVlanID_Object = MibTableColumn
expressGSSwitchPortVlanID = _ExpressGSSwitchPortVlanID_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 13, 5, 2, 1, 1, 12),
    _ExpressGSSwitchPortVlanID_Type()
)
expressGSSwitchPortVlanID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    expressGSSwitchPortVlanID.setStatus("mandatory")


class _ExpressGSSwitchPort3ComMappingTableIndex_Type(Integer32):
    """Custom type expressGSSwitchPort3ComMappingTableIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_ExpressGSSwitchPort3ComMappingTableIndex_Type.__name__ = "Integer32"
_ExpressGSSwitchPort3ComMappingTableIndex_Object = MibTableColumn
expressGSSwitchPort3ComMappingTableIndex = _ExpressGSSwitchPort3ComMappingTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 13, 5, 2, 1, 1, 13),
    _ExpressGSSwitchPort3ComMappingTableIndex_Type()
)
expressGSSwitchPort3ComMappingTableIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    expressGSSwitchPort3ComMappingTableIndex.setStatus("mandatory")


class _ExpressGSSwitchPortAutoVlanCreation_Type(Integer32):
    """Custom type expressGSSwitchPortAutoVlanCreation based on Integer32"""
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


_ExpressGSSwitchPortAutoVlanCreation_Type.__name__ = "Integer32"
_ExpressGSSwitchPortAutoVlanCreation_Object = MibTableColumn
expressGSSwitchPortAutoVlanCreation = _ExpressGSSwitchPortAutoVlanCreation_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 13, 5, 2, 1, 1, 14),
    _ExpressGSSwitchPortAutoVlanCreation_Type()
)
expressGSSwitchPortAutoVlanCreation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    expressGSSwitchPortAutoVlanCreation.setStatus("mandatory")


class _ExpressGSSwitchPortMirrorMode_Type(Integer32):
    """Custom type expressGSSwitchPortMirrorMode based on Integer32"""
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


_ExpressGSSwitchPortMirrorMode_Type.__name__ = "Integer32"
_ExpressGSSwitchPortMirrorMode_Object = MibScalar
expressGSSwitchPortMirrorMode = _ExpressGSSwitchPortMirrorMode_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 13, 5, 2, 1, 1, 15),
    _ExpressGSSwitchPortMirrorMode_Type()
)
expressGSSwitchPortMirrorMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    expressGSSwitchPortMirrorMode.setStatus("mandatory")
_ExpressGSSwitchPortIfIndex_Type = Integer32
_ExpressGSSwitchPortIfIndex_Object = MibScalar
expressGSSwitchPortIfIndex = _ExpressGSSwitchPortIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 13, 5, 2, 1, 1, 16),
    _ExpressGSSwitchPortIfIndex_Type()
)
expressGSSwitchPortIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    expressGSSwitchPortIfIndex.setStatus("mandatory")


class _ExpressGSSwitchPortFastStart_Type(Integer32):
    """Custom type expressGSSwitchPortFastStart based on Integer32"""
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


_ExpressGSSwitchPortFastStart_Type.__name__ = "Integer32"
_ExpressGSSwitchPortFastStart_Object = MibTableColumn
expressGSSwitchPortFastStart = _ExpressGSSwitchPortFastStart_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 13, 5, 2, 1, 1, 17),
    _ExpressGSSwitchPortFastStart_Type()
)
expressGSSwitchPortFastStart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    expressGSSwitchPortFastStart.setStatus("mandatory")
_ExpressGSHuntGroupMgt_ObjectIdentity = ObjectIdentity
expressGSHuntGroupMgt = _ExpressGSHuntGroupMgt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 343, 6, 13, 5, 4)
)
_ExpressGSHuntGroupTable_Object = MibTable
expressGSHuntGroupTable = _ExpressGSHuntGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 13, 5, 4, 1)
)
if mibBuilder.loadTexts:
    expressGSHuntGroupTable.setStatus("mandatory")
_ExpressGSHuntGroupEntry_Object = MibTableRow
expressGSHuntGroupEntry = _ExpressGSHuntGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 13, 5, 4, 1, 1)
)
expressGSHuntGroupEntry.setIndexNames(
    (0, "EXPRESSGS-MIB", "expressGSHuntGroupIndex"),
)
if mibBuilder.loadTexts:
    expressGSHuntGroupEntry.setStatus("mandatory")
_ExpressGSHuntGroupIndex_Type = Integer32
_ExpressGSHuntGroupIndex_Object = MibTableColumn
expressGSHuntGroupIndex = _ExpressGSHuntGroupIndex_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 13, 5, 4, 1, 1, 1),
    _ExpressGSHuntGroupIndex_Type()
)
expressGSHuntGroupIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    expressGSHuntGroupIndex.setStatus("mandatory")
_ExpressGSHuntGroupName_Type = DisplayString
_ExpressGSHuntGroupName_Object = MibTableColumn
expressGSHuntGroupName = _ExpressGSHuntGroupName_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 13, 5, 4, 1, 1, 2),
    _ExpressGSHuntGroupName_Type()
)
expressGSHuntGroupName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    expressGSHuntGroupName.setStatus("mandatory")
_ExpressGSHuntGroupBasePort_Type = ResourceId
_ExpressGSHuntGroupBasePort_Object = MibTableColumn
expressGSHuntGroupBasePort = _ExpressGSHuntGroupBasePort_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 13, 5, 4, 1, 1, 3),
    _ExpressGSHuntGroupBasePort_Type()
)
expressGSHuntGroupBasePort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    expressGSHuntGroupBasePort.setStatus("mandatory")
_ExpressGSHuntGroupNumberOfPorts_Type = Integer32
_ExpressGSHuntGroupNumberOfPorts_Object = MibTableColumn
expressGSHuntGroupNumberOfPorts = _ExpressGSHuntGroupNumberOfPorts_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 13, 5, 4, 1, 1, 4),
    _ExpressGSHuntGroupNumberOfPorts_Type()
)
expressGSHuntGroupNumberOfPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    expressGSHuntGroupNumberOfPorts.setStatus("mandatory")


class _ExpressGSHuntGroupLoadSharing_Type(Integer32):
    """Custom type expressGSHuntGroupLoadSharing based on Integer32"""
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


_ExpressGSHuntGroupLoadSharing_Type.__name__ = "Integer32"
_ExpressGSHuntGroupLoadSharing_Object = MibTableColumn
expressGSHuntGroupLoadSharing = _ExpressGSHuntGroupLoadSharing_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 13, 5, 4, 1, 1, 5),
    _ExpressGSHuntGroupLoadSharing_Type()
)
expressGSHuntGroupLoadSharing.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    expressGSHuntGroupLoadSharing.setStatus("mandatory")


class _ExpressGSHuntGroupStatus_Type(Integer32):
    """Custom type expressGSHuntGroupStatus based on Integer32"""
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


_ExpressGSHuntGroupStatus_Type.__name__ = "Integer32"
_ExpressGSHuntGroupStatus_Object = MibTableColumn
expressGSHuntGroupStatus = _ExpressGSHuntGroupStatus_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 13, 5, 4, 1, 1, 6),
    _ExpressGSHuntGroupStatus_Type()
)
expressGSHuntGroupStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    expressGSHuntGroupStatus.setStatus("mandatory")
_ExpressGSPortMirroringMgt_ObjectIdentity = ObjectIdentity
expressGSPortMirroringMgt = _ExpressGSPortMirroringMgt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 343, 6, 13, 5, 5)
)
_ExpressGSPortMirroringTable_Object = MibTable
expressGSPortMirroringTable = _ExpressGSPortMirroringTable_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 13, 5, 5, 1)
)
if mibBuilder.loadTexts:
    expressGSPortMirroringTable.setStatus("mandatory")
_ExpressGSPortMirroringEntry_Object = MibTableRow
expressGSPortMirroringEntry = _ExpressGSPortMirroringEntry_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 13, 5, 5, 1, 1)
)
expressGSPortMirroringEntry.setIndexNames(
    (0, "EXPRESSGS-MIB", "expressGSPortMirroringIndex"),
)
if mibBuilder.loadTexts:
    expressGSPortMirroringEntry.setStatus("mandatory")
_ExpressGSPortMirroringIndex_Type = ResourceId
_ExpressGSPortMirroringIndex_Object = MibTableColumn
expressGSPortMirroringIndex = _ExpressGSPortMirroringIndex_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 13, 5, 5, 1, 1, 1),
    _ExpressGSPortMirroringIndex_Type()
)
expressGSPortMirroringIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    expressGSPortMirroringIndex.setStatus("mandatory")
_ExpressGSPortMirroringSourceSubPort_Type = Integer32
_ExpressGSPortMirroringSourceSubPort_Object = MibTableColumn
expressGSPortMirroringSourceSubPort = _ExpressGSPortMirroringSourceSubPort_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 13, 5, 5, 1, 1, 2),
    _ExpressGSPortMirroringSourceSubPort_Type()
)
expressGSPortMirroringSourceSubPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    expressGSPortMirroringSourceSubPort.setStatus("mandatory")


class _ExpressGSPortMirroringSamplerType_Type(Integer32):
    """Custom type expressGSPortMirroringSamplerType based on Integer32"""
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


_ExpressGSPortMirroringSamplerType_Type.__name__ = "Integer32"
_ExpressGSPortMirroringSamplerType_Object = MibTableColumn
expressGSPortMirroringSamplerType = _ExpressGSPortMirroringSamplerType_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 13, 5, 5, 1, 1, 3),
    _ExpressGSPortMirroringSamplerType_Type()
)
expressGSPortMirroringSamplerType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    expressGSPortMirroringSamplerType.setStatus("mandatory")
_ExpressGSPortMirroringRate_Type = Integer32
_ExpressGSPortMirroringRate_Object = MibTableColumn
expressGSPortMirroringRate = _ExpressGSPortMirroringRate_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 13, 5, 5, 1, 1, 4),
    _ExpressGSPortMirroringRate_Type()
)
expressGSPortMirroringRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    expressGSPortMirroringRate.setStatus("mandatory")
_ExpressGSPortMirroringMirrorPort_Type = ResourceId
_ExpressGSPortMirroringMirrorPort_Object = MibTableColumn
expressGSPortMirroringMirrorPort = _ExpressGSPortMirroringMirrorPort_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 13, 5, 5, 1, 1, 5),
    _ExpressGSPortMirroringMirrorPort_Type()
)
expressGSPortMirroringMirrorPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    expressGSPortMirroringMirrorPort.setStatus("mandatory")
_ExpressGSVlanMgt_ObjectIdentity = ObjectIdentity
expressGSVlanMgt = _ExpressGSVlanMgt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 343, 6, 13, 7)
)
_ExpressGSVlans_ObjectIdentity = ObjectIdentity
expressGSVlans = _ExpressGSVlans_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 343, 6, 13, 7, 1)
)
_ExpressGSVlanTable_Object = MibTable
expressGSVlanTable = _ExpressGSVlanTable_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 13, 7, 1, 1)
)
if mibBuilder.loadTexts:
    expressGSVlanTable.setStatus("mandatory")
_ExpressGSVlanEntry_Object = MibTableRow
expressGSVlanEntry = _ExpressGSVlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 13, 7, 1, 1, 1)
)
expressGSVlanEntry.setIndexNames(
    (0, "EXPRESSGS-MIB", "expressGSVlanID"),
)
if mibBuilder.loadTexts:
    expressGSVlanEntry.setStatus("mandatory")
_ExpressGSVlanID_Type = Integer32
_ExpressGSVlanID_Object = MibTableColumn
expressGSVlanID = _ExpressGSVlanID_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 13, 7, 1, 1, 1, 1),
    _ExpressGSVlanID_Type()
)
expressGSVlanID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    expressGSVlanID.setStatus("mandatory")


class _ExpressGSVlanName_Type(DisplayString):
    """Custom type expressGSVlanName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_ExpressGSVlanName_Type.__name__ = "DisplayString"
_ExpressGSVlanName_Object = MibTableColumn
expressGSVlanName = _ExpressGSVlanName_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 13, 7, 1, 1, 1, 2),
    _ExpressGSVlanName_Type()
)
expressGSVlanName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    expressGSVlanName.setStatus("mandatory")
_ExpressGSVlanIfIndex_Type = Integer32
_ExpressGSVlanIfIndex_Object = MibTableColumn
expressGSVlanIfIndex = _ExpressGSVlanIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 13, 7, 1, 1, 1, 3),
    _ExpressGSVlanIfIndex_Type()
)
expressGSVlanIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    expressGSVlanIfIndex.setStatus("mandatory")
_ExpressGSVlanAFTIndex_Type = Integer32
_ExpressGSVlanAFTIndex_Object = MibTableColumn
expressGSVlanAFTIndex = _ExpressGSVlanAFTIndex_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 13, 7, 1, 1, 1, 4),
    _ExpressGSVlanAFTIndex_Type()
)
expressGSVlanAFTIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    expressGSVlanAFTIndex.setStatus("mandatory")
_ExpressGSVlanBridgeIndex_Type = ResourceId
_ExpressGSVlanBridgeIndex_Object = MibTableColumn
expressGSVlanBridgeIndex = _ExpressGSVlanBridgeIndex_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 13, 7, 1, 1, 1, 5),
    _ExpressGSVlanBridgeIndex_Type()
)
expressGSVlanBridgeIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    expressGSVlanBridgeIndex.setStatus("mandatory")


class _ExpressGSVlanStatus_Type(Integer32):
    """Custom type expressGSVlanStatus based on Integer32"""
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


_ExpressGSVlanStatus_Type.__name__ = "Integer32"
_ExpressGSVlanStatus_Object = MibTableColumn
expressGSVlanStatus = _ExpressGSVlanStatus_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 13, 7, 1, 1, 1, 6),
    _ExpressGSVlanStatus_Type()
)
expressGSVlanStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    expressGSVlanStatus.setStatus("mandatory")


class _ExpressGSVlanInitialHashTableSize_Type(Integer32):
    """Custom type expressGSVlanInitialHashTableSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(16, 8192),
    )


_ExpressGSVlanInitialHashTableSize_Type.__name__ = "Integer32"
_ExpressGSVlanInitialHashTableSize_Object = MibTableColumn
expressGSVlanInitialHashTableSize = _ExpressGSVlanInitialHashTableSize_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 13, 7, 1, 1, 1, 7),
    _ExpressGSVlanInitialHashTableSize_Type()
)
expressGSVlanInitialHashTableSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    expressGSVlanInitialHashTableSize.setStatus("mandatory")


class _ExpressGSVlanAutoIncrementHTSize_Type(Integer32):
    """Custom type expressGSVlanAutoIncrementHTSize based on Integer32"""
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


_ExpressGSVlanAutoIncrementHTSize_Type.__name__ = "Integer32"
_ExpressGSVlanAutoIncrementHTSize_Object = MibTableColumn
expressGSVlanAutoIncrementHTSize = _ExpressGSVlanAutoIncrementHTSize_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 13, 7, 1, 1, 1, 8),
    _ExpressGSVlanAutoIncrementHTSize_Type()
)
expressGSVlanAutoIncrementHTSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    expressGSVlanAutoIncrementHTSize.setStatus("mandatory")
_ExpressGSVlanMappings_ObjectIdentity = ObjectIdentity
expressGSVlanMappings = _ExpressGSVlanMappings_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 343, 6, 13, 7, 3)
)
_ExpressGS3ComMapping_ObjectIdentity = ObjectIdentity
expressGS3ComMapping = _ExpressGS3ComMapping_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 343, 6, 13, 7, 3, 1)
)
_ExpressGS3ComMappingTable_Object = MibTable
expressGS3ComMappingTable = _ExpressGS3ComMappingTable_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 13, 7, 3, 1, 1)
)
if mibBuilder.loadTexts:
    expressGS3ComMappingTable.setStatus("mandatory")
_ExpressGS3ComMappingEntry_Object = MibTableRow
expressGS3ComMappingEntry = _ExpressGS3ComMappingEntry_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 13, 7, 3, 1, 1, 1)
)
expressGS3ComMappingEntry.setIndexNames(
    (0, "EXPRESSGS-MIB", "expressGS3ComMappingTableIndex"),
)
if mibBuilder.loadTexts:
    expressGS3ComMappingEntry.setStatus("mandatory")
_ExpressGS3ComMappingTableIndex_Type = Integer32
_ExpressGS3ComMappingTableIndex_Object = MibTableColumn
expressGS3ComMappingTableIndex = _ExpressGS3ComMappingTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 13, 7, 3, 1, 1, 1, 1),
    _ExpressGS3ComMappingTableIndex_Type()
)
expressGS3ComMappingTableIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    expressGS3ComMappingTableIndex.setStatus("mandatory")


class _ExpressGS3ComMappingTableName_Type(DisplayString):
    """Custom type expressGS3ComMappingTableName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_ExpressGS3ComMappingTableName_Type.__name__ = "DisplayString"
_ExpressGS3ComMappingTableName_Object = MibTableColumn
expressGS3ComMappingTableName = _ExpressGS3ComMappingTableName_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 13, 7, 3, 1, 1, 1, 2),
    _ExpressGS3ComMappingTableName_Type()
)
expressGS3ComMappingTableName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    expressGS3ComMappingTableName.setStatus("mandatory")


class _ExpressGS3ComMappingTableStatus_Type(Integer32):
    """Custom type expressGS3ComMappingTableStatus based on Integer32"""
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


_ExpressGS3ComMappingTableStatus_Type.__name__ = "Integer32"
_ExpressGS3ComMappingTableStatus_Object = MibTableColumn
expressGS3ComMappingTableStatus = _ExpressGS3ComMappingTableStatus_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 13, 7, 3, 1, 1, 1, 3),
    _ExpressGS3ComMappingTableStatus_Type()
)
expressGS3ComMappingTableStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    expressGS3ComMappingTableStatus.setStatus("mandatory")
_ExpressGSVlan3ComMapping_ObjectIdentity = ObjectIdentity
expressGSVlan3ComMapping = _ExpressGSVlan3ComMapping_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 343, 6, 13, 7, 3, 2)
)
_ExpressGSVlan3ComMappingTable_Object = MibTable
expressGSVlan3ComMappingTable = _ExpressGSVlan3ComMappingTable_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 13, 7, 3, 2, 1)
)
if mibBuilder.loadTexts:
    expressGSVlan3ComMappingTable.setStatus("mandatory")
_ExpressGSVlan3ComMappingEntry_Object = MibTableRow
expressGSVlan3ComMappingEntry = _ExpressGSVlan3ComMappingEntry_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 13, 7, 3, 2, 1, 1)
)
expressGSVlan3ComMappingEntry.setIndexNames(
    (0, "EXPRESSGS-MIB", "expressGS3ComMappingTableIndex"),
    (0, "EXPRESSGS-MIB", "expressGSVlan3ComMappingIndex"),
)
if mibBuilder.loadTexts:
    expressGSVlan3ComMappingEntry.setStatus("mandatory")


class _ExpressGSVlan3ComMappingIndex_Type(Integer32):
    """Custom type expressGSVlan3ComMappingIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_ExpressGSVlan3ComMappingIndex_Type.__name__ = "Integer32"
_ExpressGSVlan3ComMappingIndex_Object = MibTableColumn
expressGSVlan3ComMappingIndex = _ExpressGSVlan3ComMappingIndex_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 13, 7, 3, 2, 1, 1, 1),
    _ExpressGSVlan3ComMappingIndex_Type()
)
expressGSVlan3ComMappingIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    expressGSVlan3ComMappingIndex.setStatus("mandatory")
_ExpressGSVlan3ComMappingVlanID_Type = Integer32
_ExpressGSVlan3ComMappingVlanID_Object = MibTableColumn
expressGSVlan3ComMappingVlanID = _ExpressGSVlan3ComMappingVlanID_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 13, 7, 3, 2, 1, 1, 2),
    _ExpressGSVlan3ComMappingVlanID_Type()
)
expressGSVlan3ComMappingVlanID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    expressGSVlan3ComMappingVlanID.setStatus("mandatory")


class _ExpressGSVlan3ComMappingStatus_Type(Integer32):
    """Custom type expressGSVlan3ComMappingStatus based on Integer32"""
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


_ExpressGSVlan3ComMappingStatus_Type.__name__ = "Integer32"
_ExpressGSVlan3ComMappingStatus_Object = MibTableColumn
expressGSVlan3ComMappingStatus = _ExpressGSVlan3ComMappingStatus_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 13, 7, 3, 2, 1, 1, 3),
    _ExpressGSVlan3ComMappingStatus_Type()
)
expressGSVlan3ComMappingStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    expressGSVlan3ComMappingStatus.setStatus("mandatory")
_ExpressGSVirtualPorts_ObjectIdentity = ObjectIdentity
expressGSVirtualPorts = _ExpressGSVirtualPorts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 343, 6, 13, 7, 4)
)
_ExpressGSVirtualSwitchPortTable_Object = MibTable
expressGSVirtualSwitchPortTable = _ExpressGSVirtualSwitchPortTable_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 13, 7, 4, 1)
)
if mibBuilder.loadTexts:
    expressGSVirtualSwitchPortTable.setStatus("mandatory")
_ExpressGSVirtualSwitchPortEntry_Object = MibTableRow
expressGSVirtualSwitchPortEntry = _ExpressGSVirtualSwitchPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 13, 7, 4, 1, 1)
)
expressGSVirtualSwitchPortEntry.setIndexNames(
    (0, "EXPRESSGS-MIB", "expressGSVirtualSwitchPortIndex"),
)
if mibBuilder.loadTexts:
    expressGSVirtualSwitchPortEntry.setStatus("mandatory")
_ExpressGSVirtualSwitchPortIndex_Type = ResourceId
_ExpressGSVirtualSwitchPortIndex_Object = MibTableColumn
expressGSVirtualSwitchPortIndex = _ExpressGSVirtualSwitchPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 13, 7, 4, 1, 1, 1),
    _ExpressGSVirtualSwitchPortIndex_Type()
)
expressGSVirtualSwitchPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    expressGSVirtualSwitchPortIndex.setStatus("mandatory")


class _ExpressGSVirtualSwitchPortFormat_Type(Integer32):
    """Custom type expressGSVirtualSwitchPortFormat based on Integer32"""
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


_ExpressGSVirtualSwitchPortFormat_Type.__name__ = "Integer32"
_ExpressGSVirtualSwitchPortFormat_Object = MibTableColumn
expressGSVirtualSwitchPortFormat = _ExpressGSVirtualSwitchPortFormat_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 13, 7, 4, 1, 1, 2),
    _ExpressGSVirtualSwitchPortFormat_Type()
)
expressGSVirtualSwitchPortFormat.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    expressGSVirtualSwitchPortFormat.setStatus("mandatory")
_ExpressGSVirtualSwitchPortBridgePort_Type = ResourceId
_ExpressGSVirtualSwitchPortBridgePort_Object = MibTableColumn
expressGSVirtualSwitchPortBridgePort = _ExpressGSVirtualSwitchPortBridgePort_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 13, 7, 4, 1, 1, 3),
    _ExpressGSVirtualSwitchPortBridgePort_Type()
)
expressGSVirtualSwitchPortBridgePort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    expressGSVirtualSwitchPortBridgePort.setStatus("mandatory")


class _ExpressGSVirtualSwitchPortBindingType_Type(Integer32):
    """Custom type expressGSVirtualSwitchPortBindingType based on Integer32"""
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


_ExpressGSVirtualSwitchPortBindingType_Type.__name__ = "Integer32"
_ExpressGSVirtualSwitchPortBindingType_Object = MibTableColumn
expressGSVirtualSwitchPortBindingType = _ExpressGSVirtualSwitchPortBindingType_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 13, 7, 4, 1, 1, 4),
    _ExpressGSVirtualSwitchPortBindingType_Type()
)
expressGSVirtualSwitchPortBindingType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    expressGSVirtualSwitchPortBindingType.setStatus("mandatory")


class _ExpressGSVirtualSwitchPortStatus_Type(Integer32):
    """Custom type expressGSVirtualSwitchPortStatus based on Integer32"""
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


_ExpressGSVirtualSwitchPortStatus_Type.__name__ = "Integer32"
_ExpressGSVirtualSwitchPortStatus_Object = MibTableColumn
expressGSVirtualSwitchPortStatus = _ExpressGSVirtualSwitchPortStatus_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 13, 7, 4, 1, 1, 5),
    _ExpressGSVirtualSwitchPortStatus_Type()
)
expressGSVirtualSwitchPortStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    expressGSVirtualSwitchPortStatus.setStatus("mandatory")
_ExpressGSEvents_ObjectIdentity = ObjectIdentity
expressGSEvents = _ExpressGSEvents_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 343, 6, 13, 10)
)
_ExpressGSEventMgt_ObjectIdentity = ObjectIdentity
expressGSEventMgt = _ExpressGSEventMgt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 343, 6, 13, 10, 1)
)
_ExpressGSEventTable_Object = MibTable
expressGSEventTable = _ExpressGSEventTable_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 13, 10, 1, 1)
)
if mibBuilder.loadTexts:
    expressGSEventTable.setStatus("mandatory")
_ExpressGSEventEntry_Object = MibTableRow
expressGSEventEntry = _ExpressGSEventEntry_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 13, 10, 1, 1, 1)
)
expressGSEventEntry.setIndexNames(
    (0, "EXPRESSGS-MIB", "expressGSEventIndex"),
)
if mibBuilder.loadTexts:
    expressGSEventEntry.setStatus("mandatory")
_ExpressGSEventIndex_Type = Integer32
_ExpressGSEventIndex_Object = MibTableColumn
expressGSEventIndex = _ExpressGSEventIndex_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 13, 10, 1, 1, 1, 1),
    _ExpressGSEventIndex_Type()
)
expressGSEventIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    expressGSEventIndex.setStatus("mandatory")


class _ExpressGSEventMode_Type(Integer32):
    """Custom type expressGSEventMode based on Integer32"""
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


_ExpressGSEventMode_Type.__name__ = "Integer32"
_ExpressGSEventMode_Object = MibTableColumn
expressGSEventMode = _ExpressGSEventMode_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 13, 10, 1, 1, 1, 2),
    _ExpressGSEventMode_Type()
)
expressGSEventMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    expressGSEventMode.setStatus("mandatory")


class _ExpressGSEventLogAction_Type(Integer32):
    """Custom type expressGSEventLogAction based on Integer32"""
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


_ExpressGSEventLogAction_Type.__name__ = "Integer32"
_ExpressGSEventLogAction_Object = MibTableColumn
expressGSEventLogAction = _ExpressGSEventLogAction_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 13, 10, 1, 1, 1, 3),
    _ExpressGSEventLogAction_Type()
)
expressGSEventLogAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    expressGSEventLogAction.setStatus("mandatory")


class _ExpressGSEventTrapAction_Type(Integer32):
    """Custom type expressGSEventTrapAction based on Integer32"""
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


_ExpressGSEventTrapAction_Type.__name__ = "Integer32"
_ExpressGSEventTrapAction_Object = MibTableColumn
expressGSEventTrapAction = _ExpressGSEventTrapAction_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 13, 10, 1, 1, 1, 4),
    _ExpressGSEventTrapAction_Type()
)
expressGSEventTrapAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    expressGSEventTrapAction.setStatus("mandatory")


class _ExpressGSEventConsoleAction_Type(Integer32):
    """Custom type expressGSEventConsoleAction based on Integer32"""
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


_ExpressGSEventConsoleAction_Type.__name__ = "Integer32"
_ExpressGSEventConsoleAction_Object = MibTableColumn
expressGSEventConsoleAction = _ExpressGSEventConsoleAction_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 13, 10, 1, 1, 1, 5),
    _ExpressGSEventConsoleAction_Type()
)
expressGSEventConsoleAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    expressGSEventConsoleAction.setStatus("mandatory")
_ExpressGSEventLogMgt_ObjectIdentity = ObjectIdentity
expressGSEventLogMgt = _ExpressGSEventLogMgt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 343, 6, 13, 10, 2)
)


class _ExpressGSLogTableMaxSize_Type(Integer32):
    """Custom type expressGSLogTableMaxSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2048),
    )


_ExpressGSLogTableMaxSize_Type.__name__ = "Integer32"
_ExpressGSLogTableMaxSize_Object = MibScalar
expressGSLogTableMaxSize = _ExpressGSLogTableMaxSize_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 13, 10, 2, 1),
    _ExpressGSLogTableMaxSize_Type()
)
expressGSLogTableMaxSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    expressGSLogTableMaxSize.setStatus("mandatory")


class _ExpressGSLogLastEntry_Type(Integer32):
    """Custom type expressGSLogLastEntry based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_ExpressGSLogLastEntry_Type.__name__ = "Integer32"
_ExpressGSLogLastEntry_Object = MibScalar
expressGSLogLastEntry = _ExpressGSLogLastEntry_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 13, 10, 2, 2),
    _ExpressGSLogLastEntry_Type()
)
expressGSLogLastEntry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    expressGSLogLastEntry.setStatus("mandatory")
_ExpressGSLogWraps_Type = Counter32
_ExpressGSLogWraps_Object = MibScalar
expressGSLogWraps = _ExpressGSLogWraps_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 13, 10, 2, 3),
    _ExpressGSLogWraps_Type()
)
expressGSLogWraps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    expressGSLogWraps.setStatus("mandatory")
_ExpressGSEventLog_ObjectIdentity = ObjectIdentity
expressGSEventLog = _ExpressGSEventLog_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 343, 6, 13, 10, 3)
)
_ExpressGSEventLogTable_Object = MibTable
expressGSEventLogTable = _ExpressGSEventLogTable_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 13, 10, 3, 1)
)
if mibBuilder.loadTexts:
    expressGSEventLogTable.setStatus("mandatory")
_ExpressGSEventLogEntry_Object = MibTableRow
expressGSEventLogEntry = _ExpressGSEventLogEntry_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 13, 10, 3, 1, 1)
)
expressGSEventLogEntry.setIndexNames(
    (0, "EXPRESSGS-MIB", "expressGSEventLogIndex"),
)
if mibBuilder.loadTexts:
    expressGSEventLogEntry.setStatus("mandatory")


class _ExpressGSEventLogEventIndex_Type(Integer32):
    """Custom type expressGSEventLogEventIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_ExpressGSEventLogEventIndex_Type.__name__ = "Integer32"
_ExpressGSEventLogEventIndex_Object = MibTableColumn
expressGSEventLogEventIndex = _ExpressGSEventLogEventIndex_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 13, 10, 3, 1, 1, 1),
    _ExpressGSEventLogEventIndex_Type()
)
expressGSEventLogEventIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    expressGSEventLogEventIndex.setStatus("mandatory")


class _ExpressGSEventLogIndex_Type(Integer32):
    """Custom type expressGSEventLogIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_ExpressGSEventLogIndex_Type.__name__ = "Integer32"
_ExpressGSEventLogIndex_Object = MibTableColumn
expressGSEventLogIndex = _ExpressGSEventLogIndex_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 13, 10, 3, 1, 1, 2),
    _ExpressGSEventLogIndex_Type()
)
expressGSEventLogIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    expressGSEventLogIndex.setStatus("mandatory")
_ExpressGSEventLogTime_Type = TimeTicks
_ExpressGSEventLogTime_Object = MibTableColumn
expressGSEventLogTime = _ExpressGSEventLogTime_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 13, 10, 3, 1, 1, 3),
    _ExpressGSEventLogTime_Type()
)
expressGSEventLogTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    expressGSEventLogTime.setStatus("mandatory")


class _ExpressGSEventLogDescr_Type(DisplayString):
    """Custom type expressGSEventLogDescr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_ExpressGSEventLogDescr_Type.__name__ = "DisplayString"
_ExpressGSEventLogDescr_Object = MibTableColumn
expressGSEventLogDescr = _ExpressGSEventLogDescr_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 13, 10, 3, 1, 1, 4),
    _ExpressGSEventLogDescr_Type()
)
expressGSEventLogDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    expressGSEventLogDescr.setStatus("mandatory")
_ExpressGSEventLogType_Type = EventCategory
_ExpressGSEventLogType_Object = MibTableColumn
expressGSEventLogType = _ExpressGSEventLogType_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 13, 10, 3, 1, 1, 5),
    _ExpressGSEventLogType_Type()
)
expressGSEventLogType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    expressGSEventLogType.setStatus("mandatory")


class _ExpressGSEventLogSeverity_Type(Integer32):
    """Custom type expressGSEventLogSeverity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_ExpressGSEventLogSeverity_Type.__name__ = "Integer32"
_ExpressGSEventLogSeverity_Object = MibTableColumn
expressGSEventLogSeverity = _ExpressGSEventLogSeverity_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 13, 10, 3, 1, 1, 6),
    _ExpressGSEventLogSeverity_Type()
)
expressGSEventLogSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    expressGSEventLogSeverity.setStatus("mandatory")


class _ExpressGSEventLogDTM_Type(DisplayString):
    """Custom type expressGSEventLogDTM based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(18, 18),
    )


_ExpressGSEventLogDTM_Type.__name__ = "DisplayString"
_ExpressGSEventLogDTM_Object = MibTableColumn
expressGSEventLogDTM = _ExpressGSEventLogDTM_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 13, 10, 3, 1, 1, 7),
    _ExpressGSEventLogDTM_Type()
)
expressGSEventLogDTM.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    expressGSEventLogDTM.setStatus("mandatory")
_ExpressGSEventLogResType_Type = ResourceType
_ExpressGSEventLogResType_Object = MibTableColumn
expressGSEventLogResType = _ExpressGSEventLogResType_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 13, 10, 3, 1, 1, 8),
    _ExpressGSEventLogResType_Type()
)
expressGSEventLogResType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    expressGSEventLogResType.setStatus("mandatory")
_ExpressGSEventLogResID_Type = ResourceId
_ExpressGSEventLogResID_Object = MibTableColumn
expressGSEventLogResID = _ExpressGSEventLogResID_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 13, 10, 3, 1, 1, 9),
    _ExpressGSEventLogResID_Type()
)
expressGSEventLogResID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    expressGSEventLogResID.setStatus("mandatory")
_ExpressGSEventLogResLeaf_Type = Integer32
_ExpressGSEventLogResLeaf_Object = MibTableColumn
expressGSEventLogResLeaf = _ExpressGSEventLogResLeaf_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 13, 10, 3, 1, 1, 10),
    _ExpressGSEventLogResLeaf_Type()
)
expressGSEventLogResLeaf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    expressGSEventLogResLeaf.setStatus("mandatory")
_ExpressGSEventLogValueType_Type = EventValueType
_ExpressGSEventLogValueType_Object = MibTableColumn
expressGSEventLogValueType = _ExpressGSEventLogValueType_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 13, 10, 3, 1, 1, 11),
    _ExpressGSEventLogValueType_Type()
)
expressGSEventLogValueType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    expressGSEventLogValueType.setStatus("mandatory")


class _ExpressGSEventLogValue_Type(OctetString):
    """Custom type expressGSEventLogValue based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_ExpressGSEventLogValue_Type.__name__ = "OctetString"
_ExpressGSEventLogValue_Object = MibTableColumn
expressGSEventLogValue = _ExpressGSEventLogValue_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 13, 10, 3, 1, 1, 12),
    _ExpressGSEventLogValue_Type()
)
expressGSEventLogValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    expressGSEventLogValue.setStatus("mandatory")
_ExpressGSEventLogEpochTime_Type = Integer32
_ExpressGSEventLogEpochTime_Object = MibTableColumn
expressGSEventLogEpochTime = _ExpressGSEventLogEpochTime_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 13, 10, 3, 1, 1, 13),
    _ExpressGSEventLogEpochTime_Type()
)
expressGSEventLogEpochTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    expressGSEventLogEpochTime.setStatus("mandatory")


class _ExpressGSEventLogID_Type(Integer32):
    """Custom type expressGSEventLogID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_ExpressGSEventLogID_Type.__name__ = "Integer32"
_ExpressGSEventLogID_Object = MibTableColumn
expressGSEventLogID = _ExpressGSEventLogID_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 13, 10, 3, 1, 1, 14),
    _ExpressGSEventLogID_Type()
)
expressGSEventLogID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    expressGSEventLogID.setStatus("mandatory")
_ExpressGSShutdownLogMgt_ObjectIdentity = ObjectIdentity
expressGSShutdownLogMgt = _ExpressGSShutdownLogMgt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 343, 6, 13, 10, 4)
)


class _ExpressGSShutdownLogTableMaxSize_Type(Integer32):
    """Custom type expressGSShutdownLogTableMaxSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_ExpressGSShutdownLogTableMaxSize_Type.__name__ = "Integer32"
_ExpressGSShutdownLogTableMaxSize_Object = MibScalar
expressGSShutdownLogTableMaxSize = _ExpressGSShutdownLogTableMaxSize_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 13, 10, 4, 1),
    _ExpressGSShutdownLogTableMaxSize_Type()
)
expressGSShutdownLogTableMaxSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    expressGSShutdownLogTableMaxSize.setStatus("mandatory")


class _ExpressGSShutdownLogLastEntry_Type(Integer32):
    """Custom type expressGSShutdownLogLastEntry based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_ExpressGSShutdownLogLastEntry_Type.__name__ = "Integer32"
_ExpressGSShutdownLogLastEntry_Object = MibScalar
expressGSShutdownLogLastEntry = _ExpressGSShutdownLogLastEntry_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 13, 10, 4, 2),
    _ExpressGSShutdownLogLastEntry_Type()
)
expressGSShutdownLogLastEntry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    expressGSShutdownLogLastEntry.setStatus("mandatory")


class _ExpressGSShutdownLogAcknowledged_Type(Integer32):
    """Custom type expressGSShutdownLogAcknowledged based on Integer32"""
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


_ExpressGSShutdownLogAcknowledged_Type.__name__ = "Integer32"
_ExpressGSShutdownLogAcknowledged_Object = MibScalar
expressGSShutdownLogAcknowledged = _ExpressGSShutdownLogAcknowledged_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 13, 10, 4, 3),
    _ExpressGSShutdownLogAcknowledged_Type()
)
expressGSShutdownLogAcknowledged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    expressGSShutdownLogAcknowledged.setStatus("mandatory")
_ExpressGSEventShutdownLog_ObjectIdentity = ObjectIdentity
expressGSEventShutdownLog = _ExpressGSEventShutdownLog_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 343, 6, 13, 10, 5)
)
_ExpressGSEventShutdownLogTable_Object = MibTable
expressGSEventShutdownLogTable = _ExpressGSEventShutdownLogTable_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 13, 10, 5, 1)
)
if mibBuilder.loadTexts:
    expressGSEventShutdownLogTable.setStatus("mandatory")
_ExpressGSEventShutdownLogEntry_Object = MibTableRow
expressGSEventShutdownLogEntry = _ExpressGSEventShutdownLogEntry_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 13, 10, 5, 1, 1)
)
expressGSEventShutdownLogEntry.setIndexNames(
    (0, "EXPRESSGS-MIB", "expressGSEventShutdownLogIndex"),
)
if mibBuilder.loadTexts:
    expressGSEventShutdownLogEntry.setStatus("mandatory")


class _ExpressGSEventShutdownLogEventIndex_Type(Integer32):
    """Custom type expressGSEventShutdownLogEventIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_ExpressGSEventShutdownLogEventIndex_Type.__name__ = "Integer32"
_ExpressGSEventShutdownLogEventIndex_Object = MibTableColumn
expressGSEventShutdownLogEventIndex = _ExpressGSEventShutdownLogEventIndex_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 13, 10, 5, 1, 1, 1),
    _ExpressGSEventShutdownLogEventIndex_Type()
)
expressGSEventShutdownLogEventIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    expressGSEventShutdownLogEventIndex.setStatus("mandatory")


class _ExpressGSEventShutdownLogIndex_Type(Integer32):
    """Custom type expressGSEventShutdownLogIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_ExpressGSEventShutdownLogIndex_Type.__name__ = "Integer32"
_ExpressGSEventShutdownLogIndex_Object = MibTableColumn
expressGSEventShutdownLogIndex = _ExpressGSEventShutdownLogIndex_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 13, 10, 5, 1, 1, 2),
    _ExpressGSEventShutdownLogIndex_Type()
)
expressGSEventShutdownLogIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    expressGSEventShutdownLogIndex.setStatus("mandatory")
_ExpressGSEventShutdownLogTime_Type = TimeTicks
_ExpressGSEventShutdownLogTime_Object = MibTableColumn
expressGSEventShutdownLogTime = _ExpressGSEventShutdownLogTime_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 13, 10, 5, 1, 1, 3),
    _ExpressGSEventShutdownLogTime_Type()
)
expressGSEventShutdownLogTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    expressGSEventShutdownLogTime.setStatus("mandatory")


class _ExpressGSEventShutdownLogDescr_Type(DisplayString):
    """Custom type expressGSEventShutdownLogDescr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_ExpressGSEventShutdownLogDescr_Type.__name__ = "DisplayString"
_ExpressGSEventShutdownLogDescr_Object = MibTableColumn
expressGSEventShutdownLogDescr = _ExpressGSEventShutdownLogDescr_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 13, 10, 5, 1, 1, 4),
    _ExpressGSEventShutdownLogDescr_Type()
)
expressGSEventShutdownLogDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    expressGSEventShutdownLogDescr.setStatus("mandatory")
_ExpressGSEventShutdownLogType_Type = EventCategory
_ExpressGSEventShutdownLogType_Object = MibTableColumn
expressGSEventShutdownLogType = _ExpressGSEventShutdownLogType_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 13, 10, 5, 1, 1, 5),
    _ExpressGSEventShutdownLogType_Type()
)
expressGSEventShutdownLogType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    expressGSEventShutdownLogType.setStatus("mandatory")


class _ExpressGSEventShutdownLogSeverity_Type(Integer32):
    """Custom type expressGSEventShutdownLogSeverity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_ExpressGSEventShutdownLogSeverity_Type.__name__ = "Integer32"
_ExpressGSEventShutdownLogSeverity_Object = MibTableColumn
expressGSEventShutdownLogSeverity = _ExpressGSEventShutdownLogSeverity_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 13, 10, 5, 1, 1, 6),
    _ExpressGSEventShutdownLogSeverity_Type()
)
expressGSEventShutdownLogSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    expressGSEventShutdownLogSeverity.setStatus("mandatory")


class _ExpressGSEventShutdownLogDTM_Type(DisplayString):
    """Custom type expressGSEventShutdownLogDTM based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(18, 18),
    )


_ExpressGSEventShutdownLogDTM_Type.__name__ = "DisplayString"
_ExpressGSEventShutdownLogDTM_Object = MibTableColumn
expressGSEventShutdownLogDTM = _ExpressGSEventShutdownLogDTM_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 13, 10, 5, 1, 1, 7),
    _ExpressGSEventShutdownLogDTM_Type()
)
expressGSEventShutdownLogDTM.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    expressGSEventShutdownLogDTM.setStatus("mandatory")
_ExpressGSEventShutdownLogResType_Type = ResourceType
_ExpressGSEventShutdownLogResType_Object = MibTableColumn
expressGSEventShutdownLogResType = _ExpressGSEventShutdownLogResType_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 13, 10, 5, 1, 1, 8),
    _ExpressGSEventShutdownLogResType_Type()
)
expressGSEventShutdownLogResType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    expressGSEventShutdownLogResType.setStatus("mandatory")
_ExpressGSEventShutdownLogResID_Type = ResourceId
_ExpressGSEventShutdownLogResID_Object = MibTableColumn
expressGSEventShutdownLogResID = _ExpressGSEventShutdownLogResID_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 13, 10, 5, 1, 1, 9),
    _ExpressGSEventShutdownLogResID_Type()
)
expressGSEventShutdownLogResID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    expressGSEventShutdownLogResID.setStatus("mandatory")
_ExpressGSEventShutdownLogResLeaf_Type = Integer32
_ExpressGSEventShutdownLogResLeaf_Object = MibTableColumn
expressGSEventShutdownLogResLeaf = _ExpressGSEventShutdownLogResLeaf_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 13, 10, 5, 1, 1, 10),
    _ExpressGSEventShutdownLogResLeaf_Type()
)
expressGSEventShutdownLogResLeaf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    expressGSEventShutdownLogResLeaf.setStatus("mandatory")
_ExpressGSEventShutdownLogValueType_Type = EventValueType
_ExpressGSEventShutdownLogValueType_Object = MibTableColumn
expressGSEventShutdownLogValueType = _ExpressGSEventShutdownLogValueType_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 13, 10, 5, 1, 1, 11),
    _ExpressGSEventShutdownLogValueType_Type()
)
expressGSEventShutdownLogValueType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    expressGSEventShutdownLogValueType.setStatus("mandatory")


class _ExpressGSEventShutdownLogValue_Type(OctetString):
    """Custom type expressGSEventShutdownLogValue based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_ExpressGSEventShutdownLogValue_Type.__name__ = "OctetString"
_ExpressGSEventShutdownLogValue_Object = MibTableColumn
expressGSEventShutdownLogValue = _ExpressGSEventShutdownLogValue_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 13, 10, 5, 1, 1, 12),
    _ExpressGSEventShutdownLogValue_Type()
)
expressGSEventShutdownLogValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    expressGSEventShutdownLogValue.setStatus("mandatory")
_ExpressGSEventShutdownLogEpochTime_Type = Integer32
_ExpressGSEventShutdownLogEpochTime_Object = MibTableColumn
expressGSEventShutdownLogEpochTime = _ExpressGSEventShutdownLogEpochTime_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 13, 10, 5, 1, 1, 13),
    _ExpressGSEventShutdownLogEpochTime_Type()
)
expressGSEventShutdownLogEpochTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    expressGSEventShutdownLogEpochTime.setStatus("mandatory")


class _ExpressGSEventShutdownLogID_Type(Integer32):
    """Custom type expressGSEventShutdownLogID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_ExpressGSEventShutdownLogID_Type.__name__ = "Integer32"
_ExpressGSEventShutdownLogID_Object = MibTableColumn
expressGSEventShutdownLogID = _ExpressGSEventShutdownLogID_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 13, 10, 5, 1, 1, 14),
    _ExpressGSEventShutdownLogID_Type()
)
expressGSEventShutdownLogID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    expressGSEventShutdownLogID.setStatus("mandatory")
_ExpressGSEventTrapMgmt_ObjectIdentity = ObjectIdentity
expressGSEventTrapMgmt = _ExpressGSEventTrapMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 343, 6, 13, 10, 6)
)


class _ExpressGSEventTrapEventIndex_Type(Integer32):
    """Custom type expressGSEventTrapEventIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_ExpressGSEventTrapEventIndex_Type.__name__ = "Integer32"
_ExpressGSEventTrapEventIndex_Object = MibScalar
expressGSEventTrapEventIndex = _ExpressGSEventTrapEventIndex_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 13, 10, 6, 1),
    _ExpressGSEventTrapEventIndex_Type()
)
expressGSEventTrapEventIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    expressGSEventTrapEventIndex.setStatus("mandatory")
_ExpressGSEventTrapTime_Type = TimeTicks
_ExpressGSEventTrapTime_Object = MibScalar
expressGSEventTrapTime = _ExpressGSEventTrapTime_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 13, 10, 6, 2),
    _ExpressGSEventTrapTime_Type()
)
expressGSEventTrapTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    expressGSEventTrapTime.setStatus("mandatory")


class _ExpressGSEventTrapDescr_Type(DisplayString):
    """Custom type expressGSEventTrapDescr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_ExpressGSEventTrapDescr_Type.__name__ = "DisplayString"
_ExpressGSEventTrapDescr_Object = MibScalar
expressGSEventTrapDescr = _ExpressGSEventTrapDescr_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 13, 10, 6, 3),
    _ExpressGSEventTrapDescr_Type()
)
expressGSEventTrapDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    expressGSEventTrapDescr.setStatus("mandatory")
_ExpressGSEventTrapType_Type = EventCategory
_ExpressGSEventTrapType_Object = MibScalar
expressGSEventTrapType = _ExpressGSEventTrapType_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 13, 10, 6, 4),
    _ExpressGSEventTrapType_Type()
)
expressGSEventTrapType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    expressGSEventTrapType.setStatus("mandatory")


class _ExpressGSEventTrapSeverity_Type(Integer32):
    """Custom type expressGSEventTrapSeverity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_ExpressGSEventTrapSeverity_Type.__name__ = "Integer32"
_ExpressGSEventTrapSeverity_Object = MibScalar
expressGSEventTrapSeverity = _ExpressGSEventTrapSeverity_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 13, 10, 6, 5),
    _ExpressGSEventTrapSeverity_Type()
)
expressGSEventTrapSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    expressGSEventTrapSeverity.setStatus("mandatory")


class _ExpressGSEventTrapDTM_Type(DisplayString):
    """Custom type expressGSEventTrapDTM based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(18, 18),
    )


_ExpressGSEventTrapDTM_Type.__name__ = "DisplayString"
_ExpressGSEventTrapDTM_Object = MibScalar
expressGSEventTrapDTM = _ExpressGSEventTrapDTM_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 13, 10, 6, 6),
    _ExpressGSEventTrapDTM_Type()
)
expressGSEventTrapDTM.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    expressGSEventTrapDTM.setStatus("mandatory")
_ExpressGSEventTrapResType_Type = ResourceType
_ExpressGSEventTrapResType_Object = MibScalar
expressGSEventTrapResType = _ExpressGSEventTrapResType_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 13, 10, 6, 7),
    _ExpressGSEventTrapResType_Type()
)
expressGSEventTrapResType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    expressGSEventTrapResType.setStatus("mandatory")
_ExpressGSEventTrapResID_Type = ResourceId
_ExpressGSEventTrapResID_Object = MibScalar
expressGSEventTrapResID = _ExpressGSEventTrapResID_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 13, 10, 6, 8),
    _ExpressGSEventTrapResID_Type()
)
expressGSEventTrapResID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    expressGSEventTrapResID.setStatus("mandatory")
_ExpressGSEventTrapResLeaf_Type = Integer32
_ExpressGSEventTrapResLeaf_Object = MibScalar
expressGSEventTrapResLeaf = _ExpressGSEventTrapResLeaf_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 13, 10, 6, 9),
    _ExpressGSEventTrapResLeaf_Type()
)
expressGSEventTrapResLeaf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    expressGSEventTrapResLeaf.setStatus("mandatory")
_ExpressGSEventTrapValueType_Type = EventValueType
_ExpressGSEventTrapValueType_Object = MibScalar
expressGSEventTrapValueType = _ExpressGSEventTrapValueType_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 13, 10, 6, 10),
    _ExpressGSEventTrapValueType_Type()
)
expressGSEventTrapValueType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    expressGSEventTrapValueType.setStatus("mandatory")


class _ExpressGSEventTrapValue_Type(OctetString):
    """Custom type expressGSEventTrapValue based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_ExpressGSEventTrapValue_Type.__name__ = "OctetString"
_ExpressGSEventTrapValue_Object = MibScalar
expressGSEventTrapValue = _ExpressGSEventTrapValue_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 13, 10, 6, 11),
    _ExpressGSEventTrapValue_Type()
)
expressGSEventTrapValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    expressGSEventTrapValue.setStatus("mandatory")
_ExpressGSEventTrapEpochTime_Type = Integer32
_ExpressGSEventTrapEpochTime_Object = MibScalar
expressGSEventTrapEpochTime = _ExpressGSEventTrapEpochTime_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 13, 10, 6, 12),
    _ExpressGSEventTrapEpochTime_Type()
)
expressGSEventTrapEpochTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    expressGSEventTrapEpochTime.setStatus("mandatory")


class _ExpressGSEventTrapID_Type(Integer32):
    """Custom type expressGSEventTrapID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_ExpressGSEventTrapID_Type.__name__ = "Integer32"
_ExpressGSEventTrapID_Object = MibScalar
expressGSEventTrapID = _ExpressGSEventTrapID_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 13, 10, 6, 13),
    _ExpressGSEventTrapID_Type()
)
expressGSEventTrapID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    expressGSEventTrapID.setStatus("mandatory")
_ExpressGSAlarmMgt_ObjectIdentity = ObjectIdentity
expressGSAlarmMgt = _ExpressGSAlarmMgt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 343, 6, 13, 11)
)
_ExpressGSAlarmGeneral_ObjectIdentity = ObjectIdentity
expressGSAlarmGeneral = _ExpressGSAlarmGeneral_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 343, 6, 13, 11, 1)
)
_ExpressGSAlarmGeneralActiveEntries_Type = Gauge32
_ExpressGSAlarmGeneralActiveEntries_Object = MibScalar
expressGSAlarmGeneralActiveEntries = _ExpressGSAlarmGeneralActiveEntries_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 13, 11, 1, 1),
    _ExpressGSAlarmGeneralActiveEntries_Type()
)
expressGSAlarmGeneralActiveEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    expressGSAlarmGeneralActiveEntries.setStatus("mandatory")
_ExpressGSAlarmGeneralTimeStamp_Type = TimeTicks
_ExpressGSAlarmGeneralTimeStamp_Object = MibScalar
expressGSAlarmGeneralTimeStamp = _ExpressGSAlarmGeneralTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 13, 11, 1, 2),
    _ExpressGSAlarmGeneralTimeStamp_Type()
)
expressGSAlarmGeneralTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    expressGSAlarmGeneralTimeStamp.setStatus("mandatory")
_ExpressGSAlarms_ObjectIdentity = ObjectIdentity
expressGSAlarms = _ExpressGSAlarms_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 343, 6, 13, 11, 2)
)
_ExpressGSActiveAlarmTable_Object = MibTable
expressGSActiveAlarmTable = _ExpressGSActiveAlarmTable_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 13, 11, 2, 2)
)
if mibBuilder.loadTexts:
    expressGSActiveAlarmTable.setStatus("mandatory")
_ExpressGSActiveAlarmEntry_Object = MibTableRow
expressGSActiveAlarmEntry = _ExpressGSActiveAlarmEntry_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 13, 11, 2, 2, 1)
)
expressGSActiveAlarmEntry.setIndexNames(
    (0, "EXPRESSGS-MIB", "expressGSActiveAlarmIndex"),
)
if mibBuilder.loadTexts:
    expressGSActiveAlarmEntry.setStatus("mandatory")
_ExpressGSActiveAlarmIndex_Type = Integer32
_ExpressGSActiveAlarmIndex_Object = MibTableColumn
expressGSActiveAlarmIndex = _ExpressGSActiveAlarmIndex_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 13, 11, 2, 2, 1, 1),
    _ExpressGSActiveAlarmIndex_Type()
)
expressGSActiveAlarmIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    expressGSActiveAlarmIndex.setStatus("mandatory")


class _ExpressGSActiveAlarmName_Type(DisplayString):
    """Custom type expressGSActiveAlarmName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_ExpressGSActiveAlarmName_Type.__name__ = "DisplayString"
_ExpressGSActiveAlarmName_Object = MibTableColumn
expressGSActiveAlarmName = _ExpressGSActiveAlarmName_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 13, 11, 2, 2, 1, 2),
    _ExpressGSActiveAlarmName_Type()
)
expressGSActiveAlarmName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    expressGSActiveAlarmName.setStatus("mandatory")
_ExpressGSActiveAlarmValueHigh_Type = Integer32
_ExpressGSActiveAlarmValueHigh_Object = MibTableColumn
expressGSActiveAlarmValueHigh = _ExpressGSActiveAlarmValueHigh_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 13, 11, 2, 2, 1, 3),
    _ExpressGSActiveAlarmValueHigh_Type()
)
expressGSActiveAlarmValueHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    expressGSActiveAlarmValueHigh.setStatus("mandatory")
_ExpressGSActiveAlarmValueLow_Type = Integer32
_ExpressGSActiveAlarmValueLow_Object = MibTableColumn
expressGSActiveAlarmValueLow = _ExpressGSActiveAlarmValueLow_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 13, 11, 2, 2, 1, 4),
    _ExpressGSActiveAlarmValueLow_Type()
)
expressGSActiveAlarmValueLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    expressGSActiveAlarmValueLow.setStatus("mandatory")
_ExpressGSActiveAlarmVariable_Type = ObjectIdentifier
_ExpressGSActiveAlarmVariable_Object = MibTableColumn
expressGSActiveAlarmVariable = _ExpressGSActiveAlarmVariable_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 13, 11, 2, 2, 1, 5),
    _ExpressGSActiveAlarmVariable_Type()
)
expressGSActiveAlarmVariable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    expressGSActiveAlarmVariable.setStatus("mandatory")
_ExpressGSActiveAlarmResType_Type = ResourceType
_ExpressGSActiveAlarmResType_Object = MibTableColumn
expressGSActiveAlarmResType = _ExpressGSActiveAlarmResType_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 13, 11, 2, 2, 1, 6),
    _ExpressGSActiveAlarmResType_Type()
)
expressGSActiveAlarmResType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    expressGSActiveAlarmResType.setStatus("mandatory")
_ExpressGSActiveAlarmResID_Type = ResourceId
_ExpressGSActiveAlarmResID_Object = MibTableColumn
expressGSActiveAlarmResID = _ExpressGSActiveAlarmResID_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 13, 11, 2, 2, 1, 7),
    _ExpressGSActiveAlarmResID_Type()
)
expressGSActiveAlarmResID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    expressGSActiveAlarmResID.setStatus("mandatory")
_ExpressGSActiveAlarmLeaf_Type = Integer32
_ExpressGSActiveAlarmLeaf_Object = MibTableColumn
expressGSActiveAlarmLeaf = _ExpressGSActiveAlarmLeaf_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 13, 11, 2, 2, 1, 8),
    _ExpressGSActiveAlarmLeaf_Type()
)
expressGSActiveAlarmLeaf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    expressGSActiveAlarmLeaf.setStatus("mandatory")


class _ExpressGSActiveAlarmOwner_Type(DisplayString):
    """Custom type expressGSActiveAlarmOwner based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_ExpressGSActiveAlarmOwner_Type.__name__ = "DisplayString"
_ExpressGSActiveAlarmOwner_Object = MibTableColumn
expressGSActiveAlarmOwner = _ExpressGSActiveAlarmOwner_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 13, 11, 2, 2, 1, 9),
    _ExpressGSActiveAlarmOwner_Type()
)
expressGSActiveAlarmOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    expressGSActiveAlarmOwner.setStatus("mandatory")
_ExpressGSSnmpTraps_ObjectIdentity = ObjectIdentity
expressGSSnmpTraps = _ExpressGSSnmpTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 343, 6, 13, 13)
)

# Managed Objects groups


# Notification objects

expressGSSystemTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 343, 6, 13, 13, 0, 2)
)
expressGSSystemTrap.setObjects(
      *(("EXPRESSGS-MIB", "expressGSEventTrapEventIndex"),
        ("EXPRESSGS-MIB", "expressGSEventTrapTime"),
        ("EXPRESSGS-MIB", "expressGSEventTrapDescr"),
        ("EXPRESSGS-MIB", "expressGSEventTrapType"),
        ("EXPRESSGS-MIB", "expressGSEventTrapSeverity"),
        ("EXPRESSGS-MIB", "expressGSEventTrapDTM"),
        ("EXPRESSGS-MIB", "expressGSEventTrapResType"),
        ("EXPRESSGS-MIB", "expressGSEventTrapResID"),
        ("EXPRESSGS-MIB", "expressGSEventTrapResLeaf"),
        ("EXPRESSGS-MIB", "expressGSEventTrapValueType"),
        ("EXPRESSGS-MIB", "expressGSEventTrapValue"),
        ("EXPRESSGS-MIB", "expressGSEventTrapEpochTime"),
        ("EXPRESSGS-MIB", "expressGSEventTrapID"))
)
if mibBuilder.loadTexts:
    expressGSSystemTrap.setStatus(
        ""
    )

expressGSConfigurationTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 343, 6, 13, 13, 0, 3)
)
expressGSConfigurationTrap.setObjects(
      *(("EXPRESSGS-MIB", "expressGSEventTrapEventIndex"),
        ("EXPRESSGS-MIB", "expressGSEventTrapTime"),
        ("EXPRESSGS-MIB", "expressGSEventTrapDescr"),
        ("EXPRESSGS-MIB", "expressGSEventTrapType"),
        ("EXPRESSGS-MIB", "expressGSEventTrapSeverity"),
        ("EXPRESSGS-MIB", "expressGSEventTrapDTM"),
        ("EXPRESSGS-MIB", "expressGSEventTrapResType"),
        ("EXPRESSGS-MIB", "expressGSEventTrapResID"),
        ("EXPRESSGS-MIB", "expressGSEventTrapResLeaf"),
        ("EXPRESSGS-MIB", "expressGSEventTrapValueType"),
        ("EXPRESSGS-MIB", "expressGSEventTrapValue"),
        ("EXPRESSGS-MIB", "expressGSEventTrapEpochTime"),
        ("EXPRESSGS-MIB", "expressGSEventTrapID"))
)
if mibBuilder.loadTexts:
    expressGSConfigurationTrap.setStatus(
        ""
    )

expressGSTemperatureTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 343, 6, 13, 13, 0, 4)
)
expressGSTemperatureTrap.setObjects(
      *(("EXPRESSGS-MIB", "expressGSEventTrapEventIndex"),
        ("EXPRESSGS-MIB", "expressGSEventTrapTime"),
        ("EXPRESSGS-MIB", "expressGSEventTrapDescr"),
        ("EXPRESSGS-MIB", "expressGSEventTrapType"),
        ("EXPRESSGS-MIB", "expressGSEventTrapSeverity"),
        ("EXPRESSGS-MIB", "expressGSEventTrapDTM"),
        ("EXPRESSGS-MIB", "expressGSEventTrapResType"),
        ("EXPRESSGS-MIB", "expressGSEventTrapResID"),
        ("EXPRESSGS-MIB", "expressGSEventTrapResLeaf"),
        ("EXPRESSGS-MIB", "expressGSEventTrapValueType"),
        ("EXPRESSGS-MIB", "expressGSEventTrapValue"),
        ("EXPRESSGS-MIB", "expressGSEventTrapEpochTime"),
        ("EXPRESSGS-MIB", "expressGSEventTrapID"))
)
if mibBuilder.loadTexts:
    expressGSTemperatureTrap.setStatus(
        ""
    )

expressGSResourceTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 343, 6, 13, 13, 0, 5)
)
expressGSResourceTrap.setObjects(
      *(("EXPRESSGS-MIB", "expressGSEventTrapEventIndex"),
        ("EXPRESSGS-MIB", "expressGSEventTrapTime"),
        ("EXPRESSGS-MIB", "expressGSEventTrapDescr"),
        ("EXPRESSGS-MIB", "expressGSEventTrapType"),
        ("EXPRESSGS-MIB", "expressGSEventTrapSeverity"),
        ("EXPRESSGS-MIB", "expressGSEventTrapDTM"),
        ("EXPRESSGS-MIB", "expressGSEventTrapResType"),
        ("EXPRESSGS-MIB", "expressGSEventTrapResID"),
        ("EXPRESSGS-MIB", "expressGSEventTrapResLeaf"),
        ("EXPRESSGS-MIB", "expressGSEventTrapValueType"),
        ("EXPRESSGS-MIB", "expressGSEventTrapValue"),
        ("EXPRESSGS-MIB", "expressGSEventTrapEpochTime"),
        ("EXPRESSGS-MIB", "expressGSEventTrapID"))
)
if mibBuilder.loadTexts:
    expressGSResourceTrap.setStatus(
        ""
    )

expressGSFanTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 343, 6, 13, 13, 0, 6)
)
expressGSFanTrap.setObjects(
      *(("EXPRESSGS-MIB", "expressGSEventTrapEventIndex"),
        ("EXPRESSGS-MIB", "expressGSEventTrapTime"),
        ("EXPRESSGS-MIB", "expressGSEventTrapDescr"),
        ("EXPRESSGS-MIB", "expressGSEventTrapType"),
        ("EXPRESSGS-MIB", "expressGSEventTrapSeverity"),
        ("EXPRESSGS-MIB", "expressGSEventTrapDTM"),
        ("EXPRESSGS-MIB", "expressGSEventTrapResType"),
        ("EXPRESSGS-MIB", "expressGSEventTrapResID"),
        ("EXPRESSGS-MIB", "expressGSEventTrapResLeaf"),
        ("EXPRESSGS-MIB", "expressGSEventTrapValueType"),
        ("EXPRESSGS-MIB", "expressGSEventTrapValue"),
        ("EXPRESSGS-MIB", "expressGSEventTrapEpochTime"),
        ("EXPRESSGS-MIB", "expressGSEventTrapID"))
)
if mibBuilder.loadTexts:
    expressGSFanTrap.setStatus(
        ""
    )

expressGSPowerTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 343, 6, 13, 13, 0, 9)
)
expressGSPowerTrap.setObjects(
      *(("EXPRESSGS-MIB", "expressGSEventTrapEventIndex"),
        ("EXPRESSGS-MIB", "expressGSEventTrapTime"),
        ("EXPRESSGS-MIB", "expressGSEventTrapDescr"),
        ("EXPRESSGS-MIB", "expressGSEventTrapType"),
        ("EXPRESSGS-MIB", "expressGSEventTrapSeverity"),
        ("EXPRESSGS-MIB", "expressGSEventTrapDTM"),
        ("EXPRESSGS-MIB", "expressGSEventTrapResType"),
        ("EXPRESSGS-MIB", "expressGSEventTrapResID"),
        ("EXPRESSGS-MIB", "expressGSEventTrapResLeaf"),
        ("EXPRESSGS-MIB", "expressGSEventTrapValueType"),
        ("EXPRESSGS-MIB", "expressGSEventTrapValue"),
        ("EXPRESSGS-MIB", "expressGSEventTrapEpochTime"),
        ("EXPRESSGS-MIB", "expressGSEventTrapID"))
)
if mibBuilder.loadTexts:
    expressGSPowerTrap.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "EXPRESSGS-MIB",
    **{"EventValueType": EventValueType,
       "ResourceType": ResourceType,
       "ResourceId": ResourceId,
       "DisplayString": DisplayString,
       "RowStatus": RowStatus,
       "MacAddress": MacAddress,
       "BridgeId": BridgeId,
       "Timeout": Timeout,
       "EventCategory": EventCategory,
       "intel": intel,
       "mib2ext": mib2ext,
       "esGigaSwitch": esGigaSwitch,
       "expressGSAgent": expressGSAgent,
       "expressGSAgentGen": expressGSAgentGen,
       "expressGSAgentMIBVersion": expressGSAgentMIBVersion,
       "expressGSAgentMgrIndex": expressGSAgentMgrIndex,
       "expressGSAgentCommunity": expressGSAgentCommunity,
       "expressGSCommunityTable": expressGSCommunityTable,
       "expressGSCommunityEntry": expressGSCommunityEntry,
       "expressGSCommunityIndex": expressGSCommunityIndex,
       "expressGSCommunityString": expressGSCommunityString,
       "expressGSCommunityAddressType": expressGSCommunityAddressType,
       "expressGSCommunityAddress": expressGSCommunityAddress,
       "expressGSCommunityAccess": expressGSCommunityAccess,
       "expressGSCommunityTrapReceiver": expressGSCommunityTrapReceiver,
       "expressGSCommunitySecurityLevel": expressGSCommunitySecurityLevel,
       "expressGSCommunityStatus": expressGSCommunityStatus,
       "expressGSAgentWeb": expressGSAgentWeb,
       "expressGSAgentWebServerURL": expressGSAgentWebServerURL,
       "expressGSAgentWebServerHelpDirectory": expressGSAgentWebServerHelpDirectory,
       "expressGSChassis": expressGSChassis,
       "expressGSChassisGen": expressGSChassisGen,
       "expressGSChassisType": expressGSChassisType,
       "expressGSChassisSlots": expressGSChassisSlots,
       "expressGSInventory": expressGSInventory,
       "expressGSInventoryTable": expressGSInventoryTable,
       "expressGSInventoryEntry": expressGSInventoryEntry,
       "expressGSInventoryResourceType": expressGSInventoryResourceType,
       "expressGSInventoryResourceIndex": expressGSInventoryResourceIndex,
       "expressGSInventoryModelNumber": expressGSInventoryModelNumber,
       "expressGSInventorySerialNumber": expressGSInventorySerialNumber,
       "expressGSInventoryVersion": expressGSInventoryVersion,
       "expressGSInventoryManufactureInfo": expressGSInventoryManufactureInfo,
       "expressGSInventoryScratchPad": expressGSInventoryScratchPad,
       "expressGSPowerSystems": expressGSPowerSystems,
       "expressGSPowerSupplies": expressGSPowerSupplies,
       "expressGSPowerSupplyTable": expressGSPowerSupplyTable,
       "expressGSPowerSupplyEntry": expressGSPowerSupplyEntry,
       "expressGSPowerSupplyIndex": expressGSPowerSupplyIndex,
       "expressGSPowerSupplyType": expressGSPowerSupplyType,
       "expressGSPowerSupplyStatus": expressGSPowerSupplyStatus,
       "expressGSPowerSupplyInputStatus": expressGSPowerSupplyInputStatus,
       "expressGSPowerSupplyOutputStatus": expressGSPowerSupplyOutputStatus,
       "expressGSPowerSupplyOutputCapacity": expressGSPowerSupplyOutputCapacity,
       "expressGSPowerMgmtGen": expressGSPowerMgmtGen,
       "expressGSPowerCapacity": expressGSPowerCapacity,
       "expressGSPowerUsed": expressGSPowerUsed,
       "expressGSPowerMgmtCtl": expressGSPowerMgmtCtl,
       "expressGSPowerControlTable": expressGSPowerControlTable,
       "expressGSPowerControlEntry": expressGSPowerControlEntry,
       "expressGSPowerControlUsed": expressGSPowerControlUsed,
       "expressGSPowerControlPriority": expressGSPowerControlPriority,
       "expressGSPowerControlMode": expressGSPowerControlMode,
       "expressGSTemperature": expressGSTemperature,
       "expressGSTempTable": expressGSTempTable,
       "expressGSTempEntry": expressGSTempEntry,
       "expressGSTempIndex": expressGSTempIndex,
       "expressGSTempValue": expressGSTempValue,
       "expressGSTempUpperLimit": expressGSTempUpperLimit,
       "expressGSTempUpperWarning": expressGSTempUpperWarning,
       "expressGSTempLowerWarning": expressGSTempLowerWarning,
       "expressGSTempLowerLimit": expressGSTempLowerLimit,
       "expressGSModules": expressGSModules,
       "expressGSModuleTable": expressGSModuleTable,
       "expressGSModuleEntry": expressGSModuleEntry,
       "expressGSModuleIndex": expressGSModuleIndex,
       "expressGSModuleName": expressGSModuleName,
       "expressGSModuleType": expressGSModuleType,
       "expressGSModuleBaseType": expressGSModuleBaseType,
       "expressGSModuleSlotWidth": expressGSModuleSlotWidth,
       "expressGSModuleSlotOffset": expressGSModuleSlotOffset,
       "expressGSModulePorts": expressGSModulePorts,
       "expressGSPorts": expressGSPorts,
       "expressGSPortMgt": expressGSPortMgt,
       "expressGSPortTable": expressGSPortTable,
       "expressGSPortEntry": expressGSPortEntry,
       "expressGSPortIndex": expressGSPortIndex,
       "expressGSPortName": expressGSPortName,
       "expressGSPortType": expressGSPortType,
       "expressGSPortBaseType": expressGSPortBaseType,
       "expressGSPortMode": expressGSPortMode,
       "expressGSPortStatus": expressGSPortStatus,
       "expressGSPortConnector": expressGSPortConnector,
       "expressGSPortSpeedState": expressGSPortSpeedState,
       "expressGSPortDuplexState": expressGSPortDuplexState,
       "expressGSPortGroupBinding": expressGSPortGroupBinding,
       "expressGSPortFlowControlMgt": expressGSPortFlowControlMgt,
       "expressGSPortFlowControlTable": expressGSPortFlowControlTable,
       "expressGSPortFlowControlEntry": expressGSPortFlowControlEntry,
       "expressGSPortFlowControlMode": expressGSPortFlowControlMode,
       "expressGSPortDuplexMgt": expressGSPortDuplexMgt,
       "expressGSPortDuplexTable": expressGSPortDuplexTable,
       "expressGSPortDuplexEntry": expressGSPortDuplexEntry,
       "expressGSPortDuplexMode": expressGSPortDuplexMode,
       "expressGSPortSpeedMgt": expressGSPortSpeedMgt,
       "expressGSPortSpeedTable": expressGSPortSpeedTable,
       "expressGSPortSpeedEntry": expressGSPortSpeedEntry,
       "expressGSPortSpeedMode": expressGSPortSpeedMode,
       "expressGSPortAutoNegotiationMgt": expressGSPortAutoNegotiationMgt,
       "expressGSPortAutoNegotiationTable": expressGSPortAutoNegotiationTable,
       "expressGSPortAutoNegotiationEntry": expressGSPortAutoNegotiationEntry,
       "expressGSPortAutoNegotiationMode": expressGSPortAutoNegotiationMode,
       "expressGSPortAutoNegotiationSpeedAdvertisement": expressGSPortAutoNegotiationSpeedAdvertisement,
       "expressGSPortAutoNegotiationDuplexAdvertisement": expressGSPortAutoNegotiationDuplexAdvertisement,
       "expressGSPortRateLimitMgt": expressGSPortRateLimitMgt,
       "expressGSPortRateLimitTable": expressGSPortRateLimitTable,
       "expressGSPortRateLimitEntry": expressGSPortRateLimitEntry,
       "expressGSPortRateLimitMode": expressGSPortRateLimitMode,
       "expressGSPortRateLimitRate": expressGSPortRateLimitRate,
       "expressGSPortRateLimitBurstSize": expressGSPortRateLimitBurstSize,
       "expressGSPortPacePriorityMgt": expressGSPortPacePriorityMgt,
       "expressGSPortPacePriorityTable": expressGSPortPacePriorityTable,
       "expressGSPortPacePriorityEntry": expressGSPortPacePriorityEntry,
       "expressGSPortPacePriorityMode": expressGSPortPacePriorityMode,
       "expressGSPortCategoryMgt": expressGSPortCategoryMgt,
       "expressGSPortCategoryTable": expressGSPortCategoryTable,
       "expressGSPortCategoryEntry": expressGSPortCategoryEntry,
       "expressGSPortCategoryMode": expressGSPortCategoryMode,
       "expressGSBufferMgt": expressGSBufferMgt,
       "expressGSBufferTable": expressGSBufferTable,
       "expressGSBufferEntry": expressGSBufferEntry,
       "expressGSBufferIndex": expressGSBufferIndex,
       "expressGSBufferFabricPort": expressGSBufferFabricPort,
       "expressGSBufferFabricPortDirection": expressGSBufferFabricPortDirection,
       "expressGSBufferSwitchPort": expressGSBufferSwitchPort,
       "expressGSBufferMemory": expressGSBufferMemory,
       "expressGSBufferAgeTimer": expressGSBufferAgeTimer,
       "expressGSBufferPriorityServicing": expressGSBufferPriorityServicing,
       "expressGSBufferPriorityAllocation": expressGSBufferPriorityAllocation,
       "expressGSBufferPriorityThreshold": expressGSBufferPriorityThreshold,
       "expressGSBufferCongestion": expressGSBufferCongestion,
       "expressGSBufferHighOverflowDrops": expressGSBufferHighOverflowDrops,
       "expressGSBufferLowOverflowDrops": expressGSBufferLowOverflowDrops,
       "expressGSBufferHighStaleDrops": expressGSBufferHighStaleDrops,
       "expressGSBufferLowStaleDrops": expressGSBufferLowStaleDrops,
       "expressGSBufferCongestionDrops": expressGSBufferCongestionDrops,
       "expressGSSwitching": expressGSSwitching,
       "expressGSSwitchingLayerII": expressGSSwitchingLayerII,
       "expressGSSwitchGen": expressGSSwitchGen,
       "expressGSSwitchSTPConfig": expressGSSwitchSTPConfig,
       "expressGSSwitchAgingTime": expressGSSwitchAgingTime,
       "expressGSSwitchSuperAgingTime": expressGSSwitchSuperAgingTime,
       "expressGSBridgeMgmt": expressGSBridgeMgmt,
       "expressGSBridgeTable": expressGSBridgeTable,
       "expressGSBridgeEntry": expressGSBridgeEntry,
       "expressGSBridgeIndex": expressGSBridgeIndex,
       "expressGSBridgeType": expressGSBridgeType,
       "expressGSBridgeMode": expressGSBridgeMode,
       "expressGSBridgeStatus": expressGSBridgeStatus,
       "expressGSBridgeStpPriority": expressGSBridgeStpPriority,
       "expressGSBridgeStpTimeSinceTopologyChange": expressGSBridgeStpTimeSinceTopologyChange,
       "expressGSBridgeStpTopChanges": expressGSBridgeStpTopChanges,
       "expressGSBridgeStpDesignatedRoot": expressGSBridgeStpDesignatedRoot,
       "expressGSBridgeStpRootCost": expressGSBridgeStpRootCost,
       "expressGSBridgeStpRootPort": expressGSBridgeStpRootPort,
       "expressGSBridgeStpMaxAge": expressGSBridgeStpMaxAge,
       "expressGSBridgeStpHelloTime": expressGSBridgeStpHelloTime,
       "expressGSBridgeStpHoldTime": expressGSBridgeStpHoldTime,
       "expressGSBridgeStpForwardDelay": expressGSBridgeStpForwardDelay,
       "expressGSBridgeStpBridgeMaxAge": expressGSBridgeStpBridgeMaxAge,
       "expressGSBridgeStpBridgeHelloTime": expressGSBridgeStpBridgeHelloTime,
       "expressGSBridgeStpBridgeForwardDelay": expressGSBridgeStpBridgeForwardDelay,
       "expressGSBridgePortMgmt": expressGSBridgePortMgmt,
       "expressGSBridgePortTable": expressGSBridgePortTable,
       "expressGSBridgePortEntry": expressGSBridgePortEntry,
       "expressGSBridgePortIndex": expressGSBridgePortIndex,
       "expressGSBridgePortPriority": expressGSBridgePortPriority,
       "expressGSBridgePortState": expressGSBridgePortState,
       "expressGSBridgePortEnable": expressGSBridgePortEnable,
       "expressGSBridgePortPathCost": expressGSBridgePortPathCost,
       "expressGSBridgePortDesignatedRoot": expressGSBridgePortDesignatedRoot,
       "expressGSBridgePortDesignatedCost": expressGSBridgePortDesignatedCost,
       "expressGSBridgePortDesignatedBridge": expressGSBridgePortDesignatedBridge,
       "expressGSBridgePortDesignatedPort": expressGSBridgePortDesignatedPort,
       "expressGSBridgePortForwardTransitions": expressGSBridgePortForwardTransitions,
       "expressGSBridgePortFastStart": expressGSBridgePortFastStart,
       "expressGSBridgePortSetDefault": expressGSBridgePortSetDefault,
       "expressGSBridgePortEnableChangeDetection": expressGSBridgePortEnableChangeDetection,
       "expressGSL2AddrMgmt": expressGSL2AddrMgmt,
       "expressGSL2AddrDatabaseMgt": expressGSL2AddrDatabaseMgt,
       "expressGSL2AddressTable": expressGSL2AddressTable,
       "expressGSL2AddressEntry": expressGSL2AddressEntry,
       "expressGSL2AddressIndex": expressGSL2AddressIndex,
       "expressGSL2AddressTableIndex": expressGSL2AddressTableIndex,
       "expressGSL2AddressMacAddress": expressGSL2AddressMacAddress,
       "expressGSL2AddressPortBinding": expressGSL2AddressPortBinding,
       "expressGSL2AddressBindingValid": expressGSL2AddressBindingValid,
       "expressGSL2AddressVlanID": expressGSL2AddressVlanID,
       "expressGSL2AddressPriority": expressGSL2AddressPriority,
       "expressGSL2AddressForward": expressGSL2AddressForward,
       "expressGSL2AddressCopy": expressGSL2AddressCopy,
       "expressGSL2AddressPersistence": expressGSL2AddressPersistence,
       "expressGSL2AddressStatus": expressGSL2AddressStatus,
       "expressGSL2AddrSummaryMgt": expressGSL2AddrSummaryMgt,
       "expressGSL2AddrSummaryTable": expressGSL2AddrSummaryTable,
       "expressGSL2AddrSummaryEntry": expressGSL2AddrSummaryEntry,
       "expressGSL2AddrSummary": expressGSL2AddrSummary,
       "expressGSL2AddrControlMgt": expressGSL2AddrControlMgt,
       "expressGSL2AddressControlTable": expressGSL2AddressControlTable,
       "expressGSL2AddressControlEntry": expressGSL2AddressControlEntry,
       "expressGSL2AddressControlIndex": expressGSL2AddressControlIndex,
       "expressGSL2AddressControlMacAddress": expressGSL2AddressControlMacAddress,
       "expressGSL2AddressControlPortBinding": expressGSL2AddressControlPortBinding,
       "expressGSL2AddressControlVlanID": expressGSL2AddressControlVlanID,
       "expressGSL2AddressControlPriority": expressGSL2AddressControlPriority,
       "expressGSL2AddressControlPersistence": expressGSL2AddressControlPersistence,
       "expressGSL2AddressControlStatus": expressGSL2AddressControlStatus,
       "expressGSL2AddrChangeMgt": expressGSL2AddrChangeMgt,
       "expressGSL2AddressChangeLast": expressGSL2AddressChangeLast,
       "expressGSL2AddressChangeWraps": expressGSL2AddressChangeWraps,
       "expressGSL2AddressChangeMaxEntries": expressGSL2AddressChangeMaxEntries,
       "expressGSL2AddressChangeTable": expressGSL2AddressChangeTable,
       "expressGSL2AddressChangeEntry": expressGSL2AddressChangeEntry,
       "expressGSL2AddressChangeWrapCount": expressGSL2AddressChangeWrapCount,
       "expressGSL2AddressChangeIndex": expressGSL2AddressChangeIndex,
       "expressGSL2AddressChangeIndexChanged": expressGSL2AddressChangeIndexChanged,
       "expressGSL2AddressChangeSummary": expressGSL2AddressChangeSummary,
       "expressGSSwitchPortMgt": expressGSSwitchPortMgt,
       "expressGSSwitchPortTable": expressGSSwitchPortTable,
       "expressGSSwitchPortEntry": expressGSSwitchPortEntry,
       "expressGSSwitchPortIndex": expressGSSwitchPortIndex,
       "expressGSSwitchPortSTAPMode": expressGSSwitchPortSTAPMode,
       "expressGSSwitchPortConvertToStatic": expressGSSwitchPortConvertToStatic,
       "expressGSSwitchPortLearningMode": expressGSSwitchPortLearningMode,
       "expressGSSwitchPortHuntGroup": expressGSSwitchPortHuntGroup,
       "expressGSSwitchPortPhysicalPort": expressGSSwitchPortPhysicalPort,
       "expressGSSwitchPortKnownMode": expressGSSwitchPortKnownMode,
       "expressGSSwitchPortMappingMethod": expressGSSwitchPortMappingMethod,
       "expressGSSwitchPortTrunkingMode": expressGSSwitchPortTrunkingMode,
       "expressGSSwitchPortVlanBindingMethod": expressGSSwitchPortVlanBindingMethod,
       "expressGSSwitchPortIgnoreTag": expressGSSwitchPortIgnoreTag,
       "expressGSSwitchPortVlanID": expressGSSwitchPortVlanID,
       "expressGSSwitchPort3ComMappingTableIndex": expressGSSwitchPort3ComMappingTableIndex,
       "expressGSSwitchPortAutoVlanCreation": expressGSSwitchPortAutoVlanCreation,
       "expressGSSwitchPortMirrorMode": expressGSSwitchPortMirrorMode,
       "expressGSSwitchPortIfIndex": expressGSSwitchPortIfIndex,
       "expressGSSwitchPortFastStart": expressGSSwitchPortFastStart,
       "expressGSHuntGroupMgt": expressGSHuntGroupMgt,
       "expressGSHuntGroupTable": expressGSHuntGroupTable,
       "expressGSHuntGroupEntry": expressGSHuntGroupEntry,
       "expressGSHuntGroupIndex": expressGSHuntGroupIndex,
       "expressGSHuntGroupName": expressGSHuntGroupName,
       "expressGSHuntGroupBasePort": expressGSHuntGroupBasePort,
       "expressGSHuntGroupNumberOfPorts": expressGSHuntGroupNumberOfPorts,
       "expressGSHuntGroupLoadSharing": expressGSHuntGroupLoadSharing,
       "expressGSHuntGroupStatus": expressGSHuntGroupStatus,
       "expressGSPortMirroringMgt": expressGSPortMirroringMgt,
       "expressGSPortMirroringTable": expressGSPortMirroringTable,
       "expressGSPortMirroringEntry": expressGSPortMirroringEntry,
       "expressGSPortMirroringIndex": expressGSPortMirroringIndex,
       "expressGSPortMirroringSourceSubPort": expressGSPortMirroringSourceSubPort,
       "expressGSPortMirroringSamplerType": expressGSPortMirroringSamplerType,
       "expressGSPortMirroringRate": expressGSPortMirroringRate,
       "expressGSPortMirroringMirrorPort": expressGSPortMirroringMirrorPort,
       "expressGSVlanMgt": expressGSVlanMgt,
       "expressGSVlans": expressGSVlans,
       "expressGSVlanTable": expressGSVlanTable,
       "expressGSVlanEntry": expressGSVlanEntry,
       "expressGSVlanID": expressGSVlanID,
       "expressGSVlanName": expressGSVlanName,
       "expressGSVlanIfIndex": expressGSVlanIfIndex,
       "expressGSVlanAFTIndex": expressGSVlanAFTIndex,
       "expressGSVlanBridgeIndex": expressGSVlanBridgeIndex,
       "expressGSVlanStatus": expressGSVlanStatus,
       "expressGSVlanInitialHashTableSize": expressGSVlanInitialHashTableSize,
       "expressGSVlanAutoIncrementHTSize": expressGSVlanAutoIncrementHTSize,
       "expressGSVlanMappings": expressGSVlanMappings,
       "expressGS3ComMapping": expressGS3ComMapping,
       "expressGS3ComMappingTable": expressGS3ComMappingTable,
       "expressGS3ComMappingEntry": expressGS3ComMappingEntry,
       "expressGS3ComMappingTableIndex": expressGS3ComMappingTableIndex,
       "expressGS3ComMappingTableName": expressGS3ComMappingTableName,
       "expressGS3ComMappingTableStatus": expressGS3ComMappingTableStatus,
       "expressGSVlan3ComMapping": expressGSVlan3ComMapping,
       "expressGSVlan3ComMappingTable": expressGSVlan3ComMappingTable,
       "expressGSVlan3ComMappingEntry": expressGSVlan3ComMappingEntry,
       "expressGSVlan3ComMappingIndex": expressGSVlan3ComMappingIndex,
       "expressGSVlan3ComMappingVlanID": expressGSVlan3ComMappingVlanID,
       "expressGSVlan3ComMappingStatus": expressGSVlan3ComMappingStatus,
       "expressGSVirtualPorts": expressGSVirtualPorts,
       "expressGSVirtualSwitchPortTable": expressGSVirtualSwitchPortTable,
       "expressGSVirtualSwitchPortEntry": expressGSVirtualSwitchPortEntry,
       "expressGSVirtualSwitchPortIndex": expressGSVirtualSwitchPortIndex,
       "expressGSVirtualSwitchPortFormat": expressGSVirtualSwitchPortFormat,
       "expressGSVirtualSwitchPortBridgePort": expressGSVirtualSwitchPortBridgePort,
       "expressGSVirtualSwitchPortBindingType": expressGSVirtualSwitchPortBindingType,
       "expressGSVirtualSwitchPortStatus": expressGSVirtualSwitchPortStatus,
       "expressGSEvents": expressGSEvents,
       "expressGSEventMgt": expressGSEventMgt,
       "expressGSEventTable": expressGSEventTable,
       "expressGSEventEntry": expressGSEventEntry,
       "expressGSEventIndex": expressGSEventIndex,
       "expressGSEventMode": expressGSEventMode,
       "expressGSEventLogAction": expressGSEventLogAction,
       "expressGSEventTrapAction": expressGSEventTrapAction,
       "expressGSEventConsoleAction": expressGSEventConsoleAction,
       "expressGSEventLogMgt": expressGSEventLogMgt,
       "expressGSLogTableMaxSize": expressGSLogTableMaxSize,
       "expressGSLogLastEntry": expressGSLogLastEntry,
       "expressGSLogWraps": expressGSLogWraps,
       "expressGSEventLog": expressGSEventLog,
       "expressGSEventLogTable": expressGSEventLogTable,
       "expressGSEventLogEntry": expressGSEventLogEntry,
       "expressGSEventLogEventIndex": expressGSEventLogEventIndex,
       "expressGSEventLogIndex": expressGSEventLogIndex,
       "expressGSEventLogTime": expressGSEventLogTime,
       "expressGSEventLogDescr": expressGSEventLogDescr,
       "expressGSEventLogType": expressGSEventLogType,
       "expressGSEventLogSeverity": expressGSEventLogSeverity,
       "expressGSEventLogDTM": expressGSEventLogDTM,
       "expressGSEventLogResType": expressGSEventLogResType,
       "expressGSEventLogResID": expressGSEventLogResID,
       "expressGSEventLogResLeaf": expressGSEventLogResLeaf,
       "expressGSEventLogValueType": expressGSEventLogValueType,
       "expressGSEventLogValue": expressGSEventLogValue,
       "expressGSEventLogEpochTime": expressGSEventLogEpochTime,
       "expressGSEventLogID": expressGSEventLogID,
       "expressGSShutdownLogMgt": expressGSShutdownLogMgt,
       "expressGSShutdownLogTableMaxSize": expressGSShutdownLogTableMaxSize,
       "expressGSShutdownLogLastEntry": expressGSShutdownLogLastEntry,
       "expressGSShutdownLogAcknowledged": expressGSShutdownLogAcknowledged,
       "expressGSEventShutdownLog": expressGSEventShutdownLog,
       "expressGSEventShutdownLogTable": expressGSEventShutdownLogTable,
       "expressGSEventShutdownLogEntry": expressGSEventShutdownLogEntry,
       "expressGSEventShutdownLogEventIndex": expressGSEventShutdownLogEventIndex,
       "expressGSEventShutdownLogIndex": expressGSEventShutdownLogIndex,
       "expressGSEventShutdownLogTime": expressGSEventShutdownLogTime,
       "expressGSEventShutdownLogDescr": expressGSEventShutdownLogDescr,
       "expressGSEventShutdownLogType": expressGSEventShutdownLogType,
       "expressGSEventShutdownLogSeverity": expressGSEventShutdownLogSeverity,
       "expressGSEventShutdownLogDTM": expressGSEventShutdownLogDTM,
       "expressGSEventShutdownLogResType": expressGSEventShutdownLogResType,
       "expressGSEventShutdownLogResID": expressGSEventShutdownLogResID,
       "expressGSEventShutdownLogResLeaf": expressGSEventShutdownLogResLeaf,
       "expressGSEventShutdownLogValueType": expressGSEventShutdownLogValueType,
       "expressGSEventShutdownLogValue": expressGSEventShutdownLogValue,
       "expressGSEventShutdownLogEpochTime": expressGSEventShutdownLogEpochTime,
       "expressGSEventShutdownLogID": expressGSEventShutdownLogID,
       "expressGSEventTrapMgmt": expressGSEventTrapMgmt,
       "expressGSEventTrapEventIndex": expressGSEventTrapEventIndex,
       "expressGSEventTrapTime": expressGSEventTrapTime,
       "expressGSEventTrapDescr": expressGSEventTrapDescr,
       "expressGSEventTrapType": expressGSEventTrapType,
       "expressGSEventTrapSeverity": expressGSEventTrapSeverity,
       "expressGSEventTrapDTM": expressGSEventTrapDTM,
       "expressGSEventTrapResType": expressGSEventTrapResType,
       "expressGSEventTrapResID": expressGSEventTrapResID,
       "expressGSEventTrapResLeaf": expressGSEventTrapResLeaf,
       "expressGSEventTrapValueType": expressGSEventTrapValueType,
       "expressGSEventTrapValue": expressGSEventTrapValue,
       "expressGSEventTrapEpochTime": expressGSEventTrapEpochTime,
       "expressGSEventTrapID": expressGSEventTrapID,
       "expressGSAlarmMgt": expressGSAlarmMgt,
       "expressGSAlarmGeneral": expressGSAlarmGeneral,
       "expressGSAlarmGeneralActiveEntries": expressGSAlarmGeneralActiveEntries,
       "expressGSAlarmGeneralTimeStamp": expressGSAlarmGeneralTimeStamp,
       "expressGSAlarms": expressGSAlarms,
       "expressGSActiveAlarmTable": expressGSActiveAlarmTable,
       "expressGSActiveAlarmEntry": expressGSActiveAlarmEntry,
       "expressGSActiveAlarmIndex": expressGSActiveAlarmIndex,
       "expressGSActiveAlarmName": expressGSActiveAlarmName,
       "expressGSActiveAlarmValueHigh": expressGSActiveAlarmValueHigh,
       "expressGSActiveAlarmValueLow": expressGSActiveAlarmValueLow,
       "expressGSActiveAlarmVariable": expressGSActiveAlarmVariable,
       "expressGSActiveAlarmResType": expressGSActiveAlarmResType,
       "expressGSActiveAlarmResID": expressGSActiveAlarmResID,
       "expressGSActiveAlarmLeaf": expressGSActiveAlarmLeaf,
       "expressGSActiveAlarmOwner": expressGSActiveAlarmOwner,
       "expressGSSnmpTraps": expressGSSnmpTraps,
       "expressGSSystemTrap": expressGSSystemTrap,
       "expressGSConfigurationTrap": expressGSConfigurationTrap,
       "expressGSTemperatureTrap": expressGSTemperatureTrap,
       "expressGSResourceTrap": expressGSResourceTrap,
       "expressGSFanTrap": expressGSFanTrap,
       "expressGSPowerTrap": expressGSPowerTrap}
)
