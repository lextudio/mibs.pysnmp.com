# SNMP MIB module (DECATM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/DECATM-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:23:32 2024
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
_Sysobjid_ObjectIdentity = ObjectIdentity
sysobjid = _Sysobjid_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 36, 2, 15)
)
_AtmSwitch_ObjectIdentity = ObjectIdentity
atmSwitch = _AtmSwitch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 36, 2, 15, 14)
)
_AtmSwitch1_ObjectIdentity = ObjectIdentity
atmSwitch1 = _AtmSwitch1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 36, 2, 15, 14, 1)
)
_Atmversion1_ObjectIdentity = ObjectIdentity
atmversion1 = _Atmversion1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 36, 2, 15, 14, 1, 1)
)
_AtmSwitch2_ObjectIdentity = ObjectIdentity
atmSwitch2 = _AtmSwitch2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 36, 2, 15, 14, 2)
)
_Atmversion2_ObjectIdentity = ObjectIdentity
atmversion2 = _Atmversion2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 36, 2, 15, 14, 2, 1)
)
_DecMIBextension_ObjectIdentity = ObjectIdentity
decMIBextension = _DecMIBextension_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 36, 2, 18)
)
_AtmExpand_ObjectIdentity = ObjectIdentity
atmExpand = _AtmExpand_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 17)
)
_Ad_ObjectIdentity = ObjectIdentity
ad = _Ad_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 17, 1)
)
_AdUID_Type = OctetString
_AdUID_Object = MibScalar
adUID = _AdUID_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 17, 1, 1),
    _AdUID_Type()
)
adUID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adUID.setStatus("mandatory")


class _AdEscapeSupport_Type(Integer32):
    """Custom type adEscapeSupport based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("none", 2),
          ("supported", 1))
    )


_AdEscapeSupport_Type.__name__ = "Integer32"
_AdEscapeSupport_Object = MibScalar
adEscapeSupport = _AdEscapeSupport_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 17, 1, 2),
    _AdEscapeSupport_Type()
)
adEscapeSupport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adEscapeSupport.setStatus("mandatory")


class _AdFlowMaster_Type(Integer32):
    """Custom type adFlowMaster based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("none", 2),
          ("supported", 1))
    )


_AdFlowMaster_Type.__name__ = "Integer32"
_AdFlowMaster_Object = MibScalar
adFlowMaster = _AdFlowMaster_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 17, 1, 3),
    _AdFlowMaster_Type()
)
adFlowMaster.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adFlowMaster.setStatus("mandatory")


class _AdRVC_Type(Integer32):
    """Custom type adRVC based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("none", 2),
          ("supported", 1))
    )


_AdRVC_Type.__name__ = "Integer32"
_AdRVC_Object = MibScalar
adRVC = _AdRVC_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 17, 1, 4),
    _AdRVC_Type()
)
adRVC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adRVC.setStatus("mandatory")
_AdObjectId_Type = Integer32
_AdObjectId_Object = MibScalar
adObjectId = _AdObjectId_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 17, 1, 5),
    _AdObjectId_Type()
)
adObjectId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adObjectId.setStatus("mandatory")
_AdObjectSubId_Type = Integer32
_AdObjectSubId_Object = MibScalar
adObjectSubId = _AdObjectSubId_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 17, 1, 6),
    _AdObjectSubId_Type()
)
adObjectSubId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adObjectSubId.setStatus("mandatory")
_AdNumPorts_Type = Integer32
_AdNumPorts_Object = MibScalar
adNumPorts = _AdNumPorts_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 17, 1, 7),
    _AdNumPorts_Type()
)
adNumPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adNumPorts.setStatus("mandatory")
_AdPortTable_Object = MibTable
adPortTable = _AdPortTable_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 17, 1, 8)
)
if mibBuilder.loadTexts:
    adPortTable.setStatus("mandatory")
_AdPortTableEntry_Object = MibTableRow
adPortTableEntry = _AdPortTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 17, 1, 8, 1)
)
adPortTableEntry.setIndexNames(
    (0, "DECATM-MIB", "adpPortIndex"),
)
if mibBuilder.loadTexts:
    adPortTableEntry.setStatus("mandatory")
_AdpPortIndex_Type = Integer32
_AdpPortIndex_Object = MibTableColumn
adpPortIndex = _AdpPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 17, 1, 8, 1, 1),
    _AdpPortIndex_Type()
)
adpPortIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    adpPortIndex.setStatus("mandatory")
_AdpType_Type = Integer32
_AdpType_Object = MibTableColumn
adpType = _AdpType_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 17, 1, 8, 1, 2),
    _AdpType_Type()
)
adpType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adpType.setStatus("mandatory")
_AdpSubType_Type = Integer32
_AdpSubType_Object = MibTableColumn
adpSubType = _AdpSubType_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 17, 1, 8, 1, 3),
    _AdpSubType_Type()
)
adpSubType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adpSubType.setStatus("mandatory")


class _AdpFlowMaster_Type(Integer32):
    """Custom type adpFlowMaster based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("supported", 2))
    )


_AdpFlowMaster_Type.__name__ = "Integer32"
_AdpFlowMaster_Object = MibTableColumn
adpFlowMaster = _AdpFlowMaster_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 17, 1, 8, 1, 4),
    _AdpFlowMaster_Type()
)
adpFlowMaster.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adpFlowMaster.setStatus("mandatory")


