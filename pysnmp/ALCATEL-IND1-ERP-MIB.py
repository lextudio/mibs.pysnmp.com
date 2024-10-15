# SNMP MIB module (ALCATEL-IND1-ERP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ALCATEL-IND1-ERP-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:35:59 2024
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

(softentIND1Erp,) = mibBuilder.importSymbols(
    "ALCATEL-IND1-BASE",
    "softentIND1Erp")

(InterfaceIndex,
 InterfaceIndexOrZero) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex",
    "InterfaceIndexOrZero")

(VlanId,) = mibBuilder.importSymbols(
    "Q-BRIDGE-MIB",
    "VlanId")

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
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention",
    "TimeStamp",
    "TruthValue")


# MODULE-IDENTITY

alcatelIND1ERPMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 46, 1)
)
alcatelIND1ERPMIB.setRevisions(
        ("2010-05-13 00:00",
         "2008-07-10 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class AlaErpRingPortStatus(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("blocking", 2),
          ("forwarding", 1))
    )



class AlaErpRingPortType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("nonRpl", 1),
          ("rpl", 2))
    )



class AlaErpRingMepId(Unsigned32, TextualConvention):
    status = "current"
    displayHint = "d"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8191),
    )



class AlaErpRingMEGLevel(Unsigned32, TextualConvention):
    status = "current"
    displayHint = "d"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )



# MIB Managed Objects in the order of their OIDs

_AlcatelIND1ErpMIBNotifications_ObjectIdentity = ObjectIdentity
alcatelIND1ErpMIBNotifications = _AlcatelIND1ErpMIBNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 46, 1, 0)
)
if mibBuilder.loadTexts:
    alcatelIND1ErpMIBNotifications.setStatus("current")
_AlcatelIND1ERPMIBObjects_ObjectIdentity = ObjectIdentity
alcatelIND1ERPMIBObjects = _AlcatelIND1ERPMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 46, 1, 1)
)
if mibBuilder.loadTexts:
    alcatelIND1ERPMIBObjects.setStatus("current")
_AlaErpGlobal_ObjectIdentity = ObjectIdentity
alaErpGlobal = _AlaErpGlobal_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 46, 1, 1, 1)
)


class _AlaErpClearStats_Type(Integer32):
    """Custom type alaErpClearStats based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("default", 0),
          ("reset", 1))
    )


_AlaErpClearStats_Type.__name__ = "Integer32"
_AlaErpClearStats_Object = MibScalar
alaErpClearStats = _AlaErpClearStats_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 46, 1, 1, 1, 1),
    _AlaErpClearStats_Type()
)
alaErpClearStats.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaErpClearStats.setStatus("current")
_AlaErpRingAttributes_ObjectIdentity = ObjectIdentity
alaErpRingAttributes = _AlaErpRingAttributes_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 46, 1, 1, 2)
)
_AlaErpRingTable_Object = MibTable
alaErpRingTable = _AlaErpRingTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 46, 1, 1, 2, 1)
)
if mibBuilder.loadTexts:
    alaErpRingTable.setStatus("current")
_AlaErpRingEntry_Object = MibTableRow
alaErpRingEntry = _AlaErpRingEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 46, 1, 1, 2, 1, 1)
)
alaErpRingEntry.setIndexNames(
    (0, "ALCATEL-IND1-ERP-MIB", "alaErpRingId"),
)
if mibBuilder.loadTexts:
    alaErpRingEntry.setStatus("current")


class _AlaErpRingId_Type(Integer32):
    """Custom type alaErpRingId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_AlaErpRingId_Type.__name__ = "Integer32"
