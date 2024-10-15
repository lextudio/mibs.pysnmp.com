# SNMP MIB module (PDN-CP-IWF-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/PDN-CP-IWF-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:37:24 2024
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

(InterfaceIndex,
 ifIndex) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex",
    "ifIndex")

(pdnCpIwf,) = mibBuilder.importSymbols(
    "PDN-HEADER-MIB",
    "pdnCpIwf")

(SwitchState,) = mibBuilder.importSymbols(
    "PDN-TC",
    "SwitchState")

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
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

pdnCpIwfMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 50, 1)
)
pdnCpIwfMIB.setRevisions(
        ("2004-12-02 17:00",
         "2004-10-07 11:00",
         "2004-08-30 11:00",
         "2004-07-15 00:00",
         "2004-03-22 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class CpIwfRegion(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("canada", 2),
          ("usa", 1))
    )



class GatewayProtocol(Integer32, TextualConvention):
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
        *(("lescas", 1),
          ("mgcp", 3),
          ("sip", 4),
          ("voiceband", 2))
    )



class HookState(Integer32, TextualConvention):
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
        *(("offhook", 2),
          ("onhook", 1),
          ("ringground", 3))
    )



class PotsSignaling(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("groundstart", 2),
          ("loopstart", 1))
    )



class ControlProtocol(Bits, TextualConvention):
    status = "current"


class VoiceEncoding(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("g711", 0),
          ("g726", 1),
          ("g729", 2))
    )



class PdnPotsTestTypes(Integer32, TextualConvention):
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
        *(("loopback", 2),
          ("noTest", 1),
          ("ringsignal", 3))
    )



# MIB Managed Objects in the order of their OIDs

_PdnCpIwfNotifications_ObjectIdentity = ObjectIdentity
pdnCpIwfNotifications = _PdnCpIwfNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 50, 1, 0)
)
_PdnCpIwfMIBObjects_ObjectIdentity = ObjectIdentity
pdnCpIwfMIBObjects = _PdnCpIwfMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 50, 1, 1)
)
_PdnCpIwfConfigObjects_ObjectIdentity = ObjectIdentity
pdnCpIwfConfigObjects = _PdnCpIwfConfigObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 50, 1, 1, 1)
)


class _PdnCpIwfTotalNumber_Type(Integer32):
    """Custom type pdnCpIwfTotalNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_PdnCpIwfTotalNumber_Type.__name__ = "Integer32"
_PdnCpIwfTotalNumber_Object = MibScalar
pdnCpIwfTotalNumber = _PdnCpIwfTotalNumber_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 50, 1, 1, 1, 1),
    _PdnCpIwfTotalNumber_Type()
)
pdnCpIwfTotalNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdnCpIwfTotalNumber.setStatus("current")


class _PdnCpIwfIndexNext_Type(Integer32):
    """Custom type pdnCpIwfIndexNext based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_PdnCpIwfIndexNext_Type.__name__ = "Integer32"
_PdnCpIwfIndexNext_Object = MibScalar
pdnCpIwfIndexNext = _PdnCpIwfIndexNext_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 50, 1, 1, 1, 2),
    _PdnCpIwfIndexNext_Type()
)
pdnCpIwfIndexNext.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdnCpIwfIndexNext.setStatus("current")
_PdnCpIwfRegion_Type = CpIwfRegion
_PdnCpIwfRegion_Object = MibScalar
pdnCpIwfRegion = _PdnCpIwfRegion_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 50, 1, 1, 1, 3),
    _PdnCpIwfRegion_Type()
)
pdnCpIwfRegion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pdnCpIwfRegion.setStatus("current")
_PdnCpIwfTable_Object = MibTable
pdnCpIwfTable = _PdnCpIwfTable_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 50, 1, 1, 1, 4)
)
if mibBuilder.loadTexts:
    pdnCpIwfTable.setStatus("current")
_PdnCpIwfEntry_Object = MibTableRow
pdnCpIwfEntry = _PdnCpIwfEntry_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 50, 1, 1, 1, 4, 1)
)
pdnCpIwfEntry.setIndexNames(
    (0, "PDN-CP-IWF-MIB", "pdnCpIwfIndex"),
)
if mibBuilder.loadTexts:
    pdnCpIwfEntry.setStatus("current")


class _PdnCpIwfIndex_Type(Integer32):
    """Custom type pdnCpIwfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_PdnCpIwfIndex_Type.__name__ = "Integer32"
_PdnCpIwfIndex_Object = MibTableColumn
pdnCpIwfIndex = _PdnCpIwfIndex_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 50, 1, 1, 1, 4, 1, 1),
    _PdnCpIwfIndex_Type()
)
pdnCpIwfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pdnCpIwfIndex.setStatus("current")
_PdnCpIwfIfIndex_Type = InterfaceIndex
_PdnCpIwfIfIndex_Object = MibTableColumn
pdnCpIwfIfIndex = _PdnCpIwfIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 50, 1, 1, 1, 4, 1, 2),
    _PdnCpIwfIfIndex_Type()
)
pdnCpIwfIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdnCpIwfIfIndex.setStatus("current")
_PdnCpIwfRowStatus_Type = RowStatus
_PdnCpIwfRowStatus_Object = MibTableColumn
pdnCpIwfRowStatus = _PdnCpIwfRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 50, 1, 1, 1, 4, 1, 3),
    _PdnCpIwfRowStatus_Type()
)
pdnCpIwfRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pdnCpIwfRowStatus.setStatus("current")


class _PdnCpIwfNumPotsAssigned_Type(Integer32):
    """Custom type pdnCpIwfNumPotsAssigned based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 24),
    )


_PdnCpIwfNumPotsAssigned_Type.__name__ = "Integer32"
_PdnCpIwfNumPotsAssigned_Object = MibTableColumn
pdnCpIwfNumPotsAssigned = _PdnCpIwfNumPotsAssigned_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 50, 1, 1, 1, 4, 1, 4),
    _PdnCpIwfNumPotsAssigned_Type()
)
pdnCpIwfNumPotsAssigned.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdnCpIwfNumPotsAssigned.setStatus("current")
_PdnCpIwfGatewayProtocol_Type = GatewayProtocol
_PdnCpIwfGatewayProtocol_Object = MibTableColumn
pdnCpIwfGatewayProtocol = _PdnCpIwfGatewayProtocol_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 50, 1, 1, 1, 4, 1, 5),
    _PdnCpIwfGatewayProtocol_Type()
)
pdnCpIwfGatewayProtocol.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pdnCpIwfGatewayProtocol.setStatus("current")
_PdnCpIwfAtmBLESCapability_Type = ControlProtocol
_PdnCpIwfAtmBLESCapability_Object = MibTableColumn
pdnCpIwfAtmBLESCapability = _PdnCpIwfAtmBLESCapability_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 50, 1, 1, 1, 4, 1, 6),
    _PdnCpIwfAtmBLESCapability_Type()
)
pdnCpIwfAtmBLESCapability.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdnCpIwfAtmBLESCapability.setStatus("current")
_PdnCpIwfSscsPredefinedProfile_Type = Integer32
_PdnCpIwfSscsPredefinedProfile_Object = MibTableColumn
pdnCpIwfSscsPredefinedProfile = _PdnCpIwfSscsPredefinedProfile_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 50, 1, 1, 1, 4, 1, 7),
    _PdnCpIwfSscsPredefinedProfile_Type()
)
pdnCpIwfSscsPredefinedProfile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pdnCpIwfSscsPredefinedProfile.setStatus("current")


