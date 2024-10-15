# SNMP MIB module (WWP-LEOS-PBT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/WWP-LEOS-PBT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:15:01 2024
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
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "RowStatus",
    "TextualConvention",
    "TruthValue")

(wwpLeosVplsEncapTunnelActive,
 wwpLeosVplsEncapTunnelBVID,
 wwpLeosVplsEncapTunnelId,
 wwpLeosVplsEncapTunnelName) = mibBuilder.importSymbols(
    "WWP-LEOS-VPLS-MIB",
    "wwpLeosVplsEncapTunnelActive",
    "wwpLeosVplsEncapTunnelBVID",
    "wwpLeosVplsEncapTunnelId",
    "wwpLeosVplsEncapTunnelName")

(wwpModulesLeos,) = mibBuilder.importSymbols(
    "WWP-SMI",
    "wwpModulesLeos")


# MODULE-IDENTITY

wwpLeosPbtMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 38)
)
wwpLeosPbtMIB.setRevisions(
        ("2011-07-05 00:00",
         "2011-05-05 16:00",
         "2011-01-31 00:00",
         "2007-03-02 17:00",
         "2006-08-25 17:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_WwpLeosPbtMIBObjects_ObjectIdentity = ObjectIdentity
wwpLeosPbtMIBObjects = _WwpLeosPbtMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 38, 1)
)
_WwpLeosPbt_ObjectIdentity = ObjectIdentity
wwpLeosPbt = _WwpLeosPbt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 38, 1, 1)
)
_WwpLeosPbtGlobalAttrs_ObjectIdentity = ObjectIdentity
wwpLeosPbtGlobalAttrs = _WwpLeosPbtGlobalAttrs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 38, 1, 1, 1)
)
_WwpLeosPbtBridgeMac_Type = MacAddress
_WwpLeosPbtBridgeMac_Object = MibScalar
wwpLeosPbtBridgeMac = _WwpLeosPbtBridgeMac_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 38, 1, 1, 1, 1),
    _WwpLeosPbtBridgeMac_Type()
)
wwpLeosPbtBridgeMac.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosPbtBridgeMac.setStatus("current")


class _WwpLeosPbtServiceTagEType_Type(OctetString):
    """Custom type wwpLeosPbtServiceTagEType based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 2),
    )


_WwpLeosPbtServiceTagEType_Type.__name__ = "OctetString"
_WwpLeosPbtServiceTagEType_Object = MibScalar
wwpLeosPbtServiceTagEType = _WwpLeosPbtServiceTagEType_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 38, 1, 1, 1, 2),
    _WwpLeosPbtServiceTagEType_Type()
)
wwpLeosPbtServiceTagEType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosPbtServiceTagEType.setStatus("current")


class _WwpLeosPbtTunnelTagEtype_Type(OctetString):
    """Custom type wwpLeosPbtTunnelTagEtype based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 2),
    )


_WwpLeosPbtTunnelTagEtype_Type.__name__ = "OctetString"
_WwpLeosPbtTunnelTagEtype_Object = MibScalar
wwpLeosPbtTunnelTagEtype = _WwpLeosPbtTunnelTagEtype_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 38, 1, 1, 1, 3),
    _WwpLeosPbtTunnelTagEtype_Type()
)
wwpLeosPbtTunnelTagEtype.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosPbtTunnelTagEtype.setStatus("current")


class _WwpLeosPbtTunnelReversionState_Type(Integer32):
    """Custom type wwpLeosPbtTunnelReversionState based on Integer32"""
    defaultValue = 2

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


_WwpLeosPbtTunnelReversionState_Type.__name__ = "Integer32"
_WwpLeosPbtTunnelReversionState_Object = MibScalar
wwpLeosPbtTunnelReversionState = _WwpLeosPbtTunnelReversionState_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 38, 1, 1, 1, 4),
    _WwpLeosPbtTunnelReversionState_Type()
)
wwpLeosPbtTunnelReversionState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosPbtTunnelReversionState.setStatus("current")


class _WwpLeosPbtTunnelReversionHoldTime_Type(Unsigned32):
    """Custom type wwpLeosPbtTunnelReversionHoldTime based on Unsigned32"""
    defaultValue = 3000


_WwpLeosPbtTunnelReversionHoldTime_Object = MibScalar
wwpLeosPbtTunnelReversionHoldTime = _WwpLeosPbtTunnelReversionHoldTime_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 38, 1, 1, 1, 5),
    _WwpLeosPbtTunnelReversionHoldTime_Type()
)
wwpLeosPbtTunnelReversionHoldTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosPbtTunnelReversionHoldTime.setStatus("current")
if mibBuilder.loadTexts:
    wwpLeosPbtTunnelReversionHoldTime.setUnits("milliseconds")


class _WwpLeosPbtTransitTunnelEtypeRemark_Type(Integer32):
    """Custom type wwpLeosPbtTransitTunnelEtypeRemark based on Integer32"""
    defaultValue = 1

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


_WwpLeosPbtTransitTunnelEtypeRemark_Type.__name__ = "Integer32"
_WwpLeosPbtTransitTunnelEtypeRemark_Object = MibScalar
wwpLeosPbtTransitTunnelEtypeRemark = _WwpLeosPbtTransitTunnelEtypeRemark_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 38, 1, 1, 1, 6),
    _WwpLeosPbtTransitTunnelEtypeRemark_Type()
)
wwpLeosPbtTransitTunnelEtypeRemark.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosPbtTransitTunnelEtypeRemark.setStatus("current")


class _WwpLeosPbtAdminMode_Type(Integer32):
    """Custom type wwpLeosPbtAdminMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("native", 2),
          ("nonNative", 1))
    )


_WwpLeosPbtAdminMode_Type.__name__ = "Integer32"
_WwpLeosPbtAdminMode_Object = MibScalar
wwpLeosPbtAdminMode = _WwpLeosPbtAdminMode_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 38, 1, 1, 1, 7),
    _WwpLeosPbtAdminMode_Type()
)
wwpLeosPbtAdminMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosPbtAdminMode.setStatus("current")


class _WwpLeosPbtOperMode_Type(Integer32):
    """Custom type wwpLeosPbtOperMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("native", 2),
          ("nonNative", 1))
    )


_WwpLeosPbtOperMode_Type.__name__ = "Integer32"
_WwpLeosPbtOperMode_Object = MibScalar
wwpLeosPbtOperMode = _WwpLeosPbtOperMode_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 38, 1, 1, 1, 8),
    _WwpLeosPbtOperMode_Type()
)
wwpLeosPbtOperMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosPbtOperMode.setStatus("current")


class _WwpLeosPbtServiceVlanTpid_Type(OctetString):
    """Custom type wwpLeosPbtServiceVlanTpid based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 2),
    )


_WwpLeosPbtServiceVlanTpid_Type.__name__ = "OctetString"
_WwpLeosPbtServiceVlanTpid_Object = MibScalar
wwpLeosPbtServiceVlanTpid = _WwpLeosPbtServiceVlanTpid_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 38, 1, 1, 1, 9),
    _WwpLeosPbtServiceVlanTpid_Type()
)
wwpLeosPbtServiceVlanTpid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosPbtServiceVlanTpid.setStatus("current")


class _WwpLeosPbtTunnelSwitchOverHoldTime_Type(Unsigned32):
    """Custom type wwpLeosPbtTunnelSwitchOverHoldTime based on Unsigned32"""
    defaultValue = 0


_WwpLeosPbtTunnelSwitchOverHoldTime_Object = MibScalar
wwpLeosPbtTunnelSwitchOverHoldTime = _WwpLeosPbtTunnelSwitchOverHoldTime_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 38, 1, 1, 1, 10),
    _WwpLeosPbtTunnelSwitchOverHoldTime_Type()
)
wwpLeosPbtTunnelSwitchOverHoldTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosPbtTunnelSwitchOverHoldTime.setStatus("current")
if mibBuilder.loadTexts:
    wwpLeosPbtTunnelSwitchOverHoldTime.setUnits("milliseconds")
_WwpLeosPbtBridgeNameMacMapTable_Object = MibTable
wwpLeosPbtBridgeNameMacMapTable = _WwpLeosPbtBridgeNameMacMapTable_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 38, 1, 1, 2)
)
if mibBuilder.loadTexts:
    wwpLeosPbtBridgeNameMacMapTable.setStatus("current")
_WwpLeosPbtBridgeNameMacMapEntry_Object = MibTableRow
wwpLeosPbtBridgeNameMacMapEntry = _WwpLeosPbtBridgeNameMacMapEntry_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 38, 1, 1, 2, 1)
)
wwpLeosPbtBridgeNameMacMapEntry.setIndexNames(
    (0, "WWP-LEOS-PBT-MIB", "wwpLeosPbtBridgeNameMacMapIndex"),
)
if mibBuilder.loadTexts:
    wwpLeosPbtBridgeNameMacMapEntry.setStatus("current")


class _WwpLeosPbtBridgeNameMacMapIndex_Type(Integer32):
    """Custom type wwpLeosPbtBridgeNameMacMapIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_WwpLeosPbtBridgeNameMacMapIndex_Type.__name__ = "Integer32"
_WwpLeosPbtBridgeNameMacMapIndex_Object = MibTableColumn
wwpLeosPbtBridgeNameMacMapIndex = _WwpLeosPbtBridgeNameMacMapIndex_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 38, 1, 1, 2, 1, 1),
    _WwpLeosPbtBridgeNameMacMapIndex_Type()
)
wwpLeosPbtBridgeNameMacMapIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosPbtBridgeNameMacMapIndex.setStatus("current")


class _WwpLeosPbtBridgeNameMacMapBridgeName_Type(DisplayString):
    """Custom type wwpLeosPbtBridgeNameMacMapBridgeName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 15),
    )


_WwpLeosPbtBridgeNameMacMapBridgeName_Type.__name__ = "DisplayString"
_WwpLeosPbtBridgeNameMacMapBridgeName_Object = MibTableColumn
wwpLeosPbtBridgeNameMacMapBridgeName = _WwpLeosPbtBridgeNameMacMapBridgeName_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 38, 1, 1, 2, 1, 2),
    _WwpLeosPbtBridgeNameMacMapBridgeName_Type()
)
wwpLeosPbtBridgeNameMacMapBridgeName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wwpLeosPbtBridgeNameMacMapBridgeName.setStatus("current")
_WwpLeosPbtBridgeNameMacMapMacAddr_Type = MacAddress
_WwpLeosPbtBridgeNameMacMapMacAddr_Object = MibTableColumn
wwpLeosPbtBridgeNameMacMapMacAddr = _WwpLeosPbtBridgeNameMacMapMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 38, 1, 1, 2, 1, 3),
    _WwpLeosPbtBridgeNameMacMapMacAddr_Type()
)
wwpLeosPbtBridgeNameMacMapMacAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wwpLeosPbtBridgeNameMacMapMacAddr.setStatus("current")
_WwpLeosPbtBridgeNameMacMapUseCount_Type = Counter32
_WwpLeosPbtBridgeNameMacMapUseCount_Object = MibTableColumn
wwpLeosPbtBridgeNameMacMapUseCount = _WwpLeosPbtBridgeNameMacMapUseCount_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 38, 1, 1, 2, 1, 4),
    _WwpLeosPbtBridgeNameMacMapUseCount_Type()
)
wwpLeosPbtBridgeNameMacMapUseCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosPbtBridgeNameMacMapUseCount.setStatus("current")
_WwpLeosPbtBridgeNameMacMapRowStatus_Type = RowStatus
_WwpLeosPbtBridgeNameMacMapRowStatus_Object = MibTableColumn
wwpLeosPbtBridgeNameMacMapRowStatus = _WwpLeosPbtBridgeNameMacMapRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 38, 1, 1, 2, 1, 5),
    _WwpLeosPbtBridgeNameMacMapRowStatus_Type()
)
wwpLeosPbtBridgeNameMacMapRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wwpLeosPbtBridgeNameMacMapRowStatus.setStatus("current")
_WwpLeosPbtReservedBVIDTable_Object = MibTable
wwpLeosPbtReservedBVIDTable = _WwpLeosPbtReservedBVIDTable_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 38, 1, 1, 3)
)
if mibBuilder.loadTexts:
    wwpLeosPbtReservedBVIDTable.setStatus("current")
_WwpLeosPbtReservedBVIDEntry_Object = MibTableRow
wwpLeosPbtReservedBVIDEntry = _WwpLeosPbtReservedBVIDEntry_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 38, 1, 1, 3, 1)
)
wwpLeosPbtReservedBVIDEntry.setIndexNames(
    (0, "WWP-LEOS-PBT-MIB", "wwpLeosPbtReservedBVID"),
)
if mibBuilder.loadTexts:
    wwpLeosPbtReservedBVIDEntry.setStatus("current")


class _WwpLeosPbtReservedBVID_Type(Integer32):
    """Custom type wwpLeosPbtReservedBVID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 4094),
    )


_WwpLeosPbtReservedBVID_Type.__name__ = "Integer32"
_WwpLeosPbtReservedBVID_Object = MibTableColumn
wwpLeosPbtReservedBVID = _WwpLeosPbtReservedBVID_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 38, 1, 1, 3, 1, 1),
    _WwpLeosPbtReservedBVID_Type()
)
wwpLeosPbtReservedBVID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosPbtReservedBVID.setStatus("current")
_WwpLeosPbtReservedBVIDRowStatus_Type = RowStatus
_WwpLeosPbtReservedBVIDRowStatus_Object = MibTableColumn
wwpLeosPbtReservedBVIDRowStatus = _WwpLeosPbtReservedBVIDRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 38, 1, 1, 3, 1, 2),
    _WwpLeosPbtReservedBVIDRowStatus_Type()
)
wwpLeosPbtReservedBVIDRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wwpLeosPbtReservedBVIDRowStatus.setStatus("current")
_WwpLeosPbtVirtualCircuitTable_Object = MibTable
wwpLeosPbtVirtualCircuitTable = _WwpLeosPbtVirtualCircuitTable_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 38, 1, 1, 4)
)
if mibBuilder.loadTexts:
    wwpLeosPbtVirtualCircuitTable.setStatus("current")
_WwpLeosPbtVirtualCircuitEntry_Object = MibTableRow
wwpLeosPbtVirtualCircuitEntry = _WwpLeosPbtVirtualCircuitEntry_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 38, 1, 1, 4, 1)
)
wwpLeosPbtVirtualCircuitEntry.setIndexNames(
    (0, "WWP-LEOS-PBT-MIB", "wwpLeosPbtVirtualCircuitIndex"),
)
if mibBuilder.loadTexts:
    wwpLeosPbtVirtualCircuitEntry.setStatus("current")


class _WwpLeosPbtVirtualCircuitIndex_Type(Integer32):
    """Custom type wwpLeosPbtVirtualCircuitIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_WwpLeosPbtVirtualCircuitIndex_Type.__name__ = "Integer32"
_WwpLeosPbtVirtualCircuitIndex_Object = MibTableColumn
wwpLeosPbtVirtualCircuitIndex = _WwpLeosPbtVirtualCircuitIndex_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 38, 1, 1, 4, 1, 1),
    _WwpLeosPbtVirtualCircuitIndex_Type()
)
wwpLeosPbtVirtualCircuitIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosPbtVirtualCircuitIndex.setStatus("current")


class _WwpLeosPbtVirtualCircuitName_Type(DisplayString):
    """Custom type wwpLeosPbtVirtualCircuitName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 15),
    )


