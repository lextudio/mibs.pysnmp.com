# SNMP MIB module (Wellfleet-RIP6-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/Wellfleet-RIP6-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:17:01 2024
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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")

(wfIpv6PolicyGroup,
 wfIpv6RoutingGroup) = mibBuilder.importSymbols(
    "Wellfleet-IPV6-MIB",
    "wfIpv6PolicyGroup",
    "wfIpv6RoutingGroup")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_WfRipv6Group_ObjectIdentity = ObjectIdentity
wfRipv6Group = _WfRipv6Group_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 16, 1, 2)
)
_WfRipv6IfTable_Object = MibTable
wfRipv6IfTable = _WfRipv6IfTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 16, 1, 2, 1)
)
if mibBuilder.loadTexts:
    wfRipv6IfTable.setStatus("mandatory")
_WfRipv6IfEntry_Object = MibTableRow
wfRipv6IfEntry = _WfRipv6IfEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 16, 1, 2, 1, 1)
)
wfRipv6IfEntry.setIndexNames(
    (0, "Wellfleet-RIP6-MIB", "wfRipv6IntfIndex"),
)
if mibBuilder.loadTexts:
    wfRipv6IfEntry.setStatus("mandatory")


class _WfRipv6IntfCreate_Type(Integer32):
    """Custom type wfRipv6IntfCreate based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("created", 1),
          ("deleted", 2))
    )


_WfRipv6IntfCreate_Type.__name__ = "Integer32"
_WfRipv6IntfCreate_Object = MibTableColumn
wfRipv6IntfCreate = _WfRipv6IntfCreate_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 16, 1, 2, 1, 1, 1),
    _WfRipv6IntfCreate_Type()
)
wfRipv6IntfCreate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfRipv6IntfCreate.setStatus("mandatory")


class _WfRipv6IntfEnable_Type(Integer32):
    """Custom type wfRipv6IntfEnable based on Integer32"""
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


_WfRipv6IntfEnable_Type.__name__ = "Integer32"
_WfRipv6IntfEnable_Object = MibTableColumn
wfRipv6IntfEnable = _WfRipv6IntfEnable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 16, 1, 2, 1, 1, 2),
    _WfRipv6IntfEnable_Type()
)
wfRipv6IntfEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfRipv6IntfEnable.setStatus("mandatory")


class _WfRipv6IntfState_Type(Integer32):
    """Custom type wfRipv6IntfState based on Integer32"""
    defaultValue = 2

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


_WfRipv6IntfState_Type.__name__ = "Integer32"
_WfRipv6IntfState_Object = MibTableColumn
wfRipv6IntfState = _WfRipv6IntfState_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 16, 1, 2, 1, 1, 3),
    _WfRipv6IntfState_Type()
)
wfRipv6IntfState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfRipv6IntfState.setStatus("mandatory")
_WfRipv6IntfIndex_Type = Integer32
_WfRipv6IntfIndex_Object = MibTableColumn
wfRipv6IntfIndex = _WfRipv6IntfIndex_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 16, 1, 2, 1, 1, 4),
    _WfRipv6IntfIndex_Type()
)
wfRipv6IntfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfRipv6IntfIndex.setStatus("mandatory")


class _WfRipv6IntfSupply_Type(Integer32):
    """Custom type wfRipv6IntfSupply based on Integer32"""
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


_WfRipv6IntfSupply_Type.__name__ = "Integer32"
_WfRipv6IntfSupply_Object = MibTableColumn
wfRipv6IntfSupply = _WfRipv6IntfSupply_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 16, 1, 2, 1, 1, 5),
    _WfRipv6IntfSupply_Type()
)
wfRipv6IntfSupply.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfRipv6IntfSupply.setStatus("mandatory")


class _WfRipv6IntfListen_Type(Integer32):
    """Custom type wfRipv6IntfListen based on Integer32"""
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


_WfRipv6IntfListen_Type.__name__ = "Integer32"
_WfRipv6IntfListen_Object = MibTableColumn
wfRipv6IntfListen = _WfRipv6IntfListen_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 16, 1, 2, 1, 1, 6),
    _WfRipv6IntfListen_Type()
)
wfRipv6IntfListen.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfRipv6IntfListen.setStatus("mandatory")


class _WfRipv6IntfDefaultRouteSupply_Type(Integer32):
    """Custom type wfRipv6IntfDefaultRouteSupply based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1),
          ("generated", 3))
    )


_WfRipv6IntfDefaultRouteSupply_Type.__name__ = "Integer32"
_WfRipv6IntfDefaultRouteSupply_Object = MibTableColumn
wfRipv6IntfDefaultRouteSupply = _WfRipv6IntfDefaultRouteSupply_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 16, 1, 2, 1, 1, 7),
    _WfRipv6IntfDefaultRouteSupply_Type()
)
wfRipv6IntfDefaultRouteSupply.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfRipv6IntfDefaultRouteSupply.setStatus("mandatory")


class _WfRipv6IntfDefaultRouteListen_Type(Integer32):
    """Custom type wfRipv6IntfDefaultRouteListen based on Integer32"""
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