class _PdnCpIwfJitterBufferLength_Type(Integer32):
    """Custom type pdnCpIwfJitterBufferLength based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 120),
    )


_PdnCpIwfJitterBufferLength_Type.__name__ = "Integer32"
_PdnCpIwfJitterBufferLength_Object = MibTableColumn
pdnCpIwfJitterBufferLength = _PdnCpIwfJitterBufferLength_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 50, 1, 1, 1, 4, 1, 8),
    _PdnCpIwfJitterBufferLength_Type()
)
pdnCpIwfJitterBufferLength.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pdnCpIwfJitterBufferLength.setStatus("current")
if mibBuilder.loadTexts:
    pdnCpIwfJitterBufferLength.setUnits("Milliseconds")
_PdnCpIwfMappingTable_Object = MibTable
pdnCpIwfMappingTable = _PdnCpIwfMappingTable_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 50, 1, 1, 1, 5)
)
if mibBuilder.loadTexts:
    pdnCpIwfMappingTable.setStatus("current")
_PdnCpIwfMappingEntry_Object = MibTableRow
pdnCpIwfMappingEntry = _PdnCpIwfMappingEntry_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 50, 1, 1, 1, 5, 1)
)
pdnCpIwfMappingEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    pdnCpIwfMappingEntry.setStatus("current")


class _PdnCpIwfMappingIndex_Type(Integer32):
    """Custom type pdnCpIwfMappingIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_PdnCpIwfMappingIndex_Type.__name__ = "Integer32"
_PdnCpIwfMappingIndex_Object = MibTableColumn
pdnCpIwfMappingIndex = _PdnCpIwfMappingIndex_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 50, 1, 1, 1, 5, 1, 1),
    _PdnCpIwfMappingIndex_Type()
)
pdnCpIwfMappingIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdnCpIwfMappingIndex.setStatus("current")
_PdnPotsPortTable_Object = MibTable
pdnPotsPortTable = _PdnPotsPortTable_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 50, 1, 1, 1, 6)
)
if mibBuilder.loadTexts:
    pdnPotsPortTable.setStatus("current")
_PdnPotsPortEntry_Object = MibTableRow
pdnPotsPortEntry = _PdnPotsPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 50, 1, 1, 1, 6, 1)
)
pdnPotsPortEntry.setIndexNames(
    (0, "PDN-CP-IWF-MIB", "pdnPotsPortIfIndex"),
)
if mibBuilder.loadTexts:
    pdnPotsPortEntry.setStatus("current")
_PdnPotsPortIfIndex_Type = InterfaceIndex
_PdnPotsPortIfIndex_Object = MibTableColumn
pdnPotsPortIfIndex = _PdnPotsPortIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 50, 1, 1, 1, 6, 1, 1),
    _PdnPotsPortIfIndex_Type()
)
pdnPotsPortIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pdnPotsPortIfIndex.setStatus("current")


class _PdnPotsPortCpIwfIndex_Type(Integer32):
    """Custom type pdnPotsPortCpIwfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_PdnPotsPortCpIwfIndex_Type.__name__ = "Integer32"
_PdnPotsPortCpIwfIndex_Object = MibTableColumn
pdnPotsPortCpIwfIndex = _PdnPotsPortCpIwfIndex_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 50, 1, 1, 1, 6, 1, 2),
    _PdnPotsPortCpIwfIndex_Type()
)
pdnPotsPortCpIwfIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pdnPotsPortCpIwfIndex.setStatus("current")
_PdnPotsPortHookStatus_Type = HookState
_PdnPotsPortHookStatus_Object = MibTableColumn
pdnPotsPortHookStatus = _PdnPotsPortHookStatus_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 50, 1, 1, 1, 6, 1, 3),
    _PdnPotsPortHookStatus_Type()
)
pdnPotsPortHookStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdnPotsPortHookStatus.setStatus("current")
_PdnPotsPortSignalingMethod_Type = PotsSignaling
_PdnPotsPortSignalingMethod_Object = MibTableColumn
pdnPotsPortSignalingMethod = _PdnPotsPortSignalingMethod_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 50, 1, 1, 1, 6, 1, 4),
    _PdnPotsPortSignalingMethod_Type()
)
pdnPotsPortSignalingMethod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pdnPotsPortSignalingMethod.setStatus("current")


class _PdnPotsPortTxGain_Type(Integer32):
    """Custom type pdnPotsPortTxGain based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-24, 23),
    )


_PdnPotsPortTxGain_Type.__name__ = "Integer32"
_PdnPotsPortTxGain_Object = MibTableColumn
pdnPotsPortTxGain = _PdnPotsPortTxGain_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 50, 1, 1, 1, 6, 1, 5),
    _PdnPotsPortTxGain_Type()
)
pdnPotsPortTxGain.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pdnPotsPortTxGain.setStatus("current")
if mibBuilder.loadTexts:
    pdnPotsPortTxGain.setUnits("dB")


class _PdnPotsPortRxGain_Type(Integer32):
    """Custom type pdnPotsPortRxGain based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-24, 23),
    )


_PdnPotsPortRxGain_Type.__name__ = "Integer32"
_PdnPotsPortRxGain_Object = MibTableColumn
pdnPotsPortRxGain = _PdnPotsPortRxGain_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 50, 1, 1, 1, 6, 1, 6),
    _PdnPotsPortRxGain_Type()
)
pdnPotsPortRxGain.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pdnPotsPortRxGain.setStatus("current")
if mibBuilder.loadTexts:
    pdnPotsPortRxGain.setUnits("dB")
_PdnPotsPortCustInfo_Type = DisplayString
_PdnPotsPortCustInfo_Object = MibTableColumn
pdnPotsPortCustInfo = _PdnPotsPortCustInfo_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 50, 1, 1, 1, 6, 1, 7),
    _PdnPotsPortCustInfo_Type()
)
pdnPotsPortCustInfo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pdnPotsPortCustInfo.setStatus("current")
_PdnPotsPortG729VoiceCodec_Type = SwitchState
_PdnPotsPortG729VoiceCodec_Object = MibTableColumn
pdnPotsPortG729VoiceCodec = _PdnPotsPortG729VoiceCodec_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 50, 1, 1, 1, 6, 1, 8),
    _PdnPotsPortG729VoiceCodec_Type()
)
pdnPotsPortG729VoiceCodec.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pdnPotsPortG729VoiceCodec.setStatus("current")
_PdnPotsPortPreferedVoiceCodec_Type = VoiceEncoding
_PdnPotsPortPreferedVoiceCodec_Object = MibTableColumn
pdnPotsPortPreferedVoiceCodec = _PdnPotsPortPreferedVoiceCodec_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 50, 1, 1, 1, 6, 1, 9),
    _PdnPotsPortPreferedVoiceCodec_Type()
)
pdnPotsPortPreferedVoiceCodec.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pdnPotsPortPreferedVoiceCodec.setStatus("current")


class _PdnPotsPortPreferredPacketPeriod_Type(Integer32):
    """Custom type pdnPotsPortPreferredPacketPeriod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_PdnPotsPortPreferredPacketPeriod_Type.__name__ = "Integer32"
