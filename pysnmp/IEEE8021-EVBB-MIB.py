# SNMP MIB module (IEEE8021-EVBB-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/IEEE8021-EVBB-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:36:02 2024
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
 IEEE8021PbbComponentIdentifier,
 IEEE8021PbbComponentIdentifierOrZero,
 ieee802dot1mibs) = mibBuilder.importSymbols(
    "IEEE8021-TC-MIB",
    "IEEE8021BridgePortNumber",
    "IEEE8021BridgePortNumberOrZero",
    "IEEE8021PbbComponentIdentifier",
    "IEEE8021PbbComponentIdentifierOrZero",
    "ieee802dot1mibs")

(VlanIndex,) = mibBuilder.importSymbols(
    "Q-BRIDGE-MIB",
    "VlanIndex")

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

ieee8021BridgeEvbMib = ModuleIdentity(
    (1, 3, 111, 2, 802, 1, 1, 100)
)
ieee8021BridgeEvbMib.setRevisions(
        ("2010-10-25 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class IEEE8021BridgeEvbTLVTC(Bits, TextualConvention):
    status = "current"


# MIB Managed Objects in the order of their OIDs

_Ieee8021BridgeEvbNotifications_ObjectIdentity = ObjectIdentity
ieee8021BridgeEvbNotifications = _Ieee8021BridgeEvbNotifications_ObjectIdentity(
    (1, 3, 111, 2, 802, 1, 1, 100, 0)
)
_Ieee8021BridgeEvbObjects_ObjectIdentity = ObjectIdentity
ieee8021BridgeEvbObjects = _Ieee8021BridgeEvbObjects_ObjectIdentity(
    (1, 3, 111, 2, 802, 1, 1, 100, 1)
)
_Ieee8021BridgeEvbConfig_ObjectIdentity = ObjectIdentity
ieee8021BridgeEvbConfig = _Ieee8021BridgeEvbConfig_ObjectIdentity(
    (1, 3, 111, 2, 802, 1, 1, 100, 1, 1)
)
_Ieee8021BridgeEvbSysMACAddress_Type = MacAddress
_Ieee8021BridgeEvbSysMACAddress_Object = MibScalar
ieee8021BridgeEvbSysMACAddress = _Ieee8021BridgeEvbSysMACAddress_Object(
    (1, 3, 111, 2, 802, 1, 1, 100, 1, 1, 1),
    _Ieee8021BridgeEvbSysMACAddress_Type()
)
ieee8021BridgeEvbSysMACAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021BridgeEvbSysMACAddress.setStatus("current")


class _Ieee8021BridgeEvbSysName_Type(SnmpAdminString):
    """Custom type ieee8021BridgeEvbSysName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Ieee8021BridgeEvbSysName_Type.__name__ = "SnmpAdminString"
_Ieee8021BridgeEvbSysName_Object = MibScalar
ieee8021BridgeEvbSysName = _Ieee8021BridgeEvbSysName_Object(
    (1, 3, 111, 2, 802, 1, 1, 100, 1, 1, 2),
    _Ieee8021BridgeEvbSysName_Type()
)
ieee8021BridgeEvbSysName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ieee8021BridgeEvbSysName.setStatus("current")


class _Ieee8021BridgeEvbSysType_Type(Integer32):
    """Custom type ieee8021BridgeEvbSysType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("evbBridge", 1),
          ("evbStation", 2))
    )


_Ieee8021BridgeEvbSysType_Type.__name__ = "Integer32"
_Ieee8021BridgeEvbSysType_Object = MibScalar
ieee8021BridgeEvbSysType = _Ieee8021BridgeEvbSysType_Object(
    (1, 3, 111, 2, 802, 1, 1, 100, 1, 1, 3),
    _Ieee8021BridgeEvbSysType_Type()
)
ieee8021BridgeEvbSysType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021BridgeEvbSysType.setStatus("current")


class _Ieee8021BridgeEvbSysNumExternalPorts_Type(Unsigned32):
    """Custom type ieee8021BridgeEvbSysNumExternalPorts based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_Ieee8021BridgeEvbSysNumExternalPorts_Type.__name__ = "Unsigned32"
_Ieee8021BridgeEvbSysNumExternalPorts_Object = MibScalar
ieee8021BridgeEvbSysNumExternalPorts = _Ieee8021BridgeEvbSysNumExternalPorts_Object(
    (1, 3, 111, 2, 802, 1, 1, 100, 1, 1, 4),
    _Ieee8021BridgeEvbSysNumExternalPorts_Type()
)
ieee8021BridgeEvbSysNumExternalPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021BridgeEvbSysNumExternalPorts.setStatus("current")


class _Ieee8021BridgeEvbSysEvbLldpEnables_Type(Bits):
    """Custom type ieee8021BridgeEvbSysEvbLldpEnables based on Bits"""
    namedValues = NamedValues(
        *(("autoEvbLLDPTLV", 1),
          ("evbTLVEnable", 0))
    )

_Ieee8021BridgeEvbSysEvbLldpEnables_Type.__name__ = "Bits"
_Ieee8021BridgeEvbSysEvbLldpEnables_Object = MibScalar
ieee8021BridgeEvbSysEvbLldpEnables = _Ieee8021BridgeEvbSysEvbLldpEnables_Object(
    (1, 3, 111, 2, 802, 1, 1, 100, 1, 1, 5),
    _Ieee8021BridgeEvbSysEvbLldpEnables_Type()
)
ieee8021BridgeEvbSysEvbLldpEnables.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ieee8021BridgeEvbSysEvbLldpEnables.setStatus("current")
_Ieee8021BridgeEvbSysEvbLldpDfltMode_Type = IEEE8021BridgeEvbTLVTC
_Ieee8021BridgeEvbSysEvbLldpDfltMode_Object = MibScalar
ieee8021BridgeEvbSysEvbLldpDfltMode = _Ieee8021BridgeEvbSysEvbLldpDfltMode_Object(
    (1, 3, 111, 2, 802, 1, 1, 100, 1, 1, 6),
    _Ieee8021BridgeEvbSysEvbLldpDfltMode_Type()
)
ieee8021BridgeEvbSysEvbLldpDfltMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ieee8021BridgeEvbSysEvbLldpDfltMode.setStatus("current")
_Ieee8021BridgeEvbSysEvbLldpNumVsisSup_Type = Unsigned32
_Ieee8021BridgeEvbSysEvbLldpNumVsisSup_Object = MibScalar
ieee8021BridgeEvbSysEvbLldpNumVsisSup = _Ieee8021BridgeEvbSysEvbLldpNumVsisSup_Object(
    (1, 3, 111, 2, 802, 1, 1, 100, 1, 1, 7),
    _Ieee8021BridgeEvbSysEvbLldpNumVsisSup_Type()
)
ieee8021BridgeEvbSysEvbLldpNumVsisSup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ieee8021BridgeEvbSysEvbLldpNumVsisSup.setStatus("current")
_Ieee8021BridgeEvbSysNumCorErComps_Type = Unsigned32
_Ieee8021BridgeEvbSysNumCorErComps_Object = MibScalar
ieee8021BridgeEvbSysNumCorErComps = _Ieee8021BridgeEvbSysNumCorErComps_Object(
    (1, 3, 111, 2, 802, 1, 1, 100, 1, 1, 8),
    _Ieee8021BridgeEvbSysNumCorErComps_Type()
)
ieee8021BridgeEvbSysNumCorErComps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021BridgeEvbSysNumCorErComps.setStatus("current")
_Ieee8021BridgeEvbSysNumSComps_Type = Unsigned32
_Ieee8021BridgeEvbSysNumSComps_Object = MibScalar
ieee8021BridgeEvbSysNumSComps = _Ieee8021BridgeEvbSysNumSComps_Object(
    (1, 3, 111, 2, 802, 1, 1, 100, 1, 1, 9),
    _Ieee8021BridgeEvbSysNumSComps_Type()
)
ieee8021BridgeEvbSysNumSComps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021BridgeEvbSysNumSComps.setStatus("current")
_Ieee8021BridgeEvbECPACkTimer_Type = Integer32
_Ieee8021BridgeEvbECPACkTimer_Object = MibScalar
ieee8021BridgeEvbECPACkTimer = _Ieee8021BridgeEvbECPACkTimer_Object(
    (1, 3, 111, 2, 802, 1, 1, 100, 1, 1, 10),
    _Ieee8021BridgeEvbECPACkTimer_Type()
)
ieee8021BridgeEvbECPACkTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ieee8021BridgeEvbECPACkTimer.setStatus("current")


class _Ieee8021BridgeEvbECPMaxRetires_Type(Integer32):
    """Custom type ieee8021BridgeEvbECPMaxRetires based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_Ieee8021BridgeEvbECPMaxRetires_Type.__name__ = "Integer32"
_Ieee8021BridgeEvbECPMaxRetires_Object = MibScalar
ieee8021BridgeEvbECPMaxRetires = _Ieee8021BridgeEvbECPMaxRetires_Object(
    (1, 3, 111, 2, 802, 1, 1, 100, 1, 1, 11),
    _Ieee8021BridgeEvbECPMaxRetires_Type()
)
ieee8021BridgeEvbECPMaxRetires.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ieee8021BridgeEvbECPMaxRetires.setStatus("current")
_Ieee8021BridgeEvbSysVdpDfltRsrcWaitDelay_Type = Integer32
_Ieee8021BridgeEvbSysVdpDfltRsrcWaitDelay_Object = MibScalar
ieee8021BridgeEvbSysVdpDfltRsrcWaitDelay = _Ieee8021BridgeEvbSysVdpDfltRsrcWaitDelay_Object(
    (1, 3, 111, 2, 802, 1, 1, 100, 1, 1, 12),
    _Ieee8021BridgeEvbSysVdpDfltRsrcWaitDelay_Type()
)
ieee8021BridgeEvbSysVdpDfltRsrcWaitDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ieee8021BridgeEvbSysVdpDfltRsrcWaitDelay.setStatus("current")
_Ieee8021BridgeEvbSysVdpDfltReinitKeepAlive_Type = Integer32
_Ieee8021BridgeEvbSysVdpDfltReinitKeepAlive_Object = MibScalar
ieee8021BridgeEvbSysVdpDfltReinitKeepAlive = _Ieee8021BridgeEvbSysVdpDfltReinitKeepAlive_Object(
    (1, 3, 111, 2, 802, 1, 1, 100, 1, 1, 13),
    _Ieee8021BridgeEvbSysVdpDfltReinitKeepAlive_Type()
)
ieee8021BridgeEvbSysVdpDfltReinitKeepAlive.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ieee8021BridgeEvbSysVdpDfltReinitKeepAlive.setStatus("current")
_Ieee8021BridgeEvbPhyPortTable_Object = MibTable
ieee8021BridgeEvbPhyPortTable = _Ieee8021BridgeEvbPhyPortTable_Object(
    (1, 3, 111, 2, 802, 1, 1, 100, 1, 1, 14)
)
if mibBuilder.loadTexts:
    ieee8021BridgeEvbPhyPortTable.setStatus("current")
