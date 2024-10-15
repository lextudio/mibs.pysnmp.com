# SNMP MIB module (IEEE8021-PBB-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/IEEE8021-PBB-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:08:25 2024
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

(ieee8021BridgeBasePort,
 ieee8021BridgeBasePortComponentId) = mibBuilder.importSymbols(
    "IEEE8021-BRIDGE-MIB",
    "ieee8021BridgeBasePort",
    "ieee8021BridgeBasePortComponentId")

(IEEE8021BridgePortNumber,
 IEEE8021PbbComponentIdentifier,
 IEEE8021PbbIngressEgress,
 IEEE8021PbbServiceIdentifier,
 IEEE8021PbbServiceIdentifierOrUnassigned,
 IEEE8021PriorityCodePoint,
 IEEE8021PriorityValue,
 ieee802dot1mibs) = mibBuilder.importSymbols(
    "IEEE8021-TC-MIB",
    "IEEE8021BridgePortNumber",
    "IEEE8021PbbComponentIdentifier",
    "IEEE8021PbbIngressEgress",
    "IEEE8021PbbServiceIdentifier",
    "IEEE8021PbbServiceIdentifierOrUnassigned",
    "IEEE8021PriorityCodePoint",
    "IEEE8021PriorityValue",
    "ieee802dot1mibs")

(InterfaceIndex,
 InterfaceIndexOrZero) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex",
    "InterfaceIndexOrZero")

(VlanId,) = mibBuilder.importSymbols(
    "Q-BRIDGE-MIB",
    "VlanId")

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
 StorageType,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "RowStatus",
    "StorageType",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

