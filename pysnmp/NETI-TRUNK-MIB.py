# SNMP MIB module (NETI-TRUNK-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/NETI-TRUNK-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:26:36 2024
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

(netiGeneric,) = mibBuilder.importSymbols(
    "NETI-COMMON-MIB",
    "netiGeneric")

(SnmpAdminString,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString")

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
 RowPointer,
 TextualConvention,
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowPointer",
    "TextualConvention",
    "TimeStamp",
    "TruthValue")


# MODULE-IDENTITY

netiTrunkMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2928, 2, 3)
)
netiTrunkMIB.setRevisions(
        ("2014-03-14 08:00",
         "2013-08-29 16:00",
         "2013-01-24 15:00",
         "2009-08-26 15:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class FecMode(Integer32, TextualConvention):
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
        *(("fec1D", 2),
          ("fec2D", 3),
          ("fecNone", 1))
    )



class DppipSupport(OctetString, TextualConvention):
    status = "current"
    displayHint = "1d.1d"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )



# MIB Managed Objects in the order of their OIDs

_TrunkObjects_ObjectIdentity = ObjectIdentity
trunkObjects = _TrunkObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2928, 2, 3, 1)
)
_DppipGroup_ObjectIdentity = ObjectIdentity
dppipGroup = _DppipGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2928, 2, 3, 1, 1)
)
_DppipNumber_Type = Integer32
_DppipNumber_Object = MibScalar
dppipNumber = _DppipNumber_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 3, 1, 1, 1),
    _DppipNumber_Type()
)
dppipNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dppipNumber.setStatus("current")
_DppipLastChange_Type = TimeStamp
_DppipLastChange_Object = MibScalar
dppipLastChange = _DppipLastChange_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 3, 1, 1, 2),
    _DppipLastChange_Type()
)
dppipLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dppipLastChange.setStatus("current")
_DppipTable_Object = MibTable
dppipTable = _DppipTable_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 3, 1, 1, 3)
)
if mibBuilder.loadTexts:
    dppipTable.setStatus("current")
_DppipEntry_Object = MibTableRow
dppipEntry = _DppipEntry_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 3, 1, 1, 3, 1)
)
dppipEntry.setIndexNames(
    (0, "NETI-TRUNK-MIB", "dppipIndex"),
)
if mibBuilder.loadTexts:
    dppipEntry.setStatus("current")
_DppipIndex_Type = Unsigned32
_DppipIndex_Object = MibTableColumn
dppipIndex = _DppipIndex_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 3, 1, 1, 3, 1, 1),
    _DppipIndex_Type()
)
dppipIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dppipIndex.setStatus("current")
_DppipName_Type = SnmpAdminString
_DppipName_Object = MibTableColumn
dppipName = _DppipName_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 3, 1, 1, 3, 1, 2),
    _DppipName_Type()
)
dppipName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dppipName.setStatus("current")
_DppipAddress_Type = IpAddress
_DppipAddress_Object = MibTableColumn
dppipAddress = _DppipAddress_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 3, 1, 1, 3, 1, 3),
    _DppipAddress_Type()
)
dppipAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dppipAddress.setStatus("current")
_DppipNetMask_Type = IpAddress
_DppipNetMask_Object = MibTableColumn
dppipNetMask = _DppipNetMask_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 3, 1, 1, 3, 1, 4),
    _DppipNetMask_Type()
)
dppipNetMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dppipNetMask.setStatus("current")
_DppipDefaultGateway_Type = IpAddress
_DppipDefaultGateway_Object = MibTableColumn
dppipDefaultGateway = _DppipDefaultGateway_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 3, 1, 1, 3, 1, 5),
    _DppipDefaultGateway_Type()
)
dppipDefaultGateway.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dppipDefaultGateway.setStatus("current")
_DppipPeerAddress_Type = IpAddress
_DppipPeerAddress_Object = MibTableColumn
dppipPeerAddress = _DppipPeerAddress_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 3, 1, 1, 3, 1, 6),
    _DppipPeerAddress_Type()
)
dppipPeerAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dppipPeerAddress.setStatus("current")
_DppipTxSlots_Type = Unsigned32
_DppipTxSlots_Object = MibTableColumn
dppipTxSlots = _DppipTxSlots_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 3, 1, 1, 3, 1, 7),
    _DppipTxSlots_Type()
)
dppipTxSlots.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dppipTxSlots.setStatus("current")
_DppipTxUsedCapacity_Type = Gauge32
_DppipTxUsedCapacity_Object = MibTableColumn
dppipTxUsedCapacity = _DppipTxUsedCapacity_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 3, 1, 1, 3, 1, 8),
    _DppipTxUsedCapacity_Type()
)
dppipTxUsedCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dppipTxUsedCapacity.setStatus("current")
_DppipRxSlots_Type = Gauge32
_DppipRxSlots_Object = MibTableColumn
dppipRxSlots = _DppipRxSlots_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 3, 1, 1, 3, 1, 9),
    _DppipRxSlots_Type()
)
dppipRxSlots.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dppipRxSlots.setStatus("current")
_DppipRxUsedCapacity_Type = Gauge32
_DppipRxUsedCapacity_Object = MibTableColumn
dppipRxUsedCapacity = _DppipRxUsedCapacity_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 3, 1, 1, 3, 1, 10),
    _DppipRxUsedCapacity_Type()
)
dppipRxUsedCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dppipRxUsedCapacity.setStatus("current")
_DppipDelayVariation_Type = Unsigned32
_DppipDelayVariation_Object = MibTableColumn
dppipDelayVariation = _DppipDelayVariation_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 3, 1, 1, 3, 1, 11),
    _DppipDelayVariation_Type()
)
dppipDelayVariation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dppipDelayVariation.setStatus("current")


