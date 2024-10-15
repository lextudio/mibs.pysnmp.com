# SNMP MIB module (RBN-RADIUS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/RBN-RADIUS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:45:21 2024
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

(radiusAccClientServerPortNumber,
 radiusAccServerAddress,
 radiusAccServerEntry) = mibBuilder.importSymbols(
    "RADIUS-ACC-CLIENT-MIB",
    "radiusAccClientServerPortNumber",
    "radiusAccServerAddress",
    "radiusAccServerEntry")

(radiusAuthClientServerPortNumber,
 radiusAuthServerAddress,
 radiusAuthServerEntry) = mibBuilder.importSymbols(
    "RADIUS-AUTH-CLIENT-MIB",
    "radiusAuthClientServerPortNumber",
    "radiusAuthServerAddress",
    "radiusAuthServerEntry")

(rbnMgmt,) = mibBuilder.importSymbols(
    "RBN-SMI",
    "rbnMgmt")

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
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention",
    "TimeStamp",
    "TruthValue")


# MODULE-IDENTITY

rbnRadiusMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 2, 32)
)
rbnRadiusMib.setRevisions(
        ("2005-03-29 17:00",
         "2003-12-16 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class RbnRadiusServerState(Integer32, TextualConvention):
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
        *(("down", 3),
          ("unknown", 1),
          ("up", 2))
    )



class RbnRadiusServerReason(Integer32, TextualConvention):
    status = "current"
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
        *(("packetTimeout", 2),
          ("portDown", 4),
          ("responding", 1),
          ("serverTimeout", 3))
    )



# MIB Managed Objects in the order of their OIDs

_RbnRadiusMIBNotifications_ObjectIdentity = ObjectIdentity
rbnRadiusMIBNotifications = _RbnRadiusMIBNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 2, 32, 0)
)
_RbnRadiusMIBObjects_ObjectIdentity = ObjectIdentity
rbnRadiusMIBObjects = _RbnRadiusMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 2, 32, 1)
)
_RbnRadiusAuthObjects_ObjectIdentity = ObjectIdentity
rbnRadiusAuthObjects = _RbnRadiusAuthObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 2, 32, 1, 1)
)


class _RbnRadiusAuthPktTimeout_Type(Unsigned32):
    """Custom type rbnRadiusAuthPktTimeout based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_RbnRadiusAuthPktTimeout_Type.__name__ = "Unsigned32"
_RbnRadiusAuthPktTimeout_Object = MibScalar
rbnRadiusAuthPktTimeout = _RbnRadiusAuthPktTimeout_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 32, 1, 1, 1),
    _RbnRadiusAuthPktTimeout_Type()
)
rbnRadiusAuthPktTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rbnRadiusAuthPktTimeout.setStatus("current")
if mibBuilder.loadTexts:
    rbnRadiusAuthPktTimeout.setUnits("seconds")


class _RbnRadiusAuthSrvTimeout_Type(Unsigned32):
    """Custom type rbnRadiusAuthSrvTimeout based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_RbnRadiusAuthSrvTimeout_Type.__name__ = "Unsigned32"
_RbnRadiusAuthSrvTimeout_Object = MibScalar
rbnRadiusAuthSrvTimeout = _RbnRadiusAuthSrvTimeout_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 32, 1, 1, 2),
    _RbnRadiusAuthSrvTimeout_Type()
)
rbnRadiusAuthSrvTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rbnRadiusAuthSrvTimeout.setStatus("current")
if mibBuilder.loadTexts:
    rbnRadiusAuthSrvTimeout.setUnits("seconds")


class _RbnRadiusAuthDeadtime_Type(Unsigned32):
    """Custom type rbnRadiusAuthDeadtime based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_RbnRadiusAuthDeadtime_Type.__name__ = "Unsigned32"
_RbnRadiusAuthDeadtime_Object = MibScalar
rbnRadiusAuthDeadtime = _RbnRadiusAuthDeadtime_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 32, 1, 1, 3),
    _RbnRadiusAuthDeadtime_Type()
)
rbnRadiusAuthDeadtime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rbnRadiusAuthDeadtime.setStatus("current")
if mibBuilder.loadTexts:
    rbnRadiusAuthDeadtime.setUnits("minutes")


class _RbnRadiusAuthTries_Type(Unsigned32):
    """Custom type rbnRadiusAuthTries based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_RbnRadiusAuthTries_Type.__name__ = "Unsigned32"