ieee8021PbbMib = ModuleIdentity(
    (1, 3, 111, 2, 802, 1, 1, 9)
)
ieee8021PbbMib.setRevisions(
        ("2018-06-28 00:00",
         "2014-12-15 00:00",
         "2011-02-27 00:00",
         "2008-11-18 00:00",
         "2008-10-15 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Ieee8021PbbNotifications_ObjectIdentity = ObjectIdentity
ieee8021PbbNotifications = _Ieee8021PbbNotifications_ObjectIdentity(
    (1, 3, 111, 2, 802, 1, 1, 9, 0)
)
_Ieee8021PbbObjects_ObjectIdentity = ObjectIdentity
ieee8021PbbObjects = _Ieee8021PbbObjects_ObjectIdentity(
    (1, 3, 111, 2, 802, 1, 1, 9, 1)
)
_Ieee8021PbbProviderBackboneBridge_ObjectIdentity = ObjectIdentity
ieee8021PbbProviderBackboneBridge = _Ieee8021PbbProviderBackboneBridge_ObjectIdentity(
    (1, 3, 111, 2, 802, 1, 1, 9, 1, 1)
)
_Ieee8021PbbBackboneEdgeBridgeObjects_ObjectIdentity = ObjectIdentity
ieee8021PbbBackboneEdgeBridgeObjects = _Ieee8021PbbBackboneEdgeBridgeObjects_ObjectIdentity(
    (1, 3, 111, 2, 802, 1, 1, 9, 1, 1, 1)
)
_Ieee8021PbbBackboneEdgeBridgeAddress_Type = MacAddress
_Ieee8021PbbBackboneEdgeBridgeAddress_Object = MibScalar
ieee8021PbbBackboneEdgeBridgeAddress = _Ieee8021PbbBackboneEdgeBridgeAddress_Object(
    (1, 3, 111, 2, 802, 1, 1, 9, 1, 1, 1, 1),
    _Ieee8021PbbBackboneEdgeBridgeAddress_Type()
)
ieee8021PbbBackboneEdgeBridgeAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021PbbBackboneEdgeBridgeAddress.setStatus("current")


class _Ieee8021PbbBackboneEdgeBridgeName_Type(SnmpAdminString):
    """Custom type ieee8021PbbBackboneEdgeBridgeName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Ieee8021PbbBackboneEdgeBridgeName_Type.__name__ = "SnmpAdminString"
_Ieee8021PbbBackboneEdgeBridgeName_Object = MibScalar
ieee8021PbbBackboneEdgeBridgeName = _Ieee8021PbbBackboneEdgeBridgeName_Object(
    (1, 3, 111, 2, 802, 1, 1, 9, 1, 1, 1, 2),
    _Ieee8021PbbBackboneEdgeBridgeName_Type()
)
ieee8021PbbBackboneEdgeBridgeName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ieee8021PbbBackboneEdgeBridgeName.setStatus("current")
_Ieee8021PbbNumberOfIComponents_Type = Unsigned32
_Ieee8021PbbNumberOfIComponents_Object = MibScalar
ieee8021PbbNumberOfIComponents = _Ieee8021PbbNumberOfIComponents_Object(
    (1, 3, 111, 2, 802, 1, 1, 9, 1, 1, 1, 3),
    _Ieee8021PbbNumberOfIComponents_Type()
)
ieee8021PbbNumberOfIComponents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021PbbNumberOfIComponents.setStatus("current")


class _Ieee8021PbbNumberOfBComponents_Type(Unsigned32):
    """Custom type ieee8021PbbNumberOfBComponents based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Ieee8021PbbNumberOfBComponents_Type.__name__ = "Unsigned32"
_Ieee8021PbbNumberOfBComponents_Object = MibScalar
ieee8021PbbNumberOfBComponents = _Ieee8021PbbNumberOfBComponents_Object(
    (1, 3, 111, 2, 802, 1, 1, 9, 1, 1, 1, 4),
    _Ieee8021PbbNumberOfBComponents_Type()
)
ieee8021PbbNumberOfBComponents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021PbbNumberOfBComponents.setStatus("current")
_Ieee8021PbbNumberOfBebPorts_Type = Unsigned32
_Ieee8021PbbNumberOfBebPorts_Object = MibScalar
ieee8021PbbNumberOfBebPorts = _Ieee8021PbbNumberOfBebPorts_Object(
    (1, 3, 111, 2, 802, 1, 1, 9, 1, 1, 1, 5),
    _Ieee8021PbbNumberOfBebPorts_Type()
)
ieee8021PbbNumberOfBebPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021PbbNumberOfBebPorts.setStatus("current")
_Ieee8021PbbNextAvailablePipIfIndex_Type = InterfaceIndex
_Ieee8021PbbNextAvailablePipIfIndex_Object = MibScalar
ieee8021PbbNextAvailablePipIfIndex = _Ieee8021PbbNextAvailablePipIfIndex_Object(
    (1, 3, 111, 2, 802, 1, 1, 9, 1, 1, 1, 6),
    _Ieee8021PbbNextAvailablePipIfIndex_Type()
)
ieee8021PbbNextAvailablePipIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021PbbNextAvailablePipIfIndex.setStatus("current")
_Ieee8021PbbVipTable_Object = MibTable
ieee8021PbbVipTable = _Ieee8021PbbVipTable_Object(
    (1, 3, 111, 2, 802, 1, 1, 9, 1, 1, 2)
)
if mibBuilder.loadTexts:
    ieee8021PbbVipTable.setStatus("current")
_Ieee8021PbbVipEntry_Object = MibTableRow
ieee8021PbbVipEntry = _Ieee8021PbbVipEntry_Object(
    (1, 3, 111, 2, 802, 1, 1, 9, 1, 1, 2, 1)
)
ieee8021PbbVipEntry.setIndexNames(
    (0, "IEEE8021-BRIDGE-MIB", "ieee8021BridgeBasePortComponentId"),
    (0, "IEEE8021-BRIDGE-MIB", "ieee8021BridgeBasePort"),
)
if mibBuilder.loadTexts:
    ieee8021PbbVipEntry.setStatus("current")


class _Ieee8021PbbVipPipIfIndex_Type(InterfaceIndexOrZero):
    """Custom type ieee8021PbbVipPipIfIndex based on InterfaceIndexOrZero"""
    defaultValue = 0


_Ieee8021PbbVipPipIfIndex_Object = MibTableColumn
ieee8021PbbVipPipIfIndex = _Ieee8021PbbVipPipIfIndex_Object(
    (1, 3, 111, 2, 802, 1, 1, 9, 1, 1, 2, 1, 1),
    _Ieee8021PbbVipPipIfIndex_Type()
)
ieee8021PbbVipPipIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021PbbVipPipIfIndex.setStatus("current")


class _Ieee8021PbbVipISid_Type(IEEE8021PbbServiceIdentifierOrUnassigned):
    """Custom type ieee8021PbbVipISid based on IEEE8021PbbServiceIdentifierOrUnassigned"""
    defaultValue = 1


_Ieee8021PbbVipISid_Object = MibTableColumn
ieee8021PbbVipISid = _Ieee8021PbbVipISid_Object(
    (1, 3, 111, 2, 802, 1, 1, 9, 1, 1, 2, 1, 2),
    _Ieee8021PbbVipISid_Type()
)
ieee8021PbbVipISid.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ieee8021PbbVipISid.setStatus("current")


class _Ieee8021PbbVipDefaultDstBMAC_Type(MacAddress):
    """Custom type ieee8021PbbVipDefaultDstBMAC based on MacAddress"""
    defaultHexValue = "001e83000001"


_Ieee8021PbbVipDefaultDstBMAC_Object = MibTableColumn
ieee8021PbbVipDefaultDstBMAC = _Ieee8021PbbVipDefaultDstBMAC_Object(
    (1, 3, 111, 2, 802, 1, 1, 9, 1, 1, 2, 1, 3),
    _Ieee8021PbbVipDefaultDstBMAC_Type()
)
ieee8021PbbVipDefaultDstBMAC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021PbbVipDefaultDstBMAC.setStatus("current")


class _Ieee8021PbbVipType_Type(IEEE8021PbbIngressEgress):
    """Custom type ieee8021PbbVipType based on IEEE8021PbbIngressEgress"""
    defaultBinValue = "11"


_Ieee8021PbbVipType_Object = MibTableColumn
ieee8021PbbVipType = _Ieee8021PbbVipType_Object(
    (1, 3, 111, 2, 802, 1, 1, 9, 1, 1, 2, 1, 4),
    _Ieee8021PbbVipType_Type()
)
ieee8021PbbVipType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ieee8021PbbVipType.setStatus("deprecated")
_Ieee8021PbbVipRowStatus_Type = RowStatus
_Ieee8021PbbVipRowStatus_Object = MibTableColumn
ieee8021PbbVipRowStatus = _Ieee8021PbbVipRowStatus_Object(
    (1, 3, 111, 2, 802, 1, 1, 9, 1, 1, 2, 1, 5),
    _Ieee8021PbbVipRowStatus_Type()
)
ieee8021PbbVipRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ieee8021PbbVipRowStatus.setStatus("current")


class _Ieee8021PbbVipEnableConnectionId_Type(TruthValue):
    """Custom type ieee8021PbbVipEnableConnectionId based on TruthValue"""


_Ieee8021PbbVipEnableConnectionId_Object = MibTableColumn
ieee8021PbbVipEnableConnectionId = _Ieee8021PbbVipEnableConnectionId_Object(
    (1, 3, 111, 2, 802, 1, 1, 9, 1, 1, 2, 1, 6),
    _Ieee8021PbbVipEnableConnectionId_Type()
)
ieee8021PbbVipEnableConnectionId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ieee8021PbbVipEnableConnectionId.setStatus("current")
_Ieee8021PbbISidToVipTable_Object = MibTable
ieee8021PbbISidToVipTable = _Ieee8021PbbISidToVipTable_Object(
    (1, 3, 111, 2, 802, 1, 1, 9, 1, 1, 3)
)
if mibBuilder.loadTexts:
    ieee8021PbbISidToVipTable.setStatus("current")
_Ieee8021PbbISidToVipEntry_Object = MibTableRow
ieee8021PbbISidToVipEntry = _Ieee8021PbbISidToVipEntry_Object(
    (1, 3, 111, 2, 802, 1, 1, 9, 1, 1, 3, 1)
)
ieee8021PbbISidToVipEntry.setIndexNames(
    (0, "IEEE8021-PBB-MIB", "ieee8021PbbISidToVipISid"),
)
if mibBuilder.loadTexts:
    ieee8021PbbISidToVipEntry.setStatus("current")
_Ieee8021PbbISidToVipISid_Type = IEEE8021PbbServiceIdentifier
_Ieee8021PbbISidToVipISid_Object = MibTableColumn
ieee8021PbbISidToVipISid = _Ieee8021PbbISidToVipISid_Object(
    (1, 3, 111, 2, 802, 1, 1, 9, 1, 1, 3, 1, 1),
    _Ieee8021PbbISidToVipISid_Type()
)
ieee8021PbbISidToVipISid.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ieee8021PbbISidToVipISid.setStatus("current")
_Ieee8021PbbISidToVipComponentId_Type = IEEE8021PbbComponentIdentifier
_Ieee8021PbbISidToVipComponentId_Object = MibTableColumn
ieee8021PbbISidToVipComponentId = _Ieee8021PbbISidToVipComponentId_Object(
    (1, 3, 111, 2, 802, 1, 1, 9, 1, 1, 3, 1, 2),
    _Ieee8021PbbISidToVipComponentId_Type()
)
ieee8021PbbISidToVipComponentId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021PbbISidToVipComponentId.setStatus("current")
_Ieee8021PbbISidToVipPort_Type = IEEE8021BridgePortNumber
_Ieee8021PbbISidToVipPort_Object = MibTableColumn
ieee8021PbbISidToVipPort = _Ieee8021PbbISidToVipPort_Object(
    (1, 3, 111, 2, 802, 1, 1, 9, 1, 1, 3, 1, 3),
    _Ieee8021PbbISidToVipPort_Type()
)
ieee8021PbbISidToVipPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021PbbISidToVipPort.setStatus("current")
_Ieee8021PbbPipTable_Object = MibTable
ieee8021PbbPipTable = _Ieee8021PbbPipTable_Object(
    (1, 3, 111, 2, 802, 1, 1, 9, 1, 1, 4)
)
if mibBuilder.loadTexts:
    ieee8021PbbPipTable.setStatus("current")
_Ieee8021PbbPipEntry_Object = MibTableRow
ieee8021PbbPipEntry = _Ieee8021PbbPipEntry_Object(
    (1, 3, 111, 2, 802, 1, 1, 9, 1, 1, 4, 1)
)
ieee8021PbbPipEntry.setIndexNames(
    (0, "IEEE8021-PBB-MIB", "ieee8021PbbPipIfIndex"),
)
if mibBuilder.loadTexts:
    ieee8021PbbPipEntry.setStatus("current")
_Ieee8021PbbPipIfIndex_Type = InterfaceIndex
_Ieee8021PbbPipIfIndex_Object = MibTableColumn
ieee8021PbbPipIfIndex = _Ieee8021PbbPipIfIndex_Object(
    (1, 3, 111, 2, 802, 1, 1, 9, 1, 1, 4, 1, 1),
    _Ieee8021PbbPipIfIndex_Type()
)
ieee8021PbbPipIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ieee8021PbbPipIfIndex.setStatus("current")
_Ieee8021PbbPipBMACAddress_Type = MacAddress
_Ieee8021PbbPipBMACAddress_Object = MibTableColumn
ieee8021PbbPipBMACAddress = _Ieee8021PbbPipBMACAddress_Object(
    (1, 3, 111, 2, 802, 1, 1, 9, 1, 1, 4, 1, 2),
    _Ieee8021PbbPipBMACAddress_Type()
)
ieee8021PbbPipBMACAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ieee8021PbbPipBMACAddress.setStatus("current")


class _Ieee8021PbbPipName_Type(SnmpAdminString):
    """Custom type ieee8021PbbPipName based on SnmpAdminString"""
    defaultHexValue = ""

    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Ieee8021PbbPipName_Type.__name__ = "SnmpAdminString"
_Ieee8021PbbPipName_Object = MibTableColumn
ieee8021PbbPipName = _Ieee8021PbbPipName_Object(
    (1, 3, 111, 2, 802, 1, 1, 9, 1, 1, 4, 1, 3),
    _Ieee8021PbbPipName_Type()
)
ieee8021PbbPipName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ieee8021PbbPipName.setStatus("current")
_Ieee8021PbbPipIComponentId_Type = IEEE8021PbbComponentIdentifier
_Ieee8021PbbPipIComponentId_Object = MibTableColumn
ieee8021PbbPipIComponentId = _Ieee8021PbbPipIComponentId_Object(
    (1, 3, 111, 2, 802, 1, 1, 9, 1, 1, 4, 1, 4),
    _Ieee8021PbbPipIComponentId_Type()
)
ieee8021PbbPipIComponentId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021PbbPipIComponentId.setStatus("current")


class _Ieee8021PbbPipVipMap_Type(OctetString):
    """Custom type ieee8021PbbPipVipMap based on OctetString"""
    defaultHexValue = ""

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 512),
    )


