# SNMP MIB module (HH3C-LswMSTP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HH3C-LswMSTP-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:53:58 2024
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

(hh3clswCommon,) = mibBuilder.importSymbols(
    "HH3C-OID-MIB",
    "hh3clswCommon")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY

hh3cdot1sMstp = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 14)
)
hh3cdot1sMstp.setRevisions(
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



class Hh3cdot1sFormatStatus(Integer32, TextualConvention):
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

_Hh3cMstpEventsV2_ObjectIdentity = ObjectIdentity
hh3cMstpEventsV2 = _Hh3cMstpEventsV2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 14, 0)
)
if mibBuilder.loadTexts:
    hh3cMstpEventsV2.setStatus("current")


class _Hh3cdot1sStpStatus_Type(EnabledStatus):
    """Custom type hh3cdot1sStpStatus based on EnabledStatus"""
    defaultValue = 2


_Hh3cdot1sStpStatus_Object = MibScalar
hh3cdot1sStpStatus = _Hh3cdot1sStpStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 14, 1),
    _Hh3cdot1sStpStatus_Type()
)
hh3cdot1sStpStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cdot1sStpStatus.setStatus("current")


class _Hh3cdot1sStpForceVersion_Type(Integer32):
    """Custom type hh3cdot1sStpForceVersion based on Integer32"""
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


_Hh3cdot1sStpForceVersion_Type.__name__ = "Integer32"
_Hh3cdot1sStpForceVersion_Object = MibScalar
hh3cdot1sStpForceVersion = _Hh3cdot1sStpForceVersion_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 14, 2),
    _Hh3cdot1sStpForceVersion_Type()
)
hh3cdot1sStpForceVersion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cdot1sStpForceVersion.setStatus("current")


class _Hh3cdot1sStpDiameter_Type(Integer32):
    """Custom type hh3cdot1sStpDiameter based on Integer32"""
    defaultValue = 7

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 7),
    )


_Hh3cdot1sStpDiameter_Type.__name__ = "Integer32"
_Hh3cdot1sStpDiameter_Object = MibScalar
hh3cdot1sStpDiameter = _Hh3cdot1sStpDiameter_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 14, 3),
    _Hh3cdot1sStpDiameter_Type()
)
hh3cdot1sStpDiameter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cdot1sStpDiameter.setStatus("current")


class _Hh3cdot1sMstBridgeMaxHops_Type(Integer32):
    """Custom type hh3cdot1sMstBridgeMaxHops based on Integer32"""
    defaultValue = 20

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 40),
    )


_Hh3cdot1sMstBridgeMaxHops_Type.__name__ = "Integer32"
_Hh3cdot1sMstBridgeMaxHops_Object = MibScalar
hh3cdot1sMstBridgeMaxHops = _Hh3cdot1sMstBridgeMaxHops_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 14, 4),
    _Hh3cdot1sMstBridgeMaxHops_Type()
)
hh3cdot1sMstBridgeMaxHops.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cdot1sMstBridgeMaxHops.setStatus("current")
_Hh3cdot1sMstMasterBridgeID_Type = BridgeId
_Hh3cdot1sMstMasterBridgeID_Object = MibScalar
hh3cdot1sMstMasterBridgeID = _Hh3cdot1sMstMasterBridgeID_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 14, 5),
    _Hh3cdot1sMstMasterBridgeID_Type()
)
hh3cdot1sMstMasterBridgeID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cdot1sMstMasterBridgeID.setStatus("current")


class _Hh3cdot1sMstMasterPathCost_Type(Integer32):
    """Custom type hh3cdot1sMstMasterPathCost based on Integer32"""
    defaultValue = 0


_Hh3cdot1sMstMasterPathCost_Object = MibScalar
hh3cdot1sMstMasterPathCost = _Hh3cdot1sMstMasterPathCost_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 14, 6),
    _Hh3cdot1sMstMasterPathCost_Type()
)
hh3cdot1sMstMasterPathCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cdot1sMstMasterPathCost.setStatus("current")


class _Hh3cdot1sMstBpduGuard_Type(EnabledStatus):
    """Custom type hh3cdot1sMstBpduGuard based on EnabledStatus"""


_Hh3cdot1sMstBpduGuard_Object = MibScalar
hh3cdot1sMstBpduGuard = _Hh3cdot1sMstBpduGuard_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 14, 7),
    _Hh3cdot1sMstBpduGuard_Type()
)
hh3cdot1sMstBpduGuard.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cdot1sMstBpduGuard.setStatus("current")


class _Hh3cdot1sMstAdminFormatSelector_Type(Integer32):
    """Custom type hh3cdot1sMstAdminFormatSelector based on Integer32"""
    defaultValue = 0


_Hh3cdot1sMstAdminFormatSelector_Object = MibScalar
hh3cdot1sMstAdminFormatSelector = _Hh3cdot1sMstAdminFormatSelector_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 14, 8),
    _Hh3cdot1sMstAdminFormatSelector_Type()
)
hh3cdot1sMstAdminFormatSelector.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cdot1sMstAdminFormatSelector.setStatus("current")


class _Hh3cdot1sMstAdminRegionName_Type(OctetString):
    """Custom type hh3cdot1sMstAdminRegionName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_Hh3cdot1sMstAdminRegionName_Type.__name__ = "OctetString"
_Hh3cdot1sMstAdminRegionName_Object = MibScalar
hh3cdot1sMstAdminRegionName = _Hh3cdot1sMstAdminRegionName_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 14, 9),
    _Hh3cdot1sMstAdminRegionName_Type()
)
hh3cdot1sMstAdminRegionName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cdot1sMstAdminRegionName.setStatus("current")


class _Hh3cdot1sMstAdminRevisionLevel_Type(Integer32):
    """Custom type hh3cdot1sMstAdminRevisionLevel based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Hh3cdot1sMstAdminRevisionLevel_Type.__name__ = "Integer32"
_Hh3cdot1sMstAdminRevisionLevel_Object = MibScalar
hh3cdot1sMstAdminRevisionLevel = _Hh3cdot1sMstAdminRevisionLevel_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 14, 10),
    _Hh3cdot1sMstAdminRevisionLevel_Type()
)
hh3cdot1sMstAdminRevisionLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cdot1sMstAdminRevisionLevel.setStatus("current")