class _AdpCreditResync_Type(Integer32):
    """Custom type adpCreditResync based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("an2Style", 3),
          ("none", 2),
          ("unknown", 1))
    )


_AdpCreditResync_Type.__name__ = "Integer32"
_AdpCreditResync_Object = MibTableColumn
adpCreditResync = _AdpCreditResync_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 17, 1, 8, 1, 5),
    _AdpCreditResync_Type()
)
adpCreditResync.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adpCreditResync.setStatus("mandatory")
_AdpResyncVCI_Type = Integer32
_AdpResyncVCI_Object = MibTableColumn
adpResyncVCI = _AdpResyncVCI_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 17, 1, 8, 1, 6),
    _AdpResyncVCI_Type()
)
adpResyncVCI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adpResyncVCI.setStatus("mandatory")
_AdpReceiveBuffers_Type = Integer32
_AdpReceiveBuffers_Object = MibTableColumn
adpReceiveBuffers = _AdpReceiveBuffers_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 17, 1, 8, 1, 7),
    _AdpReceiveBuffers_Type()
)
adpReceiveBuffers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adpReceiveBuffers.setStatus("mandatory")
_AdpPVCMin_Type = Integer32
_AdpPVCMin_Object = MibTableColumn
adpPVCMin = _AdpPVCMin_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 17, 1, 8, 1, 8),
    _AdpPVCMin_Type()
)
adpPVCMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adpPVCMin.setStatus("mandatory")
_AdpPVCMax_Type = Integer32
_AdpPVCMax_Object = MibTableColumn
adpPVCMax = _AdpPVCMax_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 17, 1, 8, 1, 9),
    _AdpPVCMax_Type()
)
adpPVCMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adpPVCMax.setStatus("mandatory")
_AdpSVCMin_Type = Integer32
_AdpSVCMin_Object = MibTableColumn
adpSVCMin = _AdpSVCMin_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 17, 1, 8, 1, 10),
    _AdpSVCMin_Type()
)
adpSVCMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adpSVCMin.setStatus("mandatory")
_AdpSVCMax_Type = Integer32
_AdpSVCMax_Object = MibTableColumn
adpSVCMax = _AdpSVCMax_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 17, 1, 8, 1, 11),
    _AdpSVCMax_Type()
)
adpSVCMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adpSVCMax.setStatus("mandatory")
_AdpRVCMin_Type = Integer32
_AdpRVCMin_Object = MibTableColumn
adpRVCMin = _AdpRVCMin_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 17, 1, 8, 1, 12),
    _AdpRVCMin_Type()
)
adpRVCMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adpRVCMin.setStatus("mandatory")
_AdpRVCMax_Type = Integer32
_AdpRVCMax_Object = MibTableColumn
adpRVCMax = _AdpRVCMax_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 17, 1, 8, 1, 13),
    _AdpRVCMax_Type()
)
adpRVCMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adpRVCMax.setStatus("mandatory")
_AdpBroadcastVCI_Type = Integer32
_AdpBroadcastVCI_Object = MibTableColumn
adpBroadcastVCI = _AdpBroadcastVCI_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 17, 1, 8, 1, 14),
    _AdpBroadcastVCI_Type()
)
adpBroadcastVCI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adpBroadcastVCI.setStatus("mandatory")
_AdpArpVCI_Type = Integer32
_AdpArpVCI_Object = MibTableColumn
adpArpVCI = _AdpArpVCI_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 17, 1, 8, 1, 15),
    _AdpArpVCI_Type()
)
adpArpVCI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adpArpVCI.setStatus("mandatory")
_AdpHomeVCI_Type = Integer32
_AdpHomeVCI_Object = MibTableColumn
adpHomeVCI = _AdpHomeVCI_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 17, 1, 8, 1, 16),
    _AdpHomeVCI_Type()
)
adpHomeVCI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adpHomeVCI.setStatus("mandatory")
_AdpMaxReceiveBufferCounter_Type = Integer32
_AdpMaxReceiveBufferCounter_Object = MibTableColumn
adpMaxReceiveBufferCounter = _AdpMaxReceiveBufferCounter_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 17, 1, 8, 1, 17),
    _AdpMaxReceiveBufferCounter_Type()
)
adpMaxReceiveBufferCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adpMaxReceiveBufferCounter.setStatus("mandatory")
_AdpUsedReceiveBuffers_Type = Integer32
_AdpUsedReceiveBuffers_Object = MibTableColumn
adpUsedReceiveBuffers = _AdpUsedReceiveBuffers_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 17, 1, 8, 1, 18),
    _AdpUsedReceiveBuffers_Type()
)
adpUsedReceiveBuffers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adpUsedReceiveBuffers.setStatus("mandatory")


class _AdpRemoteFlowMaster_Type(Integer32):
    """Custom type adpRemoteFlowMaster based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("none", 2),
          ("supported", 1))
    )


_AdpRemoteFlowMaster_Type.__name__ = "Integer32"
_AdpRemoteFlowMaster_Object = MibTableColumn
adpRemoteFlowMaster = _AdpRemoteFlowMaster_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 17, 1, 8, 1, 19),
    _AdpRemoteFlowMaster_Type()
)
adpRemoteFlowMaster.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adpRemoteFlowMaster.setStatus("mandatory")
_AdpOutputBandwidth_Type = Integer32
_AdpOutputBandwidth_Object = MibTableColumn
adpOutputBandwidth = _AdpOutputBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 17, 1, 8, 1, 20),
    _AdpOutputBandwidth_Type()
)
adpOutputBandwidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adpOutputBandwidth.setStatus("mandatory")
_AdpAvailableOutputBandwidth_Type = Integer32
_AdpAvailableOutputBandwidth_Object = MibTableColumn
adpAvailableOutputBandwidth = _AdpAvailableOutputBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 17, 1, 8, 1, 21),
    _AdpAvailableOutputBandwidth_Type()
)
adpAvailableOutputBandwidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adpAvailableOutputBandwidth.setStatus("mandatory")
_Dxatm_ObjectIdentity = ObjectIdentity
dxatm = _Dxatm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 17, 2)
)
_DxatmPvcTable_Object = MibTable
dxatmPvcTable = _DxatmPvcTable_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 17, 2, 1)
)
if mibBuilder.loadTexts:
    dxatmPvcTable.setStatus("mandatory")
_DxatmPvcEntry_Object = MibTableRow
dxatmPvcEntry = _DxatmPvcEntry_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 17, 2, 1, 1)
)
dxatmPvcEntry.setIndexNames(
    (0, "DECATM-MIB", "dxatmPvcLowIfIndex"),
    (0, "DECATM-MIB", "dxatmPvcLowVpi"),
    (0, "DECATM-MIB", "dxatmPvcLowVci"),
    (0, "DECATM-MIB", "dxatmPvcHighIfIndex"),
    (0, "DECATM-MIB", "dxatmPvcHighVpi"),
    (0, "DECATM-MIB", "dxatmPvcHighVci"),
)
if mibBuilder.loadTexts:
    dxatmPvcEntry.setStatus("mandatory")
_DxatmPvcLowIfIndex_Type = Integer32
_DxatmPvcLowIfIndex_Object = MibTableColumn
dxatmPvcLowIfIndex = _DxatmPvcLowIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 17, 2, 1, 1, 1),
    _DxatmPvcLowIfIndex_Type()
)
dxatmPvcLowIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dxatmPvcLowIfIndex.setStatus("mandatory")


class _DxatmPvcLowVpi_Type(Integer32):
    """Custom type dxatmPvcLowVpi based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_DxatmPvcLowVpi_Type.__name__ = "Integer32"
_DxatmPvcLowVpi_Object = MibTableColumn
dxatmPvcLowVpi = _DxatmPvcLowVpi_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 17, 2, 1, 1, 2),
    _DxatmPvcLowVpi_Type()
)
dxatmPvcLowVpi.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dxatmPvcLowVpi.setStatus("mandatory")


class _DxatmPvcLowVci_Type(Integer32):
    """Custom type dxatmPvcLowVci based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_DxatmPvcLowVci_Type.__name__ = "Integer32"
