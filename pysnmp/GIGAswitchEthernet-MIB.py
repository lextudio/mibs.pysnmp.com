# SNMP MIB module (GIGAswitchEthernet-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/GIGAswitchEthernet-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:48:40 2024
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

_Dec_ObjectIdentity = ObjectIdentity
dec = _Dec_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 36)
)
_Ema_ObjectIdentity = ObjectIdentity
ema = _Ema_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 36, 2)
)
_Mib_extensions_1_ObjectIdentity = ObjectIdentity
mib_extensions_1 = _Mib_extensions_1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 36, 2, 18)
)
_GsEMIB_ObjectIdentity = ObjectIdentity
gsEMIB = _GsEMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 39)
)
_GsEAgent_ObjectIdentity = ObjectIdentity
gsEAgent = _GsEAgent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 39, 1)
)
_GsEAgentGen_ObjectIdentity = ObjectIdentity
gsEAgentGen = _GsEAgentGen_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 39, 1, 1)
)


class _GsEAgentMIBVersion_Type(DisplayString):
    """Custom type gsEAgentMIBVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_GsEAgentMIBVersion_Type.__name__ = "DisplayString"
_GsEAgentMIBVersion_Object = MibScalar
gsEAgentMIBVersion = _GsEAgentMIBVersion_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 39, 1, 1, 1),
    _GsEAgentMIBVersion_Type()
)
gsEAgentMIBVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gsEAgentMIBVersion.setStatus("mandatory")
_GsEAgentMgrIndex_Type = Integer32
_GsEAgentMgrIndex_Object = MibScalar
gsEAgentMgrIndex = _GsEAgentMgrIndex_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 39, 1, 1, 2),
    _GsEAgentMgrIndex_Type()
)
gsEAgentMgrIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gsEAgentMgrIndex.setStatus("mandatory")
_GsEAgentCommunity_ObjectIdentity = ObjectIdentity
gsEAgentCommunity = _GsEAgentCommunity_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 39, 1, 2)
)
_GsECommunityTable_Object = MibTable
gsECommunityTable = _GsECommunityTable_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 39, 1, 2, 1)
)
if mibBuilder.loadTexts:
    gsECommunityTable.setStatus("mandatory")
_GsECommunityEntry_Object = MibTableRow
gsECommunityEntry = _GsECommunityEntry_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 39, 1, 2, 1, 1)
)
gsECommunityEntry.setIndexNames(
    (0, "GIGAswitchEthernet-MIB", "gsECommunityIndex"),
)
if mibBuilder.loadTexts:
    gsECommunityEntry.setStatus("mandatory")
_GsECommunityIndex_Type = Integer32
_GsECommunityIndex_Object = MibTableColumn
gsECommunityIndex = _GsECommunityIndex_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 39, 1, 2, 1, 1, 1),
    _GsECommunityIndex_Type()
)
gsECommunityIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gsECommunityIndex.setStatus("mandatory")


class _GsECommunityString_Type(DisplayString):
    """Custom type gsECommunityString based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_GsECommunityString_Type.__name__ = "DisplayString"
_GsECommunityString_Object = MibTableColumn
gsECommunityString = _GsECommunityString_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 39, 1, 2, 1, 1, 2),
    _GsECommunityString_Type()
)
gsECommunityString.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gsECommunityString.setStatus("mandatory")


class _GsECommunityAddressType_Type(Integer32):
    """Custom type gsECommunityAddressType based on Integer32"""
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


_GsECommunityAddressType_Type.__name__ = "Integer32"
_GsECommunityAddressType_Object = MibTableColumn
gsECommunityAddressType = _GsECommunityAddressType_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 39, 1, 2, 1, 1, 3),
    _GsECommunityAddressType_Type()
)
gsECommunityAddressType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gsECommunityAddressType.setStatus("mandatory")
_GsECommunityAddress_Type = IpAddress
_GsECommunityAddress_Object = MibTableColumn
gsECommunityAddress = _GsECommunityAddress_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 39, 1, 2, 1, 1, 4),
    _GsECommunityAddress_Type()
)
gsECommunityAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gsECommunityAddress.setStatus("mandatory")


class _GsECommunityAccess_Type(Integer32):
    """Custom type gsECommunityAccess based on Integer32"""
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


_GsECommunityAccess_Type.__name__ = "Integer32"
_GsECommunityAccess_Object = MibTableColumn
gsECommunityAccess = _GsECommunityAccess_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 39, 1, 2, 1, 1, 5),
    _GsECommunityAccess_Type()
)
gsECommunityAccess.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gsECommunityAccess.setStatus("mandatory")


class _GsECommunityTrapReceiver_Type(Integer32):
    """Custom type gsECommunityTrapReceiver based on Integer32"""
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


_GsECommunityTrapReceiver_Type.__name__ = "Integer32"
_GsECommunityTrapReceiver_Object = MibTableColumn
gsECommunityTrapReceiver = _GsECommunityTrapReceiver_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 39, 1, 2, 1, 1, 6),
    _GsECommunityTrapReceiver_Type()
)
gsECommunityTrapReceiver.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gsECommunityTrapReceiver.setStatus("mandatory")


class _GsECommunitySecurityLevel_Type(Integer32):
    """Custom type gsECommunitySecurityLevel based on Integer32"""
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


_GsECommunitySecurityLevel_Type.__name__ = "Integer32"
_GsECommunitySecurityLevel_Object = MibTableColumn
gsECommunitySecurityLevel = _GsECommunitySecurityLevel_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 39, 1, 2, 1, 1, 7),
    _GsECommunitySecurityLevel_Type()
)
gsECommunitySecurityLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gsECommunitySecurityLevel.setStatus("mandatory")
_GsECommunityStatus_Type = RowStatus
_GsECommunityStatus_Object = MibTableColumn
gsECommunityStatus = _GsECommunityStatus_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 39, 1, 2, 1, 1, 8),
    _GsECommunityStatus_Type()
)
gsECommunityStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gsECommunityStatus.setStatus("mandatory")
_GsEAgentWeb_ObjectIdentity = ObjectIdentity
gsEAgentWeb = _GsEAgentWeb_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 39, 1, 3)
)


class _GsEAgentWebServerURL_Type(DisplayString):
    """Custom type gsEAgentWebServerURL based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_GsEAgentWebServerURL_Type.__name__ = "DisplayString"
_GsEAgentWebServerURL_Object = MibScalar
gsEAgentWebServerURL = _GsEAgentWebServerURL_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 39, 1, 3, 1),
    _GsEAgentWebServerURL_Type()
)
gsEAgentWebServerURL.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gsEAgentWebServerURL.setStatus("mandatory")


class _GsEAgentWebServerHelpDirectory_Type(DisplayString):
    """Custom type gsEAgentWebServerHelpDirectory based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_GsEAgentWebServerHelpDirectory_Type.__name__ = "DisplayString"
_GsEAgentWebServerHelpDirectory_Object = MibScalar
gsEAgentWebServerHelpDirectory = _GsEAgentWebServerHelpDirectory_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 39, 1, 3, 2),
    _GsEAgentWebServerHelpDirectory_Type()
)
gsEAgentWebServerHelpDirectory.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gsEAgentWebServerHelpDirectory.setStatus("mandatory")
_GsEChassis_ObjectIdentity = ObjectIdentity
gsEChassis = _GsEChassis_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 39, 3)
)
_GsEChassisGen_ObjectIdentity = ObjectIdentity
gsEChassisGen = _GsEChassisGen_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 39, 3, 1)
)


class _GsEChassisType_Type(Integer32):
    """Custom type gsEChassisType based on Integer32"""
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


_GsEChassisType_Type.__name__ = "Integer32"
_GsEChassisType_Object = MibScalar
gsEChassisType = _GsEChassisType_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 39, 3, 1, 1),
    _GsEChassisType_Type()
)
gsEChassisType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gsEChassisType.setStatus("mandatory")
_GsEChassisSlots_Type = Integer32
_GsEChassisSlots_Object = MibScalar
gsEChassisSlots = _GsEChassisSlots_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 39, 3, 1, 2),
    _GsEChassisSlots_Type()
)
gsEChassisSlots.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gsEChassisSlots.setStatus("mandatory")
_GsEInventory_ObjectIdentity = ObjectIdentity
gsEInventory = _GsEInventory_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 39, 3, 2)
)
_GsEInventoryTable_Object = MibTable
gsEInventoryTable = _GsEInventoryTable_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 39, 3, 2, 1)
)
if mibBuilder.loadTexts:
    gsEInventoryTable.setStatus("mandatory")
_GsEInventoryEntry_Object = MibTableRow
gsEInventoryEntry = _GsEInventoryEntry_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 39, 3, 2, 1, 1)
)
gsEInventoryEntry.setIndexNames(
    (0, "GIGAswitchEthernet-MIB", "gsEInventoryResourceType"),
    (0, "GIGAswitchEthernet-MIB", "gsEInventoryResourceIndex"),
)
if mibBuilder.loadTexts:
    gsEInventoryEntry.setStatus("mandatory")
_GsEInventoryResourceType_Type = ResourceType
_GsEInventoryResourceType_Object = MibTableColumn
gsEInventoryResourceType = _GsEInventoryResourceType_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 39, 3, 2, 1, 1, 1),
    _GsEInventoryResourceType_Type()
)
gsEInventoryResourceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gsEInventoryResourceType.setStatus("mandatory")
_GsEInventoryResourceIndex_Type = ResourceId
_GsEInventoryResourceIndex_Object = MibTableColumn
gsEInventoryResourceIndex = _GsEInventoryResourceIndex_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 39, 3, 2, 1, 1, 2),
    _GsEInventoryResourceIndex_Type()
)
gsEInventoryResourceIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gsEInventoryResourceIndex.setStatus("mandatory")


class _GsEInventoryModelNumber_Type(DisplayString):
    """Custom type gsEInventoryModelNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_GsEInventoryModelNumber_Type.__name__ = "DisplayString"
_GsEInventoryModelNumber_Object = MibTableColumn
gsEInventoryModelNumber = _GsEInventoryModelNumber_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 39, 3, 2, 1, 1, 3),
    _GsEInventoryModelNumber_Type()
)
gsEInventoryModelNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gsEInventoryModelNumber.setStatus("mandatory")


class _GsEInventorySerialNumber_Type(DisplayString):
    """Custom type gsEInventorySerialNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_GsEInventorySerialNumber_Type.__name__ = "DisplayString"
_GsEInventorySerialNumber_Object = MibTableColumn
gsEInventorySerialNumber = _GsEInventorySerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 39, 3, 2, 1, 1, 4),
    _GsEInventorySerialNumber_Type()
)
gsEInventorySerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gsEInventorySerialNumber.setStatus("mandatory")


class _GsEInventoryVersion_Type(DisplayString):
    """Custom type gsEInventoryVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_GsEInventoryVersion_Type.__name__ = "DisplayString"
_GsEInventoryVersion_Object = MibTableColumn
gsEInventoryVersion = _GsEInventoryVersion_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 39, 3, 2, 1, 1, 5),
    _GsEInventoryVersion_Type()
)
gsEInventoryVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gsEInventoryVersion.setStatus("mandatory")


class _GsEInventoryManufactureInfo_Type(DisplayString):
    """Custom type gsEInventoryManufactureInfo based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_GsEInventoryManufactureInfo_Type.__name__ = "DisplayString"
_GsEInventoryManufactureInfo_Object = MibTableColumn
gsEInventoryManufactureInfo = _GsEInventoryManufactureInfo_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 39, 3, 2, 1, 1, 6),
    _GsEInventoryManufactureInfo_Type()
)
gsEInventoryManufactureInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gsEInventoryManufactureInfo.setStatus("mandatory")


class _GsEInventoryScratchPad_Type(DisplayString):
    """Custom type gsEInventoryScratchPad based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_GsEInventoryScratchPad_Type.__name__ = "DisplayString"
_GsEInventoryScratchPad_Object = MibTableColumn
gsEInventoryScratchPad = _GsEInventoryScratchPad_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 39, 3, 2, 1, 1, 7),
    _GsEInventoryScratchPad_Type()
)
gsEInventoryScratchPad.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gsEInventoryScratchPad.setStatus("mandatory")
_GsEPowerSystems_ObjectIdentity = ObjectIdentity
gsEPowerSystems = _GsEPowerSystems_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 39, 3, 3)
)
_GsEPowerSupplies_ObjectIdentity = ObjectIdentity
gsEPowerSupplies = _GsEPowerSupplies_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 39, 3, 3, 1)
)
_GsEPowerSupplyTable_Object = MibTable
gsEPowerSupplyTable = _GsEPowerSupplyTable_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 39, 3, 3, 1, 1)
)
if mibBuilder.loadTexts:
    gsEPowerSupplyTable.setStatus("mandatory")
_GsEPowerSupplyEntry_Object = MibTableRow
gsEPowerSupplyEntry = _GsEPowerSupplyEntry_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 39, 3, 3, 1, 1, 1)
)
gsEPowerSupplyEntry.setIndexNames(
    (0, "GIGAswitchEthernet-MIB", "gsEPowerSupplyIndex"),
)
if mibBuilder.loadTexts:
    gsEPowerSupplyEntry.setStatus("mandatory")
_GsEPowerSupplyIndex_Type = ResourceId
_GsEPowerSupplyIndex_Object = MibTableColumn
gsEPowerSupplyIndex = _GsEPowerSupplyIndex_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 39, 3, 3, 1, 1, 1, 1),
    _GsEPowerSupplyIndex_Type()
)
gsEPowerSupplyIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gsEPowerSupplyIndex.setStatus("mandatory")


class _GsEPowerSupplyType_Type(Integer32):
    """Custom type gsEPowerSupplyType based on Integer32"""
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


_GsEPowerSupplyType_Type.__name__ = "Integer32"
_GsEPowerSupplyType_Object = MibTableColumn
gsEPowerSupplyType = _GsEPowerSupplyType_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 39, 3, 3, 1, 1, 1, 2),
    _GsEPowerSupplyType_Type()
)
gsEPowerSupplyType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gsEPowerSupplyType.setStatus("mandatory")


class _GsEPowerSupplyStatus_Type(Integer32):
    """Custom type gsEPowerSupplyStatus based on Integer32"""
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


_GsEPowerSupplyStatus_Type.__name__ = "Integer32"
_GsEPowerSupplyStatus_Object = MibTableColumn
gsEPowerSupplyStatus = _GsEPowerSupplyStatus_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 39, 3, 3, 1, 1, 1, 3),
    _GsEPowerSupplyStatus_Type()
)
gsEPowerSupplyStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gsEPowerSupplyStatus.setStatus("mandatory")


class _GsEPowerSupplyInputStatus_Type(Integer32):
    """Custom type gsEPowerSupplyInputStatus based on Integer32"""
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


_GsEPowerSupplyInputStatus_Type.__name__ = "Integer32"
_GsEPowerSupplyInputStatus_Object = MibTableColumn
gsEPowerSupplyInputStatus = _GsEPowerSupplyInputStatus_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 39, 3, 3, 1, 1, 1, 4),
    _GsEPowerSupplyInputStatus_Type()
)
gsEPowerSupplyInputStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gsEPowerSupplyInputStatus.setStatus("mandatory")


class _GsEPowerSupplyOutputStatus_Type(Integer32):
    """Custom type gsEPowerSupplyOutputStatus based on Integer32"""
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


_GsEPowerSupplyOutputStatus_Type.__name__ = "Integer32"
_GsEPowerSupplyOutputStatus_Object = MibTableColumn
gsEPowerSupplyOutputStatus = _GsEPowerSupplyOutputStatus_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 39, 3, 3, 1, 1, 1, 5),
    _GsEPowerSupplyOutputStatus_Type()
)
gsEPowerSupplyOutputStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gsEPowerSupplyOutputStatus.setStatus("mandatory")
_GsEPowerSupplyOutputCapacity_Type = Integer32
_GsEPowerSupplyOutputCapacity_Object = MibTableColumn
gsEPowerSupplyOutputCapacity = _GsEPowerSupplyOutputCapacity_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 39, 3, 3, 1, 1, 1, 6),
    _GsEPowerSupplyOutputCapacity_Type()
)
gsEPowerSupplyOutputCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gsEPowerSupplyOutputCapacity.setStatus("mandatory")
_GsEPowerMgmtGen_ObjectIdentity = ObjectIdentity
gsEPowerMgmtGen = _GsEPowerMgmtGen_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 39, 3, 3, 2)
)
_GsEPowerCapacity_Type = Integer32
_GsEPowerCapacity_Object = MibScalar
gsEPowerCapacity = _GsEPowerCapacity_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 39, 3, 3, 2, 1),
    _GsEPowerCapacity_Type()
)
gsEPowerCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gsEPowerCapacity.setStatus("mandatory")
_GsEPowerUsed_Type = Integer32
_GsEPowerUsed_Object = MibScalar
gsEPowerUsed = _GsEPowerUsed_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 39, 3, 3, 2, 2),
    _GsEPowerUsed_Type()
)
gsEPowerUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gsEPowerUsed.setStatus("mandatory")
_GsEPowerMgmtCtl_ObjectIdentity = ObjectIdentity
gsEPowerMgmtCtl = _GsEPowerMgmtCtl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 39, 3, 3, 3)
)
_GsEPowerControlTable_Object = MibTable
gsEPowerControlTable = _GsEPowerControlTable_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 39, 3, 3, 3, 1)
)
if mibBuilder.loadTexts:
    gsEPowerControlTable.setStatus("mandatory")
_GsEPowerControlEntry_Object = MibTableRow
gsEPowerControlEntry = _GsEPowerControlEntry_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 39, 3, 3, 3, 1, 1)
)
gsEPowerControlEntry.setIndexNames(
    (0, "GIGAswitchEthernet-MIB", "gsEModuleIndex"),
)
if mibBuilder.loadTexts:
    gsEPowerControlEntry.setStatus("mandatory")
_GsEPowerControlUsed_Type = Integer32
_GsEPowerControlUsed_Object = MibTableColumn
gsEPowerControlUsed = _GsEPowerControlUsed_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 39, 3, 3, 3, 1, 1, 1),
    _GsEPowerControlUsed_Type()
)
gsEPowerControlUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gsEPowerControlUsed.setStatus("mandatory")


class _GsEPowerControlPriority_Type(Integer32):
    """Custom type gsEPowerControlPriority based on Integer32"""
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


_GsEPowerControlPriority_Type.__name__ = "Integer32"
_GsEPowerControlPriority_Object = MibTableColumn
gsEPowerControlPriority = _GsEPowerControlPriority_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 39, 3, 3, 3, 1, 1, 2),
    _GsEPowerControlPriority_Type()
)
gsEPowerControlPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gsEPowerControlPriority.setStatus("mandatory")


class _GsEPowerControlMode_Type(Integer32):
    """Custom type gsEPowerControlMode based on Integer32"""
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


_GsEPowerControlMode_Type.__name__ = "Integer32"
_GsEPowerControlMode_Object = MibTableColumn
gsEPowerControlMode = _GsEPowerControlMode_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 39, 3, 3, 3, 1, 1, 3),
    _GsEPowerControlMode_Type()
)
gsEPowerControlMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gsEPowerControlMode.setStatus("mandatory")
_GsETemperature_ObjectIdentity = ObjectIdentity
gsETemperature = _GsETemperature_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 39, 3, 4)
)
_GsETempTable_Object = MibTable
gsETempTable = _GsETempTable_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 39, 3, 4, 1)
)
if mibBuilder.loadTexts:
    gsETempTable.setStatus("mandatory")
_GsETempEntry_Object = MibTableRow
gsETempEntry = _GsETempEntry_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 39, 3, 4, 1, 1)
)
gsETempEntry.setIndexNames(
    (0, "GIGAswitchEthernet-MIB", "gsETempIndex"),
)
if mibBuilder.loadTexts:
    gsETempEntry.setStatus("mandatory")
_GsETempIndex_Type = ResourceId
_GsETempIndex_Object = MibTableColumn
gsETempIndex = _GsETempIndex_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 39, 3, 4, 1, 1, 1),
    _GsETempIndex_Type()
)
gsETempIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gsETempIndex.setStatus("mandatory")
_GsETempValue_Type = Integer32
_GsETempValue_Object = MibTableColumn
gsETempValue = _GsETempValue_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 39, 3, 4, 1, 1, 2),
    _GsETempValue_Type()
)
gsETempValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gsETempValue.setStatus("mandatory")
_GsETempUpperLimit_Type = Integer32
_GsETempUpperLimit_Object = MibTableColumn
gsETempUpperLimit = _GsETempUpperLimit_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 39, 3, 4, 1, 1, 3),
    _GsETempUpperLimit_Type()
)
gsETempUpperLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gsETempUpperLimit.setStatus("mandatory")
_GsETempUpperWarning_Type = Integer32
_GsETempUpperWarning_Object = MibTableColumn
gsETempUpperWarning = _GsETempUpperWarning_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 39, 3, 4, 1, 1, 4),
    _GsETempUpperWarning_Type()
)
gsETempUpperWarning.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gsETempUpperWarning.setStatus("mandatory")
_GsETempLowerWarning_Type = Integer32
_GsETempLowerWarning_Object = MibTableColumn
gsETempLowerWarning = _GsETempLowerWarning_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 39, 3, 4, 1, 1, 5),
    _GsETempLowerWarning_Type()
)
gsETempLowerWarning.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gsETempLowerWarning.setStatus("mandatory")
_GsETempLowerLimit_Type = Integer32
_GsETempLowerLimit_Object = MibTableColumn
gsETempLowerLimit = _GsETempLowerLimit_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 39, 3, 4, 1, 1, 6),
    _GsETempLowerLimit_Type()
)
gsETempLowerLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gsETempLowerLimit.setStatus("mandatory")
_GsEModules_ObjectIdentity = ObjectIdentity
gsEModules = _GsEModules_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 39, 3, 5)
)
_GsEModuleTable_Object = MibTable
gsEModuleTable = _GsEModuleTable_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 39, 3, 5, 1)
)
if mibBuilder.loadTexts:
    gsEModuleTable.setStatus("mandatory")
_GsEModuleEntry_Object = MibTableRow
gsEModuleEntry = _GsEModuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 39, 3, 5, 1, 1)
)
gsEModuleEntry.setIndexNames(
    (0, "GIGAswitchEthernet-MIB", "gsEModuleIndex"),
)
if mibBuilder.loadTexts:
    gsEModuleEntry.setStatus("mandatory")
_GsEModuleIndex_Type = ResourceId
_GsEModuleIndex_Object = MibTableColumn
gsEModuleIndex = _GsEModuleIndex_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 39, 3, 5, 1, 1, 1),
    _GsEModuleIndex_Type()
)
gsEModuleIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gsEModuleIndex.setStatus("mandatory")


class _GsEModuleName_Type(DisplayString):
    """Custom type gsEModuleName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_GsEModuleName_Type.__name__ = "DisplayString"