class _DppipOperStatus_Type(Integer32):
    """Custom type dppipOperStatus based on Integer32"""
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
        *(("dormant", 5),
          ("down", 2),
          ("lowerLayerDown", 7),
          ("notPresent", 6),
          ("testing", 3),
          ("unknown", 4),
          ("up", 1))
    )


_DppipOperStatus_Type.__name__ = "Integer32"
_DppipOperStatus_Object = MibTableColumn
dppipOperStatus = _DppipOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 3, 1, 1, 3, 1, 12),
    _DppipOperStatus_Type()
)
dppipOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dppipOperStatus.setStatus("current")
_DppipFailure_Type = SnmpAdminString
_DppipFailure_Object = MibTableColumn
dppipFailure = _DppipFailure_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 3, 1, 1, 3, 1, 13),
    _DppipFailure_Type()
)
dppipFailure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dppipFailure.setStatus("current")
_DppipReceivedFrames_Type = Counter64
_DppipReceivedFrames_Object = MibTableColumn
dppipReceivedFrames = _DppipReceivedFrames_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 3, 1, 1, 3, 1, 14),
    _DppipReceivedFrames_Type()
)
dppipReceivedFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dppipReceivedFrames.setStatus("current")
_DppipMissingFrames_Type = Counter64
_DppipMissingFrames_Object = MibTableColumn
dppipMissingFrames = _DppipMissingFrames_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 3, 1, 1, 3, 1, 15),
    _DppipMissingFrames_Type()
)
dppipMissingFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dppipMissingFrames.setStatus("current")
_DppipDeliveredFrames_Type = Counter64
_DppipDeliveredFrames_Object = MibTableColumn
dppipDeliveredFrames = _DppipDeliveredFrames_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 3, 1, 1, 3, 1, 16),
    _DppipDeliveredFrames_Type()
)
dppipDeliveredFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dppipDeliveredFrames.setStatus("current")
_DppipDroppedFrames_Type = Counter64
_DppipDroppedFrames_Object = MibTableColumn
dppipDroppedFrames = _DppipDroppedFrames_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 3, 1, 1, 3, 1, 17),
    _DppipDroppedFrames_Type()
)
dppipDroppedFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dppipDroppedFrames.setStatus("current")
_DppipDuplicateFrames_Type = Counter64
_DppipDuplicateFrames_Object = MibTableColumn
dppipDuplicateFrames = _DppipDuplicateFrames_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 3, 1, 1, 3, 1, 18),
    _DppipDuplicateFrames_Type()
)
dppipDuplicateFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dppipDuplicateFrames.setStatus("current")
_DppipReorderedFrames_Type = Counter64
_DppipReorderedFrames_Object = MibTableColumn
dppipReorderedFrames = _DppipReorderedFrames_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 3, 1, 1, 3, 1, 19),
    _DppipReorderedFrames_Type()
)
dppipReorderedFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dppipReorderedFrames.setStatus("current")
_DppipLostFrames_Type = Counter64
_DppipLostFrames_Object = MibTableColumn
dppipLostFrames = _DppipLostFrames_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 3, 1, 1, 3, 1, 20),
    _DppipLostFrames_Type()
)
dppipLostFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dppipLostFrames.setStatus("current")
_DppipRecoveredFrames_Type = Counter64
_DppipRecoveredFrames_Object = MibTableColumn
dppipRecoveredFrames = _DppipRecoveredFrames_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 3, 1, 1, 3, 1, 21),
    _DppipRecoveredFrames_Type()
)
dppipRecoveredFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dppipRecoveredFrames.setStatus("current")
_DppipSentFrames_Type = Counter64
_DppipSentFrames_Object = MibTableColumn
dppipSentFrames = _DppipSentFrames_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 3, 1, 1, 3, 1, 22),
    _DppipSentFrames_Type()
)
dppipSentFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dppipSentFrames.setStatus("current")
_DppipDelayVarPtp_Type = Unsigned32
_DppipDelayVarPtp_Object = MibTableColumn
dppipDelayVarPtp = _DppipDelayVarPtp_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 3, 1, 1, 3, 1, 23),
    _DppipDelayVarPtp_Type()
)
dppipDelayVarPtp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dppipDelayVarPtp.setStatus("current")
_DppipDelayVar999_Type = Unsigned32
_DppipDelayVar999_Object = MibTableColumn
dppipDelayVar999 = _DppipDelayVar999_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 3, 1, 1, 3, 1, 24),
    _DppipDelayVar999_Type()
)
dppipDelayVar999.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dppipDelayVar999.setStatus("current")


