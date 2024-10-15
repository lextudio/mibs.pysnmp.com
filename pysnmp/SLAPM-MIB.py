# SNMP MIB module (SLAPM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/SLAPM-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:53:52 2024
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
 experimental,
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
    "experimental",
    "iso")

(DateAndTime,
 DisplayString,
 RowStatus,
 TextualConvention,
 TestAndIncr) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "RowStatus",
    "TextualConvention",
    "TestAndIncr")


# MODULE-IDENTITY

slapmMIB = ModuleIdentity(
    (1, 3, 6, 1, 3, 88)
)
slapmMIB.setRevisions(
        ("2000-01-24 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class SlapmNameType(SnmpAdminString, TextualConvention):
    status = "deprecated"
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )



class SlapmStatus(Bits, TextualConvention):
    status = "current"


class SlapmPolicyRuleName(OctetString, TextualConvention):
    status = "current"
    displayHint = "1024t"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 1024),
    )



# MIB Managed Objects in the order of their OIDs

_SlapmNotifications_ObjectIdentity = ObjectIdentity
slapmNotifications = _SlapmNotifications_ObjectIdentity(
    (1, 3, 6, 1, 3, 88, 0)
)
_SlapmObjects_ObjectIdentity = ObjectIdentity
slapmObjects = _SlapmObjects_ObjectIdentity(
    (1, 3, 6, 1, 3, 88, 1)
)
_SlapmBaseObjects_ObjectIdentity = ObjectIdentity
slapmBaseObjects = _SlapmBaseObjects_ObjectIdentity(
    (1, 3, 6, 1, 3, 88, 1, 1)
)
_SlapmSpinLock_Type = TestAndIncr
_SlapmSpinLock_Object = MibScalar
slapmSpinLock = _SlapmSpinLock_Object(
    (1, 3, 6, 1, 3, 88, 1, 1, 1),
    _SlapmSpinLock_Type()
)
slapmSpinLock.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slapmSpinLock.setStatus("current")
_SlapmPolicyCountQueries_Type = Counter32
_SlapmPolicyCountQueries_Object = MibScalar
slapmPolicyCountQueries = _SlapmPolicyCountQueries_Object(
    (1, 3, 6, 1, 3, 88, 1, 1, 2),
    _SlapmPolicyCountQueries_Type()
)
slapmPolicyCountQueries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slapmPolicyCountQueries.setStatus("current")
_SlapmPolicyCountAccesses_Type = Counter32
_SlapmPolicyCountAccesses_Object = MibScalar
slapmPolicyCountAccesses = _SlapmPolicyCountAccesses_Object(
    (1, 3, 6, 1, 3, 88, 1, 1, 3),
    _SlapmPolicyCountAccesses_Type()
)
slapmPolicyCountAccesses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slapmPolicyCountAccesses.setStatus("current")
_SlapmPolicyCountSuccessAccesses_Type = Counter32
_SlapmPolicyCountSuccessAccesses_Object = MibScalar
slapmPolicyCountSuccessAccesses = _SlapmPolicyCountSuccessAccesses_Object(
    (1, 3, 6, 1, 3, 88, 1, 1, 4),
    _SlapmPolicyCountSuccessAccesses_Type()
)
slapmPolicyCountSuccessAccesses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slapmPolicyCountSuccessAccesses.setStatus("current")
_SlapmPolicyCountNotFounds_Type = Counter32
_SlapmPolicyCountNotFounds_Object = MibScalar
slapmPolicyCountNotFounds = _SlapmPolicyCountNotFounds_Object(
    (1, 3, 6, 1, 3, 88, 1, 1, 5),
    _SlapmPolicyCountNotFounds_Type()
)
slapmPolicyCountNotFounds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slapmPolicyCountNotFounds.setStatus("current")


class _SlapmPolicyPurgeTime_Type(Integer32):
    """Custom type slapmPolicyPurgeTime based on Integer32"""
    defaultValue = 900

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3600),
    )


_SlapmPolicyPurgeTime_Type.__name__ = "Integer32"
_SlapmPolicyPurgeTime_Object = MibScalar
slapmPolicyPurgeTime = _SlapmPolicyPurgeTime_Object(
    (1, 3, 6, 1, 3, 88, 1, 1, 6),
    _SlapmPolicyPurgeTime_Type()
)
slapmPolicyPurgeTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slapmPolicyPurgeTime.setStatus("current")
if mibBuilder.loadTexts:
    slapmPolicyPurgeTime.setUnits("seconds")


class _SlapmPolicyTrapEnable_Type(Integer32):
    """Custom type slapmPolicyTrapEnable based on Integer32"""
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


_SlapmPolicyTrapEnable_Type.__name__ = "Integer32"
_SlapmPolicyTrapEnable_Object = MibScalar
slapmPolicyTrapEnable = _SlapmPolicyTrapEnable_Object(
    (1, 3, 6, 1, 3, 88, 1, 1, 7),
    _SlapmPolicyTrapEnable_Type()
)
slapmPolicyTrapEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slapmPolicyTrapEnable.setStatus("current")


class _SlapmPolicyTrapFilter_Type(Integer32):
    """Custom type slapmPolicyTrapFilter based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 64),
    )


_SlapmPolicyTrapFilter_Type.__name__ = "Integer32"
_SlapmPolicyTrapFilter_Object = MibScalar
slapmPolicyTrapFilter = _SlapmPolicyTrapFilter_Object(
    (1, 3, 6, 1, 3, 88, 1, 1, 8),
    _SlapmPolicyTrapFilter_Type()
)
slapmPolicyTrapFilter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slapmPolicyTrapFilter.setStatus("current")
if mibBuilder.loadTexts:
    slapmPolicyTrapFilter.setUnits("intervals")
_SlapmTableObjects_ObjectIdentity = ObjectIdentity
slapmTableObjects = _SlapmTableObjects_ObjectIdentity(
    (1, 3, 6, 1, 3, 88, 1, 2)
)
_SlapmPolicyStatsTable_Object = MibTable
slapmPolicyStatsTable = _SlapmPolicyStatsTable_Object(
    (1, 3, 6, 1, 3, 88, 1, 2, 1)
)
if mibBuilder.loadTexts:
    slapmPolicyStatsTable.setStatus("deprecated")
_SlapmPolicyStatsEntry_Object = MibTableRow
slapmPolicyStatsEntry = _SlapmPolicyStatsEntry_Object(
    (1, 3, 6, 1, 3, 88, 1, 2, 1, 1)
)
slapmPolicyStatsEntry.setIndexNames(
    (0, "SLAPM-MIB", "slapmPolicyStatsSystemAddress"),
    (0, "SLAPM-MIB", "slapmPolicyStatsPolicyName"),
    (0, "SLAPM-MIB", "slapmPolicyStatsTrafficProfileName"),
)
if mibBuilder.loadTexts:
    slapmPolicyStatsEntry.setStatus("deprecated")


class _SlapmPolicyStatsSystemAddress_Type(OctetString):
    """Custom type slapmPolicyStatsSystemAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_SlapmPolicyStatsSystemAddress_Type.__name__ = "OctetString"
_SlapmPolicyStatsSystemAddress_Object = MibTableColumn
slapmPolicyStatsSystemAddress = _SlapmPolicyStatsSystemAddress_Object(
    (1, 3, 6, 1, 3, 88, 1, 2, 1, 1, 1),
    _SlapmPolicyStatsSystemAddress_Type()
)
slapmPolicyStatsSystemAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    slapmPolicyStatsSystemAddress.setStatus("deprecated")
_SlapmPolicyStatsPolicyName_Type = SlapmNameType
_SlapmPolicyStatsPolicyName_Object = MibTableColumn
slapmPolicyStatsPolicyName = _SlapmPolicyStatsPolicyName_Object(
    (1, 3, 6, 1, 3, 88, 1, 2, 1, 1, 2),
    _SlapmPolicyStatsPolicyName_Type()
)
slapmPolicyStatsPolicyName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    slapmPolicyStatsPolicyName.setStatus("deprecated")
_SlapmPolicyStatsTrafficProfileName_Type = SlapmNameType
_SlapmPolicyStatsTrafficProfileName_Object = MibTableColumn
slapmPolicyStatsTrafficProfileName = _SlapmPolicyStatsTrafficProfileName_Object(
    (1, 3, 6, 1, 3, 88, 1, 2, 1, 1, 3),
    _SlapmPolicyStatsTrafficProfileName_Type()
)
slapmPolicyStatsTrafficProfileName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    slapmPolicyStatsTrafficProfileName.setStatus("deprecated")


class _SlapmPolicyStatsOperStatus_Type(Integer32):
    """Custom type slapmPolicyStatsOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("active", 2),
          ("deleteNeeded", 3),
          ("inactive", 1))
    )


_SlapmPolicyStatsOperStatus_Type.__name__ = "Integer32"
_SlapmPolicyStatsOperStatus_Object = MibTableColumn
slapmPolicyStatsOperStatus = _SlapmPolicyStatsOperStatus_Object(
    (1, 3, 6, 1, 3, 88, 1, 2, 1, 1, 4),
    _SlapmPolicyStatsOperStatus_Type()
)
slapmPolicyStatsOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slapmPolicyStatsOperStatus.setStatus("deprecated")
_SlapmPolicyStatsActiveConns_Type = Gauge32
_SlapmPolicyStatsActiveConns_Object = MibTableColumn
slapmPolicyStatsActiveConns = _SlapmPolicyStatsActiveConns_Object(
    (1, 3, 6, 1, 3, 88, 1, 2, 1, 1, 5),
    _SlapmPolicyStatsActiveConns_Type()
)
slapmPolicyStatsActiveConns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slapmPolicyStatsActiveConns.setStatus("deprecated")
_SlapmPolicyStatsTotalConns_Type = Counter32
_SlapmPolicyStatsTotalConns_Object = MibTableColumn
slapmPolicyStatsTotalConns = _SlapmPolicyStatsTotalConns_Object(
    (1, 3, 6, 1, 3, 88, 1, 2, 1, 1, 6),
    _SlapmPolicyStatsTotalConns_Type()
)
slapmPolicyStatsTotalConns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slapmPolicyStatsTotalConns.setStatus("deprecated")


class _SlapmPolicyStatsFirstActivated_Type(DateAndTime):
    """Custom type slapmPolicyStatsFirstActivated based on DateAndTime"""
    defaultHexValue = "0000000000000000"


_SlapmPolicyStatsFirstActivated_Object = MibTableColumn
slapmPolicyStatsFirstActivated = _SlapmPolicyStatsFirstActivated_Object(
    (1, 3, 6, 1, 3, 88, 1, 2, 1, 1, 7),
    _SlapmPolicyStatsFirstActivated_Type()
)
slapmPolicyStatsFirstActivated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slapmPolicyStatsFirstActivated.setStatus("deprecated")


class _SlapmPolicyStatsLastMapping_Type(DateAndTime):
    """Custom type slapmPolicyStatsLastMapping based on DateAndTime"""
    defaultHexValue = "0000000000000000"


_SlapmPolicyStatsLastMapping_Object = MibTableColumn
slapmPolicyStatsLastMapping = _SlapmPolicyStatsLastMapping_Object(
    (1, 3, 6, 1, 3, 88, 1, 2, 1, 1, 8),
    _SlapmPolicyStatsLastMapping_Type()
)
slapmPolicyStatsLastMapping.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slapmPolicyStatsLastMapping.setStatus("deprecated")
_SlapmPolicyStatsInOctets_Type = Counter32
_SlapmPolicyStatsInOctets_Object = MibTableColumn
slapmPolicyStatsInOctets = _SlapmPolicyStatsInOctets_Object(
    (1, 3, 6, 1, 3, 88, 1, 2, 1, 1, 9),
    _SlapmPolicyStatsInOctets_Type()
)
slapmPolicyStatsInOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slapmPolicyStatsInOctets.setStatus("deprecated")
_SlapmPolicyStatsOutOctets_Type = Counter32
_SlapmPolicyStatsOutOctets_Object = MibTableColumn
slapmPolicyStatsOutOctets = _SlapmPolicyStatsOutOctets_Object(
    (1, 3, 6, 1, 3, 88, 1, 2, 1, 1, 10),
    _SlapmPolicyStatsOutOctets_Type()
)
slapmPolicyStatsOutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slapmPolicyStatsOutOctets.setStatus("deprecated")
_SlapmPolicyStatsConnectionLimit_Type = Integer32
_SlapmPolicyStatsConnectionLimit_Object = MibTableColumn
slapmPolicyStatsConnectionLimit = _SlapmPolicyStatsConnectionLimit_Object(
    (1, 3, 6, 1, 3, 88, 1, 2, 1, 1, 11),
    _SlapmPolicyStatsConnectionLimit_Type()
)
slapmPolicyStatsConnectionLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slapmPolicyStatsConnectionLimit.setStatus("deprecated")
_SlapmPolicyStatsCountAccepts_Type = Counter32
_SlapmPolicyStatsCountAccepts_Object = MibTableColumn
slapmPolicyStatsCountAccepts = _SlapmPolicyStatsCountAccepts_Object(
    (1, 3, 6, 1, 3, 88, 1, 2, 1, 1, 12),
    _SlapmPolicyStatsCountAccepts_Type()
)
slapmPolicyStatsCountAccepts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slapmPolicyStatsCountAccepts.setStatus("deprecated")
_SlapmPolicyStatsCountDenies_Type = Counter32
_SlapmPolicyStatsCountDenies_Object = MibTableColumn
slapmPolicyStatsCountDenies = _SlapmPolicyStatsCountDenies_Object(
    (1, 3, 6, 1, 3, 88, 1, 2, 1, 1, 13),
    _SlapmPolicyStatsCountDenies_Type()
)
slapmPolicyStatsCountDenies.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slapmPolicyStatsCountDenies.setStatus("deprecated")
_SlapmPolicyStatsInDiscards_Type = Counter32
_SlapmPolicyStatsInDiscards_Object = MibTableColumn
slapmPolicyStatsInDiscards = _SlapmPolicyStatsInDiscards_Object(
    (1, 3, 6, 1, 3, 88, 1, 2, 1, 1, 14),
    _SlapmPolicyStatsInDiscards_Type()
)
slapmPolicyStatsInDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slapmPolicyStatsInDiscards.setStatus("deprecated")
_SlapmPolicyStatsOutDiscards_Type = Counter32
_SlapmPolicyStatsOutDiscards_Object = MibTableColumn
slapmPolicyStatsOutDiscards = _SlapmPolicyStatsOutDiscards_Object(
    (1, 3, 6, 1, 3, 88, 1, 2, 1, 1, 15),
    _SlapmPolicyStatsOutDiscards_Type()
)
slapmPolicyStatsOutDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slapmPolicyStatsOutDiscards.setStatus("deprecated")
_SlapmPolicyStatsInPackets_Type = Counter32
_SlapmPolicyStatsInPackets_Object = MibTableColumn
slapmPolicyStatsInPackets = _SlapmPolicyStatsInPackets_Object(
    (1, 3, 6, 1, 3, 88, 1, 2, 1, 1, 16),
    _SlapmPolicyStatsInPackets_Type()
)
slapmPolicyStatsInPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slapmPolicyStatsInPackets.setStatus("deprecated")
_SlapmPolicyStatsOutPackets_Type = Counter32
_SlapmPolicyStatsOutPackets_Object = MibTableColumn
slapmPolicyStatsOutPackets = _SlapmPolicyStatsOutPackets_Object(
    (1, 3, 6, 1, 3, 88, 1, 2, 1, 1, 17),
    _SlapmPolicyStatsOutPackets_Type()
)
slapmPolicyStatsOutPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slapmPolicyStatsOutPackets.setStatus("deprecated")
_SlapmPolicyStatsInProfileOctets_Type = Counter32
_SlapmPolicyStatsInProfileOctets_Object = MibTableColumn
slapmPolicyStatsInProfileOctets = _SlapmPolicyStatsInProfileOctets_Object(
    (1, 3, 6, 1, 3, 88, 1, 2, 1, 1, 18),
    _SlapmPolicyStatsInProfileOctets_Type()
)
slapmPolicyStatsInProfileOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slapmPolicyStatsInProfileOctets.setStatus("deprecated")
_SlapmPolicyStatsOutProfileOctets_Type = Counter32
_SlapmPolicyStatsOutProfileOctets_Object = MibTableColumn
slapmPolicyStatsOutProfileOctets = _SlapmPolicyStatsOutProfileOctets_Object(
    (1, 3, 6, 1, 3, 88, 1, 2, 1, 1, 19),
    _SlapmPolicyStatsOutProfileOctets_Type()
)
slapmPolicyStatsOutProfileOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slapmPolicyStatsOutProfileOctets.setStatus("deprecated")
_SlapmPolicyStatsMinRate_Type = Integer32
_SlapmPolicyStatsMinRate_Object = MibTableColumn
slapmPolicyStatsMinRate = _SlapmPolicyStatsMinRate_Object(
    (1, 3, 6, 1, 3, 88, 1, 2, 1, 1, 20),
    _SlapmPolicyStatsMinRate_Type()
)
slapmPolicyStatsMinRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slapmPolicyStatsMinRate.setStatus("deprecated")
if mibBuilder.loadTexts:
    slapmPolicyStatsMinRate.setUnits("Kilobits per second")
_SlapmPolicyStatsMaxRate_Type = Integer32
_SlapmPolicyStatsMaxRate_Object = MibTableColumn
slapmPolicyStatsMaxRate = _SlapmPolicyStatsMaxRate_Object(
    (1, 3, 6, 1, 3, 88, 1, 2, 1, 1, 21),
    _SlapmPolicyStatsMaxRate_Type()
)
slapmPolicyStatsMaxRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slapmPolicyStatsMaxRate.setStatus("deprecated")
if mibBuilder.loadTexts:
    slapmPolicyStatsMaxRate.setUnits("Kilobits per second")
_SlapmPolicyStatsMaxDelay_Type = Integer32
_SlapmPolicyStatsMaxDelay_Object = MibTableColumn
slapmPolicyStatsMaxDelay = _SlapmPolicyStatsMaxDelay_Object(
    (1, 3, 6, 1, 3, 88, 1, 2, 1, 1, 22),
    _SlapmPolicyStatsMaxDelay_Type()
)
slapmPolicyStatsMaxDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slapmPolicyStatsMaxDelay.setStatus("deprecated")
if mibBuilder.loadTexts:
    slapmPolicyStatsMaxDelay.setUnits("milliseconds")
_SlapmPolicyMonitorTable_Object = MibTable
slapmPolicyMonitorTable = _SlapmPolicyMonitorTable_Object(
    (1, 3, 6, 1, 3, 88, 1, 2, 2)
)
if mibBuilder.loadTexts:
    slapmPolicyMonitorTable.setStatus("deprecated")
_SlapmPolicyMonitorEntry_Object = MibTableRow
slapmPolicyMonitorEntry = _SlapmPolicyMonitorEntry_Object(
    (1, 3, 6, 1, 3, 88, 1, 2, 2, 1)
)
slapmPolicyMonitorEntry.setIndexNames(
    (0, "SLAPM-MIB", "slapmPolicyMonitorOwnerIndex"),
    (0, "SLAPM-MIB", "slapmPolicyMonitorSystemAddress"),
    (0, "SLAPM-MIB", "slapmPolicyMonitorPolicyName"),
    (0, "SLAPM-MIB", "slapmPolicyMonitorTrafficProfileName"),
)
if mibBuilder.loadTexts:
    slapmPolicyMonitorEntry.setStatus("deprecated")


class _SlapmPolicyMonitorOwnerIndex_Type(SnmpAdminString):
    """Custom type slapmPolicyMonitorOwnerIndex based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_SlapmPolicyMonitorOwnerIndex_Type.__name__ = "SnmpAdminString"
