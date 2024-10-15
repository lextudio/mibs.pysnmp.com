# SNMP MIB module (SONUS-REDUNDANCY-SERVICES-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/SONUS-REDUNDANCY-SERVICES-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:57:06 2024
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

(sonusEventClass,
 sonusEventDescription,
 sonusEventLevel,
 sonusShelfIndex,
 sonusSlotIndex) = mibBuilder.importSymbols(
    "SONUS-COMMON-MIB",
    "sonusEventClass",
    "sonusEventDescription",
    "sonusEventLevel",
    "sonusShelfIndex",
    "sonusSlotIndex")

(sonusServicesMIBs,) = mibBuilder.importSymbols(
    "SONUS-SMI",
    "sonusServicesMIBs")

(ServerFunctionType,
 ServerTypeID,
 SonusName) = mibBuilder.importSymbols(
    "SONUS-TC",
    "ServerFunctionType",
    "ServerTypeID",
    "SonusName")


# MODULE-IDENTITY

sonusRedundancyServicesMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 8)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_SonusRedundancyServicesMIBObjects_ObjectIdentity = ObjectIdentity
sonusRedundancyServicesMIBObjects = _SonusRedundancyServicesMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 8, 1)
)
_SonusRedundGroup_ObjectIdentity = ObjectIdentity
sonusRedundGroup = _SonusRedundGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 8, 1, 1)
)
_SonusRedundGroupNextIndex_Type = Integer32
_SonusRedundGroupNextIndex_Object = MibScalar
sonusRedundGroupNextIndex = _SonusRedundGroupNextIndex_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 8, 1, 1, 1),
    _SonusRedundGroupNextIndex_Type()
)
sonusRedundGroupNextIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusRedundGroupNextIndex.setStatus("current")
_SonusRedundGroupTable_Object = MibTable
sonusRedundGroupTable = _SonusRedundGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 8, 1, 1, 2)
)
if mibBuilder.loadTexts:
    sonusRedundGroupTable.setStatus("current")
_SonusRedundGroupEntry_Object = MibTableRow
sonusRedundGroupEntry = _SonusRedundGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 8, 1, 1, 2, 1)
)
sonusRedundGroupEntry.setIndexNames(
    (0, "SONUS-REDUNDANCY-SERVICES-MIB", "sonusRedundGroupAdmnIndex"),
)
if mibBuilder.loadTexts:
    sonusRedundGroupEntry.setStatus("current")
_SonusRedundGroupAdmnIndex_Type = Integer32
_SonusRedundGroupAdmnIndex_Object = MibTableColumn
sonusRedundGroupAdmnIndex = _SonusRedundGroupAdmnIndex_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 8, 1, 1, 2, 1, 1),
    _SonusRedundGroupAdmnIndex_Type()
)
sonusRedundGroupAdmnIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusRedundGroupAdmnIndex.setStatus("current")


class _SonusRedundGroupAdmnState_Type(Integer32):
    """Custom type sonusRedundGroupAdmnState based on Integer32"""
    defaultValue = 1

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


_SonusRedundGroupAdmnState_Type.__name__ = "Integer32"
_SonusRedundGroupAdmnState_Object = MibTableColumn
sonusRedundGroupAdmnState = _SonusRedundGroupAdmnState_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 8, 1, 1, 2, 1, 2),
    _SonusRedundGroupAdmnState_Type()
)
sonusRedundGroupAdmnState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusRedundGroupAdmnState.setStatus("current")
_SonusRedundGroupName_Type = SonusName
_SonusRedundGroupName_Object = MibTableColumn
sonusRedundGroupName = _SonusRedundGroupName_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 8, 1, 1, 2, 1, 3),
    _SonusRedundGroupName_Type()
)
sonusRedundGroupName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusRedundGroupName.setStatus("current")


