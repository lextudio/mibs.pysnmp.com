# SNMP MIB module (Juniper-ATM-1483-Profile-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/Juniper-ATM-1483-Profile-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:14:39 2024
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

(juniMibs,) = mibBuilder.importSymbols(
    "Juniper-MIBs",
    "juniMibs")

(JuniProfileIfEncaps,) = mibBuilder.importSymbols(
    "Juniper-PROFILE-MIB",
    "JuniProfileIfEncaps")

(JuniEnable,
 JuniSetMap) = mibBuilder.importSymbols(
    "Juniper-TC",
    "JuniEnable",
    "JuniSetMap")

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

juniAtm1483ProfileMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 58)
)
juniAtm1483ProfileMIB.setRevisions(
        ("2005-11-18 14:07",
         "2004-11-02 21:07",
         "2004-11-02 21:07",
         "2004-11-02 21:07")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_JuniAtm1483ProfileObjects_ObjectIdentity = ObjectIdentity
juniAtm1483ProfileObjects = _JuniAtm1483ProfileObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 58, 1)
)
_JuniAtm1483Profile_ObjectIdentity = ObjectIdentity
juniAtm1483Profile = _JuniAtm1483Profile_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 58, 1, 1)
)
_JuniAtm1483ProfileTable_Object = MibTable
juniAtm1483ProfileTable = _JuniAtm1483ProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 58, 1, 1, 1)
)
if mibBuilder.loadTexts:
    juniAtm1483ProfileTable.setStatus("current")
_JuniAtm1483ProfileEntry_Object = MibTableRow
juniAtm1483ProfileEntry = _JuniAtm1483ProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 58, 1, 1, 1, 1)
)
juniAtm1483ProfileEntry.setIndexNames(
    (0, "Juniper-ATM-1483-Profile-MIB", "juniAtm1483ProfileId"),
)
if mibBuilder.loadTexts:
    juniAtm1483ProfileEntry.setStatus("current")
_JuniAtm1483ProfileId_Type = Unsigned32
_JuniAtm1483ProfileId_Object = MibTableColumn
juniAtm1483ProfileId = _JuniAtm1483ProfileId_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 58, 1, 1, 1, 1, 1),
    _JuniAtm1483ProfileId_Type()
)
juniAtm1483ProfileId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    juniAtm1483ProfileId.setStatus("current")
_JuniAtm1483ProfileSetMap_Type = JuniSetMap
_JuniAtm1483ProfileSetMap_Object = MibTableColumn
juniAtm1483ProfileSetMap = _JuniAtm1483ProfileSetMap_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 58, 1, 1, 1, 1, 2),
    _JuniAtm1483ProfileSetMap_Type()
)
juniAtm1483ProfileSetMap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniAtm1483ProfileSetMap.setStatus("current")


class _JuniAtm1483ProfileVccType_Type(Integer32):
    """Custom type juniAtm1483ProfileVccType based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("autoconfig", 2),
          ("rfc1483Llc", 1),
          ("rfc1483VcMux", 0))
    )


_JuniAtm1483ProfileVccType_Type.__name__ = "Integer32"
_JuniAtm1483ProfileVccType_Object = MibTableColumn
juniAtm1483ProfileVccType = _JuniAtm1483ProfileVccType_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 58, 1, 1, 1, 1, 3),
    _JuniAtm1483ProfileVccType_Type()
)
juniAtm1483ProfileVccType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniAtm1483ProfileVccType.setStatus("current")


class _JuniAtm1483ProfileVccServiceCategory_Type(Integer32):
    """Custom type juniAtm1483ProfileVccServiceCategory based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("cbr", 3),
          ("nrtVbr", 2),
          ("rtVbr", 4),
          ("ubr", 0),
          ("ubrPcr", 1))
    )


_JuniAtm1483ProfileVccServiceCategory_Type.__name__ = "Integer32"
_JuniAtm1483ProfileVccServiceCategory_Object = MibTableColumn
juniAtm1483ProfileVccServiceCategory = _JuniAtm1483ProfileVccServiceCategory_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 58, 1, 1, 1, 1, 4),
    _JuniAtm1483ProfileVccServiceCategory_Type()
)
juniAtm1483ProfileVccServiceCategory.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniAtm1483ProfileVccServiceCategory.setStatus("current")


class _JuniAtm1483ProfileVccPcr_Type(Gauge32):
    """Custom type juniAtm1483ProfileVccPcr based on Gauge32"""
    defaultValue = 0


_JuniAtm1483ProfileVccPcr_Object = MibTableColumn
juniAtm1483ProfileVccPcr = _JuniAtm1483ProfileVccPcr_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 58, 1, 1, 1, 1, 5),
    _JuniAtm1483ProfileVccPcr_Type()
)
juniAtm1483ProfileVccPcr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniAtm1483ProfileVccPcr.setStatus("current")
if mibBuilder.loadTexts:
    juniAtm1483ProfileVccPcr.setUnits("kilo-bits per second")


class _JuniAtm1483ProfileVccScr_Type(Gauge32):
    """Custom type juniAtm1483ProfileVccScr based on Gauge32"""
    defaultValue = 0