_SlapmPolicyMonitorOwnerIndex_Object = MibTableColumn
slapmPolicyMonitorOwnerIndex = _SlapmPolicyMonitorOwnerIndex_Object(
    (1, 3, 6, 1, 3, 88, 1, 2, 2, 1, 1),
    _SlapmPolicyMonitorOwnerIndex_Type()
)
slapmPolicyMonitorOwnerIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    slapmPolicyMonitorOwnerIndex.setStatus("deprecated")


class _SlapmPolicyMonitorSystemAddress_Type(OctetString):
    """Custom type slapmPolicyMonitorSystemAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_SlapmPolicyMonitorSystemAddress_Type.__name__ = "OctetString"
_SlapmPolicyMonitorSystemAddress_Object = MibTableColumn
slapmPolicyMonitorSystemAddress = _SlapmPolicyMonitorSystemAddress_Object(
    (1, 3, 6, 1, 3, 88, 1, 2, 2, 1, 2),
    _SlapmPolicyMonitorSystemAddress_Type()
)
slapmPolicyMonitorSystemAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    slapmPolicyMonitorSystemAddress.setStatus("deprecated")
_SlapmPolicyMonitorPolicyName_Type = SlapmNameType
_SlapmPolicyMonitorPolicyName_Object = MibTableColumn
slapmPolicyMonitorPolicyName = _SlapmPolicyMonitorPolicyName_Object(
    (1, 3, 6, 1, 3, 88, 1, 2, 2, 1, 3),
    _SlapmPolicyMonitorPolicyName_Type()
)
slapmPolicyMonitorPolicyName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    slapmPolicyMonitorPolicyName.setStatus("deprecated")
_SlapmPolicyMonitorTrafficProfileName_Type = SlapmNameType
_SlapmPolicyMonitorTrafficProfileName_Object = MibTableColumn
slapmPolicyMonitorTrafficProfileName = _SlapmPolicyMonitorTrafficProfileName_Object(
    (1, 3, 6, 1, 3, 88, 1, 2, 2, 1, 4),
    _SlapmPolicyMonitorTrafficProfileName_Type()
)
slapmPolicyMonitorTrafficProfileName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    slapmPolicyMonitorTrafficProfileName.setStatus("deprecated")


class _SlapmPolicyMonitorControl_Type(Bits):
    """Custom type slapmPolicyMonitorControl based on Bits"""
    defaultBinValue = "111"

    namedValues = NamedValues(
        *(("enableAggregateTraps", 3),
          ("enableSubcomponentTraps", 4),
          ("monitorMaxDelay", 2),
          ("monitorMaxRate", 1),
          ("monitorMinRate", 0),
          ("monitorSubcomponents", 5))
    )

_SlapmPolicyMonitorControl_Type.__name__ = "Bits"
_SlapmPolicyMonitorControl_Object = MibTableColumn
slapmPolicyMonitorControl = _SlapmPolicyMonitorControl_Object(
    (1, 3, 6, 1, 3, 88, 1, 2, 2, 1, 5),
    _SlapmPolicyMonitorControl_Type()
)
slapmPolicyMonitorControl.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    slapmPolicyMonitorControl.setStatus("deprecated")
_SlapmPolicyMonitorStatus_Type = SlapmStatus
_SlapmPolicyMonitorStatus_Object = MibTableColumn
slapmPolicyMonitorStatus = _SlapmPolicyMonitorStatus_Object(
    (1, 3, 6, 1, 3, 88, 1, 2, 2, 1, 6),
    _SlapmPolicyMonitorStatus_Type()
)
slapmPolicyMonitorStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slapmPolicyMonitorStatus.setStatus("deprecated")


class _SlapmPolicyMonitorInterval_Type(Integer32):
    """Custom type slapmPolicyMonitorInterval based on Integer32"""
    defaultValue = 20

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(15, 86400),
    )


_SlapmPolicyMonitorInterval_Type.__name__ = "Integer32"
_SlapmPolicyMonitorInterval_Object = MibTableColumn
slapmPolicyMonitorInterval = _SlapmPolicyMonitorInterval_Object(
    (1, 3, 6, 1, 3, 88, 1, 2, 2, 1, 7),
    _SlapmPolicyMonitorInterval_Type()
)
slapmPolicyMonitorInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    slapmPolicyMonitorInterval.setStatus("deprecated")
if mibBuilder.loadTexts:
    slapmPolicyMonitorInterval.setUnits("seconds")


class _SlapmPolicyMonitorIntTime_Type(DateAndTime):
    """Custom type slapmPolicyMonitorIntTime based on DateAndTime"""
    defaultHexValue = "0000000000000000"


_SlapmPolicyMonitorIntTime_Object = MibTableColumn
slapmPolicyMonitorIntTime = _SlapmPolicyMonitorIntTime_Object(
    (1, 3, 6, 1, 3, 88, 1, 2, 2, 1, 8),
    _SlapmPolicyMonitorIntTime_Type()
)
slapmPolicyMonitorIntTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slapmPolicyMonitorIntTime.setStatus("deprecated")
_SlapmPolicyMonitorCurrentInRate_Type = Gauge32
_SlapmPolicyMonitorCurrentInRate_Object = MibTableColumn
slapmPolicyMonitorCurrentInRate = _SlapmPolicyMonitorCurrentInRate_Object(
    (1, 3, 6, 1, 3, 88, 1, 2, 2, 1, 9),
    _SlapmPolicyMonitorCurrentInRate_Type()
)
slapmPolicyMonitorCurrentInRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slapmPolicyMonitorCurrentInRate.setStatus("deprecated")
if mibBuilder.loadTexts:
    slapmPolicyMonitorCurrentInRate.setUnits("kilobits per second")
_SlapmPolicyMonitorCurrentOutRate_Type = Gauge32
_SlapmPolicyMonitorCurrentOutRate_Object = MibTableColumn
slapmPolicyMonitorCurrentOutRate = _SlapmPolicyMonitorCurrentOutRate_Object(
    (1, 3, 6, 1, 3, 88, 1, 2, 2, 1, 10),
    _SlapmPolicyMonitorCurrentOutRate_Type()
)
slapmPolicyMonitorCurrentOutRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slapmPolicyMonitorCurrentOutRate.setStatus("deprecated")
if mibBuilder.loadTexts:
    slapmPolicyMonitorCurrentOutRate.setUnits("kilobits per second")
_SlapmPolicyMonitorMinRateLow_Type = Integer32
_SlapmPolicyMonitorMinRateLow_Object = MibTableColumn
slapmPolicyMonitorMinRateLow = _SlapmPolicyMonitorMinRateLow_Object(
    (1, 3, 6, 1, 3, 88, 1, 2, 2, 1, 11),
    _SlapmPolicyMonitorMinRateLow_Type()
)
slapmPolicyMonitorMinRateLow.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    slapmPolicyMonitorMinRateLow.setStatus("deprecated")
if mibBuilder.loadTexts:
    slapmPolicyMonitorMinRateLow.setUnits("kilobits per second")
_SlapmPolicyMonitorMinRateHigh_Type = Integer32
_SlapmPolicyMonitorMinRateHigh_Object = MibTableColumn
slapmPolicyMonitorMinRateHigh = _SlapmPolicyMonitorMinRateHigh_Object(
    (1, 3, 6, 1, 3, 88, 1, 2, 2, 1, 12),
    _SlapmPolicyMonitorMinRateHigh_Type()
)
slapmPolicyMonitorMinRateHigh.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    slapmPolicyMonitorMinRateHigh.setStatus("deprecated")
if mibBuilder.loadTexts:
    slapmPolicyMonitorMinRateHigh.setUnits("kilobits per second")
_SlapmPolicyMonitorMaxRateHigh_Type = Integer32
_SlapmPolicyMonitorMaxRateHigh_Object = MibTableColumn
slapmPolicyMonitorMaxRateHigh = _SlapmPolicyMonitorMaxRateHigh_Object(
    (1, 3, 6, 1, 3, 88, 1, 2, 2, 1, 13),
    _SlapmPolicyMonitorMaxRateHigh_Type()
)
slapmPolicyMonitorMaxRateHigh.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    slapmPolicyMonitorMaxRateHigh.setStatus("deprecated")
if mibBuilder.loadTexts:
    slapmPolicyMonitorMaxRateHigh.setUnits("kilobits per second")
_SlapmPolicyMonitorMaxRateLow_Type = Integer32
_SlapmPolicyMonitorMaxRateLow_Object = MibTableColumn
slapmPolicyMonitorMaxRateLow = _SlapmPolicyMonitorMaxRateLow_Object(
    (1, 3, 6, 1, 3, 88, 1, 2, 2, 1, 14),
    _SlapmPolicyMonitorMaxRateLow_Type()
)
slapmPolicyMonitorMaxRateLow.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    slapmPolicyMonitorMaxRateLow.setStatus("deprecated")
if mibBuilder.loadTexts:
    slapmPolicyMonitorMaxRateLow.setUnits("kilobits per second")
_SlapmPolicyMonitorMaxDelayHigh_Type = Integer32
_SlapmPolicyMonitorMaxDelayHigh_Object = MibTableColumn
slapmPolicyMonitorMaxDelayHigh = _SlapmPolicyMonitorMaxDelayHigh_Object(
    (1, 3, 6, 1, 3, 88, 1, 2, 2, 1, 15),
    _SlapmPolicyMonitorMaxDelayHigh_Type()
)
slapmPolicyMonitorMaxDelayHigh.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    slapmPolicyMonitorMaxDelayHigh.setStatus("deprecated")
if mibBuilder.loadTexts:
    slapmPolicyMonitorMaxDelayHigh.setUnits("milliseconds")
_SlapmPolicyMonitorMaxDelayLow_Type = Integer32
_SlapmPolicyMonitorMaxDelayLow_Object = MibTableColumn
slapmPolicyMonitorMaxDelayLow = _SlapmPolicyMonitorMaxDelayLow_Object(
    (1, 3, 6, 1, 3, 88, 1, 2, 2, 1, 16),
    _SlapmPolicyMonitorMaxDelayLow_Type()
)
slapmPolicyMonitorMaxDelayLow.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    slapmPolicyMonitorMaxDelayLow.setStatus("deprecated")
if mibBuilder.loadTexts:
    slapmPolicyMonitorMaxDelayLow.setUnits("milliseconds")
_SlapmPolicyMonitorMinInRateNotAchieves_Type = Counter32
_SlapmPolicyMonitorMinInRateNotAchieves_Object = MibTableColumn
slapmPolicyMonitorMinInRateNotAchieves = _SlapmPolicyMonitorMinInRateNotAchieves_Object(
    (1, 3, 6, 1, 3, 88, 1, 2, 2, 1, 17),
    _SlapmPolicyMonitorMinInRateNotAchieves_Type()
)
slapmPolicyMonitorMinInRateNotAchieves.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slapmPolicyMonitorMinInRateNotAchieves.setStatus("deprecated")
_SlapmPolicyMonitorMaxInRateExceeds_Type = Counter32
_SlapmPolicyMonitorMaxInRateExceeds_Object = MibTableColumn
slapmPolicyMonitorMaxInRateExceeds = _SlapmPolicyMonitorMaxInRateExceeds_Object(
    (1, 3, 6, 1, 3, 88, 1, 2, 2, 1, 18),
    _SlapmPolicyMonitorMaxInRateExceeds_Type()
)
slapmPolicyMonitorMaxInRateExceeds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slapmPolicyMonitorMaxInRateExceeds.setStatus("deprecated")
_SlapmPolicyMonitorMaxDelayExceeds_Type = Counter32
_SlapmPolicyMonitorMaxDelayExceeds_Object = MibTableColumn
slapmPolicyMonitorMaxDelayExceeds = _SlapmPolicyMonitorMaxDelayExceeds_Object(
    (1, 3, 6, 1, 3, 88, 1, 2, 2, 1, 19),
    _SlapmPolicyMonitorMaxDelayExceeds_Type()
)
slapmPolicyMonitorMaxDelayExceeds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slapmPolicyMonitorMaxDelayExceeds.setStatus("deprecated")
_SlapmPolicyMonitorMinOutRateNotAchieves_Type = Counter32
_SlapmPolicyMonitorMinOutRateNotAchieves_Object = MibTableColumn
slapmPolicyMonitorMinOutRateNotAchieves = _SlapmPolicyMonitorMinOutRateNotAchieves_Object(
    (1, 3, 6, 1, 3, 88, 1, 2, 2, 1, 20),
    _SlapmPolicyMonitorMinOutRateNotAchieves_Type()
)
slapmPolicyMonitorMinOutRateNotAchieves.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slapmPolicyMonitorMinOutRateNotAchieves.setStatus("deprecated")
_SlapmPolicyMonitorMaxOutRateExceeds_Type = Counter32
_SlapmPolicyMonitorMaxOutRateExceeds_Object = MibTableColumn
slapmPolicyMonitorMaxOutRateExceeds = _SlapmPolicyMonitorMaxOutRateExceeds_Object(
    (1, 3, 6, 1, 3, 88, 1, 2, 2, 1, 21),
    _SlapmPolicyMonitorMaxOutRateExceeds_Type()
)
slapmPolicyMonitorMaxOutRateExceeds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slapmPolicyMonitorMaxOutRateExceeds.setStatus("deprecated")
_SlapmPolicyMonitorCurrentDelayRate_Type = Gauge32
_SlapmPolicyMonitorCurrentDelayRate_Object = MibTableColumn
slapmPolicyMonitorCurrentDelayRate = _SlapmPolicyMonitorCurrentDelayRate_Object(
    (1, 3, 6, 1, 3, 88, 1, 2, 2, 1, 22),
    _SlapmPolicyMonitorCurrentDelayRate_Type()
)
slapmPolicyMonitorCurrentDelayRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slapmPolicyMonitorCurrentDelayRate.setStatus("deprecated")
if mibBuilder.loadTexts:
    slapmPolicyMonitorCurrentDelayRate.setUnits("milliseconds")
_SlapmPolicyMonitorRowStatus_Type = RowStatus
_SlapmPolicyMonitorRowStatus_Object = MibTableColumn
slapmPolicyMonitorRowStatus = _SlapmPolicyMonitorRowStatus_Object(
    (1, 3, 6, 1, 3, 88, 1, 2, 2, 1, 23),
    _SlapmPolicyMonitorRowStatus_Type()
)
slapmPolicyMonitorRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    slapmPolicyMonitorRowStatus.setStatus("deprecated")
_SlapmSubcomponentTable_Object = MibTable
slapmSubcomponentTable = _SlapmSubcomponentTable_Object(
    (1, 3, 6, 1, 3, 88, 1, 2, 3)
)
if mibBuilder.loadTexts:
    slapmSubcomponentTable.setStatus("current")
_SlapmSubcomponentEntry_Object = MibTableRow
slapmSubcomponentEntry = _SlapmSubcomponentEntry_Object(
    (1, 3, 6, 1, 3, 88, 1, 2, 3, 1)
)
slapmSubcomponentEntry.setIndexNames(
    (0, "SLAPM-MIB", "slapmSubcomponentRemAddress"),
    (0, "SLAPM-MIB", "slapmSubcomponentRemPort"),
    (0, "SLAPM-MIB", "slapmSubcomponentLocalAddress"),
    (0, "SLAPM-MIB", "slapmSubcomponentLocalPort"),
)
if mibBuilder.loadTexts:
    slapmSubcomponentEntry.setStatus("current")


class _SlapmSubcomponentRemAddress_Type(OctetString):
    """Custom type slapmSubcomponentRemAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_SlapmSubcomponentRemAddress_Type.__name__ = "OctetString"
