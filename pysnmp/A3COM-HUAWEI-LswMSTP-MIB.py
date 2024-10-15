# SNMP MIB module (A3COM-HUAWEI-LswMSTP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/A3COM-HUAWEI-LswMSTP-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:28:26 2024
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

(lswCommon,) = mibBuilder.importSymbols(
    "A3COM-HUAWEI-OID-MIB",
    "lswCommon")

(dot1dStpPort,
 dot1dStpPortEntry) = mibBuilder.importSymbols(
    "BRIDGE-MIB",
    "dot1dStpPort",
    "dot1dStpPortEntry")

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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

hwdot1sMstp = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 23, 1, 14)
)
hwdot1sMstp.setRevisions(
        ("2001-06-29 00:00",)
)


# Types definitions



class BridgeId(OctetString):
    """Custom type BridgeId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )




# TEXTUAL-CONVENTIONS



class EnabledStatus(Integer32, TextualConvention):
    status = "current"
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



class Hwdot1sFormatStatus(Integer32, TextualConvention):
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
        *(("auto", 3),
          ("dot1s", 2),
          ("legacy", 1))
    )



# MIB Managed Objects in the order of their OIDs

_HwMstpEventsV2_ObjectIdentity = ObjectIdentity
hwMstpEventsV2 = _HwMstpEventsV2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 23, 1, 14, 0)
)
if mibBuilder.loadTexts:
    hwMstpEventsV2.setStatus("current")


class _Hwdot1sStpStatus_Type(EnabledStatus):
    """Custom type hwdot1sStpStatus based on EnabledStatus"""
    defaultValue = 2


_Hwdot1sStpStatus_Object = MibScalar
hwdot1sStpStatus = _Hwdot1sStpStatus_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 23, 1, 14, 1),
    _Hwdot1sStpStatus_Type()
)
hwdot1sStpStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwdot1sStpStatus.setStatus("current")


class _Hwdot1sStpForceVersion_Type(Integer32):
    """Custom type hwdot1sStpForceVersion based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("mstp", 3),
          ("rstp", 2),
          ("stp", 0))
    )


_Hwdot1sStpForceVersion_Type.__name__ = "Integer32"
_Hwdot1sStpForceVersion_Object = MibScalar
hwdot1sStpForceVersion = _Hwdot1sStpForceVersion_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 23, 1, 14, 2),
    _Hwdot1sStpForceVersion_Type()
)
hwdot1sStpForceVersion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwdot1sStpForceVersion.setStatus("current")


class _Hwdot1sStpDiameter_Type(Integer32):
    """Custom type hwdot1sStpDiameter based on Integer32"""
    defaultValue = 7

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 7),
    )


_Hwdot1sStpDiameter_Type.__name__ = "Integer32"
_Hwdot1sStpDiameter_Object = MibScalar
hwdot1sStpDiameter = _Hwdot1sStpDiameter_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 23, 1, 14, 3),
    _Hwdot1sStpDiameter_Type()
)
hwdot1sStpDiameter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwdot1sStpDiameter.setStatus("current")


class _Hwdot1sMstBridgeMaxHops_Type(Integer32):
    """Custom type hwdot1sMstBridgeMaxHops based on Integer32"""
    defaultValue = 20

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 40),
    )


_Hwdot1sMstBridgeMaxHops_Type.__name__ = "Integer32"
_Hwdot1sMstBridgeMaxHops_Object = MibScalar
hwdot1sMstBridgeMaxHops = _Hwdot1sMstBridgeMaxHops_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 23, 1, 14, 4),
    _Hwdot1sMstBridgeMaxHops_Type()
)
hwdot1sMstBridgeMaxHops.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwdot1sMstBridgeMaxHops.setStatus("current")
_Hwdot1sMstMasterBridgeID_Type = BridgeId
_Hwdot1sMstMasterBridgeID_Object = MibScalar
hwdot1sMstMasterBridgeID = _Hwdot1sMstMasterBridgeID_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 23, 1, 14, 5),
    _Hwdot1sMstMasterBridgeID_Type()
)
hwdot1sMstMasterBridgeID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwdot1sMstMasterBridgeID.setStatus("current")


class _Hwdot1sMstMasterPathCost_Type(Integer32):
    """Custom type hwdot1sMstMasterPathCost based on Integer32"""
    defaultValue = 0


_Hwdot1sMstMasterPathCost_Object = MibScalar
hwdot1sMstMasterPathCost = _Hwdot1sMstMasterPathCost_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 23, 1, 14, 6),
    _Hwdot1sMstMasterPathCost_Type()
)
hwdot1sMstMasterPathCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwdot1sMstMasterPathCost.setStatus("current")


class _Hwdot1sMstBpduGuard_Type(EnabledStatus):
    """Custom type hwdot1sMstBpduGuard based on EnabledStatus"""


_Hwdot1sMstBpduGuard_Object = MibScalar
hwdot1sMstBpduGuard = _Hwdot1sMstBpduGuard_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 23, 1, 14, 7),
    _Hwdot1sMstBpduGuard_Type()
)
hwdot1sMstBpduGuard.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwdot1sMstBpduGuard.setStatus("current")


class _Hwdot1sMstAdminFormatSelector_Type(Integer32):
    """Custom type hwdot1sMstAdminFormatSelector based on Integer32"""
    defaultValue = 0


_Hwdot1sMstAdminFormatSelector_Object = MibScalar
hwdot1sMstAdminFormatSelector = _Hwdot1sMstAdminFormatSelector_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 23, 1, 14, 8),
    _Hwdot1sMstAdminFormatSelector_Type()
)
hwdot1sMstAdminFormatSelector.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwdot1sMstAdminFormatSelector.setStatus("current")


class _Hwdot1sMstAdminRegionName_Type(OctetString):
    """Custom type hwdot1sMstAdminRegionName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_Hwdot1sMstAdminRegionName_Type.__name__ = "OctetString"
_Hwdot1sMstAdminRegionName_Object = MibScalar
hwdot1sMstAdminRegionName = _Hwdot1sMstAdminRegionName_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 23, 1, 14, 9),
    _Hwdot1sMstAdminRegionName_Type()
)
hwdot1sMstAdminRegionName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwdot1sMstAdminRegionName.setStatus("current")


class _Hwdot1sMstAdminRevisionLevel_Type(Integer32):
    """Custom type hwdot1sMstAdminRevisionLevel based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Hwdot1sMstAdminRevisionLevel_Type.__name__ = "Integer32"