class _DppipAdminStatus_Type(Integer32):
    """Custom type dppipAdminStatus based on Integer32"""
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


_DppipAdminStatus_Type.__name__ = "Integer32"
_DppipAdminStatus_Object = MibTableColumn
dppipAdminStatus = _DppipAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 3, 1, 1, 3, 1, 25),
    _DppipAdminStatus_Type()
)
dppipAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dppipAdminStatus.setStatus("current")


class _DppipVlan_Type(Integer32):
    """Custom type dppipVlan based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 4095),
    )


_DppipVlan_Type.__name__ = "Integer32"
_DppipVlan_Object = MibTableColumn
dppipVlan = _DppipVlan_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 3, 1, 1, 3, 1, 26),
    _DppipVlan_Type()
)
dppipVlan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dppipVlan.setStatus("current")
_DppipDelayVar01_Type = Unsigned32
_DppipDelayVar01_Object = MibTableColumn
dppipDelayVar01 = _DppipDelayVar01_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 3, 1, 1, 3, 1, 27),
    _DppipDelayVar01_Type()
)
dppipDelayVar01.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dppipDelayVar01.setStatus("current")


class _DppipPrio_Type(Unsigned32):
    """Custom type dppipPrio based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_DppipPrio_Type.__name__ = "Unsigned32"
_DppipPrio_Object = MibTableColumn
dppipPrio = _DppipPrio_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 3, 1, 1, 3, 1, 28),
    _DppipPrio_Type()
)
dppipPrio.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dppipPrio.setStatus("current")
_DppipPhysIf_Type = RowPointer
_DppipPhysIf_Object = MibTableColumn
dppipPhysIf = _DppipPhysIf_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 3, 1, 1, 3, 1, 29),
    _DppipPhysIf_Type()
)
dppipPhysIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dppipPhysIf.setStatus("current")


class _DppipMtu_Type(Unsigned32):
    """Custom type dppipMtu based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(64, 1500),
    )


_DppipMtu_Type.__name__ = "Unsigned32"
_DppipMtu_Object = MibTableColumn
dppipMtu = _DppipMtu_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 3, 1, 1, 3, 1, 30),
    _DppipMtu_Type()
)
dppipMtu.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dppipMtu.setStatus("current")


class _DppipTtl_Type(Unsigned32):
    """Custom type dppipTtl based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 127),
    )


_DppipTtl_Type.__name__ = "Unsigned32"
_DppipTtl_Object = MibTableColumn
dppipTtl = _DppipTtl_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 3, 1, 1, 3, 1, 31),
    _DppipTtl_Type()
)
dppipTtl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dppipTtl.setStatus("current")


