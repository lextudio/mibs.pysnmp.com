# SNMP MIB module (BAY-STACK-RADIUS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/BAY-STACK-RADIUS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:46:20 2024
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

(InetAddress,
 InetAddressType,
 InetPortNumber) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType",
    "InetPortNumber")

(radiusDynAuthClientEntry,) = mibBuilder.importSymbols(
    "RADIUS-DYNAUTH-SERVER-MIB",
    "radiusDynAuthClientEntry")

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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention",
    "TruthValue")

(bayStackMibs,) = mibBuilder.importSymbols(
    "SYNOPTICS-ROOT-MIB",
    "bayStackMibs")


# MODULE-IDENTITY

bayStackRadiusMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 45, 5, 21)
)
bayStackRadiusMib.setRevisions(
        ("2015-07-23 00:00",
         "2014-10-20 00:00",
         "2012-03-15 00:00",
         "2010-10-15 00:00",
         "2010-10-14 00:00",
         "2010-09-07 00:00",
         "2010-02-10 00:00",
         "2009-10-13 00:00",
         "2009-05-28 00:00",
         "2009-04-16 00:00",
         "2009-03-30 00:00",
         "2008-10-30 00:00",
         "2008-05-29 00:00",
         "2008-03-25 00:00",
         "2007-04-03 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_BsRadiusNotifications_ObjectIdentity = ObjectIdentity
bsRadiusNotifications = _BsRadiusNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 5, 21, 0)
)
_BsRadiusObjects_ObjectIdentity = ObjectIdentity
bsRadiusObjects = _BsRadiusObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 5, 21, 1)
)
_BsRadiusScalars_ObjectIdentity = ObjectIdentity
bsRadiusScalars = _BsRadiusScalars_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 5, 21, 1, 1)
)


class _BsRadiusUseMgmtIp_Type(TruthValue):
    """Custom type bsRadiusUseMgmtIp based on TruthValue"""


_BsRadiusUseMgmtIp_Object = MibScalar
bsRadiusUseMgmtIp = _BsRadiusUseMgmtIp_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 21, 1, 1, 1),
    _BsRadiusUseMgmtIp_Type()
)
bsRadiusUseMgmtIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bsRadiusUseMgmtIp.setStatus("current")


class _BsRadiusAccountingEnabled_Type(TruthValue):
    """Custom type bsRadiusAccountingEnabled based on TruthValue"""


_BsRadiusAccountingEnabled_Object = MibScalar
bsRadiusAccountingEnabled = _BsRadiusAccountingEnabled_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 21, 1, 1, 2),
    _BsRadiusAccountingEnabled_Type()
)
bsRadiusAccountingEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bsRadiusAccountingEnabled.setStatus("current")


class _BsRadiusPasswordFallbackEnabled_Type(TruthValue):
    """Custom type bsRadiusPasswordFallbackEnabled based on TruthValue"""


_BsRadiusPasswordFallbackEnabled_Object = MibScalar
bsRadiusPasswordFallbackEnabled = _BsRadiusPasswordFallbackEnabled_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 21, 1, 1, 3),
    _BsRadiusPasswordFallbackEnabled_Type()
)
bsRadiusPasswordFallbackEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bsRadiusPasswordFallbackEnabled.setStatus("current")


class _BsRadiusAccountingPort_Type(InetPortNumber):
    """Custom type bsRadiusAccountingPort based on InetPortNumber"""
    defaultValue = 1813


_BsRadiusAccountingPort_Object = MibScalar
bsRadiusAccountingPort = _BsRadiusAccountingPort_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 21, 1, 1, 4),
    _BsRadiusAccountingPort_Type()
)
bsRadiusAccountingPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bsRadiusAccountingPort.setStatus("current")


class _BsRadiusAccountingInterimUpdates_Type(TruthValue):
    """Custom type bsRadiusAccountingInterimUpdates based on TruthValue"""


_BsRadiusAccountingInterimUpdates_Object = MibScalar
bsRadiusAccountingInterimUpdates = _BsRadiusAccountingInterimUpdates_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 21, 1, 1, 5),
    _BsRadiusAccountingInterimUpdates_Type()
)
bsRadiusAccountingInterimUpdates.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bsRadiusAccountingInterimUpdates.setStatus("current")


class _BsRadiusAccountingInterimUpdatesInterval_Type(Unsigned32):
    """Custom type bsRadiusAccountingInterimUpdatesInterval based on Unsigned32"""
    defaultValue = 60

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(60, 3600),
    )