_WfRipv6IntfDefaultRouteListen_Type.__name__ = "Integer32"
_WfRipv6IntfDefaultRouteListen_Object = MibTableColumn
wfRipv6IntfDefaultRouteListen = _WfRipv6IntfDefaultRouteListen_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 16, 1, 2, 1, 1, 8),
    _WfRipv6IntfDefaultRouteListen_Type()
)
wfRipv6IntfDefaultRouteListen.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfRipv6IntfDefaultRouteListen.setStatus("mandatory")


class _WfRipv6IntfPoisonedReversed_Type(Integer32):
    """Custom type wfRipv6IntfPoisonedReversed based on Integer32"""
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
        *(("actual", 2),
          ("poisoned", 1),
          ("split", 3))
    )


_WfRipv6IntfPoisonedReversed_Type.__name__ = "Integer32"
_WfRipv6IntfPoisonedReversed_Object = MibTableColumn
wfRipv6IntfPoisonedReversed = _WfRipv6IntfPoisonedReversed_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 16, 1, 2, 1, 1, 9),
    _WfRipv6IntfPoisonedReversed_Type()
)
wfRipv6IntfPoisonedReversed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfRipv6IntfPoisonedReversed.setStatus("mandatory")


class _WfRipv6IntfBroadcastTimer_Type(Integer32):
    """Custom type wfRipv6IntfBroadcastTimer based on Integer32"""
    defaultValue = 30

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 86400),
    )


_WfRipv6IntfBroadcastTimer_Type.__name__ = "Integer32"
_WfRipv6IntfBroadcastTimer_Object = MibTableColumn
wfRipv6IntfBroadcastTimer = _WfRipv6IntfBroadcastTimer_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 16, 1, 2, 1, 1, 10),
    _WfRipv6IntfBroadcastTimer_Type()
)
wfRipv6IntfBroadcastTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfRipv6IntfBroadcastTimer.setStatus("mandatory")


class _WfRipv6IntfTimeoutTimer_Type(Integer32):
    """Custom type wfRipv6IntfTimeoutTimer based on Integer32"""
    defaultValue = 90

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(15, 259200),
    )


_WfRipv6IntfTimeoutTimer_Type.__name__ = "Integer32"
_WfRipv6IntfTimeoutTimer_Object = MibTableColumn
wfRipv6IntfTimeoutTimer = _WfRipv6IntfTimeoutTimer_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 16, 1, 2, 1, 1, 11),
    _WfRipv6IntfTimeoutTimer_Type()
)
wfRipv6IntfTimeoutTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfRipv6IntfTimeoutTimer.setStatus("mandatory")


class _WfRipv6IntfHolddownTimer_Type(Integer32):
    """Custom type wfRipv6IntfHolddownTimer based on Integer32"""
    defaultValue = 90

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(15, 259200),
    )


_WfRipv6IntfHolddownTimer_Type.__name__ = "Integer32"
_WfRipv6IntfHolddownTimer_Object = MibTableColumn
wfRipv6IntfHolddownTimer = _WfRipv6IntfHolddownTimer_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 16, 1, 2, 1, 1, 12),
    _WfRipv6IntfHolddownTimer_Type()
)
wfRipv6IntfHolddownTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfRipv6IntfHolddownTimer.setStatus("mandatory")


class _WfRipv6IntfTriggeredUpdates_Type(Integer32):
    """Custom type wfRipv6IntfTriggeredUpdates based on Integer32"""
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


_WfRipv6IntfTriggeredUpdates_Type.__name__ = "Integer32"
_WfRipv6IntfTriggeredUpdates_Object = MibTableColumn
wfRipv6IntfTriggeredUpdates = _WfRipv6IntfTriggeredUpdates_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 16, 1, 2, 1, 1, 13),
    _WfRipv6IntfTriggeredUpdates_Type()
)
wfRipv6IntfTriggeredUpdates.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfRipv6IntfTriggeredUpdates.setStatus("mandatory")


