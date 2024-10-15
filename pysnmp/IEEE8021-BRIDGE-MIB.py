# SNMP MIB module (IEEE8021-BRIDGE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/IEEE8021-BRIDGE-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:54:56 2024
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

(IEEE8021BridgePortNumber,
 IEEE8021BridgePortNumberOrZero,
 IEEE8021BridgePortType,
 IEEE8021PbbComponentIdentifier,
 IEEE8021PbbComponentIdentifierOrZero,
 IEEE8021PriorityCodePoint,
 IEEE8021PriorityValue,
 ieee802dot1mibs) = mibBuilder.importSymbols(
    "IEEE8021-TC-MIB",
    "IEEE8021BridgePortNumber",
    "IEEE8021BridgePortNumberOrZero",
    "IEEE8021BridgePortType",
    "IEEE8021PbbComponentIdentifier",
    "IEEE8021PbbComponentIdentifierOrZero",
    "IEEE8021PriorityCodePoint",
    "IEEE8021PriorityValue",
    "ieee802dot1mibs")

(InterfaceIndexOrZero,
 ifGeneralInformationGroup,
 ifIndex) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndexOrZero",
    "ifGeneralInformationGroup",
    "ifIndex")

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

(systemGroup,) = mibBuilder.importSymbols(
    "SNMPv2-MIB",
    "systemGroup")

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
 TimeInterval,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "RowStatus",
    "TextualConvention",
    "TimeInterval",
    "TruthValue")


# MODULE-IDENTITY

ieee8021BridgeMib = ModuleIdentity(
    (1, 3, 111, 2, 802, 1, 1, 2)
)
ieee8021BridgeMib.setRevisions(
        ("2018-06-28 00:00",
         "2014-12-15 00:00",
         "2012-08-10 00:00",
         "2012-02-15 00:00",
         "2011-04-06 00:00",
         "2011-02-27 00:00",
         "2008-10-15 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Ieee8021BridgeNotifications_ObjectIdentity = ObjectIdentity
ieee8021BridgeNotifications = _Ieee8021BridgeNotifications_ObjectIdentity(
    (1, 3, 111, 2, 802, 1, 1, 2, 0)
)
_Ieee8021BridgeObjects_ObjectIdentity = ObjectIdentity
ieee8021BridgeObjects = _Ieee8021BridgeObjects_ObjectIdentity(
    (1, 3, 111, 2, 802, 1, 1, 2, 1)
)
_Ieee8021BridgeBase_ObjectIdentity = ObjectIdentity
ieee8021BridgeBase = _Ieee8021BridgeBase_ObjectIdentity(
    (1, 3, 111, 2, 802, 1, 1, 2, 1, 1)
)
_Ieee8021BridgeBaseTable_Object = MibTable
ieee8021BridgeBaseTable = _Ieee8021BridgeBaseTable_Object(
    (1, 3, 111, 2, 802, 1, 1, 2, 1, 1, 1)
)
if mibBuilder.loadTexts:
    ieee8021BridgeBaseTable.setStatus("current")
_Ieee8021BridgeBaseEntry_Object = MibTableRow
ieee8021BridgeBaseEntry = _Ieee8021BridgeBaseEntry_Object(
    (1, 3, 111, 2, 802, 1, 1, 2, 1, 1, 1, 1)
)
ieee8021BridgeBaseEntry.setIndexNames(
    (0, "IEEE8021-BRIDGE-MIB", "ieee8021BridgeBaseComponentId"),
)
if mibBuilder.loadTexts:
    ieee8021BridgeBaseEntry.setStatus("current")
_Ieee8021BridgeBaseComponentId_Type = IEEE8021PbbComponentIdentifier
_Ieee8021BridgeBaseComponentId_Object = MibTableColumn
ieee8021BridgeBaseComponentId = _Ieee8021BridgeBaseComponentId_Object(
    (1, 3, 111, 2, 802, 1, 1, 2, 1, 1, 1, 1, 1),
    _Ieee8021BridgeBaseComponentId_Type()
)
ieee8021BridgeBaseComponentId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ieee8021BridgeBaseComponentId.setStatus("current")
_Ieee8021BridgeBaseBridgeAddress_Type = MacAddress
_Ieee8021BridgeBaseBridgeAddress_Object = MibTableColumn
ieee8021BridgeBaseBridgeAddress = _Ieee8021BridgeBaseBridgeAddress_Object(
    (1, 3, 111, 2, 802, 1, 1, 2, 1, 1, 1, 1, 2),
    _Ieee8021BridgeBaseBridgeAddress_Type()
)
ieee8021BridgeBaseBridgeAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ieee8021BridgeBaseBridgeAddress.setStatus("current")
_Ieee8021BridgeBaseNumPorts_Type = Integer32
_Ieee8021BridgeBaseNumPorts_Object = MibTableColumn
ieee8021BridgeBaseNumPorts = _Ieee8021BridgeBaseNumPorts_Object(
    (1, 3, 111, 2, 802, 1, 1, 2, 1, 1, 1, 1, 3),
    _Ieee8021BridgeBaseNumPorts_Type()
)
ieee8021BridgeBaseNumPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021BridgeBaseNumPorts.setStatus("current")
if mibBuilder.loadTexts:
    ieee8021BridgeBaseNumPorts.setUnits("ports")


class _Ieee8021BridgeBaseComponentType_Type(Integer32):
    """Custom type ieee8021BridgeBaseComponentType based on Integer32"""
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
        *(("bComponent", 2),
          ("cVlanComponent", 3),
          ("dBridgeComponent", 5),
          ("erComponent", 6),
          ("iComponent", 1),
          ("sVlanComponent", 4),
          ("tComponent", 7))
    )


_Ieee8021BridgeBaseComponentType_Type.__name__ = "Integer32"
_Ieee8021BridgeBaseComponentType_Object = MibTableColumn
ieee8021BridgeBaseComponentType = _Ieee8021BridgeBaseComponentType_Object(
    (1, 3, 111, 2, 802, 1, 1, 2, 1, 1, 1, 1, 4),
    _Ieee8021BridgeBaseComponentType_Type()
)
ieee8021BridgeBaseComponentType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ieee8021BridgeBaseComponentType.setStatus("current")


class _Ieee8021BridgeBaseDeviceCapabilities_Type(Bits):
    """Custom type ieee8021BridgeBaseDeviceCapabilities based on Bits"""
    namedValues = NamedValues(
        *(("dot1dExtendedFilteringServices", 0),
          ("dot1dLocalVlanCapable", 7),
          ("dot1dTrafficClasses", 1),
          ("dot1qConfigurablePvidTagging", 6),
          ("dot1qHybridCapable", 5),
          ("dot1qIVLCapable", 3),
          ("dot1qSVLCapable", 4),
          ("dot1qStaticEntryIndividualPort", 2))
    )

_Ieee8021BridgeBaseDeviceCapabilities_Type.__name__ = "Bits"
_Ieee8021BridgeBaseDeviceCapabilities_Object = MibTableColumn
ieee8021BridgeBaseDeviceCapabilities = _Ieee8021BridgeBaseDeviceCapabilities_Object(
    (1, 3, 111, 2, 802, 1, 1, 2, 1, 1, 1, 1, 5),
    _Ieee8021BridgeBaseDeviceCapabilities_Type()
)
ieee8021BridgeBaseDeviceCapabilities.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ieee8021BridgeBaseDeviceCapabilities.setStatus("current")


class _Ieee8021BridgeBaseTrafficClassesEnabled_Type(TruthValue):
    """Custom type ieee8021BridgeBaseTrafficClassesEnabled based on TruthValue"""


_Ieee8021BridgeBaseTrafficClassesEnabled_Object = MibTableColumn
ieee8021BridgeBaseTrafficClassesEnabled = _Ieee8021BridgeBaseTrafficClassesEnabled_Object(
    (1, 3, 111, 2, 802, 1, 1, 2, 1, 1, 1, 1, 6),
    _Ieee8021BridgeBaseTrafficClassesEnabled_Type()
)
ieee8021BridgeBaseTrafficClassesEnabled.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ieee8021BridgeBaseTrafficClassesEnabled.setStatus("current")


class _Ieee8021BridgeBaseMmrpEnabledStatus_Type(TruthValue):
    """Custom type ieee8021BridgeBaseMmrpEnabledStatus based on TruthValue"""


_Ieee8021BridgeBaseMmrpEnabledStatus_Object = MibTableColumn
ieee8021BridgeBaseMmrpEnabledStatus = _Ieee8021BridgeBaseMmrpEnabledStatus_Object(
    (1, 3, 111, 2, 802, 1, 1, 2, 1, 1, 1, 1, 7),
    _Ieee8021BridgeBaseMmrpEnabledStatus_Type()
)
ieee8021BridgeBaseMmrpEnabledStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ieee8021BridgeBaseMmrpEnabledStatus.setStatus("current")
_Ieee8021BridgeBaseRowStatus_Type = RowStatus
_Ieee8021BridgeBaseRowStatus_Object = MibTableColumn
ieee8021BridgeBaseRowStatus = _Ieee8021BridgeBaseRowStatus_Object(
    (1, 3, 111, 2, 802, 1, 1, 2, 1, 1, 1, 1, 8),
    _Ieee8021BridgeBaseRowStatus_Type()
)
ieee8021BridgeBaseRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ieee8021BridgeBaseRowStatus.setStatus("current")
_Ieee8021BridgeBasePortTable_Object = MibTable
ieee8021BridgeBasePortTable = _Ieee8021BridgeBasePortTable_Object(
    (1, 3, 111, 2, 802, 1, 1, 2, 1, 1, 4)
)
if mibBuilder.loadTexts:
    ieee8021BridgeBasePortTable.setStatus("current")
_Ieee8021BridgeBasePortEntry_Object = MibTableRow
ieee8021BridgeBasePortEntry = _Ieee8021BridgeBasePortEntry_Object(
    (1, 3, 111, 2, 802, 1, 1, 2, 1, 1, 4, 1)
)
ieee8021BridgeBasePortEntry.setIndexNames(
    (0, "IEEE8021-BRIDGE-MIB", "ieee8021BridgeBasePortComponentId"),
    (0, "IEEE8021-BRIDGE-MIB", "ieee8021BridgeBasePort"),
)
if mibBuilder.loadTexts:
    ieee8021BridgeBasePortEntry.setStatus("current")
_Ieee8021BridgeBasePortComponentId_Type = IEEE8021PbbComponentIdentifier
_Ieee8021BridgeBasePortComponentId_Object = MibTableColumn
ieee8021BridgeBasePortComponentId = _Ieee8021BridgeBasePortComponentId_Object(
    (1, 3, 111, 2, 802, 1, 1, 2, 1, 1, 4, 1, 1),
    _Ieee8021BridgeBasePortComponentId_Type()
)
ieee8021BridgeBasePortComponentId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ieee8021BridgeBasePortComponentId.setStatus("current")
_Ieee8021BridgeBasePort_Type = IEEE8021BridgePortNumber
_Ieee8021BridgeBasePort_Object = MibTableColumn
ieee8021BridgeBasePort = _Ieee8021BridgeBasePort_Object(
    (1, 3, 111, 2, 802, 1, 1, 2, 1, 1, 4, 1, 2),
    _Ieee8021BridgeBasePort_Type()
)
ieee8021BridgeBasePort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ieee8021BridgeBasePort.setStatus("current")
_Ieee8021BridgeBasePortIfIndex_Type = InterfaceIndexOrZero
_Ieee8021BridgeBasePortIfIndex_Object = MibTableColumn
ieee8021BridgeBasePortIfIndex = _Ieee8021BridgeBasePortIfIndex_Object(
    (1, 3, 111, 2, 802, 1, 1, 2, 1, 1, 4, 1, 3),
    _Ieee8021BridgeBasePortIfIndex_Type()
)
ieee8021BridgeBasePortIfIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ieee8021BridgeBasePortIfIndex.setStatus("current")
_Ieee8021BridgeBasePortDelayExceededDiscards_Type = Counter64
_Ieee8021BridgeBasePortDelayExceededDiscards_Object = MibTableColumn
ieee8021BridgeBasePortDelayExceededDiscards = _Ieee8021BridgeBasePortDelayExceededDiscards_Object(
    (1, 3, 111, 2, 802, 1, 1, 2, 1, 1, 4, 1, 4),
    _Ieee8021BridgeBasePortDelayExceededDiscards_Type()
)
ieee8021BridgeBasePortDelayExceededDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021BridgeBasePortDelayExceededDiscards.setStatus("current")
if mibBuilder.loadTexts:
    ieee8021BridgeBasePortDelayExceededDiscards.setUnits("frames")
_Ieee8021BridgeBasePortMtuExceededDiscards_Type = Counter64
_Ieee8021BridgeBasePortMtuExceededDiscards_Object = MibTableColumn
ieee8021BridgeBasePortMtuExceededDiscards = _Ieee8021BridgeBasePortMtuExceededDiscards_Object(
    (1, 3, 111, 2, 802, 1, 1, 2, 1, 1, 4, 1, 5),
    _Ieee8021BridgeBasePortMtuExceededDiscards_Type()
)
ieee8021BridgeBasePortMtuExceededDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021BridgeBasePortMtuExceededDiscards.setStatus("current")
if mibBuilder.loadTexts:
    ieee8021BridgeBasePortMtuExceededDiscards.setUnits("frames")


class _Ieee8021BridgeBasePortCapabilities_Type(Bits):
    """Custom type ieee8021BridgeBasePortCapabilities based on Bits"""
    namedValues = NamedValues(
        *(("dot1qConfigurableAcceptableFrameTypes", 1),
          ("dot1qDot1qTagging", 0),
          ("dot1qIngressFiltering", 2))
    )

_Ieee8021BridgeBasePortCapabilities_Type.__name__ = "Bits"
_Ieee8021BridgeBasePortCapabilities_Object = MibTableColumn
ieee8021BridgeBasePortCapabilities = _Ieee8021BridgeBasePortCapabilities_Object(
    (1, 3, 111, 2, 802, 1, 1, 2, 1, 1, 4, 1, 6),
    _Ieee8021BridgeBasePortCapabilities_Type()
)
ieee8021BridgeBasePortCapabilities.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021BridgeBasePortCapabilities.setStatus("current")


class _Ieee8021BridgeBasePortTypeCapabilities_Type(Bits):
    """Custom type ieee8021BridgeBasePortTypeCapabilities based on Bits"""
    namedValues = NamedValues(
        *(("customerBackbonePort", 4),
          ("customerEdgePort", 3),
          ("customerNetworkPort", 2),
          ("customerVlanPort", 0),
          ("dBridgePort", 6),
          ("providerNetworkPort", 1),
          ("remoteCustomerAccessPort", 7),
          ("stationFacingBridgePort", 8),
          ("uplinkAccessPort", 9),
          ("uplinkRelayPort", 10),
          ("virtualInstancePort", 5))
    )

_Ieee8021BridgeBasePortTypeCapabilities_Type.__name__ = "Bits"
_Ieee8021BridgeBasePortTypeCapabilities_Object = MibTableColumn
ieee8021BridgeBasePortTypeCapabilities = _Ieee8021BridgeBasePortTypeCapabilities_Object(
    (1, 3, 111, 2, 802, 1, 1, 2, 1, 1, 4, 1, 7),
    _Ieee8021BridgeBasePortTypeCapabilities_Type()
)
ieee8021BridgeBasePortTypeCapabilities.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021BridgeBasePortTypeCapabilities.setStatus("current")
_Ieee8021BridgeBasePortType_Type = IEEE8021BridgePortType
_Ieee8021BridgeBasePortType_Object = MibTableColumn
ieee8021BridgeBasePortType = _Ieee8021BridgeBasePortType_Object(
    (1, 3, 111, 2, 802, 1, 1, 2, 1, 1, 4, 1, 8),
    _Ieee8021BridgeBasePortType_Type()
)
ieee8021BridgeBasePortType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021BridgeBasePortType.setStatus("current")
_Ieee8021BridgeBasePortExternal_Type = TruthValue
_Ieee8021BridgeBasePortExternal_Object = MibTableColumn
ieee8021BridgeBasePortExternal = _Ieee8021BridgeBasePortExternal_Object(
    (1, 3, 111, 2, 802, 1, 1, 2, 1, 1, 4, 1, 9),
    _Ieee8021BridgeBasePortExternal_Type()
)
ieee8021BridgeBasePortExternal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021BridgeBasePortExternal.setStatus("current")


class _Ieee8021BridgeBasePortAdminPointToPoint_Type(Integer32):
    """Custom type ieee8021BridgeBasePortAdminPointToPoint based on Integer32"""
    defaultValue = 2

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
          ("forceFalse", 2),
          ("forceTrue", 1))
    )