_DxatmPvcLowVci_Object = MibTableColumn
dxatmPvcLowVci = _DxatmPvcLowVci_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 17, 2, 1, 1, 3),
    _DxatmPvcLowVci_Type()
)
dxatmPvcLowVci.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dxatmPvcLowVci.setStatus("mandatory")
_DxatmPvcHighIfIndex_Type = Integer32
_DxatmPvcHighIfIndex_Object = MibTableColumn
dxatmPvcHighIfIndex = _DxatmPvcHighIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 17, 2, 1, 1, 4),
    _DxatmPvcHighIfIndex_Type()
)
dxatmPvcHighIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dxatmPvcHighIfIndex.setStatus("mandatory")


class _DxatmPvcHighVpi_Type(Integer32):
    """Custom type dxatmPvcHighVpi based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_DxatmPvcHighVpi_Type.__name__ = "Integer32"
_DxatmPvcHighVpi_Object = MibTableColumn
dxatmPvcHighVpi = _DxatmPvcHighVpi_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 17, 2, 1, 1, 5),
    _DxatmPvcHighVpi_Type()
)
dxatmPvcHighVpi.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dxatmPvcHighVpi.setStatus("mandatory")


class _DxatmPvcHighVci_Type(Integer32):
    """Custom type dxatmPvcHighVci based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_DxatmPvcHighVci_Type.__name__ = "Integer32"
_DxatmPvcHighVci_Object = MibTableColumn
dxatmPvcHighVci = _DxatmPvcHighVci_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 17, 2, 1, 1, 6),
    _DxatmPvcHighVci_Type()
)
dxatmPvcHighVci.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dxatmPvcHighVci.setStatus("mandatory")


class _DxatmPvcAdminStatus_Type(Integer32):
    """Custom type dxatmPvcAdminStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("down", 2),
          ("up", 1))
    )


_DxatmPvcAdminStatus_Type.__name__ = "Integer32"
_DxatmPvcAdminStatus_Object = MibTableColumn
dxatmPvcAdminStatus = _DxatmPvcAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 17, 2, 1, 1, 7),
    _DxatmPvcAdminStatus_Type()
)
dxatmPvcAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dxatmPvcAdminStatus.setStatus("mandatory")


class _DxatmPvcL2HOperStatus_Type(Integer32):
    """Custom type dxatmPvcL2HOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("down", 2),
          ("unknown", 3),
          ("up", 1))
    )


_DxatmPvcL2HOperStatus_Type.__name__ = "Integer32"
_DxatmPvcL2HOperStatus_Object = MibTableColumn
dxatmPvcL2HOperStatus = _DxatmPvcL2HOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 17, 2, 1, 1, 8),
    _DxatmPvcL2HOperStatus_Type()
)
dxatmPvcL2HOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dxatmPvcL2HOperStatus.setStatus("mandatory")


class _DxatmPvcH2LOperStatus_Type(Integer32):
    """Custom type dxatmPvcH2LOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("down", 2),
          ("unknown", 3),
          ("up", 1))
    )


_DxatmPvcH2LOperStatus_Type.__name__ = "Integer32"
_DxatmPvcH2LOperStatus_Object = MibTableColumn
dxatmPvcH2LOperStatus = _DxatmPvcH2LOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 17, 2, 1, 1, 9),
    _DxatmPvcH2LOperStatus_Type()
)
dxatmPvcH2LOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dxatmPvcH2LOperStatus.setStatus("mandatory")


class _DxatmPvcL2HFCStatus_Type(Integer32):
    """Custom type dxatmPvcL2HFCStatus based on Integer32"""
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
          ("enabled", 1),
          ("notApplicable", 3))
    )


_DxatmPvcL2HFCStatus_Type.__name__ = "Integer32"
_DxatmPvcL2HFCStatus_Object = MibTableColumn
dxatmPvcL2HFCStatus = _DxatmPvcL2HFCStatus_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 17, 2, 1, 1, 10),
    _DxatmPvcL2HFCStatus_Type()
)
dxatmPvcL2HFCStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dxatmPvcL2HFCStatus.setStatus("mandatory")


class _DxatmPvcH2LFCStatus_Type(Integer32):
    """Custom type dxatmPvcH2LFCStatus based on Integer32"""
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
          ("enabled", 1),
          ("notApplicable", 3))
    )


_DxatmPvcH2LFCStatus_Type.__name__ = "Integer32"
_DxatmPvcH2LFCStatus_Object = MibTableColumn
dxatmPvcH2LFCStatus = _DxatmPvcH2LFCStatus_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 17, 2, 1, 1, 11),
    _DxatmPvcH2LFCStatus_Type()
)
dxatmPvcH2LFCStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dxatmPvcH2LFCStatus.setStatus("mandatory")
_DxatmPvcL2HTrafficDescriptorType_Type = ObjectIdentifier
_DxatmPvcL2HTrafficDescriptorType_Object = MibTableColumn
dxatmPvcL2HTrafficDescriptorType = _DxatmPvcL2HTrafficDescriptorType_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 17, 2, 1, 1, 12),
    _DxatmPvcL2HTrafficDescriptorType_Type()
)
dxatmPvcL2HTrafficDescriptorType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dxatmPvcL2HTrafficDescriptorType.setStatus("mandatory")


class _DxatmPvcL2HTrafficDescriptorParam1_Type(Integer32):
    """Custom type dxatmPvcL2HTrafficDescriptorParam1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_DxatmPvcL2HTrafficDescriptorParam1_Type.__name__ = "Integer32"
_DxatmPvcL2HTrafficDescriptorParam1_Object = MibTableColumn
dxatmPvcL2HTrafficDescriptorParam1 = _DxatmPvcL2HTrafficDescriptorParam1_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 17, 2, 1, 1, 13),
    _DxatmPvcL2HTrafficDescriptorParam1_Type()
)
dxatmPvcL2HTrafficDescriptorParam1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dxatmPvcL2HTrafficDescriptorParam1.setStatus("mandatory")