_JuniAtm1483ProfileVccScr_Object = MibTableColumn
juniAtm1483ProfileVccScr = _JuniAtm1483ProfileVccScr_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 58, 1, 1, 1, 1, 6),
    _JuniAtm1483ProfileVccScr_Type()
)
juniAtm1483ProfileVccScr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniAtm1483ProfileVccScr.setStatus("current")
if mibBuilder.loadTexts:
    juniAtm1483ProfileVccScr.setUnits("kilo-bits per second")


class _JuniAtm1483ProfileVccMbs_Type(Gauge32):
    """Custom type juniAtm1483ProfileVccMbs based on Gauge32"""
    defaultValue = 0


_JuniAtm1483ProfileVccMbs_Object = MibTableColumn
juniAtm1483ProfileVccMbs = _JuniAtm1483ProfileVccMbs_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 58, 1, 1, 1, 1, 7),
    _JuniAtm1483ProfileVccMbs_Type()
)
juniAtm1483ProfileVccMbs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniAtm1483ProfileVccMbs.setStatus("current")
if mibBuilder.loadTexts:
    juniAtm1483ProfileVccMbs.setUnits("cells")


class _JuniAtm1483ProfileIfAlias_Type(DisplayString):
    """Custom type juniAtm1483ProfileIfAlias based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_JuniAtm1483ProfileIfAlias_Type.__name__ = "DisplayString"
_JuniAtm1483ProfileIfAlias_Object = MibTableColumn
juniAtm1483ProfileIfAlias = _JuniAtm1483ProfileIfAlias_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 58, 1, 1, 1, 1, 8),
    _JuniAtm1483ProfileIfAlias_Type()
)
juniAtm1483ProfileIfAlias.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniAtm1483ProfileIfAlias.setStatus("current")


class _JuniAtm1483ProfileAdvisoryRxSpeed_Type(Integer32):
    """Custom type juniAtm1483ProfileAdvisoryRxSpeed based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_JuniAtm1483ProfileAdvisoryRxSpeed_Type.__name__ = "Integer32"
_JuniAtm1483ProfileAdvisoryRxSpeed_Object = MibTableColumn
juniAtm1483ProfileAdvisoryRxSpeed = _JuniAtm1483ProfileAdvisoryRxSpeed_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 58, 1, 1, 1, 1, 9),
    _JuniAtm1483ProfileAdvisoryRxSpeed_Type()
)
juniAtm1483ProfileAdvisoryRxSpeed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniAtm1483ProfileAdvisoryRxSpeed.setStatus("current")
if mibBuilder.loadTexts:
    juniAtm1483ProfileAdvisoryRxSpeed.setUnits("kilo-bits per second")


class _JuniAtm1483ProfileVccOamAdminStatus_Type(Integer32):
    """Custom type juniAtm1483ProfileVccOamAdminStatus based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("oamAdminStateDisabled", 1),
          ("oamAdminStateEnabled", 2))
    )


_JuniAtm1483ProfileVccOamAdminStatus_Type.__name__ = "Integer32"
_JuniAtm1483ProfileVccOamAdminStatus_Object = MibTableColumn
juniAtm1483ProfileVccOamAdminStatus = _JuniAtm1483ProfileVccOamAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 58, 1, 1, 1, 1, 10),
    _JuniAtm1483ProfileVccOamAdminStatus_Type()
)
juniAtm1483ProfileVccOamAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniAtm1483ProfileVccOamAdminStatus.setStatus("current")


class _JuniAtm1483ProfileVccOamLoopbackFrequency_Type(Unsigned32):
    """Custom type juniAtm1483ProfileVccOamLoopbackFrequency based on Unsigned32"""
    defaultValue = 10

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 600),
    )


_JuniAtm1483ProfileVccOamLoopbackFrequency_Type.__name__ = "Unsigned32"
_JuniAtm1483ProfileVccOamLoopbackFrequency_Object = MibTableColumn
juniAtm1483ProfileVccOamLoopbackFrequency = _JuniAtm1483ProfileVccOamLoopbackFrequency_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 58, 1, 1, 1, 1, 11),
    _JuniAtm1483ProfileVccOamLoopbackFrequency_Type()
)
juniAtm1483ProfileVccOamLoopbackFrequency.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniAtm1483ProfileVccOamLoopbackFrequency.setStatus("current")
if mibBuilder.loadTexts:
    juniAtm1483ProfileVccOamLoopbackFrequency.setUnits("seconds")


class _JuniAtm1483ProfileVcClassName_Type(DisplayString):
    """Custom type juniAtm1483ProfileVcClassName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_JuniAtm1483ProfileVcClassName_Type.__name__ = "DisplayString"
_JuniAtm1483ProfileVcClassName_Object = MibTableColumn
juniAtm1483ProfileVcClassName = _JuniAtm1483ProfileVcClassName_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 58, 1, 1, 1, 1, 12),
    _JuniAtm1483ProfileVcClassName_Type()
)
juniAtm1483ProfileVcClassName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniAtm1483ProfileVcClassName.setStatus("current")
_JuniAtm1483ProfileAutoConfTable_Object = MibTable
juniAtm1483ProfileAutoConfTable = _JuniAtm1483ProfileAutoConfTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 58, 1, 1, 2)
)
if mibBuilder.loadTexts:
    juniAtm1483ProfileAutoConfTable.setStatus("current")