_PdnPotsPortPreferredPacketPeriod_Object = MibTableColumn
pdnPotsPortPreferredPacketPeriod = _PdnPotsPortPreferredPacketPeriod_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 50, 1, 1, 1, 6, 1, 10),
    _PdnPotsPortPreferredPacketPeriod_Type()
)
pdnPotsPortPreferredPacketPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pdnPotsPortPreferredPacketPeriod.setStatus("current")
if mibBuilder.loadTexts:
    pdnPotsPortPreferredPacketPeriod.setUnits("Milliseconds")
_PdnPotsPortSilenceSuppression_Type = SwitchState
_PdnPotsPortSilenceSuppression_Object = MibTableColumn
pdnPotsPortSilenceSuppression = _PdnPotsPortSilenceSuppression_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 50, 1, 1, 1, 6, 1, 11),
    _PdnPotsPortSilenceSuppression_Type()
)
pdnPotsPortSilenceSuppression.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pdnPotsPortSilenceSuppression.setStatus("current")
_PdnPotsPortActualVoiceCodec_Type = VoiceEncoding
_PdnPotsPortActualVoiceCodec_Object = MibTableColumn
pdnPotsPortActualVoiceCodec = _PdnPotsPortActualVoiceCodec_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 50, 1, 1, 1, 6, 1, 12),
    _PdnPotsPortActualVoiceCodec_Type()
)
pdnPotsPortActualVoiceCodec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdnPotsPortActualVoiceCodec.setStatus("current")


class _PdnPotsPortCallElapsedTime_Type(Integer32):
    """Custom type pdnPotsPortCallElapsedTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_PdnPotsPortCallElapsedTime_Type.__name__ = "Integer32"
_PdnPotsPortCallElapsedTime_Object = MibTableColumn
pdnPotsPortCallElapsedTime = _PdnPotsPortCallElapsedTime_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 50, 1, 1, 1, 6, 1, 13),
    _PdnPotsPortCallElapsedTime_Type()
)
pdnPotsPortCallElapsedTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdnPotsPortCallElapsedTime.setStatus("current")
if mibBuilder.loadTexts:
    pdnPotsPortCallElapsedTime.setUnits("Seconds")
_PdnPotsPortModemDetected_Type = TruthValue
_PdnPotsPortModemDetected_Object = MibTableColumn
pdnPotsPortModemDetected = _PdnPotsPortModemDetected_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 50, 1, 1, 1, 6, 1, 14),
    _PdnPotsPortModemDetected_Type()
)
pdnPotsPortModemDetected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdnPotsPortModemDetected.setStatus("current")


class _PdnPotsPortEchoCanceller_Type(Integer32):
    """Custom type pdnPotsPortEchoCanceller based on Integer32"""
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


_PdnPotsPortEchoCanceller_Type.__name__ = "Integer32"
_PdnPotsPortEchoCanceller_Object = MibTableColumn
pdnPotsPortEchoCanceller = _PdnPotsPortEchoCanceller_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 50, 1, 1, 1, 6, 1, 15),
    _PdnPotsPortEchoCanceller_Type()
)
pdnPotsPortEchoCanceller.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdnPotsPortEchoCanceller.setStatus("current")


class _PdnPotsPortLocalEndName_Type(DisplayString):
    """Custom type pdnPotsPortLocalEndName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_PdnPotsPortLocalEndName_Type.__name__ = "DisplayString"
_PdnPotsPortLocalEndName_Object = MibTableColumn
pdnPotsPortLocalEndName = _PdnPotsPortLocalEndName_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 50, 1, 1, 1, 6, 1, 16),
    _PdnPotsPortLocalEndName_Type()
)
pdnPotsPortLocalEndName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pdnPotsPortLocalEndName.setStatus("current")


class _PdnPotsPortActiveSoftswitch_Type(Integer32):
    """Custom type pdnPotsPortActiveSoftswitch based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("none", 3),
          ("primary", 1),
          ("secondary", 2))
    )


_PdnPotsPortActiveSoftswitch_Type.__name__ = "Integer32"
_PdnPotsPortActiveSoftswitch_Object = MibTableColumn
pdnPotsPortActiveSoftswitch = _PdnPotsPortActiveSoftswitch_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 50, 1, 1, 1, 6, 1, 17),
    _PdnPotsPortActiveSoftswitch_Type()
)
pdnPotsPortActiveSoftswitch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdnPotsPortActiveSoftswitch.setStatus("current")
_PdnCpIwfTestObjects_ObjectIdentity = ObjectIdentity
pdnCpIwfTestObjects = _PdnCpIwfTestObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 50, 1, 1, 2)
)
_PdnPotsTestTable_Object = MibTable
pdnPotsTestTable = _PdnPotsTestTable_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 50, 1, 1, 2, 1)
)
if mibBuilder.loadTexts:
    pdnPotsTestTable.setStatus("current")
_PdnPotsTestEntry_Object = MibTableRow
pdnPotsTestEntry = _PdnPotsTestEntry_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 50, 1, 1, 2, 1, 1)
)
pdnPotsTestEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    pdnPotsTestEntry.setStatus("current")
_PdnPotsTestType_Type = PdnPotsTestTypes
_PdnPotsTestType_Object = MibTableColumn
pdnPotsTestType = _PdnPotsTestType_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 50, 1, 1, 2, 1, 1, 1),
    _PdnPotsTestType_Type()
)
pdnPotsTestType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pdnPotsTestType.setStatus("current")


class _PdnPotsTestCmd_Type(Integer32):
    """Custom type pdnPotsTestCmd based on Integer32"""
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
        *(("keepAlive", 4),
          ("noOp", 1),
          ("start", 2),
          ("stop", 3))
    )


_PdnPotsTestCmd_Type.__name__ = "Integer32"
_PdnPotsTestCmd_Object = MibTableColumn
pdnPotsTestCmd = _PdnPotsTestCmd_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 50, 1, 1, 2, 1, 1, 2),
    _PdnPotsTestCmd_Type()
)
pdnPotsTestCmd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pdnPotsTestCmd.setStatus("current")


class _PdnPotsTestStatus_Type(Integer32):
    """Custom type pdnPotsTestStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("inactive", 2))
    )


_PdnPotsTestStatus_Type.__name__ = "Integer32"
_PdnPotsTestStatus_Object = MibTableColumn
pdnPotsTestStatus = _PdnPotsTestStatus_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 50, 1, 1, 2, 1, 1, 3),
    _PdnPotsTestStatus_Type()
)
pdnPotsTestStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdnPotsTestStatus.setStatus("current")
_PdnCpIwfStatsObjects_ObjectIdentity = ObjectIdentity
pdnCpIwfStatsObjects = _PdnCpIwfStatsObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 50, 1, 1, 3)
)
_PdnCpIwfAal2StatsTable_Object = MibTable
pdnCpIwfAal2StatsTable = _PdnCpIwfAal2StatsTable_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 50, 1, 1, 3, 1)
)
if mibBuilder.loadTexts:
    pdnCpIwfAal2StatsTable.setStatus("current")
