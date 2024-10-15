# SNMP MIB module (IEEE8021-PE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/IEEE8021-PE-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:08:33 2024
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
 ieee802dot1mibs) = mibBuilder.importSymbols(
    "IEEE8021-TC-MIB",
    "IEEE8021BridgePortNumber",
    "IEEE8021BridgePortNumberOrZero",
    "IEEE8021PbbComponentIdentifier",
    "ieee802dot1mibs")

(PortList,) = mibBuilder.importSymbols(
    "Q-BRIDGE-MIB",
    "PortList")

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
 TextualConvention,
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "TextualConvention",
    "TimeStamp",
    "TruthValue")


# MODULE-IDENTITY

ieee8021BridgePEMib = ModuleIdentity(
    (1, 3, 111, 2, 802, 1, 1, 25)
)
ieee8021BridgePEMib.setRevisions(
        ("2012-01-22 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class IEEE802BridgePEEChannelIDTC(Unsigned32, TextualConvention):
    status = "current"
    displayHint = "d"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4194302),
    )



class IEEE802BridgePETrafficClassValueTC(Unsigned32, TextualConvention):
    status = "current"
    displayHint = "d"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )



class IEEE802BridgePETrafficSelectionAlgorithmTC(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              255)
        )
    )
    namedValues = NamedValues(
        *(("tsaCreditBasedShaper", 1),
          ("tsaEnhancedTransmission", 2),
          ("tsaStrictPriority", 0),
          ("tsaVendorSpecific", 255))
    )



class IEEE802BridgePETrafficClassBandwidthValue(Unsigned32, TextualConvention):
    status = "current"
    displayHint = "d"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )



# MIB Managed Objects in the order of their OIDs

_Ieee8021BridgePENotifications_ObjectIdentity = ObjectIdentity
ieee8021BridgePENotifications = _Ieee8021BridgePENotifications_ObjectIdentity(
    (1, 3, 111, 2, 802, 1, 1, 25, 1)
)
_Ieee8021BridgePEObjects_ObjectIdentity = ObjectIdentity
ieee8021BridgePEObjects = _Ieee8021BridgePEObjects_ObjectIdentity(
    (1, 3, 111, 2, 802, 1, 1, 25, 2)
)
_Ieee8021BridgePEPortTable_Object = MibTable
ieee8021BridgePEPortTable = _Ieee8021BridgePEPortTable_Object(
    (1, 3, 111, 2, 802, 1, 1, 25, 2, 1)
)
if mibBuilder.loadTexts:
    ieee8021BridgePEPortTable.setStatus("current")
_Ieee8021BridgePEPortEntry_Object = MibTableRow
ieee8021BridgePEPortEntry = _Ieee8021BridgePEPortEntry_Object(
    (1, 3, 111, 2, 802, 1, 1, 25, 2, 1, 1)
)
ieee8021BridgePEPortEntry.setIndexNames(
    (0, "IEEE8021-PE-MIB", "ieee8021BridgePEPortComponentId"),
    (0, "IEEE8021-PE-MIB", "ieee8021BridgePEPort"),
    (0, "IEEE8021-PE-MIB", "ieee8021BridgePEPortType"),
)
if mibBuilder.loadTexts:
    ieee8021BridgePEPortEntry.setStatus("current")
_Ieee8021BridgePEPortComponentId_Type = IEEE8021PbbComponentIdentifier
_Ieee8021BridgePEPortComponentId_Object = MibTableColumn
ieee8021BridgePEPortComponentId = _Ieee8021BridgePEPortComponentId_Object(
    (1, 3, 111, 2, 802, 1, 1, 25, 2, 1, 1, 1),
    _Ieee8021BridgePEPortComponentId_Type()
)
ieee8021BridgePEPortComponentId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ieee8021BridgePEPortComponentId.setStatus("current")
_Ieee8021BridgePEPort_Type = IEEE8021BridgePortNumber
_Ieee8021BridgePEPort_Object = MibTableColumn
ieee8021BridgePEPort = _Ieee8021BridgePEPort_Object(
    (1, 3, 111, 2, 802, 1, 1, 25, 2, 1, 1, 2),
    _Ieee8021BridgePEPort_Type()
)
ieee8021BridgePEPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ieee8021BridgePEPort.setStatus("current")