_Ieee8021BridgeEvbPhyPortEntry_Object = MibTableRow
ieee8021BridgeEvbPhyPortEntry = _Ieee8021BridgeEvbPhyPortEntry_Object(
    (1, 3, 111, 2, 802, 1, 1, 100, 1, 1, 14, 1)
)
ieee8021BridgeEvbPhyPortEntry.setIndexNames(
    (0, "IEEE8021-EVBB-MIB", "ieee8021BridgeEvbPhyPort"),
)
if mibBuilder.loadTexts:
    ieee8021BridgeEvbPhyPortEntry.setStatus("current")
_Ieee8021BridgeEvbPhyPort_Type = IEEE8021BridgePortNumber
_Ieee8021BridgeEvbPhyPort_Object = MibTableColumn
ieee8021BridgeEvbPhyPort = _Ieee8021BridgeEvbPhyPort_Object(
    (1, 3, 111, 2, 802, 1, 1, 100, 1, 1, 14, 1, 1),
    _Ieee8021BridgeEvbPhyPort_Type()
)
ieee8021BridgeEvbPhyPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ieee8021BridgeEvbPhyPort.setStatus("current")
_Ieee8021BridgeEvbPhyPortMacAddress_Type = MacAddress
_Ieee8021BridgeEvbPhyPortMacAddress_Object = MibTableColumn
ieee8021BridgeEvbPhyPortMacAddress = _Ieee8021BridgeEvbPhyPortMacAddress_Object(
    (1, 3, 111, 2, 802, 1, 1, 100, 1, 1, 14, 1, 2),
    _Ieee8021BridgeEvbPhyPortMacAddress_Type()
)
ieee8021BridgeEvbPhyPortMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021BridgeEvbPhyPortMacAddress.setStatus("current")


class _Ieee8021BridgeEvbPhyPortTypeCap_Type(Bits):
    """Custom type ieee8021BridgeEvbPhyPortTypeCap based on Bits"""
    namedValues = NamedValues(
        *(("customerBackbonePort", 4),
          ("customerEdgePort", 3),
          ("customerNetworkPort", 2),
          ("customerVlanPort", 0),
          ("dBridgePort", 6),
          ("providerNetworkPort", 1),
          ("serverEdgePort", 7),
          ("virtualInstancePort", 5))
    )

_Ieee8021BridgeEvbPhyPortTypeCap_Type.__name__ = "Bits"
_Ieee8021BridgeEvbPhyPortTypeCap_Object = MibTableColumn
ieee8021BridgeEvbPhyPortTypeCap = _Ieee8021BridgeEvbPhyPortTypeCap_Object(
    (1, 3, 111, 2, 802, 1, 1, 100, 1, 1, 14, 1, 3),
    _Ieee8021BridgeEvbPhyPortTypeCap_Type()
)
ieee8021BridgeEvbPhyPortTypeCap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021BridgeEvbPhyPortTypeCap.setStatus("current")


class _Ieee8021BridgeEvbPhyPortType_Type(Integer32):
    """Custom type ieee8021BridgeEvbPhyPortType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("customerVlanPort", 1),
          ("uplinkAccessPort", 2))
    )


_Ieee8021BridgeEvbPhyPortType_Type.__name__ = "Integer32"
_Ieee8021BridgeEvbPhyPortType_Object = MibTableColumn
ieee8021BridgeEvbPhyPortType = _Ieee8021BridgeEvbPhyPortType_Object(
    (1, 3, 111, 2, 802, 1, 1, 100, 1, 1, 14, 1, 4),
    _Ieee8021BridgeEvbPhyPortType_Type()
)
ieee8021BridgeEvbPhyPortType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ieee8021BridgeEvbPhyPortType.setStatus("current")
_Ieee8021BridgeEvbPhyPortToComponentId_Type = IEEE8021PbbComponentIdentifierOrZero
_Ieee8021BridgeEvbPhyPortToComponentId_Object = MibTableColumn
ieee8021BridgeEvbPhyPortToComponentId = _Ieee8021BridgeEvbPhyPortToComponentId_Object(
    (1, 3, 111, 2, 802, 1, 1, 100, 1, 1, 14, 1, 5),
    _Ieee8021BridgeEvbPhyPortToComponentId_Type()
)
ieee8021BridgeEvbPhyPortToComponentId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ieee8021BridgeEvbPhyPortToComponentId.setStatus("current")
_Ieee8021BridgeEvbPhyPortToInternalPort_Type = IEEE8021BridgePortNumberOrZero
_Ieee8021BridgeEvbPhyPortToInternalPort_Object = MibTableColumn
ieee8021BridgeEvbPhyPortToInternalPort = _Ieee8021BridgeEvbPhyPortToInternalPort_Object(
    (1, 3, 111, 2, 802, 1, 1, 100, 1, 1, 14, 1, 6),
    _Ieee8021BridgeEvbPhyPortToInternalPort_Type()
)
ieee8021BridgeEvbPhyPortToInternalPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ieee8021BridgeEvbPhyPortToInternalPort.setStatus("current")
_Ieee8021BridgeEvbPortTable_Object = MibTable
ieee8021BridgeEvbPortTable = _Ieee8021BridgeEvbPortTable_Object(
    (1, 3, 111, 2, 802, 1, 1, 100, 1, 1, 15)
)
if mibBuilder.loadTexts:
    ieee8021BridgeEvbPortTable.setStatus("current")
_Ieee8021BridgeEvbPortEntry_Object = MibTableRow
ieee8021BridgeEvbPortEntry = _Ieee8021BridgeEvbPortEntry_Object(
    (1, 3, 111, 2, 802, 1, 1, 100, 1, 1, 15, 1)
)
ieee8021BridgeEvbPortEntry.setIndexNames(
    (0, "IEEE8021-EVBB-MIB", "ieee8021BridgeEvbPortComponentId"),
    (0, "IEEE8021-EVBB-MIB", "ieee8021BridgeEvbPort"),
)
if mibBuilder.loadTexts:
    ieee8021BridgeEvbPortEntry.setStatus("current")
_Ieee8021BridgeEvbPortComponentId_Type = IEEE8021PbbComponentIdentifierOrZero
_Ieee8021BridgeEvbPortComponentId_Object = MibTableColumn
ieee8021BridgeEvbPortComponentId = _Ieee8021BridgeEvbPortComponentId_Object(
    (1, 3, 111, 2, 802, 1, 1, 100, 1, 1, 15, 1, 1),
    _Ieee8021BridgeEvbPortComponentId_Type()
)
ieee8021BridgeEvbPortComponentId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ieee8021BridgeEvbPortComponentId.setStatus("current")
_Ieee8021BridgeEvbPort_Type = IEEE8021BridgePortNumber
_Ieee8021BridgeEvbPort_Object = MibTableColumn
ieee8021BridgeEvbPort = _Ieee8021BridgeEvbPort_Object(
    (1, 3, 111, 2, 802, 1, 1, 100, 1, 1, 15, 1, 2),
    _Ieee8021BridgeEvbPort_Type()
)
ieee8021BridgeEvbPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ieee8021BridgeEvbPort.setStatus("current")


class _Ieee8021BridgeEvbPortType_Type(Integer32):
    """Custom type ieee8021BridgeEvbPortType based on Integer32"""
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
        *(("cVlanBridgePort", 1),
          ("edgeRelayPort", 6),
          ("sChannelAccessPort", 4),
          ("stationFacingBridgePort", 2),
          ("uplinkAccessPort", 3),
          ("uplinkRelayPort", 5))
    )


_Ieee8021BridgeEvbPortType_Type.__name__ = "Integer32"
_Ieee8021BridgeEvbPortType_Object = MibTableColumn
ieee8021BridgeEvbPortType = _Ieee8021BridgeEvbPortType_Object(
    (1, 3, 111, 2, 802, 1, 1, 100, 1, 1, 15, 1, 3),
    _Ieee8021BridgeEvbPortType_Type()
)
ieee8021BridgeEvbPortType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ieee8021BridgeEvbPortType.setStatus("current")
_Ieee8021BridgeEvbPortRowStatus_Type = RowStatus
_Ieee8021BridgeEvbPortRowStatus_Object = MibTableColumn
ieee8021BridgeEvbPortRowStatus = _Ieee8021BridgeEvbPortRowStatus_Object(
    (1, 3, 111, 2, 802, 1, 1, 100, 1, 1, 15, 1, 4),
    _Ieee8021BridgeEvbPortRowStatus_Type()
)
ieee8021BridgeEvbPortRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ieee8021BridgeEvbPortRowStatus.setStatus("current")
_Ieee8021BridgeEvbVSIDBObjects_ObjectIdentity = ObjectIdentity
ieee8021BridgeEvbVSIDBObjects = _Ieee8021BridgeEvbVSIDBObjects_ObjectIdentity(
    (1, 3, 111, 2, 802, 1, 1, 100, 1, 2)
)
_Ieee8021BridgeEvbVSIDBTable_Object = MibTable
ieee8021BridgeEvbVSIDBTable = _Ieee8021BridgeEvbVSIDBTable_Object(
    (1, 3, 111, 2, 802, 1, 1, 100, 1, 2, 1)
)
if mibBuilder.loadTexts:
    ieee8021BridgeEvbVSIDBTable.setStatus("current")
_Ieee8021BridgeEvbVSIDBEntry_Object = MibTableRow
ieee8021BridgeEvbVSIDBEntry = _Ieee8021BridgeEvbVSIDBEntry_Object(
    (1, 3, 111, 2, 802, 1, 1, 100, 1, 2, 1, 1)
)
ieee8021BridgeEvbVSIDBEntry.setIndexNames(
    (0, "IEEE8021-EVBB-MIB", "ieee8021BridgeEvbPhyPort"),
    (0, "IEEE8021-EVBB-MIB", "ieee8021BridgeEvbVsiSvid"),
    (0, "IEEE8021-EVBB-MIB", "ieee8021BridgeEvbVSIID"),
)
if mibBuilder.loadTexts:
    ieee8021BridgeEvbVSIDBEntry.setStatus("current")


class _Ieee8021BridgeEvbVsiSvid_Type(Unsigned32):
    """Custom type ieee8021BridgeEvbVsiSvid based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_Ieee8021BridgeEvbVsiSvid_Type.__name__ = "Unsigned32"
_Ieee8021BridgeEvbVsiSvid_Object = MibTableColumn
ieee8021BridgeEvbVsiSvid = _Ieee8021BridgeEvbVsiSvid_Object(
    (1, 3, 111, 2, 802, 1, 1, 100, 1, 2, 1, 1, 1),
    _Ieee8021BridgeEvbVsiSvid_Type()
)
ieee8021BridgeEvbVsiSvid.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ieee8021BridgeEvbVsiSvid.setStatus("current")


