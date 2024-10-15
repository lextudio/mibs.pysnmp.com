# SNMP MIB module (HPN-ICF-LswMSTP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HPN-ICF-LswMSTP-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:00:57 2024
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

(dot1dStpPort,
 dot1dStpPortEntry) = mibBuilder.importSymbols(
    "BRIDGE-MIB",
    "dot1dStpPort",
    "dot1dStpPortEntry")

(hpnicflswCommon,) = mibBuilder.importSymbols(
    "HPN-ICF-OID-MIB",
    "hpnicflswCommon")

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

hpnicfdot1sMstp = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 14)
)
hpnicfdot1sMstp.setRevisions(
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



class Hpnicfdot1sFormatStatus(Integer32, TextualConvention):
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

_HpnicfMstpEventsV2_ObjectIdentity = ObjectIdentity
hpnicfMstpEventsV2 = _HpnicfMstpEventsV2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 14, 0)
)
if mibBuilder.loadTexts:
    hpnicfMstpEventsV2.setStatus("current")


class _Hpnicfdot1sStpStatus_Type(EnabledStatus):
    """Custom type hpnicfdot1sStpStatus based on EnabledStatus"""
    defaultValue = 2


_Hpnicfdot1sStpStatus_Object = MibScalar
hpnicfdot1sStpStatus = _Hpnicfdot1sStpStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 14, 1),
    _Hpnicfdot1sStpStatus_Type()
)
hpnicfdot1sStpStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfdot1sStpStatus.setStatus("current")


class _Hpnicfdot1sStpForceVersion_Type(Integer32):
    """Custom type hpnicfdot1sStpForceVersion based on Integer32"""
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


_Hpnicfdot1sStpForceVersion_Type.__name__ = "Integer32"
_Hpnicfdot1sStpForceVersion_Object = MibScalar
hpnicfdot1sStpForceVersion = _Hpnicfdot1sStpForceVersion_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 14, 2),
    _Hpnicfdot1sStpForceVersion_Type()
)
hpnicfdot1sStpForceVersion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfdot1sStpForceVersion.setStatus("current")


class _Hpnicfdot1sStpDiameter_Type(Integer32):
    """Custom type hpnicfdot1sStpDiameter based on Integer32"""
    defaultValue = 7

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 7),
    )


_Hpnicfdot1sStpDiameter_Type.__name__ = "Integer32"
_Hpnicfdot1sStpDiameter_Object = MibScalar
hpnicfdot1sStpDiameter = _Hpnicfdot1sStpDiameter_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 14, 3),
    _Hpnicfdot1sStpDiameter_Type()
)
hpnicfdot1sStpDiameter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfdot1sStpDiameter.setStatus("current")


class _Hpnicfdot1sMstBridgeMaxHops_Type(Integer32):
    """Custom type hpnicfdot1sMstBridgeMaxHops based on Integer32"""
    defaultValue = 20

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 40),
    )


_Hpnicfdot1sMstBridgeMaxHops_Type.__name__ = "Integer32"
_Hpnicfdot1sMstBridgeMaxHops_Object = MibScalar
hpnicfdot1sMstBridgeMaxHops = _Hpnicfdot1sMstBridgeMaxHops_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 14, 4),
    _Hpnicfdot1sMstBridgeMaxHops_Type()
)
hpnicfdot1sMstBridgeMaxHops.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfdot1sMstBridgeMaxHops.setStatus("current")
_Hpnicfdot1sMstMasterBridgeID_Type = BridgeId
_Hpnicfdot1sMstMasterBridgeID_Object = MibScalar
hpnicfdot1sMstMasterBridgeID = _Hpnicfdot1sMstMasterBridgeID_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 14, 5),
    _Hpnicfdot1sMstMasterBridgeID_Type()
)
hpnicfdot1sMstMasterBridgeID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfdot1sMstMasterBridgeID.setStatus("current")


class _Hpnicfdot1sMstMasterPathCost_Type(Integer32):
    """Custom type hpnicfdot1sMstMasterPathCost based on Integer32"""
    defaultValue = 0


_Hpnicfdot1sMstMasterPathCost_Object = MibScalar
hpnicfdot1sMstMasterPathCost = _Hpnicfdot1sMstMasterPathCost_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 14, 6),
    _Hpnicfdot1sMstMasterPathCost_Type()
)
hpnicfdot1sMstMasterPathCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfdot1sMstMasterPathCost.setStatus("current")


class _Hpnicfdot1sMstBpduGuard_Type(EnabledStatus):
    """Custom type hpnicfdot1sMstBpduGuard based on EnabledStatus"""


_Hpnicfdot1sMstBpduGuard_Object = MibScalar
hpnicfdot1sMstBpduGuard = _Hpnicfdot1sMstBpduGuard_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 14, 7),
    _Hpnicfdot1sMstBpduGuard_Type()
)
hpnicfdot1sMstBpduGuard.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfdot1sMstBpduGuard.setStatus("current")


class _Hpnicfdot1sMstAdminFormatSelector_Type(Integer32):
    """Custom type hpnicfdot1sMstAdminFormatSelector based on Integer32"""
    defaultValue = 0


_Hpnicfdot1sMstAdminFormatSelector_Object = MibScalar
hpnicfdot1sMstAdminFormatSelector = _Hpnicfdot1sMstAdminFormatSelector_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 14, 8),
    _Hpnicfdot1sMstAdminFormatSelector_Type()
)
hpnicfdot1sMstAdminFormatSelector.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfdot1sMstAdminFormatSelector.setStatus("current")


class _Hpnicfdot1sMstAdminRegionName_Type(OctetString):
    """Custom type hpnicfdot1sMstAdminRegionName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_Hpnicfdot1sMstAdminRegionName_Type.__name__ = "OctetString"
_Hpnicfdot1sMstAdminRegionName_Object = MibScalar
hpnicfdot1sMstAdminRegionName = _Hpnicfdot1sMstAdminRegionName_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 14, 9),
    _Hpnicfdot1sMstAdminRegionName_Type()
)
hpnicfdot1sMstAdminRegionName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfdot1sMstAdminRegionName.setStatus("current")


class _Hpnicfdot1sMstAdminRevisionLevel_Type(Integer32):
    """Custom type hpnicfdot1sMstAdminRevisionLevel based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Hpnicfdot1sMstAdminRevisionLevel_Type.__name__ = "Integer32"
_Hpnicfdot1sMstAdminRevisionLevel_Object = MibScalar
hpnicfdot1sMstAdminRevisionLevel = _Hpnicfdot1sMstAdminRevisionLevel_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 14, 10),
    _Hpnicfdot1sMstAdminRevisionLevel_Type()
)
hpnicfdot1sMstAdminRevisionLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfdot1sMstAdminRevisionLevel.setStatus("current")