class _Ieee8021BridgePEPortType_Type(Integer32):
    """Custom type ieee8021BridgePEPortType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("pepCascade", 1),
          ("pepExtended", 3),
          ("pepUpstream", 2))
    )


_Ieee8021BridgePEPortType_Type.__name__ = "Integer32"
_Ieee8021BridgePEPortType_Object = MibTableColumn
ieee8021BridgePEPortType = _Ieee8021BridgePEPortType_Object(
    (1, 3, 111, 2, 802, 1, 1, 25, 2, 1, 1, 3),
    _Ieee8021BridgePEPortType_Type()
)
ieee8021BridgePEPortType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ieee8021BridgePEPortType.setStatus("current")
_Ieee8021BridgePEPortUpstreamCSPAddress_Type = MacAddress
_Ieee8021BridgePEPortUpstreamCSPAddress_Object = MibTableColumn
ieee8021BridgePEPortUpstreamCSPAddress = _Ieee8021BridgePEPortUpstreamCSPAddress_Object(
    (1, 3, 111, 2, 802, 1, 1, 25, 2, 1, 1, 4),
    _Ieee8021BridgePEPortUpstreamCSPAddress_Type()
)
ieee8021BridgePEPortUpstreamCSPAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021BridgePEPortUpstreamCSPAddress.setStatus("current")
_Ieee8021BridgePEPortEcid_Type = IEEE802BridgePEEChannelIDTC
_Ieee8021BridgePEPortEcid_Object = MibTableColumn
ieee8021BridgePEPortEcid = _Ieee8021BridgePEPortEcid_Object(
    (1, 3, 111, 2, 802, 1, 1, 25, 2, 1, 1, 5),
    _Ieee8021BridgePEPortEcid_Type()
)
ieee8021BridgePEPortEcid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021BridgePEPortEcid.setStatus("current")
_Ieee8021BridgePEPortNumber_Type = IEEE8021BridgePortNumberOrZero
_Ieee8021BridgePEPortNumber_Object = MibTableColumn
ieee8021BridgePEPortNumber = _Ieee8021BridgePEPortNumber_Object(
    (1, 3, 111, 2, 802, 1, 1, 25, 2, 1, 1, 6),
    _Ieee8021BridgePEPortNumber_Type()
)
ieee8021BridgePEPortNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021BridgePEPortNumber.setStatus("current")
_Ieee8021BridgePECounterDiscontinuityTime_Type = TimeStamp
_Ieee8021BridgePECounterDiscontinuityTime_Object = MibTableColumn
ieee8021BridgePECounterDiscontinuityTime = _Ieee8021BridgePECounterDiscontinuityTime_Object(
    (1, 3, 111, 2, 802, 1, 1, 25, 2, 1, 1, 7),
    _Ieee8021BridgePECounterDiscontinuityTime_Type()
)
ieee8021BridgePECounterDiscontinuityTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021BridgePECounterDiscontinuityTime.setStatus("current")
_Ieee8021BridgePEPortRxrqErrorsBridge_Type = Counter64
_Ieee8021BridgePEPortRxrqErrorsBridge_Object = MibTableColumn
ieee8021BridgePEPortRxrqErrorsBridge = _Ieee8021BridgePEPortRxrqErrorsBridge_Object(
    (1, 3, 111, 2, 802, 1, 1, 25, 2, 1, 1, 8),
    _Ieee8021BridgePEPortRxrqErrorsBridge_Type()
)
ieee8021BridgePEPortRxrqErrorsBridge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021BridgePEPortRxrqErrorsBridge.setStatus("current")
if mibBuilder.loadTexts:
    ieee8021BridgePEPortRxrqErrorsBridge.setUnits("frames")
_Ieee8021BridgePEPortRxrspErrorsBridge_Type = Counter64
_Ieee8021BridgePEPortRxrspErrorsBridge_Object = MibTableColumn
ieee8021BridgePEPortRxrspErrorsBridge = _Ieee8021BridgePEPortRxrspErrorsBridge_Object(
    (1, 3, 111, 2, 802, 1, 1, 25, 2, 1, 1, 9),
    _Ieee8021BridgePEPortRxrspErrorsBridge_Type()
)
ieee8021BridgePEPortRxrspErrorsBridge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021BridgePEPortRxrspErrorsBridge.setStatus("current")
if mibBuilder.loadTexts:
    ieee8021BridgePEPortRxrspErrorsBridge.setUnits("octets")
_Ieee8021BridgePEPortRxrqErrorsPE_Type = Counter64
_Ieee8021BridgePEPortRxrqErrorsPE_Object = MibTableColumn
ieee8021BridgePEPortRxrqErrorsPE = _Ieee8021BridgePEPortRxrqErrorsPE_Object(
    (1, 3, 111, 2, 802, 1, 1, 25, 2, 1, 1, 10),
    _Ieee8021BridgePEPortRxrqErrorsPE_Type()
)
ieee8021BridgePEPortRxrqErrorsPE.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021BridgePEPortRxrqErrorsPE.setStatus("current")
if mibBuilder.loadTexts:
    ieee8021BridgePEPortRxrqErrorsPE.setUnits("frames")
_Ieee8021BridgePEPortRxrspErrorsPE_Type = Counter64
_Ieee8021BridgePEPortRxrspErrorsPE_Object = MibTableColumn
ieee8021BridgePEPortRxrspErrorsPE = _Ieee8021BridgePEPortRxrspErrorsPE_Object(
    (1, 3, 111, 2, 802, 1, 1, 25, 2, 1, 1, 11),
    _Ieee8021BridgePEPortRxrspErrorsPE_Type()
)
ieee8021BridgePEPortRxrspErrorsPE.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021BridgePEPortRxrspErrorsPE.setStatus("current")
if mibBuilder.loadTexts:
    ieee8021BridgePEPortRxrspErrorsPE.setUnits("octets")
_Ieee8021BridgePEPCP_Type = TruthValue
_Ieee8021BridgePEPCP_Object = MibTableColumn
ieee8021BridgePEPCP = _Ieee8021BridgePEPCP_Object(
    (1, 3, 111, 2, 802, 1, 1, 25, 2, 1, 1, 12),
    _Ieee8021BridgePEPCP_Type()
)
ieee8021BridgePEPCP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021BridgePEPCP.setStatus("current")
_Ieee8021BridgePEROW_Type = TruthValue
_Ieee8021BridgePEROW_Object = MibTableColumn
ieee8021BridgePEROW = _Ieee8021BridgePEROW_Object(
    (1, 3, 111, 2, 802, 1, 1, 25, 2, 1, 1, 13),
    _Ieee8021BridgePEROW_Type()
)
ieee8021BridgePEROW.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021BridgePEROW.setStatus("current")
_Ieee8021BridgePEDEI_Type = TruthValue
_Ieee8021BridgePEDEI_Object = MibTableColumn
ieee8021BridgePEDEI = _Ieee8021BridgePEDEI_Object(
    (1, 3, 111, 2, 802, 1, 1, 25, 2, 1, 1, 14),
    _Ieee8021BridgePEDEI_Type()
)
ieee8021BridgePEDEI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021BridgePEDEI.setStatus("current")
_Ieee8021BridgePECN_Type = TruthValue
_Ieee8021BridgePECN_Object = MibTableColumn
ieee8021BridgePECN = _Ieee8021BridgePECN_Object(
    (1, 3, 111, 2, 802, 1, 1, 25, 2, 1, 1, 15),
    _Ieee8021BridgePECN_Type()
)
ieee8021BridgePECN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021BridgePECN.setStatus("current")
_Ieee8021BridgePEPFC_Type = TruthValue
_Ieee8021BridgePEPFC_Object = MibTableColumn
ieee8021BridgePEPFC = _Ieee8021BridgePEPFC_Object(
    (1, 3, 111, 2, 802, 1, 1, 25, 2, 1, 1, 16),
    _Ieee8021BridgePEPFC_Type()
)
ieee8021BridgePEPFC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021BridgePEPFC.setStatus("current")


class _Ieee8021BridgePEExtPortEChannelsSupported_Type(Unsigned32):
    """Custom type ieee8021BridgePEExtPortEChannelsSupported based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1048575),
    )


