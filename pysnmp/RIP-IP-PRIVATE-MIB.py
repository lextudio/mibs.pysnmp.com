# SNMP MIB module (RIP-IP-PRIVATE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/RIP-IP-PRIVATE-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:47:36 2024
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

cjnRip = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 10)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CjnIpRipGblGroup_ObjectIdentity = ObjectIdentity
cjnIpRipGblGroup = _CjnIpRipGblGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 10, 1)
)


class _CjnIpRipIsEnabled_Type(Integer32):
    """Custom type cjnIpRipIsEnabled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("false", 0),
          ("true", 1))
    )


_CjnIpRipIsEnabled_Type.__name__ = "Integer32"
_CjnIpRipIsEnabled_Object = MibScalar
cjnIpRipIsEnabled = _CjnIpRipIsEnabled_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 10, 1, 1),
    _CjnIpRipIsEnabled_Type()
)
cjnIpRipIsEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cjnIpRipIsEnabled.setStatus("current")
_CjnIpRipUpdateTimer_Type = Integer32
_CjnIpRipUpdateTimer_Object = MibScalar
cjnIpRipUpdateTimer = _CjnIpRipUpdateTimer_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 10, 1, 2),
    _CjnIpRipUpdateTimer_Type()
)
cjnIpRipUpdateTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cjnIpRipUpdateTimer.setStatus("current")
_CjnIpRipPurgeTTL_Type = Integer32
_CjnIpRipPurgeTTL_Object = MibScalar
cjnIpRipPurgeTTL = _CjnIpRipPurgeTTL_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 10, 1, 3),
    _CjnIpRipPurgeTTL_Type()
)
cjnIpRipPurgeTTL.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cjnIpRipPurgeTTL.setStatus("current")


class _CjnIpRipTriggeredUpdates_Type(Integer32):
    """Custom type cjnIpRipTriggeredUpdates based on Integer32"""
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


_CjnIpRipTriggeredUpdates_Type.__name__ = "Integer32"
_CjnIpRipTriggeredUpdates_Object = MibScalar
cjnIpRipTriggeredUpdates = _CjnIpRipTriggeredUpdates_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 10, 1, 4),
    _CjnIpRipTriggeredUpdates_Type()
)
cjnIpRipTriggeredUpdates.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cjnIpRipTriggeredUpdates.setStatus("current")
_CjnIpRipInterPktDelay_Type = Integer32
_CjnIpRipInterPktDelay_Object = MibScalar
cjnIpRipInterPktDelay = _CjnIpRipInterPktDelay_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 10, 1, 5),
    _CjnIpRipInterPktDelay_Type()
)
cjnIpRipInterPktDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cjnIpRipInterPktDelay.setStatus("current")
_CjnIpRipStatGroup_ObjectIdentity = ObjectIdentity
cjnIpRipStatGroup = _CjnIpRipStatGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 10, 2)
)
_CjnIpRipIfGroup_ObjectIdentity = ObjectIdentity
cjnIpRipIfGroup = _CjnIpRipIfGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 10, 3)
)
_CjnIpRipIfTable_Object = MibTable
cjnIpRipIfTable = _CjnIpRipIfTable_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 10, 3, 1)
)
if mibBuilder.loadTexts:
    cjnIpRipIfTable.setStatus("current")
_CjnIpRipIfEntry_Object = MibTableRow
cjnIpRipIfEntry = _CjnIpRipIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 10, 3, 1, 1)
)
cjnIpRipIfEntry.setIndexNames(
    (0, "RIP-IP-PRIVATE-MIB", "cjnIpRipIfIpAddr"),
)
if mibBuilder.loadTexts:
    cjnIpRipIfEntry.setStatus("current")
_CjnIpRipIfIpAddr_Type = IpAddress
_CjnIpRipIfIpAddr_Object = MibTableColumn
cjnIpRipIfIpAddr = _CjnIpRipIfIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 10, 3, 1, 1, 1),
    _CjnIpRipIfIpAddr_Type()
)
cjnIpRipIfIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cjnIpRipIfIpAddr.setStatus("current")
_CjnIpRipIfRowStatus_Type = RowStatus
_CjnIpRipIfRowStatus_Object = MibTableColumn
cjnIpRipIfRowStatus = _CjnIpRipIfRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 10, 3, 1, 1, 2),
    _CjnIpRipIfRowStatus_Type()
)
cjnIpRipIfRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cjnIpRipIfRowStatus.setStatus("current")


class _CjnIpRipIfSendRcvMode_Type(Integer32):
    """Custom type cjnIpRipIfSendRcvMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("listenOnly", 2),
          ("talkAndListen", 3),
          ("talkOnly", 1))
    )


