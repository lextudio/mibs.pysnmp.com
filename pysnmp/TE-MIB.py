# SNMP MIB module (TE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/TE-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:01:04 2024
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

(MplsBitRate,
 TeHopAddress,
 TeHopAddressType) = mibBuilder.importSymbols(
    "MPLS-TC-STD-MIB",
    "MplsBitRate",
    "TeHopAddress",
    "TeHopAddressType")

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
 iso,
 mib_2) = mibBuilder.importSymbols(
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
    "iso",
    "mib-2")

(DisplayString,
 RowStatus,
 StorageType,
 TextualConvention,
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "StorageType",
    "TextualConvention",
    "TimeStamp",
    "TruthValue")


# MODULE-IDENTITY

teMIB = ModuleIdentity(
    (1, 3, 6, 1, 2, 1, 122)
)
teMIB.setRevisions(
        ("2005-01-04 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_TeMIBNotifications_ObjectIdentity = ObjectIdentity
teMIBNotifications = _TeMIBNotifications_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 122, 0)
)
_TeMIBObjects_ObjectIdentity = ObjectIdentity
teMIBObjects = _TeMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 122, 1)
)
_TeInfo_ObjectIdentity = ObjectIdentity
teInfo = _TeInfo_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 122, 1, 1)
)


class _TeDistProtocol_Type(Bits):
    """Custom type teDistProtocol based on Bits"""
    namedValues = NamedValues(
        *(("isis", 1),
          ("ospf", 2),
          ("other", 0))
    )

_TeDistProtocol_Type.__name__ = "Bits"
_TeDistProtocol_Object = MibScalar
teDistProtocol = _TeDistProtocol_Object(
    (1, 3, 6, 1, 2, 1, 122, 1, 1, 1),
    _TeDistProtocol_Type()
)
teDistProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teDistProtocol.setStatus("current")


class _TeSignalingProto_Type(Bits):
    """Custom type teSignalingProto based on Bits"""
    namedValues = NamedValues(
        *(("crldp", 2),
          ("other", 0),
          ("rsvpte", 1),
          ("static", 3))
    )

_TeSignalingProto_Type.__name__ = "Bits"
_TeSignalingProto_Object = MibScalar
teSignalingProto = _TeSignalingProto_Object(
    (1, 3, 6, 1, 2, 1, 122, 1, 1, 2),
    _TeSignalingProto_Type()
)
teSignalingProto.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teSignalingProto.setStatus("current")


class _TeNotificationEnable_Type(TruthValue):
    """Custom type teNotificationEnable based on TruthValue"""


_TeNotificationEnable_Object = MibScalar
teNotificationEnable = _TeNotificationEnable_Object(
    (1, 3, 6, 1, 2, 1, 122, 1, 1, 3),
    _TeNotificationEnable_Type()
)
teNotificationEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    teNotificationEnable.setStatus("current")
_TeNextTunnelIndex_Type = Unsigned32
_TeNextTunnelIndex_Object = MibScalar
teNextTunnelIndex = _TeNextTunnelIndex_Object(
    (1, 3, 6, 1, 2, 1, 122, 1, 1, 4),
    _TeNextTunnelIndex_Type()
)
teNextTunnelIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teNextTunnelIndex.setStatus("current")
_TeNextPathHopIndex_Type = Unsigned32
_TeNextPathHopIndex_Object = MibScalar
teNextPathHopIndex = _TeNextPathHopIndex_Object(
    (1, 3, 6, 1, 2, 1, 122, 1, 1, 5),
    _TeNextPathHopIndex_Type()
)
teNextPathHopIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teNextPathHopIndex.setStatus("current")
_TeConfiguredTunnels_Type = Gauge32
_TeConfiguredTunnels_Object = MibScalar
teConfiguredTunnels = _TeConfiguredTunnels_Object(
    (1, 3, 6, 1, 2, 1, 122, 1, 1, 6),
    _TeConfiguredTunnels_Type()
)
teConfiguredTunnels.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teConfiguredTunnels.setStatus("current")
_TeActiveTunnels_Type = Gauge32
_TeActiveTunnels_Object = MibScalar
teActiveTunnels = _TeActiveTunnels_Object(
    (1, 3, 6, 1, 2, 1, 122, 1, 1, 7),
    _TeActiveTunnels_Type()
)
teActiveTunnels.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teActiveTunnels.setStatus("current")
_TePrimaryTunnels_Type = Gauge32
_TePrimaryTunnels_Object = MibScalar
tePrimaryTunnels = _TePrimaryTunnels_Object(
    (1, 3, 6, 1, 2, 1, 122, 1, 1, 8),
    _TePrimaryTunnels_Type()
)
tePrimaryTunnels.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tePrimaryTunnels.setStatus("current")
_TeAdminGroupTable_Object = MibTable
teAdminGroupTable = _TeAdminGroupTable_Object(
    (1, 3, 6, 1, 2, 1, 122, 1, 1, 9)
)
if mibBuilder.loadTexts:
    teAdminGroupTable.setStatus("current")