_BsRadiusAccountingInterimUpdatesInterval_Type.__name__ = "Unsigned32"
_BsRadiusAccountingInterimUpdatesInterval_Object = MibScalar
bsRadiusAccountingInterimUpdatesInterval = _BsRadiusAccountingInterimUpdatesInterval_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 21, 1, 1, 6),
    _BsRadiusAccountingInterimUpdatesInterval_Type()
)
bsRadiusAccountingInterimUpdatesInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bsRadiusAccountingInterimUpdatesInterval.setStatus("current")
if mibBuilder.loadTexts:
    bsRadiusAccountingInterimUpdatesInterval.setUnits("seconds")


class _BsRadiusAccountingInterimUpdatesIntervalSource_Type(Integer32):
    """Custom type bsRadiusAccountingInterimUpdatesIntervalSource based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("configuredValue", 1),
          ("radiusServer", 2))
    )


_BsRadiusAccountingInterimUpdatesIntervalSource_Type.__name__ = "Integer32"
_BsRadiusAccountingInterimUpdatesIntervalSource_Object = MibScalar
bsRadiusAccountingInterimUpdatesIntervalSource = _BsRadiusAccountingInterimUpdatesIntervalSource_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 21, 1, 1, 7),
    _BsRadiusAccountingInterimUpdatesIntervalSource_Type()
)
bsRadiusAccountingInterimUpdatesIntervalSource.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bsRadiusAccountingInterimUpdatesIntervalSource.setStatus("current")
_BsRadiusDynAuthReplayProtection_Type = TruthValue
_BsRadiusDynAuthReplayProtection_Object = MibScalar
bsRadiusDynAuthReplayProtection = _BsRadiusDynAuthReplayProtection_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 21, 1, 1, 8),
    _BsRadiusDynAuthReplayProtection_Type()
)
bsRadiusDynAuthReplayProtection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bsRadiusDynAuthReplayProtection.setStatus("current")


class _BsRadiusReachability_Type(Integer32):
    """Custom type bsRadiusReachability based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("useIcmp", 2),
          ("useRadius", 1))
    )


_BsRadiusReachability_Type.__name__ = "Integer32"
_BsRadiusReachability_Object = MibScalar
bsRadiusReachability = _BsRadiusReachability_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 21, 1, 1, 9),
    _BsRadiusReachability_Type()
)
bsRadiusReachability.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bsRadiusReachability.setStatus("current")


class _BsRadiusReachabilityUserName_Type(DisplayString):
    """Custom type bsRadiusReachabilityUserName based on DisplayString"""
    defaultValue = OctetString("avaya")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_BsRadiusReachabilityUserName_Type.__name__ = "DisplayString"
_BsRadiusReachabilityUserName_Object = MibScalar
bsRadiusReachabilityUserName = _BsRadiusReachabilityUserName_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 21, 1, 1, 10),
    _BsRadiusReachabilityUserName_Type()
)
bsRadiusReachabilityUserName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bsRadiusReachabilityUserName.setStatus("current")


class _BsRadiusReachabilityPassword_Type(DisplayString):
    """Custom type bsRadiusReachabilityPassword based on DisplayString"""
    defaultValue = OctetString("avaya")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_BsRadiusReachabilityPassword_Type.__name__ = "DisplayString"
_BsRadiusReachabilityPassword_Object = MibScalar
bsRadiusReachabilityPassword = _BsRadiusReachabilityPassword_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 21, 1, 1, 11),
    _BsRadiusReachabilityPassword_Type()
)
bsRadiusReachabilityPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bsRadiusReachabilityPassword.setStatus("current")


class _BsRadiusEncapsulationProtocol_Type(Integer32):
    """Custom type bsRadiusEncapsulationProtocol based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ms-chap-v2", 2),
          ("pap", 1))
    )


_BsRadiusEncapsulationProtocol_Type.__name__ = "Integer32"
_BsRadiusEncapsulationProtocol_Object = MibScalar
bsRadiusEncapsulationProtocol = _BsRadiusEncapsulationProtocol_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 21, 1, 1, 12),
    _BsRadiusEncapsulationProtocol_Type()
)
bsRadiusEncapsulationProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bsRadiusEncapsulationProtocol.setStatus("current")


class _BsRadiusReachabilityTimeout_Type(Integer32):
    """Custom type bsRadiusReachabilityTimeout based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 60),
    )


_BsRadiusReachabilityTimeout_Type.__name__ = "Integer32"
_BsRadiusReachabilityTimeout_Object = MibScalar
bsRadiusReachabilityTimeout = _BsRadiusReachabilityTimeout_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 21, 1, 1, 13),
    _BsRadiusReachabilityTimeout_Type()
)
bsRadiusReachabilityTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bsRadiusReachabilityTimeout.setStatus("current")
if mibBuilder.loadTexts:
    bsRadiusReachabilityTimeout.setUnits("seconds")