_RbnRadiusAuthTries_Object = MibScalar
rbnRadiusAuthTries = _RbnRadiusAuthTries_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 32, 1, 1, 4),
    _RbnRadiusAuthTries_Type()
)
rbnRadiusAuthTries.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rbnRadiusAuthTries.setStatus("current")
if mibBuilder.loadTexts:
    rbnRadiusAuthTries.setUnits("tries")
_RbnRadiusAuthSrvTable_Object = MibTable
rbnRadiusAuthSrvTable = _RbnRadiusAuthSrvTable_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 32, 1, 1, 5)
)
if mibBuilder.loadTexts:
    rbnRadiusAuthSrvTable.setStatus("current")
_RbnRadiusAuthSrvEntry_Object = MibTableRow
rbnRadiusAuthSrvEntry = _RbnRadiusAuthSrvEntry_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 32, 1, 1, 5, 1)
)
if mibBuilder.loadTexts:
    rbnRadiusAuthSrvEntry.setStatus("current")
_RbnRadiusAuthSrvState_Type = RbnRadiusServerState
_RbnRadiusAuthSrvState_Object = MibTableColumn
rbnRadiusAuthSrvState = _RbnRadiusAuthSrvState_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 32, 1, 1, 5, 1, 1),
    _RbnRadiusAuthSrvState_Type()
)
rbnRadiusAuthSrvState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnRadiusAuthSrvState.setStatus("current")
_RbnRadiusAuthSrvLastChange_Type = TimeStamp
_RbnRadiusAuthSrvLastChange_Object = MibTableColumn
rbnRadiusAuthSrvLastChange = _RbnRadiusAuthSrvLastChange_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 32, 1, 1, 5, 1, 2),
    _RbnRadiusAuthSrvLastChange_Type()
)
rbnRadiusAuthSrvLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnRadiusAuthSrvLastChange.setStatus("current")
_RbnRadiusAuthSrvCounterResetTime_Type = TimeStamp
_RbnRadiusAuthSrvCounterResetTime_Object = MibTableColumn
rbnRadiusAuthSrvCounterResetTime = _RbnRadiusAuthSrvCounterResetTime_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 32, 1, 1, 5, 1, 3),
    _RbnRadiusAuthSrvCounterResetTime_Type()
)
rbnRadiusAuthSrvCounterResetTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnRadiusAuthSrvCounterResetTime.setStatus("current")
_RbnRadiusAuthSrvSendErrors_Type = Counter32
_RbnRadiusAuthSrvSendErrors_Object = MibTableColumn
rbnRadiusAuthSrvSendErrors = _RbnRadiusAuthSrvSendErrors_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 32, 1, 1, 5, 1, 4),
    _RbnRadiusAuthSrvSendErrors_Type()
)
rbnRadiusAuthSrvSendErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnRadiusAuthSrvSendErrors.setStatus("current")
if mibBuilder.loadTexts:
    rbnRadiusAuthSrvSendErrors.setUnits("packets")
_RbnRadiusAuthStripDomain_Type = TruthValue
_RbnRadiusAuthStripDomain_Object = MibScalar
rbnRadiusAuthStripDomain = _RbnRadiusAuthStripDomain_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 32, 1, 1, 6),
    _RbnRadiusAuthStripDomain_Type()
)
rbnRadiusAuthStripDomain.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rbnRadiusAuthStripDomain.setStatus("current")
_RbnRadiusAcctObjects_ObjectIdentity = ObjectIdentity
rbnRadiusAcctObjects = _RbnRadiusAcctObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 2, 32, 1, 2)
)