_JuniAtm1483ProfileAutoConfEntry_Object = MibTableRow
juniAtm1483ProfileAutoConfEntry = _JuniAtm1483ProfileAutoConfEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 58, 1, 1, 2, 1)
)
juniAtm1483ProfileAutoConfEntry.setIndexNames(
    (0, "Juniper-ATM-1483-Profile-MIB", "juniAtm1483ProfileAutoConfId"),
    (0, "Juniper-ATM-1483-Profile-MIB", "juniAtm1483ProfileAutoConfEncaps"),
)
if mibBuilder.loadTexts:
    juniAtm1483ProfileAutoConfEntry.setStatus("current")
_JuniAtm1483ProfileAutoConfId_Type = Unsigned32
_JuniAtm1483ProfileAutoConfId_Object = MibTableColumn
juniAtm1483ProfileAutoConfId = _JuniAtm1483ProfileAutoConfId_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 58, 1, 1, 2, 1, 1),
    _JuniAtm1483ProfileAutoConfId_Type()
)
juniAtm1483ProfileAutoConfId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    juniAtm1483ProfileAutoConfId.setStatus("current")
_JuniAtm1483ProfileAutoConfEncaps_Type = JuniProfileIfEncaps
_JuniAtm1483ProfileAutoConfEncaps_Object = MibTableColumn
juniAtm1483ProfileAutoConfEncaps = _JuniAtm1483ProfileAutoConfEncaps_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 58, 1, 1, 2, 1, 2),
    _JuniAtm1483ProfileAutoConfEncaps_Type()
)
juniAtm1483ProfileAutoConfEncaps.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    juniAtm1483ProfileAutoConfEncaps.setStatus("current")
_JuniAtm1483ProfileAutoConfEnable_Type = JuniEnable
_JuniAtm1483ProfileAutoConfEnable_Object = MibTableColumn
juniAtm1483ProfileAutoConfEnable = _JuniAtm1483ProfileAutoConfEnable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 58, 1, 1, 2, 1, 3),
    _JuniAtm1483ProfileAutoConfEnable_Type()
)
juniAtm1483ProfileAutoConfEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniAtm1483ProfileAutoConfEnable.setStatus("current")