class _BsRadiusReachabilityRetry_Type(Integer32):
    """Custom type bsRadiusReachabilityRetry based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5),
    )


_BsRadiusReachabilityRetry_Type.__name__ = "Integer32"
_BsRadiusReachabilityRetry_Object = MibScalar
bsRadiusReachabilityRetry = _BsRadiusReachabilityRetry_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 21, 1, 1, 14),
    _BsRadiusReachabilityRetry_Type()
)
bsRadiusReachabilityRetry.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bsRadiusReachabilityRetry.setStatus("current")


class _BsRadiusReachabilityBadTimer_Type(Integer32):
    """Custom type bsRadiusReachabilityBadTimer based on Integer32"""
    defaultValue = 60

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(30, 600),
    )


_BsRadiusReachabilityBadTimer_Type.__name__ = "Integer32"
_BsRadiusReachabilityBadTimer_Object = MibScalar
bsRadiusReachabilityBadTimer = _BsRadiusReachabilityBadTimer_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 21, 1, 1, 15),
    _BsRadiusReachabilityBadTimer_Type()
)
bsRadiusReachabilityBadTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bsRadiusReachabilityBadTimer.setStatus("current")
if mibBuilder.loadTexts:
    bsRadiusReachabilityBadTimer.setUnits("seconds")


class _BsRadiusReachabilityGoodTimer_Type(Integer32):
    """Custom type bsRadiusReachabilityGoodTimer based on Integer32"""
    defaultValue = 180

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(30, 600),
    )


_BsRadiusReachabilityGoodTimer_Type.__name__ = "Integer32"
_BsRadiusReachabilityGoodTimer_Object = MibScalar
bsRadiusReachabilityGoodTimer = _BsRadiusReachabilityGoodTimer_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 21, 1, 1, 16),
    _BsRadiusReachabilityGoodTimer_Type()
)
bsRadiusReachabilityGoodTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bsRadiusReachabilityGoodTimer.setStatus("current")
if mibBuilder.loadTexts:
    bsRadiusReachabilityGoodTimer.setUnits("seconds")
_BsRadiusServerTable_Object = MibTable
bsRadiusServerTable = _BsRadiusServerTable_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 21, 1, 2)
)
if mibBuilder.loadTexts:
    bsRadiusServerTable.setStatus("current")
_BsRadiusServerEntry_Object = MibTableRow
bsRadiusServerEntry = _BsRadiusServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 21, 1, 2, 1)
)
bsRadiusServerEntry.setIndexNames(
    (0, "BAY-STACK-RADIUS-MIB", "bsRadiusServerIndex"),
)
if mibBuilder.loadTexts:
    bsRadiusServerEntry.setStatus("current")


class _BsRadiusServerIndex_Type(Integer32):
    """Custom type bsRadiusServerIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_BsRadiusServerIndex_Type.__name__ = "Integer32"
_BsRadiusServerIndex_Object = MibTableColumn
bsRadiusServerIndex = _BsRadiusServerIndex_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 21, 1, 2, 1, 1),
    _BsRadiusServerIndex_Type()
)
bsRadiusServerIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    bsRadiusServerIndex.setStatus("current")


class _BsRadiusServerPriority_Type(Integer32):
    """Custom type bsRadiusServerPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_BsRadiusServerPriority_Type.__name__ = "Integer32"
_BsRadiusServerPriority_Object = MibTableColumn
bsRadiusServerPriority = _BsRadiusServerPriority_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 21, 1, 2, 1, 2),
    _BsRadiusServerPriority_Type()
)
bsRadiusServerPriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bsRadiusServerPriority.setStatus("current")
_BsRadiusServerAddressType_Type = InetAddressType
_BsRadiusServerAddressType_Object = MibTableColumn
bsRadiusServerAddressType = _BsRadiusServerAddressType_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 21, 1, 2, 1, 3),
    _BsRadiusServerAddressType_Type()
)
bsRadiusServerAddressType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bsRadiusServerAddressType.setStatus("current")
_BsRadiusServerAddress_Type = InetAddress
_BsRadiusServerAddress_Object = MibTableColumn
bsRadiusServerAddress = _BsRadiusServerAddress_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 21, 1, 2, 1, 4),
    _BsRadiusServerAddress_Type()
)
bsRadiusServerAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bsRadiusServerAddress.setStatus("current")
_BsRadiusServerUdpPort_Type = InetPortNumber
_BsRadiusServerUdpPort_Object = MibTableColumn
bsRadiusServerUdpPort = _BsRadiusServerUdpPort_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 21, 1, 2, 1, 5),
    _BsRadiusServerUdpPort_Type()
)
bsRadiusServerUdpPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bsRadiusServerUdpPort.setStatus("current")
_BsRadiusServerTimeout_Type = Integer32
_BsRadiusServerTimeout_Object = MibTableColumn
bsRadiusServerTimeout = _BsRadiusServerTimeout_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 21, 1, 2, 1, 6),
    _BsRadiusServerTimeout_Type()
)
bsRadiusServerTimeout.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bsRadiusServerTimeout.setStatus("current")
if mibBuilder.loadTexts:
    bsRadiusServerTimeout.setUnits("seconds")


class _BsRadiusServerSecret_Type(OctetString):
    """Custom type bsRadiusServerSecret based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_BsRadiusServerSecret_Type.__name__ = "OctetString"