class _Hh3cdot1sMstOperFormatSelector_Type(Integer32):
    """Custom type hh3cdot1sMstOperFormatSelector based on Integer32"""
    defaultValue = 0


_Hh3cdot1sMstOperFormatSelector_Object = MibScalar
hh3cdot1sMstOperFormatSelector = _Hh3cdot1sMstOperFormatSelector_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 14, 11),
    _Hh3cdot1sMstOperFormatSelector_Type()
)
hh3cdot1sMstOperFormatSelector.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cdot1sMstOperFormatSelector.setStatus("current")


class _Hh3cdot1sMstOperRegionName_Type(OctetString):
    """Custom type hh3cdot1sMstOperRegionName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Hh3cdot1sMstOperRegionName_Type.__name__ = "OctetString"
_Hh3cdot1sMstOperRegionName_Object = MibScalar
hh3cdot1sMstOperRegionName = _Hh3cdot1sMstOperRegionName_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 14, 12),
    _Hh3cdot1sMstOperRegionName_Type()
)
hh3cdot1sMstOperRegionName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cdot1sMstOperRegionName.setStatus("current")


class _Hh3cdot1sMstOperRevisionLevel_Type(Integer32):
    """Custom type hh3cdot1sMstOperRevisionLevel based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Hh3cdot1sMstOperRevisionLevel_Type.__name__ = "Integer32"
_Hh3cdot1sMstOperRevisionLevel_Object = MibScalar
hh3cdot1sMstOperRevisionLevel = _Hh3cdot1sMstOperRevisionLevel_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 14, 13),
    _Hh3cdot1sMstOperRevisionLevel_Type()
)
hh3cdot1sMstOperRevisionLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cdot1sMstOperRevisionLevel.setStatus("current")


class _Hh3cdot1sMstOperConfigDigest_Type(OctetString):
    """Custom type hh3cdot1sMstOperConfigDigest based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_Hh3cdot1sMstOperConfigDigest_Type.__name__ = "OctetString"
_Hh3cdot1sMstOperConfigDigest_Object = MibScalar
hh3cdot1sMstOperConfigDigest = _Hh3cdot1sMstOperConfigDigest_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 14, 14),
    _Hh3cdot1sMstOperConfigDigest_Type()
)
hh3cdot1sMstOperConfigDigest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cdot1sMstOperConfigDigest.setStatus("current")


class _Hh3cdot1sMstRegionConfActive_Type(Integer32):
    """Custom type hh3cdot1sMstRegionConfActive based on Integer32"""
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


_Hh3cdot1sMstRegionConfActive_Type.__name__ = "Integer32"
_Hh3cdot1sMstRegionConfActive_Object = MibScalar
hh3cdot1sMstRegionConfActive = _Hh3cdot1sMstRegionConfActive_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 14, 15),
    _Hh3cdot1sMstRegionConfActive_Type()
)
hh3cdot1sMstRegionConfActive.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cdot1sMstRegionConfActive.setStatus("current")


class _Hh3cdot1sMstDefaultVlanAllo_Type(Integer32):
    """Custom type hh3cdot1sMstDefaultVlanAllo based on Integer32"""
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


_Hh3cdot1sMstDefaultVlanAllo_Type.__name__ = "Integer32"
_Hh3cdot1sMstDefaultVlanAllo_Object = MibScalar
hh3cdot1sMstDefaultVlanAllo = _Hh3cdot1sMstDefaultVlanAllo_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 14, 16),
    _Hh3cdot1sMstDefaultVlanAllo_Type()
)
hh3cdot1sMstDefaultVlanAllo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cdot1sMstDefaultVlanAllo.setStatus("current")


class _Hh3cdot1sMstDefaultRegionName_Type(Integer32):
    """Custom type hh3cdot1sMstDefaultRegionName based on Integer32"""
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


_Hh3cdot1sMstDefaultRegionName_Type.__name__ = "Integer32"
_Hh3cdot1sMstDefaultRegionName_Object = MibScalar
hh3cdot1sMstDefaultRegionName = _Hh3cdot1sMstDefaultRegionName_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 14, 17),
    _Hh3cdot1sMstDefaultRegionName_Type()
)
hh3cdot1sMstDefaultRegionName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cdot1sMstDefaultRegionName.setStatus("current")
_Hh3cdot1sVIDAllocationTable_Object = MibTable
hh3cdot1sVIDAllocationTable = _Hh3cdot1sVIDAllocationTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 14, 18)
)
if mibBuilder.loadTexts:
    hh3cdot1sVIDAllocationTable.setStatus("current")
_Hh3cdot1sVIDAllocationEntry_Object = MibTableRow
hh3cdot1sVIDAllocationEntry = _Hh3cdot1sVIDAllocationEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 14, 18, 1)
)
hh3cdot1sVIDAllocationEntry.setIndexNames(
    (0, "HH3C-LswMSTP-MIB", "hh3cdot1sMstVID"),
)
if mibBuilder.loadTexts:
    hh3cdot1sVIDAllocationEntry.setStatus("current")


class _Hh3cdot1sMstVID_Type(Integer32):
    """Custom type hh3cdot1sMstVID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_Hh3cdot1sMstVID_Type.__name__ = "Integer32"
_Hh3cdot1sMstVID_Object = MibTableColumn
hh3cdot1sMstVID = _Hh3cdot1sMstVID_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 14, 18, 1, 1),
    _Hh3cdot1sMstVID_Type()
)
hh3cdot1sMstVID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cdot1sMstVID.setStatus("current")


class _Hh3cdot1sAdminMstID_Type(Integer32):
    """Custom type hh3cdot1sAdminMstID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 64),
    )


_Hh3cdot1sAdminMstID_Type.__name__ = "Integer32"
_Hh3cdot1sAdminMstID_Object = MibTableColumn
hh3cdot1sAdminMstID = _Hh3cdot1sAdminMstID_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 14, 18, 1, 2),
    _Hh3cdot1sAdminMstID_Type()
)
hh3cdot1sAdminMstID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cdot1sAdminMstID.setStatus("current")


class _Hh3cdot1sOperMstID_Type(Integer32):
    """Custom type hh3cdot1sOperMstID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 64),
    )