class _DppipDscp_Type(Unsigned32):
    """Custom type dppipDscp based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_DppipDscp_Type.__name__ = "Unsigned32"
_DppipDscp_Object = MibTableColumn
dppipDscp = _DppipDscp_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 3, 1, 1, 3, 1, 32),
    _DppipDscp_Type()
)
dppipDscp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dppipDscp.setStatus("current")
_DppipRxSlotsPerFrame_Type = Unsigned32
_DppipRxSlotsPerFrame_Object = MibTableColumn
dppipRxSlotsPerFrame = _DppipRxSlotsPerFrame_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 3, 1, 1, 3, 1, 33),
    _DppipRxSlotsPerFrame_Type()
)
dppipRxSlotsPerFrame.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dppipRxSlotsPerFrame.setStatus("current")
_DppipAvailTxSlots_Type = Gauge32
_DppipAvailTxSlots_Object = MibTableColumn
dppipAvailTxSlots = _DppipAvailTxSlots_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 3, 1, 1, 3, 1, 34),
    _DppipAvailTxSlots_Type()
)
dppipAvailTxSlots.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dppipAvailTxSlots.setStatus("current")
_DppipAvailRxSlots_Type = Gauge32
_DppipAvailRxSlots_Object = MibTableColumn
dppipAvailRxSlots = _DppipAvailRxSlots_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 3, 1, 1, 3, 1, 35),
    _DppipAvailRxSlots_Type()
)
dppipAvailRxSlots.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dppipAvailRxSlots.setStatus("current")
_DppipMinUsageRatio_Type = Unsigned32
_DppipMinUsageRatio_Object = MibTableColumn
dppipMinUsageRatio = _DppipMinUsageRatio_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 3, 1, 1, 3, 1, 36),
    _DppipMinUsageRatio_Type()
)
dppipMinUsageRatio.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dppipMinUsageRatio.setStatus("current")
_DppipTxTranspSlots_Type = Gauge32
_DppipTxTranspSlots_Object = MibTableColumn
dppipTxTranspSlots = _DppipTxTranspSlots_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 3, 1, 1, 3, 1, 37),
    _DppipTxTranspSlots_Type()
)
dppipTxTranspSlots.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dppipTxTranspSlots.setStatus("current")
_DppipRxTranspSlots_Type = Gauge32
_DppipRxTranspSlots_Object = MibTableColumn
dppipRxTranspSlots = _DppipRxTranspSlots_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 3, 1, 1, 3, 1, 38),
    _DppipRxTranspSlots_Type()
)
dppipRxTranspSlots.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dppipRxTranspSlots.setStatus("current")
_DppipNomDTDelay_Type = Unsigned32
_DppipNomDTDelay_Object = MibTableColumn
dppipNomDTDelay = _DppipNomDTDelay_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 3, 1, 1, 3, 1, 39),
    _DppipNomDTDelay_Type()
)
dppipNomDTDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dppipNomDTDelay.setStatus("current")
_DppipTxFecMode_Type = FecMode
_DppipTxFecMode_Object = MibTableColumn
dppipTxFecMode = _DppipTxFecMode_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 3, 1, 1, 3, 1, 40),
    _DppipTxFecMode_Type()
)
dppipTxFecMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dppipTxFecMode.setStatus("current")
_DppipTxFecRows_Type = Unsigned32
_DppipTxFecRows_Object = MibTableColumn
dppipTxFecRows = _DppipTxFecRows_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 3, 1, 1, 3, 1, 41),
    _DppipTxFecRows_Type()
)
dppipTxFecRows.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dppipTxFecRows.setStatus("current")
_DppipTxFecCols_Type = Unsigned32
_DppipTxFecCols_Object = MibTableColumn
dppipTxFecCols = _DppipTxFecCols_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 3, 1, 1, 3, 1, 42),
    _DppipTxFecCols_Type()
)
dppipTxFecCols.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dppipTxFecCols.setStatus("current")
_DppipRxFecMode_Type = FecMode
_DppipRxFecMode_Object = MibTableColumn
dppipRxFecMode = _DppipRxFecMode_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 3, 1, 1, 3, 1, 43),
    _DppipRxFecMode_Type()
)
dppipRxFecMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dppipRxFecMode.setStatus("current")
_DppipRxFecRows_Type = Unsigned32
_DppipRxFecRows_Object = MibTableColumn
dppipRxFecRows = _DppipRxFecRows_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 3, 1, 1, 3, 1, 44),
    _DppipRxFecRows_Type()
)
dppipRxFecRows.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dppipRxFecRows.setStatus("current")
_DppipRxFecCols_Type = Unsigned32
_DppipRxFecCols_Object = MibTableColumn
dppipRxFecCols = _DppipRxFecCols_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 3, 1, 1, 3, 1, 45),
    _DppipRxFecCols_Type()
)
dppipRxFecCols.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dppipRxFecCols.setStatus("current")


class _DppipCntControl_Type(Integer32):
    """Custom type dppipCntControl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("reset", 1)
    )