_CjnIpRipIfSendRcvMode_Type.__name__ = "Integer32"
_CjnIpRipIfSendRcvMode_Object = MibTableColumn
cjnIpRipIfSendRcvMode = _CjnIpRipIfSendRcvMode_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 10, 3, 1, 1, 3),
    _CjnIpRipIfSendRcvMode_Type()
)
cjnIpRipIfSendRcvMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cjnIpRipIfSendRcvMode.setStatus("current")


class _CjnIpRipIfSendVersion_Type(Integer32):
    """Custom type cjnIpRipIfSendVersion based on Integer32"""
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
        *(("off", 4),
          ("v1", 1),
          ("v1v2", 3),
          ("v2", 2))
    )


_CjnIpRipIfSendVersion_Type.__name__ = "Integer32"
_CjnIpRipIfSendVersion_Object = MibTableColumn
cjnIpRipIfSendVersion = _CjnIpRipIfSendVersion_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 10, 3, 1, 1, 4),
    _CjnIpRipIfSendVersion_Type()
)
cjnIpRipIfSendVersion.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cjnIpRipIfSendVersion.setStatus("current")


class _CjnIpRipIfRcvVersion_Type(Integer32):
    """Custom type cjnIpRipIfRcvVersion based on Integer32"""
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
        *(("off", 4),
          ("v1", 1),
          ("v1v2", 3),
          ("v2", 2))
    )


_CjnIpRipIfRcvVersion_Type.__name__ = "Integer32"
_CjnIpRipIfRcvVersion_Object = MibTableColumn
cjnIpRipIfRcvVersion = _CjnIpRipIfRcvVersion_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 10, 3, 1, 1, 5),
    _CjnIpRipIfRcvVersion_Type()
)
cjnIpRipIfRcvVersion.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cjnIpRipIfRcvVersion.setStatus("current")


class _CjnIpRipIfDefaultRouteMode_Type(Integer32):
    """Custom type cjnIpRipIfDefaultRouteMode based on Integer32"""
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
        *(("disable", 4),
          ("listenOnly", 2),
          ("talkAndListen", 3),
          ("talkOnly", 1))
    )


_CjnIpRipIfDefaultRouteMode_Type.__name__ = "Integer32"
_CjnIpRipIfDefaultRouteMode_Object = MibTableColumn
cjnIpRipIfDefaultRouteMode = _CjnIpRipIfDefaultRouteMode_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 10, 3, 1, 1, 6),
    _CjnIpRipIfDefaultRouteMode_Type()
)
cjnIpRipIfDefaultRouteMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cjnIpRipIfDefaultRouteMode.setStatus("current")


class _CjnIpRipIfPoisonMethod_Type(Integer32):
    """Custom type cjnIpRipIfPoisonMethod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("splitHorizon", 1),
          ("splitHorizonWithPoisonReverse", 2))
    )


_CjnIpRipIfPoisonMethod_Type.__name__ = "Integer32"
_CjnIpRipIfPoisonMethod_Object = MibTableColumn
cjnIpRipIfPoisonMethod = _CjnIpRipIfPoisonMethod_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 10, 3, 1, 1, 7),
    _CjnIpRipIfPoisonMethod_Type()
)
cjnIpRipIfPoisonMethod.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cjnIpRipIfPoisonMethod.setStatus("current")


class _CjnIpRipIfAuthType_Type(Integer32):
    """Custom type cjnIpRipIfAuthType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("mD5", 3),
          ("none", 1),
          ("simplePassword", 2))
    )


_CjnIpRipIfAuthType_Type.__name__ = "Integer32"
_CjnIpRipIfAuthType_Object = MibTableColumn
cjnIpRipIfAuthType = _CjnIpRipIfAuthType_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 10, 3, 1, 1, 8),
    _CjnIpRipIfAuthType_Type()
)
cjnIpRipIfAuthType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cjnIpRipIfAuthType.setStatus("current")