_Ieee8021BridgePEExtPortEChannelsSupported_Type.__name__ = "Unsigned32"
_Ieee8021BridgePEExtPortEChannelsSupported_Object = MibTableColumn
ieee8021BridgePEExtPortEChannelsSupported = _Ieee8021BridgePEExtPortEChannelsSupported_Object(
    (1, 3, 111, 2, 802, 1, 1, 25, 2, 1, 1, 17),
    _Ieee8021BridgePEExtPortEChannelsSupported_Type()
)
ieee8021BridgePEExtPortEChannelsSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021BridgePEExtPortEChannelsSupported.setStatus("current")
if mibBuilder.loadTexts:
    ieee8021BridgePEExtPortEChannelsSupported.setUnits("E-channels")


class _Ieee8021BridgePERemoteRepEChannelsSupported_Type(Unsigned32):
    """Custom type ieee8021BridgePERemoteRepEChannelsSupported based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3145727),
    )


_Ieee8021BridgePERemoteRepEChannelsSupported_Type.__name__ = "Unsigned32"
_Ieee8021BridgePERemoteRepEChannelsSupported_Object = MibTableColumn
ieee8021BridgePERemoteRepEChannelsSupported = _Ieee8021BridgePERemoteRepEChannelsSupported_Object(
    (1, 3, 111, 2, 802, 1, 1, 25, 2, 1, 1, 18),
    _Ieee8021BridgePERemoteRepEChannelsSupported_Type()
)
ieee8021BridgePERemoteRepEChannelsSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021BridgePERemoteRepEChannelsSupported.setStatus("current")
if mibBuilder.loadTexts:
    ieee8021BridgePERemoteRepEChannelsSupported.setUnits("E-channels")


class _Ieee8021BridgePETCsSupported_Type(Unsigned32):
    """Custom type ieee8021BridgePETCsSupported based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_Ieee8021BridgePETCsSupported_Type.__name__ = "Unsigned32"