class _WfRipv6IntfDiameter_Type(Integer32):
    """Custom type wfRipv6IntfDiameter based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_WfRipv6IntfDiameter_Type.__name__ = "Integer32"
_WfRipv6IntfDiameter_Object = MibTableColumn
wfRipv6IntfDiameter = _WfRipv6IntfDiameter_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 16, 1, 2, 1, 1, 14),
    _WfRipv6IntfDiameter_Type()
)
wfRipv6IntfDiameter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfRipv6IntfDiameter.setStatus("mandatory")
_WfRipv6IfStatsTable_Object = MibTable
wfRipv6IfStatsTable = _WfRipv6IfStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 16, 1, 2, 2)
)
if mibBuilder.loadTexts:
    wfRipv6IfStatsTable.setStatus("mandatory")
_WfRipv6IfStatsEntry_Object = MibTableRow
wfRipv6IfStatsEntry = _WfRipv6IfStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 16, 1, 2, 2, 1)
)
wfRipv6IfStatsEntry.setIndexNames(
    (0, "Wellfleet-RIP6-MIB", "wfRipv6IfStatsIntfIndex"),
)
if mibBuilder.loadTexts:
    wfRipv6IfStatsEntry.setStatus("mandatory")
_WfRipv6IfStatsIntfIndex_Type = Integer32
_WfRipv6IfStatsIntfIndex_Object = MibTableColumn
wfRipv6IfStatsIntfIndex = _WfRipv6IfStatsIntfIndex_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 16, 1, 2, 2, 1, 1),
    _WfRipv6IfStatsIntfIndex_Type()
)
wfRipv6IfStatsIntfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfRipv6IfStatsIntfIndex.setStatus("mandatory")
_WfRipv6IfStatsInMsgs_Type = Counter32
_WfRipv6IfStatsInMsgs_Object = MibTableColumn
wfRipv6IfStatsInMsgs = _WfRipv6IfStatsInMsgs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 16, 1, 2, 2, 1, 2),
    _WfRipv6IfStatsInMsgs_Type()
)
wfRipv6IfStatsInMsgs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfRipv6IfStatsInMsgs.setStatus("mandatory")
_WfRipv6IfStatsInRequests_Type = Counter32
_WfRipv6IfStatsInRequests_Object = MibTableColumn
wfRipv6IfStatsInRequests = _WfRipv6IfStatsInRequests_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 16, 1, 2, 2, 1, 3),
    _WfRipv6IfStatsInRequests_Type()
)
wfRipv6IfStatsInRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfRipv6IfStatsInRequests.setStatus("mandatory")
_WfRipv6IfStatsInResponses_Type = Counter32
_WfRipv6IfStatsInResponses_Object = MibTableColumn
wfRipv6IfStatsInResponses = _WfRipv6IfStatsInResponses_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 16, 1, 2, 2, 1, 4),
    _WfRipv6IfStatsInResponses_Type()
)
wfRipv6IfStatsInResponses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfRipv6IfStatsInResponses.setStatus("mandatory")
_WfRipv6IfStatsInBadResponses_Type = Counter32
_WfRipv6IfStatsInBadResponses_Object = MibTableColumn
wfRipv6IfStatsInBadResponses = _WfRipv6IfStatsInBadResponses_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 16, 1, 2, 2, 1, 5),
    _WfRipv6IfStatsInBadResponses_Type()
)
wfRipv6IfStatsInBadResponses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfRipv6IfStatsInBadResponses.setStatus("mandatory")
_WfRipv6IfStatsInBadRoutes_Type = Counter32
_WfRipv6IfStatsInBadRoutes_Object = MibTableColumn
wfRipv6IfStatsInBadRoutes = _WfRipv6IfStatsInBadRoutes_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 16, 1, 2, 2, 1, 6),
    _WfRipv6IfStatsInBadRoutes_Type()
)
wfRipv6IfStatsInBadRoutes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfRipv6IfStatsInBadRoutes.setStatus("mandatory")
_WfRipv6IfStatsOutMsgs_Type = Counter32
_WfRipv6IfStatsOutMsgs_Object = MibTableColumn
wfRipv6IfStatsOutMsgs = _WfRipv6IfStatsOutMsgs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 16, 1, 2, 2, 1, 7),
    _WfRipv6IfStatsOutMsgs_Type()
)
wfRipv6IfStatsOutMsgs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfRipv6IfStatsOutMsgs.setStatus("mandatory")
_WfRipv6IfStatsOutRequests_Type = Counter32
_WfRipv6IfStatsOutRequests_Object = MibTableColumn
wfRipv6IfStatsOutRequests = _WfRipv6IfStatsOutRequests_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 16, 1, 2, 2, 1, 8),
    _WfRipv6IfStatsOutRequests_Type()
)
wfRipv6IfStatsOutRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfRipv6IfStatsOutRequests.setStatus("mandatory")
_WfRipv6IfStatsOutResponses_Type = Counter32
_WfRipv6IfStatsOutResponses_Object = MibTableColumn
wfRipv6IfStatsOutResponses = _WfRipv6IfStatsOutResponses_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 16, 1, 2, 2, 1, 9),
    _WfRipv6IfStatsOutResponses_Type()
)
wfRipv6IfStatsOutResponses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfRipv6IfStatsOutResponses.setStatus("mandatory")
_WfRipv6IfStatsOutFullUpdates_Type = Counter32
_WfRipv6IfStatsOutFullUpdates_Object = MibTableColumn
wfRipv6IfStatsOutFullUpdates = _WfRipv6IfStatsOutFullUpdates_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 16, 1, 2, 2, 1, 10),
    _WfRipv6IfStatsOutFullUpdates_Type()
)
wfRipv6IfStatsOutFullUpdates.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfRipv6IfStatsOutFullUpdates.setStatus("mandatory")
_WfRipv6IfStatsOutTriggeredUpdates_Type = Counter32
_WfRipv6IfStatsOutTriggeredUpdates_Object = MibTableColumn
wfRipv6IfStatsOutTriggeredUpdates = _WfRipv6IfStatsOutTriggeredUpdates_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 16, 1, 2, 2, 1, 11),
    _WfRipv6IfStatsOutTriggeredUpdates_Type()
)
wfRipv6IfStatsOutTriggeredUpdates.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfRipv6IfStatsOutTriggeredUpdates.setStatus("mandatory")
_WfRipv6IfStatsOutRoutesAdvertised_Type = Counter32
_WfRipv6IfStatsOutRoutesAdvertised_Object = MibTableColumn
wfRipv6IfStatsOutRoutesAdvertised = _WfRipv6IfStatsOutRoutesAdvertised_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 16, 1, 2, 2, 1, 12),
    _WfRipv6IfStatsOutRoutesAdvertised_Type()
)
wfRipv6IfStatsOutRoutesAdvertised.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfRipv6IfStatsOutRoutesAdvertised.setStatus("mandatory")
_WfRipv6Log_ObjectIdentity = ObjectIdentity
wfRipv6Log = _WfRipv6Log_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 16, 1, 2, 3)
)


class _WfRipv6LogDelete_Type(Integer32):
    """Custom type wfRipv6LogDelete based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("created", 1),
          ("deleted", 2))
    )