_WwpLeosPbtVirtualCircuitName_Type.__name__ = "DisplayString"
_WwpLeosPbtVirtualCircuitName_Object = MibTableColumn
wwpLeosPbtVirtualCircuitName = _WwpLeosPbtVirtualCircuitName_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 38, 1, 1, 4, 1, 2),
    _WwpLeosPbtVirtualCircuitName_Type()
)
wwpLeosPbtVirtualCircuitName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wwpLeosPbtVirtualCircuitName.setStatus("current")
_WwpLeosPbtVirtualCircuitFixedEncapTunnelId_Type = Integer32
_WwpLeosPbtVirtualCircuitFixedEncapTunnelId_Object = MibTableColumn
wwpLeosPbtVirtualCircuitFixedEncapTunnelId = _WwpLeosPbtVirtualCircuitFixedEncapTunnelId_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 38, 1, 1, 4, 1, 3),
    _WwpLeosPbtVirtualCircuitFixedEncapTunnelId_Type()
)
wwpLeosPbtVirtualCircuitFixedEncapTunnelId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wwpLeosPbtVirtualCircuitFixedEncapTunnelId.setStatus("current")


class _WwpLeosPbtVirtualCircuitDestBridgeIndex_Type(Integer32):
    """Custom type wwpLeosPbtVirtualCircuitDestBridgeIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 64),
    )


_WwpLeosPbtVirtualCircuitDestBridgeIndex_Type.__name__ = "Integer32"
_WwpLeosPbtVirtualCircuitDestBridgeIndex_Object = MibTableColumn
wwpLeosPbtVirtualCircuitDestBridgeIndex = _WwpLeosPbtVirtualCircuitDestBridgeIndex_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 38, 1, 1, 4, 1, 4),
    _WwpLeosPbtVirtualCircuitDestBridgeIndex_Type()
)
wwpLeosPbtVirtualCircuitDestBridgeIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wwpLeosPbtVirtualCircuitDestBridgeIndex.setStatus("current")


class _WwpLeosPbtVirtualCircuitIngressISID_Type(Integer32):
    """Custom type wwpLeosPbtVirtualCircuitIngressISID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16777215),
    )


_WwpLeosPbtVirtualCircuitIngressISID_Type.__name__ = "Integer32"
_WwpLeosPbtVirtualCircuitIngressISID_Object = MibTableColumn
wwpLeosPbtVirtualCircuitIngressISID = _WwpLeosPbtVirtualCircuitIngressISID_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 38, 1, 1, 4, 1, 5),
    _WwpLeosPbtVirtualCircuitIngressISID_Type()
)
wwpLeosPbtVirtualCircuitIngressISID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wwpLeosPbtVirtualCircuitIngressISID.setStatus("current")


class _WwpLeosPbtVirtualCircuitEgressISID_Type(Integer32):
    """Custom type wwpLeosPbtVirtualCircuitEgressISID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16777215),
    )


_WwpLeosPbtVirtualCircuitEgressISID_Type.__name__ = "Integer32"
_WwpLeosPbtVirtualCircuitEgressISID_Object = MibTableColumn
wwpLeosPbtVirtualCircuitEgressISID = _WwpLeosPbtVirtualCircuitEgressISID_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 38, 1, 1, 4, 1, 6),
    _WwpLeosPbtVirtualCircuitEgressISID_Type()
)
wwpLeosPbtVirtualCircuitEgressISID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wwpLeosPbtVirtualCircuitEgressISID.setStatus("current")


class _WwpLeosPbtVirtualCircuitOperState_Type(Integer32):
    """Custom type wwpLeosPbtVirtualCircuitOperState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_WwpLeosPbtVirtualCircuitOperState_Type.__name__ = "Integer32"
_WwpLeosPbtVirtualCircuitOperState_Object = MibTableColumn
wwpLeosPbtVirtualCircuitOperState = _WwpLeosPbtVirtualCircuitOperState_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 38, 1, 1, 4, 1, 7),
    _WwpLeosPbtVirtualCircuitOperState_Type()
)
wwpLeosPbtVirtualCircuitOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosPbtVirtualCircuitOperState.setStatus("current")
_WwpLeosPbtVirtualCircuitEncapTunnelIdInUse_Type = Integer32
_WwpLeosPbtVirtualCircuitEncapTunnelIdInUse_Object = MibTableColumn
wwpLeosPbtVirtualCircuitEncapTunnelIdInUse = _WwpLeosPbtVirtualCircuitEncapTunnelIdInUse_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 38, 1, 1, 4, 1, 8),
    _WwpLeosPbtVirtualCircuitEncapTunnelIdInUse_Type()
)
wwpLeosPbtVirtualCircuitEncapTunnelIdInUse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosPbtVirtualCircuitEncapTunnelIdInUse.setStatus("current")
_WwpLeosPbtVirtualCircuitRowStatus_Type = RowStatus
_WwpLeosPbtVirtualCircuitRowStatus_Object = MibTableColumn
wwpLeosPbtVirtualCircuitRowStatus = _WwpLeosPbtVirtualCircuitRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 38, 1, 1, 4, 1, 9),
    _WwpLeosPbtVirtualCircuitRowStatus_Type()
)
wwpLeosPbtVirtualCircuitRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wwpLeosPbtVirtualCircuitRowStatus.setStatus("current")
_WwpLeosPbtVirtualCircuitRetainSTAG_Type = TruthValue
_WwpLeosPbtVirtualCircuitRetainSTAG_Object = MibTableColumn
wwpLeosPbtVirtualCircuitRetainSTAG = _WwpLeosPbtVirtualCircuitRetainSTAG_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 38, 1, 1, 4, 1, 10),
    _WwpLeosPbtVirtualCircuitRetainSTAG_Type()
)
wwpLeosPbtVirtualCircuitRetainSTAG.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wwpLeosPbtVirtualCircuitRetainSTAG.setStatus("current")
_WwpLeosPbtVirtualCircuitStag_Type = Integer32
_WwpLeosPbtVirtualCircuitStag_Object = MibTableColumn
wwpLeosPbtVirtualCircuitStag = _WwpLeosPbtVirtualCircuitStag_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 38, 1, 1, 4, 1, 11),
    _WwpLeosPbtVirtualCircuitStag_Type()
)
wwpLeosPbtVirtualCircuitStag.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wwpLeosPbtVirtualCircuitStag.setStatus("current")
_WwpLeosPbtVirtualCircuitStatsTable_Object = MibTable
wwpLeosPbtVirtualCircuitStatsTable = _WwpLeosPbtVirtualCircuitStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 38, 1, 1, 5)
)
if mibBuilder.loadTexts:
    wwpLeosPbtVirtualCircuitStatsTable.setStatus("current")
_WwpLeosPbtVirtualCircuitStatsEntry_Object = MibTableRow
wwpLeosPbtVirtualCircuitStatsEntry = _WwpLeosPbtVirtualCircuitStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 38, 1, 1, 5, 1)
)
wwpLeosPbtVirtualCircuitStatsEntry.setIndexNames(
    (0, "WWP-LEOS-PBT-MIB", "wwpLeosPbtVirtualCircuitIndex"),
)
if mibBuilder.loadTexts:
    wwpLeosPbtVirtualCircuitStatsEntry.setStatus("current")
_WwpLeosPbtVirtualCircuitTxBytesHi_Type = Counter32
_WwpLeosPbtVirtualCircuitTxBytesHi_Object = MibTableColumn
wwpLeosPbtVirtualCircuitTxBytesHi = _WwpLeosPbtVirtualCircuitTxBytesHi_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 38, 1, 1, 5, 1, 1),
    _WwpLeosPbtVirtualCircuitTxBytesHi_Type()
)
wwpLeosPbtVirtualCircuitTxBytesHi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosPbtVirtualCircuitTxBytesHi.setStatus("current")
_WwpLeosPbtVirtualCircuitTxBytesLo_Type = Counter32
_WwpLeosPbtVirtualCircuitTxBytesLo_Object = MibTableColumn
wwpLeosPbtVirtualCircuitTxBytesLo = _WwpLeosPbtVirtualCircuitTxBytesLo_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 38, 1, 1, 5, 1, 2),
    _WwpLeosPbtVirtualCircuitTxBytesLo_Type()
)
wwpLeosPbtVirtualCircuitTxBytesLo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosPbtVirtualCircuitTxBytesLo.setStatus("current")
_WwpLeosPbtVirtualCircuitRxBytesHi_Type = Counter32
_WwpLeosPbtVirtualCircuitRxBytesHi_Object = MibTableColumn
wwpLeosPbtVirtualCircuitRxBytesHi = _WwpLeosPbtVirtualCircuitRxBytesHi_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 38, 1, 1, 5, 1, 3),
    _WwpLeosPbtVirtualCircuitRxBytesHi_Type()
)
wwpLeosPbtVirtualCircuitRxBytesHi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosPbtVirtualCircuitRxBytesHi.setStatus("current")
_WwpLeosPbtVirtualCircuitRxBytesLo_Type = Counter32
_WwpLeosPbtVirtualCircuitRxBytesLo_Object = MibTableColumn
wwpLeosPbtVirtualCircuitRxBytesLo = _WwpLeosPbtVirtualCircuitRxBytesLo_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 38, 1, 1, 5, 1, 4),
    _WwpLeosPbtVirtualCircuitRxBytesLo_Type()
)
wwpLeosPbtVirtualCircuitRxBytesLo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosPbtVirtualCircuitRxBytesLo.setStatus("current")
_WwpLeosPbtLocalBridgeNameMacMapTable_Object = MibTable
wwpLeosPbtLocalBridgeNameMacMapTable = _WwpLeosPbtLocalBridgeNameMacMapTable_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 38, 1, 1, 6)
)
if mibBuilder.loadTexts:
    wwpLeosPbtLocalBridgeNameMacMapTable.setStatus("current")
_WwpLeosPbtLocalBridgeNameMacMapEntry_Object = MibTableRow
wwpLeosPbtLocalBridgeNameMacMapEntry = _WwpLeosPbtLocalBridgeNameMacMapEntry_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 38, 1, 1, 6, 1)
)
wwpLeosPbtLocalBridgeNameMacMapEntry.setIndexNames(
    (0, "WWP-LEOS-PBT-MIB", "wwpLeosPbtLocalBridgeNameMacMapIndex"),
)
if mibBuilder.loadTexts:
    wwpLeosPbtLocalBridgeNameMacMapEntry.setStatus("current")


class _WwpLeosPbtLocalBridgeNameMacMapIndex_Type(Integer32):
    """Custom type wwpLeosPbtLocalBridgeNameMacMapIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_WwpLeosPbtLocalBridgeNameMacMapIndex_Type.__name__ = "Integer32"
_WwpLeosPbtLocalBridgeNameMacMapIndex_Object = MibTableColumn
wwpLeosPbtLocalBridgeNameMacMapIndex = _WwpLeosPbtLocalBridgeNameMacMapIndex_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 38, 1, 1, 6, 1, 1),
    _WwpLeosPbtLocalBridgeNameMacMapIndex_Type()
)
wwpLeosPbtLocalBridgeNameMacMapIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosPbtLocalBridgeNameMacMapIndex.setStatus("current")


class _WwpLeosPbtLocalBridgeNameMacMapBridgeName_Type(DisplayString):
    """Custom type wwpLeosPbtLocalBridgeNameMacMapBridgeName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 15),
    )


_WwpLeosPbtLocalBridgeNameMacMapBridgeName_Type.__name__ = "DisplayString"
_WwpLeosPbtLocalBridgeNameMacMapBridgeName_Object = MibTableColumn
wwpLeosPbtLocalBridgeNameMacMapBridgeName = _WwpLeosPbtLocalBridgeNameMacMapBridgeName_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 38, 1, 1, 6, 1, 2),
    _WwpLeosPbtLocalBridgeNameMacMapBridgeName_Type()
)
wwpLeosPbtLocalBridgeNameMacMapBridgeName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wwpLeosPbtLocalBridgeNameMacMapBridgeName.setStatus("current")
_WwpLeosPbtLocalBridgeNameMacMapMacAddr_Type = MacAddress
_WwpLeosPbtLocalBridgeNameMacMapMacAddr_Object = MibTableColumn
wwpLeosPbtLocalBridgeNameMacMapMacAddr = _WwpLeosPbtLocalBridgeNameMacMapMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 38, 1, 1, 6, 1, 3),
    _WwpLeosPbtLocalBridgeNameMacMapMacAddr_Type()
)
wwpLeosPbtLocalBridgeNameMacMapMacAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosPbtLocalBridgeNameMacMapMacAddr.setStatus("current")
_WwpLeosPbtLocalBridgeNameMacMapUseCount_Type = Counter32
_WwpLeosPbtLocalBridgeNameMacMapUseCount_Object = MibTableColumn
wwpLeosPbtLocalBridgeNameMacMapUseCount = _WwpLeosPbtLocalBridgeNameMacMapUseCount_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 38, 1, 1, 6, 1, 4),
    _WwpLeosPbtLocalBridgeNameMacMapUseCount_Type()
)
wwpLeosPbtLocalBridgeNameMacMapUseCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosPbtLocalBridgeNameMacMapUseCount.setStatus("current")
_WwpLeosPbtLocalBridgeNameMacMapRowStatus_Type = RowStatus
_WwpLeosPbtLocalBridgeNameMacMapRowStatus_Object = MibTableColumn
wwpLeosPbtLocalBridgeNameMacMapRowStatus = _WwpLeosPbtLocalBridgeNameMacMapRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 38, 1, 1, 6, 1, 5),
    _WwpLeosPbtLocalBridgeNameMacMapRowStatus_Type()
)
wwpLeosPbtLocalBridgeNameMacMapRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wwpLeosPbtLocalBridgeNameMacMapRowStatus.setStatus("current")
_WwpLeosTcePbt_ObjectIdentity = ObjectIdentity
wwpLeosTcePbt = _WwpLeosTcePbt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 38, 1, 1, 10)
)
_WwpLeosTcePbtServiceTable_Object = MibTable
wwpLeosTcePbtServiceTable = _WwpLeosTcePbtServiceTable_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 38, 1, 1, 10, 1)
)
if mibBuilder.loadTexts:
    wwpLeosTcePbtServiceTable.setStatus("current")
_WwpLeosTcePbtServiceEntry_Object = MibTableRow
wwpLeosTcePbtServiceEntry = _WwpLeosTcePbtServiceEntry_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 38, 1, 1, 10, 1, 1)
)
wwpLeosTcePbtServiceEntry.setIndexNames(
    (0, "WWP-LEOS-PBT-MIB", "wwpLeosTcePbtServiceIndex"),
)
if mibBuilder.loadTexts:
    wwpLeosTcePbtServiceEntry.setStatus("current")
_WwpLeosTcePbtServiceIndex_Type = Unsigned32
_WwpLeosTcePbtServiceIndex_Object = MibTableColumn
wwpLeosTcePbtServiceIndex = _WwpLeosTcePbtServiceIndex_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 38, 1, 1, 10, 1, 1, 1),
    _WwpLeosTcePbtServiceIndex_Type()
)
wwpLeosTcePbtServiceIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wwpLeosTcePbtServiceIndex.setStatus("current")


class _WwpLeosTcePbtServiceName_Type(DisplayString):
    """Custom type wwpLeosTcePbtServiceName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_WwpLeosTcePbtServiceName_Type.__name__ = "DisplayString"
_WwpLeosTcePbtServiceName_Object = MibTableColumn
wwpLeosTcePbtServiceName = _WwpLeosTcePbtServiceName_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 38, 1, 1, 10, 1, 1, 2),
    _WwpLeosTcePbtServiceName_Type()
)
wwpLeosTcePbtServiceName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wwpLeosTcePbtServiceName.setStatus("current")


class _WwpLeosTcePbtServiceOperStatus_Type(Integer32):
    """Custom type wwpLeosTcePbtServiceOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_WwpLeosTcePbtServiceOperStatus_Type.__name__ = "Integer32"