_PdnCpIwfAal2StatsEntry_Object = MibTableRow
pdnCpIwfAal2StatsEntry = _PdnCpIwfAal2StatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 50, 1, 1, 3, 1, 1)
)
pdnCpIwfAal2StatsEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    pdnCpIwfAal2StatsEntry.setStatus("current")
_PdnCpIwfAal2CpsRxPkts_Type = Counter32
_PdnCpIwfAal2CpsRxPkts_Object = MibTableColumn
pdnCpIwfAal2CpsRxPkts = _PdnCpIwfAal2CpsRxPkts_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 50, 1, 1, 3, 1, 1, 1),
    _PdnCpIwfAal2CpsRxPkts_Type()
)
pdnCpIwfAal2CpsRxPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdnCpIwfAal2CpsRxPkts.setStatus("current")
_PdnCpIwfAal2CpsTxPkts_Type = Counter32
_PdnCpIwfAal2CpsTxPkts_Object = MibTableColumn
pdnCpIwfAal2CpsTxPkts = _PdnCpIwfAal2CpsTxPkts_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 50, 1, 1, 3, 1, 1, 2),
    _PdnCpIwfAal2CpsTxPkts_Type()
)
pdnCpIwfAal2CpsTxPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdnCpIwfAal2CpsTxPkts.setStatus("current")
_PdnCpIwfAal2CpsParityErrors_Type = Counter32
_PdnCpIwfAal2CpsParityErrors_Object = MibTableColumn
pdnCpIwfAal2CpsParityErrors = _PdnCpIwfAal2CpsParityErrors_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 50, 1, 1, 3, 1, 1, 3),
    _PdnCpIwfAal2CpsParityErrors_Type()
)
pdnCpIwfAal2CpsParityErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdnCpIwfAal2CpsParityErrors.setStatus("current")
_PdnCpIwfAal2CpsSeqNumErrors_Type = Counter32
_PdnCpIwfAal2CpsSeqNumErrors_Object = MibTableColumn
pdnCpIwfAal2CpsSeqNumErrors = _PdnCpIwfAal2CpsSeqNumErrors_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 50, 1, 1, 3, 1, 1, 4),
    _PdnCpIwfAal2CpsSeqNumErrors_Type()
)
pdnCpIwfAal2CpsSeqNumErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdnCpIwfAal2CpsSeqNumErrors.setStatus("current")
_PdnCpIwfAal2CpsOsfMismatchErrors_Type = Counter32
_PdnCpIwfAal2CpsOsfMismatchErrors_Object = MibTableColumn
pdnCpIwfAal2CpsOsfMismatchErrors = _PdnCpIwfAal2CpsOsfMismatchErrors_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 50, 1, 1, 3, 1, 1, 5),
    _PdnCpIwfAal2CpsOsfMismatchErrors_Type()
)
pdnCpIwfAal2CpsOsfMismatchErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdnCpIwfAal2CpsOsfMismatchErrors.setStatus("current")
_PdnCpIwfAal2CpsOsfErrors_Type = Counter32
_PdnCpIwfAal2CpsOsfErrors_Object = MibTableColumn
pdnCpIwfAal2CpsOsfErrors = _PdnCpIwfAal2CpsOsfErrors_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 50, 1, 1, 3, 1, 1, 6),
    _PdnCpIwfAal2CpsOsfErrors_Type()
)
pdnCpIwfAal2CpsOsfErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdnCpIwfAal2CpsOsfErrors.setStatus("current")
_PdnCpIwfAal2CpsHecErrors_Type = Counter32
_PdnCpIwfAal2CpsHecErrors_Object = MibTableColumn
pdnCpIwfAal2CpsHecErrors = _PdnCpIwfAal2CpsHecErrors_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 50, 1, 1, 3, 1, 1, 7),
    _PdnCpIwfAal2CpsHecErrors_Type()
)
pdnCpIwfAal2CpsHecErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdnCpIwfAal2CpsHecErrors.setStatus("current")
_PdnCpIwfAal2CpsOversizeSduErrors_Type = Counter32
_PdnCpIwfAal2CpsOversizeSduErrors_Object = MibTableColumn
pdnCpIwfAal2CpsOversizeSduErrors = _PdnCpIwfAal2CpsOversizeSduErrors_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 50, 1, 1, 3, 1, 1, 8),
    _PdnCpIwfAal2CpsOversizeSduErrors_Type()
)
pdnCpIwfAal2CpsOversizeSduErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdnCpIwfAal2CpsOversizeSduErrors.setStatus("current")
_PdnCpIwfAal2CpsReassemblyErrors_Type = Counter32
_PdnCpIwfAal2CpsReassemblyErrors_Object = MibTableColumn
pdnCpIwfAal2CpsReassemblyErrors = _PdnCpIwfAal2CpsReassemblyErrors_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 50, 1, 1, 3, 1, 1, 9),
    _PdnCpIwfAal2CpsReassemblyErrors_Type()
)
pdnCpIwfAal2CpsReassemblyErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdnCpIwfAal2CpsReassemblyErrors.setStatus("current")
_PdnCpIwfAal2CpsHecOverlapErrors_Type = Counter32
_PdnCpIwfAal2CpsHecOverlapErrors_Object = MibTableColumn
pdnCpIwfAal2CpsHecOverlapErrors = _PdnCpIwfAal2CpsHecOverlapErrors_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 50, 1, 1, 3, 1, 1, 10),
    _PdnCpIwfAal2CpsHecOverlapErrors_Type()
)
pdnCpIwfAal2CpsHecOverlapErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdnCpIwfAal2CpsHecOverlapErrors.setStatus("current")
_PdnCpIwfAal2CpsUuiErrors_Type = Counter32
_PdnCpIwfAal2CpsUuiErrors_Object = MibTableColumn
pdnCpIwfAal2CpsUuiErrors = _PdnCpIwfAal2CpsUuiErrors_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 50, 1, 1, 3, 1, 1, 11),
    _PdnCpIwfAal2CpsUuiErrors_Type()
)
pdnCpIwfAal2CpsUuiErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdnCpIwfAal2CpsUuiErrors.setStatus("current")
_PdnCpIwfAal2CpsCidErrors_Type = Counter32
_PdnCpIwfAal2CpsCidErrors_Object = MibTableColumn
pdnCpIwfAal2CpsCidErrors = _PdnCpIwfAal2CpsCidErrors_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 50, 1, 1, 3, 1, 1, 12),
    _PdnCpIwfAal2CpsCidErrors_Type()
)
pdnCpIwfAal2CpsCidErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdnCpIwfAal2CpsCidErrors.setStatus("current")
_PdnPotsPortStatsTable_Object = MibTable
pdnPotsPortStatsTable = _PdnPotsPortStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 50, 1, 1, 3, 2)
)
if mibBuilder.loadTexts:
    pdnPotsPortStatsTable.setStatus("current")