class _SonusRedundGroupShelfIndex_Type(Integer32):
    """Custom type sonusRedundGroupShelfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 6),
    )


_SonusRedundGroupShelfIndex_Type.__name__ = "Integer32"
_SonusRedundGroupShelfIndex_Object = MibTableColumn
sonusRedundGroupShelfIndex = _SonusRedundGroupShelfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 8, 1, 1, 2, 1, 4),
    _SonusRedundGroupShelfIndex_Type()
)
sonusRedundGroupShelfIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusRedundGroupShelfIndex.setStatus("current")


class _SonusRedundGroupRedundSlotIndex_Type(Integer32):
    """Custom type sonusRedundGroupRedundSlotIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_SonusRedundGroupRedundSlotIndex_Type.__name__ = "Integer32"
_SonusRedundGroupRedundSlotIndex_Object = MibTableColumn
sonusRedundGroupRedundSlotIndex = _SonusRedundGroupRedundSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 8, 1, 1, 2, 1, 5),
    _SonusRedundGroupRedundSlotIndex_Type()
)
sonusRedundGroupRedundSlotIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusRedundGroupRedundSlotIndex.setStatus("current")


class _SonusRedundGroupSwitchoverCntrl_Type(Integer32):
    """Custom type sonusRedundGroupSwitchoverCntrl based on Integer32"""
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
        *(("forced", 3),
          ("none", 1),
          ("normal", 2),
          ("revert", 4),
          ("revertForced", 5))
    )


_SonusRedundGroupSwitchoverCntrl_Type.__name__ = "Integer32"
_SonusRedundGroupSwitchoverCntrl_Object = MibTableColumn
sonusRedundGroupSwitchoverCntrl = _SonusRedundGroupSwitchoverCntrl_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 8, 1, 1, 2, 1, 6),
    _SonusRedundGroupSwitchoverCntrl_Type()
)
sonusRedundGroupSwitchoverCntrl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusRedundGroupSwitchoverCntrl.setStatus("current")


class _SonusRedundGroupSwitchoverClientSlotIndex_Type(Integer32):
    """Custom type sonusRedundGroupSwitchoverClientSlotIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_SonusRedundGroupSwitchoverClientSlotIndex_Type.__name__ = "Integer32"
_SonusRedundGroupSwitchoverClientSlotIndex_Object = MibTableColumn
sonusRedundGroupSwitchoverClientSlotIndex = _SonusRedundGroupSwitchoverClientSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 8, 1, 1, 2, 1, 7),
    _SonusRedundGroupSwitchoverClientSlotIndex_Type()
)
sonusRedundGroupSwitchoverClientSlotIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusRedundGroupSwitchoverClientSlotIndex.setStatus("current")


class _SonusRedundGroupFallbackCntrl_Type(Integer32):
    """Custom type sonusRedundGroupFallbackCntrl based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("nonrevertive", 2),
          ("revertive", 1))
    )


_SonusRedundGroupFallbackCntrl_Type.__name__ = "Integer32"
_SonusRedundGroupFallbackCntrl_Object = MibTableColumn
sonusRedundGroupFallbackCntrl = _SonusRedundGroupFallbackCntrl_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 8, 1, 1, 2, 1, 8),
    _SonusRedundGroupFallbackCntrl_Type()
)
sonusRedundGroupFallbackCntrl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusRedundGroupFallbackCntrl.setStatus("current")


class _SonusRedundGroupWaitToRevertTime_Type(Integer32):
    """Custom type sonusRedundGroupWaitToRevertTime based on Integer32"""
    defaultValue = 5

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 12),
    )


_SonusRedundGroupWaitToRevertTime_Type.__name__ = "Integer32"
_SonusRedundGroupWaitToRevertTime_Object = MibTableColumn
sonusRedundGroupWaitToRevertTime = _SonusRedundGroupWaitToRevertTime_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 8, 1, 1, 2, 1, 9),
    _SonusRedundGroupWaitToRevertTime_Type()
)
sonusRedundGroupWaitToRevertTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusRedundGroupWaitToRevertTime.setStatus("current")


class _SonusRedundGroupAutoDetectCntrl_Type(Integer32):
    """Custom type sonusRedundGroupAutoDetectCntrl based on Integer32"""
    defaultValue = 1

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