_Ieee8021BridgeBasePortAdminPointToPoint_Type.__name__ = "Integer32"
_Ieee8021BridgeBasePortAdminPointToPoint_Object = MibTableColumn
ieee8021BridgeBasePortAdminPointToPoint = _Ieee8021BridgeBasePortAdminPointToPoint_Object(
    (1, 3, 111, 2, 802, 1, 1, 2, 1, 1, 4, 1, 10),
    _Ieee8021BridgeBasePortAdminPointToPoint_Type()
)
ieee8021BridgeBasePortAdminPointToPoint.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ieee8021BridgeBasePortAdminPointToPoint.setStatus("current")
_Ieee8021BridgeBasePortOperPointToPoint_Type = TruthValue
_Ieee8021BridgeBasePortOperPointToPoint_Object = MibTableColumn
ieee8021BridgeBasePortOperPointToPoint = _Ieee8021BridgeBasePortOperPointToPoint_Object(
    (1, 3, 111, 2, 802, 1, 1, 2, 1, 1, 4, 1, 11),
    _Ieee8021BridgeBasePortOperPointToPoint_Type()
)
ieee8021BridgeBasePortOperPointToPoint.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021BridgeBasePortOperPointToPoint.setStatus("current")
_Ieee8021BridgeBasePortName_Type = SnmpAdminString
_Ieee8021BridgeBasePortName_Object = MibTableColumn
ieee8021BridgeBasePortName = _Ieee8021BridgeBasePortName_Object(
    (1, 3, 111, 2, 802, 1, 1, 2, 1, 1, 4, 1, 12),
    _Ieee8021BridgeBasePortName_Type()
)
ieee8021BridgeBasePortName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021BridgeBasePortName.setStatus("current")
_Ieee8021BridgeBaseIfToPortTable_Object = MibTable
ieee8021BridgeBaseIfToPortTable = _Ieee8021BridgeBaseIfToPortTable_Object(
    (1, 3, 111, 2, 802, 1, 1, 2, 1, 1, 5)
)
if mibBuilder.loadTexts:
    ieee8021BridgeBaseIfToPortTable.setStatus("current")
_Ieee8021BridgeBaseIfToPortEntry_Object = MibTableRow
ieee8021BridgeBaseIfToPortEntry = _Ieee8021BridgeBaseIfToPortEntry_Object(
    (1, 3, 111, 2, 802, 1, 1, 2, 1, 1, 5, 1)
)
ieee8021BridgeBaseIfToPortEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    ieee8021BridgeBaseIfToPortEntry.setStatus("current")
_Ieee8021BridgeBaseIfIndexComponentId_Type = IEEE8021PbbComponentIdentifier
_Ieee8021BridgeBaseIfIndexComponentId_Object = MibTableColumn
ieee8021BridgeBaseIfIndexComponentId = _Ieee8021BridgeBaseIfIndexComponentId_Object(
    (1, 3, 111, 2, 802, 1, 1, 2, 1, 1, 5, 1, 1),
    _Ieee8021BridgeBaseIfIndexComponentId_Type()
)
ieee8021BridgeBaseIfIndexComponentId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021BridgeBaseIfIndexComponentId.setStatus("current")
_Ieee8021BridgeBaseIfIndexPort_Type = IEEE8021BridgePortNumber
_Ieee8021BridgeBaseIfIndexPort_Object = MibTableColumn
ieee8021BridgeBaseIfIndexPort = _Ieee8021BridgeBaseIfIndexPort_Object(
    (1, 3, 111, 2, 802, 1, 1, 2, 1, 1, 5, 1, 2),
    _Ieee8021BridgeBaseIfIndexPort_Type()
)
ieee8021BridgeBaseIfIndexPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021BridgeBaseIfIndexPort.setStatus("current")
_Ieee8021BridgePhyPortTable_Object = MibTable
ieee8021BridgePhyPortTable = _Ieee8021BridgePhyPortTable_Object(
    (1, 3, 111, 2, 802, 1, 1, 2, 1, 1, 6)
)
if mibBuilder.loadTexts:
    ieee8021BridgePhyPortTable.setStatus("current")
_Ieee8021BridgePhyPortEntry_Object = MibTableRow
ieee8021BridgePhyPortEntry = _Ieee8021BridgePhyPortEntry_Object(
    (1, 3, 111, 2, 802, 1, 1, 2, 1, 1, 6, 1)
)
ieee8021BridgePhyPortEntry.setIndexNames(
    (0, "IEEE8021-BRIDGE-MIB", "ieee8021BridgePhyPort"),
)
if mibBuilder.loadTexts:
    ieee8021BridgePhyPortEntry.setStatus("current")
_Ieee8021BridgePhyPort_Type = IEEE8021BridgePortNumber
_Ieee8021BridgePhyPort_Object = MibTableColumn
ieee8021BridgePhyPort = _Ieee8021BridgePhyPort_Object(
    (1, 3, 111, 2, 802, 1, 1, 2, 1, 1, 6, 1, 1),
    _Ieee8021BridgePhyPort_Type()
)
ieee8021BridgePhyPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ieee8021BridgePhyPort.setStatus("current")
_Ieee8021BridgePhyPortIfIndex_Type = InterfaceIndexOrZero
_Ieee8021BridgePhyPortIfIndex_Object = MibTableColumn
ieee8021BridgePhyPortIfIndex = _Ieee8021BridgePhyPortIfIndex_Object(
    (1, 3, 111, 2, 802, 1, 1, 2, 1, 1, 6, 1, 2),
    _Ieee8021BridgePhyPortIfIndex_Type()
)
ieee8021BridgePhyPortIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021BridgePhyPortIfIndex.setStatus("current")
_Ieee8021BridgePhyMacAddress_Type = MacAddress
_Ieee8021BridgePhyMacAddress_Object = MibTableColumn
ieee8021BridgePhyMacAddress = _Ieee8021BridgePhyMacAddress_Object(
    (1, 3, 111, 2, 802, 1, 1, 2, 1, 1, 6, 1, 3),
    _Ieee8021BridgePhyMacAddress_Type()
)
ieee8021BridgePhyMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021BridgePhyMacAddress.setStatus("current")
_Ieee8021BridgePhyPortToComponentId_Type = IEEE8021PbbComponentIdentifierOrZero
_Ieee8021BridgePhyPortToComponentId_Object = MibTableColumn
ieee8021BridgePhyPortToComponentId = _Ieee8021BridgePhyPortToComponentId_Object(
    (1, 3, 111, 2, 802, 1, 1, 2, 1, 1, 6, 1, 4),
    _Ieee8021BridgePhyPortToComponentId_Type()
)
ieee8021BridgePhyPortToComponentId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021BridgePhyPortToComponentId.setStatus("current")
_Ieee8021BridgePhyPortToInternalPort_Type = IEEE8021BridgePortNumberOrZero
_Ieee8021BridgePhyPortToInternalPort_Object = MibTableColumn
ieee8021BridgePhyPortToInternalPort = _Ieee8021BridgePhyPortToInternalPort_Object(
    (1, 3, 111, 2, 802, 1, 1, 2, 1, 1, 6, 1, 5),
    _Ieee8021BridgePhyPortToInternalPort_Type()
)
ieee8021BridgePhyPortToInternalPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021BridgePhyPortToInternalPort.setStatus("current")
_Ieee8021BridgeTp_ObjectIdentity = ObjectIdentity
ieee8021BridgeTp = _Ieee8021BridgeTp_ObjectIdentity(
    (1, 3, 111, 2, 802, 1, 1, 2, 1, 2)
)
_Ieee8021BridgeTpPortTable_Object = MibTable
ieee8021BridgeTpPortTable = _Ieee8021BridgeTpPortTable_Object(
    (1, 3, 111, 2, 802, 1, 1, 2, 1, 2, 1)
)
if mibBuilder.loadTexts:
    ieee8021BridgeTpPortTable.setStatus("current")
