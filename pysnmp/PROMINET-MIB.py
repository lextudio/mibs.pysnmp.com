# SNMP MIB module (PROMINET-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/PROMINET-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:39:49 2024
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
 TextualConvention,
 TimeStamp) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention",
    "TimeStamp")


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
_Marconi_ObjectIdentity = ObjectIdentity
marconi = _Marconi_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1012)
)
_EthernetL3_ObjectIdentity = ObjectIdentity
ethernetL3 = _EthernetL3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1012, 81)
)
_EsrSwitch_ObjectIdentity = ObjectIdentity
esrSwitch = _EsrSwitch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1012, 81, 1)
)
_Prominet_ObjectIdentity = ObjectIdentity
prominet = _Prominet_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2167)
)
_PromAgent_ObjectIdentity = ObjectIdentity
promAgent = _PromAgent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2167, 1)
)
_PromAgentGen_ObjectIdentity = ObjectIdentity
promAgentGen = _PromAgentGen_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2167, 1, 1)
)


class _PromAgentMIBVersion_Type(DisplayString):
    """Custom type promAgentMIBVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_PromAgentMIBVersion_Type.__name__ = "DisplayString"
_PromAgentMIBVersion_Object = MibScalar
promAgentMIBVersion = _PromAgentMIBVersion_Object(
    (1, 3, 6, 1, 4, 1, 2167, 1, 1, 1),
    _PromAgentMIBVersion_Type()
)
promAgentMIBVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    promAgentMIBVersion.setStatus("mandatory")
_PromAgentMgrIndex_Type = Integer32
_PromAgentMgrIndex_Object = MibScalar
promAgentMgrIndex = _PromAgentMgrIndex_Object(
    (1, 3, 6, 1, 4, 1, 2167, 1, 1, 2),
    _PromAgentMgrIndex_Type()
)
promAgentMgrIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    promAgentMgrIndex.setStatus("mandatory")
_PromAgentCommunity_ObjectIdentity = ObjectIdentity
promAgentCommunity = _PromAgentCommunity_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2167, 1, 2)
)
_PromCommunityTable_Object = MibTable
promCommunityTable = _PromCommunityTable_Object(
    (1, 3, 6, 1, 4, 1, 2167, 1, 2, 1)
)
if mibBuilder.loadTexts:
    promCommunityTable.setStatus("mandatory")
_PromCommunityEntry_Object = MibTableRow
promCommunityEntry = _PromCommunityEntry_Object(
    (1, 3, 6, 1, 4, 1, 2167, 1, 2, 1, 1)
)
promCommunityEntry.setIndexNames(
    (0, "PROMINET-MIB", "promCommunityIndex"),
)
if mibBuilder.loadTexts:
    promCommunityEntry.setStatus("mandatory")
_PromCommunityIndex_Type = Integer32
_PromCommunityIndex_Object = MibTableColumn
promCommunityIndex = _PromCommunityIndex_Object(
    (1, 3, 6, 1, 4, 1, 2167, 1, 2, 1, 1, 1),
    _PromCommunityIndex_Type()
)
promCommunityIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    promCommunityIndex.setStatus("mandatory")


class _PromCommunityString_Type(DisplayString):
    """Custom type promCommunityString based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_PromCommunityString_Type.__name__ = "DisplayString"
_PromCommunityString_Object = MibTableColumn
promCommunityString = _PromCommunityString_Object(
    (1, 3, 6, 1, 4, 1, 2167, 1, 2, 1, 1, 2),
    _PromCommunityString_Type()
)
promCommunityString.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    promCommunityString.setStatus("mandatory")


class _PromCommunityAddressType_Type(Integer32):
    """Custom type promCommunityAddressType based on Integer32"""
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


_PromCommunityAddressType_Type.__name__ = "Integer32"
_PromCommunityAddressType_Object = MibTableColumn
promCommunityAddressType = _PromCommunityAddressType_Object(
    (1, 3, 6, 1, 4, 1, 2167, 1, 2, 1, 1, 3),
    _PromCommunityAddressType_Type()
)
promCommunityAddressType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    promCommunityAddressType.setStatus("mandatory")
_PromCommunityAddress_Type = IpAddress
_PromCommunityAddress_Object = MibTableColumn
promCommunityAddress = _PromCommunityAddress_Object(
    (1, 3, 6, 1, 4, 1, 2167, 1, 2, 1, 1, 4),
    _PromCommunityAddress_Type()
)
promCommunityAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    promCommunityAddress.setStatus("mandatory")


class _PromCommunityAccess_Type(Integer32):
    """Custom type promCommunityAccess based on Integer32"""
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


_PromCommunityAccess_Type.__name__ = "Integer32"
_PromCommunityAccess_Object = MibTableColumn
promCommunityAccess = _PromCommunityAccess_Object(
    (1, 3, 6, 1, 4, 1, 2167, 1, 2, 1, 1, 5),
    _PromCommunityAccess_Type()
)
promCommunityAccess.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    promCommunityAccess.setStatus("mandatory")


class _PromCommunityTrapReceiver_Type(Integer32):
    """Custom type promCommunityTrapReceiver based on Integer32"""
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


_PromCommunityTrapReceiver_Type.__name__ = "Integer32"
_PromCommunityTrapReceiver_Object = MibTableColumn
promCommunityTrapReceiver = _PromCommunityTrapReceiver_Object(
    (1, 3, 6, 1, 4, 1, 2167, 1, 2, 1, 1, 6),
    _PromCommunityTrapReceiver_Type()
)
promCommunityTrapReceiver.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    promCommunityTrapReceiver.setStatus("mandatory")


class _PromCommunitySecurityLevel_Type(Integer32):
    """Custom type promCommunitySecurityLevel based on Integer32"""
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


_PromCommunitySecurityLevel_Type.__name__ = "Integer32"
_PromCommunitySecurityLevel_Object = MibTableColumn
promCommunitySecurityLevel = _PromCommunitySecurityLevel_Object(
    (1, 3, 6, 1, 4, 1, 2167, 1, 2, 1, 1, 7),
    _PromCommunitySecurityLevel_Type()
)
promCommunitySecurityLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    promCommunitySecurityLevel.setStatus("mandatory")
_PromCommunityStatus_Type = RowStatus
_PromCommunityStatus_Object = MibTableColumn
promCommunityStatus = _PromCommunityStatus_Object(
    (1, 3, 6, 1, 4, 1, 2167, 1, 2, 1, 1, 8),
    _PromCommunityStatus_Type()
)
promCommunityStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    promCommunityStatus.setStatus("mandatory")
_PromAgentWeb_ObjectIdentity = ObjectIdentity
promAgentWeb = _PromAgentWeb_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2167, 1, 3)
)


class _PromAgentWebServerURL_Type(DisplayString):
    """Custom type promAgentWebServerURL based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_PromAgentWebServerURL_Type.__name__ = "DisplayString"
_PromAgentWebServerURL_Object = MibScalar
promAgentWebServerURL = _PromAgentWebServerURL_Object(
    (1, 3, 6, 1, 4, 1, 2167, 1, 3, 1),
    _PromAgentWebServerURL_Type()
)
promAgentWebServerURL.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    promAgentWebServerURL.setStatus("mandatory")


class _PromAgentWebServerHelpDirectory_Type(DisplayString):
    """Custom type promAgentWebServerHelpDirectory based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_PromAgentWebServerHelpDirectory_Type.__name__ = "DisplayString"
_PromAgentWebServerHelpDirectory_Object = MibScalar
promAgentWebServerHelpDirectory = _PromAgentWebServerHelpDirectory_Object(
    (1, 3, 6, 1, 4, 1, 2167, 1, 3, 2),
    _PromAgentWebServerHelpDirectory_Type()
)
promAgentWebServerHelpDirectory.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    promAgentWebServerHelpDirectory.setStatus("mandatory")
_PromChassis_ObjectIdentity = ObjectIdentity
promChassis = _PromChassis_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2167, 3)
)
_PromChassisGen_ObjectIdentity = ObjectIdentity
promChassisGen = _PromChassisGen_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2167, 3, 1)
)


class _PromChassisType_Type(Integer32):
    """Custom type promChassisType based on Integer32"""
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
        *(("p220", 2),
          ("p550", 1),
          ("p580", 5),
          ("p660", 3),
          ("p880", 4),
          ("p882", 6))
    )


_PromChassisType_Type.__name__ = "Integer32"
_PromChassisType_Object = MibScalar
promChassisType = _PromChassisType_Object(
    (1, 3, 6, 1, 4, 1, 2167, 3, 1, 1),
    _PromChassisType_Type()
)
promChassisType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    promChassisType.setStatus("mandatory")
_PromChassisSlots_Type = Integer32
_PromChassisSlots_Object = MibScalar
promChassisSlots = _PromChassisSlots_Object(
    (1, 3, 6, 1, 4, 1, 2167, 3, 1, 2),
    _PromChassisSlots_Type()
)
promChassisSlots.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    promChassisSlots.setStatus("mandatory")


class _PromChassisSystemReset_Type(Integer32):
    """Custom type promChassisSystemReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("reset", 1)
    )


_PromChassisSystemReset_Type.__name__ = "Integer32"
_PromChassisSystemReset_Object = MibScalar
promChassisSystemReset = _PromChassisSystemReset_Object(
    (1, 3, 6, 1, 4, 1, 2167, 3, 1, 3),
    _PromChassisSystemReset_Type()
)
promChassisSystemReset.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    promChassisSystemReset.setStatus("mandatory")
_PromInventory_ObjectIdentity = ObjectIdentity
promInventory = _PromInventory_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2167, 3, 2)
)
_PromInventoryTable_Object = MibTable
promInventoryTable = _PromInventoryTable_Object(
    (1, 3, 6, 1, 4, 1, 2167, 3, 2, 1)
)
if mibBuilder.loadTexts:
    promInventoryTable.setStatus("mandatory")
_PromInventoryEntry_Object = MibTableRow
promInventoryEntry = _PromInventoryEntry_Object(
    (1, 3, 6, 1, 4, 1, 2167, 3, 2, 1, 1)
)
promInventoryEntry.setIndexNames(
    (0, "PROMINET-MIB", "promInventoryResourceType"),
    (0, "PROMINET-MIB", "promInventoryResourceIndex"),
)
if mibBuilder.loadTexts:
    promInventoryEntry.setStatus("mandatory")
_PromInventoryResourceType_Type = ResourceType
_PromInventoryResourceType_Object = MibTableColumn
promInventoryResourceType = _PromInventoryResourceType_Object(
    (1, 3, 6, 1, 4, 1, 2167, 3, 2, 1, 1, 1),
    _PromInventoryResourceType_Type()
)
promInventoryResourceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    promInventoryResourceType.setStatus("mandatory")
_PromInventoryResourceIndex_Type = ResourceId
_PromInventoryResourceIndex_Object = MibTableColumn
promInventoryResourceIndex = _PromInventoryResourceIndex_Object(
    (1, 3, 6, 1, 4, 1, 2167, 3, 2, 1, 1, 2),
    _PromInventoryResourceIndex_Type()
)
promInventoryResourceIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    promInventoryResourceIndex.setStatus("mandatory")


class _PromInventoryModelNumber_Type(DisplayString):
    """Custom type promInventoryModelNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_PromInventoryModelNumber_Type.__name__ = "DisplayString"
_PromInventoryModelNumber_Object = MibTableColumn
promInventoryModelNumber = _PromInventoryModelNumber_Object(
    (1, 3, 6, 1, 4, 1, 2167, 3, 2, 1, 1, 3),
    _PromInventoryModelNumber_Type()
)
promInventoryModelNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    promInventoryModelNumber.setStatus("mandatory")


class _PromInventorySerialNumber_Type(DisplayString):
    """Custom type promInventorySerialNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_PromInventorySerialNumber_Type.__name__ = "DisplayString"
_PromInventorySerialNumber_Object = MibTableColumn
promInventorySerialNumber = _PromInventorySerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 2167, 3, 2, 1, 1, 4),
    _PromInventorySerialNumber_Type()
)
promInventorySerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    promInventorySerialNumber.setStatus("mandatory")


class _PromInventoryVersion_Type(DisplayString):
    """Custom type promInventoryVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_PromInventoryVersion_Type.__name__ = "DisplayString"
_PromInventoryVersion_Object = MibTableColumn
promInventoryVersion = _PromInventoryVersion_Object(
    (1, 3, 6, 1, 4, 1, 2167, 3, 2, 1, 1, 5),
    _PromInventoryVersion_Type()
)
promInventoryVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    promInventoryVersion.setStatus("mandatory")


class _PromInventoryManufactureInfo_Type(DisplayString):
    """Custom type promInventoryManufactureInfo based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_PromInventoryManufactureInfo_Type.__name__ = "DisplayString"
_PromInventoryManufactureInfo_Object = MibTableColumn
promInventoryManufactureInfo = _PromInventoryManufactureInfo_Object(
    (1, 3, 6, 1, 4, 1, 2167, 3, 2, 1, 1, 6),
    _PromInventoryManufactureInfo_Type()
)
promInventoryManufactureInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    promInventoryManufactureInfo.setStatus("mandatory")


class _PromInventoryScratchPad_Type(DisplayString):
    """Custom type promInventoryScratchPad based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_PromInventoryScratchPad_Type.__name__ = "DisplayString"
_PromInventoryScratchPad_Object = MibTableColumn
promInventoryScratchPad = _PromInventoryScratchPad_Object(
    (1, 3, 6, 1, 4, 1, 2167, 3, 2, 1, 1, 7),
    _PromInventoryScratchPad_Type()
)
promInventoryScratchPad.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    promInventoryScratchPad.setStatus("mandatory")


class _PromInventoryPowerConsumption_Type(DisplayString):
    """Custom type promInventoryPowerConsumption based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_PromInventoryPowerConsumption_Type.__name__ = "DisplayString"
_PromInventoryPowerConsumption_Object = MibTableColumn
promInventoryPowerConsumption = _PromInventoryPowerConsumption_Object(
    (1, 3, 6, 1, 4, 1, 2167, 3, 2, 1, 1, 8),
    _PromInventoryPowerConsumption_Type()
)
promInventoryPowerConsumption.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    promInventoryPowerConsumption.setStatus("mandatory")
_PromPowerSystems_ObjectIdentity = ObjectIdentity
promPowerSystems = _PromPowerSystems_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2167, 3, 3)
)
_PromPowerSupplies_ObjectIdentity = ObjectIdentity
promPowerSupplies = _PromPowerSupplies_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2167, 3, 3, 1)
)
_PromPowerSupplyTable_Object = MibTable
promPowerSupplyTable = _PromPowerSupplyTable_Object(
    (1, 3, 6, 1, 4, 1, 2167, 3, 3, 1, 1)
)
if mibBuilder.loadTexts:
    promPowerSupplyTable.setStatus("mandatory")
_PromPowerSupplyEntry_Object = MibTableRow
promPowerSupplyEntry = _PromPowerSupplyEntry_Object(
    (1, 3, 6, 1, 4, 1, 2167, 3, 3, 1, 1, 1)
)
promPowerSupplyEntry.setIndexNames(
    (0, "PROMINET-MIB", "promPowerSupplyIndex"),
)
if mibBuilder.loadTexts:
    promPowerSupplyEntry.setStatus("mandatory")
_PromPowerSupplyIndex_Type = ResourceId
_PromPowerSupplyIndex_Object = MibTableColumn
promPowerSupplyIndex = _PromPowerSupplyIndex_Object(
    (1, 3, 6, 1, 4, 1, 2167, 3, 3, 1, 1, 1, 1),
    _PromPowerSupplyIndex_Type()
)
promPowerSupplyIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    promPowerSupplyIndex.setStatus("mandatory")


class _PromPowerSupplyType_Type(Integer32):
    """Custom type promPowerSupplyType based on Integer32"""
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


_PromPowerSupplyType_Type.__name__ = "Integer32"
_PromPowerSupplyType_Object = MibTableColumn
promPowerSupplyType = _PromPowerSupplyType_Object(
    (1, 3, 6, 1, 4, 1, 2167, 3, 3, 1, 1, 1, 2),
    _PromPowerSupplyType_Type()
)
promPowerSupplyType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    promPowerSupplyType.setStatus("mandatory")


class _PromPowerSupplyStatus_Type(Integer32):
    """Custom type promPowerSupplyStatus based on Integer32"""
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


_PromPowerSupplyStatus_Type.__name__ = "Integer32"
_PromPowerSupplyStatus_Object = MibTableColumn
promPowerSupplyStatus = _PromPowerSupplyStatus_Object(
    (1, 3, 6, 1, 4, 1, 2167, 3, 3, 1, 1, 1, 3),
    _PromPowerSupplyStatus_Type()
)
promPowerSupplyStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    promPowerSupplyStatus.setStatus("mandatory")


class _PromPowerSupplyInputStatus_Type(Integer32):
    """Custom type promPowerSupplyInputStatus based on Integer32"""
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


_PromPowerSupplyInputStatus_Type.__name__ = "Integer32"
_PromPowerSupplyInputStatus_Object = MibTableColumn
promPowerSupplyInputStatus = _PromPowerSupplyInputStatus_Object(
    (1, 3, 6, 1, 4, 1, 2167, 3, 3, 1, 1, 1, 4),
    _PromPowerSupplyInputStatus_Type()
)
promPowerSupplyInputStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    promPowerSupplyInputStatus.setStatus("mandatory")


class _PromPowerSupplyOutputStatus_Type(Integer32):
    """Custom type promPowerSupplyOutputStatus based on Integer32"""
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


_PromPowerSupplyOutputStatus_Type.__name__ = "Integer32"
_PromPowerSupplyOutputStatus_Object = MibTableColumn
promPowerSupplyOutputStatus = _PromPowerSupplyOutputStatus_Object(
    (1, 3, 6, 1, 4, 1, 2167, 3, 3, 1, 1, 1, 5),
    _PromPowerSupplyOutputStatus_Type()
)
promPowerSupplyOutputStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    promPowerSupplyOutputStatus.setStatus("mandatory")
_PromPowerSupplyOutputCapacity_Type = Integer32
_PromPowerSupplyOutputCapacity_Object = MibTableColumn
promPowerSupplyOutputCapacity = _PromPowerSupplyOutputCapacity_Object(
    (1, 3, 6, 1, 4, 1, 2167, 3, 3, 1, 1, 1, 6),
    _PromPowerSupplyOutputCapacity_Type()
)
promPowerSupplyOutputCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    promPowerSupplyOutputCapacity.setStatus("mandatory")
_PromPowerMgmtGen_ObjectIdentity = ObjectIdentity
promPowerMgmtGen = _PromPowerMgmtGen_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2167, 3, 3, 2)
)
_PromPowerCapacity_Type = Integer32
_PromPowerCapacity_Object = MibScalar
promPowerCapacity = _PromPowerCapacity_Object(
    (1, 3, 6, 1, 4, 1, 2167, 3, 3, 2, 1),
    _PromPowerCapacity_Type()
)
promPowerCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    promPowerCapacity.setStatus("mandatory")
_PromPowerUsed_Type = Integer32
_PromPowerUsed_Object = MibScalar
promPowerUsed = _PromPowerUsed_Object(
    (1, 3, 6, 1, 4, 1, 2167, 3, 3, 2, 2),
    _PromPowerUsed_Type()
)
promPowerUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    promPowerUsed.setStatus("mandatory")
_PromPowerMgmtCtl_ObjectIdentity = ObjectIdentity
promPowerMgmtCtl = _PromPowerMgmtCtl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2167, 3, 3, 3)
)
_PromPowerControlTable_Object = MibTable
promPowerControlTable = _PromPowerControlTable_Object(
    (1, 3, 6, 1, 4, 1, 2167, 3, 3, 3, 1)
)
if mibBuilder.loadTexts:
    promPowerControlTable.setStatus("obsolete")
_PromPowerControlEntry_Object = MibTableRow
promPowerControlEntry = _PromPowerControlEntry_Object(
    (1, 3, 6, 1, 4, 1, 2167, 3, 3, 3, 1, 1)
)
promPowerControlEntry.setIndexNames(
    (0, "PROMINET-MIB", "promModuleIndex"),
)
if mibBuilder.loadTexts:
    promPowerControlEntry.setStatus("obsolete")
_PromPowerControlUsed_Type = Integer32
_PromPowerControlUsed_Object = MibTableColumn
promPowerControlUsed = _PromPowerControlUsed_Object(
    (1, 3, 6, 1, 4, 1, 2167, 3, 3, 3, 1, 1, 1),
    _PromPowerControlUsed_Type()
)
promPowerControlUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    promPowerControlUsed.setStatus("obsolete")


class _PromPowerControlPriority_Type(Integer32):
    """Custom type promPowerControlPriority based on Integer32"""
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


_PromPowerControlPriority_Type.__name__ = "Integer32"
_PromPowerControlPriority_Object = MibTableColumn
promPowerControlPriority = _PromPowerControlPriority_Object(
    (1, 3, 6, 1, 4, 1, 2167, 3, 3, 3, 1, 1, 2),
    _PromPowerControlPriority_Type()
)
promPowerControlPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    promPowerControlPriority.setStatus("obsolete")


class _PromPowerControlMode_Type(Integer32):
    """Custom type promPowerControlMode based on Integer32"""
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


_PromPowerControlMode_Type.__name__ = "Integer32"
_PromPowerControlMode_Object = MibTableColumn
promPowerControlMode = _PromPowerControlMode_Object(
    (1, 3, 6, 1, 4, 1, 2167, 3, 3, 3, 1, 1, 3),
    _PromPowerControlMode_Type()
)
promPowerControlMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    promPowerControlMode.setStatus("obsolete")
_PromTemperature_ObjectIdentity = ObjectIdentity
promTemperature = _PromTemperature_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2167, 3, 4)
)
_PromTempTable_Object = MibTable
promTempTable = _PromTempTable_Object(
    (1, 3, 6, 1, 4, 1, 2167, 3, 4, 1)
)
if mibBuilder.loadTexts:
    promTempTable.setStatus("mandatory")
_PromTempEntry_Object = MibTableRow
promTempEntry = _PromTempEntry_Object(
    (1, 3, 6, 1, 4, 1, 2167, 3, 4, 1, 1)
)
promTempEntry.setIndexNames(
    (0, "PROMINET-MIB", "promTempIndex"),
)
if mibBuilder.loadTexts:
    promTempEntry.setStatus("mandatory")
_PromTempIndex_Type = ResourceId
_PromTempIndex_Object = MibTableColumn
promTempIndex = _PromTempIndex_Object(
    (1, 3, 6, 1, 4, 1, 2167, 3, 4, 1, 1, 1),
    _PromTempIndex_Type()
)
promTempIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    promTempIndex.setStatus("mandatory")
_PromTempValue_Type = Integer32
_PromTempValue_Object = MibTableColumn
promTempValue = _PromTempValue_Object(
    (1, 3, 6, 1, 4, 1, 2167, 3, 4, 1, 1, 2),
    _PromTempValue_Type()
)
promTempValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    promTempValue.setStatus("mandatory")
_PromTempUpperLimit_Type = Integer32
_PromTempUpperLimit_Object = MibTableColumn
promTempUpperLimit = _PromTempUpperLimit_Object(
    (1, 3, 6, 1, 4, 1, 2167, 3, 4, 1, 1, 3),
    _PromTempUpperLimit_Type()
)
promTempUpperLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    promTempUpperLimit.setStatus("mandatory")
_PromTempUpperWarning_Type = Integer32
_PromTempUpperWarning_Object = MibTableColumn
promTempUpperWarning = _PromTempUpperWarning_Object(
    (1, 3, 6, 1, 4, 1, 2167, 3, 4, 1, 1, 4),
    _PromTempUpperWarning_Type()
)
promTempUpperWarning.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    promTempUpperWarning.setStatus("mandatory")
_PromTempLowerWarning_Type = Integer32
_PromTempLowerWarning_Object = MibTableColumn
promTempLowerWarning = _PromTempLowerWarning_Object(
    (1, 3, 6, 1, 4, 1, 2167, 3, 4, 1, 1, 5),
    _PromTempLowerWarning_Type()
)
promTempLowerWarning.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    promTempLowerWarning.setStatus("mandatory")
_PromTempLowerLimit_Type = Integer32
_PromTempLowerLimit_Object = MibTableColumn
promTempLowerLimit = _PromTempLowerLimit_Object(
    (1, 3, 6, 1, 4, 1, 2167, 3, 4, 1, 1, 6),
    _PromTempLowerLimit_Type()
)
promTempLowerLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    promTempLowerLimit.setStatus("mandatory")
_PromModules_ObjectIdentity = ObjectIdentity
promModules = _PromModules_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2167, 3, 5)
)
_PromModuleTable_Object = MibTable
promModuleTable = _PromModuleTable_Object(
    (1, 3, 6, 1, 4, 1, 2167, 3, 5, 1)
)
if mibBuilder.loadTexts:
    promModuleTable.setStatus("mandatory")
_PromModuleEntry_Object = MibTableRow
promModuleEntry = _PromModuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 2167, 3, 5, 1, 1)
)
promModuleEntry.setIndexNames(
    (0, "PROMINET-MIB", "promModuleIndex"),
)
if mibBuilder.loadTexts:
    promModuleEntry.setStatus("mandatory")
_PromModuleIndex_Type = ResourceId
_PromModuleIndex_Object = MibTableColumn
promModuleIndex = _PromModuleIndex_Object(
    (1, 3, 6, 1, 4, 1, 2167, 3, 5, 1, 1, 1),
    _PromModuleIndex_Type()
)
promModuleIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    promModuleIndex.setStatus("mandatory")


class _PromModuleName_Type(DisplayString):
    """Custom type promModuleName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_PromModuleName_Type.__name__ = "DisplayString"