_SlapmSubcomponentRemAddress_Object = MibTableColumn
slapmSubcomponentRemAddress = _SlapmSubcomponentRemAddress_Object(
    (1, 3, 6, 1, 3, 88, 1, 2, 3, 1, 1),
    _SlapmSubcomponentRemAddress_Type()
)
slapmSubcomponentRemAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    slapmSubcomponentRemAddress.setStatus("current")


class _SlapmSubcomponentRemPort_Type(Integer32):
    """Custom type slapmSubcomponentRemPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SlapmSubcomponentRemPort_Type.__name__ = "Integer32"
_SlapmSubcomponentRemPort_Object = MibTableColumn
slapmSubcomponentRemPort = _SlapmSubcomponentRemPort_Object(
    (1, 3, 6, 1, 3, 88, 1, 2, 3, 1, 2),
    _SlapmSubcomponentRemPort_Type()
)
slapmSubcomponentRemPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    slapmSubcomponentRemPort.setStatus("current")


class _SlapmSubcomponentLocalAddress_Type(OctetString):
    """Custom type slapmSubcomponentLocalAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_SlapmSubcomponentLocalAddress_Type.__name__ = "OctetString"
_SlapmSubcomponentLocalAddress_Object = MibTableColumn
slapmSubcomponentLocalAddress = _SlapmSubcomponentLocalAddress_Object(
    (1, 3, 6, 1, 3, 88, 1, 2, 3, 1, 3),
    _SlapmSubcomponentLocalAddress_Type()
)
slapmSubcomponentLocalAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    slapmSubcomponentLocalAddress.setStatus("current")


class _SlapmSubcomponentLocalPort_Type(Integer32):
    """Custom type slapmSubcomponentLocalPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SlapmSubcomponentLocalPort_Type.__name__ = "Integer32"
_SlapmSubcomponentLocalPort_Object = MibTableColumn
slapmSubcomponentLocalPort = _SlapmSubcomponentLocalPort_Object(
    (1, 3, 6, 1, 3, 88, 1, 2, 3, 1, 4),
    _SlapmSubcomponentLocalPort_Type()
)
slapmSubcomponentLocalPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    slapmSubcomponentLocalPort.setStatus("current")


class _SlapmSubcomponentProtocol_Type(Integer32):
    """Custom type slapmSubcomponentProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("tcpConnection", 2),
          ("udpListener", 1))
    )


_SlapmSubcomponentProtocol_Type.__name__ = "Integer32"
_SlapmSubcomponentProtocol_Object = MibTableColumn
slapmSubcomponentProtocol = _SlapmSubcomponentProtocol_Object(
    (1, 3, 6, 1, 3, 88, 1, 2, 3, 1, 5),
    _SlapmSubcomponentProtocol_Type()
)
slapmSubcomponentProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slapmSubcomponentProtocol.setStatus("current")


class _SlapmSubcomponentSystemAddress_Type(OctetString):
    """Custom type slapmSubcomponentSystemAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_SlapmSubcomponentSystemAddress_Type.__name__ = "OctetString"
_SlapmSubcomponentSystemAddress_Object = MibTableColumn
slapmSubcomponentSystemAddress = _SlapmSubcomponentSystemAddress_Object(
    (1, 3, 6, 1, 3, 88, 1, 2, 3, 1, 6),
    _SlapmSubcomponentSystemAddress_Type()
)
slapmSubcomponentSystemAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slapmSubcomponentSystemAddress.setStatus("current")
_SlapmSubcomponentPolicyName_Type = SlapmNameType
_SlapmSubcomponentPolicyName_Object = MibTableColumn
slapmSubcomponentPolicyName = _SlapmSubcomponentPolicyName_Object(
    (1, 3, 6, 1, 3, 88, 1, 2, 3, 1, 7),
    _SlapmSubcomponentPolicyName_Type()
)
slapmSubcomponentPolicyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slapmSubcomponentPolicyName.setStatus("deprecated")
_SlapmSubcomponentTrafficProfileName_Type = SlapmNameType
_SlapmSubcomponentTrafficProfileName_Object = MibTableColumn
slapmSubcomponentTrafficProfileName = _SlapmSubcomponentTrafficProfileName_Object(
    (1, 3, 6, 1, 3, 88, 1, 2, 3, 1, 8),
    _SlapmSubcomponentTrafficProfileName_Type()
)
slapmSubcomponentTrafficProfileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slapmSubcomponentTrafficProfileName.setStatus("deprecated")


class _SlapmSubcomponentLastActivity_Type(DateAndTime):
    """Custom type slapmSubcomponentLastActivity based on DateAndTime"""
    defaultHexValue = "0000000000000000"


_SlapmSubcomponentLastActivity_Object = MibTableColumn
slapmSubcomponentLastActivity = _SlapmSubcomponentLastActivity_Object(
    (1, 3, 6, 1, 3, 88, 1, 2, 3, 1, 9),
    _SlapmSubcomponentLastActivity_Type()
)
slapmSubcomponentLastActivity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slapmSubcomponentLastActivity.setStatus("current")
_SlapmSubcomponentInOctets_Type = Counter32
_SlapmSubcomponentInOctets_Object = MibTableColumn
slapmSubcomponentInOctets = _SlapmSubcomponentInOctets_Object(
    (1, 3, 6, 1, 3, 88, 1, 2, 3, 1, 10),
    _SlapmSubcomponentInOctets_Type()
)
slapmSubcomponentInOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slapmSubcomponentInOctets.setStatus("current")
_SlapmSubcomponentOutOctets_Type = Counter32
_SlapmSubcomponentOutOctets_Object = MibTableColumn
slapmSubcomponentOutOctets = _SlapmSubcomponentOutOctets_Object(
    (1, 3, 6, 1, 3, 88, 1, 2, 3, 1, 11),
    _SlapmSubcomponentOutOctets_Type()
)
slapmSubcomponentOutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slapmSubcomponentOutOctets.setStatus("current")
_SlapmSubcomponentTcpOutBufferedOctets_Type = Counter32
_SlapmSubcomponentTcpOutBufferedOctets_Object = MibTableColumn
slapmSubcomponentTcpOutBufferedOctets = _SlapmSubcomponentTcpOutBufferedOctets_Object(
    (1, 3, 6, 1, 3, 88, 1, 2, 3, 1, 12),
    _SlapmSubcomponentTcpOutBufferedOctets_Type()
)
slapmSubcomponentTcpOutBufferedOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slapmSubcomponentTcpOutBufferedOctets.setStatus("current")
_SlapmSubcomponentTcpInBufferedOctets_Type = Counter32
_SlapmSubcomponentTcpInBufferedOctets_Object = MibTableColumn
slapmSubcomponentTcpInBufferedOctets = _SlapmSubcomponentTcpInBufferedOctets_Object(
    (1, 3, 6, 1, 3, 88, 1, 2, 3, 1, 13),
    _SlapmSubcomponentTcpInBufferedOctets_Type()
)
slapmSubcomponentTcpInBufferedOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slapmSubcomponentTcpInBufferedOctets.setStatus("current")
_SlapmSubcomponentTcpReXmts_Type = Counter32
_SlapmSubcomponentTcpReXmts_Object = MibTableColumn
slapmSubcomponentTcpReXmts = _SlapmSubcomponentTcpReXmts_Object(
    (1, 3, 6, 1, 3, 88, 1, 2, 3, 1, 14),
    _SlapmSubcomponentTcpReXmts_Type()
)
slapmSubcomponentTcpReXmts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slapmSubcomponentTcpReXmts.setStatus("current")
_SlapmSubcomponentTcpRoundTripTime_Type = Integer32
_SlapmSubcomponentTcpRoundTripTime_Object = MibTableColumn
slapmSubcomponentTcpRoundTripTime = _SlapmSubcomponentTcpRoundTripTime_Object(
    (1, 3, 6, 1, 3, 88, 1, 2, 3, 1, 15),
    _SlapmSubcomponentTcpRoundTripTime_Type()
)
slapmSubcomponentTcpRoundTripTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slapmSubcomponentTcpRoundTripTime.setStatus("current")
if mibBuilder.loadTexts:
    slapmSubcomponentTcpRoundTripTime.setUnits("milliseconds")
_SlapmSubcomponentTcpRoundTripVariance_Type = Integer32
_SlapmSubcomponentTcpRoundTripVariance_Object = MibTableColumn
slapmSubcomponentTcpRoundTripVariance = _SlapmSubcomponentTcpRoundTripVariance_Object(
    (1, 3, 6, 1, 3, 88, 1, 2, 3, 1, 16),
    _SlapmSubcomponentTcpRoundTripVariance_Type()
)
slapmSubcomponentTcpRoundTripVariance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slapmSubcomponentTcpRoundTripVariance.setStatus("current")
_SlapmSubcomponentInPdus_Type = Counter32
_SlapmSubcomponentInPdus_Object = MibTableColumn
slapmSubcomponentInPdus = _SlapmSubcomponentInPdus_Object(
    (1, 3, 6, 1, 3, 88, 1, 2, 3, 1, 17),
    _SlapmSubcomponentInPdus_Type()
)
slapmSubcomponentInPdus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slapmSubcomponentInPdus.setStatus("current")
_SlapmSubcomponentOutPdus_Type = Counter32
_SlapmSubcomponentOutPdus_Object = MibTableColumn
slapmSubcomponentOutPdus = _SlapmSubcomponentOutPdus_Object(
    (1, 3, 6, 1, 3, 88, 1, 2, 3, 1, 18),
    _SlapmSubcomponentOutPdus_Type()
)
slapmSubcomponentOutPdus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slapmSubcomponentOutPdus.setStatus("current")


class _SlapmSubcomponentApplName_Type(SnmpAdminString):
    """Custom type slapmSubcomponentApplName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_SlapmSubcomponentApplName_Type.__name__ = "SnmpAdminString"
