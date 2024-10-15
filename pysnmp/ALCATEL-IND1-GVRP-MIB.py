# SNMP MIB module (ALCATEL-IND1-GVRP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ALCATEL-IND1-GVRP-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:36:07 2024
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

(softentIND1Gvrp,) = mibBuilder.importSymbols(
    "ALCATEL-IND1-BASE",
    "softentIND1Gvrp")

(VlanBitmap,) = mibBuilder.importSymbols(
    "ALCATEL-IND1-VLAN-STP-MIB",
    "VlanBitmap")

(InterfaceIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY

alcatelIND1GVRPMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 36, 1)
)
alcatelIND1GVRPMIB.setRevisions(
        ("2010-05-13 00:00",
         "2007-07-02 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_AlcatelIND1GVRPMIBNotifications_ObjectIdentity = ObjectIdentity
alcatelIND1GVRPMIBNotifications = _AlcatelIND1GVRPMIBNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 36, 1, 0)
)
if mibBuilder.loadTexts:
    alcatelIND1GVRPMIBNotifications.setStatus("current")
_AlcatelIND1GVRPMIBObjects_ObjectIdentity = ObjectIdentity
alcatelIND1GVRPMIBObjects = _AlcatelIND1GVRPMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 36, 1, 1)
)
if mibBuilder.loadTexts:
    alcatelIND1GVRPMIBObjects.setStatus("current")


class _AlaGvrpGlobalClearStats_Type(Integer32):
    """Custom type alaGvrpGlobalClearStats based on Integer32"""
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


_AlaGvrpGlobalClearStats_Type.__name__ = "Integer32"
_AlaGvrpGlobalClearStats_Object = MibScalar
alaGvrpGlobalClearStats = _AlaGvrpGlobalClearStats_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 36, 1, 1, 1),
    _AlaGvrpGlobalClearStats_Type()
)
alaGvrpGlobalClearStats.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaGvrpGlobalClearStats.setStatus("current")


class _AlaGvrpTransparentSwitching_Type(Integer32):
    """Custom type alaGvrpTransparentSwitching based on Integer32"""
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


_AlaGvrpTransparentSwitching_Type.__name__ = "Integer32"
_AlaGvrpTransparentSwitching_Object = MibScalar
alaGvrpTransparentSwitching = _AlaGvrpTransparentSwitching_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 36, 1, 1, 2),
    _AlaGvrpTransparentSwitching_Type()
)
alaGvrpTransparentSwitching.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaGvrpTransparentSwitching.setStatus("current")


class _AlaGvrpMaxVlanLimit_Type(Integer32):
    """Custom type alaGvrpMaxVlanLimit based on Integer32"""
    defaultValue = 256

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(32, 4094),
    )


_AlaGvrpMaxVlanLimit_Type.__name__ = "Integer32"
_AlaGvrpMaxVlanLimit_Object = MibScalar
alaGvrpMaxVlanLimit = _AlaGvrpMaxVlanLimit_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 36, 1, 1, 3),
    _AlaGvrpMaxVlanLimit_Type()
)
alaGvrpMaxVlanLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaGvrpMaxVlanLimit.setStatus("current")
_GvrpPortConfig_ObjectIdentity = ObjectIdentity
gvrpPortConfig = _GvrpPortConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 36, 1, 1, 4)
)
_AlaGvrpPortConfigTable_Object = MibTable
alaGvrpPortConfigTable = _AlaGvrpPortConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 36, 1, 1, 4, 1)
)
if mibBuilder.loadTexts:
    alaGvrpPortConfigTable.setStatus("current")
_AlaGvrpPortConfigEntry_Object = MibTableRow
alaGvrpPortConfigEntry = _AlaGvrpPortConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 36, 1, 1, 4, 1, 1)
)
alaGvrpPortConfigEntry.setIndexNames(
    (0, "ALCATEL-IND1-GVRP-MIB", "alaGvrpPortConfigIfIndex"),
)
if mibBuilder.loadTexts:
    alaGvrpPortConfigEntry.setStatus("current")
_AlaGvrpPortConfigIfIndex_Type = InterfaceIndex
_AlaGvrpPortConfigIfIndex_Object = MibTableColumn
alaGvrpPortConfigIfIndex = _AlaGvrpPortConfigIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 36, 1, 1, 4, 1, 1, 1),
    _AlaGvrpPortConfigIfIndex_Type()
)
alaGvrpPortConfigIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaGvrpPortConfigIfIndex.setStatus("current")


class _AlaGvrpPortConfigRegistrarMode_Type(Integer32):
    """Custom type alaGvrpPortConfigRegistrarMode based on Integer32"""
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