_Hh3cdot1sOperMstID_Type.__name__ = "Integer32"
_Hh3cdot1sOperMstID_Object = MibTableColumn
hh3cdot1sOperMstID = _Hh3cdot1sOperMstID_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 14, 18, 1, 3),
    _Hh3cdot1sOperMstID_Type()
)
hh3cdot1sOperMstID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cdot1sOperMstID.setStatus("current")
_Hh3cdot1sInstanceTable_Object = MibTable
hh3cdot1sInstanceTable = _Hh3cdot1sInstanceTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 14, 19)
)
if mibBuilder.loadTexts:
    hh3cdot1sInstanceTable.setStatus("current")
_Hh3cdot1sInstanceEntry_Object = MibTableRow
hh3cdot1sInstanceEntry = _Hh3cdot1sInstanceEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 14, 19, 1)
)
hh3cdot1sInstanceEntry.setIndexNames(
    (0, "HH3C-LswMSTP-MIB", "hh3cdot1sInstanceID"),
)
if mibBuilder.loadTexts:
    hh3cdot1sInstanceEntry.setStatus("current")


class _Hh3cdot1sInstanceID_Type(Integer32):
    """Custom type hh3cdot1sInstanceID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 64),
    )


_Hh3cdot1sInstanceID_Type.__name__ = "Integer32"
_Hh3cdot1sInstanceID_Object = MibTableColumn
hh3cdot1sInstanceID = _Hh3cdot1sInstanceID_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 14, 19, 1, 1),
    _Hh3cdot1sInstanceID_Type()
)
hh3cdot1sInstanceID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cdot1sInstanceID.setStatus("current")
_Hh3cdot1sMstiBridgeID_Type = BridgeId
_Hh3cdot1sMstiBridgeID_Object = MibTableColumn
hh3cdot1sMstiBridgeID = _Hh3cdot1sMstiBridgeID_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 14, 19, 1, 2),
    _Hh3cdot1sMstiBridgeID_Type()
)
hh3cdot1sMstiBridgeID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cdot1sMstiBridgeID.setStatus("current")


class _Hh3cdot1sMstiBridgePriority_Type(Integer32):
    """Custom type hh3cdot1sMstiBridgePriority based on Integer32"""
    defaultValue = 32768

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 61440),
    )


_Hh3cdot1sMstiBridgePriority_Type.__name__ = "Integer32"
_Hh3cdot1sMstiBridgePriority_Object = MibTableColumn
hh3cdot1sMstiBridgePriority = _Hh3cdot1sMstiBridgePriority_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 14, 19, 1, 3),
    _Hh3cdot1sMstiBridgePriority_Type()
)
hh3cdot1sMstiBridgePriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cdot1sMstiBridgePriority.setStatus("current")
_Hh3cdot1sMstiDesignedRoot_Type = BridgeId
_Hh3cdot1sMstiDesignedRoot_Object = MibTableColumn
hh3cdot1sMstiDesignedRoot = _Hh3cdot1sMstiDesignedRoot_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 14, 19, 1, 4),
    _Hh3cdot1sMstiDesignedRoot_Type()
)
hh3cdot1sMstiDesignedRoot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cdot1sMstiDesignedRoot.setStatus("current")
_Hh3cdot1sMstiRootPathCost_Type = Integer32
_Hh3cdot1sMstiRootPathCost_Object = MibTableColumn
hh3cdot1sMstiRootPathCost = _Hh3cdot1sMstiRootPathCost_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 14, 19, 1, 5),
    _Hh3cdot1sMstiRootPathCost_Type()
)
hh3cdot1sMstiRootPathCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cdot1sMstiRootPathCost.setStatus("current")
_Hh3cdot1sMstiRootPort_Type = Integer32
_Hh3cdot1sMstiRootPort_Object = MibTableColumn
hh3cdot1sMstiRootPort = _Hh3cdot1sMstiRootPort_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 14, 19, 1, 6),
    _Hh3cdot1sMstiRootPort_Type()
)
hh3cdot1sMstiRootPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cdot1sMstiRootPort.setStatus("current")


class _Hh3cdot1sMstiRootType_Type(Integer32):
    """Custom type hh3cdot1sMstiRootType based on Integer32"""
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


_Hh3cdot1sMstiRootType_Type.__name__ = "Integer32"
_Hh3cdot1sMstiRootType_Object = MibTableColumn
hh3cdot1sMstiRootType = _Hh3cdot1sMstiRootType_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 14, 19, 1, 7),
    _Hh3cdot1sMstiRootType_Type()
)
hh3cdot1sMstiRootType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cdot1sMstiRootType.setStatus("current")
_Hh3cdot1sMstiRemainingHops_Type = Integer32
_Hh3cdot1sMstiRemainingHops_Object = MibTableColumn
hh3cdot1sMstiRemainingHops = _Hh3cdot1sMstiRemainingHops_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 14, 19, 1, 8),
    _Hh3cdot1sMstiRemainingHops_Type()
)
hh3cdot1sMstiRemainingHops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cdot1sMstiRemainingHops.setStatus("current")


class _Hh3cdot1sMstiAdminMappedVlanListLow_Type(OctetString):
    """Custom type hh3cdot1sMstiAdminMappedVlanListLow based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_Hh3cdot1sMstiAdminMappedVlanListLow_Type.__name__ = "OctetString"
_Hh3cdot1sMstiAdminMappedVlanListLow_Object = MibTableColumn
hh3cdot1sMstiAdminMappedVlanListLow = _Hh3cdot1sMstiAdminMappedVlanListLow_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 14, 19, 1, 9),
    _Hh3cdot1sMstiAdminMappedVlanListLow_Type()
)
hh3cdot1sMstiAdminMappedVlanListLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cdot1sMstiAdminMappedVlanListLow.setStatus("current")


class _Hh3cdot1sMstiAdminMappedVlanListHigh_Type(OctetString):
    """Custom type hh3cdot1sMstiAdminMappedVlanListHigh based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_Hh3cdot1sMstiAdminMappedVlanListHigh_Type.__name__ = "OctetString"
_Hh3cdot1sMstiAdminMappedVlanListHigh_Object = MibTableColumn
hh3cdot1sMstiAdminMappedVlanListHigh = _Hh3cdot1sMstiAdminMappedVlanListHigh_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 14, 19, 1, 10),
    _Hh3cdot1sMstiAdminMappedVlanListHigh_Type()
)
hh3cdot1sMstiAdminMappedVlanListHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cdot1sMstiAdminMappedVlanListHigh.setStatus("current")


class _Hh3cdot1sMstiOperMappedVlanListLow_Type(OctetString):
    """Custom type hh3cdot1sMstiOperMappedVlanListLow based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_Hh3cdot1sMstiOperMappedVlanListLow_Type.__name__ = "OctetString"