_Ieee8021PbbPipVipMap_Type.__name__ = "OctetString"
_Ieee8021PbbPipVipMap_Object = MibTableColumn
ieee8021PbbPipVipMap = _Ieee8021PbbPipVipMap_Object(
    (1, 3, 111, 2, 802, 1, 1, 9, 1, 1, 4, 1, 5),
    _Ieee8021PbbPipVipMap_Type()
)
ieee8021PbbPipVipMap.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ieee8021PbbPipVipMap.setStatus("current")


class _Ieee8021PbbPipVipMap1_Type(OctetString):
    """Custom type ieee8021PbbPipVipMap1 based on OctetString"""
    defaultHexValue = ""

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 2048),
    )


_Ieee8021PbbPipVipMap1_Type.__name__ = "OctetString"
_Ieee8021PbbPipVipMap1_Object = MibTableColumn
ieee8021PbbPipVipMap1 = _Ieee8021PbbPipVipMap1_Object(
    (1, 3, 111, 2, 802, 1, 1, 9, 1, 1, 4, 1, 6),
    _Ieee8021PbbPipVipMap1_Type()
)
ieee8021PbbPipVipMap1.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ieee8021PbbPipVipMap1.setStatus("current")


class _Ieee8021PbbPipVipMap2_Type(OctetString):
    """Custom type ieee8021PbbPipVipMap2 based on OctetString"""
    defaultHexValue = ""

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 2048),
    )


_Ieee8021PbbPipVipMap2_Type.__name__ = "OctetString"
_Ieee8021PbbPipVipMap2_Object = MibTableColumn
ieee8021PbbPipVipMap2 = _Ieee8021PbbPipVipMap2_Object(
    (1, 3, 111, 2, 802, 1, 1, 9, 1, 1, 4, 1, 7),
    _Ieee8021PbbPipVipMap2_Type()
)
ieee8021PbbPipVipMap2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ieee8021PbbPipVipMap2.setStatus("current")


class _Ieee8021PbbPipVipMap3_Type(OctetString):
    """Custom type ieee8021PbbPipVipMap3 based on OctetString"""
    defaultHexValue = ""

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 2048),
    )


_Ieee8021PbbPipVipMap3_Type.__name__ = "OctetString"
_Ieee8021PbbPipVipMap3_Object = MibTableColumn
ieee8021PbbPipVipMap3 = _Ieee8021PbbPipVipMap3_Object(
    (1, 3, 111, 2, 802, 1, 1, 9, 1, 1, 4, 1, 8),
    _Ieee8021PbbPipVipMap3_Type()
)
ieee8021PbbPipVipMap3.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ieee8021PbbPipVipMap3.setStatus("current")


class _Ieee8021PbbPipVipMap4_Type(OctetString):
    """Custom type ieee8021PbbPipVipMap4 based on OctetString"""
    defaultHexValue = ""

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 1537),
    )


_Ieee8021PbbPipVipMap4_Type.__name__ = "OctetString"
_Ieee8021PbbPipVipMap4_Object = MibTableColumn
ieee8021PbbPipVipMap4 = _Ieee8021PbbPipVipMap4_Object(
    (1, 3, 111, 2, 802, 1, 1, 9, 1, 1, 4, 1, 9),
    _Ieee8021PbbPipVipMap4_Type()
)
ieee8021PbbPipVipMap4.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ieee8021PbbPipVipMap4.setStatus("current")
_Ieee8021PbbPipRowStatus_Type = RowStatus
_Ieee8021PbbPipRowStatus_Object = MibTableColumn
ieee8021PbbPipRowStatus = _Ieee8021PbbPipRowStatus_Object(
    (1, 3, 111, 2, 802, 1, 1, 9, 1, 1, 4, 1, 10),
    _Ieee8021PbbPipRowStatus_Type()
)
ieee8021PbbPipRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ieee8021PbbPipRowStatus.setStatus("current")
_Ieee8021PbbPipPriorityTable_Object = MibTable
ieee8021PbbPipPriorityTable = _Ieee8021PbbPipPriorityTable_Object(
    (1, 3, 111, 2, 802, 1, 1, 9, 1, 1, 5)
)
if mibBuilder.loadTexts:
    ieee8021PbbPipPriorityTable.setStatus("current")
_Ieee8021PbbPipPriorityEntry_Object = MibTableRow
ieee8021PbbPipPriorityEntry = _Ieee8021PbbPipPriorityEntry_Object(
    (1, 3, 111, 2, 802, 1, 1, 9, 1, 1, 5, 1)
)
if mibBuilder.loadTexts:
    ieee8021PbbPipPriorityEntry.setStatus("current")