_Hwdot1sMstAdminRevisionLevel_Object = MibScalar
hwdot1sMstAdminRevisionLevel = _Hwdot1sMstAdminRevisionLevel_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 23, 1, 14, 10),
    _Hwdot1sMstAdminRevisionLevel_Type()
)
hwdot1sMstAdminRevisionLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwdot1sMstAdminRevisionLevel.setStatus("current")


class _Hwdot1sMstOperFormatSelector_Type(Integer32):
    """Custom type hwdot1sMstOperFormatSelector based on Integer32"""
    defaultValue = 0


_Hwdot1sMstOperFormatSelector_Object = MibScalar
hwdot1sMstOperFormatSelector = _Hwdot1sMstOperFormatSelector_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 23, 1, 14, 11),
    _Hwdot1sMstOperFormatSelector_Type()
)
hwdot1sMstOperFormatSelector.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwdot1sMstOperFormatSelector.setStatus("current")


class _Hwdot1sMstOperRegionName_Type(OctetString):
    """Custom type hwdot1sMstOperRegionName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Hwdot1sMstOperRegionName_Type.__name__ = "OctetString"
_Hwdot1sMstOperRegionName_Object = MibScalar
hwdot1sMstOperRegionName = _Hwdot1sMstOperRegionName_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 23, 1, 14, 12),
    _Hwdot1sMstOperRegionName_Type()
)
hwdot1sMstOperRegionName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwdot1sMstOperRegionName.setStatus("current")


class _Hwdot1sMstOperRevisionLevel_Type(Integer32):
    """Custom type hwdot1sMstOperRevisionLevel based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Hwdot1sMstOperRevisionLevel_Type.__name__ = "Integer32"
_Hwdot1sMstOperRevisionLevel_Object = MibScalar
hwdot1sMstOperRevisionLevel = _Hwdot1sMstOperRevisionLevel_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 23, 1, 14, 13),
    _Hwdot1sMstOperRevisionLevel_Type()
)
hwdot1sMstOperRevisionLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwdot1sMstOperRevisionLevel.setStatus("current")


class _Hwdot1sMstOperConfigDigest_Type(OctetString):
    """Custom type hwdot1sMstOperConfigDigest based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_Hwdot1sMstOperConfigDigest_Type.__name__ = "OctetString"
_Hwdot1sMstOperConfigDigest_Object = MibScalar
hwdot1sMstOperConfigDigest = _Hwdot1sMstOperConfigDigest_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 23, 1, 14, 14),
    _Hwdot1sMstOperConfigDigest_Type()
)
hwdot1sMstOperConfigDigest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwdot1sMstOperConfigDigest.setStatus("current")


class _Hwdot1sMstRegionConfActive_Type(Integer32):
    """Custom type hwdot1sMstRegionConfActive based on Integer32"""
    defaultValue = 2

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


_Hwdot1sMstRegionConfActive_Type.__name__ = "Integer32"
_Hwdot1sMstRegionConfActive_Object = MibScalar
hwdot1sMstRegionConfActive = _Hwdot1sMstRegionConfActive_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 23, 1, 14, 15),
    _Hwdot1sMstRegionConfActive_Type()
)
hwdot1sMstRegionConfActive.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwdot1sMstRegionConfActive.setStatus("current")


class _Hwdot1sMstDefaultVlanAllo_Type(Integer32):
    """Custom type hwdot1sMstDefaultVlanAllo based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              65535)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("unused", 65535))
    )


_Hwdot1sMstDefaultVlanAllo_Type.__name__ = "Integer32"
_Hwdot1sMstDefaultVlanAllo_Object = MibScalar
hwdot1sMstDefaultVlanAllo = _Hwdot1sMstDefaultVlanAllo_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 23, 1, 14, 16),
    _Hwdot1sMstDefaultVlanAllo_Type()
)
hwdot1sMstDefaultVlanAllo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwdot1sMstDefaultVlanAllo.setStatus("current")


class _Hwdot1sMstDefaultRegionName_Type(Integer32):
    """Custom type hwdot1sMstDefaultRegionName based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              65535)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("unused", 65535))
    )


_Hwdot1sMstDefaultRegionName_Type.__name__ = "Integer32"
_Hwdot1sMstDefaultRegionName_Object = MibScalar
hwdot1sMstDefaultRegionName = _Hwdot1sMstDefaultRegionName_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 23, 1, 14, 17),
    _Hwdot1sMstDefaultRegionName_Type()
)
hwdot1sMstDefaultRegionName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwdot1sMstDefaultRegionName.setStatus("current")
_Hwdot1sVIDAllocationTable_Object = MibTable
hwdot1sVIDAllocationTable = _Hwdot1sVIDAllocationTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 23, 1, 14, 18)
)
if mibBuilder.loadTexts:
    hwdot1sVIDAllocationTable.setStatus("current")
_Hwdot1sVIDAllocationEntry_Object = MibTableRow
hwdot1sVIDAllocationEntry = _Hwdot1sVIDAllocationEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 23, 1, 14, 18, 1)
)
hwdot1sVIDAllocationEntry.setIndexNames(
    (0, "A3COM-HUAWEI-LswMSTP-MIB", "hwdot1sMstVID"),
)
if mibBuilder.loadTexts:
    hwdot1sVIDAllocationEntry.setStatus("current")


class _Hwdot1sMstVID_Type(Integer32):
    """Custom type hwdot1sMstVID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_Hwdot1sMstVID_Type.__name__ = "Integer32"
_Hwdot1sMstVID_Object = MibTableColumn
hwdot1sMstVID = _Hwdot1sMstVID_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 23, 1, 14, 18, 1, 1),
    _Hwdot1sMstVID_Type()
)
hwdot1sMstVID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwdot1sMstVID.setStatus("current")


class _Hwdot1sAdminMstID_Type(Integer32):
    """Custom type hwdot1sAdminMstID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_Hwdot1sAdminMstID_Type.__name__ = "Integer32"
_Hwdot1sAdminMstID_Object = MibTableColumn
hwdot1sAdminMstID = _Hwdot1sAdminMstID_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 23, 1, 14, 18, 1, 2),
    _Hwdot1sAdminMstID_Type()
)
hwdot1sAdminMstID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwdot1sAdminMstID.setStatus("current")


class _Hwdot1sOperMstID_Type(Integer32):
    """Custom type hwdot1sOperMstID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_Hwdot1sOperMstID_Type.__name__ = "Integer32"