_Ieee8021BridgeTpPortEntry_Object = MibTableRow
ieee8021BridgeTpPortEntry = _Ieee8021BridgeTpPortEntry_Object(
    (1, 3, 111, 2, 802, 1, 1, 2, 1, 2, 1, 1)
)
ieee8021BridgeTpPortEntry.setIndexNames(
    (0, "IEEE8021-BRIDGE-MIB", "ieee8021BridgeTpPortComponentId"),
    (0, "IEEE8021-BRIDGE-MIB", "ieee8021BridgeTpPort"),
)
if mibBuilder.loadTexts:
    ieee8021BridgeTpPortEntry.setStatus("current")
_Ieee8021BridgeTpPortComponentId_Type = IEEE8021PbbComponentIdentifier
_Ieee8021BridgeTpPortComponentId_Object = MibTableColumn
ieee8021BridgeTpPortComponentId = _Ieee8021BridgeTpPortComponentId_Object(
    (1, 3, 111, 2, 802, 1, 1, 2, 1, 2, 1, 1, 1),
    _Ieee8021BridgeTpPortComponentId_Type()
)
ieee8021BridgeTpPortComponentId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ieee8021BridgeTpPortComponentId.setStatus("current")
_Ieee8021BridgeTpPort_Type = IEEE8021BridgePortNumber
_Ieee8021BridgeTpPort_Object = MibTableColumn
ieee8021BridgeTpPort = _Ieee8021BridgeTpPort_Object(
    (1, 3, 111, 2, 802, 1, 1, 2, 1, 2, 1, 1, 2),
    _Ieee8021BridgeTpPort_Type()
)
ieee8021BridgeTpPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ieee8021BridgeTpPort.setStatus("current")
_Ieee8021BridgeTpPortMaxInfo_Type = Integer32
_Ieee8021BridgeTpPortMaxInfo_Object = MibTableColumn
ieee8021BridgeTpPortMaxInfo = _Ieee8021BridgeTpPortMaxInfo_Object(
    (1, 3, 111, 2, 802, 1, 1, 2, 1, 2, 1, 1, 3),
    _Ieee8021BridgeTpPortMaxInfo_Type()
)
ieee8021BridgeTpPortMaxInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021BridgeTpPortMaxInfo.setStatus("current")
if mibBuilder.loadTexts:
    ieee8021BridgeTpPortMaxInfo.setUnits("bytes")
_Ieee8021BridgeTpPortInFrames_Type = Counter64
_Ieee8021BridgeTpPortInFrames_Object = MibTableColumn
ieee8021BridgeTpPortInFrames = _Ieee8021BridgeTpPortInFrames_Object(
    (1, 3, 111, 2, 802, 1, 1, 2, 1, 2, 1, 1, 4),
    _Ieee8021BridgeTpPortInFrames_Type()
)
ieee8021BridgeTpPortInFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021BridgeTpPortInFrames.setStatus("current")
if mibBuilder.loadTexts:
    ieee8021BridgeTpPortInFrames.setUnits("frames")
_Ieee8021BridgeTpPortOutFrames_Type = Counter64
_Ieee8021BridgeTpPortOutFrames_Object = MibTableColumn
ieee8021BridgeTpPortOutFrames = _Ieee8021BridgeTpPortOutFrames_Object(
    (1, 3, 111, 2, 802, 1, 1, 2, 1, 2, 1, 1, 5),
    _Ieee8021BridgeTpPortOutFrames_Type()
)
ieee8021BridgeTpPortOutFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021BridgeTpPortOutFrames.setStatus("current")
if mibBuilder.loadTexts:
    ieee8021BridgeTpPortOutFrames.setUnits("frames")
_Ieee8021BridgeTpPortInDiscards_Type = Counter64
_Ieee8021BridgeTpPortInDiscards_Object = MibTableColumn
ieee8021BridgeTpPortInDiscards = _Ieee8021BridgeTpPortInDiscards_Object(
    (1, 3, 111, 2, 802, 1, 1, 2, 1, 2, 1, 1, 6),
    _Ieee8021BridgeTpPortInDiscards_Type()
)
ieee8021BridgeTpPortInDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021BridgeTpPortInDiscards.setStatus("current")
if mibBuilder.loadTexts:
    ieee8021BridgeTpPortInDiscards.setUnits("frames")
_Ieee8021BridgePriority_ObjectIdentity = ObjectIdentity
ieee8021BridgePriority = _Ieee8021BridgePriority_ObjectIdentity(
    (1, 3, 111, 2, 802, 1, 1, 2, 1, 3)
)
_Ieee8021BridgePortPriorityTable_Object = MibTable
ieee8021BridgePortPriorityTable = _Ieee8021BridgePortPriorityTable_Object(
    (1, 3, 111, 2, 802, 1, 1, 2, 1, 3, 1)
)
if mibBuilder.loadTexts:
    ieee8021BridgePortPriorityTable.setStatus("current")
_Ieee8021BridgePortPriorityEntry_Object = MibTableRow
ieee8021BridgePortPriorityEntry = _Ieee8021BridgePortPriorityEntry_Object(
    (1, 3, 111, 2, 802, 1, 1, 2, 1, 3, 1, 1)
)
if mibBuilder.loadTexts:
    ieee8021BridgePortPriorityEntry.setStatus("current")
_Ieee8021BridgePortDefaultUserPriority_Type = IEEE8021PriorityValue
_Ieee8021BridgePortDefaultUserPriority_Object = MibTableColumn
ieee8021BridgePortDefaultUserPriority = _Ieee8021BridgePortDefaultUserPriority_Object(
    (1, 3, 111, 2, 802, 1, 1, 2, 1, 3, 1, 1, 1),
    _Ieee8021BridgePortDefaultUserPriority_Type()
)
ieee8021BridgePortDefaultUserPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ieee8021BridgePortDefaultUserPriority.setStatus("current")


class _Ieee8021BridgePortNumTrafficClasses_Type(Integer32):
    """Custom type ieee8021BridgePortNumTrafficClasses based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_Ieee8021BridgePortNumTrafficClasses_Type.__name__ = "Integer32"
_Ieee8021BridgePortNumTrafficClasses_Object = MibTableColumn
ieee8021BridgePortNumTrafficClasses = _Ieee8021BridgePortNumTrafficClasses_Object(
    (1, 3, 111, 2, 802, 1, 1, 2, 1, 3, 1, 1, 2),
    _Ieee8021BridgePortNumTrafficClasses_Type()
)
ieee8021BridgePortNumTrafficClasses.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ieee8021BridgePortNumTrafficClasses.setStatus("current")
_Ieee8021BridgePortPriorityCodePointSelection_Type = IEEE8021PriorityCodePoint
_Ieee8021BridgePortPriorityCodePointSelection_Object = MibTableColumn
ieee8021BridgePortPriorityCodePointSelection = _Ieee8021BridgePortPriorityCodePointSelection_Object(
    (1, 3, 111, 2, 802, 1, 1, 2, 1, 3, 1, 1, 3),
    _Ieee8021BridgePortPriorityCodePointSelection_Type()
)
ieee8021BridgePortPriorityCodePointSelection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ieee8021BridgePortPriorityCodePointSelection.setStatus("current")
_Ieee8021BridgePortUseDEI_Type = TruthValue
_Ieee8021BridgePortUseDEI_Object = MibTableColumn
ieee8021BridgePortUseDEI = _Ieee8021BridgePortUseDEI_Object(
    (1, 3, 111, 2, 802, 1, 1, 2, 1, 3, 1, 1, 4),
    _Ieee8021BridgePortUseDEI_Type()
)
ieee8021BridgePortUseDEI.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ieee8021BridgePortUseDEI.setStatus("current")


class _Ieee8021BridgePortRequireDropEncoding_Type(TruthValue):
    """Custom type ieee8021BridgePortRequireDropEncoding based on TruthValue"""


_Ieee8021BridgePortRequireDropEncoding_Object = MibTableColumn
ieee8021BridgePortRequireDropEncoding = _Ieee8021BridgePortRequireDropEncoding_Object(
    (1, 3, 111, 2, 802, 1, 1, 2, 1, 3, 1, 1, 5),
    _Ieee8021BridgePortRequireDropEncoding_Type()
)
ieee8021BridgePortRequireDropEncoding.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ieee8021BridgePortRequireDropEncoding.setStatus("current")
_Ieee8021BridgePortServiceAccessPrioritySelection_Type = TruthValue
_Ieee8021BridgePortServiceAccessPrioritySelection_Object = MibTableColumn
ieee8021BridgePortServiceAccessPrioritySelection = _Ieee8021BridgePortServiceAccessPrioritySelection_Object(
    (1, 3, 111, 2, 802, 1, 1, 2, 1, 3, 1, 1, 6),
    _Ieee8021BridgePortServiceAccessPrioritySelection_Type()
)
ieee8021BridgePortServiceAccessPrioritySelection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ieee8021BridgePortServiceAccessPrioritySelection.setStatus("current")
_Ieee8021BridgeUserPriorityRegenTable_Object = MibTable
ieee8021BridgeUserPriorityRegenTable = _Ieee8021BridgeUserPriorityRegenTable_Object(
    (1, 3, 111, 2, 802, 1, 1, 2, 1, 3, 2)
)
if mibBuilder.loadTexts:
    ieee8021BridgeUserPriorityRegenTable.setStatus("current")
_Ieee8021BridgeUserPriorityRegenEntry_Object = MibTableRow
ieee8021BridgeUserPriorityRegenEntry = _Ieee8021BridgeUserPriorityRegenEntry_Object(
    (1, 3, 111, 2, 802, 1, 1, 2, 1, 3, 2, 1)
)
ieee8021BridgeUserPriorityRegenEntry.setIndexNames(
    (0, "IEEE8021-BRIDGE-MIB", "ieee8021BridgeBasePortComponentId"),
    (0, "IEEE8021-BRIDGE-MIB", "ieee8021BridgeBasePort"),
    (0, "IEEE8021-BRIDGE-MIB", "ieee8021BridgeUserPriority"),
)
if mibBuilder.loadTexts:
    ieee8021BridgeUserPriorityRegenEntry.setStatus("current")
_Ieee8021BridgeUserPriority_Type = IEEE8021PriorityValue
_Ieee8021BridgeUserPriority_Object = MibTableColumn
ieee8021BridgeUserPriority = _Ieee8021BridgeUserPriority_Object(
    (1, 3, 111, 2, 802, 1, 1, 2, 1, 3, 2, 1, 1),
    _Ieee8021BridgeUserPriority_Type()
)
ieee8021BridgeUserPriority.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ieee8021BridgeUserPriority.setStatus("current")
_Ieee8021BridgeRegenUserPriority_Type = IEEE8021PriorityValue
_Ieee8021BridgeRegenUserPriority_Object = MibTableColumn
ieee8021BridgeRegenUserPriority = _Ieee8021BridgeRegenUserPriority_Object(
    (1, 3, 111, 2, 802, 1, 1, 2, 1, 3, 2, 1, 2),
    _Ieee8021BridgeRegenUserPriority_Type()
)
ieee8021BridgeRegenUserPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ieee8021BridgeRegenUserPriority.setStatus("current")
_Ieee8021BridgeTrafficClassTable_Object = MibTable
ieee8021BridgeTrafficClassTable = _Ieee8021BridgeTrafficClassTable_Object(
    (1, 3, 111, 2, 802, 1, 1, 2, 1, 3, 3)
)
if mibBuilder.loadTexts:
    ieee8021BridgeTrafficClassTable.setStatus("current")
_Ieee8021BridgeTrafficClassEntry_Object = MibTableRow
ieee8021BridgeTrafficClassEntry = _Ieee8021BridgeTrafficClassEntry_Object(
    (1, 3, 111, 2, 802, 1, 1, 2, 1, 3, 3, 1)
)
ieee8021BridgeTrafficClassEntry.setIndexNames(
    (0, "IEEE8021-BRIDGE-MIB", "ieee8021BridgeBasePortComponentId"),
    (0, "IEEE8021-BRIDGE-MIB", "ieee8021BridgeBasePort"),
    (0, "IEEE8021-BRIDGE-MIB", "ieee8021BridgeTrafficClassPriority"),
)
if mibBuilder.loadTexts:
    ieee8021BridgeTrafficClassEntry.setStatus("current")
_Ieee8021BridgeTrafficClassPriority_Type = IEEE8021PriorityValue
_Ieee8021BridgeTrafficClassPriority_Object = MibTableColumn
ieee8021BridgeTrafficClassPriority = _Ieee8021BridgeTrafficClassPriority_Object(
    (1, 3, 111, 2, 802, 1, 1, 2, 1, 3, 3, 1, 1),
    _Ieee8021BridgeTrafficClassPriority_Type()
)
ieee8021BridgeTrafficClassPriority.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ieee8021BridgeTrafficClassPriority.setStatus("current")


class _Ieee8021BridgeTrafficClass_Type(Integer32):
    """Custom type ieee8021BridgeTrafficClass based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_Ieee8021BridgeTrafficClass_Type.__name__ = "Integer32"