class _Hpnicfdot1sMstOperFormatSelector_Type(Integer32):
    """Custom type hpnicfdot1sMstOperFormatSelector based on Integer32"""
    defaultValue = 0


_Hpnicfdot1sMstOperFormatSelector_Object = MibScalar
hpnicfdot1sMstOperFormatSelector = _Hpnicfdot1sMstOperFormatSelector_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 14, 11),
    _Hpnicfdot1sMstOperFormatSelector_Type()
)
hpnicfdot1sMstOperFormatSelector.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfdot1sMstOperFormatSelector.setStatus("current")


class _Hpnicfdot1sMstOperRegionName_Type(OctetString):
    """Custom type hpnicfdot1sMstOperRegionName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Hpnicfdot1sMstOperRegionName_Type.__name__ = "OctetString"
_Hpnicfdot1sMstOperRegionName_Object = MibScalar
hpnicfdot1sMstOperRegionName = _Hpnicfdot1sMstOperRegionName_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 14, 12),
    _Hpnicfdot1sMstOperRegionName_Type()
)
hpnicfdot1sMstOperRegionName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfdot1sMstOperRegionName.setStatus("current")


class _Hpnicfdot1sMstOperRevisionLevel_Type(Integer32):
    """Custom type hpnicfdot1sMstOperRevisionLevel based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Hpnicfdot1sMstOperRevisionLevel_Type.__name__ = "Integer32"
_Hpnicfdot1sMstOperRevisionLevel_Object = MibScalar
hpnicfdot1sMstOperRevisionLevel = _Hpnicfdot1sMstOperRevisionLevel_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 14, 13),
    _Hpnicfdot1sMstOperRevisionLevel_Type()
)
hpnicfdot1sMstOperRevisionLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfdot1sMstOperRevisionLevel.setStatus("current")


class _Hpnicfdot1sMstOperConfigDigest_Type(OctetString):
    """Custom type hpnicfdot1sMstOperConfigDigest based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_Hpnicfdot1sMstOperConfigDigest_Type.__name__ = "OctetString"
_Hpnicfdot1sMstOperConfigDigest_Object = MibScalar
hpnicfdot1sMstOperConfigDigest = _Hpnicfdot1sMstOperConfigDigest_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 14, 14),
    _Hpnicfdot1sMstOperConfigDigest_Type()
)
hpnicfdot1sMstOperConfigDigest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfdot1sMstOperConfigDigest.setStatus("current")


class _Hpnicfdot1sMstRegionConfActive_Type(Integer32):
    """Custom type hpnicfdot1sMstRegionConfActive based on Integer32"""
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


_Hpnicfdot1sMstRegionConfActive_Type.__name__ = "Integer32"
_Hpnicfdot1sMstRegionConfActive_Object = MibScalar
hpnicfdot1sMstRegionConfActive = _Hpnicfdot1sMstRegionConfActive_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 14, 15),
    _Hpnicfdot1sMstRegionConfActive_Type()
)
hpnicfdot1sMstRegionConfActive.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfdot1sMstRegionConfActive.setStatus("current")


class _Hpnicfdot1sMstDefaultVlanAllo_Type(Integer32):
    """Custom type hpnicfdot1sMstDefaultVlanAllo based on Integer32"""
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


_Hpnicfdot1sMstDefaultVlanAllo_Type.__name__ = "Integer32"
_Hpnicfdot1sMstDefaultVlanAllo_Object = MibScalar
hpnicfdot1sMstDefaultVlanAllo = _Hpnicfdot1sMstDefaultVlanAllo_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 14, 16),
    _Hpnicfdot1sMstDefaultVlanAllo_Type()
)
hpnicfdot1sMstDefaultVlanAllo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfdot1sMstDefaultVlanAllo.setStatus("current")


class _Hpnicfdot1sMstDefaultRegionName_Type(Integer32):
    """Custom type hpnicfdot1sMstDefaultRegionName based on Integer32"""
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


_Hpnicfdot1sMstDefaultRegionName_Type.__name__ = "Integer32"
_Hpnicfdot1sMstDefaultRegionName_Object = MibScalar
hpnicfdot1sMstDefaultRegionName = _Hpnicfdot1sMstDefaultRegionName_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 14, 17),
    _Hpnicfdot1sMstDefaultRegionName_Type()
)
hpnicfdot1sMstDefaultRegionName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfdot1sMstDefaultRegionName.setStatus("current")
_Hpnicfdot1sVIDAllocationTable_Object = MibTable
hpnicfdot1sVIDAllocationTable = _Hpnicfdot1sVIDAllocationTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 14, 18)
)
if mibBuilder.loadTexts:
    hpnicfdot1sVIDAllocationTable.setStatus("current")
_Hpnicfdot1sVIDAllocationEntry_Object = MibTableRow
hpnicfdot1sVIDAllocationEntry = _Hpnicfdot1sVIDAllocationEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 14, 18, 1)
)
hpnicfdot1sVIDAllocationEntry.setIndexNames(
    (0, "HPN-ICF-LswMSTP-MIB", "hpnicfdot1sMstVID"),
)
if mibBuilder.loadTexts:
    hpnicfdot1sVIDAllocationEntry.setStatus("current")


class _Hpnicfdot1sMstVID_Type(Integer32):
    """Custom type hpnicfdot1sMstVID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_Hpnicfdot1sMstVID_Type.__name__ = "Integer32"
_Hpnicfdot1sMstVID_Object = MibTableColumn
hpnicfdot1sMstVID = _Hpnicfdot1sMstVID_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 14, 18, 1, 1),
    _Hpnicfdot1sMstVID_Type()
)
hpnicfdot1sMstVID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfdot1sMstVID.setStatus("current")


class _Hpnicfdot1sAdminMstID_Type(Integer32):
    """Custom type hpnicfdot1sAdminMstID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_Hpnicfdot1sAdminMstID_Type.__name__ = "Integer32"
_Hpnicfdot1sAdminMstID_Object = MibTableColumn
hpnicfdot1sAdminMstID = _Hpnicfdot1sAdminMstID_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 14, 18, 1, 2),
    _Hpnicfdot1sAdminMstID_Type()
)
hpnicfdot1sAdminMstID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfdot1sAdminMstID.setStatus("current")


class _Hpnicfdot1sOperMstID_Type(Integer32):
    """Custom type hpnicfdot1sOperMstID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_Hpnicfdot1sOperMstID_Type.__name__ = "Integer32"
_Hpnicfdot1sOperMstID_Object = MibTableColumn
hpnicfdot1sOperMstID = _Hpnicfdot1sOperMstID_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 14, 18, 1, 3),
    _Hpnicfdot1sOperMstID_Type()
)
hpnicfdot1sOperMstID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfdot1sOperMstID.setStatus("current")
_Hpnicfdot1sInstanceTable_Object = MibTable
hpnicfdot1sInstanceTable = _Hpnicfdot1sInstanceTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 14, 19)
)
if mibBuilder.loadTexts:
    hpnicfdot1sInstanceTable.setStatus("current")