_Hwdot1sOperMstID_Object = MibTableColumn
hwdot1sOperMstID = _Hwdot1sOperMstID_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 23, 1, 14, 18, 1, 3),
    _Hwdot1sOperMstID_Type()
)
hwdot1sOperMstID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwdot1sOperMstID.setStatus("current")
_Hwdot1sInstanceTable_Object = MibTable
hwdot1sInstanceTable = _Hwdot1sInstanceTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 23, 1, 14, 19)
)
if mibBuilder.loadTexts:
    hwdot1sInstanceTable.setStatus("current")
_Hwdot1sInstanceEntry_Object = MibTableRow
hwdot1sInstanceEntry = _Hwdot1sInstanceEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 23, 1, 14, 19, 1)
)
hwdot1sInstanceEntry.setIndexNames(
    (0, "A3COM-HUAWEI-LswMSTP-MIB", "hwdot1sInstanceID"),
)
if mibBuilder.loadTexts:
    hwdot1sInstanceEntry.setStatus("current")


class _Hwdot1sInstanceID_Type(Integer32):
    """Custom type hwdot1sInstanceID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_Hwdot1sInstanceID_Type.__name__ = "Integer32"
_Hwdot1sInstanceID_Object = MibTableColumn
hwdot1sInstanceID = _Hwdot1sInstanceID_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 23, 1, 14, 19, 1, 1),
    _Hwdot1sInstanceID_Type()
)
hwdot1sInstanceID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwdot1sInstanceID.setStatus("current")
_Hwdot1sMstiBridgeID_Type = BridgeId
_Hwdot1sMstiBridgeID_Object = MibTableColumn
hwdot1sMstiBridgeID = _Hwdot1sMstiBridgeID_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 23, 1, 14, 19, 1, 2),
    _Hwdot1sMstiBridgeID_Type()
)
hwdot1sMstiBridgeID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwdot1sMstiBridgeID.setStatus("current")


class _Hwdot1sMstiBridgePriority_Type(Integer32):
    """Custom type hwdot1sMstiBridgePriority based on Integer32"""
    defaultValue = 32768

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 61440),
    )


_Hwdot1sMstiBridgePriority_Type.__name__ = "Integer32"
_Hwdot1sMstiBridgePriority_Object = MibTableColumn
hwdot1sMstiBridgePriority = _Hwdot1sMstiBridgePriority_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 23, 1, 14, 19, 1, 3),
    _Hwdot1sMstiBridgePriority_Type()
)
hwdot1sMstiBridgePriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwdot1sMstiBridgePriority.setStatus("current")
_Hwdot1sMstiDesignedRoot_Type = BridgeId
_Hwdot1sMstiDesignedRoot_Object = MibTableColumn
hwdot1sMstiDesignedRoot = _Hwdot1sMstiDesignedRoot_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 23, 1, 14, 19, 1, 4),
    _Hwdot1sMstiDesignedRoot_Type()
)
hwdot1sMstiDesignedRoot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwdot1sMstiDesignedRoot.setStatus("current")
_Hwdot1sMstiRootPathCost_Type = Integer32
_Hwdot1sMstiRootPathCost_Object = MibTableColumn
hwdot1sMstiRootPathCost = _Hwdot1sMstiRootPathCost_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 23, 1, 14, 19, 1, 5),
    _Hwdot1sMstiRootPathCost_Type()
)
hwdot1sMstiRootPathCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwdot1sMstiRootPathCost.setStatus("current")
_Hwdot1sMstiRootPort_Type = Integer32
_Hwdot1sMstiRootPort_Object = MibTableColumn
hwdot1sMstiRootPort = _Hwdot1sMstiRootPort_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 23, 1, 14, 19, 1, 6),
    _Hwdot1sMstiRootPort_Type()
)
hwdot1sMstiRootPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwdot1sMstiRootPort.setStatus("current")


class _Hwdot1sMstiRootType_Type(Integer32):
    """Custom type hwdot1sMstiRootType based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("normal", 0),
          ("primary", 2),
          ("secondary", 1))
    )


_Hwdot1sMstiRootType_Type.__name__ = "Integer32"
_Hwdot1sMstiRootType_Object = MibTableColumn
hwdot1sMstiRootType = _Hwdot1sMstiRootType_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 23, 1, 14, 19, 1, 7),
    _Hwdot1sMstiRootType_Type()
)
hwdot1sMstiRootType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwdot1sMstiRootType.setStatus("current")
_Hwdot1sMstiRemainingHops_Type = Integer32
_Hwdot1sMstiRemainingHops_Object = MibTableColumn
hwdot1sMstiRemainingHops = _Hwdot1sMstiRemainingHops_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 23, 1, 14, 19, 1, 8),
    _Hwdot1sMstiRemainingHops_Type()
)
hwdot1sMstiRemainingHops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwdot1sMstiRemainingHops.setStatus("current")


class _Hwdot1sMstiAdminMappedVlanListLow_Type(OctetString):
    """Custom type hwdot1sMstiAdminMappedVlanListLow based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_Hwdot1sMstiAdminMappedVlanListLow_Type.__name__ = "OctetString"
_Hwdot1sMstiAdminMappedVlanListLow_Object = MibTableColumn
hwdot1sMstiAdminMappedVlanListLow = _Hwdot1sMstiAdminMappedVlanListLow_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 23, 1, 14, 19, 1, 9),
    _Hwdot1sMstiAdminMappedVlanListLow_Type()
)
hwdot1sMstiAdminMappedVlanListLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwdot1sMstiAdminMappedVlanListLow.setStatus("current")


class _Hwdot1sMstiAdminMappedVlanListHigh_Type(OctetString):
    """Custom type hwdot1sMstiAdminMappedVlanListHigh based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_Hwdot1sMstiAdminMappedVlanListHigh_Type.__name__ = "OctetString"
_Hwdot1sMstiAdminMappedVlanListHigh_Object = MibTableColumn
hwdot1sMstiAdminMappedVlanListHigh = _Hwdot1sMstiAdminMappedVlanListHigh_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 23, 1, 14, 19, 1, 10),
    _Hwdot1sMstiAdminMappedVlanListHigh_Type()
)
hwdot1sMstiAdminMappedVlanListHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwdot1sMstiAdminMappedVlanListHigh.setStatus("current")