_Hh3cdot1sMstiOperMappedVlanListLow_Object = MibTableColumn
hh3cdot1sMstiOperMappedVlanListLow = _Hh3cdot1sMstiOperMappedVlanListLow_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 14, 19, 1, 11),
    _Hh3cdot1sMstiOperMappedVlanListLow_Type()
)
hh3cdot1sMstiOperMappedVlanListLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cdot1sMstiOperMappedVlanListLow.setStatus("current")


class _Hh3cdot1sMstiOperMappedVlanListHigh_Type(OctetString):
    """Custom type hh3cdot1sMstiOperMappedVlanListHigh based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_Hh3cdot1sMstiOperMappedVlanListHigh_Type.__name__ = "OctetString"
_Hh3cdot1sMstiOperMappedVlanListHigh_Object = MibTableColumn
hh3cdot1sMstiOperMappedVlanListHigh = _Hh3cdot1sMstiOperMappedVlanListHigh_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 14, 19, 1, 12),
    _Hh3cdot1sMstiOperMappedVlanListHigh_Type()
)
hh3cdot1sMstiOperMappedVlanListHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cdot1sMstiOperMappedVlanListHigh.setStatus("current")
_Hh3cdot1sPortTable_Object = MibTable
hh3cdot1sPortTable = _Hh3cdot1sPortTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 14, 20)
)
if mibBuilder.loadTexts:
    hh3cdot1sPortTable.setStatus("current")
_Hh3cdot1sPortEntry_Object = MibTableRow
hh3cdot1sPortEntry = _Hh3cdot1sPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 14, 20, 1)
)
hh3cdot1sPortEntry.setIndexNames(
    (0, "HH3C-LswMSTP-MIB", "hh3cdot1sInstanceID"),
    (0, "HH3C-LswMSTP-MIB", "hh3cdot1sMstiPortIndex"),
)
if mibBuilder.loadTexts:
    hh3cdot1sPortEntry.setStatus("current")
_Hh3cdot1sMstiPortIndex_Type = Integer32
_Hh3cdot1sMstiPortIndex_Object = MibTableColumn
hh3cdot1sMstiPortIndex = _Hh3cdot1sMstiPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 14, 20, 1, 1),
    _Hh3cdot1sMstiPortIndex_Type()
)
hh3cdot1sMstiPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cdot1sMstiPortIndex.setStatus("current")


class _Hh3cdot1sMstiState_Type(Integer32):
    """Custom type hh3cdot1sMstiState based on Integer32"""
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


_Hh3cdot1sMstiState_Type.__name__ = "Integer32"
_Hh3cdot1sMstiState_Object = MibTableColumn
hh3cdot1sMstiState = _Hh3cdot1sMstiState_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 14, 20, 1, 2),
    _Hh3cdot1sMstiState_Type()
)
hh3cdot1sMstiState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cdot1sMstiState.setStatus("current")


class _Hh3cdot1sMstiPortPriority_Type(Integer32):
    """Custom type hh3cdot1sMstiPortPriority based on Integer32"""
    defaultValue = 128

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 240),
    )


_Hh3cdot1sMstiPortPriority_Type.__name__ = "Integer32"
_Hh3cdot1sMstiPortPriority_Object = MibTableColumn
hh3cdot1sMstiPortPriority = _Hh3cdot1sMstiPortPriority_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 14, 20, 1, 3),
    _Hh3cdot1sMstiPortPriority_Type()
)
hh3cdot1sMstiPortPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cdot1sMstiPortPriority.setStatus("current")


class _Hh3cdot1sMstiPathCost_Type(Integer32):
    """Custom type hh3cdot1sMstiPathCost based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 200000000),
    )


_Hh3cdot1sMstiPathCost_Type.__name__ = "Integer32"
_Hh3cdot1sMstiPathCost_Object = MibTableColumn
hh3cdot1sMstiPathCost = _Hh3cdot1sMstiPathCost_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 14, 20, 1, 4),
    _Hh3cdot1sMstiPathCost_Type()
)
hh3cdot1sMstiPathCost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cdot1sMstiPathCost.setStatus("current")
_Hh3cdot1sMstiDesignatedRoot_Type = BridgeId
_Hh3cdot1sMstiDesignatedRoot_Object = MibTableColumn
hh3cdot1sMstiDesignatedRoot = _Hh3cdot1sMstiDesignatedRoot_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 14, 20, 1, 5),
    _Hh3cdot1sMstiDesignatedRoot_Type()
)
hh3cdot1sMstiDesignatedRoot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cdot1sMstiDesignatedRoot.setStatus("current")
_Hh3cdot1sMstiDesignatedCost_Type = Integer32
_Hh3cdot1sMstiDesignatedCost_Object = MibTableColumn
hh3cdot1sMstiDesignatedCost = _Hh3cdot1sMstiDesignatedCost_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 14, 20, 1, 6),
    _Hh3cdot1sMstiDesignatedCost_Type()
)
hh3cdot1sMstiDesignatedCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cdot1sMstiDesignatedCost.setStatus("current")
_Hh3cdot1sMstiDesignatedBridge_Type = BridgeId
_Hh3cdot1sMstiDesignatedBridge_Object = MibTableColumn
hh3cdot1sMstiDesignatedBridge = _Hh3cdot1sMstiDesignatedBridge_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 14, 20, 1, 7),
    _Hh3cdot1sMstiDesignatedBridge_Type()
)
hh3cdot1sMstiDesignatedBridge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cdot1sMstiDesignatedBridge.setStatus("current")


