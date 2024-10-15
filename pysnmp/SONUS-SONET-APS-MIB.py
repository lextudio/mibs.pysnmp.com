# SNMP MIB module (SONUS-SONET-APS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/SONUS-SONET-APS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:57:10 2024
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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention")

(sonusServicesMIBs,) = mibBuilder.importSymbols(
    "SONUS-SMI",
    "sonusServicesMIBs")


# MODULE-IDENTITY

sonusSonetApsMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 9)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class ApsK1K2(Integer32, TextualConvention):
    status = "current"


# MIB Managed Objects in the order of their OIDs

_SonusSonetApsMIBObjects_ObjectIdentity = ObjectIdentity
sonusSonetApsMIBObjects = _SonusSonetApsMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 9, 1)
)
_SonusApsGroupCount_Type = Gauge32
_SonusApsGroupCount_Object = MibScalar
sonusApsGroupCount = _SonusApsGroupCount_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 9, 1, 1),
    _SonusApsGroupCount_Type()
)
sonusApsGroupCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusApsGroupCount.setStatus("current")
_SonusApsGroupTable_Object = MibTable
sonusApsGroupTable = _SonusApsGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 9, 1, 2)
)
if mibBuilder.loadTexts:
    sonusApsGroupTable.setStatus("current")
_SonusApsGroupEntry_Object = MibTableRow
sonusApsGroupEntry = _SonusApsGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 9, 1, 2, 1)
)
sonusApsGroupEntry.setIndexNames(
    (0, "SONUS-SONET-APS-MIB", "sonusApsGroupId"),
)
if mibBuilder.loadTexts:
    sonusApsGroupEntry.setStatus("current")
_SonusApsGroupId_Type = InterfaceIndex
_SonusApsGroupId_Object = MibTableColumn
sonusApsGroupId = _SonusApsGroupId_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 9, 1, 2, 1, 1),
    _SonusApsGroupId_Type()
)
sonusApsGroupId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sonusApsGroupId.setStatus("current")
_SonusApsGroupStatus_Type = RowStatus
_SonusApsGroupStatus_Object = MibTableColumn
sonusApsGroupStatus = _SonusApsGroupStatus_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 9, 1, 2, 1, 2),
    _SonusApsGroupStatus_Type()
)
sonusApsGroupStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sonusApsGroupStatus.setStatus("current")


class _SonusApsGroupArchitecture_Type(Integer32):
    """Custom type sonusApsGroupArchitecture based on Integer32"""
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
        *(("onePlusOne", 1),
          ("oneToN", 2),
          ("resilientUNI", 3))
    )


_SonusApsGroupArchitecture_Type.__name__ = "Integer32"
_SonusApsGroupArchitecture_Object = MibTableColumn
sonusApsGroupArchitecture = _SonusApsGroupArchitecture_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 9, 1, 2, 1, 3),
    _SonusApsGroupArchitecture_Type()
)
sonusApsGroupArchitecture.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sonusApsGroupArchitecture.setStatus("current")


class _SonusApsGroupAdminDirection_Type(Integer32):
    """Custom type sonusApsGroupAdminDirection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("bidirectional", 2),
          ("unidirectional", 1))
    )


_SonusApsGroupAdminDirection_Type.__name__ = "Integer32"
_SonusApsGroupAdminDirection_Object = MibTableColumn
sonusApsGroupAdminDirection = _SonusApsGroupAdminDirection_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 9, 1, 2, 1, 4),
    _SonusApsGroupAdminDirection_Type()
)
sonusApsGroupAdminDirection.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sonusApsGroupAdminDirection.setStatus("current")


class _SonusApsGroupAdminSwitching_Type(Integer32):
    """Custom type sonusApsGroupAdminSwitching based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("nonrevertive", 1),
          ("revertive", 2))
    )


_SonusApsGroupAdminSwitching_Type.__name__ = "Integer32"
_SonusApsGroupAdminSwitching_Object = MibTableColumn
sonusApsGroupAdminSwitching = _SonusApsGroupAdminSwitching_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 9, 1, 2, 1, 5),
    _SonusApsGroupAdminSwitching_Type()
)
sonusApsGroupAdminSwitching.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sonusApsGroupAdminSwitching.setStatus("current")