_BsRadiusServerSecret_Object = MibTableColumn
bsRadiusServerSecret = _BsRadiusServerSecret_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 21, 1, 2, 1, 7),
    _BsRadiusServerSecret_Type()
)
bsRadiusServerSecret.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bsRadiusServerSecret.setStatus("current")
_BsRadiusServerRowStatus_Type = RowStatus
_BsRadiusServerRowStatus_Object = MibTableColumn
bsRadiusServerRowStatus = _BsRadiusServerRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 21, 1, 2, 1, 8),
    _BsRadiusServerRowStatus_Type()
)
bsRadiusServerRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bsRadiusServerRowStatus.setStatus("current")
_BsRadiusServerAccountingPort_Type = InetPortNumber
_BsRadiusServerAccountingPort_Object = MibTableColumn
bsRadiusServerAccountingPort = _BsRadiusServerAccountingPort_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 21, 1, 2, 1, 9),
    _BsRadiusServerAccountingPort_Type()
)
bsRadiusServerAccountingPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bsRadiusServerAccountingPort.setStatus("current")


class _BsRadiusServerAccountingEnabled_Type(TruthValue):
    """Custom type bsRadiusServerAccountingEnabled based on TruthValue"""


_BsRadiusServerAccountingEnabled_Object = MibTableColumn
bsRadiusServerAccountingEnabled = _BsRadiusServerAccountingEnabled_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 21, 1, 2, 1, 10),
    _BsRadiusServerAccountingEnabled_Type()
)
bsRadiusServerAccountingEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bsRadiusServerAccountingEnabled.setStatus("current")


class _BsRadiusServerRetryLimit_Type(Integer32):
    """Custom type bsRadiusServerRetryLimit based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5),
    )


_BsRadiusServerRetryLimit_Type.__name__ = "Integer32"
_BsRadiusServerRetryLimit_Object = MibTableColumn
bsRadiusServerRetryLimit = _BsRadiusServerRetryLimit_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 21, 1, 2, 1, 11),
    _BsRadiusServerRetryLimit_Type()
)
bsRadiusServerRetryLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bsRadiusServerRetryLimit.setStatus("current")
_BsRadiusDynAuthClientTable_Object = MibTable
bsRadiusDynAuthClientTable = _BsRadiusDynAuthClientTable_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 21, 1, 3)
)
if mibBuilder.loadTexts:
    bsRadiusDynAuthClientTable.setStatus("current")
_BsRadiusDynAuthClientEntry_Object = MibTableRow
bsRadiusDynAuthClientEntry = _BsRadiusDynAuthClientEntry_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 21, 1, 3, 1)
)
bsRadiusDynAuthClientEntry.setIndexNames(
    (0, "BAY-STACK-RADIUS-MIB", "bsRadiusDynAuthClientAddressType"),
    (0, "BAY-STACK-RADIUS-MIB", "bsRadiusDynAuthClientAddress"),
)
if mibBuilder.loadTexts:
    bsRadiusDynAuthClientEntry.setStatus("current")
_BsRadiusDynAuthClientAddressType_Type = InetAddressType
_BsRadiusDynAuthClientAddressType_Object = MibTableColumn
bsRadiusDynAuthClientAddressType = _BsRadiusDynAuthClientAddressType_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 21, 1, 3, 1, 1),
    _BsRadiusDynAuthClientAddressType_Type()
)
bsRadiusDynAuthClientAddressType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    bsRadiusDynAuthClientAddressType.setStatus("current")


class _BsRadiusDynAuthClientAddress_Type(InetAddress):
    """Custom type bsRadiusDynAuthClientAddress based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 113),
    )


_BsRadiusDynAuthClientAddress_Type.__name__ = "InetAddress"
_BsRadiusDynAuthClientAddress_Object = MibTableColumn
bsRadiusDynAuthClientAddress = _BsRadiusDynAuthClientAddress_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 21, 1, 3, 1, 2),
    _BsRadiusDynAuthClientAddress_Type()
)
bsRadiusDynAuthClientAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    bsRadiusDynAuthClientAddress.setStatus("current")


class _BsRadiusDynAuthClientUdpPort_Type(InetPortNumber):
    """Custom type bsRadiusDynAuthClientUdpPort based on InetPortNumber"""
    defaultValue = 3799