_AlaErpRingId_Object = MibTableColumn
alaErpRingId = _AlaErpRingId_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 46, 1, 1, 2, 1, 1, 1),
    _AlaErpRingId_Type()
)
alaErpRingId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    alaErpRingId.setStatus("current")
_AlaErpRingServiceVid_Type = VlanId
_AlaErpRingServiceVid_Object = MibTableColumn
alaErpRingServiceVid = _AlaErpRingServiceVid_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 46, 1, 1, 2, 1, 1, 2),
    _AlaErpRingServiceVid_Type()
)
alaErpRingServiceVid.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaErpRingServiceVid.setStatus("current")
_AlaErpRingMEGLevel_Type = AlaErpRingMEGLevel
_AlaErpRingMEGLevel_Object = MibTableColumn
alaErpRingMEGLevel = _AlaErpRingMEGLevel_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 46, 1, 1, 2, 1, 1, 3),
    _AlaErpRingMEGLevel_Type()
)
alaErpRingMEGLevel.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaErpRingMEGLevel.setStatus("current")
_AlaErpRingPort1_Type = InterfaceIndex
_AlaErpRingPort1_Object = MibTableColumn
alaErpRingPort1 = _AlaErpRingPort1_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 46, 1, 1, 2, 1, 1, 4),
    _AlaErpRingPort1_Type()
)
alaErpRingPort1.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaErpRingPort1.setStatus("current")
_AlaErpRingPort2_Type = InterfaceIndexOrZero
_AlaErpRingPort2_Object = MibTableColumn
alaErpRingPort2 = _AlaErpRingPort2_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 46, 1, 1, 2, 1, 1, 5),
    _AlaErpRingPort2_Type()
)
alaErpRingPort2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaErpRingPort2.setStatus("current")


class _AlaErpRingStatus_Type(Integer32):
    """Custom type alaErpRingStatus based on Integer32"""
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


_AlaErpRingStatus_Type.__name__ = "Integer32"
_AlaErpRingStatus_Object = MibTableColumn
alaErpRingStatus = _AlaErpRingStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 46, 1, 1, 2, 1, 1, 6),
    _AlaErpRingStatus_Type()
)
alaErpRingStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaErpRingStatus.setStatus("current")


class _AlaErpRingState_Type(Integer32):
    """Custom type alaErpRingState based on Integer32"""
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
        *(("forcedSwitch", 4),
          ("idle", 0),
          ("init", 2),
          ("manualSwitch", 3),
          ("pending", 5),
          ("protection", 1))
    )


_AlaErpRingState_Type.__name__ = "Integer32"
_AlaErpRingState_Object = MibTableColumn
alaErpRingState = _AlaErpRingState_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 46, 1, 1, 2, 1, 1, 7),
    _AlaErpRingState_Type()
)
alaErpRingState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaErpRingState.setStatus("current")


class _AlaErpRingWaitToRestoreTimer_Type(Unsigned32):
    """Custom type alaErpRingWaitToRestoreTimer based on Unsigned32"""
    defaultValue = 5

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 12),
    )


_AlaErpRingWaitToRestoreTimer_Type.__name__ = "Unsigned32"
_AlaErpRingWaitToRestoreTimer_Object = MibTableColumn
alaErpRingWaitToRestoreTimer = _AlaErpRingWaitToRestoreTimer_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 46, 1, 1, 2, 1, 1, 8),
    _AlaErpRingWaitToRestoreTimer_Type()
)
alaErpRingWaitToRestoreTimer.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaErpRingWaitToRestoreTimer.setStatus("current")


class _AlaErpRingGuardTimer_Type(Integer32):
    """Custom type alaErpRingGuardTimer based on Integer32"""
    defaultValue = 50

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 200),
    )


_AlaErpRingGuardTimer_Type.__name__ = "Integer32"
_AlaErpRingGuardTimer_Object = MibTableColumn
alaErpRingGuardTimer = _AlaErpRingGuardTimer_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 46, 1, 1, 2, 1, 1, 9),
    _AlaErpRingGuardTimer_Type()
)
alaErpRingGuardTimer.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaErpRingGuardTimer.setStatus("current")
if mibBuilder.loadTexts:
    alaErpRingGuardTimer.setUnits("10 milliseconds")