_Ieee8021BridgeTrafficClass_Object = MibTableColumn
ieee8021BridgeTrafficClass = _Ieee8021BridgeTrafficClass_Object(
    (1, 3, 111, 2, 802, 1, 1, 2, 1, 3, 3, 1, 2),
    _Ieee8021BridgeTrafficClass_Type()
)
ieee8021BridgeTrafficClass.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ieee8021BridgeTrafficClass.setStatus("current")
_Ieee8021BridgePortOutboundAccessPriorityTable_Object = MibTable
ieee8021BridgePortOutboundAccessPriorityTable = _Ieee8021BridgePortOutboundAccessPriorityTable_Object(
    (1, 3, 111, 2, 802, 1, 1, 2, 1, 3, 4)
)
if mibBuilder.loadTexts:
    ieee8021BridgePortOutboundAccessPriorityTable.setStatus("current")
_Ieee8021BridgePortOutboundAccessPriorityEntry_Object = MibTableRow
ieee8021BridgePortOutboundAccessPriorityEntry = _Ieee8021BridgePortOutboundAccessPriorityEntry_Object(
    (1, 3, 111, 2, 802, 1, 1, 2, 1, 3, 4, 1)
)
ieee8021BridgePortOutboundAccessPriorityEntry.setIndexNames(
    (0, "IEEE8021-BRIDGE-MIB", "ieee8021BridgeBasePortComponentId"),
    (0, "IEEE8021-BRIDGE-MIB", "ieee8021BridgeBasePort"),
    (0, "IEEE8021-BRIDGE-MIB", "ieee8021BridgeRegenUserPriority"),
)
if mibBuilder.loadTexts:
    ieee8021BridgePortOutboundAccessPriorityEntry.setStatus("current")
_Ieee8021BridgePortOutboundAccessPriority_Type = IEEE8021PriorityValue
_Ieee8021BridgePortOutboundAccessPriority_Object = MibTableColumn
ieee8021BridgePortOutboundAccessPriority = _Ieee8021BridgePortOutboundAccessPriority_Object(
    (1, 3, 111, 2, 802, 1, 1, 2, 1, 3, 4, 1, 1),
    _Ieee8021BridgePortOutboundAccessPriority_Type()
)
ieee8021BridgePortOutboundAccessPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021BridgePortOutboundAccessPriority.setStatus("current")
_Ieee8021BridgePortDecodingTable_Object = MibTable
ieee8021BridgePortDecodingTable = _Ieee8021BridgePortDecodingTable_Object(
    (1, 3, 111, 2, 802, 1, 1, 2, 1, 3, 5)
)
if mibBuilder.loadTexts:
    ieee8021BridgePortDecodingTable.setStatus("current")
_Ieee8021BridgePortDecodingEntry_Object = MibTableRow
ieee8021BridgePortDecodingEntry = _Ieee8021BridgePortDecodingEntry_Object(
    (1, 3, 111, 2, 802, 1, 1, 2, 1, 3, 5, 1)
)
ieee8021BridgePortDecodingEntry.setIndexNames(
    (0, "IEEE8021-BRIDGE-MIB", "ieee8021BridgePortDecodingComponentId"),
    (0, "IEEE8021-BRIDGE-MIB", "ieee8021BridgePortDecodingPortNum"),
    (0, "IEEE8021-BRIDGE-MIB", "ieee8021BridgePortDecodingPriorityCodePointRow"),
    (0, "IEEE8021-BRIDGE-MIB", "ieee8021BridgePortDecodingPriorityCodePoint"),
)
if mibBuilder.loadTexts:
    ieee8021BridgePortDecodingEntry.setStatus("current")
_Ieee8021BridgePortDecodingComponentId_Type = IEEE8021PbbComponentIdentifier
_Ieee8021BridgePortDecodingComponentId_Object = MibTableColumn
ieee8021BridgePortDecodingComponentId = _Ieee8021BridgePortDecodingComponentId_Object(
    (1, 3, 111, 2, 802, 1, 1, 2, 1, 3, 5, 1, 1),
    _Ieee8021BridgePortDecodingComponentId_Type()
)
ieee8021BridgePortDecodingComponentId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ieee8021BridgePortDecodingComponentId.setStatus("current")
_Ieee8021BridgePortDecodingPortNum_Type = IEEE8021BridgePortNumber
_Ieee8021BridgePortDecodingPortNum_Object = MibTableColumn
ieee8021BridgePortDecodingPortNum = _Ieee8021BridgePortDecodingPortNum_Object(
    (1, 3, 111, 2, 802, 1, 1, 2, 1, 3, 5, 1, 2),
    _Ieee8021BridgePortDecodingPortNum_Type()
)
ieee8021BridgePortDecodingPortNum.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ieee8021BridgePortDecodingPortNum.setStatus("current")
_Ieee8021BridgePortDecodingPriorityCodePointRow_Type = IEEE8021PriorityCodePoint
_Ieee8021BridgePortDecodingPriorityCodePointRow_Object = MibTableColumn
ieee8021BridgePortDecodingPriorityCodePointRow = _Ieee8021BridgePortDecodingPriorityCodePointRow_Object(
    (1, 3, 111, 2, 802, 1, 1, 2, 1, 3, 5, 1, 3),
    _Ieee8021BridgePortDecodingPriorityCodePointRow_Type()
)
ieee8021BridgePortDecodingPriorityCodePointRow.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ieee8021BridgePortDecodingPriorityCodePointRow.setStatus("current")


class _Ieee8021BridgePortDecodingPriorityCodePoint_Type(Integer32):
    """Custom type ieee8021BridgePortDecodingPriorityCodePoint based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_Ieee8021BridgePortDecodingPriorityCodePoint_Type.__name__ = "Integer32"
_Ieee8021BridgePortDecodingPriorityCodePoint_Object = MibTableColumn
ieee8021BridgePortDecodingPriorityCodePoint = _Ieee8021BridgePortDecodingPriorityCodePoint_Object(
    (1, 3, 111, 2, 802, 1, 1, 2, 1, 3, 5, 1, 4),
    _Ieee8021BridgePortDecodingPriorityCodePoint_Type()
)
ieee8021BridgePortDecodingPriorityCodePoint.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ieee8021BridgePortDecodingPriorityCodePoint.setStatus("current")
_Ieee8021BridgePortDecodingPriority_Type = IEEE8021PriorityValue
_Ieee8021BridgePortDecodingPriority_Object = MibTableColumn
ieee8021BridgePortDecodingPriority = _Ieee8021BridgePortDecodingPriority_Object(
    (1, 3, 111, 2, 802, 1, 1, 2, 1, 3, 5, 1, 5),
    _Ieee8021BridgePortDecodingPriority_Type()
)
ieee8021BridgePortDecodingPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ieee8021BridgePortDecodingPriority.setStatus("current")
_Ieee8021BridgePortDecodingDropEligible_Type = TruthValue
_Ieee8021BridgePortDecodingDropEligible_Object = MibTableColumn
ieee8021BridgePortDecodingDropEligible = _Ieee8021BridgePortDecodingDropEligible_Object(
    (1, 3, 111, 2, 802, 1, 1, 2, 1, 3, 5, 1, 6),
    _Ieee8021BridgePortDecodingDropEligible_Type()
)
ieee8021BridgePortDecodingDropEligible.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ieee8021BridgePortDecodingDropEligible.setStatus("current")
_Ieee8021BridgePortEncodingTable_Object = MibTable
ieee8021BridgePortEncodingTable = _Ieee8021BridgePortEncodingTable_Object(
    (1, 3, 111, 2, 802, 1, 1, 2, 1, 3, 6)
)
if mibBuilder.loadTexts:
    ieee8021BridgePortEncodingTable.setStatus("current")
_Ieee8021BridgePortEncodingEntry_Object = MibTableRow
ieee8021BridgePortEncodingEntry = _Ieee8021BridgePortEncodingEntry_Object(
    (1, 3, 111, 2, 802, 1, 1, 2, 1, 3, 6, 1)
)
ieee8021BridgePortEncodingEntry.setIndexNames(
    (0, "IEEE8021-BRIDGE-MIB", "ieee8021BridgePortEncodingComponentId"),
    (0, "IEEE8021-BRIDGE-MIB", "ieee8021BridgePortEncodingPortNum"),
    (0, "IEEE8021-BRIDGE-MIB", "ieee8021BridgePortEncodingPriorityCodePointRow"),
    (0, "IEEE8021-BRIDGE-MIB", "ieee8021BridgePortEncodingPriorityCodePoint"),
    (0, "IEEE8021-BRIDGE-MIB", "ieee8021BridgePortEncodingDropEligible"),
)
if mibBuilder.loadTexts:
    ieee8021BridgePortEncodingEntry.setStatus("current")
_Ieee8021BridgePortEncodingComponentId_Type = IEEE8021PbbComponentIdentifier
_Ieee8021BridgePortEncodingComponentId_Object = MibTableColumn
ieee8021BridgePortEncodingComponentId = _Ieee8021BridgePortEncodingComponentId_Object(
    (1, 3, 111, 2, 802, 1, 1, 2, 1, 3, 6, 1, 1),
    _Ieee8021BridgePortEncodingComponentId_Type()
)
ieee8021BridgePortEncodingComponentId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ieee8021BridgePortEncodingComponentId.setStatus("current")
_Ieee8021BridgePortEncodingPortNum_Type = IEEE8021BridgePortNumber
_Ieee8021BridgePortEncodingPortNum_Object = MibTableColumn
ieee8021BridgePortEncodingPortNum = _Ieee8021BridgePortEncodingPortNum_Object(
    (1, 3, 111, 2, 802, 1, 1, 2, 1, 3, 6, 1, 2),
    _Ieee8021BridgePortEncodingPortNum_Type()
)
ieee8021BridgePortEncodingPortNum.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ieee8021BridgePortEncodingPortNum.setStatus("current")
_Ieee8021BridgePortEncodingPriorityCodePointRow_Type = IEEE8021PriorityCodePoint
_Ieee8021BridgePortEncodingPriorityCodePointRow_Object = MibTableColumn
ieee8021BridgePortEncodingPriorityCodePointRow = _Ieee8021BridgePortEncodingPriorityCodePointRow_Object(
    (1, 3, 111, 2, 802, 1, 1, 2, 1, 3, 6, 1, 3),
    _Ieee8021BridgePortEncodingPriorityCodePointRow_Type()
)
ieee8021BridgePortEncodingPriorityCodePointRow.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ieee8021BridgePortEncodingPriorityCodePointRow.setStatus("current")


class _Ieee8021BridgePortEncodingPriorityCodePoint_Type(Integer32):
    """Custom type ieee8021BridgePortEncodingPriorityCodePoint based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_Ieee8021BridgePortEncodingPriorityCodePoint_Type.__name__ = "Integer32"