_BsRadiusDynAuthClientUdpPort_Object = MibTableColumn
bsRadiusDynAuthClientUdpPort = _BsRadiusDynAuthClientUdpPort_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 21, 1, 3, 1, 3),
    _BsRadiusDynAuthClientUdpPort_Type()
)
bsRadiusDynAuthClientUdpPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bsRadiusDynAuthClientUdpPort.setStatus("current")


class _BsRadiusDynAuthClientSecret_Type(OctetString):
    """Custom type bsRadiusDynAuthClientSecret based on OctetString"""
    defaultHexValue = ""

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_BsRadiusDynAuthClientSecret_Type.__name__ = "OctetString"
_BsRadiusDynAuthClientSecret_Object = MibTableColumn
bsRadiusDynAuthClientSecret = _BsRadiusDynAuthClientSecret_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 21, 1, 3, 1, 4),
    _BsRadiusDynAuthClientSecret_Type()
)
bsRadiusDynAuthClientSecret.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bsRadiusDynAuthClientSecret.setStatus("current")


class _BsRadiusDynAuthClientEnabled_Type(TruthValue):
    """Custom type bsRadiusDynAuthClientEnabled based on TruthValue"""


_BsRadiusDynAuthClientEnabled_Object = MibTableColumn
bsRadiusDynAuthClientEnabled = _BsRadiusDynAuthClientEnabled_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 21, 1, 3, 1, 5),
    _BsRadiusDynAuthClientEnabled_Type()
)
bsRadiusDynAuthClientEnabled.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bsRadiusDynAuthClientEnabled.setStatus("current")


class _BsRadiusDynAuthClientProcessDisconnectRequests_Type(TruthValue):
    """Custom type bsRadiusDynAuthClientProcessDisconnectRequests based on TruthValue"""


_BsRadiusDynAuthClientProcessDisconnectRequests_Object = MibTableColumn
bsRadiusDynAuthClientProcessDisconnectRequests = _BsRadiusDynAuthClientProcessDisconnectRequests_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 21, 1, 3, 1, 6),
    _BsRadiusDynAuthClientProcessDisconnectRequests_Type()
)
bsRadiusDynAuthClientProcessDisconnectRequests.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bsRadiusDynAuthClientProcessDisconnectRequests.setStatus("current")


class _BsRadiusDynAuthClientProcessCoARequests_Type(TruthValue):
    """Custom type bsRadiusDynAuthClientProcessCoARequests based on TruthValue"""


_BsRadiusDynAuthClientProcessCoARequests_Object = MibTableColumn
bsRadiusDynAuthClientProcessCoARequests = _BsRadiusDynAuthClientProcessCoARequests_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 21, 1, 3, 1, 7),
    _BsRadiusDynAuthClientProcessCoARequests_Type()
)
bsRadiusDynAuthClientProcessCoARequests.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bsRadiusDynAuthClientProcessCoARequests.setStatus("current")
_BsRadiusDynAuthClientRowStatus_Type = RowStatus
_BsRadiusDynAuthClientRowStatus_Object = MibTableColumn
bsRadiusDynAuthClientRowStatus = _BsRadiusDynAuthClientRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 21, 1, 3, 1, 8),
    _BsRadiusDynAuthClientRowStatus_Type()
)
bsRadiusDynAuthClientRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bsRadiusDynAuthClientRowStatus.setStatus("current")
_BsRadiusDynAuthClientReplayProtection_Type = TruthValue
_BsRadiusDynAuthClientReplayProtection_Object = MibTableColumn
bsRadiusDynAuthClientReplayProtection = _BsRadiusDynAuthClientReplayProtection_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 21, 1, 3, 1, 9),
    _BsRadiusDynAuthClientReplayProtection_Type()
)
bsRadiusDynAuthClientReplayProtection.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bsRadiusDynAuthClientReplayProtection.setStatus("current")


class _BsRadiusDynAuthClientProcessReAuthRequests_Type(TruthValue):
    """Custom type bsRadiusDynAuthClientProcessReAuthRequests based on TruthValue"""


_BsRadiusDynAuthClientProcessReAuthRequests_Object = MibTableColumn
bsRadiusDynAuthClientProcessReAuthRequests = _BsRadiusDynAuthClientProcessReAuthRequests_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 21, 1, 3, 1, 10),
    _BsRadiusDynAuthClientProcessReAuthRequests_Type()
)
bsRadiusDynAuthClientProcessReAuthRequests.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bsRadiusDynAuthClientProcessReAuthRequests.setStatus("current")
_BsRadiusExtDynAuthClientTable_Object = MibTable
bsRadiusExtDynAuthClientTable = _BsRadiusExtDynAuthClientTable_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 21, 1, 4)
)
if mibBuilder.loadTexts:
    bsRadiusExtDynAuthClientTable.setStatus("current")