_WfRipv6LogDelete_Type.__name__ = "Integer32"
_WfRipv6LogDelete_Object = MibScalar
wfRipv6LogDelete = _WfRipv6LogDelete_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 16, 1, 2, 3, 1),
    _WfRipv6LogDelete_Type()
)
wfRipv6LogDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfRipv6LogDelete.setStatus("mandatory")


class _WfRipv6LogDisable_Type(Integer32):
    """Custom type wfRipv6LogDisable based on Integer32"""
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


_WfRipv6LogDisable_Type.__name__ = "Integer32"
_WfRipv6LogDisable_Object = MibScalar
wfRipv6LogDisable = _WfRipv6LogDisable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 16, 1, 2, 3, 2),
    _WfRipv6LogDisable_Type()
)
wfRipv6LogDisable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfRipv6LogDisable.setStatus("mandatory")


class _WfRipv6LogLevel_Type(Integer32):
    """Custom type wfRipv6LogLevel based on Integer32"""
    defaultValue = 3

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
        *(("debug", 1),
          ("fault", 5),
          ("info", 3),
          ("trace", 2),
          ("warning", 4))
    )


_WfRipv6LogLevel_Type.__name__ = "Integer32"
_WfRipv6LogLevel_Object = MibScalar
wfRipv6LogLevel = _WfRipv6LogLevel_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 16, 1, 2, 3, 3),
    _WfRipv6LogLevel_Type()
)
wfRipv6LogLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfRipv6LogLevel.setStatus("mandatory")


class _WfRipv6LogEvent_Type(Integer32):
    """Custom type wfRipv6LogEvent based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_WfRipv6LogEvent_Type.__name__ = "Integer32"
_WfRipv6LogEvent_Object = MibScalar
wfRipv6LogEvent = _WfRipv6LogEvent_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 16, 1, 2, 3, 4),
    _WfRipv6LogEvent_Type()
)
wfRipv6LogEvent.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfRipv6LogEvent.setStatus("mandatory")


class _WfRipv6LogEventDisable_Type(Integer32):
    """Custom type wfRipv6LogEventDisable based on Integer32"""
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


_WfRipv6LogEventDisable_Type.__name__ = "Integer32"
_WfRipv6LogEventDisable_Object = MibScalar
wfRipv6LogEventDisable = _WfRipv6LogEventDisable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 16, 1, 2, 3, 5),
    _WfRipv6LogEventDisable_Type()
)
wfRipv6LogEventDisable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfRipv6LogEventDisable.setStatus("mandatory")
_WfRipv6LogEvents_Type = OctetString
_WfRipv6LogEvents_Object = MibScalar
wfRipv6LogEvents = _WfRipv6LogEvents_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 16, 1, 2, 3, 6),
    _WfRipv6LogEvents_Type()
)
wfRipv6LogEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfRipv6LogEvents.setStatus("mandatory")
_WfRipv6LogCfgEvents_Type = OctetString
_WfRipv6LogCfgEvents_Object = MibScalar
wfRipv6LogCfgEvents = _WfRipv6LogCfgEvents_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 16, 1, 2, 3, 7),
    _WfRipv6LogCfgEvents_Type()
)
wfRipv6LogCfgEvents.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfRipv6LogCfgEvents.setStatus("mandatory")
_WfRipv6Base_ObjectIdentity = ObjectIdentity
wfRipv6Base = _WfRipv6Base_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 16, 1, 2, 4)
)


class _WfRipv6BaseDelete_Type(Integer32):
    """Custom type wfRipv6BaseDelete based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("created", 1),
          ("deleted", 2))
    )


_WfRipv6BaseDelete_Type.__name__ = "Integer32"
_WfRipv6BaseDelete_Object = MibScalar
wfRipv6BaseDelete = _WfRipv6BaseDelete_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 16, 1, 2, 4, 1),
    _WfRipv6BaseDelete_Type()
)
wfRipv6BaseDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfRipv6BaseDelete.setStatus("mandatory")