_PdnPotsPortStatsEntry_Object = MibTableRow
pdnPotsPortStatsEntry = _PdnPotsPortStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 50, 1, 1, 3, 2, 1)
)
pdnPotsPortStatsEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    pdnPotsPortStatsEntry.setStatus("current")
_PdnPotsPortTotalCalls_Type = Counter32
_PdnPotsPortTotalCalls_Object = MibTableColumn
pdnPotsPortTotalCalls = _PdnPotsPortTotalCalls_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 50, 1, 1, 3, 2, 1, 1),
    _PdnPotsPortTotalCalls_Type()
)
pdnPotsPortTotalCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdnPotsPortTotalCalls.setStatus("current")
_PdnPotsPortTotalCallsFailure_Type = Counter32
_PdnPotsPortTotalCallsFailure_Object = MibTableColumn
pdnPotsPortTotalCallsFailure = _PdnPotsPortTotalCallsFailure_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 50, 1, 1, 3, 2, 1, 2),
    _PdnPotsPortTotalCallsFailure_Type()
)
pdnPotsPortTotalCallsFailure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdnPotsPortTotalCallsFailure.setStatus("current")
_PdnPotsPortTotalCallsDropped_Type = Counter32
_PdnPotsPortTotalCallsDropped_Object = MibTableColumn
pdnPotsPortTotalCallsDropped = _PdnPotsPortTotalCallsDropped_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 50, 1, 1, 3, 2, 1, 3),
    _PdnPotsPortTotalCallsDropped_Type()
)
pdnPotsPortTotalCallsDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdnPotsPortTotalCallsDropped.setStatus("current")
_PdnPotsPortInCallsReceived_Type = Counter32
_PdnPotsPortInCallsReceived_Object = MibTableColumn
pdnPotsPortInCallsReceived = _PdnPotsPortInCallsReceived_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 50, 1, 1, 3, 2, 1, 4),
    _PdnPotsPortInCallsReceived_Type()
)
pdnPotsPortInCallsReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdnPotsPortInCallsReceived.setStatus("current")
_PdnPotsPortInCallsAnswered_Type = Counter32
_PdnPotsPortInCallsAnswered_Object = MibTableColumn
pdnPotsPortInCallsAnswered = _PdnPotsPortInCallsAnswered_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 50, 1, 1, 3, 2, 1, 5),
    _PdnPotsPortInCallsAnswered_Type()
)
pdnPotsPortInCallsAnswered.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdnPotsPortInCallsAnswered.setStatus("current")
_PdnPotsPortInCallsConnected_Type = Counter32
_PdnPotsPortInCallsConnected_Object = MibTableColumn
pdnPotsPortInCallsConnected = _PdnPotsPortInCallsConnected_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 50, 1, 1, 3, 2, 1, 6),
    _PdnPotsPortInCallsConnected_Type()
)
pdnPotsPortInCallsConnected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdnPotsPortInCallsConnected.setStatus("current")
_PdnPotsPortInCallsFailure_Type = Counter32
_PdnPotsPortInCallsFailure_Object = MibTableColumn
pdnPotsPortInCallsFailure = _PdnPotsPortInCallsFailure_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 50, 1, 1, 3, 2, 1, 7),
    _PdnPotsPortInCallsFailure_Type()
)
pdnPotsPortInCallsFailure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdnPotsPortInCallsFailure.setStatus("current")
_PdnPotsPortOutCallsAttempted_Type = Counter32
_PdnPotsPortOutCallsAttempted_Object = MibTableColumn
pdnPotsPortOutCallsAttempted = _PdnPotsPortOutCallsAttempted_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 50, 1, 1, 3, 2, 1, 8),
    _PdnPotsPortOutCallsAttempted_Type()
)
pdnPotsPortOutCallsAttempted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdnPotsPortOutCallsAttempted.setStatus("current")
_PdnPotsPortOutCallsAnswered_Type = Counter32
_PdnPotsPortOutCallsAnswered_Object = MibTableColumn
pdnPotsPortOutCallsAnswered = _PdnPotsPortOutCallsAnswered_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 50, 1, 1, 3, 2, 1, 9),
    _PdnPotsPortOutCallsAnswered_Type()
)
pdnPotsPortOutCallsAnswered.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdnPotsPortOutCallsAnswered.setStatus("current")
_PdnPotsPortOutCallsConnected_Type = Counter32
_PdnPotsPortOutCallsConnected_Object = MibTableColumn
pdnPotsPortOutCallsConnected = _PdnPotsPortOutCallsConnected_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 50, 1, 1, 3, 2, 1, 10),
    _PdnPotsPortOutCallsConnected_Type()
)
pdnPotsPortOutCallsConnected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdnPotsPortOutCallsConnected.setStatus("current")
_PdnPotsPortOutCallsFailure_Type = Counter32
_PdnPotsPortOutCallsFailure_Object = MibTableColumn
pdnPotsPortOutCallsFailure = _PdnPotsPortOutCallsFailure_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 50, 1, 1, 3, 2, 1, 11),
    _PdnPotsPortOutCallsFailure_Type()
)
pdnPotsPortOutCallsFailure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdnPotsPortOutCallsFailure.setStatus("current")
_PdnPotsPortPacketsSent_Type = Counter32
_PdnPotsPortPacketsSent_Object = MibTableColumn
pdnPotsPortPacketsSent = _PdnPotsPortPacketsSent_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 50, 1, 1, 3, 2, 1, 12),
    _PdnPotsPortPacketsSent_Type()
)
pdnPotsPortPacketsSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdnPotsPortPacketsSent.setStatus("current")
_PdnPotsPortPacketsReceived_Type = Counter32
_PdnPotsPortPacketsReceived_Object = MibTableColumn
pdnPotsPortPacketsReceived = _PdnPotsPortPacketsReceived_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 50, 1, 1, 3, 2, 1, 13),
    _PdnPotsPortPacketsReceived_Type()
)
pdnPotsPortPacketsReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdnPotsPortPacketsReceived.setStatus("current")
_PdnPotsPortPacketsLost_Type = Counter32
_PdnPotsPortPacketsLost_Object = MibTableColumn
pdnPotsPortPacketsLost = _PdnPotsPortPacketsLost_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 50, 1, 1, 3, 2, 1, 14),
    _PdnPotsPortPacketsLost_Type()
)
pdnPotsPortPacketsLost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdnPotsPortPacketsLost.setStatus("current")
_PdnPotsPortBytesSent_Type = Counter32
_PdnPotsPortBytesSent_Object = MibTableColumn
pdnPotsPortBytesSent = _PdnPotsPortBytesSent_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 50, 1, 1, 3, 2, 1, 15),
    _PdnPotsPortBytesSent_Type()
)
pdnPotsPortBytesSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdnPotsPortBytesSent.setStatus("current")
_PdnPotsPortBytesReceived_Type = Counter32
_PdnPotsPortBytesReceived_Object = MibTableColumn
pdnPotsPortBytesReceived = _PdnPotsPortBytesReceived_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 50, 1, 1, 3, 2, 1, 16),
    _PdnPotsPortBytesReceived_Type()
)
pdnPotsPortBytesReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdnPotsPortBytesReceived.setStatus("current")
_PdnCpIwfMIBConformance_ObjectIdentity = ObjectIdentity
pdnCpIwfMIBConformance = _PdnCpIwfMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 50, 1, 2)
)
_PdnCpIwfMIBCompliances_ObjectIdentity = ObjectIdentity
pdnCpIwfMIBCompliances = _PdnCpIwfMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 50, 1, 2, 1)
)
_PdnCpIwfMIBGroups_ObjectIdentity = ObjectIdentity
pdnCpIwfMIBGroups = _PdnCpIwfMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 50, 1, 2, 2)
)