_Ieee8021BridgePETCsSupported_Object = MibTableColumn
ieee8021BridgePETCsSupported = _Ieee8021BridgePETCsSupported_Object(
    (1, 3, 111, 2, 802, 1, 1, 25, 2, 1, 1, 19),
    _Ieee8021BridgePETCsSupported_Type()
)
ieee8021BridgePETCsSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021BridgePETCsSupported.setStatus("current")
if mibBuilder.loadTexts:
    ieee8021BridgePETCsSupported.setUnits("traffic classes")


class _Ieee8021BridgePEUtVLANsSupported_Type(Unsigned32):
    """Custom type ieee8021BridgePEUtVLANsSupported based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_Ieee8021BridgePEUtVLANsSupported_Type.__name__ = "Unsigned32"
_Ieee8021BridgePEUtVLANsSupported_Object = MibTableColumn
ieee8021BridgePEUtVLANsSupported = _Ieee8021BridgePEUtVLANsSupported_Object(
    (1, 3, 111, 2, 802, 1, 1, 25, 2, 1, 1, 20),
    _Ieee8021BridgePEUtVLANsSupported_Type()
)
ieee8021BridgePEUtVLANsSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021BridgePEUtVLANsSupported.setStatus("current")
if mibBuilder.loadTexts:
    ieee8021BridgePEUtVLANsSupported.setUnits("VLANs")
_Ieee8021BridgePERemoteReplicationTable_Object = MibTable
ieee8021BridgePERemoteReplicationTable = _Ieee8021BridgePERemoteReplicationTable_Object(
    (1, 3, 111, 2, 802, 1, 1, 25, 2, 2)
)
if mibBuilder.loadTexts:
    ieee8021BridgePERemoteReplicationTable.setStatus("current")
_Ieee8021BridgePERemoteReplicationEntry_Object = MibTableRow
ieee8021BridgePERemoteReplicationEntry = _Ieee8021BridgePERemoteReplicationEntry_Object(
    (1, 3, 111, 2, 802, 1, 1, 25, 2, 2, 1)
)
ieee8021BridgePERemoteReplicationEntry.setIndexNames(
    (0, "IEEE8021-PE-MIB", "ieee8021BridgePEPortComponentId"),
    (0, "IEEE8021-PE-MIB", "ieee8021BridgePERREcid"),
)
if mibBuilder.loadTexts:
    ieee8021BridgePERemoteReplicationEntry.setStatus("current")
_Ieee8021BridgePERREcid_Type = IEEE802BridgePEEChannelIDTC
_Ieee8021BridgePERREcid_Object = MibTableColumn
ieee8021BridgePERREcid = _Ieee8021BridgePERREcid_Object(
    (1, 3, 111, 2, 802, 1, 1, 25, 2, 2, 1, 1),
    _Ieee8021BridgePERREcid_Type()
)
ieee8021BridgePERREcid.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ieee8021BridgePERREcid.setStatus("current")
_Ieee8021BridgePERRPortMap_Type = PortList
_Ieee8021BridgePERRPortMap_Object = MibTableColumn
ieee8021BridgePERRPortMap = _Ieee8021BridgePERRPortMap_Object(
    (1, 3, 111, 2, 802, 1, 1, 25, 2, 2, 1, 2),
    _Ieee8021BridgePERRPortMap_Type()
)
ieee8021BridgePERRPortMap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021BridgePERRPortMap.setStatus("current")
_Ieee8021BridgePEETSTable_Object = MibTable
ieee8021BridgePEETSTable = _Ieee8021BridgePEETSTable_Object(
    (1, 3, 111, 2, 802, 1, 1, 25, 2, 3)
)
if mibBuilder.loadTexts:
    ieee8021BridgePEETSTable.setStatus("current")
_Ieee8021BridgePEETSEntry_Object = MibTableRow
ieee8021BridgePEETSEntry = _Ieee8021BridgePEETSEntry_Object(
    (1, 3, 111, 2, 802, 1, 1, 25, 2, 3, 1)
)
ieee8021BridgePEETSEntry.setIndexNames(
    (0, "IEEE8021-PE-MIB", "ieee8021BridgePEPortComponentId"),
    (0, "IEEE8021-PE-MIB", "ieee8021BridgePEPort"),
    (0, "IEEE8021-PE-MIB", "ieee8021BridgePEETSTrafficClass"),
)
if mibBuilder.loadTexts:
    ieee8021BridgePEETSEntry.setStatus("current")
_Ieee8021BridgePEETSTrafficClass_Type = IEEE802BridgePETrafficClassValueTC
_Ieee8021BridgePEETSTrafficClass_Object = MibTableColumn
ieee8021BridgePEETSTrafficClass = _Ieee8021BridgePEETSTrafficClass_Object(
    (1, 3, 111, 2, 802, 1, 1, 25, 2, 3, 1, 1),
    _Ieee8021BridgePEETSTrafficClass_Type()
)
ieee8021BridgePEETSTrafficClass.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ieee8021BridgePEETSTrafficClass.setStatus("current")
_Ieee8021BridgePEETSTrafficSelectionAlgorthm_Type = IEEE802BridgePETrafficSelectionAlgorithmTC
_Ieee8021BridgePEETSTrafficSelectionAlgorthm_Object = MibTableColumn
ieee8021BridgePEETSTrafficSelectionAlgorthm = _Ieee8021BridgePEETSTrafficSelectionAlgorthm_Object(
    (1, 3, 111, 2, 802, 1, 1, 25, 2, 3, 1, 2),
    _Ieee8021BridgePEETSTrafficSelectionAlgorthm_Type()
)
ieee8021BridgePEETSTrafficSelectionAlgorthm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ieee8021BridgePEETSTrafficSelectionAlgorthm.setStatus("current")
_Ieee8021BridgePEETSBandwidth_Type = IEEE802BridgePETrafficClassBandwidthValue
_Ieee8021BridgePEETSBandwidth_Object = MibTableColumn
ieee8021BridgePEETSBandwidth = _Ieee8021BridgePEETSBandwidth_Object(
    (1, 3, 111, 2, 802, 1, 1, 25, 2, 3, 1, 3),
    _Ieee8021BridgePEETSBandwidth_Type()
)
ieee8021BridgePEETSBandwidth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ieee8021BridgePEETSBandwidth.setStatus("current")
_Ieee8021BridgePEConformance_ObjectIdentity = ObjectIdentity
ieee8021BridgePEConformance = _Ieee8021BridgePEConformance_ObjectIdentity(
    (1, 3, 111, 2, 802, 1, 1, 25, 3)
)
_Ieee8021BridgePEGroups_ObjectIdentity = ObjectIdentity
ieee8021BridgePEGroups = _Ieee8021BridgePEGroups_ObjectIdentity(
    (1, 3, 111, 2, 802, 1, 1, 25, 3, 1)
)
_Ieee8021BridgePECompliances_ObjectIdentity = ObjectIdentity
ieee8021BridgePECompliances = _Ieee8021BridgePECompliances_ObjectIdentity(
    (1, 3, 111, 2, 802, 1, 1, 25, 3, 2)
)

# Managed Objects groups

ieee8021BridgePEGroup = ObjectGroup(
    (1, 3, 111, 2, 802, 1, 1, 25, 3, 1, 1)
)
ieee8021BridgePEGroup.setObjects(
      *(("IEEE8021-PE-MIB", "ieee8021BridgePEPortUpstreamCSPAddress"),
        ("IEEE8021-PE-MIB", "ieee8021BridgePEPortEcid"),
        ("IEEE8021-PE-MIB", "ieee8021BridgePEPortNumber"),
        ("IEEE8021-PE-MIB", "ieee8021BridgePECounterDiscontinuityTime"),
        ("IEEE8021-PE-MIB", "ieee8021BridgePEPortRxrqErrorsBridge"),
        ("IEEE8021-PE-MIB", "ieee8021BridgePEPortRxrspErrorsBridge"),
        ("IEEE8021-PE-MIB", "ieee8021BridgePEPortRxrqErrorsPE"),
        ("IEEE8021-PE-MIB", "ieee8021BridgePEPortRxrspErrorsPE"),
        ("IEEE8021-PE-MIB", "ieee8021BridgePEPCP"),
        ("IEEE8021-PE-MIB", "ieee8021BridgePEROW"),
        ("IEEE8021-PE-MIB", "ieee8021BridgePEDEI"),
        ("IEEE8021-PE-MIB", "ieee8021BridgePECN"),
        ("IEEE8021-PE-MIB", "ieee8021BridgePEPFC"),
        ("IEEE8021-PE-MIB", "ieee8021BridgePEExtPortEChannelsSupported"),
        ("IEEE8021-PE-MIB", "ieee8021BridgePERemoteRepEChannelsSupported"),
        ("IEEE8021-PE-MIB", "ieee8021BridgePETCsSupported"),
        ("IEEE8021-PE-MIB", "ieee8021BridgePEUtVLANsSupported"),
        ("IEEE8021-PE-MIB", "ieee8021BridgePERRPortMap"),
        ("IEEE8021-PE-MIB", "ieee8021BridgePEETSTrafficSelectionAlgorthm"),
        ("IEEE8021-PE-MIB", "ieee8021BridgePEETSBandwidth"))
)
if mibBuilder.loadTexts:
    ieee8021BridgePEGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

ieee8021BridgePECompliance = ModuleCompliance(
    (1, 3, 111, 2, 802, 1, 1, 25, 3, 2, 1)
)
if mibBuilder.loadTexts:
    ieee8021BridgePECompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "IEEE8021-PE-MIB",
    **{"IEEE802BridgePEEChannelIDTC": IEEE802BridgePEEChannelIDTC,
       "IEEE802BridgePETrafficClassValueTC": IEEE802BridgePETrafficClassValueTC,
       "IEEE802BridgePETrafficSelectionAlgorithmTC": IEEE802BridgePETrafficSelectionAlgorithmTC,
       "IEEE802BridgePETrafficClassBandwidthValue": IEEE802BridgePETrafficClassBandwidthValue,
       "ieee8021BridgePEMib": ieee8021BridgePEMib,
       "ieee8021BridgePENotifications": ieee8021BridgePENotifications,
       "ieee8021BridgePEObjects": ieee8021BridgePEObjects,
       "ieee8021BridgePEPortTable": ieee8021BridgePEPortTable,
       "ieee8021BridgePEPortEntry": ieee8021BridgePEPortEntry,
       "ieee8021BridgePEPortComponentId": ieee8021BridgePEPortComponentId,
       "ieee8021BridgePEPort": ieee8021BridgePEPort,
       "ieee8021BridgePEPortType": ieee8021BridgePEPortType,
       "ieee8021BridgePEPortUpstreamCSPAddress": ieee8021BridgePEPortUpstreamCSPAddress,
       "ieee8021BridgePEPortEcid": ieee8021BridgePEPortEcid,
       "ieee8021BridgePEPortNumber": ieee8021BridgePEPortNumber,
       "ieee8021BridgePECounterDiscontinuityTime": ieee8021BridgePECounterDiscontinuityTime,
       "ieee8021BridgePEPortRxrqErrorsBridge": ieee8021BridgePEPortRxrqErrorsBridge,
       "ieee8021BridgePEPortRxrspErrorsBridge": ieee8021BridgePEPortRxrspErrorsBridge,
       "ieee8021BridgePEPortRxrqErrorsPE": ieee8021BridgePEPortRxrqErrorsPE,
       "ieee8021BridgePEPortRxrspErrorsPE": ieee8021BridgePEPortRxrspErrorsPE,
       "ieee8021BridgePEPCP": ieee8021BridgePEPCP,
       "ieee8021BridgePEROW": ieee8021BridgePEROW,
       "ieee8021BridgePEDEI": ieee8021BridgePEDEI,
       "ieee8021BridgePECN": ieee8021BridgePECN,
       "ieee8021BridgePEPFC": ieee8021BridgePEPFC,
       "ieee8021BridgePEExtPortEChannelsSupported": ieee8021BridgePEExtPortEChannelsSupported,
       "ieee8021BridgePERemoteRepEChannelsSupported": ieee8021BridgePERemoteRepEChannelsSupported,
       "ieee8021BridgePETCsSupported": ieee8021BridgePETCsSupported,
       "ieee8021BridgePEUtVLANsSupported": ieee8021BridgePEUtVLANsSupported,
       "ieee8021BridgePERemoteReplicationTable": ieee8021BridgePERemoteReplicationTable,
       "ieee8021BridgePERemoteReplicationEntry": ieee8021BridgePERemoteReplicationEntry,
       "ieee8021BridgePERREcid": ieee8021BridgePERREcid,
       "ieee8021BridgePERRPortMap": ieee8021BridgePERRPortMap,
       "ieee8021BridgePEETSTable": ieee8021BridgePEETSTable,
       "ieee8021BridgePEETSEntry": ieee8021BridgePEETSEntry,
       "ieee8021BridgePEETSTrafficClass": ieee8021BridgePEETSTrafficClass,
       "ieee8021BridgePEETSTrafficSelectionAlgorthm": ieee8021BridgePEETSTrafficSelectionAlgorthm,
       "ieee8021BridgePEETSBandwidth": ieee8021BridgePEETSBandwidth,
       "ieee8021BridgePEConformance": ieee8021BridgePEConformance,
       "ieee8021BridgePEGroups": ieee8021BridgePEGroups,
       "ieee8021BridgePEGroup": ieee8021BridgePEGroup,
       "ieee8021BridgePECompliances": ieee8021BridgePECompliances,
       "ieee8021BridgePECompliance": ieee8021BridgePECompliance}
)