class _AlaErpRingClearStats_Type(Integer32):
    """Custom type alaErpRingClearStats based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("default", 0),
          ("reset", 1))
    )


_AlaErpRingClearStats_Type.__name__ = "Integer32"
_AlaErpRingClearStats_Object = MibTableColumn
alaErpRingClearStats = _AlaErpRingClearStats_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 46, 1, 1, 2, 1, 1, 10),
    _AlaErpRingClearStats_Type()
)
alaErpRingClearStats.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaErpRingClearStats.setStatus("current")
_AlaErpRingLastStateChange_Type = TimeStamp
_AlaErpRingLastStateChange_Object = MibTableColumn
alaErpRingLastStateChange = _AlaErpRingLastStateChange_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 46, 1, 1, 2, 1, 1, 11),
    _AlaErpRingLastStateChange_Type()
)
alaErpRingLastStateChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaErpRingLastStateChange.setStatus("current")
_AlaErpRingTimeToRevert_Type = TimeTicks
_AlaErpRingTimeToRevert_Object = MibTableColumn
alaErpRingTimeToRevert = _AlaErpRingTimeToRevert_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 46, 1, 1, 2, 1, 1, 12),
    _AlaErpRingTimeToRevert_Type()
)
alaErpRingTimeToRevert.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaErpRingTimeToRevert.setStatus("current")
_AlaErpRingRowStatus_Type = RowStatus
_AlaErpRingRowStatus_Object = MibTableColumn
alaErpRingRowStatus = _AlaErpRingRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 46, 1, 1, 2, 1, 1, 13),
    _AlaErpRingRowStatus_Type()
)
alaErpRingRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaErpRingRowStatus.setStatus("current")


class _AlaErpRingVirtualChannel_Type(Integer32):
    """Custom type alaErpRingVirtualChannel based on Integer32"""
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


_AlaErpRingVirtualChannel_Type.__name__ = "Integer32"
_AlaErpRingVirtualChannel_Object = MibTableColumn
alaErpRingVirtualChannel = _AlaErpRingVirtualChannel_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 46, 1, 1, 2, 1, 1, 14),
    _AlaErpRingVirtualChannel_Type()
)
alaErpRingVirtualChannel.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaErpRingVirtualChannel.setStatus("current")


class _AlaErpRingRevertive_Type(Integer32):
    """Custom type alaErpRingRevertive based on Integer32"""
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


_AlaErpRingRevertive_Type.__name__ = "Integer32"
_AlaErpRingRevertive_Object = MibTableColumn
alaErpRingRevertive = _AlaErpRingRevertive_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 46, 1, 1, 2, 1, 1, 15),
    _AlaErpRingRevertive_Type()
)
alaErpRingRevertive.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaErpRingRevertive.setStatus("current")


class _AlaErpRingClearAction_Type(Integer32):
    """Custom type alaErpRingClearAction based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("default", 0),
          ("reset", 1))
    )


_AlaErpRingClearAction_Type.__name__ = "Integer32"
_AlaErpRingClearAction_Object = MibTableColumn
alaErpRingClearAction = _AlaErpRingClearAction_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 46, 1, 1, 2, 1, 1, 16),
    _AlaErpRingClearAction_Type()
)
alaErpRingClearAction.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaErpRingClearAction.setStatus("current")


class _AlaErpRingActiveVersion_Type(Unsigned32):
    """Custom type alaErpRingActiveVersion based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_AlaErpRingActiveVersion_Type.__name__ = "Unsigned32"
_AlaErpRingActiveVersion_Object = MibTableColumn
alaErpRingActiveVersion = _AlaErpRingActiveVersion_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 46, 1, 1, 2, 1, 1, 17),
    _AlaErpRingActiveVersion_Type()
)
alaErpRingActiveVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaErpRingActiveVersion.setStatus("current")


class _AlaErpRingResetVersionFallback_Type(Integer32):
    """Custom type alaErpRingResetVersionFallback based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("default", 0),
          ("reset", 1))
    )


_AlaErpRingResetVersionFallback_Type.__name__ = "Integer32"
_AlaErpRingResetVersionFallback_Object = MibTableColumn
alaErpRingResetVersionFallback = _AlaErpRingResetVersionFallback_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 46, 1, 1, 2, 1, 1, 18),
    _AlaErpRingResetVersionFallback_Type()
)
alaErpRingResetVersionFallback.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaErpRingResetVersionFallback.setStatus("current")
_AlaErpRingPortTable_Object = MibTable
alaErpRingPortTable = _AlaErpRingPortTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 46, 1, 1, 2, 2)
)
if mibBuilder.loadTexts:
    alaErpRingPortTable.setStatus("current")
_AlaErpRingPortEntry_Object = MibTableRow
alaErpRingPortEntry = _AlaErpRingPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 46, 1, 1, 2, 2, 1)
)
alaErpRingPortEntry.setIndexNames(
    (0, "ALCATEL-IND1-ERP-MIB", "alaErpRingId"),
    (0, "ALCATEL-IND1-ERP-MIB", "alaErpRingPortIfIndex"),
)
if mibBuilder.loadTexts:
    alaErpRingPortEntry.setStatus("current")