_GsEModuleName_Object = MibTableColumn
gsEModuleName = _GsEModuleName_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 39, 3, 5, 1, 1, 2),
    _GsEModuleName_Type()
)
gsEModuleName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gsEModuleName.setStatus("mandatory")


class _GsEModuleType_Type(Integer32):
    """Custom type gsEModuleType based on Integer32"""
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


_GsEModuleType_Type.__name__ = "Integer32"
_GsEModuleType_Object = MibTableColumn
gsEModuleType = _GsEModuleType_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 39, 3, 5, 1, 1, 3),
    _GsEModuleType_Type()
)
gsEModuleType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gsEModuleType.setStatus("mandatory")


class _GsEModuleBaseType_Type(Integer32):
    """Custom type gsEModuleBaseType based on Integer32"""
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


_GsEModuleBaseType_Type.__name__ = "Integer32"
_GsEModuleBaseType_Object = MibTableColumn
gsEModuleBaseType = _GsEModuleBaseType_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 39, 3, 5, 1, 1, 4),
    _GsEModuleBaseType_Type()
)
gsEModuleBaseType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gsEModuleBaseType.setStatus("mandatory")
_GsEModuleSlotWidth_Type = Integer32
_GsEModuleSlotWidth_Object = MibTableColumn
gsEModuleSlotWidth = _GsEModuleSlotWidth_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 39, 3, 5, 1, 1, 5),
    _GsEModuleSlotWidth_Type()
)
gsEModuleSlotWidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gsEModuleSlotWidth.setStatus("mandatory")
_GsEModuleSlotOffset_Type = Integer32
_GsEModuleSlotOffset_Object = MibTableColumn
gsEModuleSlotOffset = _GsEModuleSlotOffset_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 39, 3, 5, 1, 1, 6),
    _GsEModuleSlotOffset_Type()
)
gsEModuleSlotOffset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gsEModuleSlotOffset.setStatus("mandatory")
_GsEModulePorts_Type = Integer32
_GsEModulePorts_Object = MibTableColumn
gsEModulePorts = _GsEModulePorts_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 39, 3, 5, 1, 1, 7),
    _GsEModulePorts_Type()
)
gsEModulePorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gsEModulePorts.setStatus("mandatory")
_GsEPorts_ObjectIdentity = ObjectIdentity
gsEPorts = _GsEPorts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 39, 3, 6)
)
_GsEPortMgt_ObjectIdentity = ObjectIdentity
gsEPortMgt = _GsEPortMgt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 39, 3, 6, 1)
)
_GsEPortTable_Object = MibTable
gsEPortTable = _GsEPortTable_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 39, 3, 6, 1, 1)
)
if mibBuilder.loadTexts:
    gsEPortTable.setStatus("mandatory")
_GsEPortEntry_Object = MibTableRow
gsEPortEntry = _GsEPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 39, 3, 6, 1, 1, 1)
)
gsEPortEntry.setIndexNames(
    (0, "GIGAswitchEthernet-MIB", "gsEPortIndex"),
)
if mibBuilder.loadTexts:
    gsEPortEntry.setStatus("mandatory")
_GsEPortIndex_Type = ResourceId
_GsEPortIndex_Object = MibTableColumn
gsEPortIndex = _GsEPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 39, 3, 6, 1, 1, 1, 1),
    _GsEPortIndex_Type()
)
gsEPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gsEPortIndex.setStatus("mandatory")


class _GsEPortName_Type(DisplayString):
    """Custom type gsEPortName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_GsEPortName_Type.__name__ = "DisplayString"
_GsEPortName_Object = MibTableColumn
gsEPortName = _GsEPortName_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 39, 3, 6, 1, 1, 1, 2),
    _GsEPortName_Type()
)
gsEPortName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gsEPortName.setStatus("mandatory")


class _GsEPortType_Type(Integer32):
    """Custom type gsEPortType based on Integer32"""
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


_GsEPortType_Type.__name__ = "Integer32"
_GsEPortType_Object = MibTableColumn
gsEPortType = _GsEPortType_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 39, 3, 6, 1, 1, 1, 3),
    _GsEPortType_Type()
)
gsEPortType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gsEPortType.setStatus("mandatory")


class _GsEPortBaseType_Type(Integer32):
    """Custom type gsEPortBaseType based on Integer32"""
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


_GsEPortBaseType_Type.__name__ = "Integer32"
_GsEPortBaseType_Object = MibTableColumn
gsEPortBaseType = _GsEPortBaseType_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 39, 3, 6, 1, 1, 1, 4),
    _GsEPortBaseType_Type()
)
gsEPortBaseType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gsEPortBaseType.setStatus("mandatory")


class _GsEPortMode_Type(Integer32):
    """Custom type gsEPortMode based on Integer32"""
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


_GsEPortMode_Type.__name__ = "Integer32"
_GsEPortMode_Object = MibTableColumn
gsEPortMode = _GsEPortMode_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 39, 3, 6, 1, 1, 1, 5),
    _GsEPortMode_Type()
)
gsEPortMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gsEPortMode.setStatus("mandatory")


class _GsEPortStatus_Type(Integer32):
    """Custom type gsEPortStatus based on Integer32"""
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


_GsEPortStatus_Type.__name__ = "Integer32"
_GsEPortStatus_Object = MibTableColumn
gsEPortStatus = _GsEPortStatus_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 39, 3, 6, 1, 1, 1, 6),
    _GsEPortStatus_Type()
)
gsEPortStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gsEPortStatus.setStatus("mandatory")


class _GsEPortConnector_Type(Integer32):
    """Custom type gsEPortConnector based on Integer32"""
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


_GsEPortConnector_Type.__name__ = "Integer32"
_GsEPortConnector_Object = MibTableColumn
gsEPortConnector = _GsEPortConnector_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 39, 3, 6, 1, 1, 1, 7),
    _GsEPortConnector_Type()
)
gsEPortConnector.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gsEPortConnector.setStatus("mandatory")


class _GsEPortSpeedState_Type(Integer32):
    """Custom type gsEPortSpeedState based on Integer32"""
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


_GsEPortSpeedState_Type.__name__ = "Integer32"
_GsEPortSpeedState_Object = MibTableColumn
gsEPortSpeedState = _GsEPortSpeedState_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 39, 3, 6, 1, 1, 1, 8),
    _GsEPortSpeedState_Type()
)
gsEPortSpeedState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gsEPortSpeedState.setStatus("mandatory")


class _GsEPortDuplexState_Type(Integer32):
    """Custom type gsEPortDuplexState based on Integer32"""
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


_GsEPortDuplexState_Type.__name__ = "Integer32"
_GsEPortDuplexState_Object = MibTableColumn
gsEPortDuplexState = _GsEPortDuplexState_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 39, 3, 6, 1, 1, 1, 9),
    _GsEPortDuplexState_Type()
)
gsEPortDuplexState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gsEPortDuplexState.setStatus("mandatory")
_GsEPortGroupBinding_Type = ResourceId
_GsEPortGroupBinding_Object = MibTableColumn
gsEPortGroupBinding = _GsEPortGroupBinding_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 39, 3, 6, 1, 1, 1, 10),
    _GsEPortGroupBinding_Type()
)
gsEPortGroupBinding.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gsEPortGroupBinding.setStatus("mandatory")
_GsEPortFlowControlMgt_ObjectIdentity = ObjectIdentity
gsEPortFlowControlMgt = _GsEPortFlowControlMgt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 39, 3, 6, 2)
)
_GsEPortFlowControlTable_Object = MibTable
gsEPortFlowControlTable = _GsEPortFlowControlTable_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 39, 3, 6, 2, 1)
)
if mibBuilder.loadTexts:
    gsEPortFlowControlTable.setStatus("mandatory")
_GsEPortFlowControlEntry_Object = MibTableRow
gsEPortFlowControlEntry = _GsEPortFlowControlEntry_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 39, 3, 6, 2, 1, 1)
)
gsEPortFlowControlEntry.setIndexNames(
    (0, "GIGAswitchEthernet-MIB", "gsEPortIndex"),
)
if mibBuilder.loadTexts:
    gsEPortFlowControlEntry.setStatus("mandatory")


class _GsEPortFlowControlMode_Type(Integer32):
    """Custom type gsEPortFlowControlMode based on Integer32"""
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


_GsEPortFlowControlMode_Type.__name__ = "Integer32"
_GsEPortFlowControlMode_Object = MibTableColumn
gsEPortFlowControlMode = _GsEPortFlowControlMode_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 39, 3, 6, 2, 1, 1, 21),
    _GsEPortFlowControlMode_Type()
)
gsEPortFlowControlMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gsEPortFlowControlMode.setStatus("mandatory")
_GsEPortDuplexMgt_ObjectIdentity = ObjectIdentity
gsEPortDuplexMgt = _GsEPortDuplexMgt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 39, 3, 6, 3)
)
_GsEPortDuplexTable_Object = MibTable
gsEPortDuplexTable = _GsEPortDuplexTable_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 39, 3, 6, 3, 1)
)
if mibBuilder.loadTexts:
    gsEPortDuplexTable.setStatus("mandatory")
_GsEPortDuplexEntry_Object = MibTableRow
gsEPortDuplexEntry = _GsEPortDuplexEntry_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 39, 3, 6, 3, 1, 1)
)
gsEPortDuplexEntry.setIndexNames(
    (0, "GIGAswitchEthernet-MIB", "gsEPortIndex"),
)
if mibBuilder.loadTexts:
    gsEPortDuplexEntry.setStatus("mandatory")


class _GsEPortDuplexMode_Type(Integer32):
    """Custom type gsEPortDuplexMode based on Integer32"""
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


_GsEPortDuplexMode_Type.__name__ = "Integer32"
_GsEPortDuplexMode_Object = MibTableColumn
gsEPortDuplexMode = _GsEPortDuplexMode_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 39, 3, 6, 3, 1, 1, 31),
    _GsEPortDuplexMode_Type()
)
gsEPortDuplexMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gsEPortDuplexMode.setStatus("mandatory")
_GsEPortSpeedMgt_ObjectIdentity = ObjectIdentity
gsEPortSpeedMgt = _GsEPortSpeedMgt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 39, 3, 6, 4)
)
_GsEPortSpeedTable_Object = MibTable
gsEPortSpeedTable = _GsEPortSpeedTable_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 39, 3, 6, 4, 1)
)
if mibBuilder.loadTexts:
    gsEPortSpeedTable.setStatus("mandatory")
_GsEPortSpeedEntry_Object = MibTableRow
gsEPortSpeedEntry = _GsEPortSpeedEntry_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 39, 3, 6, 4, 1, 1)
)
gsEPortSpeedEntry.setIndexNames(
    (0, "GIGAswitchEthernet-MIB", "gsEPortIndex"),
)
if mibBuilder.loadTexts:
    gsEPortSpeedEntry.setStatus("mandatory")


class _GsEPortSpeedMode_Type(Integer32):
    """Custom type gsEPortSpeedMode based on Integer32"""
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


_GsEPortSpeedMode_Type.__name__ = "Integer32"
_GsEPortSpeedMode_Object = MibTableColumn
gsEPortSpeedMode = _GsEPortSpeedMode_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 39, 3, 6, 4, 1, 1, 41),
    _GsEPortSpeedMode_Type()
)
gsEPortSpeedMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gsEPortSpeedMode.setStatus("mandatory")
_GsEPortAutoNegotiationMgt_ObjectIdentity = ObjectIdentity
gsEPortAutoNegotiationMgt = _GsEPortAutoNegotiationMgt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 39, 3, 6, 5)
)
_GsEPortAutoNegotiationTable_Object = MibTable
gsEPortAutoNegotiationTable = _GsEPortAutoNegotiationTable_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 39, 3, 6, 5, 1)
)
if mibBuilder.loadTexts:
    gsEPortAutoNegotiationTable.setStatus("mandatory")
_GsEPortAutoNegotiationEntry_Object = MibTableRow
gsEPortAutoNegotiationEntry = _GsEPortAutoNegotiationEntry_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 39, 3, 6, 5, 1, 1)
)
gsEPortAutoNegotiationEntry.setIndexNames(
    (0, "GIGAswitchEthernet-MIB", "gsEPortIndex"),
)
if mibBuilder.loadTexts:
    gsEPortAutoNegotiationEntry.setStatus("mandatory")


class _GsEPortAutoNegotiationMode_Type(Integer32):
    """Custom type gsEPortAutoNegotiationMode based on Integer32"""
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


_GsEPortAutoNegotiationMode_Type.__name__ = "Integer32"
_GsEPortAutoNegotiationMode_Object = MibTableColumn
gsEPortAutoNegotiationMode = _GsEPortAutoNegotiationMode_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 39, 3, 6, 5, 1, 1, 51),
    _GsEPortAutoNegotiationMode_Type()
)
gsEPortAutoNegotiationMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gsEPortAutoNegotiationMode.setStatus("mandatory")


class _GsEPortAutoNegotiationSpeedAdvertisement_Type(Integer32):
    """Custom type gsEPortAutoNegotiationSpeedAdvertisement based on Integer32"""
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


_GsEPortAutoNegotiationSpeedAdvertisement_Type.__name__ = "Integer32"
_GsEPortAutoNegotiationSpeedAdvertisement_Object = MibTableColumn
gsEPortAutoNegotiationSpeedAdvertisement = _GsEPortAutoNegotiationSpeedAdvertisement_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 39, 3, 6, 5, 1, 1, 52),
    _GsEPortAutoNegotiationSpeedAdvertisement_Type()
)
gsEPortAutoNegotiationSpeedAdvertisement.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gsEPortAutoNegotiationSpeedAdvertisement.setStatus("mandatory")


class _GsEPortAutoNegotiationDuplexAdvertisement_Type(Integer32):
    """Custom type gsEPortAutoNegotiationDuplexAdvertisement based on Integer32"""
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


_GsEPortAutoNegotiationDuplexAdvertisement_Type.__name__ = "Integer32"
_GsEPortAutoNegotiationDuplexAdvertisement_Object = MibTableColumn
gsEPortAutoNegotiationDuplexAdvertisement = _GsEPortAutoNegotiationDuplexAdvertisement_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 39, 3, 6, 5, 1, 1, 53),
    _GsEPortAutoNegotiationDuplexAdvertisement_Type()
)
gsEPortAutoNegotiationDuplexAdvertisement.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gsEPortAutoNegotiationDuplexAdvertisement.setStatus("mandatory")
_GsEPortRateLimitMgt_ObjectIdentity = ObjectIdentity
gsEPortRateLimitMgt = _GsEPortRateLimitMgt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 39, 3, 6, 6)
)
_GsEPortRateLimitTable_Object = MibTable
gsEPortRateLimitTable = _GsEPortRateLimitTable_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 39, 3, 6, 6, 1)
)
if mibBuilder.loadTexts:
    gsEPortRateLimitTable.setStatus("mandatory")
_GsEPortRateLimitEntry_Object = MibTableRow
gsEPortRateLimitEntry = _GsEPortRateLimitEntry_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 39, 3, 6, 6, 1, 1)
)
gsEPortRateLimitEntry.setIndexNames(
    (0, "GIGAswitchEthernet-MIB", "gsEPortIndex"),
)
if mibBuilder.loadTexts:
    gsEPortRateLimitEntry.setStatus("mandatory")


class _GsEPortRateLimitMode_Type(Integer32):
    """Custom type gsEPortRateLimitMode based on Integer32"""
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


_GsEPortRateLimitMode_Type.__name__ = "Integer32"
_GsEPortRateLimitMode_Object = MibTableColumn
gsEPortRateLimitMode = _GsEPortRateLimitMode_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 39, 3, 6, 6, 1, 1, 61),
    _GsEPortRateLimitMode_Type()
)
gsEPortRateLimitMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gsEPortRateLimitMode.setStatus("mandatory")


class _GsEPortRateLimitRate_Type(Integer32):
    """Custom type gsEPortRateLimitRate based on Integer32"""
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


_GsEPortRateLimitRate_Type.__name__ = "Integer32"
_GsEPortRateLimitRate_Object = MibTableColumn
gsEPortRateLimitRate = _GsEPortRateLimitRate_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 39, 3, 6, 6, 1, 1, 62),
    _GsEPortRateLimitRate_Type()
)
gsEPortRateLimitRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gsEPortRateLimitRate.setStatus("mandatory")


class _GsEPortRateLimitBurstSize_Type(Integer32):
    """Custom type gsEPortRateLimitBurstSize based on Integer32"""
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


_GsEPortRateLimitBurstSize_Type.__name__ = "Integer32"
_GsEPortRateLimitBurstSize_Object = MibTableColumn
gsEPortRateLimitBurstSize = _GsEPortRateLimitBurstSize_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 39, 3, 6, 6, 1, 1, 63),
    _GsEPortRateLimitBurstSize_Type()
)
gsEPortRateLimitBurstSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gsEPortRateLimitBurstSize.setStatus("mandatory")
_GsEPortCategoryMgt_ObjectIdentity = ObjectIdentity
gsEPortCategoryMgt = _GsEPortCategoryMgt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 39, 3, 6, 8)
)
_GsEPortCategoryTable_Object = MibTable
gsEPortCategoryTable = _GsEPortCategoryTable_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 39, 3, 6, 8, 1)
)
if mibBuilder.loadTexts:
    gsEPortCategoryTable.setStatus("mandatory")
_GsEPortCategoryEntry_Object = MibTableRow
gsEPortCategoryEntry = _GsEPortCategoryEntry_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 39, 3, 6, 8, 1, 1)
)
gsEPortCategoryEntry.setIndexNames(
    (0, "GIGAswitchEthernet-MIB", "gsEPortIndex"),
)
if mibBuilder.loadTexts:
    gsEPortCategoryEntry.setStatus("mandatory")


class _GsEPortCategoryMode_Type(Integer32):
    """Custom type gsEPortCategoryMode based on Integer32"""
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


_GsEPortCategoryMode_Type.__name__ = "Integer32"
_GsEPortCategoryMode_Object = MibTableColumn
gsEPortCategoryMode = _GsEPortCategoryMode_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 39, 3, 6, 8, 1, 1, 81),
    _GsEPortCategoryMode_Type()
)
gsEPortCategoryMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gsEPortCategoryMode.setStatus("mandatory")
_GsEBufferMgt_ObjectIdentity = ObjectIdentity
gsEBufferMgt = _GsEBufferMgt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 39, 3, 7)
)
_GsEBufferTable_Object = MibTable
gsEBufferTable = _GsEBufferTable_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 39, 3, 7, 1)
)
if mibBuilder.loadTexts:
    gsEBufferTable.setStatus("mandatory")
_GsEBufferEntry_Object = MibTableRow
gsEBufferEntry = _GsEBufferEntry_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 39, 3, 7, 1, 1)
)
gsEBufferEntry.setIndexNames(
    (0, "GIGAswitchEthernet-MIB", "gsEBufferIndex"),
)
if mibBuilder.loadTexts:
    gsEBufferEntry.setStatus("mandatory")
_GsEBufferIndex_Type = ResourceId
_GsEBufferIndex_Object = MibTableColumn
gsEBufferIndex = _GsEBufferIndex_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 39, 3, 7, 1, 1, 1),
    _GsEBufferIndex_Type()
)
gsEBufferIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gsEBufferIndex.setStatus("mandatory")
_GsEBufferFabricPort_Type = ResourceId
_GsEBufferFabricPort_Object = MibTableColumn
gsEBufferFabricPort = _GsEBufferFabricPort_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 39, 3, 7, 1, 1, 2),
    _GsEBufferFabricPort_Type()
)
gsEBufferFabricPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gsEBufferFabricPort.setStatus("mandatory")


class _GsEBufferFabricPortDirection_Type(Integer32):
    """Custom type gsEBufferFabricPortDirection based on Integer32"""
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


_GsEBufferFabricPortDirection_Type.__name__ = "Integer32"
_GsEBufferFabricPortDirection_Object = MibTableColumn
gsEBufferFabricPortDirection = _GsEBufferFabricPortDirection_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 39, 3, 7, 1, 1, 3),
    _GsEBufferFabricPortDirection_Type()
)
gsEBufferFabricPortDirection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gsEBufferFabricPortDirection.setStatus("mandatory")
_GsEBufferSwitchPort_Type = ResourceId
_GsEBufferSwitchPort_Object = MibTableColumn
gsEBufferSwitchPort = _GsEBufferSwitchPort_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 39, 3, 7, 1, 1, 4),
    _GsEBufferSwitchPort_Type()
)
gsEBufferSwitchPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gsEBufferSwitchPort.setStatus("mandatory")
_GsEBufferMemory_Type = Integer32
_GsEBufferMemory_Object = MibTableColumn
gsEBufferMemory = _GsEBufferMemory_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 39, 3, 7, 1, 1, 5),
    _GsEBufferMemory_Type()
)
gsEBufferMemory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gsEBufferMemory.setStatus("mandatory")


class _GsEBufferAgeTimer_Type(Integer32):
    """Custom type gsEBufferAgeTimer based on Integer32"""
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


_GsEBufferAgeTimer_Type.__name__ = "Integer32"
_GsEBufferAgeTimer_Object = MibTableColumn
gsEBufferAgeTimer = _GsEBufferAgeTimer_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 39, 3, 7, 1, 1, 6),
    _GsEBufferAgeTimer_Type()
)
gsEBufferAgeTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gsEBufferAgeTimer.setStatus("mandatory")


class _GsEBufferPriorityServicing_Type(Integer32):
    """Custom type gsEBufferPriorityServicing based on Integer32"""
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


_GsEBufferPriorityServicing_Type.__name__ = "Integer32"
_GsEBufferPriorityServicing_Object = MibTableColumn
gsEBufferPriorityServicing = _GsEBufferPriorityServicing_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 39, 3, 7, 1, 1, 7),
    _GsEBufferPriorityServicing_Type()
)
gsEBufferPriorityServicing.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gsEBufferPriorityServicing.setStatus("mandatory")


class _GsEBufferPriorityAllocation_Type(Integer32):
    """Custom type gsEBufferPriorityAllocation based on Integer32"""
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


_GsEBufferPriorityAllocation_Type.__name__ = "Integer32"
_GsEBufferPriorityAllocation_Object = MibTableColumn
gsEBufferPriorityAllocation = _GsEBufferPriorityAllocation_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 39, 3, 7, 1, 1, 8),
    _GsEBufferPriorityAllocation_Type()
)
gsEBufferPriorityAllocation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gsEBufferPriorityAllocation.setStatus("mandatory")


class _GsEBufferPriorityThreshold_Type(Integer32):
    """Custom type gsEBufferPriorityThreshold based on Integer32"""
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


_GsEBufferPriorityThreshold_Type.__name__ = "Integer32"
_GsEBufferPriorityThreshold_Object = MibTableColumn
gsEBufferPriorityThreshold = _GsEBufferPriorityThreshold_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 39, 3, 7, 1, 1, 9),
    _GsEBufferPriorityThreshold_Type()
)
gsEBufferPriorityThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gsEBufferPriorityThreshold.setStatus("mandatory")


class _GsEBufferCongestion_Type(Integer32):
    """Custom type gsEBufferCongestion based on Integer32"""
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


_GsEBufferCongestion_Type.__name__ = "Integer32"
_GsEBufferCongestion_Object = MibTableColumn
gsEBufferCongestion = _GsEBufferCongestion_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 39, 3, 7, 1, 1, 10),
    _GsEBufferCongestion_Type()
)
gsEBufferCongestion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gsEBufferCongestion.setStatus("mandatory")
_GsEBufferHighOverflowDrops_Type = Counter32
_GsEBufferHighOverflowDrops_Object = MibTableColumn
gsEBufferHighOverflowDrops = _GsEBufferHighOverflowDrops_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 39, 3, 7, 1, 1, 11),
    _GsEBufferHighOverflowDrops_Type()
)
gsEBufferHighOverflowDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gsEBufferHighOverflowDrops.setStatus("mandatory")
_GsEBufferLowOverflowDrops_Type = Counter32
_GsEBufferLowOverflowDrops_Object = MibTableColumn
gsEBufferLowOverflowDrops = _GsEBufferLowOverflowDrops_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 39, 3, 7, 1, 1, 12),
    _GsEBufferLowOverflowDrops_Type()
)
gsEBufferLowOverflowDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gsEBufferLowOverflowDrops.setStatus("mandatory")
_GsEBufferHighStaleDrops_Type = Counter32
_GsEBufferHighStaleDrops_Object = MibTableColumn
gsEBufferHighStaleDrops = _GsEBufferHighStaleDrops_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 39, 3, 7, 1, 1, 13),
    _GsEBufferHighStaleDrops_Type()
)
gsEBufferHighStaleDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gsEBufferHighStaleDrops.setStatus("mandatory")
_GsEBufferLowStaleDrops_Type = Counter32
_GsEBufferLowStaleDrops_Object = MibTableColumn
gsEBufferLowStaleDrops = _GsEBufferLowStaleDrops_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 39, 3, 7, 1, 1, 14),
    _GsEBufferLowStaleDrops_Type()
)
gsEBufferLowStaleDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gsEBufferLowStaleDrops.setStatus("mandatory")
_GsEBufferCongestionDrops_Type = Counter32
_GsEBufferCongestionDrops_Object = MibTableColumn
gsEBufferCongestionDrops = _GsEBufferCongestionDrops_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 39, 3, 7, 1, 1, 16),
    _GsEBufferCongestionDrops_Type()
)
gsEBufferCongestionDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gsEBufferCongestionDrops.setStatus("mandatory")
_GsESwitching_ObjectIdentity = ObjectIdentity
gsESwitching = _GsESwitching_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 39, 5)
)
_GsESwitchingLayerII_ObjectIdentity = ObjectIdentity
gsESwitchingLayerII = _GsESwitchingLayerII_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 39, 5, 1)
)
_GsESwitchGen_ObjectIdentity = ObjectIdentity
gsESwitchGen = _GsESwitchGen_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 39, 5, 1, 1)
)


class _GsESwitchSTPConfig_Type(Integer32):
    """Custom type gsESwitchSTPConfig based on Integer32"""
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


_GsESwitchSTPConfig_Type.__name__ = "Integer32"
_GsESwitchSTPConfig_Object = MibScalar
gsESwitchSTPConfig = _GsESwitchSTPConfig_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 39, 5, 1, 1, 1),
    _GsESwitchSTPConfig_Type()
)
gsESwitchSTPConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gsESwitchSTPConfig.setStatus("mandatory")


class _GsESwitchAgingTime_Type(Integer32):
    """Custom type gsESwitchAgingTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 1000000),
    )