_AlaGvrpPortConfigRegistrarMode_Type.__name__ = "Integer32"
_AlaGvrpPortConfigRegistrarMode_Object = MibTableColumn
alaGvrpPortConfigRegistrarMode = _AlaGvrpPortConfigRegistrarMode_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 36, 1, 1, 4, 1, 1, 2),
    _AlaGvrpPortConfigRegistrarMode_Type()
)
alaGvrpPortConfigRegistrarMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaGvrpPortConfigRegistrarMode.setStatus("current")


class _AlaGvrpPortConfigApplicantMode_Type(Integer32):
    """Custom type alaGvrpPortConfigApplicantMode based on Integer32"""
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
        *(("active", 3),
          ("nonparticipant", 2),
          ("participant", 1))
    )


_AlaGvrpPortConfigApplicantMode_Type.__name__ = "Integer32"
_AlaGvrpPortConfigApplicantMode_Object = MibTableColumn
alaGvrpPortConfigApplicantMode = _AlaGvrpPortConfigApplicantMode_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 36, 1, 1, 4, 1, 1, 3),
    _AlaGvrpPortConfigApplicantMode_Type()
)
alaGvrpPortConfigApplicantMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaGvrpPortConfigApplicantMode.setStatus("current")
_AlaGvrpPortConfigRestrictedRegistrationBitmap_Type = VlanBitmap
_AlaGvrpPortConfigRestrictedRegistrationBitmap_Object = MibTableColumn
alaGvrpPortConfigRestrictedRegistrationBitmap = _AlaGvrpPortConfigRestrictedRegistrationBitmap_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 36, 1, 1, 4, 1, 1, 4),
    _AlaGvrpPortConfigRestrictedRegistrationBitmap_Type()
)
alaGvrpPortConfigRestrictedRegistrationBitmap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaGvrpPortConfigRestrictedRegistrationBitmap.setStatus("current")
_AlaGvrpPortConfigAllowRegistrationBitmap_Type = VlanBitmap
_AlaGvrpPortConfigAllowRegistrationBitmap_Object = MibTableColumn
alaGvrpPortConfigAllowRegistrationBitmap = _AlaGvrpPortConfigAllowRegistrationBitmap_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 36, 1, 1, 4, 1, 1, 5),
    _AlaGvrpPortConfigAllowRegistrationBitmap_Type()
)
alaGvrpPortConfigAllowRegistrationBitmap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaGvrpPortConfigAllowRegistrationBitmap.setStatus("current")
_AlaGvrpPortConfigRegistrationBitmap_Type = VlanBitmap
_AlaGvrpPortConfigRegistrationBitmap_Object = MibTableColumn
alaGvrpPortConfigRegistrationBitmap = _AlaGvrpPortConfigRegistrationBitmap_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 36, 1, 1, 4, 1, 1, 6),
    _AlaGvrpPortConfigRegistrationBitmap_Type()
)
alaGvrpPortConfigRegistrationBitmap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaGvrpPortConfigRegistrationBitmap.setStatus("current")
_AlaGvrpPortConfigRestrictedApplicantBitmap_Type = VlanBitmap
_AlaGvrpPortConfigRestrictedApplicantBitmap_Object = MibTableColumn
alaGvrpPortConfigRestrictedApplicantBitmap = _AlaGvrpPortConfigRestrictedApplicantBitmap_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 36, 1, 1, 4, 1, 1, 7),
    _AlaGvrpPortConfigRestrictedApplicantBitmap_Type()
)
alaGvrpPortConfigRestrictedApplicantBitmap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaGvrpPortConfigRestrictedApplicantBitmap.setStatus("current")
_AlaGvrpPortConfigAllowApplicantBitmap_Type = VlanBitmap
_AlaGvrpPortConfigAllowApplicantBitmap_Object = MibTableColumn
alaGvrpPortConfigAllowApplicantBitmap = _AlaGvrpPortConfigAllowApplicantBitmap_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 36, 1, 1, 4, 1, 1, 8),
    _AlaGvrpPortConfigAllowApplicantBitmap_Type()
)
alaGvrpPortConfigAllowApplicantBitmap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaGvrpPortConfigAllowApplicantBitmap.setStatus("current")
_AlaGvrpPortConfigApplicantBitmap_Type = VlanBitmap
_AlaGvrpPortConfigApplicantBitmap_Object = MibTableColumn
alaGvrpPortConfigApplicantBitmap = _AlaGvrpPortConfigApplicantBitmap_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 36, 1, 1, 4, 1, 1, 9),
    _AlaGvrpPortConfigApplicantBitmap_Type()
)
alaGvrpPortConfigApplicantBitmap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaGvrpPortConfigApplicantBitmap.setStatus("current")
_AlaGvrpPortConfigRegistrationToStaticVlanLearn_Type = VlanBitmap
_AlaGvrpPortConfigRegistrationToStaticVlanLearn_Object = MibTableColumn
alaGvrpPortConfigRegistrationToStaticVlanLearn = _AlaGvrpPortConfigRegistrationToStaticVlanLearn_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 36, 1, 1, 4, 1, 1, 10),
    _AlaGvrpPortConfigRegistrationToStaticVlanLearn_Type()
)
alaGvrpPortConfigRegistrationToStaticVlanLearn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaGvrpPortConfigRegistrationToStaticVlanLearn.setStatus("current")
_AlaGvrpPortConfigRegistrationToStaticVlanRestrict_Type = VlanBitmap
_AlaGvrpPortConfigRegistrationToStaticVlanRestrict_Object = MibTableColumn
alaGvrpPortConfigRegistrationToStaticVlanRestrict = _AlaGvrpPortConfigRegistrationToStaticVlanRestrict_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 36, 1, 1, 4, 1, 1, 11),
    _AlaGvrpPortConfigRegistrationToStaticVlanRestrict_Type()
)
alaGvrpPortConfigRegistrationToStaticVlanRestrict.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaGvrpPortConfigRegistrationToStaticVlanRestrict.setStatus("current")
_AlaGvrpPortConfigRegistrationToStaticVlan_Type = VlanBitmap
_AlaGvrpPortConfigRegistrationToStaticVlan_Object = MibTableColumn
alaGvrpPortConfigRegistrationToStaticVlan = _AlaGvrpPortConfigRegistrationToStaticVlan_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 36, 1, 1, 4, 1, 1, 12),
    _AlaGvrpPortConfigRegistrationToStaticVlan_Type()
)
alaGvrpPortConfigRegistrationToStaticVlan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaGvrpPortConfigRegistrationToStaticVlan.setStatus("current")