class _Ieee8021BridgeEvbVSIID_Type(OctetString):
    """Custom type ieee8021BridgeEvbVSIID based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )


_Ieee8021BridgeEvbVSIID_Type.__name__ = "OctetString"
_Ieee8021BridgeEvbVSIID_Object = MibTableColumn
ieee8021BridgeEvbVSIID = _Ieee8021BridgeEvbVSIID_Object(
    (1, 3, 111, 2, 802, 1, 1, 100, 1, 2, 1, 1, 2),
    _Ieee8021BridgeEvbVSIID_Type()
)
ieee8021BridgeEvbVSIID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ieee8021BridgeEvbVSIID.setStatus("current")
_Ieee8021BridgeEvbVSIComponentID_Type = IEEE8021PbbComponentIdentifier
_Ieee8021BridgeEvbVSIComponentID_Object = MibTableColumn
ieee8021BridgeEvbVSIComponentID = _Ieee8021BridgeEvbVSIComponentID_Object(
    (1, 3, 111, 2, 802, 1, 1, 100, 1, 2, 1, 1, 3),
    _Ieee8021BridgeEvbVSIComponentID_Type()
)
ieee8021BridgeEvbVSIComponentID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021BridgeEvbVSIComponentID.setStatus("current")
_Ieee8021BridgeEvbVSIPortNumber_Type = IEEE8021BridgePortNumber
_Ieee8021BridgeEvbVSIPortNumber_Object = MibTableColumn
ieee8021BridgeEvbVSIPortNumber = _Ieee8021BridgeEvbVSIPortNumber_Object(
    (1, 3, 111, 2, 802, 1, 1, 100, 1, 2, 1, 1, 4),
    _Ieee8021BridgeEvbVSIPortNumber_Type()
)
ieee8021BridgeEvbVSIPortNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021BridgeEvbVSIPortNumber.setStatus("current")
_Ieee8021BridgeEvbVSITimeSinceCreate_Type = TimeInterval
_Ieee8021BridgeEvbVSITimeSinceCreate_Object = MibTableColumn
ieee8021BridgeEvbVSITimeSinceCreate = _Ieee8021BridgeEvbVSITimeSinceCreate_Object(
    (1, 3, 111, 2, 802, 1, 1, 100, 1, 2, 1, 1, 5),
    _Ieee8021BridgeEvbVSITimeSinceCreate_Type()
)
ieee8021BridgeEvbVSITimeSinceCreate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021BridgeEvbVSITimeSinceCreate.setStatus("current")


class _Ieee8021BridgeEvbVsiVdpOperCmd_Type(Integer32):
    """Custom type ieee8021BridgeEvbVsiVdpOperCmd based on Integer32"""
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
        *(("associate", 3),
          ("deAssociate", 4),
          ("preAssociate", 1),
          ("preAssociateWithRsrcReservation", 2))
    )


_Ieee8021BridgeEvbVsiVdpOperCmd_Type.__name__ = "Integer32"
_Ieee8021BridgeEvbVsiVdpOperCmd_Object = MibTableColumn
ieee8021BridgeEvbVsiVdpOperCmd = _Ieee8021BridgeEvbVsiVdpOperCmd_Object(
    (1, 3, 111, 2, 802, 1, 1, 100, 1, 2, 1, 1, 6),
    _Ieee8021BridgeEvbVsiVdpOperCmd_Type()
)
ieee8021BridgeEvbVsiVdpOperCmd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021BridgeEvbVsiVdpOperCmd.setStatus("current")
_Ieee8021BridgeEvbVsiOperRevert_Type = TruthValue
_Ieee8021BridgeEvbVsiOperRevert_Object = MibTableColumn
ieee8021BridgeEvbVsiOperRevert = _Ieee8021BridgeEvbVsiOperRevert_Object(
    (1, 3, 111, 2, 802, 1, 1, 100, 1, 2, 1, 1, 7),
    _Ieee8021BridgeEvbVsiOperRevert_Type()
)
ieee8021BridgeEvbVsiOperRevert.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021BridgeEvbVsiOperRevert.setStatus("current")
_Ieee8021BridgeEvbVsiOperHard_Type = TruthValue
_Ieee8021BridgeEvbVsiOperHard_Object = MibTableColumn
ieee8021BridgeEvbVsiOperHard = _Ieee8021BridgeEvbVsiOperHard_Object(
    (1, 3, 111, 2, 802, 1, 1, 100, 1, 2, 1, 1, 8),
    _Ieee8021BridgeEvbVsiOperHard_Type()
)
ieee8021BridgeEvbVsiOperHard.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021BridgeEvbVsiOperHard.setStatus("current")


class _Ieee8021BridgeEvbVsiOperReason_Type(Bits):
    """Custom type ieee8021BridgeEvbVsiOperReason based on Bits"""
    namedValues = NamedValues(
        *(("insufficientResources", 2),
          ("invalidFormat", 1),
          ("otherfailure", 3),
          ("success", 0))
    )

_Ieee8021BridgeEvbVsiOperReason_Type.__name__ = "Bits"
_Ieee8021BridgeEvbVsiOperReason_Object = MibTableColumn
ieee8021BridgeEvbVsiOperReason = _Ieee8021BridgeEvbVsiOperReason_Object(
    (1, 3, 111, 2, 802, 1, 1, 100, 1, 2, 1, 1, 9),
    _Ieee8021BridgeEvbVsiOperReason_Type()
)
ieee8021BridgeEvbVsiOperReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021BridgeEvbVsiOperReason.setStatus("current")


class _Ieee8021BridgeEvbVSIMgrID_Type(OctetString):
    """Custom type ieee8021BridgeEvbVSIMgrID based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_Ieee8021BridgeEvbVSIMgrID_Type.__name__ = "OctetString"
_Ieee8021BridgeEvbVSIMgrID_Object = MibTableColumn
ieee8021BridgeEvbVSIMgrID = _Ieee8021BridgeEvbVSIMgrID_Object(
    (1, 3, 111, 2, 802, 1, 1, 100, 1, 2, 1, 1, 10),
    _Ieee8021BridgeEvbVSIMgrID_Type()
)
ieee8021BridgeEvbVSIMgrID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021BridgeEvbVSIMgrID.setStatus("current")


class _Ieee8021BridgeEvbVSIType_Type(OctetString):
    """Custom type ieee8021BridgeEvbVSIType based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(3, 3),
    )


_Ieee8021BridgeEvbVSIType_Type.__name__ = "OctetString"
_Ieee8021BridgeEvbVSIType_Object = MibTableColumn
ieee8021BridgeEvbVSIType = _Ieee8021BridgeEvbVSIType_Object(
    (1, 3, 111, 2, 802, 1, 1, 100, 1, 2, 1, 1, 11),
    _Ieee8021BridgeEvbVSIType_Type()
)
ieee8021BridgeEvbVSIType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021BridgeEvbVSIType.setStatus("current")


class _Ieee8021BridgeEvbVSITypeVersion_Type(OctetString):
    """Custom type ieee8021BridgeEvbVSITypeVersion based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_Ieee8021BridgeEvbVSITypeVersion_Type.__name__ = "OctetString"
_Ieee8021BridgeEvbVSITypeVersion_Object = MibTableColumn
ieee8021BridgeEvbVSITypeVersion = _Ieee8021BridgeEvbVSITypeVersion_Object(
    (1, 3, 111, 2, 802, 1, 1, 100, 1, 2, 1, 1, 12),
    _Ieee8021BridgeEvbVSITypeVersion_Type()
)
ieee8021BridgeEvbVSITypeVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021BridgeEvbVSITypeVersion.setStatus("current")