class _Hh3cdot1sMstiDesignatedPort_Type(OctetString):
    """Custom type hh3cdot1sMstiDesignatedPort based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_Hh3cdot1sMstiDesignatedPort_Type.__name__ = "OctetString"
_Hh3cdot1sMstiDesignatedPort_Object = MibTableColumn
hh3cdot1sMstiDesignatedPort = _Hh3cdot1sMstiDesignatedPort_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 14, 20, 1, 8),
    _Hh3cdot1sMstiDesignatedPort_Type()
)
hh3cdot1sMstiDesignatedPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cdot1sMstiDesignatedPort.setStatus("current")
_Hh3cdot1sMstiMasterBridgeID_Type = BridgeId
_Hh3cdot1sMstiMasterBridgeID_Object = MibTableColumn
hh3cdot1sMstiMasterBridgeID = _Hh3cdot1sMstiMasterBridgeID_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 14, 20, 1, 9),
    _Hh3cdot1sMstiMasterBridgeID_Type()
)
hh3cdot1sMstiMasterBridgeID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cdot1sMstiMasterBridgeID.setStatus("current")
_Hh3cdot1sMstiMasterPortCost_Type = Integer32
_Hh3cdot1sMstiMasterPortCost_Object = MibTableColumn
hh3cdot1sMstiMasterPortCost = _Hh3cdot1sMstiMasterPortCost_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 14, 20, 1, 10),
    _Hh3cdot1sMstiMasterPortCost_Type()
)
hh3cdot1sMstiMasterPortCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cdot1sMstiMasterPortCost.setStatus("current")


class _Hh3cdot1sMstiStpPortEdgeport_Type(EnabledStatus):
    """Custom type hh3cdot1sMstiStpPortEdgeport based on EnabledStatus"""


_Hh3cdot1sMstiStpPortEdgeport_Object = MibTableColumn
hh3cdot1sMstiStpPortEdgeport = _Hh3cdot1sMstiStpPortEdgeport_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 14, 20, 1, 11),
    _Hh3cdot1sMstiStpPortEdgeport_Type()
)
hh3cdot1sMstiStpPortEdgeport.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cdot1sMstiStpPortEdgeport.setStatus("current")


class _Hh3cdot1sMstiStpPortPointToPoint_Type(Integer32):
    """Custom type hh3cdot1sMstiStpPortPointToPoint based on Integer32"""
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


_Hh3cdot1sMstiStpPortPointToPoint_Type.__name__ = "Integer32"
_Hh3cdot1sMstiStpPortPointToPoint_Object = MibTableColumn
hh3cdot1sMstiStpPortPointToPoint = _Hh3cdot1sMstiStpPortPointToPoint_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 14, 20, 1, 12),
    _Hh3cdot1sMstiStpPortPointToPoint_Type()
)
hh3cdot1sMstiStpPortPointToPoint.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cdot1sMstiStpPortPointToPoint.setStatus("current")


class _Hh3cdot1sMstiStpMcheck_Type(Integer32):
    """Custom type hh3cdot1sMstiStpMcheck based on Integer32"""
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


_Hh3cdot1sMstiStpMcheck_Type.__name__ = "Integer32"
_Hh3cdot1sMstiStpMcheck_Object = MibTableColumn
hh3cdot1sMstiStpMcheck = _Hh3cdot1sMstiStpMcheck_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 14, 20, 1, 13),
    _Hh3cdot1sMstiStpMcheck_Type()
)
hh3cdot1sMstiStpMcheck.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cdot1sMstiStpMcheck.setStatus("current")


class _Hh3cdot1sMstiStpTransLimit_Type(Integer32):
    """Custom type hh3cdot1sMstiStpTransLimit based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_Hh3cdot1sMstiStpTransLimit_Type.__name__ = "Integer32"
_Hh3cdot1sMstiStpTransLimit_Object = MibTableColumn
hh3cdot1sMstiStpTransLimit = _Hh3cdot1sMstiStpTransLimit_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 14, 20, 1, 14),
    _Hh3cdot1sMstiStpTransLimit_Type()
)
hh3cdot1sMstiStpTransLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cdot1sMstiStpTransLimit.setStatus("current")
_Hh3cdot1sMstiStpRXStpBPDU_Type = Counter32
_Hh3cdot1sMstiStpRXStpBPDU_Object = MibTableColumn
hh3cdot1sMstiStpRXStpBPDU = _Hh3cdot1sMstiStpRXStpBPDU_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 14, 20, 1, 15),
    _Hh3cdot1sMstiStpRXStpBPDU_Type()
)
hh3cdot1sMstiStpRXStpBPDU.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cdot1sMstiStpRXStpBPDU.setStatus("current")
_Hh3cdot1sMstiStpTXStpBPDU_Type = Counter32
_Hh3cdot1sMstiStpTXStpBPDU_Object = MibTableColumn
hh3cdot1sMstiStpTXStpBPDU = _Hh3cdot1sMstiStpTXStpBPDU_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 14, 20, 1, 16),
    _Hh3cdot1sMstiStpTXStpBPDU_Type()
)
hh3cdot1sMstiStpTXStpBPDU.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cdot1sMstiStpTXStpBPDU.setStatus("current")
_Hh3cdot1sMstiStpRXTCNBPDU_Type = Counter32
_Hh3cdot1sMstiStpRXTCNBPDU_Object = MibTableColumn
hh3cdot1sMstiStpRXTCNBPDU = _Hh3cdot1sMstiStpRXTCNBPDU_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 14, 20, 1, 17),
    _Hh3cdot1sMstiStpRXTCNBPDU_Type()
)
hh3cdot1sMstiStpRXTCNBPDU.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cdot1sMstiStpRXTCNBPDU.setStatus("current")
_Hh3cdot1sMstiStpTXTCNBPDU_Type = Counter32
_Hh3cdot1sMstiStpTXTCNBPDU_Object = MibTableColumn
hh3cdot1sMstiStpTXTCNBPDU = _Hh3cdot1sMstiStpTXTCNBPDU_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 14, 20, 1, 18),
    _Hh3cdot1sMstiStpTXTCNBPDU_Type()
)
hh3cdot1sMstiStpTXTCNBPDU.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cdot1sMstiStpTXTCNBPDU.setStatus("current")
_Hh3cdot1sMstiStpRXRSTPBPDU_Type = Counter32
_Hh3cdot1sMstiStpRXRSTPBPDU_Object = MibTableColumn
hh3cdot1sMstiStpRXRSTPBPDU = _Hh3cdot1sMstiStpRXRSTPBPDU_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 14, 20, 1, 19),
    _Hh3cdot1sMstiStpRXRSTPBPDU_Type()
)
hh3cdot1sMstiStpRXRSTPBPDU.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cdot1sMstiStpRXRSTPBPDU.setStatus("current")
_Hh3cdot1sMstiStpTXRSTPBPDU_Type = Counter32
_Hh3cdot1sMstiStpTXRSTPBPDU_Object = MibTableColumn
hh3cdot1sMstiStpTXRSTPBPDU = _Hh3cdot1sMstiStpTXRSTPBPDU_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 14, 20, 1, 20),
    _Hh3cdot1sMstiStpTXRSTPBPDU_Type()
)
hh3cdot1sMstiStpTXRSTPBPDU.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cdot1sMstiStpTXRSTPBPDU.setStatus("current")
_Hh3cdot1sMstiStpRXMSTPBPDU_Type = Counter32
_Hh3cdot1sMstiStpRXMSTPBPDU_Object = MibTableColumn
hh3cdot1sMstiStpRXMSTPBPDU = _Hh3cdot1sMstiStpRXMSTPBPDU_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 14, 20, 1, 21),
    _Hh3cdot1sMstiStpRXMSTPBPDU_Type()
)
hh3cdot1sMstiStpRXMSTPBPDU.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cdot1sMstiStpRXMSTPBPDU.setStatus("current")
_Hh3cdot1sMstiStpTXMSTPBPDU_Type = Counter32
_Hh3cdot1sMstiStpTXMSTPBPDU_Object = MibTableColumn
hh3cdot1sMstiStpTXMSTPBPDU = _Hh3cdot1sMstiStpTXMSTPBPDU_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 14, 20, 1, 22),
    _Hh3cdot1sMstiStpTXMSTPBPDU_Type()
)
hh3cdot1sMstiStpTXMSTPBPDU.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cdot1sMstiStpTXMSTPBPDU.setStatus("current")