_Ieee8021BridgePortEncodingPriorityCodePoint_Object = MibTableColumn
ieee8021BridgePortEncodingPriorityCodePoint = _Ieee8021BridgePortEncodingPriorityCodePoint_Object(
    (1, 3, 111, 2, 802, 1, 1, 2, 1, 3, 6, 1, 4),
    _Ieee8021BridgePortEncodingPriorityCodePoint_Type()
)
ieee8021BridgePortEncodingPriorityCodePoint.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ieee8021BridgePortEncodingPriorityCodePoint.setStatus("current")
_Ieee8021BridgePortEncodingDropEligible_Type = TruthValue
_Ieee8021BridgePortEncodingDropEligible_Object = MibTableColumn
ieee8021BridgePortEncodingDropEligible = _Ieee8021BridgePortEncodingDropEligible_Object(
    (1, 3, 111, 2, 802, 1, 1, 2, 1, 3, 6, 1, 5),
    _Ieee8021BridgePortEncodingDropEligible_Type()
)
ieee8021BridgePortEncodingDropEligible.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ieee8021BridgePortEncodingDropEligible.setStatus("current")
_Ieee8021BridgePortEncodingPriority_Type = IEEE8021PriorityValue
_Ieee8021BridgePortEncodingPriority_Object = MibTableColumn
ieee8021BridgePortEncodingPriority = _Ieee8021BridgePortEncodingPriority_Object(
    (1, 3, 111, 2, 802, 1, 1, 2, 1, 3, 6, 1, 6),
    _Ieee8021BridgePortEncodingPriority_Type()
)
ieee8021BridgePortEncodingPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ieee8021BridgePortEncodingPriority.setStatus("current")
_Ieee8021BridgeServiceAccessPriorityTable_Object = MibTable
ieee8021BridgeServiceAccessPriorityTable = _Ieee8021BridgeServiceAccessPriorityTable_Object(
    (1, 3, 111, 2, 802, 1, 1, 2, 1, 3, 7)
)
if mibBuilder.loadTexts:
    ieee8021BridgeServiceAccessPriorityTable.setStatus("current")
_Ieee8021BridgeServiceAccessPriorityEntry_Object = MibTableRow
ieee8021BridgeServiceAccessPriorityEntry = _Ieee8021BridgeServiceAccessPriorityEntry_Object(
    (1, 3, 111, 2, 802, 1, 1, 2, 1, 3, 7, 1)
)
ieee8021BridgeServiceAccessPriorityEntry.setIndexNames(
    (0, "IEEE8021-BRIDGE-MIB", "ieee8021BridgeServiceAccessPriorityComponentId"),
    (0, "IEEE8021-BRIDGE-MIB", "ieee8021BridgeServiceAccessPriorityPortNum"),
    (0, "IEEE8021-BRIDGE-MIB", "ieee8021BridgeServiceAccessPriorityReceived"),
)
if mibBuilder.loadTexts:
    ieee8021BridgeServiceAccessPriorityEntry.setStatus("current")
_Ieee8021BridgeServiceAccessPriorityComponentId_Type = IEEE8021PbbComponentIdentifier
_Ieee8021BridgeServiceAccessPriorityComponentId_Object = MibTableColumn
ieee8021BridgeServiceAccessPriorityComponentId = _Ieee8021BridgeServiceAccessPriorityComponentId_Object(
    (1, 3, 111, 2, 802, 1, 1, 2, 1, 3, 7, 1, 1),
    _Ieee8021BridgeServiceAccessPriorityComponentId_Type()
)
ieee8021BridgeServiceAccessPriorityComponentId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ieee8021BridgeServiceAccessPriorityComponentId.setStatus("current")
_Ieee8021BridgeServiceAccessPriorityPortNum_Type = IEEE8021BridgePortNumber
_Ieee8021BridgeServiceAccessPriorityPortNum_Object = MibTableColumn
ieee8021BridgeServiceAccessPriorityPortNum = _Ieee8021BridgeServiceAccessPriorityPortNum_Object(
    (1, 3, 111, 2, 802, 1, 1, 2, 1, 3, 7, 1, 2),
    _Ieee8021BridgeServiceAccessPriorityPortNum_Type()
)
ieee8021BridgeServiceAccessPriorityPortNum.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ieee8021BridgeServiceAccessPriorityPortNum.setStatus("current")
_Ieee8021BridgeServiceAccessPriorityReceived_Type = IEEE8021PriorityValue
_Ieee8021BridgeServiceAccessPriorityReceived_Object = MibTableColumn
ieee8021BridgeServiceAccessPriorityReceived = _Ieee8021BridgeServiceAccessPriorityReceived_Object(
    (1, 3, 111, 2, 802, 1, 1, 2, 1, 3, 7, 1, 3),
    _Ieee8021BridgeServiceAccessPriorityReceived_Type()
)
ieee8021BridgeServiceAccessPriorityReceived.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ieee8021BridgeServiceAccessPriorityReceived.setStatus("current")
_Ieee8021BridgeServiceAccessPriorityValue_Type = IEEE8021PriorityValue
_Ieee8021BridgeServiceAccessPriorityValue_Object = MibTableColumn
ieee8021BridgeServiceAccessPriorityValue = _Ieee8021BridgeServiceAccessPriorityValue_Object(
    (1, 3, 111, 2, 802, 1, 1, 2, 1, 3, 7, 1, 4),
    _Ieee8021BridgeServiceAccessPriorityValue_Type()
)
ieee8021BridgeServiceAccessPriorityValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ieee8021BridgeServiceAccessPriorityValue.setStatus("current")
_Ieee8021BridgeMrp_ObjectIdentity = ObjectIdentity
ieee8021BridgeMrp = _Ieee8021BridgeMrp_ObjectIdentity(
    (1, 3, 111, 2, 802, 1, 1, 2, 1, 4)
)
_Ieee8021BridgePortMrpTable_Object = MibTable
ieee8021BridgePortMrpTable = _Ieee8021BridgePortMrpTable_Object(
    (1, 3, 111, 2, 802, 1, 1, 2, 1, 4, 1)
)
if mibBuilder.loadTexts:
    ieee8021BridgePortMrpTable.setStatus("current")
_Ieee8021BridgePortMrpEntry_Object = MibTableRow
ieee8021BridgePortMrpEntry = _Ieee8021BridgePortMrpEntry_Object(
    (1, 3, 111, 2, 802, 1, 1, 2, 1, 4, 1, 1)
)
if mibBuilder.loadTexts:
    ieee8021BridgePortMrpEntry.setStatus("current")


class _Ieee8021BridgePortMrpJoinTime_Type(TimeInterval):
    """Custom type ieee8021BridgePortMrpJoinTime based on TimeInterval"""
    defaultValue = 20


_Ieee8021BridgePortMrpJoinTime_Object = MibTableColumn
ieee8021BridgePortMrpJoinTime = _Ieee8021BridgePortMrpJoinTime_Object(
    (1, 3, 111, 2, 802, 1, 1, 2, 1, 4, 1, 1, 1),
    _Ieee8021BridgePortMrpJoinTime_Type()
)
ieee8021BridgePortMrpJoinTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ieee8021BridgePortMrpJoinTime.setStatus("current")
if mibBuilder.loadTexts:
    ieee8021BridgePortMrpJoinTime.setUnits("centi-seconds")


class _Ieee8021BridgePortMrpLeaveTime_Type(TimeInterval):
    """Custom type ieee8021BridgePortMrpLeaveTime based on TimeInterval"""
    defaultValue = 60


_Ieee8021BridgePortMrpLeaveTime_Object = MibTableColumn
ieee8021BridgePortMrpLeaveTime = _Ieee8021BridgePortMrpLeaveTime_Object(
    (1, 3, 111, 2, 802, 1, 1, 2, 1, 4, 1, 1, 2),
    _Ieee8021BridgePortMrpLeaveTime_Type()
)
ieee8021BridgePortMrpLeaveTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ieee8021BridgePortMrpLeaveTime.setStatus("current")
if mibBuilder.loadTexts:
    ieee8021BridgePortMrpLeaveTime.setUnits("centi-seconds")


class _Ieee8021BridgePortMrpLeaveAllTime_Type(TimeInterval):
    """Custom type ieee8021BridgePortMrpLeaveAllTime based on TimeInterval"""
    defaultValue = 1000


_Ieee8021BridgePortMrpLeaveAllTime_Object = MibTableColumn
ieee8021BridgePortMrpLeaveAllTime = _Ieee8021BridgePortMrpLeaveAllTime_Object(
    (1, 3, 111, 2, 802, 1, 1, 2, 1, 4, 1, 1, 3),
    _Ieee8021BridgePortMrpLeaveAllTime_Type()
)
ieee8021BridgePortMrpLeaveAllTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ieee8021BridgePortMrpLeaveAllTime.setStatus("current")
if mibBuilder.loadTexts:
    ieee8021BridgePortMrpLeaveAllTime.setUnits("centi-seconds")
_Ieee8021BridgeMmrp_ObjectIdentity = ObjectIdentity
ieee8021BridgeMmrp = _Ieee8021BridgeMmrp_ObjectIdentity(
    (1, 3, 111, 2, 802, 1, 1, 2, 1, 5)
)
_Ieee8021BridgePortMmrpTable_Object = MibTable
ieee8021BridgePortMmrpTable = _Ieee8021BridgePortMmrpTable_Object(
    (1, 3, 111, 2, 802, 1, 1, 2, 1, 5, 1)
)
if mibBuilder.loadTexts:
    ieee8021BridgePortMmrpTable.setStatus("current")