class _SonusApsGroupExtraTraffic_Type(Integer32):
    """Custom type sonusApsGroupExtraTraffic based on Integer32"""
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


_SonusApsGroupExtraTraffic_Type.__name__ = "Integer32"
_SonusApsGroupExtraTraffic_Object = MibTableColumn
sonusApsGroupExtraTraffic = _SonusApsGroupExtraTraffic_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 9, 1, 2, 1, 6),
    _SonusApsGroupExtraTraffic_Type()
)
sonusApsGroupExtraTraffic.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sonusApsGroupExtraTraffic.setStatus("current")


class _SonusApsGroupSignalFailBerThreshold_Type(Integer32):
    """Custom type sonusApsGroupSignalFailBerThreshold based on Integer32"""
    defaultValue = 5

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(3, 5),
    )


_SonusApsGroupSignalFailBerThreshold_Type.__name__ = "Integer32"
_SonusApsGroupSignalFailBerThreshold_Object = MibTableColumn
sonusApsGroupSignalFailBerThreshold = _SonusApsGroupSignalFailBerThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 9, 1, 2, 1, 7),
    _SonusApsGroupSignalFailBerThreshold_Type()
)
sonusApsGroupSignalFailBerThreshold.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sonusApsGroupSignalFailBerThreshold.setStatus("current")


class _SonusApsGroupSignalDegradeBerThreshold_Type(Integer32):
    """Custom type sonusApsGroupSignalDegradeBerThreshold based on Integer32"""
    defaultValue = 9

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 9),
    )


_SonusApsGroupSignalDegradeBerThreshold_Type.__name__ = "Integer32"
_SonusApsGroupSignalDegradeBerThreshold_Object = MibTableColumn
sonusApsGroupSignalDegradeBerThreshold = _SonusApsGroupSignalDegradeBerThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 9, 1, 2, 1, 8),
    _SonusApsGroupSignalDegradeBerThreshold_Type()
)
sonusApsGroupSignalDegradeBerThreshold.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sonusApsGroupSignalDegradeBerThreshold.setStatus("current")


class _SonusApsGroupWaitToRestoreTime_Type(Integer32):
    """Custom type sonusApsGroupWaitToRestoreTime based on Integer32"""
    defaultValue = 5

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 12),
    )


_SonusApsGroupWaitToRestoreTime_Type.__name__ = "Integer32"
_SonusApsGroupWaitToRestoreTime_Object = MibTableColumn
sonusApsGroupWaitToRestoreTime = _SonusApsGroupWaitToRestoreTime_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 9, 1, 2, 1, 9),
    _SonusApsGroupWaitToRestoreTime_Type()
)
sonusApsGroupWaitToRestoreTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sonusApsGroupWaitToRestoreTime.setStatus("current")


class _SonusApsGroupName_Type(DisplayString):
    """Custom type sonusApsGroupName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_SonusApsGroupName_Type.__name__ = "DisplayString"
_SonusApsGroupName_Object = MibTableColumn
sonusApsGroupName = _SonusApsGroupName_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 9, 1, 2, 1, 10),
    _SonusApsGroupName_Type()
)
sonusApsGroupName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sonusApsGroupName.setStatus("current")


class _SonusApsGroupSwitchedChannel_Type(Integer32):
    """Custom type sonusApsGroupSwitchedChannel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_SonusApsGroupSwitchedChannel_Type.__name__ = "Integer32"
_SonusApsGroupSwitchedChannel_Object = MibTableColumn
sonusApsGroupSwitchedChannel = _SonusApsGroupSwitchedChannel_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 9, 1, 2, 1, 11),
    _SonusApsGroupSwitchedChannel_Type()
)
sonusApsGroupSwitchedChannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusApsGroupSwitchedChannel.setStatus("current")