class _WfRipv6BaseDisable_Type(Integer32):
    """Custom type wfRipv6BaseDisable based on Integer32"""
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


_WfRipv6BaseDisable_Type.__name__ = "Integer32"
_WfRipv6BaseDisable_Object = MibScalar
wfRipv6BaseDisable = _WfRipv6BaseDisable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 16, 1, 2, 4, 2),
    _WfRipv6BaseDisable_Type()
)
wfRipv6BaseDisable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfRipv6BaseDisable.setStatus("mandatory")


class _WfRipv6BaseState_Type(Integer32):
    """Custom type wfRipv6BaseState based on Integer32"""
    defaultValue = 2

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


_WfRipv6BaseState_Type.__name__ = "Integer32"
_WfRipv6BaseState_Object = MibScalar
wfRipv6BaseState = _WfRipv6BaseState_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 16, 1, 2, 4, 3),
    _WfRipv6BaseState_Type()
)
wfRipv6BaseState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfRipv6BaseState.setStatus("mandatory")


class _WfRipv6BaseDiameter_Type(Integer32):
    """Custom type wfRipv6BaseDiameter based on Integer32"""
    defaultValue = 15

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_WfRipv6BaseDiameter_Type.__name__ = "Integer32"
_WfRipv6BaseDiameter_Object = MibScalar
wfRipv6BaseDiameter = _WfRipv6BaseDiameter_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 16, 1, 2, 4, 4),
    _WfRipv6BaseDiameter_Type()
)
wfRipv6BaseDiameter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfRipv6BaseDiameter.setStatus("mandatory")
_WfRip6AcceptTable_Object = MibTable
wfRip6AcceptTable = _WfRip6AcceptTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 16, 6, 1)
)
if mibBuilder.loadTexts:
    wfRip6AcceptTable.setStatus("mandatory")
_WfRip6AcceptEntry_Object = MibTableRow
wfRip6AcceptEntry = _WfRip6AcceptEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 16, 6, 1, 1)
)
wfRip6AcceptEntry.setIndexNames(
    (0, "Wellfleet-RIP6-MIB", "wfRip6AcceptIndex"),
)
if mibBuilder.loadTexts:
    wfRip6AcceptEntry.setStatus("mandatory")


class _WfRip6AcceptDelete_Type(Integer32):
    """Custom type wfRip6AcceptDelete based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("created", 1),
          ("deleted", 2))
    )


_WfRip6AcceptDelete_Type.__name__ = "Integer32"
_WfRip6AcceptDelete_Object = MibTableColumn
wfRip6AcceptDelete = _WfRip6AcceptDelete_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 16, 6, 1, 1, 1),
    _WfRip6AcceptDelete_Type()
)
wfRip6AcceptDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfRip6AcceptDelete.setStatus("mandatory")


class _WfRip6AcceptDisable_Type(Integer32):
    """Custom type wfRip6AcceptDisable based on Integer32"""
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


_WfRip6AcceptDisable_Type.__name__ = "Integer32"
_WfRip6AcceptDisable_Object = MibTableColumn
wfRip6AcceptDisable = _WfRip6AcceptDisable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 16, 6, 1, 1, 2),
    _WfRip6AcceptDisable_Type()
)
wfRip6AcceptDisable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfRip6AcceptDisable.setStatus("mandatory")
_WfRip6AcceptIndex_Type = Integer32
_WfRip6AcceptIndex_Object = MibTableColumn
wfRip6AcceptIndex = _WfRip6AcceptIndex_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 16, 6, 1, 1, 3),
    _WfRip6AcceptIndex_Type()
)
wfRip6AcceptIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfRip6AcceptIndex.setStatus("mandatory")
_WfRip6AcceptName_Type = DisplayString
_WfRip6AcceptName_Object = MibTableColumn
wfRip6AcceptName = _WfRip6AcceptName_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 16, 6, 1, 1, 4),
    _WfRip6AcceptName_Type()
)
wfRip6AcceptName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfRip6AcceptName.setStatus("mandatory")
_WfRip6AcceptPrefixes_Type = OctetString
_WfRip6AcceptPrefixes_Object = MibTableColumn
wfRip6AcceptPrefixes = _WfRip6AcceptPrefixes_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 16, 6, 1, 1, 5),
    _WfRip6AcceptPrefixes_Type()
)
wfRip6AcceptPrefixes.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfRip6AcceptPrefixes.setStatus("mandatory")


class _WfRip6AcceptAction_Type(Integer32):
    """Custom type wfRip6AcceptAction based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              3)
        )
    )
    namedValues = NamedValues(
        *(("accept", 1),
          ("ignore", 3))
    )


_WfRip6AcceptAction_Type.__name__ = "Integer32"
_WfRip6AcceptAction_Object = MibTableColumn
wfRip6AcceptAction = _WfRip6AcceptAction_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 16, 6, 1, 1, 6),
    _WfRip6AcceptAction_Type()
)
wfRip6AcceptAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfRip6AcceptAction.setStatus("mandatory")


