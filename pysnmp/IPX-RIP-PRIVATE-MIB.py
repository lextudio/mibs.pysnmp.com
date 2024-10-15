# SNMP MIB module (IPX-RIP-PRIVATE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/IPX-RIP-PRIVATE-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:11:36 2024
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

(cjnProtocol,) = mibBuilder.importSymbols(
    "Cajun-ROOT",
    "cjnProtocol")

(cjnIpxIfIndex,) = mibBuilder.importSymbols(
    "IPX-INTERFACE-MANAGEMENT-PRIVATE-MIB",
    "cjnIpxIfIndex")

(NetNumber,) = mibBuilder.importSymbols(
    "IPX-PRIVATE-MIB",
    "NetNumber")

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


# MODULE-IDENTITY

cjnIpxRip = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 20)
)


# Types definitions



class FilterPrec(Integer32):
    """Custom type FilterPrec based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 9999),
    )




# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CjnIpxRipGlobalGroup_ObjectIdentity = ObjectIdentity
cjnIpxRipGlobalGroup = _CjnIpxRipGlobalGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 20, 1)
)


class _CjnIpxRipEnabled_Type(Integer32):
    """Custom type cjnIpxRipEnabled based on Integer32"""
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


_CjnIpxRipEnabled_Type.__name__ = "Integer32"
_CjnIpxRipEnabled_Object = MibScalar
cjnIpxRipEnabled = _CjnIpxRipEnabled_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 20, 1, 1),
    _CjnIpxRipEnabled_Type()
)
cjnIpxRipEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cjnIpxRipEnabled.setStatus("current")
_CjnIpxRipFilterGroup_ObjectIdentity = ObjectIdentity
cjnIpxRipFilterGroup = _CjnIpxRipFilterGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 20, 2)
)
_CjnIpxRipFilterTable_Object = MibTable
cjnIpxRipFilterTable = _CjnIpxRipFilterTable_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 20, 2, 1)
)
if mibBuilder.loadTexts:
    cjnIpxRipFilterTable.setStatus("current")
_CjnIpxRipFilterEntry_Object = MibTableRow
cjnIpxRipFilterEntry = _CjnIpxRipFilterEntry_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 20, 2, 1, 1)
)
cjnIpxRipFilterEntry.setIndexNames(
    (0, "IPX-INTERFACE-MANAGEMENT-PRIVATE-MIB", "cjnIpxIfIndex"),
    (0, "IPX-RIP-PRIVATE-MIB", "cjnIpxRipFilterPrec"),
)
if mibBuilder.loadTexts:
    cjnIpxRipFilterEntry.setStatus("current")
_CjnIpxRipFilterPrec_Type = FilterPrec
_CjnIpxRipFilterPrec_Object = MibTableColumn
cjnIpxRipFilterPrec = _CjnIpxRipFilterPrec_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 20, 2, 1, 1, 1),
    _CjnIpxRipFilterPrec_Type()
)
cjnIpxRipFilterPrec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cjnIpxRipFilterPrec.setStatus("current")
_CjnIpxRipFilterRowStatus_Type = RowStatus
_CjnIpxRipFilterRowStatus_Object = MibTableColumn
cjnIpxRipFilterRowStatus = _CjnIpxRipFilterRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 20, 2, 1, 1, 2),
    _CjnIpxRipFilterRowStatus_Type()
)
cjnIpxRipFilterRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cjnIpxRipFilterRowStatus.setStatus("current")
_CjnIpxRipFilterNetStart_Type = NetNumber
_CjnIpxRipFilterNetStart_Object = MibTableColumn
cjnIpxRipFilterNetStart = _CjnIpxRipFilterNetStart_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 20, 2, 1, 1, 3),
    _CjnIpxRipFilterNetStart_Type()
)
cjnIpxRipFilterNetStart.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cjnIpxRipFilterNetStart.setStatus("current")
_CjnIpxRipFilterNetEnd_Type = NetNumber
_CjnIpxRipFilterNetEnd_Object = MibTableColumn
cjnIpxRipFilterNetEnd = _CjnIpxRipFilterNetEnd_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 20, 2, 1, 1, 4),
    _CjnIpxRipFilterNetEnd_Type()
)
cjnIpxRipFilterNetEnd.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cjnIpxRipFilterNetEnd.setStatus("current")


class _CjnIpxRipFilterDirection_Type(Integer32):
    """Custom type cjnIpxRipFilterDirection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("both", 3),
          ("inbound", 1),
          ("outbound", 2))
    )