class _Hwdot1sMstiOperMappedVlanListLow_Type(OctetString):
    """Custom type hwdot1sMstiOperMappedVlanListLow based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_Hwdot1sMstiOperMappedVlanListLow_Type.__name__ = "OctetString"
_Hwdot1sMstiOperMappedVlanListLow_Object = MibTableColumn
hwdot1sMstiOperMappedVlanListLow = _Hwdot1sMstiOperMappedVlanListLow_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 23, 1, 14, 19, 1, 11),
    _Hwdot1sMstiOperMappedVlanListLow_Type()
)
hwdot1sMstiOperMappedVlanListLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwdot1sMstiOperMappedVlanListLow.setStatus("current")


class _Hwdot1sMstiOperMappedVlanListHigh_Type(OctetString):
    """Custom type hwdot1sMstiOperMappedVlanListHigh based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_Hwdot1sMstiOperMappedVlanListHigh_Type.__name__ = "OctetString"
_Hwdot1sMstiOperMappedVlanListHigh_Object = MibTableColumn
hwdot1sMstiOperMappedVlanListHigh = _Hwdot1sMstiOperMappedVlanListHigh_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 23, 1, 14, 19, 1, 12),
    _Hwdot1sMstiOperMappedVlanListHigh_Type()
)
hwdot1sMstiOperMappedVlanListHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwdot1sMstiOperMappedVlanListHigh.setStatus("current")
_Hwdot1sPortTable_Object = MibTable
hwdot1sPortTable = _Hwdot1sPortTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 23, 1, 14, 20)
)
if mibBuilder.loadTexts:
    hwdot1sPortTable.setStatus("current")
_Hwdot1sPortEntry_Object = MibTableRow
hwdot1sPortEntry = _Hwdot1sPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 23, 1, 14, 20, 1)
)
hwdot1sPortEntry.setIndexNames(
    (0, "A3COM-HUAWEI-LswMSTP-MIB", "hwdot1sInstanceID"),
    (0, "A3COM-HUAWEI-LswMSTP-MIB", "hwdot1sMstiPortIndex"),
)
if mibBuilder.loadTexts:
    hwdot1sPortEntry.setStatus("current")
_Hwdot1sMstiPortIndex_Type = Integer32
_Hwdot1sMstiPortIndex_Object = MibTableColumn
hwdot1sMstiPortIndex = _Hwdot1sMstiPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 23, 1, 14, 20, 1, 1),
    _Hwdot1sMstiPortIndex_Type()
)
hwdot1sMstiPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwdot1sMstiPortIndex.setStatus("current")


class _Hwdot1sMstiState_Type(Integer32):
    """Custom type hwdot1sMstiState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("discarding", 2),
          ("forwarding", 5),
          ("learning", 4))
    )


_Hwdot1sMstiState_Type.__name__ = "Integer32"
_Hwdot1sMstiState_Object = MibTableColumn
hwdot1sMstiState = _Hwdot1sMstiState_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 23, 1, 14, 20, 1, 2),
    _Hwdot1sMstiState_Type()
)
hwdot1sMstiState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwdot1sMstiState.setStatus("current")


class _Hwdot1sMstiPortPriority_Type(Integer32):
    """Custom type hwdot1sMstiPortPriority based on Integer32"""
    defaultValue = 128

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 240),
    )


_Hwdot1sMstiPortPriority_Type.__name__ = "Integer32"
_Hwdot1sMstiPortPriority_Object = MibTableColumn
hwdot1sMstiPortPriority = _Hwdot1sMstiPortPriority_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 23, 1, 14, 20, 1, 3),
    _Hwdot1sMstiPortPriority_Type()
)
hwdot1sMstiPortPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwdot1sMstiPortPriority.setStatus("current")


class _Hwdot1sMstiPathCost_Type(Integer32):
    """Custom type hwdot1sMstiPathCost based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 200000000),
    )


_Hwdot1sMstiPathCost_Type.__name__ = "Integer32"
_Hwdot1sMstiPathCost_Object = MibTableColumn
hwdot1sMstiPathCost = _Hwdot1sMstiPathCost_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 23, 1, 14, 20, 1, 4),
    _Hwdot1sMstiPathCost_Type()
)
hwdot1sMstiPathCost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwdot1sMstiPathCost.setStatus("current")
_Hwdot1sMstiDesignatedRoot_Type = BridgeId
_Hwdot1sMstiDesignatedRoot_Object = MibTableColumn
hwdot1sMstiDesignatedRoot = _Hwdot1sMstiDesignatedRoot_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 23, 1, 14, 20, 1, 5),
    _Hwdot1sMstiDesignatedRoot_Type()
)
hwdot1sMstiDesignatedRoot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwdot1sMstiDesignatedRoot.setStatus("current")
_Hwdot1sMstiDesignatedCost_Type = Integer32
_Hwdot1sMstiDesignatedCost_Object = MibTableColumn
hwdot1sMstiDesignatedCost = _Hwdot1sMstiDesignatedCost_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 23, 1, 14, 20, 1, 6),
    _Hwdot1sMstiDesignatedCost_Type()
)
hwdot1sMstiDesignatedCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwdot1sMstiDesignatedCost.setStatus("current")
_Hwdot1sMstiDesignatedBridge_Type = BridgeId
_Hwdot1sMstiDesignatedBridge_Object = MibTableColumn
hwdot1sMstiDesignatedBridge = _Hwdot1sMstiDesignatedBridge_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 23, 1, 14, 20, 1, 7),
    _Hwdot1sMstiDesignatedBridge_Type()
)
hwdot1sMstiDesignatedBridge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwdot1sMstiDesignatedBridge.setStatus("current")


