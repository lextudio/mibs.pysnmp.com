# SNMP MIB module (ALCATEL-IND1-MVRP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ALCATEL-IND1-MVRP-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:36:36 2024
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

(softentIND1Mvrp,) = mibBuilder.importSymbols(
    "ALCATEL-IND1-BASE",
    "softentIND1Mvrp")

(InterfaceIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex")

(EnabledStatus,) = mibBuilder.importSymbols(
    "P-BRIDGE-MIB",
    "EnabledStatus")

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
 MacAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "TextualConvention")


# MODULE-IDENTITY

alcatelIND1MVRPMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 62, 1)
)
alcatelIND1MVRPMIB.setRevisions(
        ("2010-05-13 00:00",
         "2009-08-07 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class MvrpPortVlanRestrictBitmap(Bits, TextualConvention):
    status = "current"


# MIB Managed Objects in the order of their OIDs

_AlcatelIND1MVRPMIBNotifications_ObjectIdentity = ObjectIdentity
alcatelIND1MVRPMIBNotifications = _AlcatelIND1MVRPMIBNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 62, 1, 0)
)
if mibBuilder.loadTexts:
    alcatelIND1MVRPMIBNotifications.setStatus("current")
_AlcatelIND1MVRPMIBObjects_ObjectIdentity = ObjectIdentity
alcatelIND1MVRPMIBObjects = _AlcatelIND1MVRPMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 62, 1, 1)
)
if mibBuilder.loadTexts:
    alcatelIND1MVRPMIBObjects.setStatus("current")


class _AlaMvrpGlobalStatus_Type(EnabledStatus):
    """Custom type alaMvrpGlobalStatus based on EnabledStatus"""


_AlaMvrpGlobalStatus_Object = MibScalar
alaMvrpGlobalStatus = _AlaMvrpGlobalStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 62, 1, 1, 1),
    _AlaMvrpGlobalStatus_Type()
)
alaMvrpGlobalStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaMvrpGlobalStatus.setStatus("current")


class _AlaMvrpGlobalClearStats_Type(Integer32):
    """Custom type alaMvrpGlobalClearStats based on Integer32"""
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


_AlaMvrpGlobalClearStats_Type.__name__ = "Integer32"
_AlaMvrpGlobalClearStats_Object = MibScalar
alaMvrpGlobalClearStats = _AlaMvrpGlobalClearStats_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 62, 1, 1, 2),
    _AlaMvrpGlobalClearStats_Type()
)
alaMvrpGlobalClearStats.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaMvrpGlobalClearStats.setStatus("current")


class _AlaMvrpTransparentSwitching_Type(EnabledStatus):
    """Custom type alaMvrpTransparentSwitching based on EnabledStatus"""


_AlaMvrpTransparentSwitching_Object = MibScalar
alaMvrpTransparentSwitching = _AlaMvrpTransparentSwitching_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 62, 1, 1, 3),
    _AlaMvrpTransparentSwitching_Type()
)
alaMvrpTransparentSwitching.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaMvrpTransparentSwitching.setStatus("current")


class _AlaMvrpMaxVlanLimit_Type(Integer32):
    """Custom type alaMvrpMaxVlanLimit based on Integer32"""
    defaultValue = 256

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(32, 4094),
    )


_AlaMvrpMaxVlanLimit_Type.__name__ = "Integer32"
_AlaMvrpMaxVlanLimit_Object = MibScalar
alaMvrpMaxVlanLimit = _AlaMvrpMaxVlanLimit_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 62, 1, 1, 4),
    _AlaMvrpMaxVlanLimit_Type()
)
alaMvrpMaxVlanLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaMvrpMaxVlanLimit.setStatus("current")


class _AlaMvrpVlanConflictInfo_Type(OctetString):
    """Custom type alaMvrpVlanConflictInfo based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 100),
    )


_AlaMvrpVlanConflictInfo_Type.__name__ = "OctetString"
_AlaMvrpVlanConflictInfo_Object = MibScalar
alaMvrpVlanConflictInfo = _AlaMvrpVlanConflictInfo_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 62, 1, 1, 5),
    _AlaMvrpVlanConflictInfo_Type()
)
alaMvrpVlanConflictInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaMvrpVlanConflictInfo.setStatus("current")


class _AlaVlanRegistrationProtocolType_Type(Integer32):
    """Custom type alaVlanRegistrationProtocolType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("gvrp", 0),
          ("mvrp", 1))
    )


_AlaVlanRegistrationProtocolType_Type.__name__ = "Integer32"
_AlaVlanRegistrationProtocolType_Object = MibScalar
alaVlanRegistrationProtocolType = _AlaVlanRegistrationProtocolType_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 62, 1, 1, 6),
    _AlaVlanRegistrationProtocolType_Type()
)
alaVlanRegistrationProtocolType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaVlanRegistrationProtocolType.setStatus("current")
_AlaMvrpPortConfig_ObjectIdentity = ObjectIdentity
alaMvrpPortConfig = _AlaMvrpPortConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 62, 1, 1, 7)
)
_AlaMvrpPortConfigTable_Object = MibTable
alaMvrpPortConfigTable = _AlaMvrpPortConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 62, 1, 1, 7, 1)
)
if mibBuilder.loadTexts:
    alaMvrpPortConfigTable.setStatus("current")