class _Hh3cdot1sMstiStpClearStatistics_Type(Integer32):
    """Custom type hh3cdot1sMstiStpClearStatistics based on Integer32"""
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


_Hh3cdot1sMstiStpClearStatistics_Type.__name__ = "Integer32"
_Hh3cdot1sMstiStpClearStatistics_Object = MibTableColumn
hh3cdot1sMstiStpClearStatistics = _Hh3cdot1sMstiStpClearStatistics_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 14, 20, 1, 23),
    _Hh3cdot1sMstiStpClearStatistics_Type()
)
hh3cdot1sMstiStpClearStatistics.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cdot1sMstiStpClearStatistics.setStatus("current")


class _Hh3cdot1sMstiStpDefaultPortCost_Type(Integer32):
    """Custom type hh3cdot1sMstiStpDefaultPortCost based on Integer32"""
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


_Hh3cdot1sMstiStpDefaultPortCost_Type.__name__ = "Integer32"
_Hh3cdot1sMstiStpDefaultPortCost_Object = MibTableColumn
hh3cdot1sMstiStpDefaultPortCost = _Hh3cdot1sMstiStpDefaultPortCost_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 14, 20, 1, 24),
    _Hh3cdot1sMstiStpDefaultPortCost_Type()
)
hh3cdot1sMstiStpDefaultPortCost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cdot1sMstiStpDefaultPortCost.setStatus("current")


class _Hh3cdot1sMstiStpStatus_Type(EnabledStatus):
    """Custom type hh3cdot1sMstiStpStatus based on EnabledStatus"""


_Hh3cdot1sMstiStpStatus_Object = MibTableColumn
hh3cdot1sMstiStpStatus = _Hh3cdot1sMstiStpStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 14, 20, 1, 25),
    _Hh3cdot1sMstiStpStatus_Type()
)
hh3cdot1sMstiStpStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cdot1sMstiStpStatus.setStatus("current")


class _Hh3cdot1sMstiPortRootGuard_Type(EnabledStatus):
    """Custom type hh3cdot1sMstiPortRootGuard based on EnabledStatus"""


_Hh3cdot1sMstiPortRootGuard_Object = MibTableColumn
hh3cdot1sMstiPortRootGuard = _Hh3cdot1sMstiPortRootGuard_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 14, 20, 1, 26),
    _Hh3cdot1sMstiPortRootGuard_Type()
)
hh3cdot1sMstiPortRootGuard.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cdot1sMstiPortRootGuard.setStatus("current")


class _Hh3cdot1sMstiPortLoopGuard_Type(EnabledStatus):
    """Custom type hh3cdot1sMstiPortLoopGuard based on EnabledStatus"""


_Hh3cdot1sMstiPortLoopGuard_Object = MibTableColumn
hh3cdot1sMstiPortLoopGuard = _Hh3cdot1sMstiPortLoopGuard_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 14, 20, 1, 27),
    _Hh3cdot1sMstiPortLoopGuard_Type()
)
hh3cdot1sMstiPortLoopGuard.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cdot1sMstiPortLoopGuard.setStatus("current")


class _Hh3cdot1sMstiStpPortSendingBPDUType_Type(Integer32):
    """Custom type hh3cdot1sMstiStpPortSendingBPDUType based on Integer32"""
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


_Hh3cdot1sMstiStpPortSendingBPDUType_Type.__name__ = "Integer32"
_Hh3cdot1sMstiStpPortSendingBPDUType_Object = MibTableColumn
hh3cdot1sMstiStpPortSendingBPDUType = _Hh3cdot1sMstiStpPortSendingBPDUType_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 14, 20, 1, 28),
    _Hh3cdot1sMstiStpPortSendingBPDUType_Type()
)
hh3cdot1sMstiStpPortSendingBPDUType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cdot1sMstiStpPortSendingBPDUType.setStatus("current")


class _Hh3cdot1sMstiStpOperPortPointToPoint_Type(Integer32):
    """Custom type hh3cdot1sMstiStpOperPortPointToPoint based on Integer32"""
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