_Hpnicfdot1sInstanceEntry_Object = MibTableRow
hpnicfdot1sInstanceEntry = _Hpnicfdot1sInstanceEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 14, 19, 1)
)
hpnicfdot1sInstanceEntry.setIndexNames(
    (0, "HPN-ICF-LswMSTP-MIB", "hpnicfdot1sInstanceID"),
)
if mibBuilder.loadTexts:
    hpnicfdot1sInstanceEntry.setStatus("current")


class _Hpnicfdot1sInstanceID_Type(Integer32):
    """Custom type hpnicfdot1sInstanceID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_Hpnicfdot1sInstanceID_Type.__name__ = "Integer32"
_Hpnicfdot1sInstanceID_Object = MibTableColumn
hpnicfdot1sInstanceID = _Hpnicfdot1sInstanceID_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 14, 19, 1, 1),
    _Hpnicfdot1sInstanceID_Type()
)
hpnicfdot1sInstanceID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfdot1sInstanceID.setStatus("current")
_Hpnicfdot1sMstiBridgeID_Type = BridgeId
_Hpnicfdot1sMstiBridgeID_Object = MibTableColumn
hpnicfdot1sMstiBridgeID = _Hpnicfdot1sMstiBridgeID_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 14, 19, 1, 2),
    _Hpnicfdot1sMstiBridgeID_Type()
)
hpnicfdot1sMstiBridgeID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfdot1sMstiBridgeID.setStatus("current")


class _Hpnicfdot1sMstiBridgePriority_Type(Integer32):
    """Custom type hpnicfdot1sMstiBridgePriority based on Integer32"""
    defaultValue = 32768

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 61440),
    )


_Hpnicfdot1sMstiBridgePriority_Type.__name__ = "Integer32"
_Hpnicfdot1sMstiBridgePriority_Object = MibTableColumn
hpnicfdot1sMstiBridgePriority = _Hpnicfdot1sMstiBridgePriority_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 14, 19, 1, 3),
    _Hpnicfdot1sMstiBridgePriority_Type()
)
hpnicfdot1sMstiBridgePriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfdot1sMstiBridgePriority.setStatus("current")
_Hpnicfdot1sMstiDesignedRoot_Type = BridgeId
_Hpnicfdot1sMstiDesignedRoot_Object = MibTableColumn
hpnicfdot1sMstiDesignedRoot = _Hpnicfdot1sMstiDesignedRoot_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 14, 19, 1, 4),
    _Hpnicfdot1sMstiDesignedRoot_Type()
)
hpnicfdot1sMstiDesignedRoot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfdot1sMstiDesignedRoot.setStatus("current")
_Hpnicfdot1sMstiRootPathCost_Type = Integer32
_Hpnicfdot1sMstiRootPathCost_Object = MibTableColumn
hpnicfdot1sMstiRootPathCost = _Hpnicfdot1sMstiRootPathCost_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 14, 19, 1, 5),
    _Hpnicfdot1sMstiRootPathCost_Type()
)
hpnicfdot1sMstiRootPathCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfdot1sMstiRootPathCost.setStatus("current")
_Hpnicfdot1sMstiRootPort_Type = Integer32
_Hpnicfdot1sMstiRootPort_Object = MibTableColumn
hpnicfdot1sMstiRootPort = _Hpnicfdot1sMstiRootPort_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 14, 19, 1, 6),
    _Hpnicfdot1sMstiRootPort_Type()
)
hpnicfdot1sMstiRootPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfdot1sMstiRootPort.setStatus("current")


class _Hpnicfdot1sMstiRootType_Type(Integer32):
    """Custom type hpnicfdot1sMstiRootType based on Integer32"""
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


_Hpnicfdot1sMstiRootType_Type.__name__ = "Integer32"
_Hpnicfdot1sMstiRootType_Object = MibTableColumn
hpnicfdot1sMstiRootType = _Hpnicfdot1sMstiRootType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 14, 19, 1, 7),
    _Hpnicfdot1sMstiRootType_Type()
)
hpnicfdot1sMstiRootType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfdot1sMstiRootType.setStatus("current")
_Hpnicfdot1sMstiRemainingHops_Type = Integer32
_Hpnicfdot1sMstiRemainingHops_Object = MibTableColumn
hpnicfdot1sMstiRemainingHops = _Hpnicfdot1sMstiRemainingHops_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 14, 19, 1, 8),
    _Hpnicfdot1sMstiRemainingHops_Type()
)
hpnicfdot1sMstiRemainingHops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfdot1sMstiRemainingHops.setStatus("current")


class _Hpnicfdot1sMstiAdminMappedVlanListLow_Type(OctetString):
    """Custom type hpnicfdot1sMstiAdminMappedVlanListLow based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_Hpnicfdot1sMstiAdminMappedVlanListLow_Type.__name__ = "OctetString"
_Hpnicfdot1sMstiAdminMappedVlanListLow_Object = MibTableColumn
hpnicfdot1sMstiAdminMappedVlanListLow = _Hpnicfdot1sMstiAdminMappedVlanListLow_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 14, 19, 1, 9),
    _Hpnicfdot1sMstiAdminMappedVlanListLow_Type()
)
hpnicfdot1sMstiAdminMappedVlanListLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfdot1sMstiAdminMappedVlanListLow.setStatus("current")


class _Hpnicfdot1sMstiAdminMappedVlanListHigh_Type(OctetString):
    """Custom type hpnicfdot1sMstiAdminMappedVlanListHigh based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_Hpnicfdot1sMstiAdminMappedVlanListHigh_Type.__name__ = "OctetString"
_Hpnicfdot1sMstiAdminMappedVlanListHigh_Object = MibTableColumn
hpnicfdot1sMstiAdminMappedVlanListHigh = _Hpnicfdot1sMstiAdminMappedVlanListHigh_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 14, 19, 1, 10),
    _Hpnicfdot1sMstiAdminMappedVlanListHigh_Type()
)
hpnicfdot1sMstiAdminMappedVlanListHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfdot1sMstiAdminMappedVlanListHigh.setStatus("current")


class _Hpnicfdot1sMstiOperMappedVlanListLow_Type(OctetString):
    """Custom type hpnicfdot1sMstiOperMappedVlanListLow based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_Hpnicfdot1sMstiOperMappedVlanListLow_Type.__name__ = "OctetString"
_Hpnicfdot1sMstiOperMappedVlanListLow_Object = MibTableColumn
hpnicfdot1sMstiOperMappedVlanListLow = _Hpnicfdot1sMstiOperMappedVlanListLow_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 14, 19, 1, 11),
    _Hpnicfdot1sMstiOperMappedVlanListLow_Type()
)
hpnicfdot1sMstiOperMappedVlanListLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfdot1sMstiOperMappedVlanListLow.setStatus("current")