class _Ieee8021BridgeEvbVSIMvFormat_Type(Integer32):
    """Custom type ieee8021BridgeEvbVSIMvFormat based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("basic", 0),
          ("partial", 1),
          ("vlanOnly", 2))
    )


_Ieee8021BridgeEvbVSIMvFormat_Type.__name__ = "Integer32"
_Ieee8021BridgeEvbVSIMvFormat_Object = MibTableColumn
ieee8021BridgeEvbVSIMvFormat = _Ieee8021BridgeEvbVSIMvFormat_Object(
    (1, 3, 111, 2, 802, 1, 1, 100, 1, 2, 1, 1, 13),
    _Ieee8021BridgeEvbVSIMvFormat_Type()
)
ieee8021BridgeEvbVSIMvFormat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021BridgeEvbVSIMvFormat.setStatus("current")
_Ieee8021BridgeEvbVSINumMACs_Type = Integer32
_Ieee8021BridgeEvbVSINumMACs_Object = MibTableColumn
ieee8021BridgeEvbVSINumMACs = _Ieee8021BridgeEvbVSINumMACs_Object(
    (1, 3, 111, 2, 802, 1, 1, 100, 1, 2, 1, 1, 14),
    _Ieee8021BridgeEvbVSINumMACs_Type()
)
ieee8021BridgeEvbVSINumMACs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021BridgeEvbVSINumMACs.setStatus("current")


class _Ieee8021BridgeEvbVDPMachineState_Type(Integer32):
    """Custom type ieee8021BridgeEvbVDPMachineState based on Integer32"""
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
        *(("associate", 3),
          ("deAssociate", 4),
          ("preAssociate", 1),
          ("preAssociateWithRsrcReservation", 2))
    )


_Ieee8021BridgeEvbVDPMachineState_Type.__name__ = "Integer32"
_Ieee8021BridgeEvbVDPMachineState_Object = MibTableColumn
ieee8021BridgeEvbVDPMachineState = _Ieee8021BridgeEvbVDPMachineState_Object(
    (1, 3, 111, 2, 802, 1, 1, 100, 1, 2, 1, 1, 15),
    _Ieee8021BridgeEvbVDPMachineState_Type()
)
ieee8021BridgeEvbVDPMachineState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021BridgeEvbVDPMachineState.setStatus("current")
_Ieee8021BridgeEvbVDPCommandsSucceeded_Type = Counter32
_Ieee8021BridgeEvbVDPCommandsSucceeded_Object = MibTableColumn
ieee8021BridgeEvbVDPCommandsSucceeded = _Ieee8021BridgeEvbVDPCommandsSucceeded_Object(
    (1, 3, 111, 2, 802, 1, 1, 100, 1, 2, 1, 1, 16),
    _Ieee8021BridgeEvbVDPCommandsSucceeded_Type()
)
ieee8021BridgeEvbVDPCommandsSucceeded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021BridgeEvbVDPCommandsSucceeded.setStatus("current")
_Ieee8021BridgeEvbVDPCommandsFailed_Type = Counter32
_Ieee8021BridgeEvbVDPCommandsFailed_Object = MibTableColumn
ieee8021BridgeEvbVDPCommandsFailed = _Ieee8021BridgeEvbVDPCommandsFailed_Object(
    (1, 3, 111, 2, 802, 1, 1, 100, 1, 2, 1, 1, 17),
    _Ieee8021BridgeEvbVDPCommandsFailed_Type()
)
ieee8021BridgeEvbVDPCommandsFailed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021BridgeEvbVDPCommandsFailed.setStatus("current")
_Ieee8021BridgeEvbVDPCommandReverts_Type = Counter32
_Ieee8021BridgeEvbVDPCommandReverts_Object = MibTableColumn
ieee8021BridgeEvbVDPCommandReverts = _Ieee8021BridgeEvbVDPCommandReverts_Object(
    (1, 3, 111, 2, 802, 1, 1, 100, 1, 2, 1, 1, 18),
    _Ieee8021BridgeEvbVDPCommandReverts_Type()
)
ieee8021BridgeEvbVDPCommandReverts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021BridgeEvbVDPCommandReverts.setStatus("current")
_Ieee8021BridgeEvbVSIDBMacTable_Object = MibTable
ieee8021BridgeEvbVSIDBMacTable = _Ieee8021BridgeEvbVSIDBMacTable_Object(
    (1, 3, 111, 2, 802, 1, 1, 100, 1, 2, 2)
)
if mibBuilder.loadTexts:
    ieee8021BridgeEvbVSIDBMacTable.setStatus("current")
_Ieee8021BridgeEvbVSIDBMacEntry_Object = MibTableRow
ieee8021BridgeEvbVSIDBMacEntry = _Ieee8021BridgeEvbVSIDBMacEntry_Object(
    (1, 3, 111, 2, 802, 1, 1, 100, 1, 2, 2, 1)
)
ieee8021BridgeEvbVSIDBMacEntry.setIndexNames(
    (0, "IEEE8021-EVBB-MIB", "ieee8021BridgeEvbPhyPort"),
    (0, "IEEE8021-EVBB-MIB", "ieee8021BridgeEvbVsiSvid"),
    (0, "IEEE8021-EVBB-MIB", "ieee8021BridgeEvbVSIID"),
    (0, "IEEE8021-EVBB-MIB", "ieee8021BridgeEvbGroupID"),
    (0, "IEEE8021-EVBB-MIB", "ieee8021BridgeEvbVSIMac"),
    (0, "IEEE8021-EVBB-MIB", "ieee8021BridgeEvbVSIVlanId"),
)
if mibBuilder.loadTexts:
    ieee8021BridgeEvbVSIDBMacEntry.setStatus("current")
_Ieee8021BridgeEvbGroupID_Type = Unsigned32
_Ieee8021BridgeEvbGroupID_Object = MibTableColumn
ieee8021BridgeEvbGroupID = _Ieee8021BridgeEvbGroupID_Object(
    (1, 3, 111, 2, 802, 1, 1, 100, 1, 2, 2, 1, 1),
    _Ieee8021BridgeEvbGroupID_Type()
)
ieee8021BridgeEvbGroupID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ieee8021BridgeEvbGroupID.setStatus("current")
_Ieee8021BridgeEvbVSIMac_Type = MacAddress
_Ieee8021BridgeEvbVSIMac_Object = MibTableColumn
ieee8021BridgeEvbVSIMac = _Ieee8021BridgeEvbVSIMac_Object(
    (1, 3, 111, 2, 802, 1, 1, 100, 1, 2, 2, 1, 2),
    _Ieee8021BridgeEvbVSIMac_Type()
)
ieee8021BridgeEvbVSIMac.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ieee8021BridgeEvbVSIMac.setStatus("current")
_Ieee8021BridgeEvbVSIVlanId_Type = VlanIndex
_Ieee8021BridgeEvbVSIVlanId_Object = MibTableColumn
ieee8021BridgeEvbVSIVlanId = _Ieee8021BridgeEvbVSIVlanId_Object(
    (1, 3, 111, 2, 802, 1, 1, 100, 1, 2, 2, 1, 3),
    _Ieee8021BridgeEvbVSIVlanId_Type()
)
ieee8021BridgeEvbVSIVlanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021BridgeEvbVSIVlanId.setStatus("current")
_Ieee8021BridgeEvbSChannelObjects_ObjectIdentity = ObjectIdentity
ieee8021BridgeEvbSChannelObjects = _Ieee8021BridgeEvbSChannelObjects_ObjectIdentity(
    (1, 3, 111, 2, 802, 1, 1, 100, 1, 4)
)
_Ieee8021BridgeEvbUAPConfigTable_Object = MibTable
ieee8021BridgeEvbUAPConfigTable = _Ieee8021BridgeEvbUAPConfigTable_Object(
    (1, 3, 111, 2, 802, 1, 1, 100, 1, 4, 1)
)
if mibBuilder.loadTexts:
    ieee8021BridgeEvbUAPConfigTable.setStatus("current")
_Ieee8021BridgeEvbUAPConfigEntry_Object = MibTableRow
ieee8021BridgeEvbUAPConfigEntry = _Ieee8021BridgeEvbUAPConfigEntry_Object(
    (1, 3, 111, 2, 802, 1, 1, 100, 1, 4, 1, 1)
)
ieee8021BridgeEvbUAPConfigEntry.setIndexNames(
    (0, "IEEE8021-EVBB-MIB", "ieee8021BridgeEvbPhyPort"),
)
if mibBuilder.loadTexts:
    ieee8021BridgeEvbUAPConfigEntry.setStatus("current")
_Ieee8021BridgeEvbUAPComponentId_Type = IEEE8021PbbComponentIdentifier
_Ieee8021BridgeEvbUAPComponentId_Object = MibTableColumn
ieee8021BridgeEvbUAPComponentId = _Ieee8021BridgeEvbUAPComponentId_Object(
    (1, 3, 111, 2, 802, 1, 1, 100, 1, 4, 1, 1, 1),
    _Ieee8021BridgeEvbUAPComponentId_Type()
)
ieee8021BridgeEvbUAPComponentId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021BridgeEvbUAPComponentId.setStatus("current")
_Ieee8021BridgeEvbUAPPort_Type = IEEE8021BridgePortNumber
_Ieee8021BridgeEvbUAPPort_Object = MibTableColumn
ieee8021BridgeEvbUAPPort = _Ieee8021BridgeEvbUAPPort_Object(
    (1, 3, 111, 2, 802, 1, 1, 100, 1, 4, 1, 1, 2),
    _Ieee8021BridgeEvbUAPPort_Type()
)
ieee8021BridgeEvbUAPPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021BridgeEvbUAPPort.setStatus("current")


class _Ieee8021BridgeEvbUAPSchCdcpAdminEnable_Type(Integer32):
    """Custom type ieee8021BridgeEvbUAPSchCdcpAdminEnable based on Integer32"""
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


_Ieee8021BridgeEvbUAPSchCdcpAdminEnable_Type.__name__ = "Integer32"
_Ieee8021BridgeEvbUAPSchCdcpAdminEnable_Object = MibTableColumn
ieee8021BridgeEvbUAPSchCdcpAdminEnable = _Ieee8021BridgeEvbUAPSchCdcpAdminEnable_Object(
    (1, 3, 111, 2, 802, 1, 1, 100, 1, 4, 1, 1, 3),
    _Ieee8021BridgeEvbUAPSchCdcpAdminEnable_Type()
)
ieee8021BridgeEvbUAPSchCdcpAdminEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ieee8021BridgeEvbUAPSchCdcpAdminEnable.setStatus("current")


class _Ieee8021BridgeEvbUAPSchAdminCDCPRole_Type(Integer32):
    """Custom type ieee8021BridgeEvbUAPSchAdminCDCPRole based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("cdcpRoleB", 1),
          ("cdcpRoleS", 2))
    )


_Ieee8021BridgeEvbUAPSchAdminCDCPRole_Type.__name__ = "Integer32"
_Ieee8021BridgeEvbUAPSchAdminCDCPRole_Object = MibTableColumn
ieee8021BridgeEvbUAPSchAdminCDCPRole = _Ieee8021BridgeEvbUAPSchAdminCDCPRole_Object(
    (1, 3, 111, 2, 802, 1, 1, 100, 1, 4, 1, 1, 4),
    _Ieee8021BridgeEvbUAPSchAdminCDCPRole_Type()
)
ieee8021BridgeEvbUAPSchAdminCDCPRole.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ieee8021BridgeEvbUAPSchAdminCDCPRole.setStatus("current")


class _Ieee8021BridgeEvbUAPSchAdminCDCPChanCap_Type(Integer32):
    """Custom type ieee8021BridgeEvbUAPSchAdminCDCPChanCap based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 167),
    )


_Ieee8021BridgeEvbUAPSchAdminCDCPChanCap_Type.__name__ = "Integer32"
_Ieee8021BridgeEvbUAPSchAdminCDCPChanCap_Object = MibTableColumn
ieee8021BridgeEvbUAPSchAdminCDCPChanCap = _Ieee8021BridgeEvbUAPSchAdminCDCPChanCap_Object(
    (1, 3, 111, 2, 802, 1, 1, 100, 1, 4, 1, 1, 5),
    _Ieee8021BridgeEvbUAPSchAdminCDCPChanCap_Type()
)
ieee8021BridgeEvbUAPSchAdminCDCPChanCap.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ieee8021BridgeEvbUAPSchAdminCDCPChanCap.setStatus("current")


class _Ieee8021BridgeEvbUAPSchOperCDCPChanCap_Type(Integer32):
    """Custom type ieee8021BridgeEvbUAPSchOperCDCPChanCap based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 167),
    )


_Ieee8021BridgeEvbUAPSchOperCDCPChanCap_Type.__name__ = "Integer32"
_Ieee8021BridgeEvbUAPSchOperCDCPChanCap_Object = MibTableColumn
ieee8021BridgeEvbUAPSchOperCDCPChanCap = _Ieee8021BridgeEvbUAPSchOperCDCPChanCap_Object(
    (1, 3, 111, 2, 802, 1, 1, 100, 1, 4, 1, 1, 6),
    _Ieee8021BridgeEvbUAPSchOperCDCPChanCap_Type()
)
ieee8021BridgeEvbUAPSchOperCDCPChanCap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021BridgeEvbUAPSchOperCDCPChanCap.setStatus("current")
_Ieee8021BridgeEvbUAPSchAdminCDCPSVIDPoolLow_Type = VlanIndex
_Ieee8021BridgeEvbUAPSchAdminCDCPSVIDPoolLow_Object = MibTableColumn
ieee8021BridgeEvbUAPSchAdminCDCPSVIDPoolLow = _Ieee8021BridgeEvbUAPSchAdminCDCPSVIDPoolLow_Object(
    (1, 3, 111, 2, 802, 1, 1, 100, 1, 4, 1, 1, 7),
    _Ieee8021BridgeEvbUAPSchAdminCDCPSVIDPoolLow_Type()
)
ieee8021BridgeEvbUAPSchAdminCDCPSVIDPoolLow.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ieee8021BridgeEvbUAPSchAdminCDCPSVIDPoolLow.setStatus("current")
_Ieee8021BridgeEvbUAPSchAdminCDCPSVIDPoolHigh_Type = VlanIndex
_Ieee8021BridgeEvbUAPSchAdminCDCPSVIDPoolHigh_Object = MibTableColumn
ieee8021BridgeEvbUAPSchAdminCDCPSVIDPoolHigh = _Ieee8021BridgeEvbUAPSchAdminCDCPSVIDPoolHigh_Object(
    (1, 3, 111, 2, 802, 1, 1, 100, 1, 4, 1, 1, 8),
    _Ieee8021BridgeEvbUAPSchAdminCDCPSVIDPoolHigh_Type()
)
ieee8021BridgeEvbUAPSchAdminCDCPSVIDPoolHigh.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ieee8021BridgeEvbUAPSchAdminCDCPSVIDPoolHigh.setStatus("current")