_BsRadiusExtDynAuthClientEntry_Object = MibTableRow
bsRadiusExtDynAuthClientEntry = _BsRadiusExtDynAuthClientEntry_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 21, 1, 4, 1)
)
if mibBuilder.loadTexts:
    bsRadiusExtDynAuthClientEntry.setStatus("current")
_BsRadiusExtDynAuthServRcRequests_Type = Counter32
_BsRadiusExtDynAuthServRcRequests_Object = MibTableColumn
bsRadiusExtDynAuthServRcRequests = _BsRadiusExtDynAuthServRcRequests_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 21, 1, 4, 1, 1),
    _BsRadiusExtDynAuthServRcRequests_Type()
)
bsRadiusExtDynAuthServRcRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsRadiusExtDynAuthServRcRequests.setStatus("current")
if mibBuilder.loadTexts:
    bsRadiusExtDynAuthServRcRequests.setUnits("requests")
_BsRadiusExtDynAuthServRcAuthOnlyRequests_Type = Counter32
_BsRadiusExtDynAuthServRcAuthOnlyRequests_Object = MibTableColumn
bsRadiusExtDynAuthServRcAuthOnlyRequests = _BsRadiusExtDynAuthServRcAuthOnlyRequests_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 21, 1, 4, 1, 2),
    _BsRadiusExtDynAuthServRcAuthOnlyRequests_Type()
)
bsRadiusExtDynAuthServRcAuthOnlyRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsRadiusExtDynAuthServRcAuthOnlyRequests.setStatus("current")
if mibBuilder.loadTexts:
    bsRadiusExtDynAuthServRcAuthOnlyRequests.setUnits("requests")
_BsRadiusExtDynAuthServRcDupRequests_Type = Counter32
_BsRadiusExtDynAuthServRcDupRequests_Object = MibTableColumn
bsRadiusExtDynAuthServRcDupRequests = _BsRadiusExtDynAuthServRcDupRequests_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 21, 1, 4, 1, 3),
    _BsRadiusExtDynAuthServRcDupRequests_Type()
)
bsRadiusExtDynAuthServRcDupRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsRadiusExtDynAuthServRcDupRequests.setStatus("current")
if mibBuilder.loadTexts:
    bsRadiusExtDynAuthServRcDupRequests.setUnits("requests")
_BsRadiusExtDynAuthServRcAcks_Type = Counter32
_BsRadiusExtDynAuthServRcAcks_Object = MibTableColumn
bsRadiusExtDynAuthServRcAcks = _BsRadiusExtDynAuthServRcAcks_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 21, 1, 4, 1, 4),
    _BsRadiusExtDynAuthServRcAcks_Type()
)
bsRadiusExtDynAuthServRcAcks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsRadiusExtDynAuthServRcAcks.setStatus("current")
if mibBuilder.loadTexts:
    bsRadiusExtDynAuthServRcAcks.setUnits("requests")
_BsRadiusExtDynAuthServRcNacks_Type = Counter32
_BsRadiusExtDynAuthServRcNacks_Object = MibTableColumn
bsRadiusExtDynAuthServRcNacks = _BsRadiusExtDynAuthServRcNacks_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 21, 1, 4, 1, 5),
    _BsRadiusExtDynAuthServRcNacks_Type()
)
bsRadiusExtDynAuthServRcNacks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsRadiusExtDynAuthServRcNacks.setStatus("current")
if mibBuilder.loadTexts:
    bsRadiusExtDynAuthServRcNacks.setUnits("requests")
_BsRadiusExtDynAuthServRcNacksAuthOnlyRequests_Type = Counter32
_BsRadiusExtDynAuthServRcNacksAuthOnlyRequests_Object = MibTableColumn
bsRadiusExtDynAuthServRcNacksAuthOnlyRequests = _BsRadiusExtDynAuthServRcNacksAuthOnlyRequests_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 21, 1, 4, 1, 6),
    _BsRadiusExtDynAuthServRcNacksAuthOnlyRequests_Type()
)
bsRadiusExtDynAuthServRcNacksAuthOnlyRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsRadiusExtDynAuthServRcNacksAuthOnlyRequests.setStatus("current")
if mibBuilder.loadTexts:
    bsRadiusExtDynAuthServRcNacksAuthOnlyRequests.setUnits("requests")
_BsRadiusExtDynAuthServRcNacksNoSess_Type = Counter32
_BsRadiusExtDynAuthServRcNacksNoSess_Object = MibTableColumn
bsRadiusExtDynAuthServRcNacksNoSess = _BsRadiusExtDynAuthServRcNacksNoSess_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 21, 1, 4, 1, 7),
    _BsRadiusExtDynAuthServRcNacksNoSess_Type()
)
bsRadiusExtDynAuthServRcNacksNoSess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsRadiusExtDynAuthServRcNacksNoSess.setStatus("current")
if mibBuilder.loadTexts:
    bsRadiusExtDynAuthServRcNacksNoSess.setUnits("requests")