_TeAdminGroupEntry_Object = MibTableRow
teAdminGroupEntry = _TeAdminGroupEntry_Object(
    (1, 3, 6, 1, 2, 1, 122, 1, 1, 9, 1)
)
teAdminGroupEntry.setIndexNames(
    (0, "TE-MIB", "teAdminGroupNumber"),
)
if mibBuilder.loadTexts:
    teAdminGroupEntry.setStatus("current")


class _TeAdminGroupNumber_Type(Integer32):
    """Custom type teAdminGroupNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_TeAdminGroupNumber_Type.__name__ = "Integer32"
_TeAdminGroupNumber_Object = MibTableColumn
teAdminGroupNumber = _TeAdminGroupNumber_Object(
    (1, 3, 6, 1, 2, 1, 122, 1, 1, 9, 1, 1),
    _TeAdminGroupNumber_Type()
)
teAdminGroupNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    teAdminGroupNumber.setStatus("current")


class _TeAdminGroupName_Type(SnmpAdminString):
    """Custom type teAdminGroupName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_TeAdminGroupName_Type.__name__ = "SnmpAdminString"
_TeAdminGroupName_Object = MibTableColumn
teAdminGroupName = _TeAdminGroupName_Object(
    (1, 3, 6, 1, 2, 1, 122, 1, 1, 9, 1, 2),
    _TeAdminGroupName_Type()
)
teAdminGroupName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    teAdminGroupName.setStatus("current")
_TeAdminGroupRowStatus_Type = RowStatus
_TeAdminGroupRowStatus_Object = MibTableColumn
teAdminGroupRowStatus = _TeAdminGroupRowStatus_Object(
    (1, 3, 6, 1, 2, 1, 122, 1, 1, 9, 1, 3),
    _TeAdminGroupRowStatus_Type()
)
teAdminGroupRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    teAdminGroupRowStatus.setStatus("current")
_TeTunnelTable_Object = MibTable
teTunnelTable = _TeTunnelTable_Object(
    (1, 3, 6, 1, 2, 1, 122, 1, 2)
)
if mibBuilder.loadTexts:
    teTunnelTable.setStatus("current")
_TeTunnelEntry_Object = MibTableRow
teTunnelEntry = _TeTunnelEntry_Object(
    (1, 3, 6, 1, 2, 1, 122, 1, 2, 1)
)
teTunnelEntry.setIndexNames(
    (0, "TE-MIB", "teTunnelIndex"),
)
if mibBuilder.loadTexts:
    teTunnelEntry.setStatus("current")


class _TeTunnelIndex_Type(Unsigned32):
    """Custom type teTunnelIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_TeTunnelIndex_Type.__name__ = "Unsigned32"
_TeTunnelIndex_Object = MibTableColumn
teTunnelIndex = _TeTunnelIndex_Object(
    (1, 3, 6, 1, 2, 1, 122, 1, 2, 1, 1),
    _TeTunnelIndex_Type()
)
teTunnelIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    teTunnelIndex.setStatus("current")


class _TeTunnelName_Type(SnmpAdminString):
    """Custom type teTunnelName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_TeTunnelName_Type.__name__ = "SnmpAdminString"
_TeTunnelName_Object = MibTableColumn
teTunnelName = _TeTunnelName_Object(
    (1, 3, 6, 1, 2, 1, 122, 1, 2, 1, 2),
    _TeTunnelName_Type()
)
teTunnelName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    teTunnelName.setStatus("current")
_TeTunnelNextPathIndex_Type = Unsigned32
_TeTunnelNextPathIndex_Object = MibTableColumn
teTunnelNextPathIndex = _TeTunnelNextPathIndex_Object(
    (1, 3, 6, 1, 2, 1, 122, 1, 2, 1, 3),
    _TeTunnelNextPathIndex_Type()
)
teTunnelNextPathIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teTunnelNextPathIndex.setStatus("current")
_TeTunnelRowStatus_Type = RowStatus
_TeTunnelRowStatus_Object = MibTableColumn
teTunnelRowStatus = _TeTunnelRowStatus_Object(
    (1, 3, 6, 1, 2, 1, 122, 1, 2, 1, 4),
    _TeTunnelRowStatus_Type()
)
teTunnelRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    teTunnelRowStatus.setStatus("current")
_TeTunnelStorageType_Type = StorageType
_TeTunnelStorageType_Object = MibTableColumn
teTunnelStorageType = _TeTunnelStorageType_Object(
    (1, 3, 6, 1, 2, 1, 122, 1, 2, 1, 5),
    _TeTunnelStorageType_Type()
)
teTunnelStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    teTunnelStorageType.setStatus("current")
_TeTunnelSourceAddressType_Type = TeHopAddressType
_TeTunnelSourceAddressType_Object = MibTableColumn
teTunnelSourceAddressType = _TeTunnelSourceAddressType_Object(
    (1, 3, 6, 1, 2, 1, 122, 1, 2, 1, 6),
    _TeTunnelSourceAddressType_Type()
)
teTunnelSourceAddressType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    teTunnelSourceAddressType.setStatus("current")
_TeTunnelSourceAddress_Type = TeHopAddress
_TeTunnelSourceAddress_Object = MibTableColumn
teTunnelSourceAddress = _TeTunnelSourceAddress_Object(
    (1, 3, 6, 1, 2, 1, 122, 1, 2, 1, 7),
    _TeTunnelSourceAddress_Type()
)
teTunnelSourceAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    teTunnelSourceAddress.setStatus("current")
_TeTunnelDestinationAddressType_Type = TeHopAddressType
_TeTunnelDestinationAddressType_Object = MibTableColumn
teTunnelDestinationAddressType = _TeTunnelDestinationAddressType_Object(
    (1, 3, 6, 1, 2, 1, 122, 1, 2, 1, 8),
    _TeTunnelDestinationAddressType_Type()
)
teTunnelDestinationAddressType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    teTunnelDestinationAddressType.setStatus("current")
_TeTunnelDestinationAddress_Type = TeHopAddress
_TeTunnelDestinationAddress_Object = MibTableColumn
teTunnelDestinationAddress = _TeTunnelDestinationAddress_Object(
    (1, 3, 6, 1, 2, 1, 122, 1, 2, 1, 9),
    _TeTunnelDestinationAddress_Type()
)
teTunnelDestinationAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    teTunnelDestinationAddress.setStatus("current")