_AlaMvrpPortConfigEntry_Object = MibTableRow
alaMvrpPortConfigEntry = _AlaMvrpPortConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 62, 1, 1, 7, 1, 1)
)
alaMvrpPortConfigEntry.setIndexNames(
    (0, "ALCATEL-IND1-MVRP-MIB", "alaMvrpPortConfigIfIndex"),
)
if mibBuilder.loadTexts:
    alaMvrpPortConfigEntry.setStatus("current")
_AlaMvrpPortConfigIfIndex_Type = InterfaceIndex
_AlaMvrpPortConfigIfIndex_Object = MibTableColumn
alaMvrpPortConfigIfIndex = _AlaMvrpPortConfigIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 62, 1, 1, 7, 1, 1, 1),
    _AlaMvrpPortConfigIfIndex_Type()
)
alaMvrpPortConfigIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaMvrpPortConfigIfIndex.setStatus("current")


class _AlaMvrpPortStatus_Type(EnabledStatus):
    """Custom type alaMvrpPortStatus based on EnabledStatus"""


_AlaMvrpPortStatus_Object = MibTableColumn
alaMvrpPortStatus = _AlaMvrpPortStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 62, 1, 1, 7, 1, 1, 2),
    _AlaMvrpPortStatus_Type()
)
alaMvrpPortStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaMvrpPortStatus.setStatus("current")


class _AlaMvrpPortConfigRegistrarMode_Type(Integer32):
    """Custom type alaMvrpPortConfigRegistrarMode based on Integer32"""
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
        *(("fixed", 2),
          ("forbidden", 3),
          ("normal", 1))
    )


_AlaMvrpPortConfigRegistrarMode_Type.__name__ = "Integer32"
_AlaMvrpPortConfigRegistrarMode_Object = MibTableColumn
alaMvrpPortConfigRegistrarMode = _AlaMvrpPortConfigRegistrarMode_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 62, 1, 1, 7, 1, 1, 3),
    _AlaMvrpPortConfigRegistrarMode_Type()
)
alaMvrpPortConfigRegistrarMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaMvrpPortConfigRegistrarMode.setStatus("current")


class _AlaMvrpPortConfigApplicantMode_Type(Integer32):
    """Custom type alaMvrpPortConfigApplicantMode based on Integer32"""
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
        *(("active", 3),
          ("nonparticipant", 2),
          ("participant", 1))
    )


_AlaMvrpPortConfigApplicantMode_Type.__name__ = "Integer32"
_AlaMvrpPortConfigApplicantMode_Object = MibTableColumn
alaMvrpPortConfigApplicantMode = _AlaMvrpPortConfigApplicantMode_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 62, 1, 1, 7, 1, 1, 4),
    _AlaMvrpPortConfigApplicantMode_Type()
)
alaMvrpPortConfigApplicantMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaMvrpPortConfigApplicantMode.setStatus("current")


class _AlaMvrpPortConfigJoinTimer_Type(Integer32):
    """Custom type alaMvrpPortConfigJoinTimer based on Integer32"""
    defaultValue = 600

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(250, 2147483647),
    )


_AlaMvrpPortConfigJoinTimer_Type.__name__ = "Integer32"
_AlaMvrpPortConfigJoinTimer_Object = MibTableColumn
alaMvrpPortConfigJoinTimer = _AlaMvrpPortConfigJoinTimer_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 62, 1, 1, 7, 1, 1, 5),
    _AlaMvrpPortConfigJoinTimer_Type()
)
alaMvrpPortConfigJoinTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaMvrpPortConfigJoinTimer.setStatus("current")
if mibBuilder.loadTexts:
    alaMvrpPortConfigJoinTimer.setUnits("milliseconds")


class _AlaMvrpPortConfigLeaveTimer_Type(Integer32):
    """Custom type alaMvrpPortConfigLeaveTimer based on Integer32"""
    defaultValue = 1800

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(750, 2147483647),
    )


_AlaMvrpPortConfigLeaveTimer_Type.__name__ = "Integer32"
_AlaMvrpPortConfigLeaveTimer_Object = MibTableColumn
alaMvrpPortConfigLeaveTimer = _AlaMvrpPortConfigLeaveTimer_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 62, 1, 1, 7, 1, 1, 6),
    _AlaMvrpPortConfigLeaveTimer_Type()
)
alaMvrpPortConfigLeaveTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaMvrpPortConfigLeaveTimer.setStatus("current")
if mibBuilder.loadTexts:
    alaMvrpPortConfigLeaveTimer.setUnits("milliseconds")


class _AlaMvrpPortConfigLeaveAllTimer_Type(Integer32):
    """Custom type alaMvrpPortConfigLeaveAllTimer based on Integer32"""
    defaultValue = 30000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(750, 2147483647),
    )


_AlaMvrpPortConfigLeaveAllTimer_Type.__name__ = "Integer32"
_AlaMvrpPortConfigLeaveAllTimer_Object = MibTableColumn
alaMvrpPortConfigLeaveAllTimer = _AlaMvrpPortConfigLeaveAllTimer_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 62, 1, 1, 7, 1, 1, 7),
    _AlaMvrpPortConfigLeaveAllTimer_Type()
)
alaMvrpPortConfigLeaveAllTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaMvrpPortConfigLeaveAllTimer.setStatus("current")
if mibBuilder.loadTexts:
    alaMvrpPortConfigLeaveAllTimer.setUnits("milliseconds")