_SlapmSubcomponentApplName_Object = MibTableColumn
slapmSubcomponentApplName = _SlapmSubcomponentApplName_Object(
    (1, 3, 6, 1, 3, 88, 1, 2, 3, 1, 19),
    _SlapmSubcomponentApplName_Type()
)
slapmSubcomponentApplName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slapmSubcomponentApplName.setStatus("current")
_SlapmSubcomponentMonitorStatus_Type = SlapmStatus
_SlapmSubcomponentMonitorStatus_Object = MibTableColumn
slapmSubcomponentMonitorStatus = _SlapmSubcomponentMonitorStatus_Object(
    (1, 3, 6, 1, 3, 88, 1, 2, 3, 1, 20),
    _SlapmSubcomponentMonitorStatus_Type()
)
slapmSubcomponentMonitorStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slapmSubcomponentMonitorStatus.setStatus("current")


class _SlapmSubcomponentMonitorIntTime_Type(DateAndTime):
    """Custom type slapmSubcomponentMonitorIntTime based on DateAndTime"""
    defaultHexValue = "0000000000000000"


_SlapmSubcomponentMonitorIntTime_Object = MibTableColumn
slapmSubcomponentMonitorIntTime = _SlapmSubcomponentMonitorIntTime_Object(
    (1, 3, 6, 1, 3, 88, 1, 2, 3, 1, 21),
    _SlapmSubcomponentMonitorIntTime_Type()
)
slapmSubcomponentMonitorIntTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slapmSubcomponentMonitorIntTime.setStatus("current")
_SlapmSubcomponentMonitorCurrentInRate_Type = Gauge32
_SlapmSubcomponentMonitorCurrentInRate_Object = MibTableColumn
slapmSubcomponentMonitorCurrentInRate = _SlapmSubcomponentMonitorCurrentInRate_Object(
    (1, 3, 6, 1, 3, 88, 1, 2, 3, 1, 22),
    _SlapmSubcomponentMonitorCurrentInRate_Type()
)
slapmSubcomponentMonitorCurrentInRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slapmSubcomponentMonitorCurrentInRate.setStatus("current")
if mibBuilder.loadTexts:
    slapmSubcomponentMonitorCurrentInRate.setUnits("kilobits per second")
_SlapmSubcomponentMonitorCurrentOutRate_Type = Gauge32
_SlapmSubcomponentMonitorCurrentOutRate_Object = MibTableColumn
slapmSubcomponentMonitorCurrentOutRate = _SlapmSubcomponentMonitorCurrentOutRate_Object(
    (1, 3, 6, 1, 3, 88, 1, 2, 3, 1, 23),
    _SlapmSubcomponentMonitorCurrentOutRate_Type()
)
slapmSubcomponentMonitorCurrentOutRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slapmSubcomponentMonitorCurrentOutRate.setStatus("current")
if mibBuilder.loadTexts:
    slapmSubcomponentMonitorCurrentOutRate.setUnits("kilobits per second")


class _SlapmSubcomponentPolicyRuleIndex_Type(Unsigned32):
    """Custom type slapmSubcomponentPolicyRuleIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_SlapmSubcomponentPolicyRuleIndex_Type.__name__ = "Unsigned32"
_SlapmSubcomponentPolicyRuleIndex_Object = MibTableColumn
slapmSubcomponentPolicyRuleIndex = _SlapmSubcomponentPolicyRuleIndex_Object(
    (1, 3, 6, 1, 3, 88, 1, 2, 3, 1, 24),
    _SlapmSubcomponentPolicyRuleIndex_Type()
)
slapmSubcomponentPolicyRuleIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slapmSubcomponentPolicyRuleIndex.setStatus("current")
_SlapmPolicyNameTable_Object = MibTable
slapmPolicyNameTable = _SlapmPolicyNameTable_Object(
    (1, 3, 6, 1, 3, 88, 1, 2, 4)
)
if mibBuilder.loadTexts:
    slapmPolicyNameTable.setStatus("current")
_SlapmPolicyNameEntry_Object = MibTableRow
slapmPolicyNameEntry = _SlapmPolicyNameEntry_Object(
    (1, 3, 6, 1, 3, 88, 1, 2, 4, 1)
)
slapmPolicyNameEntry.setIndexNames(
    (0, "SLAPM-MIB", "slapmPolicyNameSystemAddress"),
    (0, "SLAPM-MIB", "slapmPolicyNameIndex"),
)
if mibBuilder.loadTexts:
    slapmPolicyNameEntry.setStatus("current")


class _SlapmPolicyNameSystemAddress_Type(OctetString):
    """Custom type slapmPolicyNameSystemAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_SlapmPolicyNameSystemAddress_Type.__name__ = "OctetString"
_SlapmPolicyNameSystemAddress_Object = MibTableColumn
slapmPolicyNameSystemAddress = _SlapmPolicyNameSystemAddress_Object(
    (1, 3, 6, 1, 3, 88, 1, 2, 4, 1, 1),
    _SlapmPolicyNameSystemAddress_Type()
)
slapmPolicyNameSystemAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    slapmPolicyNameSystemAddress.setStatus("current")


class _SlapmPolicyNameIndex_Type(Unsigned32):
    """Custom type slapmPolicyNameIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_SlapmPolicyNameIndex_Type.__name__ = "Unsigned32"
_SlapmPolicyNameIndex_Object = MibTableColumn
slapmPolicyNameIndex = _SlapmPolicyNameIndex_Object(
    (1, 3, 6, 1, 3, 88, 1, 2, 4, 1, 2),
    _SlapmPolicyNameIndex_Type()
)
slapmPolicyNameIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    slapmPolicyNameIndex.setStatus("current")
_SlapmPolicyNameOfRule_Type = SlapmPolicyRuleName
_SlapmPolicyNameOfRule_Object = MibTableColumn
slapmPolicyNameOfRule = _SlapmPolicyNameOfRule_Object(
    (1, 3, 6, 1, 3, 88, 1, 2, 4, 1, 3),
    _SlapmPolicyNameOfRule_Type()
)
slapmPolicyNameOfRule.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slapmPolicyNameOfRule.setStatus("current")
_SlapmPolicyRuleStatsTable_Object = MibTable
slapmPolicyRuleStatsTable = _SlapmPolicyRuleStatsTable_Object(
    (1, 3, 6, 1, 3, 88, 1, 2, 5)
)
if mibBuilder.loadTexts:
    slapmPolicyRuleStatsTable.setStatus("current")
_SlapmPolicyRuleStatsEntry_Object = MibTableRow
slapmPolicyRuleStatsEntry = _SlapmPolicyRuleStatsEntry_Object(
    (1, 3, 6, 1, 3, 88, 1, 2, 5, 1)
)
slapmPolicyRuleStatsEntry.setIndexNames(
    (0, "SLAPM-MIB", "slapmPolicyNameSystemAddress"),
    (0, "SLAPM-MIB", "slapmPolicyNameIndex"),
)
if mibBuilder.loadTexts:
    slapmPolicyRuleStatsEntry.setStatus("current")


class _SlapmPolicyRuleStatsOperStatus_Type(Integer32):
    """Custom type slapmPolicyRuleStatsOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("active", 2),
          ("deleteNeeded", 3),
          ("inactive", 1))
    )


_SlapmPolicyRuleStatsOperStatus_Type.__name__ = "Integer32"
_SlapmPolicyRuleStatsOperStatus_Object = MibTableColumn
slapmPolicyRuleStatsOperStatus = _SlapmPolicyRuleStatsOperStatus_Object(
    (1, 3, 6, 1, 3, 88, 1, 2, 5, 1, 1),
    _SlapmPolicyRuleStatsOperStatus_Type()
)
slapmPolicyRuleStatsOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slapmPolicyRuleStatsOperStatus.setStatus("current")
_SlapmPolicyRuleStatsActiveConns_Type = Gauge32
_SlapmPolicyRuleStatsActiveConns_Object = MibTableColumn
slapmPolicyRuleStatsActiveConns = _SlapmPolicyRuleStatsActiveConns_Object(
    (1, 3, 6, 1, 3, 88, 1, 2, 5, 1, 2),
    _SlapmPolicyRuleStatsActiveConns_Type()
)
slapmPolicyRuleStatsActiveConns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slapmPolicyRuleStatsActiveConns.setStatus("current")
_SlapmPolicyRuleStatsTotalConns_Type = Counter32
_SlapmPolicyRuleStatsTotalConns_Object = MibTableColumn
slapmPolicyRuleStatsTotalConns = _SlapmPolicyRuleStatsTotalConns_Object(
    (1, 3, 6, 1, 3, 88, 1, 2, 5, 1, 3),
    _SlapmPolicyRuleStatsTotalConns_Type()
)
slapmPolicyRuleStatsTotalConns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slapmPolicyRuleStatsTotalConns.setStatus("current")


class _SlapmPolicyRuleStatsLActivated_Type(DateAndTime):
    """Custom type slapmPolicyRuleStatsLActivated based on DateAndTime"""
    defaultHexValue = "0000000000000000"


_SlapmPolicyRuleStatsLActivated_Object = MibTableColumn
slapmPolicyRuleStatsLActivated = _SlapmPolicyRuleStatsLActivated_Object(
    (1, 3, 6, 1, 3, 88, 1, 2, 5, 1, 4),
    _SlapmPolicyRuleStatsLActivated_Type()
)
slapmPolicyRuleStatsLActivated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slapmPolicyRuleStatsLActivated.setStatus("current")


class _SlapmPolicyRuleStatsLastMapping_Type(DateAndTime):
    """Custom type slapmPolicyRuleStatsLastMapping based on DateAndTime"""
    defaultHexValue = "0000000000000000"


_SlapmPolicyRuleStatsLastMapping_Object = MibTableColumn
slapmPolicyRuleStatsLastMapping = _SlapmPolicyRuleStatsLastMapping_Object(
    (1, 3, 6, 1, 3, 88, 1, 2, 5, 1, 5),
    _SlapmPolicyRuleStatsLastMapping_Type()
)
slapmPolicyRuleStatsLastMapping.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slapmPolicyRuleStatsLastMapping.setStatus("current")
_SlapmPolicyRuleStatsInOctets_Type = Counter32
_SlapmPolicyRuleStatsInOctets_Object = MibTableColumn
slapmPolicyRuleStatsInOctets = _SlapmPolicyRuleStatsInOctets_Object(
    (1, 3, 6, 1, 3, 88, 1, 2, 5, 1, 6),
    _SlapmPolicyRuleStatsInOctets_Type()
)
slapmPolicyRuleStatsInOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slapmPolicyRuleStatsInOctets.setStatus("current")
_SlapmPolicyRuleStatsOutOctets_Type = Counter32
_SlapmPolicyRuleStatsOutOctets_Object = MibTableColumn
slapmPolicyRuleStatsOutOctets = _SlapmPolicyRuleStatsOutOctets_Object(
    (1, 3, 6, 1, 3, 88, 1, 2, 5, 1, 7),
    _SlapmPolicyRuleStatsOutOctets_Type()
)
slapmPolicyRuleStatsOutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slapmPolicyRuleStatsOutOctets.setStatus("current")
_SlapmPolicyRuleStatsConnLimit_Type = Unsigned32
_SlapmPolicyRuleStatsConnLimit_Object = MibTableColumn
slapmPolicyRuleStatsConnLimit = _SlapmPolicyRuleStatsConnLimit_Object(
    (1, 3, 6, 1, 3, 88, 1, 2, 5, 1, 8),
    _SlapmPolicyRuleStatsConnLimit_Type()
)
slapmPolicyRuleStatsConnLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slapmPolicyRuleStatsConnLimit.setStatus("current")
_SlapmPolicyRuleStatsCountAccepts_Type = Counter32
_SlapmPolicyRuleStatsCountAccepts_Object = MibTableColumn
slapmPolicyRuleStatsCountAccepts = _SlapmPolicyRuleStatsCountAccepts_Object(
    (1, 3, 6, 1, 3, 88, 1, 2, 5, 1, 9),
    _SlapmPolicyRuleStatsCountAccepts_Type()
)
slapmPolicyRuleStatsCountAccepts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slapmPolicyRuleStatsCountAccepts.setStatus("current")
_SlapmPolicyRuleStatsCountDenies_Type = Counter32
_SlapmPolicyRuleStatsCountDenies_Object = MibTableColumn
slapmPolicyRuleStatsCountDenies = _SlapmPolicyRuleStatsCountDenies_Object(
    (1, 3, 6, 1, 3, 88, 1, 2, 5, 1, 10),
    _SlapmPolicyRuleStatsCountDenies_Type()
)
slapmPolicyRuleStatsCountDenies.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slapmPolicyRuleStatsCountDenies.setStatus("current")
_SlapmPolicyRuleStatsInDiscards_Type = Counter32
_SlapmPolicyRuleStatsInDiscards_Object = MibTableColumn
slapmPolicyRuleStatsInDiscards = _SlapmPolicyRuleStatsInDiscards_Object(
    (1, 3, 6, 1, 3, 88, 1, 2, 5, 1, 11),
    _SlapmPolicyRuleStatsInDiscards_Type()
)
slapmPolicyRuleStatsInDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slapmPolicyRuleStatsInDiscards.setStatus("current")
_SlapmPolicyRuleStatsOutDiscards_Type = Counter32
_SlapmPolicyRuleStatsOutDiscards_Object = MibTableColumn
slapmPolicyRuleStatsOutDiscards = _SlapmPolicyRuleStatsOutDiscards_Object(
    (1, 3, 6, 1, 3, 88, 1, 2, 5, 1, 12),
    _SlapmPolicyRuleStatsOutDiscards_Type()
)
slapmPolicyRuleStatsOutDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slapmPolicyRuleStatsOutDiscards.setStatus("current")
_SlapmPolicyRuleStatsInPackets_Type = Counter32
_SlapmPolicyRuleStatsInPackets_Object = MibTableColumn
slapmPolicyRuleStatsInPackets = _SlapmPolicyRuleStatsInPackets_Object(
    (1, 3, 6, 1, 3, 88, 1, 2, 5, 1, 13),
    _SlapmPolicyRuleStatsInPackets_Type()
)
slapmPolicyRuleStatsInPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slapmPolicyRuleStatsInPackets.setStatus("current")
_SlapmPolicyRuleStatsOutPackets_Type = Counter32
_SlapmPolicyRuleStatsOutPackets_Object = MibTableColumn
slapmPolicyRuleStatsOutPackets = _SlapmPolicyRuleStatsOutPackets_Object(
    (1, 3, 6, 1, 3, 88, 1, 2, 5, 1, 14),
    _SlapmPolicyRuleStatsOutPackets_Type()
)
slapmPolicyRuleStatsOutPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slapmPolicyRuleStatsOutPackets.setStatus("current")
_SlapmPolicyRuleStatsInProOctets_Type = Counter32
_SlapmPolicyRuleStatsInProOctets_Object = MibTableColumn
slapmPolicyRuleStatsInProOctets = _SlapmPolicyRuleStatsInProOctets_Object(
    (1, 3, 6, 1, 3, 88, 1, 2, 5, 1, 15),
    _SlapmPolicyRuleStatsInProOctets_Type()
)
slapmPolicyRuleStatsInProOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slapmPolicyRuleStatsInProOctets.setStatus("current")
_SlapmPolicyRuleStatsOutProOctets_Type = Counter32
_SlapmPolicyRuleStatsOutProOctets_Object = MibTableColumn
slapmPolicyRuleStatsOutProOctets = _SlapmPolicyRuleStatsOutProOctets_Object(
    (1, 3, 6, 1, 3, 88, 1, 2, 5, 1, 16),
    _SlapmPolicyRuleStatsOutProOctets_Type()
)
slapmPolicyRuleStatsOutProOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slapmPolicyRuleStatsOutProOctets.setStatus("current")
_SlapmPolicyRuleStatsMinRate_Type = Unsigned32
_SlapmPolicyRuleStatsMinRate_Object = MibTableColumn
slapmPolicyRuleStatsMinRate = _SlapmPolicyRuleStatsMinRate_Object(
    (1, 3, 6, 1, 3, 88, 1, 2, 5, 1, 17),
    _SlapmPolicyRuleStatsMinRate_Type()
)
slapmPolicyRuleStatsMinRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slapmPolicyRuleStatsMinRate.setStatus("current")
if mibBuilder.loadTexts:
    slapmPolicyRuleStatsMinRate.setUnits("Kilobits per second")