_PromModuleName_Object = MibTableColumn
promModuleName = _PromModuleName_Object(
    (1, 3, 6, 1, 4, 1, 2167, 3, 5, 1, 1, 2),
    _PromModuleName_Type()
)
promModuleName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    promModuleName.setStatus("mandatory")


class _PromModuleType_Type(Integer32):
    """Custom type promModuleType based on Integer32"""
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
              20,
              21,
              22,
              23,
              24,
              25,
              26,
              27,
              28,
              29,
              30,
              31,
              32,
              33,
              34,
              35,
              36,
              37,
              38,
              39,
              40,
              41,
              42,
              43,
              44,
              45,
              46,
              47,
              48,
              57)
        )
    )
    namedValues = NamedValues(
        *(("m2200-SUP", 15),
          ("m2201-1000", 8),
          ("m2201-1000LX", 25),
          ("m2201-1000SLX", 26),
          ("m2201-1000SX", 24),
          ("m2202-100FX", 10),
          ("m2204-100TX-I", 16),
          ("m2204-100TX-LUC", 20),
          ("m2206-1000", 3),
          ("m2224-100TX", 17),
          ("m5500-SUP", 6),
          ("m5500R-HUR", 30),
          ("m5500R-SUP", 13),
          ("m5500R-SUPA", 27),
          ("m5502-1000", 2),
          ("m5502-AOC12MMF", 23),
          ("m5502-AOC12SMF", 22),
          ("m5502-AOC3MMF", 40),
          ("m5502-AOC3SMF", 39),
          ("m5502-OC3", 18),
          ("m5502R-1000", 14),
          ("m5504-1000", 7),
          ("m5504-AOC3MMF", 36),
          ("m5504-AOC3SMF", 35),
          ("m5510-100FX", 5),
          ("m5510R-100FX", 11),
          ("m5512R-100TX", 12),
          ("m5520-100TX-I", 9),
          ("m5520-100TX-LUC", 19),
          ("m5520-100TX-QS", 4),
          ("m5548-100TX-BCM", 21),
          ("m8000R-HUR", 41),
          ("m8000R-SUP", 28),
          ("m8001-CMTS", 38),
          ("m8002-1000", 29),
          ("m8002R-AOC12MMF", 46),
          ("m8002R-AOC12SMF", 45),
          ("m8002R-AOC3MMF", 48),
          ("m8002R-AOC3SMF", 47),
          ("m8004-1000", 37),
          ("m8004R-1000T", 43),
          ("m8008-1000", 34),
          ("m8008R-1000T", 42),
          ("m8024-100FX", 33),
          ("m8024-100TX", 31),
          ("m8024R-100FXW", 44),
          ("m8048-100TX", 32),
          ("m8048-JB-100TX", 57),
          ("unknown", 1))
    )


_PromModuleType_Type.__name__ = "Integer32"
_PromModuleType_Object = MibTableColumn
promModuleType = _PromModuleType_Object(
    (1, 3, 6, 1, 4, 1, 2167, 3, 5, 1, 1, 3),
    _PromModuleType_Type()
)
promModuleType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    promModuleType.setStatus("mandatory")


class _PromModuleBaseType_Type(Integer32):
    """Custom type promModuleBaseType based on Integer32"""
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
        *(("fastEthernet", 2),
          ("gigabit", 1),
          ("serverSwitching", 6),
          ("supervisor", 3),
          ("unspecified", 4),
          ("uplink", 5))
    )


_PromModuleBaseType_Type.__name__ = "Integer32"
_PromModuleBaseType_Object = MibTableColumn
promModuleBaseType = _PromModuleBaseType_Object(
    (1, 3, 6, 1, 4, 1, 2167, 3, 5, 1, 1, 4),
    _PromModuleBaseType_Type()
)
promModuleBaseType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    promModuleBaseType.setStatus("mandatory")
_PromModuleSlotWidth_Type = Integer32
_PromModuleSlotWidth_Object = MibTableColumn
promModuleSlotWidth = _PromModuleSlotWidth_Object(
    (1, 3, 6, 1, 4, 1, 2167, 3, 5, 1, 1, 5),
    _PromModuleSlotWidth_Type()
)
promModuleSlotWidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    promModuleSlotWidth.setStatus("mandatory")
_PromModuleSlotOffset_Type = Integer32
_PromModuleSlotOffset_Object = MibTableColumn
promModuleSlotOffset = _PromModuleSlotOffset_Object(
    (1, 3, 6, 1, 4, 1, 2167, 3, 5, 1, 1, 6),
    _PromModuleSlotOffset_Type()
)
promModuleSlotOffset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    promModuleSlotOffset.setStatus("mandatory")
_PromModulePorts_Type = Integer32
_PromModulePorts_Object = MibTableColumn
promModulePorts = _PromModulePorts_Object(
    (1, 3, 6, 1, 4, 1, 2167, 3, 5, 1, 1, 7),
    _PromModulePorts_Type()
)
promModulePorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    promModulePorts.setStatus("mandatory")
_PromModuleUpdateTime_Type = TimeStamp
_PromModuleUpdateTime_Object = MibScalar
promModuleUpdateTime = _PromModuleUpdateTime_Object(
    (1, 3, 6, 1, 4, 1, 2167, 3, 5, 2),
    _PromModuleUpdateTime_Type()
)
promModuleUpdateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    promModuleUpdateTime.setStatus("mandatory")
_PromModuleUpdateList_Type = OctetString
_PromModuleUpdateList_Object = MibScalar
promModuleUpdateList = _PromModuleUpdateList_Object(
    (1, 3, 6, 1, 4, 1, 2167, 3, 5, 3),
    _PromModuleUpdateList_Type()
)
promModuleUpdateList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    promModuleUpdateList.setStatus("mandatory")
_PromPorts_ObjectIdentity = ObjectIdentity
promPorts = _PromPorts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2167, 3, 6)
)
_PromPortMgt_ObjectIdentity = ObjectIdentity
promPortMgt = _PromPortMgt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2167, 3, 6, 1)
)
_PromPortTable_Object = MibTable
promPortTable = _PromPortTable_Object(
    (1, 3, 6, 1, 4, 1, 2167, 3, 6, 1, 1)
)
if mibBuilder.loadTexts:
    promPortTable.setStatus("mandatory")
_PromPortEntry_Object = MibTableRow
promPortEntry = _PromPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 2167, 3, 6, 1, 1, 1)
)
promPortEntry.setIndexNames(
    (0, "PROMINET-MIB", "promPortIndex"),
)
if mibBuilder.loadTexts:
    promPortEntry.setStatus("mandatory")
_PromPortIndex_Type = ResourceId
_PromPortIndex_Object = MibTableColumn
promPortIndex = _PromPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 2167, 3, 6, 1, 1, 1, 1),
    _PromPortIndex_Type()
)
promPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    promPortIndex.setStatus("mandatory")


class _PromPortName_Type(DisplayString):
    """Custom type promPortName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_PromPortName_Type.__name__ = "DisplayString"
_PromPortName_Object = MibTableColumn
promPortName = _PromPortName_Object(
    (1, 3, 6, 1, 4, 1, 2167, 3, 6, 1, 1, 1, 2),
    _PromPortName_Type()
)
promPortName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    promPortName.setStatus("mandatory")


class _PromPortType_Type(Integer32):
    """Custom type promPortType based on Integer32"""
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
        *(("atm", 8),
          ("ether-gigabit", 4),
          ("ether-gigabit-lxt1000-copper", 6),
          ("ether-gigabit2", 5),
          ("ether-oneHundred", 3),
          ("ether-ten-oneHundred", 2),
          ("ether-ten-oneHundred-bcm5308-rj71", 7),
          ("internal", 1))
    )


_PromPortType_Type.__name__ = "Integer32"
_PromPortType_Object = MibTableColumn
promPortType = _PromPortType_Object(
    (1, 3, 6, 1, 4, 1, 2167, 3, 6, 1, 1, 1, 3),
    _PromPortType_Type()
)
promPortType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    promPortType.setStatus("mandatory")


class _PromPortBaseType_Type(Integer32):
    """Custom type promPortBaseType based on Integer32"""
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
        *(("atm", 5),
          ("ether-gigabit", 4),
          ("ether-oneHundred", 3),
          ("ether-ten-oneHundred", 2),
          ("internal", 1))
    )


_PromPortBaseType_Type.__name__ = "Integer32"
_PromPortBaseType_Object = MibTableColumn
promPortBaseType = _PromPortBaseType_Object(
    (1, 3, 6, 1, 4, 1, 2167, 3, 6, 1, 1, 1, 4),
    _PromPortBaseType_Type()
)
promPortBaseType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    promPortBaseType.setStatus("mandatory")


class _PromPortMode_Type(Integer32):
    """Custom type promPortMode based on Integer32"""
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


_PromPortMode_Type.__name__ = "Integer32"
_PromPortMode_Object = MibTableColumn
promPortMode = _PromPortMode_Object(
    (1, 3, 6, 1, 4, 1, 2167, 3, 6, 1, 1, 1, 5),
    _PromPortMode_Type()
)
promPortMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    promPortMode.setStatus("mandatory")


class _PromPortStatus_Type(Integer32):
    """Custom type promPortStatus based on Integer32"""
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


_PromPortStatus_Type.__name__ = "Integer32"
_PromPortStatus_Object = MibTableColumn
promPortStatus = _PromPortStatus_Object(
    (1, 3, 6, 1, 4, 1, 2167, 3, 6, 1, 1, 1, 6),
    _PromPortStatus_Type()
)
promPortStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    promPortStatus.setStatus("mandatory")


class _PromPortConnector_Type(Integer32):
    """Custom type promPortConnector based on Integer32"""
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
              12)
        )
    )
    namedValues = NamedValues(
        *(("aui", 6),
          ("fiber-SC", 4),
          ("fiber-ST", 3),
          ("gbic-1000-LX", 9),
          ("gbic-1000-LX-LH", 10),
          ("gbic-1000-SX", 8),
          ("internal", 1),
          ("notPresent", 11),
          ("rj45", 2),
          ("rj71", 7),
          ("rs-232", 5),
          ("unsupported", 12))
    )


_PromPortConnector_Type.__name__ = "Integer32"
_PromPortConnector_Object = MibTableColumn
promPortConnector = _PromPortConnector_Object(
    (1, 3, 6, 1, 4, 1, 2167, 3, 6, 1, 1, 1, 7),
    _PromPortConnector_Type()
)
promPortConnector.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    promPortConnector.setStatus("mandatory")


class _PromPortSpeedState_Type(Integer32):
    """Custom type promPortSpeedState based on Integer32"""
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
        *(("one-gigabit-per-second", 5),
          ("one-hundred-fifty-five-megabits-per-second", 3),
          ("one-hundred-megabits-per-second", 2),
          ("six-hundred-twenty-two-megabits-per-second", 4),
          ("ten-megabits-per-second", 1),
          ("under-negotiation", 6))
    )


_PromPortSpeedState_Type.__name__ = "Integer32"
_PromPortSpeedState_Object = MibTableColumn
promPortSpeedState = _PromPortSpeedState_Object(
    (1, 3, 6, 1, 4, 1, 2167, 3, 6, 1, 1, 1, 8),
    _PromPortSpeedState_Type()
)
promPortSpeedState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    promPortSpeedState.setStatus("mandatory")


class _PromPortDuplexState_Type(Integer32):
    """Custom type promPortDuplexState based on Integer32"""
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


_PromPortDuplexState_Type.__name__ = "Integer32"
_PromPortDuplexState_Object = MibTableColumn
promPortDuplexState = _PromPortDuplexState_Object(
    (1, 3, 6, 1, 4, 1, 2167, 3, 6, 1, 1, 1, 9),
    _PromPortDuplexState_Type()
)
promPortDuplexState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    promPortDuplexState.setStatus("mandatory")
_PromPortGroupBinding_Type = ResourceId
_PromPortGroupBinding_Object = MibTableColumn
promPortGroupBinding = _PromPortGroupBinding_Object(
    (1, 3, 6, 1, 4, 1, 2167, 3, 6, 1, 1, 1, 10),
    _PromPortGroupBinding_Type()
)
promPortGroupBinding.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    promPortGroupBinding.setStatus("mandatory")


class _PromPortFlowControlState_Type(Integer32):
    """Custom type promPortFlowControlState based on Integer32"""
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
        *(("disable", 2),
          ("enable", 1),
          ("enable-respond-only", 5),
          ("enable-send-only", 4),
          ("enable-with-aggressive-backoff", 3),
          ("under-negotiation", 6))
    )


_PromPortFlowControlState_Type.__name__ = "Integer32"
_PromPortFlowControlState_Object = MibTableColumn
promPortFlowControlState = _PromPortFlowControlState_Object(
    (1, 3, 6, 1, 4, 1, 2167, 3, 6, 1, 1, 1, 11),
    _PromPortFlowControlState_Type()
)
promPortFlowControlState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    promPortFlowControlState.setStatus("mandatory")
_PromPortFlowControlMgt_ObjectIdentity = ObjectIdentity
promPortFlowControlMgt = _PromPortFlowControlMgt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2167, 3, 6, 2)
)
_PromPortFlowControlTable_Object = MibTable
promPortFlowControlTable = _PromPortFlowControlTable_Object(
    (1, 3, 6, 1, 4, 1, 2167, 3, 6, 2, 1)
)
if mibBuilder.loadTexts:
    promPortFlowControlTable.setStatus("mandatory")
_PromPortFlowControlEntry_Object = MibTableRow
promPortFlowControlEntry = _PromPortFlowControlEntry_Object(
    (1, 3, 6, 1, 4, 1, 2167, 3, 6, 2, 1, 1)
)
promPortFlowControlEntry.setIndexNames(
    (0, "PROMINET-MIB", "promPortIndex"),
)
if mibBuilder.loadTexts:
    promPortFlowControlEntry.setStatus("mandatory")


class _PromPortFlowControlMode_Type(Integer32):
    """Custom type promPortFlowControlMode based on Integer32"""
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
        *(("disable", 2),
          ("enable", 1),
          ("enable-respond-only", 5),
          ("enable-send-only", 4),
          ("enable-with-aggressive-backoff", 3))
    )


_PromPortFlowControlMode_Type.__name__ = "Integer32"
_PromPortFlowControlMode_Object = MibTableColumn
promPortFlowControlMode = _PromPortFlowControlMode_Object(
    (1, 3, 6, 1, 4, 1, 2167, 3, 6, 2, 1, 1, 21),
    _PromPortFlowControlMode_Type()
)
promPortFlowControlMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    promPortFlowControlMode.setStatus("mandatory")
_PromPortDuplexMgt_ObjectIdentity = ObjectIdentity
promPortDuplexMgt = _PromPortDuplexMgt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2167, 3, 6, 3)
)
_PromPortDuplexTable_Object = MibTable
promPortDuplexTable = _PromPortDuplexTable_Object(
    (1, 3, 6, 1, 4, 1, 2167, 3, 6, 3, 1)
)
if mibBuilder.loadTexts:
    promPortDuplexTable.setStatus("mandatory")
_PromPortDuplexEntry_Object = MibTableRow
promPortDuplexEntry = _PromPortDuplexEntry_Object(
    (1, 3, 6, 1, 4, 1, 2167, 3, 6, 3, 1, 1)
)
promPortDuplexEntry.setIndexNames(
    (0, "PROMINET-MIB", "promPortIndex"),
)
if mibBuilder.loadTexts:
    promPortDuplexEntry.setStatus("mandatory")


class _PromPortDuplexMode_Type(Integer32):
    """Custom type promPortDuplexMode based on Integer32"""
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


_PromPortDuplexMode_Type.__name__ = "Integer32"
_PromPortDuplexMode_Object = MibTableColumn
promPortDuplexMode = _PromPortDuplexMode_Object(
    (1, 3, 6, 1, 4, 1, 2167, 3, 6, 3, 1, 1, 31),
    _PromPortDuplexMode_Type()
)
promPortDuplexMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    promPortDuplexMode.setStatus("mandatory")
_PromPortSpeedMgt_ObjectIdentity = ObjectIdentity
promPortSpeedMgt = _PromPortSpeedMgt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2167, 3, 6, 4)
)
_PromPortSpeedTable_Object = MibTable
promPortSpeedTable = _PromPortSpeedTable_Object(
    (1, 3, 6, 1, 4, 1, 2167, 3, 6, 4, 1)
)
if mibBuilder.loadTexts:
    promPortSpeedTable.setStatus("mandatory")
_PromPortSpeedEntry_Object = MibTableRow
promPortSpeedEntry = _PromPortSpeedEntry_Object(
    (1, 3, 6, 1, 4, 1, 2167, 3, 6, 4, 1, 1)
)
promPortSpeedEntry.setIndexNames(
    (0, "PROMINET-MIB", "promPortIndex"),
)
if mibBuilder.loadTexts:
    promPortSpeedEntry.setStatus("mandatory")


class _PromPortSpeedMode_Type(Integer32):
    """Custom type promPortSpeedMode based on Integer32"""
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
        *(("one-gigabit-per-second", 5),
          ("one-hundred-fifty-five-megabits-per-second", 3),
          ("one-hundred-megabits-per-second", 2),
          ("six-hundred-twenty-two-megabits-per-second", 4),
          ("ten-megabits-per-second", 1))
    )


_PromPortSpeedMode_Type.__name__ = "Integer32"
_PromPortSpeedMode_Object = MibTableColumn
promPortSpeedMode = _PromPortSpeedMode_Object(
    (1, 3, 6, 1, 4, 1, 2167, 3, 6, 4, 1, 1, 41),
    _PromPortSpeedMode_Type()
)
promPortSpeedMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    promPortSpeedMode.setStatus("mandatory")
_PromPortAutoNegotiationMgt_ObjectIdentity = ObjectIdentity
promPortAutoNegotiationMgt = _PromPortAutoNegotiationMgt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2167, 3, 6, 5)
)
_PromPortAutoNegotiationTable_Object = MibTable
promPortAutoNegotiationTable = _PromPortAutoNegotiationTable_Object(
    (1, 3, 6, 1, 4, 1, 2167, 3, 6, 5, 1)
)
if mibBuilder.loadTexts:
    promPortAutoNegotiationTable.setStatus("mandatory")
_PromPortAutoNegotiationEntry_Object = MibTableRow
promPortAutoNegotiationEntry = _PromPortAutoNegotiationEntry_Object(
    (1, 3, 6, 1, 4, 1, 2167, 3, 6, 5, 1, 1)
)
promPortAutoNegotiationEntry.setIndexNames(
    (0, "PROMINET-MIB", "promPortIndex"),
)
if mibBuilder.loadTexts:
    promPortAutoNegotiationEntry.setStatus("mandatory")


class _PromPortAutoNegotiationMode_Type(Integer32):
    """Custom type promPortAutoNegotiationMode based on Integer32"""
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


_PromPortAutoNegotiationMode_Type.__name__ = "Integer32"
_PromPortAutoNegotiationMode_Object = MibTableColumn
promPortAutoNegotiationMode = _PromPortAutoNegotiationMode_Object(
    (1, 3, 6, 1, 4, 1, 2167, 3, 6, 5, 1, 1, 51),
    _PromPortAutoNegotiationMode_Type()
)
promPortAutoNegotiationMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    promPortAutoNegotiationMode.setStatus("mandatory")


class _PromPortAutoNegotiationSpeedAdvertisement_Type(Integer32):
    """Custom type promPortAutoNegotiationSpeedAdvertisement based on Integer32"""
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


_PromPortAutoNegotiationSpeedAdvertisement_Type.__name__ = "Integer32"
_PromPortAutoNegotiationSpeedAdvertisement_Object = MibTableColumn
promPortAutoNegotiationSpeedAdvertisement = _PromPortAutoNegotiationSpeedAdvertisement_Object(
    (1, 3, 6, 1, 4, 1, 2167, 3, 6, 5, 1, 1, 52),
    _PromPortAutoNegotiationSpeedAdvertisement_Type()
)
promPortAutoNegotiationSpeedAdvertisement.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    promPortAutoNegotiationSpeedAdvertisement.setStatus("mandatory")


class _PromPortAutoNegotiationDuplexAdvertisement_Type(Integer32):
    """Custom type promPortAutoNegotiationDuplexAdvertisement based on Integer32"""
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


_PromPortAutoNegotiationDuplexAdvertisement_Type.__name__ = "Integer32"
_PromPortAutoNegotiationDuplexAdvertisement_Object = MibTableColumn
promPortAutoNegotiationDuplexAdvertisement = _PromPortAutoNegotiationDuplexAdvertisement_Object(
    (1, 3, 6, 1, 4, 1, 2167, 3, 6, 5, 1, 1, 53),
    _PromPortAutoNegotiationDuplexAdvertisement_Type()
)
promPortAutoNegotiationDuplexAdvertisement.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    promPortAutoNegotiationDuplexAdvertisement.setStatus("mandatory")


class _PromPortAutoNegotiationFlowControlAdvertisement_Type(Integer32):
    """Custom type promPortAutoNegotiationFlowControlAdvertisement based on Integer32"""
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
        *(("disable", 2),
          ("enable", 1),
          ("enable-respond-only", 4),
          ("enable-send-only", 3))
    )


_PromPortAutoNegotiationFlowControlAdvertisement_Type.__name__ = "Integer32"
_PromPortAutoNegotiationFlowControlAdvertisement_Object = MibTableColumn
promPortAutoNegotiationFlowControlAdvertisement = _PromPortAutoNegotiationFlowControlAdvertisement_Object(
    (1, 3, 6, 1, 4, 1, 2167, 3, 6, 5, 1, 1, 54),
    _PromPortAutoNegotiationFlowControlAdvertisement_Type()
)
promPortAutoNegotiationFlowControlAdvertisement.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    promPortAutoNegotiationFlowControlAdvertisement.setStatus("mandatory")
_PromPortRateLimitMgt_ObjectIdentity = ObjectIdentity
promPortRateLimitMgt = _PromPortRateLimitMgt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2167, 3, 6, 6)
)
_PromPortRateLimitTable_Object = MibTable
promPortRateLimitTable = _PromPortRateLimitTable_Object(
    (1, 3, 6, 1, 4, 1, 2167, 3, 6, 6, 1)
)
if mibBuilder.loadTexts:
    promPortRateLimitTable.setStatus("mandatory")
_PromPortRateLimitEntry_Object = MibTableRow
promPortRateLimitEntry = _PromPortRateLimitEntry_Object(
    (1, 3, 6, 1, 4, 1, 2167, 3, 6, 6, 1, 1)
)
promPortRateLimitEntry.setIndexNames(
    (0, "PROMINET-MIB", "promPortIndex"),
)
if mibBuilder.loadTexts:
    promPortRateLimitEntry.setStatus("mandatory")


class _PromPortRateLimitMode_Type(Integer32):
    """Custom type promPortRateLimitMode based on Integer32"""
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


_PromPortRateLimitMode_Type.__name__ = "Integer32"
_PromPortRateLimitMode_Object = MibTableColumn
promPortRateLimitMode = _PromPortRateLimitMode_Object(
    (1, 3, 6, 1, 4, 1, 2167, 3, 6, 6, 1, 1, 61),
    _PromPortRateLimitMode_Type()
)
promPortRateLimitMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    promPortRateLimitMode.setStatus("mandatory")


class _PromPortRateLimitRate_Type(Integer32):
    """Custom type promPortRateLimitRate based on Integer32"""
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


_PromPortRateLimitRate_Type.__name__ = "Integer32"
_PromPortRateLimitRate_Object = MibTableColumn
promPortRateLimitRate = _PromPortRateLimitRate_Object(
    (1, 3, 6, 1, 4, 1, 2167, 3, 6, 6, 1, 1, 62),
    _PromPortRateLimitRate_Type()
)
promPortRateLimitRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    promPortRateLimitRate.setStatus("mandatory")


class _PromPortRateLimitBurstSize_Type(Integer32):
    """Custom type promPortRateLimitBurstSize based on Integer32"""
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
              12)
        )
    )
    namedValues = NamedValues(
        *(("rateLimit1", 1),
          ("rateLimit1024", 11),
          ("rateLimit128", 8),
          ("rateLimit16", 5),
          ("rateLimit2", 2),
          ("rateLimit2048", 12),
          ("rateLimit256", 9),
          ("rateLimit32", 6),
          ("rateLimit4", 3),
          ("rateLimit512", 10),
          ("rateLimit64", 7),
          ("rateLimit8", 4))
    )


_PromPortRateLimitBurstSize_Type.__name__ = "Integer32"
_PromPortRateLimitBurstSize_Object = MibTableColumn
promPortRateLimitBurstSize = _PromPortRateLimitBurstSize_Object(
    (1, 3, 6, 1, 4, 1, 2167, 3, 6, 6, 1, 1, 63),
    _PromPortRateLimitBurstSize_Type()
)
promPortRateLimitBurstSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    promPortRateLimitBurstSize.setStatus("mandatory")
_PromPortPacePriorityMgt_ObjectIdentity = ObjectIdentity
promPortPacePriorityMgt = _PromPortPacePriorityMgt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2167, 3, 6, 7)
)
_PromPortPacePriorityTable_Object = MibTable
promPortPacePriorityTable = _PromPortPacePriorityTable_Object(
    (1, 3, 6, 1, 4, 1, 2167, 3, 6, 7, 1)
)
if mibBuilder.loadTexts:
    promPortPacePriorityTable.setStatus("mandatory")
_PromPortPacePriorityEntry_Object = MibTableRow
promPortPacePriorityEntry = _PromPortPacePriorityEntry_Object(
    (1, 3, 6, 1, 4, 1, 2167, 3, 6, 7, 1, 1)
)
promPortPacePriorityEntry.setIndexNames(
    (0, "PROMINET-MIB", "promPortIndex"),
)
if mibBuilder.loadTexts:
    promPortPacePriorityEntry.setStatus("mandatory")


class _PromPortPacePriorityMode_Type(Integer32):
    """Custom type promPortPacePriorityMode based on Integer32"""
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


_PromPortPacePriorityMode_Type.__name__ = "Integer32"
_PromPortPacePriorityMode_Object = MibTableColumn
promPortPacePriorityMode = _PromPortPacePriorityMode_Object(
    (1, 3, 6, 1, 4, 1, 2167, 3, 6, 7, 1, 1, 71),
    _PromPortPacePriorityMode_Type()
)
promPortPacePriorityMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    promPortPacePriorityMode.setStatus("mandatory")
_PromPortCategoryMgt_ObjectIdentity = ObjectIdentity
promPortCategoryMgt = _PromPortCategoryMgt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2167, 3, 6, 8)
)
_PromPortCategoryTable_Object = MibTable
promPortCategoryTable = _PromPortCategoryTable_Object(
    (1, 3, 6, 1, 4, 1, 2167, 3, 6, 8, 1)
)
if mibBuilder.loadTexts:
    promPortCategoryTable.setStatus("mandatory")
_PromPortCategoryEntry_Object = MibTableRow
promPortCategoryEntry = _PromPortCategoryEntry_Object(
    (1, 3, 6, 1, 4, 1, 2167, 3, 6, 8, 1, 1)
)
promPortCategoryEntry.setIndexNames(
    (0, "PROMINET-MIB", "promPortIndex"),
)
if mibBuilder.loadTexts:
    promPortCategoryEntry.setStatus("mandatory")


class _PromPortCategoryMode_Type(Integer32):
    """Custom type promPortCategoryMode based on Integer32"""
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


_PromPortCategoryMode_Type.__name__ = "Integer32"
_PromPortCategoryMode_Object = MibTableColumn
promPortCategoryMode = _PromPortCategoryMode_Object(
    (1, 3, 6, 1, 4, 1, 2167, 3, 6, 8, 1, 1, 81),
    _PromPortCategoryMode_Type()
)
promPortCategoryMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    promPortCategoryMode.setStatus("mandatory")
_PromPortRemoteFaultMgt_ObjectIdentity = ObjectIdentity
promPortRemoteFaultMgt = _PromPortRemoteFaultMgt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2167, 3, 6, 9)
)
_PromPortRemoteFaultTable_Object = MibTable
promPortRemoteFaultTable = _PromPortRemoteFaultTable_Object(
    (1, 3, 6, 1, 4, 1, 2167, 3, 6, 9, 1)
)
if mibBuilder.loadTexts:
    promPortRemoteFaultTable.setStatus("mandatory")
_PromPortRemoteFaultEntry_Object = MibTableRow
promPortRemoteFaultEntry = _PromPortRemoteFaultEntry_Object(
    (1, 3, 6, 1, 4, 1, 2167, 3, 6, 9, 1, 1)
)
promPortRemoteFaultEntry.setIndexNames(
    (0, "PROMINET-MIB", "promPortIndex"),
)
if mibBuilder.loadTexts:
    promPortRemoteFaultEntry.setStatus("mandatory")


class _PromPortRemoteFaultDetect_Type(Integer32):
    """Custom type promPortRemoteFaultDetect based on Integer32"""
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


_PromPortRemoteFaultDetect_Type.__name__ = "Integer32"
_PromPortRemoteFaultDetect_Object = MibTableColumn
promPortRemoteFaultDetect = _PromPortRemoteFaultDetect_Object(
    (1, 3, 6, 1, 4, 1, 2167, 3, 6, 9, 1, 1, 91),
    _PromPortRemoteFaultDetect_Type()
)
promPortRemoteFaultDetect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    promPortRemoteFaultDetect.setStatus("mandatory")
_PromBufferMgt_ObjectIdentity = ObjectIdentity
promBufferMgt = _PromBufferMgt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2167, 3, 7)
)
_PromBufferTable_Object = MibTable
promBufferTable = _PromBufferTable_Object(
    (1, 3, 6, 1, 4, 1, 2167, 3, 7, 1)
)
if mibBuilder.loadTexts:
    promBufferTable.setStatus("mandatory")
_PromBufferEntry_Object = MibTableRow
promBufferEntry = _PromBufferEntry_Object(
    (1, 3, 6, 1, 4, 1, 2167, 3, 7, 1, 1)
)
promBufferEntry.setIndexNames(
    (0, "PROMINET-MIB", "promBufferIndex"),
)
if mibBuilder.loadTexts:
    promBufferEntry.setStatus("mandatory")
_PromBufferIndex_Type = ResourceId
_PromBufferIndex_Object = MibTableColumn
promBufferIndex = _PromBufferIndex_Object(
    (1, 3, 6, 1, 4, 1, 2167, 3, 7, 1, 1, 1),
    _PromBufferIndex_Type()
)
promBufferIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    promBufferIndex.setStatus("mandatory")
_PromBufferFabricPort_Type = ResourceId
_PromBufferFabricPort_Object = MibTableColumn
promBufferFabricPort = _PromBufferFabricPort_Object(
    (1, 3, 6, 1, 4, 1, 2167, 3, 7, 1, 1, 2),
    _PromBufferFabricPort_Type()
)
promBufferFabricPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    promBufferFabricPort.setStatus("mandatory")


class _PromBufferFabricPortDirection_Type(Integer32):
    """Custom type promBufferFabricPortDirection based on Integer32"""
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


_PromBufferFabricPortDirection_Type.__name__ = "Integer32"
_PromBufferFabricPortDirection_Object = MibTableColumn
promBufferFabricPortDirection = _PromBufferFabricPortDirection_Object(
    (1, 3, 6, 1, 4, 1, 2167, 3, 7, 1, 1, 3),
    _PromBufferFabricPortDirection_Type()
)
promBufferFabricPortDirection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    promBufferFabricPortDirection.setStatus("mandatory")
_PromBufferSwitchPort_Type = ResourceId
_PromBufferSwitchPort_Object = MibTableColumn
promBufferSwitchPort = _PromBufferSwitchPort_Object(
    (1, 3, 6, 1, 4, 1, 2167, 3, 7, 1, 1, 4),
    _PromBufferSwitchPort_Type()
)
promBufferSwitchPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    promBufferSwitchPort.setStatus("mandatory")
_PromBufferMemory_Type = Integer32
_PromBufferMemory_Object = MibTableColumn
promBufferMemory = _PromBufferMemory_Object(
    (1, 3, 6, 1, 4, 1, 2167, 3, 7, 1, 1, 5),
    _PromBufferMemory_Type()
)
promBufferMemory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    promBufferMemory.setStatus("mandatory")


class _PromBufferAgeTimer_Type(Integer32):
    """Custom type promBufferAgeTimer based on Integer32"""
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


_PromBufferAgeTimer_Type.__name__ = "Integer32"
_PromBufferAgeTimer_Object = MibTableColumn
promBufferAgeTimer = _PromBufferAgeTimer_Object(
    (1, 3, 6, 1, 4, 1, 2167, 3, 7, 1, 1, 6),
    _PromBufferAgeTimer_Type()
)
promBufferAgeTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    promBufferAgeTimer.setStatus("mandatory")


class _PromBufferPriorityServicing_Type(Integer32):
    """Custom type promBufferPriorityServicing based on Integer32"""
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


_PromBufferPriorityServicing_Type.__name__ = "Integer32"
_PromBufferPriorityServicing_Object = MibTableColumn
promBufferPriorityServicing = _PromBufferPriorityServicing_Object(
    (1, 3, 6, 1, 4, 1, 2167, 3, 7, 1, 1, 7),
    _PromBufferPriorityServicing_Type()
)
promBufferPriorityServicing.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    promBufferPriorityServicing.setStatus("mandatory")


class _PromBufferPriorityAllocation_Type(Integer32):
    """Custom type promBufferPriorityAllocation based on Integer32"""
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


_PromBufferPriorityAllocation_Type.__name__ = "Integer32"
_PromBufferPriorityAllocation_Object = MibTableColumn
promBufferPriorityAllocation = _PromBufferPriorityAllocation_Object(
    (1, 3, 6, 1, 4, 1, 2167, 3, 7, 1, 1, 8),
    _PromBufferPriorityAllocation_Type()
)
promBufferPriorityAllocation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    promBufferPriorityAllocation.setStatus("mandatory")


class _PromBufferPriorityThreshold_Type(Integer32):
    """Custom type promBufferPriorityThreshold based on Integer32"""
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


_PromBufferPriorityThreshold_Type.__name__ = "Integer32"
_PromBufferPriorityThreshold_Object = MibTableColumn
promBufferPriorityThreshold = _PromBufferPriorityThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2167, 3, 7, 1, 1, 9),
    _PromBufferPriorityThreshold_Type()
)
promBufferPriorityThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    promBufferPriorityThreshold.setStatus("mandatory")


class _PromBufferCongestion_Type(Integer32):
    """Custom type promBufferCongestion based on Integer32"""
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


_PromBufferCongestion_Type.__name__ = "Integer32"
_PromBufferCongestion_Object = MibTableColumn
promBufferCongestion = _PromBufferCongestion_Object(
    (1, 3, 6, 1, 4, 1, 2167, 3, 7, 1, 1, 10),
    _PromBufferCongestion_Type()
)
promBufferCongestion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    promBufferCongestion.setStatus("mandatory")
_PromBufferHighOverflowDrops_Type = Counter32
_PromBufferHighOverflowDrops_Object = MibTableColumn
promBufferHighOverflowDrops = _PromBufferHighOverflowDrops_Object(
    (1, 3, 6, 1, 4, 1, 2167, 3, 7, 1, 1, 11),
    _PromBufferHighOverflowDrops_Type()
)
promBufferHighOverflowDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    promBufferHighOverflowDrops.setStatus("mandatory")
_PromBufferLowOverflowDrops_Type = Counter32
_PromBufferLowOverflowDrops_Object = MibTableColumn
promBufferLowOverflowDrops = _PromBufferLowOverflowDrops_Object(
    (1, 3, 6, 1, 4, 1, 2167, 3, 7, 1, 1, 12),
    _PromBufferLowOverflowDrops_Type()
)
promBufferLowOverflowDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    promBufferLowOverflowDrops.setStatus("mandatory")
_PromBufferHighStaleDrops_Type = Counter32
_PromBufferHighStaleDrops_Object = MibTableColumn
promBufferHighStaleDrops = _PromBufferHighStaleDrops_Object(
    (1, 3, 6, 1, 4, 1, 2167, 3, 7, 1, 1, 13),
    _PromBufferHighStaleDrops_Type()
)
promBufferHighStaleDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    promBufferHighStaleDrops.setStatus("mandatory")
_PromBufferLowStaleDrops_Type = Counter32
_PromBufferLowStaleDrops_Object = MibTableColumn
promBufferLowStaleDrops = _PromBufferLowStaleDrops_Object(
    (1, 3, 6, 1, 4, 1, 2167, 3, 7, 1, 1, 14),
    _PromBufferLowStaleDrops_Type()
)
promBufferLowStaleDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    promBufferLowStaleDrops.setStatus("mandatory")
_PromBufferCongestionDrops_Type = Counter32
_PromBufferCongestionDrops_Object = MibTableColumn
promBufferCongestionDrops = _PromBufferCongestionDrops_Object(
    (1, 3, 6, 1, 4, 1, 2167, 3, 7, 1, 1, 16),
    _PromBufferCongestionDrops_Type()
)
promBufferCongestionDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    promBufferCongestionDrops.setStatus("mandatory")
_PromSwitching_ObjectIdentity = ObjectIdentity
promSwitching = _PromSwitching_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2167, 5)
)
_PromSwitchingLayerII_ObjectIdentity = ObjectIdentity
promSwitchingLayerII = _PromSwitchingLayerII_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2167, 5, 1)
)
_PromSwitchGen_ObjectIdentity = ObjectIdentity
promSwitchGen = _PromSwitchGen_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2167, 5, 1, 1)
)


class _PromSwitchSTPConfig_Type(Integer32):
    """Custom type promSwitchSTPConfig based on Integer32"""
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


_PromSwitchSTPConfig_Type.__name__ = "Integer32"
_PromSwitchSTPConfig_Object = MibScalar
promSwitchSTPConfig = _PromSwitchSTPConfig_Object(
    (1, 3, 6, 1, 4, 1, 2167, 5, 1, 1, 1),
    _PromSwitchSTPConfig_Type()
)
promSwitchSTPConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    promSwitchSTPConfig.setStatus("mandatory")


class _PromSwitchAgingTime_Type(Integer32):
    """Custom type promSwitchAgingTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 1000000),
    )