_DppipCntControl_Type.__name__ = "Integer32"
_DppipCntControl_Object = MibTableColumn
dppipCntControl = _DppipCntControl_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 3, 1, 1, 3, 1, 46),
    _DppipCntControl_Type()
)
dppipCntControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dppipCntControl.setStatus("current")
_DppipSuppressAlarms_Type = TruthValue
_DppipSuppressAlarms_Object = MibTableColumn
dppipSuppressAlarms = _DppipSuppressAlarms_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 3, 1, 1, 3, 1, 47),
    _DppipSuppressAlarms_Type()
)
dppipSuppressAlarms.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dppipSuppressAlarms.setStatus("current")


class _DppipSigFailFilter_Type(Unsigned32):
    """Custom type dppipSigFailFilter based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2000),
    )


_DppipSigFailFilter_Type.__name__ = "Unsigned32"
_DppipSigFailFilter_Object = MibTableColumn
dppipSigFailFilter = _DppipSigFailFilter_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 3, 1, 1, 3, 1, 48),
    _DppipSigFailFilter_Type()
)
dppipSigFailFilter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dppipSigFailFilter.setStatus("current")


class _DppipDegThreshold_Type(Unsigned32):
    """Custom type dppipDegThreshold based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8000),
    )


_DppipDegThreshold_Type.__name__ = "Unsigned32"
_DppipDegThreshold_Object = MibTableColumn
dppipDegThreshold = _DppipDegThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 3, 1, 1, 3, 1, 49),
    _DppipDegThreshold_Type()
)
dppipDegThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dppipDegThreshold.setStatus("current")