_Hh3cdot1sMstiStpOperPortPointToPoint_Type.__name__ = "Integer32"
_Hh3cdot1sMstiStpOperPortPointToPoint_Object = MibTableColumn
hh3cdot1sMstiStpOperPortPointToPoint = _Hh3cdot1sMstiStpOperPortPointToPoint_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 14, 20, 1, 29),
    _Hh3cdot1sMstiStpOperPortPointToPoint_Type()
)
hh3cdot1sMstiStpOperPortPointToPoint.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cdot1sMstiStpOperPortPointToPoint.setStatus("current")
_Hh3cdot1sMstiStpPortAdminBPDUFmt_Type = Hh3cdot1sFormatStatus
_Hh3cdot1sMstiStpPortAdminBPDUFmt_Object = MibTableColumn
hh3cdot1sMstiStpPortAdminBPDUFmt = _Hh3cdot1sMstiStpPortAdminBPDUFmt_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 14, 20, 1, 30),
    _Hh3cdot1sMstiStpPortAdminBPDUFmt_Type()
)
hh3cdot1sMstiStpPortAdminBPDUFmt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cdot1sMstiStpPortAdminBPDUFmt.setStatus("current")
_Hh3cdot1sMstiStpPortOperBPDUFmt_Type = Hh3cdot1sFormatStatus
_Hh3cdot1sMstiStpPortOperBPDUFmt_Object = MibTableColumn
hh3cdot1sMstiStpPortOperBPDUFmt = _Hh3cdot1sMstiStpPortOperBPDUFmt_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 14, 20, 1, 31),
    _Hh3cdot1sMstiStpPortOperBPDUFmt_Type()
)
hh3cdot1sMstiStpPortOperBPDUFmt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cdot1sMstiStpPortOperBPDUFmt.setStatus("current")


class _Hh3cdot1sStpPathCostStandard_Type(Integer32):
    """Custom type hh3cdot1sStpPathCostStandard based on Integer32"""
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


_Hh3cdot1sStpPathCostStandard_Type.__name__ = "Integer32"
_Hh3cdot1sStpPathCostStandard_Object = MibScalar
hh3cdot1sStpPathCostStandard = _Hh3cdot1sStpPathCostStandard_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 14, 21),
    _Hh3cdot1sStpPathCostStandard_Type()
)
hh3cdot1sStpPathCostStandard.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cdot1sStpPathCostStandard.setStatus("current")

# Managed Objects groups


# Notification objects

hh3cPortMstiStateForwarding = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 14, 0, 1)
)
hh3cPortMstiStateForwarding.setObjects(
      *(("HH3C-LswMSTP-MIB", "hh3cdot1sInstanceID"),
        ("HH3C-LswMSTP-MIB", "hh3cdot1sMstiPortIndex"))
)
if mibBuilder.loadTexts:
    hh3cPortMstiStateForwarding.setStatus(
        "current"
    )

hh3cPortMstiStateDiscarding = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 14, 0, 2)
)
hh3cPortMstiStateDiscarding.setObjects(
      *(("HH3C-LswMSTP-MIB", "hh3cdot1sInstanceID"),
        ("HH3C-LswMSTP-MIB", "hh3cdot1sMstiPortIndex"))
)
if mibBuilder.loadTexts:
    hh3cPortMstiStateDiscarding.setStatus(
        "current"
    )

hh3cBridgeLostRootPrimary = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 14, 0, 3)
)
hh3cBridgeLostRootPrimary.setObjects(
    ("HH3C-LswMSTP-MIB", "hh3cdot1sInstanceID")
)
if mibBuilder.loadTexts:
    hh3cBridgeLostRootPrimary.setStatus(
        "current"
    )

hh3cPortMstiRootGuarded = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 14, 0, 4)
)
hh3cPortMstiRootGuarded.setObjects(
      *(("HH3C-LswMSTP-MIB", "hh3cdot1sInstanceID"),
        ("HH3C-LswMSTP-MIB", "hh3cdot1sMstiPortIndex"))
)
if mibBuilder.loadTexts:
    hh3cPortMstiRootGuarded.setStatus(
        "current"
    )

hh3cPortMstiBpduGuarded = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 14, 0, 5)
)
hh3cPortMstiBpduGuarded.setObjects(
    ("BRIDGE-MIB", "dot1dStpPort")
)
if mibBuilder.loadTexts:
    hh3cPortMstiBpduGuarded.setStatus(
        "current"
    )

