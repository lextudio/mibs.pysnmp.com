# SNMP MIB module (CISCO-GSLB-HEALTH-MON-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-GSLB-HEALTH-MON-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:01:01 2024
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

(cgdAnswerId,) = mibBuilder.importSymbols(
    "CISCO-GSLB-DNS-MIB",
    "cgdAnswerId")

(CiscoGslbKalapType,
 CiscoGslbKeepaliveMethod,
 CiscoGslbKeepaliveRate,
 CiscoGslbKeepaliveStatus,
 CiscoGslbKeepaliveTargetType,
 CiscoGslbTerminationMethod) = mibBuilder.importSymbols(
    "CISCO-GSLB-TC-MIB",
    "CiscoGslbKalapType",
    "CiscoGslbKeepaliveMethod",
    "CiscoGslbKeepaliveRate",
    "CiscoGslbKeepaliveStatus",
    "CiscoGslbKeepaliveTargetType",
    "CiscoGslbTerminationMethod")

(ciscoMgmt,) = mibBuilder.importSymbols(
    "CISCO-SMI",
    "ciscoMgmt")

(InetAddress,
 InetAddressType,
 InetPortNumber) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType",
    "InetPortNumber")

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

(sysName,) = mibBuilder.importSymbols(
    "SNMPv2-MIB",
    "sysName")

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
 StorageType,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "StorageType",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

ciscoGslbHealthMonMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 600)
)
ciscoGslbHealthMonMIB.setRevisions(
        ("2007-04-09 00:00",
         "2006-12-04 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CiscoGslbHealthMonMIBNotifs_ObjectIdentity = ObjectIdentity
ciscoGslbHealthMonMIBNotifs = _CiscoGslbHealthMonMIBNotifs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 600, 0)
)
_CiscoGslbHealthMonMIBObjects_ObjectIdentity = ObjectIdentity
ciscoGslbHealthMonMIBObjects = _CiscoGslbHealthMonMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 600, 1)
)
_CghMonNotifControl_ObjectIdentity = ObjectIdentity
cghMonNotifControl = _CghMonNotifControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 600, 1, 1)
)


class _CghMonKalNotifEnable_Type(TruthValue):
    """Custom type cghMonKalNotifEnable based on TruthValue"""


_CghMonKalNotifEnable_Object = MibScalar
cghMonKalNotifEnable = _CghMonKalNotifEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 600, 1, 1, 1),
    _CghMonKalNotifEnable_Type()
)
cghMonKalNotifEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cghMonKalNotifEnable.setStatus("current")
_CghMonNotifObjects_ObjectIdentity = ObjectIdentity
cghMonNotifObjects = _CghMonNotifObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 600, 1, 2)
)
_CghMonKalPrevStatus_Type = CiscoGslbKeepaliveStatus
_CghMonKalPrevStatus_Object = MibScalar
cghMonKalPrevStatus = _CghMonKalPrevStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 600, 1, 2, 1),
    _CghMonKalPrevStatus_Type()
)
cghMonKalPrevStatus.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cghMonKalPrevStatus.setStatus("current")
_CghMonKalGeneralConfig_ObjectIdentity = ObjectIdentity
cghMonKalGeneralConfig = _CghMonKalGeneralConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 600, 1, 3)
)


class _CghMonNsQueryDomainName_Type(SnmpAdminString):
    """Custom type cghMonNsQueryDomainName based on SnmpAdminString"""
    defaultValue = OctetString(".")


_CghMonNsQueryDomainName_Object = MibScalar
cghMonNsQueryDomainName = _CghMonNsQueryDomainName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 600, 1, 3, 1),
    _CghMonNsQueryDomainName_Type()
)
cghMonNsQueryDomainName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cghMonNsQueryDomainName.setStatus("current")


class _CghMonCappHash_Type(SnmpAdminString):
    """Custom type cghMonCappHash based on SnmpAdminString"""
    defaultValue = OctetString("hash-not-set")


_CghMonCappHash_Object = MibScalar
cghMonCappHash = _CghMonCappHash_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 600, 1, 3, 2),
    _CghMonCappHash_Type()
)
cghMonCappHash.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cghMonCappHash.setStatus("current")


class _CghMonHttpHeadPath_Type(SnmpAdminString):
    """Custom type cghMonHttpHeadPath based on SnmpAdminString"""
    defaultValue = OctetString("/")


_CghMonHttpHeadPath_Object = MibScalar
cghMonHttpHeadPath = _CghMonHttpHeadPath_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 600, 1, 3, 3),
    _CghMonHttpHeadPath_Type()
)
cghMonHttpHeadPath.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cghMonHttpHeadPath.setStatus("current")


class _CghMonHttpHeadConnTermMethod_Type(CiscoGslbTerminationMethod):
    """Custom type cghMonHttpHeadConnTermMethod based on CiscoGslbTerminationMethod"""


_CghMonHttpHeadConnTermMethod_Object = MibScalar
cghMonHttpHeadConnTermMethod = _CghMonHttpHeadConnTermMethod_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 600, 1, 3, 4),
    _CghMonHttpHeadConnTermMethod_Type()
)
cghMonHttpHeadConnTermMethod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cghMonHttpHeadConnTermMethod.setStatus("current")


class _CghMonTcpConnTermMethod_Type(CiscoGslbTerminationMethod):
    """Custom type cghMonTcpConnTermMethod based on CiscoGslbTerminationMethod"""


_CghMonTcpConnTermMethod_Object = MibScalar
cghMonTcpConnTermMethod = _CghMonTcpConnTermMethod_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 600, 1, 3, 5),
    _CghMonTcpConnTermMethod_Type()
)
cghMonTcpConnTermMethod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cghMonTcpConnTermMethod.setStatus("current")