class _TeTunnelState_Type(Integer32):
    """Custom type teTunnelState based on Integer32"""
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
        *(("down", 3),
          ("testing", 4),
          ("unknown", 1),
          ("up", 2))
    )


_TeTunnelState_Type.__name__ = "Integer32"
_TeTunnelState_Object = MibTableColumn
teTunnelState = _TeTunnelState_Object(
    (1, 3, 6, 1, 2, 1, 122, 1, 2, 1, 10),
    _TeTunnelState_Type()
)
teTunnelState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teTunnelState.setStatus("current")
_TeTunnelDiscontinuityTimer_Type = TimeStamp
_TeTunnelDiscontinuityTimer_Object = MibTableColumn
teTunnelDiscontinuityTimer = _TeTunnelDiscontinuityTimer_Object(
    (1, 3, 6, 1, 2, 1, 122, 1, 2, 1, 11),
    _TeTunnelDiscontinuityTimer_Type()
)
teTunnelDiscontinuityTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teTunnelDiscontinuityTimer.setStatus("current")
_TeTunnelOctets_Type = Counter64
_TeTunnelOctets_Object = MibTableColumn
teTunnelOctets = _TeTunnelOctets_Object(
    (1, 3, 6, 1, 2, 1, 122, 1, 2, 1, 12),
    _TeTunnelOctets_Type()
)
teTunnelOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teTunnelOctets.setStatus("current")
_TeTunnelPackets_Type = Counter64
_TeTunnelPackets_Object = MibTableColumn
teTunnelPackets = _TeTunnelPackets_Object(
    (1, 3, 6, 1, 2, 1, 122, 1, 2, 1, 13),
    _TeTunnelPackets_Type()
)
teTunnelPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teTunnelPackets.setStatus("current")
_TeTunnelLPOctets_Type = Counter32
_TeTunnelLPOctets_Object = MibTableColumn
teTunnelLPOctets = _TeTunnelLPOctets_Object(
    (1, 3, 6, 1, 2, 1, 122, 1, 2, 1, 14),
    _TeTunnelLPOctets_Type()
)
teTunnelLPOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teTunnelLPOctets.setStatus("current")
_TeTunnelLPPackets_Type = Counter32
_TeTunnelLPPackets_Object = MibTableColumn
teTunnelLPPackets = _TeTunnelLPPackets_Object(
    (1, 3, 6, 1, 2, 1, 122, 1, 2, 1, 15),
    _TeTunnelLPPackets_Type()
)
teTunnelLPPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teTunnelLPPackets.setStatus("current")
_TeTunnelAge_Type = TimeTicks
_TeTunnelAge_Object = MibTableColumn
teTunnelAge = _TeTunnelAge_Object(
    (1, 3, 6, 1, 2, 1, 122, 1, 2, 1, 16),
    _TeTunnelAge_Type()
)
teTunnelAge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teTunnelAge.setStatus("current")
_TeTunnelTimeUp_Type = TimeTicks
_TeTunnelTimeUp_Object = MibTableColumn
teTunnelTimeUp = _TeTunnelTimeUp_Object(
    (1, 3, 6, 1, 2, 1, 122, 1, 2, 1, 17),
    _TeTunnelTimeUp_Type()
)
teTunnelTimeUp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teTunnelTimeUp.setStatus("current")
_TeTunnelPrimaryTimeUp_Type = TimeTicks
_TeTunnelPrimaryTimeUp_Object = MibTableColumn
teTunnelPrimaryTimeUp = _TeTunnelPrimaryTimeUp_Object(
    (1, 3, 6, 1, 2, 1, 122, 1, 2, 1, 18),
    _TeTunnelPrimaryTimeUp_Type()
)
teTunnelPrimaryTimeUp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teTunnelPrimaryTimeUp.setStatus("current")
_TeTunnelTransitions_Type = Counter32
_TeTunnelTransitions_Object = MibTableColumn
teTunnelTransitions = _TeTunnelTransitions_Object(
    (1, 3, 6, 1, 2, 1, 122, 1, 2, 1, 19),
    _TeTunnelTransitions_Type()
)
teTunnelTransitions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teTunnelTransitions.setStatus("current")
_TeTunnelLastTransition_Type = TimeTicks
_TeTunnelLastTransition_Object = MibTableColumn
teTunnelLastTransition = _TeTunnelLastTransition_Object(
    (1, 3, 6, 1, 2, 1, 122, 1, 2, 1, 20),
    _TeTunnelLastTransition_Type()
)
teTunnelLastTransition.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teTunnelLastTransition.setStatus("current")
_TeTunnelPathChanges_Type = Counter32
_TeTunnelPathChanges_Object = MibTableColumn
teTunnelPathChanges = _TeTunnelPathChanges_Object(
    (1, 3, 6, 1, 2, 1, 122, 1, 2, 1, 21),
    _TeTunnelPathChanges_Type()
)
teTunnelPathChanges.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teTunnelPathChanges.setStatus("current")
_TeTunnelLastPathChange_Type = TimeTicks
_TeTunnelLastPathChange_Object = MibTableColumn
teTunnelLastPathChange = _TeTunnelLastPathChange_Object(
    (1, 3, 6, 1, 2, 1, 122, 1, 2, 1, 22),
    _TeTunnelLastPathChange_Type()
)
teTunnelLastPathChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teTunnelLastPathChange.setStatus("current")
_TeTunnelConfiguredPaths_Type = Gauge32
_TeTunnelConfiguredPaths_Object = MibTableColumn
teTunnelConfiguredPaths = _TeTunnelConfiguredPaths_Object(
    (1, 3, 6, 1, 2, 1, 122, 1, 2, 1, 23),
    _TeTunnelConfiguredPaths_Type()
)
teTunnelConfiguredPaths.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teTunnelConfiguredPaths.setStatus("current")
_TeTunnelStandbyPaths_Type = Gauge32
_TeTunnelStandbyPaths_Object = MibTableColumn
teTunnelStandbyPaths = _TeTunnelStandbyPaths_Object(
    (1, 3, 6, 1, 2, 1, 122, 1, 2, 1, 24),
    _TeTunnelStandbyPaths_Type()
)
teTunnelStandbyPaths.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teTunnelStandbyPaths.setStatus("current")
_TeTunnelOperationalPaths_Type = Gauge32
_TeTunnelOperationalPaths_Object = MibTableColumn
teTunnelOperationalPaths = _TeTunnelOperationalPaths_Object(
    (1, 3, 6, 1, 2, 1, 122, 1, 2, 1, 25),
    _TeTunnelOperationalPaths_Type()
)
teTunnelOperationalPaths.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teTunnelOperationalPaths.setStatus("current")
_TePathTable_Object = MibTable
tePathTable = _TePathTable_Object(
    (1, 3, 6, 1, 2, 1, 122, 1, 3)
)
if mibBuilder.loadTexts:
    tePathTable.setStatus("current")