class _AlaMvrpPortConfigPeriodicTimer_Type(Integer32):
    """Custom type alaMvrpPortConfigPeriodicTimer based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_AlaMvrpPortConfigPeriodicTimer_Type.__name__ = "Integer32"
_AlaMvrpPortConfigPeriodicTimer_Object = MibTableColumn
alaMvrpPortConfigPeriodicTimer = _AlaMvrpPortConfigPeriodicTimer_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 62, 1, 1, 7, 1, 1, 8),
    _AlaMvrpPortConfigPeriodicTimer_Type()
)
alaMvrpPortConfigPeriodicTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaMvrpPortConfigPeriodicTimer.setStatus("current")
if mibBuilder.loadTexts:
    alaMvrpPortConfigPeriodicTimer.setUnits("seconds")


class _AlaMvrpPortConfigPeriodicTransmissionStatus_Type(EnabledStatus):
    """Custom type alaMvrpPortConfigPeriodicTransmissionStatus based on EnabledStatus"""


_AlaMvrpPortConfigPeriodicTransmissionStatus_Object = MibTableColumn
alaMvrpPortConfigPeriodicTransmissionStatus = _AlaMvrpPortConfigPeriodicTransmissionStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 62, 1, 1, 7, 1, 1, 9),
    _AlaMvrpPortConfigPeriodicTransmissionStatus_Type()
)
alaMvrpPortConfigPeriodicTransmissionStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaMvrpPortConfigPeriodicTransmissionStatus.setStatus("current")
_AlaMvrpPortStats_ObjectIdentity = ObjectIdentity
alaMvrpPortStats = _AlaMvrpPortStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 62, 1, 1, 8)
)
_AlaMvrpPortStatsTable_Object = MibTable
alaMvrpPortStatsTable = _AlaMvrpPortStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 62, 1, 1, 8, 1)
)
if mibBuilder.loadTexts:
    alaMvrpPortStatsTable.setStatus("current")
_AlaMvrpPortStatsEntry_Object = MibTableRow
alaMvrpPortStatsEntry = _AlaMvrpPortStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 62, 1, 1, 8, 1, 1)
)
alaMvrpPortStatsEntry.setIndexNames(
    (0, "ALCATEL-IND1-MVRP-MIB", "alaMvrpPortStatsIfIndex"),
)
if mibBuilder.loadTexts:
    alaMvrpPortStatsEntry.setStatus("current")
_AlaMvrpPortStatsIfIndex_Type = InterfaceIndex
_AlaMvrpPortStatsIfIndex_Object = MibTableColumn
alaMvrpPortStatsIfIndex = _AlaMvrpPortStatsIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 62, 1, 1, 8, 1, 1, 1),
    _AlaMvrpPortStatsIfIndex_Type()
)
alaMvrpPortStatsIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaMvrpPortStatsIfIndex.setStatus("current")
_AlaMvrpPortStatsNewReceived_Type = Counter32
_AlaMvrpPortStatsNewReceived_Object = MibTableColumn
alaMvrpPortStatsNewReceived = _AlaMvrpPortStatsNewReceived_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 62, 1, 1, 8, 1, 1, 2),
    _AlaMvrpPortStatsNewReceived_Type()
)
alaMvrpPortStatsNewReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaMvrpPortStatsNewReceived.setStatus("current")
_AlaMvrpPortStatsJoinInReceived_Type = Counter32
_AlaMvrpPortStatsJoinInReceived_Object = MibTableColumn
alaMvrpPortStatsJoinInReceived = _AlaMvrpPortStatsJoinInReceived_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 62, 1, 1, 8, 1, 1, 3),
    _AlaMvrpPortStatsJoinInReceived_Type()
)
alaMvrpPortStatsJoinInReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaMvrpPortStatsJoinInReceived.setStatus("current")
_AlaMvrpPortStatsJoinEmptyReceived_Type = Counter32
_AlaMvrpPortStatsJoinEmptyReceived_Object = MibTableColumn
alaMvrpPortStatsJoinEmptyReceived = _AlaMvrpPortStatsJoinEmptyReceived_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 62, 1, 1, 8, 1, 1, 4),
    _AlaMvrpPortStatsJoinEmptyReceived_Type()
)
alaMvrpPortStatsJoinEmptyReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaMvrpPortStatsJoinEmptyReceived.setStatus("current")
_AlaMvrpPortStatsLeaveReceived_Type = Counter32
_AlaMvrpPortStatsLeaveReceived_Object = MibTableColumn
alaMvrpPortStatsLeaveReceived = _AlaMvrpPortStatsLeaveReceived_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 62, 1, 1, 8, 1, 1, 5),
    _AlaMvrpPortStatsLeaveReceived_Type()
)
alaMvrpPortStatsLeaveReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaMvrpPortStatsLeaveReceived.setStatus("current")
_AlaMvrpPortStatsInReceived_Type = Counter32
_AlaMvrpPortStatsInReceived_Object = MibTableColumn
alaMvrpPortStatsInReceived = _AlaMvrpPortStatsInReceived_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 62, 1, 1, 8, 1, 1, 6),
    _AlaMvrpPortStatsInReceived_Type()
)
alaMvrpPortStatsInReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaMvrpPortStatsInReceived.setStatus("current")
_AlaMvrpPortStatsEmptyReceived_Type = Counter32
_AlaMvrpPortStatsEmptyReceived_Object = MibTableColumn
alaMvrpPortStatsEmptyReceived = _AlaMvrpPortStatsEmptyReceived_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 62, 1, 1, 8, 1, 1, 7),
    _AlaMvrpPortStatsEmptyReceived_Type()
)
alaMvrpPortStatsEmptyReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaMvrpPortStatsEmptyReceived.setStatus("current")
_AlaMvrpPortStatsLeaveAllReceived_Type = Counter32
_AlaMvrpPortStatsLeaveAllReceived_Object = MibTableColumn
alaMvrpPortStatsLeaveAllReceived = _AlaMvrpPortStatsLeaveAllReceived_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 62, 1, 1, 8, 1, 1, 8),
    _AlaMvrpPortStatsLeaveAllReceived_Type()
)
alaMvrpPortStatsLeaveAllReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaMvrpPortStatsLeaveAllReceived.setStatus("current")
_AlaMvrpPortStatsNewTransmitted_Type = Counter32
_AlaMvrpPortStatsNewTransmitted_Object = MibTableColumn
alaMvrpPortStatsNewTransmitted = _AlaMvrpPortStatsNewTransmitted_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 62, 1, 1, 8, 1, 1, 9),
    _AlaMvrpPortStatsNewTransmitted_Type()
)
alaMvrpPortStatsNewTransmitted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaMvrpPortStatsNewTransmitted.setStatus("current")
_AlaMvrpPortStatsJoinInTransmitted_Type = Counter32
_AlaMvrpPortStatsJoinInTransmitted_Object = MibTableColumn
alaMvrpPortStatsJoinInTransmitted = _AlaMvrpPortStatsJoinInTransmitted_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 62, 1, 1, 8, 1, 1, 10),
    _AlaMvrpPortStatsJoinInTransmitted_Type()
)
alaMvrpPortStatsJoinInTransmitted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaMvrpPortStatsJoinInTransmitted.setStatus("current")
_AlaMvrpPortStatsJoinEmptyTransmitted_Type = Counter32
_AlaMvrpPortStatsJoinEmptyTransmitted_Object = MibTableColumn
alaMvrpPortStatsJoinEmptyTransmitted = _AlaMvrpPortStatsJoinEmptyTransmitted_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 62, 1, 1, 8, 1, 1, 11),
    _AlaMvrpPortStatsJoinEmptyTransmitted_Type()
)
alaMvrpPortStatsJoinEmptyTransmitted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaMvrpPortStatsJoinEmptyTransmitted.setStatus("current")
_AlaMvrpPortStatsLeaveTransmitted_Type = Counter32
_AlaMvrpPortStatsLeaveTransmitted_Object = MibTableColumn
alaMvrpPortStatsLeaveTransmitted = _AlaMvrpPortStatsLeaveTransmitted_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 62, 1, 1, 8, 1, 1, 12),
    _AlaMvrpPortStatsLeaveTransmitted_Type()
)
alaMvrpPortStatsLeaveTransmitted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaMvrpPortStatsLeaveTransmitted.setStatus("current")
_AlaMvrpPortStatsInTransmitted_Type = Counter32
_AlaMvrpPortStatsInTransmitted_Object = MibTableColumn
alaMvrpPortStatsInTransmitted = _AlaMvrpPortStatsInTransmitted_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 62, 1, 1, 8, 1, 1, 13),
    _AlaMvrpPortStatsInTransmitted_Type()
)
alaMvrpPortStatsInTransmitted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaMvrpPortStatsInTransmitted.setStatus("current")
_AlaMvrpPortStatsEmptyTransmitted_Type = Counter32
_AlaMvrpPortStatsEmptyTransmitted_Object = MibTableColumn
alaMvrpPortStatsEmptyTransmitted = _AlaMvrpPortStatsEmptyTransmitted_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 62, 1, 1, 8, 1, 1, 14),
    _AlaMvrpPortStatsEmptyTransmitted_Type()
)
alaMvrpPortStatsEmptyTransmitted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaMvrpPortStatsEmptyTransmitted.setStatus("current")
_AlaMvrpPortStatsLeaveAllTransmitted_Type = Counter32
_AlaMvrpPortStatsLeaveAllTransmitted_Object = MibTableColumn
alaMvrpPortStatsLeaveAllTransmitted = _AlaMvrpPortStatsLeaveAllTransmitted_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 62, 1, 1, 8, 1, 1, 15),
    _AlaMvrpPortStatsLeaveAllTransmitted_Type()
)
alaMvrpPortStatsLeaveAllTransmitted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaMvrpPortStatsLeaveAllTransmitted.setStatus("current")
_AlaMvrpPortStatsTotalPDUReceived_Type = Counter32
_AlaMvrpPortStatsTotalPDUReceived_Object = MibTableColumn
alaMvrpPortStatsTotalPDUReceived = _AlaMvrpPortStatsTotalPDUReceived_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 62, 1, 1, 8, 1, 1, 16),
    _AlaMvrpPortStatsTotalPDUReceived_Type()
)
alaMvrpPortStatsTotalPDUReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaMvrpPortStatsTotalPDUReceived.setStatus("current")
_AlaMvrpPortStatsTotalPDUTransmitted_Type = Counter32
_AlaMvrpPortStatsTotalPDUTransmitted_Object = MibTableColumn
alaMvrpPortStatsTotalPDUTransmitted = _AlaMvrpPortStatsTotalPDUTransmitted_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 62, 1, 1, 8, 1, 1, 17),
    _AlaMvrpPortStatsTotalPDUTransmitted_Type()
)
alaMvrpPortStatsTotalPDUTransmitted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaMvrpPortStatsTotalPDUTransmitted.setStatus("current")
_AlaMvrpPortStatsTotalMsgsReceived_Type = Counter32
_AlaMvrpPortStatsTotalMsgsReceived_Object = MibTableColumn
alaMvrpPortStatsTotalMsgsReceived = _AlaMvrpPortStatsTotalMsgsReceived_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 62, 1, 1, 8, 1, 1, 18),
    _AlaMvrpPortStatsTotalMsgsReceived_Type()
)
alaMvrpPortStatsTotalMsgsReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaMvrpPortStatsTotalMsgsReceived.setStatus("current")
_AlaMvrpPortStatsTotalMsgsTransmitted_Type = Counter32
_AlaMvrpPortStatsTotalMsgsTransmitted_Object = MibTableColumn
alaMvrpPortStatsTotalMsgsTransmitted = _AlaMvrpPortStatsTotalMsgsTransmitted_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 62, 1, 1, 8, 1, 1, 19),
    _AlaMvrpPortStatsTotalMsgsTransmitted_Type()
)
alaMvrpPortStatsTotalMsgsTransmitted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaMvrpPortStatsTotalMsgsTransmitted.setStatus("current")
_AlaMvrpPortStatsInvalidMsgsReceived_Type = Counter32
_AlaMvrpPortStatsInvalidMsgsReceived_Object = MibTableColumn
alaMvrpPortStatsInvalidMsgsReceived = _AlaMvrpPortStatsInvalidMsgsReceived_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 62, 1, 1, 8, 1, 1, 20),
    _AlaMvrpPortStatsInvalidMsgsReceived_Type()
)
alaMvrpPortStatsInvalidMsgsReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaMvrpPortStatsInvalidMsgsReceived.setStatus("current")
_AlaMvrpPortFailedRegistrations_Type = Counter32
_AlaMvrpPortFailedRegistrations_Object = MibTableColumn
alaMvrpPortFailedRegistrations = _AlaMvrpPortFailedRegistrations_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 62, 1, 1, 8, 1, 1, 21),
    _AlaMvrpPortFailedRegistrations_Type()
)
alaMvrpPortFailedRegistrations.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaMvrpPortFailedRegistrations.setStatus("current")
_AlaMvrpPortLastPduOrigin_Type = MacAddress
_AlaMvrpPortLastPduOrigin_Object = MibTableColumn
alaMvrpPortLastPduOrigin = _AlaMvrpPortLastPduOrigin_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 62, 1, 1, 8, 1, 1, 22),
    _AlaMvrpPortLastPduOrigin_Type()
)
alaMvrpPortLastPduOrigin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaMvrpPortLastPduOrigin.setStatus("current")


class _AlaMvrpPortStatsClearStats_Type(Integer32):
    """Custom type alaMvrpPortStatsClearStats based on Integer32"""
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


_AlaMvrpPortStatsClearStats_Type.__name__ = "Integer32"
_AlaMvrpPortStatsClearStats_Object = MibTableColumn
alaMvrpPortStatsClearStats = _AlaMvrpPortStatsClearStats_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 62, 1, 1, 8, 1, 1, 23),
    _AlaMvrpPortStatsClearStats_Type()
)
alaMvrpPortStatsClearStats.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaMvrpPortStatsClearStats.setStatus("current")
_AlaMvrpPortRestrictVlanConfig_ObjectIdentity = ObjectIdentity
alaMvrpPortRestrictVlanConfig = _AlaMvrpPortRestrictVlanConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 62, 1, 1, 9)
)
_AlaMvrpPortRestrictVlanConfigTable_Object = MibTable
alaMvrpPortRestrictVlanConfigTable = _AlaMvrpPortRestrictVlanConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 62, 1, 1, 9, 1)
)
if mibBuilder.loadTexts:
    alaMvrpPortRestrictVlanConfigTable.setStatus("current")
_AlaMvrpPortRestrictVlanConfigEntry_Object = MibTableRow
alaMvrpPortRestrictVlanConfigEntry = _AlaMvrpPortRestrictVlanConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 62, 1, 1, 9, 1, 1)
)
alaMvrpPortRestrictVlanConfigEntry.setIndexNames(
    (0, "ALCATEL-IND1-MVRP-MIB", "alaMvrpPortRestrictVlanIfIndex"),
    (0, "ALCATEL-IND1-MVRP-MIB", "alaMvrpPortRestrictVlanID"),
)
if mibBuilder.loadTexts:
    alaMvrpPortRestrictVlanConfigEntry.setStatus("current")
_AlaMvrpPortRestrictVlanIfIndex_Type = InterfaceIndex
_AlaMvrpPortRestrictVlanIfIndex_Object = MibTableColumn
alaMvrpPortRestrictVlanIfIndex = _AlaMvrpPortRestrictVlanIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 62, 1, 1, 9, 1, 1, 1),
    _AlaMvrpPortRestrictVlanIfIndex_Type()
)
alaMvrpPortRestrictVlanIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaMvrpPortRestrictVlanIfIndex.setStatus("current")
_AlaMvrpPortRestrictVlanID_Type = VlanId
_AlaMvrpPortRestrictVlanID_Object = MibTableColumn
alaMvrpPortRestrictVlanID = _AlaMvrpPortRestrictVlanID_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 62, 1, 1, 9, 1, 1, 2),
    _AlaMvrpPortRestrictVlanID_Type()
)
alaMvrpPortRestrictVlanID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaMvrpPortRestrictVlanID.setStatus("current")


class _AlaMvrpPortVlanRestrictions_Type(MvrpPortVlanRestrictBitmap):
    """Custom type alaMvrpPortVlanRestrictions based on MvrpPortVlanRestrictBitmap"""
    defaultBinValue = "1"


_AlaMvrpPortVlanRestrictions_Object = MibTableColumn
alaMvrpPortVlanRestrictions = _AlaMvrpPortVlanRestrictions_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 62, 1, 1, 9, 1, 1, 3),
    _AlaMvrpPortVlanRestrictions_Type()
)
alaMvrpPortVlanRestrictions.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaMvrpPortVlanRestrictions.setStatus("current")
_AlcatelIND1MVRPMIBConformance_ObjectIdentity = ObjectIdentity
alcatelIND1MVRPMIBConformance = _AlcatelIND1MVRPMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 62, 1, 2)
)
if mibBuilder.loadTexts:
    alcatelIND1MVRPMIBConformance.setStatus("current")
_AlcatelIND1MVRPMIBGroups_ObjectIdentity = ObjectIdentity
alcatelIND1MVRPMIBGroups = _AlcatelIND1MVRPMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 62, 1, 2, 1)
)
if mibBuilder.loadTexts:
    alcatelIND1MVRPMIBGroups.setStatus("current")
_AlcatelIND1MVRPMIBCompliances_ObjectIdentity = ObjectIdentity
alcatelIND1MVRPMIBCompliances = _AlcatelIND1MVRPMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 62, 1, 2, 2)
)
if mibBuilder.loadTexts:
    alcatelIND1MVRPMIBCompliances.setStatus("current")

# Managed Objects groups

alaMvrpBaseGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 62, 1, 2, 1, 1)
)
alaMvrpBaseGroup.setObjects(
      *(("ALCATEL-IND1-MVRP-MIB", "alaMvrpGlobalStatus"),
        ("ALCATEL-IND1-MVRP-MIB", "alaMvrpGlobalClearStats"),
        ("ALCATEL-IND1-MVRP-MIB", "alaMvrpTransparentSwitching"),
        ("ALCATEL-IND1-MVRP-MIB", "alaMvrpMaxVlanLimit"),
        ("ALCATEL-IND1-MVRP-MIB", "alaMvrpVlanConflictInfo"),
        ("ALCATEL-IND1-MVRP-MIB", "alaVlanRegistrationProtocolType"))
)
if mibBuilder.loadTexts:
    alaMvrpBaseGroup.setStatus("current")

alaMvrpPortConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 62, 1, 2, 1, 2)
)
alaMvrpPortConfigGroup.setObjects(
      *(("ALCATEL-IND1-MVRP-MIB", "alaMvrpPortStatus"),
        ("ALCATEL-IND1-MVRP-MIB", "alaMvrpPortConfigRegistrarMode"),
        ("ALCATEL-IND1-MVRP-MIB", "alaMvrpPortConfigApplicantMode"),
        ("ALCATEL-IND1-MVRP-MIB", "alaMvrpPortConfigJoinTimer"),
        ("ALCATEL-IND1-MVRP-MIB", "alaMvrpPortConfigLeaveTimer"),
        ("ALCATEL-IND1-MVRP-MIB", "alaMvrpPortConfigLeaveAllTimer"),
        ("ALCATEL-IND1-MVRP-MIB", "alaMvrpPortConfigPeriodicTimer"),
        ("ALCATEL-IND1-MVRP-MIB", "alaMvrpPortConfigPeriodicTransmissionStatus"))
)
if mibBuilder.loadTexts:
    alaMvrpPortConfigGroup.setStatus("current")

alaMvrpPortStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 62, 1, 2, 1, 3)
)
alaMvrpPortStatsGroup.setObjects(
      *(("ALCATEL-IND1-MVRP-MIB", "alaMvrpPortStatsNewReceived"),
        ("ALCATEL-IND1-MVRP-MIB", "alaMvrpPortStatsJoinInReceived"),
        ("ALCATEL-IND1-MVRP-MIB", "alaMvrpPortStatsJoinEmptyReceived"),
        ("ALCATEL-IND1-MVRP-MIB", "alaMvrpPortStatsLeaveReceived"),
        ("ALCATEL-IND1-MVRP-MIB", "alaMvrpPortStatsInReceived"),
        ("ALCATEL-IND1-MVRP-MIB", "alaMvrpPortStatsEmptyReceived"),
        ("ALCATEL-IND1-MVRP-MIB", "alaMvrpPortStatsLeaveAllReceived"),
        ("ALCATEL-IND1-MVRP-MIB", "alaMvrpPortStatsNewTransmitted"),
        ("ALCATEL-IND1-MVRP-MIB", "alaMvrpPortStatsJoinInTransmitted"),
        ("ALCATEL-IND1-MVRP-MIB", "alaMvrpPortStatsJoinEmptyTransmitted"),
        ("ALCATEL-IND1-MVRP-MIB", "alaMvrpPortStatsLeaveTransmitted"),
        ("ALCATEL-IND1-MVRP-MIB", "alaMvrpPortStatsInTransmitted"),
        ("ALCATEL-IND1-MVRP-MIB", "alaMvrpPortStatsEmptyTransmitted"),
        ("ALCATEL-IND1-MVRP-MIB", "alaMvrpPortStatsLeaveAllTransmitted"),
        ("ALCATEL-IND1-MVRP-MIB", "alaMvrpPortStatsTotalPDUReceived"),
        ("ALCATEL-IND1-MVRP-MIB", "alaMvrpPortStatsTotalPDUTransmitted"),
        ("ALCATEL-IND1-MVRP-MIB", "alaMvrpPortStatsTotalMsgsReceived"),
        ("ALCATEL-IND1-MVRP-MIB", "alaMvrpPortStatsTotalMsgsTransmitted"),
        ("ALCATEL-IND1-MVRP-MIB", "alaMvrpPortStatsInvalidMsgsReceived"),
        ("ALCATEL-IND1-MVRP-MIB", "alaMvrpPortFailedRegistrations"),
        ("ALCATEL-IND1-MVRP-MIB", "alaMvrpPortLastPduOrigin"),
        ("ALCATEL-IND1-MVRP-MIB", "alaMvrpPortStatsClearStats"))
)
if mibBuilder.loadTexts:
    alaMvrpPortStatsGroup.setStatus("current")

alaMvrpPortRestrictVlanConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 62, 1, 2, 1, 4)
)
alaMvrpPortRestrictVlanConfigGroup.setObjects(
    ("ALCATEL-IND1-MVRP-MIB", "alaMvrpPortVlanRestrictions")
)
if mibBuilder.loadTexts:
    alaMvrpPortRestrictVlanConfigGroup.setStatus("current")


# Notification objects

alaMvrpVlanLimitReachedEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 62, 1, 0, 1)
)
alaMvrpVlanLimitReachedEvent.setObjects(
    ("ALCATEL-IND1-MVRP-MIB", "alaMvrpMaxVlanLimit")
)
if mibBuilder.loadTexts:
    alaMvrpVlanLimitReachedEvent.setStatus(
        "current"
    )

alaMvrpE2eVlanConflict = NotificationType(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 62, 1, 0, 2)
)
alaMvrpE2eVlanConflict.setObjects(
    ("ALCATEL-IND1-MVRP-MIB", "alaMvrpVlanConflictInfo")
)
if mibBuilder.loadTexts:
    alaMvrpE2eVlanConflict.setStatus(
        "current"
    )


# Notifications groups

alaIND1MvrpNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 62, 1, 2, 1, 5)
)
alaIND1MvrpNotificationGroup.setObjects(
      *(("ALCATEL-IND1-MVRP-MIB", "alaMvrpVlanLimitReachedEvent"),
        ("ALCATEL-IND1-MVRP-MIB", "alaMvrpE2eVlanConflict"))
)
if mibBuilder.loadTexts:
    alaIND1MvrpNotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

alcatelIND1MVRPMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 62, 1, 2, 2, 1)
)
if mibBuilder.loadTexts:
    alcatelIND1MVRPMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ALCATEL-IND1-MVRP-MIB",
    **{"MvrpPortVlanRestrictBitmap": MvrpPortVlanRestrictBitmap,
       "alcatelIND1MVRPMIB": alcatelIND1MVRPMIB,
       "alcatelIND1MVRPMIBNotifications": alcatelIND1MVRPMIBNotifications,
       "alaMvrpVlanLimitReachedEvent": alaMvrpVlanLimitReachedEvent,
       "alaMvrpE2eVlanConflict": alaMvrpE2eVlanConflict,
       "alcatelIND1MVRPMIBObjects": alcatelIND1MVRPMIBObjects,
       "alaMvrpGlobalStatus": alaMvrpGlobalStatus,
       "alaMvrpGlobalClearStats": alaMvrpGlobalClearStats,
       "alaMvrpTransparentSwitching": alaMvrpTransparentSwitching,
       "alaMvrpMaxVlanLimit": alaMvrpMaxVlanLimit,
       "alaMvrpVlanConflictInfo": alaMvrpVlanConflictInfo,
       "alaVlanRegistrationProtocolType": alaVlanRegistrationProtocolType,
       "alaMvrpPortConfig": alaMvrpPortConfig,
       "alaMvrpPortConfigTable": alaMvrpPortConfigTable,
       "alaMvrpPortConfigEntry": alaMvrpPortConfigEntry,
       "alaMvrpPortConfigIfIndex": alaMvrpPortConfigIfIndex,
       "alaMvrpPortStatus": alaMvrpPortStatus,
       "alaMvrpPortConfigRegistrarMode": alaMvrpPortConfigRegistrarMode,
       "alaMvrpPortConfigApplicantMode": alaMvrpPortConfigApplicantMode,
       "alaMvrpPortConfigJoinTimer": alaMvrpPortConfigJoinTimer,
       "alaMvrpPortConfigLeaveTimer": alaMvrpPortConfigLeaveTimer,
       "alaMvrpPortConfigLeaveAllTimer": alaMvrpPortConfigLeaveAllTimer,
       "alaMvrpPortConfigPeriodicTimer": alaMvrpPortConfigPeriodicTimer,
       "alaMvrpPortConfigPeriodicTransmissionStatus": alaMvrpPortConfigPeriodicTransmissionStatus,
       "alaMvrpPortStats": alaMvrpPortStats,
       "alaMvrpPortStatsTable": alaMvrpPortStatsTable,
       "alaMvrpPortStatsEntry": alaMvrpPortStatsEntry,
       "alaMvrpPortStatsIfIndex": alaMvrpPortStatsIfIndex,
       "alaMvrpPortStatsNewReceived": alaMvrpPortStatsNewReceived,
       "alaMvrpPortStatsJoinInReceived": alaMvrpPortStatsJoinInReceived,
       "alaMvrpPortStatsJoinEmptyReceived": alaMvrpPortStatsJoinEmptyReceived,
       "alaMvrpPortStatsLeaveReceived": alaMvrpPortStatsLeaveReceived,
       "alaMvrpPortStatsInReceived": alaMvrpPortStatsInReceived,
       "alaMvrpPortStatsEmptyReceived": alaMvrpPortStatsEmptyReceived,
       "alaMvrpPortStatsLeaveAllReceived": alaMvrpPortStatsLeaveAllReceived,
       "alaMvrpPortStatsNewTransmitted": alaMvrpPortStatsNewTransmitted,
       "alaMvrpPortStatsJoinInTransmitted": alaMvrpPortStatsJoinInTransmitted,
       "alaMvrpPortStatsJoinEmptyTransmitted": alaMvrpPortStatsJoinEmptyTransmitted,
       "alaMvrpPortStatsLeaveTransmitted": alaMvrpPortStatsLeaveTransmitted,
       "alaMvrpPortStatsInTransmitted": alaMvrpPortStatsInTransmitted,
       "alaMvrpPortStatsEmptyTransmitted": alaMvrpPortStatsEmptyTransmitted,
       "alaMvrpPortStatsLeaveAllTransmitted": alaMvrpPortStatsLeaveAllTransmitted,
       "alaMvrpPortStatsTotalPDUReceived": alaMvrpPortStatsTotalPDUReceived,
       "alaMvrpPortStatsTotalPDUTransmitted": alaMvrpPortStatsTotalPDUTransmitted,
       "alaMvrpPortStatsTotalMsgsReceived": alaMvrpPortStatsTotalMsgsReceived,
       "alaMvrpPortStatsTotalMsgsTransmitted": alaMvrpPortStatsTotalMsgsTransmitted,
       "alaMvrpPortStatsInvalidMsgsReceived": alaMvrpPortStatsInvalidMsgsReceived,
       "alaMvrpPortFailedRegistrations": alaMvrpPortFailedRegistrations,
       "alaMvrpPortLastPduOrigin": alaMvrpPortLastPduOrigin,
       "alaMvrpPortStatsClearStats": alaMvrpPortStatsClearStats,
       "alaMvrpPortRestrictVlanConfig": alaMvrpPortRestrictVlanConfig,
       "alaMvrpPortRestrictVlanConfigTable": alaMvrpPortRestrictVlanConfigTable,
       "alaMvrpPortRestrictVlanConfigEntry": alaMvrpPortRestrictVlanConfigEntry,
       "alaMvrpPortRestrictVlanIfIndex": alaMvrpPortRestrictVlanIfIndex,
       "alaMvrpPortRestrictVlanID": alaMvrpPortRestrictVlanID,
       "alaMvrpPortVlanRestrictions": alaMvrpPortVlanRestrictions,
       "alcatelIND1MVRPMIBConformance": alcatelIND1MVRPMIBConformance,
       "alcatelIND1MVRPMIBGroups": alcatelIND1MVRPMIBGroups,
       "alaMvrpBaseGroup": alaMvrpBaseGroup,
       "alaMvrpPortConfigGroup": alaMvrpPortConfigGroup,
       "alaMvrpPortStatsGroup": alaMvrpPortStatsGroup,
       "alaMvrpPortRestrictVlanConfigGroup": alaMvrpPortRestrictVlanConfigGroup,
       "alaIND1MvrpNotificationGroup": alaIND1MvrpNotificationGroup,
       "alcatelIND1MVRPMIBCompliances": alcatelIND1MVRPMIBCompliances,
       "alcatelIND1MVRPMIBCompliance": alcatelIND1MVRPMIBCompliance}
)