_SonusRedundGroupAutoDetectCntrl_Type.__name__ = "Integer32"
_SonusRedundGroupAutoDetectCntrl_Object = MibTableColumn
sonusRedundGroupAutoDetectCntrl = _SonusRedundGroupAutoDetectCntrl_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 8, 1, 1, 2, 1, 10),
    _SonusRedundGroupAutoDetectCntrl_Type()
)
sonusRedundGroupAutoDetectCntrl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusRedundGroupAutoDetectCntrl.setStatus("current")
_SonusRedundGroupHwType_Type = ServerTypeID
_SonusRedundGroupHwType_Object = MibTableColumn
sonusRedundGroupHwType = _SonusRedundGroupHwType_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 8, 1, 1, 2, 1, 11),
    _SonusRedundGroupHwType_Type()
)
sonusRedundGroupHwType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusRedundGroupHwType.setStatus("current")


class _SonusRedundGroupHealthcheckCntrl_Type(Integer32):
    """Custom type sonusRedundGroupHealthcheckCntrl based on Integer32"""
    defaultValue = 2

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


_SonusRedundGroupHealthcheckCntrl_Type.__name__ = "Integer32"
_SonusRedundGroupHealthcheckCntrl_Object = MibTableColumn
sonusRedundGroupHealthcheckCntrl = _SonusRedundGroupHealthcheckCntrl_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 8, 1, 1, 2, 1, 12),
    _SonusRedundGroupHealthcheckCntrl_Type()
)
sonusRedundGroupHealthcheckCntrl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusRedundGroupHealthcheckCntrl.setStatus("current")
_SonusRedundGroupAdmnRowStatus_Type = RowStatus
_SonusRedundGroupAdmnRowStatus_Object = MibTableColumn
sonusRedundGroupAdmnRowStatus = _SonusRedundGroupAdmnRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 8, 1, 1, 2, 1, 13),
    _SonusRedundGroupAdmnRowStatus_Type()
)
sonusRedundGroupAdmnRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusRedundGroupAdmnRowStatus.setStatus("current")
_SonusRedundGroupSrvrFunction_Type = ServerFunctionType
_SonusRedundGroupSrvrFunction_Object = MibTableColumn
sonusRedundGroupSrvrFunction = _SonusRedundGroupSrvrFunction_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 8, 1, 1, 2, 1, 14),
    _SonusRedundGroupSrvrFunction_Type()
)
sonusRedundGroupSrvrFunction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusRedundGroupSrvrFunction.setStatus("current")
_SonusRedundClient_ObjectIdentity = ObjectIdentity
sonusRedundClient = _SonusRedundClient_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 8, 1, 2)
)
_SonusRedundClientNextIndex_Type = Integer32
_SonusRedundClientNextIndex_Object = MibScalar
sonusRedundClientNextIndex = _SonusRedundClientNextIndex_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 8, 1, 2, 1),
    _SonusRedundClientNextIndex_Type()
)
sonusRedundClientNextIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusRedundClientNextIndex.setStatus("current")
_SonusRedundClientTable_Object = MibTable
sonusRedundClientTable = _SonusRedundClientTable_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 8, 1, 2, 2)
)
if mibBuilder.loadTexts:
    sonusRedundClientTable.setStatus("current")
_SonusRedundClientEntry_Object = MibTableRow
sonusRedundClientEntry = _SonusRedundClientEntry_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 8, 1, 2, 2, 1)
)
sonusRedundClientEntry.setIndexNames(
    (0, "SONUS-REDUNDANCY-SERVICES-MIB", "sonusRedundClientAdmnGroupIndex"),
    (0, "SONUS-REDUNDANCY-SERVICES-MIB", "sonusRedundClientAdmnSlotIndex"),
)
if mibBuilder.loadTexts:
    sonusRedundClientEntry.setStatus("current")
_SonusRedundClientAdmnGroupIndex_Type = Integer32
_SonusRedundClientAdmnGroupIndex_Object = MibTableColumn
sonusRedundClientAdmnGroupIndex = _SonusRedundClientAdmnGroupIndex_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 8, 1, 2, 2, 1, 1),
    _SonusRedundClientAdmnGroupIndex_Type()
)
sonusRedundClientAdmnGroupIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusRedundClientAdmnGroupIndex.setStatus("current")