_TePathEntry_Object = MibTableRow
tePathEntry = _TePathEntry_Object(
    (1, 3, 6, 1, 2, 1, 122, 1, 3, 1)
)
tePathEntry.setIndexNames(
    (0, "TE-MIB", "teTunnelIndex"),
    (0, "TE-MIB", "tePathIndex"),
)
if mibBuilder.loadTexts:
    tePathEntry.setStatus("current")


class _TePathIndex_Type(Unsigned32):
    """Custom type tePathIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_TePathIndex_Type.__name__ = "Unsigned32"
_TePathIndex_Object = MibTableColumn
tePathIndex = _TePathIndex_Object(
    (1, 3, 6, 1, 2, 1, 122, 1, 3, 1, 1),
    _TePathIndex_Type()
)
tePathIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tePathIndex.setStatus("current")


class _TePathName_Type(SnmpAdminString):
    """Custom type tePathName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_TePathName_Type.__name__ = "SnmpAdminString"
_TePathName_Object = MibTableColumn
tePathName = _TePathName_Object(
    (1, 3, 6, 1, 2, 1, 122, 1, 3, 1, 2),
    _TePathName_Type()
)
tePathName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tePathName.setStatus("current")
_TePathRowStatus_Type = RowStatus
_TePathRowStatus_Object = MibTableColumn
tePathRowStatus = _TePathRowStatus_Object(
    (1, 3, 6, 1, 2, 1, 122, 1, 3, 1, 3),
    _TePathRowStatus_Type()
)
tePathRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tePathRowStatus.setStatus("current")
_TePathStorageType_Type = StorageType
_TePathStorageType_Object = MibTableColumn
tePathStorageType = _TePathStorageType_Object(
    (1, 3, 6, 1, 2, 1, 122, 1, 3, 1, 4),
    _TePathStorageType_Type()
)
tePathStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tePathStorageType.setStatus("current")


class _TePathType_Type(Integer32):
    """Custom type tePathType based on Integer32"""
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
        *(("other", 1),
          ("primary", 2),
          ("secondary", 4),
          ("standby", 3))
    )


_TePathType_Type.__name__ = "Integer32"
_TePathType_Object = MibTableColumn
tePathType = _TePathType_Object(
    (1, 3, 6, 1, 2, 1, 122, 1, 3, 1, 5),
    _TePathType_Type()
)
tePathType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tePathType.setStatus("current")
_TePathConfiguredRoute_Type = Unsigned32
_TePathConfiguredRoute_Object = MibTableColumn
tePathConfiguredRoute = _TePathConfiguredRoute_Object(
    (1, 3, 6, 1, 2, 1, 122, 1, 3, 1, 6),
    _TePathConfiguredRoute_Type()
)
tePathConfiguredRoute.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tePathConfiguredRoute.setStatus("current")