_GsESwitchAgingTime_Type.__name__ = "Integer32"
_GsESwitchAgingTime_Object = MibScalar
gsESwitchAgingTime = _GsESwitchAgingTime_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 39, 5, 1, 1, 2),
    _GsESwitchAgingTime_Type()
)
gsESwitchAgingTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gsESwitchAgingTime.setStatus("mandatory")


class _GsESwitchSuperAgingTime_Type(Integer32):
    """Custom type gsESwitchSuperAgingTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 30),
    )


_GsESwitchSuperAgingTime_Type.__name__ = "Integer32"
_GsESwitchSuperAgingTime_Object = MibScalar
gsESwitchSuperAgingTime = _GsESwitchSuperAgingTime_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 39, 5, 1, 1, 3),
    _GsESwitchSuperAgingTime_Type()
)
gsESwitchSuperAgingTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gsESwitchSuperAgingTime.setStatus("mandatory")
_GsEBridgeMgmt_ObjectIdentity = ObjectIdentity
gsEBridgeMgmt = _GsEBridgeMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 39, 5, 1, 2)
)
_GsEBridgeTable_Object = MibTable
gsEBridgeTable = _GsEBridgeTable_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 39, 5, 1, 2, 1)
)
if mibBuilder.loadTexts:
    gsEBridgeTable.setStatus("mandatory")
_GsEBridgeEntry_Object = MibTableRow
gsEBridgeEntry = _GsEBridgeEntry_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 39, 5, 1, 2, 1, 1)
)
gsEBridgeEntry.setIndexNames(
    (0, "GIGAswitchEthernet-MIB", "gsEBridgeIndex"),
)
if mibBuilder.loadTexts:
    gsEBridgeEntry.setStatus("mandatory")
_GsEBridgeIndex_Type = ResourceId
_GsEBridgeIndex_Object = MibTableColumn
gsEBridgeIndex = _GsEBridgeIndex_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 39, 5, 1, 2, 1, 1, 1),
    _GsEBridgeIndex_Type()
)
gsEBridgeIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gsEBridgeIndex.setStatus("mandatory")


class _GsEBridgeType_Type(Integer32):
    """Custom type gsEBridgeType based on Integer32"""
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


_GsEBridgeType_Type.__name__ = "Integer32"
_GsEBridgeType_Object = MibTableColumn
gsEBridgeType = _GsEBridgeType_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 39, 5, 1, 2, 1, 1, 2),
    _GsEBridgeType_Type()
)
gsEBridgeType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gsEBridgeType.setStatus("mandatory")


class _GsEBridgeMode_Type(Integer32):
    """Custom type gsEBridgeMode based on Integer32"""
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


_GsEBridgeMode_Type.__name__ = "Integer32"
_GsEBridgeMode_Object = MibTableColumn
gsEBridgeMode = _GsEBridgeMode_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 39, 5, 1, 2, 1, 1, 3),
    _GsEBridgeMode_Type()
)
gsEBridgeMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gsEBridgeMode.setStatus("mandatory")


class _GsEBridgeStatus_Type(Integer32):
    """Custom type gsEBridgeStatus based on Integer32"""
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


_GsEBridgeStatus_Type.__name__ = "Integer32"
_GsEBridgeStatus_Object = MibTableColumn
gsEBridgeStatus = _GsEBridgeStatus_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 39, 5, 1, 2, 1, 1, 4),
    _GsEBridgeStatus_Type()
)
gsEBridgeStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gsEBridgeStatus.setStatus("mandatory")


class _GsEBridgeStpPriority_Type(Integer32):
    """Custom type gsEBridgeStpPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_GsEBridgeStpPriority_Type.__name__ = "Integer32"
_GsEBridgeStpPriority_Object = MibTableColumn
gsEBridgeStpPriority = _GsEBridgeStpPriority_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 39, 5, 1, 2, 1, 1, 5),
    _GsEBridgeStpPriority_Type()
)
gsEBridgeStpPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gsEBridgeStpPriority.setStatus("mandatory")
_GsEBridgeStpTimeSinceTopologyChange_Type = TimeTicks
_GsEBridgeStpTimeSinceTopologyChange_Object = MibTableColumn
gsEBridgeStpTimeSinceTopologyChange = _GsEBridgeStpTimeSinceTopologyChange_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 39, 5, 1, 2, 1, 1, 6),
    _GsEBridgeStpTimeSinceTopologyChange_Type()
)
gsEBridgeStpTimeSinceTopologyChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gsEBridgeStpTimeSinceTopologyChange.setStatus("mandatory")
_GsEBridgeStpTopChanges_Type = Counter32
_GsEBridgeStpTopChanges_Object = MibTableColumn
gsEBridgeStpTopChanges = _GsEBridgeStpTopChanges_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 39, 5, 1, 2, 1, 1, 7),
    _GsEBridgeStpTopChanges_Type()
)
gsEBridgeStpTopChanges.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gsEBridgeStpTopChanges.setStatus("mandatory")
_GsEBridgeStpDesignatedRoot_Type = BridgeId
_GsEBridgeStpDesignatedRoot_Object = MibTableColumn
gsEBridgeStpDesignatedRoot = _GsEBridgeStpDesignatedRoot_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 39, 5, 1, 2, 1, 1, 8),
    _GsEBridgeStpDesignatedRoot_Type()
)
gsEBridgeStpDesignatedRoot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gsEBridgeStpDesignatedRoot.setStatus("mandatory")
_GsEBridgeStpRootCost_Type = Integer32
_GsEBridgeStpRootCost_Object = MibTableColumn
gsEBridgeStpRootCost = _GsEBridgeStpRootCost_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 39, 5, 1, 2, 1, 1, 9),
    _GsEBridgeStpRootCost_Type()
)
gsEBridgeStpRootCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gsEBridgeStpRootCost.setStatus("mandatory")
_GsEBridgeStpRootPort_Type = Integer32
_GsEBridgeStpRootPort_Object = MibTableColumn
gsEBridgeStpRootPort = _GsEBridgeStpRootPort_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 39, 5, 1, 2, 1, 1, 10),
    _GsEBridgeStpRootPort_Type()
)
gsEBridgeStpRootPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gsEBridgeStpRootPort.setStatus("mandatory")
_GsEBridgeStpMaxAge_Type = Timeout
_GsEBridgeStpMaxAge_Object = MibTableColumn
gsEBridgeStpMaxAge = _GsEBridgeStpMaxAge_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 39, 5, 1, 2, 1, 1, 11),
    _GsEBridgeStpMaxAge_Type()
)
gsEBridgeStpMaxAge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gsEBridgeStpMaxAge.setStatus("mandatory")
_GsEBridgeStpHelloTime_Type = Timeout
_GsEBridgeStpHelloTime_Object = MibTableColumn
gsEBridgeStpHelloTime = _GsEBridgeStpHelloTime_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 39, 5, 1, 2, 1, 1, 12),
    _GsEBridgeStpHelloTime_Type()
)
gsEBridgeStpHelloTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gsEBridgeStpHelloTime.setStatus("mandatory")
_GsEBridgeStpHoldTime_Type = Integer32
_GsEBridgeStpHoldTime_Object = MibTableColumn
gsEBridgeStpHoldTime = _GsEBridgeStpHoldTime_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 39, 5, 1, 2, 1, 1, 13),
    _GsEBridgeStpHoldTime_Type()
)
gsEBridgeStpHoldTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gsEBridgeStpHoldTime.setStatus("mandatory")
_GsEBridgeStpForwardDelay_Type = Timeout
_GsEBridgeStpForwardDelay_Object = MibTableColumn
gsEBridgeStpForwardDelay = _GsEBridgeStpForwardDelay_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 39, 5, 1, 2, 1, 1, 14),
    _GsEBridgeStpForwardDelay_Type()
)
gsEBridgeStpForwardDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gsEBridgeStpForwardDelay.setStatus("mandatory")


class _GsEBridgeStpBridgeMaxAge_Type(Timeout):
    """Custom type gsEBridgeStpBridgeMaxAge based on Timeout"""
    subtypeSpec = Timeout.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(600, 4000),
    )


_GsEBridgeStpBridgeMaxAge_Type.__name__ = "Timeout"
_GsEBridgeStpBridgeMaxAge_Object = MibTableColumn
gsEBridgeStpBridgeMaxAge = _GsEBridgeStpBridgeMaxAge_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 39, 5, 1, 2, 1, 1, 15),
    _GsEBridgeStpBridgeMaxAge_Type()
)
gsEBridgeStpBridgeMaxAge.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gsEBridgeStpBridgeMaxAge.setStatus("mandatory")


class _GsEBridgeStpBridgeHelloTime_Type(Timeout):
    """Custom type gsEBridgeStpBridgeHelloTime based on Timeout"""
    subtypeSpec = Timeout.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(100, 1000),
    )


_GsEBridgeStpBridgeHelloTime_Type.__name__ = "Timeout"
_GsEBridgeStpBridgeHelloTime_Object = MibTableColumn
gsEBridgeStpBridgeHelloTime = _GsEBridgeStpBridgeHelloTime_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 39, 5, 1, 2, 1, 1, 16),
    _GsEBridgeStpBridgeHelloTime_Type()
)
gsEBridgeStpBridgeHelloTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gsEBridgeStpBridgeHelloTime.setStatus("mandatory")


class _GsEBridgeStpBridgeForwardDelay_Type(Timeout):
    """Custom type gsEBridgeStpBridgeForwardDelay based on Timeout"""
    subtypeSpec = Timeout.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(400, 3000),
    )


_GsEBridgeStpBridgeForwardDelay_Type.__name__ = "Timeout"
_GsEBridgeStpBridgeForwardDelay_Object = MibTableColumn
gsEBridgeStpBridgeForwardDelay = _GsEBridgeStpBridgeForwardDelay_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 39, 5, 1, 2, 1, 1, 17),
    _GsEBridgeStpBridgeForwardDelay_Type()
)
gsEBridgeStpBridgeForwardDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gsEBridgeStpBridgeForwardDelay.setStatus("mandatory")
_GsEBridgePortMgmt_ObjectIdentity = ObjectIdentity
gsEBridgePortMgmt = _GsEBridgePortMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 39, 5, 1, 3)
)
_GsEBridgePortTable_Object = MibTable
gsEBridgePortTable = _GsEBridgePortTable_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 39, 5, 1, 3, 1)
)
if mibBuilder.loadTexts:
    gsEBridgePortTable.setStatus("mandatory")
_GsEBridgePortEntry_Object = MibTableRow
gsEBridgePortEntry = _GsEBridgePortEntry_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 39, 5, 1, 3, 1, 1)
)
gsEBridgePortEntry.setIndexNames(
    (0, "GIGAswitchEthernet-MIB", "gsEBridgePortIndex"),
)
if mibBuilder.loadTexts:
    gsEBridgePortEntry.setStatus("mandatory")
_GsEBridgePortIndex_Type = ResourceId
_GsEBridgePortIndex_Object = MibTableColumn
gsEBridgePortIndex = _GsEBridgePortIndex_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 39, 5, 1, 3, 1, 1, 1),
    _GsEBridgePortIndex_Type()
)
gsEBridgePortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gsEBridgePortIndex.setStatus("mandatory")


class _GsEBridgePortPriority_Type(Integer32):
    """Custom type gsEBridgePortPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_GsEBridgePortPriority_Type.__name__ = "Integer32"
_GsEBridgePortPriority_Object = MibTableColumn
gsEBridgePortPriority = _GsEBridgePortPriority_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 39, 5, 1, 3, 1, 1, 2),
    _GsEBridgePortPriority_Type()
)
gsEBridgePortPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gsEBridgePortPriority.setStatus("mandatory")


class _GsEBridgePortState_Type(Integer32):
    """Custom type gsEBridgePortState based on Integer32"""
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


_GsEBridgePortState_Type.__name__ = "Integer32"
_GsEBridgePortState_Object = MibTableColumn
gsEBridgePortState = _GsEBridgePortState_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 39, 5, 1, 3, 1, 1, 3),
    _GsEBridgePortState_Type()
)
gsEBridgePortState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gsEBridgePortState.setStatus("mandatory")


class _GsEBridgePortEnable_Type(Integer32):
    """Custom type gsEBridgePortEnable based on Integer32"""
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


_GsEBridgePortEnable_Type.__name__ = "Integer32"
_GsEBridgePortEnable_Object = MibTableColumn
gsEBridgePortEnable = _GsEBridgePortEnable_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 39, 5, 1, 3, 1, 1, 4),
    _GsEBridgePortEnable_Type()
)
gsEBridgePortEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gsEBridgePortEnable.setStatus("mandatory")


class _GsEBridgePortPathCost_Type(Integer32):
    """Custom type gsEBridgePortPathCost based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_GsEBridgePortPathCost_Type.__name__ = "Integer32"
_GsEBridgePortPathCost_Object = MibTableColumn
gsEBridgePortPathCost = _GsEBridgePortPathCost_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 39, 5, 1, 3, 1, 1, 5),
    _GsEBridgePortPathCost_Type()
)
gsEBridgePortPathCost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gsEBridgePortPathCost.setStatus("mandatory")
_GsEBridgePortDesignatedRoot_Type = BridgeId
_GsEBridgePortDesignatedRoot_Object = MibTableColumn
gsEBridgePortDesignatedRoot = _GsEBridgePortDesignatedRoot_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 39, 5, 1, 3, 1, 1, 6),
    _GsEBridgePortDesignatedRoot_Type()
)
gsEBridgePortDesignatedRoot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gsEBridgePortDesignatedRoot.setStatus("mandatory")
_GsEBridgePortDesignatedCost_Type = Integer32
_GsEBridgePortDesignatedCost_Object = MibTableColumn
gsEBridgePortDesignatedCost = _GsEBridgePortDesignatedCost_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 39, 5, 1, 3, 1, 1, 7),
    _GsEBridgePortDesignatedCost_Type()
)
gsEBridgePortDesignatedCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gsEBridgePortDesignatedCost.setStatus("mandatory")
_GsEBridgePortDesignatedBridge_Type = BridgeId
_GsEBridgePortDesignatedBridge_Object = MibTableColumn
gsEBridgePortDesignatedBridge = _GsEBridgePortDesignatedBridge_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 39, 5, 1, 3, 1, 1, 8),
    _GsEBridgePortDesignatedBridge_Type()
)
gsEBridgePortDesignatedBridge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gsEBridgePortDesignatedBridge.setStatus("mandatory")