_AlaErpRingPortIfIndex_Type = InterfaceIndex
_AlaErpRingPortIfIndex_Object = MibTableColumn
alaErpRingPortIfIndex = _AlaErpRingPortIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 46, 1, 1, 2, 2, 1, 1),
    _AlaErpRingPortIfIndex_Type()
)
alaErpRingPortIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaErpRingPortIfIndex.setStatus("current")


class _AlaErpRingPortStatus_Type(AlaErpRingPortStatus):
    """Custom type alaErpRingPortStatus based on AlaErpRingPortStatus"""


_AlaErpRingPortStatus_Object = MibTableColumn
alaErpRingPortStatus = _AlaErpRingPortStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 46, 1, 1, 2, 2, 1, 2),
    _AlaErpRingPortStatus_Type()
)
alaErpRingPortStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaErpRingPortStatus.setStatus("current")


class _AlaErpRingPortType_Type(AlaErpRingPortType):
    """Custom type alaErpRingPortType based on AlaErpRingPortType"""


_AlaErpRingPortType_Object = MibTableColumn
alaErpRingPortType = _AlaErpRingPortType_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 46, 1, 1, 2, 2, 1, 3),
    _AlaErpRingPortType_Type()
)
alaErpRingPortType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaErpRingPortType.setStatus("current")


class _AlaErpRingPortEthOAMEvent_Type(TruthValue):
    """Custom type alaErpRingPortEthOAMEvent based on TruthValue"""


_AlaErpRingPortEthOAMEvent_Object = MibTableColumn
alaErpRingPortEthOAMEvent = _AlaErpRingPortEthOAMEvent_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 46, 1, 1, 2, 2, 1, 4),
    _AlaErpRingPortEthOAMEvent_Type()
)
alaErpRingPortEthOAMEvent.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaErpRingPortEthOAMEvent.setStatus("current")