class _Hpnicfdot1sMstiOperMappedVlanListHigh_Type(OctetString):
    """Custom type hpnicfdot1sMstiOperMappedVlanListHigh based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_Hpnicfdot1sMstiOperMappedVlanListHigh_Type.__name__ = "OctetString"
_Hpnicfdot1sMstiOperMappedVlanListHigh_Object = MibTableColumn
hpnicfdot1sMstiOperMappedVlanListHigh = _Hpnicfdot1sMstiOperMappedVlanListHigh_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 14, 19, 1, 12),
    _Hpnicfdot1sMstiOperMappedVlanListHigh_Type()
)
hpnicfdot1sMstiOperMappedVlanListHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfdot1sMstiOperMappedVlanListHigh.setStatus("current")
_Hpnicfdot1sPortTable_Object = MibTable
hpnicfdot1sPortTable = _Hpnicfdot1sPortTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 14, 20)
)
if mibBuilder.loadTexts:
    hpnicfdot1sPortTable.setStatus("current")
_Hpnicfdot1sPortEntry_Object = MibTableRow
hpnicfdot1sPortEntry = _Hpnicfdot1sPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 14, 20, 1)
)
hpnicfdot1sPortEntry.setIndexNames(
    (0, "HPN-ICF-LswMSTP-MIB", "hpnicfdot1sInstanceID"),
    (0, "HPN-ICF-LswMSTP-MIB", "hpnicfdot1sMstiPortIndex"),
)
if mibBuilder.loadTexts:
    hpnicfdot1sPortEntry.setStatus("current")
_Hpnicfdot1sMstiPortIndex_Type = Integer32
_Hpnicfdot1sMstiPortIndex_Object = MibTableColumn
hpnicfdot1sMstiPortIndex = _Hpnicfdot1sMstiPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 14, 20, 1, 1),
    _Hpnicfdot1sMstiPortIndex_Type()
)
hpnicfdot1sMstiPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfdot1sMstiPortIndex.setStatus("current")


class _Hpnicfdot1sMstiState_Type(Integer32):
    """Custom type hpnicfdot1sMstiState based on Integer32"""
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


_Hpnicfdot1sMstiState_Type.__name__ = "Integer32"
_Hpnicfdot1sMstiState_Object = MibTableColumn
hpnicfdot1sMstiState = _Hpnicfdot1sMstiState_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 14, 20, 1, 2),
    _Hpnicfdot1sMstiState_Type()
)
hpnicfdot1sMstiState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfdot1sMstiState.setStatus("current")


class _Hpnicfdot1sMstiPortPriority_Type(Integer32):
    """Custom type hpnicfdot1sMstiPortPriority based on Integer32"""
    defaultValue = 128

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 240),
    )


_Hpnicfdot1sMstiPortPriority_Type.__name__ = "Integer32"
_Hpnicfdot1sMstiPortPriority_Object = MibTableColumn
hpnicfdot1sMstiPortPriority = _Hpnicfdot1sMstiPortPriority_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 14, 20, 1, 3),
    _Hpnicfdot1sMstiPortPriority_Type()
)
hpnicfdot1sMstiPortPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfdot1sMstiPortPriority.setStatus("current")


class _Hpnicfdot1sMstiPathCost_Type(Integer32):
    """Custom type hpnicfdot1sMstiPathCost based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 200000000),
    )


_Hpnicfdot1sMstiPathCost_Type.__name__ = "Integer32"
_Hpnicfdot1sMstiPathCost_Object = MibTableColumn
hpnicfdot1sMstiPathCost = _Hpnicfdot1sMstiPathCost_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 14, 20, 1, 4),
    _Hpnicfdot1sMstiPathCost_Type()
)
hpnicfdot1sMstiPathCost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfdot1sMstiPathCost.setStatus("current")
_Hpnicfdot1sMstiDesignatedRoot_Type = BridgeId
_Hpnicfdot1sMstiDesignatedRoot_Object = MibTableColumn
hpnicfdot1sMstiDesignatedRoot = _Hpnicfdot1sMstiDesignatedRoot_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 14, 20, 1, 5),
    _Hpnicfdot1sMstiDesignatedRoot_Type()
)
hpnicfdot1sMstiDesignatedRoot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfdot1sMstiDesignatedRoot.setStatus("current")
_Hpnicfdot1sMstiDesignatedCost_Type = Integer32
_Hpnicfdot1sMstiDesignatedCost_Object = MibTableColumn
hpnicfdot1sMstiDesignatedCost = _Hpnicfdot1sMstiDesignatedCost_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 14, 20, 1, 6),
    _Hpnicfdot1sMstiDesignatedCost_Type()
)
hpnicfdot1sMstiDesignatedCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfdot1sMstiDesignatedCost.setStatus("current")
_Hpnicfdot1sMstiDesignatedBridge_Type = BridgeId
_Hpnicfdot1sMstiDesignatedBridge_Object = MibTableColumn
hpnicfdot1sMstiDesignatedBridge = _Hpnicfdot1sMstiDesignatedBridge_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 14, 20, 1, 7),
    _Hpnicfdot1sMstiDesignatedBridge_Type()
)
hpnicfdot1sMstiDesignatedBridge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfdot1sMstiDesignatedBridge.setStatus("current")