class _Ieee8021BridgeEvbUAPSchOperState_Type(Integer32):
    """Custom type ieee8021BridgeEvbUAPSchOperState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("notRunning", 2),
          ("running", 1))
    )


_Ieee8021BridgeEvbUAPSchOperState_Type.__name__ = "Integer32"
_Ieee8021BridgeEvbUAPSchOperState_Object = MibTableColumn
ieee8021BridgeEvbUAPSchOperState = _Ieee8021BridgeEvbUAPSchOperState_Object(
    (1, 3, 111, 2, 802, 1, 1, 100, 1, 4, 1, 1, 9),
    _Ieee8021BridgeEvbUAPSchOperState_Type()
)
ieee8021BridgeEvbUAPSchOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021BridgeEvbUAPSchOperState.setStatus("current")


class _Ieee8021BridgeEvbSchCdcpRemoteEnabled_Type(Integer32):
    """Custom type ieee8021BridgeEvbSchCdcpRemoteEnabled based on Integer32"""
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


_Ieee8021BridgeEvbSchCdcpRemoteEnabled_Type.__name__ = "Integer32"
_Ieee8021BridgeEvbSchCdcpRemoteEnabled_Object = MibTableColumn
ieee8021BridgeEvbSchCdcpRemoteEnabled = _Ieee8021BridgeEvbSchCdcpRemoteEnabled_Object(
    (1, 3, 111, 2, 802, 1, 1, 100, 1, 4, 1, 1, 10),
    _Ieee8021BridgeEvbSchCdcpRemoteEnabled_Type()
)
ieee8021BridgeEvbSchCdcpRemoteEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021BridgeEvbSchCdcpRemoteEnabled.setStatus("current")


class _Ieee8021BridgeEvbSchCdcpRemoteRole_Type(Integer32):
    """Custom type ieee8021BridgeEvbSchCdcpRemoteRole based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("cdcpRoleB", 1),
          ("cdcpRoleS", 2))
    )


_Ieee8021BridgeEvbSchCdcpRemoteRole_Type.__name__ = "Integer32"
_Ieee8021BridgeEvbSchCdcpRemoteRole_Object = MibTableColumn
ieee8021BridgeEvbSchCdcpRemoteRole = _Ieee8021BridgeEvbSchCdcpRemoteRole_Object(
    (1, 3, 111, 2, 802, 1, 1, 100, 1, 4, 1, 1, 11),
    _Ieee8021BridgeEvbSchCdcpRemoteRole_Type()
)
ieee8021BridgeEvbSchCdcpRemoteRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021BridgeEvbSchCdcpRemoteRole.setStatus("current")
_Ieee8021BridgeEvbUAPConfigRowStatus_Type = RowStatus
_Ieee8021BridgeEvbUAPConfigRowStatus_Object = MibTableColumn
ieee8021BridgeEvbUAPConfigRowStatus = _Ieee8021BridgeEvbUAPConfigRowStatus_Object(
    (1, 3, 111, 2, 802, 1, 1, 100, 1, 4, 1, 1, 12),
    _Ieee8021BridgeEvbUAPConfigRowStatus_Type()
)
ieee8021BridgeEvbUAPConfigRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ieee8021BridgeEvbUAPConfigRowStatus.setStatus("current")
_Ieee8021BridgeEvbCAPConfigTable_Object = MibTable
ieee8021BridgeEvbCAPConfigTable = _Ieee8021BridgeEvbCAPConfigTable_Object(
    (1, 3, 111, 2, 802, 1, 1, 100, 1, 4, 2)
)
if mibBuilder.loadTexts:
    ieee8021BridgeEvbCAPConfigTable.setStatus("current")
_Ieee8021BridgeEvbCAPConfigEntry_Object = MibTableRow
ieee8021BridgeEvbCAPConfigEntry = _Ieee8021BridgeEvbCAPConfigEntry_Object(
    (1, 3, 111, 2, 802, 1, 1, 100, 1, 4, 2, 1)
)
ieee8021BridgeEvbCAPConfigEntry.setIndexNames(
    (0, "IEEE8021-EVBB-MIB", "ieee8021BridgeEvbPhyPort"),
    (0, "IEEE8021-EVBB-MIB", "ieee8021BridgeEvbVsiSvid"),
)
if mibBuilder.loadTexts:
    ieee8021BridgeEvbCAPConfigEntry.setStatus("current")
_Ieee8021BridgeEvbCAPComponentId_Type = IEEE8021PbbComponentIdentifier
_Ieee8021BridgeEvbCAPComponentId_Object = MibTableColumn
ieee8021BridgeEvbCAPComponentId = _Ieee8021BridgeEvbCAPComponentId_Object(
    (1, 3, 111, 2, 802, 1, 1, 100, 1, 4, 2, 1, 1),
    _Ieee8021BridgeEvbCAPComponentId_Type()
)
ieee8021BridgeEvbCAPComponentId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021BridgeEvbCAPComponentId.setStatus("current")
_Ieee8021BridgeEvbCAPPort_Type = IEEE8021BridgePortNumber
_Ieee8021BridgeEvbCAPPort_Object = MibTableColumn
ieee8021BridgeEvbCAPPort = _Ieee8021BridgeEvbCAPPort_Object(
    (1, 3, 111, 2, 802, 1, 1, 100, 1, 4, 2, 1, 2),
    _Ieee8021BridgeEvbCAPPort_Type()
)
ieee8021BridgeEvbCAPPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021BridgeEvbCAPPort.setStatus("current")
_Ieee8021BridgeEvbCAPSChannelID_Type = Integer32
_Ieee8021BridgeEvbCAPSChannelID_Object = MibTableColumn
ieee8021BridgeEvbCAPSChannelID = _Ieee8021BridgeEvbCAPSChannelID_Object(
    (1, 3, 111, 2, 802, 1, 1, 100, 1, 4, 2, 1, 3),
    _Ieee8021BridgeEvbCAPSChannelID_Type()
)
ieee8021BridgeEvbCAPSChannelID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021BridgeEvbCAPSChannelID.setStatus("current")
_Ieee8021BridgeEvbCAPAssociateSBPCompID_Type = IEEE8021PbbComponentIdentifier
_Ieee8021BridgeEvbCAPAssociateSBPCompID_Object = MibTableColumn
ieee8021BridgeEvbCAPAssociateSBPCompID = _Ieee8021BridgeEvbCAPAssociateSBPCompID_Object(
    (1, 3, 111, 2, 802, 1, 1, 100, 1, 4, 2, 1, 6),
    _Ieee8021BridgeEvbCAPAssociateSBPCompID_Type()
)
ieee8021BridgeEvbCAPAssociateSBPCompID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ieee8021BridgeEvbCAPAssociateSBPCompID.setStatus("current")
_Ieee8021BridgeEvbCAPAssociateSBPPort_Type = IEEE8021BridgePortNumber
_Ieee8021BridgeEvbCAPAssociateSBPPort_Object = MibTableColumn
ieee8021BridgeEvbCAPAssociateSBPPort = _Ieee8021BridgeEvbCAPAssociateSBPPort_Object(
    (1, 3, 111, 2, 802, 1, 1, 100, 1, 4, 2, 1, 7),
    _Ieee8021BridgeEvbCAPAssociateSBPPort_Type()
)
ieee8021BridgeEvbCAPAssociateSBPPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ieee8021BridgeEvbCAPAssociateSBPPort.setStatus("current")


class _Ieee8021BridgeEvbCAPLldpAdminEnables_Type(Bits):
    """Custom type ieee8021BridgeEvbCAPLldpAdminEnables based on Bits"""
    namedValues = NamedValues(
        *(("autoEvbLLDPTLV", 1),
          ("evbTLVEnable", 0))
    )

_Ieee8021BridgeEvbCAPLldpAdminEnables_Type.__name__ = "Bits"
_Ieee8021BridgeEvbCAPLldpAdminEnables_Object = MibTableColumn
ieee8021BridgeEvbCAPLldpAdminEnables = _Ieee8021BridgeEvbCAPLldpAdminEnables_Object(
    (1, 3, 111, 2, 802, 1, 1, 100, 1, 4, 2, 1, 8),
    _Ieee8021BridgeEvbCAPLldpAdminEnables_Type()
)
ieee8021BridgeEvbCAPLldpAdminEnables.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ieee8021BridgeEvbCAPLldpAdminEnables.setStatus("current")
_Ieee8021BridgeEvbCAPLldpAdminCap_Type = IEEE8021BridgeEvbTLVTC
_Ieee8021BridgeEvbCAPLldpAdminCap_Object = MibTableColumn
ieee8021BridgeEvbCAPLldpAdminCap = _Ieee8021BridgeEvbCAPLldpAdminCap_Object(
    (1, 3, 111, 2, 802, 1, 1, 100, 1, 4, 2, 1, 9),
    _Ieee8021BridgeEvbCAPLldpAdminCap_Type()
)
ieee8021BridgeEvbCAPLldpAdminCap.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ieee8021BridgeEvbCAPLldpAdminCap.setStatus("current")
_Ieee8021BridgeEvbCAPLldpOperMode_Type = IEEE8021BridgeEvbTLVTC
_Ieee8021BridgeEvbCAPLldpOperMode_Object = MibTableColumn
ieee8021BridgeEvbCAPLldpOperMode = _Ieee8021BridgeEvbCAPLldpOperMode_Object(
    (1, 3, 111, 2, 802, 1, 1, 100, 1, 4, 2, 1, 10),
    _Ieee8021BridgeEvbCAPLldpOperMode_Type()
)
ieee8021BridgeEvbCAPLldpOperMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021BridgeEvbCAPLldpOperMode.setStatus("current")
_Ieee8021BridgeEvbCAPEcpAdminAckTimerInit_Type = TimeInterval
_Ieee8021BridgeEvbCAPEcpAdminAckTimerInit_Object = MibTableColumn
ieee8021BridgeEvbCAPEcpAdminAckTimerInit = _Ieee8021BridgeEvbCAPEcpAdminAckTimerInit_Object(
    (1, 3, 111, 2, 802, 1, 1, 100, 1, 4, 2, 1, 11),
    _Ieee8021BridgeEvbCAPEcpAdminAckTimerInit_Type()
)
ieee8021BridgeEvbCAPEcpAdminAckTimerInit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ieee8021BridgeEvbCAPEcpAdminAckTimerInit.setStatus("current")
_Ieee8021BridgeEvbCAPEcpOperAckTimerInit_Type = TimeInterval
_Ieee8021BridgeEvbCAPEcpOperAckTimerInit_Object = MibTableColumn
ieee8021BridgeEvbCAPEcpOperAckTimerInit = _Ieee8021BridgeEvbCAPEcpOperAckTimerInit_Object(
    (1, 3, 111, 2, 802, 1, 1, 100, 1, 4, 2, 1, 12),
    _Ieee8021BridgeEvbCAPEcpOperAckTimerInit_Type()
)
ieee8021BridgeEvbCAPEcpOperAckTimerInit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021BridgeEvbCAPEcpOperAckTimerInit.setStatus("current")