class _DxatmPvcL2HTrafficDescriptorParam2_Type(Integer32):
    """Custom type dxatmPvcL2HTrafficDescriptorParam2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_DxatmPvcL2HTrafficDescriptorParam2_Type.__name__ = "Integer32"
_DxatmPvcL2HTrafficDescriptorParam2_Object = MibTableColumn
dxatmPvcL2HTrafficDescriptorParam2 = _DxatmPvcL2HTrafficDescriptorParam2_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 17, 2, 1, 1, 14),
    _DxatmPvcL2HTrafficDescriptorParam2_Type()
)
dxatmPvcL2HTrafficDescriptorParam2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dxatmPvcL2HTrafficDescriptorParam2.setStatus("mandatory")


class _DxatmPvcL2HTrafficDescriptorParam3_Type(Integer32):
    """Custom type dxatmPvcL2HTrafficDescriptorParam3 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_DxatmPvcL2HTrafficDescriptorParam3_Type.__name__ = "Integer32"
_DxatmPvcL2HTrafficDescriptorParam3_Object = MibTableColumn
dxatmPvcL2HTrafficDescriptorParam3 = _DxatmPvcL2HTrafficDescriptorParam3_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 17, 2, 1, 1, 15),
    _DxatmPvcL2HTrafficDescriptorParam3_Type()
)
dxatmPvcL2HTrafficDescriptorParam3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dxatmPvcL2HTrafficDescriptorParam3.setStatus("mandatory")


class _DxatmPvcL2HTrafficDescriptorParam4_Type(Integer32):
    """Custom type dxatmPvcL2HTrafficDescriptorParam4 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_DxatmPvcL2HTrafficDescriptorParam4_Type.__name__ = "Integer32"
_DxatmPvcL2HTrafficDescriptorParam4_Object = MibTableColumn
dxatmPvcL2HTrafficDescriptorParam4 = _DxatmPvcL2HTrafficDescriptorParam4_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 17, 2, 1, 1, 16),
    _DxatmPvcL2HTrafficDescriptorParam4_Type()
)
dxatmPvcL2HTrafficDescriptorParam4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dxatmPvcL2HTrafficDescriptorParam4.setStatus("mandatory")


class _DxatmPvcL2HTrafficDescriptorParam5_Type(Integer32):
    """Custom type dxatmPvcL2HTrafficDescriptorParam5 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_DxatmPvcL2HTrafficDescriptorParam5_Type.__name__ = "Integer32"
_DxatmPvcL2HTrafficDescriptorParam5_Object = MibTableColumn
dxatmPvcL2HTrafficDescriptorParam5 = _DxatmPvcL2HTrafficDescriptorParam5_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 17, 2, 1, 1, 17),
    _DxatmPvcL2HTrafficDescriptorParam5_Type()
)
dxatmPvcL2HTrafficDescriptorParam5.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dxatmPvcL2HTrafficDescriptorParam5.setStatus("mandatory")
_DxatmPvcH2LTrafficDescriptorType_Type = ObjectIdentifier
_DxatmPvcH2LTrafficDescriptorType_Object = MibTableColumn
dxatmPvcH2LTrafficDescriptorType = _DxatmPvcH2LTrafficDescriptorType_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 17, 2, 1, 1, 18),
    _DxatmPvcH2LTrafficDescriptorType_Type()
)
dxatmPvcH2LTrafficDescriptorType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dxatmPvcH2LTrafficDescriptorType.setStatus("mandatory")


class _DxatmPvcH2LTrafficDescriptorParam1_Type(Integer32):
    """Custom type dxatmPvcH2LTrafficDescriptorParam1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_DxatmPvcH2LTrafficDescriptorParam1_Type.__name__ = "Integer32"
_DxatmPvcH2LTrafficDescriptorParam1_Object = MibTableColumn
dxatmPvcH2LTrafficDescriptorParam1 = _DxatmPvcH2LTrafficDescriptorParam1_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 17, 2, 1, 1, 19),
    _DxatmPvcH2LTrafficDescriptorParam1_Type()
)
dxatmPvcH2LTrafficDescriptorParam1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dxatmPvcH2LTrafficDescriptorParam1.setStatus("mandatory")


class _DxatmPvcH2LTrafficDescriptorParam2_Type(Integer32):
    """Custom type dxatmPvcH2LTrafficDescriptorParam2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_DxatmPvcH2LTrafficDescriptorParam2_Type.__name__ = "Integer32"
_DxatmPvcH2LTrafficDescriptorParam2_Object = MibTableColumn
dxatmPvcH2LTrafficDescriptorParam2 = _DxatmPvcH2LTrafficDescriptorParam2_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 17, 2, 1, 1, 20),
    _DxatmPvcH2LTrafficDescriptorParam2_Type()
)
dxatmPvcH2LTrafficDescriptorParam2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dxatmPvcH2LTrafficDescriptorParam2.setStatus("mandatory")


class _DxatmPvcH2LTrafficDescriptorParam3_Type(Integer32):
    """Custom type dxatmPvcH2LTrafficDescriptorParam3 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_DxatmPvcH2LTrafficDescriptorParam3_Type.__name__ = "Integer32"
_DxatmPvcH2LTrafficDescriptorParam3_Object = MibTableColumn
dxatmPvcH2LTrafficDescriptorParam3 = _DxatmPvcH2LTrafficDescriptorParam3_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 17, 2, 1, 1, 21),
    _DxatmPvcH2LTrafficDescriptorParam3_Type()
)
dxatmPvcH2LTrafficDescriptorParam3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dxatmPvcH2LTrafficDescriptorParam3.setStatus("mandatory")


class _DxatmPvcH2LTrafficDescriptorParam4_Type(Integer32):
    """Custom type dxatmPvcH2LTrafficDescriptorParam4 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_DxatmPvcH2LTrafficDescriptorParam4_Type.__name__ = "Integer32"
_DxatmPvcH2LTrafficDescriptorParam4_Object = MibTableColumn
dxatmPvcH2LTrafficDescriptorParam4 = _DxatmPvcH2LTrafficDescriptorParam4_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 17, 2, 1, 1, 22),
    _DxatmPvcH2LTrafficDescriptorParam4_Type()
)
dxatmPvcH2LTrafficDescriptorParam4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dxatmPvcH2LTrafficDescriptorParam4.setStatus("mandatory")