class _SonusRedundClientAdmnSlotIndex_Type(Integer32):
    """Custom type sonusRedundClientAdmnSlotIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_SonusRedundClientAdmnSlotIndex_Type.__name__ = "Integer32"
_SonusRedundClientAdmnSlotIndex_Object = MibTableColumn
sonusRedundClientAdmnSlotIndex = _SonusRedundClientAdmnSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 8, 1, 2, 2, 1, 2),
    _SonusRedundClientAdmnSlotIndex_Type()
)
sonusRedundClientAdmnSlotIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusRedundClientAdmnSlotIndex.setStatus("current")


class _SonusRedundClientAdmnState_Type(Integer32):
    """Custom type sonusRedundClientAdmnState based on Integer32"""
    defaultValue = 1

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


_SonusRedundClientAdmnState_Type.__name__ = "Integer32"
_SonusRedundClientAdmnState_Object = MibTableColumn
sonusRedundClientAdmnState = _SonusRedundClientAdmnState_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 8, 1, 2, 2, 1, 3),
    _SonusRedundClientAdmnState_Type()
)
sonusRedundClientAdmnState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusRedundClientAdmnState.setStatus("current")
_SonusRedundClientAdmnRowStatus_Type = RowStatus
_SonusRedundClientAdmnRowStatus_Object = MibTableColumn
sonusRedundClientAdmnRowStatus = _SonusRedundClientAdmnRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 8, 1, 2, 2, 1, 4),
    _SonusRedundClientAdmnRowStatus_Type()
)
sonusRedundClientAdmnRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusRedundClientAdmnRowStatus.setStatus("current")
_SonusRedundGroupStatTable_Object = MibTable
sonusRedundGroupStatTable = _SonusRedundGroupStatTable_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 8, 1, 3)
)
if mibBuilder.loadTexts:
    sonusRedundGroupStatTable.setStatus("current")
_SonusRedundGroupStatEntry_Object = MibTableRow
sonusRedundGroupStatEntry = _SonusRedundGroupStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 8, 1, 3, 1)
)
sonusRedundGroupStatEntry.setIndexNames(
    (0, "SONUS-REDUNDANCY-SERVICES-MIB", "sonusRedundGroupStatIndex"),
)
if mibBuilder.loadTexts:
    sonusRedundGroupStatEntry.setStatus("current")
_SonusRedundGroupStatIndex_Type = Integer32
_SonusRedundGroupStatIndex_Object = MibTableColumn
sonusRedundGroupStatIndex = _SonusRedundGroupStatIndex_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 8, 1, 3, 1, 1),
    _SonusRedundGroupStatIndex_Type()
)
sonusRedundGroupStatIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusRedundGroupStatIndex.setStatus("current")


class _SonusRedundGroupRedundOpState_Type(Integer32):
    """Custom type sonusRedundGroupRedundOpState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9)
        )
    )
    namedValues = NamedValues(
        *(("absent", 5),
          ("activeNotSynced", 4),
          ("activeSynced", 2),
          ("activeSyncing", 3),
          ("failed", 7),
          ("outOfService", 9),
          ("reset", 6),
          ("standby", 1),
          ("unknown", 8))
    )