_PromSwitchAgingTime_Type.__name__ = "Integer32"
_PromSwitchAgingTime_Object = MibScalar
promSwitchAgingTime = _PromSwitchAgingTime_Object(
    (1, 3, 6, 1, 4, 1, 2167, 5, 1, 1, 2),
    _PromSwitchAgingTime_Type()
)
promSwitchAgingTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    promSwitchAgingTime.setStatus("mandatory")


class _PromSwitchSuperAgingTime_Type(Integer32):
    """Custom type promSwitchSuperAgingTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 30),
    )


_PromSwitchSuperAgingTime_Type.__name__ = "Integer32"
_PromSwitchSuperAgingTime_Object = MibScalar
promSwitchSuperAgingTime = _PromSwitchSuperAgingTime_Object(
    (1, 3, 6, 1, 4, 1, 2167, 5, 1, 1, 3),
    _PromSwitchSuperAgingTime_Type()
)
promSwitchSuperAgingTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    promSwitchSuperAgingTime.setStatus("mandatory")
_PromBridgeMgmt_ObjectIdentity = ObjectIdentity
promBridgeMgmt = _PromBridgeMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2167, 5, 1, 2)
)
_PromBridgeTable_Object = MibTable
promBridgeTable = _PromBridgeTable_Object(
    (1, 3, 6, 1, 4, 1, 2167, 5, 1, 2, 1)
)
if mibBuilder.loadTexts:
    promBridgeTable.setStatus("mandatory")
_PromBridgeEntry_Object = MibTableRow
promBridgeEntry = _PromBridgeEntry_Object(
    (1, 3, 6, 1, 4, 1, 2167, 5, 1, 2, 1, 1)
)
promBridgeEntry.setIndexNames(
    (0, "PROMINET-MIB", "promBridgeIndex"),
)
if mibBuilder.loadTexts:
    promBridgeEntry.setStatus("mandatory")
_PromBridgeIndex_Type = ResourceId
_PromBridgeIndex_Object = MibTableColumn
promBridgeIndex = _PromBridgeIndex_Object(
    (1, 3, 6, 1, 4, 1, 2167, 5, 1, 2, 1, 1, 1),
    _PromBridgeIndex_Type()
)
promBridgeIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    promBridgeIndex.setStatus("mandatory")


class _PromBridgeType_Type(Integer32):
    """Custom type promBridgeType based on Integer32"""
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


_PromBridgeType_Type.__name__ = "Integer32"
_PromBridgeType_Object = MibTableColumn
promBridgeType = _PromBridgeType_Object(
    (1, 3, 6, 1, 4, 1, 2167, 5, 1, 2, 1, 1, 2),
    _PromBridgeType_Type()
)
promBridgeType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    promBridgeType.setStatus("mandatory")


class _PromBridgeMode_Type(Integer32):
    """Custom type promBridgeMode based on Integer32"""
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


_PromBridgeMode_Type.__name__ = "Integer32"
_PromBridgeMode_Object = MibTableColumn
promBridgeMode = _PromBridgeMode_Object(
    (1, 3, 6, 1, 4, 1, 2167, 5, 1, 2, 1, 1, 3),
    _PromBridgeMode_Type()
)
promBridgeMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    promBridgeMode.setStatus("mandatory")


class _PromBridgeStatus_Type(Integer32):
    """Custom type promBridgeStatus based on Integer32"""
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


_PromBridgeStatus_Type.__name__ = "Integer32"
_PromBridgeStatus_Object = MibTableColumn
promBridgeStatus = _PromBridgeStatus_Object(
    (1, 3, 6, 1, 4, 1, 2167, 5, 1, 2, 1, 1, 4),
    _PromBridgeStatus_Type()
)
promBridgeStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    promBridgeStatus.setStatus("mandatory")


class _PromBridgeStpPriority_Type(Integer32):
    """Custom type promBridgeStpPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_PromBridgeStpPriority_Type.__name__ = "Integer32"
_PromBridgeStpPriority_Object = MibTableColumn
promBridgeStpPriority = _PromBridgeStpPriority_Object(
    (1, 3, 6, 1, 4, 1, 2167, 5, 1, 2, 1, 1, 5),
    _PromBridgeStpPriority_Type()
)
promBridgeStpPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    promBridgeStpPriority.setStatus("mandatory")
_PromBridgeStpTimeSinceTopologyChange_Type = TimeTicks
_PromBridgeStpTimeSinceTopologyChange_Object = MibTableColumn
promBridgeStpTimeSinceTopologyChange = _PromBridgeStpTimeSinceTopologyChange_Object(
    (1, 3, 6, 1, 4, 1, 2167, 5, 1, 2, 1, 1, 6),
    _PromBridgeStpTimeSinceTopologyChange_Type()
)
promBridgeStpTimeSinceTopologyChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    promBridgeStpTimeSinceTopologyChange.setStatus("mandatory")
_PromBridgeStpTopChanges_Type = Counter32
_PromBridgeStpTopChanges_Object = MibTableColumn
promBridgeStpTopChanges = _PromBridgeStpTopChanges_Object(
    (1, 3, 6, 1, 4, 1, 2167, 5, 1, 2, 1, 1, 7),
    _PromBridgeStpTopChanges_Type()
)
promBridgeStpTopChanges.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    promBridgeStpTopChanges.setStatus("mandatory")
_PromBridgeStpDesignatedRoot_Type = BridgeId
_PromBridgeStpDesignatedRoot_Object = MibTableColumn
promBridgeStpDesignatedRoot = _PromBridgeStpDesignatedRoot_Object(
    (1, 3, 6, 1, 4, 1, 2167, 5, 1, 2, 1, 1, 8),
    _PromBridgeStpDesignatedRoot_Type()
)
promBridgeStpDesignatedRoot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    promBridgeStpDesignatedRoot.setStatus("mandatory")
_PromBridgeStpRootCost_Type = Integer32
_PromBridgeStpRootCost_Object = MibTableColumn
promBridgeStpRootCost = _PromBridgeStpRootCost_Object(
    (1, 3, 6, 1, 4, 1, 2167, 5, 1, 2, 1, 1, 9),
    _PromBridgeStpRootCost_Type()
)
promBridgeStpRootCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    promBridgeStpRootCost.setStatus("mandatory")
_PromBridgeStpRootPort_Type = Integer32
_PromBridgeStpRootPort_Object = MibTableColumn
promBridgeStpRootPort = _PromBridgeStpRootPort_Object(
    (1, 3, 6, 1, 4, 1, 2167, 5, 1, 2, 1, 1, 10),
    _PromBridgeStpRootPort_Type()
)
promBridgeStpRootPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    promBridgeStpRootPort.setStatus("mandatory")
_PromBridgeStpMaxAge_Type = Timeout
_PromBridgeStpMaxAge_Object = MibTableColumn
promBridgeStpMaxAge = _PromBridgeStpMaxAge_Object(
    (1, 3, 6, 1, 4, 1, 2167, 5, 1, 2, 1, 1, 11),
    _PromBridgeStpMaxAge_Type()
)
promBridgeStpMaxAge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    promBridgeStpMaxAge.setStatus("mandatory")
_PromBridgeStpHelloTime_Type = Timeout
_PromBridgeStpHelloTime_Object = MibTableColumn
promBridgeStpHelloTime = _PromBridgeStpHelloTime_Object(
    (1, 3, 6, 1, 4, 1, 2167, 5, 1, 2, 1, 1, 12),
    _PromBridgeStpHelloTime_Type()
)
promBridgeStpHelloTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    promBridgeStpHelloTime.setStatus("mandatory")
_PromBridgeStpHoldTime_Type = Integer32
_PromBridgeStpHoldTime_Object = MibTableColumn
promBridgeStpHoldTime = _PromBridgeStpHoldTime_Object(
    (1, 3, 6, 1, 4, 1, 2167, 5, 1, 2, 1, 1, 13),
    _PromBridgeStpHoldTime_Type()
)
promBridgeStpHoldTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    promBridgeStpHoldTime.setStatus("mandatory")
_PromBridgeStpForwardDelay_Type = Timeout
_PromBridgeStpForwardDelay_Object = MibTableColumn
promBridgeStpForwardDelay = _PromBridgeStpForwardDelay_Object(
    (1, 3, 6, 1, 4, 1, 2167, 5, 1, 2, 1, 1, 14),
    _PromBridgeStpForwardDelay_Type()
)
promBridgeStpForwardDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    promBridgeStpForwardDelay.setStatus("mandatory")


class _PromBridgeStpBridgeMaxAge_Type(Timeout):
    """Custom type promBridgeStpBridgeMaxAge based on Timeout"""
    subtypeSpec = Timeout.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(600, 4000),
    )


_PromBridgeStpBridgeMaxAge_Type.__name__ = "Timeout"
_PromBridgeStpBridgeMaxAge_Object = MibTableColumn
promBridgeStpBridgeMaxAge = _PromBridgeStpBridgeMaxAge_Object(
    (1, 3, 6, 1, 4, 1, 2167, 5, 1, 2, 1, 1, 15),
    _PromBridgeStpBridgeMaxAge_Type()
)
promBridgeStpBridgeMaxAge.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    promBridgeStpBridgeMaxAge.setStatus("mandatory")


class _PromBridgeStpBridgeHelloTime_Type(Timeout):
    """Custom type promBridgeStpBridgeHelloTime based on Timeout"""
    subtypeSpec = Timeout.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(100, 1000),
    )


_PromBridgeStpBridgeHelloTime_Type.__name__ = "Timeout"
_PromBridgeStpBridgeHelloTime_Object = MibTableColumn
promBridgeStpBridgeHelloTime = _PromBridgeStpBridgeHelloTime_Object(
    (1, 3, 6, 1, 4, 1, 2167, 5, 1, 2, 1, 1, 16),
    _PromBridgeStpBridgeHelloTime_Type()
)
promBridgeStpBridgeHelloTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    promBridgeStpBridgeHelloTime.setStatus("mandatory")


class _PromBridgeStpBridgeForwardDelay_Type(Timeout):
    """Custom type promBridgeStpBridgeForwardDelay based on Timeout"""
    subtypeSpec = Timeout.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(400, 3000),
    )


_PromBridgeStpBridgeForwardDelay_Type.__name__ = "Timeout"
_PromBridgeStpBridgeForwardDelay_Object = MibTableColumn
promBridgeStpBridgeForwardDelay = _PromBridgeStpBridgeForwardDelay_Object(
    (1, 3, 6, 1, 4, 1, 2167, 5, 1, 2, 1, 1, 17),
    _PromBridgeStpBridgeForwardDelay_Type()
)
promBridgeStpBridgeForwardDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    promBridgeStpBridgeForwardDelay.setStatus("mandatory")
_PromBridgePortMgmt_ObjectIdentity = ObjectIdentity
promBridgePortMgmt = _PromBridgePortMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2167, 5, 1, 3)
)
_PromBridgePortTable_Object = MibTable
promBridgePortTable = _PromBridgePortTable_Object(
    (1, 3, 6, 1, 4, 1, 2167, 5, 1, 3, 1)
)
if mibBuilder.loadTexts:
    promBridgePortTable.setStatus("mandatory")
_PromBridgePortEntry_Object = MibTableRow
promBridgePortEntry = _PromBridgePortEntry_Object(
    (1, 3, 6, 1, 4, 1, 2167, 5, 1, 3, 1, 1)
)
promBridgePortEntry.setIndexNames(
    (0, "PROMINET-MIB", "promBridgePortIndex"),
)
if mibBuilder.loadTexts:
    promBridgePortEntry.setStatus("mandatory")
_PromBridgePortIndex_Type = ResourceId
_PromBridgePortIndex_Object = MibTableColumn
promBridgePortIndex = _PromBridgePortIndex_Object(
    (1, 3, 6, 1, 4, 1, 2167, 5, 1, 3, 1, 1, 1),
    _PromBridgePortIndex_Type()
)
promBridgePortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    promBridgePortIndex.setStatus("mandatory")


class _PromBridgePortPriority_Type(Integer32):
    """Custom type promBridgePortPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_PromBridgePortPriority_Type.__name__ = "Integer32"
_PromBridgePortPriority_Object = MibTableColumn
promBridgePortPriority = _PromBridgePortPriority_Object(
    (1, 3, 6, 1, 4, 1, 2167, 5, 1, 3, 1, 1, 2),
    _PromBridgePortPriority_Type()
)
promBridgePortPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    promBridgePortPriority.setStatus("mandatory")


class _PromBridgePortState_Type(Integer32):
    """Custom type promBridgePortState based on Integer32"""
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


_PromBridgePortState_Type.__name__ = "Integer32"
_PromBridgePortState_Object = MibTableColumn
promBridgePortState = _PromBridgePortState_Object(
    (1, 3, 6, 1, 4, 1, 2167, 5, 1, 3, 1, 1, 3),
    _PromBridgePortState_Type()
)
promBridgePortState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    promBridgePortState.setStatus("mandatory")


class _PromBridgePortEnable_Type(Integer32):
    """Custom type promBridgePortEnable based on Integer32"""
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


_PromBridgePortEnable_Type.__name__ = "Integer32"
_PromBridgePortEnable_Object = MibTableColumn
promBridgePortEnable = _PromBridgePortEnable_Object(
    (1, 3, 6, 1, 4, 1, 2167, 5, 1, 3, 1, 1, 4),
    _PromBridgePortEnable_Type()
)
promBridgePortEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    promBridgePortEnable.setStatus("mandatory")


class _PromBridgePortPathCost_Type(Integer32):
    """Custom type promBridgePortPathCost based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_PromBridgePortPathCost_Type.__name__ = "Integer32"