class _WfRip6AcceptPreference_Type(Integer32):
    """Custom type wfRip6AcceptPreference based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_WfRip6AcceptPreference_Type.__name__ = "Integer32"
_WfRip6AcceptPreference_Object = MibTableColumn
wfRip6AcceptPreference = _WfRip6AcceptPreference_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 16, 6, 1, 1, 7),
    _WfRip6AcceptPreference_Type()
)
wfRip6AcceptPreference.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfRip6AcceptPreference.setStatus("mandatory")
_WfRip6AcceptPrecedence_Type = Integer32
_WfRip6AcceptPrecedence_Object = MibTableColumn
wfRip6AcceptPrecedence = _WfRip6AcceptPrecedence_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 16, 6, 1, 1, 8),
    _WfRip6AcceptPrecedence_Type()
)
wfRip6AcceptPrecedence.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfRip6AcceptPrecedence.setStatus("mandatory")
_WfRip6AcceptInject_Type = OctetString
_WfRip6AcceptInject_Object = MibTableColumn
wfRip6AcceptInject = _WfRip6AcceptInject_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 16, 6, 1, 1, 9),
    _WfRip6AcceptInject_Type()
)
wfRip6AcceptInject.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfRip6AcceptInject.setStatus("mandatory")
_WfRip6AcceptGateway_Type = OctetString
_WfRip6AcceptGateway_Object = MibTableColumn
wfRip6AcceptGateway = _WfRip6AcceptGateway_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 16, 6, 1, 1, 10),
    _WfRip6AcceptGateway_Type()
)
wfRip6AcceptGateway.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfRip6AcceptGateway.setStatus("mandatory")
_WfRip6AcceptInterface_Type = OctetString
_WfRip6AcceptInterface_Object = MibTableColumn
wfRip6AcceptInterface = _WfRip6AcceptInterface_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 16, 6, 1, 1, 11),
    _WfRip6AcceptInterface_Type()
)
wfRip6AcceptInterface.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfRip6AcceptInterface.setStatus("mandatory")


class _WfRip6AcceptLog_Type(Integer32):
    """Custom type wfRip6AcceptLog based on Integer32"""
    defaultValue = 2

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


_WfRip6AcceptLog_Type.__name__ = "Integer32"
_WfRip6AcceptLog_Object = MibTableColumn
wfRip6AcceptLog = _WfRip6AcceptLog_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 16, 6, 1, 1, 12),
    _WfRip6AcceptLog_Type()
)
wfRip6AcceptLog.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfRip6AcceptLog.setStatus("mandatory")
_WfRip6AnnounceTable_Object = MibTable
wfRip6AnnounceTable = _WfRip6AnnounceTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 16, 6, 2)
)
if mibBuilder.loadTexts:
    wfRip6AnnounceTable.setStatus("mandatory")
_WfRip6AnnounceEntry_Object = MibTableRow
wfRip6AnnounceEntry = _WfRip6AnnounceEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 16, 6, 2, 1)
)
wfRip6AnnounceEntry.setIndexNames(
    (0, "Wellfleet-RIP6-MIB", "wfRip6AnnounceIndex"),
)
if mibBuilder.loadTexts:
    wfRip6AnnounceEntry.setStatus("mandatory")


class _WfRip6AnnounceDelete_Type(Integer32):
    """Custom type wfRip6AnnounceDelete based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("created", 1),
          ("deleted", 2))
    )


_WfRip6AnnounceDelete_Type.__name__ = "Integer32"
_WfRip6AnnounceDelete_Object = MibTableColumn
wfRip6AnnounceDelete = _WfRip6AnnounceDelete_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 16, 6, 2, 1, 1),
    _WfRip6AnnounceDelete_Type()
)
wfRip6AnnounceDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfRip6AnnounceDelete.setStatus("mandatory")


class _WfRip6AnnounceDisable_Type(Integer32):
    """Custom type wfRip6AnnounceDisable based on Integer32"""
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


_WfRip6AnnounceDisable_Type.__name__ = "Integer32"
_WfRip6AnnounceDisable_Object = MibTableColumn
wfRip6AnnounceDisable = _WfRip6AnnounceDisable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 16, 6, 2, 1, 2),
    _WfRip6AnnounceDisable_Type()
)
wfRip6AnnounceDisable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfRip6AnnounceDisable.setStatus("mandatory")
_WfRip6AnnounceIndex_Type = Integer32
_WfRip6AnnounceIndex_Object = MibTableColumn
wfRip6AnnounceIndex = _WfRip6AnnounceIndex_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 16, 6, 2, 1, 3),
    _WfRip6AnnounceIndex_Type()
)
wfRip6AnnounceIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfRip6AnnounceIndex.setStatus("mandatory")
_WfRip6AnnounceName_Type = DisplayString
_WfRip6AnnounceName_Object = MibTableColumn
wfRip6AnnounceName = _WfRip6AnnounceName_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 16, 6, 2, 1, 4),
    _WfRip6AnnounceName_Type()
)
wfRip6AnnounceName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfRip6AnnounceName.setStatus("mandatory")
_WfRip6AnnouncePrefixes_Type = OctetString
_WfRip6AnnouncePrefixes_Object = MibTableColumn
wfRip6AnnouncePrefixes = _WfRip6AnnouncePrefixes_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 16, 6, 2, 1, 5),
    _WfRip6AnnouncePrefixes_Type()
)
wfRip6AnnouncePrefixes.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfRip6AnnouncePrefixes.setStatus("mandatory")