_WwpLeosTcePbtServiceOperStatus_Object = MibTableColumn
wwpLeosTcePbtServiceOperStatus = _WwpLeosTcePbtServiceOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 38, 1, 1, 10, 1, 1, 3),
    _WwpLeosTcePbtServiceOperStatus_Type()
)
wwpLeosTcePbtServiceOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosTcePbtServiceOperStatus.setStatus("current")


class _WwpLeosTcePbtServiceFloodContProfileId_Type(Integer32):
    """Custom type wwpLeosTcePbtServiceFloodContProfileId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_WwpLeosTcePbtServiceFloodContProfileId_Type.__name__ = "Integer32"
_WwpLeosTcePbtServiceFloodContProfileId_Object = MibTableColumn
wwpLeosTcePbtServiceFloodContProfileId = _WwpLeosTcePbtServiceFloodContProfileId_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 38, 1, 1, 10, 1, 1, 4),
    _WwpLeosTcePbtServiceFloodContProfileId_Type()
)
wwpLeosTcePbtServiceFloodContProfileId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wwpLeosTcePbtServiceFloodContProfileId.setStatus("current")


class _WwpLeosTcePbtServiceFloodContProfileName_Type(DisplayString):
    """Custom type wwpLeosTcePbtServiceFloodContProfileName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_WwpLeosTcePbtServiceFloodContProfileName_Type.__name__ = "DisplayString"
_WwpLeosTcePbtServiceFloodContProfileName_Object = MibTableColumn
wwpLeosTcePbtServiceFloodContProfileName = _WwpLeosTcePbtServiceFloodContProfileName_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 38, 1, 1, 10, 1, 1, 5),
    _WwpLeosTcePbtServiceFloodContProfileName_Type()
)
wwpLeosTcePbtServiceFloodContProfileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosTcePbtServiceFloodContProfileName.setStatus("current")
_WwpLeosTcePbtServiceVsIndex_Type = Unsigned32
_WwpLeosTcePbtServiceVsIndex_Object = MibTableColumn
wwpLeosTcePbtServiceVsIndex = _WwpLeosTcePbtServiceVsIndex_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 38, 1, 1, 10, 1, 1, 6),
    _WwpLeosTcePbtServiceVsIndex_Type()
)
wwpLeosTcePbtServiceVsIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wwpLeosTcePbtServiceVsIndex.setStatus("current")


class _WwpLeosTcePbtServiceVsName_Type(DisplayString):
    """Custom type wwpLeosTcePbtServiceVsName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_WwpLeosTcePbtServiceVsName_Type.__name__ = "DisplayString"
_WwpLeosTcePbtServiceVsName_Object = MibTableColumn
wwpLeosTcePbtServiceVsName = _WwpLeosTcePbtServiceVsName_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 38, 1, 1, 10, 1, 1, 7),
    _WwpLeosTcePbtServiceVsName_Type()
)
wwpLeosTcePbtServiceVsName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosTcePbtServiceVsName.setStatus("current")
_WwpLeosTcePbtServiceTnlGroupIndex_Type = Unsigned32
_WwpLeosTcePbtServiceTnlGroupIndex_Object = MibTableColumn
wwpLeosTcePbtServiceTnlGroupIndex = _WwpLeosTcePbtServiceTnlGroupIndex_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 38, 1, 1, 10, 1, 1, 8),
    _WwpLeosTcePbtServiceTnlGroupIndex_Type()
)
wwpLeosTcePbtServiceTnlGroupIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wwpLeosTcePbtServiceTnlGroupIndex.setStatus("current")


class _WwpLeosTcePbtServiceTnlGroupName_Type(DisplayString):
    """Custom type wwpLeosTcePbtServiceTnlGroupName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_WwpLeosTcePbtServiceTnlGroupName_Type.__name__ = "DisplayString"
_WwpLeosTcePbtServiceTnlGroupName_Object = MibTableColumn
wwpLeosTcePbtServiceTnlGroupName = _WwpLeosTcePbtServiceTnlGroupName_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 38, 1, 1, 10, 1, 1, 9),
    _WwpLeosTcePbtServiceTnlGroupName_Type()
)
wwpLeosTcePbtServiceTnlGroupName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosTcePbtServiceTnlGroupName.setStatus("current")
_WwpLeosTcePbtServiceIngressIsId_Type = Unsigned32
_WwpLeosTcePbtServiceIngressIsId_Object = MibTableColumn
wwpLeosTcePbtServiceIngressIsId = _WwpLeosTcePbtServiceIngressIsId_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 38, 1, 1, 10, 1, 1, 10),
    _WwpLeosTcePbtServiceIngressIsId_Type()
)
wwpLeosTcePbtServiceIngressIsId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wwpLeosTcePbtServiceIngressIsId.setStatus("current")
_WwpLeosTcePbtServiceEgressIsId_Type = Unsigned32
_WwpLeosTcePbtServiceEgressIsId_Object = MibTableColumn
wwpLeosTcePbtServiceEgressIsId = _WwpLeosTcePbtServiceEgressIsId_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 38, 1, 1, 10, 1, 1, 11),
    _WwpLeosTcePbtServiceEgressIsId_Type()
)
wwpLeosTcePbtServiceEgressIsId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wwpLeosTcePbtServiceEgressIsId.setStatus("current")


class _WwpLeosTcePbtServiceFixedEgressPcp_Type(Integer32):
    """Custom type wwpLeosTcePbtServiceFixedEgressPcp based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_WwpLeosTcePbtServiceFixedEgressPcp_Type.__name__ = "Integer32"
_WwpLeosTcePbtServiceFixedEgressPcp_Object = MibTableColumn
wwpLeosTcePbtServiceFixedEgressPcp = _WwpLeosTcePbtServiceFixedEgressPcp_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 38, 1, 1, 10, 1, 1, 12),
    _WwpLeosTcePbtServiceFixedEgressPcp_Type()
)
wwpLeosTcePbtServiceFixedEgressPcp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wwpLeosTcePbtServiceFixedEgressPcp.setStatus("current")


class _WwpLeosTcePbtServiceFrameCosPolicy_Type(Integer32):
    """Custom type wwpLeosTcePbtServiceFrameCosPolicy based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("fixed", 1),
          ("isidPcPMap", 2))
    )


_WwpLeosTcePbtServiceFrameCosPolicy_Type.__name__ = "Integer32"
_WwpLeosTcePbtServiceFrameCosPolicy_Object = MibTableColumn
wwpLeosTcePbtServiceFrameCosPolicy = _WwpLeosTcePbtServiceFrameCosPolicy_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 38, 1, 1, 10, 1, 1, 13),
    _WwpLeosTcePbtServiceFrameCosPolicy_Type()
)
wwpLeosTcePbtServiceFrameCosPolicy.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wwpLeosTcePbtServiceFrameCosPolicy.setStatus("current")


class _WwpLeosTcePbtServiceFrameCosMapIndex_Type(Integer32):
    """Custom type wwpLeosTcePbtServiceFrameCosMapIndex based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_WwpLeosTcePbtServiceFrameCosMapIndex_Type.__name__ = "Integer32"
_WwpLeosTcePbtServiceFrameCosMapIndex_Object = MibTableColumn
wwpLeosTcePbtServiceFrameCosMapIndex = _WwpLeosTcePbtServiceFrameCosMapIndex_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 38, 1, 1, 10, 1, 1, 14),
    _WwpLeosTcePbtServiceFrameCosMapIndex_Type()
)
wwpLeosTcePbtServiceFrameCosMapIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wwpLeosTcePbtServiceFrameCosMapIndex.setStatus("current")


class _WwpLeosTcePbtServiceFrameCosMapName_Type(DisplayString):
    """Custom type wwpLeosTcePbtServiceFrameCosMapName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_WwpLeosTcePbtServiceFrameCosMapName_Type.__name__ = "DisplayString"
_WwpLeosTcePbtServiceFrameCosMapName_Object = MibTableColumn
wwpLeosTcePbtServiceFrameCosMapName = _WwpLeosTcePbtServiceFrameCosMapName_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 38, 1, 1, 10, 1, 1, 15),
    _WwpLeosTcePbtServiceFrameCosMapName_Type()
)
wwpLeosTcePbtServiceFrameCosMapName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosTcePbtServiceFrameCosMapName.setStatus("current")


class _WwpLeosTcePbtServiceResolvedCosPolicy_Type(Integer32):
    """Custom type wwpLeosTcePbtServiceResolvedCosPolicy based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("fixed", 2),
          ("ignore", 1),
          ("isidPcpMap", 3))
    )


_WwpLeosTcePbtServiceResolvedCosPolicy_Type.__name__ = "Integer32"
_WwpLeosTcePbtServiceResolvedCosPolicy_Object = MibTableColumn
wwpLeosTcePbtServiceResolvedCosPolicy = _WwpLeosTcePbtServiceResolvedCosPolicy_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 38, 1, 1, 10, 1, 1, 16),
    _WwpLeosTcePbtServiceResolvedCosPolicy_Type()
)
wwpLeosTcePbtServiceResolvedCosPolicy.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wwpLeosTcePbtServiceResolvedCosPolicy.setStatus("current")


class _WwpLeosTcePbtServiceResolvedCosProfileIndex_Type(Integer32):
    """Custom type wwpLeosTcePbtServiceResolvedCosProfileIndex based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_WwpLeosTcePbtServiceResolvedCosProfileIndex_Type.__name__ = "Integer32"
_WwpLeosTcePbtServiceResolvedCosProfileIndex_Object = MibTableColumn
wwpLeosTcePbtServiceResolvedCosProfileIndex = _WwpLeosTcePbtServiceResolvedCosProfileIndex_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 38, 1, 1, 10, 1, 1, 17),
    _WwpLeosTcePbtServiceResolvedCosProfileIndex_Type()
)
wwpLeosTcePbtServiceResolvedCosProfileIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wwpLeosTcePbtServiceResolvedCosProfileIndex.setStatus("current")


class _WwpLeosTcePbtServiceResolvedCosProfileName_Type(DisplayString):
    """Custom type wwpLeosTcePbtServiceResolvedCosProfileName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_WwpLeosTcePbtServiceResolvedCosProfileName_Type.__name__ = "DisplayString"
_WwpLeosTcePbtServiceResolvedCosProfileName_Object = MibTableColumn
wwpLeosTcePbtServiceResolvedCosProfileName = _WwpLeosTcePbtServiceResolvedCosProfileName_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 38, 1, 1, 10, 1, 1, 18),
    _WwpLeosTcePbtServiceResolvedCosProfileName_Type()
)
wwpLeosTcePbtServiceResolvedCosProfileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosTcePbtServiceResolvedCosProfileName.setStatus("current")


class _WwpLeosTcePbtServiceIngressMeterProfileId_Type(Integer32):
    """Custom type wwpLeosTcePbtServiceIngressMeterProfileId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_WwpLeosTcePbtServiceIngressMeterProfileId_Type.__name__ = "Integer32"
_WwpLeosTcePbtServiceIngressMeterProfileId_Object = MibTableColumn
wwpLeosTcePbtServiceIngressMeterProfileId = _WwpLeosTcePbtServiceIngressMeterProfileId_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 38, 1, 1, 10, 1, 1, 19),
    _WwpLeosTcePbtServiceIngressMeterProfileId_Type()
)
wwpLeosTcePbtServiceIngressMeterProfileId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wwpLeosTcePbtServiceIngressMeterProfileId.setStatus("current")
_WwpLeosTcePbtServiceIngressMeterProfileName_Type = DisplayString
_WwpLeosTcePbtServiceIngressMeterProfileName_Object = MibTableColumn
wwpLeosTcePbtServiceIngressMeterProfileName = _WwpLeosTcePbtServiceIngressMeterProfileName_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 38, 1, 1, 10, 1, 1, 20),
    _WwpLeosTcePbtServiceIngressMeterProfileName_Type()
)
wwpLeosTcePbtServiceIngressMeterProfileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosTcePbtServiceIngressMeterProfileName.setStatus("current")


class _WwpLeosTcePbtServiceIngressMeterPolicy_Type(Integer32):
    """Custom type wwpLeosTcePbtServiceIngressMeterPolicy based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("hierarchical", 2),
          ("nonhierarchical", 1))
    )


_WwpLeosTcePbtServiceIngressMeterPolicy_Type.__name__ = "Integer32"
_WwpLeosTcePbtServiceIngressMeterPolicy_Object = MibTableColumn
wwpLeosTcePbtServiceIngressMeterPolicy = _WwpLeosTcePbtServiceIngressMeterPolicy_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 38, 1, 1, 10, 1, 1, 21),
    _WwpLeosTcePbtServiceIngressMeterPolicy_Type()
)
wwpLeosTcePbtServiceIngressMeterPolicy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosTcePbtServiceIngressMeterPolicy.setStatus("current")
_WwpLeosTcePbtServiceRowStatus_Type = RowStatus
_WwpLeosTcePbtServiceRowStatus_Object = MibTableColumn
wwpLeosTcePbtServiceRowStatus = _WwpLeosTcePbtServiceRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 38, 1, 1, 10, 1, 1, 64),
    _WwpLeosTcePbtServiceRowStatus_Type()
)
wwpLeosTcePbtServiceRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wwpLeosTcePbtServiceRowStatus.setStatus("current")
_WwpLeosTcePbtTnlGroupTable_Object = MibTable
wwpLeosTcePbtTnlGroupTable = _WwpLeosTcePbtTnlGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 38, 1, 1, 10, 5)
)
if mibBuilder.loadTexts:
    wwpLeosTcePbtTnlGroupTable.setStatus("current")
_WwpLeosTcePbtTnlGroupEntry_Object = MibTableRow
wwpLeosTcePbtTnlGroupEntry = _WwpLeosTcePbtTnlGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 38, 1, 1, 10, 5, 1)
)
wwpLeosTcePbtTnlGroupEntry.setIndexNames(
    (0, "WWP-LEOS-PBT-MIB", "wwpLeosTcePbtTnlGroupIndex"),
)
if mibBuilder.loadTexts:
    wwpLeosTcePbtTnlGroupEntry.setStatus("current")
_WwpLeosTcePbtTnlGroupIndex_Type = Unsigned32
_WwpLeosTcePbtTnlGroupIndex_Object = MibTableColumn
wwpLeosTcePbtTnlGroupIndex = _WwpLeosTcePbtTnlGroupIndex_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 38, 1, 1, 10, 5, 1, 1),
    _WwpLeosTcePbtTnlGroupIndex_Type()
)
wwpLeosTcePbtTnlGroupIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    wwpLeosTcePbtTnlGroupIndex.setStatus("current")


class _WwpLeosTcePbtTnlGroupName_Type(DisplayString):
    """Custom type wwpLeosTcePbtTnlGroupName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_WwpLeosTcePbtTnlGroupName_Type.__name__ = "DisplayString"
_WwpLeosTcePbtTnlGroupName_Object = MibTableColumn
wwpLeosTcePbtTnlGroupName = _WwpLeosTcePbtTnlGroupName_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 38, 1, 1, 10, 5, 1, 2),
    _WwpLeosTcePbtTnlGroupName_Type()
)
wwpLeosTcePbtTnlGroupName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wwpLeosTcePbtTnlGroupName.setStatus("current")


class _WwpLeosTcePbtTnlGroupSyncEnabled_Type(TruthValue):
    """Custom type wwpLeosTcePbtTnlGroupSyncEnabled based on TruthValue"""


_WwpLeosTcePbtTnlGroupSyncEnabled_Object = MibTableColumn
wwpLeosTcePbtTnlGroupSyncEnabled = _WwpLeosTcePbtTnlGroupSyncEnabled_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 38, 1, 1, 10, 5, 1, 3),
    _WwpLeosTcePbtTnlGroupSyncEnabled_Type()
)
wwpLeosTcePbtTnlGroupSyncEnabled.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wwpLeosTcePbtTnlGroupSyncEnabled.setStatus("current")