class _RbnRadiusAcctPktTimeout_Type(Unsigned32):
    """Custom type rbnRadiusAcctPktTimeout based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_RbnRadiusAcctPktTimeout_Type.__name__ = "Unsigned32"
_RbnRadiusAcctPktTimeout_Object = MibScalar
rbnRadiusAcctPktTimeout = _RbnRadiusAcctPktTimeout_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 32, 1, 2, 1),
    _RbnRadiusAcctPktTimeout_Type()
)
rbnRadiusAcctPktTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rbnRadiusAcctPktTimeout.setStatus("current")
if mibBuilder.loadTexts:
    rbnRadiusAcctPktTimeout.setUnits("seconds")


class _RbnRadiusAcctSrvTimeout_Type(Unsigned32):
    """Custom type rbnRadiusAcctSrvTimeout based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_RbnRadiusAcctSrvTimeout_Type.__name__ = "Unsigned32"
_RbnRadiusAcctSrvTimeout_Object = MibScalar
rbnRadiusAcctSrvTimeout = _RbnRadiusAcctSrvTimeout_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 32, 1, 2, 2),
    _RbnRadiusAcctSrvTimeout_Type()
)
rbnRadiusAcctSrvTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rbnRadiusAcctSrvTimeout.setStatus("current")
if mibBuilder.loadTexts:
    rbnRadiusAcctSrvTimeout.setUnits("seconds")


class _RbnRadiusAcctDeadtime_Type(Unsigned32):
    """Custom type rbnRadiusAcctDeadtime based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_RbnRadiusAcctDeadtime_Type.__name__ = "Unsigned32"
_RbnRadiusAcctDeadtime_Object = MibScalar
rbnRadiusAcctDeadtime = _RbnRadiusAcctDeadtime_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 32, 1, 2, 3),
    _RbnRadiusAcctDeadtime_Type()
)
rbnRadiusAcctDeadtime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rbnRadiusAcctDeadtime.setStatus("current")
if mibBuilder.loadTexts:
    rbnRadiusAcctDeadtime.setUnits("minutes")


class _RbnRadiusAcctTries_Type(Unsigned32):
    """Custom type rbnRadiusAcctTries based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_RbnRadiusAcctTries_Type.__name__ = "Unsigned32"
_RbnRadiusAcctTries_Object = MibScalar
rbnRadiusAcctTries = _RbnRadiusAcctTries_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 32, 1, 2, 4),
    _RbnRadiusAcctTries_Type()
)
rbnRadiusAcctTries.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rbnRadiusAcctTries.setStatus("current")
if mibBuilder.loadTexts:
    rbnRadiusAcctTries.setUnits("retries")
_RbnRadiusAcctSrvTable_Object = MibTable
rbnRadiusAcctSrvTable = _RbnRadiusAcctSrvTable_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 32, 1, 2, 5)
)
if mibBuilder.loadTexts:
    rbnRadiusAcctSrvTable.setStatus("current")
_RbnRadiusAcctSrvEntry_Object = MibTableRow
rbnRadiusAcctSrvEntry = _RbnRadiusAcctSrvEntry_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 32, 1, 2, 5, 1)
)
if mibBuilder.loadTexts:
    rbnRadiusAcctSrvEntry.setStatus("current")