class _AlaErpRingPortClearStats_Type(Integer32):
    """Custom type alaErpRingPortClearStats based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("default", 0),
          ("reset", 1))
    )


_AlaErpRingPortClearStats_Type.__name__ = "Integer32"
_AlaErpRingPortClearStats_Object = MibTableColumn
alaErpRingPortClearStats = _AlaErpRingPortClearStats_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 46, 1, 1, 2, 2, 1, 5),
    _AlaErpRingPortClearStats_Type()
)
alaErpRingPortClearStats.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaErpRingPortClearStats.setStatus("current")
_AlaErpRingPortRmepId_Type = AlaErpRingMepId
_AlaErpRingPortRmepId_Object = MibTableColumn
alaErpRingPortRmepId = _AlaErpRingPortRmepId_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 46, 1, 1, 2, 2, 1, 6),
    _AlaErpRingPortRmepId_Type()
)
alaErpRingPortRmepId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaErpRingPortRmepId.setStatus("current")


class _AlaErpRingPortVirtualSfMonitor_Type(TruthValue):
    """Custom type alaErpRingPortVirtualSfMonitor based on TruthValue"""


_AlaErpRingPortVirtualSfMonitor_Object = MibTableColumn
alaErpRingPortVirtualSfMonitor = _AlaErpRingPortVirtualSfMonitor_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 46, 1, 1, 2, 2, 1, 7),
    _AlaErpRingPortVirtualSfMonitor_Type()
)
alaErpRingPortVirtualSfMonitor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaErpRingPortVirtualSfMonitor.setStatus("current")
_AlaErpRingVlanTable_Object = MibTable
alaErpRingVlanTable = _AlaErpRingVlanTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 46, 1, 1, 2, 3)
)
if mibBuilder.loadTexts:
    alaErpRingVlanTable.setStatus("current")
_AlaErpRingVlanEntry_Object = MibTableRow
alaErpRingVlanEntry = _AlaErpRingVlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 46, 1, 1, 2, 3, 1)
)
alaErpRingVlanEntry.setIndexNames(
    (0, "ALCATEL-IND1-ERP-MIB", "alaErpRingId"),
    (0, "ALCATEL-IND1-ERP-MIB", "alaErpRingVlanProtectedVid"),
)
if mibBuilder.loadTexts:
    alaErpRingVlanEntry.setStatus("current")
_AlaErpRingVlanProtectedVid_Type = VlanId
_AlaErpRingVlanProtectedVid_Object = MibTableColumn
alaErpRingVlanProtectedVid = _AlaErpRingVlanProtectedVid_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 46, 1, 1, 2, 3, 1, 1),
    _AlaErpRingVlanProtectedVid_Type()
)
alaErpRingVlanProtectedVid.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaErpRingVlanProtectedVid.setStatus("current")
_AlaErpRingVlanRowStatus_Type = RowStatus
_AlaErpRingVlanRowStatus_Object = MibTableColumn
alaErpRingVlanRowStatus = _AlaErpRingVlanRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 46, 1, 1, 2, 3, 1, 2),
    _AlaErpRingVlanRowStatus_Type()
)
alaErpRingVlanRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaErpRingVlanRowStatus.setStatus("current")
_AlaErpStatsTable_Object = MibTable
alaErpStatsTable = _AlaErpStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 46, 1, 1, 2, 4)
)
if mibBuilder.loadTexts:
    alaErpStatsTable.setStatus("current")
_AlaErpStatsEntry_Object = MibTableRow
alaErpStatsEntry = _AlaErpStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 46, 1, 1, 2, 4, 1)
)
if mibBuilder.loadTexts:
    alaErpStatsEntry.setStatus("current")
_AlaErpStatsSignalFailPduTx_Type = Counter32
_AlaErpStatsSignalFailPduTx_Object = MibTableColumn
alaErpStatsSignalFailPduTx = _AlaErpStatsSignalFailPduTx_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 46, 1, 1, 2, 4, 1, 1),
    _AlaErpStatsSignalFailPduTx_Type()
)
alaErpStatsSignalFailPduTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaErpStatsSignalFailPduTx.setStatus("current")
_AlaErpStatsSignalFailPduRx_Type = Counter32
_AlaErpStatsSignalFailPduRx_Object = MibTableColumn
alaErpStatsSignalFailPduRx = _AlaErpStatsSignalFailPduRx_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 46, 1, 1, 2, 4, 1, 2),
    _AlaErpStatsSignalFailPduRx_Type()
)
alaErpStatsSignalFailPduRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaErpStatsSignalFailPduRx.setStatus("current")
_AlaErpStatsSignalFailPduDrop_Type = Counter32
_AlaErpStatsSignalFailPduDrop_Object = MibTableColumn
alaErpStatsSignalFailPduDrop = _AlaErpStatsSignalFailPduDrop_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 46, 1, 1, 2, 4, 1, 3),
    _AlaErpStatsSignalFailPduDrop_Type()
)
alaErpStatsSignalFailPduDrop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaErpStatsSignalFailPduDrop.setStatus("current")
_AlaErpStatsNoRequestPduTx_Type = Counter32
_AlaErpStatsNoRequestPduTx_Object = MibTableColumn
alaErpStatsNoRequestPduTx = _AlaErpStatsNoRequestPduTx_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 46, 1, 1, 2, 4, 1, 4),
    _AlaErpStatsNoRequestPduTx_Type()
)
alaErpStatsNoRequestPduTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaErpStatsNoRequestPduTx.setStatus("current")
_AlaErpStatsNoRequestPduRx_Type = Counter32
_AlaErpStatsNoRequestPduRx_Object = MibTableColumn
alaErpStatsNoRequestPduRx = _AlaErpStatsNoRequestPduRx_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 46, 1, 1, 2, 4, 1, 5),
    _AlaErpStatsNoRequestPduRx_Type()
)
alaErpStatsNoRequestPduRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaErpStatsNoRequestPduRx.setStatus("current")
_AlaErpStatsNoRequestPduDrop_Type = Counter32
_AlaErpStatsNoRequestPduDrop_Object = MibTableColumn
alaErpStatsNoRequestPduDrop = _AlaErpStatsNoRequestPduDrop_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 46, 1, 1, 2, 4, 1, 6),
    _AlaErpStatsNoRequestPduDrop_Type()
)
alaErpStatsNoRequestPduDrop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaErpStatsNoRequestPduDrop.setStatus("current")
_AlaErpStatsRPLBlockPDUTx_Type = Counter32
_AlaErpStatsRPLBlockPDUTx_Object = MibTableColumn
alaErpStatsRPLBlockPDUTx = _AlaErpStatsRPLBlockPDUTx_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 46, 1, 1, 2, 4, 1, 7),
    _AlaErpStatsRPLBlockPDUTx_Type()
)
alaErpStatsRPLBlockPDUTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaErpStatsRPLBlockPDUTx.setStatus("current")
_AlaErpStatsRPLBlockPDURx_Type = Counter32
_AlaErpStatsRPLBlockPDURx_Object = MibTableColumn
alaErpStatsRPLBlockPDURx = _AlaErpStatsRPLBlockPDURx_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 46, 1, 1, 2, 4, 1, 8),
    _AlaErpStatsRPLBlockPDURx_Type()
)
alaErpStatsRPLBlockPDURx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaErpStatsRPLBlockPDURx.setStatus("current")
_AlaErpStatsRPLBlockPDUDrop_Type = Counter32
_AlaErpStatsRPLBlockPDUDrop_Object = MibTableColumn
alaErpStatsRPLBlockPDUDrop = _AlaErpStatsRPLBlockPDUDrop_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 46, 1, 1, 2, 4, 1, 9),
    _AlaErpStatsRPLBlockPDUDrop_Type()
)
alaErpStatsRPLBlockPDUDrop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaErpStatsRPLBlockPDUDrop.setStatus("current")
_AlaErpStatsPDUErr_Type = Counter32
_AlaErpStatsPDUErr_Object = MibTableColumn
alaErpStatsPDUErr = _AlaErpStatsPDUErr_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 46, 1, 1, 2, 4, 1, 10),
    _AlaErpStatsPDUErr_Type()
)
alaErpStatsPDUErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaErpStatsPDUErr.setStatus("current")
_AlcatelIND1ERPMIBConformance_ObjectIdentity = ObjectIdentity
alcatelIND1ERPMIBConformance = _AlcatelIND1ERPMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 46, 1, 2)
)
_AlcatelIND1ERPMIBCompliances_ObjectIdentity = ObjectIdentity
alcatelIND1ERPMIBCompliances = _AlcatelIND1ERPMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 46, 1, 2, 1)
)
_AlcatelIND1ERPMIBGroups_ObjectIdentity = ObjectIdentity
alcatelIND1ERPMIBGroups = _AlcatelIND1ERPMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 46, 1, 2, 2)
)
alaErpRingPortEntry.registerAugmentions(
    ("ALCATEL-IND1-ERP-MIB",
     "alaErpStatsEntry")
)
alaErpStatsEntry.setIndexNames(*alaErpRingPortEntry.getIndexNames())

# Managed Objects groups

alaErpGlobalGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 46, 1, 2, 2, 1)
)
alaErpGlobalGroup.setObjects(
    ("ALCATEL-IND1-ERP-MIB", "alaErpClearStats")
)
if mibBuilder.loadTexts:
    alaErpGlobalGroup.setStatus("current")

alaErpRingAttributesGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 46, 1, 2, 2, 2)
)
alaErpRingAttributesGroup.setObjects(
      *(("ALCATEL-IND1-ERP-MIB", "alaErpRingId"),
        ("ALCATEL-IND1-ERP-MIB", "alaErpRingServiceVid"),
        ("ALCATEL-IND1-ERP-MIB", "alaErpRingMEGLevel"),
        ("ALCATEL-IND1-ERP-MIB", "alaErpRingPort1"),
        ("ALCATEL-IND1-ERP-MIB", "alaErpRingPort2"),
        ("ALCATEL-IND1-ERP-MIB", "alaErpRingStatus"),
        ("ALCATEL-IND1-ERP-MIB", "alaErpRingState"),
        ("ALCATEL-IND1-ERP-MIB", "alaErpRingWaitToRestoreTimer"),
        ("ALCATEL-IND1-ERP-MIB", "alaErpRingGuardTimer"),
        ("ALCATEL-IND1-ERP-MIB", "alaErpRingClearStats"),
        ("ALCATEL-IND1-ERP-MIB", "alaErpRingLastStateChange"),
        ("ALCATEL-IND1-ERP-MIB", "alaErpRingTimeToRevert"),
        ("ALCATEL-IND1-ERP-MIB", "alaErpRingRowStatus"),
        ("ALCATEL-IND1-ERP-MIB", "alaErpRingVirtualChannel"),
        ("ALCATEL-IND1-ERP-MIB", "alaErpRingRevertive"),
        ("ALCATEL-IND1-ERP-MIB", "alaErpRingClearAction"),
        ("ALCATEL-IND1-ERP-MIB", "alaErpRingPortStatus"),
        ("ALCATEL-IND1-ERP-MIB", "alaErpRingPortType"),
        ("ALCATEL-IND1-ERP-MIB", "alaErpRingPortEthOAMEvent"),
        ("ALCATEL-IND1-ERP-MIB", "alaErpRingPortClearStats"),
        ("ALCATEL-IND1-ERP-MIB", "alaErpRingPortRmepId"),
        ("ALCATEL-IND1-ERP-MIB", "alaErpRingVlanRowStatus"),
        ("ALCATEL-IND1-ERP-MIB", "alaErpStatsSignalFailPduTx"),
        ("ALCATEL-IND1-ERP-MIB", "alaErpStatsSignalFailPduRx"),
        ("ALCATEL-IND1-ERP-MIB", "alaErpStatsSignalFailPduDrop"),
        ("ALCATEL-IND1-ERP-MIB", "alaErpStatsNoRequestPduTx"),
        ("ALCATEL-IND1-ERP-MIB", "alaErpStatsNoRequestPduRx"),
        ("ALCATEL-IND1-ERP-MIB", "alaErpStatsNoRequestPduDrop"),
        ("ALCATEL-IND1-ERP-MIB", "alaErpStatsRPLBlockPDUTx"),
        ("ALCATEL-IND1-ERP-MIB", "alaErpStatsRPLBlockPDURx"),
        ("ALCATEL-IND1-ERP-MIB", "alaErpStatsRPLBlockPDUDrop"),
        ("ALCATEL-IND1-ERP-MIB", "alaErpStatsPDUErr"),
        ("ALCATEL-IND1-ERP-MIB", "alaErpRingPortVirtualSfMonitor"),
        ("ALCATEL-IND1-ERP-MIB", "alaErpRingActiveVersion"),
        ("ALCATEL-IND1-ERP-MIB", "alaErpRingResetVersionFallback"))
)
if mibBuilder.loadTexts:
    alaErpRingAttributesGroup.setStatus("current")


# Notification objects

alaErpRingStateChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 46, 1, 0, 1)
)
alaErpRingStateChanged.setObjects(
      *(("ALCATEL-IND1-ERP-MIB", "alaErpRingId"),
        ("ALCATEL-IND1-ERP-MIB", "alaErpRingState"))
)
if mibBuilder.loadTexts:
    alaErpRingStateChanged.setStatus(
        "current"
    )

alaErpRingMultipleRpl = NotificationType(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 46, 1, 0, 2)
)
alaErpRingMultipleRpl.setObjects(
    ("ALCATEL-IND1-ERP-MIB", "alaErpRingId")
)
if mibBuilder.loadTexts:
    alaErpRingMultipleRpl.setStatus(
        "current"
    )

alaErpRingRemoved = NotificationType(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 46, 1, 0, 3)
)
alaErpRingRemoved.setObjects(
    ("ALCATEL-IND1-ERP-MIB", "alaErpRingId")
)
if mibBuilder.loadTexts:
    alaErpRingRemoved.setStatus(
        "current"
    )


# Notifications groups

alaErpNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 46, 1, 2, 2, 3)
)
alaErpNotificationGroup.setObjects(
      *(("ALCATEL-IND1-ERP-MIB", "alaErpRingStateChanged"),
        ("ALCATEL-IND1-ERP-MIB", "alaErpRingMultipleRpl"),
        ("ALCATEL-IND1-ERP-MIB", "alaErpRingRemoved"))
)
if mibBuilder.loadTexts:
    alaErpNotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

alcatelIND1ERPMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 46, 1, 2, 1, 1)
)
if mibBuilder.loadTexts:
    alcatelIND1ERPMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ALCATEL-IND1-ERP-MIB",
    **{"AlaErpRingPortStatus": AlaErpRingPortStatus,
       "AlaErpRingPortType": AlaErpRingPortType,
       "AlaErpRingMepId": AlaErpRingMepId,
       "AlaErpRingMEGLevel": AlaErpRingMEGLevel,
       "alcatelIND1ERPMIB": alcatelIND1ERPMIB,
       "alcatelIND1ErpMIBNotifications": alcatelIND1ErpMIBNotifications,
       "alaErpRingStateChanged": alaErpRingStateChanged,
       "alaErpRingMultipleRpl": alaErpRingMultipleRpl,
       "alaErpRingRemoved": alaErpRingRemoved,
       "alcatelIND1ERPMIBObjects": alcatelIND1ERPMIBObjects,
       "alaErpGlobal": alaErpGlobal,
       "alaErpClearStats": alaErpClearStats,
       "alaErpRingAttributes": alaErpRingAttributes,
       "alaErpRingTable": alaErpRingTable,
       "alaErpRingEntry": alaErpRingEntry,
       "alaErpRingId": alaErpRingId,
       "alaErpRingServiceVid": alaErpRingServiceVid,
       "alaErpRingMEGLevel": alaErpRingMEGLevel,
       "alaErpRingPort1": alaErpRingPort1,
       "alaErpRingPort2": alaErpRingPort2,
       "alaErpRingStatus": alaErpRingStatus,
       "alaErpRingState": alaErpRingState,
       "alaErpRingWaitToRestoreTimer": alaErpRingWaitToRestoreTimer,
       "alaErpRingGuardTimer": alaErpRingGuardTimer,
       "alaErpRingClearStats": alaErpRingClearStats,
       "alaErpRingLastStateChange": alaErpRingLastStateChange,
       "alaErpRingTimeToRevert": alaErpRingTimeToRevert,
       "alaErpRingRowStatus": alaErpRingRowStatus,
       "alaErpRingVirtualChannel": alaErpRingVirtualChannel,
       "alaErpRingRevertive": alaErpRingRevertive,
       "alaErpRingClearAction": alaErpRingClearAction,
       "alaErpRingActiveVersion": alaErpRingActiveVersion,
       "alaErpRingResetVersionFallback": alaErpRingResetVersionFallback,
       "alaErpRingPortTable": alaErpRingPortTable,
       "alaErpRingPortEntry": alaErpRingPortEntry,
       "alaErpRingPortIfIndex": alaErpRingPortIfIndex,
       "alaErpRingPortStatus": alaErpRingPortStatus,
       "alaErpRingPortType": alaErpRingPortType,
       "alaErpRingPortEthOAMEvent": alaErpRingPortEthOAMEvent,
       "alaErpRingPortClearStats": alaErpRingPortClearStats,
       "alaErpRingPortRmepId": alaErpRingPortRmepId,
       "alaErpRingPortVirtualSfMonitor": alaErpRingPortVirtualSfMonitor,
       "alaErpRingVlanTable": alaErpRingVlanTable,
       "alaErpRingVlanEntry": alaErpRingVlanEntry,
       "alaErpRingVlanProtectedVid": alaErpRingVlanProtectedVid,
       "alaErpRingVlanRowStatus": alaErpRingVlanRowStatus,
       "alaErpStatsTable": alaErpStatsTable,
       "alaErpStatsEntry": alaErpStatsEntry,
       "alaErpStatsSignalFailPduTx": alaErpStatsSignalFailPduTx,
       "alaErpStatsSignalFailPduRx": alaErpStatsSignalFailPduRx,
       "alaErpStatsSignalFailPduDrop": alaErpStatsSignalFailPduDrop,
       "alaErpStatsNoRequestPduTx": alaErpStatsNoRequestPduTx,
       "alaErpStatsNoRequestPduRx": alaErpStatsNoRequestPduRx,
       "alaErpStatsNoRequestPduDrop": alaErpStatsNoRequestPduDrop,
       "alaErpStatsRPLBlockPDUTx": alaErpStatsRPLBlockPDUTx,
       "alaErpStatsRPLBlockPDURx": alaErpStatsRPLBlockPDURx,
       "alaErpStatsRPLBlockPDUDrop": alaErpStatsRPLBlockPDUDrop,
       "alaErpStatsPDUErr": alaErpStatsPDUErr,
       "alcatelIND1ERPMIBConformance": alcatelIND1ERPMIBConformance,
       "alcatelIND1ERPMIBCompliances": alcatelIND1ERPMIBCompliances,
       "alcatelIND1ERPMIBCompliance": alcatelIND1ERPMIBCompliance,
       "alcatelIND1ERPMIBGroups": alcatelIND1ERPMIBGroups,
       "alaErpGlobalGroup": alaErpGlobalGroup,
       "alaErpRingAttributesGroup": alaErpRingAttributesGroup,
       "alaErpNotificationGroup": alaErpNotificationGroup}
)