_PromBridgePortPathCost_Object = MibTableColumn
promBridgePortPathCost = _PromBridgePortPathCost_Object(
    (1, 3, 6, 1, 4, 1, 2167, 5, 1, 3, 1, 1, 5),
    _PromBridgePortPathCost_Type()
)
promBridgePortPathCost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    promBridgePortPathCost.setStatus("mandatory")
_PromBridgePortDesignatedRoot_Type = BridgeId
_PromBridgePortDesignatedRoot_Object = MibTableColumn
promBridgePortDesignatedRoot = _PromBridgePortDesignatedRoot_Object(
    (1, 3, 6, 1, 4, 1, 2167, 5, 1, 3, 1, 1, 6),
    _PromBridgePortDesignatedRoot_Type()
)
promBridgePortDesignatedRoot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    promBridgePortDesignatedRoot.setStatus("mandatory")
_PromBridgePortDesignatedCost_Type = Integer32
_PromBridgePortDesignatedCost_Object = MibTableColumn
promBridgePortDesignatedCost = _PromBridgePortDesignatedCost_Object(
    (1, 3, 6, 1, 4, 1, 2167, 5, 1, 3, 1, 1, 7),
    _PromBridgePortDesignatedCost_Type()
)
promBridgePortDesignatedCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    promBridgePortDesignatedCost.setStatus("mandatory")
_PromBridgePortDesignatedBridge_Type = BridgeId
_PromBridgePortDesignatedBridge_Object = MibTableColumn
promBridgePortDesignatedBridge = _PromBridgePortDesignatedBridge_Object(
    (1, 3, 6, 1, 4, 1, 2167, 5, 1, 3, 1, 1, 8),
    _PromBridgePortDesignatedBridge_Type()
)
promBridgePortDesignatedBridge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    promBridgePortDesignatedBridge.setStatus("mandatory")


class _PromBridgePortDesignatedPort_Type(OctetString):
    """Custom type promBridgePortDesignatedPort based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_PromBridgePortDesignatedPort_Type.__name__ = "OctetString"
_PromBridgePortDesignatedPort_Object = MibTableColumn
promBridgePortDesignatedPort = _PromBridgePortDesignatedPort_Object(
    (1, 3, 6, 1, 4, 1, 2167, 5, 1, 3, 1, 1, 9),
    _PromBridgePortDesignatedPort_Type()
)
promBridgePortDesignatedPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    promBridgePortDesignatedPort.setStatus("mandatory")
_PromBridgePortForwardTransitions_Type = Counter32
_PromBridgePortForwardTransitions_Object = MibTableColumn
promBridgePortForwardTransitions = _PromBridgePortForwardTransitions_Object(
    (1, 3, 6, 1, 4, 1, 2167, 5, 1, 3, 1, 1, 10),
    _PromBridgePortForwardTransitions_Type()
)
promBridgePortForwardTransitions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    promBridgePortForwardTransitions.setStatus("mandatory")


class _PromBridgePortFastStart_Type(Integer32):
    """Custom type promBridgePortFastStart based on Integer32"""
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


_PromBridgePortFastStart_Type.__name__ = "Integer32"
_PromBridgePortFastStart_Object = MibTableColumn
promBridgePortFastStart = _PromBridgePortFastStart_Object(
    (1, 3, 6, 1, 4, 1, 2167, 5, 1, 3, 1, 1, 11),
    _PromBridgePortFastStart_Type()
)
promBridgePortFastStart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    promBridgePortFastStart.setStatus("deprecated")


class _PromBridgePortSetDefault_Type(Integer32):
    """Custom type promBridgePortSetDefault based on Integer32"""
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


_PromBridgePortSetDefault_Type.__name__ = "Integer32"
_PromBridgePortSetDefault_Object = MibTableColumn
promBridgePortSetDefault = _PromBridgePortSetDefault_Object(
    (1, 3, 6, 1, 4, 1, 2167, 5, 1, 3, 1, 1, 12),
    _PromBridgePortSetDefault_Type()
)
promBridgePortSetDefault.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    promBridgePortSetDefault.setStatus("mandatory")


class _PromBridgePortEnableChangeDetection_Type(Integer32):
    """Custom type promBridgePortEnableChangeDetection based on Integer32"""
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


_PromBridgePortEnableChangeDetection_Type.__name__ = "Integer32"
_PromBridgePortEnableChangeDetection_Object = MibTableColumn
promBridgePortEnableChangeDetection = _PromBridgePortEnableChangeDetection_Object(
    (1, 3, 6, 1, 4, 1, 2167, 5, 1, 3, 1, 1, 13),
    _PromBridgePortEnableChangeDetection_Type()
)
promBridgePortEnableChangeDetection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    promBridgePortEnableChangeDetection.setStatus("mandatory")
_PromL2AddrMgmt_ObjectIdentity = ObjectIdentity
promL2AddrMgmt = _PromL2AddrMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2167, 5, 1, 4)
)
_PromL2AddrDatabaseMgt_ObjectIdentity = ObjectIdentity
promL2AddrDatabaseMgt = _PromL2AddrDatabaseMgt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2167, 5, 1, 4, 1)
)
_PromL2AddressTable_Object = MibTable
promL2AddressTable = _PromL2AddressTable_Object(
    (1, 3, 6, 1, 4, 1, 2167, 5, 1, 4, 1, 1)
)
if mibBuilder.loadTexts:
    promL2AddressTable.setStatus("mandatory")
_PromL2AddressEntry_Object = MibTableRow
promL2AddressEntry = _PromL2AddressEntry_Object(
    (1, 3, 6, 1, 4, 1, 2167, 5, 1, 4, 1, 1, 1)
)
promL2AddressEntry.setIndexNames(
    (0, "PROMINET-MIB", "promL2AddressIndex"),
)
if mibBuilder.loadTexts:
    promL2AddressEntry.setStatus("mandatory")
_PromL2AddressIndex_Type = Integer32
_PromL2AddressIndex_Object = MibTableColumn
promL2AddressIndex = _PromL2AddressIndex_Object(
    (1, 3, 6, 1, 4, 1, 2167, 5, 1, 4, 1, 1, 1, 1),
    _PromL2AddressIndex_Type()
)
promL2AddressIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    promL2AddressIndex.setStatus("mandatory")
_PromL2AddressTableIndex_Type = Integer32
_PromL2AddressTableIndex_Object = MibTableColumn
promL2AddressTableIndex = _PromL2AddressTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 2167, 5, 1, 4, 1, 1, 1, 2),
    _PromL2AddressTableIndex_Type()
)
promL2AddressTableIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    promL2AddressTableIndex.setStatus("mandatory")
_PromL2AddressMacAddress_Type = MacAddress
_PromL2AddressMacAddress_Object = MibTableColumn
promL2AddressMacAddress = _PromL2AddressMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 2167, 5, 1, 4, 1, 1, 1, 3),
    _PromL2AddressMacAddress_Type()
)
promL2AddressMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    promL2AddressMacAddress.setStatus("mandatory")
_PromL2AddressPortBinding_Type = ResourceId
_PromL2AddressPortBinding_Object = MibTableColumn
promL2AddressPortBinding = _PromL2AddressPortBinding_Object(
    (1, 3, 6, 1, 4, 1, 2167, 5, 1, 4, 1, 1, 1, 4),
    _PromL2AddressPortBinding_Type()
)
promL2AddressPortBinding.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    promL2AddressPortBinding.setStatus("mandatory")


class _PromL2AddressBindingValid_Type(Integer32):
    """Custom type promL2AddressBindingValid based on Integer32"""
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


_PromL2AddressBindingValid_Type.__name__ = "Integer32"
_PromL2AddressBindingValid_Object = MibTableColumn
promL2AddressBindingValid = _PromL2AddressBindingValid_Object(
    (1, 3, 6, 1, 4, 1, 2167, 5, 1, 4, 1, 1, 1, 5),
    _PromL2AddressBindingValid_Type()
)
promL2AddressBindingValid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    promL2AddressBindingValid.setStatus("mandatory")
_PromL2AddressVlanID_Type = Integer32
_PromL2AddressVlanID_Object = MibTableColumn
promL2AddressVlanID = _PromL2AddressVlanID_Object(
    (1, 3, 6, 1, 4, 1, 2167, 5, 1, 4, 1, 1, 1, 6),
    _PromL2AddressVlanID_Type()
)
promL2AddressVlanID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    promL2AddressVlanID.setStatus("mandatory")


class _PromL2AddressPriority_Type(Integer32):
    """Custom type promL2AddressPriority based on Integer32"""
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


_PromL2AddressPriority_Type.__name__ = "Integer32"
_PromL2AddressPriority_Object = MibTableColumn
promL2AddressPriority = _PromL2AddressPriority_Object(
    (1, 3, 6, 1, 4, 1, 2167, 5, 1, 4, 1, 1, 1, 7),
    _PromL2AddressPriority_Type()
)
promL2AddressPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    promL2AddressPriority.setStatus("mandatory")


class _PromL2AddressForward_Type(Integer32):
    """Custom type promL2AddressForward based on Integer32"""
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


_PromL2AddressForward_Type.__name__ = "Integer32"
_PromL2AddressForward_Object = MibTableColumn
promL2AddressForward = _PromL2AddressForward_Object(
    (1, 3, 6, 1, 4, 1, 2167, 5, 1, 4, 1, 1, 1, 8),
    _PromL2AddressForward_Type()
)
promL2AddressForward.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    promL2AddressForward.setStatus("mandatory")


class _PromL2AddressCopy_Type(Integer32):
    """Custom type promL2AddressCopy based on Integer32"""
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


_PromL2AddressCopy_Type.__name__ = "Integer32"
_PromL2AddressCopy_Object = MibTableColumn
promL2AddressCopy = _PromL2AddressCopy_Object(
    (1, 3, 6, 1, 4, 1, 2167, 5, 1, 4, 1, 1, 1, 9),
    _PromL2AddressCopy_Type()
)
promL2AddressCopy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    promL2AddressCopy.setStatus("mandatory")


class _PromL2AddressPersistence_Type(Integer32):
    """Custom type promL2AddressPersistence based on Integer32"""
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


_PromL2AddressPersistence_Type.__name__ = "Integer32"
_PromL2AddressPersistence_Object = MibTableColumn
promL2AddressPersistence = _PromL2AddressPersistence_Object(
    (1, 3, 6, 1, 4, 1, 2167, 5, 1, 4, 1, 1, 1, 10),
    _PromL2AddressPersistence_Type()
)
promL2AddressPersistence.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    promL2AddressPersistence.setStatus("mandatory")


class _PromL2AddressStatus_Type(Integer32):
    """Custom type promL2AddressStatus based on Integer32"""
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


_PromL2AddressStatus_Type.__name__ = "Integer32"
_PromL2AddressStatus_Object = MibTableColumn
promL2AddressStatus = _PromL2AddressStatus_Object(
    (1, 3, 6, 1, 4, 1, 2167, 5, 1, 4, 1, 1, 1, 11),
    _PromL2AddressStatus_Type()
)
promL2AddressStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    promL2AddressStatus.setStatus("mandatory")
_PromL2AddrSummaryMgt_ObjectIdentity = ObjectIdentity
promL2AddrSummaryMgt = _PromL2AddrSummaryMgt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2167, 5, 1, 4, 2)
)
_PromL2AddrSummaryTable_Object = MibTable
promL2AddrSummaryTable = _PromL2AddrSummaryTable_Object(
    (1, 3, 6, 1, 4, 1, 2167, 5, 1, 4, 2, 1)
)
if mibBuilder.loadTexts:
    promL2AddrSummaryTable.setStatus("mandatory")
_PromL2AddrSummaryEntry_Object = MibTableRow
promL2AddrSummaryEntry = _PromL2AddrSummaryEntry_Object(
    (1, 3, 6, 1, 4, 1, 2167, 5, 1, 4, 2, 1, 1)
)
promL2AddrSummaryEntry.setIndexNames(
    (0, "PROMINET-MIB", "promL2AddressIndex"),
)
if mibBuilder.loadTexts:
    promL2AddrSummaryEntry.setStatus("mandatory")


class _PromL2AddrSummary_Type(OctetString):
    """Custom type promL2AddrSummary based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(20, 4096),
    )


_PromL2AddrSummary_Type.__name__ = "OctetString"
_PromL2AddrSummary_Object = MibTableColumn
promL2AddrSummary = _PromL2AddrSummary_Object(
    (1, 3, 6, 1, 4, 1, 2167, 5, 1, 4, 2, 1, 1, 1),
    _PromL2AddrSummary_Type()
)
promL2AddrSummary.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    promL2AddrSummary.setStatus("mandatory")
_PromL2AddrControlMgt_ObjectIdentity = ObjectIdentity
promL2AddrControlMgt = _PromL2AddrControlMgt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2167, 5, 1, 4, 3)
)
_PromL2AddressControlTable_Object = MibTable
promL2AddressControlTable = _PromL2AddressControlTable_Object(
    (1, 3, 6, 1, 4, 1, 2167, 5, 1, 4, 3, 1)
)
if mibBuilder.loadTexts:
    promL2AddressControlTable.setStatus("mandatory")
_PromL2AddressControlEntry_Object = MibTableRow
promL2AddressControlEntry = _PromL2AddressControlEntry_Object(
    (1, 3, 6, 1, 4, 1, 2167, 5, 1, 4, 3, 1, 1)
)
promL2AddressControlEntry.setIndexNames(
    (0, "PROMINET-MIB", "promAgentMgrIndex"),
)
if mibBuilder.loadTexts:
    promL2AddressControlEntry.setStatus("mandatory")
_PromL2AddressControlIndex_Type = Integer32
_PromL2AddressControlIndex_Object = MibTableColumn
promL2AddressControlIndex = _PromL2AddressControlIndex_Object(
    (1, 3, 6, 1, 4, 1, 2167, 5, 1, 4, 3, 1, 1, 1),
    _PromL2AddressControlIndex_Type()
)
promL2AddressControlIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    promL2AddressControlIndex.setStatus("mandatory")
_PromL2AddressControlMacAddress_Type = MacAddress
_PromL2AddressControlMacAddress_Object = MibTableColumn
promL2AddressControlMacAddress = _PromL2AddressControlMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 2167, 5, 1, 4, 3, 1, 1, 2),
    _PromL2AddressControlMacAddress_Type()
)
promL2AddressControlMacAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    promL2AddressControlMacAddress.setStatus("mandatory")
_PromL2AddressControlPortBinding_Type = ResourceId
_PromL2AddressControlPortBinding_Object = MibTableColumn
promL2AddressControlPortBinding = _PromL2AddressControlPortBinding_Object(
    (1, 3, 6, 1, 4, 1, 2167, 5, 1, 4, 3, 1, 1, 3),
    _PromL2AddressControlPortBinding_Type()
)
promL2AddressControlPortBinding.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    promL2AddressControlPortBinding.setStatus("mandatory")
_PromL2AddressControlVlanID_Type = Integer32
_PromL2AddressControlVlanID_Object = MibTableColumn
promL2AddressControlVlanID = _PromL2AddressControlVlanID_Object(
    (1, 3, 6, 1, 4, 1, 2167, 5, 1, 4, 3, 1, 1, 4),
    _PromL2AddressControlVlanID_Type()
)
promL2AddressControlVlanID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    promL2AddressControlVlanID.setStatus("mandatory")


class _PromL2AddressControlPriority_Type(Integer32):
    """Custom type promL2AddressControlPriority based on Integer32"""
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


_PromL2AddressControlPriority_Type.__name__ = "Integer32"
_PromL2AddressControlPriority_Object = MibTableColumn
promL2AddressControlPriority = _PromL2AddressControlPriority_Object(
    (1, 3, 6, 1, 4, 1, 2167, 5, 1, 4, 3, 1, 1, 5),
    _PromL2AddressControlPriority_Type()
)
promL2AddressControlPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    promL2AddressControlPriority.setStatus("mandatory")


class _PromL2AddressControlPersistence_Type(Integer32):
    """Custom type promL2AddressControlPersistence based on Integer32"""
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


_PromL2AddressControlPersistence_Type.__name__ = "Integer32"
_PromL2AddressControlPersistence_Object = MibTableColumn
promL2AddressControlPersistence = _PromL2AddressControlPersistence_Object(
    (1, 3, 6, 1, 4, 1, 2167, 5, 1, 4, 3, 1, 1, 6),
    _PromL2AddressControlPersistence_Type()
)
promL2AddressControlPersistence.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    promL2AddressControlPersistence.setStatus("mandatory")


class _PromL2AddressControlStatus_Type(Integer32):
    """Custom type promL2AddressControlStatus based on Integer32"""
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


_PromL2AddressControlStatus_Type.__name__ = "Integer32"
_PromL2AddressControlStatus_Object = MibTableColumn
promL2AddressControlStatus = _PromL2AddressControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 2167, 5, 1, 4, 3, 1, 1, 7),
    _PromL2AddressControlStatus_Type()
)
promL2AddressControlStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    promL2AddressControlStatus.setStatus("mandatory")
_PromL2AddrChangeMgt_ObjectIdentity = ObjectIdentity
promL2AddrChangeMgt = _PromL2AddrChangeMgt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2167, 5, 1, 4, 4)
)
_PromL2AddressChangeLast_Type = Integer32
_PromL2AddressChangeLast_Object = MibScalar
promL2AddressChangeLast = _PromL2AddressChangeLast_Object(
    (1, 3, 6, 1, 4, 1, 2167, 5, 1, 4, 4, 1),
    _PromL2AddressChangeLast_Type()
)
promL2AddressChangeLast.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    promL2AddressChangeLast.setStatus("mandatory")
_PromL2AddressChangeWraps_Type = Counter32
_PromL2AddressChangeWraps_Object = MibScalar
promL2AddressChangeWraps = _PromL2AddressChangeWraps_Object(
    (1, 3, 6, 1, 4, 1, 2167, 5, 1, 4, 4, 2),
    _PromL2AddressChangeWraps_Type()
)
promL2AddressChangeWraps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    promL2AddressChangeWraps.setStatus("mandatory")


class _PromL2AddressChangeMaxEntries_Type(Integer32):
    """Custom type promL2AddressChangeMaxEntries based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1024, 4096),
    )


_PromL2AddressChangeMaxEntries_Type.__name__ = "Integer32"
_PromL2AddressChangeMaxEntries_Object = MibScalar
promL2AddressChangeMaxEntries = _PromL2AddressChangeMaxEntries_Object(
    (1, 3, 6, 1, 4, 1, 2167, 5, 1, 4, 4, 3),
    _PromL2AddressChangeMaxEntries_Type()
)
promL2AddressChangeMaxEntries.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    promL2AddressChangeMaxEntries.setStatus("mandatory")
_PromL2AddressChangeTable_Object = MibTable
promL2AddressChangeTable = _PromL2AddressChangeTable_Object(
    (1, 3, 6, 1, 4, 1, 2167, 5, 1, 4, 4, 4)
)
if mibBuilder.loadTexts:
    promL2AddressChangeTable.setStatus("mandatory")
_PromL2AddressChangeEntry_Object = MibTableRow
promL2AddressChangeEntry = _PromL2AddressChangeEntry_Object(
    (1, 3, 6, 1, 4, 1, 2167, 5, 1, 4, 4, 4, 1)
)
promL2AddressChangeEntry.setIndexNames(
    (0, "PROMINET-MIB", "promL2AddressChangeWrapCount"),
    (0, "PROMINET-MIB", "promL2AddressChangeIndex"),
)
if mibBuilder.loadTexts:
    promL2AddressChangeEntry.setStatus("mandatory")
_PromL2AddressChangeWrapCount_Type = Integer32
_PromL2AddressChangeWrapCount_Object = MibTableColumn
promL2AddressChangeWrapCount = _PromL2AddressChangeWrapCount_Object(
    (1, 3, 6, 1, 4, 1, 2167, 5, 1, 4, 4, 4, 1, 1),
    _PromL2AddressChangeWrapCount_Type()
)
promL2AddressChangeWrapCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    promL2AddressChangeWrapCount.setStatus("mandatory")
_PromL2AddressChangeIndex_Type = Integer32
_PromL2AddressChangeIndex_Object = MibTableColumn
promL2AddressChangeIndex = _PromL2AddressChangeIndex_Object(
    (1, 3, 6, 1, 4, 1, 2167, 5, 1, 4, 4, 4, 1, 2),
    _PromL2AddressChangeIndex_Type()
)
promL2AddressChangeIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    promL2AddressChangeIndex.setStatus("mandatory")
_PromL2AddressChangeIndexChanged_Type = Integer32
_PromL2AddressChangeIndexChanged_Object = MibTableColumn
promL2AddressChangeIndexChanged = _PromL2AddressChangeIndexChanged_Object(
    (1, 3, 6, 1, 4, 1, 2167, 5, 1, 4, 4, 4, 1, 3),
    _PromL2AddressChangeIndexChanged_Type()
)
promL2AddressChangeIndexChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    promL2AddressChangeIndexChanged.setStatus("mandatory")


class _PromL2AddressChangeSummary_Type(OctetString):
    """Custom type promL2AddressChangeSummary based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(20, 20),
    )


_PromL2AddressChangeSummary_Type.__name__ = "OctetString"
_PromL2AddressChangeSummary_Object = MibTableColumn
promL2AddressChangeSummary = _PromL2AddressChangeSummary_Object(
    (1, 3, 6, 1, 4, 1, 2167, 5, 1, 4, 4, 4, 1, 4),
    _PromL2AddressChangeSummary_Type()
)
promL2AddressChangeSummary.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    promL2AddressChangeSummary.setStatus("mandatory")
_PromSwitchPortMgt_ObjectIdentity = ObjectIdentity
promSwitchPortMgt = _PromSwitchPortMgt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2167, 5, 2)
)
_PromSwitchPortTable_Object = MibTable
promSwitchPortTable = _PromSwitchPortTable_Object(
    (1, 3, 6, 1, 4, 1, 2167, 5, 2, 1)
)
if mibBuilder.loadTexts:
    promSwitchPortTable.setStatus("mandatory")
_PromSwitchPortEntry_Object = MibTableRow
promSwitchPortEntry = _PromSwitchPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 2167, 5, 2, 1, 1)
)
promSwitchPortEntry.setIndexNames(
    (0, "PROMINET-MIB", "promSwitchPortIndex"),
)
if mibBuilder.loadTexts:
    promSwitchPortEntry.setStatus("mandatory")
_PromSwitchPortIndex_Type = ResourceId
_PromSwitchPortIndex_Object = MibTableColumn
promSwitchPortIndex = _PromSwitchPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 2167, 5, 2, 1, 1, 1),
    _PromSwitchPortIndex_Type()
)
promSwitchPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    promSwitchPortIndex.setStatus("mandatory")


class _PromSwitchPortSTAPMode_Type(Integer32):
    """Custom type promSwitchPortSTAPMode based on Integer32"""
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


_PromSwitchPortSTAPMode_Type.__name__ = "Integer32"
_PromSwitchPortSTAPMode_Object = MibTableColumn
promSwitchPortSTAPMode = _PromSwitchPortSTAPMode_Object(
    (1, 3, 6, 1, 4, 1, 2167, 5, 2, 1, 1, 2),
    _PromSwitchPortSTAPMode_Type()
)
promSwitchPortSTAPMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    promSwitchPortSTAPMode.setStatus("mandatory")


class _PromSwitchPortConvertToStatic_Type(Integer32):
    """Custom type promSwitchPortConvertToStatic based on Integer32"""
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


_PromSwitchPortConvertToStatic_Type.__name__ = "Integer32"
_PromSwitchPortConvertToStatic_Object = MibTableColumn
promSwitchPortConvertToStatic = _PromSwitchPortConvertToStatic_Object(
    (1, 3, 6, 1, 4, 1, 2167, 5, 2, 1, 1, 3),
    _PromSwitchPortConvertToStatic_Type()
)
promSwitchPortConvertToStatic.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    promSwitchPortConvertToStatic.setStatus("mandatory")


class _PromSwitchPortLearningMode_Type(Integer32):
    """Custom type promSwitchPortLearningMode based on Integer32"""
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


_PromSwitchPortLearningMode_Type.__name__ = "Integer32"
_PromSwitchPortLearningMode_Object = MibTableColumn
promSwitchPortLearningMode = _PromSwitchPortLearningMode_Object(
    (1, 3, 6, 1, 4, 1, 2167, 5, 2, 1, 1, 4),
    _PromSwitchPortLearningMode_Type()
)
promSwitchPortLearningMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    promSwitchPortLearningMode.setStatus("mandatory")
_PromSwitchPortHuntGroup_Type = Integer32
_PromSwitchPortHuntGroup_Object = MibTableColumn
promSwitchPortHuntGroup = _PromSwitchPortHuntGroup_Object(
    (1, 3, 6, 1, 4, 1, 2167, 5, 2, 1, 1, 5),
    _PromSwitchPortHuntGroup_Type()
)
promSwitchPortHuntGroup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    promSwitchPortHuntGroup.setStatus("mandatory")
_PromSwitchPortPhysicalPort_Type = ResourceId
_PromSwitchPortPhysicalPort_Object = MibTableColumn
promSwitchPortPhysicalPort = _PromSwitchPortPhysicalPort_Object(
    (1, 3, 6, 1, 4, 1, 2167, 5, 2, 1, 1, 6),
    _PromSwitchPortPhysicalPort_Type()
)
promSwitchPortPhysicalPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    promSwitchPortPhysicalPort.setStatus("mandatory")