_Ieee8021BridgePortMmrpEntry_Object = MibTableRow
ieee8021BridgePortMmrpEntry = _Ieee8021BridgePortMmrpEntry_Object(
    (1, 3, 111, 2, 802, 1, 1, 2, 1, 5, 1, 1)
)
if mibBuilder.loadTexts:
    ieee8021BridgePortMmrpEntry.setStatus("current")


class _Ieee8021BridgePortMmrpEnabledStatus_Type(TruthValue):
    """Custom type ieee8021BridgePortMmrpEnabledStatus based on TruthValue"""


_Ieee8021BridgePortMmrpEnabledStatus_Object = MibTableColumn
ieee8021BridgePortMmrpEnabledStatus = _Ieee8021BridgePortMmrpEnabledStatus_Object(
    (1, 3, 111, 2, 802, 1, 1, 2, 1, 5, 1, 1, 1),
    _Ieee8021BridgePortMmrpEnabledStatus_Type()
)
ieee8021BridgePortMmrpEnabledStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ieee8021BridgePortMmrpEnabledStatus.setStatus("current")
_Ieee8021BridgePortMmrpFailedRegistrations_Type = Counter64
_Ieee8021BridgePortMmrpFailedRegistrations_Object = MibTableColumn
ieee8021BridgePortMmrpFailedRegistrations = _Ieee8021BridgePortMmrpFailedRegistrations_Object(
    (1, 3, 111, 2, 802, 1, 1, 2, 1, 5, 1, 1, 2),
    _Ieee8021BridgePortMmrpFailedRegistrations_Type()
)
ieee8021BridgePortMmrpFailedRegistrations.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021BridgePortMmrpFailedRegistrations.setStatus("current")
if mibBuilder.loadTexts:
    ieee8021BridgePortMmrpFailedRegistrations.setUnits("failed MMRP registrations")
_Ieee8021BridgePortMmrpLastPduOrigin_Type = MacAddress
_Ieee8021BridgePortMmrpLastPduOrigin_Object = MibTableColumn
ieee8021BridgePortMmrpLastPduOrigin = _Ieee8021BridgePortMmrpLastPduOrigin_Object(
    (1, 3, 111, 2, 802, 1, 1, 2, 1, 5, 1, 1, 3),
    _Ieee8021BridgePortMmrpLastPduOrigin_Type()
)
ieee8021BridgePortMmrpLastPduOrigin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021BridgePortMmrpLastPduOrigin.setStatus("current")


class _Ieee8021BridgePortRestrictedGroupRegistration_Type(TruthValue):
    """Custom type ieee8021BridgePortRestrictedGroupRegistration based on TruthValue"""


_Ieee8021BridgePortRestrictedGroupRegistration_Object = MibTableColumn
ieee8021BridgePortRestrictedGroupRegistration = _Ieee8021BridgePortRestrictedGroupRegistration_Object(
    (1, 3, 111, 2, 802, 1, 1, 2, 1, 5, 1, 1, 4),
    _Ieee8021BridgePortRestrictedGroupRegistration_Type()
)
ieee8021BridgePortRestrictedGroupRegistration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ieee8021BridgePortRestrictedGroupRegistration.setStatus("current")
_Ieee8021BridgeInternalLan_ObjectIdentity = ObjectIdentity
ieee8021BridgeInternalLan = _Ieee8021BridgeInternalLan_ObjectIdentity(
    (1, 3, 111, 2, 802, 1, 1, 2, 1, 6)
)
_Ieee8021BridgeILanIfTable_Object = MibTable
ieee8021BridgeILanIfTable = _Ieee8021BridgeILanIfTable_Object(
    (1, 3, 111, 2, 802, 1, 1, 2, 1, 6, 1)
)
if mibBuilder.loadTexts:
    ieee8021BridgeILanIfTable.setStatus("current")
_Ieee8021BridgeILanIfEntry_Object = MibTableRow
ieee8021BridgeILanIfEntry = _Ieee8021BridgeILanIfEntry_Object(
    (1, 3, 111, 2, 802, 1, 1, 2, 1, 6, 1, 1)
)
ieee8021BridgeILanIfEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    ieee8021BridgeILanIfEntry.setStatus("current")
_Ieee8021BridgeILanIfRowStatus_Type = RowStatus
_Ieee8021BridgeILanIfRowStatus_Object = MibTableColumn
ieee8021BridgeILanIfRowStatus = _Ieee8021BridgeILanIfRowStatus_Object(
    (1, 3, 111, 2, 802, 1, 1, 2, 1, 6, 1, 1, 1),
    _Ieee8021BridgeILanIfRowStatus_Type()
)
ieee8021BridgeILanIfRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ieee8021BridgeILanIfRowStatus.setStatus("current")
_Ieee8021BridgeDot1d_ObjectIdentity = ObjectIdentity
ieee8021BridgeDot1d = _Ieee8021BridgeDot1d_ObjectIdentity(
    (1, 3, 111, 2, 802, 1, 1, 2, 1, 7)
)
_Ieee8021BridgeDot1dPortTable_Object = MibTable
ieee8021BridgeDot1dPortTable = _Ieee8021BridgeDot1dPortTable_Object(
    (1, 3, 111, 2, 802, 1, 1, 2, 1, 7, 1)
)
if mibBuilder.loadTexts:
    ieee8021BridgeDot1dPortTable.setStatus("current")
_Ieee8021BridgeDot1dPortEntry_Object = MibTableRow
ieee8021BridgeDot1dPortEntry = _Ieee8021BridgeDot1dPortEntry_Object(
    (1, 3, 111, 2, 802, 1, 1, 2, 1, 7, 1, 1)
)
ieee8021BridgeDot1dPortEntry.setIndexNames(
    (0, "IEEE8021-BRIDGE-MIB", "ieee8021BridgeBasePortComponentId"),
    (0, "IEEE8021-BRIDGE-MIB", "ieee8021BridgeBasePort"),
)
if mibBuilder.loadTexts:
    ieee8021BridgeDot1dPortEntry.setStatus("current")
_Ieee8021BridgeDot1dPortRowStatus_Type = RowStatus
_Ieee8021BridgeDot1dPortRowStatus_Object = MibTableColumn
ieee8021BridgeDot1dPortRowStatus = _Ieee8021BridgeDot1dPortRowStatus_Object(
    (1, 3, 111, 2, 802, 1, 1, 2, 1, 7, 1, 1, 1),
    _Ieee8021BridgeDot1dPortRowStatus_Type()
)
ieee8021BridgeDot1dPortRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ieee8021BridgeDot1dPortRowStatus.setStatus("current")
_Ieee8021BridgeConformance_ObjectIdentity = ObjectIdentity
ieee8021BridgeConformance = _Ieee8021BridgeConformance_ObjectIdentity(
    (1, 3, 111, 2, 802, 1, 1, 2, 2)
)
_Ieee8021BridgeCompliances_ObjectIdentity = ObjectIdentity
ieee8021BridgeCompliances = _Ieee8021BridgeCompliances_ObjectIdentity(
    (1, 3, 111, 2, 802, 1, 1, 2, 2, 1)
)
_Ieee8021BridgeGroups_ObjectIdentity = ObjectIdentity
ieee8021BridgeGroups = _Ieee8021BridgeGroups_ObjectIdentity(
    (1, 3, 111, 2, 802, 1, 1, 2, 2, 2)
)
ieee8021BridgeBasePortEntry.registerAugmentions(
    ("IEEE8021-BRIDGE-MIB",
     "ieee8021BridgePortPriorityEntry")
)
ieee8021BridgePortPriorityEntry.setIndexNames(*ieee8021BridgeBasePortEntry.getIndexNames())
ieee8021BridgeBasePortEntry.registerAugmentions(
    ("IEEE8021-BRIDGE-MIB",
     "ieee8021BridgePortMrpEntry")
)
ieee8021BridgePortMrpEntry.setIndexNames(*ieee8021BridgeBasePortEntry.getIndexNames())
ieee8021BridgeBasePortEntry.registerAugmentions(
    ("IEEE8021-BRIDGE-MIB",
     "ieee8021BridgePortMmrpEntry")
)
ieee8021BridgePortMmrpEntry.setIndexNames(*ieee8021BridgeBasePortEntry.getIndexNames())

# Managed Objects groups

ieee8021BridgeBaseBridgeGroup = ObjectGroup(
    (1, 3, 111, 2, 802, 1, 1, 2, 2, 2, 1)
)
ieee8021BridgeBaseBridgeGroup.setObjects(
      *(("IEEE8021-BRIDGE-MIB", "ieee8021BridgeBaseBridgeAddress"),
        ("IEEE8021-BRIDGE-MIB", "ieee8021BridgeBaseNumPorts"),
        ("IEEE8021-BRIDGE-MIB", "ieee8021BridgeBaseComponentType"))
)
if mibBuilder.loadTexts:
    ieee8021BridgeBaseBridgeGroup.setStatus("current")

ieee8021BridgeBasePortGroup = ObjectGroup(
    (1, 3, 111, 2, 802, 1, 1, 2, 2, 2, 2)
)
ieee8021BridgeBasePortGroup.setObjects(
      *(("IEEE8021-BRIDGE-MIB", "ieee8021BridgeBasePortIfIndex"),
        ("IEEE8021-BRIDGE-MIB", "ieee8021BridgeBasePortDelayExceededDiscards"),
        ("IEEE8021-BRIDGE-MIB", "ieee8021BridgeBasePortMtuExceededDiscards"),
        ("IEEE8021-BRIDGE-MIB", "ieee8021BridgeBasePortType"),
        ("IEEE8021-BRIDGE-MIB", "ieee8021BridgeBasePortExternal"),
        ("IEEE8021-BRIDGE-MIB", "ieee8021BridgeBasePortAdminPointToPoint"),
        ("IEEE8021-BRIDGE-MIB", "ieee8021BridgeBasePortOperPointToPoint"),
        ("IEEE8021-BRIDGE-MIB", "ieee8021BridgeBasePortName"))
)
if mibBuilder.loadTexts:
    ieee8021BridgeBasePortGroup.setStatus("current")

ieee8021BridgeCapGroup = ObjectGroup(
    (1, 3, 111, 2, 802, 1, 1, 2, 2, 2, 3)
)
ieee8021BridgeCapGroup.setObjects(
      *(("IEEE8021-BRIDGE-MIB", "ieee8021BridgeBaseDeviceCapabilities"),
        ("IEEE8021-BRIDGE-MIB", "ieee8021BridgeBasePortCapabilities"),
        ("IEEE8021-BRIDGE-MIB", "ieee8021BridgeBasePortTypeCapabilities"))
)
if mibBuilder.loadTexts:
    ieee8021BridgeCapGroup.setStatus("current")

ieee8021BridgeDeviceMmrpGroup = ObjectGroup(
    (1, 3, 111, 2, 802, 1, 1, 2, 2, 2, 4)
)
ieee8021BridgeDeviceMmrpGroup.setObjects(
    ("IEEE8021-BRIDGE-MIB", "ieee8021BridgeBaseMmrpEnabledStatus")
)
if mibBuilder.loadTexts:
    ieee8021BridgeDeviceMmrpGroup.setStatus("current")

ieee8021BridgeTpPortGroup = ObjectGroup(
    (1, 3, 111, 2, 802, 1, 1, 2, 2, 2, 6)
)
ieee8021BridgeTpPortGroup.setObjects(
      *(("IEEE8021-BRIDGE-MIB", "ieee8021BridgeTpPortMaxInfo"),
        ("IEEE8021-BRIDGE-MIB", "ieee8021BridgeTpPortInFrames"),
        ("IEEE8021-BRIDGE-MIB", "ieee8021BridgeTpPortOutFrames"),
        ("IEEE8021-BRIDGE-MIB", "ieee8021BridgeTpPortInDiscards"))
)
if mibBuilder.loadTexts:
    ieee8021BridgeTpPortGroup.setStatus("current")