_Ieee8021PbbPipPriorityCodePointSelection_Type = IEEE8021PriorityCodePoint
_Ieee8021PbbPipPriorityCodePointSelection_Object = MibTableColumn
ieee8021PbbPipPriorityCodePointSelection = _Ieee8021PbbPipPriorityCodePointSelection_Object(
    (1, 3, 111, 2, 802, 1, 1, 9, 1, 1, 5, 1, 1),
    _Ieee8021PbbPipPriorityCodePointSelection_Type()
)
ieee8021PbbPipPriorityCodePointSelection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ieee8021PbbPipPriorityCodePointSelection.setStatus("current")
_Ieee8021PbbPipUseDEI_Type = TruthValue
_Ieee8021PbbPipUseDEI_Object = MibTableColumn
ieee8021PbbPipUseDEI = _Ieee8021PbbPipUseDEI_Object(
    (1, 3, 111, 2, 802, 1, 1, 9, 1, 1, 5, 1, 2),
    _Ieee8021PbbPipUseDEI_Type()
)
ieee8021PbbPipUseDEI.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ieee8021PbbPipUseDEI.setStatus("current")


class _Ieee8021PbbPipRequireDropEncoding_Type(TruthValue):
    """Custom type ieee8021PbbPipRequireDropEncoding based on TruthValue"""


_Ieee8021PbbPipRequireDropEncoding_Object = MibTableColumn
ieee8021PbbPipRequireDropEncoding = _Ieee8021PbbPipRequireDropEncoding_Object(
    (1, 3, 111, 2, 802, 1, 1, 9, 1, 1, 5, 1, 3),
    _Ieee8021PbbPipRequireDropEncoding_Type()
)
ieee8021PbbPipRequireDropEncoding.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ieee8021PbbPipRequireDropEncoding.setStatus("current")
_Ieee8021PbbPipDecodingTable_Object = MibTable
ieee8021PbbPipDecodingTable = _Ieee8021PbbPipDecodingTable_Object(
    (1, 3, 111, 2, 802, 1, 1, 9, 1, 1, 6)
)
if mibBuilder.loadTexts:
    ieee8021PbbPipDecodingTable.setStatus("current")
_Ieee8021PbbPipDecodingEntry_Object = MibTableRow
ieee8021PbbPipDecodingEntry = _Ieee8021PbbPipDecodingEntry_Object(
    (1, 3, 111, 2, 802, 1, 1, 9, 1, 1, 6, 1)
)
ieee8021PbbPipDecodingEntry.setIndexNames(
    (0, "IEEE8021-PBB-MIB", "ieee8021PbbPipIfIndex"),
    (0, "IEEE8021-PBB-MIB", "ieee8021PbbPipDecodingPriorityCodePointRow"),
    (0, "IEEE8021-PBB-MIB", "ieee8021PbbPipDecodingPriorityCodePoint"),
)
if mibBuilder.loadTexts:
    ieee8021PbbPipDecodingEntry.setStatus("current")
_Ieee8021PbbPipDecodingPriorityCodePointRow_Type = IEEE8021PriorityCodePoint
_Ieee8021PbbPipDecodingPriorityCodePointRow_Object = MibTableColumn
ieee8021PbbPipDecodingPriorityCodePointRow = _Ieee8021PbbPipDecodingPriorityCodePointRow_Object(
    (1, 3, 111, 2, 802, 1, 1, 9, 1, 1, 6, 1, 1),
    _Ieee8021PbbPipDecodingPriorityCodePointRow_Type()
)
ieee8021PbbPipDecodingPriorityCodePointRow.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ieee8021PbbPipDecodingPriorityCodePointRow.setStatus("current")


class _Ieee8021PbbPipDecodingPriorityCodePoint_Type(Integer32):
    """Custom type ieee8021PbbPipDecodingPriorityCodePoint based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_Ieee8021PbbPipDecodingPriorityCodePoint_Type.__name__ = "Integer32"
_Ieee8021PbbPipDecodingPriorityCodePoint_Object = MibTableColumn
ieee8021PbbPipDecodingPriorityCodePoint = _Ieee8021PbbPipDecodingPriorityCodePoint_Object(
    (1, 3, 111, 2, 802, 1, 1, 9, 1, 1, 6, 1, 2),
    _Ieee8021PbbPipDecodingPriorityCodePoint_Type()
)
ieee8021PbbPipDecodingPriorityCodePoint.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ieee8021PbbPipDecodingPriorityCodePoint.setStatus("current")
_Ieee8021PbbPipDecodingPriority_Type = IEEE8021PriorityValue
_Ieee8021PbbPipDecodingPriority_Object = MibTableColumn
ieee8021PbbPipDecodingPriority = _Ieee8021PbbPipDecodingPriority_Object(
    (1, 3, 111, 2, 802, 1, 1, 9, 1, 1, 6, 1, 3),
    _Ieee8021PbbPipDecodingPriority_Type()
)
ieee8021PbbPipDecodingPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ieee8021PbbPipDecodingPriority.setStatus("current")
_Ieee8021PbbPipDecodingDropEligible_Type = TruthValue
_Ieee8021PbbPipDecodingDropEligible_Object = MibTableColumn
ieee8021PbbPipDecodingDropEligible = _Ieee8021PbbPipDecodingDropEligible_Object(
    (1, 3, 111, 2, 802, 1, 1, 9, 1, 1, 6, 1, 4),
    _Ieee8021PbbPipDecodingDropEligible_Type()
)
ieee8021PbbPipDecodingDropEligible.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ieee8021PbbPipDecodingDropEligible.setStatus("current")
_Ieee8021PbbPipEncodingTable_Object = MibTable
ieee8021PbbPipEncodingTable = _Ieee8021PbbPipEncodingTable_Object(
    (1, 3, 111, 2, 802, 1, 1, 9, 1, 1, 7)
)
if mibBuilder.loadTexts:
    ieee8021PbbPipEncodingTable.setStatus("current")
_Ieee8021PbbPipEncodingEntry_Object = MibTableRow
ieee8021PbbPipEncodingEntry = _Ieee8021PbbPipEncodingEntry_Object(
    (1, 3, 111, 2, 802, 1, 1, 9, 1, 1, 7, 1)
)
ieee8021PbbPipEncodingEntry.setIndexNames(
    (0, "IEEE8021-PBB-MIB", "ieee8021PbbPipIfIndex"),
    (0, "IEEE8021-PBB-MIB", "ieee8021PbbPipEncodingPriorityCodePointRow"),
    (0, "IEEE8021-PBB-MIB", "ieee8021PbbPipEncodingPriorityCodePoint"),
    (0, "IEEE8021-PBB-MIB", "ieee8021PbbPipEncodingDropEligible"),
)
if mibBuilder.loadTexts:
    ieee8021PbbPipEncodingEntry.setStatus("current")
_Ieee8021PbbPipEncodingPriorityCodePointRow_Type = IEEE8021PriorityCodePoint
_Ieee8021PbbPipEncodingPriorityCodePointRow_Object = MibTableColumn
ieee8021PbbPipEncodingPriorityCodePointRow = _Ieee8021PbbPipEncodingPriorityCodePointRow_Object(
    (1, 3, 111, 2, 802, 1, 1, 9, 1, 1, 7, 1, 1),
    _Ieee8021PbbPipEncodingPriorityCodePointRow_Type()
)
ieee8021PbbPipEncodingPriorityCodePointRow.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ieee8021PbbPipEncodingPriorityCodePointRow.setStatus("current")


class _Ieee8021PbbPipEncodingPriorityCodePoint_Type(Integer32):
    """Custom type ieee8021PbbPipEncodingPriorityCodePoint based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_Ieee8021PbbPipEncodingPriorityCodePoint_Type.__name__ = "Integer32"