class _AlaGvrpPortConfigJoinTimer_Type(Unsigned32):
    """Custom type alaGvrpPortConfigJoinTimer based on Unsigned32"""
    defaultValue = 600

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_AlaGvrpPortConfigJoinTimer_Type.__name__ = "Unsigned32"
_AlaGvrpPortConfigJoinTimer_Object = MibTableColumn
alaGvrpPortConfigJoinTimer = _AlaGvrpPortConfigJoinTimer_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 36, 1, 1, 4, 1, 1, 13),
    _AlaGvrpPortConfigJoinTimer_Type()
)
alaGvrpPortConfigJoinTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaGvrpPortConfigJoinTimer.setStatus("current")
if mibBuilder.loadTexts:
    alaGvrpPortConfigJoinTimer.setUnits("milliseconds")


class _AlaGvrpPortConfigLeaveTimer_Type(Unsigned32):
    """Custom type alaGvrpPortConfigLeaveTimer based on Unsigned32"""
    defaultValue = 1800

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(3, 2147483647),
    )


_AlaGvrpPortConfigLeaveTimer_Type.__name__ = "Unsigned32"
_AlaGvrpPortConfigLeaveTimer_Object = MibTableColumn
alaGvrpPortConfigLeaveTimer = _AlaGvrpPortConfigLeaveTimer_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 36, 1, 1, 4, 1, 1, 14),
    _AlaGvrpPortConfigLeaveTimer_Type()
)
alaGvrpPortConfigLeaveTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaGvrpPortConfigLeaveTimer.setStatus("current")
if mibBuilder.loadTexts:
    alaGvrpPortConfigLeaveTimer.setUnits("milliseconds")


class _AlaGvrpPortConfigLeaveAllTimer_Type(Unsigned32):
    """Custom type alaGvrpPortConfigLeaveAllTimer based on Unsigned32"""
    defaultValue = 30000

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(3, 2147483647),
    )


_AlaGvrpPortConfigLeaveAllTimer_Type.__name__ = "Unsigned32"
_AlaGvrpPortConfigLeaveAllTimer_Object = MibTableColumn
alaGvrpPortConfigLeaveAllTimer = _AlaGvrpPortConfigLeaveAllTimer_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 36, 1, 1, 4, 1, 1, 15),
    _AlaGvrpPortConfigLeaveAllTimer_Type()
)
alaGvrpPortConfigLeaveAllTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaGvrpPortConfigLeaveAllTimer.setStatus("current")
if mibBuilder.loadTexts:
    alaGvrpPortConfigLeaveAllTimer.setUnits("milliseconds")


class _AlaGvrpPortConfigProviderBpduMac_Type(Integer32):
    """Custom type alaGvrpPortConfigProviderBpduMac based on Integer32"""
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