ieee8021BridgeDevicePriorityGroup = ObjectGroup(
    (1, 3, 111, 2, 802, 1, 1, 2, 2, 2, 7)
)
ieee8021BridgeDevicePriorityGroup.setObjects(
    ("IEEE8021-BRIDGE-MIB", "ieee8021BridgeBaseTrafficClassesEnabled")
)
if mibBuilder.loadTexts:
    ieee8021BridgeDevicePriorityGroup.setStatus("current")

ieee8021BridgeDefaultPriorityGroup = ObjectGroup(
    (1, 3, 111, 2, 802, 1, 1, 2, 2, 2, 8)
)
ieee8021BridgeDefaultPriorityGroup.setObjects(
      *(("IEEE8021-BRIDGE-MIB", "ieee8021BridgePortDefaultUserPriority"),
        ("IEEE8021-BRIDGE-MIB", "ieee8021BridgePortPriorityCodePointSelection"),
        ("IEEE8021-BRIDGE-MIB", "ieee8021BridgePortUseDEI"),
        ("IEEE8021-BRIDGE-MIB", "ieee8021BridgePortRequireDropEncoding"),
        ("IEEE8021-BRIDGE-MIB", "ieee8021BridgePortServiceAccessPrioritySelection"))
)
if mibBuilder.loadTexts:
    ieee8021BridgeDefaultPriorityGroup.setStatus("current")

ieee8021BridgeRegenPriorityGroup = ObjectGroup(
    (1, 3, 111, 2, 802, 1, 1, 2, 2, 2, 9)
)
ieee8021BridgeRegenPriorityGroup.setObjects(
    ("IEEE8021-BRIDGE-MIB", "ieee8021BridgeRegenUserPriority")
)
if mibBuilder.loadTexts:
    ieee8021BridgeRegenPriorityGroup.setStatus("current")

ieee8021BridgePriorityGroup = ObjectGroup(
    (1, 3, 111, 2, 802, 1, 1, 2, 2, 2, 10)
)
ieee8021BridgePriorityGroup.setObjects(
      *(("IEEE8021-BRIDGE-MIB", "ieee8021BridgePortNumTrafficClasses"),
        ("IEEE8021-BRIDGE-MIB", "ieee8021BridgeTrafficClass"))
)
if mibBuilder.loadTexts:
    ieee8021BridgePriorityGroup.setStatus("current")

ieee8021BridgeAccessPriorityGroup = ObjectGroup(
    (1, 3, 111, 2, 802, 1, 1, 2, 2, 2, 11)
)
ieee8021BridgeAccessPriorityGroup.setObjects(
    ("IEEE8021-BRIDGE-MIB", "ieee8021BridgePortOutboundAccessPriority")
)
if mibBuilder.loadTexts:
    ieee8021BridgeAccessPriorityGroup.setStatus("current")

ieee8021BridgePortMrpGroup = ObjectGroup(
    (1, 3, 111, 2, 802, 1, 1, 2, 2, 2, 12)
)
ieee8021BridgePortMrpGroup.setObjects(
      *(("IEEE8021-BRIDGE-MIB", "ieee8021BridgePortMrpJoinTime"),
        ("IEEE8021-BRIDGE-MIB", "ieee8021BridgePortMrpLeaveTime"),
        ("IEEE8021-BRIDGE-MIB", "ieee8021BridgePortMrpLeaveAllTime"))
)
if mibBuilder.loadTexts:
    ieee8021BridgePortMrpGroup.setStatus("current")

ieee8021BridgePortMmrpGroup = ObjectGroup(
    (1, 3, 111, 2, 802, 1, 1, 2, 2, 2, 13)
)
ieee8021BridgePortMmrpGroup.setObjects(
      *(("IEEE8021-BRIDGE-MIB", "ieee8021BridgePortMmrpEnabledStatus"),
        ("IEEE8021-BRIDGE-MIB", "ieee8021BridgePortMmrpFailedRegistrations"),
        ("IEEE8021-BRIDGE-MIB", "ieee8021BridgePortMmrpLastPduOrigin"),
        ("IEEE8021-BRIDGE-MIB", "ieee8021BridgePortRestrictedGroupRegistration"))
)
if mibBuilder.loadTexts:
    ieee8021BridgePortMmrpGroup.setStatus("deprecated")

ieee8021BridgePortDecodingGroup = ObjectGroup(
    (1, 3, 111, 2, 802, 1, 1, 2, 2, 2, 14)
)
ieee8021BridgePortDecodingGroup.setObjects(
      *(("IEEE8021-BRIDGE-MIB", "ieee8021BridgePortDecodingPriority"),
        ("IEEE8021-BRIDGE-MIB", "ieee8021BridgePortDecodingDropEligible"))
)
if mibBuilder.loadTexts:
    ieee8021BridgePortDecodingGroup.setStatus("current")

ieee8021BridgePortEncodingGroup = ObjectGroup(
    (1, 3, 111, 2, 802, 1, 1, 2, 2, 2, 15)
)
ieee8021BridgePortEncodingGroup.setObjects(
    ("IEEE8021-BRIDGE-MIB", "ieee8021BridgePortEncodingPriority")
)
if mibBuilder.loadTexts:
    ieee8021BridgePortEncodingGroup.setStatus("current")

ieee8021BridgeServiceAccessPriorityGroup = ObjectGroup(
    (1, 3, 111, 2, 802, 1, 1, 2, 2, 2, 16)
)
ieee8021BridgeServiceAccessPriorityGroup.setObjects(
    ("IEEE8021-BRIDGE-MIB", "ieee8021BridgeServiceAccessPriorityValue")
)
if mibBuilder.loadTexts:
    ieee8021BridgeServiceAccessPriorityGroup.setStatus("current")

ieee8021BridgeInternalLANGroup = ObjectGroup(
    (1, 3, 111, 2, 802, 1, 1, 2, 2, 2, 17)
)
ieee8021BridgeInternalLANGroup.setObjects(
    ("IEEE8021-BRIDGE-MIB", "ieee8021BridgeILanIfRowStatus")
)
if mibBuilder.loadTexts:
    ieee8021BridgeInternalLANGroup.setStatus("current")

ieee8021BridgeCreatableBaseBridgeGroup = ObjectGroup(
    (1, 3, 111, 2, 802, 1, 1, 2, 2, 2, 18)
)
ieee8021BridgeCreatableBaseBridgeGroup.setObjects(
    ("IEEE8021-BRIDGE-MIB", "ieee8021BridgeBaseRowStatus")
)
if mibBuilder.loadTexts:
    ieee8021BridgeCreatableBaseBridgeGroup.setStatus("current")

ieee8021BridgeDot1dDynamicPortCreationGroup = ObjectGroup(
    (1, 3, 111, 2, 802, 1, 1, 2, 2, 2, 19)
)
ieee8021BridgeDot1dDynamicPortCreationGroup.setObjects(
    ("IEEE8021-BRIDGE-MIB", "ieee8021BridgeDot1dPortRowStatus")
)
if mibBuilder.loadTexts:
    ieee8021BridgeDot1dDynamicPortCreationGroup.setStatus("current")

ieee8021BridgeBaseIfToPortGroup = ObjectGroup(
    (1, 3, 111, 2, 802, 1, 1, 2, 2, 2, 20)
)
ieee8021BridgeBaseIfToPortGroup.setObjects(
      *(("IEEE8021-BRIDGE-MIB", "ieee8021BridgeBaseIfIndexComponentId"),
        ("IEEE8021-BRIDGE-MIB", "ieee8021BridgeBaseIfIndexPort"))
)
if mibBuilder.loadTexts:
    ieee8021BridgeBaseIfToPortGroup.setStatus("current")

ieee8021BridgePhyPortGroup = ObjectGroup(
    (1, 3, 111, 2, 802, 1, 1, 2, 2, 2, 21)
)
ieee8021BridgePhyPortGroup.setObjects(
      *(("IEEE8021-BRIDGE-MIB", "ieee8021BridgePhyPortIfIndex"),
        ("IEEE8021-BRIDGE-MIB", "ieee8021BridgePhyMacAddress"),
        ("IEEE8021-BRIDGE-MIB", "ieee8021BridgePhyPortToComponentId"),
        ("IEEE8021-BRIDGE-MIB", "ieee8021BridgePhyPortToInternalPort"))
)
if mibBuilder.loadTexts:
    ieee8021BridgePhyPortGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

ieee8021BridgeCompliance = ModuleCompliance(
    (1, 3, 111, 2, 802, 1, 1, 2, 2, 1, 1)
)
if mibBuilder.loadTexts:
    ieee8021BridgeCompliance.setStatus(
        "current"
    )

ieee8021BridgePriorityAndMulticastFilteringCompliance = ModuleCompliance(
    (1, 3, 111, 2, 802, 1, 1, 2, 2, 1, 2)
)
if mibBuilder.loadTexts:
    ieee8021BridgePriorityAndMulticastFilteringCompliance.setStatus(
        "deprecated"
    )