class _PromSwitchPortKnownMode_Type(Integer32):
    """Custom type promSwitchPortKnownMode based on Integer32"""
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


_PromSwitchPortKnownMode_Type.__name__ = "Integer32"
_PromSwitchPortKnownMode_Object = MibTableColumn
promSwitchPortKnownMode = _PromSwitchPortKnownMode_Object(
    (1, 3, 6, 1, 4, 1, 2167, 5, 2, 1, 1, 7),
    _PromSwitchPortKnownMode_Type()
)
promSwitchPortKnownMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    promSwitchPortKnownMode.setStatus("mandatory")


class _PromSwitchPortMappingMethod_Type(Integer32):
    """Custom type promSwitchPortMappingMethod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("port-based", 1)
    )


_PromSwitchPortMappingMethod_Type.__name__ = "Integer32"
_PromSwitchPortMappingMethod_Object = MibTableColumn
promSwitchPortMappingMethod = _PromSwitchPortMappingMethod_Object(
    (1, 3, 6, 1, 4, 1, 2167, 5, 2, 1, 1, 8),
    _PromSwitchPortMappingMethod_Type()
)
promSwitchPortMappingMethod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    promSwitchPortMappingMethod.setStatus("mandatory")


class _PromSwitchPortTrunkingMode_Type(Integer32):
    """Custom type promSwitchPortTrunkingMode based on Integer32"""
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


_PromSwitchPortTrunkingMode_Type.__name__ = "Integer32"
_PromSwitchPortTrunkingMode_Object = MibTableColumn
promSwitchPortTrunkingMode = _PromSwitchPortTrunkingMode_Object(
    (1, 3, 6, 1, 4, 1, 2167, 5, 2, 1, 1, 9),
    _PromSwitchPortTrunkingMode_Type()
)
promSwitchPortTrunkingMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    promSwitchPortTrunkingMode.setStatus("mandatory")


class _PromSwitchPortVlanBindingMethod_Type(Integer32):
    """Custom type promSwitchPortVlanBindingMethod based on Integer32"""
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


_PromSwitchPortVlanBindingMethod_Type.__name__ = "Integer32"
_PromSwitchPortVlanBindingMethod_Object = MibTableColumn
promSwitchPortVlanBindingMethod = _PromSwitchPortVlanBindingMethod_Object(
    (1, 3, 6, 1, 4, 1, 2167, 5, 2, 1, 1, 10),
    _PromSwitchPortVlanBindingMethod_Type()
)
promSwitchPortVlanBindingMethod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    promSwitchPortVlanBindingMethod.setStatus("mandatory")


class _PromSwitchPortIgnoreTag_Type(Integer32):
    """Custom type promSwitchPortIgnoreTag based on Integer32"""
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


_PromSwitchPortIgnoreTag_Type.__name__ = "Integer32"
_PromSwitchPortIgnoreTag_Object = MibTableColumn
promSwitchPortIgnoreTag = _PromSwitchPortIgnoreTag_Object(
    (1, 3, 6, 1, 4, 1, 2167, 5, 2, 1, 1, 11),
    _PromSwitchPortIgnoreTag_Type()
)
promSwitchPortIgnoreTag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    promSwitchPortIgnoreTag.setStatus("mandatory")
_PromSwitchPortVlanID_Type = Integer32
_PromSwitchPortVlanID_Object = MibTableColumn
promSwitchPortVlanID = _PromSwitchPortVlanID_Object(
    (1, 3, 6, 1, 4, 1, 2167, 5, 2, 1, 1, 12),
    _PromSwitchPortVlanID_Type()
)
promSwitchPortVlanID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    promSwitchPortVlanID.setStatus("mandatory")


class _PromSwitchPort3ComMappingTableIndex_Type(Integer32):
    """Custom type promSwitchPort3ComMappingTableIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_PromSwitchPort3ComMappingTableIndex_Type.__name__ = "Integer32"
_PromSwitchPort3ComMappingTableIndex_Object = MibTableColumn
promSwitchPort3ComMappingTableIndex = _PromSwitchPort3ComMappingTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 2167, 5, 2, 1, 1, 13),
    _PromSwitchPort3ComMappingTableIndex_Type()
)
promSwitchPort3ComMappingTableIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    promSwitchPort3ComMappingTableIndex.setStatus("mandatory")


class _PromSwitchPortAutoVlanCreation_Type(Integer32):
    """Custom type promSwitchPortAutoVlanCreation based on Integer32"""
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


_PromSwitchPortAutoVlanCreation_Type.__name__ = "Integer32"
_PromSwitchPortAutoVlanCreation_Object = MibTableColumn
promSwitchPortAutoVlanCreation = _PromSwitchPortAutoVlanCreation_Object(
    (1, 3, 6, 1, 4, 1, 2167, 5, 2, 1, 1, 14),
    _PromSwitchPortAutoVlanCreation_Type()
)
promSwitchPortAutoVlanCreation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    promSwitchPortAutoVlanCreation.setStatus("mandatory")


class _PromSwitchPortMirrorMode_Type(Integer32):
    """Custom type promSwitchPortMirrorMode based on Integer32"""
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


_PromSwitchPortMirrorMode_Type.__name__ = "Integer32"
_PromSwitchPortMirrorMode_Object = MibTableColumn
promSwitchPortMirrorMode = _PromSwitchPortMirrorMode_Object(
    (1, 3, 6, 1, 4, 1, 2167, 5, 2, 1, 1, 15),
    _PromSwitchPortMirrorMode_Type()
)
promSwitchPortMirrorMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    promSwitchPortMirrorMode.setStatus("mandatory")
_PromSwitchPortIfIndex_Type = Integer32
_PromSwitchPortIfIndex_Object = MibTableColumn
promSwitchPortIfIndex = _PromSwitchPortIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2167, 5, 2, 1, 1, 16),
    _PromSwitchPortIfIndex_Type()
)
promSwitchPortIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    promSwitchPortIfIndex.setStatus("mandatory")


class _PromSwitchPortFastStart_Type(Integer32):
    """Custom type promSwitchPortFastStart based on Integer32"""
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


_PromSwitchPortFastStart_Type.__name__ = "Integer32"
_PromSwitchPortFastStart_Object = MibTableColumn
promSwitchPortFastStart = _PromSwitchPortFastStart_Object(
    (1, 3, 6, 1, 4, 1, 2167, 5, 2, 1, 1, 17),
    _PromSwitchPortFastStart_Type()
)
promSwitchPortFastStart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    promSwitchPortFastStart.setStatus("mandatory")


class _PromSwitchPortVtpSnooping_Type(Integer32):
    """Custom type promSwitchPortVtpSnooping based on Integer32"""
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


_PromSwitchPortVtpSnooping_Type.__name__ = "Integer32"
_PromSwitchPortVtpSnooping_Object = MibTableColumn
promSwitchPortVtpSnooping = _PromSwitchPortVtpSnooping_Object(
    (1, 3, 6, 1, 4, 1, 2167, 5, 2, 1, 1, 18),
    _PromSwitchPortVtpSnooping_Type()
)
promSwitchPortVtpSnooping.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    promSwitchPortVtpSnooping.setStatus("mandatory")


class _PromSwitchPortIntrusionTrap_Type(Integer32):
    """Custom type promSwitchPortIntrusionTrap based on Integer32"""
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


_PromSwitchPortIntrusionTrap_Type.__name__ = "Integer32"
_PromSwitchPortIntrusionTrap_Object = MibTableColumn
promSwitchPortIntrusionTrap = _PromSwitchPortIntrusionTrap_Object(
    (1, 3, 6, 1, 4, 1, 2167, 5, 2, 1, 1, 19),
    _PromSwitchPortIntrusionTrap_Type()
)
promSwitchPortIntrusionTrap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    promSwitchPortIntrusionTrap.setStatus("mandatory")
_PromSwitchPortIntrusionTrapTimer_Type = Integer32
_PromSwitchPortIntrusionTrapTimer_Object = MibTableColumn
promSwitchPortIntrusionTrapTimer = _PromSwitchPortIntrusionTrapTimer_Object(
    (1, 3, 6, 1, 4, 1, 2167, 5, 2, 1, 1, 20),
    _PromSwitchPortIntrusionTrapTimer_Type()
)
promSwitchPortIntrusionTrapTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    promSwitchPortIntrusionTrapTimer.setStatus("mandatory")
_PromHuntGroupMgt_ObjectIdentity = ObjectIdentity
promHuntGroupMgt = _PromHuntGroupMgt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2167, 5, 4)
)
_PromHuntGroupTable_Object = MibTable
promHuntGroupTable = _PromHuntGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 2167, 5, 4, 1)
)
if mibBuilder.loadTexts:
    promHuntGroupTable.setStatus("mandatory")
_PromHuntGroupEntry_Object = MibTableRow
promHuntGroupEntry = _PromHuntGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 2167, 5, 4, 1, 1)
)
promHuntGroupEntry.setIndexNames(
    (0, "PROMINET-MIB", "promHuntGroupIndex"),
)
if mibBuilder.loadTexts:
    promHuntGroupEntry.setStatus("mandatory")
_PromHuntGroupIndex_Type = Integer32
_PromHuntGroupIndex_Object = MibTableColumn
promHuntGroupIndex = _PromHuntGroupIndex_Object(
    (1, 3, 6, 1, 4, 1, 2167, 5, 4, 1, 1, 1),
    _PromHuntGroupIndex_Type()
)
promHuntGroupIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    promHuntGroupIndex.setStatus("mandatory")
_PromHuntGroupName_Type = DisplayString
_PromHuntGroupName_Object = MibTableColumn
promHuntGroupName = _PromHuntGroupName_Object(
    (1, 3, 6, 1, 4, 1, 2167, 5, 4, 1, 1, 2),
    _PromHuntGroupName_Type()
)
promHuntGroupName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    promHuntGroupName.setStatus("mandatory")
_PromHuntGroupBasePort_Type = ResourceId
_PromHuntGroupBasePort_Object = MibTableColumn
promHuntGroupBasePort = _PromHuntGroupBasePort_Object(
    (1, 3, 6, 1, 4, 1, 2167, 5, 4, 1, 1, 3),
    _PromHuntGroupBasePort_Type()
)
promHuntGroupBasePort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    promHuntGroupBasePort.setStatus("mandatory")
_PromHuntGroupNumberOfPorts_Type = Integer32
_PromHuntGroupNumberOfPorts_Object = MibTableColumn
promHuntGroupNumberOfPorts = _PromHuntGroupNumberOfPorts_Object(
    (1, 3, 6, 1, 4, 1, 2167, 5, 4, 1, 1, 4),
    _PromHuntGroupNumberOfPorts_Type()
)
promHuntGroupNumberOfPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    promHuntGroupNumberOfPorts.setStatus("mandatory")


class _PromHuntGroupLoadSharing_Type(Integer32):
    """Custom type promHuntGroupLoadSharing based on Integer32"""
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


_PromHuntGroupLoadSharing_Type.__name__ = "Integer32"
_PromHuntGroupLoadSharing_Object = MibTableColumn
promHuntGroupLoadSharing = _PromHuntGroupLoadSharing_Object(
    (1, 3, 6, 1, 4, 1, 2167, 5, 4, 1, 1, 5),
    _PromHuntGroupLoadSharing_Type()
)
promHuntGroupLoadSharing.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    promHuntGroupLoadSharing.setStatus("mandatory")


class _PromHuntGroupStatus_Type(Integer32):
    """Custom type promHuntGroupStatus based on Integer32"""
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


_PromHuntGroupStatus_Type.__name__ = "Integer32"
_PromHuntGroupStatus_Object = MibTableColumn
promHuntGroupStatus = _PromHuntGroupStatus_Object(
    (1, 3, 6, 1, 4, 1, 2167, 5, 4, 1, 1, 6),
    _PromHuntGroupStatus_Type()
)
promHuntGroupStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    promHuntGroupStatus.setStatus("mandatory")
_PromPortMirroringMgt_ObjectIdentity = ObjectIdentity
promPortMirroringMgt = _PromPortMirroringMgt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2167, 5, 5)
)
_PromPortMirroringTable_Object = MibTable
promPortMirroringTable = _PromPortMirroringTable_Object(
    (1, 3, 6, 1, 4, 1, 2167, 5, 5, 1)
)
if mibBuilder.loadTexts:
    promPortMirroringTable.setStatus("mandatory")
_PromPortMirroringEntry_Object = MibTableRow
promPortMirroringEntry = _PromPortMirroringEntry_Object(
    (1, 3, 6, 1, 4, 1, 2167, 5, 5, 1, 1)
)
promPortMirroringEntry.setIndexNames(
    (0, "PROMINET-MIB", "promPortMirroringIndex"),
)
if mibBuilder.loadTexts:
    promPortMirroringEntry.setStatus("mandatory")
_PromPortMirroringIndex_Type = ResourceId
_PromPortMirroringIndex_Object = MibTableColumn
promPortMirroringIndex = _PromPortMirroringIndex_Object(
    (1, 3, 6, 1, 4, 1, 2167, 5, 5, 1, 1, 1),
    _PromPortMirroringIndex_Type()
)
promPortMirroringIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    promPortMirroringIndex.setStatus("mandatory")
_PromPortMirroringSourceSubPort_Type = Integer32
_PromPortMirroringSourceSubPort_Object = MibTableColumn
promPortMirroringSourceSubPort = _PromPortMirroringSourceSubPort_Object(
    (1, 3, 6, 1, 4, 1, 2167, 5, 5, 1, 1, 2),
    _PromPortMirroringSourceSubPort_Type()
)
promPortMirroringSourceSubPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    promPortMirroringSourceSubPort.setStatus("mandatory")


class _PromPortMirroringSamplerType_Type(Integer32):
    """Custom type promPortMirroringSamplerType based on Integer32"""
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


_PromPortMirroringSamplerType_Type.__name__ = "Integer32"
_PromPortMirroringSamplerType_Object = MibTableColumn
promPortMirroringSamplerType = _PromPortMirroringSamplerType_Object(
    (1, 3, 6, 1, 4, 1, 2167, 5, 5, 1, 1, 3),
    _PromPortMirroringSamplerType_Type()
)
promPortMirroringSamplerType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    promPortMirroringSamplerType.setStatus("mandatory")
_PromPortMirroringRate_Type = Integer32
_PromPortMirroringRate_Object = MibTableColumn
promPortMirroringRate = _PromPortMirroringRate_Object(
    (1, 3, 6, 1, 4, 1, 2167, 5, 5, 1, 1, 4),
    _PromPortMirroringRate_Type()
)
promPortMirroringRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    promPortMirroringRate.setStatus("mandatory")
_PromPortMirroringMirrorPort_Type = ResourceId
_PromPortMirroringMirrorPort_Object = MibTableColumn
promPortMirroringMirrorPort = _PromPortMirroringMirrorPort_Object(
    (1, 3, 6, 1, 4, 1, 2167, 5, 5, 1, 1, 5),
    _PromPortMirroringMirrorPort_Type()
)
promPortMirroringMirrorPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    promPortMirroringMirrorPort.setStatus("mandatory")
_PromVlanMgt_ObjectIdentity = ObjectIdentity
promVlanMgt = _PromVlanMgt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2167, 7)
)
_PromVlans_ObjectIdentity = ObjectIdentity
promVlans = _PromVlans_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2167, 7, 1)
)
_PromVlanTable_Object = MibTable
promVlanTable = _PromVlanTable_Object(
    (1, 3, 6, 1, 4, 1, 2167, 7, 1, 1)
)
if mibBuilder.loadTexts:
    promVlanTable.setStatus("mandatory")
_PromVlanEntry_Object = MibTableRow
promVlanEntry = _PromVlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 2167, 7, 1, 1, 1)
)
promVlanEntry.setIndexNames(
    (0, "PROMINET-MIB", "promVlanID"),
)
if mibBuilder.loadTexts:
    promVlanEntry.setStatus("mandatory")
_PromVlanID_Type = Integer32
_PromVlanID_Object = MibTableColumn
promVlanID = _PromVlanID_Object(
    (1, 3, 6, 1, 4, 1, 2167, 7, 1, 1, 1, 1),
    _PromVlanID_Type()
)
promVlanID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    promVlanID.setStatus("mandatory")


class _PromVlanName_Type(DisplayString):
    """Custom type promVlanName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_PromVlanName_Type.__name__ = "DisplayString"
_PromVlanName_Object = MibTableColumn
promVlanName = _PromVlanName_Object(
    (1, 3, 6, 1, 4, 1, 2167, 7, 1, 1, 1, 2),
    _PromVlanName_Type()
)
promVlanName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    promVlanName.setStatus("mandatory")
_PromVlanIfIndex_Type = Integer32
_PromVlanIfIndex_Object = MibTableColumn
promVlanIfIndex = _PromVlanIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2167, 7, 1, 1, 1, 3),
    _PromVlanIfIndex_Type()
)
promVlanIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    promVlanIfIndex.setStatus("mandatory")
_PromVlanAFTIndex_Type = Integer32
_PromVlanAFTIndex_Object = MibTableColumn
promVlanAFTIndex = _PromVlanAFTIndex_Object(
    (1, 3, 6, 1, 4, 1, 2167, 7, 1, 1, 1, 4),
    _PromVlanAFTIndex_Type()
)
promVlanAFTIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    promVlanAFTIndex.setStatus("mandatory")
_PromVlanBridgeIndex_Type = ResourceId
_PromVlanBridgeIndex_Object = MibTableColumn
promVlanBridgeIndex = _PromVlanBridgeIndex_Object(
    (1, 3, 6, 1, 4, 1, 2167, 7, 1, 1, 1, 5),
    _PromVlanBridgeIndex_Type()
)
promVlanBridgeIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    promVlanBridgeIndex.setStatus("mandatory")


class _PromVlanStatus_Type(Integer32):
    """Custom type promVlanStatus based on Integer32"""
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


_PromVlanStatus_Type.__name__ = "Integer32"
_PromVlanStatus_Object = MibTableColumn
promVlanStatus = _PromVlanStatus_Object(
    (1, 3, 6, 1, 4, 1, 2167, 7, 1, 1, 1, 6),
    _PromVlanStatus_Type()
)
promVlanStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    promVlanStatus.setStatus("mandatory")


class _PromVlanInitialHashTableSize_Type(Integer32):
    """Custom type promVlanInitialHashTableSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(16, 8192),
    )


_PromVlanInitialHashTableSize_Type.__name__ = "Integer32"
_PromVlanInitialHashTableSize_Object = MibTableColumn
promVlanInitialHashTableSize = _PromVlanInitialHashTableSize_Object(
    (1, 3, 6, 1, 4, 1, 2167, 7, 1, 1, 1, 7),
    _PromVlanInitialHashTableSize_Type()
)
promVlanInitialHashTableSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    promVlanInitialHashTableSize.setStatus("mandatory")


class _PromVlanAutoIncrementHTSize_Type(Integer32):
    """Custom type promVlanAutoIncrementHTSize based on Integer32"""
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


_PromVlanAutoIncrementHTSize_Type.__name__ = "Integer32"
_PromVlanAutoIncrementHTSize_Object = MibTableColumn
promVlanAutoIncrementHTSize = _PromVlanAutoIncrementHTSize_Object(
    (1, 3, 6, 1, 4, 1, 2167, 7, 1, 1, 1, 8),
    _PromVlanAutoIncrementHTSize_Type()
)
promVlanAutoIncrementHTSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    promVlanAutoIncrementHTSize.setStatus("mandatory")


class _PromVlanLearnStatus_Type(Integer32):
    """Custom type promVlanLearnStatus based on Integer32"""
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
          ("vtpSnooping", 2))
    )


_PromVlanLearnStatus_Type.__name__ = "Integer32"
_PromVlanLearnStatus_Object = MibTableColumn
promVlanLearnStatus = _PromVlanLearnStatus_Object(
    (1, 3, 6, 1, 4, 1, 2167, 7, 1, 1, 1, 9),
    _PromVlanLearnStatus_Type()
)
promVlanLearnStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    promVlanLearnStatus.setStatus("mandatory")
_PromVlanMappings_ObjectIdentity = ObjectIdentity
promVlanMappings = _PromVlanMappings_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2167, 7, 3)
)
_Prom3ComMapping_ObjectIdentity = ObjectIdentity
prom3ComMapping = _Prom3ComMapping_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2167, 7, 3, 1)
)
_Prom3ComMappingTable_Object = MibTable
prom3ComMappingTable = _Prom3ComMappingTable_Object(
    (1, 3, 6, 1, 4, 1, 2167, 7, 3, 1, 1)
)
if mibBuilder.loadTexts:
    prom3ComMappingTable.setStatus("mandatory")
_Prom3ComMappingEntry_Object = MibTableRow
prom3ComMappingEntry = _Prom3ComMappingEntry_Object(
    (1, 3, 6, 1, 4, 1, 2167, 7, 3, 1, 1, 1)
)
prom3ComMappingEntry.setIndexNames(
    (0, "PROMINET-MIB", "prom3ComMappingTableIndex"),
)
if mibBuilder.loadTexts:
    prom3ComMappingEntry.setStatus("mandatory")
_Prom3ComMappingTableIndex_Type = Integer32
_Prom3ComMappingTableIndex_Object = MibTableColumn
prom3ComMappingTableIndex = _Prom3ComMappingTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 2167, 7, 3, 1, 1, 1, 1),
    _Prom3ComMappingTableIndex_Type()
)
prom3ComMappingTableIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prom3ComMappingTableIndex.setStatus("mandatory")


class _Prom3ComMappingTableName_Type(DisplayString):
    """Custom type prom3ComMappingTableName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_Prom3ComMappingTableName_Type.__name__ = "DisplayString"
_Prom3ComMappingTableName_Object = MibTableColumn
prom3ComMappingTableName = _Prom3ComMappingTableName_Object(
    (1, 3, 6, 1, 4, 1, 2167, 7, 3, 1, 1, 1, 2),
    _Prom3ComMappingTableName_Type()
)
prom3ComMappingTableName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prom3ComMappingTableName.setStatus("mandatory")


class _Prom3ComMappingTableStatus_Type(Integer32):
    """Custom type prom3ComMappingTableStatus based on Integer32"""
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


_Prom3ComMappingTableStatus_Type.__name__ = "Integer32"
_Prom3ComMappingTableStatus_Object = MibTableColumn
prom3ComMappingTableStatus = _Prom3ComMappingTableStatus_Object(
    (1, 3, 6, 1, 4, 1, 2167, 7, 3, 1, 1, 1, 3),
    _Prom3ComMappingTableStatus_Type()
)
prom3ComMappingTableStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prom3ComMappingTableStatus.setStatus("mandatory")
_PromVlan3ComMapping_ObjectIdentity = ObjectIdentity
promVlan3ComMapping = _PromVlan3ComMapping_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2167, 7, 3, 2)
)
_PromVlan3ComMappingTable_Object = MibTable
promVlan3ComMappingTable = _PromVlan3ComMappingTable_Object(
    (1, 3, 6, 1, 4, 1, 2167, 7, 3, 2, 1)
)
if mibBuilder.loadTexts:
    promVlan3ComMappingTable.setStatus("mandatory")
_PromVlan3ComMappingEntry_Object = MibTableRow
promVlan3ComMappingEntry = _PromVlan3ComMappingEntry_Object(
    (1, 3, 6, 1, 4, 1, 2167, 7, 3, 2, 1, 1)
)
promVlan3ComMappingEntry.setIndexNames(
    (0, "PROMINET-MIB", "prom3ComMappingTableIndex"),
    (0, "PROMINET-MIB", "promVlan3ComMappingIndex"),
)
if mibBuilder.loadTexts:
    promVlan3ComMappingEntry.setStatus("mandatory")


class _PromVlan3ComMappingIndex_Type(Integer32):
    """Custom type promVlan3ComMappingIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_PromVlan3ComMappingIndex_Type.__name__ = "Integer32"
_PromVlan3ComMappingIndex_Object = MibTableColumn
promVlan3ComMappingIndex = _PromVlan3ComMappingIndex_Object(
    (1, 3, 6, 1, 4, 1, 2167, 7, 3, 2, 1, 1, 1),
    _PromVlan3ComMappingIndex_Type()
)
promVlan3ComMappingIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    promVlan3ComMappingIndex.setStatus("mandatory")
_PromVlan3ComMappingVlanID_Type = Integer32
_PromVlan3ComMappingVlanID_Object = MibTableColumn
promVlan3ComMappingVlanID = _PromVlan3ComMappingVlanID_Object(
    (1, 3, 6, 1, 4, 1, 2167, 7, 3, 2, 1, 1, 2),
    _PromVlan3ComMappingVlanID_Type()
)
promVlan3ComMappingVlanID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    promVlan3ComMappingVlanID.setStatus("mandatory")


class _PromVlan3ComMappingStatus_Type(Integer32):
    """Custom type promVlan3ComMappingStatus based on Integer32"""
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