class _TePathBandwidth_Type(MplsBitRate):
    """Custom type tePathBandwidth based on MplsBitRate"""
    defaultValue = 0


_TePathBandwidth_Object = MibTableColumn
tePathBandwidth = _TePathBandwidth_Object(
    (1, 3, 6, 1, 2, 1, 122, 1, 3, 1, 7),
    _TePathBandwidth_Type()
)
tePathBandwidth.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tePathBandwidth.setStatus("current")
if mibBuilder.loadTexts:
    tePathBandwidth.setUnits("Kilobits per second")


class _TePathIncludeAny_Type(Unsigned32):
    """Custom type tePathIncludeAny based on Unsigned32"""
    defaultValue = 0


_TePathIncludeAny_Object = MibTableColumn
tePathIncludeAny = _TePathIncludeAny_Object(
    (1, 3, 6, 1, 2, 1, 122, 1, 3, 1, 8),
    _TePathIncludeAny_Type()
)
tePathIncludeAny.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tePathIncludeAny.setStatus("current")


class _TePathIncludeAll_Type(Unsigned32):
    """Custom type tePathIncludeAll based on Unsigned32"""
    defaultValue = 0


_TePathIncludeAll_Object = MibTableColumn
tePathIncludeAll = _TePathIncludeAll_Object(
    (1, 3, 6, 1, 2, 1, 122, 1, 3, 1, 9),
    _TePathIncludeAll_Type()
)
tePathIncludeAll.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tePathIncludeAll.setStatus("current")


class _TePathExclude_Type(Unsigned32):
    """Custom type tePathExclude based on Unsigned32"""
    defaultValue = 0


_TePathExclude_Object = MibTableColumn
tePathExclude = _TePathExclude_Object(
    (1, 3, 6, 1, 2, 1, 122, 1, 3, 1, 10),
    _TePathExclude_Type()
)
tePathExclude.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tePathExclude.setStatus("current")


class _TePathSetupPriority_Type(Integer32):
    """Custom type tePathSetupPriority based on Integer32"""
    defaultValue = 7

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_TePathSetupPriority_Type.__name__ = "Integer32"
_TePathSetupPriority_Object = MibTableColumn
tePathSetupPriority = _TePathSetupPriority_Object(
    (1, 3, 6, 1, 2, 1, 122, 1, 3, 1, 11),
    _TePathSetupPriority_Type()
)
tePathSetupPriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tePathSetupPriority.setStatus("current")


class _TePathHoldPriority_Type(Integer32):
    """Custom type tePathHoldPriority based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_TePathHoldPriority_Type.__name__ = "Integer32"
_TePathHoldPriority_Object = MibTableColumn
tePathHoldPriority = _TePathHoldPriority_Object(
    (1, 3, 6, 1, 2, 1, 122, 1, 3, 1, 12),
    _TePathHoldPriority_Type()
)
tePathHoldPriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tePathHoldPriority.setStatus("current")


class _TePathProperties_Type(Bits):
    """Custom type tePathProperties based on Bits"""
    namedValues = NamedValues(
        *(("cspf", 1),
          ("fastReroute", 4),
          ("makeBeforeBreak", 2),
          ("mergeable", 3),
          ("protected", 5),
          ("recordRoute", 0))
    )

_TePathProperties_Type.__name__ = "Bits"
_TePathProperties_Object = MibTableColumn
tePathProperties = _TePathProperties_Object(
    (1, 3, 6, 1, 2, 1, 122, 1, 3, 1, 13),
    _TePathProperties_Type()
)
tePathProperties.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tePathProperties.setStatus("current")


class _TePathOperStatus_Type(Integer32):
    """Custom type tePathOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("dormant", 3),
          ("down", 1),
          ("operational", 5),
          ("ready", 4),
          ("testing", 2),
          ("unknown", 0))
    )


_TePathOperStatus_Type.__name__ = "Integer32"
_TePathOperStatus_Object = MibTableColumn
tePathOperStatus = _TePathOperStatus_Object(
    (1, 3, 6, 1, 2, 1, 122, 1, 3, 1, 14),
    _TePathOperStatus_Type()
)
tePathOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tePathOperStatus.setStatus("current")