class _DxatmPvcH2LTrafficDescriptorParam5_Type(Integer32):
    """Custom type dxatmPvcH2LTrafficDescriptorParam5 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_DxatmPvcH2LTrafficDescriptorParam5_Type.__name__ = "Integer32"
_DxatmPvcH2LTrafficDescriptorParam5_Object = MibTableColumn
dxatmPvcH2LTrafficDescriptorParam5 = _DxatmPvcH2LTrafficDescriptorParam5_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 17, 2, 1, 1, 23),
    _DxatmPvcH2LTrafficDescriptorParam5_Type()
)
dxatmPvcH2LTrafficDescriptorParam5.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dxatmPvcH2LTrafficDescriptorParam5.setStatus("mandatory")
_DxatmPvcL2HQoSClass_Type = Integer32
_DxatmPvcL2HQoSClass_Object = MibTableColumn
dxatmPvcL2HQoSClass = _DxatmPvcL2HQoSClass_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 17, 2, 1, 1, 24),
    _DxatmPvcL2HQoSClass_Type()
)
dxatmPvcL2HQoSClass.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dxatmPvcL2HQoSClass.setStatus("mandatory")
_DxatmPvcH2LQoSClass_Type = Integer32
_DxatmPvcH2LQoSClass_Object = MibTableColumn
dxatmPvcH2LQoSClass = _DxatmPvcH2LQoSClass_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 17, 2, 1, 1, 25),
    _DxatmPvcH2LQoSClass_Type()
)
dxatmPvcH2LQoSClass.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dxatmPvcH2LQoSClass.setStatus("mandatory")
_DxatmPvcRowStatus_Type = Integer32
_DxatmPvcRowStatus_Object = MibTableColumn
dxatmPvcRowStatus = _DxatmPvcRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 17, 2, 1, 1, 26),
    _DxatmPvcRowStatus_Type()
)
dxatmPvcRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dxatmPvcRowStatus.setStatus("mandatory")
_DxatmPvcMpTable_Object = MibTable
dxatmPvcMpTable = _DxatmPvcMpTable_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 17, 2, 2)
)
if mibBuilder.loadTexts:
    dxatmPvcMpTable.setStatus("mandatory")
_DxatmPvcMpEntry_Object = MibTableRow
dxatmPvcMpEntry = _DxatmPvcMpEntry_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 17, 2, 2, 1)
)
dxatmPvcMpEntry.setIndexNames(
    (0, "DECATM-MIB", "dxatmPvcMpRootIfIndex"),
    (0, "DECATM-MIB", "dxatmPvcMpRootVpi"),
    (0, "DECATM-MIB", "dxatmPvcMpRootVci"),
    (0, "DECATM-MIB", "dxatmPvcMpLeafIfIndex"),
    (0, "DECATM-MIB", "dxatmPvcMpLeafVpi"),
    (0, "DECATM-MIB", "dxatmPvcMpLeafVci"),
)
if mibBuilder.loadTexts:
    dxatmPvcMpEntry.setStatus("mandatory")
_DxatmPvcMpRootIfIndex_Type = Integer32
_DxatmPvcMpRootIfIndex_Object = MibTableColumn
dxatmPvcMpRootIfIndex = _DxatmPvcMpRootIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 17, 2, 2, 1, 1),
    _DxatmPvcMpRootIfIndex_Type()
)
dxatmPvcMpRootIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dxatmPvcMpRootIfIndex.setStatus("mandatory")


class _DxatmPvcMpRootVpi_Type(Integer32):
    """Custom type dxatmPvcMpRootVpi based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_DxatmPvcMpRootVpi_Type.__name__ = "Integer32"
_DxatmPvcMpRootVpi_Object = MibTableColumn
dxatmPvcMpRootVpi = _DxatmPvcMpRootVpi_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 17, 2, 2, 1, 2),
    _DxatmPvcMpRootVpi_Type()
)
dxatmPvcMpRootVpi.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dxatmPvcMpRootVpi.setStatus("mandatory")


class _DxatmPvcMpRootVci_Type(Integer32):
    """Custom type dxatmPvcMpRootVci based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_DxatmPvcMpRootVci_Type.__name__ = "Integer32"
_DxatmPvcMpRootVci_Object = MibTableColumn
dxatmPvcMpRootVci = _DxatmPvcMpRootVci_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 17, 2, 2, 1, 3),
    _DxatmPvcMpRootVci_Type()
)
dxatmPvcMpRootVci.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dxatmPvcMpRootVci.setStatus("mandatory")
_DxatmPvcMpLeafIfIndex_Type = Integer32
_DxatmPvcMpLeafIfIndex_Object = MibTableColumn
dxatmPvcMpLeafIfIndex = _DxatmPvcMpLeafIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 17, 2, 2, 1, 4),
    _DxatmPvcMpLeafIfIndex_Type()
)
dxatmPvcMpLeafIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dxatmPvcMpLeafIfIndex.setStatus("mandatory")


class _DxatmPvcMpLeafVpi_Type(Integer32):
    """Custom type dxatmPvcMpLeafVpi based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_DxatmPvcMpLeafVpi_Type.__name__ = "Integer32"
_DxatmPvcMpLeafVpi_Object = MibTableColumn
dxatmPvcMpLeafVpi = _DxatmPvcMpLeafVpi_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 17, 2, 2, 1, 5),
    _DxatmPvcMpLeafVpi_Type()
)
dxatmPvcMpLeafVpi.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dxatmPvcMpLeafVpi.setStatus("mandatory")


class _DxatmPvcMpLeafVci_Type(Integer32):
    """Custom type dxatmPvcMpLeafVci based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_DxatmPvcMpLeafVci_Type.__name__ = "Integer32"
_DxatmPvcMpLeafVci_Object = MibTableColumn
dxatmPvcMpLeafVci = _DxatmPvcMpLeafVci_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 17, 2, 2, 1, 6),
    _DxatmPvcMpLeafVci_Type()
)
dxatmPvcMpLeafVci.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dxatmPvcMpLeafVci.setStatus("mandatory")


class _DxatmPvcMpAdminStatus_Type(Integer32):
    """Custom type dxatmPvcMpAdminStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("down", 2),
          ("up", 1))
    )


_DxatmPvcMpAdminStatus_Type.__name__ = "Integer32"
_DxatmPvcMpAdminStatus_Object = MibTableColumn
dxatmPvcMpAdminStatus = _DxatmPvcMpAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 17, 2, 2, 1, 7),
    _DxatmPvcMpAdminStatus_Type()
)
dxatmPvcMpAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dxatmPvcMpAdminStatus.setStatus("mandatory")