class _WwpLeosTcePbtTnlGroupOperStatus_Type(Integer32):
    """Custom type wwpLeosTcePbtTnlGroupOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_WwpLeosTcePbtTnlGroupOperStatus_Type.__name__ = "Integer32"
_WwpLeosTcePbtTnlGroupOperStatus_Object = MibTableColumn
wwpLeosTcePbtTnlGroupOperStatus = _WwpLeosTcePbtTnlGroupOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 38, 1, 1, 10, 5, 1, 4),
    _WwpLeosTcePbtTnlGroupOperStatus_Type()
)
wwpLeosTcePbtTnlGroupOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosTcePbtTnlGroupOperStatus.setStatus("current")
_WwpLeosTcePbtTnlGroupUseCount_Type = Unsigned32
_WwpLeosTcePbtTnlGroupUseCount_Object = MibTableColumn
wwpLeosTcePbtTnlGroupUseCount = _WwpLeosTcePbtTnlGroupUseCount_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 38, 1, 1, 10, 5, 1, 5),
    _WwpLeosTcePbtTnlGroupUseCount_Type()
)
wwpLeosTcePbtTnlGroupUseCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosTcePbtTnlGroupUseCount.setStatus("current")
_WwpLeosTcePbtTnlGroupActivePair_Type = Unsigned32
_WwpLeosTcePbtTnlGroupActivePair_Object = MibTableColumn
wwpLeosTcePbtTnlGroupActivePair = _WwpLeosTcePbtTnlGroupActivePair_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 38, 1, 1, 10, 5, 1, 6),
    _WwpLeosTcePbtTnlGroupActivePair_Type()
)
wwpLeosTcePbtTnlGroupActivePair.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosTcePbtTnlGroupActivePair.setStatus("current")
_WwpLeosTcePbtTnlGroupReverting_Type = TruthValue
_WwpLeosTcePbtTnlGroupReverting_Object = MibTableColumn
wwpLeosTcePbtTnlGroupReverting = _WwpLeosTcePbtTnlGroupReverting_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 38, 1, 1, 10, 5, 1, 7),
    _WwpLeosTcePbtTnlGroupReverting_Type()
)
wwpLeosTcePbtTnlGroupReverting.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosTcePbtTnlGroupReverting.setStatus("current")
_WwpLeosTcePbtTnlGroupRowStatus_Type = RowStatus
_WwpLeosTcePbtTnlGroupRowStatus_Object = MibTableColumn
wwpLeosTcePbtTnlGroupRowStatus = _WwpLeosTcePbtTnlGroupRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 38, 1, 1, 10, 5, 1, 64),
    _WwpLeosTcePbtTnlGroupRowStatus_Type()
)
wwpLeosTcePbtTnlGroupRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wwpLeosTcePbtTnlGroupRowStatus.setStatus("current")
_WwpLeosTcePbtEncapTnlTable_Object = MibTable
wwpLeosTcePbtEncapTnlTable = _WwpLeosTcePbtEncapTnlTable_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 38, 1, 1, 10, 6)
)
if mibBuilder.loadTexts:
    wwpLeosTcePbtEncapTnlTable.setStatus("current")
_WwpLeosTcePbtEncapTnlEntry_Object = MibTableRow
wwpLeosTcePbtEncapTnlEntry = _WwpLeosTcePbtEncapTnlEntry_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 38, 1, 1, 10, 6, 1)
)
wwpLeosTcePbtEncapTnlEntry.setIndexNames(
    (0, "WWP-LEOS-PBT-MIB", "wwpLeosTcePbtEncapTnlIndex"),
)
if mibBuilder.loadTexts:
    wwpLeosTcePbtEncapTnlEntry.setStatus("current")
_WwpLeosTcePbtEncapTnlIndex_Type = Unsigned32
_WwpLeosTcePbtEncapTnlIndex_Object = MibTableColumn
wwpLeosTcePbtEncapTnlIndex = _WwpLeosTcePbtEncapTnlIndex_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 38, 1, 1, 10, 6, 1, 1),
    _WwpLeosTcePbtEncapTnlIndex_Type()
)
wwpLeosTcePbtEncapTnlIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    wwpLeosTcePbtEncapTnlIndex.setStatus("current")


class _WwpLeosTcePbtEncapTnlName_Type(DisplayString):
    """Custom type wwpLeosTcePbtEncapTnlName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_WwpLeosTcePbtEncapTnlName_Type.__name__ = "DisplayString"
_WwpLeosTcePbtEncapTnlName_Object = MibTableColumn
wwpLeosTcePbtEncapTnlName = _WwpLeosTcePbtEncapTnlName_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 38, 1, 1, 10, 6, 1, 2),
    _WwpLeosTcePbtEncapTnlName_Type()
)
wwpLeosTcePbtEncapTnlName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wwpLeosTcePbtEncapTnlName.setStatus("current")
_WwpLeosTcePbtEncapTnlRemoteBridgeIndex_Type = Unsigned32
_WwpLeosTcePbtEncapTnlRemoteBridgeIndex_Object = MibTableColumn
wwpLeosTcePbtEncapTnlRemoteBridgeIndex = _WwpLeosTcePbtEncapTnlRemoteBridgeIndex_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 38, 1, 1, 10, 6, 1, 3),
    _WwpLeosTcePbtEncapTnlRemoteBridgeIndex_Type()
)
wwpLeosTcePbtEncapTnlRemoteBridgeIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wwpLeosTcePbtEncapTnlRemoteBridgeIndex.setStatus("current")


class _WwpLeosTcePbtEncapTnlRemoteBridgeName_Type(DisplayString):
    """Custom type wwpLeosTcePbtEncapTnlRemoteBridgeName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_WwpLeosTcePbtEncapTnlRemoteBridgeName_Type.__name__ = "DisplayString"
_WwpLeosTcePbtEncapTnlRemoteBridgeName_Object = MibTableColumn
wwpLeosTcePbtEncapTnlRemoteBridgeName = _WwpLeosTcePbtEncapTnlRemoteBridgeName_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 38, 1, 1, 10, 6, 1, 4),
    _WwpLeosTcePbtEncapTnlRemoteBridgeName_Type()
)
wwpLeosTcePbtEncapTnlRemoteBridgeName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosTcePbtEncapTnlRemoteBridgeName.setStatus("current")
_WwpLeosTcePbtEncapTnlGroupIndex_Type = Unsigned32
_WwpLeosTcePbtEncapTnlGroupIndex_Object = MibTableColumn
wwpLeosTcePbtEncapTnlGroupIndex = _WwpLeosTcePbtEncapTnlGroupIndex_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 38, 1, 1, 10, 6, 1, 5),
    _WwpLeosTcePbtEncapTnlGroupIndex_Type()
)
wwpLeosTcePbtEncapTnlGroupIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wwpLeosTcePbtEncapTnlGroupIndex.setStatus("current")


class _WwpLeosTcePbtEncapTnlGroupName_Type(DisplayString):
    """Custom type wwpLeosTcePbtEncapTnlGroupName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_WwpLeosTcePbtEncapTnlGroupName_Type.__name__ = "DisplayString"
_WwpLeosTcePbtEncapTnlGroupName_Object = MibTableColumn
wwpLeosTcePbtEncapTnlGroupName = _WwpLeosTcePbtEncapTnlGroupName_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 38, 1, 1, 10, 6, 1, 6),
    _WwpLeosTcePbtEncapTnlGroupName_Type()
)
wwpLeosTcePbtEncapTnlGroupName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosTcePbtEncapTnlGroupName.setStatus("current")
_WwpLeosTcePbtEncapTnlBvId_Type = Unsigned32
_WwpLeosTcePbtEncapTnlBvId_Object = MibTableColumn
wwpLeosTcePbtEncapTnlBvId = _WwpLeosTcePbtEncapTnlBvId_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 38, 1, 1, 10, 6, 1, 7),
    _WwpLeosTcePbtEncapTnlBvId_Type()
)
wwpLeosTcePbtEncapTnlBvId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wwpLeosTcePbtEncapTnlBvId.setStatus("current")
_WwpLeosTcePbtEncapTnlPgId_Type = Unsigned32
_WwpLeosTcePbtEncapTnlPgId_Object = MibTableColumn
wwpLeosTcePbtEncapTnlPgId = _WwpLeosTcePbtEncapTnlPgId_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 38, 1, 1, 10, 6, 1, 8),
    _WwpLeosTcePbtEncapTnlPgId_Type()
)
wwpLeosTcePbtEncapTnlPgId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wwpLeosTcePbtEncapTnlPgId.setStatus("current")


class _WwpLeosTcePbtEncapTnlPortName_Type(DisplayString):
    """Custom type wwpLeosTcePbtEncapTnlPortName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_WwpLeosTcePbtEncapTnlPortName_Type.__name__ = "DisplayString"
_WwpLeosTcePbtEncapTnlPortName_Object = MibTableColumn
wwpLeosTcePbtEncapTnlPortName = _WwpLeosTcePbtEncapTnlPortName_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 38, 1, 1, 10, 6, 1, 9),
    _WwpLeosTcePbtEncapTnlPortName_Type()
)
wwpLeosTcePbtEncapTnlPortName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosTcePbtEncapTnlPortName.setStatus("current")
_WwpLeosTcePbtEncapTnlFaults_Type = Unsigned32
_WwpLeosTcePbtEncapTnlFaults_Object = MibTableColumn
wwpLeosTcePbtEncapTnlFaults = _WwpLeosTcePbtEncapTnlFaults_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 38, 1, 1, 10, 6, 1, 10),
    _WwpLeosTcePbtEncapTnlFaults_Type()
)
wwpLeosTcePbtEncapTnlFaults.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosTcePbtEncapTnlFaults.setStatus("current")


class _WwpLeosTcePbtEncapTnlAdminState_Type(Integer32):
    """Custom type wwpLeosTcePbtEncapTnlAdminState based on Integer32"""
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


_WwpLeosTcePbtEncapTnlAdminState_Type.__name__ = "Integer32"
_WwpLeosTcePbtEncapTnlAdminState_Object = MibTableColumn
wwpLeosTcePbtEncapTnlAdminState = _WwpLeosTcePbtEncapTnlAdminState_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 38, 1, 1, 10, 6, 1, 11),
    _WwpLeosTcePbtEncapTnlAdminState_Type()
)
wwpLeosTcePbtEncapTnlAdminState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wwpLeosTcePbtEncapTnlAdminState.setStatus("current")


class _WwpLeosTcePbtEncapTnlOperState_Type(Integer32):
    """Custom type wwpLeosTcePbtEncapTnlOperState based on Integer32"""
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


_WwpLeosTcePbtEncapTnlOperState_Type.__name__ = "Integer32"
_WwpLeosTcePbtEncapTnlOperState_Object = MibTableColumn
wwpLeosTcePbtEncapTnlOperState = _WwpLeosTcePbtEncapTnlOperState_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 38, 1, 1, 10, 6, 1, 12),
    _WwpLeosTcePbtEncapTnlOperState_Type()
)
wwpLeosTcePbtEncapTnlOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosTcePbtEncapTnlOperState.setStatus("current")


class _WwpLeosTcePbtEncapTnlFwdState_Type(Integer32):
    """Custom type wwpLeosTcePbtEncapTnlFwdState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("standby", 2))
    )


_WwpLeosTcePbtEncapTnlFwdState_Type.__name__ = "Integer32"
_WwpLeosTcePbtEncapTnlFwdState_Object = MibTableColumn
wwpLeosTcePbtEncapTnlFwdState = _WwpLeosTcePbtEncapTnlFwdState_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 38, 1, 1, 10, 6, 1, 13),
    _WwpLeosTcePbtEncapTnlFwdState_Type()
)
wwpLeosTcePbtEncapTnlFwdState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosTcePbtEncapTnlFwdState.setStatus("current")
_WwpLeosTcePbtEncapTnlPaired_Type = TruthValue
_WwpLeosTcePbtEncapTnlPaired_Object = MibTableColumn
wwpLeosTcePbtEncapTnlPaired = _WwpLeosTcePbtEncapTnlPaired_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 38, 1, 1, 10, 6, 1, 14),
    _WwpLeosTcePbtEncapTnlPaired_Type()
)
wwpLeosTcePbtEncapTnlPaired.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosTcePbtEncapTnlPaired.setStatus("current")


class _WwpLeosTcePbtEncapTnlPairIndex_Type(Integer32):
    """Custom type wwpLeosTcePbtEncapTnlPairIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_WwpLeosTcePbtEncapTnlPairIndex_Type.__name__ = "Integer32"
_WwpLeosTcePbtEncapTnlPairIndex_Object = MibTableColumn
wwpLeosTcePbtEncapTnlPairIndex = _WwpLeosTcePbtEncapTnlPairIndex_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 38, 1, 1, 10, 6, 1, 15),
    _WwpLeosTcePbtEncapTnlPairIndex_Type()
)
wwpLeosTcePbtEncapTnlPairIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wwpLeosTcePbtEncapTnlPairIndex.setStatus("current")


class _WwpLeosTcePbtEncapTnlPairOperState_Type(Integer32):
    """Custom type wwpLeosTcePbtEncapTnlPairOperState based on Integer32"""
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


_WwpLeosTcePbtEncapTnlPairOperState_Type.__name__ = "Integer32"
_WwpLeosTcePbtEncapTnlPairOperState_Object = MibTableColumn
wwpLeosTcePbtEncapTnlPairOperState = _WwpLeosTcePbtEncapTnlPairOperState_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 38, 1, 1, 10, 6, 1, 16),
    _WwpLeosTcePbtEncapTnlPairOperState_Type()
)
wwpLeosTcePbtEncapTnlPairOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosTcePbtEncapTnlPairOperState.setStatus("current")


class _WwpLeosTcePbtEncapTnlFrameCosPolicy_Type(Integer32):
    """Custom type wwpLeosTcePbtEncapTnlFrameCosPolicy based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("fixed", 1),
          ("isidPcPMap", 2))
    )


_WwpLeosTcePbtEncapTnlFrameCosPolicy_Type.__name__ = "Integer32"
_WwpLeosTcePbtEncapTnlFrameCosPolicy_Object = MibTableColumn
wwpLeosTcePbtEncapTnlFrameCosPolicy = _WwpLeosTcePbtEncapTnlFrameCosPolicy_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 38, 1, 1, 10, 6, 1, 17),
    _WwpLeosTcePbtEncapTnlFrameCosPolicy_Type()
)
wwpLeosTcePbtEncapTnlFrameCosPolicy.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wwpLeosTcePbtEncapTnlFrameCosPolicy.setStatus("current")
_WwpLeosTcePbtEncapTnlFrameCosMapIndex_Type = Unsigned32
_WwpLeosTcePbtEncapTnlFrameCosMapIndex_Object = MibTableColumn
wwpLeosTcePbtEncapTnlFrameCosMapIndex = _WwpLeosTcePbtEncapTnlFrameCosMapIndex_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 38, 1, 1, 10, 6, 1, 18),
    _WwpLeosTcePbtEncapTnlFrameCosMapIndex_Type()
)
wwpLeosTcePbtEncapTnlFrameCosMapIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wwpLeosTcePbtEncapTnlFrameCosMapIndex.setStatus("current")


class _WwpLeosTcePbtEncapTnlFrameCosMapName_Type(DisplayString):
    """Custom type wwpLeosTcePbtEncapTnlFrameCosMapName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_WwpLeosTcePbtEncapTnlFrameCosMapName_Type.__name__ = "DisplayString"
_WwpLeosTcePbtEncapTnlFrameCosMapName_Object = MibTableColumn
wwpLeosTcePbtEncapTnlFrameCosMapName = _WwpLeosTcePbtEncapTnlFrameCosMapName_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 38, 1, 1, 10, 6, 1, 19),
    _WwpLeosTcePbtEncapTnlFrameCosMapName_Type()
)
wwpLeosTcePbtEncapTnlFrameCosMapName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosTcePbtEncapTnlFrameCosMapName.setStatus("current")


class _WwpLeosTcePbtEncapTnlFixedPcp_Type(Integer32):
    """Custom type wwpLeosTcePbtEncapTnlFixedPcp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_WwpLeosTcePbtEncapTnlFixedPcp_Type.__name__ = "Integer32"