_AlaGvrpPortConfigProviderBpduMac_Type.__name__ = "Integer32"
_AlaGvrpPortConfigProviderBpduMac_Object = MibTableColumn
alaGvrpPortConfigProviderBpduMac = _AlaGvrpPortConfigProviderBpduMac_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 36, 1, 1, 4, 1, 1, 16),
    _AlaGvrpPortConfigProviderBpduMac_Type()
)
alaGvrpPortConfigProviderBpduMac.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaGvrpPortConfigProviderBpduMac.setStatus("current")
_GvrpPortStats_ObjectIdentity = ObjectIdentity
gvrpPortStats = _GvrpPortStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 36, 1, 1, 5)
)
_AlaGvrpPortStatsTable_Object = MibTable
alaGvrpPortStatsTable = _AlaGvrpPortStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 36, 1, 1, 5, 1)
)
if mibBuilder.loadTexts:
    alaGvrpPortStatsTable.setStatus("current")
_AlaGvrpPortStatsEntry_Object = MibTableRow
alaGvrpPortStatsEntry = _AlaGvrpPortStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 36, 1, 1, 5, 1, 1)
)
alaGvrpPortStatsEntry.setIndexNames(
    (0, "ALCATEL-IND1-GVRP-MIB", "alaGvrpPortStatsIfIndex"),
)
if mibBuilder.loadTexts:
    alaGvrpPortStatsEntry.setStatus("current")