class _Hpnicfdot1sMstiDesignatedPort_Type(OctetString):
    """Custom type hpnicfdot1sMstiDesignatedPort based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_Hpnicfdot1sMstiDesignatedPort_Type.__name__ = "OctetString"
_Hpnicfdot1sMstiDesignatedPort_Object = MibTableColumn
hpnicfdot1sMstiDesignatedPort = _Hpnicfdot1sMstiDesignatedPort_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 14, 20, 1, 8),
    _Hpnicfdot1sMstiDesignatedPort_Type()
)
hpnicfdot1sMstiDesignatedPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfdot1sMstiDesignatedPort.setStatus("current")
_Hpnicfdot1sMstiMasterBridgeID_Type = BridgeId
_Hpnicfdot1sMstiMasterBridgeID_Object = MibTableColumn
hpnicfdot1sMstiMasterBridgeID = _Hpnicfdot1sMstiMasterBridgeID_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 14, 20, 1, 9),
    _Hpnicfdot1sMstiMasterBridgeID_Type()
)
hpnicfdot1sMstiMasterBridgeID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfdot1sMstiMasterBridgeID.setStatus("current")
_Hpnicfdot1sMstiMasterPortCost_Type = Integer32
_Hpnicfdot1sMstiMasterPortCost_Object = MibTableColumn
hpnicfdot1sMstiMasterPortCost = _Hpnicfdot1sMstiMasterPortCost_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 14, 20, 1, 10),
    _Hpnicfdot1sMstiMasterPortCost_Type()
)
hpnicfdot1sMstiMasterPortCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfdot1sMstiMasterPortCost.setStatus("current")


class _Hpnicfdot1sMstiStpPortEdgeport_Type(EnabledStatus):
    """Custom type hpnicfdot1sMstiStpPortEdgeport based on EnabledStatus"""


_Hpnicfdot1sMstiStpPortEdgeport_Object = MibTableColumn
hpnicfdot1sMstiStpPortEdgeport = _Hpnicfdot1sMstiStpPortEdgeport_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 14, 20, 1, 11),
    _Hpnicfdot1sMstiStpPortEdgeport_Type()
)
hpnicfdot1sMstiStpPortEdgeport.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfdot1sMstiStpPortEdgeport.setStatus("current")


class _Hpnicfdot1sMstiStpPortPointToPoint_Type(Integer32):
    """Custom type hpnicfdot1sMstiStpPortPointToPoint based on Integer32"""
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


_Hpnicfdot1sMstiStpPortPointToPoint_Type.__name__ = "Integer32"
_Hpnicfdot1sMstiStpPortPointToPoint_Object = MibTableColumn
hpnicfdot1sMstiStpPortPointToPoint = _Hpnicfdot1sMstiStpPortPointToPoint_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 14, 20, 1, 12),
    _Hpnicfdot1sMstiStpPortPointToPoint_Type()
)
hpnicfdot1sMstiStpPortPointToPoint.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfdot1sMstiStpPortPointToPoint.setStatus("current")


class _Hpnicfdot1sMstiStpMcheck_Type(Integer32):
    """Custom type hpnicfdot1sMstiStpMcheck based on Integer32"""
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


_Hpnicfdot1sMstiStpMcheck_Type.__name__ = "Integer32"
_Hpnicfdot1sMstiStpMcheck_Object = MibTableColumn
hpnicfdot1sMstiStpMcheck = _Hpnicfdot1sMstiStpMcheck_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 14, 20, 1, 13),
    _Hpnicfdot1sMstiStpMcheck_Type()
)
hpnicfdot1sMstiStpMcheck.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfdot1sMstiStpMcheck.setStatus("current")


class _Hpnicfdot1sMstiStpTransLimit_Type(Integer32):
    """Custom type hpnicfdot1sMstiStpTransLimit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_Hpnicfdot1sMstiStpTransLimit_Type.__name__ = "Integer32"
_Hpnicfdot1sMstiStpTransLimit_Object = MibTableColumn
hpnicfdot1sMstiStpTransLimit = _Hpnicfdot1sMstiStpTransLimit_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 14, 20, 1, 14),
    _Hpnicfdot1sMstiStpTransLimit_Type()
)
hpnicfdot1sMstiStpTransLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfdot1sMstiStpTransLimit.setStatus("current")
_Hpnicfdot1sMstiStpRXStpBPDU_Type = Counter32
_Hpnicfdot1sMstiStpRXStpBPDU_Object = MibTableColumn
hpnicfdot1sMstiStpRXStpBPDU = _Hpnicfdot1sMstiStpRXStpBPDU_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 14, 20, 1, 15),
    _Hpnicfdot1sMstiStpRXStpBPDU_Type()
)
hpnicfdot1sMstiStpRXStpBPDU.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfdot1sMstiStpRXStpBPDU.setStatus("current")
_Hpnicfdot1sMstiStpTXStpBPDU_Type = Counter32
_Hpnicfdot1sMstiStpTXStpBPDU_Object = MibTableColumn
hpnicfdot1sMstiStpTXStpBPDU = _Hpnicfdot1sMstiStpTXStpBPDU_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 14, 20, 1, 16),
    _Hpnicfdot1sMstiStpTXStpBPDU_Type()
)
hpnicfdot1sMstiStpTXStpBPDU.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfdot1sMstiStpTXStpBPDU.setStatus("current")
_Hpnicfdot1sMstiStpRXTCNBPDU_Type = Counter32
_Hpnicfdot1sMstiStpRXTCNBPDU_Object = MibTableColumn
hpnicfdot1sMstiStpRXTCNBPDU = _Hpnicfdot1sMstiStpRXTCNBPDU_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 14, 20, 1, 17),
    _Hpnicfdot1sMstiStpRXTCNBPDU_Type()
)
hpnicfdot1sMstiStpRXTCNBPDU.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfdot1sMstiStpRXTCNBPDU.setStatus("current")
_Hpnicfdot1sMstiStpTXTCNBPDU_Type = Counter32
_Hpnicfdot1sMstiStpTXTCNBPDU_Object = MibTableColumn
hpnicfdot1sMstiStpTXTCNBPDU = _Hpnicfdot1sMstiStpTXTCNBPDU_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 14, 20, 1, 18),
    _Hpnicfdot1sMstiStpTXTCNBPDU_Type()
)
hpnicfdot1sMstiStpTXTCNBPDU.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfdot1sMstiStpTXTCNBPDU.setStatus("current")
_Hpnicfdot1sMstiStpRXRSTPBPDU_Type = Counter32
_Hpnicfdot1sMstiStpRXRSTPBPDU_Object = MibTableColumn
hpnicfdot1sMstiStpRXRSTPBPDU = _Hpnicfdot1sMstiStpRXRSTPBPDU_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 14, 20, 1, 19),
    _Hpnicfdot1sMstiStpRXRSTPBPDU_Type()
)
hpnicfdot1sMstiStpRXRSTPBPDU.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfdot1sMstiStpRXRSTPBPDU.setStatus("current")
_Hpnicfdot1sMstiStpTXRSTPBPDU_Type = Counter32
_Hpnicfdot1sMstiStpTXRSTPBPDU_Object = MibTableColumn
hpnicfdot1sMstiStpTXRSTPBPDU = _Hpnicfdot1sMstiStpTXRSTPBPDU_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 14, 20, 1, 20),
    _Hpnicfdot1sMstiStpTXRSTPBPDU_Type()
)
hpnicfdot1sMstiStpTXRSTPBPDU.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfdot1sMstiStpTXRSTPBPDU.setStatus("current")
_Hpnicfdot1sMstiStpRXMSTPBPDU_Type = Counter32
_Hpnicfdot1sMstiStpRXMSTPBPDU_Object = MibTableColumn
hpnicfdot1sMstiStpRXMSTPBPDU = _Hpnicfdot1sMstiStpRXMSTPBPDU_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 14, 20, 1, 21),
    _Hpnicfdot1sMstiStpRXMSTPBPDU_Type()
)
hpnicfdot1sMstiStpRXMSTPBPDU.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfdot1sMstiStpRXMSTPBPDU.setStatus("current")
_Hpnicfdot1sMstiStpTXMSTPBPDU_Type = Counter32
_Hpnicfdot1sMstiStpTXMSTPBPDU_Object = MibTableColumn
hpnicfdot1sMstiStpTXMSTPBPDU = _Hpnicfdot1sMstiStpTXMSTPBPDU_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 14, 20, 1, 22),
    _Hpnicfdot1sMstiStpTXMSTPBPDU_Type()
)
hpnicfdot1sMstiStpTXMSTPBPDU.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfdot1sMstiStpTXMSTPBPDU.setStatus("current")