# Managed Objects groups

pdnCpIwfGeneralConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 50, 1, 2, 2, 1)
)
pdnCpIwfGeneralConfigGroup.setObjects(
      *(("PDN-CP-IWF-MIB", "pdnCpIwfTotalNumber"),
        ("PDN-CP-IWF-MIB", "pdnCpIwfIndexNext"),
        ("PDN-CP-IWF-MIB", "pdnCpIwfRegion"),
        ("PDN-CP-IWF-MIB", "pdnCpIwfIfIndex"),
        ("PDN-CP-IWF-MIB", "pdnCpIwfRowStatus"),
        ("PDN-CP-IWF-MIB", "pdnCpIwfNumPotsAssigned"),
        ("PDN-CP-IWF-MIB", "pdnCpIwfGatewayProtocol"),
        ("PDN-CP-IWF-MIB", "pdnCpIwfAtmBLESCapability"),
        ("PDN-CP-IWF-MIB", "pdnCpIwfSscsPredefinedProfile"),
        ("PDN-CP-IWF-MIB", "pdnCpIwfMappingIndex"))
)
if mibBuilder.loadTexts:
    pdnCpIwfGeneralConfigGroup.setStatus("deprecated")

pdnCpIwfPotsPortConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 50, 1, 2, 2, 2)
)
pdnCpIwfPotsPortConfigGroup.setObjects(
      *(("PDN-CP-IWF-MIB", "pdnPotsPortCpIwfIndex"),
        ("PDN-CP-IWF-MIB", "pdnPotsPortHookStatus"),
        ("PDN-CP-IWF-MIB", "pdnPotsPortSignalingMethod"),
        ("PDN-CP-IWF-MIB", "pdnPotsPortTxGain"),
        ("PDN-CP-IWF-MIB", "pdnPotsPortRxGain"))
)
if mibBuilder.loadTexts:
    pdnCpIwfPotsPortConfigGroup.setStatus("deprecated")

pdnCpIwfAal2StatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 50, 1, 2, 2, 3)
)
pdnCpIwfAal2StatsGroup.setObjects(
      *(("PDN-CP-IWF-MIB", "pdnCpIwfAal2CpsRxPkts"),
        ("PDN-CP-IWF-MIB", "pdnCpIwfAal2CpsTxPkts"),
        ("PDN-CP-IWF-MIB", "pdnCpIwfAal2CpsParityErrors"),
        ("PDN-CP-IWF-MIB", "pdnCpIwfAal2CpsSeqNumErrors"),
        ("PDN-CP-IWF-MIB", "pdnCpIwfAal2CpsOsfMismatchErrors"),
        ("PDN-CP-IWF-MIB", "pdnCpIwfAal2CpsOsfErrors"),
        ("PDN-CP-IWF-MIB", "pdnCpIwfAal2CpsHecErrors"),
        ("PDN-CP-IWF-MIB", "pdnCpIwfAal2CpsOversizeSduErrors"),
        ("PDN-CP-IWF-MIB", "pdnCpIwfAal2CpsReassemblyErrors"),
        ("PDN-CP-IWF-MIB", "pdnCpIwfAal2CpsHecOverlapErrors"),
        ("PDN-CP-IWF-MIB", "pdnCpIwfAal2CpsUuiErrors"),
        ("PDN-CP-IWF-MIB", "pdnCpIwfAal2CpsCidErrors"))
)
if mibBuilder.loadTexts:
    pdnCpIwfAal2StatsGroup.setStatus("current")

pdnCpIwfPotsPortStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 50, 1, 2, 2, 4)
)
pdnCpIwfPotsPortStatsGroup.setObjects(
    ("PDN-CP-IWF-MIB", "pdnPotsPortTotalCalls")
)
if mibBuilder.loadTexts:
    pdnCpIwfPotsPortStatsGroup.setStatus("deprecated")

pdnCpIwfGeneralConfigGroupV2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 50, 1, 2, 2, 5)
)
pdnCpIwfGeneralConfigGroupV2.setObjects(
      *(("PDN-CP-IWF-MIB", "pdnCpIwfTotalNumber"),
        ("PDN-CP-IWF-MIB", "pdnCpIwfIndexNext"),
        ("PDN-CP-IWF-MIB", "pdnCpIwfRegion"))
)
if mibBuilder.loadTexts:
    pdnCpIwfGeneralConfigGroupV2.setStatus("current")

pdnCpIwfIADConfigGroupV2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 50, 1, 2, 2, 6)
)
pdnCpIwfIADConfigGroupV2.setObjects(
      *(("PDN-CP-IWF-MIB", "pdnCpIwfIfIndex"),
        ("PDN-CP-IWF-MIB", "pdnCpIwfRowStatus"),
        ("PDN-CP-IWF-MIB", "pdnCpIwfNumPotsAssigned"),
        ("PDN-CP-IWF-MIB", "pdnCpIwfGatewayProtocol"),
        ("PDN-CP-IWF-MIB", "pdnCpIwfAtmBLESCapability"),
        ("PDN-CP-IWF-MIB", "pdnCpIwfSscsPredefinedProfile"),
        ("PDN-CP-IWF-MIB", "pdnCpIwfMappingIndex"))
)
if mibBuilder.loadTexts:
    pdnCpIwfIADConfigGroupV2.setStatus("current")

pdnCpIwfPotsPortStatsGroupV2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 50, 1, 2, 2, 7)
)
pdnCpIwfPotsPortStatsGroupV2.setObjects(
      *(("PDN-CP-IWF-MIB", "pdnPotsPortTotalCalls"),
        ("PDN-CP-IWF-MIB", "pdnPotsPortTotalCallsFailure"),
        ("PDN-CP-IWF-MIB", "pdnPotsPortTotalCallsDropped"),
        ("PDN-CP-IWF-MIB", "pdnPotsPortInCallsReceived"),
        ("PDN-CP-IWF-MIB", "pdnPotsPortInCallsAnswered"),
        ("PDN-CP-IWF-MIB", "pdnPotsPortInCallsConnected"),
        ("PDN-CP-IWF-MIB", "pdnPotsPortInCallsFailure"),
        ("PDN-CP-IWF-MIB", "pdnPotsPortOutCallsAttempted"),
        ("PDN-CP-IWF-MIB", "pdnPotsPortOutCallsAnswered"),
        ("PDN-CP-IWF-MIB", "pdnPotsPortOutCallsConnected"),
        ("PDN-CP-IWF-MIB", "pdnPotsPortOutCallsFailure"),
        ("PDN-CP-IWF-MIB", "pdnPotsPortPacketsSent"),
        ("PDN-CP-IWF-MIB", "pdnPotsPortPacketsReceived"),
        ("PDN-CP-IWF-MIB", "pdnPotsPortPacketsLost"),
        ("PDN-CP-IWF-MIB", "pdnPotsPortBytesSent"),
        ("PDN-CP-IWF-MIB", "pdnPotsPortBytesReceived"))
)
if mibBuilder.loadTexts:
    pdnCpIwfPotsPortStatsGroupV2.setStatus("current")