_WwpLeosTcePbtEncapTnlFixedPcp_Object = MibTableColumn
wwpLeosTcePbtEncapTnlFixedPcp = _WwpLeosTcePbtEncapTnlFixedPcp_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 38, 1, 1, 10, 6, 1, 20),
    _WwpLeosTcePbtEncapTnlFixedPcp_Type()
)
wwpLeosTcePbtEncapTnlFixedPcp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wwpLeosTcePbtEncapTnlFixedPcp.setStatus("current")
_WwpLeosTcePbtEncapTnlCfmConfigured_Type = TruthValue
_WwpLeosTcePbtEncapTnlCfmConfigured_Object = MibTableColumn
wwpLeosTcePbtEncapTnlCfmConfigured = _WwpLeosTcePbtEncapTnlCfmConfigured_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 38, 1, 1, 10, 6, 1, 21),
    _WwpLeosTcePbtEncapTnlCfmConfigured_Type()
)
wwpLeosTcePbtEncapTnlCfmConfigured.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosTcePbtEncapTnlCfmConfigured.setStatus("current")
_WwpLeosTcePbtEncapTnlPairedDecapIndex_Type = Unsigned32
_WwpLeosTcePbtEncapTnlPairedDecapIndex_Object = MibTableColumn
wwpLeosTcePbtEncapTnlPairedDecapIndex = _WwpLeosTcePbtEncapTnlPairedDecapIndex_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 38, 1, 1, 10, 6, 1, 22),
    _WwpLeosTcePbtEncapTnlPairedDecapIndex_Type()
)
wwpLeosTcePbtEncapTnlPairedDecapIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosTcePbtEncapTnlPairedDecapIndex.setStatus("current")


class _WwpLeosTcePbtEncapTnlPairedDecapName_Type(DisplayString):
    """Custom type wwpLeosTcePbtEncapTnlPairedDecapName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_WwpLeosTcePbtEncapTnlPairedDecapName_Type.__name__ = "DisplayString"
_WwpLeosTcePbtEncapTnlPairedDecapName_Object = MibTableColumn
wwpLeosTcePbtEncapTnlPairedDecapName = _WwpLeosTcePbtEncapTnlPairedDecapName_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 38, 1, 1, 10, 6, 1, 23),
    _WwpLeosTcePbtEncapTnlPairedDecapName_Type()
)
wwpLeosTcePbtEncapTnlPairedDecapName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosTcePbtEncapTnlPairedDecapName.setStatus("current")
_WwpLeosTcePbtEncapTnlWeight_Type = Unsigned32
_WwpLeosTcePbtEncapTnlWeight_Object = MibTableColumn
wwpLeosTcePbtEncapTnlWeight = _WwpLeosTcePbtEncapTnlWeight_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 38, 1, 1, 10, 6, 1, 24),
    _WwpLeosTcePbtEncapTnlWeight_Type()
)
wwpLeosTcePbtEncapTnlWeight.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wwpLeosTcePbtEncapTnlWeight.setStatus("current")
_WwpLeosTcePbtEncapTnlStatsEnabled_Type = TruthValue
_WwpLeosTcePbtEncapTnlStatsEnabled_Object = MibTableColumn
wwpLeosTcePbtEncapTnlStatsEnabled = _WwpLeosTcePbtEncapTnlStatsEnabled_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 38, 1, 1, 10, 6, 1, 25),
    _WwpLeosTcePbtEncapTnlStatsEnabled_Type()
)
wwpLeosTcePbtEncapTnlStatsEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosTcePbtEncapTnlStatsEnabled.setStatus("current")
_WwpLeosTcePbtEncapTnlLocalBridgeIndex_Type = Unsigned32
_WwpLeosTcePbtEncapTnlLocalBridgeIndex_Object = MibTableColumn
wwpLeosTcePbtEncapTnlLocalBridgeIndex = _WwpLeosTcePbtEncapTnlLocalBridgeIndex_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 38, 1, 1, 10, 6, 1, 26),
    _WwpLeosTcePbtEncapTnlLocalBridgeIndex_Type()
)
wwpLeosTcePbtEncapTnlLocalBridgeIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wwpLeosTcePbtEncapTnlLocalBridgeIndex.setStatus("current")
_WwpLeosTcePbtEncapTnlLocalBridgeName_Type = DisplayString
_WwpLeosTcePbtEncapTnlLocalBridgeName_Object = MibTableColumn
wwpLeosTcePbtEncapTnlLocalBridgeName = _WwpLeosTcePbtEncapTnlLocalBridgeName_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 38, 1, 1, 10, 6, 1, 27),
    _WwpLeosTcePbtEncapTnlLocalBridgeName_Type()
)
wwpLeosTcePbtEncapTnlLocalBridgeName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosTcePbtEncapTnlLocalBridgeName.setStatus("current")
_WwpLeosTcePbtEncapTnlReversionToPairIndex_Type = Unsigned32
_WwpLeosTcePbtEncapTnlReversionToPairIndex_Object = MibTableColumn
wwpLeosTcePbtEncapTnlReversionToPairIndex = _WwpLeosTcePbtEncapTnlReversionToPairIndex_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 38, 1, 1, 10, 6, 1, 28),
    _WwpLeosTcePbtEncapTnlReversionToPairIndex_Type()
)
wwpLeosTcePbtEncapTnlReversionToPairIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    wwpLeosTcePbtEncapTnlReversionToPairIndex.setStatus("current")
_WwpLeosTcePbtEncapTnlReversionFromPairIndex_Type = Unsigned32
_WwpLeosTcePbtEncapTnlReversionFromPairIndex_Object = MibTableColumn
wwpLeosTcePbtEncapTnlReversionFromPairIndex = _WwpLeosTcePbtEncapTnlReversionFromPairIndex_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 38, 1, 1, 10, 6, 1, 29),
    _WwpLeosTcePbtEncapTnlReversionFromPairIndex_Type()
)
wwpLeosTcePbtEncapTnlReversionFromPairIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    wwpLeosTcePbtEncapTnlReversionFromPairIndex.setStatus("current")
_WwpLeosTcePbtEncapTnlRowStatus_Type = RowStatus
_WwpLeosTcePbtEncapTnlRowStatus_Object = MibTableColumn
wwpLeosTcePbtEncapTnlRowStatus = _WwpLeosTcePbtEncapTnlRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 38, 1, 1, 10, 6, 1, 64),
    _WwpLeosTcePbtEncapTnlRowStatus_Type()
)
wwpLeosTcePbtEncapTnlRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wwpLeosTcePbtEncapTnlRowStatus.setStatus("current")
_WwpLeosTcePbtDecapTnlTable_Object = MibTable
wwpLeosTcePbtDecapTnlTable = _WwpLeosTcePbtDecapTnlTable_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 38, 1, 1, 10, 7)
)
if mibBuilder.loadTexts:
    wwpLeosTcePbtDecapTnlTable.setStatus("current")
_WwpLeosTcePbtDecapTnlEntry_Object = MibTableRow
wwpLeosTcePbtDecapTnlEntry = _WwpLeosTcePbtDecapTnlEntry_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 38, 1, 1, 10, 7, 1)
)
wwpLeosTcePbtDecapTnlEntry.setIndexNames(
    (0, "WWP-LEOS-PBT-MIB", "wwpLeosTcePbtDecapTnlIndex"),
)
if mibBuilder.loadTexts:
    wwpLeosTcePbtDecapTnlEntry.setStatus("current")
_WwpLeosTcePbtDecapTnlIndex_Type = Unsigned32
_WwpLeosTcePbtDecapTnlIndex_Object = MibTableColumn
wwpLeosTcePbtDecapTnlIndex = _WwpLeosTcePbtDecapTnlIndex_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 38, 1, 1, 10, 7, 1, 1),
    _WwpLeosTcePbtDecapTnlIndex_Type()
)
wwpLeosTcePbtDecapTnlIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wwpLeosTcePbtDecapTnlIndex.setStatus("current")


class _WwpLeosTcePbtDecapTnlName_Type(DisplayString):
    """Custom type wwpLeosTcePbtDecapTnlName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_WwpLeosTcePbtDecapTnlName_Type.__name__ = "DisplayString"
_WwpLeosTcePbtDecapTnlName_Object = MibTableColumn
wwpLeosTcePbtDecapTnlName = _WwpLeosTcePbtDecapTnlName_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 38, 1, 1, 10, 7, 1, 2),
    _WwpLeosTcePbtDecapTnlName_Type()
)
wwpLeosTcePbtDecapTnlName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wwpLeosTcePbtDecapTnlName.setStatus("current")
_WwpLeosTcePbtDecapTnlRemoteBridgeIndex_Type = Unsigned32
_WwpLeosTcePbtDecapTnlRemoteBridgeIndex_Object = MibTableColumn
wwpLeosTcePbtDecapTnlRemoteBridgeIndex = _WwpLeosTcePbtDecapTnlRemoteBridgeIndex_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 38, 1, 1, 10, 7, 1, 3),
    _WwpLeosTcePbtDecapTnlRemoteBridgeIndex_Type()
)
wwpLeosTcePbtDecapTnlRemoteBridgeIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wwpLeosTcePbtDecapTnlRemoteBridgeIndex.setStatus("current")


class _WwpLeosTcePbtDecapTnlRemoteBridgeName_Type(DisplayString):
    """Custom type wwpLeosTcePbtDecapTnlRemoteBridgeName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_WwpLeosTcePbtDecapTnlRemoteBridgeName_Type.__name__ = "DisplayString"
_WwpLeosTcePbtDecapTnlRemoteBridgeName_Object = MibTableColumn
wwpLeosTcePbtDecapTnlRemoteBridgeName = _WwpLeosTcePbtDecapTnlRemoteBridgeName_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 38, 1, 1, 10, 7, 1, 4),
    _WwpLeosTcePbtDecapTnlRemoteBridgeName_Type()
)
wwpLeosTcePbtDecapTnlRemoteBridgeName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosTcePbtDecapTnlRemoteBridgeName.setStatus("current")
_WwpLeosTcePbtDecapTnlGroupIndex_Type = Unsigned32
_WwpLeosTcePbtDecapTnlGroupIndex_Object = MibTableColumn
wwpLeosTcePbtDecapTnlGroupIndex = _WwpLeosTcePbtDecapTnlGroupIndex_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 38, 1, 1, 10, 7, 1, 5),
    _WwpLeosTcePbtDecapTnlGroupIndex_Type()
)
wwpLeosTcePbtDecapTnlGroupIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wwpLeosTcePbtDecapTnlGroupIndex.setStatus("current")


class _WwpLeosTcePbtDecapTnlGroupName_Type(DisplayString):
    """Custom type wwpLeosTcePbtDecapTnlGroupName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_WwpLeosTcePbtDecapTnlGroupName_Type.__name__ = "DisplayString"
_WwpLeosTcePbtDecapTnlGroupName_Object = MibTableColumn
wwpLeosTcePbtDecapTnlGroupName = _WwpLeosTcePbtDecapTnlGroupName_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 38, 1, 1, 10, 7, 1, 6),
    _WwpLeosTcePbtDecapTnlGroupName_Type()
)
wwpLeosTcePbtDecapTnlGroupName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosTcePbtDecapTnlGroupName.setStatus("current")
_WwpLeosTcePbtDecapTnlBvId_Type = Unsigned32
_WwpLeosTcePbtDecapTnlBvId_Object = MibTableColumn
wwpLeosTcePbtDecapTnlBvId = _WwpLeosTcePbtDecapTnlBvId_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 38, 1, 1, 10, 7, 1, 7),
    _WwpLeosTcePbtDecapTnlBvId_Type()
)
wwpLeosTcePbtDecapTnlBvId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wwpLeosTcePbtDecapTnlBvId.setStatus("current")
_WwpLeosTcePbtDecapTnlPgId_Type = Unsigned32
_WwpLeosTcePbtDecapTnlPgId_Object = MibTableColumn
wwpLeosTcePbtDecapTnlPgId = _WwpLeosTcePbtDecapTnlPgId_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 38, 1, 1, 10, 7, 1, 8),
    _WwpLeosTcePbtDecapTnlPgId_Type()
)
wwpLeosTcePbtDecapTnlPgId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wwpLeosTcePbtDecapTnlPgId.setStatus("current")


class _WwpLeosTcePbtDecapTnlPortName_Type(DisplayString):
    """Custom type wwpLeosTcePbtDecapTnlPortName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_WwpLeosTcePbtDecapTnlPortName_Type.__name__ = "DisplayString"
_WwpLeosTcePbtDecapTnlPortName_Object = MibTableColumn
wwpLeosTcePbtDecapTnlPortName = _WwpLeosTcePbtDecapTnlPortName_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 38, 1, 1, 10, 7, 1, 9),
    _WwpLeosTcePbtDecapTnlPortName_Type()
)
wwpLeosTcePbtDecapTnlPortName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosTcePbtDecapTnlPortName.setStatus("current")
_WwpLeosTcePbtDecapTnlFaults_Type = Unsigned32
_WwpLeosTcePbtDecapTnlFaults_Object = MibTableColumn
wwpLeosTcePbtDecapTnlFaults = _WwpLeosTcePbtDecapTnlFaults_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 38, 1, 1, 10, 7, 1, 10),
    _WwpLeosTcePbtDecapTnlFaults_Type()
)
wwpLeosTcePbtDecapTnlFaults.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosTcePbtDecapTnlFaults.setStatus("current")


class _WwpLeosTcePbtDecapTnlOperState_Type(Integer32):
    """Custom type wwpLeosTcePbtDecapTnlOperState based on Integer32"""
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


_WwpLeosTcePbtDecapTnlOperState_Type.__name__ = "Integer32"
_WwpLeosTcePbtDecapTnlOperState_Object = MibTableColumn
wwpLeosTcePbtDecapTnlOperState = _WwpLeosTcePbtDecapTnlOperState_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 38, 1, 1, 10, 7, 1, 11),
    _WwpLeosTcePbtDecapTnlOperState_Type()
)
wwpLeosTcePbtDecapTnlOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosTcePbtDecapTnlOperState.setStatus("current")


class _WwpLeosTcePbtDecapTnlFwdState_Type(Integer32):
    """Custom type wwpLeosTcePbtDecapTnlFwdState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("standby", 2))
    )


_WwpLeosTcePbtDecapTnlFwdState_Type.__name__ = "Integer32"
_WwpLeosTcePbtDecapTnlFwdState_Object = MibTableColumn
wwpLeosTcePbtDecapTnlFwdState = _WwpLeosTcePbtDecapTnlFwdState_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 38, 1, 1, 10, 7, 1, 12),
    _WwpLeosTcePbtDecapTnlFwdState_Type()
)
wwpLeosTcePbtDecapTnlFwdState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosTcePbtDecapTnlFwdState.setStatus("current")
_WwpLeosTcePbtDecapTnlPaired_Type = TruthValue
_WwpLeosTcePbtDecapTnlPaired_Object = MibTableColumn
wwpLeosTcePbtDecapTnlPaired = _WwpLeosTcePbtDecapTnlPaired_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 38, 1, 1, 10, 7, 1, 13),
    _WwpLeosTcePbtDecapTnlPaired_Type()
)
wwpLeosTcePbtDecapTnlPaired.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosTcePbtDecapTnlPaired.setStatus("current")