class _Hpnicfdot1sMstiStpClearStatistics_Type(Integer32):
    """Custom type hpnicfdot1sMstiStpClearStatistics based on Integer32"""
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


_Hpnicfdot1sMstiStpClearStatistics_Type.__name__ = "Integer32"
_Hpnicfdot1sMstiStpClearStatistics_Object = MibTableColumn
hpnicfdot1sMstiStpClearStatistics = _Hpnicfdot1sMstiStpClearStatistics_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 14, 20, 1, 23),
    _Hpnicfdot1sMstiStpClearStatistics_Type()
)
hpnicfdot1sMstiStpClearStatistics.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfdot1sMstiStpClearStatistics.setStatus("current")


class _Hpnicfdot1sMstiStpDefaultPortCost_Type(Integer32):
    """Custom type hpnicfdot1sMstiStpDefaultPortCost based on Integer32"""
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


_Hpnicfdot1sMstiStpDefaultPortCost_Type.__name__ = "Integer32"
_Hpnicfdot1sMstiStpDefaultPortCost_Object = MibTableColumn
hpnicfdot1sMstiStpDefaultPortCost = _Hpnicfdot1sMstiStpDefaultPortCost_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 14, 20, 1, 24),
    _Hpnicfdot1sMstiStpDefaultPortCost_Type()
)
hpnicfdot1sMstiStpDefaultPortCost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfdot1sMstiStpDefaultPortCost.setStatus("current")


class _Hpnicfdot1sMstiStpStatus_Type(EnabledStatus):
    """Custom type hpnicfdot1sMstiStpStatus based on EnabledStatus"""


_Hpnicfdot1sMstiStpStatus_Object = MibTableColumn
hpnicfdot1sMstiStpStatus = _Hpnicfdot1sMstiStpStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 14, 20, 1, 25),
    _Hpnicfdot1sMstiStpStatus_Type()
)
hpnicfdot1sMstiStpStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfdot1sMstiStpStatus.setStatus("current")


class _Hpnicfdot1sMstiPortRootGuard_Type(EnabledStatus):
    """Custom type hpnicfdot1sMstiPortRootGuard based on EnabledStatus"""


_Hpnicfdot1sMstiPortRootGuard_Object = MibTableColumn
hpnicfdot1sMstiPortRootGuard = _Hpnicfdot1sMstiPortRootGuard_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 14, 20, 1, 26),
    _Hpnicfdot1sMstiPortRootGuard_Type()
)
hpnicfdot1sMstiPortRootGuard.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfdot1sMstiPortRootGuard.setStatus("current")


class _Hpnicfdot1sMstiPortLoopGuard_Type(EnabledStatus):
    """Custom type hpnicfdot1sMstiPortLoopGuard based on EnabledStatus"""


_Hpnicfdot1sMstiPortLoopGuard_Object = MibTableColumn
hpnicfdot1sMstiPortLoopGuard = _Hpnicfdot1sMstiPortLoopGuard_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 14, 20, 1, 27),
    _Hpnicfdot1sMstiPortLoopGuard_Type()
)
hpnicfdot1sMstiPortLoopGuard.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfdot1sMstiPortLoopGuard.setStatus("current")


class _Hpnicfdot1sMstiStpPortSendingBPDUType_Type(Integer32):
    """Custom type hpnicfdot1sMstiStpPortSendingBPDUType based on Integer32"""
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


_Hpnicfdot1sMstiStpPortSendingBPDUType_Type.__name__ = "Integer32"
_Hpnicfdot1sMstiStpPortSendingBPDUType_Object = MibTableColumn
hpnicfdot1sMstiStpPortSendingBPDUType = _Hpnicfdot1sMstiStpPortSendingBPDUType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 14, 20, 1, 28),
    _Hpnicfdot1sMstiStpPortSendingBPDUType_Type()
)
hpnicfdot1sMstiStpPortSendingBPDUType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfdot1sMstiStpPortSendingBPDUType.setStatus("current")


class _Hpnicfdot1sMstiStpOperPortPointToPoint_Type(Integer32):
    """Custom type hpnicfdot1sMstiStpOperPortPointToPoint based on Integer32"""
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


_Hpnicfdot1sMstiStpOperPortPointToPoint_Type.__name__ = "Integer32"
_Hpnicfdot1sMstiStpOperPortPointToPoint_Object = MibTableColumn
hpnicfdot1sMstiStpOperPortPointToPoint = _Hpnicfdot1sMstiStpOperPortPointToPoint_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 14, 20, 1, 29),
    _Hpnicfdot1sMstiStpOperPortPointToPoint_Type()
)
hpnicfdot1sMstiStpOperPortPointToPoint.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfdot1sMstiStpOperPortPointToPoint.setStatus("current")
_Hpnicfdot1sMstiStpPortAdminBPDUFmt_Type = Hpnicfdot1sFormatStatus
_Hpnicfdot1sMstiStpPortAdminBPDUFmt_Object = MibTableColumn
hpnicfdot1sMstiStpPortAdminBPDUFmt = _Hpnicfdot1sMstiStpPortAdminBPDUFmt_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 14, 20, 1, 30),
    _Hpnicfdot1sMstiStpPortAdminBPDUFmt_Type()
)
hpnicfdot1sMstiStpPortAdminBPDUFmt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfdot1sMstiStpPortAdminBPDUFmt.setStatus("current")
_Hpnicfdot1sMstiStpPortOperBPDUFmt_Type = Hpnicfdot1sFormatStatus
_Hpnicfdot1sMstiStpPortOperBPDUFmt_Object = MibTableColumn
hpnicfdot1sMstiStpPortOperBPDUFmt = _Hpnicfdot1sMstiStpPortOperBPDUFmt_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 14, 20, 1, 31),
    _Hpnicfdot1sMstiStpPortOperBPDUFmt_Type()
)
hpnicfdot1sMstiStpPortOperBPDUFmt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfdot1sMstiStpPortOperBPDUFmt.setStatus("current")


class _Hpnicfdot1sMstiStpPortRoleRestriction_Type(EnabledStatus):
    """Custom type hpnicfdot1sMstiStpPortRoleRestriction based on EnabledStatus"""