pdnCpIwfPotsPortConfigGroupV2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 50, 1, 2, 2, 8)
)
pdnCpIwfPotsPortConfigGroupV2.setObjects(
      *(("PDN-CP-IWF-MIB", "pdnPotsPortCpIwfIndex"),
        ("PDN-CP-IWF-MIB", "pdnPotsPortHookStatus"),
        ("PDN-CP-IWF-MIB", "pdnPotsPortSignalingMethod"),
        ("PDN-CP-IWF-MIB", "pdnPotsPortTxGain"),
        ("PDN-CP-IWF-MIB", "pdnPotsPortRxGain"),
        ("PDN-CP-IWF-MIB", "pdnPotsPortCustInfo"),
        ("PDN-CP-IWF-MIB", "pdnPotsPortG729VoiceCodec"),
        ("PDN-CP-IWF-MIB", "pdnPotsPortPreferedVoiceCodec"),
        ("PDN-CP-IWF-MIB", "pdnPotsPortPreferredPacketPeriod"),
        ("PDN-CP-IWF-MIB", "pdnPotsPortSilenceSuppression"),
        ("PDN-CP-IWF-MIB", "pdnPotsPortActualVoiceCodec"),
        ("PDN-CP-IWF-MIB", "pdnPotsPortCallElapsedTime"),
        ("PDN-CP-IWF-MIB", "pdnPotsPortModemDetected"),
        ("PDN-CP-IWF-MIB", "pdnPotsPortEchoCanceller"),
        ("PDN-CP-IWF-MIB", "pdnPotsPortLocalEndName"),
        ("PDN-CP-IWF-MIB", "pdnPotsPortActiveSoftswitch"))
)
if mibBuilder.loadTexts:
    pdnCpIwfPotsPortConfigGroupV2.setStatus("current")

pdnCpIwfPotsPortTestGroupV2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 50, 1, 2, 2, 9)
)
pdnCpIwfPotsPortTestGroupV2.setObjects(
      *(("PDN-CP-IWF-MIB", "pdnPotsTestType"),
        ("PDN-CP-IWF-MIB", "pdnPotsTestCmd"),
        ("PDN-CP-IWF-MIB", "pdnPotsTestStatus"))
)
if mibBuilder.loadTexts:
    pdnCpIwfPotsPortTestGroupV2.setStatus("current")

pdnCpIwfIADConfigGroupV3 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 50, 1, 2, 2, 10)
)
pdnCpIwfIADConfigGroupV3.setObjects(
      *(("PDN-CP-IWF-MIB", "pdnCpIwfIfIndex"),
        ("PDN-CP-IWF-MIB", "pdnCpIwfRowStatus"),
        ("PDN-CP-IWF-MIB", "pdnCpIwfNumPotsAssigned"),
        ("PDN-CP-IWF-MIB", "pdnCpIwfGatewayProtocol"),
        ("PDN-CP-IWF-MIB", "pdnCpIwfAtmBLESCapability"),
        ("PDN-CP-IWF-MIB", "pdnCpIwfSscsPredefinedProfile"),
        ("PDN-CP-IWF-MIB", "pdnCpIwfJitterBufferLength"),
        ("PDN-CP-IWF-MIB", "pdnCpIwfMappingIndex"))
)
if mibBuilder.loadTexts:
    pdnCpIwfIADConfigGroupV3.setStatus("current")

pdnCpIwfPotsPortPacketStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 50, 1, 2, 2, 11)
)
pdnCpIwfPotsPortPacketStatsGroup.setObjects(
      *(("PDN-CP-IWF-MIB", "pdnPotsPortPacketsSent"),
        ("PDN-CP-IWF-MIB", "pdnPotsPortPacketsReceived"),
        ("PDN-CP-IWF-MIB", "pdnPotsPortPacketsLost"),
        ("PDN-CP-IWF-MIB", "pdnPotsPortBytesSent"),
        ("PDN-CP-IWF-MIB", "pdnPotsPortBytesReceived"))
)
if mibBuilder.loadTexts:
    pdnCpIwfPotsPortPacketStatsGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

pdnCpIwfMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 50, 1, 2, 1, 1)
)
if mibBuilder.loadTexts:
    pdnCpIwfMIBCompliance.setStatus(
        "deprecated"
    )

pdnCpIwfMIBComplianceV2 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 50, 1, 2, 1, 2)
)
if mibBuilder.loadTexts:
    pdnCpIwfMIBComplianceV2.setStatus(
        "deprecated"
    )