class _DppipDegPeriod_Type(Unsigned32):
    """Custom type dppipDegPeriod based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 10),
    )


_DppipDegPeriod_Type.__name__ = "Unsigned32"
_DppipDegPeriod_Object = MibTableColumn
dppipDegPeriod = _DppipDegPeriod_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 3, 1, 1, 3, 1, 50),
    _DppipDegPeriod_Type()
)
dppipDegPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dppipDegPeriod.setStatus("current")
_DppipTolJitter_Type = Unsigned32
_DppipTolJitter_Object = MibTableColumn
dppipTolJitter = _DppipTolJitter_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 3, 1, 1, 3, 1, 51),
    _DppipTolJitter_Type()
)
dppipTolJitter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dppipTolJitter.setStatus("current")
_DppipLimitsTable_Object = MibTable
dppipLimitsTable = _DppipLimitsTable_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 3, 1, 1, 4)
)
if mibBuilder.loadTexts:
    dppipLimitsTable.setStatus("current")
_DppipLimitsEntry_Object = MibTableRow
dppipLimitsEntry = _DppipLimitsEntry_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 3, 1, 1, 4, 1)
)
dppipLimitsEntry.setIndexNames(
    (0, "NETI-TRUNK-MIB", "dppipIndex"),
)
if mibBuilder.loadTexts:
    dppipLimitsEntry.setStatus("current")
_DppipMaxFecMode_Type = FecMode
_DppipMaxFecMode_Object = MibTableColumn
dppipMaxFecMode = _DppipMaxFecMode_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 3, 1, 1, 4, 1, 1),
    _DppipMaxFecMode_Type()
)
dppipMaxFecMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dppipMaxFecMode.setStatus("current")
_DppipMaxFecRows_Type = Unsigned32
_DppipMaxFecRows_Object = MibTableColumn
dppipMaxFecRows = _DppipMaxFecRows_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 3, 1, 1, 4, 1, 2),
    _DppipMaxFecRows_Type()
)
dppipMaxFecRows.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dppipMaxFecRows.setStatus("current")
_DppipMinFecRows_Type = Unsigned32
_DppipMinFecRows_Object = MibTableColumn
dppipMinFecRows = _DppipMinFecRows_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 3, 1, 1, 4, 1, 3),
    _DppipMinFecRows_Type()
)
dppipMinFecRows.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dppipMinFecRows.setStatus("current")
_DppipMaxFecCols_Type = Unsigned32
_DppipMaxFecCols_Object = MibTableColumn
dppipMaxFecCols = _DppipMaxFecCols_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 3, 1, 1, 4, 1, 4),
    _DppipMaxFecCols_Type()
)
dppipMaxFecCols.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dppipMaxFecCols.setStatus("current")
_DppipMinFecCols_Type = Unsigned32
_DppipMinFecCols_Object = MibTableColumn
dppipMinFecCols = _DppipMinFecCols_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 3, 1, 1, 4, 1, 5),
    _DppipMinFecCols_Type()
)
dppipMinFecCols.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dppipMinFecCols.setStatus("current")
_DppipMaxFecElems_Type = Unsigned32
_DppipMaxFecElems_Object = MibTableColumn
dppipMaxFecElems = _DppipMaxFecElems_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 3, 1, 1, 4, 1, 6),
    _DppipMaxFecElems_Type()
)
dppipMaxFecElems.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dppipMaxFecElems.setStatus("current")
_DppipMaxTxSlots_Type = Unsigned32
_DppipMaxTxSlots_Object = MibTableColumn
dppipMaxTxSlots = _DppipMaxTxSlots_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 3, 1, 1, 4, 1, 7),
    _DppipMaxTxSlots_Type()
)
dppipMaxTxSlots.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dppipMaxTxSlots.setStatus("current")
_DppipMinTxSlots_Type = Unsigned32
_DppipMinTxSlots_Object = MibTableColumn
dppipMinTxSlots = _DppipMinTxSlots_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 3, 1, 1, 4, 1, 8),
    _DppipMinTxSlots_Type()
)
dppipMinTxSlots.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dppipMinTxSlots.setStatus("current")
_DppipMaxTolJitter_Type = Unsigned32
_DppipMaxTolJitter_Object = MibTableColumn
dppipMaxTolJitter = _DppipMaxTolJitter_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 3, 1, 1, 4, 1, 9),
    _DppipMaxTolJitter_Type()
)
dppipMaxTolJitter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dppipMaxTolJitter.setStatus("current")
_DppipMinTolJitter_Type = Unsigned32
_DppipMinTolJitter_Object = MibTableColumn
dppipMinTolJitter = _DppipMinTolJitter_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 3, 1, 1, 4, 1, 10),
    _DppipMinTolJitter_Type()
)
dppipMinTolJitter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dppipMinTolJitter.setStatus("current")
_DppipDTSupport_Type = DppipSupport
_DppipDTSupport_Object = MibTableColumn
dppipDTSupport = _DppipDTSupport_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 3, 1, 1, 4, 1, 11),
    _DppipDTSupport_Type()
)
dppipDTSupport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dppipDTSupport.setStatus("current")
_DppipTTSupport_Type = DppipSupport
_DppipTTSupport_Object = MibTableColumn
dppipTTSupport = _DppipTTSupport_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 3, 1, 1, 4, 1, 12),
    _DppipTTSupport_Type()
)
dppipTTSupport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dppipTTSupport.setStatus("current")
_DppipPeerLimitsTable_Object = MibTable
dppipPeerLimitsTable = _DppipPeerLimitsTable_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 3, 1, 1, 5)
)
if mibBuilder.loadTexts:
    dppipPeerLimitsTable.setStatus("current")
_DppipPeerLimitsEntry_Object = MibTableRow
dppipPeerLimitsEntry = _DppipPeerLimitsEntry_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 3, 1, 1, 5, 1)
)
dppipPeerLimitsEntry.setIndexNames(
    (0, "NETI-TRUNK-MIB", "dppipIndex"),
)
if mibBuilder.loadTexts:
    dppipPeerLimitsEntry.setStatus("current")
_DppipPeerMaxFecMode_Type = FecMode
_DppipPeerMaxFecMode_Object = MibTableColumn
dppipPeerMaxFecMode = _DppipPeerMaxFecMode_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 3, 1, 1, 5, 1, 1),
    _DppipPeerMaxFecMode_Type()
)
dppipPeerMaxFecMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dppipPeerMaxFecMode.setStatus("current")
_DppipPeerMaxFecRows_Type = Unsigned32
_DppipPeerMaxFecRows_Object = MibTableColumn
dppipPeerMaxFecRows = _DppipPeerMaxFecRows_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 3, 1, 1, 5, 1, 2),
    _DppipPeerMaxFecRows_Type()
)
dppipPeerMaxFecRows.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dppipPeerMaxFecRows.setStatus("current")
_DppipPeerMinFecRows_Type = Unsigned32
_DppipPeerMinFecRows_Object = MibTableColumn
dppipPeerMinFecRows = _DppipPeerMinFecRows_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 3, 1, 1, 5, 1, 3),
    _DppipPeerMinFecRows_Type()
)
dppipPeerMinFecRows.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dppipPeerMinFecRows.setStatus("current")
_DppipPeerMaxFecCols_Type = Unsigned32
_DppipPeerMaxFecCols_Object = MibTableColumn
dppipPeerMaxFecCols = _DppipPeerMaxFecCols_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 3, 1, 1, 5, 1, 4),
    _DppipPeerMaxFecCols_Type()
)
dppipPeerMaxFecCols.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dppipPeerMaxFecCols.setStatus("current")
_DppipPeerMinFecCols_Type = Unsigned32
_DppipPeerMinFecCols_Object = MibTableColumn
dppipPeerMinFecCols = _DppipPeerMinFecCols_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 3, 1, 1, 5, 1, 5),
    _DppipPeerMinFecCols_Type()
)
dppipPeerMinFecCols.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dppipPeerMinFecCols.setStatus("current")
_DppipPeerMaxFecElems_Type = Unsigned32
_DppipPeerMaxFecElems_Object = MibTableColumn
dppipPeerMaxFecElems = _DppipPeerMaxFecElems_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 3, 1, 1, 5, 1, 6),
    _DppipPeerMaxFecElems_Type()
)
dppipPeerMaxFecElems.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dppipPeerMaxFecElems.setStatus("current")
_DppipPeerMaxRxSlots_Type = Unsigned32
_DppipPeerMaxRxSlots_Object = MibTableColumn
dppipPeerMaxRxSlots = _DppipPeerMaxRxSlots_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 3, 1, 1, 5, 1, 7),
    _DppipPeerMaxRxSlots_Type()
)
dppipPeerMaxRxSlots.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dppipPeerMaxRxSlots.setStatus("current")
_DppipPeerMinRxSlots_Type = Unsigned32
_DppipPeerMinRxSlots_Object = MibTableColumn
dppipPeerMinRxSlots = _DppipPeerMinRxSlots_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 3, 1, 1, 5, 1, 8),
    _DppipPeerMinRxSlots_Type()
)
dppipPeerMinRxSlots.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dppipPeerMinRxSlots.setStatus("current")
_DppipPeerDTSupport_Type = DppipSupport
_DppipPeerDTSupport_Object = MibTableColumn
dppipPeerDTSupport = _DppipPeerDTSupport_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 3, 1, 1, 5, 1, 9),
    _DppipPeerDTSupport_Type()
)
dppipPeerDTSupport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dppipPeerDTSupport.setStatus("current")
_DppipPeerTTSupport_Type = DppipSupport
_DppipPeerTTSupport_Object = MibTableColumn
dppipPeerTTSupport = _DppipPeerTTSupport_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 3, 1, 1, 5, 1, 10),
    _DppipPeerTTSupport_Type()
)
dppipPeerTTSupport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dppipPeerTTSupport.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "NETI-TRUNK-MIB",
    **{"FecMode": FecMode,
       "DppipSupport": DppipSupport,
       "netiTrunkMIB": netiTrunkMIB,
       "trunkObjects": trunkObjects,
       "dppipGroup": dppipGroup,
       "dppipNumber": dppipNumber,
       "dppipLastChange": dppipLastChange,
       "dppipTable": dppipTable,
       "dppipEntry": dppipEntry,
       "dppipIndex": dppipIndex,
       "dppipName": dppipName,
       "dppipAddress": dppipAddress,
       "dppipNetMask": dppipNetMask,
       "dppipDefaultGateway": dppipDefaultGateway,
       "dppipPeerAddress": dppipPeerAddress,
       "dppipTxSlots": dppipTxSlots,
       "dppipTxUsedCapacity": dppipTxUsedCapacity,
       "dppipRxSlots": dppipRxSlots,
       "dppipRxUsedCapacity": dppipRxUsedCapacity,
       "dppipDelayVariation": dppipDelayVariation,
       "dppipOperStatus": dppipOperStatus,
       "dppipFailure": dppipFailure,
       "dppipReceivedFrames": dppipReceivedFrames,
       "dppipMissingFrames": dppipMissingFrames,
       "dppipDeliveredFrames": dppipDeliveredFrames,
       "dppipDroppedFrames": dppipDroppedFrames,
       "dppipDuplicateFrames": dppipDuplicateFrames,
       "dppipReorderedFrames": dppipReorderedFrames,
       "dppipLostFrames": dppipLostFrames,
       "dppipRecoveredFrames": dppipRecoveredFrames,
       "dppipSentFrames": dppipSentFrames,
       "dppipDelayVarPtp": dppipDelayVarPtp,
       "dppipDelayVar999": dppipDelayVar999,
       "dppipAdminStatus": dppipAdminStatus,
       "dppipVlan": dppipVlan,
       "dppipDelayVar01": dppipDelayVar01,
       "dppipPrio": dppipPrio,
       "dppipPhysIf": dppipPhysIf,
       "dppipMtu": dppipMtu,
       "dppipTtl": dppipTtl,
       "dppipDscp": dppipDscp,
       "dppipRxSlotsPerFrame": dppipRxSlotsPerFrame,
       "dppipAvailTxSlots": dppipAvailTxSlots,
       "dppipAvailRxSlots": dppipAvailRxSlots,
       "dppipMinUsageRatio": dppipMinUsageRatio,
       "dppipTxTranspSlots": dppipTxTranspSlots,
       "dppipRxTranspSlots": dppipRxTranspSlots,
       "dppipNomDTDelay": dppipNomDTDelay,
       "dppipTxFecMode": dppipTxFecMode,
       "dppipTxFecRows": dppipTxFecRows,
       "dppipTxFecCols": dppipTxFecCols,
       "dppipRxFecMode": dppipRxFecMode,
       "dppipRxFecRows": dppipRxFecRows,
       "dppipRxFecCols": dppipRxFecCols,
       "dppipCntControl": dppipCntControl,
       "dppipSuppressAlarms": dppipSuppressAlarms,
       "dppipSigFailFilter": dppipSigFailFilter,
       "dppipDegThreshold": dppipDegThreshold,
       "dppipDegPeriod": dppipDegPeriod,
       "dppipTolJitter": dppipTolJitter,
       "dppipLimitsTable": dppipLimitsTable,
       "dppipLimitsEntry": dppipLimitsEntry,
       "dppipMaxFecMode": dppipMaxFecMode,
       "dppipMaxFecRows": dppipMaxFecRows,
       "dppipMinFecRows": dppipMinFecRows,
       "dppipMaxFecCols": dppipMaxFecCols,
       "dppipMinFecCols": dppipMinFecCols,
       "dppipMaxFecElems": dppipMaxFecElems,
       "dppipMaxTxSlots": dppipMaxTxSlots,
       "dppipMinTxSlots": dppipMinTxSlots,
       "dppipMaxTolJitter": dppipMaxTolJitter,
       "dppipMinTolJitter": dppipMinTolJitter,
       "dppipDTSupport": dppipDTSupport,
       "dppipTTSupport": dppipTTSupport,
       "dppipPeerLimitsTable": dppipPeerLimitsTable,
       "dppipPeerLimitsEntry": dppipPeerLimitsEntry,
       "dppipPeerMaxFecMode": dppipPeerMaxFecMode,
       "dppipPeerMaxFecRows": dppipPeerMaxFecRows,
       "dppipPeerMinFecRows": dppipPeerMinFecRows,
       "dppipPeerMaxFecCols": dppipPeerMaxFecCols,
       "dppipPeerMinFecCols": dppipPeerMinFecCols,
       "dppipPeerMaxFecElems": dppipPeerMaxFecElems,
       "dppipPeerMaxRxSlots": dppipPeerMaxRxSlots,
       "dppipPeerMinRxSlots": dppipPeerMinRxSlots,
       "dppipPeerDTSupport": dppipPeerDTSupport,
       "dppipPeerTTSupport": dppipPeerTTSupport}
)