_Hpnicfdot1sMstiStpPortRoleRestriction_Object = MibTableColumn
hpnicfdot1sMstiStpPortRoleRestriction = _Hpnicfdot1sMstiStpPortRoleRestriction_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 14, 20, 1, 32),
    _Hpnicfdot1sMstiStpPortRoleRestriction_Type()
)
hpnicfdot1sMstiStpPortRoleRestriction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfdot1sMstiStpPortRoleRestriction.setStatus("current")


class _Hpnicfdot1sMstiStpPortTcRestriction_Type(EnabledStatus):
    """Custom type hpnicfdot1sMstiStpPortTcRestriction based on EnabledStatus"""


_Hpnicfdot1sMstiStpPortTcRestriction_Object = MibTableColumn
hpnicfdot1sMstiStpPortTcRestriction = _Hpnicfdot1sMstiStpPortTcRestriction_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 14, 20, 1, 33),
    _Hpnicfdot1sMstiStpPortTcRestriction_Type()
)
hpnicfdot1sMstiStpPortTcRestriction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfdot1sMstiStpPortTcRestriction.setStatus("current")
_Hpnicfdot1sMstiStpPortDisputed_Type = TruthValue
_Hpnicfdot1sMstiStpPortDisputed_Object = MibTableColumn
hpnicfdot1sMstiStpPortDisputed = _Hpnicfdot1sMstiStpPortDisputed_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 14, 20, 1, 34),
    _Hpnicfdot1sMstiStpPortDisputed_Type()
)
hpnicfdot1sMstiStpPortDisputed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfdot1sMstiStpPortDisputed.setStatus("current")


class _Hpnicfdot1sStpPathCostStandard_Type(Integer32):
    """Custom type hpnicfdot1sStpPathCostStandard based on Integer32"""
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


_Hpnicfdot1sStpPathCostStandard_Type.__name__ = "Integer32"
_Hpnicfdot1sStpPathCostStandard_Object = MibScalar
hpnicfdot1sStpPathCostStandard = _Hpnicfdot1sStpPathCostStandard_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 14, 21),
    _Hpnicfdot1sStpPathCostStandard_Type()
)
hpnicfdot1sStpPathCostStandard.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfdot1sStpPathCostStandard.setStatus("current")

# Managed Objects groups


# Notification objects

hpnicfPortMstiStateForwarding = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 14, 0, 1)
)
hpnicfPortMstiStateForwarding.setObjects(
      *(("HPN-ICF-LswMSTP-MIB", "hpnicfdot1sInstanceID"),
        ("HPN-ICF-LswMSTP-MIB", "hpnicfdot1sMstiPortIndex"))
)
if mibBuilder.loadTexts:
    hpnicfPortMstiStateForwarding.setStatus(
        "current"
    )

hpnicfPortMstiStateDiscarding = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 14, 0, 2)
)
hpnicfPortMstiStateDiscarding.setObjects(
      *(("HPN-ICF-LswMSTP-MIB", "hpnicfdot1sInstanceID"),
        ("HPN-ICF-LswMSTP-MIB", "hpnicfdot1sMstiPortIndex"))
)
if mibBuilder.loadTexts:
    hpnicfPortMstiStateDiscarding.setStatus(
        "current"
    )

hpnicfBridgeLostRootPrimary = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 14, 0, 3)
)
hpnicfBridgeLostRootPrimary.setObjects(
    ("HPN-ICF-LswMSTP-MIB", "hpnicfdot1sInstanceID")
)
if mibBuilder.loadTexts:
    hpnicfBridgeLostRootPrimary.setStatus(
        "current"
    )

hpnicfPortMstiRootGuarded = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 14, 0, 4)
)
hpnicfPortMstiRootGuarded.setObjects(
      *(("HPN-ICF-LswMSTP-MIB", "hpnicfdot1sInstanceID"),
        ("HPN-ICF-LswMSTP-MIB", "hpnicfdot1sMstiPortIndex"))
)
if mibBuilder.loadTexts:
    hpnicfPortMstiRootGuarded.setStatus(
        "current"
    )

hpnicfPortMstiBpduGuarded = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 14, 0, 5)
)
hpnicfPortMstiBpduGuarded.setObjects(
    ("BRIDGE-MIB", "dot1dStpPort")
)
if mibBuilder.loadTexts:
    hpnicfPortMstiBpduGuarded.setStatus(
        "current"
    )