_Ieee8021PbbPipEncodingPriorityCodePoint_Object = MibTableColumn
ieee8021PbbPipEncodingPriorityCodePoint = _Ieee8021PbbPipEncodingPriorityCodePoint_Object(
    (1, 3, 111, 2, 802, 1, 1, 9, 1, 1, 7, 1, 2),
    _Ieee8021PbbPipEncodingPriorityCodePoint_Type()
)
ieee8021PbbPipEncodingPriorityCodePoint.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ieee8021PbbPipEncodingPriorityCodePoint.setStatus("current")
_Ieee8021PbbPipEncodingDropEligible_Type = TruthValue
_Ieee8021PbbPipEncodingDropEligible_Object = MibTableColumn
ieee8021PbbPipEncodingDropEligible = _Ieee8021PbbPipEncodingDropEligible_Object(
    (1, 3, 111, 2, 802, 1, 1, 9, 1, 1, 7, 1, 3),
    _Ieee8021PbbPipEncodingDropEligible_Type()
)
ieee8021PbbPipEncodingDropEligible.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ieee8021PbbPipEncodingDropEligible.setStatus("current")
_Ieee8021PbbPipEncodingPriority_Type = IEEE8021PriorityValue
_Ieee8021PbbPipEncodingPriority_Object = MibTableColumn
ieee8021PbbPipEncodingPriority = _Ieee8021PbbPipEncodingPriority_Object(
    (1, 3, 111, 2, 802, 1, 1, 9, 1, 1, 7, 1, 4),
    _Ieee8021PbbPipEncodingPriority_Type()
)
ieee8021PbbPipEncodingPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ieee8021PbbPipEncodingPriority.setStatus("current")
_Ieee8021PbbVipToPipMappingTable_Object = MibTable
ieee8021PbbVipToPipMappingTable = _Ieee8021PbbVipToPipMappingTable_Object(
    (1, 3, 111, 2, 802, 1, 1, 9, 1, 1, 8)
)
if mibBuilder.loadTexts:
    ieee8021PbbVipToPipMappingTable.setStatus("current")
_Ieee8021PbbVipToPipMappingEntry_Object = MibTableRow
ieee8021PbbVipToPipMappingEntry = _Ieee8021PbbVipToPipMappingEntry_Object(
    (1, 3, 111, 2, 802, 1, 1, 9, 1, 1, 8, 1)
)
ieee8021PbbVipToPipMappingEntry.setIndexNames(
    (0, "IEEE8021-BRIDGE-MIB", "ieee8021BridgeBasePortComponentId"),
    (0, "IEEE8021-BRIDGE-MIB", "ieee8021BridgeBasePort"),
)
if mibBuilder.loadTexts:
    ieee8021PbbVipToPipMappingEntry.setStatus("current")
_Ieee8021PbbVipToPipMappingPipIfIndex_Type = InterfaceIndex
_Ieee8021PbbVipToPipMappingPipIfIndex_Object = MibTableColumn
ieee8021PbbVipToPipMappingPipIfIndex = _Ieee8021PbbVipToPipMappingPipIfIndex_Object(
    (1, 3, 111, 2, 802, 1, 1, 9, 1, 1, 8, 1, 1),
    _Ieee8021PbbVipToPipMappingPipIfIndex_Type()
)
ieee8021PbbVipToPipMappingPipIfIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ieee8021PbbVipToPipMappingPipIfIndex.setStatus("current")
_Ieee8021PbbVipToPipMappingStorageType_Type = StorageType
_Ieee8021PbbVipToPipMappingStorageType_Object = MibTableColumn
ieee8021PbbVipToPipMappingStorageType = _Ieee8021PbbVipToPipMappingStorageType_Object(
    (1, 3, 111, 2, 802, 1, 1, 9, 1, 1, 8, 1, 2),
    _Ieee8021PbbVipToPipMappingStorageType_Type()
)
ieee8021PbbVipToPipMappingStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ieee8021PbbVipToPipMappingStorageType.setStatus("current")
_Ieee8021PbbVipToPipMappingRowStatus_Type = RowStatus
_Ieee8021PbbVipToPipMappingRowStatus_Object = MibTableColumn
ieee8021PbbVipToPipMappingRowStatus = _Ieee8021PbbVipToPipMappingRowStatus_Object(
    (1, 3, 111, 2, 802, 1, 1, 9, 1, 1, 8, 1, 3),
    _Ieee8021PbbVipToPipMappingRowStatus_Type()
)
ieee8021PbbVipToPipMappingRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ieee8021PbbVipToPipMappingRowStatus.setStatus("current")
_Ieee8021PbbCBPServiceMappingTable_Object = MibTable
ieee8021PbbCBPServiceMappingTable = _Ieee8021PbbCBPServiceMappingTable_Object(
    (1, 3, 111, 2, 802, 1, 1, 9, 1, 1, 9)
)
if mibBuilder.loadTexts:
    ieee8021PbbCBPServiceMappingTable.setStatus("current")
_Ieee8021PbbCBPServiceMappingEntry_Object = MibTableRow
ieee8021PbbCBPServiceMappingEntry = _Ieee8021PbbCBPServiceMappingEntry_Object(
    (1, 3, 111, 2, 802, 1, 1, 9, 1, 1, 9, 1)
)
ieee8021PbbCBPServiceMappingEntry.setIndexNames(
    (0, "IEEE8021-BRIDGE-MIB", "ieee8021BridgeBasePortComponentId"),
    (0, "IEEE8021-BRIDGE-MIB", "ieee8021BridgeBasePort"),
    (0, "IEEE8021-PBB-MIB", "ieee8021PbbCBPServiceMappingBackboneSid"),
)
if mibBuilder.loadTexts:
    ieee8021PbbCBPServiceMappingEntry.setStatus("current")