_SonusRedundGroupRedundOpState_Type.__name__ = "Integer32"
_SonusRedundGroupRedundOpState_Object = MibTableColumn
sonusRedundGroupRedundOpState = _SonusRedundGroupRedundOpState_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 8, 1, 3, 1, 2),
    _SonusRedundGroupRedundOpState_Type()
)
sonusRedundGroupRedundOpState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusRedundGroupRedundOpState.setStatus("current")
_SonusRedundGroupStandbySlotIndex_Type = Integer32
_SonusRedundGroupStandbySlotIndex_Object = MibTableColumn
sonusRedundGroupStandbySlotIndex = _SonusRedundGroupStandbySlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 8, 1, 3, 1, 3),
    _SonusRedundGroupStandbySlotIndex_Type()
)
sonusRedundGroupStandbySlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusRedundGroupStandbySlotIndex.setStatus("current")
_SonusRedundGroupRedundSonicId_Type = Integer32
_SonusRedundGroupRedundSonicId_Object = MibTableColumn
sonusRedundGroupRedundSonicId = _SonusRedundGroupRedundSonicId_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 8, 1, 3, 1, 4),
    _SonusRedundGroupRedundSonicId_Type()
)
sonusRedundGroupRedundSonicId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusRedundGroupRedundSonicId.setStatus("current")
_SonusRedundGroupProtectedSlotIndex_Type = Integer32
_SonusRedundGroupProtectedSlotIndex_Object = MibTableColumn
sonusRedundGroupProtectedSlotIndex = _SonusRedundGroupProtectedSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 8, 1, 3, 1, 5),
    _SonusRedundGroupProtectedSlotIndex_Type()
)
sonusRedundGroupProtectedSlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusRedundGroupProtectedSlotIndex.setStatus("current")
_SonusRedundGroupNumClients_Type = Integer32
_SonusRedundGroupNumClients_Object = MibTableColumn
sonusRedundGroupNumClients = _SonusRedundGroupNumClients_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 8, 1, 3, 1, 6),
    _SonusRedundGroupNumClients_Type()
)
sonusRedundGroupNumClients.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusRedundGroupNumClients.setStatus("current")
_SonusRedundGroupNumSwitchovers_Type = Integer32
_SonusRedundGroupNumSwitchovers_Object = MibTableColumn
sonusRedundGroupNumSwitchovers = _SonusRedundGroupNumSwitchovers_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 8, 1, 3, 1, 7),
    _SonusRedundGroupNumSwitchovers_Type()
)
sonusRedundGroupNumSwitchovers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusRedundGroupNumSwitchovers.setStatus("current")


class _SonusRedundGroupLastSwitchoverReason_Type(Integer32):
    """Custom type sonusRedundGroupLastSwitchoverReason based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13)
        )
    )
    namedValues = NamedValues(
        *(("adminSwitchover", 2),
          ("autoReversion", 3),
          ("excessiveLinkFailure", 11),
          ("hardwareFailure", 7),
          ("healthCheckTimeout", 8),
          ("none", 1),
          ("other", 9),
          ("removal", 5),
          ("reserved2", 12),
          ("reset", 4),
          ("softwareFailure", 6),
          ("softwareUpgrade", 10),
          ("unknown", 13))
    )


_SonusRedundGroupLastSwitchoverReason_Type.__name__ = "Integer32"
_SonusRedundGroupLastSwitchoverReason_Object = MibTableColumn
sonusRedundGroupLastSwitchoverReason = _SonusRedundGroupLastSwitchoverReason_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 8, 1, 3, 1, 8),
    _SonusRedundGroupLastSwitchoverReason_Type()
)
sonusRedundGroupLastSwitchoverReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusRedundGroupLastSwitchoverReason.setStatus("current")
_SonusRedundClientStatTable_Object = MibTable
sonusRedundClientStatTable = _SonusRedundClientStatTable_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 8, 1, 4)
)
if mibBuilder.loadTexts:
    sonusRedundClientStatTable.setStatus("current")
_SonusRedundClientStatEntry_Object = MibTableRow
sonusRedundClientStatEntry = _SonusRedundClientStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 8, 1, 4, 1)
)
sonusRedundClientStatEntry.setIndexNames(
    (0, "SONUS-REDUNDANCY-SERVICES-MIB", "sonusRedundClientStatGroupIndex"),
    (0, "SONUS-REDUNDANCY-SERVICES-MIB", "sonusRedundClientStatSlotIndex"),
)
if mibBuilder.loadTexts:
    sonusRedundClientStatEntry.setStatus("current")
_SonusRedundClientStatGroupIndex_Type = Integer32
_SonusRedundClientStatGroupIndex_Object = MibTableColumn
sonusRedundClientStatGroupIndex = _SonusRedundClientStatGroupIndex_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 8, 1, 4, 1, 1),
    _SonusRedundClientStatGroupIndex_Type()
)
sonusRedundClientStatGroupIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusRedundClientStatGroupIndex.setStatus("current")


class _SonusRedundClientStatSlotIndex_Type(Integer32):
    """Custom type sonusRedundClientStatSlotIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_SonusRedundClientStatSlotIndex_Type.__name__ = "Integer32"