_SlapmPolicyRuleStatsMaxRate_Type = Unsigned32
_SlapmPolicyRuleStatsMaxRate_Object = MibTableColumn
slapmPolicyRuleStatsMaxRate = _SlapmPolicyRuleStatsMaxRate_Object(
    (1, 3, 6, 1, 3, 88, 1, 2, 5, 1, 18),
    _SlapmPolicyRuleStatsMaxRate_Type()
)
slapmPolicyRuleStatsMaxRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slapmPolicyRuleStatsMaxRate.setStatus("current")
if mibBuilder.loadTexts:
    slapmPolicyRuleStatsMaxRate.setUnits("Kilobits per second")
_SlapmPolicyRuleStatsMaxDelay_Type = Unsigned32
_SlapmPolicyRuleStatsMaxDelay_Object = MibTableColumn
slapmPolicyRuleStatsMaxDelay = _SlapmPolicyRuleStatsMaxDelay_Object(
    (1, 3, 6, 1, 3, 88, 1, 2, 5, 1, 19),
    _SlapmPolicyRuleStatsMaxDelay_Type()
)
slapmPolicyRuleStatsMaxDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slapmPolicyRuleStatsMaxDelay.setStatus("current")
if mibBuilder.loadTexts:
    slapmPolicyRuleStatsMaxDelay.setUnits("milliseconds")
_SlapmPolicyRuleStatsTotalRsvpFlows_Type = Counter32
_SlapmPolicyRuleStatsTotalRsvpFlows_Object = MibTableColumn
slapmPolicyRuleStatsTotalRsvpFlows = _SlapmPolicyRuleStatsTotalRsvpFlows_Object(
    (1, 3, 6, 1, 3, 88, 1, 2, 5, 1, 20),
    _SlapmPolicyRuleStatsTotalRsvpFlows_Type()
)
slapmPolicyRuleStatsTotalRsvpFlows.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slapmPolicyRuleStatsTotalRsvpFlows.setStatus("current")
_SlapmPolicyRuleStatsActRsvpFlows_Type = Gauge32
_SlapmPolicyRuleStatsActRsvpFlows_Object = MibTableColumn
slapmPolicyRuleStatsActRsvpFlows = _SlapmPolicyRuleStatsActRsvpFlows_Object(
    (1, 3, 6, 1, 3, 88, 1, 2, 5, 1, 21),
    _SlapmPolicyRuleStatsActRsvpFlows_Type()
)
slapmPolicyRuleStatsActRsvpFlows.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slapmPolicyRuleStatsActRsvpFlows.setStatus("current")
_SlapmPRMonTable_Object = MibTable
slapmPRMonTable = _SlapmPRMonTable_Object(
    (1, 3, 6, 1, 3, 88, 1, 2, 6)
)
if mibBuilder.loadTexts:
    slapmPRMonTable.setStatus("current")
_SlapmPRMonEntry_Object = MibTableRow
slapmPRMonEntry = _SlapmPRMonEntry_Object(
    (1, 3, 6, 1, 3, 88, 1, 2, 6, 1)
)
slapmPRMonEntry.setIndexNames(
    (0, "SLAPM-MIB", "slapmPRMonOwnerIndex"),
    (0, "SLAPM-MIB", "slapmPRMonSystemAddress"),
    (0, "SLAPM-MIB", "slapmPRMonIndex"),
)
if mibBuilder.loadTexts:
    slapmPRMonEntry.setStatus("current")


class _SlapmPRMonOwnerIndex_Type(SnmpAdminString):
    """Custom type slapmPRMonOwnerIndex based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_SlapmPRMonOwnerIndex_Type.__name__ = "SnmpAdminString"
_SlapmPRMonOwnerIndex_Object = MibTableColumn
slapmPRMonOwnerIndex = _SlapmPRMonOwnerIndex_Object(
    (1, 3, 6, 1, 3, 88, 1, 2, 6, 1, 1),
    _SlapmPRMonOwnerIndex_Type()
)
slapmPRMonOwnerIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    slapmPRMonOwnerIndex.setStatus("current")


class _SlapmPRMonSystemAddress_Type(OctetString):
    """Custom type slapmPRMonSystemAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_SlapmPRMonSystemAddress_Type.__name__ = "OctetString"
_SlapmPRMonSystemAddress_Object = MibTableColumn
slapmPRMonSystemAddress = _SlapmPRMonSystemAddress_Object(
    (1, 3, 6, 1, 3, 88, 1, 2, 6, 1, 2),
    _SlapmPRMonSystemAddress_Type()
)
slapmPRMonSystemAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    slapmPRMonSystemAddress.setStatus("current")
_SlapmPRMonIndex_Type = Unsigned32
_SlapmPRMonIndex_Object = MibTableColumn
slapmPRMonIndex = _SlapmPRMonIndex_Object(
    (1, 3, 6, 1, 3, 88, 1, 2, 6, 1, 3),
    _SlapmPRMonIndex_Type()
)
slapmPRMonIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    slapmPRMonIndex.setStatus("current")


class _SlapmPRMonControl_Type(Bits):
    """Custom type slapmPRMonControl based on Bits"""
    defaultBinValue = "111"

    namedValues = NamedValues(
        *(("enableAggregateTraps", 3),
          ("enableSubcomponentTraps", 4),
          ("monitorMaxDelay", 2),
          ("monitorMaxRate", 1),
          ("monitorMinRate", 0),
          ("monitorSubcomponents", 5))
    )

_SlapmPRMonControl_Type.__name__ = "Bits"
_SlapmPRMonControl_Object = MibTableColumn
slapmPRMonControl = _SlapmPRMonControl_Object(
    (1, 3, 6, 1, 3, 88, 1, 2, 6, 1, 4),
    _SlapmPRMonControl_Type()
)
slapmPRMonControl.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    slapmPRMonControl.setStatus("current")
_SlapmPRMonStatus_Type = SlapmStatus
_SlapmPRMonStatus_Object = MibTableColumn
slapmPRMonStatus = _SlapmPRMonStatus_Object(
    (1, 3, 6, 1, 3, 88, 1, 2, 6, 1, 5),
    _SlapmPRMonStatus_Type()
)
slapmPRMonStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slapmPRMonStatus.setStatus("current")


class _SlapmPRMonInterval_Type(Unsigned32):
    """Custom type slapmPRMonInterval based on Unsigned32"""
    defaultValue = 20

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(15, 86400),
    )


_SlapmPRMonInterval_Type.__name__ = "Unsigned32"
_SlapmPRMonInterval_Object = MibTableColumn
slapmPRMonInterval = _SlapmPRMonInterval_Object(
    (1, 3, 6, 1, 3, 88, 1, 2, 6, 1, 6),
    _SlapmPRMonInterval_Type()
)
slapmPRMonInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    slapmPRMonInterval.setStatus("current")
if mibBuilder.loadTexts:
    slapmPRMonInterval.setUnits("seconds")


class _SlapmPRMonIntTime_Type(DateAndTime):
    """Custom type slapmPRMonIntTime based on DateAndTime"""
    defaultHexValue = "0000000000000000"


_SlapmPRMonIntTime_Object = MibTableColumn
slapmPRMonIntTime = _SlapmPRMonIntTime_Object(
    (1, 3, 6, 1, 3, 88, 1, 2, 6, 1, 7),
    _SlapmPRMonIntTime_Type()
)
slapmPRMonIntTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slapmPRMonIntTime.setStatus("current")
_SlapmPRMonCurrentInRate_Type = Gauge32
_SlapmPRMonCurrentInRate_Object = MibTableColumn
slapmPRMonCurrentInRate = _SlapmPRMonCurrentInRate_Object(
    (1, 3, 6, 1, 3, 88, 1, 2, 6, 1, 8),
    _SlapmPRMonCurrentInRate_Type()
)
slapmPRMonCurrentInRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slapmPRMonCurrentInRate.setStatus("current")
if mibBuilder.loadTexts:
    slapmPRMonCurrentInRate.setUnits("kilobits per second")
_SlapmPRMonCurrentOutRate_Type = Gauge32
_SlapmPRMonCurrentOutRate_Object = MibTableColumn
slapmPRMonCurrentOutRate = _SlapmPRMonCurrentOutRate_Object(
    (1, 3, 6, 1, 3, 88, 1, 2, 6, 1, 9),
    _SlapmPRMonCurrentOutRate_Type()
)
slapmPRMonCurrentOutRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slapmPRMonCurrentOutRate.setStatus("current")
if mibBuilder.loadTexts:
    slapmPRMonCurrentOutRate.setUnits("kilobits per second")
_SlapmPRMonMinRateLow_Type = Unsigned32
_SlapmPRMonMinRateLow_Object = MibTableColumn
slapmPRMonMinRateLow = _SlapmPRMonMinRateLow_Object(
    (1, 3, 6, 1, 3, 88, 1, 2, 6, 1, 10),
    _SlapmPRMonMinRateLow_Type()
)
slapmPRMonMinRateLow.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    slapmPRMonMinRateLow.setStatus("current")
if mibBuilder.loadTexts:
    slapmPRMonMinRateLow.setUnits("kilobits per second")
_SlapmPRMonMinRateHigh_Type = Unsigned32
_SlapmPRMonMinRateHigh_Object = MibTableColumn
slapmPRMonMinRateHigh = _SlapmPRMonMinRateHigh_Object(
    (1, 3, 6, 1, 3, 88, 1, 2, 6, 1, 11),
    _SlapmPRMonMinRateHigh_Type()
)
slapmPRMonMinRateHigh.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    slapmPRMonMinRateHigh.setStatus("current")
if mibBuilder.loadTexts:
    slapmPRMonMinRateHigh.setUnits("kilobits per second")
_SlapmPRMonMaxRateHigh_Type = Unsigned32
_SlapmPRMonMaxRateHigh_Object = MibTableColumn
slapmPRMonMaxRateHigh = _SlapmPRMonMaxRateHigh_Object(
    (1, 3, 6, 1, 3, 88, 1, 2, 6, 1, 12),
    _SlapmPRMonMaxRateHigh_Type()
)
slapmPRMonMaxRateHigh.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    slapmPRMonMaxRateHigh.setStatus("current")
if mibBuilder.loadTexts:
    slapmPRMonMaxRateHigh.setUnits("kilobits per second")
_SlapmPRMonMaxRateLow_Type = Unsigned32
_SlapmPRMonMaxRateLow_Object = MibTableColumn
slapmPRMonMaxRateLow = _SlapmPRMonMaxRateLow_Object(
    (1, 3, 6, 1, 3, 88, 1, 2, 6, 1, 13),
    _SlapmPRMonMaxRateLow_Type()
)
slapmPRMonMaxRateLow.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    slapmPRMonMaxRateLow.setStatus("current")
if mibBuilder.loadTexts:
    slapmPRMonMaxRateLow.setUnits("kilobits per second")
_SlapmPRMonMaxDelayHigh_Type = Unsigned32
_SlapmPRMonMaxDelayHigh_Object = MibTableColumn
slapmPRMonMaxDelayHigh = _SlapmPRMonMaxDelayHigh_Object(
    (1, 3, 6, 1, 3, 88, 1, 2, 6, 1, 14),
    _SlapmPRMonMaxDelayHigh_Type()
)
slapmPRMonMaxDelayHigh.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    slapmPRMonMaxDelayHigh.setStatus("current")
if mibBuilder.loadTexts:
    slapmPRMonMaxDelayHigh.setUnits("milliseconds")
_SlapmPRMonMaxDelayLow_Type = Unsigned32
_SlapmPRMonMaxDelayLow_Object = MibTableColumn
slapmPRMonMaxDelayLow = _SlapmPRMonMaxDelayLow_Object(
    (1, 3, 6, 1, 3, 88, 1, 2, 6, 1, 15),
    _SlapmPRMonMaxDelayLow_Type()
)
slapmPRMonMaxDelayLow.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    slapmPRMonMaxDelayLow.setStatus("current")
if mibBuilder.loadTexts:
    slapmPRMonMaxDelayLow.setUnits("milliseconds")
_SlapmPRMonMinInRateNotAchieves_Type = Counter32
_SlapmPRMonMinInRateNotAchieves_Object = MibTableColumn
slapmPRMonMinInRateNotAchieves = _SlapmPRMonMinInRateNotAchieves_Object(
    (1, 3, 6, 1, 3, 88, 1, 2, 6, 1, 16),
    _SlapmPRMonMinInRateNotAchieves_Type()
)
slapmPRMonMinInRateNotAchieves.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slapmPRMonMinInRateNotAchieves.setStatus("current")
_SlapmPRMonMaxInRateExceeds_Type = Counter32
_SlapmPRMonMaxInRateExceeds_Object = MibTableColumn
slapmPRMonMaxInRateExceeds = _SlapmPRMonMaxInRateExceeds_Object(
    (1, 3, 6, 1, 3, 88, 1, 2, 6, 1, 17),
    _SlapmPRMonMaxInRateExceeds_Type()
)
slapmPRMonMaxInRateExceeds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slapmPRMonMaxInRateExceeds.setStatus("current")
_SlapmPRMonMaxDelayExceeds_Type = Counter32
_SlapmPRMonMaxDelayExceeds_Object = MibTableColumn
slapmPRMonMaxDelayExceeds = _SlapmPRMonMaxDelayExceeds_Object(
    (1, 3, 6, 1, 3, 88, 1, 2, 6, 1, 18),
    _SlapmPRMonMaxDelayExceeds_Type()
)
slapmPRMonMaxDelayExceeds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slapmPRMonMaxDelayExceeds.setStatus("current")
_SlapmPRMonMinOutRateNotAchieves_Type = Counter32
_SlapmPRMonMinOutRateNotAchieves_Object = MibTableColumn
slapmPRMonMinOutRateNotAchieves = _SlapmPRMonMinOutRateNotAchieves_Object(
    (1, 3, 6, 1, 3, 88, 1, 2, 6, 1, 19),
    _SlapmPRMonMinOutRateNotAchieves_Type()
)
slapmPRMonMinOutRateNotAchieves.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slapmPRMonMinOutRateNotAchieves.setStatus("current")
_SlapmPRMonMaxOutRateExceeds_Type = Counter32
_SlapmPRMonMaxOutRateExceeds_Object = MibTableColumn
slapmPRMonMaxOutRateExceeds = _SlapmPRMonMaxOutRateExceeds_Object(
    (1, 3, 6, 1, 3, 88, 1, 2, 6, 1, 20),
    _SlapmPRMonMaxOutRateExceeds_Type()
)
slapmPRMonMaxOutRateExceeds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slapmPRMonMaxOutRateExceeds.setStatus("current")
_SlapmPRMonCurrentDelayRate_Type = Gauge32
_SlapmPRMonCurrentDelayRate_Object = MibTableColumn
slapmPRMonCurrentDelayRate = _SlapmPRMonCurrentDelayRate_Object(
    (1, 3, 6, 1, 3, 88, 1, 2, 6, 1, 21),
    _SlapmPRMonCurrentDelayRate_Type()
)
slapmPRMonCurrentDelayRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slapmPRMonCurrentDelayRate.setStatus("current")
if mibBuilder.loadTexts:
    slapmPRMonCurrentDelayRate.setUnits("milliseconds")