class _TePathAdminStatus_Type(Integer32):
    """Custom type tePathAdminStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("normal", 1),
          ("testing", 2))
    )


_TePathAdminStatus_Type.__name__ = "Integer32"
_TePathAdminStatus_Object = MibTableColumn
tePathAdminStatus = _TePathAdminStatus_Object(
    (1, 3, 6, 1, 2, 1, 122, 1, 3, 1, 15),
    _TePathAdminStatus_Type()
)
tePathAdminStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tePathAdminStatus.setStatus("current")
_TePathComputedRoute_Type = Unsigned32
_TePathComputedRoute_Object = MibTableColumn
tePathComputedRoute = _TePathComputedRoute_Object(
    (1, 3, 6, 1, 2, 1, 122, 1, 3, 1, 16),
    _TePathComputedRoute_Type()
)
tePathComputedRoute.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tePathComputedRoute.setStatus("current")
_TePathRecordedRoute_Type = Unsigned32
_TePathRecordedRoute_Object = MibTableColumn
tePathRecordedRoute = _TePathRecordedRoute_Object(
    (1, 3, 6, 1, 2, 1, 122, 1, 3, 1, 17),
    _TePathRecordedRoute_Type()
)
tePathRecordedRoute.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tePathRecordedRoute.setStatus("current")
_TePathHopTable_Object = MibTable
tePathHopTable = _TePathHopTable_Object(
    (1, 3, 6, 1, 2, 1, 122, 1, 4)
)
if mibBuilder.loadTexts:
    tePathHopTable.setStatus("current")
_TePathHopEntry_Object = MibTableRow
tePathHopEntry = _TePathHopEntry_Object(
    (1, 3, 6, 1, 2, 1, 122, 1, 4, 1)
)
tePathHopEntry.setIndexNames(
    (0, "TE-MIB", "teHopListIndex"),
    (0, "TE-MIB", "tePathHopIndex"),
)
if mibBuilder.loadTexts:
    tePathHopEntry.setStatus("current")


class _TeHopListIndex_Type(Unsigned32):
    """Custom type teHopListIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_TeHopListIndex_Type.__name__ = "Unsigned32"
_TeHopListIndex_Object = MibTableColumn
teHopListIndex = _TeHopListIndex_Object(
    (1, 3, 6, 1, 2, 1, 122, 1, 4, 1, 1),
    _TeHopListIndex_Type()
)
teHopListIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    teHopListIndex.setStatus("current")


class _TePathHopIndex_Type(Unsigned32):
    """Custom type tePathHopIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_TePathHopIndex_Type.__name__ = "Unsigned32"
_TePathHopIndex_Object = MibTableColumn
tePathHopIndex = _TePathHopIndex_Object(
    (1, 3, 6, 1, 2, 1, 122, 1, 4, 1, 2),
    _TePathHopIndex_Type()
)
tePathHopIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tePathHopIndex.setStatus("current")
_TePathHopRowStatus_Type = RowStatus
_TePathHopRowStatus_Object = MibTableColumn
tePathHopRowStatus = _TePathHopRowStatus_Object(
    (1, 3, 6, 1, 2, 1, 122, 1, 4, 1, 3),
    _TePathHopRowStatus_Type()
)
tePathHopRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tePathHopRowStatus.setStatus("current")
_TePathHopStorageType_Type = StorageType
_TePathHopStorageType_Object = MibTableColumn
tePathHopStorageType = _TePathHopStorageType_Object(
    (1, 3, 6, 1, 2, 1, 122, 1, 4, 1, 4),
    _TePathHopStorageType_Type()
)
tePathHopStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tePathHopStorageType.setStatus("current")
_TePathHopAddrType_Type = TeHopAddressType
_TePathHopAddrType_Object = MibTableColumn
tePathHopAddrType = _TePathHopAddrType_Object(
    (1, 3, 6, 1, 2, 1, 122, 1, 4, 1, 5),
    _TePathHopAddrType_Type()
)
tePathHopAddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tePathHopAddrType.setStatus("current")
_TePathHopAddress_Type = TeHopAddress
_TePathHopAddress_Object = MibTableColumn
tePathHopAddress = _TePathHopAddress_Object(
    (1, 3, 6, 1, 2, 1, 122, 1, 4, 1, 6),
    _TePathHopAddress_Type()
)
tePathHopAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tePathHopAddress.setStatus("current")


class _TePathHopType_Type(Integer32):
    """Custom type tePathHopType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("loose", 1),
          ("strict", 2),
          ("unknown", 0))
    )


_TePathHopType_Type.__name__ = "Integer32"
_TePathHopType_Object = MibTableColumn
tePathHopType = _TePathHopType_Object(
    (1, 3, 6, 1, 2, 1, 122, 1, 4, 1, 7),
    _TePathHopType_Type()
)
tePathHopType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tePathHopType.setStatus("current")
_TeMIBConformance_ObjectIdentity = ObjectIdentity
teMIBConformance = _TeMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 122, 2)
)
_TeGroups_ObjectIdentity = ObjectIdentity
teGroups = _TeGroups_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 122, 2, 1)
)
_TeModuleCompliance_ObjectIdentity = ObjectIdentity
teModuleCompliance = _TeModuleCompliance_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 122, 2, 2)
)

# Managed Objects groups

teTrafficEngineeringGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 122, 2, 1, 1)
)
teTrafficEngineeringGroup.setObjects(
      *(("TE-MIB", "teTunnelName"),
        ("TE-MIB", "teTunnelNextPathIndex"),
        ("TE-MIB", "teTunnelRowStatus"),
        ("TE-MIB", "teTunnelStorageType"),
        ("TE-MIB", "teTunnelSourceAddressType"),
        ("TE-MIB", "teTunnelSourceAddress"),
        ("TE-MIB", "teTunnelDestinationAddressType"),
        ("TE-MIB", "teTunnelDestinationAddress"),
        ("TE-MIB", "teTunnelState"),
        ("TE-MIB", "teTunnelDiscontinuityTimer"),
        ("TE-MIB", "teTunnelOctets"),
        ("TE-MIB", "teTunnelPackets"),
        ("TE-MIB", "teTunnelLPOctets"),
        ("TE-MIB", "teTunnelLPPackets"),
        ("TE-MIB", "teTunnelAge"),
        ("TE-MIB", "teTunnelTimeUp"),
        ("TE-MIB", "teTunnelPrimaryTimeUp"),
        ("TE-MIB", "teTunnelTransitions"),
        ("TE-MIB", "teTunnelLastTransition"),
        ("TE-MIB", "teTunnelPathChanges"),
        ("TE-MIB", "teTunnelLastPathChange"),
        ("TE-MIB", "teTunnelConfiguredPaths"),
        ("TE-MIB", "teTunnelStandbyPaths"),
        ("TE-MIB", "teTunnelOperationalPaths"),
        ("TE-MIB", "tePathBandwidth"),
        ("TE-MIB", "tePathIncludeAny"),
        ("TE-MIB", "tePathIncludeAll"),
        ("TE-MIB", "tePathExclude"),
        ("TE-MIB", "tePathSetupPriority"),
        ("TE-MIB", "tePathHoldPriority"),
        ("TE-MIB", "tePathProperties"),
        ("TE-MIB", "tePathOperStatus"),
        ("TE-MIB", "tePathAdminStatus"),
        ("TE-MIB", "tePathComputedRoute"),
        ("TE-MIB", "tePathRecordedRoute"),
        ("TE-MIB", "teDistProtocol"),
        ("TE-MIB", "teSignalingProto"),
        ("TE-MIB", "teNotificationEnable"),
        ("TE-MIB", "teNextTunnelIndex"),
        ("TE-MIB", "teNextPathHopIndex"),
        ("TE-MIB", "teAdminGroupName"),
        ("TE-MIB", "teAdminGroupRowStatus"),
        ("TE-MIB", "teConfiguredTunnels"),
        ("TE-MIB", "teActiveTunnels"),
        ("TE-MIB", "tePrimaryTunnels"),
        ("TE-MIB", "tePathName"),
        ("TE-MIB", "tePathType"),
        ("TE-MIB", "tePathRowStatus"),
        ("TE-MIB", "tePathStorageType"),
        ("TE-MIB", "tePathConfiguredRoute"),
        ("TE-MIB", "tePathHopRowStatus"),
        ("TE-MIB", "tePathHopStorageType"),
        ("TE-MIB", "tePathHopAddrType"),
        ("TE-MIB", "tePathHopAddress"),
        ("TE-MIB", "tePathHopType"))
)
if mibBuilder.loadTexts:
    teTrafficEngineeringGroup.setStatus("current")


# Notification objects

teTunnelUp = NotificationType(
    (1, 3, 6, 1, 2, 1, 122, 0, 1)
)
teTunnelUp.setObjects(
      *(("TE-MIB", "teTunnelName"),
        ("TE-MIB", "tePathName"))
)
if mibBuilder.loadTexts:
    teTunnelUp.setStatus(
        "current"
    )

teTunnelDown = NotificationType(
    (1, 3, 6, 1, 2, 1, 122, 0, 2)
)
teTunnelDown.setObjects(
      *(("TE-MIB", "teTunnelName"),
        ("TE-MIB", "tePathName"))
)
if mibBuilder.loadTexts:
    teTunnelDown.setStatus(
        "current"
    )

teTunnelChanged = NotificationType(
    (1, 3, 6, 1, 2, 1, 122, 0, 3)
)
teTunnelChanged.setObjects(
      *(("TE-MIB", "teTunnelName"),
        ("TE-MIB", "tePathName"))
)
if mibBuilder.loadTexts:
    teTunnelChanged.setStatus(
        "current"
    )

teTunnelRerouted = NotificationType(
    (1, 3, 6, 1, 2, 1, 122, 0, 4)
)
teTunnelRerouted.setObjects(
      *(("TE-MIB", "teTunnelName"),
        ("TE-MIB", "tePathName"))
)
if mibBuilder.loadTexts:
    teTunnelRerouted.setStatus(
        "current"
    )


# Notifications groups

teNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 2, 1, 122, 2, 1, 2)
)
teNotificationGroup.setObjects(
      *(("TE-MIB", "teTunnelUp"),
        ("TE-MIB", "teTunnelDown"),
        ("TE-MIB", "teTunnelChanged"),
        ("TE-MIB", "teTunnelRerouted"))
)
if mibBuilder.loadTexts:
    teNotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

teModuleReadOnlyCompliance = ModuleCompliance(
    (1, 3, 6, 1, 2, 1, 122, 2, 2, 1)
)
if mibBuilder.loadTexts:
    teModuleReadOnlyCompliance.setStatus(
        "current"
    )

teModuleFullCompliance = ModuleCompliance(
    (1, 3, 6, 1, 2, 1, 122, 2, 2, 2)
)
if mibBuilder.loadTexts:
    teModuleFullCompliance.setStatus(
        "current"
    )

teModuleServerReadOnlyCompliance = ModuleCompliance(
    (1, 3, 6, 1, 2, 1, 122, 2, 2, 3)
)
if mibBuilder.loadTexts:
    teModuleServerReadOnlyCompliance.setStatus(
        "current"
    )