class _Ieee8021BridgeEvbCAPEcpAdminMaxTries_Type(Unsigned32):
    """Custom type ieee8021BridgeEvbCAPEcpAdminMaxTries based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16),
    )


_Ieee8021BridgeEvbCAPEcpAdminMaxTries_Type.__name__ = "Unsigned32"
_Ieee8021BridgeEvbCAPEcpAdminMaxTries_Object = MibTableColumn
ieee8021BridgeEvbCAPEcpAdminMaxTries = _Ieee8021BridgeEvbCAPEcpAdminMaxTries_Object(
    (1, 3, 111, 2, 802, 1, 1, 100, 1, 4, 2, 1, 13),
    _Ieee8021BridgeEvbCAPEcpAdminMaxTries_Type()
)
ieee8021BridgeEvbCAPEcpAdminMaxTries.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ieee8021BridgeEvbCAPEcpAdminMaxTries.setStatus("current")


class _Ieee8021BridgeEvbCAPEcpOperMaxRetries_Type(Unsigned32):
    """Custom type ieee8021BridgeEvbCAPEcpOperMaxRetries based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_Ieee8021BridgeEvbCAPEcpOperMaxRetries_Type.__name__ = "Unsigned32"
_Ieee8021BridgeEvbCAPEcpOperMaxRetries_Object = MibTableColumn
ieee8021BridgeEvbCAPEcpOperMaxRetries = _Ieee8021BridgeEvbCAPEcpOperMaxRetries_Object(
    (1, 3, 111, 2, 802, 1, 1, 100, 1, 4, 2, 1, 14),
    _Ieee8021BridgeEvbCAPEcpOperMaxRetries_Type()
)
ieee8021BridgeEvbCAPEcpOperMaxRetries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021BridgeEvbCAPEcpOperMaxRetries.setStatus("current")
_Ieee8021BridgeEvbCAPEcpTxFrameCount_Type = Counter32
_Ieee8021BridgeEvbCAPEcpTxFrameCount_Object = MibTableColumn
ieee8021BridgeEvbCAPEcpTxFrameCount = _Ieee8021BridgeEvbCAPEcpTxFrameCount_Object(
    (1, 3, 111, 2, 802, 1, 1, 100, 1, 4, 2, 1, 15),
    _Ieee8021BridgeEvbCAPEcpTxFrameCount_Type()
)
ieee8021BridgeEvbCAPEcpTxFrameCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021BridgeEvbCAPEcpTxFrameCount.setStatus("current")
_Ieee8021BridgeEvbCAPEcpTxRetryCount_Type = Counter32
_Ieee8021BridgeEvbCAPEcpTxRetryCount_Object = MibTableColumn
ieee8021BridgeEvbCAPEcpTxRetryCount = _Ieee8021BridgeEvbCAPEcpTxRetryCount_Object(
    (1, 3, 111, 2, 802, 1, 1, 100, 1, 4, 2, 1, 16),
    _Ieee8021BridgeEvbCAPEcpTxRetryCount_Type()
)
ieee8021BridgeEvbCAPEcpTxRetryCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021BridgeEvbCAPEcpTxRetryCount.setStatus("current")
_Ieee8021BridgeEvbCAPEcpTxFailures_Type = Counter32
_Ieee8021BridgeEvbCAPEcpTxFailures_Object = MibTableColumn
ieee8021BridgeEvbCAPEcpTxFailures = _Ieee8021BridgeEvbCAPEcpTxFailures_Object(
    (1, 3, 111, 2, 802, 1, 1, 100, 1, 4, 2, 1, 17),
    _Ieee8021BridgeEvbCAPEcpTxFailures_Type()
)
ieee8021BridgeEvbCAPEcpTxFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021BridgeEvbCAPEcpTxFailures.setStatus("current")
_Ieee8021BridgeEvbCAPEcpRxFrameCount_Type = Counter32
_Ieee8021BridgeEvbCAPEcpRxFrameCount_Object = MibTableColumn
ieee8021BridgeEvbCAPEcpRxFrameCount = _Ieee8021BridgeEvbCAPEcpRxFrameCount_Object(
    (1, 3, 111, 2, 802, 1, 1, 100, 1, 4, 2, 1, 18),
    _Ieee8021BridgeEvbCAPEcpRxFrameCount_Type()
)
ieee8021BridgeEvbCAPEcpRxFrameCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021BridgeEvbCAPEcpRxFrameCount.setStatus("current")
_Ieee8021BridgeEvbCAPVdpOperRsrcWaitDelay_Type = TimeInterval
_Ieee8021BridgeEvbCAPVdpOperRsrcWaitDelay_Object = MibTableColumn
ieee8021BridgeEvbCAPVdpOperRsrcWaitDelay = _Ieee8021BridgeEvbCAPVdpOperRsrcWaitDelay_Object(
    (1, 3, 111, 2, 802, 1, 1, 100, 1, 4, 2, 1, 19),
    _Ieee8021BridgeEvbCAPVdpOperRsrcWaitDelay_Type()
)
ieee8021BridgeEvbCAPVdpOperRsrcWaitDelay.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ieee8021BridgeEvbCAPVdpOperRsrcWaitDelay.setStatus("current")
_Ieee8021BridgeEvbCAPVdpOperRespWaitDelay_Type = TimeInterval
_Ieee8021BridgeEvbCAPVdpOperRespWaitDelay_Object = MibTableColumn
ieee8021BridgeEvbCAPVdpOperRespWaitDelay = _Ieee8021BridgeEvbCAPVdpOperRespWaitDelay_Object(
    (1, 3, 111, 2, 802, 1, 1, 100, 1, 4, 2, 1, 20),
    _Ieee8021BridgeEvbCAPVdpOperRespWaitDelay_Type()
)
ieee8021BridgeEvbCAPVdpOperRespWaitDelay.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ieee8021BridgeEvbCAPVdpOperRespWaitDelay.setStatus("current")
_Ieee8021BridgeEvbCAPVdpOperReinitKeepAlive_Type = TimeInterval
_Ieee8021BridgeEvbCAPVdpOperReinitKeepAlive_Object = MibTableColumn
ieee8021BridgeEvbCAPVdpOperReinitKeepAlive = _Ieee8021BridgeEvbCAPVdpOperReinitKeepAlive_Object(
    (1, 3, 111, 2, 802, 1, 1, 100, 1, 4, 2, 1, 21),
    _Ieee8021BridgeEvbCAPVdpOperReinitKeepAlive_Type()
)
ieee8021BridgeEvbCAPVdpOperReinitKeepAlive.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ieee8021BridgeEvbCAPVdpOperReinitKeepAlive.setStatus("current")
_Ieee8021BridgeEvbCAPVdpOperToutKeepAlive_Type = TimeInterval
_Ieee8021BridgeEvbCAPVdpOperToutKeepAlive_Object = MibTableColumn
ieee8021BridgeEvbCAPVdpOperToutKeepAlive = _Ieee8021BridgeEvbCAPVdpOperToutKeepAlive_Object(
    (1, 3, 111, 2, 802, 1, 1, 100, 1, 4, 2, 1, 22),
    _Ieee8021BridgeEvbCAPVdpOperToutKeepAlive_Type()
)
ieee8021BridgeEvbCAPVdpOperToutKeepAlive.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ieee8021BridgeEvbCAPVdpOperToutKeepAlive.setStatus("current")
_Ieee8021BridgeEvbCAPRowStatus_Type = RowStatus
_Ieee8021BridgeEvbCAPRowStatus_Object = MibTableColumn
ieee8021BridgeEvbCAPRowStatus = _Ieee8021BridgeEvbCAPRowStatus_Object(
    (1, 3, 111, 2, 802, 1, 1, 100, 1, 4, 2, 1, 23),
    _Ieee8021BridgeEvbCAPRowStatus_Type()
)
ieee8021BridgeEvbCAPRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ieee8021BridgeEvbCAPRowStatus.setStatus("current")
_Ieee8021BridgeEvbConformance_ObjectIdentity = ObjectIdentity
ieee8021BridgeEvbConformance = _Ieee8021BridgeEvbConformance_ObjectIdentity(
    (1, 3, 111, 2, 802, 1, 1, 100, 2)
)
_Ieee8021BridgeEvbGroups_ObjectIdentity = ObjectIdentity
ieee8021BridgeEvbGroups = _Ieee8021BridgeEvbGroups_ObjectIdentity(
    (1, 3, 111, 2, 802, 1, 1, 100, 2, 1)
)
_Ieee8021BridgeEvbCompliances_ObjectIdentity = ObjectIdentity
ieee8021BridgeEvbCompliances = _Ieee8021BridgeEvbCompliances_ObjectIdentity(
    (1, 3, 111, 2, 802, 1, 1, 100, 2, 2)
)

# Managed Objects groups

ieee8021BridgeEvbConfigGroup = ObjectGroup(
    (1, 3, 111, 2, 802, 1, 1, 100, 2, 1, 1)
)
ieee8021BridgeEvbConfigGroup.setObjects(
      *(("IEEE8021-EVBB-MIB", "ieee8021BridgeEvbSysMACAddress"),
        ("IEEE8021-EVBB-MIB", "ieee8021BridgeEvbSysName"),
        ("IEEE8021-EVBB-MIB", "ieee8021BridgeEvbSysType"),
        ("IEEE8021-EVBB-MIB", "ieee8021BridgeEvbSysNumExternalPorts"),
        ("IEEE8021-EVBB-MIB", "ieee8021BridgeEvbSysEvbLldpEnables"),
        ("IEEE8021-EVBB-MIB", "ieee8021BridgeEvbSysEvbLldpDfltMode"),
        ("IEEE8021-EVBB-MIB", "ieee8021BridgeEvbSysEvbLldpNumVsisSup"),
        ("IEEE8021-EVBB-MIB", "ieee8021BridgeEvbSysNumCorErComps"),
        ("IEEE8021-EVBB-MIB", "ieee8021BridgeEvbSysNumSComps"),
        ("IEEE8021-EVBB-MIB", "ieee8021BridgeEvbECPACkTimer"),
        ("IEEE8021-EVBB-MIB", "ieee8021BridgeEvbECPMaxRetires"),
        ("IEEE8021-EVBB-MIB", "ieee8021BridgeEvbSysVdpDfltRsrcWaitDelay"),
        ("IEEE8021-EVBB-MIB", "ieee8021BridgeEvbSysVdpDfltReinitKeepAlive"))
)
if mibBuilder.loadTexts:
    ieee8021BridgeEvbConfigGroup.setStatus("current")