_SlapmPRMonRowStatus_Type = RowStatus
_SlapmPRMonRowStatus_Object = MibTableColumn
slapmPRMonRowStatus = _SlapmPRMonRowStatus_Object(
    (1, 3, 6, 1, 3, 88, 1, 2, 6, 1, 22),
    _SlapmPRMonRowStatus_Type()
)
slapmPRMonRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    slapmPRMonRowStatus.setStatus("current")
_SlapmConformance_ObjectIdentity = ObjectIdentity
slapmConformance = _SlapmConformance_ObjectIdentity(
    (1, 3, 6, 1, 3, 88, 2)
)
_SlapmCompliances_ObjectIdentity = ObjectIdentity
slapmCompliances = _SlapmCompliances_ObjectIdentity(
    (1, 3, 6, 1, 3, 88, 2, 1)
)
_SlapmGroups_ObjectIdentity = ObjectIdentity
slapmGroups = _SlapmGroups_ObjectIdentity(
    (1, 3, 6, 1, 3, 88, 2, 2)
)

# Managed Objects groups

slapmBaseGroup = ObjectGroup(
    (1, 3, 6, 1, 3, 88, 2, 2, 1)
)
slapmBaseGroup.setObjects(
      *(("SLAPM-MIB", "slapmSpinLock"),
        ("SLAPM-MIB", "slapmPolicyCountQueries"),
        ("SLAPM-MIB", "slapmPolicyCountAccesses"),
        ("SLAPM-MIB", "slapmPolicyCountSuccessAccesses"),
        ("SLAPM-MIB", "slapmPolicyCountNotFounds"),
        ("SLAPM-MIB", "slapmPolicyPurgeTime"),
        ("SLAPM-MIB", "slapmPolicyTrapEnable"),
        ("SLAPM-MIB", "slapmPolicyStatsOperStatus"),
        ("SLAPM-MIB", "slapmPolicyStatsActiveConns"),
        ("SLAPM-MIB", "slapmPolicyStatsFirstActivated"),
        ("SLAPM-MIB", "slapmPolicyStatsLastMapping"),
        ("SLAPM-MIB", "slapmPolicyStatsInOctets"),
        ("SLAPM-MIB", "slapmPolicyStatsOutOctets"),
        ("SLAPM-MIB", "slapmPolicyStatsConnectionLimit"),
        ("SLAPM-MIB", "slapmPolicyStatsTotalConns"),
        ("SLAPM-MIB", "slapmPolicyStatsCountAccepts"),
        ("SLAPM-MIB", "slapmPolicyStatsCountDenies"),
        ("SLAPM-MIB", "slapmPolicyStatsInDiscards"),
        ("SLAPM-MIB", "slapmPolicyStatsOutDiscards"),
        ("SLAPM-MIB", "slapmPolicyStatsInPackets"),
        ("SLAPM-MIB", "slapmPolicyStatsOutPackets"),
        ("SLAPM-MIB", "slapmPolicyStatsMinRate"),
        ("SLAPM-MIB", "slapmPolicyStatsMaxRate"),
        ("SLAPM-MIB", "slapmPolicyStatsMaxDelay"),
        ("SLAPM-MIB", "slapmPolicyMonitorControl"),
        ("SLAPM-MIB", "slapmPolicyMonitorStatus"),
        ("SLAPM-MIB", "slapmPolicyMonitorInterval"),
        ("SLAPM-MIB", "slapmPolicyMonitorIntTime"),
        ("SLAPM-MIB", "slapmPolicyMonitorCurrentInRate"),
        ("SLAPM-MIB", "slapmPolicyMonitorCurrentOutRate"),
        ("SLAPM-MIB", "slapmPolicyMonitorMinRateLow"),
        ("SLAPM-MIB", "slapmPolicyMonitorMinRateHigh"),
        ("SLAPM-MIB", "slapmPolicyMonitorMaxRateHigh"),
        ("SLAPM-MIB", "slapmPolicyMonitorMaxRateLow"),
        ("SLAPM-MIB", "slapmPolicyMonitorMaxDelayHigh"),
        ("SLAPM-MIB", "slapmPolicyMonitorMaxDelayLow"),
        ("SLAPM-MIB", "slapmPolicyMonitorMinInRateNotAchieves"),
        ("SLAPM-MIB", "slapmPolicyMonitorMaxInRateExceeds"),
        ("SLAPM-MIB", "slapmPolicyMonitorMaxDelayExceeds"),
        ("SLAPM-MIB", "slapmPolicyMonitorMinOutRateNotAchieves"),
        ("SLAPM-MIB", "slapmPolicyMonitorMaxOutRateExceeds"),
        ("SLAPM-MIB", "slapmPolicyMonitorCurrentDelayRate"),
        ("SLAPM-MIB", "slapmPolicyMonitorRowStatus"))
)
if mibBuilder.loadTexts:
    slapmBaseGroup.setStatus("deprecated")

slapmOptionalGroup = ObjectGroup(
    (1, 3, 6, 1, 3, 88, 2, 2, 2)
)
slapmOptionalGroup.setObjects(
      *(("SLAPM-MIB", "slapmPolicyStatsInProfileOctets"),
        ("SLAPM-MIB", "slapmPolicyStatsOutProfileOctets"))
)
if mibBuilder.loadTexts:
    slapmOptionalGroup.setStatus("deprecated")

slapmEndSystemGroup = ObjectGroup(
    (1, 3, 6, 1, 3, 88, 2, 2, 3)
)
slapmEndSystemGroup.setObjects(
      *(("SLAPM-MIB", "slapmPolicyTrapFilter"),
        ("SLAPM-MIB", "slapmSubcomponentProtocol"),
        ("SLAPM-MIB", "slapmSubcomponentSystemAddress"),
        ("SLAPM-MIB", "slapmSubcomponentPolicyName"),
        ("SLAPM-MIB", "slapmSubcomponentTrafficProfileName"),
        ("SLAPM-MIB", "slapmSubcomponentLastActivity"),
        ("SLAPM-MIB", "slapmSubcomponentInOctets"),
        ("SLAPM-MIB", "slapmSubcomponentOutOctets"),
        ("SLAPM-MIB", "slapmSubcomponentTcpOutBufferedOctets"),
        ("SLAPM-MIB", "slapmSubcomponentTcpInBufferedOctets"),
        ("SLAPM-MIB", "slapmSubcomponentTcpReXmts"),
        ("SLAPM-MIB", "slapmSubcomponentTcpRoundTripTime"),
        ("SLAPM-MIB", "slapmSubcomponentTcpRoundTripVariance"),
        ("SLAPM-MIB", "slapmSubcomponentInPdus"),
        ("SLAPM-MIB", "slapmSubcomponentOutPdus"),
        ("SLAPM-MIB", "slapmSubcomponentApplName"),
        ("SLAPM-MIB", "slapmSubcomponentMonitorStatus"),
        ("SLAPM-MIB", "slapmSubcomponentMonitorIntTime"),
        ("SLAPM-MIB", "slapmSubcomponentMonitorCurrentOutRate"),
        ("SLAPM-MIB", "slapmSubcomponentMonitorCurrentInRate"))
)
if mibBuilder.loadTexts:
    slapmEndSystemGroup.setStatus("deprecated")

slapmBaseGroup2 = ObjectGroup(
    (1, 3, 6, 1, 3, 88, 2, 2, 6)
)
slapmBaseGroup2.setObjects(
      *(("SLAPM-MIB", "slapmSpinLock"),
        ("SLAPM-MIB", "slapmPolicyCountQueries"),
        ("SLAPM-MIB", "slapmPolicyCountAccesses"),
        ("SLAPM-MIB", "slapmPolicyCountSuccessAccesses"),
        ("SLAPM-MIB", "slapmPolicyCountNotFounds"),
        ("SLAPM-MIB", "slapmPolicyPurgeTime"),
        ("SLAPM-MIB", "slapmPolicyTrapEnable"),
        ("SLAPM-MIB", "slapmPolicyNameOfRule"),
        ("SLAPM-MIB", "slapmPolicyRuleStatsOperStatus"),
        ("SLAPM-MIB", "slapmPolicyRuleStatsActiveConns"),
        ("SLAPM-MIB", "slapmPolicyRuleStatsTotalConns"),
        ("SLAPM-MIB", "slapmPolicyRuleStatsLActivated"),
        ("SLAPM-MIB", "slapmPolicyRuleStatsLastMapping"),
        ("SLAPM-MIB", "slapmPolicyRuleStatsInOctets"),
        ("SLAPM-MIB", "slapmPolicyRuleStatsOutOctets"),
        ("SLAPM-MIB", "slapmPolicyRuleStatsConnLimit"),
        ("SLAPM-MIB", "slapmPolicyRuleStatsCountAccepts"),
        ("SLAPM-MIB", "slapmPolicyRuleStatsCountDenies"),
        ("SLAPM-MIB", "slapmPolicyRuleStatsInDiscards"),
        ("SLAPM-MIB", "slapmPolicyRuleStatsOutDiscards"),
        ("SLAPM-MIB", "slapmPolicyRuleStatsInPackets"),
        ("SLAPM-MIB", "slapmPolicyRuleStatsOutPackets"),
        ("SLAPM-MIB", "slapmPolicyRuleStatsInProOctets"),
        ("SLAPM-MIB", "slapmPolicyRuleStatsOutProOctets"),
        ("SLAPM-MIB", "slapmPolicyRuleStatsMinRate"),
        ("SLAPM-MIB", "slapmPolicyRuleStatsMaxRate"),
        ("SLAPM-MIB", "slapmPolicyRuleStatsMaxDelay"),
        ("SLAPM-MIB", "slapmPolicyRuleStatsTotalRsvpFlows"),
        ("SLAPM-MIB", "slapmPolicyRuleStatsActRsvpFlows"),
        ("SLAPM-MIB", "slapmPRMonControl"),
        ("SLAPM-MIB", "slapmPRMonStatus"),
        ("SLAPM-MIB", "slapmPRMonInterval"),
        ("SLAPM-MIB", "slapmPRMonIntTime"),
        ("SLAPM-MIB", "slapmPRMonCurrentInRate"),
        ("SLAPM-MIB", "slapmPRMonCurrentOutRate"),
        ("SLAPM-MIB", "slapmPRMonMinRateLow"),
        ("SLAPM-MIB", "slapmPRMonMinRateHigh"),
        ("SLAPM-MIB", "slapmPRMonMaxRateHigh"),
        ("SLAPM-MIB", "slapmPRMonMaxRateLow"),
        ("SLAPM-MIB", "slapmPRMonMaxDelayHigh"),
        ("SLAPM-MIB", "slapmPRMonMaxDelayLow"),
        ("SLAPM-MIB", "slapmPRMonMinInRateNotAchieves"),
        ("SLAPM-MIB", "slapmPRMonMaxInRateExceeds"),
        ("SLAPM-MIB", "slapmPRMonMaxDelayExceeds"),
        ("SLAPM-MIB", "slapmPRMonMinOutRateNotAchieves"),
        ("SLAPM-MIB", "slapmPRMonMaxOutRateExceeds"),
        ("SLAPM-MIB", "slapmPRMonCurrentDelayRate"),
        ("SLAPM-MIB", "slapmPRMonRowStatus"))
)
if mibBuilder.loadTexts:
    slapmBaseGroup2.setStatus("current")

slapmEndSystemGroup2 = ObjectGroup(
    (1, 3, 6, 1, 3, 88, 2, 2, 7)
)
slapmEndSystemGroup2.setObjects(
      *(("SLAPM-MIB", "slapmPolicyTrapFilter"),
        ("SLAPM-MIB", "slapmSubcomponentProtocol"),
        ("SLAPM-MIB", "slapmSubcomponentSystemAddress"),
        ("SLAPM-MIB", "slapmSubcomponentLastActivity"),
        ("SLAPM-MIB", "slapmSubcomponentInOctets"),
        ("SLAPM-MIB", "slapmSubcomponentOutOctets"),
        ("SLAPM-MIB", "slapmSubcomponentTcpOutBufferedOctets"),
        ("SLAPM-MIB", "slapmSubcomponentTcpInBufferedOctets"),
        ("SLAPM-MIB", "slapmSubcomponentTcpReXmts"),
        ("SLAPM-MIB", "slapmSubcomponentTcpRoundTripTime"),
        ("SLAPM-MIB", "slapmSubcomponentTcpRoundTripVariance"),
        ("SLAPM-MIB", "slapmSubcomponentInPdus"),
        ("SLAPM-MIB", "slapmSubcomponentOutPdus"),
        ("SLAPM-MIB", "slapmSubcomponentApplName"),
        ("SLAPM-MIB", "slapmSubcomponentMonitorStatus"),
        ("SLAPM-MIB", "slapmSubcomponentMonitorIntTime"),
        ("SLAPM-MIB", "slapmSubcomponentMonitorCurrentOutRate"),
        ("SLAPM-MIB", "slapmSubcomponentMonitorCurrentInRate"),
        ("SLAPM-MIB", "slapmSubcomponentPolicyRuleIndex"))
)
if mibBuilder.loadTexts:
    slapmEndSystemGroup2.setStatus("current")


# Notification objects

slapmMonitoredEventNotAchieved = NotificationType(
    (1, 3, 6, 1, 3, 88, 0, 1)
)
slapmMonitoredEventNotAchieved.setObjects(
      *(("SLAPM-MIB", "slapmPolicyMonitorIntTime"),
        ("SLAPM-MIB", "slapmPolicyMonitorControl"),
        ("SLAPM-MIB", "slapmPolicyMonitorStatus"),
        ("SLAPM-MIB", "slapmPolicyMonitorStatus"),
        ("SLAPM-MIB", "slapmPolicyMonitorCurrentInRate"),
        ("SLAPM-MIB", "slapmPolicyMonitorCurrentOutRate"),
        ("SLAPM-MIB", "slapmPolicyMonitorCurrentDelayRate"))
)
if mibBuilder.loadTexts:
    slapmMonitoredEventNotAchieved.setStatus(
        "deprecated"
    )