class _Hwdot1sMstiDesignatedPort_Type(OctetString):
    """Custom type hwdot1sMstiDesignatedPort based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_Hwdot1sMstiDesignatedPort_Type.__name__ = "OctetString"
_Hwdot1sMstiDesignatedPort_Object = MibTableColumn
hwdot1sMstiDesignatedPort = _Hwdot1sMstiDesignatedPort_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 23, 1, 14, 20, 1, 8),
    _Hwdot1sMstiDesignatedPort_Type()
)
hwdot1sMstiDesignatedPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwdot1sMstiDesignatedPort.setStatus("current")
_Hwdot1sMstiMasterBridgeID_Type = BridgeId
_Hwdot1sMstiMasterBridgeID_Object = MibTableColumn
hwdot1sMstiMasterBridgeID = _Hwdot1sMstiMasterBridgeID_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 23, 1, 14, 20, 1, 9),
    _Hwdot1sMstiMasterBridgeID_Type()
)
hwdot1sMstiMasterBridgeID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwdot1sMstiMasterBridgeID.setStatus("current")
_Hwdot1sMstiMasterPortCost_Type = Integer32
_Hwdot1sMstiMasterPortCost_Object = MibTableColumn
hwdot1sMstiMasterPortCost = _Hwdot1sMstiMasterPortCost_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 23, 1, 14, 20, 1, 10),
    _Hwdot1sMstiMasterPortCost_Type()
)
hwdot1sMstiMasterPortCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwdot1sMstiMasterPortCost.setStatus("current")


class _Hwdot1sMstiStpPortEdgeport_Type(EnabledStatus):
    """Custom type hwdot1sMstiStpPortEdgeport based on EnabledStatus"""


_Hwdot1sMstiStpPortEdgeport_Object = MibTableColumn
hwdot1sMstiStpPortEdgeport = _Hwdot1sMstiStpPortEdgeport_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 23, 1, 14, 20, 1, 11),
    _Hwdot1sMstiStpPortEdgeport_Type()
)
hwdot1sMstiStpPortEdgeport.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwdot1sMstiStpPortEdgeport.setStatus("current")


class _Hwdot1sMstiStpPortPointToPoint_Type(Integer32):
    """Custom type hwdot1sMstiStpPortPointToPoint based on Integer32"""
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
        *(("auto", 3),
          ("forceFalse", 2),
          ("forceTrue", 1))
    )


_Hwdot1sMstiStpPortPointToPoint_Type.__name__ = "Integer32"
_Hwdot1sMstiStpPortPointToPoint_Object = MibTableColumn
hwdot1sMstiStpPortPointToPoint = _Hwdot1sMstiStpPortPointToPoint_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 23, 1, 14, 20, 1, 12),
    _Hwdot1sMstiStpPortPointToPoint_Type()
)
hwdot1sMstiStpPortPointToPoint.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwdot1sMstiStpPortPointToPoint.setStatus("current")


class _Hwdot1sMstiStpMcheck_Type(Integer32):
    """Custom type hwdot1sMstiStpMcheck based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              65535)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("unused", 65535))
    )


_Hwdot1sMstiStpMcheck_Type.__name__ = "Integer32"
_Hwdot1sMstiStpMcheck_Object = MibTableColumn
hwdot1sMstiStpMcheck = _Hwdot1sMstiStpMcheck_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 23, 1, 14, 20, 1, 13),
    _Hwdot1sMstiStpMcheck_Type()
)
hwdot1sMstiStpMcheck.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwdot1sMstiStpMcheck.setStatus("current")


class _Hwdot1sMstiStpTransLimit_Type(Integer32):
    """Custom type hwdot1sMstiStpTransLimit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_Hwdot1sMstiStpTransLimit_Type.__name__ = "Integer32"
_Hwdot1sMstiStpTransLimit_Object = MibTableColumn
hwdot1sMstiStpTransLimit = _Hwdot1sMstiStpTransLimit_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 23, 1, 14, 20, 1, 14),
    _Hwdot1sMstiStpTransLimit_Type()
)
hwdot1sMstiStpTransLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwdot1sMstiStpTransLimit.setStatus("current")
_Hwdot1sMstiStpRXStpBPDU_Type = Counter32
_Hwdot1sMstiStpRXStpBPDU_Object = MibTableColumn
hwdot1sMstiStpRXStpBPDU = _Hwdot1sMstiStpRXStpBPDU_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 23, 1, 14, 20, 1, 15),
    _Hwdot1sMstiStpRXStpBPDU_Type()
)
hwdot1sMstiStpRXStpBPDU.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwdot1sMstiStpRXStpBPDU.setStatus("current")
_Hwdot1sMstiStpTXStpBPDU_Type = Counter32
_Hwdot1sMstiStpTXStpBPDU_Object = MibTableColumn
hwdot1sMstiStpTXStpBPDU = _Hwdot1sMstiStpTXStpBPDU_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 23, 1, 14, 20, 1, 16),
    _Hwdot1sMstiStpTXStpBPDU_Type()
)
hwdot1sMstiStpTXStpBPDU.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwdot1sMstiStpTXStpBPDU.setStatus("current")
_Hwdot1sMstiStpRXTCNBPDU_Type = Counter32
_Hwdot1sMstiStpRXTCNBPDU_Object = MibTableColumn
hwdot1sMstiStpRXTCNBPDU = _Hwdot1sMstiStpRXTCNBPDU_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 23, 1, 14, 20, 1, 17),
    _Hwdot1sMstiStpRXTCNBPDU_Type()
)
hwdot1sMstiStpRXTCNBPDU.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwdot1sMstiStpRXTCNBPDU.setStatus("current")
_Hwdot1sMstiStpTXTCNBPDU_Type = Counter32
_Hwdot1sMstiStpTXTCNBPDU_Object = MibTableColumn
hwdot1sMstiStpTXTCNBPDU = _Hwdot1sMstiStpTXTCNBPDU_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 23, 1, 14, 20, 1, 18),
    _Hwdot1sMstiStpTXTCNBPDU_Type()
)
hwdot1sMstiStpTXTCNBPDU.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwdot1sMstiStpTXTCNBPDU.setStatus("current")
_Hwdot1sMstiStpRXRSTPBPDU_Type = Counter32
_Hwdot1sMstiStpRXRSTPBPDU_Object = MibTableColumn
hwdot1sMstiStpRXRSTPBPDU = _Hwdot1sMstiStpRXRSTPBPDU_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 23, 1, 14, 20, 1, 19),
    _Hwdot1sMstiStpRXRSTPBPDU_Type()
)
hwdot1sMstiStpRXRSTPBPDU.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwdot1sMstiStpRXRSTPBPDU.setStatus("current")
_Hwdot1sMstiStpTXRSTPBPDU_Type = Counter32
_Hwdot1sMstiStpTXRSTPBPDU_Object = MibTableColumn
hwdot1sMstiStpTXRSTPBPDU = _Hwdot1sMstiStpTXRSTPBPDU_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 23, 1, 14, 20, 1, 20),
    _Hwdot1sMstiStpTXRSTPBPDU_Type()
)
hwdot1sMstiStpTXRSTPBPDU.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwdot1sMstiStpTXRSTPBPDU.setStatus("current")
_Hwdot1sMstiStpRXMSTPBPDU_Type = Counter32
_Hwdot1sMstiStpRXMSTPBPDU_Object = MibTableColumn
hwdot1sMstiStpRXMSTPBPDU = _Hwdot1sMstiStpRXMSTPBPDU_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 23, 1, 14, 20, 1, 21),
    _Hwdot1sMstiStpRXMSTPBPDU_Type()
)
hwdot1sMstiStpRXMSTPBPDU.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwdot1sMstiStpRXMSTPBPDU.setStatus("current")
_Hwdot1sMstiStpTXMSTPBPDU_Type = Counter32
_Hwdot1sMstiStpTXMSTPBPDU_Object = MibTableColumn
hwdot1sMstiStpTXMSTPBPDU = _Hwdot1sMstiStpTXMSTPBPDU_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 23, 1, 14, 20, 1, 22),
    _Hwdot1sMstiStpTXMSTPBPDU_Type()
)
hwdot1sMstiStpTXMSTPBPDU.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwdot1sMstiStpTXMSTPBPDU.setStatus("current")


class _Hwdot1sMstiStpClearStatistics_Type(Integer32):
    """Custom type hwdot1sMstiStpClearStatistics based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              65535)
        )
    )
    namedValues = NamedValues(
        *(("clear", 1),
          ("unused", 65535))
    )