pdnCpIwfMIBComplianceV3 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 50, 1, 2, 1, 3)
)
if mibBuilder.loadTexts:
    pdnCpIwfMIBComplianceV3.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "PDN-CP-IWF-MIB",
    **{"CpIwfRegion": CpIwfRegion,
       "GatewayProtocol": GatewayProtocol,
       "HookState": HookState,
       "PotsSignaling": PotsSignaling,
       "ControlProtocol": ControlProtocol,
       "VoiceEncoding": VoiceEncoding,
       "PdnPotsTestTypes": PdnPotsTestTypes,
       "pdnCpIwfMIB": pdnCpIwfMIB,
       "pdnCpIwfNotifications": pdnCpIwfNotifications,
       "pdnCpIwfMIBObjects": pdnCpIwfMIBObjects,
       "pdnCpIwfConfigObjects": pdnCpIwfConfigObjects,
       "pdnCpIwfTotalNumber": pdnCpIwfTotalNumber,
       "pdnCpIwfIndexNext": pdnCpIwfIndexNext,
       "pdnCpIwfRegion": pdnCpIwfRegion,
       "pdnCpIwfTable": pdnCpIwfTable,
       "pdnCpIwfEntry": pdnCpIwfEntry,
       "pdnCpIwfIndex": pdnCpIwfIndex,
       "pdnCpIwfIfIndex": pdnCpIwfIfIndex,
       "pdnCpIwfRowStatus": pdnCpIwfRowStatus,
       "pdnCpIwfNumPotsAssigned": pdnCpIwfNumPotsAssigned,
       "pdnCpIwfGatewayProtocol": pdnCpIwfGatewayProtocol,
       "pdnCpIwfAtmBLESCapability": pdnCpIwfAtmBLESCapability,
       "pdnCpIwfSscsPredefinedProfile": pdnCpIwfSscsPredefinedProfile,
       "pdnCpIwfJitterBufferLength": pdnCpIwfJitterBufferLength,
       "pdnCpIwfMappingTable": pdnCpIwfMappingTable,
       "pdnCpIwfMappingEntry": pdnCpIwfMappingEntry,
       "pdnCpIwfMappingIndex": pdnCpIwfMappingIndex,
       "pdnPotsPortTable": pdnPotsPortTable,
       "pdnPotsPortEntry": pdnPotsPortEntry,
       "pdnPotsPortIfIndex": pdnPotsPortIfIndex,
       "pdnPotsPortCpIwfIndex": pdnPotsPortCpIwfIndex,
       "pdnPotsPortHookStatus": pdnPotsPortHookStatus,
       "pdnPotsPortSignalingMethod": pdnPotsPortSignalingMethod,
       "pdnPotsPortTxGain": pdnPotsPortTxGain,
       "pdnPotsPortRxGain": pdnPotsPortRxGain,
       "pdnPotsPortCustInfo": pdnPotsPortCustInfo,
       "pdnPotsPortG729VoiceCodec": pdnPotsPortG729VoiceCodec,
       "pdnPotsPortPreferedVoiceCodec": pdnPotsPortPreferedVoiceCodec,
       "pdnPotsPortPreferredPacketPeriod": pdnPotsPortPreferredPacketPeriod,
       "pdnPotsPortSilenceSuppression": pdnPotsPortSilenceSuppression,
       "pdnPotsPortActualVoiceCodec": pdnPotsPortActualVoiceCodec,
       "pdnPotsPortCallElapsedTime": pdnPotsPortCallElapsedTime,
       "pdnPotsPortModemDetected": pdnPotsPortModemDetected,
       "pdnPotsPortEchoCanceller": pdnPotsPortEchoCanceller,
       "pdnPotsPortLocalEndName": pdnPotsPortLocalEndName,
       "pdnPotsPortActiveSoftswitch": pdnPotsPortActiveSoftswitch,
       "pdnCpIwfTestObjects": pdnCpIwfTestObjects,
       "pdnPotsTestTable": pdnPotsTestTable,
       "pdnPotsTestEntry": pdnPotsTestEntry,
       "pdnPotsTestType": pdnPotsTestType,
       "pdnPotsTestCmd": pdnPotsTestCmd,
       "pdnPotsTestStatus": pdnPotsTestStatus,
       "pdnCpIwfStatsObjects": pdnCpIwfStatsObjects,
       "pdnCpIwfAal2StatsTable": pdnCpIwfAal2StatsTable,
       "pdnCpIwfAal2StatsEntry": pdnCpIwfAal2StatsEntry,
       "pdnCpIwfAal2CpsRxPkts": pdnCpIwfAal2CpsRxPkts,
       "pdnCpIwfAal2CpsTxPkts": pdnCpIwfAal2CpsTxPkts,
       "pdnCpIwfAal2CpsParityErrors": pdnCpIwfAal2CpsParityErrors,
       "pdnCpIwfAal2CpsSeqNumErrors": pdnCpIwfAal2CpsSeqNumErrors,
       "pdnCpIwfAal2CpsOsfMismatchErrors": pdnCpIwfAal2CpsOsfMismatchErrors,
       "pdnCpIwfAal2CpsOsfErrors": pdnCpIwfAal2CpsOsfErrors,
       "pdnCpIwfAal2CpsHecErrors": pdnCpIwfAal2CpsHecErrors,
       "pdnCpIwfAal2CpsOversizeSduErrors": pdnCpIwfAal2CpsOversizeSduErrors,
       "pdnCpIwfAal2CpsReassemblyErrors": pdnCpIwfAal2CpsReassemblyErrors,
       "pdnCpIwfAal2CpsHecOverlapErrors": pdnCpIwfAal2CpsHecOverlapErrors,
       "pdnCpIwfAal2CpsUuiErrors": pdnCpIwfAal2CpsUuiErrors,
       "pdnCpIwfAal2CpsCidErrors": pdnCpIwfAal2CpsCidErrors,
       "pdnPotsPortStatsTable": pdnPotsPortStatsTable,
       "pdnPotsPortStatsEntry": pdnPotsPortStatsEntry,
       "pdnPotsPortTotalCalls": pdnPotsPortTotalCalls,
       "pdnPotsPortTotalCallsFailure": pdnPotsPortTotalCallsFailure,
       "pdnPotsPortTotalCallsDropped": pdnPotsPortTotalCallsDropped,
       "pdnPotsPortInCallsReceived": pdnPotsPortInCallsReceived,
       "pdnPotsPortInCallsAnswered": pdnPotsPortInCallsAnswered,
       "pdnPotsPortInCallsConnected": pdnPotsPortInCallsConnected,
       "pdnPotsPortInCallsFailure": pdnPotsPortInCallsFailure,
       "pdnPotsPortOutCallsAttempted": pdnPotsPortOutCallsAttempted,
       "pdnPotsPortOutCallsAnswered": pdnPotsPortOutCallsAnswered,
       "pdnPotsPortOutCallsConnected": pdnPotsPortOutCallsConnected,
       "pdnPotsPortOutCallsFailure": pdnPotsPortOutCallsFailure,
       "pdnPotsPortPacketsSent": pdnPotsPortPacketsSent,
       "pdnPotsPortPacketsReceived": pdnPotsPortPacketsReceived,
       "pdnPotsPortPacketsLost": pdnPotsPortPacketsLost,
       "pdnPotsPortBytesSent": pdnPotsPortBytesSent,
       "pdnPotsPortBytesReceived": pdnPotsPortBytesReceived,
       "pdnCpIwfMIBConformance": pdnCpIwfMIBConformance,
       "pdnCpIwfMIBCompliances": pdnCpIwfMIBCompliances,
       "pdnCpIwfMIBCompliance": pdnCpIwfMIBCompliance,
       "pdnCpIwfMIBComplianceV2": pdnCpIwfMIBComplianceV2,
       "pdnCpIwfMIBComplianceV3": pdnCpIwfMIBComplianceV3,
       "pdnCpIwfMIBGroups": pdnCpIwfMIBGroups,
       "pdnCpIwfGeneralConfigGroup": pdnCpIwfGeneralConfigGroup,
       "pdnCpIwfPotsPortConfigGroup": pdnCpIwfPotsPortConfigGroup,
       "pdnCpIwfAal2StatsGroup": pdnCpIwfAal2StatsGroup,
       "pdnCpIwfPotsPortStatsGroup": pdnCpIwfPotsPortStatsGroup,
       "pdnCpIwfGeneralConfigGroupV2": pdnCpIwfGeneralConfigGroupV2,
       "pdnCpIwfIADConfigGroupV2": pdnCpIwfIADConfigGroupV2,
       "pdnCpIwfPotsPortStatsGroupV2": pdnCpIwfPotsPortStatsGroupV2,
       "pdnCpIwfPotsPortConfigGroupV2": pdnCpIwfPotsPortConfigGroupV2,
       "pdnCpIwfPotsPortTestGroupV2": pdnCpIwfPotsPortTestGroupV2,
       "pdnCpIwfIADConfigGroupV3": pdnCpIwfIADConfigGroupV3,
       "pdnCpIwfPotsPortPacketStatsGroup": pdnCpIwfPotsPortPacketStatsGroup}
)