class _SonusApsGroupOperStatus_Type(Bits):
    """Custom type sonusApsGroupOperStatus based on Bits"""
    namedValues = NamedValues(
        *(("apsModeMismatch", 3),
          ("channelMismatch", 2),
          ("extraTraffic", 0),
          ("farEndProtectionLineDefect", 4),
          ("protectionSwitchingByteDefect", 1))
    )

_SonusApsGroupOperStatus_Type.__name__ = "Bits"
_SonusApsGroupOperStatus_Object = MibTableColumn
sonusApsGroupOperStatus = _SonusApsGroupOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 9, 1, 2, 1, 12),
    _SonusApsGroupOperStatus_Type()
)
sonusApsGroupOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusApsGroupOperStatus.setStatus("current")
_SonusApsGroupK1K2Received_Type = ApsK1K2
_SonusApsGroupK1K2Received_Object = MibTableColumn
sonusApsGroupK1K2Received = _SonusApsGroupK1K2Received_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 9, 1, 2, 1, 13),
    _SonusApsGroupK1K2Received_Type()
)
sonusApsGroupK1K2Received.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusApsGroupK1K2Received.setStatus("current")
_SonusApsGroupK1K2Transmitted_Type = ApsK1K2
_SonusApsGroupK1K2Transmitted_Object = MibTableColumn
sonusApsGroupK1K2Transmitted = _SonusApsGroupK1K2Transmitted_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 9, 1, 2, 1, 14),
    _SonusApsGroupK1K2Transmitted_Type()
)
sonusApsGroupK1K2Transmitted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusApsGroupK1K2Transmitted.setStatus("current")
_SonusApsGroupProtectionSwitchingByteFailures_Type = Counter32
_SonusApsGroupProtectionSwitchingByteFailures_Object = MibTableColumn
sonusApsGroupProtectionSwitchingByteFailures = _SonusApsGroupProtectionSwitchingByteFailures_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 9, 1, 2, 1, 15),
    _SonusApsGroupProtectionSwitchingByteFailures_Type()
)
sonusApsGroupProtectionSwitchingByteFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusApsGroupProtectionSwitchingByteFailures.setStatus("current")
_SonusApsGroupChannelMismatches_Type = Counter32
_SonusApsGroupChannelMismatches_Object = MibTableColumn
sonusApsGroupChannelMismatches = _SonusApsGroupChannelMismatches_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 9, 1, 2, 1, 16),
    _SonusApsGroupChannelMismatches_Type()
)
sonusApsGroupChannelMismatches.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusApsGroupChannelMismatches.setStatus("current")
_SonusApsGroupModeMismatches_Type = Counter32
_SonusApsGroupModeMismatches_Object = MibTableColumn
sonusApsGroupModeMismatches = _SonusApsGroupModeMismatches_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 9, 1, 2, 1, 17),
    _SonusApsGroupModeMismatches_Type()
)
sonusApsGroupModeMismatches.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusApsGroupModeMismatches.setStatus("current")
_SonusApsGroupFarEndProtectionLineFailures_Type = Counter32
_SonusApsGroupFarEndProtectionLineFailures_Object = MibTableColumn
sonusApsGroupFarEndProtectionLineFailures = _SonusApsGroupFarEndProtectionLineFailures_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 9, 1, 2, 1, 18),
    _SonusApsGroupFarEndProtectionLineFailures_Type()
)
sonusApsGroupFarEndProtectionLineFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusApsGroupFarEndProtectionLineFailures.setStatus("current")
_SonusApsGroupCreationTime_Type = TimeTicks
_SonusApsGroupCreationTime_Object = MibTableColumn
sonusApsGroupCreationTime = _SonusApsGroupCreationTime_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 9, 1, 2, 1, 19),
    _SonusApsGroupCreationTime_Type()
)
sonusApsGroupCreationTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusApsGroupCreationTime.setStatus("current")
_SonusApsChannelTable_Object = MibTable
sonusApsChannelTable = _SonusApsChannelTable_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 9, 1, 3)
)
if mibBuilder.loadTexts:
    sonusApsChannelTable.setStatus("current")