class _GsEBridgePortDesignatedPort_Type(OctetString):
    """Custom type gsEBridgePortDesignatedPort based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_GsEBridgePortDesignatedPort_Type.__name__ = "OctetString"
_GsEBridgePortDesignatedPort_Object = MibTableColumn
gsEBridgePortDesignatedPort = _GsEBridgePortDesignatedPort_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 39, 5, 1, 3, 1, 1, 9),
    _GsEBridgePortDesignatedPort_Type()
)
gsEBridgePortDesignatedPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gsEBridgePortDesignatedPort.setStatus("mandatory")
_GsEBridgePortForwardTransitions_Type = Counter32
_GsEBridgePortForwardTransitions_Object = MibTableColumn
gsEBridgePortForwardTransitions = _GsEBridgePortForwardTransitions_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 39, 5, 1, 3, 1, 1, 10),
    _GsEBridgePortForwardTransitions_Type()
)
gsEBridgePortForwardTransitions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gsEBridgePortForwardTransitions.setStatus("mandatory")


class _GsEBridgePortFastStart_Type(Integer32):
    """Custom type gsEBridgePortFastStart based on Integer32"""
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


_GsEBridgePortFastStart_Type.__name__ = "Integer32"
_GsEBridgePortFastStart_Object = MibTableColumn
gsEBridgePortFastStart = _GsEBridgePortFastStart_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 39, 5, 1, 3, 1, 1, 11),
    _GsEBridgePortFastStart_Type()
)
gsEBridgePortFastStart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gsEBridgePortFastStart.setStatus("deprecated")


class _GsEBridgePortSetDefault_Type(Integer32):
    """Custom type gsEBridgePortSetDefault based on Integer32"""
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


_GsEBridgePortSetDefault_Type.__name__ = "Integer32"
_GsEBridgePortSetDefault_Object = MibTableColumn
gsEBridgePortSetDefault = _GsEBridgePortSetDefault_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 39, 5, 1, 3, 1, 1, 12),
    _GsEBridgePortSetDefault_Type()
)
gsEBridgePortSetDefault.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gsEBridgePortSetDefault.setStatus("mandatory")


class _GsEBridgePortEnableChangeDetection_Type(Integer32):
    """Custom type gsEBridgePortEnableChangeDetection based on Integer32"""
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


_GsEBridgePortEnableChangeDetection_Type.__name__ = "Integer32"
_GsEBridgePortEnableChangeDetection_Object = MibTableColumn
gsEBridgePortEnableChangeDetection = _GsEBridgePortEnableChangeDetection_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 39, 5, 1, 3, 1, 1, 13),
    _GsEBridgePortEnableChangeDetection_Type()
)
gsEBridgePortEnableChangeDetection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gsEBridgePortEnableChangeDetection.setStatus("mandatory")
_GsEL2AddrMgmt_ObjectIdentity = ObjectIdentity
gsEL2AddrMgmt = _GsEL2AddrMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 39, 5, 1, 4)
)
_GsEL2AddrDatabaseMgt_ObjectIdentity = ObjectIdentity
gsEL2AddrDatabaseMgt = _GsEL2AddrDatabaseMgt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 39, 5, 1, 4, 1)
)
_GsEL2AddressTable_Object = MibTable
gsEL2AddressTable = _GsEL2AddressTable_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 39, 5, 1, 4, 1, 1)
)
if mibBuilder.loadTexts:
    gsEL2AddressTable.setStatus("mandatory")
_GsEL2AddressEntry_Object = MibTableRow
gsEL2AddressEntry = _GsEL2AddressEntry_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 39, 5, 1, 4, 1, 1, 1)
)
gsEL2AddressEntry.setIndexNames(
    (0, "GIGAswitchEthernet-MIB", "gsEL2AddressIndex"),
)
if mibBuilder.loadTexts:
    gsEL2AddressEntry.setStatus("mandatory")
_GsEL2AddressIndex_Type = Integer32
_GsEL2AddressIndex_Object = MibTableColumn
gsEL2AddressIndex = _GsEL2AddressIndex_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 39, 5, 1, 4, 1, 1, 1, 1),
    _GsEL2AddressIndex_Type()
)
gsEL2AddressIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gsEL2AddressIndex.setStatus("mandatory")
_GsEL2AddressTableIndex_Type = Integer32
_GsEL2AddressTableIndex_Object = MibTableColumn
gsEL2AddressTableIndex = _GsEL2AddressTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 39, 5, 1, 4, 1, 1, 1, 2),
    _GsEL2AddressTableIndex_Type()
)
gsEL2AddressTableIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gsEL2AddressTableIndex.setStatus("mandatory")
_GsEL2AddressMacAddress_Type = MacAddress
_GsEL2AddressMacAddress_Object = MibTableColumn
gsEL2AddressMacAddress = _GsEL2AddressMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 39, 5, 1, 4, 1, 1, 1, 3),
    _GsEL2AddressMacAddress_Type()
)
gsEL2AddressMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gsEL2AddressMacAddress.setStatus("mandatory")
_GsEL2AddressPortBinding_Type = ResourceId
_GsEL2AddressPortBinding_Object = MibTableColumn
gsEL2AddressPortBinding = _GsEL2AddressPortBinding_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 39, 5, 1, 4, 1, 1, 1, 4),
    _GsEL2AddressPortBinding_Type()
)
gsEL2AddressPortBinding.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gsEL2AddressPortBinding.setStatus("mandatory")


class _GsEL2AddressBindingValid_Type(Integer32):
    """Custom type gsEL2AddressBindingValid based on Integer32"""
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


_GsEL2AddressBindingValid_Type.__name__ = "Integer32"
_GsEL2AddressBindingValid_Object = MibTableColumn
gsEL2AddressBindingValid = _GsEL2AddressBindingValid_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 39, 5, 1, 4, 1, 1, 1, 5),
    _GsEL2AddressBindingValid_Type()
)
gsEL2AddressBindingValid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gsEL2AddressBindingValid.setStatus("mandatory")
_GsEL2AddressVlanID_Type = Integer32
_GsEL2AddressVlanID_Object = MibTableColumn
gsEL2AddressVlanID = _GsEL2AddressVlanID_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 39, 5, 1, 4, 1, 1, 1, 6),
    _GsEL2AddressVlanID_Type()
)
gsEL2AddressVlanID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gsEL2AddressVlanID.setStatus("mandatory")


class _GsEL2AddressPriority_Type(Integer32):
    """Custom type gsEL2AddressPriority based on Integer32"""
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


_GsEL2AddressPriority_Type.__name__ = "Integer32"
_GsEL2AddressPriority_Object = MibTableColumn
gsEL2AddressPriority = _GsEL2AddressPriority_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 39, 5, 1, 4, 1, 1, 1, 7),
    _GsEL2AddressPriority_Type()
)
gsEL2AddressPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gsEL2AddressPriority.setStatus("mandatory")


class _GsEL2AddressForward_Type(Integer32):
    """Custom type gsEL2AddressForward based on Integer32"""
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


_GsEL2AddressForward_Type.__name__ = "Integer32"
_GsEL2AddressForward_Object = MibTableColumn
gsEL2AddressForward = _GsEL2AddressForward_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 39, 5, 1, 4, 1, 1, 1, 8),
    _GsEL2AddressForward_Type()
)
gsEL2AddressForward.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gsEL2AddressForward.setStatus("mandatory")


class _GsEL2AddressCopy_Type(Integer32):
    """Custom type gsEL2AddressCopy based on Integer32"""
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


_GsEL2AddressCopy_Type.__name__ = "Integer32"
_GsEL2AddressCopy_Object = MibTableColumn
gsEL2AddressCopy = _GsEL2AddressCopy_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 39, 5, 1, 4, 1, 1, 1, 9),
    _GsEL2AddressCopy_Type()
)
gsEL2AddressCopy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gsEL2AddressCopy.setStatus("mandatory")


class _GsEL2AddressPersistence_Type(Integer32):
    """Custom type gsEL2AddressPersistence based on Integer32"""
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


_GsEL2AddressPersistence_Type.__name__ = "Integer32"
_GsEL2AddressPersistence_Object = MibTableColumn
gsEL2AddressPersistence = _GsEL2AddressPersistence_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 39, 5, 1, 4, 1, 1, 1, 10),
    _GsEL2AddressPersistence_Type()
)
gsEL2AddressPersistence.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gsEL2AddressPersistence.setStatus("mandatory")


class _GsEL2AddressStatus_Type(Integer32):
    """Custom type gsEL2AddressStatus based on Integer32"""
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


_GsEL2AddressStatus_Type.__name__ = "Integer32"
_GsEL2AddressStatus_Object = MibTableColumn
gsEL2AddressStatus = _GsEL2AddressStatus_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 39, 5, 1, 4, 1, 1, 1, 11),
    _GsEL2AddressStatus_Type()
)
gsEL2AddressStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gsEL2AddressStatus.setStatus("mandatory")
_GsEL2AddrSummaryMgt_ObjectIdentity = ObjectIdentity
gsEL2AddrSummaryMgt = _GsEL2AddrSummaryMgt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 39, 5, 1, 4, 2)
)
_GsEL2AddrSummaryTable_Object = MibTable
gsEL2AddrSummaryTable = _GsEL2AddrSummaryTable_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 39, 5, 1, 4, 2, 1)
)
if mibBuilder.loadTexts:
    gsEL2AddrSummaryTable.setStatus("mandatory")
_GsEL2AddrSummaryEntry_Object = MibTableRow
gsEL2AddrSummaryEntry = _GsEL2AddrSummaryEntry_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 39, 5, 1, 4, 2, 1, 1)
)
gsEL2AddrSummaryEntry.setIndexNames(
    (0, "GIGAswitchEthernet-MIB", "gsEL2AddressIndex"),
)
if mibBuilder.loadTexts:
    gsEL2AddrSummaryEntry.setStatus("mandatory")


class _GsEL2AddrSummary_Type(OctetString):
    """Custom type gsEL2AddrSummary based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(20, 4096),
    )


_GsEL2AddrSummary_Type.__name__ = "OctetString"
_GsEL2AddrSummary_Object = MibTableColumn
gsEL2AddrSummary = _GsEL2AddrSummary_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 39, 5, 1, 4, 2, 1, 1, 1),
    _GsEL2AddrSummary_Type()
)
gsEL2AddrSummary.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gsEL2AddrSummary.setStatus("mandatory")
_GsEL2AddrControlMgt_ObjectIdentity = ObjectIdentity
gsEL2AddrControlMgt = _GsEL2AddrControlMgt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 39, 5, 1, 4, 3)
)
_GsEL2AddressControlTable_Object = MibTable
gsEL2AddressControlTable = _GsEL2AddressControlTable_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 39, 5, 1, 4, 3, 1)
)
if mibBuilder.loadTexts:
    gsEL2AddressControlTable.setStatus("mandatory")
_GsEL2AddressControlEntry_Object = MibTableRow
gsEL2AddressControlEntry = _GsEL2AddressControlEntry_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 39, 5, 1, 4, 3, 1, 1)
)
gsEL2AddressControlEntry.setIndexNames(
    (0, "GIGAswitchEthernet-MIB", "gsEAgentMgrIndex"),
)
if mibBuilder.loadTexts:
    gsEL2AddressControlEntry.setStatus("mandatory")
_GsEL2AddressControlIndex_Type = Integer32
_GsEL2AddressControlIndex_Object = MibTableColumn
gsEL2AddressControlIndex = _GsEL2AddressControlIndex_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 39, 5, 1, 4, 3, 1, 1, 1),
    _GsEL2AddressControlIndex_Type()
)
gsEL2AddressControlIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gsEL2AddressControlIndex.setStatus("mandatory")
_GsEL2AddressControlMacAddress_Type = MacAddress
_GsEL2AddressControlMacAddress_Object = MibTableColumn
gsEL2AddressControlMacAddress = _GsEL2AddressControlMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 39, 5, 1, 4, 3, 1, 1, 2),
    _GsEL2AddressControlMacAddress_Type()
)
gsEL2AddressControlMacAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gsEL2AddressControlMacAddress.setStatus("mandatory")
_GsEL2AddressControlPortBinding_Type = ResourceId
_GsEL2AddressControlPortBinding_Object = MibTableColumn
gsEL2AddressControlPortBinding = _GsEL2AddressControlPortBinding_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 39, 5, 1, 4, 3, 1, 1, 3),
    _GsEL2AddressControlPortBinding_Type()
)
gsEL2AddressControlPortBinding.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gsEL2AddressControlPortBinding.setStatus("mandatory")
_GsEL2AddressControlVlanID_Type = Integer32
_GsEL2AddressControlVlanID_Object = MibTableColumn
gsEL2AddressControlVlanID = _GsEL2AddressControlVlanID_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 39, 5, 1, 4, 3, 1, 1, 4),
    _GsEL2AddressControlVlanID_Type()
)
gsEL2AddressControlVlanID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gsEL2AddressControlVlanID.setStatus("mandatory")


class _GsEL2AddressControlPriority_Type(Integer32):
    """Custom type gsEL2AddressControlPriority based on Integer32"""
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


_GsEL2AddressControlPriority_Type.__name__ = "Integer32"
_GsEL2AddressControlPriority_Object = MibTableColumn
gsEL2AddressControlPriority = _GsEL2AddressControlPriority_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 39, 5, 1, 4, 3, 1, 1, 5),
    _GsEL2AddressControlPriority_Type()
)
gsEL2AddressControlPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gsEL2AddressControlPriority.setStatus("mandatory")


class _GsEL2AddressControlPersistence_Type(Integer32):
    """Custom type gsEL2AddressControlPersistence based on Integer32"""
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


_GsEL2AddressControlPersistence_Type.__name__ = "Integer32"
_GsEL2AddressControlPersistence_Object = MibTableColumn
gsEL2AddressControlPersistence = _GsEL2AddressControlPersistence_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 39, 5, 1, 4, 3, 1, 1, 6),
    _GsEL2AddressControlPersistence_Type()
)
gsEL2AddressControlPersistence.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gsEL2AddressControlPersistence.setStatus("mandatory")


class _GsEL2AddressControlStatus_Type(Integer32):
    """Custom type gsEL2AddressControlStatus based on Integer32"""
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


_GsEL2AddressControlStatus_Type.__name__ = "Integer32"
_GsEL2AddressControlStatus_Object = MibTableColumn
gsEL2AddressControlStatus = _GsEL2AddressControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 39, 5, 1, 4, 3, 1, 1, 7),
    _GsEL2AddressControlStatus_Type()
)
gsEL2AddressControlStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gsEL2AddressControlStatus.setStatus("mandatory")
_GsEL2AddrChangeMgt_ObjectIdentity = ObjectIdentity
gsEL2AddrChangeMgt = _GsEL2AddrChangeMgt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 39, 5, 1, 4, 4)
)
_GsEL2AddressChangeLast_Type = Integer32
_GsEL2AddressChangeLast_Object = MibScalar
gsEL2AddressChangeLast = _GsEL2AddressChangeLast_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 39, 5, 1, 4, 4, 1),
    _GsEL2AddressChangeLast_Type()
)
gsEL2AddressChangeLast.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gsEL2AddressChangeLast.setStatus("mandatory")
_GsEL2AddressChangeWraps_Type = Counter32
_GsEL2AddressChangeWraps_Object = MibScalar
gsEL2AddressChangeWraps = _GsEL2AddressChangeWraps_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 39, 5, 1, 4, 4, 2),
    _GsEL2AddressChangeWraps_Type()
)
gsEL2AddressChangeWraps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gsEL2AddressChangeWraps.setStatus("mandatory")


class _GsEL2AddressChangeMaxEntries_Type(Integer32):
    """Custom type gsEL2AddressChangeMaxEntries based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1024, 4096),
    )


_GsEL2AddressChangeMaxEntries_Type.__name__ = "Integer32"
_GsEL2AddressChangeMaxEntries_Object = MibScalar
gsEL2AddressChangeMaxEntries = _GsEL2AddressChangeMaxEntries_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 39, 5, 1, 4, 4, 3),
    _GsEL2AddressChangeMaxEntries_Type()
)
gsEL2AddressChangeMaxEntries.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gsEL2AddressChangeMaxEntries.setStatus("mandatory")
_GsEL2AddressChangeTable_Object = MibTable
gsEL2AddressChangeTable = _GsEL2AddressChangeTable_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 39, 5, 1, 4, 4, 4)
)
if mibBuilder.loadTexts:
    gsEL2AddressChangeTable.setStatus("mandatory")
_GsEL2AddressChangeEntry_Object = MibTableRow
gsEL2AddressChangeEntry = _GsEL2AddressChangeEntry_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 39, 5, 1, 4, 4, 4, 1)
)
gsEL2AddressChangeEntry.setIndexNames(
    (0, "GIGAswitchEthernet-MIB", "gsEL2AddressChangeWrapCount"),
    (0, "GIGAswitchEthernet-MIB", "gsEL2AddressChangeIndex"),
)
if mibBuilder.loadTexts:
    gsEL2AddressChangeEntry.setStatus("mandatory")
_GsEL2AddressChangeWrapCount_Type = Integer32
_GsEL2AddressChangeWrapCount_Object = MibTableColumn
gsEL2AddressChangeWrapCount = _GsEL2AddressChangeWrapCount_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 39, 5, 1, 4, 4, 4, 1, 1),
    _GsEL2AddressChangeWrapCount_Type()
)
gsEL2AddressChangeWrapCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gsEL2AddressChangeWrapCount.setStatus("mandatory")
_GsEL2AddressChangeIndex_Type = Integer32
_GsEL2AddressChangeIndex_Object = MibTableColumn
gsEL2AddressChangeIndex = _GsEL2AddressChangeIndex_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 39, 5, 1, 4, 4, 4, 1, 2),
    _GsEL2AddressChangeIndex_Type()
)
gsEL2AddressChangeIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gsEL2AddressChangeIndex.setStatus("mandatory")
_GsEL2AddressChangeIndexChanged_Type = Integer32
_GsEL2AddressChangeIndexChanged_Object = MibTableColumn
gsEL2AddressChangeIndexChanged = _GsEL2AddressChangeIndexChanged_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 39, 5, 1, 4, 4, 4, 1, 3),
    _GsEL2AddressChangeIndexChanged_Type()
)
gsEL2AddressChangeIndexChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gsEL2AddressChangeIndexChanged.setStatus("mandatory")


class _GsEL2AddressChangeSummary_Type(OctetString):
    """Custom type gsEL2AddressChangeSummary based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(20, 20),
    )


_GsEL2AddressChangeSummary_Type.__name__ = "OctetString"
_GsEL2AddressChangeSummary_Object = MibTableColumn
gsEL2AddressChangeSummary = _GsEL2AddressChangeSummary_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 39, 5, 1, 4, 4, 4, 1, 4),
    _GsEL2AddressChangeSummary_Type()
)
gsEL2AddressChangeSummary.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gsEL2AddressChangeSummary.setStatus("mandatory")
_GsESwitchPortMgt_ObjectIdentity = ObjectIdentity
gsESwitchPortMgt = _GsESwitchPortMgt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 39, 5, 2)
)
_GsESwitchPortTable_Object = MibTable
gsESwitchPortTable = _GsESwitchPortTable_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 39, 5, 2, 1)
)
if mibBuilder.loadTexts:
    gsESwitchPortTable.setStatus("mandatory")
_GsESwitchPortEntry_Object = MibTableRow
gsESwitchPortEntry = _GsESwitchPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 39, 5, 2, 1, 1)
)
gsESwitchPortEntry.setIndexNames(
    (0, "GIGAswitchEthernet-MIB", "gsESwitchPortIndex"),
)
if mibBuilder.loadTexts:
    gsESwitchPortEntry.setStatus("mandatory")
_GsESwitchPortIndex_Type = ResourceId
_GsESwitchPortIndex_Object = MibTableColumn
gsESwitchPortIndex = _GsESwitchPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 39, 5, 2, 1, 1, 1),
    _GsESwitchPortIndex_Type()
)
gsESwitchPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gsESwitchPortIndex.setStatus("mandatory")


class _GsESwitchPortSTAPMode_Type(Integer32):
    """Custom type gsESwitchPortSTAPMode based on Integer32"""
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


_GsESwitchPortSTAPMode_Type.__name__ = "Integer32"
_GsESwitchPortSTAPMode_Object = MibTableColumn
gsESwitchPortSTAPMode = _GsESwitchPortSTAPMode_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 39, 5, 2, 1, 1, 2),
    _GsESwitchPortSTAPMode_Type()
)
gsESwitchPortSTAPMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gsESwitchPortSTAPMode.setStatus("mandatory")


class _GsESwitchPortConvertToStatic_Type(Integer32):
    """Custom type gsESwitchPortConvertToStatic based on Integer32"""
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


_GsESwitchPortConvertToStatic_Type.__name__ = "Integer32"
_GsESwitchPortConvertToStatic_Object = MibTableColumn
gsESwitchPortConvertToStatic = _GsESwitchPortConvertToStatic_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 39, 5, 2, 1, 1, 3),
    _GsESwitchPortConvertToStatic_Type()
)
gsESwitchPortConvertToStatic.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gsESwitchPortConvertToStatic.setStatus("mandatory")