_Ieee8021PbbCBPServiceMappingBackboneSid_Type = IEEE8021PbbServiceIdentifier
_Ieee8021PbbCBPServiceMappingBackboneSid_Object = MibTableColumn
ieee8021PbbCBPServiceMappingBackboneSid = _Ieee8021PbbCBPServiceMappingBackboneSid_Object(
    (1, 3, 111, 2, 802, 1, 1, 9, 1, 1, 9, 1, 1),
    _Ieee8021PbbCBPServiceMappingBackboneSid_Type()
)
ieee8021PbbCBPServiceMappingBackboneSid.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ieee8021PbbCBPServiceMappingBackboneSid.setStatus("current")
_Ieee8021PbbCBPServiceMappingBVid_Type = VlanId
_Ieee8021PbbCBPServiceMappingBVid_Object = MibTableColumn
ieee8021PbbCBPServiceMappingBVid = _Ieee8021PbbCBPServiceMappingBVid_Object(
    (1, 3, 111, 2, 802, 1, 1, 9, 1, 1, 9, 1, 2),
    _Ieee8021PbbCBPServiceMappingBVid_Type()
)
ieee8021PbbCBPServiceMappingBVid.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ieee8021PbbCBPServiceMappingBVid.setStatus("current")
_Ieee8021PbbCBPServiceMappingDefaultBackboneDest_Type = MacAddress
_Ieee8021PbbCBPServiceMappingDefaultBackboneDest_Object = MibTableColumn
ieee8021PbbCBPServiceMappingDefaultBackboneDest = _Ieee8021PbbCBPServiceMappingDefaultBackboneDest_Object(
    (1, 3, 111, 2, 802, 1, 1, 9, 1, 1, 9, 1, 3),
    _Ieee8021PbbCBPServiceMappingDefaultBackboneDest_Type()
)
ieee8021PbbCBPServiceMappingDefaultBackboneDest.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ieee8021PbbCBPServiceMappingDefaultBackboneDest.setStatus("current")
_Ieee8021PbbCBPServiceMappingType_Type = IEEE8021PbbIngressEgress
_Ieee8021PbbCBPServiceMappingType_Object = MibTableColumn
ieee8021PbbCBPServiceMappingType = _Ieee8021PbbCBPServiceMappingType_Object(
    (1, 3, 111, 2, 802, 1, 1, 9, 1, 1, 9, 1, 4),
    _Ieee8021PbbCBPServiceMappingType_Type()
)
ieee8021PbbCBPServiceMappingType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ieee8021PbbCBPServiceMappingType.setStatus("deprecated")


class _Ieee8021PbbCBPServiceMappingLocalSid_Type(IEEE8021PbbServiceIdentifierOrUnassigned):
    """Custom type ieee8021PbbCBPServiceMappingLocalSid based on IEEE8021PbbServiceIdentifierOrUnassigned"""
    defaultValue = 1


_Ieee8021PbbCBPServiceMappingLocalSid_Object = MibTableColumn
ieee8021PbbCBPServiceMappingLocalSid = _Ieee8021PbbCBPServiceMappingLocalSid_Object(
    (1, 3, 111, 2, 802, 1, 1, 9, 1, 1, 9, 1, 5),
    _Ieee8021PbbCBPServiceMappingLocalSid_Type()
)
ieee8021PbbCBPServiceMappingLocalSid.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ieee8021PbbCBPServiceMappingLocalSid.setStatus("current")
_Ieee8021PbbCBPServiceMappingRowStatus_Type = RowStatus
_Ieee8021PbbCBPServiceMappingRowStatus_Object = MibTableColumn
ieee8021PbbCBPServiceMappingRowStatus = _Ieee8021PbbCBPServiceMappingRowStatus_Object(
    (1, 3, 111, 2, 802, 1, 1, 9, 1, 1, 9, 1, 6),
    _Ieee8021PbbCBPServiceMappingRowStatus_Type()
)
ieee8021PbbCBPServiceMappingRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ieee8021PbbCBPServiceMappingRowStatus.setStatus("current")
_Ieee8021PbbCbpTable_Object = MibTable
ieee8021PbbCbpTable = _Ieee8021PbbCbpTable_Object(
    (1, 3, 111, 2, 802, 1, 1, 9, 1, 1, 10)
)
if mibBuilder.loadTexts:
    ieee8021PbbCbpTable.setStatus("current")
_Ieee8021PbbCbpEntry_Object = MibTableRow
ieee8021PbbCbpEntry = _Ieee8021PbbCbpEntry_Object(
    (1, 3, 111, 2, 802, 1, 1, 9, 1, 1, 10, 1)
)
ieee8021PbbCbpEntry.setIndexNames(
    (0, "IEEE8021-BRIDGE-MIB", "ieee8021BridgeBasePortComponentId"),
    (0, "IEEE8021-BRIDGE-MIB", "ieee8021BridgeBasePort"),
)
if mibBuilder.loadTexts:
    ieee8021PbbCbpEntry.setStatus("current")
_Ieee8021PbbCbpRowStatus_Type = RowStatus
_Ieee8021PbbCbpRowStatus_Object = MibTableColumn
ieee8021PbbCbpRowStatus = _Ieee8021PbbCbpRowStatus_Object(
    (1, 3, 111, 2, 802, 1, 1, 9, 1, 1, 10, 1, 1),
    _Ieee8021PbbCbpRowStatus_Type()
)
ieee8021PbbCbpRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ieee8021PbbCbpRowStatus.setStatus("current")
_Ieee8021PbbConformance_ObjectIdentity = ObjectIdentity
ieee8021PbbConformance = _Ieee8021PbbConformance_ObjectIdentity(
    (1, 3, 111, 2, 802, 1, 1, 9, 2)
)
_Ieee8021PbbGroups_ObjectIdentity = ObjectIdentity
ieee8021PbbGroups = _Ieee8021PbbGroups_ObjectIdentity(
    (1, 3, 111, 2, 802, 1, 1, 9, 2, 1)
)
_Ieee8021PbbCompliances_ObjectIdentity = ObjectIdentity
ieee8021PbbCompliances = _Ieee8021PbbCompliances_ObjectIdentity(
    (1, 3, 111, 2, 802, 1, 1, 9, 2, 2)
)
ieee8021PbbPipEntry.registerAugmentions(
    ("IEEE8021-PBB-MIB",
     "ieee8021PbbPipPriorityEntry")
)
ieee8021PbbPipPriorityEntry.setIndexNames(*ieee8021PbbPipEntry.getIndexNames())

# Managed Objects groups

ieee8021PbbBackboneEdgeBridgeGroup = ObjectGroup(
    (1, 3, 111, 2, 802, 1, 1, 9, 2, 1, 1)
)
ieee8021PbbBackboneEdgeBridgeGroup.setObjects(
      *(("IEEE8021-PBB-MIB", "ieee8021PbbBackboneEdgeBridgeAddress"),
        ("IEEE8021-PBB-MIB", "ieee8021PbbBackboneEdgeBridgeName"),
        ("IEEE8021-PBB-MIB", "ieee8021PbbNumberOfIComponents"),
        ("IEEE8021-PBB-MIB", "ieee8021PbbNumberOfBComponents"),
        ("IEEE8021-PBB-MIB", "ieee8021PbbNumberOfBebPorts"))
)
if mibBuilder.loadTexts:
    ieee8021PbbBackboneEdgeBridgeGroup.setStatus("current")

ieee8021PbbVipGroup = ObjectGroup(
    (1, 3, 111, 2, 802, 1, 1, 9, 2, 1, 2)
)
ieee8021PbbVipGroup.setObjects(
      *(("IEEE8021-PBB-MIB", "ieee8021PbbVipPipIfIndex"),
        ("IEEE8021-PBB-MIB", "ieee8021PbbVipISid"),
        ("IEEE8021-PBB-MIB", "ieee8021PbbVipDefaultDstBMAC"),
        ("IEEE8021-PBB-MIB", "ieee8021PbbVipType"),
        ("IEEE8021-PBB-MIB", "ieee8021PbbVipRowStatus"),
        ("IEEE8021-PBB-MIB", "ieee8021PbbISidToVipComponentId"),
        ("IEEE8021-PBB-MIB", "ieee8021PbbISidToVipPort"))
)
if mibBuilder.loadTexts:
    ieee8021PbbVipGroup.setStatus("current")