_SonusApsChannelEntry_Object = MibTableRow
sonusApsChannelEntry = _SonusApsChannelEntry_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 9, 1, 3, 1)
)
sonusApsChannelEntry.setIndexNames(
    (0, "SONUS-SONET-APS-MIB", "sonusApsGroupId"),
    (0, "SONUS-SONET-APS-MIB", "sonusApsChannelNumber"),
)
if mibBuilder.loadTexts:
    sonusApsChannelEntry.setStatus("current")


class _SonusApsChannelNumber_Type(Integer32):
    """Custom type sonusApsChannelNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_SonusApsChannelNumber_Type.__name__ = "Integer32"
_SonusApsChannelNumber_Object = MibTableColumn
sonusApsChannelNumber = _SonusApsChannelNumber_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 9, 1, 3, 1, 1),
    _SonusApsChannelNumber_Type()
)
sonusApsChannelNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sonusApsChannelNumber.setStatus("current")
_SonusApsChannelLineId_Type = InterfaceIndex
_SonusApsChannelLineId_Object = MibTableColumn
sonusApsChannelLineId = _SonusApsChannelLineId_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 9, 1, 3, 1, 2),
    _SonusApsChannelLineId_Type()
)
sonusApsChannelLineId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sonusApsChannelLineId.setStatus("current")


class _SonusApsChannelPriority_Type(Integer32):
    """Custom type sonusApsChannelPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("high", 2),
          ("low", 1))
    )


_SonusApsChannelPriority_Type.__name__ = "Integer32"
_SonusApsChannelPriority_Object = MibTableColumn
sonusApsChannelPriority = _SonusApsChannelPriority_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 9, 1, 3, 1, 3),
    _SonusApsChannelPriority_Type()
)
sonusApsChannelPriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sonusApsChannelPriority.setStatus("current")


class _SonusApsChannelSwitchCommand_Type(Integer32):
    """Custom type sonusApsChannelSwitchCommand based on Integer32"""
    defaultValue = 1

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
        *(("clear", 1),
          ("exercise", 7),
          ("forcedSwitchOfProtection", 4),
          ("forcedSwitchOfWorking", 3),
          ("lockoutOfProtection", 2),
          ("manualSwitchOfProtection", 6),
          ("manualSwitchOfWorking", 5))
    )


_SonusApsChannelSwitchCommand_Type.__name__ = "Integer32"
_SonusApsChannelSwitchCommand_Object = MibTableColumn
sonusApsChannelSwitchCommand = _SonusApsChannelSwitchCommand_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 9, 1, 3, 1, 4),
    _SonusApsChannelSwitchCommand_Type()
)
sonusApsChannelSwitchCommand.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sonusApsChannelSwitchCommand.setStatus("current")


class _SonusApsChannelControlCommand_Type(Integer32):
    """Custom type sonusApsChannelControlCommand based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("clearLockout", 2),
          ("lockoutWorkingChannel", 1))
    )


_SonusApsChannelControlCommand_Type.__name__ = "Integer32"
_SonusApsChannelControlCommand_Object = MibTableColumn
sonusApsChannelControlCommand = _SonusApsChannelControlCommand_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 9, 1, 3, 1, 5),
    _SonusApsChannelControlCommand_Type()
)
sonusApsChannelControlCommand.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sonusApsChannelControlCommand.setStatus("current")


class _SonusApsChannelStatus_Type(Bits):
    """Custom type sonusApsChannelStatus based on Bits"""
    namedValues = NamedValues(
        *(("bothLinesFailed", 4),
          ("lockedOut", 2),
          ("protectionLineBusy", 5),
          ("sdCondition", 0),
          ("sfCondition", 1),
          ("switched", 3))
    )

_SonusApsChannelStatus_Type.__name__ = "Bits"
_SonusApsChannelStatus_Object = MibTableColumn
sonusApsChannelStatus = _SonusApsChannelStatus_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 9, 1, 3, 1, 6),
    _SonusApsChannelStatus_Type()
)
sonusApsChannelStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusApsChannelStatus.setStatus("current")


class _SonusApsChannelOperDirectionMode_Type(Integer32):
    """Custom type sonusApsChannelOperDirectionMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("bidirectional", 2),
          ("unidirectional", 1))
    )