_Hwdot1sMstiStpClearStatistics_Type.__name__ = "Integer32"
_Hwdot1sMstiStpClearStatistics_Object = MibTableColumn
hwdot1sMstiStpClearStatistics = _Hwdot1sMstiStpClearStatistics_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 23, 1, 14, 20, 1, 23),
    _Hwdot1sMstiStpClearStatistics_Type()
)
hwdot1sMstiStpClearStatistics.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwdot1sMstiStpClearStatistics.setStatus("current")


class _Hwdot1sMstiStpDefaultPortCost_Type(Integer32):
    """Custom type hwdot1sMstiStpDefaultPortCost based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              65535)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("unused", 65535))
    )


_Hwdot1sMstiStpDefaultPortCost_Type.__name__ = "Integer32"
_Hwdot1sMstiStpDefaultPortCost_Object = MibTableColumn
hwdot1sMstiStpDefaultPortCost = _Hwdot1sMstiStpDefaultPortCost_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 23, 1, 14, 20, 1, 24),
    _Hwdot1sMstiStpDefaultPortCost_Type()
)
hwdot1sMstiStpDefaultPortCost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwdot1sMstiStpDefaultPortCost.setStatus("current")


class _Hwdot1sMstiStpStatus_Type(EnabledStatus):
    """Custom type hwdot1sMstiStpStatus based on EnabledStatus"""


_Hwdot1sMstiStpStatus_Object = MibTableColumn
hwdot1sMstiStpStatus = _Hwdot1sMstiStpStatus_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 23, 1, 14, 20, 1, 25),
    _Hwdot1sMstiStpStatus_Type()
)
hwdot1sMstiStpStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwdot1sMstiStpStatus.setStatus("current")


class _Hwdot1sMstiPortRootGuard_Type(EnabledStatus):
    """Custom type hwdot1sMstiPortRootGuard based on EnabledStatus"""


_Hwdot1sMstiPortRootGuard_Object = MibTableColumn
hwdot1sMstiPortRootGuard = _Hwdot1sMstiPortRootGuard_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 23, 1, 14, 20, 1, 26),
    _Hwdot1sMstiPortRootGuard_Type()
)
hwdot1sMstiPortRootGuard.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwdot1sMstiPortRootGuard.setStatus("current")


class _Hwdot1sMstiPortLoopGuard_Type(EnabledStatus):
    """Custom type hwdot1sMstiPortLoopGuard based on EnabledStatus"""


_Hwdot1sMstiPortLoopGuard_Object = MibTableColumn
hwdot1sMstiPortLoopGuard = _Hwdot1sMstiPortLoopGuard_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 23, 1, 14, 20, 1, 27),
    _Hwdot1sMstiPortLoopGuard_Type()
)
hwdot1sMstiPortLoopGuard.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwdot1sMstiPortLoopGuard.setStatus("current")


class _Hwdot1sMstiStpPortSendingBPDUType_Type(Integer32):
    """Custom type hwdot1sMstiStpPortSendingBPDUType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("mstp", 3),
          ("rstp", 2),
          ("stp", 1))
    )


_Hwdot1sMstiStpPortSendingBPDUType_Type.__name__ = "Integer32"
_Hwdot1sMstiStpPortSendingBPDUType_Object = MibTableColumn
hwdot1sMstiStpPortSendingBPDUType = _Hwdot1sMstiStpPortSendingBPDUType_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 23, 1, 14, 20, 1, 28),
    _Hwdot1sMstiStpPortSendingBPDUType_Type()
)
hwdot1sMstiStpPortSendingBPDUType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwdot1sMstiStpPortSendingBPDUType.setStatus("current")


class _Hwdot1sMstiStpOperPortPointToPoint_Type(Integer32):
    """Custom type hwdot1sMstiStpOperPortPointToPoint based on Integer32"""
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


_Hwdot1sMstiStpOperPortPointToPoint_Type.__name__ = "Integer32"
_Hwdot1sMstiStpOperPortPointToPoint_Object = MibTableColumn
hwdot1sMstiStpOperPortPointToPoint = _Hwdot1sMstiStpOperPortPointToPoint_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 23, 1, 14, 20, 1, 29),
    _Hwdot1sMstiStpOperPortPointToPoint_Type()
)
hwdot1sMstiStpOperPortPointToPoint.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwdot1sMstiStpOperPortPointToPoint.setStatus("current")
_Hwdot1sMstiStpPortAdminBPDUFmt_Type = Hwdot1sFormatStatus
_Hwdot1sMstiStpPortAdminBPDUFmt_Object = MibTableColumn
hwdot1sMstiStpPortAdminBPDUFmt = _Hwdot1sMstiStpPortAdminBPDUFmt_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 23, 1, 14, 20, 1, 30),
    _Hwdot1sMstiStpPortAdminBPDUFmt_Type()
)
hwdot1sMstiStpPortAdminBPDUFmt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwdot1sMstiStpPortAdminBPDUFmt.setStatus("current")
_Hwdot1sMstiStpPortOperBPDUFmt_Type = Hwdot1sFormatStatus
_Hwdot1sMstiStpPortOperBPDUFmt_Object = MibTableColumn
hwdot1sMstiStpPortOperBPDUFmt = _Hwdot1sMstiStpPortOperBPDUFmt_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 23, 1, 14, 20, 1, 31),
    _Hwdot1sMstiStpPortOperBPDUFmt_Type()
)
hwdot1sMstiStpPortOperBPDUFmt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwdot1sMstiStpPortOperBPDUFmt.setStatus("current")