class _CjnIpRipIfAuthKey_Type(OctetString):
    """Custom type cjnIpRipIfAuthKey based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_CjnIpRipIfAuthKey_Type.__name__ = "OctetString"
_CjnIpRipIfAuthKey_Object = MibTableColumn
cjnIpRipIfAuthKey = _CjnIpRipIfAuthKey_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 10, 3, 1, 1, 9),
    _CjnIpRipIfAuthKey_Type()
)
cjnIpRipIfAuthKey.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cjnIpRipIfAuthKey.setStatus("current")
_CjnIpRipIfStatTable_Object = MibTable
cjnIpRipIfStatTable = _CjnIpRipIfStatTable_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 10, 3, 2)
)
if mibBuilder.loadTexts:
    cjnIpRipIfStatTable.setStatus("current")
_CjnIpRipIfStatEntry_Object = MibTableRow
cjnIpRipIfStatEntry = _CjnIpRipIfStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 10, 3, 2, 1)
)
cjnIpRipIfStatEntry.setIndexNames(
    (0, "RIP-IP-PRIVATE-MIB", "cjnIpRipIfStatIpAddr"),
)
if mibBuilder.loadTexts:
    cjnIpRipIfStatEntry.setStatus("current")
_CjnIpRipIfStatIpAddr_Type = IpAddress
_CjnIpRipIfStatIpAddr_Object = MibTableColumn
cjnIpRipIfStatIpAddr = _CjnIpRipIfStatIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 10, 3, 2, 1, 1),
    _CjnIpRipIfStatIpAddr_Type()
)
cjnIpRipIfStatIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cjnIpRipIfStatIpAddr.setStatus("current")
_CjnIpRipIfUpdatesSent_Type = Integer32
_CjnIpRipIfUpdatesSent_Object = MibTableColumn
cjnIpRipIfUpdatesSent = _CjnIpRipIfUpdatesSent_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 10, 3, 2, 1, 2),
    _CjnIpRipIfUpdatesSent_Type()
)
cjnIpRipIfUpdatesSent.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cjnIpRipIfUpdatesSent.setStatus("current")
_CjnIpRipIfUpdatesRcvd_Type = Integer32
_CjnIpRipIfUpdatesRcvd_Object = MibTableColumn
cjnIpRipIfUpdatesRcvd = _CjnIpRipIfUpdatesRcvd_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 10, 3, 2, 1, 3),
    _CjnIpRipIfUpdatesRcvd_Type()
)
cjnIpRipIfUpdatesRcvd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cjnIpRipIfUpdatesRcvd.setStatus("current")
_CjnIpRipIfTrigUpdatesSent_Type = Integer32
_CjnIpRipIfTrigUpdatesSent_Object = MibTableColumn
cjnIpRipIfTrigUpdatesSent = _CjnIpRipIfTrigUpdatesSent_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 10, 3, 2, 1, 4),
    _CjnIpRipIfTrigUpdatesSent_Type()
)
cjnIpRipIfTrigUpdatesSent.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cjnIpRipIfTrigUpdatesSent.setStatus("current")
_CjnIpRipIfBadPktRcvd_Type = Integer32
_CjnIpRipIfBadPktRcvd_Object = MibTableColumn
cjnIpRipIfBadPktRcvd = _CjnIpRipIfBadPktRcvd_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 10, 3, 2, 1, 5),
    _CjnIpRipIfBadPktRcvd_Type()
)
cjnIpRipIfBadPktRcvd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cjnIpRipIfBadPktRcvd.setStatus("current")
_CjnIpRipIfBadRoutesRcvd_Type = Integer32
_CjnIpRipIfBadRoutesRcvd_Object = MibTableColumn
cjnIpRipIfBadRoutesRcvd = _CjnIpRipIfBadRoutesRcvd_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 10, 3, 2, 1, 6),
    _CjnIpRipIfBadRoutesRcvd_Type()
)
cjnIpRipIfBadRoutesRcvd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cjnIpRipIfBadRoutesRcvd.setStatus("current")
_CjnIpRipNeighborGroup_ObjectIdentity = ObjectIdentity
cjnIpRipNeighborGroup = _CjnIpRipNeighborGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 10, 4)
)
_CjnIpRipNeighborTable_Object = MibTable
cjnIpRipNeighborTable = _CjnIpRipNeighborTable_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 10, 4, 1)
)
if mibBuilder.loadTexts:
    cjnIpRipNeighborTable.setStatus("current")
_CjnIpRipNeighborEntry_Object = MibTableRow
cjnIpRipNeighborEntry = _CjnIpRipNeighborEntry_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 10, 4, 1, 1)
)
cjnIpRipNeighborEntry.setIndexNames(
    (0, "RIP-IP-PRIVATE-MIB", "cjnIpRipNeighborIpAddr"),
)
if mibBuilder.loadTexts:
    cjnIpRipNeighborEntry.setStatus("current")
_CjnIpRipNeighborIpAddr_Type = IpAddress
_CjnIpRipNeighborIpAddr_Object = MibTableColumn
cjnIpRipNeighborIpAddr = _CjnIpRipNeighborIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 10, 4, 1, 1, 1),
    _CjnIpRipNeighborIpAddr_Type()
)
cjnIpRipNeighborIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cjnIpRipNeighborIpAddr.setStatus("current")
_CjnIpRipNeighborRowStatus_Type = RowStatus
_CjnIpRipNeighborRowStatus_Object = MibTableColumn
cjnIpRipNeighborRowStatus = _CjnIpRipNeighborRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 2, 10, 4, 1, 1, 2),
    _CjnIpRipNeighborRowStatus_Type()
)
cjnIpRipNeighborRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cjnIpRipNeighborRowStatus.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "RIP-IP-PRIVATE-MIB",
    **{"cjnRip": cjnRip,
       "cjnIpRipGblGroup": cjnIpRipGblGroup,
       "cjnIpRipIsEnabled": cjnIpRipIsEnabled,
       "cjnIpRipUpdateTimer": cjnIpRipUpdateTimer,
       "cjnIpRipPurgeTTL": cjnIpRipPurgeTTL,
       "cjnIpRipTriggeredUpdates": cjnIpRipTriggeredUpdates,
       "cjnIpRipInterPktDelay": cjnIpRipInterPktDelay,
       "cjnIpRipStatGroup": cjnIpRipStatGroup,
       "cjnIpRipIfGroup": cjnIpRipIfGroup,
       "cjnIpRipIfTable": cjnIpRipIfTable,
       "cjnIpRipIfEntry": cjnIpRipIfEntry,
       "cjnIpRipIfIpAddr": cjnIpRipIfIpAddr,
       "cjnIpRipIfRowStatus": cjnIpRipIfRowStatus,
       "cjnIpRipIfSendRcvMode": cjnIpRipIfSendRcvMode,
       "cjnIpRipIfSendVersion": cjnIpRipIfSendVersion,
       "cjnIpRipIfRcvVersion": cjnIpRipIfRcvVersion,
       "cjnIpRipIfDefaultRouteMode": cjnIpRipIfDefaultRouteMode,
       "cjnIpRipIfPoisonMethod": cjnIpRipIfPoisonMethod,
       "cjnIpRipIfAuthType": cjnIpRipIfAuthType,
       "cjnIpRipIfAuthKey": cjnIpRipIfAuthKey,
       "cjnIpRipIfStatTable": cjnIpRipIfStatTable,
       "cjnIpRipIfStatEntry": cjnIpRipIfStatEntry,
       "cjnIpRipIfStatIpAddr": cjnIpRipIfStatIpAddr,
       "cjnIpRipIfUpdatesSent": cjnIpRipIfUpdatesSent,
       "cjnIpRipIfUpdatesRcvd": cjnIpRipIfUpdatesRcvd,
       "cjnIpRipIfTrigUpdatesSent": cjnIpRipIfTrigUpdatesSent,
       "cjnIpRipIfBadPktRcvd": cjnIpRipIfBadPktRcvd,
       "cjnIpRipIfBadRoutesRcvd": cjnIpRipIfBadRoutesRcvd,
       "cjnIpRipNeighborGroup": cjnIpRipNeighborGroup,
       "cjnIpRipNeighborTable": cjnIpRipNeighborTable,
       "cjnIpRipNeighborEntry": cjnIpRipNeighborEntry,
       "cjnIpRipNeighborIpAddr": cjnIpRipNeighborIpAddr,
       "cjnIpRipNeighborRowStatus": cjnIpRipNeighborRowStatus}
)