teModuleServerFullCompliance = ModuleCompliance(
    (1, 3, 6, 1, 2, 1, 122, 2, 2, 4)
)
if mibBuilder.loadTexts:
    teModuleServerFullCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TE-MIB",
    **{"teMIB": teMIB,
       "teMIBNotifications": teMIBNotifications,
       "teTunnelUp": teTunnelUp,
       "teTunnelDown": teTunnelDown,
       "teTunnelChanged": teTunnelChanged,
       "teTunnelRerouted": teTunnelRerouted,
       "teMIBObjects": teMIBObjects,
       "teInfo": teInfo,
       "teDistProtocol": teDistProtocol,
       "teSignalingProto": teSignalingProto,
       "teNotificationEnable": teNotificationEnable,
       "teNextTunnelIndex": teNextTunnelIndex,
       "teNextPathHopIndex": teNextPathHopIndex,
       "teConfiguredTunnels": teConfiguredTunnels,
       "teActiveTunnels": teActiveTunnels,
       "tePrimaryTunnels": tePrimaryTunnels,
       "teAdminGroupTable": teAdminGroupTable,
       "teAdminGroupEntry": teAdminGroupEntry,
       "teAdminGroupNumber": teAdminGroupNumber,
       "teAdminGroupName": teAdminGroupName,
       "teAdminGroupRowStatus": teAdminGroupRowStatus,
       "teTunnelTable": teTunnelTable,
       "teTunnelEntry": teTunnelEntry,
       "teTunnelIndex": teTunnelIndex,
       "teTunnelName": teTunnelName,
       "teTunnelNextPathIndex": teTunnelNextPathIndex,
       "teTunnelRowStatus": teTunnelRowStatus,
       "teTunnelStorageType": teTunnelStorageType,
       "teTunnelSourceAddressType": teTunnelSourceAddressType,
       "teTunnelSourceAddress": teTunnelSourceAddress,
       "teTunnelDestinationAddressType": teTunnelDestinationAddressType,
       "teTunnelDestinationAddress": teTunnelDestinationAddress,
       "teTunnelState": teTunnelState,
       "teTunnelDiscontinuityTimer": teTunnelDiscontinuityTimer,
       "teTunnelOctets": teTunnelOctets,
       "teTunnelPackets": teTunnelPackets,
       "teTunnelLPOctets": teTunnelLPOctets,
       "teTunnelLPPackets": teTunnelLPPackets,
       "teTunnelAge": teTunnelAge,
       "teTunnelTimeUp": teTunnelTimeUp,
       "teTunnelPrimaryTimeUp": teTunnelPrimaryTimeUp,
       "teTunnelTransitions": teTunnelTransitions,
       "teTunnelLastTransition": teTunnelLastTransition,
       "teTunnelPathChanges": teTunnelPathChanges,
       "teTunnelLastPathChange": teTunnelLastPathChange,
       "teTunnelConfiguredPaths": teTunnelConfiguredPaths,
       "teTunnelStandbyPaths": teTunnelStandbyPaths,
       "teTunnelOperationalPaths": teTunnelOperationalPaths,
       "tePathTable": tePathTable,
       "tePathEntry": tePathEntry,
       "tePathIndex": tePathIndex,
       "tePathName": tePathName,
       "tePathRowStatus": tePathRowStatus,
       "tePathStorageType": tePathStorageType,
       "tePathType": tePathType,
       "tePathConfiguredRoute": tePathConfiguredRoute,
       "tePathBandwidth": tePathBandwidth,
       "tePathIncludeAny": tePathIncludeAny,
       "tePathIncludeAll": tePathIncludeAll,
       "tePathExclude": tePathExclude,
       "tePathSetupPriority": tePathSetupPriority,
       "tePathHoldPriority": tePathHoldPriority,
       "tePathProperties": tePathProperties,
       "tePathOperStatus": tePathOperStatus,
       "tePathAdminStatus": tePathAdminStatus,
       "tePathComputedRoute": tePathComputedRoute,
       "tePathRecordedRoute": tePathRecordedRoute,
       "tePathHopTable": tePathHopTable,
       "tePathHopEntry": tePathHopEntry,
       "teHopListIndex": teHopListIndex,
       "tePathHopIndex": tePathHopIndex,
       "tePathHopRowStatus": tePathHopRowStatus,
       "tePathHopStorageType": tePathHopStorageType,
       "tePathHopAddrType": tePathHopAddrType,
       "tePathHopAddress": tePathHopAddress,
       "tePathHopType": tePathHopType,
       "teMIBConformance": teMIBConformance,
       "teGroups": teGroups,
       "teTrafficEngineeringGroup": teTrafficEngineeringGroup,
       "teNotificationGroup": teNotificationGroup,
       "teModuleCompliance": teModuleCompliance,
       "teModuleReadOnlyCompliance": teModuleReadOnlyCompliance,
       "teModuleFullCompliance": teModuleFullCompliance,
       "teModuleServerReadOnlyCompliance": teModuleServerReadOnlyCompliance,
       "teModuleServerFullCompliance": teModuleServerFullCompliance}
)