ieee8021PbbPipGroup = ObjectGroup(
    (1, 3, 111, 2, 802, 1, 1, 9, 2, 1, 3)
)
ieee8021PbbPipGroup.setObjects(
      *(("IEEE8021-PBB-MIB", "ieee8021PbbNextAvailablePipIfIndex"),
        ("IEEE8021-PBB-MIB", "ieee8021PbbPipBMACAddress"),
        ("IEEE8021-PBB-MIB", "ieee8021PbbPipName"),
        ("IEEE8021-PBB-MIB", "ieee8021PbbPipIComponentId"),
        ("IEEE8021-PBB-MIB", "ieee8021PbbPipVipMap"),
        ("IEEE8021-PBB-MIB", "ieee8021PbbPipVipMap1"),
        ("IEEE8021-PBB-MIB", "ieee8021PbbPipVipMap2"),
        ("IEEE8021-PBB-MIB", "ieee8021PbbPipVipMap3"),
        ("IEEE8021-PBB-MIB", "ieee8021PbbPipVipMap4"),
        ("IEEE8021-PBB-MIB", "ieee8021PbbPipRowStatus"))
)
if mibBuilder.loadTexts:
    ieee8021PbbPipGroup.setStatus("current")

ieee8021PbbDefaultPriorityGroup = ObjectGroup(
    (1, 3, 111, 2, 802, 1, 1, 9, 2, 1, 4)
)
ieee8021PbbDefaultPriorityGroup.setObjects(
      *(("IEEE8021-PBB-MIB", "ieee8021PbbPipPriorityCodePointSelection"),
        ("IEEE8021-PBB-MIB", "ieee8021PbbPipUseDEI"),
        ("IEEE8021-PBB-MIB", "ieee8021PbbPipRequireDropEncoding"))
)
if mibBuilder.loadTexts:
    ieee8021PbbDefaultPriorityGroup.setStatus("current")

ieee8021PbbPipDecodingGroup = ObjectGroup(
    (1, 3, 111, 2, 802, 1, 1, 9, 2, 1, 5)
)
ieee8021PbbPipDecodingGroup.setObjects(
      *(("IEEE8021-PBB-MIB", "ieee8021PbbPipDecodingPriority"),
        ("IEEE8021-PBB-MIB", "ieee8021PbbPipDecodingDropEligible"))
)
if mibBuilder.loadTexts:
    ieee8021PbbPipDecodingGroup.setStatus("current")

ieee8021PbbPipEncodingGroup = ObjectGroup(
    (1, 3, 111, 2, 802, 1, 1, 9, 2, 1, 6)
)
ieee8021PbbPipEncodingGroup.setObjects(
    ("IEEE8021-PBB-MIB", "ieee8021PbbPipEncodingPriority")
)
if mibBuilder.loadTexts:
    ieee8021PbbPipEncodingGroup.setStatus("current")

ieee8021PbbVipToPipMappingGroup = ObjectGroup(
    (1, 3, 111, 2, 802, 1, 1, 9, 2, 1, 7)
)
ieee8021PbbVipToPipMappingGroup.setObjects(
      *(("IEEE8021-PBB-MIB", "ieee8021PbbVipToPipMappingPipIfIndex"),
        ("IEEE8021-PBB-MIB", "ieee8021PbbVipToPipMappingStorageType"),
        ("IEEE8021-PBB-MIB", "ieee8021PbbVipToPipMappingRowStatus"))
)
if mibBuilder.loadTexts:
    ieee8021PbbVipToPipMappingGroup.setStatus("current")

ieee8021PbbCBPServiceMappingGroup = ObjectGroup(
    (1, 3, 111, 2, 802, 1, 1, 9, 2, 1, 8)
)
ieee8021PbbCBPServiceMappingGroup.setObjects(
      *(("IEEE8021-PBB-MIB", "ieee8021PbbCBPServiceMappingBVid"),
        ("IEEE8021-PBB-MIB", "ieee8021PbbCBPServiceMappingDefaultBackboneDest"),
        ("IEEE8021-PBB-MIB", "ieee8021PbbCBPServiceMappingType"),
        ("IEEE8021-PBB-MIB", "ieee8021PbbCBPServiceMappingLocalSid"),
        ("IEEE8021-PBB-MIB", "ieee8021PbbCBPServiceMappingRowStatus"))
)
if mibBuilder.loadTexts:
    ieee8021PbbCBPServiceMappingGroup.setStatus("current")

ieee8021PbbDynamicCbpGroup = ObjectGroup(
    (1, 3, 111, 2, 802, 1, 1, 9, 2, 1, 9)
)
ieee8021PbbDynamicCbpGroup.setObjects(
    ("IEEE8021-PBB-MIB", "ieee8021PbbCbpRowStatus")
)
if mibBuilder.loadTexts:
    ieee8021PbbDynamicCbpGroup.setStatus("current")

ieee8021PbbVipPbbTeGroup = ObjectGroup(
    (1, 3, 111, 2, 802, 1, 1, 9, 2, 1, 10)
)
ieee8021PbbVipPbbTeGroup.setObjects(
    ("IEEE8021-PBB-MIB", "ieee8021PbbVipEnableConnectionId")
)
if mibBuilder.loadTexts:
    ieee8021PbbVipPbbTeGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

ieee8021PbbCompliance = ModuleCompliance(
    (1, 3, 111, 2, 802, 1, 1, 9, 2, 2, 1)
)
if mibBuilder.loadTexts:
    ieee8021PbbCompliance.setStatus(
        "current"
    )