_RbnRadiusAcctSrvState_Type = RbnRadiusServerState
_RbnRadiusAcctSrvState_Object = MibTableColumn
rbnRadiusAcctSrvState = _RbnRadiusAcctSrvState_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 32, 1, 2, 5, 1, 1),
    _RbnRadiusAcctSrvState_Type()
)
rbnRadiusAcctSrvState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnRadiusAcctSrvState.setStatus("current")
_RbnRadiusAcctSrvLastChange_Type = TimeStamp
_RbnRadiusAcctSrvLastChange_Object = MibTableColumn
rbnRadiusAcctSrvLastChange = _RbnRadiusAcctSrvLastChange_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 32, 1, 2, 5, 1, 2),
    _RbnRadiusAcctSrvLastChange_Type()
)
rbnRadiusAcctSrvLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnRadiusAcctSrvLastChange.setStatus("current")
_RbnRadiusAcctSrvCounterResetTime_Type = TimeStamp
_RbnRadiusAcctSrvCounterResetTime_Object = MibTableColumn
rbnRadiusAcctSrvCounterResetTime = _RbnRadiusAcctSrvCounterResetTime_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 32, 1, 2, 5, 1, 3),
    _RbnRadiusAcctSrvCounterResetTime_Type()
)
rbnRadiusAcctSrvCounterResetTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnRadiusAcctSrvCounterResetTime.setStatus("current")
_RbnRadiusAcctSrvSendErrors_Type = Counter32
_RbnRadiusAcctSrvSendErrors_Object = MibTableColumn
rbnRadiusAcctSrvSendErrors = _RbnRadiusAcctSrvSendErrors_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 32, 1, 2, 5, 1, 4),
    _RbnRadiusAcctSrvSendErrors_Type()
)
rbnRadiusAcctSrvSendErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnRadiusAcctSrvSendErrors.setStatus("current")
if mibBuilder.loadTexts:
    rbnRadiusAcctSrvSendErrors.setUnits("packets")
_RbnRadiusAcctStripDomain_Type = TruthValue
_RbnRadiusAcctStripDomain_Object = MibScalar
rbnRadiusAcctStripDomain = _RbnRadiusAcctStripDomain_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 32, 1, 2, 6),
    _RbnRadiusAcctStripDomain_Type()
)
rbnRadiusAcctStripDomain.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rbnRadiusAcctStripDomain.setStatus("current")
_RbnRadiusNotifyObjects_ObjectIdentity = ObjectIdentity
rbnRadiusNotifyObjects = _RbnRadiusNotifyObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 2, 32, 1, 3)
)


class _RbnRadiusClientPort_Type(Unsigned32):
    """Custom type rbnRadiusClientPort based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1024, 65535),
    )


_RbnRadiusClientPort_Type.__name__ = "Unsigned32"
_RbnRadiusClientPort_Object = MibScalar
rbnRadiusClientPort = _RbnRadiusClientPort_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 32, 1, 3, 1),
    _RbnRadiusClientPort_Type()
)
rbnRadiusClientPort.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    rbnRadiusClientPort.setStatus("current")


class _RbnRadiusContext_Type(SnmpAdminString):
    """Custom type rbnRadiusContext based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 63),
    )


_RbnRadiusContext_Type.__name__ = "SnmpAdminString"
_RbnRadiusContext_Object = MibScalar
rbnRadiusContext = _RbnRadiusContext_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 32, 1, 3, 2),
    _RbnRadiusContext_Type()
)
rbnRadiusContext.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    rbnRadiusContext.setStatus("current")
_RbnRadiusReason_Type = RbnRadiusServerReason
_RbnRadiusReason_Object = MibScalar
rbnRadiusReason = _RbnRadiusReason_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 32, 1, 3, 3),
    _RbnRadiusReason_Type()
)
rbnRadiusReason.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    rbnRadiusReason.setStatus("current")