_AlaGvrpPortStatsIfIndex_Type = InterfaceIndex
_AlaGvrpPortStatsIfIndex_Object = MibTableColumn
alaGvrpPortStatsIfIndex = _AlaGvrpPortStatsIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 36, 1, 1, 5, 1, 1, 1),
    _AlaGvrpPortStatsIfIndex_Type()
)
alaGvrpPortStatsIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaGvrpPortStatsIfIndex.setStatus("current")
_AlaGvrpPortStatsJoinEmptyReceived_Type = Counter32
_AlaGvrpPortStatsJoinEmptyReceived_Object = MibTableColumn
alaGvrpPortStatsJoinEmptyReceived = _AlaGvrpPortStatsJoinEmptyReceived_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 36, 1, 1, 5, 1, 1, 2),
    _AlaGvrpPortStatsJoinEmptyReceived_Type()
)
alaGvrpPortStatsJoinEmptyReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaGvrpPortStatsJoinEmptyReceived.setStatus("current")
_AlaGvrpPortStatsJoinInReceived_Type = Counter32
_AlaGvrpPortStatsJoinInReceived_Object = MibTableColumn
alaGvrpPortStatsJoinInReceived = _AlaGvrpPortStatsJoinInReceived_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 36, 1, 1, 5, 1, 1, 3),
    _AlaGvrpPortStatsJoinInReceived_Type()
)
alaGvrpPortStatsJoinInReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaGvrpPortStatsJoinInReceived.setStatus("current")
_AlaGvrpPortStatsEmptyReceived_Type = Counter32
_AlaGvrpPortStatsEmptyReceived_Object = MibTableColumn
alaGvrpPortStatsEmptyReceived = _AlaGvrpPortStatsEmptyReceived_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 36, 1, 1, 5, 1, 1, 4),
    _AlaGvrpPortStatsEmptyReceived_Type()
)
alaGvrpPortStatsEmptyReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaGvrpPortStatsEmptyReceived.setStatus("current")
_AlaGvrpPortStatsLeaveInReceived_Type = Counter32
_AlaGvrpPortStatsLeaveInReceived_Object = MibTableColumn
alaGvrpPortStatsLeaveInReceived = _AlaGvrpPortStatsLeaveInReceived_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 36, 1, 1, 5, 1, 1, 5),
    _AlaGvrpPortStatsLeaveInReceived_Type()
)
alaGvrpPortStatsLeaveInReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaGvrpPortStatsLeaveInReceived.setStatus("current")
_AlaGvrpPortStatsLeaveEmptyReceived_Type = Counter32
_AlaGvrpPortStatsLeaveEmptyReceived_Object = MibTableColumn
alaGvrpPortStatsLeaveEmptyReceived = _AlaGvrpPortStatsLeaveEmptyReceived_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 36, 1, 1, 5, 1, 1, 6),
    _AlaGvrpPortStatsLeaveEmptyReceived_Type()
)
alaGvrpPortStatsLeaveEmptyReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaGvrpPortStatsLeaveEmptyReceived.setStatus("current")
_AlaGvrpPortStatsLeaveAllReceived_Type = Counter32
_AlaGvrpPortStatsLeaveAllReceived_Object = MibTableColumn
alaGvrpPortStatsLeaveAllReceived = _AlaGvrpPortStatsLeaveAllReceived_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 36, 1, 1, 5, 1, 1, 7),
    _AlaGvrpPortStatsLeaveAllReceived_Type()
)
alaGvrpPortStatsLeaveAllReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaGvrpPortStatsLeaveAllReceived.setStatus("current")
_AlaGvrpPortStatsJoinEmptyTransmitted_Type = Counter32
_AlaGvrpPortStatsJoinEmptyTransmitted_Object = MibTableColumn
alaGvrpPortStatsJoinEmptyTransmitted = _AlaGvrpPortStatsJoinEmptyTransmitted_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 36, 1, 1, 5, 1, 1, 8),
    _AlaGvrpPortStatsJoinEmptyTransmitted_Type()
)
alaGvrpPortStatsJoinEmptyTransmitted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaGvrpPortStatsJoinEmptyTransmitted.setStatus("current")
_AlaGvrpPortStatsJoinInTransmitted_Type = Counter32
_AlaGvrpPortStatsJoinInTransmitted_Object = MibTableColumn
alaGvrpPortStatsJoinInTransmitted = _AlaGvrpPortStatsJoinInTransmitted_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 36, 1, 1, 5, 1, 1, 9),
    _AlaGvrpPortStatsJoinInTransmitted_Type()
)
alaGvrpPortStatsJoinInTransmitted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaGvrpPortStatsJoinInTransmitted.setStatus("current")
_AlaGvrpPortStatsEmptyTransmitted_Type = Counter32
_AlaGvrpPortStatsEmptyTransmitted_Object = MibTableColumn
alaGvrpPortStatsEmptyTransmitted = _AlaGvrpPortStatsEmptyTransmitted_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 36, 1, 1, 5, 1, 1, 10),
    _AlaGvrpPortStatsEmptyTransmitted_Type()
)
alaGvrpPortStatsEmptyTransmitted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaGvrpPortStatsEmptyTransmitted.setStatus("current")
_AlaGvrpPortStatsLeaveInTransmitted_Type = Counter32
_AlaGvrpPortStatsLeaveInTransmitted_Object = MibTableColumn
alaGvrpPortStatsLeaveInTransmitted = _AlaGvrpPortStatsLeaveInTransmitted_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 36, 1, 1, 5, 1, 1, 11),
    _AlaGvrpPortStatsLeaveInTransmitted_Type()
)
alaGvrpPortStatsLeaveInTransmitted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaGvrpPortStatsLeaveInTransmitted.setStatus("current")
_AlaGvrpPortStatsLeaveEmptyTransmitted_Type = Counter32
_AlaGvrpPortStatsLeaveEmptyTransmitted_Object = MibTableColumn
alaGvrpPortStatsLeaveEmptyTransmitted = _AlaGvrpPortStatsLeaveEmptyTransmitted_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 36, 1, 1, 5, 1, 1, 12),
    _AlaGvrpPortStatsLeaveEmptyTransmitted_Type()
)
alaGvrpPortStatsLeaveEmptyTransmitted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaGvrpPortStatsLeaveEmptyTransmitted.setStatus("current")
_AlaGvrpPortStatsLeaveAllTransmitted_Type = Counter32
_AlaGvrpPortStatsLeaveAllTransmitted_Object = MibTableColumn
alaGvrpPortStatsLeaveAllTransmitted = _AlaGvrpPortStatsLeaveAllTransmitted_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 36, 1, 1, 5, 1, 1, 13),
    _AlaGvrpPortStatsLeaveAllTransmitted_Type()
)
alaGvrpPortStatsLeaveAllTransmitted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaGvrpPortStatsLeaveAllTransmitted.setStatus("current")
_AlaGvrpPortStatsTotalPDUReceived_Type = Counter32
_AlaGvrpPortStatsTotalPDUReceived_Object = MibTableColumn
alaGvrpPortStatsTotalPDUReceived = _AlaGvrpPortStatsTotalPDUReceived_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 36, 1, 1, 5, 1, 1, 14),
    _AlaGvrpPortStatsTotalPDUReceived_Type()
)
alaGvrpPortStatsTotalPDUReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaGvrpPortStatsTotalPDUReceived.setStatus("current")
_AlaGvrpPortStatsTotalPDUTransmitted_Type = Counter32
_AlaGvrpPortStatsTotalPDUTransmitted_Object = MibTableColumn
alaGvrpPortStatsTotalPDUTransmitted = _AlaGvrpPortStatsTotalPDUTransmitted_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 36, 1, 1, 5, 1, 1, 15),
    _AlaGvrpPortStatsTotalPDUTransmitted_Type()
)
alaGvrpPortStatsTotalPDUTransmitted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaGvrpPortStatsTotalPDUTransmitted.setStatus("current")
_AlaGvrpPortStatsTotalMsgsReceived_Type = Counter32
_AlaGvrpPortStatsTotalMsgsReceived_Object = MibTableColumn
alaGvrpPortStatsTotalMsgsReceived = _AlaGvrpPortStatsTotalMsgsReceived_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 36, 1, 1, 5, 1, 1, 16),
    _AlaGvrpPortStatsTotalMsgsReceived_Type()
)
alaGvrpPortStatsTotalMsgsReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaGvrpPortStatsTotalMsgsReceived.setStatus("current")
_AlaGvrpPortStatsTotalMsgsTransmitted_Type = Counter32
_AlaGvrpPortStatsTotalMsgsTransmitted_Object = MibTableColumn
alaGvrpPortStatsTotalMsgsTransmitted = _AlaGvrpPortStatsTotalMsgsTransmitted_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 36, 1, 1, 5, 1, 1, 17),
    _AlaGvrpPortStatsTotalMsgsTransmitted_Type()
)
alaGvrpPortStatsTotalMsgsTransmitted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaGvrpPortStatsTotalMsgsTransmitted.setStatus("current")
_AlaGvrpPortStatsInvalidMsgsReceived_Type = Counter32
_AlaGvrpPortStatsInvalidMsgsReceived_Object = MibTableColumn
alaGvrpPortStatsInvalidMsgsReceived = _AlaGvrpPortStatsInvalidMsgsReceived_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 36, 1, 1, 5, 1, 1, 18),
    _AlaGvrpPortStatsInvalidMsgsReceived_Type()
)
alaGvrpPortStatsInvalidMsgsReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaGvrpPortStatsInvalidMsgsReceived.setStatus("current")