class _GsESwitchPortLearningMode_Type(Integer32):
    """Custom type gsESwitchPortLearningMode based on Integer32"""
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


_GsESwitchPortLearningMode_Type.__name__ = "Integer32"
_GsESwitchPortLearningMode_Object = MibTableColumn
gsESwitchPortLearningMode = _GsESwitchPortLearningMode_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 39, 5, 2, 1, 1, 4),
    _GsESwitchPortLearningMode_Type()
)
gsESwitchPortLearningMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gsESwitchPortLearningMode.setStatus("mandatory")
_GsESwitchPortHuntGroup_Type = Integer32
_GsESwitchPortHuntGroup_Object = MibTableColumn
gsESwitchPortHuntGroup = _GsESwitchPortHuntGroup_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 39, 5, 2, 1, 1, 5),
    _GsESwitchPortHuntGroup_Type()
)
gsESwitchPortHuntGroup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gsESwitchPortHuntGroup.setStatus("mandatory")
_GsESwitchPortPhysicalPort_Type = ResourceId
_GsESwitchPortPhysicalPort_Object = MibTableColumn
gsESwitchPortPhysicalPort = _GsESwitchPortPhysicalPort_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 39, 5, 2, 1, 1, 6),
    _GsESwitchPortPhysicalPort_Type()
)
gsESwitchPortPhysicalPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gsESwitchPortPhysicalPort.setStatus("mandatory")


class _GsESwitchPortKnownMode_Type(Integer32):
    """Custom type gsESwitchPortKnownMode based on Integer32"""
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


_GsESwitchPortKnownMode_Type.__name__ = "Integer32"
_GsESwitchPortKnownMode_Object = MibTableColumn
gsESwitchPortKnownMode = _GsESwitchPortKnownMode_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 39, 5, 2, 1, 1, 7),
    _GsESwitchPortKnownMode_Type()
)
gsESwitchPortKnownMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gsESwitchPortKnownMode.setStatus("mandatory")


class _GsESwitchPortMappingMethod_Type(Integer32):
    """Custom type gsESwitchPortMappingMethod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("port-based", 1)
    )


_GsESwitchPortMappingMethod_Type.__name__ = "Integer32"
_GsESwitchPortMappingMethod_Object = MibTableColumn
gsESwitchPortMappingMethod = _GsESwitchPortMappingMethod_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 39, 5, 2, 1, 1, 8),
    _GsESwitchPortMappingMethod_Type()
)
gsESwitchPortMappingMethod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gsESwitchPortMappingMethod.setStatus("mandatory")


class _GsESwitchPortTrunkingMode_Type(Integer32):
    """Custom type gsESwitchPortTrunkingMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("clear", 1),
          ("ieee8021q", 2))
    )


_GsESwitchPortTrunkingMode_Type.__name__ = "Integer32"
_GsESwitchPortTrunkingMode_Object = MibTableColumn
gsESwitchPortTrunkingMode = _GsESwitchPortTrunkingMode_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 39, 5, 2, 1, 1, 9),
    _GsESwitchPortTrunkingMode_Type()
)
gsESwitchPortTrunkingMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gsESwitchPortTrunkingMode.setStatus("mandatory")


class _GsESwitchPortVlanBindingMethod_Type(Integer32):
    """Custom type gsESwitchPortVlanBindingMethod based on Integer32"""
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


_GsESwitchPortVlanBindingMethod_Type.__name__ = "Integer32"
_GsESwitchPortVlanBindingMethod_Object = MibTableColumn
gsESwitchPortVlanBindingMethod = _GsESwitchPortVlanBindingMethod_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 39, 5, 2, 1, 1, 10),
    _GsESwitchPortVlanBindingMethod_Type()
)
gsESwitchPortVlanBindingMethod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gsESwitchPortVlanBindingMethod.setStatus("mandatory")


class _GsESwitchPortIgnoreTag_Type(Integer32):
    """Custom type gsESwitchPortIgnoreTag based on Integer32"""
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


_GsESwitchPortIgnoreTag_Type.__name__ = "Integer32"
_GsESwitchPortIgnoreTag_Object = MibTableColumn
gsESwitchPortIgnoreTag = _GsESwitchPortIgnoreTag_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 39, 5, 2, 1, 1, 11),
    _GsESwitchPortIgnoreTag_Type()
)
gsESwitchPortIgnoreTag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gsESwitchPortIgnoreTag.setStatus("mandatory")
_GsESwitchPortVlanID_Type = Integer32
_GsESwitchPortVlanID_Object = MibTableColumn
gsESwitchPortVlanID = _GsESwitchPortVlanID_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 39, 5, 2, 1, 1, 12),
    _GsESwitchPortVlanID_Type()
)
gsESwitchPortVlanID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gsESwitchPortVlanID.setStatus("mandatory")


class _GsESwitchPortAutoVlanCreation_Type(Integer32):
    """Custom type gsESwitchPortAutoVlanCreation based on Integer32"""
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


_GsESwitchPortAutoVlanCreation_Type.__name__ = "Integer32"
_GsESwitchPortAutoVlanCreation_Object = MibTableColumn
gsESwitchPortAutoVlanCreation = _GsESwitchPortAutoVlanCreation_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 39, 5, 2, 1, 1, 14),
    _GsESwitchPortAutoVlanCreation_Type()
)
gsESwitchPortAutoVlanCreation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gsESwitchPortAutoVlanCreation.setStatus("mandatory")


class _GsESwitchPortMirrorMode_Type(Integer32):
    """Custom type gsESwitchPortMirrorMode based on Integer32"""
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


_GsESwitchPortMirrorMode_Type.__name__ = "Integer32"
_GsESwitchPortMirrorMode_Object = MibScalar
gsESwitchPortMirrorMode = _GsESwitchPortMirrorMode_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 39, 5, 2, 1, 1, 15),
    _GsESwitchPortMirrorMode_Type()
)
gsESwitchPortMirrorMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gsESwitchPortMirrorMode.setStatus("mandatory")
_GsESwitchPortIfIndex_Type = Integer32
_GsESwitchPortIfIndex_Object = MibTableColumn
gsESwitchPortIfIndex = _GsESwitchPortIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 39, 5, 2, 1, 1, 16),
    _GsESwitchPortIfIndex_Type()
)
gsESwitchPortIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gsESwitchPortIfIndex.setStatus("mandatory")


class _GsESwitchPortFastStart_Type(Integer32):
    """Custom type gsESwitchPortFastStart based on Integer32"""
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


_GsESwitchPortFastStart_Type.__name__ = "Integer32"
_GsESwitchPortFastStart_Object = MibTableColumn
gsESwitchPortFastStart = _GsESwitchPortFastStart_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 39, 5, 2, 1, 1, 17),
    _GsESwitchPortFastStart_Type()
)
gsESwitchPortFastStart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gsESwitchPortFastStart.setStatus("mandatory")
_GsEHuntGroupMgt_ObjectIdentity = ObjectIdentity
gsEHuntGroupMgt = _GsEHuntGroupMgt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 39, 5, 4)
)
_GsEHuntGroupTable_Object = MibTable
gsEHuntGroupTable = _GsEHuntGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 39, 5, 4, 1)
)
if mibBuilder.loadTexts:
    gsEHuntGroupTable.setStatus("mandatory")
_GsEHuntGroupEntry_Object = MibTableRow
gsEHuntGroupEntry = _GsEHuntGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 39, 5, 4, 1, 1)
)
gsEHuntGroupEntry.setIndexNames(
    (0, "GIGAswitchEthernet-MIB", "gsEHuntGroupIndex"),
)
if mibBuilder.loadTexts:
    gsEHuntGroupEntry.setStatus("mandatory")
_GsEHuntGroupIndex_Type = Integer32
_GsEHuntGroupIndex_Object = MibTableColumn
gsEHuntGroupIndex = _GsEHuntGroupIndex_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 39, 5, 4, 1, 1, 1),
    _GsEHuntGroupIndex_Type()
)
gsEHuntGroupIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gsEHuntGroupIndex.setStatus("mandatory")
_GsEHuntGroupName_Type = DisplayString
_GsEHuntGroupName_Object = MibTableColumn
gsEHuntGroupName = _GsEHuntGroupName_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 39, 5, 4, 1, 1, 2),
    _GsEHuntGroupName_Type()
)
gsEHuntGroupName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gsEHuntGroupName.setStatus("mandatory")
_GsEHuntGroupBasePort_Type = ResourceId
_GsEHuntGroupBasePort_Object = MibTableColumn
gsEHuntGroupBasePort = _GsEHuntGroupBasePort_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 39, 5, 4, 1, 1, 3),
    _GsEHuntGroupBasePort_Type()
)
gsEHuntGroupBasePort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gsEHuntGroupBasePort.setStatus("mandatory")
_GsEHuntGroupNumberOfPorts_Type = Integer32
_GsEHuntGroupNumberOfPorts_Object = MibTableColumn
gsEHuntGroupNumberOfPorts = _GsEHuntGroupNumberOfPorts_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 39, 5, 4, 1, 1, 4),
    _GsEHuntGroupNumberOfPorts_Type()
)
gsEHuntGroupNumberOfPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gsEHuntGroupNumberOfPorts.setStatus("mandatory")


class _GsEHuntGroupLoadSharing_Type(Integer32):
    """Custom type gsEHuntGroupLoadSharing based on Integer32"""
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


_GsEHuntGroupLoadSharing_Type.__name__ = "Integer32"
_GsEHuntGroupLoadSharing_Object = MibTableColumn
gsEHuntGroupLoadSharing = _GsEHuntGroupLoadSharing_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 39, 5, 4, 1, 1, 5),
    _GsEHuntGroupLoadSharing_Type()
)
gsEHuntGroupLoadSharing.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gsEHuntGroupLoadSharing.setStatus("mandatory")


class _GsEHuntGroupStatus_Type(Integer32):
    """Custom type gsEHuntGroupStatus based on Integer32"""
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


_GsEHuntGroupStatus_Type.__name__ = "Integer32"
_GsEHuntGroupStatus_Object = MibTableColumn
gsEHuntGroupStatus = _GsEHuntGroupStatus_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 39, 5, 4, 1, 1, 6),
    _GsEHuntGroupStatus_Type()
)
gsEHuntGroupStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gsEHuntGroupStatus.setStatus("mandatory")
_GsEPortMirroringMgt_ObjectIdentity = ObjectIdentity
gsEPortMirroringMgt = _GsEPortMirroringMgt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 39, 5, 5)
)
_GsEPortMirroringTable_Object = MibTable
gsEPortMirroringTable = _GsEPortMirroringTable_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 39, 5, 5, 1)
)
if mibBuilder.loadTexts:
    gsEPortMirroringTable.setStatus("mandatory")
_GsEPortMirroringEntry_Object = MibTableRow
gsEPortMirroringEntry = _GsEPortMirroringEntry_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 39, 5, 5, 1, 1)
)
gsEPortMirroringEntry.setIndexNames(
    (0, "GIGAswitchEthernet-MIB", "gsEPortMirroringIndex"),
)
if mibBuilder.loadTexts:
    gsEPortMirroringEntry.setStatus("mandatory")
_GsEPortMirroringIndex_Type = ResourceId
_GsEPortMirroringIndex_Object = MibTableColumn
gsEPortMirroringIndex = _GsEPortMirroringIndex_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 39, 5, 5, 1, 1, 1),
    _GsEPortMirroringIndex_Type()
)
gsEPortMirroringIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gsEPortMirroringIndex.setStatus("mandatory")
_GsEPortMirroringSourceSubPort_Type = Integer32
_GsEPortMirroringSourceSubPort_Object = MibTableColumn
gsEPortMirroringSourceSubPort = _GsEPortMirroringSourceSubPort_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 39, 5, 5, 1, 1, 2),
    _GsEPortMirroringSourceSubPort_Type()
)
gsEPortMirroringSourceSubPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gsEPortMirroringSourceSubPort.setStatus("mandatory")


class _GsEPortMirroringSamplerType_Type(Integer32):
    """Custom type gsEPortMirroringSamplerType based on Integer32"""
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


_GsEPortMirroringSamplerType_Type.__name__ = "Integer32"
_GsEPortMirroringSamplerType_Object = MibTableColumn
gsEPortMirroringSamplerType = _GsEPortMirroringSamplerType_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 39, 5, 5, 1, 1, 3),
    _GsEPortMirroringSamplerType_Type()
)
gsEPortMirroringSamplerType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gsEPortMirroringSamplerType.setStatus("mandatory")
_GsEPortMirroringRate_Type = Integer32
_GsEPortMirroringRate_Object = MibTableColumn
gsEPortMirroringRate = _GsEPortMirroringRate_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 39, 5, 5, 1, 1, 4),
    _GsEPortMirroringRate_Type()
)
gsEPortMirroringRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gsEPortMirroringRate.setStatus("mandatory")
_GsEPortMirroringMirrorPort_Type = ResourceId
_GsEPortMirroringMirrorPort_Object = MibTableColumn
gsEPortMirroringMirrorPort = _GsEPortMirroringMirrorPort_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 39, 5, 5, 1, 1, 5),
    _GsEPortMirroringMirrorPort_Type()
)
gsEPortMirroringMirrorPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gsEPortMirroringMirrorPort.setStatus("mandatory")
_GsEVlanMgt_ObjectIdentity = ObjectIdentity
gsEVlanMgt = _GsEVlanMgt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 39, 7)
)
_GsEVlans_ObjectIdentity = ObjectIdentity
gsEVlans = _GsEVlans_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 39, 7, 1)
)
_GsEVlanTable_Object = MibTable
gsEVlanTable = _GsEVlanTable_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 39, 7, 1, 1)
)
if mibBuilder.loadTexts:
    gsEVlanTable.setStatus("mandatory")
_GsEVlanEntry_Object = MibTableRow
gsEVlanEntry = _GsEVlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 39, 7, 1, 1, 1)
)
gsEVlanEntry.setIndexNames(
    (0, "GIGAswitchEthernet-MIB", "gsEVlanID"),
)
if mibBuilder.loadTexts:
    gsEVlanEntry.setStatus("mandatory")
_GsEVlanID_Type = Integer32
_GsEVlanID_Object = MibTableColumn
gsEVlanID = _GsEVlanID_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 39, 7, 1, 1, 1, 1),
    _GsEVlanID_Type()
)
gsEVlanID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gsEVlanID.setStatus("mandatory")


class _GsEVlanName_Type(DisplayString):
    """Custom type gsEVlanName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_GsEVlanName_Type.__name__ = "DisplayString"
_GsEVlanName_Object = MibTableColumn
gsEVlanName = _GsEVlanName_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 39, 7, 1, 1, 1, 2),
    _GsEVlanName_Type()
)
gsEVlanName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gsEVlanName.setStatus("mandatory")
_GsEVlanIfIndex_Type = Integer32
_GsEVlanIfIndex_Object = MibTableColumn
gsEVlanIfIndex = _GsEVlanIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 39, 7, 1, 1, 1, 3),
    _GsEVlanIfIndex_Type()
)
gsEVlanIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gsEVlanIfIndex.setStatus("mandatory")
_GsEVlanAFTIndex_Type = Integer32
_GsEVlanAFTIndex_Object = MibTableColumn
gsEVlanAFTIndex = _GsEVlanAFTIndex_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 39, 7, 1, 1, 1, 4),
    _GsEVlanAFTIndex_Type()
)
gsEVlanAFTIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gsEVlanAFTIndex.setStatus("mandatory")
_GsEVlanBridgeIndex_Type = ResourceId
_GsEVlanBridgeIndex_Object = MibTableColumn
gsEVlanBridgeIndex = _GsEVlanBridgeIndex_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 39, 7, 1, 1, 1, 5),
    _GsEVlanBridgeIndex_Type()
)
gsEVlanBridgeIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gsEVlanBridgeIndex.setStatus("mandatory")


class _GsEVlanStatus_Type(Integer32):
    """Custom type gsEVlanStatus based on Integer32"""
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


_GsEVlanStatus_Type.__name__ = "Integer32"
_GsEVlanStatus_Object = MibTableColumn
gsEVlanStatus = _GsEVlanStatus_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 39, 7, 1, 1, 1, 6),
    _GsEVlanStatus_Type()
)
gsEVlanStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gsEVlanStatus.setStatus("mandatory")


class _GsEVlanInitialHashTableSize_Type(Integer32):
    """Custom type gsEVlanInitialHashTableSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(16, 8192),
    )


_GsEVlanInitialHashTableSize_Type.__name__ = "Integer32"
_GsEVlanInitialHashTableSize_Object = MibTableColumn
gsEVlanInitialHashTableSize = _GsEVlanInitialHashTableSize_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 39, 7, 1, 1, 1, 7),
    _GsEVlanInitialHashTableSize_Type()
)
gsEVlanInitialHashTableSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gsEVlanInitialHashTableSize.setStatus("mandatory")


class _GsEVlanAutoIncrementHTSize_Type(Integer32):
    """Custom type gsEVlanAutoIncrementHTSize based on Integer32"""
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


_GsEVlanAutoIncrementHTSize_Type.__name__ = "Integer32"
_GsEVlanAutoIncrementHTSize_Object = MibTableColumn
gsEVlanAutoIncrementHTSize = _GsEVlanAutoIncrementHTSize_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 39, 7, 1, 1, 1, 8),
    _GsEVlanAutoIncrementHTSize_Type()
)
gsEVlanAutoIncrementHTSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gsEVlanAutoIncrementHTSize.setStatus("mandatory")
_GsEVirtualPorts_ObjectIdentity = ObjectIdentity
gsEVirtualPorts = _GsEVirtualPorts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 39, 7, 4)
)
_GsEVirtualSwitchPortTable_Object = MibTable
gsEVirtualSwitchPortTable = _GsEVirtualSwitchPortTable_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 39, 7, 4, 1)
)
if mibBuilder.loadTexts:
    gsEVirtualSwitchPortTable.setStatus("mandatory")
_GsEVirtualSwitchPortEntry_Object = MibTableRow
gsEVirtualSwitchPortEntry = _GsEVirtualSwitchPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 39, 7, 4, 1, 1)
)
gsEVirtualSwitchPortEntry.setIndexNames(
    (0, "GIGAswitchEthernet-MIB", "gsEVirtualSwitchPortIndex"),
)
if mibBuilder.loadTexts:
    gsEVirtualSwitchPortEntry.setStatus("mandatory")
_GsEVirtualSwitchPortIndex_Type = ResourceId
_GsEVirtualSwitchPortIndex_Object = MibTableColumn
gsEVirtualSwitchPortIndex = _GsEVirtualSwitchPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 39, 7, 4, 1, 1, 1),
    _GsEVirtualSwitchPortIndex_Type()
)
gsEVirtualSwitchPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gsEVirtualSwitchPortIndex.setStatus("mandatory")


class _GsEVirtualSwitchPortFormat_Type(Integer32):
    """Custom type gsEVirtualSwitchPortFormat based on Integer32"""
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


_GsEVirtualSwitchPortFormat_Type.__name__ = "Integer32"
_GsEVirtualSwitchPortFormat_Object = MibTableColumn
gsEVirtualSwitchPortFormat = _GsEVirtualSwitchPortFormat_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 39, 7, 4, 1, 1, 2),
    _GsEVirtualSwitchPortFormat_Type()
)
gsEVirtualSwitchPortFormat.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gsEVirtualSwitchPortFormat.setStatus("mandatory")
_GsEVirtualSwitchPortBridgePort_Type = ResourceId
_GsEVirtualSwitchPortBridgePort_Object = MibTableColumn
gsEVirtualSwitchPortBridgePort = _GsEVirtualSwitchPortBridgePort_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 39, 7, 4, 1, 1, 3),
    _GsEVirtualSwitchPortBridgePort_Type()
)
gsEVirtualSwitchPortBridgePort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gsEVirtualSwitchPortBridgePort.setStatus("mandatory")


class _GsEVirtualSwitchPortBindingType_Type(Integer32):
    """Custom type gsEVirtualSwitchPortBindingType based on Integer32"""
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


_GsEVirtualSwitchPortBindingType_Type.__name__ = "Integer32"
_GsEVirtualSwitchPortBindingType_Object = MibTableColumn
gsEVirtualSwitchPortBindingType = _GsEVirtualSwitchPortBindingType_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 39, 7, 4, 1, 1, 4),
    _GsEVirtualSwitchPortBindingType_Type()
)
gsEVirtualSwitchPortBindingType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gsEVirtualSwitchPortBindingType.setStatus("mandatory")


class _GsEVirtualSwitchPortStatus_Type(Integer32):
    """Custom type gsEVirtualSwitchPortStatus based on Integer32"""
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


_GsEVirtualSwitchPortStatus_Type.__name__ = "Integer32"
_GsEVirtualSwitchPortStatus_Object = MibTableColumn
gsEVirtualSwitchPortStatus = _GsEVirtualSwitchPortStatus_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 39, 7, 4, 1, 1, 5),
    _GsEVirtualSwitchPortStatus_Type()
)
gsEVirtualSwitchPortStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gsEVirtualSwitchPortStatus.setStatus("mandatory")
_GsEEvents_ObjectIdentity = ObjectIdentity
gsEEvents = _GsEEvents_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 39, 10)
)
_GsEEventMgt_ObjectIdentity = ObjectIdentity
gsEEventMgt = _GsEEventMgt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 39, 10, 1)
)
_GsEEventTable_Object = MibTable
gsEEventTable = _GsEEventTable_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 39, 10, 1, 1)
)
if mibBuilder.loadTexts:
    gsEEventTable.setStatus("mandatory")