slapmMonitoredEventOkay = NotificationType(
    (1, 3, 6, 1, 3, 88, 0, 2)
)
slapmMonitoredEventOkay.setObjects(
      *(("SLAPM-MIB", "slapmPolicyMonitorIntTime"),
        ("SLAPM-MIB", "slapmPolicyMonitorControl"),
        ("SLAPM-MIB", "slapmPolicyMonitorStatus"),
        ("SLAPM-MIB", "slapmPolicyMonitorStatus"),
        ("SLAPM-MIB", "slapmPolicyMonitorCurrentInRate"),
        ("SLAPM-MIB", "slapmPolicyMonitorCurrentOutRate"),
        ("SLAPM-MIB", "slapmPolicyMonitorCurrentDelayRate"))
)
if mibBuilder.loadTexts:
    slapmMonitoredEventOkay.setStatus(
        "deprecated"
    )

slapmPolicyProfileDeleted = NotificationType(
    (1, 3, 6, 1, 3, 88, 0, 3)
)
slapmPolicyProfileDeleted.setObjects(
      *(("SLAPM-MIB", "slapmPolicyStatsActiveConns"),
        ("SLAPM-MIB", "slapmPolicyStatsTotalConns"),
        ("SLAPM-MIB", "slapmPolicyStatsFirstActivated"),
        ("SLAPM-MIB", "slapmPolicyStatsLastMapping"),
        ("SLAPM-MIB", "slapmPolicyStatsInOctets"),
        ("SLAPM-MIB", "slapmPolicyStatsOutOctets"),
        ("SLAPM-MIB", "slapmPolicyStatsConnectionLimit"),
        ("SLAPM-MIB", "slapmPolicyStatsCountAccepts"),
        ("SLAPM-MIB", "slapmPolicyStatsCountDenies"),
        ("SLAPM-MIB", "slapmPolicyStatsInDiscards"),
        ("SLAPM-MIB", "slapmPolicyStatsOutDiscards"),
        ("SLAPM-MIB", "slapmPolicyStatsInPackets"),
        ("SLAPM-MIB", "slapmPolicyStatsOutPackets"),
        ("SLAPM-MIB", "slapmPolicyStatsInProfileOctets"),
        ("SLAPM-MIB", "slapmPolicyStatsOutProfileOctets"),
        ("SLAPM-MIB", "slapmPolicyStatsMinRate"),
        ("SLAPM-MIB", "slapmPolicyStatsMaxRate"),
        ("SLAPM-MIB", "slapmPolicyStatsMaxDelay"))
)
if mibBuilder.loadTexts:
    slapmPolicyProfileDeleted.setStatus(
        "deprecated"
    )

slapmPolicyMonitorDeleted = NotificationType(
    (1, 3, 6, 1, 3, 88, 0, 4)
)
slapmPolicyMonitorDeleted.setObjects(
      *(("SLAPM-MIB", "slapmPolicyMonitorStatus"),
        ("SLAPM-MIB", "slapmPolicyMonitorInterval"),
        ("SLAPM-MIB", "slapmPolicyMonitorIntTime"),
        ("SLAPM-MIB", "slapmPolicyMonitorCurrentInRate"),
        ("SLAPM-MIB", "slapmPolicyMonitorCurrentOutRate"),
        ("SLAPM-MIB", "slapmPolicyMonitorCurrentDelayRate"),
        ("SLAPM-MIB", "slapmPolicyMonitorMinRateLow"),
        ("SLAPM-MIB", "slapmPolicyMonitorMinRateHigh"),
        ("SLAPM-MIB", "slapmPolicyMonitorMaxRateHigh"),
        ("SLAPM-MIB", "slapmPolicyMonitorMaxRateLow"),
        ("SLAPM-MIB", "slapmPolicyMonitorMaxDelayHigh"),
        ("SLAPM-MIB", "slapmPolicyMonitorMaxDelayLow"),
        ("SLAPM-MIB", "slapmPolicyMonitorMinInRateNotAchieves"),
        ("SLAPM-MIB", "slapmPolicyMonitorMaxInRateExceeds"),
        ("SLAPM-MIB", "slapmPolicyMonitorMaxDelayExceeds"),
        ("SLAPM-MIB", "slapmPolicyMonitorMinOutRateNotAchieves"),
        ("SLAPM-MIB", "slapmPolicyMonitorMaxOutRateExceeds"))
)
if mibBuilder.loadTexts:
    slapmPolicyMonitorDeleted.setStatus(
        "deprecated"
    )

slapmSubcomponentMonitoredEventNotAchieved = NotificationType(
    (1, 3, 6, 1, 3, 88, 0, 5)
)
slapmSubcomponentMonitoredEventNotAchieved.setObjects(
      *(("SLAPM-MIB", "slapmSubcomponentSystemAddress"),
        ("SLAPM-MIB", "slapmSubcomponentPolicyName"),
        ("SLAPM-MIB", "slapmSubcomponentTrafficProfileName"),
        ("SLAPM-MIB", "slapmSubcomponentMonitorStatus"),
        ("SLAPM-MIB", "slapmSubcomponentMonitorStatus"),
        ("SLAPM-MIB", "slapmSubcomponentMonitorIntTime"),
        ("SLAPM-MIB", "slapmSubcomponentMonitorCurrentInRate"),
        ("SLAPM-MIB", "slapmSubcomponentMonitorCurrentOutRate"),
        ("SLAPM-MIB", "slapmSubcomponentTcpRoundTripTime"))
)
if mibBuilder.loadTexts:
    slapmSubcomponentMonitoredEventNotAchieved.setStatus(
        "deprecated"
    )

slapmSubcomponentMonitoredEventOkay = NotificationType(
    (1, 3, 6, 1, 3, 88, 0, 6)
)
slapmSubcomponentMonitoredEventOkay.setObjects(
      *(("SLAPM-MIB", "slapmSubcomponentSystemAddress"),
        ("SLAPM-MIB", "slapmSubcomponentPolicyName"),
        ("SLAPM-MIB", "slapmSubcomponentTrafficProfileName"),
        ("SLAPM-MIB", "slapmSubcomponentMonitorStatus"),
        ("SLAPM-MIB", "slapmSubcomponentMonitorStatus"),
        ("SLAPM-MIB", "slapmSubcomponentMonitorIntTime"),
        ("SLAPM-MIB", "slapmSubcomponentMonitorCurrentInRate"),
        ("SLAPM-MIB", "slapmSubcomponentMonitorCurrentOutRate"),
        ("SLAPM-MIB", "slapmSubcomponentTcpRoundTripTime"))
)
if mibBuilder.loadTexts:
    slapmSubcomponentMonitoredEventOkay.setStatus(
        "deprecated"
    )

slapmPolicyRuleMonNotOkay = NotificationType(
    (1, 3, 6, 1, 3, 88, 0, 7)
)
slapmPolicyRuleMonNotOkay.setObjects(
      *(("SLAPM-MIB", "slapmPRMonIntTime"),
        ("SLAPM-MIB", "slapmPRMonControl"),
        ("SLAPM-MIB", "slapmPRMonStatus"),
        ("SLAPM-MIB", "slapmPRMonStatus"),
        ("SLAPM-MIB", "slapmPRMonCurrentInRate"),
        ("SLAPM-MIB", "slapmPRMonCurrentOutRate"),
        ("SLAPM-MIB", "slapmPRMonCurrentDelayRate"))
)
if mibBuilder.loadTexts:
    slapmPolicyRuleMonNotOkay.setStatus(
        "current"
    )

slapmPolicyRuleMonOkay = NotificationType(
    (1, 3, 6, 1, 3, 88, 0, 8)
)
slapmPolicyRuleMonOkay.setObjects(
      *(("SLAPM-MIB", "slapmPRMonIntTime"),
        ("SLAPM-MIB", "slapmPRMonControl"),
        ("SLAPM-MIB", "slapmPRMonStatus"),
        ("SLAPM-MIB", "slapmPRMonStatus"),
        ("SLAPM-MIB", "slapmPRMonCurrentInRate"),
        ("SLAPM-MIB", "slapmPRMonCurrentOutRate"),
        ("SLAPM-MIB", "slapmPRMonCurrentDelayRate"))
)
if mibBuilder.loadTexts:
    slapmPolicyRuleMonOkay.setStatus(
        "current"
    )

slapmPolicyRuleDeleted = NotificationType(
    (1, 3, 6, 1, 3, 88, 0, 9)
)
slapmPolicyRuleDeleted.setObjects(
      *(("SLAPM-MIB", "slapmPolicyRuleStatsActiveConns"),
        ("SLAPM-MIB", "slapmPolicyRuleStatsTotalConns"),
        ("SLAPM-MIB", "slapmPolicyRuleStatsLActivated"),
        ("SLAPM-MIB", "slapmPolicyRuleStatsLastMapping"),
        ("SLAPM-MIB", "slapmPolicyRuleStatsInOctets"),
        ("SLAPM-MIB", "slapmPolicyRuleStatsOutOctets"),
        ("SLAPM-MIB", "slapmPolicyRuleStatsConnLimit"),
        ("SLAPM-MIB", "slapmPolicyRuleStatsCountAccepts"),
        ("SLAPM-MIB", "slapmPolicyRuleStatsCountDenies"),
        ("SLAPM-MIB", "slapmPolicyRuleStatsInDiscards"),
        ("SLAPM-MIB", "slapmPolicyRuleStatsOutDiscards"),
        ("SLAPM-MIB", "slapmPolicyRuleStatsInPackets"),
        ("SLAPM-MIB", "slapmPolicyRuleStatsOutPackets"),
        ("SLAPM-MIB", "slapmPolicyRuleStatsInProOctets"),
        ("SLAPM-MIB", "slapmPolicyRuleStatsOutProOctets"),
        ("SLAPM-MIB", "slapmPolicyRuleStatsMinRate"),
        ("SLAPM-MIB", "slapmPolicyRuleStatsMaxRate"),
        ("SLAPM-MIB", "slapmPolicyRuleStatsMaxDelay"),
        ("SLAPM-MIB", "slapmPolicyRuleStatsTotalRsvpFlows"),
        ("SLAPM-MIB", "slapmPolicyRuleStatsActRsvpFlows"))
)
if mibBuilder.loadTexts:
    slapmPolicyRuleDeleted.setStatus(
        "current"
    )

slapmPolicyRuleMonDeleted = NotificationType(
    (1, 3, 6, 1, 3, 88, 0, 10)
)
slapmPolicyRuleMonDeleted.setObjects(
      *(("SLAPM-MIB", "slapmPRMonControl"),
        ("SLAPM-MIB", "slapmPRMonStatus"),
        ("SLAPM-MIB", "slapmPRMonInterval"),
        ("SLAPM-MIB", "slapmPRMonIntTime"),
        ("SLAPM-MIB", "slapmPRMonCurrentInRate"),
        ("SLAPM-MIB", "slapmPRMonCurrentOutRate"),
        ("SLAPM-MIB", "slapmPRMonCurrentDelayRate"),
        ("SLAPM-MIB", "slapmPRMonMinRateLow"),
        ("SLAPM-MIB", "slapmPRMonMinRateHigh"),
        ("SLAPM-MIB", "slapmPRMonMaxRateHigh"),
        ("SLAPM-MIB", "slapmPRMonMaxRateLow"),
        ("SLAPM-MIB", "slapmPRMonMaxDelayHigh"),
        ("SLAPM-MIB", "slapmPRMonMaxDelayLow"),
        ("SLAPM-MIB", "slapmPRMonMinInRateNotAchieves"),
        ("SLAPM-MIB", "slapmPRMonMaxInRateExceeds"),
        ("SLAPM-MIB", "slapmPRMonMaxDelayExceeds"),
        ("SLAPM-MIB", "slapmPRMonMinOutRateNotAchieves"),
        ("SLAPM-MIB", "slapmPRMonMaxOutRateExceeds"))
)
if mibBuilder.loadTexts:
    slapmPolicyRuleMonDeleted.setStatus(
        "current"
    )

slapmSubcMonitorNotOkay = NotificationType(
    (1, 3, 6, 1, 3, 88, 0, 11)
)
slapmSubcMonitorNotOkay.setObjects(
      *(("SLAPM-MIB", "slapmSubcomponentSystemAddress"),
        ("SLAPM-MIB", "slapmSubcomponentPolicyRuleIndex"),
        ("SLAPM-MIB", "slapmPRMonControl"),
        ("SLAPM-MIB", "slapmSubcomponentMonitorStatus"),
        ("SLAPM-MIB", "slapmSubcomponentMonitorStatus"),
        ("SLAPM-MIB", "slapmSubcomponentMonitorIntTime"),
        ("SLAPM-MIB", "slapmSubcomponentMonitorCurrentInRate"),
        ("SLAPM-MIB", "slapmSubcomponentMonitorCurrentOutRate"),
        ("SLAPM-MIB", "slapmSubcomponentTcpRoundTripTime"))
)
if mibBuilder.loadTexts:
    slapmSubcMonitorNotOkay.setStatus(
        "current"
    )

slapmSubcMonitorOkay = NotificationType(
    (1, 3, 6, 1, 3, 88, 0, 12)
)
slapmSubcMonitorOkay.setObjects(
      *(("SLAPM-MIB", "slapmSubcomponentSystemAddress"),
        ("SLAPM-MIB", "slapmSubcomponentPolicyRuleIndex"),
        ("SLAPM-MIB", "slapmPRMonControl"),
        ("SLAPM-MIB", "slapmSubcomponentMonitorStatus"),
        ("SLAPM-MIB", "slapmSubcomponentMonitorStatus"),
        ("SLAPM-MIB", "slapmSubcomponentMonitorIntTime"),
        ("SLAPM-MIB", "slapmSubcomponentMonitorCurrentInRate"),
        ("SLAPM-MIB", "slapmSubcomponentMonitorCurrentOutRate"),
        ("SLAPM-MIB", "slapmSubcomponentTcpRoundTripTime"))
)
if mibBuilder.loadTexts:
    slapmSubcMonitorOkay.setStatus(
        "current"
    )


# Notifications groups

slapmNotGroup = NotificationGroup(
    (1, 3, 6, 1, 3, 88, 2, 2, 4)
)
slapmNotGroup.setObjects(
      *(("SLAPM-MIB", "slapmMonitoredEventNotAchieved"),
        ("SLAPM-MIB", "slapmMonitoredEventOkay"),
        ("SLAPM-MIB", "slapmPolicyProfileDeleted"),
        ("SLAPM-MIB", "slapmPolicyMonitorDeleted"))
)
if mibBuilder.loadTexts:
    slapmNotGroup.setStatus(
        "deprecated"
    )

slapmEndSystemNotGroup = NotificationGroup(
    (1, 3, 6, 1, 3, 88, 2, 2, 5)
)
slapmEndSystemNotGroup.setObjects(
      *(("SLAPM-MIB", "slapmSubcomponentMonitoredEventNotAchieved"),
        ("SLAPM-MIB", "slapmSubcomponentMonitoredEventOkay"))
)
if mibBuilder.loadTexts:
    slapmEndSystemNotGroup.setStatus(
        "deprecated"
    )

slapmNotGroup2 = NotificationGroup(
    (1, 3, 6, 1, 3, 88, 2, 2, 8)
)
slapmNotGroup2.setObjects(
      *(("SLAPM-MIB", "slapmPolicyRuleMonNotOkay"),
        ("SLAPM-MIB", "slapmPolicyRuleMonOkay"),
        ("SLAPM-MIB", "slapmPolicyRuleDeleted"),
        ("SLAPM-MIB", "slapmPolicyRuleMonDeleted"))
)
if mibBuilder.loadTexts:
    slapmNotGroup2.setStatus(
        "current"
    )