_SonusRedundClientStatSlotIndex_Object = MibTableColumn
sonusRedundClientStatSlotIndex = _SonusRedundClientStatSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 8, 1, 4, 1, 2),
    _SonusRedundClientStatSlotIndex_Type()
)
sonusRedundClientStatSlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusRedundClientStatSlotIndex.setStatus("current")
_SonusRedundClientSonicId_Type = Integer32
_SonusRedundClientSonicId_Object = MibTableColumn
sonusRedundClientSonicId = _SonusRedundClientSonicId_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 8, 1, 4, 1, 3),
    _SonusRedundClientSonicId_Type()
)
sonusRedundClientSonicId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusRedundClientSonicId.setStatus("current")


class _SonusRedundClientState_Type(Integer32):
    """Custom type sonusRedundClientState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9)
        )
    )
    namedValues = NamedValues(
        *(("absent", 5),
          ("activeNotSynced", 4),
          ("activeSynced", 2),
          ("activeSyncing", 3),
          ("failed", 7),
          ("outOfService", 9),
          ("reset", 6),
          ("standby", 1),
          ("unknown", 8))
    )


_SonusRedundClientState_Type.__name__ = "Integer32"
_SonusRedundClientState_Object = MibTableColumn
sonusRedundClientState = _SonusRedundClientState_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 8, 1, 4, 1, 4),
    _SonusRedundClientState_Type()
)
sonusRedundClientState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusRedundClientState.setStatus("current")
_SonusRedundancyServicesMIBNotifications_ObjectIdentity = ObjectIdentity
sonusRedundancyServicesMIBNotifications = _SonusRedundancyServicesMIBNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 8, 2)
)
_SonusRedundancyServicesMIBNotificationsPrefix_ObjectIdentity = ObjectIdentity
sonusRedundancyServicesMIBNotificationsPrefix = _SonusRedundancyServicesMIBNotificationsPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 8, 2, 0)
)
_SonusRedundancyServicesMIBNotificationsObjects_ObjectIdentity = ObjectIdentity
sonusRedundancyServicesMIBNotificationsObjects = _SonusRedundancyServicesMIBNotificationsObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 8, 2, 1)
)


class _SonusRedundPrevActiveSlotIndex_Type(Integer32):
    """Custom type sonusRedundPrevActiveSlotIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_SonusRedundPrevActiveSlotIndex_Type.__name__ = "Integer32"
_SonusRedundPrevActiveSlotIndex_Object = MibScalar
sonusRedundPrevActiveSlotIndex = _SonusRedundPrevActiveSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 8, 2, 1, 1),
    _SonusRedundPrevActiveSlotIndex_Type()
)
sonusRedundPrevActiveSlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusRedundPrevActiveSlotIndex.setStatus("current")

# Managed Objects groups


# Notification objects

sonusRedundGroupSwitchOverNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 8, 2, 0, 1)
)
sonusRedundGroupSwitchOverNotification.setObjects(
      *(("SONUS-COMMON-MIB", "sonusShelfIndex"),
        ("SONUS-COMMON-MIB", "sonusSlotIndex"),
        ("SONUS-REDUNDANCY-SERVICES-MIB", "sonusRedundPrevActiveSlotIndex"),
        ("SONUS-REDUNDANCY-SERVICES-MIB", "sonusRedundGroupLastSwitchoverReason"),
        ("SONUS-REDUNDANCY-SERVICES-MIB", "sonusRedundGroupName"),
        ("SONUS-REDUNDANCY-SERVICES-MIB", "sonusRedundGroupAdmnIndex"),
        ("SONUS-COMMON-MIB", "sonusEventDescription"),
        ("SONUS-COMMON-MIB", "sonusEventClass"),
        ("SONUS-COMMON-MIB", "sonusEventLevel"))
)
if mibBuilder.loadTexts:
    sonusRedundGroupSwitchOverNotification.setStatus(
        "current"
    )

sonusRedundGroupNoRedundancyNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 8, 2, 0, 2)
)
sonusRedundGroupNoRedundancyNotification.setObjects(
      *(("SONUS-REDUNDANCY-SERVICES-MIB", "sonusRedundGroupName"),
        ("SONUS-REDUNDANCY-SERVICES-MIB", "sonusRedundGroupAdmnIndex"),
        ("SONUS-COMMON-MIB", "sonusEventDescription"),
        ("SONUS-COMMON-MIB", "sonusEventClass"),
        ("SONUS-COMMON-MIB", "sonusEventLevel"))
)
if mibBuilder.loadTexts:
    sonusRedundGroupNoRedundancyNotification.setStatus(
        "current"
    )

sonusRedundGroupFullRedundancyNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 8, 2, 0, 3)
)
sonusRedundGroupFullRedundancyNotification.setObjects(
      *(("SONUS-REDUNDANCY-SERVICES-MIB", "sonusRedundGroupName"),
        ("SONUS-REDUNDANCY-SERVICES-MIB", "sonusRedundGroupAdmnIndex"),
        ("SONUS-COMMON-MIB", "sonusEventDescription"),
        ("SONUS-COMMON-MIB", "sonusEventClass"),
        ("SONUS-COMMON-MIB", "sonusEventLevel"))
)
if mibBuilder.loadTexts:
    sonusRedundGroupFullRedundancyNotification.setStatus(
        "current"
    )

sonusRedundGroupProtectedClientRestored = NotificationType(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 8, 2, 0, 4)
)
sonusRedundGroupProtectedClientRestored.setObjects(
      *(("SONUS-COMMON-MIB", "sonusShelfIndex"),
        ("SONUS-COMMON-MIB", "sonusSlotIndex"),
        ("SONUS-REDUNDANCY-SERVICES-MIB", "sonusRedundGroupName"),
        ("SONUS-REDUNDANCY-SERVICES-MIB", "sonusRedundGroupAdmnIndex"),
        ("SONUS-COMMON-MIB", "sonusEventDescription"),
        ("SONUS-COMMON-MIB", "sonusEventClass"),
        ("SONUS-COMMON-MIB", "sonusEventLevel"))
)
if mibBuilder.loadTexts:
    sonusRedundGroupProtectedClientRestored.setStatus(
        "current"
    )

sonusRedundGroupMnsActiveNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 8, 2, 0, 5)
)
sonusRedundGroupMnsActiveNotification.setObjects(
      *(("SONUS-COMMON-MIB", "sonusShelfIndex"),
        ("SONUS-COMMON-MIB", "sonusSlotIndex"),
        ("SONUS-COMMON-MIB", "sonusEventDescription"),
        ("SONUS-COMMON-MIB", "sonusEventClass"),
        ("SONUS-COMMON-MIB", "sonusEventLevel"))
)
if mibBuilder.loadTexts:
    sonusRedundGroupMnsActiveNotification.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SONUS-REDUNDANCY-SERVICES-MIB",
    **{"sonusRedundancyServicesMIB": sonusRedundancyServicesMIB,
       "sonusRedundancyServicesMIBObjects": sonusRedundancyServicesMIBObjects,
       "sonusRedundGroup": sonusRedundGroup,
       "sonusRedundGroupNextIndex": sonusRedundGroupNextIndex,
       "sonusRedundGroupTable": sonusRedundGroupTable,
       "sonusRedundGroupEntry": sonusRedundGroupEntry,
       "sonusRedundGroupAdmnIndex": sonusRedundGroupAdmnIndex,
       "sonusRedundGroupAdmnState": sonusRedundGroupAdmnState,
       "sonusRedundGroupName": sonusRedundGroupName,
       "sonusRedundGroupShelfIndex": sonusRedundGroupShelfIndex,
       "sonusRedundGroupRedundSlotIndex": sonusRedundGroupRedundSlotIndex,
       "sonusRedundGroupSwitchoverCntrl": sonusRedundGroupSwitchoverCntrl,
       "sonusRedundGroupSwitchoverClientSlotIndex": sonusRedundGroupSwitchoverClientSlotIndex,
       "sonusRedundGroupFallbackCntrl": sonusRedundGroupFallbackCntrl,
       "sonusRedundGroupWaitToRevertTime": sonusRedundGroupWaitToRevertTime,
       "sonusRedundGroupAutoDetectCntrl": sonusRedundGroupAutoDetectCntrl,
       "sonusRedundGroupHwType": sonusRedundGroupHwType,
       "sonusRedundGroupHealthcheckCntrl": sonusRedundGroupHealthcheckCntrl,
       "sonusRedundGroupAdmnRowStatus": sonusRedundGroupAdmnRowStatus,
       "sonusRedundGroupSrvrFunction": sonusRedundGroupSrvrFunction,
       "sonusRedundClient": sonusRedundClient,
       "sonusRedundClientNextIndex": sonusRedundClientNextIndex,
       "sonusRedundClientTable": sonusRedundClientTable,
       "sonusRedundClientEntry": sonusRedundClientEntry,
       "sonusRedundClientAdmnGroupIndex": sonusRedundClientAdmnGroupIndex,
       "sonusRedundClientAdmnSlotIndex": sonusRedundClientAdmnSlotIndex,
       "sonusRedundClientAdmnState": sonusRedundClientAdmnState,
       "sonusRedundClientAdmnRowStatus": sonusRedundClientAdmnRowStatus,
       "sonusRedundGroupStatTable": sonusRedundGroupStatTable,
       "sonusRedundGroupStatEntry": sonusRedundGroupStatEntry,
       "sonusRedundGroupStatIndex": sonusRedundGroupStatIndex,
       "sonusRedundGroupRedundOpState": sonusRedundGroupRedundOpState,
       "sonusRedundGroupStandbySlotIndex": sonusRedundGroupStandbySlotIndex,
       "sonusRedundGroupRedundSonicId": sonusRedundGroupRedundSonicId,
       "sonusRedundGroupProtectedSlotIndex": sonusRedundGroupProtectedSlotIndex,
       "sonusRedundGroupNumClients": sonusRedundGroupNumClients,
       "sonusRedundGroupNumSwitchovers": sonusRedundGroupNumSwitchovers,
       "sonusRedundGroupLastSwitchoverReason": sonusRedundGroupLastSwitchoverReason,
       "sonusRedundClientStatTable": sonusRedundClientStatTable,
       "sonusRedundClientStatEntry": sonusRedundClientStatEntry,
       "sonusRedundClientStatGroupIndex": sonusRedundClientStatGroupIndex,
       "sonusRedundClientStatSlotIndex": sonusRedundClientStatSlotIndex,
       "sonusRedundClientSonicId": sonusRedundClientSonicId,
       "sonusRedundClientState": sonusRedundClientState,
       "sonusRedundancyServicesMIBNotifications": sonusRedundancyServicesMIBNotifications,
       "sonusRedundancyServicesMIBNotificationsPrefix": sonusRedundancyServicesMIBNotificationsPrefix,
       "sonusRedundGroupSwitchOverNotification": sonusRedundGroupSwitchOverNotification,
       "sonusRedundGroupNoRedundancyNotification": sonusRedundGroupNoRedundancyNotification,
       "sonusRedundGroupFullRedundancyNotification": sonusRedundGroupFullRedundancyNotification,
       "sonusRedundGroupProtectedClientRestored": sonusRedundGroupProtectedClientRestored,
       "sonusRedundGroupMnsActiveNotification": sonusRedundGroupMnsActiveNotification,
       "sonusRedundancyServicesMIBNotificationsObjects": sonusRedundancyServicesMIBNotificationsObjects,
       "sonusRedundPrevActiveSlotIndex": sonusRedundPrevActiveSlotIndex}
)