_GsEEventEntry_Object = MibTableRow
gsEEventEntry = _GsEEventEntry_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 39, 10, 1, 1, 1)
)
gsEEventEntry.setIndexNames(
    (0, "GIGAswitchEthernet-MIB", "gsEEventIndex"),
)
if mibBuilder.loadTexts:
    gsEEventEntry.setStatus("mandatory")
_GsEEventIndex_Type = Integer32
_GsEEventIndex_Object = MibTableColumn
gsEEventIndex = _GsEEventIndex_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 39, 10, 1, 1, 1, 1),
    _GsEEventIndex_Type()
)
gsEEventIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gsEEventIndex.setStatus("mandatory")


class _GsEEventMode_Type(Integer32):
    """Custom type gsEEventMode based on Integer32"""
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


_GsEEventMode_Type.__name__ = "Integer32"
_GsEEventMode_Object = MibTableColumn
gsEEventMode = _GsEEventMode_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 39, 10, 1, 1, 1, 2),
    _GsEEventMode_Type()
)
gsEEventMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gsEEventMode.setStatus("mandatory")


class _GsEEventLogAction_Type(Integer32):
    """Custom type gsEEventLogAction based on Integer32"""
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


_GsEEventLogAction_Type.__name__ = "Integer32"
_GsEEventLogAction_Object = MibTableColumn
gsEEventLogAction = _GsEEventLogAction_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 39, 10, 1, 1, 1, 3),
    _GsEEventLogAction_Type()
)
gsEEventLogAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gsEEventLogAction.setStatus("mandatory")


class _GsEEventTrapAction_Type(Integer32):
    """Custom type gsEEventTrapAction based on Integer32"""
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


_GsEEventTrapAction_Type.__name__ = "Integer32"
_GsEEventTrapAction_Object = MibTableColumn
gsEEventTrapAction = _GsEEventTrapAction_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 39, 10, 1, 1, 1, 4),
    _GsEEventTrapAction_Type()
)
gsEEventTrapAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gsEEventTrapAction.setStatus("mandatory")


class _GsEEventConsoleAction_Type(Integer32):
    """Custom type gsEEventConsoleAction based on Integer32"""
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


_GsEEventConsoleAction_Type.__name__ = "Integer32"
_GsEEventConsoleAction_Object = MibTableColumn
gsEEventConsoleAction = _GsEEventConsoleAction_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 39, 10, 1, 1, 1, 5),
    _GsEEventConsoleAction_Type()
)
gsEEventConsoleAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gsEEventConsoleAction.setStatus("mandatory")
_GsEEventLogMgt_ObjectIdentity = ObjectIdentity
gsEEventLogMgt = _GsEEventLogMgt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 39, 10, 2)
)


class _GsELogTableMaxSize_Type(Integer32):
    """Custom type gsELogTableMaxSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2048),
    )


_GsELogTableMaxSize_Type.__name__ = "Integer32"
_GsELogTableMaxSize_Object = MibScalar
gsELogTableMaxSize = _GsELogTableMaxSize_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 39, 10, 2, 1),
    _GsELogTableMaxSize_Type()
)
gsELogTableMaxSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gsELogTableMaxSize.setStatus("mandatory")


class _GsELogLastEntry_Type(Integer32):
    """Custom type gsELogLastEntry based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_GsELogLastEntry_Type.__name__ = "Integer32"
_GsELogLastEntry_Object = MibScalar
gsELogLastEntry = _GsELogLastEntry_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 39, 10, 2, 2),
    _GsELogLastEntry_Type()
)
gsELogLastEntry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gsELogLastEntry.setStatus("mandatory")
_GsELogWraps_Type = Counter32
_GsELogWraps_Object = MibScalar
gsELogWraps = _GsELogWraps_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 39, 10, 2, 3),
    _GsELogWraps_Type()
)
gsELogWraps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gsELogWraps.setStatus("mandatory")
_GsEEventLog_ObjectIdentity = ObjectIdentity
gsEEventLog = _GsEEventLog_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 39, 10, 3)
)
_GsEEventLogTable_Object = MibTable
gsEEventLogTable = _GsEEventLogTable_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 39, 10, 3, 1)
)
if mibBuilder.loadTexts:
    gsEEventLogTable.setStatus("mandatory")
_GsEEventLogEntry_Object = MibTableRow
gsEEventLogEntry = _GsEEventLogEntry_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 39, 10, 3, 1, 1)
)
gsEEventLogEntry.setIndexNames(
    (0, "GIGAswitchEthernet-MIB", "gsEEventLogIndex"),
)
if mibBuilder.loadTexts:
    gsEEventLogEntry.setStatus("mandatory")


class _GsEEventLogEventIndex_Type(Integer32):
    """Custom type gsEEventLogEventIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_GsEEventLogEventIndex_Type.__name__ = "Integer32"
_GsEEventLogEventIndex_Object = MibTableColumn
gsEEventLogEventIndex = _GsEEventLogEventIndex_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 39, 10, 3, 1, 1, 1),
    _GsEEventLogEventIndex_Type()
)
gsEEventLogEventIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gsEEventLogEventIndex.setStatus("mandatory")


class _GsEEventLogIndex_Type(Integer32):
    """Custom type gsEEventLogIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_GsEEventLogIndex_Type.__name__ = "Integer32"
_GsEEventLogIndex_Object = MibTableColumn
gsEEventLogIndex = _GsEEventLogIndex_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 39, 10, 3, 1, 1, 2),
    _GsEEventLogIndex_Type()
)
gsEEventLogIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gsEEventLogIndex.setStatus("mandatory")
_GsEEventLogTime_Type = TimeTicks
_GsEEventLogTime_Object = MibTableColumn
gsEEventLogTime = _GsEEventLogTime_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 39, 10, 3, 1, 1, 3),
    _GsEEventLogTime_Type()
)
gsEEventLogTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gsEEventLogTime.setStatus("mandatory")


class _GsEEventLogDescr_Type(DisplayString):
    """Custom type gsEEventLogDescr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_GsEEventLogDescr_Type.__name__ = "DisplayString"
_GsEEventLogDescr_Object = MibTableColumn
gsEEventLogDescr = _GsEEventLogDescr_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 39, 10, 3, 1, 1, 4),
    _GsEEventLogDescr_Type()
)
gsEEventLogDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gsEEventLogDescr.setStatus("mandatory")
_GsEEventLogType_Type = EventCategory
_GsEEventLogType_Object = MibTableColumn
gsEEventLogType = _GsEEventLogType_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 39, 10, 3, 1, 1, 5),
    _GsEEventLogType_Type()
)
gsEEventLogType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gsEEventLogType.setStatus("mandatory")


class _GsEEventLogSeverity_Type(Integer32):
    """Custom type gsEEventLogSeverity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_GsEEventLogSeverity_Type.__name__ = "Integer32"
_GsEEventLogSeverity_Object = MibTableColumn
gsEEventLogSeverity = _GsEEventLogSeverity_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 39, 10, 3, 1, 1, 6),
    _GsEEventLogSeverity_Type()
)
gsEEventLogSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gsEEventLogSeverity.setStatus("mandatory")


class _GsEEventLogDTM_Type(DisplayString):
    """Custom type gsEEventLogDTM based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(18, 18),
    )


_GsEEventLogDTM_Type.__name__ = "DisplayString"
_GsEEventLogDTM_Object = MibTableColumn
gsEEventLogDTM = _GsEEventLogDTM_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 39, 10, 3, 1, 1, 7),
    _GsEEventLogDTM_Type()
)
gsEEventLogDTM.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gsEEventLogDTM.setStatus("mandatory")
_GsEEventLogResType_Type = ResourceType
_GsEEventLogResType_Object = MibTableColumn
gsEEventLogResType = _GsEEventLogResType_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 39, 10, 3, 1, 1, 8),
    _GsEEventLogResType_Type()
)
gsEEventLogResType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gsEEventLogResType.setStatus("mandatory")
_GsEEventLogResID_Type = ResourceId
_GsEEventLogResID_Object = MibTableColumn
gsEEventLogResID = _GsEEventLogResID_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 39, 10, 3, 1, 1, 9),
    _GsEEventLogResID_Type()
)
gsEEventLogResID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gsEEventLogResID.setStatus("mandatory")
_GsEEventLogResLeaf_Type = Integer32
_GsEEventLogResLeaf_Object = MibTableColumn
gsEEventLogResLeaf = _GsEEventLogResLeaf_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 39, 10, 3, 1, 1, 10),
    _GsEEventLogResLeaf_Type()
)
gsEEventLogResLeaf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gsEEventLogResLeaf.setStatus("mandatory")
_GsEEventLogValueType_Type = EventValueType
_GsEEventLogValueType_Object = MibTableColumn
gsEEventLogValueType = _GsEEventLogValueType_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 39, 10, 3, 1, 1, 11),
    _GsEEventLogValueType_Type()
)
gsEEventLogValueType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gsEEventLogValueType.setStatus("mandatory")


class _GsEEventLogValue_Type(OctetString):
    """Custom type gsEEventLogValue based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_GsEEventLogValue_Type.__name__ = "OctetString"
_GsEEventLogValue_Object = MibTableColumn
gsEEventLogValue = _GsEEventLogValue_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 39, 10, 3, 1, 1, 12),
    _GsEEventLogValue_Type()
)
gsEEventLogValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gsEEventLogValue.setStatus("mandatory")
_GsEEventLogEpochTime_Type = Integer32
_GsEEventLogEpochTime_Object = MibTableColumn
gsEEventLogEpochTime = _GsEEventLogEpochTime_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 39, 10, 3, 1, 1, 13),
    _GsEEventLogEpochTime_Type()
)
gsEEventLogEpochTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gsEEventLogEpochTime.setStatus("mandatory")


class _GsEEventLogID_Type(Integer32):
    """Custom type gsEEventLogID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_GsEEventLogID_Type.__name__ = "Integer32"
_GsEEventLogID_Object = MibTableColumn
gsEEventLogID = _GsEEventLogID_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 39, 10, 3, 1, 1, 14),
    _GsEEventLogID_Type()
)
gsEEventLogID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gsEEventLogID.setStatus("mandatory")
_GsEShutdownLogMgt_ObjectIdentity = ObjectIdentity
gsEShutdownLogMgt = _GsEShutdownLogMgt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 39, 10, 4)
)


class _GsEShutdownLogTableMaxSize_Type(Integer32):
    """Custom type gsEShutdownLogTableMaxSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_GsEShutdownLogTableMaxSize_Type.__name__ = "Integer32"
_GsEShutdownLogTableMaxSize_Object = MibScalar
gsEShutdownLogTableMaxSize = _GsEShutdownLogTableMaxSize_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 39, 10, 4, 1),
    _GsEShutdownLogTableMaxSize_Type()
)
gsEShutdownLogTableMaxSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gsEShutdownLogTableMaxSize.setStatus("mandatory")


class _GsEShutdownLogLastEntry_Type(Integer32):
    """Custom type gsEShutdownLogLastEntry based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_GsEShutdownLogLastEntry_Type.__name__ = "Integer32"
_GsEShutdownLogLastEntry_Object = MibScalar
gsEShutdownLogLastEntry = _GsEShutdownLogLastEntry_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 39, 10, 4, 2),
    _GsEShutdownLogLastEntry_Type()
)
gsEShutdownLogLastEntry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gsEShutdownLogLastEntry.setStatus("mandatory")


class _GsEShutdownLogAcknowledged_Type(Integer32):
    """Custom type gsEShutdownLogAcknowledged based on Integer32"""
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


_GsEShutdownLogAcknowledged_Type.__name__ = "Integer32"
_GsEShutdownLogAcknowledged_Object = MibScalar
gsEShutdownLogAcknowledged = _GsEShutdownLogAcknowledged_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 39, 10, 4, 3),
    _GsEShutdownLogAcknowledged_Type()
)
gsEShutdownLogAcknowledged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gsEShutdownLogAcknowledged.setStatus("mandatory")
_GsEEventShutdownLog_ObjectIdentity = ObjectIdentity
gsEEventShutdownLog = _GsEEventShutdownLog_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 39, 10, 5)
)
_GsEEventShutdownLogTable_Object = MibTable
gsEEventShutdownLogTable = _GsEEventShutdownLogTable_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 39, 10, 5, 1)
)
if mibBuilder.loadTexts:
    gsEEventShutdownLogTable.setStatus("mandatory")
_GsEEventShutdownLogEntry_Object = MibTableRow
gsEEventShutdownLogEntry = _GsEEventShutdownLogEntry_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 39, 10, 5, 1, 1)
)
gsEEventShutdownLogEntry.setIndexNames(
    (0, "GIGAswitchEthernet-MIB", "gsEEventShutdownLogIndex"),
)
if mibBuilder.loadTexts:
    gsEEventShutdownLogEntry.setStatus("mandatory")


class _GsEEventShutdownLogEventIndex_Type(Integer32):
    """Custom type gsEEventShutdownLogEventIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_GsEEventShutdownLogEventIndex_Type.__name__ = "Integer32"
_GsEEventShutdownLogEventIndex_Object = MibTableColumn
gsEEventShutdownLogEventIndex = _GsEEventShutdownLogEventIndex_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 39, 10, 5, 1, 1, 1),
    _GsEEventShutdownLogEventIndex_Type()
)
gsEEventShutdownLogEventIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gsEEventShutdownLogEventIndex.setStatus("mandatory")


class _GsEEventShutdownLogIndex_Type(Integer32):
    """Custom type gsEEventShutdownLogIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_GsEEventShutdownLogIndex_Type.__name__ = "Integer32"
_GsEEventShutdownLogIndex_Object = MibTableColumn
gsEEventShutdownLogIndex = _GsEEventShutdownLogIndex_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 39, 10, 5, 1, 1, 2),
    _GsEEventShutdownLogIndex_Type()
)
gsEEventShutdownLogIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gsEEventShutdownLogIndex.setStatus("mandatory")
_GsEEventShutdownLogTime_Type = TimeTicks
_GsEEventShutdownLogTime_Object = MibTableColumn
gsEEventShutdownLogTime = _GsEEventShutdownLogTime_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 39, 10, 5, 1, 1, 3),
    _GsEEventShutdownLogTime_Type()
)
gsEEventShutdownLogTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gsEEventShutdownLogTime.setStatus("mandatory")


class _GsEEventShutdownLogDescr_Type(DisplayString):
    """Custom type gsEEventShutdownLogDescr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_GsEEventShutdownLogDescr_Type.__name__ = "DisplayString"
_GsEEventShutdownLogDescr_Object = MibTableColumn
gsEEventShutdownLogDescr = _GsEEventShutdownLogDescr_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 39, 10, 5, 1, 1, 4),
    _GsEEventShutdownLogDescr_Type()
)
gsEEventShutdownLogDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gsEEventShutdownLogDescr.setStatus("mandatory")
_GsEEventShutdownLogType_Type = EventCategory
_GsEEventShutdownLogType_Object = MibTableColumn
gsEEventShutdownLogType = _GsEEventShutdownLogType_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 39, 10, 5, 1, 1, 5),
    _GsEEventShutdownLogType_Type()
)
gsEEventShutdownLogType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gsEEventShutdownLogType.setStatus("mandatory")


class _GsEEventShutdownLogSeverity_Type(Integer32):
    """Custom type gsEEventShutdownLogSeverity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_GsEEventShutdownLogSeverity_Type.__name__ = "Integer32"
_GsEEventShutdownLogSeverity_Object = MibTableColumn
gsEEventShutdownLogSeverity = _GsEEventShutdownLogSeverity_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 39, 10, 5, 1, 1, 6),
    _GsEEventShutdownLogSeverity_Type()
)
gsEEventShutdownLogSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gsEEventShutdownLogSeverity.setStatus("mandatory")


class _GsEEventShutdownLogDTM_Type(DisplayString):
    """Custom type gsEEventShutdownLogDTM based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(18, 18),
    )


_GsEEventShutdownLogDTM_Type.__name__ = "DisplayString"
_GsEEventShutdownLogDTM_Object = MibTableColumn
gsEEventShutdownLogDTM = _GsEEventShutdownLogDTM_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 39, 10, 5, 1, 1, 7),
    _GsEEventShutdownLogDTM_Type()
)
gsEEventShutdownLogDTM.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gsEEventShutdownLogDTM.setStatus("mandatory")
_GsEEventShutdownLogResType_Type = ResourceType
_GsEEventShutdownLogResType_Object = MibTableColumn
gsEEventShutdownLogResType = _GsEEventShutdownLogResType_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 39, 10, 5, 1, 1, 8),
    _GsEEventShutdownLogResType_Type()
)
gsEEventShutdownLogResType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gsEEventShutdownLogResType.setStatus("mandatory")
_GsEEventShutdownLogResID_Type = ResourceId
_GsEEventShutdownLogResID_Object = MibTableColumn
gsEEventShutdownLogResID = _GsEEventShutdownLogResID_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 39, 10, 5, 1, 1, 9),
    _GsEEventShutdownLogResID_Type()
)
gsEEventShutdownLogResID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gsEEventShutdownLogResID.setStatus("mandatory")
_GsEEventShutdownLogResLeaf_Type = Integer32
_GsEEventShutdownLogResLeaf_Object = MibTableColumn
gsEEventShutdownLogResLeaf = _GsEEventShutdownLogResLeaf_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 39, 10, 5, 1, 1, 10),
    _GsEEventShutdownLogResLeaf_Type()
)
gsEEventShutdownLogResLeaf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gsEEventShutdownLogResLeaf.setStatus("mandatory")
_GsEEventShutdownLogValueType_Type = EventValueType
_GsEEventShutdownLogValueType_Object = MibTableColumn
gsEEventShutdownLogValueType = _GsEEventShutdownLogValueType_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 39, 10, 5, 1, 1, 11),
    _GsEEventShutdownLogValueType_Type()
)
gsEEventShutdownLogValueType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gsEEventShutdownLogValueType.setStatus("mandatory")


class _GsEEventShutdownLogValue_Type(OctetString):
    """Custom type gsEEventShutdownLogValue based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_GsEEventShutdownLogValue_Type.__name__ = "OctetString"
_GsEEventShutdownLogValue_Object = MibTableColumn
gsEEventShutdownLogValue = _GsEEventShutdownLogValue_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 39, 10, 5, 1, 1, 12),
    _GsEEventShutdownLogValue_Type()
)
gsEEventShutdownLogValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gsEEventShutdownLogValue.setStatus("mandatory")
_GsEEventShutdownLogEpochTime_Type = Integer32
_GsEEventShutdownLogEpochTime_Object = MibTableColumn
gsEEventShutdownLogEpochTime = _GsEEventShutdownLogEpochTime_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 39, 10, 5, 1, 1, 13),
    _GsEEventShutdownLogEpochTime_Type()
)
gsEEventShutdownLogEpochTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gsEEventShutdownLogEpochTime.setStatus("mandatory")


class _GsEEventShutdownLogID_Type(Integer32):
    """Custom type gsEEventShutdownLogID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_GsEEventShutdownLogID_Type.__name__ = "Integer32"
_GsEEventShutdownLogID_Object = MibTableColumn
gsEEventShutdownLogID = _GsEEventShutdownLogID_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 39, 10, 5, 1, 1, 14),
    _GsEEventShutdownLogID_Type()
)
gsEEventShutdownLogID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gsEEventShutdownLogID.setStatus("mandatory")
_GsEEventTrapMgmt_ObjectIdentity = ObjectIdentity
gsEEventTrapMgmt = _GsEEventTrapMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 39, 10, 6)
)


class _GsEEventTrapEventIndex_Type(Integer32):
    """Custom type gsEEventTrapEventIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_GsEEventTrapEventIndex_Type.__name__ = "Integer32"
_GsEEventTrapEventIndex_Object = MibScalar
gsEEventTrapEventIndex = _GsEEventTrapEventIndex_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 39, 10, 6, 1),
    _GsEEventTrapEventIndex_Type()
)
gsEEventTrapEventIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gsEEventTrapEventIndex.setStatus("mandatory")
_GsEEventTrapTime_Type = TimeTicks
_GsEEventTrapTime_Object = MibScalar
gsEEventTrapTime = _GsEEventTrapTime_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 39, 10, 6, 2),
    _GsEEventTrapTime_Type()
)
gsEEventTrapTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gsEEventTrapTime.setStatus("mandatory")


class _GsEEventTrapDescr_Type(DisplayString):
    """Custom type gsEEventTrapDescr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_GsEEventTrapDescr_Type.__name__ = "DisplayString"
_GsEEventTrapDescr_Object = MibScalar
gsEEventTrapDescr = _GsEEventTrapDescr_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 39, 10, 6, 3),
    _GsEEventTrapDescr_Type()
)
gsEEventTrapDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gsEEventTrapDescr.setStatus("mandatory")
_GsEEventTrapType_Type = EventCategory
_GsEEventTrapType_Object = MibScalar
gsEEventTrapType = _GsEEventTrapType_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 39, 10, 6, 4),
    _GsEEventTrapType_Type()
)
gsEEventTrapType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gsEEventTrapType.setStatus("mandatory")