class _CghMonCraDecay_Type(Unsigned32):
    """Custom type cghMonCraDecay based on Unsigned32"""
    defaultValue = 2

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_CghMonCraDecay_Type.__name__ = "Unsigned32"
_CghMonCraDecay_Object = MibScalar
cghMonCraDecay = _CghMonCraDecay_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 600, 1, 3, 6),
    _CghMonCraDecay_Type()
)
cghMonCraDecay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cghMonCraDecay.setStatus("current")
_CghMonTotalConfiguredProbes_Type = Unsigned32
_CghMonTotalConfiguredProbes_Object = MibScalar
cghMonTotalConfiguredProbes = _CghMonTotalConfiguredProbes_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 600, 1, 3, 7),
    _CghMonTotalConfiguredProbes_Type()
)
cghMonTotalConfiguredProbes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cghMonTotalConfiguredProbes.setStatus("current")
_CghMonDroppedKalNotifs_Type = Unsigned32
_CghMonDroppedKalNotifs_Object = MibScalar
cghMonDroppedKalNotifs = _CghMonDroppedKalNotifs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 600, 1, 3, 8),
    _CghMonDroppedKalNotifs_Type()
)
cghMonDroppedKalNotifs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cghMonDroppedKalNotifs.setStatus("current")
if mibBuilder.loadTexts:
    cghMonDroppedKalNotifs.setUnits("traps")


class _CghMonKalTrapRateLimit_Type(Unsigned32):
    """Custom type cghMonKalTrapRateLimit based on Unsigned32"""
    defaultValue = 25

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_CghMonKalTrapRateLimit_Type.__name__ = "Unsigned32"
_CghMonKalTrapRateLimit_Object = MibScalar
cghMonKalTrapRateLimit = _CghMonKalTrapRateLimit_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 600, 1, 3, 9),
    _CghMonKalTrapRateLimit_Type()
)
cghMonKalTrapRateLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cghMonKalTrapRateLimit.setStatus("current")
if mibBuilder.loadTexts:
    cghMonKalTrapRateLimit.setUnits("traps per minute")
_CghMonKalParameterTable_Object = MibTable
cghMonKalParameterTable = _CghMonKalParameterTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 600, 1, 3, 10)
)
if mibBuilder.loadTexts:
    cghMonKalParameterTable.setStatus("current")
_CghMonKalParameterEntry_Object = MibTableRow
cghMonKalParameterEntry = _CghMonKalParameterEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 600, 1, 3, 10, 1)
)
cghMonKalParameterEntry.setIndexNames(
    (0, "CISCO-GSLB-HEALTH-MON-MIB", "cghMonKalParameterMethod"),
)
if mibBuilder.loadTexts:
    cghMonKalParameterEntry.setStatus("current")
_CghMonKalParameterMethod_Type = CiscoGslbKeepaliveMethod
_CghMonKalParameterMethod_Object = MibTableColumn
cghMonKalParameterMethod = _CghMonKalParameterMethod_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 600, 1, 3, 10, 1, 1),
    _CghMonKalParameterMethod_Type()
)
cghMonKalParameterMethod.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cghMonKalParameterMethod.setStatus("current")
_CghMonKalParameterRate_Type = CiscoGslbKeepaliveRate
_CghMonKalParameterRate_Object = MibTableColumn
cghMonKalParameterRate = _CghMonKalParameterRate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 600, 1, 3, 10, 1, 2),
    _CghMonKalParameterRate_Type()
)
cghMonKalParameterRate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cghMonKalParameterRate.setStatus("current")


class _CghMonKalParameterMinimumFrequency_Type(Unsigned32):
    """Custom type cghMonKalParameterMinimumFrequency based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_CghMonKalParameterMinimumFrequency_Type.__name__ = "Unsigned32"
_CghMonKalParameterMinimumFrequency_Object = MibTableColumn
cghMonKalParameterMinimumFrequency = _CghMonKalParameterMinimumFrequency_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 600, 1, 3, 10, 1, 3),
    _CghMonKalParameterMinimumFrequency_Type()
)
cghMonKalParameterMinimumFrequency.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cghMonKalParameterMinimumFrequency.setStatus("current")
if mibBuilder.loadTexts:
    cghMonKalParameterMinimumFrequency.setUnits("seconds")


class _CghMonKalParameterResponseTimeout_Type(Unsigned32):
    """Custom type cghMonKalParameterResponseTimeout based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_CghMonKalParameterResponseTimeout_Type.__name__ = "Unsigned32"
_CghMonKalParameterResponseTimeout_Object = MibTableColumn
cghMonKalParameterResponseTimeout = _CghMonKalParameterResponseTimeout_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 600, 1, 3, 10, 1, 4),
    _CghMonKalParameterResponseTimeout_Type()
)
cghMonKalParameterResponseTimeout.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cghMonKalParameterResponseTimeout.setStatus("current")
if mibBuilder.loadTexts:
    cghMonKalParameterResponseTimeout.setUnits("seconds")


class _CghMonKalParameterFastRetries_Type(Unsigned32):
    """Custom type cghMonKalParameterFastRetries based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_CghMonKalParameterFastRetries_Type.__name__ = "Unsigned32"
_CghMonKalParameterFastRetries_Object = MibTableColumn
cghMonKalParameterFastRetries = _CghMonKalParameterFastRetries_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 600, 1, 3, 10, 1, 5),
    _CghMonKalParameterFastRetries_Type()
)
cghMonKalParameterFastRetries.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cghMonKalParameterFastRetries.setStatus("current")
if mibBuilder.loadTexts:
    cghMonKalParameterFastRetries.setUnits("retries")


class _CghMonKalParameterFastSuccessfulProbes_Type(Unsigned32):
    """Custom type cghMonKalParameterFastSuccessfulProbes based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_CghMonKalParameterFastSuccessfulProbes_Type.__name__ = "Unsigned32"