class _Hwdot1sMstiStpPortRoleRestriction_Type(EnabledStatus):
    """Custom type hwdot1sMstiStpPortRoleRestriction based on EnabledStatus"""


_Hwdot1sMstiStpPortRoleRestriction_Object = MibTableColumn
hwdot1sMstiStpPortRoleRestriction = _Hwdot1sMstiStpPortRoleRestriction_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 23, 1, 14, 20, 1, 32),
    _Hwdot1sMstiStpPortRoleRestriction_Type()
)
hwdot1sMstiStpPortRoleRestriction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwdot1sMstiStpPortRoleRestriction.setStatus("current")


class _Hwdot1sMstiStpPortTcRestriction_Type(EnabledStatus):
    """Custom type hwdot1sMstiStpPortTcRestriction based on EnabledStatus"""


_Hwdot1sMstiStpPortTcRestriction_Object = MibTableColumn
hwdot1sMstiStpPortTcRestriction = _Hwdot1sMstiStpPortTcRestriction_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 23, 1, 14, 20, 1, 33),
    _Hwdot1sMstiStpPortTcRestriction_Type()
)
hwdot1sMstiStpPortTcRestriction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwdot1sMstiStpPortTcRestriction.setStatus("current")
_Hwdot1sMstiStpPortDisputed_Type = TruthValue
_Hwdot1sMstiStpPortDisputed_Object = MibTableColumn
hwdot1sMstiStpPortDisputed = _Hwdot1sMstiStpPortDisputed_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 23, 1, 14, 20, 1, 34),
    _Hwdot1sMstiStpPortDisputed_Type()
)
hwdot1sMstiStpPortDisputed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwdot1sMstiStpPortDisputed.setStatus("current")