_BsRadiusExtDynAuthServRcSessReauthenticated_Type = Counter32
_BsRadiusExtDynAuthServRcSessReauthenticated_Object = MibTableColumn
bsRadiusExtDynAuthServRcSessReauthenticated = _BsRadiusExtDynAuthServRcSessReauthenticated_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 21, 1, 4, 1, 8),
    _BsRadiusExtDynAuthServRcSessReauthenticated_Type()
)
bsRadiusExtDynAuthServRcSessReauthenticated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsRadiusExtDynAuthServRcSessReauthenticated.setStatus("current")
if mibBuilder.loadTexts:
    bsRadiusExtDynAuthServRcSessReauthenticated.setUnits("requests")
_BsRadiusExtDynAuthServRcMalformed_Type = Counter32
_BsRadiusExtDynAuthServRcMalformed_Object = MibTableColumn
bsRadiusExtDynAuthServRcMalformed = _BsRadiusExtDynAuthServRcMalformed_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 21, 1, 4, 1, 9),
    _BsRadiusExtDynAuthServRcMalformed_Type()
)
bsRadiusExtDynAuthServRcMalformed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsRadiusExtDynAuthServRcMalformed.setStatus("current")
if mibBuilder.loadTexts:
    bsRadiusExtDynAuthServRcMalformed.setUnits("requests")
_BsRadiusExtDynAuthServRcDropped_Type = Counter32
_BsRadiusExtDynAuthServRcDropped_Object = MibTableColumn
bsRadiusExtDynAuthServRcDropped = _BsRadiusExtDynAuthServRcDropped_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 21, 1, 4, 1, 10),
    _BsRadiusExtDynAuthServRcDropped_Type()
)
bsRadiusExtDynAuthServRcDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsRadiusExtDynAuthServRcDropped.setStatus("current")
if mibBuilder.loadTexts:
    bsRadiusExtDynAuthServRcDropped.setUnits("requests")
_BsRadiusExtDynAuthServRcBadAuths_Type = Counter32
_BsRadiusExtDynAuthServRcBadAuths_Object = MibTableColumn
bsRadiusExtDynAuthServRcBadAuths = _BsRadiusExtDynAuthServRcBadAuths_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 21, 1, 4, 1, 11),
    _BsRadiusExtDynAuthServRcBadAuths_Type()
)
bsRadiusExtDynAuthServRcBadAuths.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsRadiusExtDynAuthServRcBadAuths.setStatus("current")
if mibBuilder.loadTexts:
    bsRadiusExtDynAuthServRcBadAuths.setUnits("requests")
radiusDynAuthClientEntry.registerAugmentions(
    ("BAY-STACK-RADIUS-MIB",
     "bsRadiusExtDynAuthClientEntry")
)
bsRadiusExtDynAuthClientEntry.setIndexNames(*radiusDynAuthClientEntry.getIndexNames())

# Managed Objects groups


# Notification objects

bsRadiusReachabilityServerDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 45, 5, 21, 0, 1)
)
bsRadiusReachabilityServerDown.setObjects(
      *(("BAY-STACK-RADIUS-MIB", "bsRadiusServerAddressType"),
        ("BAY-STACK-RADIUS-MIB", "bsRadiusServerAddress"))
)
if mibBuilder.loadTexts:
    bsRadiusReachabilityServerDown.setStatus(
        "current"
    )

bsRadiusReachabilityServerUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 45, 5, 21, 0, 2)
)
bsRadiusReachabilityServerUp.setObjects(
      *(("BAY-STACK-RADIUS-MIB", "bsRadiusServerAddressType"),
        ("BAY-STACK-RADIUS-MIB", "bsRadiusServerAddress"))
)
if mibBuilder.loadTexts:
    bsRadiusReachabilityServerUp.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "BAY-STACK-RADIUS-MIB",
    **{"bayStackRadiusMib": bayStackRadiusMib,
       "bsRadiusNotifications": bsRadiusNotifications,
       "bsRadiusReachabilityServerDown": bsRadiusReachabilityServerDown,
       "bsRadiusReachabilityServerUp": bsRadiusReachabilityServerUp,
       "bsRadiusObjects": bsRadiusObjects,
       "bsRadiusScalars": bsRadiusScalars,
       "bsRadiusUseMgmtIp": bsRadiusUseMgmtIp,
       "bsRadiusAccountingEnabled": bsRadiusAccountingEnabled,
       "bsRadiusPasswordFallbackEnabled": bsRadiusPasswordFallbackEnabled,
       "bsRadiusAccountingPort": bsRadiusAccountingPort,
       "bsRadiusAccountingInterimUpdates": bsRadiusAccountingInterimUpdates,
       "bsRadiusAccountingInterimUpdatesInterval": bsRadiusAccountingInterimUpdatesInterval,
       "bsRadiusAccountingInterimUpdatesIntervalSource": bsRadiusAccountingInterimUpdatesIntervalSource,
       "bsRadiusDynAuthReplayProtection": bsRadiusDynAuthReplayProtection,
       "bsRadiusReachability": bsRadiusReachability,
       "bsRadiusReachabilityUserName": bsRadiusReachabilityUserName,
       "bsRadiusReachabilityPassword": bsRadiusReachabilityPassword,
       "bsRadiusEncapsulationProtocol": bsRadiusEncapsulationProtocol,
       "bsRadiusReachabilityTimeout": bsRadiusReachabilityTimeout,
       "bsRadiusReachabilityRetry": bsRadiusReachabilityRetry,
       "bsRadiusReachabilityBadTimer": bsRadiusReachabilityBadTimer,
       "bsRadiusReachabilityGoodTimer": bsRadiusReachabilityGoodTimer,
       "bsRadiusServerTable": bsRadiusServerTable,
       "bsRadiusServerEntry": bsRadiusServerEntry,
       "bsRadiusServerIndex": bsRadiusServerIndex,
       "bsRadiusServerPriority": bsRadiusServerPriority,
       "bsRadiusServerAddressType": bsRadiusServerAddressType,
       "bsRadiusServerAddress": bsRadiusServerAddress,
       "bsRadiusServerUdpPort": bsRadiusServerUdpPort,
       "bsRadiusServerTimeout": bsRadiusServerTimeout,
       "bsRadiusServerSecret": bsRadiusServerSecret,
       "bsRadiusServerRowStatus": bsRadiusServerRowStatus,
       "bsRadiusServerAccountingPort": bsRadiusServerAccountingPort,
       "bsRadiusServerAccountingEnabled": bsRadiusServerAccountingEnabled,
       "bsRadiusServerRetryLimit": bsRadiusServerRetryLimit,
       "bsRadiusDynAuthClientTable": bsRadiusDynAuthClientTable,
       "bsRadiusDynAuthClientEntry": bsRadiusDynAuthClientEntry,
       "bsRadiusDynAuthClientAddressType": bsRadiusDynAuthClientAddressType,
       "bsRadiusDynAuthClientAddress": bsRadiusDynAuthClientAddress,
       "bsRadiusDynAuthClientUdpPort": bsRadiusDynAuthClientUdpPort,
       "bsRadiusDynAuthClientSecret": bsRadiusDynAuthClientSecret,
       "bsRadiusDynAuthClientEnabled": bsRadiusDynAuthClientEnabled,
       "bsRadiusDynAuthClientProcessDisconnectRequests": bsRadiusDynAuthClientProcessDisconnectRequests,
       "bsRadiusDynAuthClientProcessCoARequests": bsRadiusDynAuthClientProcessCoARequests,
       "bsRadiusDynAuthClientRowStatus": bsRadiusDynAuthClientRowStatus,
       "bsRadiusDynAuthClientReplayProtection": bsRadiusDynAuthClientReplayProtection,
       "bsRadiusDynAuthClientProcessReAuthRequests": bsRadiusDynAuthClientProcessReAuthRequests,
       "bsRadiusExtDynAuthClientTable": bsRadiusExtDynAuthClientTable,
       "bsRadiusExtDynAuthClientEntry": bsRadiusExtDynAuthClientEntry,
       "bsRadiusExtDynAuthServRcRequests": bsRadiusExtDynAuthServRcRequests,
       "bsRadiusExtDynAuthServRcAuthOnlyRequests": bsRadiusExtDynAuthServRcAuthOnlyRequests,
       "bsRadiusExtDynAuthServRcDupRequests": bsRadiusExtDynAuthServRcDupRequests,
       "bsRadiusExtDynAuthServRcAcks": bsRadiusExtDynAuthServRcAcks,
       "bsRadiusExtDynAuthServRcNacks": bsRadiusExtDynAuthServRcNacks,
       "bsRadiusExtDynAuthServRcNacksAuthOnlyRequests": bsRadiusExtDynAuthServRcNacksAuthOnlyRequests,
       "bsRadiusExtDynAuthServRcNacksNoSess": bsRadiusExtDynAuthServRcNacksNoSess,
       "bsRadiusExtDynAuthServRcSessReauthenticated": bsRadiusExtDynAuthServRcSessReauthenticated,
       "bsRadiusExtDynAuthServRcMalformed": bsRadiusExtDynAuthServRcMalformed,
       "bsRadiusExtDynAuthServRcDropped": bsRadiusExtDynAuthServRcDropped,
       "bsRadiusExtDynAuthServRcBadAuths": bsRadiusExtDynAuthServRcBadAuths}
)