ieee8021BridgeEvbPhyPortGroup = ObjectGroup(
    (1, 3, 111, 2, 802, 1, 1, 100, 2, 1, 2)
)
ieee8021BridgeEvbPhyPortGroup.setObjects(
      *(("IEEE8021-EVBB-MIB", "ieee8021BridgeEvbPhyPortMacAddress"),
        ("IEEE8021-EVBB-MIB", "ieee8021BridgeEvbPhyPortTypeCap"),
        ("IEEE8021-EVBB-MIB", "ieee8021BridgeEvbPhyPortType"),
        ("IEEE8021-EVBB-MIB", "ieee8021BridgeEvbPhyPortToComponentId"),
        ("IEEE8021-EVBB-MIB", "ieee8021BridgeEvbPhyPortToInternalPort"))
)
if mibBuilder.loadTexts:
    ieee8021BridgeEvbPhyPortGroup.setStatus("current")

ieee8021BridgeEvbPortGroup = ObjectGroup(
    (1, 3, 111, 2, 802, 1, 1, 100, 2, 1, 3)
)
ieee8021BridgeEvbPortGroup.setObjects(
      *(("IEEE8021-EVBB-MIB", "ieee8021BridgeEvbPortType"),
        ("IEEE8021-EVBB-MIB", "ieee8021BridgeEvbPortRowStatus"))
)
if mibBuilder.loadTexts:
    ieee8021BridgeEvbPortGroup.setStatus("current")

ieee8021BridgeEvbVSIDBGroup = ObjectGroup(
    (1, 3, 111, 2, 802, 1, 1, 100, 2, 1, 4)
)
ieee8021BridgeEvbVSIDBGroup.setObjects(
      *(("IEEE8021-EVBB-MIB", "ieee8021BridgeEvbVSIComponentID"),
        ("IEEE8021-EVBB-MIB", "ieee8021BridgeEvbVSIPortNumber"),
        ("IEEE8021-EVBB-MIB", "ieee8021BridgeEvbVSITimeSinceCreate"),
        ("IEEE8021-EVBB-MIB", "ieee8021BridgeEvbVsiVdpOperCmd"),
        ("IEEE8021-EVBB-MIB", "ieee8021BridgeEvbVsiOperRevert"),
        ("IEEE8021-EVBB-MIB", "ieee8021BridgeEvbVsiOperHard"),
        ("IEEE8021-EVBB-MIB", "ieee8021BridgeEvbVsiOperReason"),
        ("IEEE8021-EVBB-MIB", "ieee8021BridgeEvbVSIMgrID"),
        ("IEEE8021-EVBB-MIB", "ieee8021BridgeEvbVSIType"),
        ("IEEE8021-EVBB-MIB", "ieee8021BridgeEvbVSITypeVersion"),
        ("IEEE8021-EVBB-MIB", "ieee8021BridgeEvbVSIMvFormat"),
        ("IEEE8021-EVBB-MIB", "ieee8021BridgeEvbVSINumMACs"),
        ("IEEE8021-EVBB-MIB", "ieee8021BridgeEvbVDPMachineState"),
        ("IEEE8021-EVBB-MIB", "ieee8021BridgeEvbVDPCommandsSucceeded"),
        ("IEEE8021-EVBB-MIB", "ieee8021BridgeEvbVDPCommandsFailed"),
        ("IEEE8021-EVBB-MIB", "ieee8021BridgeEvbVDPCommandReverts"),
        ("IEEE8021-EVBB-MIB", "ieee8021BridgeEvbVSIVlanId"))
)
if mibBuilder.loadTexts:
    ieee8021BridgeEvbVSIDBGroup.setStatus("current")

ieee8021BridgeEvbUAPGroup = ObjectGroup(
    (1, 3, 111, 2, 802, 1, 1, 100, 2, 1, 5)
)
ieee8021BridgeEvbUAPGroup.setObjects(
      *(("IEEE8021-EVBB-MIB", "ieee8021BridgeEvbUAPComponentId"),
        ("IEEE8021-EVBB-MIB", "ieee8021BridgeEvbUAPPort"),
        ("IEEE8021-EVBB-MIB", "ieee8021BridgeEvbUAPSchCdcpAdminEnable"),
        ("IEEE8021-EVBB-MIB", "ieee8021BridgeEvbUAPSchAdminCDCPRole"),
        ("IEEE8021-EVBB-MIB", "ieee8021BridgeEvbUAPSchAdminCDCPChanCap"),
        ("IEEE8021-EVBB-MIB", "ieee8021BridgeEvbUAPSchOperCDCPChanCap"),
        ("IEEE8021-EVBB-MIB", "ieee8021BridgeEvbUAPSchAdminCDCPSVIDPoolLow"),
        ("IEEE8021-EVBB-MIB", "ieee8021BridgeEvbUAPSchAdminCDCPSVIDPoolHigh"),
        ("IEEE8021-EVBB-MIB", "ieee8021BridgeEvbUAPSchOperState"),
        ("IEEE8021-EVBB-MIB", "ieee8021BridgeEvbSchCdcpRemoteEnabled"),
        ("IEEE8021-EVBB-MIB", "ieee8021BridgeEvbSchCdcpRemoteRole"),
        ("IEEE8021-EVBB-MIB", "ieee8021BridgeEvbUAPConfigRowStatus"))
)
if mibBuilder.loadTexts:
    ieee8021BridgeEvbUAPGroup.setStatus("current")

ieee8021BridgeEvbCAPConfigGroup = ObjectGroup(
    (1, 3, 111, 2, 802, 1, 1, 100, 2, 1, 6)
)
ieee8021BridgeEvbCAPConfigGroup.setObjects(
      *(("IEEE8021-EVBB-MIB", "ieee8021BridgeEvbCAPComponentId"),
        ("IEEE8021-EVBB-MIB", "ieee8021BridgeEvbCAPPort"),
        ("IEEE8021-EVBB-MIB", "ieee8021BridgeEvbCAPSChannelID"),
        ("IEEE8021-EVBB-MIB", "ieee8021BridgeEvbCAPAssociateSBPCompID"),
        ("IEEE8021-EVBB-MIB", "ieee8021BridgeEvbCAPAssociateSBPPort"),
        ("IEEE8021-EVBB-MIB", "ieee8021BridgeEvbCAPLldpAdminEnables"),
        ("IEEE8021-EVBB-MIB", "ieee8021BridgeEvbCAPLldpAdminCap"),
        ("IEEE8021-EVBB-MIB", "ieee8021BridgeEvbCAPLldpOperMode"),
        ("IEEE8021-EVBB-MIB", "ieee8021BridgeEvbCAPEcpAdminAckTimerInit"),
        ("IEEE8021-EVBB-MIB", "ieee8021BridgeEvbCAPEcpOperAckTimerInit"),
        ("IEEE8021-EVBB-MIB", "ieee8021BridgeEvbCAPEcpAdminMaxTries"),
        ("IEEE8021-EVBB-MIB", "ieee8021BridgeEvbCAPEcpOperMaxRetries"),
        ("IEEE8021-EVBB-MIB", "ieee8021BridgeEvbCAPEcpTxFrameCount"),
        ("IEEE8021-EVBB-MIB", "ieee8021BridgeEvbCAPEcpTxRetryCount"),
        ("IEEE8021-EVBB-MIB", "ieee8021BridgeEvbCAPEcpTxFailures"),
        ("IEEE8021-EVBB-MIB", "ieee8021BridgeEvbCAPEcpRxFrameCount"),
        ("IEEE8021-EVBB-MIB", "ieee8021BridgeEvbCAPVdpOperRsrcWaitDelay"),
        ("IEEE8021-EVBB-MIB", "ieee8021BridgeEvbCAPVdpOperReinitKeepAlive"),
        ("IEEE8021-EVBB-MIB", "ieee8021BridgeEvbCAPRowStatus"))
)
if mibBuilder.loadTexts:
    ieee8021BridgeEvbCAPConfigGroup.setStatus("current")

ieee8021BridgeEvbbCAPConfigGroup = ObjectGroup(
    (1, 3, 111, 2, 802, 1, 1, 100, 2, 1, 7)
)
ieee8021BridgeEvbbCAPConfigGroup.setObjects(
    ("IEEE8021-EVBB-MIB", "ieee8021BridgeEvbCAPVdpOperToutKeepAlive")
)
if mibBuilder.loadTexts:
    ieee8021BridgeEvbbCAPConfigGroup.setStatus("current")

ieee8021BridgeEvbsCAPConfigGroup = ObjectGroup(
    (1, 3, 111, 2, 802, 1, 1, 100, 2, 1, 8)
)
ieee8021BridgeEvbsCAPConfigGroup.setObjects(
    ("IEEE8021-EVBB-MIB", "ieee8021BridgeEvbCAPVdpOperRespWaitDelay")
)
if mibBuilder.loadTexts:
    ieee8021BridgeEvbsCAPConfigGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

ieee8021BridgeEvbbCompliance = ModuleCompliance(
    (1, 3, 111, 2, 802, 1, 1, 100, 2, 2, 1)
)
if mibBuilder.loadTexts:
    ieee8021BridgeEvbbCompliance.setStatus(
        "current"
    )