ieee8021PbbWithPbbTeCompliance = ModuleCompliance(
    (1, 3, 111, 2, 802, 1, 1, 9, 2, 2, 2)
)
if mibBuilder.loadTexts:
    ieee8021PbbWithPbbTeCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "IEEE8021-PBB-MIB",
    **{"ieee8021PbbMib": ieee8021PbbMib,
       "ieee8021PbbNotifications": ieee8021PbbNotifications,
       "ieee8021PbbObjects": ieee8021PbbObjects,
       "ieee8021PbbProviderBackboneBridge": ieee8021PbbProviderBackboneBridge,
       "ieee8021PbbBackboneEdgeBridgeObjects": ieee8021PbbBackboneEdgeBridgeObjects,
       "ieee8021PbbBackboneEdgeBridgeAddress": ieee8021PbbBackboneEdgeBridgeAddress,
       "ieee8021PbbBackboneEdgeBridgeName": ieee8021PbbBackboneEdgeBridgeName,
       "ieee8021PbbNumberOfIComponents": ieee8021PbbNumberOfIComponents,
       "ieee8021PbbNumberOfBComponents": ieee8021PbbNumberOfBComponents,
       "ieee8021PbbNumberOfBebPorts": ieee8021PbbNumberOfBebPorts,
       "ieee8021PbbNextAvailablePipIfIndex": ieee8021PbbNextAvailablePipIfIndex,
       "ieee8021PbbVipTable": ieee8021PbbVipTable,
       "ieee8021PbbVipEntry": ieee8021PbbVipEntry,
       "ieee8021PbbVipPipIfIndex": ieee8021PbbVipPipIfIndex,
       "ieee8021PbbVipISid": ieee8021PbbVipISid,
       "ieee8021PbbVipDefaultDstBMAC": ieee8021PbbVipDefaultDstBMAC,
       "ieee8021PbbVipType": ieee8021PbbVipType,
       "ieee8021PbbVipRowStatus": ieee8021PbbVipRowStatus,
       "ieee8021PbbVipEnableConnectionId": ieee8021PbbVipEnableConnectionId,
       "ieee8021PbbISidToVipTable": ieee8021PbbISidToVipTable,
       "ieee8021PbbISidToVipEntry": ieee8021PbbISidToVipEntry,
       "ieee8021PbbISidToVipISid": ieee8021PbbISidToVipISid,
       "ieee8021PbbISidToVipComponentId": ieee8021PbbISidToVipComponentId,
       "ieee8021PbbISidToVipPort": ieee8021PbbISidToVipPort,
       "ieee8021PbbPipTable": ieee8021PbbPipTable,
       "ieee8021PbbPipEntry": ieee8021PbbPipEntry,
       "ieee8021PbbPipIfIndex": ieee8021PbbPipIfIndex,
       "ieee8021PbbPipBMACAddress": ieee8021PbbPipBMACAddress,
       "ieee8021PbbPipName": ieee8021PbbPipName,
       "ieee8021PbbPipIComponentId": ieee8021PbbPipIComponentId,
       "ieee8021PbbPipVipMap": ieee8021PbbPipVipMap,
       "ieee8021PbbPipVipMap1": ieee8021PbbPipVipMap1,
       "ieee8021PbbPipVipMap2": ieee8021PbbPipVipMap2,
       "ieee8021PbbPipVipMap3": ieee8021PbbPipVipMap3,
       "ieee8021PbbPipVipMap4": ieee8021PbbPipVipMap4,
       "ieee8021PbbPipRowStatus": ieee8021PbbPipRowStatus,
       "ieee8021PbbPipPriorityTable": ieee8021PbbPipPriorityTable,
       "ieee8021PbbPipPriorityEntry": ieee8021PbbPipPriorityEntry,
       "ieee8021PbbPipPriorityCodePointSelection": ieee8021PbbPipPriorityCodePointSelection,
       "ieee8021PbbPipUseDEI": ieee8021PbbPipUseDEI,
       "ieee8021PbbPipRequireDropEncoding": ieee8021PbbPipRequireDropEncoding,
       "ieee8021PbbPipDecodingTable": ieee8021PbbPipDecodingTable,
       "ieee8021PbbPipDecodingEntry": ieee8021PbbPipDecodingEntry,
       "ieee8021PbbPipDecodingPriorityCodePointRow": ieee8021PbbPipDecodingPriorityCodePointRow,
       "ieee8021PbbPipDecodingPriorityCodePoint": ieee8021PbbPipDecodingPriorityCodePoint,
       "ieee8021PbbPipDecodingPriority": ieee8021PbbPipDecodingPriority,
       "ieee8021PbbPipDecodingDropEligible": ieee8021PbbPipDecodingDropEligible,
       "ieee8021PbbPipEncodingTable": ieee8021PbbPipEncodingTable,
       "ieee8021PbbPipEncodingEntry": ieee8021PbbPipEncodingEntry,
       "ieee8021PbbPipEncodingPriorityCodePointRow": ieee8021PbbPipEncodingPriorityCodePointRow,
       "ieee8021PbbPipEncodingPriorityCodePoint": ieee8021PbbPipEncodingPriorityCodePoint,
       "ieee8021PbbPipEncodingDropEligible": ieee8021PbbPipEncodingDropEligible,
       "ieee8021PbbPipEncodingPriority": ieee8021PbbPipEncodingPriority,
       "ieee8021PbbVipToPipMappingTable": ieee8021PbbVipToPipMappingTable,
       "ieee8021PbbVipToPipMappingEntry": ieee8021PbbVipToPipMappingEntry,
       "ieee8021PbbVipToPipMappingPipIfIndex": ieee8021PbbVipToPipMappingPipIfIndex,
       "ieee8021PbbVipToPipMappingStorageType": ieee8021PbbVipToPipMappingStorageType,
       "ieee8021PbbVipToPipMappingRowStatus": ieee8021PbbVipToPipMappingRowStatus,
       "ieee8021PbbCBPServiceMappingTable": ieee8021PbbCBPServiceMappingTable,
       "ieee8021PbbCBPServiceMappingEntry": ieee8021PbbCBPServiceMappingEntry,
       "ieee8021PbbCBPServiceMappingBackboneSid": ieee8021PbbCBPServiceMappingBackboneSid,
       "ieee8021PbbCBPServiceMappingBVid": ieee8021PbbCBPServiceMappingBVid,
       "ieee8021PbbCBPServiceMappingDefaultBackboneDest": ieee8021PbbCBPServiceMappingDefaultBackboneDest,
       "ieee8021PbbCBPServiceMappingType": ieee8021PbbCBPServiceMappingType,
       "ieee8021PbbCBPServiceMappingLocalSid": ieee8021PbbCBPServiceMappingLocalSid,
       "ieee8021PbbCBPServiceMappingRowStatus": ieee8021PbbCBPServiceMappingRowStatus,
       "ieee8021PbbCbpTable": ieee8021PbbCbpTable,
       "ieee8021PbbCbpEntry": ieee8021PbbCbpEntry,
       "ieee8021PbbCbpRowStatus": ieee8021PbbCbpRowStatus,
       "ieee8021PbbConformance": ieee8021PbbConformance,
       "ieee8021PbbGroups": ieee8021PbbGroups,
       "ieee8021PbbBackboneEdgeBridgeGroup": ieee8021PbbBackboneEdgeBridgeGroup,
       "ieee8021PbbVipGroup": ieee8021PbbVipGroup,
       "ieee8021PbbPipGroup": ieee8021PbbPipGroup,
       "ieee8021PbbDefaultPriorityGroup": ieee8021PbbDefaultPriorityGroup,
       "ieee8021PbbPipDecodingGroup": ieee8021PbbPipDecodingGroup,
       "ieee8021PbbPipEncodingGroup": ieee8021PbbPipEncodingGroup,
       "ieee8021PbbVipToPipMappingGroup": ieee8021PbbVipToPipMappingGroup,
       "ieee8021PbbCBPServiceMappingGroup": ieee8021PbbCBPServiceMappingGroup,
       "ieee8021PbbDynamicCbpGroup": ieee8021PbbDynamicCbpGroup,
       "ieee8021PbbVipPbbTeGroup": ieee8021PbbVipPbbTeGroup,
       "ieee8021PbbCompliances": ieee8021PbbCompliances,
       "ieee8021PbbCompliance": ieee8021PbbCompliance,
       "ieee8021PbbWithPbbTeCompliance": ieee8021PbbWithPbbTeCompliance}
)