_CghMonKalParameterFastSuccessfulProbes_Object = MibTableColumn
cghMonKalParameterFastSuccessfulProbes = _CghMonKalParameterFastSuccessfulProbes_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 600, 1, 3, 10, 1, 6),
    _CghMonKalParameterFastSuccessfulProbes_Type()
)
cghMonKalParameterFastSuccessfulProbes.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cghMonKalParameterFastSuccessfulProbes.setStatus("current")
if mibBuilder.loadTexts:
    cghMonKalParameterFastSuccessfulProbes.setUnits("probes")


class _CghMonKalParameterDestPort_Type(InetPortNumber):
    """Custom type cghMonKalParameterDestPort based on InetPortNumber"""
    subtypeSpec = InetPortNumber.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_CghMonKalParameterDestPort_Type.__name__ = "InetPortNumber"
_CghMonKalParameterDestPort_Object = MibTableColumn
cghMonKalParameterDestPort = _CghMonKalParameterDestPort_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 600, 1, 3, 10, 1, 7),
    _CghMonKalParameterDestPort_Type()
)
cghMonKalParameterDestPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cghMonKalParameterDestPort.setStatus("current")


class _CghMonKalParameterStorageType_Type(StorageType):
    """Custom type cghMonKalParameterStorageType based on StorageType"""


_CghMonKalParameterStorageType_Object = MibTableColumn
cghMonKalParameterStorageType = _CghMonKalParameterStorageType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 600, 1, 3, 10, 1, 8),
    _CghMonKalParameterStorageType_Type()
)
cghMonKalParameterStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cghMonKalParameterStorageType.setStatus("current")
_CghMonKalParameterRowStatus_Type = RowStatus
_CghMonKalParameterRowStatus_Object = MibTableColumn
cghMonKalParameterRowStatus = _CghMonKalParameterRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 600, 1, 3, 10, 1, 9),
    _CghMonKalParameterRowStatus_Type()
)
cghMonKalParameterRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cghMonKalParameterRowStatus.setStatus("current")
_CghMonKal_ObjectIdentity = ObjectIdentity
cghMonKal = _CghMonKal_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 600, 1, 4)
)
_CghMonKalConfigTable_Object = MibTable
cghMonKalConfigTable = _CghMonKalConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 600, 1, 4, 1)
)
if mibBuilder.loadTexts:
    cghMonKalConfigTable.setStatus("current")
_CghMonKalConfigEntry_Object = MibTableRow
cghMonKalConfigEntry = _CghMonKalConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 600, 1, 4, 1, 1)
)
cghMonKalConfigEntry.setIndexNames(
    (0, "CISCO-GSLB-HEALTH-MON-MIB", "cghMonKalId"),
)
if mibBuilder.loadTexts:
    cghMonKalConfigEntry.setStatus("current")