_SonusApsChannelOperDirectionMode_Type.__name__ = "Integer32"
_SonusApsChannelOperDirectionMode_Object = MibTableColumn
sonusApsChannelOperDirectionMode = _SonusApsChannelOperDirectionMode_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 9, 1, 3, 1, 7),
    _SonusApsChannelOperDirectionMode_Type()
)
sonusApsChannelOperDirectionMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusApsChannelOperDirectionMode.setStatus("current")
_SonusApsChannelSignalDegrades_Type = Counter32
_SonusApsChannelSignalDegrades_Object = MibTableColumn
sonusApsChannelSignalDegrades = _SonusApsChannelSignalDegrades_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 9, 1, 3, 1, 8),
    _SonusApsChannelSignalDegrades_Type()
)
sonusApsChannelSignalDegrades.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusApsChannelSignalDegrades.setStatus("current")
_SonusApsChannelSignalFails_Type = Counter32
_SonusApsChannelSignalFails_Object = MibTableColumn
sonusApsChannelSignalFails = _SonusApsChannelSignalFails_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 9, 1, 3, 1, 9),
    _SonusApsChannelSignalFails_Type()
)
sonusApsChannelSignalFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusApsChannelSignalFails.setStatus("current")
_SonusApsChannelSwitchovers_Type = Counter32
_SonusApsChannelSwitchovers_Object = MibTableColumn
sonusApsChannelSwitchovers = _SonusApsChannelSwitchovers_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 9, 1, 3, 1, 10),
    _SonusApsChannelSwitchovers_Type()
)
sonusApsChannelSwitchovers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusApsChannelSwitchovers.setStatus("current")
_SonusApsChannelLastSwitchover_Type = TimeTicks
_SonusApsChannelLastSwitchover_Object = MibTableColumn
sonusApsChannelLastSwitchover = _SonusApsChannelLastSwitchover_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 9, 1, 3, 1, 11),
    _SonusApsChannelLastSwitchover_Type()
)
sonusApsChannelLastSwitchover.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusApsChannelLastSwitchover.setStatus("current")
_SonusApsChannelRowStatus_Type = RowStatus
_SonusApsChannelRowStatus_Object = MibTableColumn
sonusApsChannelRowStatus = _SonusApsChannelRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 9, 1, 3, 1, 12),
    _SonusApsChannelRowStatus_Type()
)
sonusApsChannelRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sonusApsChannelRowStatus.setStatus("current")
_SonusApsLineTable_Object = MibTable
sonusApsLineTable = _SonusApsLineTable_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 9, 1, 4)
)
if mibBuilder.loadTexts:
    sonusApsLineTable.setStatus("current")
_SonusApsLineEntry_Object = MibTableRow
sonusApsLineEntry = _SonusApsLineEntry_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 9, 1, 4, 1)
)
sonusApsLineEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    sonusApsLineEntry.setStatus("current")
_SonusApsLineGroupId_Type = InterfaceIndex
_SonusApsLineGroupId_Object = MibTableColumn
sonusApsLineGroupId = _SonusApsLineGroupId_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 9, 1, 4, 1, 1),
    _SonusApsLineGroupId_Type()
)
sonusApsLineGroupId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusApsLineGroupId.setStatus("current")