class _WfRip6AnnounceAction_Type(Integer32):
    """Custom type wfRip6AnnounceAction based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("announce", 2),
          ("ignore", 3))
    )


_WfRip6AnnounceAction_Type.__name__ = "Integer32"
_WfRip6AnnounceAction_Object = MibTableColumn
wfRip6AnnounceAction = _WfRip6AnnounceAction_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 16, 6, 2, 1, 6),
    _WfRip6AnnounceAction_Type()
)
wfRip6AnnounceAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfRip6AnnounceAction.setStatus("mandatory")
_WfRip6AnnouncePrecedence_Type = Integer32
_WfRip6AnnouncePrecedence_Object = MibTableColumn
wfRip6AnnouncePrecedence = _WfRip6AnnouncePrecedence_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 16, 6, 2, 1, 7),
    _WfRip6AnnouncePrecedence_Type()
)
wfRip6AnnouncePrecedence.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfRip6AnnouncePrecedence.setStatus("mandatory")


class _WfRip6AnnounceRouteSource_Type(Integer32):
    """Custom type wfRip6AnnounceRouteSource based on Integer32"""
    defaultValue = 63


_WfRip6AnnounceRouteSource_Object = MibTableColumn
wfRip6AnnounceRouteSource = _WfRip6AnnounceRouteSource_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 16, 6, 2, 1, 8),
    _WfRip6AnnounceRouteSource_Type()
)
wfRip6AnnounceRouteSource.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfRip6AnnounceRouteSource.setStatus("mandatory")


class _WfRip6AnnounceExtRouteSource_Type(Integer32):
    """Custom type wfRip6AnnounceExtRouteSource based on Integer32"""
    defaultValue = 63


_WfRip6AnnounceExtRouteSource_Object = MibTableColumn
wfRip6AnnounceExtRouteSource = _WfRip6AnnounceExtRouteSource_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 16, 6, 2, 1, 9),
    _WfRip6AnnounceExtRouteSource_Type()
)
wfRip6AnnounceExtRouteSource.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfRip6AnnounceExtRouteSource.setStatus("mandatory")
_WfRip6AnnounceAdvertise_Type = OctetString
_WfRip6AnnounceAdvertise_Object = MibTableColumn
wfRip6AnnounceAdvertise = _WfRip6AnnounceAdvertise_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 16, 6, 2, 1, 10),
    _WfRip6AnnounceAdvertise_Type()
)
wfRip6AnnounceAdvertise.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfRip6AnnounceAdvertise.setStatus("mandatory")
_WfRip6AnnounceRipGateway_Type = OctetString
_WfRip6AnnounceRipGateway_Object = MibTableColumn
wfRip6AnnounceRipGateway = _WfRip6AnnounceRipGateway_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 16, 6, 2, 1, 11),
    _WfRip6AnnounceRipGateway_Type()
)
wfRip6AnnounceRipGateway.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfRip6AnnounceRipGateway.setStatus("mandatory")
_WfRip6AnnounceInterface_Type = OctetString
_WfRip6AnnounceInterface_Object = MibTableColumn
wfRip6AnnounceInterface = _WfRip6AnnounceInterface_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 16, 6, 2, 1, 12),
    _WfRip6AnnounceInterface_Type()
)
wfRip6AnnounceInterface.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfRip6AnnounceInterface.setStatus("mandatory")


class _WfRip6AnnounceRipMetric_Type(Integer32):
    """Custom type wfRip6AnnounceRipMetric based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_WfRip6AnnounceRipMetric_Type.__name__ = "Integer32"