class _CghMonKalId_Type(Unsigned32):
    """Custom type cghMonKalId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_CghMonKalId_Type.__name__ = "Unsigned32"
_CghMonKalId_Object = MibTableColumn
cghMonKalId = _CghMonKalId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 600, 1, 4, 1, 1, 1),
    _CghMonKalId_Type()
)
cghMonKalId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cghMonKalId.setStatus("current")
_CghMonKalTargetType_Type = CiscoGslbKeepaliveTargetType
_CghMonKalTargetType_Object = MibTableColumn
cghMonKalTargetType = _CghMonKalTargetType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 600, 1, 4, 1, 1, 2),
    _CghMonKalTargetType_Type()
)
cghMonKalTargetType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cghMonKalTargetType.setStatus("current")
_CghMonKalMethod_Type = CiscoGslbKeepaliveMethod
_CghMonKalMethod_Object = MibTableColumn
cghMonKalMethod = _CghMonKalMethod_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 600, 1, 4, 1, 1, 3),
    _CghMonKalMethod_Type()
)
cghMonKalMethod.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cghMonKalMethod.setStatus("current")
_CghMonKalAnswerId_Type = Unsigned32
_CghMonKalAnswerId_Object = MibTableColumn
cghMonKalAnswerId = _CghMonKalAnswerId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 600, 1, 4, 1, 1, 4),
    _CghMonKalAnswerId_Type()
)
cghMonKalAnswerId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cghMonKalAnswerId.setStatus("current")


class _CghMonKalPrimaryTargetType_Type(InetAddressType):
    """Custom type cghMonKalPrimaryTargetType based on InetAddressType"""


_CghMonKalPrimaryTargetType_Object = MibTableColumn
cghMonKalPrimaryTargetType = _CghMonKalPrimaryTargetType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 600, 1, 4, 1, 1, 5),
    _CghMonKalPrimaryTargetType_Type()
)
cghMonKalPrimaryTargetType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cghMonKalPrimaryTargetType.setStatus("current")
_CghMonKalPrimaryTarget_Type = InetAddress
_CghMonKalPrimaryTarget_Object = MibTableColumn
cghMonKalPrimaryTarget = _CghMonKalPrimaryTarget_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 600, 1, 4, 1, 1, 6),
    _CghMonKalPrimaryTarget_Type()
)
cghMonKalPrimaryTarget.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cghMonKalPrimaryTarget.setStatus("current")


class _CghMonKalEnable_Type(TruthValue):
    """Custom type cghMonKalEnable based on TruthValue"""


_CghMonKalEnable_Object = MibTableColumn
cghMonKalEnable = _CghMonKalEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 600, 1, 4, 1, 1, 7),
    _CghMonKalEnable_Type()
)
cghMonKalEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cghMonKalEnable.setStatus("current")


class _CghMonKalDelay_Type(Unsigned32):
    """Custom type cghMonKalDelay based on Unsigned32"""
    defaultValue = 0


_CghMonKalDelay_Object = MibTableColumn
cghMonKalDelay = _CghMonKalDelay_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 600, 1, 4, 1, 1, 8),
    _CghMonKalDelay_Type()
)
cghMonKalDelay.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cghMonKalDelay.setStatus("current")
if mibBuilder.loadTexts:
    cghMonKalDelay.setUnits("milliseconds")


class _CghMonKalKalapType_Type(CiscoGslbKalapType):
    """Custom type cghMonKalKalapType based on CiscoGslbKalapType"""


_CghMonKalKalapType_Object = MibTableColumn
cghMonKalKalapType = _CghMonKalKalapType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 600, 1, 4, 1, 1, 9),
    _CghMonKalKalapType_Type()
)
cghMonKalKalapType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cghMonKalKalapType.setStatus("current")
_CghMonKalTagName_Type = SnmpAdminString
_CghMonKalTagName_Object = MibTableColumn
cghMonKalTagName = _CghMonKalTagName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 600, 1, 4, 1, 1, 10),
    _CghMonKalTagName_Type()
)
cghMonKalTagName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cghMonKalTagName.setStatus("current")


class _CghMonKalDestPort_Type(InetPortNumber):
    """Custom type cghMonKalDestPort based on InetPortNumber"""
    subtypeSpec = InetPortNumber.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_CghMonKalDestPort_Type.__name__ = "InetPortNumber"
_CghMonKalDestPort_Object = MibTableColumn
cghMonKalDestPort = _CghMonKalDestPort_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 600, 1, 4, 1, 1, 11),
    _CghMonKalDestPort_Type()
)
cghMonKalDestPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cghMonKalDestPort.setStatus("current")


class _CghMonKalCappSecure_Type(TruthValue):
    """Custom type cghMonKalCappSecure based on TruthValue"""


_CghMonKalCappSecure_Object = MibTableColumn
cghMonKalCappSecure = _CghMonKalCappSecure_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 600, 1, 4, 1, 1, 12),
    _CghMonKalCappSecure_Type()
)
cghMonKalCappSecure.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cghMonKalCappSecure.setStatus("current")
_CghMonKalCappHash_Type = SnmpAdminString
_CghMonKalCappHash_Object = MibTableColumn
cghMonKalCappHash = _CghMonKalCappHash_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 600, 1, 4, 1, 1, 13),
    _CghMonKalCappHash_Type()
)
cghMonKalCappHash.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cghMonKalCappHash.setStatus("current")
_CghMonKalQueryDomainName_Type = SnmpAdminString
_CghMonKalQueryDomainName_Object = MibTableColumn
cghMonKalQueryDomainName = _CghMonKalQueryDomainName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 600, 1, 4, 1, 1, 14),
    _CghMonKalQueryDomainName_Type()
)
cghMonKalQueryDomainName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cghMonKalQueryDomainName.setStatus("current")
_CghMonKalPath_Type = SnmpAdminString
_CghMonKalPath_Object = MibTableColumn
cghMonKalPath = _CghMonKalPath_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 600, 1, 4, 1, 1, 15),
    _CghMonKalPath_Type()
)
cghMonKalPath.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cghMonKalPath.setStatus("current")
_CghMonKalHostTag_Type = SnmpAdminString
_CghMonKalHostTag_Object = MibTableColumn
cghMonKalHostTag = _CghMonKalHostTag_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 600, 1, 4, 1, 1, 16),
    _CghMonKalHostTag_Type()
)
cghMonKalHostTag.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cghMonKalHostTag.setStatus("current")


class _CghMonKalSecondaryTargetType_Type(InetAddressType):
    """Custom type cghMonKalSecondaryTargetType based on InetAddressType"""


_CghMonKalSecondaryTargetType_Object = MibTableColumn
cghMonKalSecondaryTargetType = _CghMonKalSecondaryTargetType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 600, 1, 4, 1, 1, 17),
    _CghMonKalSecondaryTargetType_Type()
)
cghMonKalSecondaryTargetType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cghMonKalSecondaryTargetType.setStatus("current")
_CghMonKalSecondaryTarget_Type = InetAddress
_CghMonKalSecondaryTarget_Object = MibTableColumn
cghMonKalSecondaryTarget = _CghMonKalSecondaryTarget_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 600, 1, 4, 1, 1, 18),
    _CghMonKalSecondaryTarget_Type()
)
cghMonKalSecondaryTarget.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cghMonKalSecondaryTarget.setStatus("current")
_CghMonKalFastRetries_Type = Unsigned32
_CghMonKalFastRetries_Object = MibTableColumn
cghMonKalFastRetries = _CghMonKalFastRetries_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 600, 1, 4, 1, 1, 19),
    _CghMonKalFastRetries_Type()
)
cghMonKalFastRetries.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cghMonKalFastRetries.setStatus("current")
if mibBuilder.loadTexts:
    cghMonKalFastRetries.setUnits("retries")
_CghMonKalFastSuccessfulProbes_Type = Unsigned32
_CghMonKalFastSuccessfulProbes_Object = MibTableColumn
cghMonKalFastSuccessfulProbes = _CghMonKalFastSuccessfulProbes_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 600, 1, 4, 1, 1, 20),
    _CghMonKalFastSuccessfulProbes_Type()
)
cghMonKalFastSuccessfulProbes.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cghMonKalFastSuccessfulProbes.setStatus("current")
if mibBuilder.loadTexts:
    cghMonKalFastSuccessfulProbes.setUnits("probes")


class _CghMonKalStorageType_Type(StorageType):
    """Custom type cghMonKalStorageType based on StorageType"""


_CghMonKalStorageType_Object = MibTableColumn
cghMonKalStorageType = _CghMonKalStorageType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 600, 1, 4, 1, 1, 21),
    _CghMonKalStorageType_Type()
)
cghMonKalStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cghMonKalStorageType.setStatus("current")
_CghMonKalRowStatus_Type = RowStatus
_CghMonKalRowStatus_Object = MibTableColumn
cghMonKalRowStatus = _CghMonKalRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 600, 1, 4, 1, 1, 22),
    _CghMonKalRowStatus_Type()
)
cghMonKalRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cghMonKalRowStatus.setStatus("current")
_CghMonKalSharedAnswerTable_Object = MibTable
cghMonKalSharedAnswerTable = _CghMonKalSharedAnswerTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 600, 1, 4, 2)
)
if mibBuilder.loadTexts:
    cghMonKalSharedAnswerTable.setStatus("current")
_CghMonKalSharedAnswerEntry_Object = MibTableRow
cghMonKalSharedAnswerEntry = _CghMonKalSharedAnswerEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 600, 1, 4, 2, 1)
)
cghMonKalSharedAnswerEntry.setIndexNames(
    (0, "CISCO-GSLB-DNS-MIB", "cgdAnswerId"),
    (0, "CISCO-GSLB-HEALTH-MON-MIB", "cghMonKalId"),
)
if mibBuilder.loadTexts:
    cghMonKalSharedAnswerEntry.setStatus("current")


class _CghMonKalShAnsStoragetype_Type(StorageType):
    """Custom type cghMonKalShAnsStoragetype based on StorageType"""


_CghMonKalShAnsStoragetype_Object = MibTableColumn
cghMonKalShAnsStoragetype = _CghMonKalShAnsStoragetype_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 600, 1, 4, 2, 1, 1),
    _CghMonKalShAnsStoragetype_Type()
)
cghMonKalShAnsStoragetype.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cghMonKalShAnsStoragetype.setStatus("current")
_CghMonKalShAnsRowStatus_Type = RowStatus
_CghMonKalShAnsRowStatus_Object = MibTableColumn
cghMonKalShAnsRowStatus = _CghMonKalShAnsRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 600, 1, 4, 2, 1, 2),
    _CghMonKalShAnsRowStatus_Type()
)
cghMonKalShAnsRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cghMonKalShAnsRowStatus.setStatus("current")
_CghMonKalStatsTable_Object = MibTable
cghMonKalStatsTable = _CghMonKalStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 600, 1, 4, 3)
)
if mibBuilder.loadTexts:
    cghMonKalStatsTable.setStatus("current")
_CghMonKalStatsEntry_Object = MibTableRow
cghMonKalStatsEntry = _CghMonKalStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 600, 1, 4, 3, 1)
)
if mibBuilder.loadTexts:
    cghMonKalStatsEntry.setStatus("current")
_CghMonKalStatus_Type = CiscoGslbKeepaliveStatus
_CghMonKalStatus_Object = MibTableColumn
cghMonKalStatus = _CghMonKalStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 600, 1, 4, 3, 1, 1),
    _CghMonKalStatus_Type()
)
cghMonKalStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cghMonKalStatus.setStatus("current")
_CghMonKalSentProbes_Type = Counter32
_CghMonKalSentProbes_Object = MibTableColumn
cghMonKalSentProbes = _CghMonKalSentProbes_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 600, 1, 4, 3, 1, 2),
    _CghMonKalSentProbes_Type()
)
cghMonKalSentProbes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cghMonKalSentProbes.setStatus("current")
if mibBuilder.loadTexts:
    cghMonKalSentProbes.setUnits("probes")
_CghMonKalReceivedProbes_Type = Counter32
_CghMonKalReceivedProbes_Object = MibTableColumn
cghMonKalReceivedProbes = _CghMonKalReceivedProbes_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 600, 1, 4, 3, 1, 3),
    _CghMonKalReceivedProbes_Type()
)
cghMonKalReceivedProbes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cghMonKalReceivedProbes.setStatus("current")
if mibBuilder.loadTexts:
    cghMonKalReceivedProbes.setUnits("probes")
_CghMonKalPositiveProbes_Type = Counter32
_CghMonKalPositiveProbes_Object = MibTableColumn
cghMonKalPositiveProbes = _CghMonKalPositiveProbes_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 600, 1, 4, 3, 1, 4),
    _CghMonKalPositiveProbes_Type()
)
cghMonKalPositiveProbes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cghMonKalPositiveProbes.setStatus("current")
if mibBuilder.loadTexts:
    cghMonKalPositiveProbes.setUnits("probes")
_CghMonKalNegativeProbes_Type = Counter32
_CghMonKalNegativeProbes_Object = MibTableColumn
cghMonKalNegativeProbes = _CghMonKalNegativeProbes_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 600, 1, 4, 3, 1, 5),
    _CghMonKalNegativeProbes_Type()
)
cghMonKalNegativeProbes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cghMonKalNegativeProbes.setStatus("current")
if mibBuilder.loadTexts:
    cghMonKalNegativeProbes.setUnits("probes")
_CghMonKalStatusTransitions_Type = Counter32
_CghMonKalStatusTransitions_Object = MibTableColumn
cghMonKalStatusTransitions = _CghMonKalStatusTransitions_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 600, 1, 4, 3, 1, 6),
    _CghMonKalStatusTransitions_Type()
)
cghMonKalStatusTransitions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cghMonKalStatusTransitions.setStatus("current")
_CghMonKalDynamicLoad_Type = Unsigned32
_CghMonKalDynamicLoad_Object = MibTableColumn
cghMonKalDynamicLoad = _CghMonKalDynamicLoad_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 600, 1, 4, 3, 1, 7),
    _CghMonKalDynamicLoad_Type()
)
cghMonKalDynamicLoad.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cghMonKalDynamicLoad.setStatus("current")
_CghMonKalVIPFailovers_Type = Counter32
_CghMonKalVIPFailovers_Object = MibTableColumn
cghMonKalVIPFailovers = _CghMonKalVIPFailovers_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 600, 1, 4, 3, 1, 8),
    _CghMonKalVIPFailovers_Type()
)
cghMonKalVIPFailovers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cghMonKalVIPFailovers.setStatus("current")
_CiscoGslbHealthMonMIBConform_ObjectIdentity = ObjectIdentity
ciscoGslbHealthMonMIBConform = _CiscoGslbHealthMonMIBConform_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 600, 2)
)
_CiscoGslbHealthMonMIBCompliances_ObjectIdentity = ObjectIdentity
ciscoGslbHealthMonMIBCompliances = _CiscoGslbHealthMonMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 600, 2, 1)
)
_CiscoGslbHealthMonMIBGroups_ObjectIdentity = ObjectIdentity
ciscoGslbHealthMonMIBGroups = _CiscoGslbHealthMonMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 600, 2, 2)
)
cghMonKalConfigEntry.registerAugmentions(
    ("CISCO-GSLB-HEALTH-MON-MIB",
     "cghMonKalStatsEntry")
)
cghMonKalStatsEntry.setIndexNames(*cghMonKalConfigEntry.getIndexNames())

# Managed Objects groups

ciscoGslbGeneralConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 600, 2, 2, 1)
)
ciscoGslbGeneralConfigGroup.setObjects(
      *(("CISCO-GSLB-HEALTH-MON-MIB", "cghMonNsQueryDomainName"),
        ("CISCO-GSLB-HEALTH-MON-MIB", "cghMonCappHash"),
        ("CISCO-GSLB-HEALTH-MON-MIB", "cghMonHttpHeadPath"),
        ("CISCO-GSLB-HEALTH-MON-MIB", "cghMonHttpHeadConnTermMethod"),
        ("CISCO-GSLB-HEALTH-MON-MIB", "cghMonCraDecay"),
        ("CISCO-GSLB-HEALTH-MON-MIB", "cghMonTcpConnTermMethod"),
        ("CISCO-GSLB-HEALTH-MON-MIB", "cghMonTotalConfiguredProbes"),
        ("CISCO-GSLB-HEALTH-MON-MIB", "cghMonDroppedKalNotifs"),
        ("CISCO-GSLB-HEALTH-MON-MIB", "cghMonKalTrapRateLimit"))
)
if mibBuilder.loadTexts:
    ciscoGslbGeneralConfigGroup.setStatus("current")

ciscoGslbKalParameterGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 600, 2, 2, 2)
)
ciscoGslbKalParameterGroup.setObjects(
      *(("CISCO-GSLB-HEALTH-MON-MIB", "cghMonKalParameterRate"),
        ("CISCO-GSLB-HEALTH-MON-MIB", "cghMonKalParameterMinimumFrequency"),
        ("CISCO-GSLB-HEALTH-MON-MIB", "cghMonKalParameterResponseTimeout"),
        ("CISCO-GSLB-HEALTH-MON-MIB", "cghMonKalParameterFastRetries"),
        ("CISCO-GSLB-HEALTH-MON-MIB", "cghMonKalParameterFastSuccessfulProbes"),
        ("CISCO-GSLB-HEALTH-MON-MIB", "cghMonKalParameterDestPort"),
        ("CISCO-GSLB-HEALTH-MON-MIB", "cghMonKalParameterStorageType"),
        ("CISCO-GSLB-HEALTH-MON-MIB", "cghMonKalParameterRowStatus"))
)
if mibBuilder.loadTexts:
    ciscoGslbKalParameterGroup.setStatus("current")

ciscoGslbKalConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 600, 2, 2, 3)
)
ciscoGslbKalConfigGroup.setObjects(
      *(("CISCO-GSLB-HEALTH-MON-MIB", "cghMonKalTargetType"),
        ("CISCO-GSLB-HEALTH-MON-MIB", "cghMonKalMethod"),
        ("CISCO-GSLB-HEALTH-MON-MIB", "cghMonKalAnswerId"),
        ("CISCO-GSLB-HEALTH-MON-MIB", "cghMonKalPrimaryTargetType"),
        ("CISCO-GSLB-HEALTH-MON-MIB", "cghMonKalPrimaryTarget"),
        ("CISCO-GSLB-HEALTH-MON-MIB", "cghMonKalEnable"),
        ("CISCO-GSLB-HEALTH-MON-MIB", "cghMonKalDelay"),
        ("CISCO-GSLB-HEALTH-MON-MIB", "cghMonKalKalapType"),
        ("CISCO-GSLB-HEALTH-MON-MIB", "cghMonKalTagName"),
        ("CISCO-GSLB-HEALTH-MON-MIB", "cghMonKalDestPort"),
        ("CISCO-GSLB-HEALTH-MON-MIB", "cghMonKalCappSecure"),
        ("CISCO-GSLB-HEALTH-MON-MIB", "cghMonKalCappHash"),
        ("CISCO-GSLB-HEALTH-MON-MIB", "cghMonKalQueryDomainName"),
        ("CISCO-GSLB-HEALTH-MON-MIB", "cghMonKalPath"),
        ("CISCO-GSLB-HEALTH-MON-MIB", "cghMonKalHostTag"),
        ("CISCO-GSLB-HEALTH-MON-MIB", "cghMonKalSecondaryTargetType"),
        ("CISCO-GSLB-HEALTH-MON-MIB", "cghMonKalSecondaryTarget"),
        ("CISCO-GSLB-HEALTH-MON-MIB", "cghMonKalFastRetries"),
        ("CISCO-GSLB-HEALTH-MON-MIB", "cghMonKalFastSuccessfulProbes"),
        ("CISCO-GSLB-HEALTH-MON-MIB", "cghMonKalStorageType"),
        ("CISCO-GSLB-HEALTH-MON-MIB", "cghMonKalRowStatus"),
        ("CISCO-GSLB-HEALTH-MON-MIB", "cghMonKalShAnsStoragetype"),
        ("CISCO-GSLB-HEALTH-MON-MIB", "cghMonKalShAnsRowStatus"))
)
if mibBuilder.loadTexts:
    ciscoGslbKalConfigGroup.setStatus("current")

ciscoGslbKalStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 600, 2, 2, 4)
)
ciscoGslbKalStatsGroup.setObjects(
      *(("CISCO-GSLB-HEALTH-MON-MIB", "cghMonKalStatus"),
        ("CISCO-GSLB-HEALTH-MON-MIB", "cghMonKalSentProbes"),
        ("CISCO-GSLB-HEALTH-MON-MIB", "cghMonKalReceivedProbes"),
        ("CISCO-GSLB-HEALTH-MON-MIB", "cghMonKalPositiveProbes"),
        ("CISCO-GSLB-HEALTH-MON-MIB", "cghMonKalNegativeProbes"),
        ("CISCO-GSLB-HEALTH-MON-MIB", "cghMonKalStatusTransitions"),
        ("CISCO-GSLB-HEALTH-MON-MIB", "cghMonKalDynamicLoad"),
        ("CISCO-GSLB-HEALTH-MON-MIB", "cghMonKalVIPFailovers"))
)
if mibBuilder.loadTexts:
    ciscoGslbKalStatsGroup.setStatus("current")

ciscoGslbKalNotifControlGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 600, 2, 2, 5)
)
ciscoGslbKalNotifControlGroup.setObjects(
    ("CISCO-GSLB-HEALTH-MON-MIB", "cghMonKalNotifEnable")
)
if mibBuilder.loadTexts:
    ciscoGslbKalNotifControlGroup.setStatus("current")

ciscoGslbKalNotifObjectsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 600, 2, 2, 6)
)
ciscoGslbKalNotifObjectsGroup.setObjects(
    ("CISCO-GSLB-HEALTH-MON-MIB", "cghMonKalPrevStatus")
)
if mibBuilder.loadTexts:
    ciscoGslbKalNotifObjectsGroup.setStatus("current")

ciscoGslbGeneralConfigRateLimitGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 600, 2, 2, 8)
)
ciscoGslbGeneralConfigRateLimitGroup.setObjects(
      *(("CISCO-GSLB-HEALTH-MON-MIB", "cghMonDroppedKalNotifs"),
        ("CISCO-GSLB-HEALTH-MON-MIB", "cghMonKalTrapRateLimit"))
)
if mibBuilder.loadTexts:
    ciscoGslbGeneralConfigRateLimitGroup.setStatus("current")


# Notification objects

ciscoGslbKalEventStatus = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 600, 0, 1)
)
ciscoGslbKalEventStatus.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("CISCO-GSLB-HEALTH-MON-MIB", "cghMonKalPrimaryTargetType"),
        ("CISCO-GSLB-HEALTH-MON-MIB", "cghMonKalPrimaryTarget"),
        ("CISCO-GSLB-HEALTH-MON-MIB", "cghMonKalMethod"),
        ("CISCO-GSLB-HEALTH-MON-MIB", "cghMonKalPrevStatus"),
        ("CISCO-GSLB-HEALTH-MON-MIB", "cghMonKalStatus"),
        ("CISCO-GSLB-HEALTH-MON-MIB", "cghMonDroppedKalNotifs"))
)
if mibBuilder.loadTexts:
    ciscoGslbKalEventStatus.setStatus(
        "current"
    )


# Notifications groups

ciscoGslbKalNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 600, 2, 2, 7)
)
ciscoGslbKalNotificationGroup.setObjects(
    ("CISCO-GSLB-HEALTH-MON-MIB", "ciscoGslbKalEventStatus")
)
if mibBuilder.loadTexts:
    ciscoGslbKalNotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

ciscoGslbHealthMonMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 600, 2, 1, 1)
)
if mibBuilder.loadTexts:
    ciscoGslbHealthMonMIBCompliance.setStatus(
        "deprecated"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-GSLB-HEALTH-MON-MIB",
    **{"ciscoGslbHealthMonMIB": ciscoGslbHealthMonMIB,
       "ciscoGslbHealthMonMIBNotifs": ciscoGslbHealthMonMIBNotifs,
       "ciscoGslbKalEventStatus": ciscoGslbKalEventStatus,
       "ciscoGslbHealthMonMIBObjects": ciscoGslbHealthMonMIBObjects,
       "cghMonNotifControl": cghMonNotifControl,
       "cghMonKalNotifEnable": cghMonKalNotifEnable,
       "cghMonNotifObjects": cghMonNotifObjects,
       "cghMonKalPrevStatus": cghMonKalPrevStatus,
       "cghMonKalGeneralConfig": cghMonKalGeneralConfig,
       "cghMonNsQueryDomainName": cghMonNsQueryDomainName,
       "cghMonCappHash": cghMonCappHash,
       "cghMonHttpHeadPath": cghMonHttpHeadPath,
       "cghMonHttpHeadConnTermMethod": cghMonHttpHeadConnTermMethod,
       "cghMonTcpConnTermMethod": cghMonTcpConnTermMethod,
       "cghMonCraDecay": cghMonCraDecay,
       "cghMonTotalConfiguredProbes": cghMonTotalConfiguredProbes,
       "cghMonDroppedKalNotifs": cghMonDroppedKalNotifs,
       "cghMonKalTrapRateLimit": cghMonKalTrapRateLimit,
       "cghMonKalParameterTable": cghMonKalParameterTable,
       "cghMonKalParameterEntry": cghMonKalParameterEntry,
       "cghMonKalParameterMethod": cghMonKalParameterMethod,
       "cghMonKalParameterRate": cghMonKalParameterRate,
       "cghMonKalParameterMinimumFrequency": cghMonKalParameterMinimumFrequency,
       "cghMonKalParameterResponseTimeout": cghMonKalParameterResponseTimeout,
       "cghMonKalParameterFastRetries": cghMonKalParameterFastRetries,
       "cghMonKalParameterFastSuccessfulProbes": cghMonKalParameterFastSuccessfulProbes,
       "cghMonKalParameterDestPort": cghMonKalParameterDestPort,
       "cghMonKalParameterStorageType": cghMonKalParameterStorageType,
       "cghMonKalParameterRowStatus": cghMonKalParameterRowStatus,
       "cghMonKal": cghMonKal,
       "cghMonKalConfigTable": cghMonKalConfigTable,
       "cghMonKalConfigEntry": cghMonKalConfigEntry,
       "cghMonKalId": cghMonKalId,
       "cghMonKalTargetType": cghMonKalTargetType,
       "cghMonKalMethod": cghMonKalMethod,
       "cghMonKalAnswerId": cghMonKalAnswerId,
       "cghMonKalPrimaryTargetType": cghMonKalPrimaryTargetType,
       "cghMonKalPrimaryTarget": cghMonKalPrimaryTarget,
       "cghMonKalEnable": cghMonKalEnable,
       "cghMonKalDelay": cghMonKalDelay,
       "cghMonKalKalapType": cghMonKalKalapType,
       "cghMonKalTagName": cghMonKalTagName,
       "cghMonKalDestPort": cghMonKalDestPort,
       "cghMonKalCappSecure": cghMonKalCappSecure,
       "cghMonKalCappHash": cghMonKalCappHash,
       "cghMonKalQueryDomainName": cghMonKalQueryDomainName,
       "cghMonKalPath": cghMonKalPath,
       "cghMonKalHostTag": cghMonKalHostTag,
       "cghMonKalSecondaryTargetType": cghMonKalSecondaryTargetType,
       "cghMonKalSecondaryTarget": cghMonKalSecondaryTarget,
       "cghMonKalFastRetries": cghMonKalFastRetries,
       "cghMonKalFastSuccessfulProbes": cghMonKalFastSuccessfulProbes,
       "cghMonKalStorageType": cghMonKalStorageType,
       "cghMonKalRowStatus": cghMonKalRowStatus,
       "cghMonKalSharedAnswerTable": cghMonKalSharedAnswerTable,
       "cghMonKalSharedAnswerEntry": cghMonKalSharedAnswerEntry,
       "cghMonKalShAnsStoragetype": cghMonKalShAnsStoragetype,
       "cghMonKalShAnsRowStatus": cghMonKalShAnsRowStatus,
       "cghMonKalStatsTable": cghMonKalStatsTable,
       "cghMonKalStatsEntry": cghMonKalStatsEntry,
       "cghMonKalStatus": cghMonKalStatus,
       "cghMonKalSentProbes": cghMonKalSentProbes,
       "cghMonKalReceivedProbes": cghMonKalReceivedProbes,
       "cghMonKalPositiveProbes": cghMonKalPositiveProbes,
       "cghMonKalNegativeProbes": cghMonKalNegativeProbes,
       "cghMonKalStatusTransitions": cghMonKalStatusTransitions,
       "cghMonKalDynamicLoad": cghMonKalDynamicLoad,
       "cghMonKalVIPFailovers": cghMonKalVIPFailovers,
       "ciscoGslbHealthMonMIBConform": ciscoGslbHealthMonMIBConform,
       "ciscoGslbHealthMonMIBCompliances": ciscoGslbHealthMonMIBCompliances,
       "ciscoGslbHealthMonMIBCompliance": ciscoGslbHealthMonMIBCompliance,
       "ciscoGslbHealthMonMIBGroups": ciscoGslbHealthMonMIBGroups,
       "ciscoGslbGeneralConfigGroup": ciscoGslbGeneralConfigGroup,
       "ciscoGslbKalParameterGroup": ciscoGslbKalParameterGroup,
       "ciscoGslbKalConfigGroup": ciscoGslbKalConfigGroup,
       "ciscoGslbKalStatsGroup": ciscoGslbKalStatsGroup,
       "ciscoGslbKalNotifControlGroup": ciscoGslbKalNotifControlGroup,
       "ciscoGslbKalNotifObjectsGroup": ciscoGslbKalNotifObjectsGroup,
       "ciscoGslbKalNotificationGroup": ciscoGslbKalNotificationGroup,
       "ciscoGslbGeneralConfigRateLimitGroup": ciscoGslbGeneralConfigRateLimitGroup}
)