_PromVlan3ComMappingStatus_Type.__name__ = "Integer32"
_PromVlan3ComMappingStatus_Object = MibTableColumn
promVlan3ComMappingStatus = _PromVlan3ComMappingStatus_Object(
    (1, 3, 6, 1, 4, 1, 2167, 7, 3, 2, 1, 1, 3),
    _PromVlan3ComMappingStatus_Type()
)
promVlan3ComMappingStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    promVlan3ComMappingStatus.setStatus("mandatory")
_PromVirtualPorts_ObjectIdentity = ObjectIdentity
promVirtualPorts = _PromVirtualPorts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2167, 7, 4)
)
_PromVirtualSwitchPortTable_Object = MibTable
promVirtualSwitchPortTable = _PromVirtualSwitchPortTable_Object(
    (1, 3, 6, 1, 4, 1, 2167, 7, 4, 1)
)
if mibBuilder.loadTexts:
    promVirtualSwitchPortTable.setStatus("mandatory")
_PromVirtualSwitchPortEntry_Object = MibTableRow
promVirtualSwitchPortEntry = _PromVirtualSwitchPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 2167, 7, 4, 1, 1)
)
promVirtualSwitchPortEntry.setIndexNames(
    (0, "PROMINET-MIB", "promVirtualSwitchPortIndex"),
)
if mibBuilder.loadTexts:
    promVirtualSwitchPortEntry.setStatus("mandatory")
_PromVirtualSwitchPortIndex_Type = ResourceId
_PromVirtualSwitchPortIndex_Object = MibTableColumn
promVirtualSwitchPortIndex = _PromVirtualSwitchPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 2167, 7, 4, 1, 1, 1),
    _PromVirtualSwitchPortIndex_Type()
)
promVirtualSwitchPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    promVirtualSwitchPortIndex.setStatus("mandatory")


class _PromVirtualSwitchPortFormat_Type(Integer32):
    """Custom type promVirtualSwitchPortFormat based on Integer32"""
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


_PromVirtualSwitchPortFormat_Type.__name__ = "Integer32"
_PromVirtualSwitchPortFormat_Object = MibTableColumn
promVirtualSwitchPortFormat = _PromVirtualSwitchPortFormat_Object(
    (1, 3, 6, 1, 4, 1, 2167, 7, 4, 1, 1, 2),
    _PromVirtualSwitchPortFormat_Type()
)
promVirtualSwitchPortFormat.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    promVirtualSwitchPortFormat.setStatus("mandatory")
_PromVirtualSwitchPortBridgePort_Type = ResourceId
_PromVirtualSwitchPortBridgePort_Object = MibTableColumn
promVirtualSwitchPortBridgePort = _PromVirtualSwitchPortBridgePort_Object(
    (1, 3, 6, 1, 4, 1, 2167, 7, 4, 1, 1, 3),
    _PromVirtualSwitchPortBridgePort_Type()
)
promVirtualSwitchPortBridgePort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    promVirtualSwitchPortBridgePort.setStatus("mandatory")


class _PromVirtualSwitchPortBindingType_Type(Integer32):
    """Custom type promVirtualSwitchPortBindingType based on Integer32"""
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


_PromVirtualSwitchPortBindingType_Type.__name__ = "Integer32"
_PromVirtualSwitchPortBindingType_Object = MibTableColumn
promVirtualSwitchPortBindingType = _PromVirtualSwitchPortBindingType_Object(
    (1, 3, 6, 1, 4, 1, 2167, 7, 4, 1, 1, 4),
    _PromVirtualSwitchPortBindingType_Type()
)
promVirtualSwitchPortBindingType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    promVirtualSwitchPortBindingType.setStatus("mandatory")


class _PromVirtualSwitchPortStatus_Type(Integer32):
    """Custom type promVirtualSwitchPortStatus based on Integer32"""
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


_PromVirtualSwitchPortStatus_Type.__name__ = "Integer32"
_PromVirtualSwitchPortStatus_Object = MibTableColumn
promVirtualSwitchPortStatus = _PromVirtualSwitchPortStatus_Object(
    (1, 3, 6, 1, 4, 1, 2167, 7, 4, 1, 1, 5),
    _PromVirtualSwitchPortStatus_Type()
)
promVirtualSwitchPortStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    promVirtualSwitchPortStatus.setStatus("mandatory")
_PromVirtualModulePortTable_Object = MibTable
promVirtualModulePortTable = _PromVirtualModulePortTable_Object(
    (1, 3, 6, 1, 4, 1, 2167, 7, 4, 2)
)
if mibBuilder.loadTexts:
    promVirtualModulePortTable.setStatus("mandatory")
_PromVirtualModulePortEntry_Object = MibTableRow
promVirtualModulePortEntry = _PromVirtualModulePortEntry_Object(
    (1, 3, 6, 1, 4, 1, 2167, 7, 4, 2, 1)
)
promVirtualModulePortEntry.setIndexNames(
    (0, "PROMINET-MIB", "promVlanID"),
    (0, "PROMINET-MIB", "promPortIndex"),
)
if mibBuilder.loadTexts:
    promVirtualModulePortEntry.setStatus("mandatory")
_PromVirtualModulePortIndex_Type = ResourceId
_PromVirtualModulePortIndex_Object = MibTableColumn
promVirtualModulePortIndex = _PromVirtualModulePortIndex_Object(
    (1, 3, 6, 1, 4, 1, 2167, 7, 4, 2, 1, 1),
    _PromVirtualModulePortIndex_Type()
)
promVirtualModulePortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    promVirtualModulePortIndex.setStatus("mandatory")


class _PromVirtualModulePortFormat_Type(Integer32):
    """Custom type promVirtualModulePortFormat based on Integer32"""
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


_PromVirtualModulePortFormat_Type.__name__ = "Integer32"
_PromVirtualModulePortFormat_Object = MibTableColumn
promVirtualModulePortFormat = _PromVirtualModulePortFormat_Object(
    (1, 3, 6, 1, 4, 1, 2167, 7, 4, 2, 1, 2),
    _PromVirtualModulePortFormat_Type()
)
promVirtualModulePortFormat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    promVirtualModulePortFormat.setStatus("mandatory")
_PromVirtualModulePortBridgePort_Type = ResourceId
_PromVirtualModulePortBridgePort_Object = MibTableColumn
promVirtualModulePortBridgePort = _PromVirtualModulePortBridgePort_Object(
    (1, 3, 6, 1, 4, 1, 2167, 7, 4, 2, 1, 3),
    _PromVirtualModulePortBridgePort_Type()
)
promVirtualModulePortBridgePort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    promVirtualModulePortBridgePort.setStatus("mandatory")


class _PromVirtualModulePortBindingType_Type(Integer32):
    """Custom type promVirtualModulePortBindingType based on Integer32"""
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


_PromVirtualModulePortBindingType_Type.__name__ = "Integer32"
_PromVirtualModulePortBindingType_Object = MibTableColumn
promVirtualModulePortBindingType = _PromVirtualModulePortBindingType_Object(
    (1, 3, 6, 1, 4, 1, 2167, 7, 4, 2, 1, 4),
    _PromVirtualModulePortBindingType_Type()
)
promVirtualModulePortBindingType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    promVirtualModulePortBindingType.setStatus("mandatory")


class _PromVirtualModulePortModuleName_Type(DisplayString):
    """Custom type promVirtualModulePortModuleName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_PromVirtualModulePortModuleName_Type.__name__ = "DisplayString"
_PromVirtualModulePortModuleName_Object = MibTableColumn
promVirtualModulePortModuleName = _PromVirtualModulePortModuleName_Object(
    (1, 3, 6, 1, 4, 1, 2167, 7, 4, 2, 1, 5),
    _PromVirtualModulePortModuleName_Type()
)
promVirtualModulePortModuleName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    promVirtualModulePortModuleName.setStatus("mandatory")


class _PromVirtualModulePortPortName_Type(DisplayString):
    """Custom type promVirtualModulePortPortName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_PromVirtualModulePortPortName_Type.__name__ = "DisplayString"
_PromVirtualModulePortPortName_Object = MibTableColumn
promVirtualModulePortPortName = _PromVirtualModulePortPortName_Object(
    (1, 3, 6, 1, 4, 1, 2167, 7, 4, 2, 1, 6),
    _PromVirtualModulePortPortName_Type()
)
promVirtualModulePortPortName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    promVirtualModulePortPortName.setStatus("mandatory")
_PromEvents_ObjectIdentity = ObjectIdentity
promEvents = _PromEvents_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2167, 10)
)
_PromEventMgt_ObjectIdentity = ObjectIdentity
promEventMgt = _PromEventMgt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2167, 10, 1)
)
_PromEventTable_Object = MibTable
promEventTable = _PromEventTable_Object(
    (1, 3, 6, 1, 4, 1, 2167, 10, 1, 1)
)
if mibBuilder.loadTexts:
    promEventTable.setStatus("mandatory")
_PromEventEntry_Object = MibTableRow
promEventEntry = _PromEventEntry_Object(
    (1, 3, 6, 1, 4, 1, 2167, 10, 1, 1, 1)
)
promEventEntry.setIndexNames(
    (0, "PROMINET-MIB", "promEventIndex"),
)
if mibBuilder.loadTexts:
    promEventEntry.setStatus("mandatory")
_PromEventIndex_Type = Integer32
_PromEventIndex_Object = MibTableColumn
promEventIndex = _PromEventIndex_Object(
    (1, 3, 6, 1, 4, 1, 2167, 10, 1, 1, 1, 1),
    _PromEventIndex_Type()
)
promEventIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    promEventIndex.setStatus("mandatory")


class _PromEventMode_Type(Integer32):
    """Custom type promEventMode based on Integer32"""
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


_PromEventMode_Type.__name__ = "Integer32"
_PromEventMode_Object = MibTableColumn
promEventMode = _PromEventMode_Object(
    (1, 3, 6, 1, 4, 1, 2167, 10, 1, 1, 1, 2),
    _PromEventMode_Type()
)
promEventMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    promEventMode.setStatus("mandatory")


class _PromEventLogAction_Type(Integer32):
    """Custom type promEventLogAction based on Integer32"""
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


_PromEventLogAction_Type.__name__ = "Integer32"
_PromEventLogAction_Object = MibTableColumn
promEventLogAction = _PromEventLogAction_Object(
    (1, 3, 6, 1, 4, 1, 2167, 10, 1, 1, 1, 3),
    _PromEventLogAction_Type()
)
promEventLogAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    promEventLogAction.setStatus("mandatory")


class _PromEventTrapAction_Type(Integer32):
    """Custom type promEventTrapAction based on Integer32"""
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


_PromEventTrapAction_Type.__name__ = "Integer32"
_PromEventTrapAction_Object = MibTableColumn
promEventTrapAction = _PromEventTrapAction_Object(
    (1, 3, 6, 1, 4, 1, 2167, 10, 1, 1, 1, 4),
    _PromEventTrapAction_Type()
)
promEventTrapAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    promEventTrapAction.setStatus("mandatory")


class _PromEventConsoleAction_Type(Integer32):
    """Custom type promEventConsoleAction based on Integer32"""
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


_PromEventConsoleAction_Type.__name__ = "Integer32"
_PromEventConsoleAction_Object = MibTableColumn
promEventConsoleAction = _PromEventConsoleAction_Object(
    (1, 3, 6, 1, 4, 1, 2167, 10, 1, 1, 1, 5),
    _PromEventConsoleAction_Type()
)
promEventConsoleAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    promEventConsoleAction.setStatus("mandatory")
_PromEventLogMgt_ObjectIdentity = ObjectIdentity
promEventLogMgt = _PromEventLogMgt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2167, 10, 2)
)


class _PromLogTableMaxSize_Type(Integer32):
    """Custom type promLogTableMaxSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2048),
    )


_PromLogTableMaxSize_Type.__name__ = "Integer32"
_PromLogTableMaxSize_Object = MibScalar
promLogTableMaxSize = _PromLogTableMaxSize_Object(
    (1, 3, 6, 1, 4, 1, 2167, 10, 2, 1),
    _PromLogTableMaxSize_Type()
)
promLogTableMaxSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    promLogTableMaxSize.setStatus("mandatory")


class _PromLogLastEntry_Type(Integer32):
    """Custom type promLogLastEntry based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_PromLogLastEntry_Type.__name__ = "Integer32"
_PromLogLastEntry_Object = MibScalar
promLogLastEntry = _PromLogLastEntry_Object(
    (1, 3, 6, 1, 4, 1, 2167, 10, 2, 2),
    _PromLogLastEntry_Type()
)
promLogLastEntry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    promLogLastEntry.setStatus("mandatory")
_PromLogWraps_Type = Counter32
_PromLogWraps_Object = MibScalar
promLogWraps = _PromLogWraps_Object(
    (1, 3, 6, 1, 4, 1, 2167, 10, 2, 3),
    _PromLogWraps_Type()
)
promLogWraps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    promLogWraps.setStatus("mandatory")
_PromEventLog_ObjectIdentity = ObjectIdentity
promEventLog = _PromEventLog_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2167, 10, 3)
)
_PromEventLogTable_Object = MibTable
promEventLogTable = _PromEventLogTable_Object(
    (1, 3, 6, 1, 4, 1, 2167, 10, 3, 1)
)
if mibBuilder.loadTexts:
    promEventLogTable.setStatus("mandatory")
_PromEventLogEntry_Object = MibTableRow
promEventLogEntry = _PromEventLogEntry_Object(
    (1, 3, 6, 1, 4, 1, 2167, 10, 3, 1, 1)
)
promEventLogEntry.setIndexNames(
    (0, "PROMINET-MIB", "promEventLogIndex"),
)
if mibBuilder.loadTexts:
    promEventLogEntry.setStatus("mandatory")


class _PromEventLogEventIndex_Type(Integer32):
    """Custom type promEventLogEventIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_PromEventLogEventIndex_Type.__name__ = "Integer32"
_PromEventLogEventIndex_Object = MibTableColumn
promEventLogEventIndex = _PromEventLogEventIndex_Object(
    (1, 3, 6, 1, 4, 1, 2167, 10, 3, 1, 1, 1),
    _PromEventLogEventIndex_Type()
)
promEventLogEventIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    promEventLogEventIndex.setStatus("mandatory")


class _PromEventLogIndex_Type(Integer32):
    """Custom type promEventLogIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_PromEventLogIndex_Type.__name__ = "Integer32"
_PromEventLogIndex_Object = MibTableColumn
promEventLogIndex = _PromEventLogIndex_Object(
    (1, 3, 6, 1, 4, 1, 2167, 10, 3, 1, 1, 2),
    _PromEventLogIndex_Type()
)
promEventLogIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    promEventLogIndex.setStatus("mandatory")
_PromEventLogTime_Type = TimeTicks
_PromEventLogTime_Object = MibTableColumn
promEventLogTime = _PromEventLogTime_Object(
    (1, 3, 6, 1, 4, 1, 2167, 10, 3, 1, 1, 3),
    _PromEventLogTime_Type()
)
promEventLogTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    promEventLogTime.setStatus("mandatory")


class _PromEventLogDescr_Type(DisplayString):
    """Custom type promEventLogDescr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_PromEventLogDescr_Type.__name__ = "DisplayString"
_PromEventLogDescr_Object = MibTableColumn
promEventLogDescr = _PromEventLogDescr_Object(
    (1, 3, 6, 1, 4, 1, 2167, 10, 3, 1, 1, 4),
    _PromEventLogDescr_Type()
)
promEventLogDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    promEventLogDescr.setStatus("mandatory")
_PromEventLogType_Type = EventCategory
_PromEventLogType_Object = MibTableColumn
promEventLogType = _PromEventLogType_Object(
    (1, 3, 6, 1, 4, 1, 2167, 10, 3, 1, 1, 5),
    _PromEventLogType_Type()
)
promEventLogType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    promEventLogType.setStatus("mandatory")


class _PromEventLogSeverity_Type(Integer32):
    """Custom type promEventLogSeverity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_PromEventLogSeverity_Type.__name__ = "Integer32"
_PromEventLogSeverity_Object = MibTableColumn
promEventLogSeverity = _PromEventLogSeverity_Object(
    (1, 3, 6, 1, 4, 1, 2167, 10, 3, 1, 1, 6),
    _PromEventLogSeverity_Type()
)
promEventLogSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    promEventLogSeverity.setStatus("mandatory")


class _PromEventLogDTM_Type(DisplayString):
    """Custom type promEventLogDTM based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(18, 18),
    )


_PromEventLogDTM_Type.__name__ = "DisplayString"
_PromEventLogDTM_Object = MibTableColumn
promEventLogDTM = _PromEventLogDTM_Object(
    (1, 3, 6, 1, 4, 1, 2167, 10, 3, 1, 1, 7),
    _PromEventLogDTM_Type()
)
promEventLogDTM.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    promEventLogDTM.setStatus("mandatory")
_PromEventLogResType_Type = ResourceType
_PromEventLogResType_Object = MibTableColumn
promEventLogResType = _PromEventLogResType_Object(
    (1, 3, 6, 1, 4, 1, 2167, 10, 3, 1, 1, 8),
    _PromEventLogResType_Type()
)
promEventLogResType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    promEventLogResType.setStatus("mandatory")
_PromEventLogResID_Type = ResourceId
_PromEventLogResID_Object = MibTableColumn
promEventLogResID = _PromEventLogResID_Object(
    (1, 3, 6, 1, 4, 1, 2167, 10, 3, 1, 1, 9),
    _PromEventLogResID_Type()
)
promEventLogResID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    promEventLogResID.setStatus("mandatory")
_PromEventLogResLeaf_Type = Integer32
_PromEventLogResLeaf_Object = MibTableColumn
promEventLogResLeaf = _PromEventLogResLeaf_Object(
    (1, 3, 6, 1, 4, 1, 2167, 10, 3, 1, 1, 10),
    _PromEventLogResLeaf_Type()
)
promEventLogResLeaf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    promEventLogResLeaf.setStatus("mandatory")
_PromEventLogValueType_Type = EventValueType
_PromEventLogValueType_Object = MibTableColumn
promEventLogValueType = _PromEventLogValueType_Object(
    (1, 3, 6, 1, 4, 1, 2167, 10, 3, 1, 1, 11),
    _PromEventLogValueType_Type()
)
promEventLogValueType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    promEventLogValueType.setStatus("mandatory")


class _PromEventLogValue_Type(OctetString):
    """Custom type promEventLogValue based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_PromEventLogValue_Type.__name__ = "OctetString"
_PromEventLogValue_Object = MibTableColumn
promEventLogValue = _PromEventLogValue_Object(
    (1, 3, 6, 1, 4, 1, 2167, 10, 3, 1, 1, 12),
    _PromEventLogValue_Type()
)
promEventLogValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    promEventLogValue.setStatus("mandatory")
_PromEventLogEpochTime_Type = Integer32
_PromEventLogEpochTime_Object = MibTableColumn
promEventLogEpochTime = _PromEventLogEpochTime_Object(
    (1, 3, 6, 1, 4, 1, 2167, 10, 3, 1, 1, 13),
    _PromEventLogEpochTime_Type()
)
promEventLogEpochTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    promEventLogEpochTime.setStatus("mandatory")


class _PromEventLogID_Type(Integer32):
    """Custom type promEventLogID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_PromEventLogID_Type.__name__ = "Integer32"
_PromEventLogID_Object = MibTableColumn
promEventLogID = _PromEventLogID_Object(
    (1, 3, 6, 1, 4, 1, 2167, 10, 3, 1, 1, 14),
    _PromEventLogID_Type()
)
promEventLogID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    promEventLogID.setStatus("mandatory")
_PromShutdownLogMgt_ObjectIdentity = ObjectIdentity
promShutdownLogMgt = _PromShutdownLogMgt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2167, 10, 4)
)


class _PromShutdownLogTableMaxSize_Type(Integer32):
    """Custom type promShutdownLogTableMaxSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 64),
    )


_PromShutdownLogTableMaxSize_Type.__name__ = "Integer32"
_PromShutdownLogTableMaxSize_Object = MibScalar
promShutdownLogTableMaxSize = _PromShutdownLogTableMaxSize_Object(
    (1, 3, 6, 1, 4, 1, 2167, 10, 4, 1),
    _PromShutdownLogTableMaxSize_Type()
)
promShutdownLogTableMaxSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    promShutdownLogTableMaxSize.setStatus("mandatory")


class _PromShutdownLogLastEntry_Type(Integer32):
    """Custom type promShutdownLogLastEntry based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_PromShutdownLogLastEntry_Type.__name__ = "Integer32"
_PromShutdownLogLastEntry_Object = MibScalar
promShutdownLogLastEntry = _PromShutdownLogLastEntry_Object(
    (1, 3, 6, 1, 4, 1, 2167, 10, 4, 2),
    _PromShutdownLogLastEntry_Type()
)
promShutdownLogLastEntry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    promShutdownLogLastEntry.setStatus("mandatory")


class _PromShutdownLogAcknowledged_Type(Integer32):
    """Custom type promShutdownLogAcknowledged based on Integer32"""
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


_PromShutdownLogAcknowledged_Type.__name__ = "Integer32"
_PromShutdownLogAcknowledged_Object = MibScalar
promShutdownLogAcknowledged = _PromShutdownLogAcknowledged_Object(
    (1, 3, 6, 1, 4, 1, 2167, 10, 4, 3),
    _PromShutdownLogAcknowledged_Type()
)
promShutdownLogAcknowledged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    promShutdownLogAcknowledged.setStatus("mandatory")
_PromEventShutdownLog_ObjectIdentity = ObjectIdentity
promEventShutdownLog = _PromEventShutdownLog_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2167, 10, 5)
)
_PromEventShutdownLogTable_Object = MibTable
promEventShutdownLogTable = _PromEventShutdownLogTable_Object(
    (1, 3, 6, 1, 4, 1, 2167, 10, 5, 1)
)
if mibBuilder.loadTexts:
    promEventShutdownLogTable.setStatus("mandatory")
_PromEventShutdownLogEntry_Object = MibTableRow
promEventShutdownLogEntry = _PromEventShutdownLogEntry_Object(
    (1, 3, 6, 1, 4, 1, 2167, 10, 5, 1, 1)
)
promEventShutdownLogEntry.setIndexNames(
    (0, "PROMINET-MIB", "promEventShutdownLogIndex"),
)
if mibBuilder.loadTexts:
    promEventShutdownLogEntry.setStatus("mandatory")


class _PromEventShutdownLogEventIndex_Type(Integer32):
    """Custom type promEventShutdownLogEventIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_PromEventShutdownLogEventIndex_Type.__name__ = "Integer32"
_PromEventShutdownLogEventIndex_Object = MibTableColumn
promEventShutdownLogEventIndex = _PromEventShutdownLogEventIndex_Object(
    (1, 3, 6, 1, 4, 1, 2167, 10, 5, 1, 1, 1),
    _PromEventShutdownLogEventIndex_Type()
)
promEventShutdownLogEventIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    promEventShutdownLogEventIndex.setStatus("mandatory")


class _PromEventShutdownLogIndex_Type(Integer32):
    """Custom type promEventShutdownLogIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_PromEventShutdownLogIndex_Type.__name__ = "Integer32"
_PromEventShutdownLogIndex_Object = MibTableColumn
promEventShutdownLogIndex = _PromEventShutdownLogIndex_Object(
    (1, 3, 6, 1, 4, 1, 2167, 10, 5, 1, 1, 2),
    _PromEventShutdownLogIndex_Type()
)
promEventShutdownLogIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    promEventShutdownLogIndex.setStatus("mandatory")
_PromEventShutdownLogTime_Type = TimeTicks
_PromEventShutdownLogTime_Object = MibTableColumn
promEventShutdownLogTime = _PromEventShutdownLogTime_Object(
    (1, 3, 6, 1, 4, 1, 2167, 10, 5, 1, 1, 3),
    _PromEventShutdownLogTime_Type()
)
promEventShutdownLogTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    promEventShutdownLogTime.setStatus("mandatory")


class _PromEventShutdownLogDescr_Type(DisplayString):
    """Custom type promEventShutdownLogDescr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_PromEventShutdownLogDescr_Type.__name__ = "DisplayString"
_PromEventShutdownLogDescr_Object = MibTableColumn
promEventShutdownLogDescr = _PromEventShutdownLogDescr_Object(
    (1, 3, 6, 1, 4, 1, 2167, 10, 5, 1, 1, 4),
    _PromEventShutdownLogDescr_Type()
)
promEventShutdownLogDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    promEventShutdownLogDescr.setStatus("mandatory")
_PromEventShutdownLogType_Type = EventCategory
_PromEventShutdownLogType_Object = MibTableColumn
promEventShutdownLogType = _PromEventShutdownLogType_Object(
    (1, 3, 6, 1, 4, 1, 2167, 10, 5, 1, 1, 5),
    _PromEventShutdownLogType_Type()
)
promEventShutdownLogType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    promEventShutdownLogType.setStatus("mandatory")


class _PromEventShutdownLogSeverity_Type(Integer32):
    """Custom type promEventShutdownLogSeverity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_PromEventShutdownLogSeverity_Type.__name__ = "Integer32"
_PromEventShutdownLogSeverity_Object = MibTableColumn
promEventShutdownLogSeverity = _PromEventShutdownLogSeverity_Object(
    (1, 3, 6, 1, 4, 1, 2167, 10, 5, 1, 1, 6),
    _PromEventShutdownLogSeverity_Type()
)
promEventShutdownLogSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    promEventShutdownLogSeverity.setStatus("mandatory")


class _PromEventShutdownLogDTM_Type(DisplayString):
    """Custom type promEventShutdownLogDTM based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(18, 18),
    )