class _DxatmPvcMpOperStatus_Type(Integer32):
    """Custom type dxatmPvcMpOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("down", 2),
          ("unknown", 3),
          ("up", 1))
    )


_DxatmPvcMpOperStatus_Type.__name__ = "Integer32"
_DxatmPvcMpOperStatus_Object = MibTableColumn
dxatmPvcMpOperStatus = _DxatmPvcMpOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 17, 2, 2, 1, 8),
    _DxatmPvcMpOperStatus_Type()
)
dxatmPvcMpOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dxatmPvcMpOperStatus.setStatus("mandatory")


class _DxatmPvcMpFCStatus_Type(Integer32):
    """Custom type dxatmPvcMpFCStatus based on Integer32"""
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
          ("enabled", 1),
          ("notApplicable", 3))
    )


_DxatmPvcMpFCStatus_Type.__name__ = "Integer32"
_DxatmPvcMpFCStatus_Object = MibTableColumn
dxatmPvcMpFCStatus = _DxatmPvcMpFCStatus_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 17, 2, 2, 1, 9),
    _DxatmPvcMpFCStatus_Type()
)
dxatmPvcMpFCStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dxatmPvcMpFCStatus.setStatus("mandatory")
_DxatmPvcMpTrafficDescriptorType_Type = ObjectIdentifier
_DxatmPvcMpTrafficDescriptorType_Object = MibTableColumn
dxatmPvcMpTrafficDescriptorType = _DxatmPvcMpTrafficDescriptorType_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 17, 2, 2, 1, 10),
    _DxatmPvcMpTrafficDescriptorType_Type()
)
dxatmPvcMpTrafficDescriptorType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dxatmPvcMpTrafficDescriptorType.setStatus("mandatory")


class _DxatmPvcMpTrafficDescriptorParam1_Type(Integer32):
    """Custom type dxatmPvcMpTrafficDescriptorParam1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_DxatmPvcMpTrafficDescriptorParam1_Type.__name__ = "Integer32"
_DxatmPvcMpTrafficDescriptorParam1_Object = MibTableColumn
dxatmPvcMpTrafficDescriptorParam1 = _DxatmPvcMpTrafficDescriptorParam1_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 17, 2, 2, 1, 11),
    _DxatmPvcMpTrafficDescriptorParam1_Type()
)
dxatmPvcMpTrafficDescriptorParam1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dxatmPvcMpTrafficDescriptorParam1.setStatus("mandatory")


class _DxatmPvcMpTrafficDescriptorParam2_Type(Integer32):
    """Custom type dxatmPvcMpTrafficDescriptorParam2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_DxatmPvcMpTrafficDescriptorParam2_Type.__name__ = "Integer32"
_DxatmPvcMpTrafficDescriptorParam2_Object = MibTableColumn
dxatmPvcMpTrafficDescriptorParam2 = _DxatmPvcMpTrafficDescriptorParam2_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 17, 2, 2, 1, 12),
    _DxatmPvcMpTrafficDescriptorParam2_Type()
)
dxatmPvcMpTrafficDescriptorParam2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dxatmPvcMpTrafficDescriptorParam2.setStatus("mandatory")


class _DxatmPvcMpTrafficDescriptorParam3_Type(Integer32):
    """Custom type dxatmPvcMpTrafficDescriptorParam3 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_DxatmPvcMpTrafficDescriptorParam3_Type.__name__ = "Integer32"
_DxatmPvcMpTrafficDescriptorParam3_Object = MibTableColumn
dxatmPvcMpTrafficDescriptorParam3 = _DxatmPvcMpTrafficDescriptorParam3_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 17, 2, 2, 1, 13),
    _DxatmPvcMpTrafficDescriptorParam3_Type()
)
dxatmPvcMpTrafficDescriptorParam3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dxatmPvcMpTrafficDescriptorParam3.setStatus("mandatory")


class _DxatmPvcMpTrafficDescriptorParam4_Type(Integer32):
    """Custom type dxatmPvcMpTrafficDescriptorParam4 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_DxatmPvcMpTrafficDescriptorParam4_Type.__name__ = "Integer32"
_DxatmPvcMpTrafficDescriptorParam4_Object = MibTableColumn
dxatmPvcMpTrafficDescriptorParam4 = _DxatmPvcMpTrafficDescriptorParam4_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 17, 2, 2, 1, 14),
    _DxatmPvcMpTrafficDescriptorParam4_Type()
)
dxatmPvcMpTrafficDescriptorParam4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dxatmPvcMpTrafficDescriptorParam4.setStatus("mandatory")


class _DxatmPvcMpTrafficDescriptorParam5_Type(Integer32):
    """Custom type dxatmPvcMpTrafficDescriptorParam5 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_DxatmPvcMpTrafficDescriptorParam5_Type.__name__ = "Integer32"
_DxatmPvcMpTrafficDescriptorParam5_Object = MibTableColumn
dxatmPvcMpTrafficDescriptorParam5 = _DxatmPvcMpTrafficDescriptorParam5_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 17, 2, 2, 1, 15),
    _DxatmPvcMpTrafficDescriptorParam5_Type()
)
dxatmPvcMpTrafficDescriptorParam5.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dxatmPvcMpTrafficDescriptorParam5.setStatus("mandatory")


class _DxatmPvcMpQoSClass_Type(Integer32):
    """Custom type dxatmPvcMpQoSClass based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_DxatmPvcMpQoSClass_Type.__name__ = "Integer32"
_DxatmPvcMpQoSClass_Object = MibTableColumn
dxatmPvcMpQoSClass = _DxatmPvcMpQoSClass_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 17, 2, 2, 1, 16),
    _DxatmPvcMpQoSClass_Type()
)
dxatmPvcMpQoSClass.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dxatmPvcMpQoSClass.setStatus("mandatory")
_DxatmPvcMpRowStatus_Type = Integer32
_DxatmPvcMpRowStatus_Object = MibTableColumn
dxatmPvcMpRowStatus = _DxatmPvcMpRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 17, 2, 2, 1, 17),
    _DxatmPvcMpRowStatus_Type()
)
dxatmPvcMpRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dxatmPvcMpRowStatus.setStatus("mandatory")
_DxatmVirtualPathObjects_ObjectIdentity = ObjectIdentity
dxatmVirtualPathObjects = _DxatmVirtualPathObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 17, 2, 3)
)
_DxatmVpModeTable_Object = MibTable
dxatmVpModeTable = _DxatmVpModeTable_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 17, 2, 3, 1)
)
if mibBuilder.loadTexts:
    dxatmVpModeTable.setStatus("mandatory")
_DxatmVpModeEntry_Object = MibTableRow
dxatmVpModeEntry = _DxatmVpModeEntry_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 17, 2, 3, 1, 1)
)
dxatmVpModeEntry.setIndexNames(
    (0, "DECATM-MIB", "dxatmVpModeSlot"),
)
if mibBuilder.loadTexts:
    dxatmVpModeEntry.setStatus("mandatory")
_DxatmVpModeSlot_Type = Integer32
_DxatmVpModeSlot_Object = MibTableColumn
dxatmVpModeSlot = _DxatmVpModeSlot_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 17, 2, 3, 1, 1, 1),
    _DxatmVpModeSlot_Type()
)
dxatmVpModeSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dxatmVpModeSlot.setStatus("mandatory")


class _DxatmVpModeDesired_Type(Integer32):
    """Custom type dxatmVpModeDesired based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 1))
    )