class _WwpLeosTcePbtDecapTnlPairIndex_Type(Integer32):
    """Custom type wwpLeosTcePbtDecapTnlPairIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_WwpLeosTcePbtDecapTnlPairIndex_Type.__name__ = "Integer32"
_WwpLeosTcePbtDecapTnlPairIndex_Object = MibTableColumn
wwpLeosTcePbtDecapTnlPairIndex = _WwpLeosTcePbtDecapTnlPairIndex_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 38, 1, 1, 10, 7, 1, 14),
    _WwpLeosTcePbtDecapTnlPairIndex_Type()
)
wwpLeosTcePbtDecapTnlPairIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wwpLeosTcePbtDecapTnlPairIndex.setStatus("current")


class _WwpLeosTcePbtDecapTnlPairOperState_Type(Integer32):
    """Custom type wwpLeosTcePbtDecapTnlPairOperState based on Integer32"""
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


_WwpLeosTcePbtDecapTnlPairOperState_Type.__name__ = "Integer32"
_WwpLeosTcePbtDecapTnlPairOperState_Object = MibTableColumn
wwpLeosTcePbtDecapTnlPairOperState = _WwpLeosTcePbtDecapTnlPairOperState_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 38, 1, 1, 10, 7, 1, 15),
    _WwpLeosTcePbtDecapTnlPairOperState_Type()
)
wwpLeosTcePbtDecapTnlPairOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosTcePbtDecapTnlPairOperState.setStatus("current")


class _WwpLeosTcePbtDecapTnlResolvedCosPolicy_Type(Integer32):
    """Custom type wwpLeosTcePbtDecapTnlResolvedCosPolicy based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("fixed", 2),
          ("ignore", 1),
          ("isidPcpMap", 3))
    )


_WwpLeosTcePbtDecapTnlResolvedCosPolicy_Type.__name__ = "Integer32"
_WwpLeosTcePbtDecapTnlResolvedCosPolicy_Object = MibTableColumn
wwpLeosTcePbtDecapTnlResolvedCosPolicy = _WwpLeosTcePbtDecapTnlResolvedCosPolicy_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 38, 1, 1, 10, 7, 1, 16),
    _WwpLeosTcePbtDecapTnlResolvedCosPolicy_Type()
)
wwpLeosTcePbtDecapTnlResolvedCosPolicy.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wwpLeosTcePbtDecapTnlResolvedCosPolicy.setStatus("current")
_WwpLeosTcePbtDecapTnlResolvedCosMapIndex_Type = Unsigned32
_WwpLeosTcePbtDecapTnlResolvedCosMapIndex_Object = MibTableColumn
wwpLeosTcePbtDecapTnlResolvedCosMapIndex = _WwpLeosTcePbtDecapTnlResolvedCosMapIndex_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 38, 1, 1, 10, 7, 1, 17),
    _WwpLeosTcePbtDecapTnlResolvedCosMapIndex_Type()
)
wwpLeosTcePbtDecapTnlResolvedCosMapIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wwpLeosTcePbtDecapTnlResolvedCosMapIndex.setStatus("current")


class _WwpLeosTcePbtDecapTnlResolvedCosMapName_Type(DisplayString):
    """Custom type wwpLeosTcePbtDecapTnlResolvedCosMapName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_WwpLeosTcePbtDecapTnlResolvedCosMapName_Type.__name__ = "DisplayString"
_WwpLeosTcePbtDecapTnlResolvedCosMapName_Object = MibTableColumn
wwpLeosTcePbtDecapTnlResolvedCosMapName = _WwpLeosTcePbtDecapTnlResolvedCosMapName_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 38, 1, 1, 10, 7, 1, 18),
    _WwpLeosTcePbtDecapTnlResolvedCosMapName_Type()
)
wwpLeosTcePbtDecapTnlResolvedCosMapName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosTcePbtDecapTnlResolvedCosMapName.setStatus("current")
_WwpLeosTcePbtDecapTnlCfmConfigured_Type = TruthValue
_WwpLeosTcePbtDecapTnlCfmConfigured_Object = MibTableColumn
wwpLeosTcePbtDecapTnlCfmConfigured = _WwpLeosTcePbtDecapTnlCfmConfigured_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 38, 1, 1, 10, 7, 1, 19),
    _WwpLeosTcePbtDecapTnlCfmConfigured_Type()
)
wwpLeosTcePbtDecapTnlCfmConfigured.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosTcePbtDecapTnlCfmConfigured.setStatus("current")
_WwpLeosTcePbtDecapTnlPairedEncapIndex_Type = Unsigned32
_WwpLeosTcePbtDecapTnlPairedEncapIndex_Object = MibTableColumn
wwpLeosTcePbtDecapTnlPairedEncapIndex = _WwpLeosTcePbtDecapTnlPairedEncapIndex_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 38, 1, 1, 10, 7, 1, 20),
    _WwpLeosTcePbtDecapTnlPairedEncapIndex_Type()
)
wwpLeosTcePbtDecapTnlPairedEncapIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosTcePbtDecapTnlPairedEncapIndex.setStatus("current")


class _WwpLeosTcePbtDecapTnlPairedEncapName_Type(DisplayString):
    """Custom type wwpLeosTcePbtDecapTnlPairedEncapName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_WwpLeosTcePbtDecapTnlPairedEncapName_Type.__name__ = "DisplayString"
_WwpLeosTcePbtDecapTnlPairedEncapName_Object = MibTableColumn
wwpLeosTcePbtDecapTnlPairedEncapName = _WwpLeosTcePbtDecapTnlPairedEncapName_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 38, 1, 1, 10, 7, 1, 21),
    _WwpLeosTcePbtDecapTnlPairedEncapName_Type()
)
wwpLeosTcePbtDecapTnlPairedEncapName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosTcePbtDecapTnlPairedEncapName.setStatus("current")
_WwpLeosTcePbtDecapTnlStatsEnabled_Type = TruthValue
_WwpLeosTcePbtDecapTnlStatsEnabled_Object = MibTableColumn
wwpLeosTcePbtDecapTnlStatsEnabled = _WwpLeosTcePbtDecapTnlStatsEnabled_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 38, 1, 1, 10, 7, 1, 22),
    _WwpLeosTcePbtDecapTnlStatsEnabled_Type()
)
wwpLeosTcePbtDecapTnlStatsEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosTcePbtDecapTnlStatsEnabled.setStatus("current")
_WwpLeosTcePbtDecapTnlRowStatus_Type = RowStatus
_WwpLeosTcePbtDecapTnlRowStatus_Object = MibTableColumn
wwpLeosTcePbtDecapTnlRowStatus = _WwpLeosTcePbtDecapTnlRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 38, 1, 1, 10, 7, 1, 64),
    _WwpLeosTcePbtDecapTnlRowStatus_Type()
)
wwpLeosTcePbtDecapTnlRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wwpLeosTcePbtDecapTnlRowStatus.setStatus("current")
_WwpLeosTcePbtServiceUserFrameL2TransformTable_Object = MibTable
wwpLeosTcePbtServiceUserFrameL2TransformTable = _WwpLeosTcePbtServiceUserFrameL2TransformTable_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 38, 1, 1, 10, 8)
)
if mibBuilder.loadTexts:
    wwpLeosTcePbtServiceUserFrameL2TransformTable.setStatus("current")
_WwpLeosTcePbtServiceUserFrameL2TransformEntry_Object = MibTableRow
wwpLeosTcePbtServiceUserFrameL2TransformEntry = _WwpLeosTcePbtServiceUserFrameL2TransformEntry_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 38, 1, 1, 10, 8, 1)
)
wwpLeosTcePbtServiceUserFrameL2TransformEntry.setIndexNames(
    (0, "WWP-LEOS-PBT-MIB", "wwpLeosTcePbtServiceIndex"),
    (0, "WWP-LEOS-PBT-MIB", "wwpLeosTcePbtServiceUserFrameL2TransformDirection"),
    (0, "WWP-LEOS-PBT-MIB", "wwpLeosTcePbtServiceUserFrameL2TransformTagIndex"),
)
if mibBuilder.loadTexts:
    wwpLeosTcePbtServiceUserFrameL2TransformEntry.setStatus("current")


class _WwpLeosTcePbtServiceUserFrameL2TransformDirection_Type(Integer32):
    """Custom type wwpLeosTcePbtServiceUserFrameL2TransformDirection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("egress", 2),
          ("ingress", 1))
    )


_WwpLeosTcePbtServiceUserFrameL2TransformDirection_Type.__name__ = "Integer32"
_WwpLeosTcePbtServiceUserFrameL2TransformDirection_Object = MibTableColumn
wwpLeosTcePbtServiceUserFrameL2TransformDirection = _WwpLeosTcePbtServiceUserFrameL2TransformDirection_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 38, 1, 1, 10, 8, 1, 1),
    _WwpLeosTcePbtServiceUserFrameL2TransformDirection_Type()
)
wwpLeosTcePbtServiceUserFrameL2TransformDirection.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wwpLeosTcePbtServiceUserFrameL2TransformDirection.setStatus("current")


class _WwpLeosTcePbtServiceUserFrameL2TransformTagIndex_Type(Integer32):
    """Custom type wwpLeosTcePbtServiceUserFrameL2TransformTagIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_WwpLeosTcePbtServiceUserFrameL2TransformTagIndex_Type.__name__ = "Integer32"
_WwpLeosTcePbtServiceUserFrameL2TransformTagIndex_Object = MibTableColumn
wwpLeosTcePbtServiceUserFrameL2TransformTagIndex = _WwpLeosTcePbtServiceUserFrameL2TransformTagIndex_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 38, 1, 1, 10, 8, 1, 2),
    _WwpLeosTcePbtServiceUserFrameL2TransformTagIndex_Type()
)
wwpLeosTcePbtServiceUserFrameL2TransformTagIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wwpLeosTcePbtServiceUserFrameL2TransformTagIndex.setStatus("current")


class _WwpLeosTcePbtServiceUserFrameL2TransformTagAction_Type(Integer32):
    """Custom type wwpLeosTcePbtServiceUserFrameL2TransformTagAction based on Integer32"""
    defaultValue = 1

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
        *(("none", 1),
          ("pop", 3),
          ("push", 2),
          ("stamp1", 4),
          ("stamp2", 5))
    )


_WwpLeosTcePbtServiceUserFrameL2TransformTagAction_Type.__name__ = "Integer32"
_WwpLeosTcePbtServiceUserFrameL2TransformTagAction_Object = MibTableColumn
wwpLeosTcePbtServiceUserFrameL2TransformTagAction = _WwpLeosTcePbtServiceUserFrameL2TransformTagAction_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 38, 1, 1, 10, 8, 1, 3),
    _WwpLeosTcePbtServiceUserFrameL2TransformTagAction_Type()
)
wwpLeosTcePbtServiceUserFrameL2TransformTagAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosTcePbtServiceUserFrameL2TransformTagAction.setStatus("current")


class _WwpLeosTcePbtServiceUserFrameL2TransformTagValue_Type(Integer32):
    """Custom type wwpLeosTcePbtServiceUserFrameL2TransformTagValue based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_WwpLeosTcePbtServiceUserFrameL2TransformTagValue_Type.__name__ = "Integer32"
_WwpLeosTcePbtServiceUserFrameL2TransformTagValue_Object = MibTableColumn
wwpLeosTcePbtServiceUserFrameL2TransformTagValue = _WwpLeosTcePbtServiceUserFrameL2TransformTagValue_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 38, 1, 1, 10, 8, 1, 4),
    _WwpLeosTcePbtServiceUserFrameL2TransformTagValue_Type()
)
wwpLeosTcePbtServiceUserFrameL2TransformTagValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosTcePbtServiceUserFrameL2TransformTagValue.setStatus("current")


class _WwpLeosTcePbtServiceUserFrameL2TransformTagEtype_Type(Integer32):
    """Custom type wwpLeosTcePbtServiceUserFrameL2TransformTagEtype based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65534),
    )


_WwpLeosTcePbtServiceUserFrameL2TransformTagEtype_Type.__name__ = "Integer32"
_WwpLeosTcePbtServiceUserFrameL2TransformTagEtype_Object = MibTableColumn
wwpLeosTcePbtServiceUserFrameL2TransformTagEtype = _WwpLeosTcePbtServiceUserFrameL2TransformTagEtype_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 38, 1, 1, 10, 8, 1, 5),
    _WwpLeosTcePbtServiceUserFrameL2TransformTagEtype_Type()
)
wwpLeosTcePbtServiceUserFrameL2TransformTagEtype.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosTcePbtServiceUserFrameL2TransformTagEtype.setStatus("current")


class _WwpLeosTcePbtServiceUserFrameL2TransformTagPriority_Type(Integer32):
    """Custom type wwpLeosTcePbtServiceUserFrameL2TransformTagPriority based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_WwpLeosTcePbtServiceUserFrameL2TransformTagPriority_Type.__name__ = "Integer32"
_WwpLeosTcePbtServiceUserFrameL2TransformTagPriority_Object = MibTableColumn
wwpLeosTcePbtServiceUserFrameL2TransformTagPriority = _WwpLeosTcePbtServiceUserFrameL2TransformTagPriority_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 38, 1, 1, 10, 8, 1, 6),
    _WwpLeosTcePbtServiceUserFrameL2TransformTagPriority_Type()
)
wwpLeosTcePbtServiceUserFrameL2TransformTagPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosTcePbtServiceUserFrameL2TransformTagPriority.setStatus("current")


class _WwpLeosTcePbtServiceUserFrameL2TransformPriPolicy_Type(Integer32):
    """Custom type wwpLeosTcePbtServiceUserFrameL2TransformPriPolicy based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("leave", 1),
          ("mapped", 3),
          ("static", 2))
    )


_WwpLeosTcePbtServiceUserFrameL2TransformPriPolicy_Type.__name__ = "Integer32"
_WwpLeosTcePbtServiceUserFrameL2TransformPriPolicy_Object = MibTableColumn
wwpLeosTcePbtServiceUserFrameL2TransformPriPolicy = _WwpLeosTcePbtServiceUserFrameL2TransformPriPolicy_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 38, 1, 1, 10, 8, 1, 7),
    _WwpLeosTcePbtServiceUserFrameL2TransformPriPolicy_Type()
)
wwpLeosTcePbtServiceUserFrameL2TransformPriPolicy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosTcePbtServiceUserFrameL2TransformPriPolicy.setStatus("current")


class _WwpLeosTcePbtServiceUserFrameL2TransformUseTagValue_Type(TruthValue):
    """Custom type wwpLeosTcePbtServiceUserFrameL2TransformUseTagValue based on TruthValue"""


_WwpLeosTcePbtServiceUserFrameL2TransformUseTagValue_Object = MibTableColumn
wwpLeosTcePbtServiceUserFrameL2TransformUseTagValue = _WwpLeosTcePbtServiceUserFrameL2TransformUseTagValue_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 38, 1, 1, 10, 8, 1, 8),
    _WwpLeosTcePbtServiceUserFrameL2TransformUseTagValue_Type()
)
wwpLeosTcePbtServiceUserFrameL2TransformUseTagValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosTcePbtServiceUserFrameL2TransformUseTagValue.setStatus("current")


class _WwpLeosTcePbtServiceUserFrameL2TransformUseTagEtype_Type(TruthValue):
    """Custom type wwpLeosTcePbtServiceUserFrameL2TransformUseTagEtype based on TruthValue"""