_PromEventShutdownLogDTM_Type.__name__ = "DisplayString"
_PromEventShutdownLogDTM_Object = MibTableColumn
promEventShutdownLogDTM = _PromEventShutdownLogDTM_Object(
    (1, 3, 6, 1, 4, 1, 2167, 10, 5, 1, 1, 7),
    _PromEventShutdownLogDTM_Type()
)
promEventShutdownLogDTM.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    promEventShutdownLogDTM.setStatus("mandatory")
_PromEventShutdownLogResType_Type = ResourceType
_PromEventShutdownLogResType_Object = MibTableColumn
promEventShutdownLogResType = _PromEventShutdownLogResType_Object(
    (1, 3, 6, 1, 4, 1, 2167, 10, 5, 1, 1, 8),
    _PromEventShutdownLogResType_Type()
)
promEventShutdownLogResType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    promEventShutdownLogResType.setStatus("mandatory")
_PromEventShutdownLogResID_Type = ResourceId
_PromEventShutdownLogResID_Object = MibTableColumn
promEventShutdownLogResID = _PromEventShutdownLogResID_Object(
    (1, 3, 6, 1, 4, 1, 2167, 10, 5, 1, 1, 9),
    _PromEventShutdownLogResID_Type()
)
promEventShutdownLogResID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    promEventShutdownLogResID.setStatus("mandatory")
_PromEventShutdownLogResLeaf_Type = Integer32
_PromEventShutdownLogResLeaf_Object = MibTableColumn
promEventShutdownLogResLeaf = _PromEventShutdownLogResLeaf_Object(
    (1, 3, 6, 1, 4, 1, 2167, 10, 5, 1, 1, 10),
    _PromEventShutdownLogResLeaf_Type()
)
promEventShutdownLogResLeaf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    promEventShutdownLogResLeaf.setStatus("mandatory")
_PromEventShutdownLogValueType_Type = EventValueType
_PromEventShutdownLogValueType_Object = MibTableColumn
promEventShutdownLogValueType = _PromEventShutdownLogValueType_Object(
    (1, 3, 6, 1, 4, 1, 2167, 10, 5, 1, 1, 11),
    _PromEventShutdownLogValueType_Type()
)
promEventShutdownLogValueType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    promEventShutdownLogValueType.setStatus("mandatory")


class _PromEventShutdownLogValue_Type(OctetString):
    """Custom type promEventShutdownLogValue based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_PromEventShutdownLogValue_Type.__name__ = "OctetString"
_PromEventShutdownLogValue_Object = MibTableColumn
promEventShutdownLogValue = _PromEventShutdownLogValue_Object(
    (1, 3, 6, 1, 4, 1, 2167, 10, 5, 1, 1, 12),
    _PromEventShutdownLogValue_Type()
)
promEventShutdownLogValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    promEventShutdownLogValue.setStatus("mandatory")
_PromEventShutdownLogEpochTime_Type = Integer32
_PromEventShutdownLogEpochTime_Object = MibTableColumn
promEventShutdownLogEpochTime = _PromEventShutdownLogEpochTime_Object(
    (1, 3, 6, 1, 4, 1, 2167, 10, 5, 1, 1, 13),
    _PromEventShutdownLogEpochTime_Type()
)
promEventShutdownLogEpochTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    promEventShutdownLogEpochTime.setStatus("mandatory")


class _PromEventShutdownLogID_Type(Integer32):
    """Custom type promEventShutdownLogID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_PromEventShutdownLogID_Type.__name__ = "Integer32"
_PromEventShutdownLogID_Object = MibTableColumn
promEventShutdownLogID = _PromEventShutdownLogID_Object(
    (1, 3, 6, 1, 4, 1, 2167, 10, 5, 1, 1, 14),
    _PromEventShutdownLogID_Type()
)
promEventShutdownLogID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    promEventShutdownLogID.setStatus("mandatory")
_PromEventTrapMgmt_ObjectIdentity = ObjectIdentity
promEventTrapMgmt = _PromEventTrapMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2167, 10, 6)
)


class _PromEventTrapEventIndex_Type(Integer32):
    """Custom type promEventTrapEventIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_PromEventTrapEventIndex_Type.__name__ = "Integer32"
_PromEventTrapEventIndex_Object = MibScalar
promEventTrapEventIndex = _PromEventTrapEventIndex_Object(
    (1, 3, 6, 1, 4, 1, 2167, 10, 6, 1),
    _PromEventTrapEventIndex_Type()
)
promEventTrapEventIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    promEventTrapEventIndex.setStatus("mandatory")
_PromEventTrapTime_Type = TimeTicks
_PromEventTrapTime_Object = MibScalar
promEventTrapTime = _PromEventTrapTime_Object(
    (1, 3, 6, 1, 4, 1, 2167, 10, 6, 2),
    _PromEventTrapTime_Type()
)
promEventTrapTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    promEventTrapTime.setStatus("mandatory")


class _PromEventTrapDescr_Type(DisplayString):
    """Custom type promEventTrapDescr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_PromEventTrapDescr_Type.__name__ = "DisplayString"
_PromEventTrapDescr_Object = MibScalar
promEventTrapDescr = _PromEventTrapDescr_Object(
    (1, 3, 6, 1, 4, 1, 2167, 10, 6, 3),
    _PromEventTrapDescr_Type()
)
promEventTrapDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    promEventTrapDescr.setStatus("mandatory")
_PromEventTrapType_Type = EventCategory
_PromEventTrapType_Object = MibScalar
promEventTrapType = _PromEventTrapType_Object(
    (1, 3, 6, 1, 4, 1, 2167, 10, 6, 4),
    _PromEventTrapType_Type()
)
promEventTrapType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    promEventTrapType.setStatus("mandatory")


class _PromEventTrapSeverity_Type(Integer32):
    """Custom type promEventTrapSeverity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_PromEventTrapSeverity_Type.__name__ = "Integer32"
_PromEventTrapSeverity_Object = MibScalar
promEventTrapSeverity = _PromEventTrapSeverity_Object(
    (1, 3, 6, 1, 4, 1, 2167, 10, 6, 5),
    _PromEventTrapSeverity_Type()
)
promEventTrapSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    promEventTrapSeverity.setStatus("mandatory")


class _PromEventTrapDTM_Type(DisplayString):
    """Custom type promEventTrapDTM based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(18, 18),
    )


_PromEventTrapDTM_Type.__name__ = "DisplayString"
_PromEventTrapDTM_Object = MibScalar
promEventTrapDTM = _PromEventTrapDTM_Object(
    (1, 3, 6, 1, 4, 1, 2167, 10, 6, 6),
    _PromEventTrapDTM_Type()
)
promEventTrapDTM.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    promEventTrapDTM.setStatus("mandatory")
_PromEventTrapResType_Type = ResourceType
_PromEventTrapResType_Object = MibScalar
promEventTrapResType = _PromEventTrapResType_Object(
    (1, 3, 6, 1, 4, 1, 2167, 10, 6, 7),
    _PromEventTrapResType_Type()
)
promEventTrapResType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    promEventTrapResType.setStatus("mandatory")
_PromEventTrapResID_Type = ResourceId
_PromEventTrapResID_Object = MibScalar
promEventTrapResID = _PromEventTrapResID_Object(
    (1, 3, 6, 1, 4, 1, 2167, 10, 6, 8),
    _PromEventTrapResID_Type()
)
promEventTrapResID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    promEventTrapResID.setStatus("mandatory")
_PromEventTrapResLeaf_Type = Integer32
_PromEventTrapResLeaf_Object = MibScalar
promEventTrapResLeaf = _PromEventTrapResLeaf_Object(
    (1, 3, 6, 1, 4, 1, 2167, 10, 6, 9),
    _PromEventTrapResLeaf_Type()
)
promEventTrapResLeaf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    promEventTrapResLeaf.setStatus("mandatory")
_PromEventTrapValueType_Type = EventValueType
_PromEventTrapValueType_Object = MibScalar
promEventTrapValueType = _PromEventTrapValueType_Object(
    (1, 3, 6, 1, 4, 1, 2167, 10, 6, 10),
    _PromEventTrapValueType_Type()
)
promEventTrapValueType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    promEventTrapValueType.setStatus("mandatory")


class _PromEventTrapValue_Type(OctetString):
    """Custom type promEventTrapValue based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_PromEventTrapValue_Type.__name__ = "OctetString"
_PromEventTrapValue_Object = MibScalar
promEventTrapValue = _PromEventTrapValue_Object(
    (1, 3, 6, 1, 4, 1, 2167, 10, 6, 11),
    _PromEventTrapValue_Type()
)
promEventTrapValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    promEventTrapValue.setStatus("mandatory")
_PromEventTrapEpochTime_Type = Integer32
_PromEventTrapEpochTime_Object = MibScalar
promEventTrapEpochTime = _PromEventTrapEpochTime_Object(
    (1, 3, 6, 1, 4, 1, 2167, 10, 6, 12),
    _PromEventTrapEpochTime_Type()
)
promEventTrapEpochTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    promEventTrapEpochTime.setStatus("mandatory")


class _PromEventTrapID_Type(Integer32):
    """Custom type promEventTrapID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_PromEventTrapID_Type.__name__ = "Integer32"
_PromEventTrapID_Object = MibScalar
promEventTrapID = _PromEventTrapID_Object(
    (1, 3, 6, 1, 4, 1, 2167, 10, 6, 13),
    _PromEventTrapID_Type()
)
promEventTrapID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    promEventTrapID.setStatus("mandatory")
_PromAlarmMgt_ObjectIdentity = ObjectIdentity
promAlarmMgt = _PromAlarmMgt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2167, 11)
)
_PromAlarmGeneral_ObjectIdentity = ObjectIdentity
promAlarmGeneral = _PromAlarmGeneral_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2167, 11, 1)
)
_PromAlarmGeneralActiveEntries_Type = Gauge32
_PromAlarmGeneralActiveEntries_Object = MibScalar
promAlarmGeneralActiveEntries = _PromAlarmGeneralActiveEntries_Object(
    (1, 3, 6, 1, 4, 1, 2167, 11, 1, 1),
    _PromAlarmGeneralActiveEntries_Type()
)
promAlarmGeneralActiveEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    promAlarmGeneralActiveEntries.setStatus("mandatory")
_PromAlarmGeneralTimeStamp_Type = TimeTicks
_PromAlarmGeneralTimeStamp_Object = MibScalar
promAlarmGeneralTimeStamp = _PromAlarmGeneralTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 2167, 11, 1, 2),
    _PromAlarmGeneralTimeStamp_Type()
)
promAlarmGeneralTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    promAlarmGeneralTimeStamp.setStatus("mandatory")
_PromAlarms_ObjectIdentity = ObjectIdentity
promAlarms = _PromAlarms_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2167, 11, 2)
)
_PromActiveAlarmTable_Object = MibTable
promActiveAlarmTable = _PromActiveAlarmTable_Object(
    (1, 3, 6, 1, 4, 1, 2167, 11, 2, 2)
)
if mibBuilder.loadTexts:
    promActiveAlarmTable.setStatus("mandatory")
_PromActiveAlarmEntry_Object = MibTableRow
promActiveAlarmEntry = _PromActiveAlarmEntry_Object(
    (1, 3, 6, 1, 4, 1, 2167, 11, 2, 2, 1)
)
promActiveAlarmEntry.setIndexNames(
    (0, "PROMINET-MIB", "promActiveAlarmIndex"),
)
if mibBuilder.loadTexts:
    promActiveAlarmEntry.setStatus("mandatory")
_PromActiveAlarmIndex_Type = Integer32
_PromActiveAlarmIndex_Object = MibTableColumn
promActiveAlarmIndex = _PromActiveAlarmIndex_Object(
    (1, 3, 6, 1, 4, 1, 2167, 11, 2, 2, 1, 1),
    _PromActiveAlarmIndex_Type()
)
promActiveAlarmIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    promActiveAlarmIndex.setStatus("mandatory")


class _PromActiveAlarmName_Type(DisplayString):
    """Custom type promActiveAlarmName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_PromActiveAlarmName_Type.__name__ = "DisplayString"
_PromActiveAlarmName_Object = MibTableColumn
promActiveAlarmName = _PromActiveAlarmName_Object(
    (1, 3, 6, 1, 4, 1, 2167, 11, 2, 2, 1, 2),
    _PromActiveAlarmName_Type()
)
promActiveAlarmName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    promActiveAlarmName.setStatus("mandatory")
_PromActiveAlarmValueHigh_Type = Integer32
_PromActiveAlarmValueHigh_Object = MibTableColumn
promActiveAlarmValueHigh = _PromActiveAlarmValueHigh_Object(
    (1, 3, 6, 1, 4, 1, 2167, 11, 2, 2, 1, 3),
    _PromActiveAlarmValueHigh_Type()
)
promActiveAlarmValueHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    promActiveAlarmValueHigh.setStatus("mandatory")
_PromActiveAlarmValueLow_Type = Integer32
_PromActiveAlarmValueLow_Object = MibTableColumn
promActiveAlarmValueLow = _PromActiveAlarmValueLow_Object(
    (1, 3, 6, 1, 4, 1, 2167, 11, 2, 2, 1, 4),
    _PromActiveAlarmValueLow_Type()
)
promActiveAlarmValueLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    promActiveAlarmValueLow.setStatus("mandatory")
_PromActiveAlarmVariable_Type = ObjectIdentifier
_PromActiveAlarmVariable_Object = MibTableColumn
promActiveAlarmVariable = _PromActiveAlarmVariable_Object(
    (1, 3, 6, 1, 4, 1, 2167, 11, 2, 2, 1, 5),
    _PromActiveAlarmVariable_Type()
)
promActiveAlarmVariable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    promActiveAlarmVariable.setStatus("mandatory")
_PromActiveAlarmResType_Type = ResourceType
_PromActiveAlarmResType_Object = MibTableColumn
promActiveAlarmResType = _PromActiveAlarmResType_Object(
    (1, 3, 6, 1, 4, 1, 2167, 11, 2, 2, 1, 6),
    _PromActiveAlarmResType_Type()
)
promActiveAlarmResType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    promActiveAlarmResType.setStatus("mandatory")
_PromActiveAlarmResID_Type = ResourceId
_PromActiveAlarmResID_Object = MibTableColumn
promActiveAlarmResID = _PromActiveAlarmResID_Object(
    (1, 3, 6, 1, 4, 1, 2167, 11, 2, 2, 1, 7),
    _PromActiveAlarmResID_Type()
)
promActiveAlarmResID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    promActiveAlarmResID.setStatus("mandatory")
_PromActiveAlarmLeaf_Type = Integer32
_PromActiveAlarmLeaf_Object = MibTableColumn
promActiveAlarmLeaf = _PromActiveAlarmLeaf_Object(
    (1, 3, 6, 1, 4, 1, 2167, 11, 2, 2, 1, 8),
    _PromActiveAlarmLeaf_Type()
)
promActiveAlarmLeaf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    promActiveAlarmLeaf.setStatus("mandatory")


class _PromActiveAlarmOwner_Type(DisplayString):
    """Custom type promActiveAlarmOwner based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_PromActiveAlarmOwner_Type.__name__ = "DisplayString"
_PromActiveAlarmOwner_Object = MibTableColumn
promActiveAlarmOwner = _PromActiveAlarmOwner_Object(
    (1, 3, 6, 1, 4, 1, 2167, 11, 2, 2, 1, 9),
    _PromActiveAlarmOwner_Type()
)
promActiveAlarmOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    promActiveAlarmOwner.setStatus("mandatory")
_PromSnmpTraps_ObjectIdentity = ObjectIdentity
promSnmpTraps = _PromSnmpTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2167, 13)
)
_PromVtpSnooping_ObjectIdentity = ObjectIdentity
promVtpSnooping = _PromVtpSnooping_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2167, 14)
)
_PromVtpSnoopingSwitch_ObjectIdentity = ObjectIdentity
promVtpSnoopingSwitch = _PromVtpSnoopingSwitch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2167, 14, 1)
)


class _PromVtpSnoopingState_Type(Integer32):
    """Custom type promVtpSnoopingState based on Integer32"""
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


_PromVtpSnoopingState_Type.__name__ = "Integer32"
_PromVtpSnoopingState_Object = MibScalar
promVtpSnoopingState = _PromVtpSnoopingState_Object(
    (1, 3, 6, 1, 4, 1, 2167, 14, 1, 1),
    _PromVtpSnoopingState_Type()
)
promVtpSnoopingState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    promVtpSnoopingState.setStatus("mandatory")


class _PromVtpSnoopingDomainName_Type(DisplayString):
    """Custom type promVtpSnoopingDomainName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_PromVtpSnoopingDomainName_Type.__name__ = "DisplayString"
_PromVtpSnoopingDomainName_Object = MibScalar
promVtpSnoopingDomainName = _PromVtpSnoopingDomainName_Object(
    (1, 3, 6, 1, 4, 1, 2167, 14, 1, 2),
    _PromVtpSnoopingDomainName_Type()
)
promVtpSnoopingDomainName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    promVtpSnoopingDomainName.setStatus("mandatory")
_PromVtpSnoopingUpdaterId_Type = IpAddress
_PromVtpSnoopingUpdaterId_Object = MibScalar
promVtpSnoopingUpdaterId = _PromVtpSnoopingUpdaterId_Object(
    (1, 3, 6, 1, 4, 1, 2167, 14, 1, 3),
    _PromVtpSnoopingUpdaterId_Type()
)
promVtpSnoopingUpdaterId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    promVtpSnoopingUpdaterId.setStatus("mandatory")


class _PromVtpSnoopingUpdateTimeStamp_Type(DisplayString):
    """Custom type promVtpSnoopingUpdateTimeStamp based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 12),
    )


_PromVtpSnoopingUpdateTimeStamp_Type.__name__ = "DisplayString"
_PromVtpSnoopingUpdateTimeStamp_Object = MibScalar
promVtpSnoopingUpdateTimeStamp = _PromVtpSnoopingUpdateTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 2167, 14, 1, 4),
    _PromVtpSnoopingUpdateTimeStamp_Type()
)
promVtpSnoopingUpdateTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    promVtpSnoopingUpdateTimeStamp.setStatus("mandatory")
_PromVtpSnoopingConfigRevNum_Type = Integer32
_PromVtpSnoopingConfigRevNum_Object = MibScalar
promVtpSnoopingConfigRevNum = _PromVtpSnoopingConfigRevNum_Object(
    (1, 3, 6, 1, 4, 1, 2167, 14, 1, 5),
    _PromVtpSnoopingConfigRevNum_Type()
)
promVtpSnoopingConfigRevNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    promVtpSnoopingConfigRevNum.setStatus("mandatory")
_PromPortMgmt_ObjectIdentity = ObjectIdentity
promPortMgmt = _PromPortMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2167, 15)
)
_PromTCPPortMgmt_ObjectIdentity = ObjectIdentity
promTCPPortMgmt = _PromTCPPortMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2167, 15, 1)
)


class _PromTCPPortHTTP_Type(Integer32):
    """Custom type promTCPPortHTTP based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(80, 80),
        ValueRangeConstraint(9000, 65535),
    )


_PromTCPPortHTTP_Type.__name__ = "Integer32"
_PromTCPPortHTTP_Object = MibScalar
promTCPPortHTTP = _PromTCPPortHTTP_Object(
    (1, 3, 6, 1, 4, 1, 2167, 15, 1, 1),
    _PromTCPPortHTTP_Type()
)
promTCPPortHTTP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    promTCPPortHTTP.setStatus("mandatory")


class _PromTCPPortTelnet_Type(Integer32):
    """Custom type promTCPPortTelnet based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(23, 23),
        ValueRangeConstraint(9000, 65535),
    )


_PromTCPPortTelnet_Type.__name__ = "Integer32"
_PromTCPPortTelnet_Object = MibScalar
promTCPPortTelnet = _PromTCPPortTelnet_Object(
    (1, 3, 6, 1, 4, 1, 2167, 15, 1, 2),
    _PromTCPPortTelnet_Type()
)
promTCPPortTelnet.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    promTCPPortTelnet.setStatus("mandatory")

# Managed Objects groups


# Notification objects

promSystemTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2167, 13, 0, 2)
)
promSystemTrap.setObjects(
      *(("PROMINET-MIB", "promEventTrapEventIndex"),
        ("PROMINET-MIB", "promEventTrapTime"),
        ("PROMINET-MIB", "promEventTrapDescr"),
        ("PROMINET-MIB", "promEventTrapType"),
        ("PROMINET-MIB", "promEventTrapSeverity"),
        ("PROMINET-MIB", "promEventTrapDTM"),
        ("PROMINET-MIB", "promEventTrapResType"),
        ("PROMINET-MIB", "promEventTrapResID"),
        ("PROMINET-MIB", "promEventTrapResLeaf"),
        ("PROMINET-MIB", "promEventTrapValueType"),
        ("PROMINET-MIB", "promEventTrapValue"),
        ("PROMINET-MIB", "promEventTrapEpochTime"),
        ("PROMINET-MIB", "promEventTrapID"))
)
if mibBuilder.loadTexts:
    promSystemTrap.setStatus(
        ""
    )

promConfigurationTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2167, 13, 0, 3)
)
promConfigurationTrap.setObjects(
      *(("PROMINET-MIB", "promEventTrapEventIndex"),
        ("PROMINET-MIB", "promEventTrapTime"),
        ("PROMINET-MIB", "promEventTrapDescr"),
        ("PROMINET-MIB", "promEventTrapType"),
        ("PROMINET-MIB", "promEventTrapSeverity"),
        ("PROMINET-MIB", "promEventTrapDTM"),
        ("PROMINET-MIB", "promEventTrapResType"),
        ("PROMINET-MIB", "promEventTrapResID"),
        ("PROMINET-MIB", "promEventTrapResLeaf"),
        ("PROMINET-MIB", "promEventTrapValueType"),
        ("PROMINET-MIB", "promEventTrapValue"),
        ("PROMINET-MIB", "promEventTrapEpochTime"),
        ("PROMINET-MIB", "promEventTrapID"))
)
if mibBuilder.loadTexts:
    promConfigurationTrap.setStatus(
        ""
    )

promTemperatureTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2167, 13, 0, 4)
)
promTemperatureTrap.setObjects(
      *(("PROMINET-MIB", "promEventTrapEventIndex"),
        ("PROMINET-MIB", "promEventTrapTime"),
        ("PROMINET-MIB", "promEventTrapDescr"),
        ("PROMINET-MIB", "promEventTrapType"),
        ("PROMINET-MIB", "promEventTrapSeverity"),
        ("PROMINET-MIB", "promEventTrapDTM"),
        ("PROMINET-MIB", "promEventTrapResType"),
        ("PROMINET-MIB", "promEventTrapResID"),
        ("PROMINET-MIB", "promEventTrapResLeaf"),
        ("PROMINET-MIB", "promEventTrapValueType"),
        ("PROMINET-MIB", "promEventTrapValue"),
        ("PROMINET-MIB", "promEventTrapEpochTime"),
        ("PROMINET-MIB", "promEventTrapID"))
)
if mibBuilder.loadTexts:
    promTemperatureTrap.setStatus(
        ""
    )

promResourceTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2167, 13, 0, 5)
)
promResourceTrap.setObjects(
      *(("PROMINET-MIB", "promEventTrapEventIndex"),
        ("PROMINET-MIB", "promEventTrapTime"),
        ("PROMINET-MIB", "promEventTrapDescr"),
        ("PROMINET-MIB", "promEventTrapType"),
        ("PROMINET-MIB", "promEventTrapSeverity"),
        ("PROMINET-MIB", "promEventTrapDTM"),
        ("PROMINET-MIB", "promEventTrapResType"),
        ("PROMINET-MIB", "promEventTrapResID"),
        ("PROMINET-MIB", "promEventTrapResLeaf"),
        ("PROMINET-MIB", "promEventTrapValueType"),
        ("PROMINET-MIB", "promEventTrapValue"),
        ("PROMINET-MIB", "promEventTrapEpochTime"),
        ("PROMINET-MIB", "promEventTrapID"))
)
if mibBuilder.loadTexts:
    promResourceTrap.setStatus(
        ""
    )

promFanTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2167, 13, 0, 6)
)
promFanTrap.setObjects(
      *(("PROMINET-MIB", "promEventTrapEventIndex"),
        ("PROMINET-MIB", "promEventTrapTime"),
        ("PROMINET-MIB", "promEventTrapDescr"),
        ("PROMINET-MIB", "promEventTrapType"),
        ("PROMINET-MIB", "promEventTrapSeverity"),
        ("PROMINET-MIB", "promEventTrapDTM"),
        ("PROMINET-MIB", "promEventTrapResType"),
        ("PROMINET-MIB", "promEventTrapResID"),
        ("PROMINET-MIB", "promEventTrapResLeaf"),
        ("PROMINET-MIB", "promEventTrapValueType"),
        ("PROMINET-MIB", "promEventTrapValue"),
        ("PROMINET-MIB", "promEventTrapEpochTime"),
        ("PROMINET-MIB", "promEventTrapID"))
)
if mibBuilder.loadTexts:
    promFanTrap.setStatus(
        ""
    )

promPowerTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2167, 13, 0, 9)
)
promPowerTrap.setObjects(
      *(("PROMINET-MIB", "promEventTrapEventIndex"),
        ("PROMINET-MIB", "promEventTrapTime"),
        ("PROMINET-MIB", "promEventTrapDescr"),
        ("PROMINET-MIB", "promEventTrapType"),
        ("PROMINET-MIB", "promEventTrapSeverity"),
        ("PROMINET-MIB", "promEventTrapDTM"),
        ("PROMINET-MIB", "promEventTrapResType"),
        ("PROMINET-MIB", "promEventTrapResID"),
        ("PROMINET-MIB", "promEventTrapResLeaf"),
        ("PROMINET-MIB", "promEventTrapValueType"),
        ("PROMINET-MIB", "promEventTrapValue"),
        ("PROMINET-MIB", "promEventTrapEpochTime"),
        ("PROMINET-MIB", "promEventTrapID"))
)
if mibBuilder.loadTexts:
    promPowerTrap.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "PROMINET-MIB",
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
       "ods": ods,
       "odsTPS": odsTPS,
       "odsLANBlazer": odsLANBlazer,
       "odsLANBlazerMibs": odsLANBlazerMibs,
       "odsLANBlazer7000Mib": odsLANBlazer7000Mib,
       "intel": intel,
       "mib2ext": mib2ext,
       "esGigaSwitch": esGigaSwitch,
       "marconi": marconi,
       "ethernetL3": ethernetL3,
       "esrSwitch": esrSwitch,
       "prominet": prominet,
       "promAgent": promAgent,
       "promAgentGen": promAgentGen,
       "promAgentMIBVersion": promAgentMIBVersion,
       "promAgentMgrIndex": promAgentMgrIndex,
       "promAgentCommunity": promAgentCommunity,
       "promCommunityTable": promCommunityTable,
       "promCommunityEntry": promCommunityEntry,
       "promCommunityIndex": promCommunityIndex,
       "promCommunityString": promCommunityString,
       "promCommunityAddressType": promCommunityAddressType,
       "promCommunityAddress": promCommunityAddress,
       "promCommunityAccess": promCommunityAccess,
       "promCommunityTrapReceiver": promCommunityTrapReceiver,
       "promCommunitySecurityLevel": promCommunitySecurityLevel,
       "promCommunityStatus": promCommunityStatus,
       "promAgentWeb": promAgentWeb,
       "promAgentWebServerURL": promAgentWebServerURL,
       "promAgentWebServerHelpDirectory": promAgentWebServerHelpDirectory,
       "promChassis": promChassis,
       "promChassisGen": promChassisGen,
       "promChassisType": promChassisType,
       "promChassisSlots": promChassisSlots,
       "promChassisSystemReset": promChassisSystemReset,
       "promInventory": promInventory,
       "promInventoryTable": promInventoryTable,
       "promInventoryEntry": promInventoryEntry,
       "promInventoryResourceType": promInventoryResourceType,
       "promInventoryResourceIndex": promInventoryResourceIndex,
       "promInventoryModelNumber": promInventoryModelNumber,
       "promInventorySerialNumber": promInventorySerialNumber,
       "promInventoryVersion": promInventoryVersion,
       "promInventoryManufactureInfo": promInventoryManufactureInfo,
       "promInventoryScratchPad": promInventoryScratchPad,
       "promInventoryPowerConsumption": promInventoryPowerConsumption,
       "promPowerSystems": promPowerSystems,
       "promPowerSupplies": promPowerSupplies,
       "promPowerSupplyTable": promPowerSupplyTable,
       "promPowerSupplyEntry": promPowerSupplyEntry,
       "promPowerSupplyIndex": promPowerSupplyIndex,
       "promPowerSupplyType": promPowerSupplyType,
       "promPowerSupplyStatus": promPowerSupplyStatus,
       "promPowerSupplyInputStatus": promPowerSupplyInputStatus,
       "promPowerSupplyOutputStatus": promPowerSupplyOutputStatus,
       "promPowerSupplyOutputCapacity": promPowerSupplyOutputCapacity,
       "promPowerMgmtGen": promPowerMgmtGen,
       "promPowerCapacity": promPowerCapacity,
       "promPowerUsed": promPowerUsed,
       "promPowerMgmtCtl": promPowerMgmtCtl,
       "promPowerControlTable": promPowerControlTable,
       "promPowerControlEntry": promPowerControlEntry,
       "promPowerControlUsed": promPowerControlUsed,
       "promPowerControlPriority": promPowerControlPriority,
       "promPowerControlMode": promPowerControlMode,
       "promTemperature": promTemperature,
       "promTempTable": promTempTable,
       "promTempEntry": promTempEntry,
       "promTempIndex": promTempIndex,
       "promTempValue": promTempValue,
       "promTempUpperLimit": promTempUpperLimit,
       "promTempUpperWarning": promTempUpperWarning,
       "promTempLowerWarning": promTempLowerWarning,
       "promTempLowerLimit": promTempLowerLimit,
       "promModules": promModules,
       "promModuleTable": promModuleTable,
       "promModuleEntry": promModuleEntry,
       "promModuleIndex": promModuleIndex,
       "promModuleName": promModuleName,
       "promModuleType": promModuleType,
       "promModuleBaseType": promModuleBaseType,
       "promModuleSlotWidth": promModuleSlotWidth,
       "promModuleSlotOffset": promModuleSlotOffset,
       "promModulePorts": promModulePorts,
       "promModuleUpdateTime": promModuleUpdateTime,
       "promModuleUpdateList": promModuleUpdateList,
       "promPorts": promPorts,
       "promPortMgt": promPortMgt,
       "promPortTable": promPortTable,
       "promPortEntry": promPortEntry,
       "promPortIndex": promPortIndex,
       "promPortName": promPortName,
       "promPortType": promPortType,
       "promPortBaseType": promPortBaseType,
       "promPortMode": promPortMode,
       "promPortStatus": promPortStatus,
       "promPortConnector": promPortConnector,
       "promPortSpeedState": promPortSpeedState,
       "promPortDuplexState": promPortDuplexState,
       "promPortGroupBinding": promPortGroupBinding,
       "promPortFlowControlState": promPortFlowControlState,
       "promPortFlowControlMgt": promPortFlowControlMgt,
       "promPortFlowControlTable": promPortFlowControlTable,
       "promPortFlowControlEntry": promPortFlowControlEntry,
       "promPortFlowControlMode": promPortFlowControlMode,
       "promPortDuplexMgt": promPortDuplexMgt,
       "promPortDuplexTable": promPortDuplexTable,
       "promPortDuplexEntry": promPortDuplexEntry,
       "promPortDuplexMode": promPortDuplexMode,
       "promPortSpeedMgt": promPortSpeedMgt,
       "promPortSpeedTable": promPortSpeedTable,
       "promPortSpeedEntry": promPortSpeedEntry,
       "promPortSpeedMode": promPortSpeedMode,
       "promPortAutoNegotiationMgt": promPortAutoNegotiationMgt,
       "promPortAutoNegotiationTable": promPortAutoNegotiationTable,
       "promPortAutoNegotiationEntry": promPortAutoNegotiationEntry,
       "promPortAutoNegotiationMode": promPortAutoNegotiationMode,
       "promPortAutoNegotiationSpeedAdvertisement": promPortAutoNegotiationSpeedAdvertisement,
       "promPortAutoNegotiationDuplexAdvertisement": promPortAutoNegotiationDuplexAdvertisement,
       "promPortAutoNegotiationFlowControlAdvertisement": promPortAutoNegotiationFlowControlAdvertisement,
       "promPortRateLimitMgt": promPortRateLimitMgt,
       "promPortRateLimitTable": promPortRateLimitTable,
       "promPortRateLimitEntry": promPortRateLimitEntry,
       "promPortRateLimitMode": promPortRateLimitMode,
       "promPortRateLimitRate": promPortRateLimitRate,
       "promPortRateLimitBurstSize": promPortRateLimitBurstSize,
       "promPortPacePriorityMgt": promPortPacePriorityMgt,
       "promPortPacePriorityTable": promPortPacePriorityTable,
       "promPortPacePriorityEntry": promPortPacePriorityEntry,
       "promPortPacePriorityMode": promPortPacePriorityMode,
       "promPortCategoryMgt": promPortCategoryMgt,
       "promPortCategoryTable": promPortCategoryTable,
       "promPortCategoryEntry": promPortCategoryEntry,
       "promPortCategoryMode": promPortCategoryMode,
       "promPortRemoteFaultMgt": promPortRemoteFaultMgt,
       "promPortRemoteFaultTable": promPortRemoteFaultTable,
       "promPortRemoteFaultEntry": promPortRemoteFaultEntry,
       "promPortRemoteFaultDetect": promPortRemoteFaultDetect,
       "promBufferMgt": promBufferMgt,
       "promBufferTable": promBufferTable,
       "promBufferEntry": promBufferEntry,
       "promBufferIndex": promBufferIndex,
       "promBufferFabricPort": promBufferFabricPort,
       "promBufferFabricPortDirection": promBufferFabricPortDirection,
       "promBufferSwitchPort": promBufferSwitchPort,
       "promBufferMemory": promBufferMemory,
       "promBufferAgeTimer": promBufferAgeTimer,
       "promBufferPriorityServicing": promBufferPriorityServicing,
       "promBufferPriorityAllocation": promBufferPriorityAllocation,
       "promBufferPriorityThreshold": promBufferPriorityThreshold,
       "promBufferCongestion": promBufferCongestion,
       "promBufferHighOverflowDrops": promBufferHighOverflowDrops,
       "promBufferLowOverflowDrops": promBufferLowOverflowDrops,
       "promBufferHighStaleDrops": promBufferHighStaleDrops,
       "promBufferLowStaleDrops": promBufferLowStaleDrops,
       "promBufferCongestionDrops": promBufferCongestionDrops,
       "promSwitching": promSwitching,
       "promSwitchingLayerII": promSwitchingLayerII,
       "promSwitchGen": promSwitchGen,
       "promSwitchSTPConfig": promSwitchSTPConfig,
       "promSwitchAgingTime": promSwitchAgingTime,
       "promSwitchSuperAgingTime": promSwitchSuperAgingTime,
       "promBridgeMgmt": promBridgeMgmt,
       "promBridgeTable": promBridgeTable,
       "promBridgeEntry": promBridgeEntry,
       "promBridgeIndex": promBridgeIndex,
       "promBridgeType": promBridgeType,
       "promBridgeMode": promBridgeMode,
       "promBridgeStatus": promBridgeStatus,
       "promBridgeStpPriority": promBridgeStpPriority,
       "promBridgeStpTimeSinceTopologyChange": promBridgeStpTimeSinceTopologyChange,
       "promBridgeStpTopChanges": promBridgeStpTopChanges,
       "promBridgeStpDesignatedRoot": promBridgeStpDesignatedRoot,
       "promBridgeStpRootCost": promBridgeStpRootCost,
       "promBridgeStpRootPort": promBridgeStpRootPort,
       "promBridgeStpMaxAge": promBridgeStpMaxAge,
       "promBridgeStpHelloTime": promBridgeStpHelloTime,
       "promBridgeStpHoldTime": promBridgeStpHoldTime,
       "promBridgeStpForwardDelay": promBridgeStpForwardDelay,
       "promBridgeStpBridgeMaxAge": promBridgeStpBridgeMaxAge,
       "promBridgeStpBridgeHelloTime": promBridgeStpBridgeHelloTime,
       "promBridgeStpBridgeForwardDelay": promBridgeStpBridgeForwardDelay,
       "promBridgePortMgmt": promBridgePortMgmt,
       "promBridgePortTable": promBridgePortTable,
       "promBridgePortEntry": promBridgePortEntry,
       "promBridgePortIndex": promBridgePortIndex,
       "promBridgePortPriority": promBridgePortPriority,
       "promBridgePortState": promBridgePortState,
       "promBridgePortEnable": promBridgePortEnable,
       "promBridgePortPathCost": promBridgePortPathCost,
       "promBridgePortDesignatedRoot": promBridgePortDesignatedRoot,
       "promBridgePortDesignatedCost": promBridgePortDesignatedCost,
       "promBridgePortDesignatedBridge": promBridgePortDesignatedBridge,
       "promBridgePortDesignatedPort": promBridgePortDesignatedPort,
       "promBridgePortForwardTransitions": promBridgePortForwardTransitions,
       "promBridgePortFastStart": promBridgePortFastStart,
       "promBridgePortSetDefault": promBridgePortSetDefault,
       "promBridgePortEnableChangeDetection": promBridgePortEnableChangeDetection,
       "promL2AddrMgmt": promL2AddrMgmt,
       "promL2AddrDatabaseMgt": promL2AddrDatabaseMgt,
       "promL2AddressTable": promL2AddressTable,
       "promL2AddressEntry": promL2AddressEntry,
       "promL2AddressIndex": promL2AddressIndex,
       "promL2AddressTableIndex": promL2AddressTableIndex,
       "promL2AddressMacAddress": promL2AddressMacAddress,
       "promL2AddressPortBinding": promL2AddressPortBinding,
       "promL2AddressBindingValid": promL2AddressBindingValid,
       "promL2AddressVlanID": promL2AddressVlanID,
       "promL2AddressPriority": promL2AddressPriority,
       "promL2AddressForward": promL2AddressForward,
       "promL2AddressCopy": promL2AddressCopy,
       "promL2AddressPersistence": promL2AddressPersistence,
       "promL2AddressStatus": promL2AddressStatus,
       "promL2AddrSummaryMgt": promL2AddrSummaryMgt,
       "promL2AddrSummaryTable": promL2AddrSummaryTable,
       "promL2AddrSummaryEntry": promL2AddrSummaryEntry,
       "promL2AddrSummary": promL2AddrSummary,
       "promL2AddrControlMgt": promL2AddrControlMgt,
       "promL2AddressControlTable": promL2AddressControlTable,
       "promL2AddressControlEntry": promL2AddressControlEntry,
       "promL2AddressControlIndex": promL2AddressControlIndex,
       "promL2AddressControlMacAddress": promL2AddressControlMacAddress,
       "promL2AddressControlPortBinding": promL2AddressControlPortBinding,
       "promL2AddressControlVlanID": promL2AddressControlVlanID,
       "promL2AddressControlPriority": promL2AddressControlPriority,
       "promL2AddressControlPersistence": promL2AddressControlPersistence,
       "promL2AddressControlStatus": promL2AddressControlStatus,
       "promL2AddrChangeMgt": promL2AddrChangeMgt,
       "promL2AddressChangeLast": promL2AddressChangeLast,
       "promL2AddressChangeWraps": promL2AddressChangeWraps,
       "promL2AddressChangeMaxEntries": promL2AddressChangeMaxEntries,
       "promL2AddressChangeTable": promL2AddressChangeTable,
       "promL2AddressChangeEntry": promL2AddressChangeEntry,
       "promL2AddressChangeWrapCount": promL2AddressChangeWrapCount,
       "promL2AddressChangeIndex": promL2AddressChangeIndex,
       "promL2AddressChangeIndexChanged": promL2AddressChangeIndexChanged,
       "promL2AddressChangeSummary": promL2AddressChangeSummary,
       "promSwitchPortMgt": promSwitchPortMgt,
       "promSwitchPortTable": promSwitchPortTable,
       "promSwitchPortEntry": promSwitchPortEntry,
       "promSwitchPortIndex": promSwitchPortIndex,
       "promSwitchPortSTAPMode": promSwitchPortSTAPMode,
       "promSwitchPortConvertToStatic": promSwitchPortConvertToStatic,
       "promSwitchPortLearningMode": promSwitchPortLearningMode,
       "promSwitchPortHuntGroup": promSwitchPortHuntGroup,
       "promSwitchPortPhysicalPort": promSwitchPortPhysicalPort,
       "promSwitchPortKnownMode": promSwitchPortKnownMode,
       "promSwitchPortMappingMethod": promSwitchPortMappingMethod,
       "promSwitchPortTrunkingMode": promSwitchPortTrunkingMode,
       "promSwitchPortVlanBindingMethod": promSwitchPortVlanBindingMethod,
       "promSwitchPortIgnoreTag": promSwitchPortIgnoreTag,
       "promSwitchPortVlanID": promSwitchPortVlanID,
       "promSwitchPort3ComMappingTableIndex": promSwitchPort3ComMappingTableIndex,
       "promSwitchPortAutoVlanCreation": promSwitchPortAutoVlanCreation,
       "promSwitchPortMirrorMode": promSwitchPortMirrorMode,
       "promSwitchPortIfIndex": promSwitchPortIfIndex,
       "promSwitchPortFastStart": promSwitchPortFastStart,
       "promSwitchPortVtpSnooping": promSwitchPortVtpSnooping,
       "promSwitchPortIntrusionTrap": promSwitchPortIntrusionTrap,
       "promSwitchPortIntrusionTrapTimer": promSwitchPortIntrusionTrapTimer,
       "promHuntGroupMgt": promHuntGroupMgt,
       "promHuntGroupTable": promHuntGroupTable,
       "promHuntGroupEntry": promHuntGroupEntry,
       "promHuntGroupIndex": promHuntGroupIndex,
       "promHuntGroupName": promHuntGroupName,
       "promHuntGroupBasePort": promHuntGroupBasePort,
       "promHuntGroupNumberOfPorts": promHuntGroupNumberOfPorts,
       "promHuntGroupLoadSharing": promHuntGroupLoadSharing,
       "promHuntGroupStatus": promHuntGroupStatus,
       "promPortMirroringMgt": promPortMirroringMgt,
       "promPortMirroringTable": promPortMirroringTable,
       "promPortMirroringEntry": promPortMirroringEntry,
       "promPortMirroringIndex": promPortMirroringIndex,
       "promPortMirroringSourceSubPort": promPortMirroringSourceSubPort,
       "promPortMirroringSamplerType": promPortMirroringSamplerType,
       "promPortMirroringRate": promPortMirroringRate,
       "promPortMirroringMirrorPort": promPortMirroringMirrorPort,
       "promVlanMgt": promVlanMgt,
       "promVlans": promVlans,
       "promVlanTable": promVlanTable,
       "promVlanEntry": promVlanEntry,
       "promVlanID": promVlanID,
       "promVlanName": promVlanName,
       "promVlanIfIndex": promVlanIfIndex,
       "promVlanAFTIndex": promVlanAFTIndex,
       "promVlanBridgeIndex": promVlanBridgeIndex,
       "promVlanStatus": promVlanStatus,
       "promVlanInitialHashTableSize": promVlanInitialHashTableSize,
       "promVlanAutoIncrementHTSize": promVlanAutoIncrementHTSize,
       "promVlanLearnStatus": promVlanLearnStatus,
       "promVlanMappings": promVlanMappings,
       "prom3ComMapping": prom3ComMapping,
       "prom3ComMappingTable": prom3ComMappingTable,
       "prom3ComMappingEntry": prom3ComMappingEntry,
       "prom3ComMappingTableIndex": prom3ComMappingTableIndex,
       "prom3ComMappingTableName": prom3ComMappingTableName,
       "prom3ComMappingTableStatus": prom3ComMappingTableStatus,
       "promVlan3ComMapping": promVlan3ComMapping,
       "promVlan3ComMappingTable": promVlan3ComMappingTable,
       "promVlan3ComMappingEntry": promVlan3ComMappingEntry,
       "promVlan3ComMappingIndex": promVlan3ComMappingIndex,
       "promVlan3ComMappingVlanID": promVlan3ComMappingVlanID,
       "promVlan3ComMappingStatus": promVlan3ComMappingStatus,
       "promVirtualPorts": promVirtualPorts,
       "promVirtualSwitchPortTable": promVirtualSwitchPortTable,
       "promVirtualSwitchPortEntry": promVirtualSwitchPortEntry,
       "promVirtualSwitchPortIndex": promVirtualSwitchPortIndex,
       "promVirtualSwitchPortFormat": promVirtualSwitchPortFormat,
       "promVirtualSwitchPortBridgePort": promVirtualSwitchPortBridgePort,
       "promVirtualSwitchPortBindingType": promVirtualSwitchPortBindingType,
       "promVirtualSwitchPortStatus": promVirtualSwitchPortStatus,
       "promVirtualModulePortTable": promVirtualModulePortTable,
       "promVirtualModulePortEntry": promVirtualModulePortEntry,
       "promVirtualModulePortIndex": promVirtualModulePortIndex,
       "promVirtualModulePortFormat": promVirtualModulePortFormat,
       "promVirtualModulePortBridgePort": promVirtualModulePortBridgePort,
       "promVirtualModulePortBindingType": promVirtualModulePortBindingType,
       "promVirtualModulePortModuleName": promVirtualModulePortModuleName,
       "promVirtualModulePortPortName": promVirtualModulePortPortName,
       "promEvents": promEvents,
       "promEventMgt": promEventMgt,
       "promEventTable": promEventTable,
       "promEventEntry": promEventEntry,
       "promEventIndex": promEventIndex,
       "promEventMode": promEventMode,
       "promEventLogAction": promEventLogAction,
       "promEventTrapAction": promEventTrapAction,
       "promEventConsoleAction": promEventConsoleAction,
       "promEventLogMgt": promEventLogMgt,
       "promLogTableMaxSize": promLogTableMaxSize,
       "promLogLastEntry": promLogLastEntry,
       "promLogWraps": promLogWraps,
       "promEventLog": promEventLog,
       "promEventLogTable": promEventLogTable,
       "promEventLogEntry": promEventLogEntry,
       "promEventLogEventIndex": promEventLogEventIndex,
       "promEventLogIndex": promEventLogIndex,
       "promEventLogTime": promEventLogTime,
       "promEventLogDescr": promEventLogDescr,
       "promEventLogType": promEventLogType,
       "promEventLogSeverity": promEventLogSeverity,
       "promEventLogDTM": promEventLogDTM,
       "promEventLogResType": promEventLogResType,
       "promEventLogResID": promEventLogResID,
       "promEventLogResLeaf": promEventLogResLeaf,
       "promEventLogValueType": promEventLogValueType,
       "promEventLogValue": promEventLogValue,
       "promEventLogEpochTime": promEventLogEpochTime,
       "promEventLogID": promEventLogID,
       "promShutdownLogMgt": promShutdownLogMgt,
       "promShutdownLogTableMaxSize": promShutdownLogTableMaxSize,
       "promShutdownLogLastEntry": promShutdownLogLastEntry,
       "promShutdownLogAcknowledged": promShutdownLogAcknowledged,
       "promEventShutdownLog": promEventShutdownLog,
       "promEventShutdownLogTable": promEventShutdownLogTable,
       "promEventShutdownLogEntry": promEventShutdownLogEntry,
       "promEventShutdownLogEventIndex": promEventShutdownLogEventIndex,
       "promEventShutdownLogIndex": promEventShutdownLogIndex,
       "promEventShutdownLogTime": promEventShutdownLogTime,
       "promEventShutdownLogDescr": promEventShutdownLogDescr,
       "promEventShutdownLogType": promEventShutdownLogType,
       "promEventShutdownLogSeverity": promEventShutdownLogSeverity,
       "promEventShutdownLogDTM": promEventShutdownLogDTM,
       "promEventShutdownLogResType": promEventShutdownLogResType,
       "promEventShutdownLogResID": promEventShutdownLogResID,
       "promEventShutdownLogResLeaf": promEventShutdownLogResLeaf,
       "promEventShutdownLogValueType": promEventShutdownLogValueType,
       "promEventShutdownLogValue": promEventShutdownLogValue,
       "promEventShutdownLogEpochTime": promEventShutdownLogEpochTime,
       "promEventShutdownLogID": promEventShutdownLogID,
       "promEventTrapMgmt": promEventTrapMgmt,
       "promEventTrapEventIndex": promEventTrapEventIndex,
       "promEventTrapTime": promEventTrapTime,
       "promEventTrapDescr": promEventTrapDescr,
       "promEventTrapType": promEventTrapType,
       "promEventTrapSeverity": promEventTrapSeverity,
       "promEventTrapDTM": promEventTrapDTM,
       "promEventTrapResType": promEventTrapResType,
       "promEventTrapResID": promEventTrapResID,
       "promEventTrapResLeaf": promEventTrapResLeaf,
       "promEventTrapValueType": promEventTrapValueType,
       "promEventTrapValue": promEventTrapValue,
       "promEventTrapEpochTime": promEventTrapEpochTime,
       "promEventTrapID": promEventTrapID,
       "promAlarmMgt": promAlarmMgt,
       "promAlarmGeneral": promAlarmGeneral,
       "promAlarmGeneralActiveEntries": promAlarmGeneralActiveEntries,
       "promAlarmGeneralTimeStamp": promAlarmGeneralTimeStamp,
       "promAlarms": promAlarms,
       "promActiveAlarmTable": promActiveAlarmTable,
       "promActiveAlarmEntry": promActiveAlarmEntry,
       "promActiveAlarmIndex": promActiveAlarmIndex,
       "promActiveAlarmName": promActiveAlarmName,
       "promActiveAlarmValueHigh": promActiveAlarmValueHigh,
       "promActiveAlarmValueLow": promActiveAlarmValueLow,
       "promActiveAlarmVariable": promActiveAlarmVariable,
       "promActiveAlarmResType": promActiveAlarmResType,
       "promActiveAlarmResID": promActiveAlarmResID,
       "promActiveAlarmLeaf": promActiveAlarmLeaf,
       "promActiveAlarmOwner": promActiveAlarmOwner,
       "promSnmpTraps": promSnmpTraps,
       "promSystemTrap": promSystemTrap,
       "promConfigurationTrap": promConfigurationTrap,
       "promTemperatureTrap": promTemperatureTrap,
       "promResourceTrap": promResourceTrap,
       "promFanTrap": promFanTrap,
       "promPowerTrap": promPowerTrap,
       "promVtpSnooping": promVtpSnooping,
       "promVtpSnoopingSwitch": promVtpSnoopingSwitch,
       "promVtpSnoopingState": promVtpSnoopingState,
       "promVtpSnoopingDomainName": promVtpSnoopingDomainName,
       "promVtpSnoopingUpdaterId": promVtpSnoopingUpdaterId,
       "promVtpSnoopingUpdateTimeStamp": promVtpSnoopingUpdateTimeStamp,
       "promVtpSnoopingConfigRevNum": promVtpSnoopingConfigRevNum,
       "promPortMgmt": promPortMgmt,
       "promTCPPortMgmt": promTCPPortMgmt,
       "promTCPPortHTTP": promTCPPortHTTP,
       "promTCPPortTelnet": promTCPPortTelnet}
)