_DxatmVpModeDesired_Type.__name__ = "Integer32"
_DxatmVpModeDesired_Object = MibTableColumn
dxatmVpModeDesired = _DxatmVpModeDesired_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 17, 2, 3, 1, 1, 2),
    _DxatmVpModeDesired_Type()
)
dxatmVpModeDesired.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dxatmVpModeDesired.setStatus("mandatory")


class _DxatmVpModeActual_Type(Integer32):
    """Custom type dxatmVpModeActual based on Integer32"""
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
        *(("emptySlot", 2),
          ("noVpSupport", 3),
          ("unknown", 1),
          ("vpModeOff", 5),
          ("vpModeOn", 4))
    )


_DxatmVpModeActual_Type.__name__ = "Integer32"
_DxatmVpModeActual_Object = MibTableColumn
dxatmVpModeActual = _DxatmVpModeActual_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 17, 2, 3, 1, 1, 3),
    _DxatmVpModeActual_Type()
)
dxatmVpModeActual.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dxatmVpModeActual.setStatus("mandatory")
_DxatmVpTermTable_Object = MibTable
dxatmVpTermTable = _DxatmVpTermTable_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 17, 2, 3, 2)
)
if mibBuilder.loadTexts:
    dxatmVpTermTable.setStatus("mandatory")
_DxatmVpTermEntry_Object = MibTableRow
dxatmVpTermEntry = _DxatmVpTermEntry_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 17, 2, 3, 2, 1)
)
dxatmVpTermEntry.setIndexNames(
    (0, "DECATM-MIB", "dxatmVpTermIfIndex"),
    (0, "DECATM-MIB", "dxatmVpTermVpi"),
)
if mibBuilder.loadTexts:
    dxatmVpTermEntry.setStatus("mandatory")
_DxatmVpTermIfIndex_Type = Integer32
_DxatmVpTermIfIndex_Object = MibTableColumn
dxatmVpTermIfIndex = _DxatmVpTermIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 17, 2, 3, 2, 1, 1),
    _DxatmVpTermIfIndex_Type()
)
dxatmVpTermIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dxatmVpTermIfIndex.setStatus("mandatory")


class _DxatmVpTermVpi_Type(Integer32):
    """Custom type dxatmVpTermVpi based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_DxatmVpTermVpi_Type.__name__ = "Integer32"
_DxatmVpTermVpi_Object = MibTableColumn
dxatmVpTermVpi = _DxatmVpTermVpi_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 17, 2, 3, 2, 1, 2),
    _DxatmVpTermVpi_Type()
)
dxatmVpTermVpi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dxatmVpTermVpi.setStatus("mandatory")


class _DxatmVpTermAdminStatus_Type(Integer32):
    """Custom type dxatmVpTermAdminStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("down", 2),
          ("up", 1))
    )


_DxatmVpTermAdminStatus_Type.__name__ = "Integer32"
_DxatmVpTermAdminStatus_Object = MibTableColumn
dxatmVpTermAdminStatus = _DxatmVpTermAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 17, 2, 3, 2, 1, 3),
    _DxatmVpTermAdminStatus_Type()
)
dxatmVpTermAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dxatmVpTermAdminStatus.setStatus("mandatory")