hh3cPortMstiLoopGuarded = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 14, 0, 6)
)
hh3cPortMstiLoopGuarded.setObjects(
      *(("HH3C-LswMSTP-MIB", "hh3cdot1sInstanceID"),
        ("HH3C-LswMSTP-MIB", "hh3cdot1sMstiPortIndex"))
)
if mibBuilder.loadTexts:
    hh3cPortMstiLoopGuarded.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HH3C-LswMSTP-MIB",
    **{"EnabledStatus": EnabledStatus,
       "BridgeId": BridgeId,
       "Hh3cdot1sFormatStatus": Hh3cdot1sFormatStatus,
       "hh3cdot1sMstp": hh3cdot1sMstp,
       "hh3cMstpEventsV2": hh3cMstpEventsV2,
       "hh3cPortMstiStateForwarding": hh3cPortMstiStateForwarding,
       "hh3cPortMstiStateDiscarding": hh3cPortMstiStateDiscarding,
       "hh3cBridgeLostRootPrimary": hh3cBridgeLostRootPrimary,
       "hh3cPortMstiRootGuarded": hh3cPortMstiRootGuarded,
       "hh3cPortMstiBpduGuarded": hh3cPortMstiBpduGuarded,
       "hh3cPortMstiLoopGuarded": hh3cPortMstiLoopGuarded,
       "hh3cdot1sStpStatus": hh3cdot1sStpStatus,
       "hh3cdot1sStpForceVersion": hh3cdot1sStpForceVersion,
       "hh3cdot1sStpDiameter": hh3cdot1sStpDiameter,
       "hh3cdot1sMstBridgeMaxHops": hh3cdot1sMstBridgeMaxHops,
       "hh3cdot1sMstMasterBridgeID": hh3cdot1sMstMasterBridgeID,
       "hh3cdot1sMstMasterPathCost": hh3cdot1sMstMasterPathCost,
       "hh3cdot1sMstBpduGuard": hh3cdot1sMstBpduGuard,
       "hh3cdot1sMstAdminFormatSelector": hh3cdot1sMstAdminFormatSelector,
       "hh3cdot1sMstAdminRegionName": hh3cdot1sMstAdminRegionName,
       "hh3cdot1sMstAdminRevisionLevel": hh3cdot1sMstAdminRevisionLevel,
       "hh3cdot1sMstOperFormatSelector": hh3cdot1sMstOperFormatSelector,
       "hh3cdot1sMstOperRegionName": hh3cdot1sMstOperRegionName,
       "hh3cdot1sMstOperRevisionLevel": hh3cdot1sMstOperRevisionLevel,
       "hh3cdot1sMstOperConfigDigest": hh3cdot1sMstOperConfigDigest,
       "hh3cdot1sMstRegionConfActive": hh3cdot1sMstRegionConfActive,
       "hh3cdot1sMstDefaultVlanAllo": hh3cdot1sMstDefaultVlanAllo,
       "hh3cdot1sMstDefaultRegionName": hh3cdot1sMstDefaultRegionName,
       "hh3cdot1sVIDAllocationTable": hh3cdot1sVIDAllocationTable,
       "hh3cdot1sVIDAllocationEntry": hh3cdot1sVIDAllocationEntry,
       "hh3cdot1sMstVID": hh3cdot1sMstVID,
       "hh3cdot1sAdminMstID": hh3cdot1sAdminMstID,
       "hh3cdot1sOperMstID": hh3cdot1sOperMstID,
       "hh3cdot1sInstanceTable": hh3cdot1sInstanceTable,
       "hh3cdot1sInstanceEntry": hh3cdot1sInstanceEntry,
       "hh3cdot1sInstanceID": hh3cdot1sInstanceID,
       "hh3cdot1sMstiBridgeID": hh3cdot1sMstiBridgeID,
       "hh3cdot1sMstiBridgePriority": hh3cdot1sMstiBridgePriority,
       "hh3cdot1sMstiDesignedRoot": hh3cdot1sMstiDesignedRoot,
       "hh3cdot1sMstiRootPathCost": hh3cdot1sMstiRootPathCost,
       "hh3cdot1sMstiRootPort": hh3cdot1sMstiRootPort,
       "hh3cdot1sMstiRootType": hh3cdot1sMstiRootType,
       "hh3cdot1sMstiRemainingHops": hh3cdot1sMstiRemainingHops,
       "hh3cdot1sMstiAdminMappedVlanListLow": hh3cdot1sMstiAdminMappedVlanListLow,
       "hh3cdot1sMstiAdminMappedVlanListHigh": hh3cdot1sMstiAdminMappedVlanListHigh,
       "hh3cdot1sMstiOperMappedVlanListLow": hh3cdot1sMstiOperMappedVlanListLow,
       "hh3cdot1sMstiOperMappedVlanListHigh": hh3cdot1sMstiOperMappedVlanListHigh,
       "hh3cdot1sPortTable": hh3cdot1sPortTable,
       "hh3cdot1sPortEntry": hh3cdot1sPortEntry,
       "hh3cdot1sMstiPortIndex": hh3cdot1sMstiPortIndex,
       "hh3cdot1sMstiState": hh3cdot1sMstiState,
       "hh3cdot1sMstiPortPriority": hh3cdot1sMstiPortPriority,
       "hh3cdot1sMstiPathCost": hh3cdot1sMstiPathCost,
       "hh3cdot1sMstiDesignatedRoot": hh3cdot1sMstiDesignatedRoot,
       "hh3cdot1sMstiDesignatedCost": hh3cdot1sMstiDesignatedCost,
       "hh3cdot1sMstiDesignatedBridge": hh3cdot1sMstiDesignatedBridge,
       "hh3cdot1sMstiDesignatedPort": hh3cdot1sMstiDesignatedPort,
       "hh3cdot1sMstiMasterBridgeID": hh3cdot1sMstiMasterBridgeID,
       "hh3cdot1sMstiMasterPortCost": hh3cdot1sMstiMasterPortCost,
       "hh3cdot1sMstiStpPortEdgeport": hh3cdot1sMstiStpPortEdgeport,
       "hh3cdot1sMstiStpPortPointToPoint": hh3cdot1sMstiStpPortPointToPoint,
       "hh3cdot1sMstiStpMcheck": hh3cdot1sMstiStpMcheck,
       "hh3cdot1sMstiStpTransLimit": hh3cdot1sMstiStpTransLimit,
       "hh3cdot1sMstiStpRXStpBPDU": hh3cdot1sMstiStpRXStpBPDU,
       "hh3cdot1sMstiStpTXStpBPDU": hh3cdot1sMstiStpTXStpBPDU,
       "hh3cdot1sMstiStpRXTCNBPDU": hh3cdot1sMstiStpRXTCNBPDU,
       "hh3cdot1sMstiStpTXTCNBPDU": hh3cdot1sMstiStpTXTCNBPDU,
       "hh3cdot1sMstiStpRXRSTPBPDU": hh3cdot1sMstiStpRXRSTPBPDU,
       "hh3cdot1sMstiStpTXRSTPBPDU": hh3cdot1sMstiStpTXRSTPBPDU,
       "hh3cdot1sMstiStpRXMSTPBPDU": hh3cdot1sMstiStpRXMSTPBPDU,
       "hh3cdot1sMstiStpTXMSTPBPDU": hh3cdot1sMstiStpTXMSTPBPDU,
       "hh3cdot1sMstiStpClearStatistics": hh3cdot1sMstiStpClearStatistics,
       "hh3cdot1sMstiStpDefaultPortCost": hh3cdot1sMstiStpDefaultPortCost,
       "hh3cdot1sMstiStpStatus": hh3cdot1sMstiStpStatus,
       "hh3cdot1sMstiPortRootGuard": hh3cdot1sMstiPortRootGuard,
       "hh3cdot1sMstiPortLoopGuard": hh3cdot1sMstiPortLoopGuard,
       "hh3cdot1sMstiStpPortSendingBPDUType": hh3cdot1sMstiStpPortSendingBPDUType,
       "hh3cdot1sMstiStpOperPortPointToPoint": hh3cdot1sMstiStpOperPortPointToPoint,
       "hh3cdot1sMstiStpPortAdminBPDUFmt": hh3cdot1sMstiStpPortAdminBPDUFmt,
       "hh3cdot1sMstiStpPortOperBPDUFmt": hh3cdot1sMstiStpPortOperBPDUFmt,
       "hh3cdot1sStpPathCostStandard": hh3cdot1sStpPathCostStandard}
)