class _GsEEventTrapSeverity_Type(Integer32):
    """Custom type gsEEventTrapSeverity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_GsEEventTrapSeverity_Type.__name__ = "Integer32"
_GsEEventTrapSeverity_Object = MibScalar
gsEEventTrapSeverity = _GsEEventTrapSeverity_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 39, 10, 6, 5),
    _GsEEventTrapSeverity_Type()
)
gsEEventTrapSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gsEEventTrapSeverity.setStatus("mandatory")


class _GsEEventTrapDTM_Type(DisplayString):
    """Custom type gsEEventTrapDTM based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(18, 18),
    )


_GsEEventTrapDTM_Type.__name__ = "DisplayString"
_GsEEventTrapDTM_Object = MibScalar
gsEEventTrapDTM = _GsEEventTrapDTM_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 39, 10, 6, 6),
    _GsEEventTrapDTM_Type()
)
gsEEventTrapDTM.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gsEEventTrapDTM.setStatus("mandatory")
_GsEEventTrapResType_Type = ResourceType
_GsEEventTrapResType_Object = MibScalar
gsEEventTrapResType = _GsEEventTrapResType_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 39, 10, 6, 7),
    _GsEEventTrapResType_Type()
)
gsEEventTrapResType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gsEEventTrapResType.setStatus("mandatory")
_GsEEventTrapResID_Type = ResourceId
_GsEEventTrapResID_Object = MibScalar
gsEEventTrapResID = _GsEEventTrapResID_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 39, 10, 6, 8),
    _GsEEventTrapResID_Type()
)
gsEEventTrapResID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gsEEventTrapResID.setStatus("mandatory")
_GsEEventTrapResLeaf_Type = Integer32
_GsEEventTrapResLeaf_Object = MibScalar
gsEEventTrapResLeaf = _GsEEventTrapResLeaf_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 39, 10, 6, 9),
    _GsEEventTrapResLeaf_Type()
)
gsEEventTrapResLeaf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gsEEventTrapResLeaf.setStatus("mandatory")
_GsEEventTrapValueType_Type = EventValueType
_GsEEventTrapValueType_Object = MibScalar
gsEEventTrapValueType = _GsEEventTrapValueType_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 39, 10, 6, 10),
    _GsEEventTrapValueType_Type()
)
gsEEventTrapValueType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gsEEventTrapValueType.setStatus("mandatory")


class _GsEEventTrapValue_Type(OctetString):
    """Custom type gsEEventTrapValue based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_GsEEventTrapValue_Type.__name__ = "OctetString"
_GsEEventTrapValue_Object = MibScalar
gsEEventTrapValue = _GsEEventTrapValue_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 39, 10, 6, 11),
    _GsEEventTrapValue_Type()
)
gsEEventTrapValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gsEEventTrapValue.setStatus("mandatory")
_GsEEventTrapEpochTime_Type = Integer32
_GsEEventTrapEpochTime_Object = MibScalar
gsEEventTrapEpochTime = _GsEEventTrapEpochTime_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 39, 10, 6, 12),
    _GsEEventTrapEpochTime_Type()
)
gsEEventTrapEpochTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gsEEventTrapEpochTime.setStatus("mandatory")


class _GsEEventTrapID_Type(Integer32):
    """Custom type gsEEventTrapID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_GsEEventTrapID_Type.__name__ = "Integer32"
_GsEEventTrapID_Object = MibScalar
gsEEventTrapID = _GsEEventTrapID_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 39, 10, 6, 13),
    _GsEEventTrapID_Type()
)
gsEEventTrapID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gsEEventTrapID.setStatus("mandatory")
_GsEAlarmMgt_ObjectIdentity = ObjectIdentity
gsEAlarmMgt = _GsEAlarmMgt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 39, 11)
)
_GsEAlarmGeneral_ObjectIdentity = ObjectIdentity
gsEAlarmGeneral = _GsEAlarmGeneral_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 39, 11, 1)
)
_GsEAlarmGeneralActiveEntries_Type = Gauge32
_GsEAlarmGeneralActiveEntries_Object = MibScalar
gsEAlarmGeneralActiveEntries = _GsEAlarmGeneralActiveEntries_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 39, 11, 1, 1),
    _GsEAlarmGeneralActiveEntries_Type()
)
gsEAlarmGeneralActiveEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gsEAlarmGeneralActiveEntries.setStatus("mandatory")
_GsEAlarmGeneralTimeStamp_Type = TimeTicks
_GsEAlarmGeneralTimeStamp_Object = MibScalar
gsEAlarmGeneralTimeStamp = _GsEAlarmGeneralTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 39, 11, 1, 2),
    _GsEAlarmGeneralTimeStamp_Type()
)
gsEAlarmGeneralTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gsEAlarmGeneralTimeStamp.setStatus("mandatory")
_GsEAlarms_ObjectIdentity = ObjectIdentity
gsEAlarms = _GsEAlarms_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 39, 11, 2)
)
_GsEActiveAlarmTable_Object = MibTable
gsEActiveAlarmTable = _GsEActiveAlarmTable_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 39, 11, 2, 2)
)
if mibBuilder.loadTexts:
    gsEActiveAlarmTable.setStatus("mandatory")
_GsEActiveAlarmEntry_Object = MibTableRow
gsEActiveAlarmEntry = _GsEActiveAlarmEntry_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 39, 11, 2, 2, 1)
)
gsEActiveAlarmEntry.setIndexNames(
    (0, "GIGAswitchEthernet-MIB", "gsEActiveAlarmIndex"),
)
if mibBuilder.loadTexts:
    gsEActiveAlarmEntry.setStatus("mandatory")
_GsEActiveAlarmIndex_Type = Integer32
_GsEActiveAlarmIndex_Object = MibTableColumn
gsEActiveAlarmIndex = _GsEActiveAlarmIndex_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 39, 11, 2, 2, 1, 1),
    _GsEActiveAlarmIndex_Type()
)
gsEActiveAlarmIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gsEActiveAlarmIndex.setStatus("mandatory")


class _GsEActiveAlarmName_Type(DisplayString):
    """Custom type gsEActiveAlarmName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_GsEActiveAlarmName_Type.__name__ = "DisplayString"
_GsEActiveAlarmName_Object = MibTableColumn
gsEActiveAlarmName = _GsEActiveAlarmName_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 39, 11, 2, 2, 1, 2),
    _GsEActiveAlarmName_Type()
)
gsEActiveAlarmName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gsEActiveAlarmName.setStatus("mandatory")
_GsEActiveAlarmValueHigh_Type = Integer32
_GsEActiveAlarmValueHigh_Object = MibTableColumn
gsEActiveAlarmValueHigh = _GsEActiveAlarmValueHigh_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 39, 11, 2, 2, 1, 3),
    _GsEActiveAlarmValueHigh_Type()
)
gsEActiveAlarmValueHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gsEActiveAlarmValueHigh.setStatus("mandatory")
_GsEActiveAlarmValueLow_Type = Integer32
_GsEActiveAlarmValueLow_Object = MibTableColumn
gsEActiveAlarmValueLow = _GsEActiveAlarmValueLow_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 39, 11, 2, 2, 1, 4),
    _GsEActiveAlarmValueLow_Type()
)
gsEActiveAlarmValueLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gsEActiveAlarmValueLow.setStatus("mandatory")
_GsEActiveAlarmVariable_Type = ObjectIdentifier
_GsEActiveAlarmVariable_Object = MibTableColumn
gsEActiveAlarmVariable = _GsEActiveAlarmVariable_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 39, 11, 2, 2, 1, 5),
    _GsEActiveAlarmVariable_Type()
)
gsEActiveAlarmVariable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gsEActiveAlarmVariable.setStatus("mandatory")
_GsEActiveAlarmResType_Type = ResourceType
_GsEActiveAlarmResType_Object = MibTableColumn
gsEActiveAlarmResType = _GsEActiveAlarmResType_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 39, 11, 2, 2, 1, 6),
    _GsEActiveAlarmResType_Type()
)
gsEActiveAlarmResType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gsEActiveAlarmResType.setStatus("mandatory")
_GsEActiveAlarmResID_Type = ResourceId
_GsEActiveAlarmResID_Object = MibTableColumn
gsEActiveAlarmResID = _GsEActiveAlarmResID_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 39, 11, 2, 2, 1, 7),
    _GsEActiveAlarmResID_Type()
)
gsEActiveAlarmResID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gsEActiveAlarmResID.setStatus("mandatory")
_GsEActiveAlarmLeaf_Type = Integer32
_GsEActiveAlarmLeaf_Object = MibTableColumn
gsEActiveAlarmLeaf = _GsEActiveAlarmLeaf_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 39, 11, 2, 2, 1, 8),
    _GsEActiveAlarmLeaf_Type()
)
gsEActiveAlarmLeaf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gsEActiveAlarmLeaf.setStatus("mandatory")


class _GsEActiveAlarmOwner_Type(DisplayString):
    """Custom type gsEActiveAlarmOwner based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_GsEActiveAlarmOwner_Type.__name__ = "DisplayString"
_GsEActiveAlarmOwner_Object = MibTableColumn
gsEActiveAlarmOwner = _GsEActiveAlarmOwner_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 39, 11, 2, 2, 1, 9),
    _GsEActiveAlarmOwner_Type()
)
gsEActiveAlarmOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gsEActiveAlarmOwner.setStatus("mandatory")
_GsESnmpTraps_ObjectIdentity = ObjectIdentity
gsESnmpTraps = _GsESnmpTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 39, 13)
)

# Managed Objects groups


# Notification objects

gsESystemTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 39, 13, 0, 2)
)
gsESystemTrap.setObjects(
      *(("GIGAswitchEthernet-MIB", "gsEEventTrapEventIndex"),
        ("GIGAswitchEthernet-MIB", "gsEEventTrapTime"),
        ("GIGAswitchEthernet-MIB", "gsEEventTrapDescr"),
        ("GIGAswitchEthernet-MIB", "gsEEventTrapType"),
        ("GIGAswitchEthernet-MIB", "gsEEventTrapSeverity"),
        ("GIGAswitchEthernet-MIB", "gsEEventTrapDTM"),
        ("GIGAswitchEthernet-MIB", "gsEEventTrapResType"),
        ("GIGAswitchEthernet-MIB", "gsEEventTrapResID"),
        ("GIGAswitchEthernet-MIB", "gsEEventTrapResLeaf"),
        ("GIGAswitchEthernet-MIB", "gsEEventTrapValueType"),
        ("GIGAswitchEthernet-MIB", "gsEEventTrapValue"),
        ("GIGAswitchEthernet-MIB", "gsEEventTrapEpochTime"),
        ("GIGAswitchEthernet-MIB", "gsEEventTrapID"))
)
if mibBuilder.loadTexts:
    gsESystemTrap.setStatus(
        ""
    )

gsEConfigurationTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 39, 13, 0, 3)
)
gsEConfigurationTrap.setObjects(
      *(("GIGAswitchEthernet-MIB", "gsEEventTrapEventIndex"),
        ("GIGAswitchEthernet-MIB", "gsEEventTrapTime"),
        ("GIGAswitchEthernet-MIB", "gsEEventTrapDescr"),
        ("GIGAswitchEthernet-MIB", "gsEEventTrapType"),
        ("GIGAswitchEthernet-MIB", "gsEEventTrapSeverity"),
        ("GIGAswitchEthernet-MIB", "gsEEventTrapDTM"),
        ("GIGAswitchEthernet-MIB", "gsEEventTrapResType"),
        ("GIGAswitchEthernet-MIB", "gsEEventTrapResID"),
        ("GIGAswitchEthernet-MIB", "gsEEventTrapResLeaf"),
        ("GIGAswitchEthernet-MIB", "gsEEventTrapValueType"),
        ("GIGAswitchEthernet-MIB", "gsEEventTrapValue"),
        ("GIGAswitchEthernet-MIB", "gsEEventTrapEpochTime"),
        ("GIGAswitchEthernet-MIB", "gsEEventTrapID"))
)
if mibBuilder.loadTexts:
    gsEConfigurationTrap.setStatus(
        ""
    )

gsETemperatureTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 39, 13, 0, 4)
)
gsETemperatureTrap.setObjects(
      *(("GIGAswitchEthernet-MIB", "gsEEventTrapEventIndex"),
        ("GIGAswitchEthernet-MIB", "gsEEventTrapTime"),
        ("GIGAswitchEthernet-MIB", "gsEEventTrapDescr"),
        ("GIGAswitchEthernet-MIB", "gsEEventTrapType"),
        ("GIGAswitchEthernet-MIB", "gsEEventTrapSeverity"),
        ("GIGAswitchEthernet-MIB", "gsEEventTrapDTM"),
        ("GIGAswitchEthernet-MIB", "gsEEventTrapResType"),
        ("GIGAswitchEthernet-MIB", "gsEEventTrapResID"),
        ("GIGAswitchEthernet-MIB", "gsEEventTrapResLeaf"),
        ("GIGAswitchEthernet-MIB", "gsEEventTrapValueType"),
        ("GIGAswitchEthernet-MIB", "gsEEventTrapValue"),
        ("GIGAswitchEthernet-MIB", "gsEEventTrapEpochTime"),
        ("GIGAswitchEthernet-MIB", "gsEEventTrapID"))
)
if mibBuilder.loadTexts:
    gsETemperatureTrap.setStatus(
        ""
    )

gsEResourceTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 39, 13, 0, 5)
)
gsEResourceTrap.setObjects(
      *(("GIGAswitchEthernet-MIB", "gsEEventTrapEventIndex"),
        ("GIGAswitchEthernet-MIB", "gsEEventTrapTime"),
        ("GIGAswitchEthernet-MIB", "gsEEventTrapDescr"),
        ("GIGAswitchEthernet-MIB", "gsEEventTrapType"),
        ("GIGAswitchEthernet-MIB", "gsEEventTrapSeverity"),
        ("GIGAswitchEthernet-MIB", "gsEEventTrapDTM"),
        ("GIGAswitchEthernet-MIB", "gsEEventTrapResType"),
        ("GIGAswitchEthernet-MIB", "gsEEventTrapResID"),
        ("GIGAswitchEthernet-MIB", "gsEEventTrapResLeaf"),
        ("GIGAswitchEthernet-MIB", "gsEEventTrapValueType"),
        ("GIGAswitchEthernet-MIB", "gsEEventTrapValue"),
        ("GIGAswitchEthernet-MIB", "gsEEventTrapEpochTime"),
        ("GIGAswitchEthernet-MIB", "gsEEventTrapID"))
)
if mibBuilder.loadTexts:
    gsEResourceTrap.setStatus(
        ""
    )

gsEFanTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 39, 13, 0, 6)
)
gsEFanTrap.setObjects(
      *(("GIGAswitchEthernet-MIB", "gsEEventTrapEventIndex"),
        ("GIGAswitchEthernet-MIB", "gsEEventTrapTime"),
        ("GIGAswitchEthernet-MIB", "gsEEventTrapDescr"),
        ("GIGAswitchEthernet-MIB", "gsEEventTrapType"),
        ("GIGAswitchEthernet-MIB", "gsEEventTrapSeverity"),
        ("GIGAswitchEthernet-MIB", "gsEEventTrapDTM"),
        ("GIGAswitchEthernet-MIB", "gsEEventTrapResType"),
        ("GIGAswitchEthernet-MIB", "gsEEventTrapResID"),
        ("GIGAswitchEthernet-MIB", "gsEEventTrapResLeaf"),
        ("GIGAswitchEthernet-MIB", "gsEEventTrapValueType"),
        ("GIGAswitchEthernet-MIB", "gsEEventTrapValue"),
        ("GIGAswitchEthernet-MIB", "gsEEventTrapEpochTime"),
        ("GIGAswitchEthernet-MIB", "gsEEventTrapID"))
)
if mibBuilder.loadTexts:
    gsEFanTrap.setStatus(
        ""
    )

gsEPowerTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 39, 13, 0, 9)
)
gsEPowerTrap.setObjects(
      *(("GIGAswitchEthernet-MIB", "gsEEventTrapEventIndex"),
        ("GIGAswitchEthernet-MIB", "gsEEventTrapTime"),
        ("GIGAswitchEthernet-MIB", "gsEEventTrapDescr"),
        ("GIGAswitchEthernet-MIB", "gsEEventTrapType"),
        ("GIGAswitchEthernet-MIB", "gsEEventTrapSeverity"),
        ("GIGAswitchEthernet-MIB", "gsEEventTrapDTM"),
        ("GIGAswitchEthernet-MIB", "gsEEventTrapResType"),
        ("GIGAswitchEthernet-MIB", "gsEEventTrapResID"),
        ("GIGAswitchEthernet-MIB", "gsEEventTrapResLeaf"),
        ("GIGAswitchEthernet-MIB", "gsEEventTrapValueType"),
        ("GIGAswitchEthernet-MIB", "gsEEventTrapValue"),
        ("GIGAswitchEthernet-MIB", "gsEEventTrapEpochTime"),
        ("GIGAswitchEthernet-MIB", "gsEEventTrapID"))
)
if mibBuilder.loadTexts:
    gsEPowerTrap.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "GIGAswitchEthernet-MIB",
    **{"EventValueType": EventValueType,
       "ResourceType": ResourceType,
       "ResourceId": ResourceId,
       "DisplayString": DisplayString,
       "RowStatus": RowStatus,
       "MacAddress": MacAddress,
       "BridgeId": BridgeId,
       "Timeout": Timeout,
       "EventCategory": EventCategory,
       "dec": dec,
       "ema": ema,
       "mib-extensions-1": mib_extensions_1,
       "gsEMIB": gsEMIB,
       "gsEAgent": gsEAgent,
       "gsEAgentGen": gsEAgentGen,
       "gsEAgentMIBVersion": gsEAgentMIBVersion,
       "gsEAgentMgrIndex": gsEAgentMgrIndex,
       "gsEAgentCommunity": gsEAgentCommunity,
       "gsECommunityTable": gsECommunityTable,
       "gsECommunityEntry": gsECommunityEntry,
       "gsECommunityIndex": gsECommunityIndex,
       "gsECommunityString": gsECommunityString,
       "gsECommunityAddressType": gsECommunityAddressType,
       "gsECommunityAddress": gsECommunityAddress,
       "gsECommunityAccess": gsECommunityAccess,
       "gsECommunityTrapReceiver": gsECommunityTrapReceiver,
       "gsECommunitySecurityLevel": gsECommunitySecurityLevel,
       "gsECommunityStatus": gsECommunityStatus,
       "gsEAgentWeb": gsEAgentWeb,
       "gsEAgentWebServerURL": gsEAgentWebServerURL,
       "gsEAgentWebServerHelpDirectory": gsEAgentWebServerHelpDirectory,
       "gsEChassis": gsEChassis,
       "gsEChassisGen": gsEChassisGen,
       "gsEChassisType": gsEChassisType,
       "gsEChassisSlots": gsEChassisSlots,
       "gsEInventory": gsEInventory,
       "gsEInventoryTable": gsEInventoryTable,
       "gsEInventoryEntry": gsEInventoryEntry,
       "gsEInventoryResourceType": gsEInventoryResourceType,
       "gsEInventoryResourceIndex": gsEInventoryResourceIndex,
       "gsEInventoryModelNumber": gsEInventoryModelNumber,
       "gsEInventorySerialNumber": gsEInventorySerialNumber,
       "gsEInventoryVersion": gsEInventoryVersion,
       "gsEInventoryManufactureInfo": gsEInventoryManufactureInfo,
       "gsEInventoryScratchPad": gsEInventoryScratchPad,
       "gsEPowerSystems": gsEPowerSystems,
       "gsEPowerSupplies": gsEPowerSupplies,
       "gsEPowerSupplyTable": gsEPowerSupplyTable,
       "gsEPowerSupplyEntry": gsEPowerSupplyEntry,
       "gsEPowerSupplyIndex": gsEPowerSupplyIndex,
       "gsEPowerSupplyType": gsEPowerSupplyType,
       "gsEPowerSupplyStatus": gsEPowerSupplyStatus,
       "gsEPowerSupplyInputStatus": gsEPowerSupplyInputStatus,
       "gsEPowerSupplyOutputStatus": gsEPowerSupplyOutputStatus,
       "gsEPowerSupplyOutputCapacity": gsEPowerSupplyOutputCapacity,
       "gsEPowerMgmtGen": gsEPowerMgmtGen,
       "gsEPowerCapacity": gsEPowerCapacity,
       "gsEPowerUsed": gsEPowerUsed,
       "gsEPowerMgmtCtl": gsEPowerMgmtCtl,
       "gsEPowerControlTable": gsEPowerControlTable,
       "gsEPowerControlEntry": gsEPowerControlEntry,
       "gsEPowerControlUsed": gsEPowerControlUsed,
       "gsEPowerControlPriority": gsEPowerControlPriority,
       "gsEPowerControlMode": gsEPowerControlMode,
       "gsETemperature": gsETemperature,
       "gsETempTable": gsETempTable,
       "gsETempEntry": gsETempEntry,
       "gsETempIndex": gsETempIndex,
       "gsETempValue": gsETempValue,
       "gsETempUpperLimit": gsETempUpperLimit,
       "gsETempUpperWarning": gsETempUpperWarning,
       "gsETempLowerWarning": gsETempLowerWarning,
       "gsETempLowerLimit": gsETempLowerLimit,
       "gsEModules": gsEModules,
       "gsEModuleTable": gsEModuleTable,
       "gsEModuleEntry": gsEModuleEntry,
       "gsEModuleIndex": gsEModuleIndex,
       "gsEModuleName": gsEModuleName,
       "gsEModuleType": gsEModuleType,
       "gsEModuleBaseType": gsEModuleBaseType,
       "gsEModuleSlotWidth": gsEModuleSlotWidth,
       "gsEModuleSlotOffset": gsEModuleSlotOffset,
       "gsEModulePorts": gsEModulePorts,
       "gsEPorts": gsEPorts,
       "gsEPortMgt": gsEPortMgt,
       "gsEPortTable": gsEPortTable,
       "gsEPortEntry": gsEPortEntry,
       "gsEPortIndex": gsEPortIndex,
       "gsEPortName": gsEPortName,
       "gsEPortType": gsEPortType,
       "gsEPortBaseType": gsEPortBaseType,
       "gsEPortMode": gsEPortMode,
       "gsEPortStatus": gsEPortStatus,
       "gsEPortConnector": gsEPortConnector,
       "gsEPortSpeedState": gsEPortSpeedState,
       "gsEPortDuplexState": gsEPortDuplexState,
       "gsEPortGroupBinding": gsEPortGroupBinding,
       "gsEPortFlowControlMgt": gsEPortFlowControlMgt,
       "gsEPortFlowControlTable": gsEPortFlowControlTable,
       "gsEPortFlowControlEntry": gsEPortFlowControlEntry,
       "gsEPortFlowControlMode": gsEPortFlowControlMode,
       "gsEPortDuplexMgt": gsEPortDuplexMgt,
       "gsEPortDuplexTable": gsEPortDuplexTable,
       "gsEPortDuplexEntry": gsEPortDuplexEntry,
       "gsEPortDuplexMode": gsEPortDuplexMode,
       "gsEPortSpeedMgt": gsEPortSpeedMgt,
       "gsEPortSpeedTable": gsEPortSpeedTable,
       "gsEPortSpeedEntry": gsEPortSpeedEntry,
       "gsEPortSpeedMode": gsEPortSpeedMode,
       "gsEPortAutoNegotiationMgt": gsEPortAutoNegotiationMgt,
       "gsEPortAutoNegotiationTable": gsEPortAutoNegotiationTable,
       "gsEPortAutoNegotiationEntry": gsEPortAutoNegotiationEntry,
       "gsEPortAutoNegotiationMode": gsEPortAutoNegotiationMode,
       "gsEPortAutoNegotiationSpeedAdvertisement": gsEPortAutoNegotiationSpeedAdvertisement,
       "gsEPortAutoNegotiationDuplexAdvertisement": gsEPortAutoNegotiationDuplexAdvertisement,
       "gsEPortRateLimitMgt": gsEPortRateLimitMgt,
       "gsEPortRateLimitTable": gsEPortRateLimitTable,
       "gsEPortRateLimitEntry": gsEPortRateLimitEntry,
       "gsEPortRateLimitMode": gsEPortRateLimitMode,
       "gsEPortRateLimitRate": gsEPortRateLimitRate,
       "gsEPortRateLimitBurstSize": gsEPortRateLimitBurstSize,
       "gsEPortCategoryMgt": gsEPortCategoryMgt,
       "gsEPortCategoryTable": gsEPortCategoryTable,
       "gsEPortCategoryEntry": gsEPortCategoryEntry,
       "gsEPortCategoryMode": gsEPortCategoryMode,
       "gsEBufferMgt": gsEBufferMgt,
       "gsEBufferTable": gsEBufferTable,
       "gsEBufferEntry": gsEBufferEntry,
       "gsEBufferIndex": gsEBufferIndex,
       "gsEBufferFabricPort": gsEBufferFabricPort,
       "gsEBufferFabricPortDirection": gsEBufferFabricPortDirection,
       "gsEBufferSwitchPort": gsEBufferSwitchPort,
       "gsEBufferMemory": gsEBufferMemory,
       "gsEBufferAgeTimer": gsEBufferAgeTimer,
       "gsEBufferPriorityServicing": gsEBufferPriorityServicing,
       "gsEBufferPriorityAllocation": gsEBufferPriorityAllocation,
       "gsEBufferPriorityThreshold": gsEBufferPriorityThreshold,
       "gsEBufferCongestion": gsEBufferCongestion,
       "gsEBufferHighOverflowDrops": gsEBufferHighOverflowDrops,
       "gsEBufferLowOverflowDrops": gsEBufferLowOverflowDrops,
       "gsEBufferHighStaleDrops": gsEBufferHighStaleDrops,
       "gsEBufferLowStaleDrops": gsEBufferLowStaleDrops,
       "gsEBufferCongestionDrops": gsEBufferCongestionDrops,
       "gsESwitching": gsESwitching,
       "gsESwitchingLayerII": gsESwitchingLayerII,
       "gsESwitchGen": gsESwitchGen,
       "gsESwitchSTPConfig": gsESwitchSTPConfig,
       "gsESwitchAgingTime": gsESwitchAgingTime,
       "gsESwitchSuperAgingTime": gsESwitchSuperAgingTime,
       "gsEBridgeMgmt": gsEBridgeMgmt,
       "gsEBridgeTable": gsEBridgeTable,
       "gsEBridgeEntry": gsEBridgeEntry,
       "gsEBridgeIndex": gsEBridgeIndex,
       "gsEBridgeType": gsEBridgeType,
       "gsEBridgeMode": gsEBridgeMode,
       "gsEBridgeStatus": gsEBridgeStatus,
       "gsEBridgeStpPriority": gsEBridgeStpPriority,
       "gsEBridgeStpTimeSinceTopologyChange": gsEBridgeStpTimeSinceTopologyChange,
       "gsEBridgeStpTopChanges": gsEBridgeStpTopChanges,
       "gsEBridgeStpDesignatedRoot": gsEBridgeStpDesignatedRoot,
       "gsEBridgeStpRootCost": gsEBridgeStpRootCost,
       "gsEBridgeStpRootPort": gsEBridgeStpRootPort,
       "gsEBridgeStpMaxAge": gsEBridgeStpMaxAge,
       "gsEBridgeStpHelloTime": gsEBridgeStpHelloTime,
       "gsEBridgeStpHoldTime": gsEBridgeStpHoldTime,
       "gsEBridgeStpForwardDelay": gsEBridgeStpForwardDelay,
       "gsEBridgeStpBridgeMaxAge": gsEBridgeStpBridgeMaxAge,
       "gsEBridgeStpBridgeHelloTime": gsEBridgeStpBridgeHelloTime,
       "gsEBridgeStpBridgeForwardDelay": gsEBridgeStpBridgeForwardDelay,
       "gsEBridgePortMgmt": gsEBridgePortMgmt,
       "gsEBridgePortTable": gsEBridgePortTable,
       "gsEBridgePortEntry": gsEBridgePortEntry,
       "gsEBridgePortIndex": gsEBridgePortIndex,
       "gsEBridgePortPriority": gsEBridgePortPriority,
       "gsEBridgePortState": gsEBridgePortState,
       "gsEBridgePortEnable": gsEBridgePortEnable,
       "gsEBridgePortPathCost": gsEBridgePortPathCost,
       "gsEBridgePortDesignatedRoot": gsEBridgePortDesignatedRoot,
       "gsEBridgePortDesignatedCost": gsEBridgePortDesignatedCost,
       "gsEBridgePortDesignatedBridge": gsEBridgePortDesignatedBridge,
       "gsEBridgePortDesignatedPort": gsEBridgePortDesignatedPort,
       "gsEBridgePortForwardTransitions": gsEBridgePortForwardTransitions,
       "gsEBridgePortFastStart": gsEBridgePortFastStart,
       "gsEBridgePortSetDefault": gsEBridgePortSetDefault,
       "gsEBridgePortEnableChangeDetection": gsEBridgePortEnableChangeDetection,
       "gsEL2AddrMgmt": gsEL2AddrMgmt,
       "gsEL2AddrDatabaseMgt": gsEL2AddrDatabaseMgt,
       "gsEL2AddressTable": gsEL2AddressTable,
       "gsEL2AddressEntry": gsEL2AddressEntry,
       "gsEL2AddressIndex": gsEL2AddressIndex,
       "gsEL2AddressTableIndex": gsEL2AddressTableIndex,
       "gsEL2AddressMacAddress": gsEL2AddressMacAddress,
       "gsEL2AddressPortBinding": gsEL2AddressPortBinding,
       "gsEL2AddressBindingValid": gsEL2AddressBindingValid,
       "gsEL2AddressVlanID": gsEL2AddressVlanID,
       "gsEL2AddressPriority": gsEL2AddressPriority,
       "gsEL2AddressForward": gsEL2AddressForward,
       "gsEL2AddressCopy": gsEL2AddressCopy,
       "gsEL2AddressPersistence": gsEL2AddressPersistence,
       "gsEL2AddressStatus": gsEL2AddressStatus,
       "gsEL2AddrSummaryMgt": gsEL2AddrSummaryMgt,
       "gsEL2AddrSummaryTable": gsEL2AddrSummaryTable,
       "gsEL2AddrSummaryEntry": gsEL2AddrSummaryEntry,
       "gsEL2AddrSummary": gsEL2AddrSummary,
       "gsEL2AddrControlMgt": gsEL2AddrControlMgt,
       "gsEL2AddressControlTable": gsEL2AddressControlTable,
       "gsEL2AddressControlEntry": gsEL2AddressControlEntry,
       "gsEL2AddressControlIndex": gsEL2AddressControlIndex,
       "gsEL2AddressControlMacAddress": gsEL2AddressControlMacAddress,
       "gsEL2AddressControlPortBinding": gsEL2AddressControlPortBinding,
       "gsEL2AddressControlVlanID": gsEL2AddressControlVlanID,
       "gsEL2AddressControlPriority": gsEL2AddressControlPriority,
       "gsEL2AddressControlPersistence": gsEL2AddressControlPersistence,
       "gsEL2AddressControlStatus": gsEL2AddressControlStatus,
       "gsEL2AddrChangeMgt": gsEL2AddrChangeMgt,
       "gsEL2AddressChangeLast": gsEL2AddressChangeLast,
       "gsEL2AddressChangeWraps": gsEL2AddressChangeWraps,
       "gsEL2AddressChangeMaxEntries": gsEL2AddressChangeMaxEntries,
       "gsEL2AddressChangeTable": gsEL2AddressChangeTable,
       "gsEL2AddressChangeEntry": gsEL2AddressChangeEntry,
       "gsEL2AddressChangeWrapCount": gsEL2AddressChangeWrapCount,
       "gsEL2AddressChangeIndex": gsEL2AddressChangeIndex,
       "gsEL2AddressChangeIndexChanged": gsEL2AddressChangeIndexChanged,
       "gsEL2AddressChangeSummary": gsEL2AddressChangeSummary,
       "gsESwitchPortMgt": gsESwitchPortMgt,
       "gsESwitchPortTable": gsESwitchPortTable,
       "gsESwitchPortEntry": gsESwitchPortEntry,
       "gsESwitchPortIndex": gsESwitchPortIndex,
       "gsESwitchPortSTAPMode": gsESwitchPortSTAPMode,
       "gsESwitchPortConvertToStatic": gsESwitchPortConvertToStatic,
       "gsESwitchPortLearningMode": gsESwitchPortLearningMode,
       "gsESwitchPortHuntGroup": gsESwitchPortHuntGroup,
       "gsESwitchPortPhysicalPort": gsESwitchPortPhysicalPort,
       "gsESwitchPortKnownMode": gsESwitchPortKnownMode,
       "gsESwitchPortMappingMethod": gsESwitchPortMappingMethod,
       "gsESwitchPortTrunkingMode": gsESwitchPortTrunkingMode,
       "gsESwitchPortVlanBindingMethod": gsESwitchPortVlanBindingMethod,
       "gsESwitchPortIgnoreTag": gsESwitchPortIgnoreTag,
       "gsESwitchPortVlanID": gsESwitchPortVlanID,
       "gsESwitchPortAutoVlanCreation": gsESwitchPortAutoVlanCreation,
       "gsESwitchPortMirrorMode": gsESwitchPortMirrorMode,
       "gsESwitchPortIfIndex": gsESwitchPortIfIndex,
       "gsESwitchPortFastStart": gsESwitchPortFastStart,
       "gsEHuntGroupMgt": gsEHuntGroupMgt,
       "gsEHuntGroupTable": gsEHuntGroupTable,
       "gsEHuntGroupEntry": gsEHuntGroupEntry,
       "gsEHuntGroupIndex": gsEHuntGroupIndex,
       "gsEHuntGroupName": gsEHuntGroupName,
       "gsEHuntGroupBasePort": gsEHuntGroupBasePort,
       "gsEHuntGroupNumberOfPorts": gsEHuntGroupNumberOfPorts,
       "gsEHuntGroupLoadSharing": gsEHuntGroupLoadSharing,
       "gsEHuntGroupStatus": gsEHuntGroupStatus,
       "gsEPortMirroringMgt": gsEPortMirroringMgt,
       "gsEPortMirroringTable": gsEPortMirroringTable,
       "gsEPortMirroringEntry": gsEPortMirroringEntry,
       "gsEPortMirroringIndex": gsEPortMirroringIndex,
       "gsEPortMirroringSourceSubPort": gsEPortMirroringSourceSubPort,
       "gsEPortMirroringSamplerType": gsEPortMirroringSamplerType,
       "gsEPortMirroringRate": gsEPortMirroringRate,
       "gsEPortMirroringMirrorPort": gsEPortMirroringMirrorPort,
       "gsEVlanMgt": gsEVlanMgt,
       "gsEVlans": gsEVlans,
       "gsEVlanTable": gsEVlanTable,
       "gsEVlanEntry": gsEVlanEntry,
       "gsEVlanID": gsEVlanID,
       "gsEVlanName": gsEVlanName,
       "gsEVlanIfIndex": gsEVlanIfIndex,
       "gsEVlanAFTIndex": gsEVlanAFTIndex,
       "gsEVlanBridgeIndex": gsEVlanBridgeIndex,
       "gsEVlanStatus": gsEVlanStatus,
       "gsEVlanInitialHashTableSize": gsEVlanInitialHashTableSize,
       "gsEVlanAutoIncrementHTSize": gsEVlanAutoIncrementHTSize,
       "gsEVirtualPorts": gsEVirtualPorts,
       "gsEVirtualSwitchPortTable": gsEVirtualSwitchPortTable,
       "gsEVirtualSwitchPortEntry": gsEVirtualSwitchPortEntry,
       "gsEVirtualSwitchPortIndex": gsEVirtualSwitchPortIndex,
       "gsEVirtualSwitchPortFormat": gsEVirtualSwitchPortFormat,
       "gsEVirtualSwitchPortBridgePort": gsEVirtualSwitchPortBridgePort,
       "gsEVirtualSwitchPortBindingType": gsEVirtualSwitchPortBindingType,
       "gsEVirtualSwitchPortStatus": gsEVirtualSwitchPortStatus,
       "gsEEvents": gsEEvents,
       "gsEEventMgt": gsEEventMgt,
       "gsEEventTable": gsEEventTable,
       "gsEEventEntry": gsEEventEntry,
       "gsEEventIndex": gsEEventIndex,
       "gsEEventMode": gsEEventMode,
       "gsEEventLogAction": gsEEventLogAction,
       "gsEEventTrapAction": gsEEventTrapAction,
       "gsEEventConsoleAction": gsEEventConsoleAction,
       "gsEEventLogMgt": gsEEventLogMgt,
       "gsELogTableMaxSize": gsELogTableMaxSize,
       "gsELogLastEntry": gsELogLastEntry,
       "gsELogWraps": gsELogWraps,
       "gsEEventLog": gsEEventLog,
       "gsEEventLogTable": gsEEventLogTable,
       "gsEEventLogEntry": gsEEventLogEntry,
       "gsEEventLogEventIndex": gsEEventLogEventIndex,
       "gsEEventLogIndex": gsEEventLogIndex,
       "gsEEventLogTime": gsEEventLogTime,
       "gsEEventLogDescr": gsEEventLogDescr,
       "gsEEventLogType": gsEEventLogType,
       "gsEEventLogSeverity": gsEEventLogSeverity,
       "gsEEventLogDTM": gsEEventLogDTM,
       "gsEEventLogResType": gsEEventLogResType,
       "gsEEventLogResID": gsEEventLogResID,
       "gsEEventLogResLeaf": gsEEventLogResLeaf,
       "gsEEventLogValueType": gsEEventLogValueType,
       "gsEEventLogValue": gsEEventLogValue,
       "gsEEventLogEpochTime": gsEEventLogEpochTime,
       "gsEEventLogID": gsEEventLogID,
       "gsEShutdownLogMgt": gsEShutdownLogMgt,
       "gsEShutdownLogTableMaxSize": gsEShutdownLogTableMaxSize,
       "gsEShutdownLogLastEntry": gsEShutdownLogLastEntry,
       "gsEShutdownLogAcknowledged": gsEShutdownLogAcknowledged,
       "gsEEventShutdownLog": gsEEventShutdownLog,
       "gsEEventShutdownLogTable": gsEEventShutdownLogTable,
       "gsEEventShutdownLogEntry": gsEEventShutdownLogEntry,
       "gsEEventShutdownLogEventIndex": gsEEventShutdownLogEventIndex,
       "gsEEventShutdownLogIndex": gsEEventShutdownLogIndex,
       "gsEEventShutdownLogTime": gsEEventShutdownLogTime,
       "gsEEventShutdownLogDescr": gsEEventShutdownLogDescr,
       "gsEEventShutdownLogType": gsEEventShutdownLogType,
       "gsEEventShutdownLogSeverity": gsEEventShutdownLogSeverity,
       "gsEEventShutdownLogDTM": gsEEventShutdownLogDTM,
       "gsEEventShutdownLogResType": gsEEventShutdownLogResType,
       "gsEEventShutdownLogResID": gsEEventShutdownLogResID,
       "gsEEventShutdownLogResLeaf": gsEEventShutdownLogResLeaf,
       "gsEEventShutdownLogValueType": gsEEventShutdownLogValueType,
       "gsEEventShutdownLogValue": gsEEventShutdownLogValue,
       "gsEEventShutdownLogEpochTime": gsEEventShutdownLogEpochTime,
       "gsEEventShutdownLogID": gsEEventShutdownLogID,
       "gsEEventTrapMgmt": gsEEventTrapMgmt,
       "gsEEventTrapEventIndex": gsEEventTrapEventIndex,
       "gsEEventTrapTime": gsEEventTrapTime,
       "gsEEventTrapDescr": gsEEventTrapDescr,
       "gsEEventTrapType": gsEEventTrapType,
       "gsEEventTrapSeverity": gsEEventTrapSeverity,
       "gsEEventTrapDTM": gsEEventTrapDTM,
       "gsEEventTrapResType": gsEEventTrapResType,
       "gsEEventTrapResID": gsEEventTrapResID,
       "gsEEventTrapResLeaf": gsEEventTrapResLeaf,
       "gsEEventTrapValueType": gsEEventTrapValueType,
       "gsEEventTrapValue": gsEEventTrapValue,
       "gsEEventTrapEpochTime": gsEEventTrapEpochTime,
       "gsEEventTrapID": gsEEventTrapID,
       "gsEAlarmMgt": gsEAlarmMgt,
       "gsEAlarmGeneral": gsEAlarmGeneral,
       "gsEAlarmGeneralActiveEntries": gsEAlarmGeneralActiveEntries,
       "gsEAlarmGeneralTimeStamp": gsEAlarmGeneralTimeStamp,
       "gsEAlarms": gsEAlarms,
       "gsEActiveAlarmTable": gsEActiveAlarmTable,
       "gsEActiveAlarmEntry": gsEActiveAlarmEntry,
       "gsEActiveAlarmIndex": gsEActiveAlarmIndex,
       "gsEActiveAlarmName": gsEActiveAlarmName,
       "gsEActiveAlarmValueHigh": gsEActiveAlarmValueHigh,
       "gsEActiveAlarmValueLow": gsEActiveAlarmValueLow,
       "gsEActiveAlarmVariable": gsEActiveAlarmVariable,
       "gsEActiveAlarmResType": gsEActiveAlarmResType,
       "gsEActiveAlarmResID": gsEActiveAlarmResID,
       "gsEActiveAlarmLeaf": gsEActiveAlarmLeaf,
       "gsEActiveAlarmOwner": gsEActiveAlarmOwner,
       "gsESnmpTraps": gsESnmpTraps,
       "gsESystemTrap": gsESystemTrap,
       "gsEConfigurationTrap": gsEConfigurationTrap,
       "gsETemperatureTrap": gsETemperatureTrap,
       "gsEResourceTrap": gsEResourceTrap,
       "gsEFanTrap": gsEFanTrap,
       "gsEPowerTrap": gsEPowerTrap}
)