ieee8021BridgeCompliance1 = ModuleCompliance(
    (1, 3, 111, 2, 802, 1, 1, 2, 2, 1, 3)
)
if mibBuilder.loadTexts:
    ieee8021BridgeCompliance1.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "IEEE8021-BRIDGE-MIB",
    **{"ieee8021BridgeMib": ieee8021BridgeMib,
       "ieee8021BridgeNotifications": ieee8021BridgeNotifications,
       "ieee8021BridgeObjects": ieee8021BridgeObjects,
       "ieee8021BridgeBase": ieee8021BridgeBase,
       "ieee8021BridgeBaseTable": ieee8021BridgeBaseTable,
       "ieee8021BridgeBaseEntry": ieee8021BridgeBaseEntry,
       "ieee8021BridgeBaseComponentId": ieee8021BridgeBaseComponentId,
       "ieee8021BridgeBaseBridgeAddress": ieee8021BridgeBaseBridgeAddress,
       "ieee8021BridgeBaseNumPorts": ieee8021BridgeBaseNumPorts,
       "ieee8021BridgeBaseComponentType": ieee8021BridgeBaseComponentType,
       "ieee8021BridgeBaseDeviceCapabilities": ieee8021BridgeBaseDeviceCapabilities,
       "ieee8021BridgeBaseTrafficClassesEnabled": ieee8021BridgeBaseTrafficClassesEnabled,
       "ieee8021BridgeBaseMmrpEnabledStatus": ieee8021BridgeBaseMmrpEnabledStatus,
       "ieee8021BridgeBaseRowStatus": ieee8021BridgeBaseRowStatus,
       "ieee8021BridgeBasePortTable": ieee8021BridgeBasePortTable,
       "ieee8021BridgeBasePortEntry": ieee8021BridgeBasePortEntry,
       "ieee8021BridgeBasePortComponentId": ieee8021BridgeBasePortComponentId,
       "ieee8021BridgeBasePort": ieee8021BridgeBasePort,
       "ieee8021BridgeBasePortIfIndex": ieee8021BridgeBasePortIfIndex,
       "ieee8021BridgeBasePortDelayExceededDiscards": ieee8021BridgeBasePortDelayExceededDiscards,
       "ieee8021BridgeBasePortMtuExceededDiscards": ieee8021BridgeBasePortMtuExceededDiscards,
       "ieee8021BridgeBasePortCapabilities": ieee8021BridgeBasePortCapabilities,
       "ieee8021BridgeBasePortTypeCapabilities": ieee8021BridgeBasePortTypeCapabilities,
       "ieee8021BridgeBasePortType": ieee8021BridgeBasePortType,
       "ieee8021BridgeBasePortExternal": ieee8021BridgeBasePortExternal,
       "ieee8021BridgeBasePortAdminPointToPoint": ieee8021BridgeBasePortAdminPointToPoint,
       "ieee8021BridgeBasePortOperPointToPoint": ieee8021BridgeBasePortOperPointToPoint,
       "ieee8021BridgeBasePortName": ieee8021BridgeBasePortName,
       "ieee8021BridgeBaseIfToPortTable": ieee8021BridgeBaseIfToPortTable,
       "ieee8021BridgeBaseIfToPortEntry": ieee8021BridgeBaseIfToPortEntry,
       "ieee8021BridgeBaseIfIndexComponentId": ieee8021BridgeBaseIfIndexComponentId,
       "ieee8021BridgeBaseIfIndexPort": ieee8021BridgeBaseIfIndexPort,
       "ieee8021BridgePhyPortTable": ieee8021BridgePhyPortTable,
       "ieee8021BridgePhyPortEntry": ieee8021BridgePhyPortEntry,
       "ieee8021BridgePhyPort": ieee8021BridgePhyPort,
       "ieee8021BridgePhyPortIfIndex": ieee8021BridgePhyPortIfIndex,
       "ieee8021BridgePhyMacAddress": ieee8021BridgePhyMacAddress,
       "ieee8021BridgePhyPortToComponentId": ieee8021BridgePhyPortToComponentId,
       "ieee8021BridgePhyPortToInternalPort": ieee8021BridgePhyPortToInternalPort,
       "ieee8021BridgeTp": ieee8021BridgeTp,
       "ieee8021BridgeTpPortTable": ieee8021BridgeTpPortTable,
       "ieee8021BridgeTpPortEntry": ieee8021BridgeTpPortEntry,
       "ieee8021BridgeTpPortComponentId": ieee8021BridgeTpPortComponentId,
       "ieee8021BridgeTpPort": ieee8021BridgeTpPort,
       "ieee8021BridgeTpPortMaxInfo": ieee8021BridgeTpPortMaxInfo,
       "ieee8021BridgeTpPortInFrames": ieee8021BridgeTpPortInFrames,
       "ieee8021BridgeTpPortOutFrames": ieee8021BridgeTpPortOutFrames,
       "ieee8021BridgeTpPortInDiscards": ieee8021BridgeTpPortInDiscards,
       "ieee8021BridgePriority": ieee8021BridgePriority,
       "ieee8021BridgePortPriorityTable": ieee8021BridgePortPriorityTable,
       "ieee8021BridgePortPriorityEntry": ieee8021BridgePortPriorityEntry,
       "ieee8021BridgePortDefaultUserPriority": ieee8021BridgePortDefaultUserPriority,
       "ieee8021BridgePortNumTrafficClasses": ieee8021BridgePortNumTrafficClasses,
       "ieee8021BridgePortPriorityCodePointSelection": ieee8021BridgePortPriorityCodePointSelection,
       "ieee8021BridgePortUseDEI": ieee8021BridgePortUseDEI,
       "ieee8021BridgePortRequireDropEncoding": ieee8021BridgePortRequireDropEncoding,
       "ieee8021BridgePortServiceAccessPrioritySelection": ieee8021BridgePortServiceAccessPrioritySelection,
       "ieee8021BridgeUserPriorityRegenTable": ieee8021BridgeUserPriorityRegenTable,
       "ieee8021BridgeUserPriorityRegenEntry": ieee8021BridgeUserPriorityRegenEntry,
       "ieee8021BridgeUserPriority": ieee8021BridgeUserPriority,
       "ieee8021BridgeRegenUserPriority": ieee8021BridgeRegenUserPriority,
       "ieee8021BridgeTrafficClassTable": ieee8021BridgeTrafficClassTable,
       "ieee8021BridgeTrafficClassEntry": ieee8021BridgeTrafficClassEntry,
       "ieee8021BridgeTrafficClassPriority": ieee8021BridgeTrafficClassPriority,
       "ieee8021BridgeTrafficClass": ieee8021BridgeTrafficClass,
       "ieee8021BridgePortOutboundAccessPriorityTable": ieee8021BridgePortOutboundAccessPriorityTable,
       "ieee8021BridgePortOutboundAccessPriorityEntry": ieee8021BridgePortOutboundAccessPriorityEntry,
       "ieee8021BridgePortOutboundAccessPriority": ieee8021BridgePortOutboundAccessPriority,
       "ieee8021BridgePortDecodingTable": ieee8021BridgePortDecodingTable,
       "ieee8021BridgePortDecodingEntry": ieee8021BridgePortDecodingEntry,
       "ieee8021BridgePortDecodingComponentId": ieee8021BridgePortDecodingComponentId,
       "ieee8021BridgePortDecodingPortNum": ieee8021BridgePortDecodingPortNum,
       "ieee8021BridgePortDecodingPriorityCodePointRow": ieee8021BridgePortDecodingPriorityCodePointRow,
       "ieee8021BridgePortDecodingPriorityCodePoint": ieee8021BridgePortDecodingPriorityCodePoint,
       "ieee8021BridgePortDecodingPriority": ieee8021BridgePortDecodingPriority,
       "ieee8021BridgePortDecodingDropEligible": ieee8021BridgePortDecodingDropEligible,
       "ieee8021BridgePortEncodingTable": ieee8021BridgePortEncodingTable,
       "ieee8021BridgePortEncodingEntry": ieee8021BridgePortEncodingEntry,
       "ieee8021BridgePortEncodingComponentId": ieee8021BridgePortEncodingComponentId,
       "ieee8021BridgePortEncodingPortNum": ieee8021BridgePortEncodingPortNum,
       "ieee8021BridgePortEncodingPriorityCodePointRow": ieee8021BridgePortEncodingPriorityCodePointRow,
       "ieee8021BridgePortEncodingPriorityCodePoint": ieee8021BridgePortEncodingPriorityCodePoint,
       "ieee8021BridgePortEncodingDropEligible": ieee8021BridgePortEncodingDropEligible,
       "ieee8021BridgePortEncodingPriority": ieee8021BridgePortEncodingPriority,
       "ieee8021BridgeServiceAccessPriorityTable": ieee8021BridgeServiceAccessPriorityTable,
       "ieee8021BridgeServiceAccessPriorityEntry": ieee8021BridgeServiceAccessPriorityEntry,
       "ieee8021BridgeServiceAccessPriorityComponentId": ieee8021BridgeServiceAccessPriorityComponentId,
       "ieee8021BridgeServiceAccessPriorityPortNum": ieee8021BridgeServiceAccessPriorityPortNum,
       "ieee8021BridgeServiceAccessPriorityReceived": ieee8021BridgeServiceAccessPriorityReceived,
       "ieee8021BridgeServiceAccessPriorityValue": ieee8021BridgeServiceAccessPriorityValue,
       "ieee8021BridgeMrp": ieee8021BridgeMrp,
       "ieee8021BridgePortMrpTable": ieee8021BridgePortMrpTable,
       "ieee8021BridgePortMrpEntry": ieee8021BridgePortMrpEntry,
       "ieee8021BridgePortMrpJoinTime": ieee8021BridgePortMrpJoinTime,
       "ieee8021BridgePortMrpLeaveTime": ieee8021BridgePortMrpLeaveTime,
       "ieee8021BridgePortMrpLeaveAllTime": ieee8021BridgePortMrpLeaveAllTime,
       "ieee8021BridgeMmrp": ieee8021BridgeMmrp,
       "ieee8021BridgePortMmrpTable": ieee8021BridgePortMmrpTable,
       "ieee8021BridgePortMmrpEntry": ieee8021BridgePortMmrpEntry,
       "ieee8021BridgePortMmrpEnabledStatus": ieee8021BridgePortMmrpEnabledStatus,
       "ieee8021BridgePortMmrpFailedRegistrations": ieee8021BridgePortMmrpFailedRegistrations,
       "ieee8021BridgePortMmrpLastPduOrigin": ieee8021BridgePortMmrpLastPduOrigin,
       "ieee8021BridgePortRestrictedGroupRegistration": ieee8021BridgePortRestrictedGroupRegistration,
       "ieee8021BridgeInternalLan": ieee8021BridgeInternalLan,
       "ieee8021BridgeILanIfTable": ieee8021BridgeILanIfTable,
       "ieee8021BridgeILanIfEntry": ieee8021BridgeILanIfEntry,
       "ieee8021BridgeILanIfRowStatus": ieee8021BridgeILanIfRowStatus,
       "ieee8021BridgeDot1d": ieee8021BridgeDot1d,
       "ieee8021BridgeDot1dPortTable": ieee8021BridgeDot1dPortTable,
       "ieee8021BridgeDot1dPortEntry": ieee8021BridgeDot1dPortEntry,
       "ieee8021BridgeDot1dPortRowStatus": ieee8021BridgeDot1dPortRowStatus,
       "ieee8021BridgeConformance": ieee8021BridgeConformance,
       "ieee8021BridgeCompliances": ieee8021BridgeCompliances,
       "ieee8021BridgeCompliance": ieee8021BridgeCompliance,
       "ieee8021BridgePriorityAndMulticastFilteringCompliance": ieee8021BridgePriorityAndMulticastFilteringCompliance,
       "ieee8021BridgeCompliance1": ieee8021BridgeCompliance1,
       "ieee8021BridgeGroups": ieee8021BridgeGroups,
       "ieee8021BridgeBaseBridgeGroup": ieee8021BridgeBaseBridgeGroup,
       "ieee8021BridgeBasePortGroup": ieee8021BridgeBasePortGroup,
       "ieee8021BridgeCapGroup": ieee8021BridgeCapGroup,
       "ieee8021BridgeDeviceMmrpGroup": ieee8021BridgeDeviceMmrpGroup,
       "ieee8021BridgeTpPortGroup": ieee8021BridgeTpPortGroup,
       "ieee8021BridgeDevicePriorityGroup": ieee8021BridgeDevicePriorityGroup,
       "ieee8021BridgeDefaultPriorityGroup": ieee8021BridgeDefaultPriorityGroup,
       "ieee8021BridgeRegenPriorityGroup": ieee8021BridgeRegenPriorityGroup,
       "ieee8021BridgePriorityGroup": ieee8021BridgePriorityGroup,
       "ieee8021BridgeAccessPriorityGroup": ieee8021BridgeAccessPriorityGroup,
       "ieee8021BridgePortMrpGroup": ieee8021BridgePortMrpGroup,
       "ieee8021BridgePortMmrpGroup": ieee8021BridgePortMmrpGroup,
       "ieee8021BridgePortDecodingGroup": ieee8021BridgePortDecodingGroup,
       "ieee8021BridgePortEncodingGroup": ieee8021BridgePortEncodingGroup,
       "ieee8021BridgeServiceAccessPriorityGroup": ieee8021BridgeServiceAccessPriorityGroup,
       "ieee8021BridgeInternalLANGroup": ieee8021BridgeInternalLANGroup,
       "ieee8021BridgeCreatableBaseBridgeGroup": ieee8021BridgeCreatableBaseBridgeGroup,
       "ieee8021BridgeDot1dDynamicPortCreationGroup": ieee8021BridgeDot1dDynamicPortCreationGroup,
       "ieee8021BridgeBaseIfToPortGroup": ieee8021BridgeBaseIfToPortGroup,
       "ieee8021BridgePhyPortGroup": ieee8021BridgePhyPortGroup}
)