ieee8021BridgeEvbsCompliance = ModuleCompliance(
    (1, 3, 111, 2, 802, 1, 1, 100, 2, 2, 2)
)
if mibBuilder.loadTexts:
    ieee8021BridgeEvbsCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "IEEE8021-EVBB-MIB",
    **{"IEEE8021BridgeEvbTLVTC": IEEE8021BridgeEvbTLVTC,
       "ieee8021BridgeEvbMib": ieee8021BridgeEvbMib,
       "ieee8021BridgeEvbNotifications": ieee8021BridgeEvbNotifications,
       "ieee8021BridgeEvbObjects": ieee8021BridgeEvbObjects,
       "ieee8021BridgeEvbConfig": ieee8021BridgeEvbConfig,
       "ieee8021BridgeEvbSysMACAddress": ieee8021BridgeEvbSysMACAddress,
       "ieee8021BridgeEvbSysName": ieee8021BridgeEvbSysName,
       "ieee8021BridgeEvbSysType": ieee8021BridgeEvbSysType,
       "ieee8021BridgeEvbSysNumExternalPorts": ieee8021BridgeEvbSysNumExternalPorts,
       "ieee8021BridgeEvbSysEvbLldpEnables": ieee8021BridgeEvbSysEvbLldpEnables,
       "ieee8021BridgeEvbSysEvbLldpDfltMode": ieee8021BridgeEvbSysEvbLldpDfltMode,
       "ieee8021BridgeEvbSysEvbLldpNumVsisSup": ieee8021BridgeEvbSysEvbLldpNumVsisSup,
       "ieee8021BridgeEvbSysNumCorErComps": ieee8021BridgeEvbSysNumCorErComps,
       "ieee8021BridgeEvbSysNumSComps": ieee8021BridgeEvbSysNumSComps,
       "ieee8021BridgeEvbECPACkTimer": ieee8021BridgeEvbECPACkTimer,
       "ieee8021BridgeEvbECPMaxRetires": ieee8021BridgeEvbECPMaxRetires,
       "ieee8021BridgeEvbSysVdpDfltRsrcWaitDelay": ieee8021BridgeEvbSysVdpDfltRsrcWaitDelay,
       "ieee8021BridgeEvbSysVdpDfltReinitKeepAlive": ieee8021BridgeEvbSysVdpDfltReinitKeepAlive,
       "ieee8021BridgeEvbPhyPortTable": ieee8021BridgeEvbPhyPortTable,
       "ieee8021BridgeEvbPhyPortEntry": ieee8021BridgeEvbPhyPortEntry,
       "ieee8021BridgeEvbPhyPort": ieee8021BridgeEvbPhyPort,
       "ieee8021BridgeEvbPhyPortMacAddress": ieee8021BridgeEvbPhyPortMacAddress,
       "ieee8021BridgeEvbPhyPortTypeCap": ieee8021BridgeEvbPhyPortTypeCap,
       "ieee8021BridgeEvbPhyPortType": ieee8021BridgeEvbPhyPortType,
       "ieee8021BridgeEvbPhyPortToComponentId": ieee8021BridgeEvbPhyPortToComponentId,
       "ieee8021BridgeEvbPhyPortToInternalPort": ieee8021BridgeEvbPhyPortToInternalPort,
       "ieee8021BridgeEvbPortTable": ieee8021BridgeEvbPortTable,
       "ieee8021BridgeEvbPortEntry": ieee8021BridgeEvbPortEntry,
       "ieee8021BridgeEvbPortComponentId": ieee8021BridgeEvbPortComponentId,
       "ieee8021BridgeEvbPort": ieee8021BridgeEvbPort,
       "ieee8021BridgeEvbPortType": ieee8021BridgeEvbPortType,
       "ieee8021BridgeEvbPortRowStatus": ieee8021BridgeEvbPortRowStatus,
       "ieee8021BridgeEvbVSIDBObjects": ieee8021BridgeEvbVSIDBObjects,
       "ieee8021BridgeEvbVSIDBTable": ieee8021BridgeEvbVSIDBTable,
       "ieee8021BridgeEvbVSIDBEntry": ieee8021BridgeEvbVSIDBEntry,
       "ieee8021BridgeEvbVsiSvid": ieee8021BridgeEvbVsiSvid,
       "ieee8021BridgeEvbVSIID": ieee8021BridgeEvbVSIID,
       "ieee8021BridgeEvbVSIComponentID": ieee8021BridgeEvbVSIComponentID,
       "ieee8021BridgeEvbVSIPortNumber": ieee8021BridgeEvbVSIPortNumber,
       "ieee8021BridgeEvbVSITimeSinceCreate": ieee8021BridgeEvbVSITimeSinceCreate,
       "ieee8021BridgeEvbVsiVdpOperCmd": ieee8021BridgeEvbVsiVdpOperCmd,
       "ieee8021BridgeEvbVsiOperRevert": ieee8021BridgeEvbVsiOperRevert,
       "ieee8021BridgeEvbVsiOperHard": ieee8021BridgeEvbVsiOperHard,
       "ieee8021BridgeEvbVsiOperReason": ieee8021BridgeEvbVsiOperReason,
       "ieee8021BridgeEvbVSIMgrID": ieee8021BridgeEvbVSIMgrID,
       "ieee8021BridgeEvbVSIType": ieee8021BridgeEvbVSIType,
       "ieee8021BridgeEvbVSITypeVersion": ieee8021BridgeEvbVSITypeVersion,
       "ieee8021BridgeEvbVSIMvFormat": ieee8021BridgeEvbVSIMvFormat,
       "ieee8021BridgeEvbVSINumMACs": ieee8021BridgeEvbVSINumMACs,
       "ieee8021BridgeEvbVDPMachineState": ieee8021BridgeEvbVDPMachineState,
       "ieee8021BridgeEvbVDPCommandsSucceeded": ieee8021BridgeEvbVDPCommandsSucceeded,
       "ieee8021BridgeEvbVDPCommandsFailed": ieee8021BridgeEvbVDPCommandsFailed,
       "ieee8021BridgeEvbVDPCommandReverts": ieee8021BridgeEvbVDPCommandReverts,
       "ieee8021BridgeEvbVSIDBMacTable": ieee8021BridgeEvbVSIDBMacTable,
       "ieee8021BridgeEvbVSIDBMacEntry": ieee8021BridgeEvbVSIDBMacEntry,
       "ieee8021BridgeEvbGroupID": ieee8021BridgeEvbGroupID,
       "ieee8021BridgeEvbVSIMac": ieee8021BridgeEvbVSIMac,
       "ieee8021BridgeEvbVSIVlanId": ieee8021BridgeEvbVSIVlanId,
       "ieee8021BridgeEvbSChannelObjects": ieee8021BridgeEvbSChannelObjects,
       "ieee8021BridgeEvbUAPConfigTable": ieee8021BridgeEvbUAPConfigTable,
       "ieee8021BridgeEvbUAPConfigEntry": ieee8021BridgeEvbUAPConfigEntry,
       "ieee8021BridgeEvbUAPComponentId": ieee8021BridgeEvbUAPComponentId,
       "ieee8021BridgeEvbUAPPort": ieee8021BridgeEvbUAPPort,
       "ieee8021BridgeEvbUAPSchCdcpAdminEnable": ieee8021BridgeEvbUAPSchCdcpAdminEnable,
       "ieee8021BridgeEvbUAPSchAdminCDCPRole": ieee8021BridgeEvbUAPSchAdminCDCPRole,
       "ieee8021BridgeEvbUAPSchAdminCDCPChanCap": ieee8021BridgeEvbUAPSchAdminCDCPChanCap,
       "ieee8021BridgeEvbUAPSchOperCDCPChanCap": ieee8021BridgeEvbUAPSchOperCDCPChanCap,
       "ieee8021BridgeEvbUAPSchAdminCDCPSVIDPoolLow": ieee8021BridgeEvbUAPSchAdminCDCPSVIDPoolLow,
       "ieee8021BridgeEvbUAPSchAdminCDCPSVIDPoolHigh": ieee8021BridgeEvbUAPSchAdminCDCPSVIDPoolHigh,
       "ieee8021BridgeEvbUAPSchOperState": ieee8021BridgeEvbUAPSchOperState,
       "ieee8021BridgeEvbSchCdcpRemoteEnabled": ieee8021BridgeEvbSchCdcpRemoteEnabled,
       "ieee8021BridgeEvbSchCdcpRemoteRole": ieee8021BridgeEvbSchCdcpRemoteRole,
       "ieee8021BridgeEvbUAPConfigRowStatus": ieee8021BridgeEvbUAPConfigRowStatus,
       "ieee8021BridgeEvbCAPConfigTable": ieee8021BridgeEvbCAPConfigTable,
       "ieee8021BridgeEvbCAPConfigEntry": ieee8021BridgeEvbCAPConfigEntry,
       "ieee8021BridgeEvbCAPComponentId": ieee8021BridgeEvbCAPComponentId,
       "ieee8021BridgeEvbCAPPort": ieee8021BridgeEvbCAPPort,
       "ieee8021BridgeEvbCAPSChannelID": ieee8021BridgeEvbCAPSChannelID,
       "ieee8021BridgeEvbCAPAssociateSBPCompID": ieee8021BridgeEvbCAPAssociateSBPCompID,
       "ieee8021BridgeEvbCAPAssociateSBPPort": ieee8021BridgeEvbCAPAssociateSBPPort,
       "ieee8021BridgeEvbCAPLldpAdminEnables": ieee8021BridgeEvbCAPLldpAdminEnables,
       "ieee8021BridgeEvbCAPLldpAdminCap": ieee8021BridgeEvbCAPLldpAdminCap,
       "ieee8021BridgeEvbCAPLldpOperMode": ieee8021BridgeEvbCAPLldpOperMode,
       "ieee8021BridgeEvbCAPEcpAdminAckTimerInit": ieee8021BridgeEvbCAPEcpAdminAckTimerInit,
       "ieee8021BridgeEvbCAPEcpOperAckTimerInit": ieee8021BridgeEvbCAPEcpOperAckTimerInit,
       "ieee8021BridgeEvbCAPEcpAdminMaxTries": ieee8021BridgeEvbCAPEcpAdminMaxTries,
       "ieee8021BridgeEvbCAPEcpOperMaxRetries": ieee8021BridgeEvbCAPEcpOperMaxRetries,
       "ieee8021BridgeEvbCAPEcpTxFrameCount": ieee8021BridgeEvbCAPEcpTxFrameCount,
       "ieee8021BridgeEvbCAPEcpTxRetryCount": ieee8021BridgeEvbCAPEcpTxRetryCount,
       "ieee8021BridgeEvbCAPEcpTxFailures": ieee8021BridgeEvbCAPEcpTxFailures,
       "ieee8021BridgeEvbCAPEcpRxFrameCount": ieee8021BridgeEvbCAPEcpRxFrameCount,
       "ieee8021BridgeEvbCAPVdpOperRsrcWaitDelay": ieee8021BridgeEvbCAPVdpOperRsrcWaitDelay,
       "ieee8021BridgeEvbCAPVdpOperRespWaitDelay": ieee8021BridgeEvbCAPVdpOperRespWaitDelay,
       "ieee8021BridgeEvbCAPVdpOperReinitKeepAlive": ieee8021BridgeEvbCAPVdpOperReinitKeepAlive,
       "ieee8021BridgeEvbCAPVdpOperToutKeepAlive": ieee8021BridgeEvbCAPVdpOperToutKeepAlive,
       "ieee8021BridgeEvbCAPRowStatus": ieee8021BridgeEvbCAPRowStatus,
       "ieee8021BridgeEvbConformance": ieee8021BridgeEvbConformance,
       "ieee8021BridgeEvbGroups": ieee8021BridgeEvbGroups,
       "ieee8021BridgeEvbConfigGroup": ieee8021BridgeEvbConfigGroup,
       "ieee8021BridgeEvbPhyPortGroup": ieee8021BridgeEvbPhyPortGroup,
       "ieee8021BridgeEvbPortGroup": ieee8021BridgeEvbPortGroup,
       "ieee8021BridgeEvbVSIDBGroup": ieee8021BridgeEvbVSIDBGroup,
       "ieee8021BridgeEvbUAPGroup": ieee8021BridgeEvbUAPGroup,
       "ieee8021BridgeEvbCAPConfigGroup": ieee8021BridgeEvbCAPConfigGroup,
       "ieee8021BridgeEvbbCAPConfigGroup": ieee8021BridgeEvbbCAPConfigGroup,
       "ieee8021BridgeEvbsCAPConfigGroup": ieee8021BridgeEvbsCAPConfigGroup,
       "ieee8021BridgeEvbCompliances": ieee8021BridgeEvbCompliances,
       "ieee8021BridgeEvbbCompliance": ieee8021BridgeEvbbCompliance,
       "ieee8021BridgeEvbsCompliance": ieee8021BridgeEvbsCompliance}
)