slapmEndSystemNotGroup2 = NotificationGroup(
    (1, 3, 6, 1, 3, 88, 2, 2, 9)
)
slapmEndSystemNotGroup2.setObjects(
      *(("SLAPM-MIB", "slapmSubcMonitorNotOkay"),
        ("SLAPM-MIB", "slapmSubcMonitorOkay"))
)
if mibBuilder.loadTexts:
    slapmEndSystemNotGroup2.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

slapmCompliance = ModuleCompliance(
    (1, 3, 6, 1, 3, 88, 2, 1, 1)
)
if mibBuilder.loadTexts:
    slapmCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SLAPM-MIB",
    **{"SlapmNameType": SlapmNameType,
       "SlapmStatus": SlapmStatus,
       "SlapmPolicyRuleName": SlapmPolicyRuleName,
       "slapmMIB": slapmMIB,
       "slapmNotifications": slapmNotifications,
       "slapmMonitoredEventNotAchieved": slapmMonitoredEventNotAchieved,
       "slapmMonitoredEventOkay": slapmMonitoredEventOkay,
       "slapmPolicyProfileDeleted": slapmPolicyProfileDeleted,
       "slapmPolicyMonitorDeleted": slapmPolicyMonitorDeleted,
       "slapmSubcomponentMonitoredEventNotAchieved": slapmSubcomponentMonitoredEventNotAchieved,
       "slapmSubcomponentMonitoredEventOkay": slapmSubcomponentMonitoredEventOkay,
       "slapmPolicyRuleMonNotOkay": slapmPolicyRuleMonNotOkay,
       "slapmPolicyRuleMonOkay": slapmPolicyRuleMonOkay,
       "slapmPolicyRuleDeleted": slapmPolicyRuleDeleted,
       "slapmPolicyRuleMonDeleted": slapmPolicyRuleMonDeleted,
       "slapmSubcMonitorNotOkay": slapmSubcMonitorNotOkay,
       "slapmSubcMonitorOkay": slapmSubcMonitorOkay,
       "slapmObjects": slapmObjects,
       "slapmBaseObjects": slapmBaseObjects,
       "slapmSpinLock": slapmSpinLock,
       "slapmPolicyCountQueries": slapmPolicyCountQueries,
       "slapmPolicyCountAccesses": slapmPolicyCountAccesses,
       "slapmPolicyCountSuccessAccesses": slapmPolicyCountSuccessAccesses,
       "slapmPolicyCountNotFounds": slapmPolicyCountNotFounds,
       "slapmPolicyPurgeTime": slapmPolicyPurgeTime,
       "slapmPolicyTrapEnable": slapmPolicyTrapEnable,
       "slapmPolicyTrapFilter": slapmPolicyTrapFilter,
       "slapmTableObjects": slapmTableObjects,
       "slapmPolicyStatsTable": slapmPolicyStatsTable,
       "slapmPolicyStatsEntry": slapmPolicyStatsEntry,
       "slapmPolicyStatsSystemAddress": slapmPolicyStatsSystemAddress,
       "slapmPolicyStatsPolicyName": slapmPolicyStatsPolicyName,
       "slapmPolicyStatsTrafficProfileName": slapmPolicyStatsTrafficProfileName,
       "slapmPolicyStatsOperStatus": slapmPolicyStatsOperStatus,
       "slapmPolicyStatsActiveConns": slapmPolicyStatsActiveConns,
       "slapmPolicyStatsTotalConns": slapmPolicyStatsTotalConns,
       "slapmPolicyStatsFirstActivated": slapmPolicyStatsFirstActivated,
       "slapmPolicyStatsLastMapping": slapmPolicyStatsLastMapping,
       "slapmPolicyStatsInOctets": slapmPolicyStatsInOctets,
       "slapmPolicyStatsOutOctets": slapmPolicyStatsOutOctets,
       "slapmPolicyStatsConnectionLimit": slapmPolicyStatsConnectionLimit,
       "slapmPolicyStatsCountAccepts": slapmPolicyStatsCountAccepts,
       "slapmPolicyStatsCountDenies": slapmPolicyStatsCountDenies,
       "slapmPolicyStatsInDiscards": slapmPolicyStatsInDiscards,
       "slapmPolicyStatsOutDiscards": slapmPolicyStatsOutDiscards,
       "slapmPolicyStatsInPackets": slapmPolicyStatsInPackets,
       "slapmPolicyStatsOutPackets": slapmPolicyStatsOutPackets,
       "slapmPolicyStatsInProfileOctets": slapmPolicyStatsInProfileOctets,
       "slapmPolicyStatsOutProfileOctets": slapmPolicyStatsOutProfileOctets,
       "slapmPolicyStatsMinRate": slapmPolicyStatsMinRate,
       "slapmPolicyStatsMaxRate": slapmPolicyStatsMaxRate,
       "slapmPolicyStatsMaxDelay": slapmPolicyStatsMaxDelay,
       "slapmPolicyMonitorTable": slapmPolicyMonitorTable,
       "slapmPolicyMonitorEntry": slapmPolicyMonitorEntry,
       "slapmPolicyMonitorOwnerIndex": slapmPolicyMonitorOwnerIndex,
       "slapmPolicyMonitorSystemAddress": slapmPolicyMonitorSystemAddress,
       "slapmPolicyMonitorPolicyName": slapmPolicyMonitorPolicyName,
       "slapmPolicyMonitorTrafficProfileName": slapmPolicyMonitorTrafficProfileName,
       "slapmPolicyMonitorControl": slapmPolicyMonitorControl,
       "slapmPolicyMonitorStatus": slapmPolicyMonitorStatus,
       "slapmPolicyMonitorInterval": slapmPolicyMonitorInterval,
       "slapmPolicyMonitorIntTime": slapmPolicyMonitorIntTime,
       "slapmPolicyMonitorCurrentInRate": slapmPolicyMonitorCurrentInRate,
       "slapmPolicyMonitorCurrentOutRate": slapmPolicyMonitorCurrentOutRate,
       "slapmPolicyMonitorMinRateLow": slapmPolicyMonitorMinRateLow,
       "slapmPolicyMonitorMinRateHigh": slapmPolicyMonitorMinRateHigh,
       "slapmPolicyMonitorMaxRateHigh": slapmPolicyMonitorMaxRateHigh,
       "slapmPolicyMonitorMaxRateLow": slapmPolicyMonitorMaxRateLow,
       "slapmPolicyMonitorMaxDelayHigh": slapmPolicyMonitorMaxDelayHigh,
       "slapmPolicyMonitorMaxDelayLow": slapmPolicyMonitorMaxDelayLow,
       "slapmPolicyMonitorMinInRateNotAchieves": slapmPolicyMonitorMinInRateNotAchieves,
       "slapmPolicyMonitorMaxInRateExceeds": slapmPolicyMonitorMaxInRateExceeds,
       "slapmPolicyMonitorMaxDelayExceeds": slapmPolicyMonitorMaxDelayExceeds,
       "slapmPolicyMonitorMinOutRateNotAchieves": slapmPolicyMonitorMinOutRateNotAchieves,
       "slapmPolicyMonitorMaxOutRateExceeds": slapmPolicyMonitorMaxOutRateExceeds,
       "slapmPolicyMonitorCurrentDelayRate": slapmPolicyMonitorCurrentDelayRate,
       "slapmPolicyMonitorRowStatus": slapmPolicyMonitorRowStatus,
       "slapmSubcomponentTable": slapmSubcomponentTable,
       "slapmSubcomponentEntry": slapmSubcomponentEntry,
       "slapmSubcomponentRemAddress": slapmSubcomponentRemAddress,
       "slapmSubcomponentRemPort": slapmSubcomponentRemPort,
       "slapmSubcomponentLocalAddress": slapmSubcomponentLocalAddress,
       "slapmSubcomponentLocalPort": slapmSubcomponentLocalPort,
       "slapmSubcomponentProtocol": slapmSubcomponentProtocol,
       "slapmSubcomponentSystemAddress": slapmSubcomponentSystemAddress,
       "slapmSubcomponentPolicyName": slapmSubcomponentPolicyName,
       "slapmSubcomponentTrafficProfileName": slapmSubcomponentTrafficProfileName,
       "slapmSubcomponentLastActivity": slapmSubcomponentLastActivity,
       "slapmSubcomponentInOctets": slapmSubcomponentInOctets,
       "slapmSubcomponentOutOctets": slapmSubcomponentOutOctets,
       "slapmSubcomponentTcpOutBufferedOctets": slapmSubcomponentTcpOutBufferedOctets,
       "slapmSubcomponentTcpInBufferedOctets": slapmSubcomponentTcpInBufferedOctets,
       "slapmSubcomponentTcpReXmts": slapmSubcomponentTcpReXmts,
       "slapmSubcomponentTcpRoundTripTime": slapmSubcomponentTcpRoundTripTime,
       "slapmSubcomponentTcpRoundTripVariance": slapmSubcomponentTcpRoundTripVariance,
       "slapmSubcomponentInPdus": slapmSubcomponentInPdus,
       "slapmSubcomponentOutPdus": slapmSubcomponentOutPdus,
       "slapmSubcomponentApplName": slapmSubcomponentApplName,
       "slapmSubcomponentMonitorStatus": slapmSubcomponentMonitorStatus,
       "slapmSubcomponentMonitorIntTime": slapmSubcomponentMonitorIntTime,
       "slapmSubcomponentMonitorCurrentInRate": slapmSubcomponentMonitorCurrentInRate,
       "slapmSubcomponentMonitorCurrentOutRate": slapmSubcomponentMonitorCurrentOutRate,
       "slapmSubcomponentPolicyRuleIndex": slapmSubcomponentPolicyRuleIndex,
       "slapmPolicyNameTable": slapmPolicyNameTable,
       "slapmPolicyNameEntry": slapmPolicyNameEntry,
       "slapmPolicyNameSystemAddress": slapmPolicyNameSystemAddress,
       "slapmPolicyNameIndex": slapmPolicyNameIndex,
       "slapmPolicyNameOfRule": slapmPolicyNameOfRule,
       "slapmPolicyRuleStatsTable": slapmPolicyRuleStatsTable,
       "slapmPolicyRuleStatsEntry": slapmPolicyRuleStatsEntry,
       "slapmPolicyRuleStatsOperStatus": slapmPolicyRuleStatsOperStatus,
       "slapmPolicyRuleStatsActiveConns": slapmPolicyRuleStatsActiveConns,
       "slapmPolicyRuleStatsTotalConns": slapmPolicyRuleStatsTotalConns,
       "slapmPolicyRuleStatsLActivated": slapmPolicyRuleStatsLActivated,
       "slapmPolicyRuleStatsLastMapping": slapmPolicyRuleStatsLastMapping,
       "slapmPolicyRuleStatsInOctets": slapmPolicyRuleStatsInOctets,
       "slapmPolicyRuleStatsOutOctets": slapmPolicyRuleStatsOutOctets,
       "slapmPolicyRuleStatsConnLimit": slapmPolicyRuleStatsConnLimit,
       "slapmPolicyRuleStatsCountAccepts": slapmPolicyRuleStatsCountAccepts,
       "slapmPolicyRuleStatsCountDenies": slapmPolicyRuleStatsCountDenies,
       "slapmPolicyRuleStatsInDiscards": slapmPolicyRuleStatsInDiscards,
       "slapmPolicyRuleStatsOutDiscards": slapmPolicyRuleStatsOutDiscards,
       "slapmPolicyRuleStatsInPackets": slapmPolicyRuleStatsInPackets,
       "slapmPolicyRuleStatsOutPackets": slapmPolicyRuleStatsOutPackets,
       "slapmPolicyRuleStatsInProOctets": slapmPolicyRuleStatsInProOctets,
       "slapmPolicyRuleStatsOutProOctets": slapmPolicyRuleStatsOutProOctets,
       "slapmPolicyRuleStatsMinRate": slapmPolicyRuleStatsMinRate,
       "slapmPolicyRuleStatsMaxRate": slapmPolicyRuleStatsMaxRate,
       "slapmPolicyRuleStatsMaxDelay": slapmPolicyRuleStatsMaxDelay,
       "slapmPolicyRuleStatsTotalRsvpFlows": slapmPolicyRuleStatsTotalRsvpFlows,
       "slapmPolicyRuleStatsActRsvpFlows": slapmPolicyRuleStatsActRsvpFlows,
       "slapmPRMonTable": slapmPRMonTable,
       "slapmPRMonEntry": slapmPRMonEntry,
       "slapmPRMonOwnerIndex": slapmPRMonOwnerIndex,
       "slapmPRMonSystemAddress": slapmPRMonSystemAddress,
       "slapmPRMonIndex": slapmPRMonIndex,
       "slapmPRMonControl": slapmPRMonControl,
       "slapmPRMonStatus": slapmPRMonStatus,
       "slapmPRMonInterval": slapmPRMonInterval,
       "slapmPRMonIntTime": slapmPRMonIntTime,
       "slapmPRMonCurrentInRate": slapmPRMonCurrentInRate,
       "slapmPRMonCurrentOutRate": slapmPRMonCurrentOutRate,
       "slapmPRMonMinRateLow": slapmPRMonMinRateLow,
       "slapmPRMonMinRateHigh": slapmPRMonMinRateHigh,
       "slapmPRMonMaxRateHigh": slapmPRMonMaxRateHigh,
       "slapmPRMonMaxRateLow": slapmPRMonMaxRateLow,
       "slapmPRMonMaxDelayHigh": slapmPRMonMaxDelayHigh,
       "slapmPRMonMaxDelayLow": slapmPRMonMaxDelayLow,
       "slapmPRMonMinInRateNotAchieves": slapmPRMonMinInRateNotAchieves,
       "slapmPRMonMaxInRateExceeds": slapmPRMonMaxInRateExceeds,
       "slapmPRMonMaxDelayExceeds": slapmPRMonMaxDelayExceeds,
       "slapmPRMonMinOutRateNotAchieves": slapmPRMonMinOutRateNotAchieves,
       "slapmPRMonMaxOutRateExceeds": slapmPRMonMaxOutRateExceeds,
       "slapmPRMonCurrentDelayRate": slapmPRMonCurrentDelayRate,
       "slapmPRMonRowStatus": slapmPRMonRowStatus,
       "slapmConformance": slapmConformance,
       "slapmCompliances": slapmCompliances,
       "slapmCompliance": slapmCompliance,
       "slapmGroups": slapmGroups,
       "slapmBaseGroup": slapmBaseGroup,
       "slapmOptionalGroup": slapmOptionalGroup,
       "slapmEndSystemGroup": slapmEndSystemGroup,
       "slapmNotGroup": slapmNotGroup,
       "slapmEndSystemNotGroup": slapmEndSystemNotGroup,
       "slapmBaseGroup2": slapmBaseGroup2,
       "slapmEndSystemGroup2": slapmEndSystemGroup2,
       "slapmNotGroup2": slapmNotGroup2,
       "slapmEndSystemNotGroup2": slapmEndSystemNotGroup2}
)