_WwpLeosTcePbtServiceUserFrameL2TransformUseTagEtype_Object = MibTableColumn
wwpLeosTcePbtServiceUserFrameL2TransformUseTagEtype = _WwpLeosTcePbtServiceUserFrameL2TransformUseTagEtype_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 38, 1, 1, 10, 8, 1, 9),
    _WwpLeosTcePbtServiceUserFrameL2TransformUseTagEtype_Type()
)
wwpLeosTcePbtServiceUserFrameL2TransformUseTagEtype.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosTcePbtServiceUserFrameL2TransformUseTagEtype.setStatus("current")
_WwpLeosPbtMIBNotificationPrefix_ObjectIdentity = ObjectIdentity
wwpLeosPbtMIBNotificationPrefix = _WwpLeosPbtMIBNotificationPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 38, 2)
)
_WwpLeosPbtMIBNotifications_ObjectIdentity = ObjectIdentity
wwpLeosPbtMIBNotifications = _WwpLeosPbtMIBNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 38, 2, 0)
)
_WwpLeosPbtMIBConformance_ObjectIdentity = ObjectIdentity
wwpLeosPbtMIBConformance = _WwpLeosPbtMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 38, 3)
)
_WwpLeosPbtMIBCompliances_ObjectIdentity = ObjectIdentity
wwpLeosPbtMIBCompliances = _WwpLeosPbtMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 38, 3, 1)
)
_WwpLeosPbtMIBGroups_ObjectIdentity = ObjectIdentity
wwpLeosPbtMIBGroups = _WwpLeosPbtMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 38, 3, 2)
)

# Managed Objects groups

pbtGlobalConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 38, 3, 2, 1)
)
pbtGlobalConfigGroup.setObjects(
      *(("WWP-LEOS-PBT-MIB", "wwpLeosPbtBridgeMac"),
        ("WWP-LEOS-PBT-MIB", "wwpLeosPbtServiceTagEType"),
        ("WWP-LEOS-PBT-MIB", "wwpLeosPbtTunnelTagEtype"),
        ("WWP-LEOS-PBT-MIB", "wwpLeosPbtTunnelReversionState"),
        ("WWP-LEOS-PBT-MIB", "wwpLeosPbtTunnelReversionHoldTime"),
        ("WWP-LEOS-PBT-MIB", "wwpLeosPbtAdminMode"),
        ("WWP-LEOS-PBT-MIB", "wwpLeosPbtOperMode"),
        ("WWP-LEOS-PBT-MIB", "wwpLeosPbtServiceVlanTpid"))
)
if mibBuilder.loadTexts:
    pbtGlobalConfigGroup.setStatus("current")

pbtBridgeNameMacMapGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 38, 3, 2, 2)
)
pbtBridgeNameMacMapGroup.setObjects(
      *(("WWP-LEOS-PBT-MIB", "wwpLeosPbtBridgeNameMacMapIndex"),
        ("WWP-LEOS-PBT-MIB", "wwpLeosPbtBridgeNameMacMapBridgeName"),
        ("WWP-LEOS-PBT-MIB", "wwpLeosPbtBridgeNameMacMapMacAddr"),
        ("WWP-LEOS-PBT-MIB", "wwpLeosPbtBridgeNameMacMapUseCount"),
        ("WWP-LEOS-PBT-MIB", "wwpLeosPbtBridgeNameMacMapRowStatus"))
)
if mibBuilder.loadTexts:
    pbtBridgeNameMacMapGroup.setStatus("current")

pbtReserveBvidGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 38, 3, 2, 3)
)
pbtReserveBvidGroup.setObjects(
      *(("WWP-LEOS-PBT-MIB", "wwpLeosPbtReservedBVID"),
        ("WWP-LEOS-PBT-MIB", "wwpLeosPbtReservedBVIDRowStatus"))
)
if mibBuilder.loadTexts:
    pbtReserveBvidGroup.setStatus("current")

pbtVirtualCircuitGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 38, 3, 2, 4)
)
pbtVirtualCircuitGroup.setObjects(
      *(("WWP-LEOS-PBT-MIB", "wwpLeosPbtVirtualCircuitIndex"),
        ("WWP-LEOS-PBT-MIB", "wwpLeosPbtVirtualCircuitName"),
        ("WWP-LEOS-PBT-MIB", "wwpLeosPbtVirtualCircuitFixedEncapTunnelId"),
        ("WWP-LEOS-PBT-MIB", "wwpLeosPbtVirtualCircuitDestBridgeIndex"),
        ("WWP-LEOS-PBT-MIB", "wwpLeosPbtVirtualCircuitIngressISID"),
        ("WWP-LEOS-PBT-MIB", "wwpLeosPbtVirtualCircuitEgressISID"),
        ("WWP-LEOS-PBT-MIB", "wwpLeosPbtVirtualCircuitOperState"),
        ("WWP-LEOS-PBT-MIB", "wwpLeosPbtVirtualCircuitEncapTunnelIdInUse"),
        ("WWP-LEOS-PBT-MIB", "wwpLeosPbtVirtualCircuitRowStatus"))
)
if mibBuilder.loadTexts:
    pbtVirtualCircuitGroup.setStatus("current")

pbtVirtualCircuitStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 38, 3, 2, 5)
)
pbtVirtualCircuitStatsGroup.setObjects(
      *(("WWP-LEOS-PBT-MIB", "wwpLeosPbtVirtualCircuitTxBytesHi"),
        ("WWP-LEOS-PBT-MIB", "wwpLeosPbtVirtualCircuitTxBytesLo"),
        ("WWP-LEOS-PBT-MIB", "wwpLeosPbtVirtualCircuitRxBytesHi"),
        ("WWP-LEOS-PBT-MIB", "wwpLeosPbtVirtualCircuitRxBytesLo"))
)
if mibBuilder.loadTexts:
    pbtVirtualCircuitStatsGroup.setStatus("current")


# Notification objects

wwpLeosPbtTunnelFaultNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 38, 2, 0, 1)
)
wwpLeosPbtTunnelFaultNotification.setObjects(
    ("WWP-LEOS-VPLS-MIB", "wwpLeosVplsEncapTunnelId")
)
if mibBuilder.loadTexts:
    wwpLeosPbtTunnelFaultNotification.setStatus(
        "deprecated"
    )

wwpLeosPbtTunnelReversionNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 38, 2, 0, 2)
)
wwpLeosPbtTunnelReversionNotification.setObjects(
      *(("WWP-LEOS-VPLS-MIB", "wwpLeosVplsEncapTunnelId"),
        ("WWP-LEOS-VPLS-MIB", "wwpLeosVplsEncapTunnelName"))
)
if mibBuilder.loadTexts:
    wwpLeosPbtTunnelReversionNotification.setStatus(
        "current"
    )

wwpLeosPbtTunnelActivateNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 38, 2, 0, 3)
)
wwpLeosPbtTunnelActivateNotification.setObjects(
      *(("WWP-LEOS-VPLS-MIB", "wwpLeosVplsEncapTunnelId"),
        ("WWP-LEOS-VPLS-MIB", "wwpLeosVplsEncapTunnelName"),
        ("WWP-LEOS-VPLS-MIB", "wwpLeosVplsEncapTunnelId"),
        ("WWP-LEOS-VPLS-MIB", "wwpLeosVplsEncapTunnelName"),
        ("WWP-LEOS-VPLS-MIB", "wwpLeosVplsEncapTunnelActive"),
        ("WWP-LEOS-VPLS-MIB", "wwpLeosVplsEncapTunnelBVID"))
)
if mibBuilder.loadTexts:
    wwpLeosPbtTunnelActivateNotification.setStatus(
        "current"
    )

wwpLeosPbtTunnelDeactivateNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 38, 2, 0, 4)
)
wwpLeosPbtTunnelDeactivateNotification.setObjects(
      *(("WWP-LEOS-VPLS-MIB", "wwpLeosVplsEncapTunnelId"),
        ("WWP-LEOS-VPLS-MIB", "wwpLeosVplsEncapTunnelName"),
        ("WWP-LEOS-VPLS-MIB", "wwpLeosVplsEncapTunnelId"),
        ("WWP-LEOS-VPLS-MIB", "wwpLeosVplsEncapTunnelName"),
        ("WWP-LEOS-VPLS-MIB", "wwpLeosVplsEncapTunnelActive"),
        ("WWP-LEOS-VPLS-MIB", "wwpLeosVplsEncapTunnelBVID"))
)
if mibBuilder.loadTexts:
    wwpLeosPbtTunnelDeactivateNotification.setStatus(
        "current"
    )

wwpLeosTcePbtTunnelActivateNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 38, 2, 0, 10)
)
wwpLeosTcePbtTunnelActivateNotification.setObjects(
      *(("WWP-LEOS-PBT-MIB", "wwpLeosTcePbtEncapTnlIndex"),
        ("WWP-LEOS-PBT-MIB", "wwpLeosTcePbtEncapTnlName"),
        ("WWP-LEOS-PBT-MIB", "wwpLeosTcePbtTnlGroupIndex"),
        ("WWP-LEOS-PBT-MIB", "wwpLeosTcePbtTnlGroupName"),
        ("WWP-LEOS-PBT-MIB", "wwpLeosTcePbtEncapTnlFwdState"))
)
if mibBuilder.loadTexts:
    wwpLeosTcePbtTunnelActivateNotification.setStatus(
        "current"
    )

wwpLeosTcePbtTunnelDeactivateNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 38, 2, 0, 11)
)
wwpLeosTcePbtTunnelDeactivateNotification.setObjects(
      *(("WWP-LEOS-PBT-MIB", "wwpLeosTcePbtEncapTnlIndex"),
        ("WWP-LEOS-PBT-MIB", "wwpLeosTcePbtEncapTnlName"),
        ("WWP-LEOS-PBT-MIB", "wwpLeosTcePbtTnlGroupIndex"),
        ("WWP-LEOS-PBT-MIB", "wwpLeosTcePbtTnlGroupName"),
        ("WWP-LEOS-PBT-MIB", "wwpLeosTcePbtEncapTnlFwdState"))
)
if mibBuilder.loadTexts:
    wwpLeosTcePbtTunnelDeactivateNotification.setStatus(
        "current"
    )

wwpLeosTcePbtTunnelReversionNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 38, 2, 0, 12)
)
wwpLeosTcePbtTunnelReversionNotification.setObjects(
      *(("WWP-LEOS-PBT-MIB", "wwpLeosTcePbtTnlGroupIndex"),
        ("WWP-LEOS-PBT-MIB", "wwpLeosTcePbtTnlGroupName"),
        ("WWP-LEOS-PBT-MIB", "wwpLeosTcePbtEncapTnlReversionToPairIndex"),
        ("WWP-LEOS-PBT-MIB", "wwpLeosTcePbtEncapTnlReversionFromPairIndex"))
)
if mibBuilder.loadTexts:
    wwpLeosTcePbtTunnelReversionNotification.setStatus(
        "current"
    )


# Notifications groups