class _RbnRadiusUsername_Type(SnmpAdminString):
    """Custom type rbnRadiusUsername based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_RbnRadiusUsername_Type.__name__ = "SnmpAdminString"
_RbnRadiusUsername_Object = MibScalar
rbnRadiusUsername = _RbnRadiusUsername_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 32, 1, 3, 4),
    _RbnRadiusUsername_Type()
)
rbnRadiusUsername.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    rbnRadiusUsername.setStatus("current")
_RbnRadiusMIBConformance_ObjectIdentity = ObjectIdentity
rbnRadiusMIBConformance = _RbnRadiusMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 2, 32, 2)
)
_RbnRadiusCompliances_ObjectIdentity = ObjectIdentity
rbnRadiusCompliances = _RbnRadiusCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 2, 32, 2, 1)
)
_RbnRadiusGroups_ObjectIdentity = ObjectIdentity
rbnRadiusGroups = _RbnRadiusGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 2, 32, 2, 2)
)
radiusAuthServerEntry.registerAugmentions(
    ("RBN-RADIUS-MIB",
     "rbnRadiusAuthSrvEntry")
)
rbnRadiusAuthSrvEntry.setIndexNames(*radiusAuthServerEntry.getIndexNames())
radiusAccServerEntry.registerAugmentions(
    ("RBN-RADIUS-MIB",
     "rbnRadiusAcctSrvEntry")
)
rbnRadiusAcctSrvEntry.setIndexNames(*radiusAccServerEntry.getIndexNames())

# Managed Objects groups

rbnRadiusAuthGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2352, 2, 32, 2, 2, 1)
)
rbnRadiusAuthGroup.setObjects(
      *(("RBN-RADIUS-MIB", "rbnRadiusAuthPktTimeout"),
        ("RBN-RADIUS-MIB", "rbnRadiusAuthSrvTimeout"),
        ("RBN-RADIUS-MIB", "rbnRadiusAuthDeadtime"),
        ("RBN-RADIUS-MIB", "rbnRadiusAuthTries"),
        ("RBN-RADIUS-MIB", "rbnRadiusAuthSrvState"),
        ("RBN-RADIUS-MIB", "rbnRadiusAuthSrvLastChange"),
        ("RBN-RADIUS-MIB", "rbnRadiusAuthSrvCounterResetTime"),
        ("RBN-RADIUS-MIB", "rbnRadiusAuthSrvSendErrors"))
)
if mibBuilder.loadTexts:
    rbnRadiusAuthGroup.setStatus("deprecated")

rbnRadiusAcctGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2352, 2, 32, 2, 2, 2)
)
rbnRadiusAcctGroup.setObjects(
      *(("RBN-RADIUS-MIB", "rbnRadiusAcctPktTimeout"),
        ("RBN-RADIUS-MIB", "rbnRadiusAcctSrvTimeout"),
        ("RBN-RADIUS-MIB", "rbnRadiusAcctDeadtime"),
        ("RBN-RADIUS-MIB", "rbnRadiusAcctTries"),
        ("RBN-RADIUS-MIB", "rbnRadiusAcctSrvState"),
        ("RBN-RADIUS-MIB", "rbnRadiusAcctSrvLastChange"),
        ("RBN-RADIUS-MIB", "rbnRadiusAcctSrvCounterResetTime"),
        ("RBN-RADIUS-MIB", "rbnRadiusAcctSrvSendErrors"))
)
if mibBuilder.loadTexts:
    rbnRadiusAcctGroup.setStatus("deprecated")

rbnRadiusNotifyGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2352, 2, 32, 2, 2, 3)
)
rbnRadiusNotifyGroup.setObjects(
      *(("RBN-RADIUS-MIB", "rbnRadiusClientPort"),
        ("RBN-RADIUS-MIB", "rbnRadiusContext"),
        ("RBN-RADIUS-MIB", "rbnRadiusReason"),
        ("RBN-RADIUS-MIB", "rbnRadiusUsername"))
)
if mibBuilder.loadTexts:
    rbnRadiusNotifyGroup.setStatus("current")

rbnRadiusAuthGroup2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2352, 2, 32, 2, 2, 6)
)
rbnRadiusAuthGroup2.setObjects(
      *(("RBN-RADIUS-MIB", "rbnRadiusAuthPktTimeout"),
        ("RBN-RADIUS-MIB", "rbnRadiusAuthSrvTimeout"),
        ("RBN-RADIUS-MIB", "rbnRadiusAuthDeadtime"),
        ("RBN-RADIUS-MIB", "rbnRadiusAuthTries"),
        ("RBN-RADIUS-MIB", "rbnRadiusAuthSrvState"),
        ("RBN-RADIUS-MIB", "rbnRadiusAuthSrvLastChange"),
        ("RBN-RADIUS-MIB", "rbnRadiusAuthSrvCounterResetTime"),
        ("RBN-RADIUS-MIB", "rbnRadiusAuthSrvSendErrors"),
        ("RBN-RADIUS-MIB", "rbnRadiusAuthStripDomain"))
)
if mibBuilder.loadTexts:
    rbnRadiusAuthGroup2.setStatus("current")

rbnRadiusAcctGroup2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2352, 2, 32, 2, 2, 7)
)
rbnRadiusAcctGroup2.setObjects(
      *(("RBN-RADIUS-MIB", "rbnRadiusAcctPktTimeout"),
        ("RBN-RADIUS-MIB", "rbnRadiusAcctSrvTimeout"),
        ("RBN-RADIUS-MIB", "rbnRadiusAcctDeadtime"),
        ("RBN-RADIUS-MIB", "rbnRadiusAcctTries"),
        ("RBN-RADIUS-MIB", "rbnRadiusAcctSrvState"),
        ("RBN-RADIUS-MIB", "rbnRadiusAcctSrvLastChange"),
        ("RBN-RADIUS-MIB", "rbnRadiusAcctSrvCounterResetTime"),
        ("RBN-RADIUS-MIB", "rbnRadiusAcctSrvSendErrors"),
        ("RBN-RADIUS-MIB", "rbnRadiusAcctStripDomain"))
)
if mibBuilder.loadTexts:
    rbnRadiusAcctGroup2.setStatus("current")


# Notification objects

rbnRadiusAuthStateChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 2352, 2, 32, 0, 1)
)
rbnRadiusAuthStateChange.setObjects(
      *(("RBN-RADIUS-MIB", "rbnRadiusAuthSrvState"),
        ("RADIUS-AUTH-CLIENT-MIB", "radiusAuthServerAddress"),
        ("RADIUS-AUTH-CLIENT-MIB", "radiusAuthClientServerPortNumber"),
        ("RBN-RADIUS-MIB", "rbnRadiusClientPort"),
        ("RBN-RADIUS-MIB", "rbnRadiusContext"),
        ("RBN-RADIUS-MIB", "rbnRadiusReason"),
        ("RBN-RADIUS-MIB", "rbnRadiusUsername"))
)
if mibBuilder.loadTexts:
    rbnRadiusAuthStateChange.setStatus(
        "current"
    )

rbnRadiusAcctStateChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 2352, 2, 32, 0, 2)
)
rbnRadiusAcctStateChange.setObjects(
      *(("RBN-RADIUS-MIB", "rbnRadiusAcctSrvState"),
        ("RADIUS-ACC-CLIENT-MIB", "radiusAccServerAddress"),
        ("RADIUS-ACC-CLIENT-MIB", "radiusAccClientServerPortNumber"),
        ("RBN-RADIUS-MIB", "rbnRadiusClientPort"),
        ("RBN-RADIUS-MIB", "rbnRadiusContext"),
        ("RBN-RADIUS-MIB", "rbnRadiusReason"),
        ("RBN-RADIUS-MIB", "rbnRadiusUsername"))
)
if mibBuilder.loadTexts:
    rbnRadiusAcctStateChange.setStatus(
        "current"
    )


# Notifications groups

rbnRadiusAuthNotifyGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 2352, 2, 32, 2, 2, 4)
)
rbnRadiusAuthNotifyGroup.setObjects(
    ("RBN-RADIUS-MIB", "rbnRadiusAuthStateChange")
)
if mibBuilder.loadTexts:
    rbnRadiusAuthNotifyGroup.setStatus(
        "current"
    )

rbnRadiusAcctNotifyGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 2352, 2, 32, 2, 2, 5)
)
rbnRadiusAcctNotifyGroup.setObjects(
    ("RBN-RADIUS-MIB", "rbnRadiusAcctStateChange")
)
if mibBuilder.loadTexts:
    rbnRadiusAcctNotifyGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

rbnRadiusCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 2352, 2, 32, 2, 1, 1)
)
if mibBuilder.loadTexts:
    rbnRadiusCompliance.setStatus(
        "deprecated"
    )

rbnRadiusCompliance2 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 2352, 2, 32, 2, 1, 2)
)
if mibBuilder.loadTexts:
    rbnRadiusCompliance2.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "RBN-RADIUS-MIB",
    **{"RbnRadiusServerState": RbnRadiusServerState,
       "RbnRadiusServerReason": RbnRadiusServerReason,
       "rbnRadiusMib": rbnRadiusMib,
       "rbnRadiusMIBNotifications": rbnRadiusMIBNotifications,
       "rbnRadiusAuthStateChange": rbnRadiusAuthStateChange,
       "rbnRadiusAcctStateChange": rbnRadiusAcctStateChange,
       "rbnRadiusMIBObjects": rbnRadiusMIBObjects,
       "rbnRadiusAuthObjects": rbnRadiusAuthObjects,
       "rbnRadiusAuthPktTimeout": rbnRadiusAuthPktTimeout,
       "rbnRadiusAuthSrvTimeout": rbnRadiusAuthSrvTimeout,
       "rbnRadiusAuthDeadtime": rbnRadiusAuthDeadtime,
       "rbnRadiusAuthTries": rbnRadiusAuthTries,
       "rbnRadiusAuthSrvTable": rbnRadiusAuthSrvTable,
       "rbnRadiusAuthSrvEntry": rbnRadiusAuthSrvEntry,
       "rbnRadiusAuthSrvState": rbnRadiusAuthSrvState,
       "rbnRadiusAuthSrvLastChange": rbnRadiusAuthSrvLastChange,
       "rbnRadiusAuthSrvCounterResetTime": rbnRadiusAuthSrvCounterResetTime,
       "rbnRadiusAuthSrvSendErrors": rbnRadiusAuthSrvSendErrors,
       "rbnRadiusAuthStripDomain": rbnRadiusAuthStripDomain,
       "rbnRadiusAcctObjects": rbnRadiusAcctObjects,
       "rbnRadiusAcctPktTimeout": rbnRadiusAcctPktTimeout,
       "rbnRadiusAcctSrvTimeout": rbnRadiusAcctSrvTimeout,
       "rbnRadiusAcctDeadtime": rbnRadiusAcctDeadtime,
       "rbnRadiusAcctTries": rbnRadiusAcctTries,
       "rbnRadiusAcctSrvTable": rbnRadiusAcctSrvTable,
       "rbnRadiusAcctSrvEntry": rbnRadiusAcctSrvEntry,
       "rbnRadiusAcctSrvState": rbnRadiusAcctSrvState,
       "rbnRadiusAcctSrvLastChange": rbnRadiusAcctSrvLastChange,
       "rbnRadiusAcctSrvCounterResetTime": rbnRadiusAcctSrvCounterResetTime,
       "rbnRadiusAcctSrvSendErrors": rbnRadiusAcctSrvSendErrors,
       "rbnRadiusAcctStripDomain": rbnRadiusAcctStripDomain,
       "rbnRadiusNotifyObjects": rbnRadiusNotifyObjects,
       "rbnRadiusClientPort": rbnRadiusClientPort,
       "rbnRadiusContext": rbnRadiusContext,
       "rbnRadiusReason": rbnRadiusReason,
       "rbnRadiusUsername": rbnRadiusUsername,
       "rbnRadiusMIBConformance": rbnRadiusMIBConformance,
       "rbnRadiusCompliances": rbnRadiusCompliances,
       "rbnRadiusCompliance": rbnRadiusCompliance,
       "rbnRadiusCompliance2": rbnRadiusCompliance2,
       "rbnRadiusGroups": rbnRadiusGroups,
       "rbnRadiusAuthGroup": rbnRadiusAuthGroup,
       "rbnRadiusAcctGroup": rbnRadiusAcctGroup,
       "rbnRadiusNotifyGroup": rbnRadiusNotifyGroup,
       "rbnRadiusAuthNotifyGroup": rbnRadiusAuthNotifyGroup,
       "rbnRadiusAcctNotifyGroup": rbnRadiusAcctNotifyGroup,
       "rbnRadiusAuthGroup2": rbnRadiusAuthGroup2,
       "rbnRadiusAcctGroup2": rbnRadiusAcctGroup2}
)