_WfRip6AnnounceRipMetric_Object = MibTableColumn
wfRip6AnnounceRipMetric = _WfRip6AnnounceRipMetric_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 16, 6, 2, 1, 13),
    _WfRip6AnnounceRipMetric_Type()
)
wfRip6AnnounceRipMetric.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfRip6AnnounceRipMetric.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Wellfleet-RIP6-MIB",
    **{"wfRipv6Group": wfRipv6Group,
       "wfRipv6IfTable": wfRipv6IfTable,
       "wfRipv6IfEntry": wfRipv6IfEntry,
       "wfRipv6IntfCreate": wfRipv6IntfCreate,
       "wfRipv6IntfEnable": wfRipv6IntfEnable,
       "wfRipv6IntfState": wfRipv6IntfState,
       "wfRipv6IntfIndex": wfRipv6IntfIndex,
       "wfRipv6IntfSupply": wfRipv6IntfSupply,
       "wfRipv6IntfListen": wfRipv6IntfListen,
       "wfRipv6IntfDefaultRouteSupply": wfRipv6IntfDefaultRouteSupply,
       "wfRipv6IntfDefaultRouteListen": wfRipv6IntfDefaultRouteListen,
       "wfRipv6IntfPoisonedReversed": wfRipv6IntfPoisonedReversed,
       "wfRipv6IntfBroadcastTimer": wfRipv6IntfBroadcastTimer,
       "wfRipv6IntfTimeoutTimer": wfRipv6IntfTimeoutTimer,
       "wfRipv6IntfHolddownTimer": wfRipv6IntfHolddownTimer,
       "wfRipv6IntfTriggeredUpdates": wfRipv6IntfTriggeredUpdates,
       "wfRipv6IntfDiameter": wfRipv6IntfDiameter,
       "wfRipv6IfStatsTable": wfRipv6IfStatsTable,
       "wfRipv6IfStatsEntry": wfRipv6IfStatsEntry,
       "wfRipv6IfStatsIntfIndex": wfRipv6IfStatsIntfIndex,
       "wfRipv6IfStatsInMsgs": wfRipv6IfStatsInMsgs,
       "wfRipv6IfStatsInRequests": wfRipv6IfStatsInRequests,
       "wfRipv6IfStatsInResponses": wfRipv6IfStatsInResponses,
       "wfRipv6IfStatsInBadResponses": wfRipv6IfStatsInBadResponses,
       "wfRipv6IfStatsInBadRoutes": wfRipv6IfStatsInBadRoutes,
       "wfRipv6IfStatsOutMsgs": wfRipv6IfStatsOutMsgs,
       "wfRipv6IfStatsOutRequests": wfRipv6IfStatsOutRequests,
       "wfRipv6IfStatsOutResponses": wfRipv6IfStatsOutResponses,
       "wfRipv6IfStatsOutFullUpdates": wfRipv6IfStatsOutFullUpdates,
       "wfRipv6IfStatsOutTriggeredUpdates": wfRipv6IfStatsOutTriggeredUpdates,
       "wfRipv6IfStatsOutRoutesAdvertised": wfRipv6IfStatsOutRoutesAdvertised,
       "wfRipv6Log": wfRipv6Log,
       "wfRipv6LogDelete": wfRipv6LogDelete,
       "wfRipv6LogDisable": wfRipv6LogDisable,
       "wfRipv6LogLevel": wfRipv6LogLevel,
       "wfRipv6LogEvent": wfRipv6LogEvent,
       "wfRipv6LogEventDisable": wfRipv6LogEventDisable,
       "wfRipv6LogEvents": wfRipv6LogEvents,
       "wfRipv6LogCfgEvents": wfRipv6LogCfgEvents,
       "wfRipv6Base": wfRipv6Base,
       "wfRipv6BaseDelete": wfRipv6BaseDelete,
       "wfRipv6BaseDisable": wfRipv6BaseDisable,
       "wfRipv6BaseState": wfRipv6BaseState,
       "wfRipv6BaseDiameter": wfRipv6BaseDiameter,
       "wfRip6AcceptTable": wfRip6AcceptTable,
       "wfRip6AcceptEntry": wfRip6AcceptEntry,
       "wfRip6AcceptDelete": wfRip6AcceptDelete,
       "wfRip6AcceptDisable": wfRip6AcceptDisable,
       "wfRip6AcceptIndex": wfRip6AcceptIndex,
       "wfRip6AcceptName": wfRip6AcceptName,
       "wfRip6AcceptPrefixes": wfRip6AcceptPrefixes,
       "wfRip6AcceptAction": wfRip6AcceptAction,
       "wfRip6AcceptPreference": wfRip6AcceptPreference,
       "wfRip6AcceptPrecedence": wfRip6AcceptPrecedence,
       "wfRip6AcceptInject": wfRip6AcceptInject,
       "wfRip6AcceptGateway": wfRip6AcceptGateway,
       "wfRip6AcceptInterface": wfRip6AcceptInterface,
       "wfRip6AcceptLog": wfRip6AcceptLog,
       "wfRip6AnnounceTable": wfRip6AnnounceTable,
       "wfRip6AnnounceEntry": wfRip6AnnounceEntry,
       "wfRip6AnnounceDelete": wfRip6AnnounceDelete,
       "wfRip6AnnounceDisable": wfRip6AnnounceDisable,
       "wfRip6AnnounceIndex": wfRip6AnnounceIndex,
       "wfRip6AnnounceName": wfRip6AnnounceName,
       "wfRip6AnnouncePrefixes": wfRip6AnnouncePrefixes,
       "wfRip6AnnounceAction": wfRip6AnnounceAction,
       "wfRip6AnnouncePrecedence": wfRip6AnnouncePrecedence,
       "wfRip6AnnounceRouteSource": wfRip6AnnounceRouteSource,
       "wfRip6AnnounceExtRouteSource": wfRip6AnnounceExtRouteSource,
       "wfRip6AnnounceAdvertise": wfRip6AnnounceAdvertise,
       "wfRip6AnnounceRipGateway": wfRip6AnnounceRipGateway,
       "wfRip6AnnounceInterface": wfRip6AnnounceInterface,
       "wfRip6AnnounceRipMetric": wfRip6AnnounceRipMetric}
)