_CjnIpxRipFilterDirection_Type.__name__ = "Integer32"
_CjnIpxRipFilterDirection_Object = MibTableColumn
cjnIpxRipFilterDirection = _CjnIpxRipFilterDirection_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 20, 2, 1, 1, 5),
    _CjnIpxRipFilterDirection_Type()
)
cjnIpxRipFilterDirection.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cjnIpxRipFilterDirection.setStatus("current")


class _CjnIpxRipFilterAction_Type(Integer32):
    """Custom type cjnIpxRipFilterAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("allow", 2),
          ("filter", 1))
    )


_CjnIpxRipFilterAction_Type.__name__ = "Integer32"
_CjnIpxRipFilterAction_Object = MibTableColumn
cjnIpxRipFilterAction = _CjnIpxRipFilterAction_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 20, 2, 1, 1, 6),
    _CjnIpxRipFilterAction_Type()
)
cjnIpxRipFilterAction.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cjnIpxRipFilterAction.setStatus("current")
_CjnIpxRipFilterTicks_Type = Integer32
_CjnIpxRipFilterTicks_Object = MibTableColumn
cjnIpxRipFilterTicks = _CjnIpxRipFilterTicks_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 20, 2, 1, 1, 7),
    _CjnIpxRipFilterTicks_Type()
)
cjnIpxRipFilterTicks.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cjnIpxRipFilterTicks.setStatus("current")
_CjnIpxRipFilterHops_Type = Integer32
_CjnIpxRipFilterHops_Object = MibTableColumn
cjnIpxRipFilterHops = _CjnIpxRipFilterHops_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 20, 2, 1, 1, 8),
    _CjnIpxRipFilterHops_Type()
)
cjnIpxRipFilterHops.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cjnIpxRipFilterHops.setStatus("current")
_CjnIpxRipIfGroup_ObjectIdentity = ObjectIdentity
cjnIpxRipIfGroup = _CjnIpxRipIfGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 20, 3)
)
_CjnIpxRipIfTable_Object = MibTable
cjnIpxRipIfTable = _CjnIpxRipIfTable_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 20, 3, 1)
)
if mibBuilder.loadTexts:
    cjnIpxRipIfTable.setStatus("current")
_CjnIpxRipIfEntry_Object = MibTableRow
cjnIpxRipIfEntry = _CjnIpxRipIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 20, 3, 1, 1)
)
cjnIpxRipIfEntry.setIndexNames(
    (0, "IPX-INTERFACE-MANAGEMENT-PRIVATE-MIB", "cjnIpxIfIndex"),
)
if mibBuilder.loadTexts:
    cjnIpxRipIfEntry.setStatus("current")
_CjnIpxRipIfRowStatus_Type = RowStatus
_CjnIpxRipIfRowStatus_Object = MibTableColumn
cjnIpxRipIfRowStatus = _CjnIpxRipIfRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 20, 3, 1, 1, 1),
    _CjnIpxRipIfRowStatus_Type()
)
cjnIpxRipIfRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cjnIpxRipIfRowStatus.setStatus("current")


class _CjnIpxRipIfInterpacketGap_Type(Integer32):
    """Custom type cjnIpxRipIfInterpacketGap based on Integer32"""
    defaultValue = 1

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


_CjnIpxRipIfInterpacketGap_Type.__name__ = "Integer32"
_CjnIpxRipIfInterpacketGap_Object = MibTableColumn
cjnIpxRipIfInterpacketGap = _CjnIpxRipIfInterpacketGap_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 20, 3, 1, 1, 2),
    _CjnIpxRipIfInterpacketGap_Type()
)
cjnIpxRipIfInterpacketGap.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cjnIpxRipIfInterpacketGap.setStatus("current")


class _CjnIpxRipIfUseMaximumPacketSize_Type(Integer32):
    """Custom type cjnIpxRipIfUseMaximumPacketSize based on Integer32"""
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


_CjnIpxRipIfUseMaximumPacketSize_Type.__name__ = "Integer32"
_CjnIpxRipIfUseMaximumPacketSize_Object = MibTableColumn
cjnIpxRipIfUseMaximumPacketSize = _CjnIpxRipIfUseMaximumPacketSize_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 20, 3, 1, 1, 3),
    _CjnIpxRipIfUseMaximumPacketSize_Type()
)
cjnIpxRipIfUseMaximumPacketSize.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cjnIpxRipIfUseMaximumPacketSize.setStatus("current")


class _CjnIpxRipIfUpdateInterval_Type(Integer32):
    """Custom type cjnIpxRipIfUpdateInterval based on Integer32"""
    defaultValue = 60


_CjnIpxRipIfUpdateInterval_Object = MibTableColumn
cjnIpxRipIfUpdateInterval = _CjnIpxRipIfUpdateInterval_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 20, 3, 1, 1, 4),
    _CjnIpxRipIfUpdateInterval_Type()
)
cjnIpxRipIfUpdateInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cjnIpxRipIfUpdateInterval.setStatus("current")


class _CjnIpxRipIfAgeMultiplier_Type(Integer32):
    """Custom type cjnIpxRipIfAgeMultiplier based on Integer32"""
    defaultValue = 3


_CjnIpxRipIfAgeMultiplier_Object = MibTableColumn
cjnIpxRipIfAgeMultiplier = _CjnIpxRipIfAgeMultiplier_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 20, 3, 1, 1, 5),
    _CjnIpxRipIfAgeMultiplier_Type()
)
cjnIpxRipIfAgeMultiplier.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cjnIpxRipIfAgeMultiplier.setStatus("current")


class _CjnIpxRipIfTriggeredUpdates_Type(Integer32):
    """Custom type cjnIpxRipIfTriggeredUpdates based on Integer32"""
    defaultValue = 1

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


_CjnIpxRipIfTriggeredUpdates_Type.__name__ = "Integer32"
_CjnIpxRipIfTriggeredUpdates_Object = MibTableColumn
cjnIpxRipIfTriggeredUpdates = _CjnIpxRipIfTriggeredUpdates_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 20, 3, 1, 1, 6),
    _CjnIpxRipIfTriggeredUpdates_Type()
)
cjnIpxRipIfTriggeredUpdates.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cjnIpxRipIfTriggeredUpdates.setStatus("current")


class _CjnIpxRipIfAdvertiseDefaultRouteOnly_Type(Integer32):
    """Custom type cjnIpxRipIfAdvertiseDefaultRouteOnly based on Integer32"""
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


_CjnIpxRipIfAdvertiseDefaultRouteOnly_Type.__name__ = "Integer32"
_CjnIpxRipIfAdvertiseDefaultRouteOnly_Object = MibTableColumn
cjnIpxRipIfAdvertiseDefaultRouteOnly = _CjnIpxRipIfAdvertiseDefaultRouteOnly_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 20, 3, 1, 1, 7),
    _CjnIpxRipIfAdvertiseDefaultRouteOnly_Type()
)
cjnIpxRipIfAdvertiseDefaultRouteOnly.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cjnIpxRipIfAdvertiseDefaultRouteOnly.setStatus("current")


class _CjnIpxRipIfMode_Type(Integer32):
    """Custom type cjnIpxRipIfMode based on Integer32"""
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
        *(("both", 3),
          ("listen", 2),
          ("talk", 1))
    )


_CjnIpxRipIfMode_Type.__name__ = "Integer32"
_CjnIpxRipIfMode_Object = MibTableColumn
cjnIpxRipIfMode = _CjnIpxRipIfMode_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 20, 3, 1, 1, 8),
    _CjnIpxRipIfMode_Type()
)
cjnIpxRipIfMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cjnIpxRipIfMode.setStatus("current")
_CjnIpxRipIfStatGroup_ObjectIdentity = ObjectIdentity
cjnIpxRipIfStatGroup = _CjnIpxRipIfStatGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 20, 4)
)
_CjnIpxRipIfStatTable_Object = MibTable
cjnIpxRipIfStatTable = _CjnIpxRipIfStatTable_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 20, 4, 1)
)
if mibBuilder.loadTexts:
    cjnIpxRipIfStatTable.setStatus("current")
_CjnIpxRipIfStatEntry_Object = MibTableRow
cjnIpxRipIfStatEntry = _CjnIpxRipIfStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 20, 4, 1, 1)
)
cjnIpxRipIfStatEntry.setIndexNames(
    (0, "IPX-INTERFACE-MANAGEMENT-PRIVATE-MIB", "cjnIpxIfIndex"),
)
if mibBuilder.loadTexts:
    cjnIpxRipIfStatEntry.setStatus("current")
_CjnIpxRipIfStatTriggeredUpdatesSent_Type = Counter32
_CjnIpxRipIfStatTriggeredUpdatesSent_Object = MibTableColumn
cjnIpxRipIfStatTriggeredUpdatesSent = _CjnIpxRipIfStatTriggeredUpdatesSent_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 20, 4, 1, 1, 1),
    _CjnIpxRipIfStatTriggeredUpdatesSent_Type()
)
cjnIpxRipIfStatTriggeredUpdatesSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cjnIpxRipIfStatTriggeredUpdatesSent.setStatus("current")
_CjnIpxRipIfStatPeriodicUpdatesSent_Type = Counter32
_CjnIpxRipIfStatPeriodicUpdatesSent_Object = MibTableColumn
cjnIpxRipIfStatPeriodicUpdatesSent = _CjnIpxRipIfStatPeriodicUpdatesSent_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 20, 4, 1, 1, 2),
    _CjnIpxRipIfStatPeriodicUpdatesSent_Type()
)
cjnIpxRipIfStatPeriodicUpdatesSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cjnIpxRipIfStatPeriodicUpdatesSent.setStatus("current")
_CjnIpxRipIfStatUpdatesReceived_Type = Counter32
_CjnIpxRipIfStatUpdatesReceived_Object = MibTableColumn
cjnIpxRipIfStatUpdatesReceived = _CjnIpxRipIfStatUpdatesReceived_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 20, 4, 1, 1, 3),
    _CjnIpxRipIfStatUpdatesReceived_Type()
)
cjnIpxRipIfStatUpdatesReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cjnIpxRipIfStatUpdatesReceived.setStatus("current")
_CjnIpxRipIfStatRequestsReceived_Type = Counter32
_CjnIpxRipIfStatRequestsReceived_Object = MibTableColumn
cjnIpxRipIfStatRequestsReceived = _CjnIpxRipIfStatRequestsReceived_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 20, 4, 1, 1, 4),
    _CjnIpxRipIfStatRequestsReceived_Type()
)
cjnIpxRipIfStatRequestsReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cjnIpxRipIfStatRequestsReceived.setStatus("current")
_CjnIpxRipIfStatBadPacketsReceived_Type = Counter32
_CjnIpxRipIfStatBadPacketsReceived_Object = MibTableColumn
cjnIpxRipIfStatBadPacketsReceived = _CjnIpxRipIfStatBadPacketsReceived_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 20, 4, 1, 1, 5),
    _CjnIpxRipIfStatBadPacketsReceived_Type()
)
cjnIpxRipIfStatBadPacketsReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cjnIpxRipIfStatBadPacketsReceived.setStatus("current")


class _CjnIpxRipIfStatsReset_Type(Integer32):
    """Custom type cjnIpxRipIfStatsReset based on Integer32"""
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


_CjnIpxRipIfStatsReset_Type.__name__ = "Integer32"
_CjnIpxRipIfStatsReset_Object = MibScalar
cjnIpxRipIfStatsReset = _CjnIpxRipIfStatsReset_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 20, 4, 1, 1, 6),
    _CjnIpxRipIfStatsReset_Type()
)
cjnIpxRipIfStatsReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cjnIpxRipIfStatsReset.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "IPX-RIP-PRIVATE-MIB",
    **{"FilterPrec": FilterPrec,
       "cjnIpxRip": cjnIpxRip,
       "cjnIpxRipGlobalGroup": cjnIpxRipGlobalGroup,
       "cjnIpxRipEnabled": cjnIpxRipEnabled,
       "cjnIpxRipFilterGroup": cjnIpxRipFilterGroup,
       "cjnIpxRipFilterTable": cjnIpxRipFilterTable,
       "cjnIpxRipFilterEntry": cjnIpxRipFilterEntry,
       "cjnIpxRipFilterPrec": cjnIpxRipFilterPrec,
       "cjnIpxRipFilterRowStatus": cjnIpxRipFilterRowStatus,
       "cjnIpxRipFilterNetStart": cjnIpxRipFilterNetStart,
       "cjnIpxRipFilterNetEnd": cjnIpxRipFilterNetEnd,
       "cjnIpxRipFilterDirection": cjnIpxRipFilterDirection,
       "cjnIpxRipFilterAction": cjnIpxRipFilterAction,
       "cjnIpxRipFilterTicks": cjnIpxRipFilterTicks,
       "cjnIpxRipFilterHops": cjnIpxRipFilterHops,
       "cjnIpxRipIfGroup": cjnIpxRipIfGroup,
       "cjnIpxRipIfTable": cjnIpxRipIfTable,
       "cjnIpxRipIfEntry": cjnIpxRipIfEntry,
       "cjnIpxRipIfRowStatus": cjnIpxRipIfRowStatus,
       "cjnIpxRipIfInterpacketGap": cjnIpxRipIfInterpacketGap,
       "cjnIpxRipIfUseMaximumPacketSize": cjnIpxRipIfUseMaximumPacketSize,
       "cjnIpxRipIfUpdateInterval": cjnIpxRipIfUpdateInterval,
       "cjnIpxRipIfAgeMultiplier": cjnIpxRipIfAgeMultiplier,
       "cjnIpxRipIfTriggeredUpdates": cjnIpxRipIfTriggeredUpdates,
       "cjnIpxRipIfAdvertiseDefaultRouteOnly": cjnIpxRipIfAdvertiseDefaultRouteOnly,
       "cjnIpxRipIfMode": cjnIpxRipIfMode,
       "cjnIpxRipIfStatGroup": cjnIpxRipIfStatGroup,
       "cjnIpxRipIfStatTable": cjnIpxRipIfStatTable,
       "cjnIpxRipIfStatEntry": cjnIpxRipIfStatEntry,
       "cjnIpxRipIfStatTriggeredUpdatesSent": cjnIpxRipIfStatTriggeredUpdatesSent,
       "cjnIpxRipIfStatPeriodicUpdatesSent": cjnIpxRipIfStatPeriodicUpdatesSent,
       "cjnIpxRipIfStatUpdatesReceived": cjnIpxRipIfStatUpdatesReceived,
       "cjnIpxRipIfStatRequestsReceived": cjnIpxRipIfStatRequestsReceived,
       "cjnIpxRipIfStatBadPacketsReceived": cjnIpxRipIfStatBadPacketsReceived,
       "cjnIpxRipIfStatsReset": cjnIpxRipIfStatsReset}
)