pbtNotificationGroups = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 38, 3, 2, 6)
)
pbtNotificationGroups.setObjects(
      *(("WWP-LEOS-PBT-MIB", "wwpLeosPbtTunnelFaultNotification"),
        ("WWP-LEOS-PBT-MIB", "wwpLeosTcePbtTunnelActivateNotification"),
        ("WWP-LEOS-PBT-MIB", "wwpLeosTcePbtTunnelDeactivateNotification"),
        ("WWP-LEOS-PBT-MIB", "wwpLeosTcePbtTunnelReversionNotification"))
)
if mibBuilder.loadTexts:
    pbtNotificationGroups.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "WWP-LEOS-PBT-MIB",
    **{"wwpLeosPbtMIB": wwpLeosPbtMIB,
       "wwpLeosPbtMIBObjects": wwpLeosPbtMIBObjects,
       "wwpLeosPbt": wwpLeosPbt,
       "wwpLeosPbtGlobalAttrs": wwpLeosPbtGlobalAttrs,
       "wwpLeosPbtBridgeMac": wwpLeosPbtBridgeMac,
       "wwpLeosPbtServiceTagEType": wwpLeosPbtServiceTagEType,
       "wwpLeosPbtTunnelTagEtype": wwpLeosPbtTunnelTagEtype,
       "wwpLeosPbtTunnelReversionState": wwpLeosPbtTunnelReversionState,
       "wwpLeosPbtTunnelReversionHoldTime": wwpLeosPbtTunnelReversionHoldTime,
       "wwpLeosPbtTransitTunnelEtypeRemark": wwpLeosPbtTransitTunnelEtypeRemark,
       "wwpLeosPbtAdminMode": wwpLeosPbtAdminMode,
       "wwpLeosPbtOperMode": wwpLeosPbtOperMode,
       "wwpLeosPbtServiceVlanTpid": wwpLeosPbtServiceVlanTpid,
       "wwpLeosPbtTunnelSwitchOverHoldTime": wwpLeosPbtTunnelSwitchOverHoldTime,
       "wwpLeosPbtBridgeNameMacMapTable": wwpLeosPbtBridgeNameMacMapTable,
       "wwpLeosPbtBridgeNameMacMapEntry": wwpLeosPbtBridgeNameMacMapEntry,
       "wwpLeosPbtBridgeNameMacMapIndex": wwpLeosPbtBridgeNameMacMapIndex,
       "wwpLeosPbtBridgeNameMacMapBridgeName": wwpLeosPbtBridgeNameMacMapBridgeName,
       "wwpLeosPbtBridgeNameMacMapMacAddr": wwpLeosPbtBridgeNameMacMapMacAddr,
       "wwpLeosPbtBridgeNameMacMapUseCount": wwpLeosPbtBridgeNameMacMapUseCount,
       "wwpLeosPbtBridgeNameMacMapRowStatus": wwpLeosPbtBridgeNameMacMapRowStatus,
       "wwpLeosPbtReservedBVIDTable": wwpLeosPbtReservedBVIDTable,
       "wwpLeosPbtReservedBVIDEntry": wwpLeosPbtReservedBVIDEntry,
       "wwpLeosPbtReservedBVID": wwpLeosPbtReservedBVID,
       "wwpLeosPbtReservedBVIDRowStatus": wwpLeosPbtReservedBVIDRowStatus,
       "wwpLeosPbtVirtualCircuitTable": wwpLeosPbtVirtualCircuitTable,
       "wwpLeosPbtVirtualCircuitEntry": wwpLeosPbtVirtualCircuitEntry,
       "wwpLeosPbtVirtualCircuitIndex": wwpLeosPbtVirtualCircuitIndex,
       "wwpLeosPbtVirtualCircuitName": wwpLeosPbtVirtualCircuitName,
       "wwpLeosPbtVirtualCircuitFixedEncapTunnelId": wwpLeosPbtVirtualCircuitFixedEncapTunnelId,
       "wwpLeosPbtVirtualCircuitDestBridgeIndex": wwpLeosPbtVirtualCircuitDestBridgeIndex,
       "wwpLeosPbtVirtualCircuitIngressISID": wwpLeosPbtVirtualCircuitIngressISID,
       "wwpLeosPbtVirtualCircuitEgressISID": wwpLeosPbtVirtualCircuitEgressISID,
       "wwpLeosPbtVirtualCircuitOperState": wwpLeosPbtVirtualCircuitOperState,
       "wwpLeosPbtVirtualCircuitEncapTunnelIdInUse": wwpLeosPbtVirtualCircuitEncapTunnelIdInUse,
       "wwpLeosPbtVirtualCircuitRowStatus": wwpLeosPbtVirtualCircuitRowStatus,
       "wwpLeosPbtVirtualCircuitRetainSTAG": wwpLeosPbtVirtualCircuitRetainSTAG,
       "wwpLeosPbtVirtualCircuitStag": wwpLeosPbtVirtualCircuitStag,
       "wwpLeosPbtVirtualCircuitStatsTable": wwpLeosPbtVirtualCircuitStatsTable,
       "wwpLeosPbtVirtualCircuitStatsEntry": wwpLeosPbtVirtualCircuitStatsEntry,
       "wwpLeosPbtVirtualCircuitTxBytesHi": wwpLeosPbtVirtualCircuitTxBytesHi,
       "wwpLeosPbtVirtualCircuitTxBytesLo": wwpLeosPbtVirtualCircuitTxBytesLo,
       "wwpLeosPbtVirtualCircuitRxBytesHi": wwpLeosPbtVirtualCircuitRxBytesHi,
       "wwpLeosPbtVirtualCircuitRxBytesLo": wwpLeosPbtVirtualCircuitRxBytesLo,
       "wwpLeosPbtLocalBridgeNameMacMapTable": wwpLeosPbtLocalBridgeNameMacMapTable,
       "wwpLeosPbtLocalBridgeNameMacMapEntry": wwpLeosPbtLocalBridgeNameMacMapEntry,
       "wwpLeosPbtLocalBridgeNameMacMapIndex": wwpLeosPbtLocalBridgeNameMacMapIndex,
       "wwpLeosPbtLocalBridgeNameMacMapBridgeName": wwpLeosPbtLocalBridgeNameMacMapBridgeName,
       "wwpLeosPbtLocalBridgeNameMacMapMacAddr": wwpLeosPbtLocalBridgeNameMacMapMacAddr,
       "wwpLeosPbtLocalBridgeNameMacMapUseCount": wwpLeosPbtLocalBridgeNameMacMapUseCount,
       "wwpLeosPbtLocalBridgeNameMacMapRowStatus": wwpLeosPbtLocalBridgeNameMacMapRowStatus,
       "wwpLeosTcePbt": wwpLeosTcePbt,
       "wwpLeosTcePbtServiceTable": wwpLeosTcePbtServiceTable,
       "wwpLeosTcePbtServiceEntry": wwpLeosTcePbtServiceEntry,
       "wwpLeosTcePbtServiceIndex": wwpLeosTcePbtServiceIndex,
       "wwpLeosTcePbtServiceName": wwpLeosTcePbtServiceName,
       "wwpLeosTcePbtServiceOperStatus": wwpLeosTcePbtServiceOperStatus,
       "wwpLeosTcePbtServiceFloodContProfileId": wwpLeosTcePbtServiceFloodContProfileId,
       "wwpLeosTcePbtServiceFloodContProfileName": wwpLeosTcePbtServiceFloodContProfileName,
       "wwpLeosTcePbtServiceVsIndex": wwpLeosTcePbtServiceVsIndex,
       "wwpLeosTcePbtServiceVsName": wwpLeosTcePbtServiceVsName,
       "wwpLeosTcePbtServiceTnlGroupIndex": wwpLeosTcePbtServiceTnlGroupIndex,
       "wwpLeosTcePbtServiceTnlGroupName": wwpLeosTcePbtServiceTnlGroupName,
       "wwpLeosTcePbtServiceIngressIsId": wwpLeosTcePbtServiceIngressIsId,
       "wwpLeosTcePbtServiceEgressIsId": wwpLeosTcePbtServiceEgressIsId,
       "wwpLeosTcePbtServiceFixedEgressPcp": wwpLeosTcePbtServiceFixedEgressPcp,
       "wwpLeosTcePbtServiceFrameCosPolicy": wwpLeosTcePbtServiceFrameCosPolicy,
       "wwpLeosTcePbtServiceFrameCosMapIndex": wwpLeosTcePbtServiceFrameCosMapIndex,
       "wwpLeosTcePbtServiceFrameCosMapName": wwpLeosTcePbtServiceFrameCosMapName,
       "wwpLeosTcePbtServiceResolvedCosPolicy": wwpLeosTcePbtServiceResolvedCosPolicy,
       "wwpLeosTcePbtServiceResolvedCosProfileIndex": wwpLeosTcePbtServiceResolvedCosProfileIndex,
       "wwpLeosTcePbtServiceResolvedCosProfileName": wwpLeosTcePbtServiceResolvedCosProfileName,
       "wwpLeosTcePbtServiceIngressMeterProfileId": wwpLeosTcePbtServiceIngressMeterProfileId,
       "wwpLeosTcePbtServiceIngressMeterProfileName": wwpLeosTcePbtServiceIngressMeterProfileName,
       "wwpLeosTcePbtServiceIngressMeterPolicy": wwpLeosTcePbtServiceIngressMeterPolicy,
       "wwpLeosTcePbtServiceRowStatus": wwpLeosTcePbtServiceRowStatus,
       "wwpLeosTcePbtTnlGroupTable": wwpLeosTcePbtTnlGroupTable,
       "wwpLeosTcePbtTnlGroupEntry": wwpLeosTcePbtTnlGroupEntry,
       "wwpLeosTcePbtTnlGroupIndex": wwpLeosTcePbtTnlGroupIndex,
       "wwpLeosTcePbtTnlGroupName": wwpLeosTcePbtTnlGroupName,
       "wwpLeosTcePbtTnlGroupSyncEnabled": wwpLeosTcePbtTnlGroupSyncEnabled,
       "wwpLeosTcePbtTnlGroupOperStatus": wwpLeosTcePbtTnlGroupOperStatus,
       "wwpLeosTcePbtTnlGroupUseCount": wwpLeosTcePbtTnlGroupUseCount,
       "wwpLeosTcePbtTnlGroupActivePair": wwpLeosTcePbtTnlGroupActivePair,
       "wwpLeosTcePbtTnlGroupReverting": wwpLeosTcePbtTnlGroupReverting,
       "wwpLeosTcePbtTnlGroupRowStatus": wwpLeosTcePbtTnlGroupRowStatus,
       "wwpLeosTcePbtEncapTnlTable": wwpLeosTcePbtEncapTnlTable,
       "wwpLeosTcePbtEncapTnlEntry": wwpLeosTcePbtEncapTnlEntry,
       "wwpLeosTcePbtEncapTnlIndex": wwpLeosTcePbtEncapTnlIndex,
       "wwpLeosTcePbtEncapTnlName": wwpLeosTcePbtEncapTnlName,
       "wwpLeosTcePbtEncapTnlRemoteBridgeIndex": wwpLeosTcePbtEncapTnlRemoteBridgeIndex,
       "wwpLeosTcePbtEncapTnlRemoteBridgeName": wwpLeosTcePbtEncapTnlRemoteBridgeName,
       "wwpLeosTcePbtEncapTnlGroupIndex": wwpLeosTcePbtEncapTnlGroupIndex,
       "wwpLeosTcePbtEncapTnlGroupName": wwpLeosTcePbtEncapTnlGroupName,
       "wwpLeosTcePbtEncapTnlBvId": wwpLeosTcePbtEncapTnlBvId,
       "wwpLeosTcePbtEncapTnlPgId": wwpLeosTcePbtEncapTnlPgId,
       "wwpLeosTcePbtEncapTnlPortName": wwpLeosTcePbtEncapTnlPortName,
       "wwpLeosTcePbtEncapTnlFaults": wwpLeosTcePbtEncapTnlFaults,
       "wwpLeosTcePbtEncapTnlAdminState": wwpLeosTcePbtEncapTnlAdminState,
       "wwpLeosTcePbtEncapTnlOperState": wwpLeosTcePbtEncapTnlOperState,
       "wwpLeosTcePbtEncapTnlFwdState": wwpLeosTcePbtEncapTnlFwdState,
       "wwpLeosTcePbtEncapTnlPaired": wwpLeosTcePbtEncapTnlPaired,
       "wwpLeosTcePbtEncapTnlPairIndex": wwpLeosTcePbtEncapTnlPairIndex,
       "wwpLeosTcePbtEncapTnlPairOperState": wwpLeosTcePbtEncapTnlPairOperState,
       "wwpLeosTcePbtEncapTnlFrameCosPolicy": wwpLeosTcePbtEncapTnlFrameCosPolicy,
       "wwpLeosTcePbtEncapTnlFrameCosMapIndex": wwpLeosTcePbtEncapTnlFrameCosMapIndex,
       "wwpLeosTcePbtEncapTnlFrameCosMapName": wwpLeosTcePbtEncapTnlFrameCosMapName,
       "wwpLeosTcePbtEncapTnlFixedPcp": wwpLeosTcePbtEncapTnlFixedPcp,
       "wwpLeosTcePbtEncapTnlCfmConfigured": wwpLeosTcePbtEncapTnlCfmConfigured,
       "wwpLeosTcePbtEncapTnlPairedDecapIndex": wwpLeosTcePbtEncapTnlPairedDecapIndex,
       "wwpLeosTcePbtEncapTnlPairedDecapName": wwpLeosTcePbtEncapTnlPairedDecapName,
       "wwpLeosTcePbtEncapTnlWeight": wwpLeosTcePbtEncapTnlWeight,
       "wwpLeosTcePbtEncapTnlStatsEnabled": wwpLeosTcePbtEncapTnlStatsEnabled,
       "wwpLeosTcePbtEncapTnlLocalBridgeIndex": wwpLeosTcePbtEncapTnlLocalBridgeIndex,
       "wwpLeosTcePbtEncapTnlLocalBridgeName": wwpLeosTcePbtEncapTnlLocalBridgeName,
       "wwpLeosTcePbtEncapTnlReversionToPairIndex": wwpLeosTcePbtEncapTnlReversionToPairIndex,
       "wwpLeosTcePbtEncapTnlReversionFromPairIndex": wwpLeosTcePbtEncapTnlReversionFromPairIndex,
       "wwpLeosTcePbtEncapTnlRowStatus": wwpLeosTcePbtEncapTnlRowStatus,
       "wwpLeosTcePbtDecapTnlTable": wwpLeosTcePbtDecapTnlTable,
       "wwpLeosTcePbtDecapTnlEntry": wwpLeosTcePbtDecapTnlEntry,
       "wwpLeosTcePbtDecapTnlIndex": wwpLeosTcePbtDecapTnlIndex,
       "wwpLeosTcePbtDecapTnlName": wwpLeosTcePbtDecapTnlName,
       "wwpLeosTcePbtDecapTnlRemoteBridgeIndex": wwpLeosTcePbtDecapTnlRemoteBridgeIndex,
       "wwpLeosTcePbtDecapTnlRemoteBridgeName": wwpLeosTcePbtDecapTnlRemoteBridgeName,
       "wwpLeosTcePbtDecapTnlGroupIndex": wwpLeosTcePbtDecapTnlGroupIndex,
       "wwpLeosTcePbtDecapTnlGroupName": wwpLeosTcePbtDecapTnlGroupName,
       "wwpLeosTcePbtDecapTnlBvId": wwpLeosTcePbtDecapTnlBvId,
       "wwpLeosTcePbtDecapTnlPgId": wwpLeosTcePbtDecapTnlPgId,
       "wwpLeosTcePbtDecapTnlPortName": wwpLeosTcePbtDecapTnlPortName,
       "wwpLeosTcePbtDecapTnlFaults": wwpLeosTcePbtDecapTnlFaults,
       "wwpLeosTcePbtDecapTnlOperState": wwpLeosTcePbtDecapTnlOperState,
       "wwpLeosTcePbtDecapTnlFwdState": wwpLeosTcePbtDecapTnlFwdState,
       "wwpLeosTcePbtDecapTnlPaired": wwpLeosTcePbtDecapTnlPaired,
       "wwpLeosTcePbtDecapTnlPairIndex": wwpLeosTcePbtDecapTnlPairIndex,
       "wwpLeosTcePbtDecapTnlPairOperState": wwpLeosTcePbtDecapTnlPairOperState,
       "wwpLeosTcePbtDecapTnlResolvedCosPolicy": wwpLeosTcePbtDecapTnlResolvedCosPolicy,
       "wwpLeosTcePbtDecapTnlResolvedCosMapIndex": wwpLeosTcePbtDecapTnlResolvedCosMapIndex,
       "wwpLeosTcePbtDecapTnlResolvedCosMapName": wwpLeosTcePbtDecapTnlResolvedCosMapName,
       "wwpLeosTcePbtDecapTnlCfmConfigured": wwpLeosTcePbtDecapTnlCfmConfigured,
       "wwpLeosTcePbtDecapTnlPairedEncapIndex": wwpLeosTcePbtDecapTnlPairedEncapIndex,
       "wwpLeosTcePbtDecapTnlPairedEncapName": wwpLeosTcePbtDecapTnlPairedEncapName,
       "wwpLeosTcePbtDecapTnlStatsEnabled": wwpLeosTcePbtDecapTnlStatsEnabled,
       "wwpLeosTcePbtDecapTnlRowStatus": wwpLeosTcePbtDecapTnlRowStatus,
       "wwpLeosTcePbtServiceUserFrameL2TransformTable": wwpLeosTcePbtServiceUserFrameL2TransformTable,
       "wwpLeosTcePbtServiceUserFrameL2TransformEntry": wwpLeosTcePbtServiceUserFrameL2TransformEntry,
       "wwpLeosTcePbtServiceUserFrameL2TransformDirection": wwpLeosTcePbtServiceUserFrameL2TransformDirection,
       "wwpLeosTcePbtServiceUserFrameL2TransformTagIndex": wwpLeosTcePbtServiceUserFrameL2TransformTagIndex,
       "wwpLeosTcePbtServiceUserFrameL2TransformTagAction": wwpLeosTcePbtServiceUserFrameL2TransformTagAction,
       "wwpLeosTcePbtServiceUserFrameL2TransformTagValue": wwpLeosTcePbtServiceUserFrameL2TransformTagValue,
       "wwpLeosTcePbtServiceUserFrameL2TransformTagEtype": wwpLeosTcePbtServiceUserFrameL2TransformTagEtype,
       "wwpLeosTcePbtServiceUserFrameL2TransformTagPriority": wwpLeosTcePbtServiceUserFrameL2TransformTagPriority,
       "wwpLeosTcePbtServiceUserFrameL2TransformPriPolicy": wwpLeosTcePbtServiceUserFrameL2TransformPriPolicy,
       "wwpLeosTcePbtServiceUserFrameL2TransformUseTagValue": wwpLeosTcePbtServiceUserFrameL2TransformUseTagValue,
       "wwpLeosTcePbtServiceUserFrameL2TransformUseTagEtype": wwpLeosTcePbtServiceUserFrameL2TransformUseTagEtype,
       "wwpLeosPbtMIBNotificationPrefix": wwpLeosPbtMIBNotificationPrefix,
       "wwpLeosPbtMIBNotifications": wwpLeosPbtMIBNotifications,
       "wwpLeosPbtTunnelFaultNotification": wwpLeosPbtTunnelFaultNotification,
       "wwpLeosPbtTunnelReversionNotification": wwpLeosPbtTunnelReversionNotification,
       "wwpLeosPbtTunnelActivateNotification": wwpLeosPbtTunnelActivateNotification,
       "wwpLeosPbtTunnelDeactivateNotification": wwpLeosPbtTunnelDeactivateNotification,
       "wwpLeosTcePbtTunnelActivateNotification": wwpLeosTcePbtTunnelActivateNotification,
       "wwpLeosTcePbtTunnelDeactivateNotification": wwpLeosTcePbtTunnelDeactivateNotification,
       "wwpLeosTcePbtTunnelReversionNotification": wwpLeosTcePbtTunnelReversionNotification,
       "wwpLeosPbtMIBConformance": wwpLeosPbtMIBConformance,
       "wwpLeosPbtMIBCompliances": wwpLeosPbtMIBCompliances,
       "wwpLeosPbtMIBGroups": wwpLeosPbtMIBGroups,
       "pbtGlobalConfigGroup": pbtGlobalConfigGroup,
       "pbtBridgeNameMacMapGroup": pbtBridgeNameMacMapGroup,
       "pbtReserveBvidGroup": pbtReserveBvidGroup,
       "pbtVirtualCircuitGroup": pbtVirtualCircuitGroup,
       "pbtVirtualCircuitStatsGroup": pbtVirtualCircuitStatsGroup,
       "pbtNotificationGroups": pbtNotificationGroups}
)