class _AlaGvrpPortStatsClearStats_Type(Integer32):
    """Custom type alaGvrpPortStatsClearStats based on Integer32"""
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


_AlaGvrpPortStatsClearStats_Type.__name__ = "Integer32"
_AlaGvrpPortStatsClearStats_Object = MibTableColumn
alaGvrpPortStatsClearStats = _AlaGvrpPortStatsClearStats_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 36, 1, 1, 5, 1, 1, 19),
    _AlaGvrpPortStatsClearStats_Type()
)
alaGvrpPortStatsClearStats.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaGvrpPortStatsClearStats.setStatus("current")
_AlcatelIND1GVRPMIBConformance_ObjectIdentity = ObjectIdentity
alcatelIND1GVRPMIBConformance = _AlcatelIND1GVRPMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 36, 1, 2)
)
if mibBuilder.loadTexts:
    alcatelIND1GVRPMIBConformance.setStatus("current")
_AlcatelIND1GVRPMIBGroups_ObjectIdentity = ObjectIdentity
alcatelIND1GVRPMIBGroups = _AlcatelIND1GVRPMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 36, 1, 2, 1)
)
if mibBuilder.loadTexts:
    alcatelIND1GVRPMIBGroups.setStatus("current")
_AlcatelIND1GVRPMIBCompliances_ObjectIdentity = ObjectIdentity
alcatelIND1GVRPMIBCompliances = _AlcatelIND1GVRPMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 36, 1, 2, 2)
)
if mibBuilder.loadTexts:
    alcatelIND1GVRPMIBCompliances.setStatus("current")

# Managed Objects groups

gvrpPortBaseGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 36, 1, 2, 1, 1)
)
gvrpPortBaseGroup.setObjects(
      *(("ALCATEL-IND1-GVRP-MIB", "alaGvrpGlobalClearStats"),
        ("ALCATEL-IND1-GVRP-MIB", "alaGvrpTransparentSwitching"),
        ("ALCATEL-IND1-GVRP-MIB", "alaGvrpMaxVlanLimit"))
)
if mibBuilder.loadTexts:
    gvrpPortBaseGroup.setStatus("current")

gvrpPortConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 36, 1, 2, 1, 2)
)
gvrpPortConfigGroup.setObjects(
      *(("ALCATEL-IND1-GVRP-MIB", "alaGvrpPortConfigRegistrarMode"),
        ("ALCATEL-IND1-GVRP-MIB", "alaGvrpPortConfigApplicantMode"),
        ("ALCATEL-IND1-GVRP-MIB", "alaGvrpPortConfigRestrictedRegistrationBitmap"),
        ("ALCATEL-IND1-GVRP-MIB", "alaGvrpPortConfigAllowRegistrationBitmap"),
        ("ALCATEL-IND1-GVRP-MIB", "alaGvrpPortConfigRegistrationBitmap"),
        ("ALCATEL-IND1-GVRP-MIB", "alaGvrpPortConfigRestrictedApplicantBitmap"),
        ("ALCATEL-IND1-GVRP-MIB", "alaGvrpPortConfigAllowApplicantBitmap"),
        ("ALCATEL-IND1-GVRP-MIB", "alaGvrpPortConfigApplicantBitmap"),
        ("ALCATEL-IND1-GVRP-MIB", "alaGvrpPortConfigRegistrationToStaticVlanLearn"),
        ("ALCATEL-IND1-GVRP-MIB", "alaGvrpPortConfigRegistrationToStaticVlanRestrict"),
        ("ALCATEL-IND1-GVRP-MIB", "alaGvrpPortConfigRegistrationToStaticVlan"),
        ("ALCATEL-IND1-GVRP-MIB", "alaGvrpPortConfigJoinTimer"),
        ("ALCATEL-IND1-GVRP-MIB", "alaGvrpPortConfigLeaveTimer"),
        ("ALCATEL-IND1-GVRP-MIB", "alaGvrpPortConfigLeaveAllTimer"),
        ("ALCATEL-IND1-GVRP-MIB", "alaGvrpPortConfigProviderBpduMac"))
)
if mibBuilder.loadTexts:
    gvrpPortConfigGroup.setStatus("current")

gvrpPortStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 36, 1, 2, 1, 3)
)
gvrpPortStatsGroup.setObjects(
      *(("ALCATEL-IND1-GVRP-MIB", "alaGvrpPortStatsJoinEmptyReceived"),
        ("ALCATEL-IND1-GVRP-MIB", "alaGvrpPortStatsJoinInReceived"),
        ("ALCATEL-IND1-GVRP-MIB", "alaGvrpPortStatsEmptyReceived"),
        ("ALCATEL-IND1-GVRP-MIB", "alaGvrpPortStatsLeaveInReceived"),
        ("ALCATEL-IND1-GVRP-MIB", "alaGvrpPortStatsLeaveEmptyReceived"),
        ("ALCATEL-IND1-GVRP-MIB", "alaGvrpPortStatsLeaveAllReceived"),
        ("ALCATEL-IND1-GVRP-MIB", "alaGvrpPortStatsJoinEmptyTransmitted"),
        ("ALCATEL-IND1-GVRP-MIB", "alaGvrpPortStatsJoinInTransmitted"),
        ("ALCATEL-IND1-GVRP-MIB", "alaGvrpPortStatsEmptyTransmitted"),
        ("ALCATEL-IND1-GVRP-MIB", "alaGvrpPortStatsLeaveInTransmitted"),
        ("ALCATEL-IND1-GVRP-MIB", "alaGvrpPortStatsLeaveEmptyTransmitted"),
        ("ALCATEL-IND1-GVRP-MIB", "alaGvrpPortStatsLeaveAllTransmitted"),
        ("ALCATEL-IND1-GVRP-MIB", "alaGvrpPortStatsTotalPDUReceived"),
        ("ALCATEL-IND1-GVRP-MIB", "alaGvrpPortStatsTotalPDUTransmitted"),
        ("ALCATEL-IND1-GVRP-MIB", "alaGvrpPortStatsTotalMsgsReceived"),
        ("ALCATEL-IND1-GVRP-MIB", "alaGvrpPortStatsTotalMsgsTransmitted"),
        ("ALCATEL-IND1-GVRP-MIB", "alaGvrpPortStatsInvalidMsgsReceived"),
        ("ALCATEL-IND1-GVRP-MIB", "alaGvrpPortStatsClearStats"))
)
if mibBuilder.loadTexts:
    gvrpPortStatsGroup.setStatus("current")


# Notification objects

gvrpVlanLimitReachedEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 36, 1, 0, 1)
)
gvrpVlanLimitReachedEvent.setObjects(
    ("ALCATEL-IND1-GVRP-MIB", "alaGvrpMaxVlanLimit")
)
if mibBuilder.loadTexts:
    gvrpVlanLimitReachedEvent.setStatus(
        "current"
    )


# Notifications groups

gvrpNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 36, 1, 2, 1, 4)
)
gvrpNotificationGroup.setObjects(
    ("ALCATEL-IND1-GVRP-MIB", "gvrpVlanLimitReachedEvent")
)
if mibBuilder.loadTexts:
    gvrpNotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