class _DxatmVpTermOperStatus_Type(Integer32):
    """Custom type dxatmVpTermOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("down", 2),
          ("unknown", 3),
          ("up", 1))
    )


_DxatmVpTermOperStatus_Type.__name__ = "Integer32"
_DxatmVpTermOperStatus_Object = MibTableColumn
dxatmVpTermOperStatus = _DxatmVpTermOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 17, 2, 3, 2, 1, 4),
    _DxatmVpTermOperStatus_Type()
)
dxatmVpTermOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dxatmVpTermOperStatus.setStatus("mandatory")
_DxatmVpTermPcr_Type = Integer32
_DxatmVpTermPcr_Object = MibTableColumn
dxatmVpTermPcr = _DxatmVpTermPcr_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 17, 2, 3, 2, 1, 5),
    _DxatmVpTermPcr_Type()
)
dxatmVpTermPcr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dxatmVpTermPcr.setStatus("mandatory")
_DxatmVpTermScr_Type = Integer32
_DxatmVpTermScr_Object = MibTableColumn
dxatmVpTermScr = _DxatmVpTermScr_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 17, 2, 3, 2, 1, 6),
    _DxatmVpTermScr_Type()
)
dxatmVpTermScr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dxatmVpTermScr.setStatus("mandatory")
_DxatmVpTermMbs_Type = Integer32
_DxatmVpTermMbs_Object = MibTableColumn
dxatmVpTermMbs = _DxatmVpTermMbs_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 17, 2, 3, 2, 1, 7),
    _DxatmVpTermMbs_Type()
)
dxatmVpTermMbs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dxatmVpTermMbs.setStatus("mandatory")
_DxatmVpTermRowStatus_Type = Integer32
_DxatmVpTermRowStatus_Object = MibTableColumn
dxatmVpTermRowStatus = _DxatmVpTermRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 17, 2, 3, 2, 1, 8),
    _DxatmVpTermRowStatus_Type()
)
dxatmVpTermRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dxatmVpTermRowStatus.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "DECATM-MIB",
    **{"dec": dec,
       "ema": ema,
       "sysobjid": sysobjid,
       "atmSwitch": atmSwitch,
       "atmSwitch1": atmSwitch1,
       "atmversion1": atmversion1,
       "atmSwitch2": atmSwitch2,
       "atmversion2": atmversion2,
       "decMIBextension": decMIBextension,
       "atmExpand": atmExpand,
       "ad": ad,
       "adUID": adUID,
       "adEscapeSupport": adEscapeSupport,
       "adFlowMaster": adFlowMaster,
       "adRVC": adRVC,
       "adObjectId": adObjectId,
       "adObjectSubId": adObjectSubId,
       "adNumPorts": adNumPorts,
       "adPortTable": adPortTable,
       "adPortTableEntry": adPortTableEntry,
       "adpPortIndex": adpPortIndex,
       "adpType": adpType,
       "adpSubType": adpSubType,
       "adpFlowMaster": adpFlowMaster,
       "adpCreditResync": adpCreditResync,
       "adpResyncVCI": adpResyncVCI,
       "adpReceiveBuffers": adpReceiveBuffers,
       "adpPVCMin": adpPVCMin,
       "adpPVCMax": adpPVCMax,
       "adpSVCMin": adpSVCMin,
       "adpSVCMax": adpSVCMax,
       "adpRVCMin": adpRVCMin,
       "adpRVCMax": adpRVCMax,
       "adpBroadcastVCI": adpBroadcastVCI,
       "adpArpVCI": adpArpVCI,
       "adpHomeVCI": adpHomeVCI,
       "adpMaxReceiveBufferCounter": adpMaxReceiveBufferCounter,
       "adpUsedReceiveBuffers": adpUsedReceiveBuffers,
       "adpRemoteFlowMaster": adpRemoteFlowMaster,
       "adpOutputBandwidth": adpOutputBandwidth,
       "adpAvailableOutputBandwidth": adpAvailableOutputBandwidth,
       "dxatm": dxatm,
       "dxatmPvcTable": dxatmPvcTable,
       "dxatmPvcEntry": dxatmPvcEntry,
       "dxatmPvcLowIfIndex": dxatmPvcLowIfIndex,
       "dxatmPvcLowVpi": dxatmPvcLowVpi,
       "dxatmPvcLowVci": dxatmPvcLowVci,
       "dxatmPvcHighIfIndex": dxatmPvcHighIfIndex,
       "dxatmPvcHighVpi": dxatmPvcHighVpi,
       "dxatmPvcHighVci": dxatmPvcHighVci,
       "dxatmPvcAdminStatus": dxatmPvcAdminStatus,
       "dxatmPvcL2HOperStatus": dxatmPvcL2HOperStatus,
       "dxatmPvcH2LOperStatus": dxatmPvcH2LOperStatus,
       "dxatmPvcL2HFCStatus": dxatmPvcL2HFCStatus,
       "dxatmPvcH2LFCStatus": dxatmPvcH2LFCStatus,
       "dxatmPvcL2HTrafficDescriptorType": dxatmPvcL2HTrafficDescriptorType,
       "dxatmPvcL2HTrafficDescriptorParam1": dxatmPvcL2HTrafficDescriptorParam1,
       "dxatmPvcL2HTrafficDescriptorParam2": dxatmPvcL2HTrafficDescriptorParam2,
       "dxatmPvcL2HTrafficDescriptorParam3": dxatmPvcL2HTrafficDescriptorParam3,
       "dxatmPvcL2HTrafficDescriptorParam4": dxatmPvcL2HTrafficDescriptorParam4,
       "dxatmPvcL2HTrafficDescriptorParam5": dxatmPvcL2HTrafficDescriptorParam5,
       "dxatmPvcH2LTrafficDescriptorType": dxatmPvcH2LTrafficDescriptorType,
       "dxatmPvcH2LTrafficDescriptorParam1": dxatmPvcH2LTrafficDescriptorParam1,
       "dxatmPvcH2LTrafficDescriptorParam2": dxatmPvcH2LTrafficDescriptorParam2,
       "dxatmPvcH2LTrafficDescriptorParam3": dxatmPvcH2LTrafficDescriptorParam3,
       "dxatmPvcH2LTrafficDescriptorParam4": dxatmPvcH2LTrafficDescriptorParam4,
       "dxatmPvcH2LTrafficDescriptorParam5": dxatmPvcH2LTrafficDescriptorParam5,
       "dxatmPvcL2HQoSClass": dxatmPvcL2HQoSClass,
       "dxatmPvcH2LQoSClass": dxatmPvcH2LQoSClass,
       "dxatmPvcRowStatus": dxatmPvcRowStatus,
       "dxatmPvcMpTable": dxatmPvcMpTable,
       "dxatmPvcMpEntry": dxatmPvcMpEntry,
       "dxatmPvcMpRootIfIndex": dxatmPvcMpRootIfIndex,
       "dxatmPvcMpRootVpi": dxatmPvcMpRootVpi,
       "dxatmPvcMpRootVci": dxatmPvcMpRootVci,
       "dxatmPvcMpLeafIfIndex": dxatmPvcMpLeafIfIndex,
       "dxatmPvcMpLeafVpi": dxatmPvcMpLeafVpi,
       "dxatmPvcMpLeafVci": dxatmPvcMpLeafVci,
       "dxatmPvcMpAdminStatus": dxatmPvcMpAdminStatus,
       "dxatmPvcMpOperStatus": dxatmPvcMpOperStatus,
       "dxatmPvcMpFCStatus": dxatmPvcMpFCStatus,
       "dxatmPvcMpTrafficDescriptorType": dxatmPvcMpTrafficDescriptorType,
       "dxatmPvcMpTrafficDescriptorParam1": dxatmPvcMpTrafficDescriptorParam1,
       "dxatmPvcMpTrafficDescriptorParam2": dxatmPvcMpTrafficDescriptorParam2,
       "dxatmPvcMpTrafficDescriptorParam3": dxatmPvcMpTrafficDescriptorParam3,
       "dxatmPvcMpTrafficDescriptorParam4": dxatmPvcMpTrafficDescriptorParam4,
       "dxatmPvcMpTrafficDescriptorParam5": dxatmPvcMpTrafficDescriptorParam5,
       "dxatmPvcMpQoSClass": dxatmPvcMpQoSClass,
       "dxatmPvcMpRowStatus": dxatmPvcMpRowStatus,
       "dxatmVirtualPathObjects": dxatmVirtualPathObjects,
       "dxatmVpModeTable": dxatmVpModeTable,
       "dxatmVpModeEntry": dxatmVpModeEntry,
       "dxatmVpModeSlot": dxatmVpModeSlot,
       "dxatmVpModeDesired": dxatmVpModeDesired,
       "dxatmVpModeActual": dxatmVpModeActual,
       "dxatmVpTermTable": dxatmVpTermTable,
       "dxatmVpTermEntry": dxatmVpTermEntry,
       "dxatmVpTermIfIndex": dxatmVpTermIfIndex,
       "dxatmVpTermVpi": dxatmVpTermVpi,
       "dxatmVpTermAdminStatus": dxatmVpTermAdminStatus,
       "dxatmVpTermOperStatus": dxatmVpTermOperStatus,
       "dxatmVpTermPcr": dxatmVpTermPcr,
       "dxatmVpTermScr": dxatmVpTermScr,
       "dxatmVpTermMbs": dxatmVpTermMbs,
       "dxatmVpTermRowStatus": dxatmVpTermRowStatus}
)