class _JuniAtm1483ProfileAutoConfLockoutMin_Type(Integer32):
    """Custom type juniAtm1483ProfileAutoConfLockoutMin based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 86400),
    )


_JuniAtm1483ProfileAutoConfLockoutMin_Type.__name__ = "Integer32"
_JuniAtm1483ProfileAutoConfLockoutMin_Object = MibTableColumn
juniAtm1483ProfileAutoConfLockoutMin = _JuniAtm1483ProfileAutoConfLockoutMin_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 58, 1, 1, 2, 1, 4),
    _JuniAtm1483ProfileAutoConfLockoutMin_Type()
)
juniAtm1483ProfileAutoConfLockoutMin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniAtm1483ProfileAutoConfLockoutMin.setStatus("current")


class _JuniAtm1483ProfileAutoConfLockoutMax_Type(Integer32):
    """Custom type juniAtm1483ProfileAutoConfLockoutMax based on Integer32"""
    defaultValue = 300

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 86400),
    )


_JuniAtm1483ProfileAutoConfLockoutMax_Type.__name__ = "Integer32"
_JuniAtm1483ProfileAutoConfLockoutMax_Object = MibTableColumn
juniAtm1483ProfileAutoConfLockoutMax = _JuniAtm1483ProfileAutoConfLockoutMax_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 58, 1, 1, 2, 1, 5),
    _JuniAtm1483ProfileAutoConfLockoutMax_Type()
)
juniAtm1483ProfileAutoConfLockoutMax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniAtm1483ProfileAutoConfLockoutMax.setStatus("current")
_JuniAtm1483ProfileNestedProfileTable_Object = MibTable
juniAtm1483ProfileNestedProfileTable = _JuniAtm1483ProfileNestedProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 58, 1, 1, 3)
)
if mibBuilder.loadTexts:
    juniAtm1483ProfileNestedProfileTable.setStatus("current")
_JuniAtm1483ProfileNestedProfileEntry_Object = MibTableRow
juniAtm1483ProfileNestedProfileEntry = _JuniAtm1483ProfileNestedProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 58, 1, 1, 3, 1)
)
juniAtm1483ProfileNestedProfileEntry.setIndexNames(
    (0, "Juniper-ATM-1483-Profile-MIB", "juniAtm1483ProfileNestedProfileId"),
    (0, "Juniper-ATM-1483-Profile-MIB", "juniAtm1483ProfileNestedProfileEncaps"),
)
if mibBuilder.loadTexts:
    juniAtm1483ProfileNestedProfileEntry.setStatus("current")
_JuniAtm1483ProfileNestedProfileId_Type = Unsigned32
_JuniAtm1483ProfileNestedProfileId_Object = MibTableColumn
juniAtm1483ProfileNestedProfileId = _JuniAtm1483ProfileNestedProfileId_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 58, 1, 1, 3, 1, 1),
    _JuniAtm1483ProfileNestedProfileId_Type()
)
juniAtm1483ProfileNestedProfileId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    juniAtm1483ProfileNestedProfileId.setStatus("current")
_JuniAtm1483ProfileNestedProfileEncaps_Type = JuniProfileIfEncaps
_JuniAtm1483ProfileNestedProfileEncaps_Object = MibTableColumn
juniAtm1483ProfileNestedProfileEncaps = _JuniAtm1483ProfileNestedProfileEncaps_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 58, 1, 1, 3, 1, 2),
    _JuniAtm1483ProfileNestedProfileEncaps_Type()
)
juniAtm1483ProfileNestedProfileEncaps.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    juniAtm1483ProfileNestedProfileEncaps.setStatus("current")
_JuniAtm1483ProfileNestedProfileUpperIfProfileName_Type = DisplayString
_JuniAtm1483ProfileNestedProfileUpperIfProfileName_Object = MibTableColumn
juniAtm1483ProfileNestedProfileUpperIfProfileName = _JuniAtm1483ProfileNestedProfileUpperIfProfileName_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 58, 1, 1, 3, 1, 3),
    _JuniAtm1483ProfileNestedProfileUpperIfProfileName_Type()
)
juniAtm1483ProfileNestedProfileUpperIfProfileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniAtm1483ProfileNestedProfileUpperIfProfileName.setStatus("current")
_JuniAtm1483ProfileSubscriberTable_Object = MibTable
juniAtm1483ProfileSubscriberTable = _JuniAtm1483ProfileSubscriberTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 58, 1, 1, 4)
)
if mibBuilder.loadTexts:
    juniAtm1483ProfileSubscriberTable.setStatus("current")
_JuniAtm1483ProfileSubscriberEntry_Object = MibTableRow
juniAtm1483ProfileSubscriberEntry = _JuniAtm1483ProfileSubscriberEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 58, 1, 1, 4, 1)
)
juniAtm1483ProfileSubscriberEntry.setIndexNames(
    (0, "Juniper-ATM-1483-Profile-MIB", "juniAtm1483ProfileSubscriberId"),
    (0, "Juniper-ATM-1483-Profile-MIB", "juniAtm1483ProfileSubscriberEncaps"),
)
if mibBuilder.loadTexts:
    juniAtm1483ProfileSubscriberEntry.setStatus("current")
_JuniAtm1483ProfileSubscriberId_Type = Unsigned32
_JuniAtm1483ProfileSubscriberId_Object = MibTableColumn
juniAtm1483ProfileSubscriberId = _JuniAtm1483ProfileSubscriberId_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 58, 1, 1, 4, 1, 1),
    _JuniAtm1483ProfileSubscriberId_Type()
)
juniAtm1483ProfileSubscriberId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    juniAtm1483ProfileSubscriberId.setStatus("current")
_JuniAtm1483ProfileSubscriberEncaps_Type = JuniProfileIfEncaps
_JuniAtm1483ProfileSubscriberEncaps_Object = MibTableColumn
juniAtm1483ProfileSubscriberEncaps = _JuniAtm1483ProfileSubscriberEncaps_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 58, 1, 1, 4, 1, 2),
    _JuniAtm1483ProfileSubscriberEncaps_Type()
)
juniAtm1483ProfileSubscriberEncaps.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    juniAtm1483ProfileSubscriberEncaps.setStatus("current")
_JuniAtm1483ProfileSubscriberNamePrefix_Type = JuniEnable
_JuniAtm1483ProfileSubscriberNamePrefix_Object = MibTableColumn
juniAtm1483ProfileSubscriberNamePrefix = _JuniAtm1483ProfileSubscriberNamePrefix_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 58, 1, 1, 4, 1, 3),
    _JuniAtm1483ProfileSubscriberNamePrefix_Type()
)
juniAtm1483ProfileSubscriberNamePrefix.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniAtm1483ProfileSubscriberNamePrefix.setStatus("current")
_JuniAtm1483ProfileSubscriberName_Type = DisplayString
_JuniAtm1483ProfileSubscriberName_Object = MibTableColumn
juniAtm1483ProfileSubscriberName = _JuniAtm1483ProfileSubscriberName_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 58, 1, 1, 4, 1, 4),
    _JuniAtm1483ProfileSubscriberName_Type()
)
juniAtm1483ProfileSubscriberName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniAtm1483ProfileSubscriberName.setStatus("current")
_JuniAtm1483ProfileSubscriberPasswordPrefix_Type = JuniEnable
_JuniAtm1483ProfileSubscriberPasswordPrefix_Object = MibTableColumn
juniAtm1483ProfileSubscriberPasswordPrefix = _JuniAtm1483ProfileSubscriberPasswordPrefix_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 58, 1, 1, 4, 1, 5),
    _JuniAtm1483ProfileSubscriberPasswordPrefix_Type()
)
juniAtm1483ProfileSubscriberPasswordPrefix.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniAtm1483ProfileSubscriberPasswordPrefix.setStatus("current")
_JuniAtm1483ProfileSubscriberPassword_Type = DisplayString
_JuniAtm1483ProfileSubscriberPassword_Object = MibTableColumn
juniAtm1483ProfileSubscriberPassword = _JuniAtm1483ProfileSubscriberPassword_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 58, 1, 1, 4, 1, 6),
    _JuniAtm1483ProfileSubscriberPassword_Type()
)
juniAtm1483ProfileSubscriberPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniAtm1483ProfileSubscriberPassword.setStatus("current")
_JuniAtm1483ProfileSubscriberDomain_Type = DisplayString
_JuniAtm1483ProfileSubscriberDomain_Object = MibTableColumn
juniAtm1483ProfileSubscriberDomain = _JuniAtm1483ProfileSubscriberDomain_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 58, 1, 1, 4, 1, 7),
    _JuniAtm1483ProfileSubscriberDomain_Type()
)
juniAtm1483ProfileSubscriberDomain.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniAtm1483ProfileSubscriberDomain.setStatus("current")
_JuniAtm1483ProfileConformance_ObjectIdentity = ObjectIdentity
juniAtm1483ProfileConformance = _JuniAtm1483ProfileConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 58, 4)
)
_JuniAtm1483ProfileCompliances_ObjectIdentity = ObjectIdentity
juniAtm1483ProfileCompliances = _JuniAtm1483ProfileCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 58, 4, 1)
)
_JuniAtm1483ProfileGroups_ObjectIdentity = ObjectIdentity
juniAtm1483ProfileGroups = _JuniAtm1483ProfileGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 58, 4, 2)
)

# Managed Objects groups

juniAtm1483ProfileGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 58, 4, 2, 1)
)
juniAtm1483ProfileGroup.setObjects(
      *(("Juniper-ATM-1483-Profile-MIB", "juniAtm1483ProfileSetMap"),
        ("Juniper-ATM-1483-Profile-MIB", "juniAtm1483ProfileVccType"),
        ("Juniper-ATM-1483-Profile-MIB", "juniAtm1483ProfileVccServiceCategory"),
        ("Juniper-ATM-1483-Profile-MIB", "juniAtm1483ProfileVccPcr"),
        ("Juniper-ATM-1483-Profile-MIB", "juniAtm1483ProfileVccScr"),
        ("Juniper-ATM-1483-Profile-MIB", "juniAtm1483ProfileVccMbs"),
        ("Juniper-ATM-1483-Profile-MIB", "juniAtm1483ProfileAutoConfEnable"),
        ("Juniper-ATM-1483-Profile-MIB", "juniAtm1483ProfileNestedProfileUpperIfProfileName"),
        ("Juniper-ATM-1483-Profile-MIB", "juniAtm1483ProfileSubscriberNamePrefix"),
        ("Juniper-ATM-1483-Profile-MIB", "juniAtm1483ProfileSubscriberName"),
        ("Juniper-ATM-1483-Profile-MIB", "juniAtm1483ProfileSubscriberPasswordPrefix"),
        ("Juniper-ATM-1483-Profile-MIB", "juniAtm1483ProfileSubscriberPassword"),
        ("Juniper-ATM-1483-Profile-MIB", "juniAtm1483ProfileSubscriberDomain"))
)
if mibBuilder.loadTexts:
    juniAtm1483ProfileGroup.setStatus("obsolete")

juniAtm1483ProfileGroup2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 58, 4, 2, 2)
)
juniAtm1483ProfileGroup2.setObjects(
      *(("Juniper-ATM-1483-Profile-MIB", "juniAtm1483ProfileSetMap"),
        ("Juniper-ATM-1483-Profile-MIB", "juniAtm1483ProfileVccType"),
        ("Juniper-ATM-1483-Profile-MIB", "juniAtm1483ProfileVccServiceCategory"),
        ("Juniper-ATM-1483-Profile-MIB", "juniAtm1483ProfileVccPcr"),
        ("Juniper-ATM-1483-Profile-MIB", "juniAtm1483ProfileVccScr"),
        ("Juniper-ATM-1483-Profile-MIB", "juniAtm1483ProfileVccMbs"),
        ("Juniper-ATM-1483-Profile-MIB", "juniAtm1483ProfileIfAlias"),
        ("Juniper-ATM-1483-Profile-MIB", "juniAtm1483ProfileAdvisoryRxSpeed"),
        ("Juniper-ATM-1483-Profile-MIB", "juniAtm1483ProfileAutoConfEnable"),
        ("Juniper-ATM-1483-Profile-MIB", "juniAtm1483ProfileNestedProfileUpperIfProfileName"),
        ("Juniper-ATM-1483-Profile-MIB", "juniAtm1483ProfileSubscriberNamePrefix"),
        ("Juniper-ATM-1483-Profile-MIB", "juniAtm1483ProfileSubscriberName"),
        ("Juniper-ATM-1483-Profile-MIB", "juniAtm1483ProfileSubscriberPasswordPrefix"),
        ("Juniper-ATM-1483-Profile-MIB", "juniAtm1483ProfileSubscriberPassword"),
        ("Juniper-ATM-1483-Profile-MIB", "juniAtm1483ProfileSubscriberDomain"))
)
if mibBuilder.loadTexts:
    juniAtm1483ProfileGroup2.setStatus("obsolete")

juniAtm1483ProfileGroup3 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 58, 4, 2, 3)
)
juniAtm1483ProfileGroup3.setObjects(
      *(("Juniper-ATM-1483-Profile-MIB", "juniAtm1483ProfileSetMap"),
        ("Juniper-ATM-1483-Profile-MIB", "juniAtm1483ProfileVccType"),
        ("Juniper-ATM-1483-Profile-MIB", "juniAtm1483ProfileVccServiceCategory"),
        ("Juniper-ATM-1483-Profile-MIB", "juniAtm1483ProfileVccPcr"),
        ("Juniper-ATM-1483-Profile-MIB", "juniAtm1483ProfileVccScr"),
        ("Juniper-ATM-1483-Profile-MIB", "juniAtm1483ProfileVccMbs"),
        ("Juniper-ATM-1483-Profile-MIB", "juniAtm1483ProfileVccOamAdminStatus"),
        ("Juniper-ATM-1483-Profile-MIB", "juniAtm1483ProfileVccOamLoopbackFrequency"),
        ("Juniper-ATM-1483-Profile-MIB", "juniAtm1483ProfileAutoConfEnable"),
        ("Juniper-ATM-1483-Profile-MIB", "juniAtm1483ProfileNestedProfileUpperIfProfileName"),
        ("Juniper-ATM-1483-Profile-MIB", "juniAtm1483ProfileSubscriberNamePrefix"),
        ("Juniper-ATM-1483-Profile-MIB", "juniAtm1483ProfileSubscriberName"),
        ("Juniper-ATM-1483-Profile-MIB", "juniAtm1483ProfileSubscriberPasswordPrefix"),
        ("Juniper-ATM-1483-Profile-MIB", "juniAtm1483ProfileSubscriberPassword"),
        ("Juniper-ATM-1483-Profile-MIB", "juniAtm1483ProfileSubscriberDomain"))
)
if mibBuilder.loadTexts:
    juniAtm1483ProfileGroup3.setStatus("obsolete")

juniAtm1483ProfileGroup4 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 58, 4, 2, 4)
)
juniAtm1483ProfileGroup4.setObjects(
      *(("Juniper-ATM-1483-Profile-MIB", "juniAtm1483ProfileSetMap"),
        ("Juniper-ATM-1483-Profile-MIB", "juniAtm1483ProfileVccType"),
        ("Juniper-ATM-1483-Profile-MIB", "juniAtm1483ProfileVccServiceCategory"),
        ("Juniper-ATM-1483-Profile-MIB", "juniAtm1483ProfileVccPcr"),
        ("Juniper-ATM-1483-Profile-MIB", "juniAtm1483ProfileVccScr"),
        ("Juniper-ATM-1483-Profile-MIB", "juniAtm1483ProfileVccMbs"),
        ("Juniper-ATM-1483-Profile-MIB", "juniAtm1483ProfileIfAlias"),
        ("Juniper-ATM-1483-Profile-MIB", "juniAtm1483ProfileAdvisoryRxSpeed"),
        ("Juniper-ATM-1483-Profile-MIB", "juniAtm1483ProfileVccOamAdminStatus"),
        ("Juniper-ATM-1483-Profile-MIB", "juniAtm1483ProfileVccOamLoopbackFrequency"),
        ("Juniper-ATM-1483-Profile-MIB", "juniAtm1483ProfileAutoConfEnable"),
        ("Juniper-ATM-1483-Profile-MIB", "juniAtm1483ProfileNestedProfileUpperIfProfileName"),
        ("Juniper-ATM-1483-Profile-MIB", "juniAtm1483ProfileSubscriberNamePrefix"),
        ("Juniper-ATM-1483-Profile-MIB", "juniAtm1483ProfileSubscriberName"),
        ("Juniper-ATM-1483-Profile-MIB", "juniAtm1483ProfileSubscriberPasswordPrefix"),
        ("Juniper-ATM-1483-Profile-MIB", "juniAtm1483ProfileSubscriberPassword"),
        ("Juniper-ATM-1483-Profile-MIB", "juniAtm1483ProfileSubscriberDomain"))
)
if mibBuilder.loadTexts:
    juniAtm1483ProfileGroup4.setStatus("obsolete")

juniAtm1483ProfileGroup5 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 58, 4, 2, 5)
)
juniAtm1483ProfileGroup5.setObjects(
      *(("Juniper-ATM-1483-Profile-MIB", "juniAtm1483ProfileSetMap"),
        ("Juniper-ATM-1483-Profile-MIB", "juniAtm1483ProfileVccType"),
        ("Juniper-ATM-1483-Profile-MIB", "juniAtm1483ProfileVccServiceCategory"),
        ("Juniper-ATM-1483-Profile-MIB", "juniAtm1483ProfileVccPcr"),
        ("Juniper-ATM-1483-Profile-MIB", "juniAtm1483ProfileVccScr"),
        ("Juniper-ATM-1483-Profile-MIB", "juniAtm1483ProfileVccMbs"),
        ("Juniper-ATM-1483-Profile-MIB", "juniAtm1483ProfileIfAlias"),
        ("Juniper-ATM-1483-Profile-MIB", "juniAtm1483ProfileAdvisoryRxSpeed"),
        ("Juniper-ATM-1483-Profile-MIB", "juniAtm1483ProfileVccOamAdminStatus"),
        ("Juniper-ATM-1483-Profile-MIB", "juniAtm1483ProfileVccOamLoopbackFrequency"),
        ("Juniper-ATM-1483-Profile-MIB", "juniAtm1483ProfileAutoConfEnable"),
        ("Juniper-ATM-1483-Profile-MIB", "juniAtm1483ProfileAutoConfLockoutMin"),
        ("Juniper-ATM-1483-Profile-MIB", "juniAtm1483ProfileAutoConfLockoutMax"),
        ("Juniper-ATM-1483-Profile-MIB", "juniAtm1483ProfileNestedProfileUpperIfProfileName"),
        ("Juniper-ATM-1483-Profile-MIB", "juniAtm1483ProfileSubscriberNamePrefix"),
        ("Juniper-ATM-1483-Profile-MIB", "juniAtm1483ProfileSubscriberName"),
        ("Juniper-ATM-1483-Profile-MIB", "juniAtm1483ProfileSubscriberPasswordPrefix"),
        ("Juniper-ATM-1483-Profile-MIB", "juniAtm1483ProfileSubscriberPassword"),
        ("Juniper-ATM-1483-Profile-MIB", "juniAtm1483ProfileSubscriberDomain"))
)
if mibBuilder.loadTexts:
    juniAtm1483ProfileGroup5.setStatus("obsolete")

juniAtm1483ProfileGroup6 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 58, 4, 2, 6)
)
juniAtm1483ProfileGroup6.setObjects(
      *(("Juniper-ATM-1483-Profile-MIB", "juniAtm1483ProfileSetMap"),
        ("Juniper-ATM-1483-Profile-MIB", "juniAtm1483ProfileVccType"),
        ("Juniper-ATM-1483-Profile-MIB", "juniAtm1483ProfileVccServiceCategory"),
        ("Juniper-ATM-1483-Profile-MIB", "juniAtm1483ProfileVccPcr"),
        ("Juniper-ATM-1483-Profile-MIB", "juniAtm1483ProfileVccScr"),
        ("Juniper-ATM-1483-Profile-MIB", "juniAtm1483ProfileVccMbs"),
        ("Juniper-ATM-1483-Profile-MIB", "juniAtm1483ProfileIfAlias"),
        ("Juniper-ATM-1483-Profile-MIB", "juniAtm1483ProfileAdvisoryRxSpeed"),
        ("Juniper-ATM-1483-Profile-MIB", "juniAtm1483ProfileVccOamAdminStatus"),
        ("Juniper-ATM-1483-Profile-MIB", "juniAtm1483ProfileVccOamLoopbackFrequency"),
        ("Juniper-ATM-1483-Profile-MIB", "juniAtm1483ProfileVcClassName"),
        ("Juniper-ATM-1483-Profile-MIB", "juniAtm1483ProfileAutoConfEnable"),
        ("Juniper-ATM-1483-Profile-MIB", "juniAtm1483ProfileAutoConfLockoutMin"),
        ("Juniper-ATM-1483-Profile-MIB", "juniAtm1483ProfileAutoConfLockoutMax"),
        ("Juniper-ATM-1483-Profile-MIB", "juniAtm1483ProfileNestedProfileUpperIfProfileName"),
        ("Juniper-ATM-1483-Profile-MIB", "juniAtm1483ProfileSubscriberNamePrefix"),
        ("Juniper-ATM-1483-Profile-MIB", "juniAtm1483ProfileSubscriberName"),
        ("Juniper-ATM-1483-Profile-MIB", "juniAtm1483ProfileSubscriberPasswordPrefix"),
        ("Juniper-ATM-1483-Profile-MIB", "juniAtm1483ProfileSubscriberPassword"),
        ("Juniper-ATM-1483-Profile-MIB", "juniAtm1483ProfileSubscriberDomain"))
)
if mibBuilder.loadTexts:
    juniAtm1483ProfileGroup6.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

juniAtm1483ProfileCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 58, 4, 1, 1)
)
if mibBuilder.loadTexts:
    juniAtm1483ProfileCompliance.setStatus(
        "obsolete"
    )

juniAtm1483ProfileCompliance2 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 58, 4, 1, 2)
)
if mibBuilder.loadTexts:
    juniAtm1483ProfileCompliance2.setStatus(
        "obsolete"
    )

juniAtm1483ProfileCompliance3 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 58, 4, 1, 3)
)
if mibBuilder.loadTexts:
    juniAtm1483ProfileCompliance3.setStatus(
        "obsolete"
    )

juniAtm1483ProfileCompliance4 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 58, 4, 1, 4)
)
if mibBuilder.loadTexts:
    juniAtm1483ProfileCompliance4.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Juniper-ATM-1483-Profile-MIB",
    **{"juniAtm1483ProfileMIB": juniAtm1483ProfileMIB,
       "juniAtm1483ProfileObjects": juniAtm1483ProfileObjects,
       "juniAtm1483Profile": juniAtm1483Profile,
       "juniAtm1483ProfileTable": juniAtm1483ProfileTable,
       "juniAtm1483ProfileEntry": juniAtm1483ProfileEntry,
       "juniAtm1483ProfileId": juniAtm1483ProfileId,
       "juniAtm1483ProfileSetMap": juniAtm1483ProfileSetMap,
       "juniAtm1483ProfileVccType": juniAtm1483ProfileVccType,
       "juniAtm1483ProfileVccServiceCategory": juniAtm1483ProfileVccServiceCategory,
       "juniAtm1483ProfileVccPcr": juniAtm1483ProfileVccPcr,
       "juniAtm1483ProfileVccScr": juniAtm1483ProfileVccScr,
       "juniAtm1483ProfileVccMbs": juniAtm1483ProfileVccMbs,
       "juniAtm1483ProfileIfAlias": juniAtm1483ProfileIfAlias,
       "juniAtm1483ProfileAdvisoryRxSpeed": juniAtm1483ProfileAdvisoryRxSpeed,
       "juniAtm1483ProfileVccOamAdminStatus": juniAtm1483ProfileVccOamAdminStatus,
       "juniAtm1483ProfileVccOamLoopbackFrequency": juniAtm1483ProfileVccOamLoopbackFrequency,
       "juniAtm1483ProfileVcClassName": juniAtm1483ProfileVcClassName,
       "juniAtm1483ProfileAutoConfTable": juniAtm1483ProfileAutoConfTable,
       "juniAtm1483ProfileAutoConfEntry": juniAtm1483ProfileAutoConfEntry,
       "juniAtm1483ProfileAutoConfId": juniAtm1483ProfileAutoConfId,
       "juniAtm1483ProfileAutoConfEncaps": juniAtm1483ProfileAutoConfEncaps,
       "juniAtm1483ProfileAutoConfEnable": juniAtm1483ProfileAutoConfEnable,
       "juniAtm1483ProfileAutoConfLockoutMin": juniAtm1483ProfileAutoConfLockoutMin,
       "juniAtm1483ProfileAutoConfLockoutMax": juniAtm1483ProfileAutoConfLockoutMax,
       "juniAtm1483ProfileNestedProfileTable": juniAtm1483ProfileNestedProfileTable,
       "juniAtm1483ProfileNestedProfileEntry": juniAtm1483ProfileNestedProfileEntry,
       "juniAtm1483ProfileNestedProfileId": juniAtm1483ProfileNestedProfileId,
       "juniAtm1483ProfileNestedProfileEncaps": juniAtm1483ProfileNestedProfileEncaps,
       "juniAtm1483ProfileNestedProfileUpperIfProfileName": juniAtm1483ProfileNestedProfileUpperIfProfileName,
       "juniAtm1483ProfileSubscriberTable": juniAtm1483ProfileSubscriberTable,
       "juniAtm1483ProfileSubscriberEntry": juniAtm1483ProfileSubscriberEntry,
       "juniAtm1483ProfileSubscriberId": juniAtm1483ProfileSubscriberId,
       "juniAtm1483ProfileSubscriberEncaps": juniAtm1483ProfileSubscriberEncaps,
       "juniAtm1483ProfileSubscriberNamePrefix": juniAtm1483ProfileSubscriberNamePrefix,
       "juniAtm1483ProfileSubscriberName": juniAtm1483ProfileSubscriberName,
       "juniAtm1483ProfileSubscriberPasswordPrefix": juniAtm1483ProfileSubscriberPasswordPrefix,
       "juniAtm1483ProfileSubscriberPassword": juniAtm1483ProfileSubscriberPassword,
       "juniAtm1483ProfileSubscriberDomain": juniAtm1483ProfileSubscriberDomain,
       "juniAtm1483ProfileConformance": juniAtm1483ProfileConformance,
       "juniAtm1483ProfileCompliances": juniAtm1483ProfileCompliances,
       "juniAtm1483ProfileCompliance": juniAtm1483ProfileCompliance,
       "juniAtm1483ProfileCompliance2": juniAtm1483ProfileCompliance2,
       "juniAtm1483ProfileCompliance3": juniAtm1483ProfileCompliance3,
       "juniAtm1483ProfileCompliance4": juniAtm1483ProfileCompliance4,
       "juniAtm1483ProfileGroups": juniAtm1483ProfileGroups,
       "juniAtm1483ProfileGroup": juniAtm1483ProfileGroup,
       "juniAtm1483ProfileGroup2": juniAtm1483ProfileGroup2,
       "juniAtm1483ProfileGroup3": juniAtm1483ProfileGroup3,
       "juniAtm1483ProfileGroup4": juniAtm1483ProfileGroup4,
       "juniAtm1483ProfileGroup5": juniAtm1483ProfileGroup5,
       "juniAtm1483ProfileGroup6": juniAtm1483ProfileGroup6}
)