hpnicfPortMstiLoopGuarded = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 14, 0, 6)
)
hpnicfPortMstiLoopGuarded.setObjects(
      *(("HPN-ICF-LswMSTP-MIB", "hpnicfdot1sInstanceID"),
        ("HPN-ICF-LswMSTP-MIB", "hpnicfdot1sMstiPortIndex"))
)
if mibBuilder.loadTexts:
    hpnicfPortMstiLoopGuarded.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HPN-ICF-LswMSTP-MIB",
    **{"EnabledStatus": EnabledStatus,
       "BridgeId": BridgeId,
       "Hpnicfdot1sFormatStatus": Hpnicfdot1sFormatStatus,
       "hpnicfdot1sMstp": hpnicfdot1sMstp,
       "hpnicfMstpEventsV2": hpnicfMstpEventsV2,
       "hpnicfPortMstiStateForwarding": hpnicfPortMstiStateForwarding,
       "hpnicfPortMstiStateDiscarding": hpnicfPortMstiStateDiscarding,
       "hpnicfBridgeLostRootPrimary": hpnicfBridgeLostRootPrimary,
       "hpnicfPortMstiRootGuarded": hpnicfPortMstiRootGuarded,
       "hpnicfPortMstiBpduGuarded": hpnicfPortMstiBpduGuarded,
       "hpnicfPortMstiLoopGuarded": hpnicfPortMstiLoopGuarded,
       "hpnicfdot1sStpStatus": hpnicfdot1sStpStatus,
       "hpnicfdot1sStpForceVersion": hpnicfdot1sStpForceVersion,
       "hpnicfdot1sStpDiameter": hpnicfdot1sStpDiameter,
       "hpnicfdot1sMstBridgeMaxHops": hpnicfdot1sMstBridgeMaxHops,
       "hpnicfdot1sMstMasterBridgeID": hpnicfdot1sMstMasterBridgeID,
       "hpnicfdot1sMstMasterPathCost": hpnicfdot1sMstMasterPathCost,
       "hpnicfdot1sMstBpduGuard": hpnicfdot1sMstBpduGuard,
       "hpnicfdot1sMstAdminFormatSelector": hpnicfdot1sMstAdminFormatSelector,
       "hpnicfdot1sMstAdminRegionName": hpnicfdot1sMstAdminRegionName,
       "hpnicfdot1sMstAdminRevisionLevel": hpnicfdot1sMstAdminRevisionLevel,
       "hpnicfdot1sMstOperFormatSelector": hpnicfdot1sMstOperFormatSelector,
       "hpnicfdot1sMstOperRegionName": hpnicfdot1sMstOperRegionName,
       "hpnicfdot1sMstOperRevisionLevel": hpnicfdot1sMstOperRevisionLevel,
       "hpnicfdot1sMstOperConfigDigest": hpnicfdot1sMstOperConfigDigest,
       "hpnicfdot1sMstRegionConfActive": hpnicfdot1sMstRegionConfActive,
       "hpnicfdot1sMstDefaultVlanAllo": hpnicfdot1sMstDefaultVlanAllo,
       "hpnicfdot1sMstDefaultRegionName": hpnicfdot1sMstDefaultRegionName,
       "hpnicfdot1sVIDAllocationTable": hpnicfdot1sVIDAllocationTable,
       "hpnicfdot1sVIDAllocationEntry": hpnicfdot1sVIDAllocationEntry,
       "hpnicfdot1sMstVID": hpnicfdot1sMstVID,
       "hpnicfdot1sAdminMstID": hpnicfdot1sAdminMstID,
       "hpnicfdot1sOperMstID": hpnicfdot1sOperMstID,
       "hpnicfdot1sInstanceTable": hpnicfdot1sInstanceTable,
       "hpnicfdot1sInstanceEntry": hpnicfdot1sInstanceEntry,
       "hpnicfdot1sInstanceID": hpnicfdot1sInstanceID,
       "hpnicfdot1sMstiBridgeID": hpnicfdot1sMstiBridgeID,
       "hpnicfdot1sMstiBridgePriority": hpnicfdot1sMstiBridgePriority,
       "hpnicfdot1sMstiDesignedRoot": hpnicfdot1sMstiDesignedRoot,
       "hpnicfdot1sMstiRootPathCost": hpnicfdot1sMstiRootPathCost,
       "hpnicfdot1sMstiRootPort": hpnicfdot1sMstiRootPort,
       "hpnicfdot1sMstiRootType": hpnicfdot1sMstiRootType,
       "hpnicfdot1sMstiRemainingHops": hpnicfdot1sMstiRemainingHops,
       "hpnicfdot1sMstiAdminMappedVlanListLow": hpnicfdot1sMstiAdminMappedVlanListLow,
       "hpnicfdot1sMstiAdminMappedVlanListHigh": hpnicfdot1sMstiAdminMappedVlanListHigh,
       "hpnicfdot1sMstiOperMappedVlanListLow": hpnicfdot1sMstiOperMappedVlanListLow,
       "hpnicfdot1sMstiOperMappedVlanListHigh": hpnicfdot1sMstiOperMappedVlanListHigh,
       "hpnicfdot1sPortTable": hpnicfdot1sPortTable,
       "hpnicfdot1sPortEntry": hpnicfdot1sPortEntry,
       "hpnicfdot1sMstiPortIndex": hpnicfdot1sMstiPortIndex,
       "hpnicfdot1sMstiState": hpnicfdot1sMstiState,
       "hpnicfdot1sMstiPortPriority": hpnicfdot1sMstiPortPriority,
       "hpnicfdot1sMstiPathCost": hpnicfdot1sMstiPathCost,
       "hpnicfdot1sMstiDesignatedRoot": hpnicfdot1sMstiDesignatedRoot,
       "hpnicfdot1sMstiDesignatedCost": hpnicfdot1sMstiDesignatedCost,
       "hpnicfdot1sMstiDesignatedBridge": hpnicfdot1sMstiDesignatedBridge,
       "hpnicfdot1sMstiDesignatedPort": hpnicfdot1sMstiDesignatedPort,
       "hpnicfdot1sMstiMasterBridgeID": hpnicfdot1sMstiMasterBridgeID,
       "hpnicfdot1sMstiMasterPortCost": hpnicfdot1sMstiMasterPortCost,
       "hpnicfdot1sMstiStpPortEdgeport": hpnicfdot1sMstiStpPortEdgeport,
       "hpnicfdot1sMstiStpPortPointToPoint": hpnicfdot1sMstiStpPortPointToPoint,
       "hpnicfdot1sMstiStpMcheck": hpnicfdot1sMstiStpMcheck,
       "hpnicfdot1sMstiStpTransLimit": hpnicfdot1sMstiStpTransLimit,
       "hpnicfdot1sMstiStpRXStpBPDU": hpnicfdot1sMstiStpRXStpBPDU,
       "hpnicfdot1sMstiStpTXStpBPDU": hpnicfdot1sMstiStpTXStpBPDU,
       "hpnicfdot1sMstiStpRXTCNBPDU": hpnicfdot1sMstiStpRXTCNBPDU,
       "hpnicfdot1sMstiStpTXTCNBPDU": hpnicfdot1sMstiStpTXTCNBPDU,
       "hpnicfdot1sMstiStpRXRSTPBPDU": hpnicfdot1sMstiStpRXRSTPBPDU,
       "hpnicfdot1sMstiStpTXRSTPBPDU": hpnicfdot1sMstiStpTXRSTPBPDU,
       "hpnicfdot1sMstiStpRXMSTPBPDU": hpnicfdot1sMstiStpRXMSTPBPDU,
       "hpnicfdot1sMstiStpTXMSTPBPDU": hpnicfdot1sMstiStpTXMSTPBPDU,
       "hpnicfdot1sMstiStpClearStatistics": hpnicfdot1sMstiStpClearStatistics,
       "hpnicfdot1sMstiStpDefaultPortCost": hpnicfdot1sMstiStpDefaultPortCost,
       "hpnicfdot1sMstiStpStatus": hpnicfdot1sMstiStpStatus,
       "hpnicfdot1sMstiPortRootGuard": hpnicfdot1sMstiPortRootGuard,
       "hpnicfdot1sMstiPortLoopGuard": hpnicfdot1sMstiPortLoopGuard,
       "hpnicfdot1sMstiStpPortSendingBPDUType": hpnicfdot1sMstiStpPortSendingBPDUType,
       "hpnicfdot1sMstiStpOperPortPointToPoint": hpnicfdot1sMstiStpOperPortPointToPoint,
       "hpnicfdot1sMstiStpPortAdminBPDUFmt": hpnicfdot1sMstiStpPortAdminBPDUFmt,
       "hpnicfdot1sMstiStpPortOperBPDUFmt": hpnicfdot1sMstiStpPortOperBPDUFmt,
       "hpnicfdot1sMstiStpPortRoleRestriction": hpnicfdot1sMstiStpPortRoleRestriction,
       "hpnicfdot1sMstiStpPortTcRestriction": hpnicfdot1sMstiStpPortTcRestriction,
       "hpnicfdot1sMstiStpPortDisputed": hpnicfdot1sMstiStpPortDisputed,
       "hpnicfdot1sStpPathCostStandard": hpnicfdot1sStpPathCostStandard}
)