class _SonusApsLineChannelNumber_Type(Integer32):
    """Custom type sonusApsLineChannelNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_SonusApsLineChannelNumber_Type.__name__ = "Integer32"
_SonusApsLineChannelNumber_Object = MibTableColumn
sonusApsLineChannelNumber = _SonusApsLineChannelNumber_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 9, 1, 4, 1, 2),
    _SonusApsLineChannelNumber_Type()
)
sonusApsLineChannelNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusApsLineChannelNumber.setStatus("current")
_SonusSonetApsMIBNotifications_ObjectIdentity = ObjectIdentity
sonusSonetApsMIBNotifications = _SonusSonetApsMIBNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 9, 2)
)
_SonusSonetApsMIBNotificationsPrefix_ObjectIdentity = ObjectIdentity
sonusSonetApsMIBNotificationsPrefix = _SonusSonetApsMIBNotificationsPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 9, 2, 0)
)
_SonusSonetApsConformance_ObjectIdentity = ObjectIdentity
sonusSonetApsConformance = _SonusSonetApsConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 9, 3)
)
_SonusSonetApsGroups_ObjectIdentity = ObjectIdentity
sonusSonetApsGroups = _SonusSonetApsGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 9, 3, 1)
)
_SonusSonetApsCompliances_ObjectIdentity = ObjectIdentity
sonusSonetApsCompliances = _SonusSonetApsCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 9, 3, 2)
)

# Managed Objects groups

sonusApsGroupGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 9, 3, 1, 1)
)
sonusApsGroupGroup.setObjects(
      *(("SONUS-SONET-APS-MIB", "sonusApsGroupCount"),
        ("SONUS-SONET-APS-MIB", "sonusApsGroupStatus"),
        ("SONUS-SONET-APS-MIB", "sonusApsGroupArchitecture"),
        ("SONUS-SONET-APS-MIB", "sonusApsGroupAdminDirection"),
        ("SONUS-SONET-APS-MIB", "sonusApsGroupAdminSwitching"),
        ("SONUS-SONET-APS-MIB", "sonusApsGroupExtraTraffic"),
        ("SONUS-SONET-APS-MIB", "sonusApsGroupSignalFailBerThreshold"),
        ("SONUS-SONET-APS-MIB", "sonusApsGroupSignalDegradeBerThreshold"),
        ("SONUS-SONET-APS-MIB", "sonusApsGroupWaitToRestoreTime"),
        ("SONUS-SONET-APS-MIB", "sonusApsGroupName"),
        ("SONUS-SONET-APS-MIB", "sonusApsGroupSwitchedChannel"),
        ("SONUS-SONET-APS-MIB", "sonusApsGroupOperStatus"),
        ("SONUS-SONET-APS-MIB", "sonusApsGroupK1K2Received"),
        ("SONUS-SONET-APS-MIB", "sonusApsGroupK1K2Transmitted"),
        ("SONUS-SONET-APS-MIB", "sonusApsGroupProtectionSwitchingByteFailures"),
        ("SONUS-SONET-APS-MIB", "sonusApsGroupChannelMismatches"),
        ("SONUS-SONET-APS-MIB", "sonusApsGroupModeMismatches"),
        ("SONUS-SONET-APS-MIB", "sonusApsGroupFarEndProtectionLineFailures"),
        ("SONUS-SONET-APS-MIB", "sonusApsGroupCreationTime"))
)
if mibBuilder.loadTexts:
    sonusApsGroupGroup.setStatus("current")

sonusApsChannelGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 9, 3, 1, 2)
)
sonusApsChannelGroup.setObjects(
      *(("SONUS-SONET-APS-MIB", "sonusApsChannelLineId"),
        ("SONUS-SONET-APS-MIB", "sonusApsChannelPriority"),
        ("SONUS-SONET-APS-MIB", "sonusApsChannelSwitchCommand"),
        ("SONUS-SONET-APS-MIB", "sonusApsChannelControlCommand"),
        ("SONUS-SONET-APS-MIB", "sonusApsChannelStatus"),
        ("SONUS-SONET-APS-MIB", "sonusApsChannelOperDirectionMode"),
        ("SONUS-SONET-APS-MIB", "sonusApsChannelSignalDegrades"),
        ("SONUS-SONET-APS-MIB", "sonusApsChannelSignalFails"),
        ("SONUS-SONET-APS-MIB", "sonusApsChannelSwitchovers"),
        ("SONUS-SONET-APS-MIB", "sonusApsChannelLastSwitchover"))
)
if mibBuilder.loadTexts:
    sonusApsChannelGroup.setStatus("current")

sonusApsLineGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 9, 3, 1, 3)
)
sonusApsLineGroup.setObjects(
      *(("SONUS-SONET-APS-MIB", "sonusApsLineGroupId"),
        ("SONUS-SONET-APS-MIB", "sonusApsLineChannelNumber"))
)
if mibBuilder.loadTexts:
    sonusApsLineGroup.setStatus("current")


# Notification objects

sonusApsTrapProtectionSwitchingByteFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 9, 2, 0, 1)
)
sonusApsTrapProtectionSwitchingByteFailure.setObjects(
      *(("SONUS-SONET-APS-MIB", "sonusApsGroupProtectionSwitchingByteFailures"),
        ("SONUS-SONET-APS-MIB", "sonusApsGroupOperStatus"))
)
if mibBuilder.loadTexts:
    sonusApsTrapProtectionSwitchingByteFailure.setStatus(
        "current"
    )

sonusApsTrapChannelMismatch = NotificationType(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 9, 2, 0, 2)
)
sonusApsTrapChannelMismatch.setObjects(
      *(("SONUS-SONET-APS-MIB", "sonusApsGroupChannelMismatches"),
        ("SONUS-SONET-APS-MIB", "sonusApsGroupOperStatus"))
)
if mibBuilder.loadTexts:
    sonusApsTrapChannelMismatch.setStatus(
        "current"
    )

sonusApsTrapModeMismatch = NotificationType(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 9, 2, 0, 3)
)
sonusApsTrapModeMismatch.setObjects(
      *(("SONUS-SONET-APS-MIB", "sonusApsGroupModeMismatches"),
        ("SONUS-SONET-APS-MIB", "sonusApsGroupOperStatus"))
)
if mibBuilder.loadTexts:
    sonusApsTrapModeMismatch.setStatus(
        "current"
    )

sonusApsTrapFarEndProtectionLineFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 9, 2, 0, 4)
)
sonusApsTrapFarEndProtectionLineFailure.setObjects(
      *(("SONUS-SONET-APS-MIB", "sonusApsGroupFarEndProtectionLineFailures"),
        ("SONUS-SONET-APS-MIB", "sonusApsGroupOperStatus"))
)
if mibBuilder.loadTexts:
    sonusApsTrapFarEndProtectionLineFailure.setStatus(
        "current"
    )

sonusApsTrapSwitchover = NotificationType(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 9, 2, 0, 5)
)
sonusApsTrapSwitchover.setObjects(
      *(("SONUS-SONET-APS-MIB", "sonusApsChannelSwitchovers"),
        ("SONUS-SONET-APS-MIB", "sonusApsChannelStatus"))
)
if mibBuilder.loadTexts:
    sonusApsTrapSwitchover.setStatus(
        "current"
    )


# Notifications groups

sonusApsNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 9, 3, 1, 4)
)
sonusApsNotificationGroup.setObjects(
      *(("SONUS-SONET-APS-MIB", "sonusApsTrapProtectionSwitchingByteFailure"),
        ("SONUS-SONET-APS-MIB", "sonusApsTrapChannelMismatch"),
        ("SONUS-SONET-APS-MIB", "sonusApsTrapModeMismatch"),
        ("SONUS-SONET-APS-MIB", "sonusApsTrapFarEndProtectionLineFailure"),
        ("SONUS-SONET-APS-MIB", "sonusApsTrapSwitchover"))
)
if mibBuilder.loadTexts:
    sonusApsNotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

sonusSonetApsCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 9, 3, 2, 1)
)
if mibBuilder.loadTexts:
    sonusSonetApsCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SONUS-SONET-APS-MIB",
    **{"ApsK1K2": ApsK1K2,
       "sonusSonetApsMIB": sonusSonetApsMIB,
       "sonusSonetApsMIBObjects": sonusSonetApsMIBObjects,
       "sonusApsGroupCount": sonusApsGroupCount,
       "sonusApsGroupTable": sonusApsGroupTable,
       "sonusApsGroupEntry": sonusApsGroupEntry,
       "sonusApsGroupId": sonusApsGroupId,
       "sonusApsGroupStatus": sonusApsGroupStatus,
       "sonusApsGroupArchitecture": sonusApsGroupArchitecture,
       "sonusApsGroupAdminDirection": sonusApsGroupAdminDirection,
       "sonusApsGroupAdminSwitching": sonusApsGroupAdminSwitching,
       "sonusApsGroupExtraTraffic": sonusApsGroupExtraTraffic,
       "sonusApsGroupSignalFailBerThreshold": sonusApsGroupSignalFailBerThreshold,
       "sonusApsGroupSignalDegradeBerThreshold": sonusApsGroupSignalDegradeBerThreshold,
       "sonusApsGroupWaitToRestoreTime": sonusApsGroupWaitToRestoreTime,
       "sonusApsGroupName": sonusApsGroupName,
       "sonusApsGroupSwitchedChannel": sonusApsGroupSwitchedChannel,
       "sonusApsGroupOperStatus": sonusApsGroupOperStatus,
       "sonusApsGroupK1K2Received": sonusApsGroupK1K2Received,
       "sonusApsGroupK1K2Transmitted": sonusApsGroupK1K2Transmitted,
       "sonusApsGroupProtectionSwitchingByteFailures": sonusApsGroupProtectionSwitchingByteFailures,
       "sonusApsGroupChannelMismatches": sonusApsGroupChannelMismatches,
       "sonusApsGroupModeMismatches": sonusApsGroupModeMismatches,
       "sonusApsGroupFarEndProtectionLineFailures": sonusApsGroupFarEndProtectionLineFailures,
       "sonusApsGroupCreationTime": sonusApsGroupCreationTime,
       "sonusApsChannelTable": sonusApsChannelTable,
       "sonusApsChannelEntry": sonusApsChannelEntry,
       "sonusApsChannelNumber": sonusApsChannelNumber,
       "sonusApsChannelLineId": sonusApsChannelLineId,
       "sonusApsChannelPriority": sonusApsChannelPriority,
       "sonusApsChannelSwitchCommand": sonusApsChannelSwitchCommand,
       "sonusApsChannelControlCommand": sonusApsChannelControlCommand,
       "sonusApsChannelStatus": sonusApsChannelStatus,
       "sonusApsChannelOperDirectionMode": sonusApsChannelOperDirectionMode,
       "sonusApsChannelSignalDegrades": sonusApsChannelSignalDegrades,
       "sonusApsChannelSignalFails": sonusApsChannelSignalFails,
       "sonusApsChannelSwitchovers": sonusApsChannelSwitchovers,
       "sonusApsChannelLastSwitchover": sonusApsChannelLastSwitchover,
       "sonusApsChannelRowStatus": sonusApsChannelRowStatus,
       "sonusApsLineTable": sonusApsLineTable,
       "sonusApsLineEntry": sonusApsLineEntry,
       "sonusApsLineGroupId": sonusApsLineGroupId,
       "sonusApsLineChannelNumber": sonusApsLineChannelNumber,
       "sonusSonetApsMIBNotifications": sonusSonetApsMIBNotifications,
       "sonusSonetApsMIBNotificationsPrefix": sonusSonetApsMIBNotificationsPrefix,
       "sonusApsTrapProtectionSwitchingByteFailure": sonusApsTrapProtectionSwitchingByteFailure,
       "sonusApsTrapChannelMismatch": sonusApsTrapChannelMismatch,
       "sonusApsTrapModeMismatch": sonusApsTrapModeMismatch,
       "sonusApsTrapFarEndProtectionLineFailure": sonusApsTrapFarEndProtectionLineFailure,
       "sonusApsTrapSwitchover": sonusApsTrapSwitchover,
       "sonusSonetApsConformance": sonusSonetApsConformance,
       "sonusSonetApsGroups": sonusSonetApsGroups,
       "sonusApsGroupGroup": sonusApsGroupGroup,
       "sonusApsChannelGroup": sonusApsChannelGroup,
       "sonusApsLineGroup": sonusApsLineGroup,
       "sonusApsNotificationGroup": sonusApsNotificationGroup,
       "sonusSonetApsCompliances": sonusSonetApsCompliances,
       "sonusSonetApsCompliance": sonusSonetApsCompliance}
)