class _Hwdot1sStpPathCostStandard_Type(Integer32):
    """Custom type hwdot1sStpPathCostStandard based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dot1d-1998", 1),
          ("dot1t", 2),
          ("legacy", 0))
    )


_Hwdot1sStpPathCostStandard_Type.__name__ = "Integer32"
_Hwdot1sStpPathCostStandard_Object = MibScalar
hwdot1sStpPathCostStandard = _Hwdot1sStpPathCostStandard_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 23, 1, 14, 21),
    _Hwdot1sStpPathCostStandard_Type()
)
hwdot1sStpPathCostStandard.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwdot1sStpPathCostStandard.setStatus("current")

# Managed Objects groups


# Notification objects

hwPortMstiStateForwarding = NotificationType(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 23, 1, 14, 0, 1)
)
hwPortMstiStateForwarding.setObjects(
      *(("A3COM-HUAWEI-LswMSTP-MIB", "hwdot1sInstanceID"),
        ("A3COM-HUAWEI-LswMSTP-MIB", "hwdot1sMstiPortIndex"))
)
if mibBuilder.loadTexts:
    hwPortMstiStateForwarding.setStatus(
        "current"
    )

hwPortMstiStateDiscarding = NotificationType(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 23, 1, 14, 0, 2)
)
hwPortMstiStateDiscarding.setObjects(
      *(("A3COM-HUAWEI-LswMSTP-MIB", "hwdot1sInstanceID"),
        ("A3COM-HUAWEI-LswMSTP-MIB", "hwdot1sMstiPortIndex"))
)
if mibBuilder.loadTexts:
    hwPortMstiStateDiscarding.setStatus(
        "current"
    )

hwBridgeLostRootPrimary = NotificationType(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 23, 1, 14, 0, 3)
)
hwBridgeLostRootPrimary.setObjects(
    ("A3COM-HUAWEI-LswMSTP-MIB", "hwdot1sInstanceID")
)
if mibBuilder.loadTexts:
    hwBridgeLostRootPrimary.setStatus(
        "current"
    )

hwPortMstiRootGuarded = NotificationType(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 23, 1, 14, 0, 4)
)
hwPortMstiRootGuarded.setObjects(
      *(("A3COM-HUAWEI-LswMSTP-MIB", "hwdot1sInstanceID"),
        ("A3COM-HUAWEI-LswMSTP-MIB", "hwdot1sMstiPortIndex"))
)
if mibBuilder.loadTexts:
    hwPortMstiRootGuarded.setStatus(
        "current"
    )

hwPortMstiBpduGuarded = NotificationType(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 23, 1, 14, 0, 5)
)
hwPortMstiBpduGuarded.setObjects(
    ("BRIDGE-MIB", "dot1dStpPort")
)
if mibBuilder.loadTexts:
    hwPortMstiBpduGuarded.setStatus(
        "current"
    )

hwPortMstiLoopGuarded = NotificationType(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 23, 1, 14, 0, 6)
)
hwPortMstiLoopGuarded.setObjects(
      *(("A3COM-HUAWEI-LswMSTP-MIB", "hwdot1sInstanceID"),
        ("A3COM-HUAWEI-LswMSTP-MIB", "hwdot1sMstiPortIndex"))
)
if mibBuilder.loadTexts:
    hwPortMstiLoopGuarded.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "A3COM-HUAWEI-LswMSTP-MIB",
    **{"EnabledStatus": EnabledStatus,
       "BridgeId": BridgeId,
       "Hwdot1sFormatStatus": Hwdot1sFormatStatus,
       "hwdot1sMstp": hwdot1sMstp,
       "hwMstpEventsV2": hwMstpEventsV2,
       "hwPortMstiStateForwarding": hwPortMstiStateForwarding,
       "hwPortMstiStateDiscarding": hwPortMstiStateDiscarding,
       "hwBridgeLostRootPrimary": hwBridgeLostRootPrimary,
       "hwPortMstiRootGuarded": hwPortMstiRootGuarded,
       "hwPortMstiBpduGuarded": hwPortMstiBpduGuarded,
       "hwPortMstiLoopGuarded": hwPortMstiLoopGuarded,
       "hwdot1sStpStatus": hwdot1sStpStatus,
       "hwdot1sStpForceVersion": hwdot1sStpForceVersion,
       "hwdot1sStpDiameter": hwdot1sStpDiameter,
       "hwdot1sMstBridgeMaxHops": hwdot1sMstBridgeMaxHops,
       "hwdot1sMstMasterBridgeID": hwdot1sMstMasterBridgeID,
       "hwdot1sMstMasterPathCost": hwdot1sMstMasterPathCost,
       "hwdot1sMstBpduGuard": hwdot1sMstBpduGuard,
       "hwdot1sMstAdminFormatSelector": hwdot1sMstAdminFormatSelector,
       "hwdot1sMstAdminRegionName": hwdot1sMstAdminRegionName,
       "hwdot1sMstAdminRevisionLevel": hwdot1sMstAdminRevisionLevel,
       "hwdot1sMstOperFormatSelector": hwdot1sMstOperFormatSelector,
       "hwdot1sMstOperRegionName": hwdot1sMstOperRegionName,
       "hwdot1sMstOperRevisionLevel": hwdot1sMstOperRevisionLevel,
       "hwdot1sMstOperConfigDigest": hwdot1sMstOperConfigDigest,
       "hwdot1sMstRegionConfActive": hwdot1sMstRegionConfActive,
       "hwdot1sMstDefaultVlanAllo": hwdot1sMstDefaultVlanAllo,
       "hwdot1sMstDefaultRegionName": hwdot1sMstDefaultRegionName,
       "hwdot1sVIDAllocationTable": hwdot1sVIDAllocationTable,
       "hwdot1sVIDAllocationEntry": hwdot1sVIDAllocationEntry,
       "hwdot1sMstVID": hwdot1sMstVID,
       "hwdot1sAdminMstID": hwdot1sAdminMstID,
       "hwdot1sOperMstID": hwdot1sOperMstID,
       "hwdot1sInstanceTable": hwdot1sInstanceTable,
       "hwdot1sInstanceEntry": hwdot1sInstanceEntry,
       "hwdot1sInstanceID": hwdot1sInstanceID,
       "hwdot1sMstiBridgeID": hwdot1sMstiBridgeID,
       "hwdot1sMstiBridgePriority": hwdot1sMstiBridgePriority,
       "hwdot1sMstiDesignedRoot": hwdot1sMstiDesignedRoot,
       "hwdot1sMstiRootPathCost": hwdot1sMstiRootPathCost,
       "hwdot1sMstiRootPort": hwdot1sMstiRootPort,
       "hwdot1sMstiRootType": hwdot1sMstiRootType,
       "hwdot1sMstiRemainingHops": hwdot1sMstiRemainingHops,
       "hwdot1sMstiAdminMappedVlanListLow": hwdot1sMstiAdminMappedVlanListLow,
       "hwdot1sMstiAdminMappedVlanListHigh": hwdot1sMstiAdminMappedVlanListHigh,
       "hwdot1sMstiOperMappedVlanListLow": hwdot1sMstiOperMappedVlanListLow,
       "hwdot1sMstiOperMappedVlanListHigh": hwdot1sMstiOperMappedVlanListHigh,
       "hwdot1sPortTable": hwdot1sPortTable,
       "hwdot1sPortEntry": hwdot1sPortEntry,
       "hwdot1sMstiPortIndex": hwdot1sMstiPortIndex,
       "hwdot1sMstiState": hwdot1sMstiState,
       "hwdot1sMstiPortPriority": hwdot1sMstiPortPriority,
       "hwdot1sMstiPathCost": hwdot1sMstiPathCost,
       "hwdot1sMstiDesignatedRoot": hwdot1sMstiDesignatedRoot,
       "hwdot1sMstiDesignatedCost": hwdot1sMstiDesignatedCost,
       "hwdot1sMstiDesignatedBridge": hwdot1sMstiDesignatedBridge,
       "hwdot1sMstiDesignatedPort": hwdot1sMstiDesignatedPort,
       "hwdot1sMstiMasterBridgeID": hwdot1sMstiMasterBridgeID,
       "hwdot1sMstiMasterPortCost": hwdot1sMstiMasterPortCost,
       "hwdot1sMstiStpPortEdgeport": hwdot1sMstiStpPortEdgeport,
       "hwdot1sMstiStpPortPointToPoint": hwdot1sMstiStpPortPointToPoint,
       "hwdot1sMstiStpMcheck": hwdot1sMstiStpMcheck,
       "hwdot1sMstiStpTransLimit": hwdot1sMstiStpTransLimit,
       "hwdot1sMstiStpRXStpBPDU": hwdot1sMstiStpRXStpBPDU,
       "hwdot1sMstiStpTXStpBPDU": hwdot1sMstiStpTXStpBPDU,
       "hwdot1sMstiStpRXTCNBPDU": hwdot1sMstiStpRXTCNBPDU,
       "hwdot1sMstiStpTXTCNBPDU": hwdot1sMstiStpTXTCNBPDU,
       "hwdot1sMstiStpRXRSTPBPDU": hwdot1sMstiStpRXRSTPBPDU,
       "hwdot1sMstiStpTXRSTPBPDU": hwdot1sMstiStpTXRSTPBPDU,
       "hwdot1sMstiStpRXMSTPBPDU": hwdot1sMstiStpRXMSTPBPDU,
       "hwdot1sMstiStpTXMSTPBPDU": hwdot1sMstiStpTXMSTPBPDU,
       "hwdot1sMstiStpClearStatistics": hwdot1sMstiStpClearStatistics,
       "hwdot1sMstiStpDefaultPortCost": hwdot1sMstiStpDefaultPortCost,
       "hwdot1sMstiStpStatus": hwdot1sMstiStpStatus,
       "hwdot1sMstiPortRootGuard": hwdot1sMstiPortRootGuard,
       "hwdot1sMstiPortLoopGuard": hwdot1sMstiPortLoopGuard,
       "hwdot1sMstiStpPortSendingBPDUType": hwdot1sMstiStpPortSendingBPDUType,
       "hwdot1sMstiStpOperPortPointToPoint": hwdot1sMstiStpOperPortPointToPoint,
       "hwdot1sMstiStpPortAdminBPDUFmt": hwdot1sMstiStpPortAdminBPDUFmt,
       "hwdot1sMstiStpPortOperBPDUFmt": hwdot1sMstiStpPortOperBPDUFmt,
       "hwdot1sMstiStpPortRoleRestriction": hwdot1sMstiStpPortRoleRestriction,
       "hwdot1sMstiStpPortTcRestriction": hwdot1sMstiStpPortTcRestriction,
       "hwdot1sMstiStpPortDisputed": hwdot1sMstiStpPortDisputed,
       "hwdot1sStpPathCostStandard": hwdot1sStpPathCostStandard}
)