alcatelIND1GVRPMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 36, 1, 2, 2, 1)
)
if mibBuilder.loadTexts:
    alcatelIND1GVRPMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ALCATEL-IND1-GVRP-MIB",
    **{"alcatelIND1GVRPMIB": alcatelIND1GVRPMIB,
       "alcatelIND1GVRPMIBNotifications": alcatelIND1GVRPMIBNotifications,
       "gvrpVlanLimitReachedEvent": gvrpVlanLimitReachedEvent,
       "alcatelIND1GVRPMIBObjects": alcatelIND1GVRPMIBObjects,
       "alaGvrpGlobalClearStats": alaGvrpGlobalClearStats,
       "alaGvrpTransparentSwitching": alaGvrpTransparentSwitching,
       "alaGvrpMaxVlanLimit": alaGvrpMaxVlanLimit,
       "gvrpPortConfig": gvrpPortConfig,
       "alaGvrpPortConfigTable": alaGvrpPortConfigTable,
       "alaGvrpPortConfigEntry": alaGvrpPortConfigEntry,
       "alaGvrpPortConfigIfIndex": alaGvrpPortConfigIfIndex,
       "alaGvrpPortConfigRegistrarMode": alaGvrpPortConfigRegistrarMode,
       "alaGvrpPortConfigApplicantMode": alaGvrpPortConfigApplicantMode,
       "alaGvrpPortConfigRestrictedRegistrationBitmap": alaGvrpPortConfigRestrictedRegistrationBitmap,
       "alaGvrpPortConfigAllowRegistrationBitmap": alaGvrpPortConfigAllowRegistrationBitmap,
       "alaGvrpPortConfigRegistrationBitmap": alaGvrpPortConfigRegistrationBitmap,
       "alaGvrpPortConfigRestrictedApplicantBitmap": alaGvrpPortConfigRestrictedApplicantBitmap,
       "alaGvrpPortConfigAllowApplicantBitmap": alaGvrpPortConfigAllowApplicantBitmap,
       "alaGvrpPortConfigApplicantBitmap": alaGvrpPortConfigApplicantBitmap,
       "alaGvrpPortConfigRegistrationToStaticVlanLearn": alaGvrpPortConfigRegistrationToStaticVlanLearn,
       "alaGvrpPortConfigRegistrationToStaticVlanRestrict": alaGvrpPortConfigRegistrationToStaticVlanRestrict,
       "alaGvrpPortConfigRegistrationToStaticVlan": alaGvrpPortConfigRegistrationToStaticVlan,
       "alaGvrpPortConfigJoinTimer": alaGvrpPortConfigJoinTimer,
       "alaGvrpPortConfigLeaveTimer": alaGvrpPortConfigLeaveTimer,
       "alaGvrpPortConfigLeaveAllTimer": alaGvrpPortConfigLeaveAllTimer,
       "alaGvrpPortConfigProviderBpduMac": alaGvrpPortConfigProviderBpduMac,
       "gvrpPortStats": gvrpPortStats,
       "alaGvrpPortStatsTable": alaGvrpPortStatsTable,
       "alaGvrpPortStatsEntry": alaGvrpPortStatsEntry,
       "alaGvrpPortStatsIfIndex": alaGvrpPortStatsIfIndex,
       "alaGvrpPortStatsJoinEmptyReceived": alaGvrpPortStatsJoinEmptyReceived,
       "alaGvrpPortStatsJoinInReceived": alaGvrpPortStatsJoinInReceived,
       "alaGvrpPortStatsEmptyReceived": alaGvrpPortStatsEmptyReceived,
       "alaGvrpPortStatsLeaveInReceived": alaGvrpPortStatsLeaveInReceived,
       "alaGvrpPortStatsLeaveEmptyReceived": alaGvrpPortStatsLeaveEmptyReceived,
       "alaGvrpPortStatsLeaveAllReceived": alaGvrpPortStatsLeaveAllReceived,
       "alaGvrpPortStatsJoinEmptyTransmitted": alaGvrpPortStatsJoinEmptyTransmitted,
       "alaGvrpPortStatsJoinInTransmitted": alaGvrpPortStatsJoinInTransmitted,
       "alaGvrpPortStatsEmptyTransmitted": alaGvrpPortStatsEmptyTransmitted,
       "alaGvrpPortStatsLeaveInTransmitted": alaGvrpPortStatsLeaveInTransmitted,
       "alaGvrpPortStatsLeaveEmptyTransmitted": alaGvrpPortStatsLeaveEmptyTransmitted,
       "alaGvrpPortStatsLeaveAllTransmitted": alaGvrpPortStatsLeaveAllTransmitted,
       "alaGvrpPortStatsTotalPDUReceived": alaGvrpPortStatsTotalPDUReceived,
       "alaGvrpPortStatsTotalPDUTransmitted": alaGvrpPortStatsTotalPDUTransmitted,
       "alaGvrpPortStatsTotalMsgsReceived": alaGvrpPortStatsTotalMsgsReceived,
       "alaGvrpPortStatsTotalMsgsTransmitted": alaGvrpPortStatsTotalMsgsTransmitted,
       "alaGvrpPortStatsInvalidMsgsReceived": alaGvrpPortStatsInvalidMsgsReceived,
       "alaGvrpPortStatsClearStats": alaGvrpPortStatsClearStats,
       "alcatelIND1GVRPMIBConformance": alcatelIND1GVRPMIBConformance,
       "alcatelIND1GVRPMIBGroups": alcatelIND1GVRPMIBGroups,
       "gvrpPortBaseGroup": gvrpPortBaseGroup,
       "gvrpPortConfigGroup": gvrpPortConfigGroup,
       "gvrpPortStatsGroup": gvrpPortStatsGroup,
       "gvrpNotificationGroup": gvrpNotificationGroup,
       "alcatelIND1GVRPMIBCompliances": alcatelIND1GVRPMIBCompliances,
       "alcatelIND1GVRPMIBCompliance": alcatelIND1GVRPMIBCompliance}
)
