# SNMP MIB module (BLUEARC-TITAN-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/BLUEARC-TITAN-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:48:14 2024
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

(blueArc,
 blueArcPrivate) = mibBuilder.importSymbols(
    "BLUEARC-SERVER-MIB",
    "blueArc",
    "blueArcPrivate")

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
 enterprises,
 iso,
 mib_2) = mibBuilder.importSymbols(
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
    "enterprises",
    "iso",
    "mib-2")

(DisplayString,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY

blueArcTitan = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 11096, 6, 2)
)
blueArcTitan.setRevisions(
        ("2007-11-05 12:00",
         "2006-04-24 12:00",
         "2004-02-20 12:00",
         "2003-11-28 12:00",
         "2003-06-16 12:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_BlueArcTitanObjs_ObjectIdentity = ObjectIdentity
blueArcTitanObjs = _BlueArcTitanObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11096, 6, 2, 1)
)
_SystemTitan_ObjectIdentity = ObjectIdentity
systemTitan = _SystemTitan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11096, 6, 2, 1, 1)
)
_StorageTitan_ObjectIdentity = ObjectIdentity
storageTitan = _StorageTitan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11096, 6, 2, 1, 2)
)
_VirtualVolumesTitan_ObjectIdentity = ObjectIdentity
virtualVolumesTitan = _VirtualVolumesTitan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11096, 6, 2, 1, 2, 1)
)


class _VirtualVolumeTitanNumber_Type(Integer32):
    """Custom type virtualVolumeTitanNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_VirtualVolumeTitanNumber_Type.__name__ = "Integer32"
_VirtualVolumeTitanNumber_Object = MibScalar
virtualVolumeTitanNumber = _VirtualVolumeTitanNumber_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 2, 1, 2, 1, 1),
    _VirtualVolumeTitanNumber_Type()
)
virtualVolumeTitanNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualVolumeTitanNumber.setStatus("current")
_VirtualVolumeTitanTable_Object = MibTable
virtualVolumeTitanTable = _VirtualVolumeTitanTable_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 2, 1, 2, 1, 2)
)
if mibBuilder.loadTexts:
    virtualVolumeTitanTable.setStatus("current")
_VirtualVolumeTitanEntry_Object = MibTableRow
virtualVolumeTitanEntry = _VirtualVolumeTitanEntry_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 2, 1, 2, 1, 2, 1)
)
virtualVolumeTitanEntry.setIndexNames(
    (0, "BLUEARC-TITAN-MIB", "virtualVolumeTitanSpanId"),
    (0, "BLUEARC-TITAN-MIB", "virtualVolumeTitanName"),
)
if mibBuilder.loadTexts:
    virtualVolumeTitanEntry.setStatus("current")


class _VirtualVolumeTitanSpanId_Type(Unsigned32):
    """Custom type virtualVolumeTitanSpanId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_VirtualVolumeTitanSpanId_Type.__name__ = "Unsigned32"
_VirtualVolumeTitanSpanId_Object = MibTableColumn
virtualVolumeTitanSpanId = _VirtualVolumeTitanSpanId_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 2, 1, 2, 1, 2, 1, 1),
    _VirtualVolumeTitanSpanId_Type()
)
virtualVolumeTitanSpanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualVolumeTitanSpanId.setStatus("current")
_VirtualVolumeTitanName_Type = DisplayString
_VirtualVolumeTitanName_Object = MibTableColumn
virtualVolumeTitanName = _VirtualVolumeTitanName_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 2, 1, 2, 1, 2, 1, 2),
    _VirtualVolumeTitanName_Type()
)
virtualVolumeTitanName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualVolumeTitanName.setStatus("current")
_VirtualVolumeTitanPath_Type = DisplayString
_VirtualVolumeTitanPath_Object = MibTableColumn
virtualVolumeTitanPath = _VirtualVolumeTitanPath_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 2, 1, 2, 1, 2, 1, 3),
    _VirtualVolumeTitanPath_Type()
)
virtualVolumeTitanPath.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualVolumeTitanPath.setStatus("current")


class _VirtualVolumeTitanEmailNumber_Type(Integer32):
    """Custom type virtualVolumeTitanEmailNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_VirtualVolumeTitanEmailNumber_Type.__name__ = "Integer32"
_VirtualVolumeTitanEmailNumber_Object = MibTableColumn
virtualVolumeTitanEmailNumber = _VirtualVolumeTitanEmailNumber_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 2, 1, 2, 1, 2, 1, 4),
    _VirtualVolumeTitanEmailNumber_Type()
)
virtualVolumeTitanEmailNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualVolumeTitanEmailNumber.setStatus("current")


class _VirtualVolumeTitanQuotaNumber_Type(Integer32):
    """Custom type virtualVolumeTitanQuotaNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_VirtualVolumeTitanQuotaNumber_Type.__name__ = "Integer32"
_VirtualVolumeTitanQuotaNumber_Object = MibTableColumn
virtualVolumeTitanQuotaNumber = _VirtualVolumeTitanQuotaNumber_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 2, 1, 2, 1, 2, 1, 5),
    _VirtualVolumeTitanQuotaNumber_Type()
)
virtualVolumeTitanQuotaNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualVolumeTitanQuotaNumber.setStatus("current")
_VirtualVolumeTitanEmailTable_Object = MibTable
virtualVolumeTitanEmailTable = _VirtualVolumeTitanEmailTable_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 2, 1, 2, 1, 3)
)
if mibBuilder.loadTexts:
    virtualVolumeTitanEmailTable.setStatus("current")
_VirtualVolumeTitanEmailEntry_Object = MibTableRow
virtualVolumeTitanEmailEntry = _VirtualVolumeTitanEmailEntry_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 2, 1, 2, 1, 3, 1)
)
virtualVolumeTitanEmailEntry.setIndexNames(
    (0, "BLUEARC-TITAN-MIB", "virtualVolumeTitanSpanId"),
    (0, "BLUEARC-TITAN-MIB", "virtualVolumeTitanName"),
    (0, "BLUEARC-TITAN-MIB", "virtualVolumeTitanEmailAddress"),
)
if mibBuilder.loadTexts:
    virtualVolumeTitanEmailEntry.setStatus("current")
_VirtualVolumeTitanEmailAddress_Type = DisplayString
_VirtualVolumeTitanEmailAddress_Object = MibTableColumn
virtualVolumeTitanEmailAddress = _VirtualVolumeTitanEmailAddress_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 2, 1, 2, 1, 3, 1, 1),
    _VirtualVolumeTitanEmailAddress_Type()
)
virtualVolumeTitanEmailAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualVolumeTitanEmailAddress.setStatus("current")
_VirtualVolumeTitanQuotaTemplateTable_Object = MibTable
virtualVolumeTitanQuotaTemplateTable = _VirtualVolumeTitanQuotaTemplateTable_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 2, 1, 2, 1, 4)
)
if mibBuilder.loadTexts:
    virtualVolumeTitanQuotaTemplateTable.setStatus("obsolete")
_VirtualVolumeTitanQuotaTemplateEntry_Object = MibTableRow
virtualVolumeTitanQuotaTemplateEntry = _VirtualVolumeTitanQuotaTemplateEntry_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 2, 1, 2, 1, 4, 1)
)
virtualVolumeTitanQuotaTemplateEntry.setIndexNames(
    (0, "BLUEARC-TITAN-MIB", "virtualVolumeTitanSpanId"),
    (0, "BLUEARC-TITAN-MIB", "virtualVolumeTitanName"),
    (0, "BLUEARC-TITAN-MIB", "virtualVolumeQuotaTemplateTargetType"),
)
if mibBuilder.loadTexts:
    virtualVolumeTitanQuotaTemplateEntry.setStatus("obsolete")


class _VirtualVolumeQuotaTemplateTargetType_Type(Integer32):
    """Custom type virtualVolumeQuotaTemplateTargetType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("group", 2),
          ("user", 1))
    )


_VirtualVolumeQuotaTemplateTargetType_Type.__name__ = "Integer32"
_VirtualVolumeQuotaTemplateTargetType_Object = MibTableColumn
virtualVolumeQuotaTemplateTargetType = _VirtualVolumeQuotaTemplateTargetType_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 2, 1, 2, 1, 4, 1, 1),
    _VirtualVolumeQuotaTemplateTargetType_Type()
)
virtualVolumeQuotaTemplateTargetType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualVolumeQuotaTemplateTargetType.setStatus("obsolete")


class _VirtualVolumeQuotaTemplateIgnoreWellKnownGroups_Type(Integer32):
    """Custom type virtualVolumeQuotaTemplateIgnoreWellKnownGroups based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("ignore", 1),
          ("include", 2),
          ("notapplicable", 3))
    )


_VirtualVolumeQuotaTemplateIgnoreWellKnownGroups_Type.__name__ = "Integer32"
_VirtualVolumeQuotaTemplateIgnoreWellKnownGroups_Object = MibTableColumn
virtualVolumeQuotaTemplateIgnoreWellKnownGroups = _VirtualVolumeQuotaTemplateIgnoreWellKnownGroups_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 2, 1, 2, 1, 4, 1, 2),
    _VirtualVolumeQuotaTemplateIgnoreWellKnownGroups_Type()
)
virtualVolumeQuotaTemplateIgnoreWellKnownGroups.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualVolumeQuotaTemplateIgnoreWellKnownGroups.setStatus("obsolete")


class _VirtualVolumeTitanQuotaTemplateUsageLimit_Type(Unsigned32):
    """Custom type virtualVolumeTitanQuotaTemplateUsageLimit based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_VirtualVolumeTitanQuotaTemplateUsageLimit_Type.__name__ = "Unsigned32"
_VirtualVolumeTitanQuotaTemplateUsageLimit_Object = MibTableColumn
virtualVolumeTitanQuotaTemplateUsageLimit = _VirtualVolumeTitanQuotaTemplateUsageLimit_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 2, 1, 2, 1, 4, 1, 3),
    _VirtualVolumeTitanQuotaTemplateUsageLimit_Type()
)
virtualVolumeTitanQuotaTemplateUsageLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualVolumeTitanQuotaTemplateUsageLimit.setStatus("obsolete")


class _VirtualVolumeTitanQuotaTemplateUsageHardLimit_Type(Integer32):
    """Custom type virtualVolumeTitanQuotaTemplateUsageHardLimit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("hard", 1),
          ("soft", 0))
    )


_VirtualVolumeTitanQuotaTemplateUsageHardLimit_Type.__name__ = "Integer32"
_VirtualVolumeTitanQuotaTemplateUsageHardLimit_Object = MibTableColumn
virtualVolumeTitanQuotaTemplateUsageHardLimit = _VirtualVolumeTitanQuotaTemplateUsageHardLimit_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 2, 1, 2, 1, 4, 1, 4),
    _VirtualVolumeTitanQuotaTemplateUsageHardLimit_Type()
)
virtualVolumeTitanQuotaTemplateUsageHardLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualVolumeTitanQuotaTemplateUsageHardLimit.setStatus("obsolete")


class _VirtualVolumeTitanQuotaTemplateUsageReset_Type(Unsigned32):
    """Custom type virtualVolumeTitanQuotaTemplateUsageReset based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_VirtualVolumeTitanQuotaTemplateUsageReset_Type.__name__ = "Unsigned32"
_VirtualVolumeTitanQuotaTemplateUsageReset_Object = MibTableColumn
virtualVolumeTitanQuotaTemplateUsageReset = _VirtualVolumeTitanQuotaTemplateUsageReset_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 2, 1, 2, 1, 4, 1, 5),
    _VirtualVolumeTitanQuotaTemplateUsageReset_Type()
)
virtualVolumeTitanQuotaTemplateUsageReset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualVolumeTitanQuotaTemplateUsageReset.setStatus("obsolete")


class _VirtualVolumeTitanQuotaTemplateUsageWarning_Type(Unsigned32):
    """Custom type virtualVolumeTitanQuotaTemplateUsageWarning based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_VirtualVolumeTitanQuotaTemplateUsageWarning_Type.__name__ = "Unsigned32"
_VirtualVolumeTitanQuotaTemplateUsageWarning_Object = MibTableColumn
virtualVolumeTitanQuotaTemplateUsageWarning = _VirtualVolumeTitanQuotaTemplateUsageWarning_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 2, 1, 2, 1, 4, 1, 6),
    _VirtualVolumeTitanQuotaTemplateUsageWarning_Type()
)
virtualVolumeTitanQuotaTemplateUsageWarning.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualVolumeTitanQuotaTemplateUsageWarning.setStatus("obsolete")


class _VirtualVolumeTitanQuotaTemplateUsageCritical_Type(Unsigned32):
    """Custom type virtualVolumeTitanQuotaTemplateUsageCritical based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_VirtualVolumeTitanQuotaTemplateUsageCritical_Type.__name__ = "Unsigned32"
_VirtualVolumeTitanQuotaTemplateUsageCritical_Object = MibTableColumn
virtualVolumeTitanQuotaTemplateUsageCritical = _VirtualVolumeTitanQuotaTemplateUsageCritical_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 2, 1, 2, 1, 4, 1, 7),
    _VirtualVolumeTitanQuotaTemplateUsageCritical_Type()
)
virtualVolumeTitanQuotaTemplateUsageCritical.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualVolumeTitanQuotaTemplateUsageCritical.setStatus("obsolete")


class _VirtualVolumeTitanQuotaTemplateFileCountLimit_Type(Unsigned32):
    """Custom type virtualVolumeTitanQuotaTemplateFileCountLimit based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_VirtualVolumeTitanQuotaTemplateFileCountLimit_Type.__name__ = "Unsigned32"
_VirtualVolumeTitanQuotaTemplateFileCountLimit_Object = MibTableColumn
virtualVolumeTitanQuotaTemplateFileCountLimit = _VirtualVolumeTitanQuotaTemplateFileCountLimit_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 2, 1, 2, 1, 4, 1, 8),
    _VirtualVolumeTitanQuotaTemplateFileCountLimit_Type()
)
virtualVolumeTitanQuotaTemplateFileCountLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualVolumeTitanQuotaTemplateFileCountLimit.setStatus("obsolete")


class _VirtualVolumeTitanQuotaTemplateFileCountHardLimit_Type(Integer32):
    """Custom type virtualVolumeTitanQuotaTemplateFileCountHardLimit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("hard", 1),
          ("soft", 0))
    )


_VirtualVolumeTitanQuotaTemplateFileCountHardLimit_Type.__name__ = "Integer32"
_VirtualVolumeTitanQuotaTemplateFileCountHardLimit_Object = MibTableColumn
virtualVolumeTitanQuotaTemplateFileCountHardLimit = _VirtualVolumeTitanQuotaTemplateFileCountHardLimit_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 2, 1, 2, 1, 4, 1, 9),
    _VirtualVolumeTitanQuotaTemplateFileCountHardLimit_Type()
)
virtualVolumeTitanQuotaTemplateFileCountHardLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualVolumeTitanQuotaTemplateFileCountHardLimit.setStatus("obsolete")


class _VirtualVolumeTitanQuotaTemplateFileCountReset_Type(Unsigned32):
    """Custom type virtualVolumeTitanQuotaTemplateFileCountReset based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_VirtualVolumeTitanQuotaTemplateFileCountReset_Type.__name__ = "Unsigned32"
_VirtualVolumeTitanQuotaTemplateFileCountReset_Object = MibTableColumn
virtualVolumeTitanQuotaTemplateFileCountReset = _VirtualVolumeTitanQuotaTemplateFileCountReset_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 2, 1, 2, 1, 4, 1, 10),
    _VirtualVolumeTitanQuotaTemplateFileCountReset_Type()
)
virtualVolumeTitanQuotaTemplateFileCountReset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualVolumeTitanQuotaTemplateFileCountReset.setStatus("obsolete")


class _VirtualVolumeTitanQuotaTemplateFileCountWarning_Type(Unsigned32):
    """Custom type virtualVolumeTitanQuotaTemplateFileCountWarning based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_VirtualVolumeTitanQuotaTemplateFileCountWarning_Type.__name__ = "Unsigned32"
_VirtualVolumeTitanQuotaTemplateFileCountWarning_Object = MibTableColumn
virtualVolumeTitanQuotaTemplateFileCountWarning = _VirtualVolumeTitanQuotaTemplateFileCountWarning_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 2, 1, 2, 1, 4, 1, 11),
    _VirtualVolumeTitanQuotaTemplateFileCountWarning_Type()
)
virtualVolumeTitanQuotaTemplateFileCountWarning.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualVolumeTitanQuotaTemplateFileCountWarning.setStatus("obsolete")


class _VirtualVolumeTitanQuotaTemplateFileCountCritical_Type(Unsigned32):
    """Custom type virtualVolumeTitanQuotaTemplateFileCountCritical based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_VirtualVolumeTitanQuotaTemplateFileCountCritical_Type.__name__ = "Unsigned32"
_VirtualVolumeTitanQuotaTemplateFileCountCritical_Object = MibTableColumn
virtualVolumeTitanQuotaTemplateFileCountCritical = _VirtualVolumeTitanQuotaTemplateFileCountCritical_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 2, 1, 2, 1, 4, 1, 12),
    _VirtualVolumeTitanQuotaTemplateFileCountCritical_Type()
)
virtualVolumeTitanQuotaTemplateFileCountCritical.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualVolumeTitanQuotaTemplateFileCountCritical.setStatus("obsolete")
_VirtualVolumeTitanQuotaTable_Object = MibTable
virtualVolumeTitanQuotaTable = _VirtualVolumeTitanQuotaTable_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 2, 1, 2, 1, 5)
)
if mibBuilder.loadTexts:
    virtualVolumeTitanQuotaTable.setStatus("obsolete")
_VirtualVolumeTitanQuotaEntry_Object = MibTableRow
virtualVolumeTitanQuotaEntry = _VirtualVolumeTitanQuotaEntry_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 2, 1, 2, 1, 5, 1)
)
virtualVolumeTitanQuotaEntry.setIndexNames(
    (0, "BLUEARC-TITAN-MIB", "virtualVolumeTitanSpanId"),
    (0, "BLUEARC-TITAN-MIB", "virtualVolumeTitanName"),
    (0, "BLUEARC-TITAN-MIB", "virtualVolumeTitanQuotaTarget"),
    (0, "BLUEARC-TITAN-MIB", "virtualVolumeTitanQuotaTargetType"),
)
if mibBuilder.loadTexts:
    virtualVolumeTitanQuotaEntry.setStatus("obsolete")
_VirtualVolumeTitanQuotaTarget_Type = DisplayString
_VirtualVolumeTitanQuotaTarget_Object = MibTableColumn
virtualVolumeTitanQuotaTarget = _VirtualVolumeTitanQuotaTarget_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 2, 1, 2, 1, 5, 1, 1),
    _VirtualVolumeTitanQuotaTarget_Type()
)
virtualVolumeTitanQuotaTarget.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualVolumeTitanQuotaTarget.setStatus("obsolete")


class _VirtualVolumeTitanQuotaType_Type(Integer32):
    """Custom type virtualVolumeTitanQuotaType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("default", 1),
          ("explicit", 2))
    )


_VirtualVolumeTitanQuotaType_Type.__name__ = "Integer32"
_VirtualVolumeTitanQuotaType_Object = MibTableColumn
virtualVolumeTitanQuotaType = _VirtualVolumeTitanQuotaType_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 2, 1, 2, 1, 5, 1, 2),
    _VirtualVolumeTitanQuotaType_Type()
)
virtualVolumeTitanQuotaType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualVolumeTitanQuotaType.setStatus("obsolete")


class _VirtualVolumeTitanQuotaTargetType_Type(Integer32):
    """Custom type virtualVolumeTitanQuotaTargetType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("group", 2),
          ("user", 1),
          ("virtualvolume", 3))
    )


_VirtualVolumeTitanQuotaTargetType_Type.__name__ = "Integer32"
_VirtualVolumeTitanQuotaTargetType_Object = MibTableColumn
virtualVolumeTitanQuotaTargetType = _VirtualVolumeTitanQuotaTargetType_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 2, 1, 2, 1, 5, 1, 3),
    _VirtualVolumeTitanQuotaTargetType_Type()
)
virtualVolumeTitanQuotaTargetType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualVolumeTitanQuotaTargetType.setStatus("obsolete")


class _VirtualVolumeTitanQuotaUsage_Type(Unsigned32):
    """Custom type virtualVolumeTitanQuotaUsage based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_VirtualVolumeTitanQuotaUsage_Type.__name__ = "Unsigned32"
_VirtualVolumeTitanQuotaUsage_Object = MibTableColumn
virtualVolumeTitanQuotaUsage = _VirtualVolumeTitanQuotaUsage_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 2, 1, 2, 1, 5, 1, 4),
    _VirtualVolumeTitanQuotaUsage_Type()
)
virtualVolumeTitanQuotaUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualVolumeTitanQuotaUsage.setStatus("obsolete")


class _VirtualVolumeTitanQuotaFileCount_Type(Unsigned32):
    """Custom type virtualVolumeTitanQuotaFileCount based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_VirtualVolumeTitanQuotaFileCount_Type.__name__ = "Unsigned32"
_VirtualVolumeTitanQuotaFileCount_Object = MibTableColumn
virtualVolumeTitanQuotaFileCount = _VirtualVolumeTitanQuotaFileCount_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 2, 1, 2, 1, 5, 1, 5),
    _VirtualVolumeTitanQuotaFileCount_Type()
)
virtualVolumeTitanQuotaFileCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualVolumeTitanQuotaFileCount.setStatus("obsolete")


class _VirtualVolumeTitanQuotaUsageLimit_Type(Unsigned32):
    """Custom type virtualVolumeTitanQuotaUsageLimit based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_VirtualVolumeTitanQuotaUsageLimit_Type.__name__ = "Unsigned32"
_VirtualVolumeTitanQuotaUsageLimit_Object = MibTableColumn
virtualVolumeTitanQuotaUsageLimit = _VirtualVolumeTitanQuotaUsageLimit_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 2, 1, 2, 1, 5, 1, 6),
    _VirtualVolumeTitanQuotaUsageLimit_Type()
)
virtualVolumeTitanQuotaUsageLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualVolumeTitanQuotaUsageLimit.setStatus("obsolete")


class _VirtualVolumeTitanQuotaUsageHardLimit_Type(Integer32):
    """Custom type virtualVolumeTitanQuotaUsageHardLimit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              3)
        )
    )
    namedValues = NamedValues(
        *(("hard", 1),
          ("soft", 0),
          ("unknown", 3))
    )


_VirtualVolumeTitanQuotaUsageHardLimit_Type.__name__ = "Integer32"
_VirtualVolumeTitanQuotaUsageHardLimit_Object = MibTableColumn
virtualVolumeTitanQuotaUsageHardLimit = _VirtualVolumeTitanQuotaUsageHardLimit_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 2, 1, 2, 1, 5, 1, 7),
    _VirtualVolumeTitanQuotaUsageHardLimit_Type()
)
virtualVolumeTitanQuotaUsageHardLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualVolumeTitanQuotaUsageHardLimit.setStatus("obsolete")


class _VirtualVolumeTitanQuotaUsageReset_Type(Unsigned32):
    """Custom type virtualVolumeTitanQuotaUsageReset based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_VirtualVolumeTitanQuotaUsageReset_Type.__name__ = "Unsigned32"
_VirtualVolumeTitanQuotaUsageReset_Object = MibTableColumn
virtualVolumeTitanQuotaUsageReset = _VirtualVolumeTitanQuotaUsageReset_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 2, 1, 2, 1, 5, 1, 8),
    _VirtualVolumeTitanQuotaUsageReset_Type()
)
virtualVolumeTitanQuotaUsageReset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualVolumeTitanQuotaUsageReset.setStatus("obsolete")


class _VirtualVolumeTitanQuotaUsageWarning_Type(Unsigned32):
    """Custom type virtualVolumeTitanQuotaUsageWarning based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_VirtualVolumeTitanQuotaUsageWarning_Type.__name__ = "Unsigned32"
_VirtualVolumeTitanQuotaUsageWarning_Object = MibTableColumn
virtualVolumeTitanQuotaUsageWarning = _VirtualVolumeTitanQuotaUsageWarning_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 2, 1, 2, 1, 5, 1, 9),
    _VirtualVolumeTitanQuotaUsageWarning_Type()
)
virtualVolumeTitanQuotaUsageWarning.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualVolumeTitanQuotaUsageWarning.setStatus("obsolete")


class _VirtualVolumeTitanQuotaUsageCritical_Type(Unsigned32):
    """Custom type virtualVolumeTitanQuotaUsageCritical based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_VirtualVolumeTitanQuotaUsageCritical_Type.__name__ = "Unsigned32"
_VirtualVolumeTitanQuotaUsageCritical_Object = MibTableColumn
virtualVolumeTitanQuotaUsageCritical = _VirtualVolumeTitanQuotaUsageCritical_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 2, 1, 2, 1, 5, 1, 10),
    _VirtualVolumeTitanQuotaUsageCritical_Type()
)
virtualVolumeTitanQuotaUsageCritical.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualVolumeTitanQuotaUsageCritical.setStatus("obsolete")


class _VirtualVolumeTitanQuotaFileCountLimit_Type(Unsigned32):
    """Custom type virtualVolumeTitanQuotaFileCountLimit based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_VirtualVolumeTitanQuotaFileCountLimit_Type.__name__ = "Unsigned32"
_VirtualVolumeTitanQuotaFileCountLimit_Object = MibTableColumn
virtualVolumeTitanQuotaFileCountLimit = _VirtualVolumeTitanQuotaFileCountLimit_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 2, 1, 2, 1, 5, 1, 11),
    _VirtualVolumeTitanQuotaFileCountLimit_Type()
)
virtualVolumeTitanQuotaFileCountLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualVolumeTitanQuotaFileCountLimit.setStatus("obsolete")


class _VirtualVolumeTitanQuotaFileCountHardLimit_Type(Integer32):
    """Custom type virtualVolumeTitanQuotaFileCountHardLimit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("hard", 1),
          ("soft", 0),
          ("unknown", 2))
    )


_VirtualVolumeTitanQuotaFileCountHardLimit_Type.__name__ = "Integer32"
_VirtualVolumeTitanQuotaFileCountHardLimit_Object = MibTableColumn
virtualVolumeTitanQuotaFileCountHardLimit = _VirtualVolumeTitanQuotaFileCountHardLimit_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 2, 1, 2, 1, 5, 1, 12),
    _VirtualVolumeTitanQuotaFileCountHardLimit_Type()
)
virtualVolumeTitanQuotaFileCountHardLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualVolumeTitanQuotaFileCountHardLimit.setStatus("obsolete")


class _VirtualVolumeTitanQuotaFileCountReset_Type(Unsigned32):
    """Custom type virtualVolumeTitanQuotaFileCountReset based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_VirtualVolumeTitanQuotaFileCountReset_Type.__name__ = "Unsigned32"
_VirtualVolumeTitanQuotaFileCountReset_Object = MibTableColumn
virtualVolumeTitanQuotaFileCountReset = _VirtualVolumeTitanQuotaFileCountReset_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 2, 1, 2, 1, 5, 1, 13),
    _VirtualVolumeTitanQuotaFileCountReset_Type()
)
virtualVolumeTitanQuotaFileCountReset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualVolumeTitanQuotaFileCountReset.setStatus("obsolete")


class _VirtualVolumeTitanQuotaFileCountWarning_Type(Unsigned32):
    """Custom type virtualVolumeTitanQuotaFileCountWarning based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_VirtualVolumeTitanQuotaFileCountWarning_Type.__name__ = "Unsigned32"
_VirtualVolumeTitanQuotaFileCountWarning_Object = MibTableColumn
virtualVolumeTitanQuotaFileCountWarning = _VirtualVolumeTitanQuotaFileCountWarning_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 2, 1, 2, 1, 5, 1, 14),
    _VirtualVolumeTitanQuotaFileCountWarning_Type()
)
virtualVolumeTitanQuotaFileCountWarning.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualVolumeTitanQuotaFileCountWarning.setStatus("obsolete")


class _VirtualVolumeTitanQuotaFileCountCritical_Type(Unsigned32):
    """Custom type virtualVolumeTitanQuotaFileCountCritical based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_VirtualVolumeTitanQuotaFileCountCritical_Type.__name__ = "Unsigned32"
_VirtualVolumeTitanQuotaFileCountCritical_Object = MibTableColumn
virtualVolumeTitanQuotaFileCountCritical = _VirtualVolumeTitanQuotaFileCountCritical_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 2, 1, 2, 1, 5, 1, 15),
    _VirtualVolumeTitanQuotaFileCountCritical_Type()
)
virtualVolumeTitanQuotaFileCountCritical.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualVolumeTitanQuotaFileCountCritical.setStatus("obsolete")
_VirtualVolumeTitanQuotaDefaultTable_Object = MibTable
virtualVolumeTitanQuotaDefaultTable = _VirtualVolumeTitanQuotaDefaultTable_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 2, 1, 2, 1, 6)
)
if mibBuilder.loadTexts:
    virtualVolumeTitanQuotaDefaultTable.setStatus("current")
_VirtualVolumeTitanQuotaDefaultEntry_Object = MibTableRow
virtualVolumeTitanQuotaDefaultEntry = _VirtualVolumeTitanQuotaDefaultEntry_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 2, 1, 2, 1, 6, 1)
)
virtualVolumeTitanQuotaDefaultEntry.setIndexNames(
    (0, "BLUEARC-TITAN-MIB", "virtualVolumeTitanSpanId"),
    (0, "BLUEARC-TITAN-MIB", "virtualVolumeTitanName"),
    (0, "BLUEARC-TITAN-MIB", "virtualVolumeQuotaDefaultTargetType"),
)
if mibBuilder.loadTexts:
    virtualVolumeTitanQuotaDefaultEntry.setStatus("current")


class _VirtualVolumeQuotaDefaultTargetType_Type(Integer32):
    """Custom type virtualVolumeQuotaDefaultTargetType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("group", 2),
          ("user", 1))
    )


_VirtualVolumeQuotaDefaultTargetType_Type.__name__ = "Integer32"
_VirtualVolumeQuotaDefaultTargetType_Object = MibTableColumn
virtualVolumeQuotaDefaultTargetType = _VirtualVolumeQuotaDefaultTargetType_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 2, 1, 2, 1, 6, 1, 1),
    _VirtualVolumeQuotaDefaultTargetType_Type()
)
virtualVolumeQuotaDefaultTargetType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualVolumeQuotaDefaultTargetType.setStatus("current")


class _VirtualVolumeQuotaDefaultIgnoreWellKnownGroups_Type(Integer32):
    """Custom type virtualVolumeQuotaDefaultIgnoreWellKnownGroups based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("ignore", 1),
          ("include", 2),
          ("notapplicable", 3))
    )


_VirtualVolumeQuotaDefaultIgnoreWellKnownGroups_Type.__name__ = "Integer32"
_VirtualVolumeQuotaDefaultIgnoreWellKnownGroups_Object = MibTableColumn
virtualVolumeQuotaDefaultIgnoreWellKnownGroups = _VirtualVolumeQuotaDefaultIgnoreWellKnownGroups_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 2, 1, 2, 1, 6, 1, 2),
    _VirtualVolumeQuotaDefaultIgnoreWellKnownGroups_Type()
)
virtualVolumeQuotaDefaultIgnoreWellKnownGroups.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualVolumeQuotaDefaultIgnoreWellKnownGroups.setStatus("current")
_VirtualVolumeTitanQuotaDefaultUsageLimit_Type = Counter64
_VirtualVolumeTitanQuotaDefaultUsageLimit_Object = MibTableColumn
virtualVolumeTitanQuotaDefaultUsageLimit = _VirtualVolumeTitanQuotaDefaultUsageLimit_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 2, 1, 2, 1, 6, 1, 3),
    _VirtualVolumeTitanQuotaDefaultUsageLimit_Type()
)
virtualVolumeTitanQuotaDefaultUsageLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualVolumeTitanQuotaDefaultUsageLimit.setStatus("current")


class _VirtualVolumeTitanQuotaDefaultUsageHardLimit_Type(Integer32):
    """Custom type virtualVolumeTitanQuotaDefaultUsageHardLimit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("hard", 1),
          ("soft", 0),
          ("unknown", 2))
    )


_VirtualVolumeTitanQuotaDefaultUsageHardLimit_Type.__name__ = "Integer32"
_VirtualVolumeTitanQuotaDefaultUsageHardLimit_Object = MibTableColumn
virtualVolumeTitanQuotaDefaultUsageHardLimit = _VirtualVolumeTitanQuotaDefaultUsageHardLimit_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 2, 1, 2, 1, 6, 1, 4),
    _VirtualVolumeTitanQuotaDefaultUsageHardLimit_Type()
)
virtualVolumeTitanQuotaDefaultUsageHardLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualVolumeTitanQuotaDefaultUsageHardLimit.setStatus("current")
_VirtualVolumeTitanQuotaDefaultUsageReset_Type = Counter64
_VirtualVolumeTitanQuotaDefaultUsageReset_Object = MibTableColumn
virtualVolumeTitanQuotaDefaultUsageReset = _VirtualVolumeTitanQuotaDefaultUsageReset_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 2, 1, 2, 1, 6, 1, 5),
    _VirtualVolumeTitanQuotaDefaultUsageReset_Type()
)
virtualVolumeTitanQuotaDefaultUsageReset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualVolumeTitanQuotaDefaultUsageReset.setStatus("current")
_VirtualVolumeTitanQuotaDefaultUsageWarning_Type = Counter64
_VirtualVolumeTitanQuotaDefaultUsageWarning_Object = MibTableColumn
virtualVolumeTitanQuotaDefaultUsageWarning = _VirtualVolumeTitanQuotaDefaultUsageWarning_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 2, 1, 2, 1, 6, 1, 6),
    _VirtualVolumeTitanQuotaDefaultUsageWarning_Type()
)
virtualVolumeTitanQuotaDefaultUsageWarning.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualVolumeTitanQuotaDefaultUsageWarning.setStatus("current")
_VirtualVolumeTitanQuotaDefaultUsageCritical_Type = Counter64
_VirtualVolumeTitanQuotaDefaultUsageCritical_Object = MibTableColumn
virtualVolumeTitanQuotaDefaultUsageCritical = _VirtualVolumeTitanQuotaDefaultUsageCritical_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 2, 1, 2, 1, 6, 1, 7),
    _VirtualVolumeTitanQuotaDefaultUsageCritical_Type()
)
virtualVolumeTitanQuotaDefaultUsageCritical.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualVolumeTitanQuotaDefaultUsageCritical.setStatus("current")


class _VirtualVolumeTitanQuotaDefaultFileCountLimit_Type(Unsigned32):
    """Custom type virtualVolumeTitanQuotaDefaultFileCountLimit based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_VirtualVolumeTitanQuotaDefaultFileCountLimit_Type.__name__ = "Unsigned32"
_VirtualVolumeTitanQuotaDefaultFileCountLimit_Object = MibTableColumn
virtualVolumeTitanQuotaDefaultFileCountLimit = _VirtualVolumeTitanQuotaDefaultFileCountLimit_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 2, 1, 2, 1, 6, 1, 8),
    _VirtualVolumeTitanQuotaDefaultFileCountLimit_Type()
)
virtualVolumeTitanQuotaDefaultFileCountLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualVolumeTitanQuotaDefaultFileCountLimit.setStatus("current")


class _VirtualVolumeTitanQuotaDefaultFileCountHardLimit_Type(Integer32):
    """Custom type virtualVolumeTitanQuotaDefaultFileCountHardLimit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("hard", 1),
          ("soft", 0),
          ("unknown", 2))
    )


_VirtualVolumeTitanQuotaDefaultFileCountHardLimit_Type.__name__ = "Integer32"
_VirtualVolumeTitanQuotaDefaultFileCountHardLimit_Object = MibTableColumn
virtualVolumeTitanQuotaDefaultFileCountHardLimit = _VirtualVolumeTitanQuotaDefaultFileCountHardLimit_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 2, 1, 2, 1, 6, 1, 9),
    _VirtualVolumeTitanQuotaDefaultFileCountHardLimit_Type()
)
virtualVolumeTitanQuotaDefaultFileCountHardLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualVolumeTitanQuotaDefaultFileCountHardLimit.setStatus("current")


class _VirtualVolumeTitanQuotaDefaultFileCountReset_Type(Unsigned32):
    """Custom type virtualVolumeTitanQuotaDefaultFileCountReset based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_VirtualVolumeTitanQuotaDefaultFileCountReset_Type.__name__ = "Unsigned32"
_VirtualVolumeTitanQuotaDefaultFileCountReset_Object = MibTableColumn
virtualVolumeTitanQuotaDefaultFileCountReset = _VirtualVolumeTitanQuotaDefaultFileCountReset_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 2, 1, 2, 1, 6, 1, 10),
    _VirtualVolumeTitanQuotaDefaultFileCountReset_Type()
)
virtualVolumeTitanQuotaDefaultFileCountReset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualVolumeTitanQuotaDefaultFileCountReset.setStatus("current")


class _VirtualVolumeTitanQuotaDefaultFileCountWarning_Type(Unsigned32):
    """Custom type virtualVolumeTitanQuotaDefaultFileCountWarning based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_VirtualVolumeTitanQuotaDefaultFileCountWarning_Type.__name__ = "Unsigned32"
_VirtualVolumeTitanQuotaDefaultFileCountWarning_Object = MibTableColumn
virtualVolumeTitanQuotaDefaultFileCountWarning = _VirtualVolumeTitanQuotaDefaultFileCountWarning_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 2, 1, 2, 1, 6, 1, 11),
    _VirtualVolumeTitanQuotaDefaultFileCountWarning_Type()
)
virtualVolumeTitanQuotaDefaultFileCountWarning.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualVolumeTitanQuotaDefaultFileCountWarning.setStatus("current")


class _VirtualVolumeTitanQuotaDefaultFileCountCritical_Type(Unsigned32):
    """Custom type virtualVolumeTitanQuotaDefaultFileCountCritical based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_VirtualVolumeTitanQuotaDefaultFileCountCritical_Type.__name__ = "Unsigned32"
_VirtualVolumeTitanQuotaDefaultFileCountCritical_Object = MibTableColumn
virtualVolumeTitanQuotaDefaultFileCountCritical = _VirtualVolumeTitanQuotaDefaultFileCountCritical_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 2, 1, 2, 1, 6, 1, 12),
    _VirtualVolumeTitanQuotaDefaultFileCountCritical_Type()
)
virtualVolumeTitanQuotaDefaultFileCountCritical.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualVolumeTitanQuotaDefaultFileCountCritical.setStatus("current")
_VirtualVolumeTitanQuotasTable_Object = MibTable
virtualVolumeTitanQuotasTable = _VirtualVolumeTitanQuotasTable_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 2, 1, 2, 1, 7)
)
if mibBuilder.loadTexts:
    virtualVolumeTitanQuotasTable.setStatus("current")
_VirtualVolumeTitanQuotasEntry_Object = MibTableRow
virtualVolumeTitanQuotasEntry = _VirtualVolumeTitanQuotasEntry_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 2, 1, 2, 1, 7, 1)
)
virtualVolumeTitanQuotasEntry.setIndexNames(
    (0, "BLUEARC-TITAN-MIB", "virtualVolumeTitanSpanId"),
    (0, "BLUEARC-TITAN-MIB", "virtualVolumeTitanName"),
    (0, "BLUEARC-TITAN-MIB", "virtualVolumeTitanQuotasTarget"),
    (0, "BLUEARC-TITAN-MIB", "virtualVolumeTitanQuotasTargetType"),
)
if mibBuilder.loadTexts:
    virtualVolumeTitanQuotasEntry.setStatus("current")
_VirtualVolumeTitanQuotasTarget_Type = DisplayString
_VirtualVolumeTitanQuotasTarget_Object = MibTableColumn
virtualVolumeTitanQuotasTarget = _VirtualVolumeTitanQuotasTarget_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 2, 1, 2, 1, 7, 1, 1),
    _VirtualVolumeTitanQuotasTarget_Type()
)
virtualVolumeTitanQuotasTarget.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualVolumeTitanQuotasTarget.setStatus("current")


class _VirtualVolumeTitanQuotasType_Type(Integer32):
    """Custom type virtualVolumeTitanQuotasType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("default", 1),
          ("explicit", 2),
          ("unknown", 3))
    )


_VirtualVolumeTitanQuotasType_Type.__name__ = "Integer32"
_VirtualVolumeTitanQuotasType_Object = MibTableColumn
virtualVolumeTitanQuotasType = _VirtualVolumeTitanQuotasType_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 2, 1, 2, 1, 7, 1, 2),
    _VirtualVolumeTitanQuotasType_Type()
)
virtualVolumeTitanQuotasType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualVolumeTitanQuotasType.setStatus("current")


class _VirtualVolumeTitanQuotasTargetType_Type(Integer32):
    """Custom type virtualVolumeTitanQuotasTargetType based on Integer32"""
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
        *(("group", 2),
          ("unknown", 4),
          ("user", 1),
          ("virtualvolume", 3))
    )


_VirtualVolumeTitanQuotasTargetType_Type.__name__ = "Integer32"
_VirtualVolumeTitanQuotasTargetType_Object = MibTableColumn
virtualVolumeTitanQuotasTargetType = _VirtualVolumeTitanQuotasTargetType_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 2, 1, 2, 1, 7, 1, 3),
    _VirtualVolumeTitanQuotasTargetType_Type()
)
virtualVolumeTitanQuotasTargetType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualVolumeTitanQuotasTargetType.setStatus("current")
_VirtualVolumeTitanQuotasUsage_Type = Counter64
_VirtualVolumeTitanQuotasUsage_Object = MibTableColumn
virtualVolumeTitanQuotasUsage = _VirtualVolumeTitanQuotasUsage_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 2, 1, 2, 1, 7, 1, 4),
    _VirtualVolumeTitanQuotasUsage_Type()
)
virtualVolumeTitanQuotasUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualVolumeTitanQuotasUsage.setStatus("current")


class _VirtualVolumeTitanQuotasFileCount_Type(Unsigned32):
    """Custom type virtualVolumeTitanQuotasFileCount based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_VirtualVolumeTitanQuotasFileCount_Type.__name__ = "Unsigned32"
_VirtualVolumeTitanQuotasFileCount_Object = MibTableColumn
virtualVolumeTitanQuotasFileCount = _VirtualVolumeTitanQuotasFileCount_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 2, 1, 2, 1, 7, 1, 5),
    _VirtualVolumeTitanQuotasFileCount_Type()
)
virtualVolumeTitanQuotasFileCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualVolumeTitanQuotasFileCount.setStatus("current")
_VirtualVolumeTitanQuotasUsageLimit_Type = Counter64
_VirtualVolumeTitanQuotasUsageLimit_Object = MibTableColumn
virtualVolumeTitanQuotasUsageLimit = _VirtualVolumeTitanQuotasUsageLimit_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 2, 1, 2, 1, 7, 1, 6),
    _VirtualVolumeTitanQuotasUsageLimit_Type()
)
virtualVolumeTitanQuotasUsageLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualVolumeTitanQuotasUsageLimit.setStatus("current")


class _VirtualVolumeTitanQuotasUsageHardLimit_Type(Integer32):
    """Custom type virtualVolumeTitanQuotasUsageHardLimit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("hard", 1),
          ("soft", 0),
          ("unknown", 2))
    )


_VirtualVolumeTitanQuotasUsageHardLimit_Type.__name__ = "Integer32"
_VirtualVolumeTitanQuotasUsageHardLimit_Object = MibTableColumn
virtualVolumeTitanQuotasUsageHardLimit = _VirtualVolumeTitanQuotasUsageHardLimit_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 2, 1, 2, 1, 7, 1, 7),
    _VirtualVolumeTitanQuotasUsageHardLimit_Type()
)
virtualVolumeTitanQuotasUsageHardLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualVolumeTitanQuotasUsageHardLimit.setStatus("current")
_VirtualVolumeTitanQuotasUsageReset_Type = Counter64
_VirtualVolumeTitanQuotasUsageReset_Object = MibTableColumn
virtualVolumeTitanQuotasUsageReset = _VirtualVolumeTitanQuotasUsageReset_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 2, 1, 2, 1, 7, 1, 8),
    _VirtualVolumeTitanQuotasUsageReset_Type()
)
virtualVolumeTitanQuotasUsageReset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualVolumeTitanQuotasUsageReset.setStatus("current")
_VirtualVolumeTitanQuotasUsageWarning_Type = Counter64
_VirtualVolumeTitanQuotasUsageWarning_Object = MibTableColumn
virtualVolumeTitanQuotasUsageWarning = _VirtualVolumeTitanQuotasUsageWarning_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 2, 1, 2, 1, 7, 1, 9),
    _VirtualVolumeTitanQuotasUsageWarning_Type()
)
virtualVolumeTitanQuotasUsageWarning.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualVolumeTitanQuotasUsageWarning.setStatus("current")
_VirtualVolumeTitanQuotasUsageCritical_Type = Counter64
_VirtualVolumeTitanQuotasUsageCritical_Object = MibTableColumn
virtualVolumeTitanQuotasUsageCritical = _VirtualVolumeTitanQuotasUsageCritical_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 2, 1, 2, 1, 7, 1, 10),
    _VirtualVolumeTitanQuotasUsageCritical_Type()
)
virtualVolumeTitanQuotasUsageCritical.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualVolumeTitanQuotasUsageCritical.setStatus("current")


class _VirtualVolumeTitanQuotasFileCountLimit_Type(Unsigned32):
    """Custom type virtualVolumeTitanQuotasFileCountLimit based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_VirtualVolumeTitanQuotasFileCountLimit_Type.__name__ = "Unsigned32"
_VirtualVolumeTitanQuotasFileCountLimit_Object = MibTableColumn
virtualVolumeTitanQuotasFileCountLimit = _VirtualVolumeTitanQuotasFileCountLimit_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 2, 1, 2, 1, 7, 1, 11),
    _VirtualVolumeTitanQuotasFileCountLimit_Type()
)
virtualVolumeTitanQuotasFileCountLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualVolumeTitanQuotasFileCountLimit.setStatus("current")


class _VirtualVolumeTitanQuotasFileCountHardLimit_Type(Integer32):
    """Custom type virtualVolumeTitanQuotasFileCountHardLimit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("hard", 1),
          ("soft", 0),
          ("unknown", 2))
    )


_VirtualVolumeTitanQuotasFileCountHardLimit_Type.__name__ = "Integer32"
_VirtualVolumeTitanQuotasFileCountHardLimit_Object = MibTableColumn
virtualVolumeTitanQuotasFileCountHardLimit = _VirtualVolumeTitanQuotasFileCountHardLimit_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 2, 1, 2, 1, 7, 1, 12),
    _VirtualVolumeTitanQuotasFileCountHardLimit_Type()
)
virtualVolumeTitanQuotasFileCountHardLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualVolumeTitanQuotasFileCountHardLimit.setStatus("current")


class _VirtualVolumeTitanQuotasFileCountReset_Type(Unsigned32):
    """Custom type virtualVolumeTitanQuotasFileCountReset based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_VirtualVolumeTitanQuotasFileCountReset_Type.__name__ = "Unsigned32"
_VirtualVolumeTitanQuotasFileCountReset_Object = MibTableColumn
virtualVolumeTitanQuotasFileCountReset = _VirtualVolumeTitanQuotasFileCountReset_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 2, 1, 2, 1, 7, 1, 13),
    _VirtualVolumeTitanQuotasFileCountReset_Type()
)
virtualVolumeTitanQuotasFileCountReset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualVolumeTitanQuotasFileCountReset.setStatus("current")


class _VirtualVolumeTitanQuotasFileCountWarning_Type(Unsigned32):
    """Custom type virtualVolumeTitanQuotasFileCountWarning based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_VirtualVolumeTitanQuotasFileCountWarning_Type.__name__ = "Unsigned32"
_VirtualVolumeTitanQuotasFileCountWarning_Object = MibTableColumn
virtualVolumeTitanQuotasFileCountWarning = _VirtualVolumeTitanQuotasFileCountWarning_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 2, 1, 2, 1, 7, 1, 14),
    _VirtualVolumeTitanQuotasFileCountWarning_Type()
)
virtualVolumeTitanQuotasFileCountWarning.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualVolumeTitanQuotasFileCountWarning.setStatus("current")


class _VirtualVolumeTitanQuotasFileCountCritical_Type(Unsigned32):
    """Custom type virtualVolumeTitanQuotasFileCountCritical based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_VirtualVolumeTitanQuotasFileCountCritical_Type.__name__ = "Unsigned32"
_VirtualVolumeTitanQuotasFileCountCritical_Object = MibTableColumn
virtualVolumeTitanQuotasFileCountCritical = _VirtualVolumeTitanQuotasFileCountCritical_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 2, 1, 2, 1, 7, 1, 15),
    _VirtualVolumeTitanQuotasFileCountCritical_Type()
)
virtualVolumeTitanQuotasFileCountCritical.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualVolumeTitanQuotasFileCountCritical.setStatus("current")
_Nvram_ObjectIdentity = ObjectIdentity
nvram = _Nvram_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11096, 6, 2, 1, 2, 2)
)


class _NvramSize_Type(Unsigned32):
    """Custom type nvramSize based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_NvramSize_Type.__name__ = "Unsigned32"
_NvramSize_Object = MibScalar
nvramSize = _NvramSize_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 2, 1, 2, 2, 1),
    _NvramSize_Type()
)
nvramSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nvramSize.setStatus("obsolete")


class _NvramMaximumUsed_Type(Unsigned32):
    """Custom type nvramMaximumUsed based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_NvramMaximumUsed_Type.__name__ = "Unsigned32"
_NvramMaximumUsed_Object = MibScalar
nvramMaximumUsed = _NvramMaximumUsed_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 2, 1, 2, 2, 2),
    _NvramMaximumUsed_Type()
)
nvramMaximumUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nvramMaximumUsed.setStatus("obsolete")


class _NvramTotalCurrentUsage_Type(Unsigned32):
    """Custom type nvramTotalCurrentUsage based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_NvramTotalCurrentUsage_Type.__name__ = "Unsigned32"
_NvramTotalCurrentUsage_Object = MibScalar
nvramTotalCurrentUsage = _NvramTotalCurrentUsage_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 2, 1, 2, 2, 3),
    _NvramTotalCurrentUsage_Type()
)
nvramTotalCurrentUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nvramTotalCurrentUsage.setStatus("obsolete")


class _NvramNumber_Type(Unsigned32):
    """Custom type nvramNumber based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_NvramNumber_Type.__name__ = "Unsigned32"
_NvramNumber_Object = MibScalar
nvramNumber = _NvramNumber_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 2, 1, 2, 2, 4),
    _NvramNumber_Type()
)
nvramNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nvramNumber.setStatus("obsolete")
_NvramTable_Object = MibTable
nvramTable = _NvramTable_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 2, 1, 2, 2, 5)
)
if mibBuilder.loadTexts:
    nvramTable.setStatus("obsolete")
_NvramEntry_Object = MibTableRow
nvramEntry = _NvramEntry_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 2, 1, 2, 2, 5, 1)
)
nvramEntry.setIndexNames(
    (0, "BLUEARC-TITAN-MIB", "spanId"),
)
if mibBuilder.loadTexts:
    nvramEntry.setStatus("obsolete")
_SpanId_Type = Unsigned32
_SpanId_Object = MibTableColumn
spanId = _SpanId_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 2, 1, 2, 2, 5, 1, 1),
    _SpanId_Type()
)
spanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    spanId.setStatus("obsolete")
_NvramCurrentUsage_Type = Unsigned32
_NvramCurrentUsage_Object = MibTableColumn
nvramCurrentUsage = _NvramCurrentUsage_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 2, 1, 2, 2, 5, 1, 2),
    _NvramCurrentUsage_Type()
)
nvramCurrentUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nvramCurrentUsage.setStatus("obsolete")
_NvramNumberCheckpoints_Type = Unsigned32
_NvramNumberCheckpoints_Object = MibTableColumn
nvramNumberCheckpoints = _NvramNumberCheckpoints_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 2, 1, 2, 2, 5, 1, 3),
    _NvramNumberCheckpoints_Type()
)
nvramNumberCheckpoints.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nvramNumberCheckpoints.setStatus("obsolete")
_NvramNumberActivityCheckpoints_Type = Unsigned32
_NvramNumberActivityCheckpoints_Object = MibTableColumn
nvramNumberActivityCheckpoints = _NvramNumberActivityCheckpoints_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 2, 1, 2, 2, 5, 1, 4),
    _NvramNumberActivityCheckpoints_Type()
)
nvramNumberActivityCheckpoints.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nvramNumberActivityCheckpoints.setStatus("obsolete")
_NvramPoolTable_Object = MibTable
nvramPoolTable = _NvramPoolTable_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 2, 1, 2, 2, 6)
)
if mibBuilder.loadTexts:
    nvramPoolTable.setStatus("obsolete")
_NvramPoolEntry_Object = MibTableRow
nvramPoolEntry = _NvramPoolEntry_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 2, 1, 2, 2, 6, 1)
)
nvramPoolEntry.setIndexNames(
    (0, "BLUEARC-TITAN-MIB", "clusterNodeId"),
)
if mibBuilder.loadTexts:
    nvramPoolEntry.setStatus("obsolete")


class _ClusterNodeId_Type(Unsigned32):
    """Custom type clusterNodeId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_ClusterNodeId_Type.__name__ = "Unsigned32"
_ClusterNodeId_Object = MibTableColumn
clusterNodeId = _ClusterNodeId_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 2, 1, 2, 2, 6, 1, 1),
    _ClusterNodeId_Type()
)
clusterNodeId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clusterNodeId.setStatus("obsolete")


class _NvramPoolSize_Type(Unsigned32):
    """Custom type nvramPoolSize based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_NvramPoolSize_Type.__name__ = "Unsigned32"
_NvramPoolSize_Object = MibTableColumn
nvramPoolSize = _NvramPoolSize_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 2, 1, 2, 2, 6, 1, 2),
    _NvramPoolSize_Type()
)
nvramPoolSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nvramPoolSize.setStatus("obsolete")


class _NvramPoolMaximumUsed_Type(Unsigned32):
    """Custom type nvramPoolMaximumUsed based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_NvramPoolMaximumUsed_Type.__name__ = "Unsigned32"
_NvramPoolMaximumUsed_Object = MibTableColumn
nvramPoolMaximumUsed = _NvramPoolMaximumUsed_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 2, 1, 2, 2, 6, 1, 3),
    _NvramPoolMaximumUsed_Type()
)
nvramPoolMaximumUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nvramPoolMaximumUsed.setStatus("obsolete")


class _NvramPoolTotalCurrentUsage_Type(Unsigned32):
    """Custom type nvramPoolTotalCurrentUsage based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_NvramPoolTotalCurrentUsage_Type.__name__ = "Unsigned32"
_NvramPoolTotalCurrentUsage_Object = MibTableColumn
nvramPoolTotalCurrentUsage = _NvramPoolTotalCurrentUsage_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 2, 1, 2, 2, 6, 1, 4),
    _NvramPoolTotalCurrentUsage_Type()
)
nvramPoolTotalCurrentUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nvramPoolTotalCurrentUsage.setStatus("obsolete")
_NetworkTitan_ObjectIdentity = ObjectIdentity
networkTitan = _NetworkTitan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11096, 6, 2, 1, 3)
)
_EthernetTitan_ObjectIdentity = ObjectIdentity
ethernetTitan = _EthernetTitan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11096, 6, 2, 1, 3, 1)
)
_LinkAggregation_ObjectIdentity = ObjectIdentity
linkAggregation = _LinkAggregation_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11096, 6, 2, 1, 3, 1, 1)
)


class _LagNumber_Type(Integer32):
    """Custom type lagNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_LagNumber_Type.__name__ = "Integer32"
_LagNumber_Object = MibScalar
lagNumber = _LagNumber_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 2, 1, 3, 1, 1, 1),
    _LagNumber_Type()
)
lagNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lagNumber.setStatus("current")
_LagTable_Object = MibTable
lagTable = _LagTable_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 2, 1, 3, 1, 1, 2)
)
if mibBuilder.loadTexts:
    lagTable.setStatus("current")
_LagEntry_Object = MibTableRow
lagEntry = _LagEntry_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 2, 1, 3, 1, 1, 2, 1)
)
lagEntry.setIndexNames(
    (0, "BLUEARC-TITAN-MIB", "lagName"),
)
if mibBuilder.loadTexts:
    lagEntry.setStatus("current")
_LagName_Type = DisplayString
_LagName_Object = MibTableColumn
lagName = _LagName_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 2, 1, 3, 1, 1, 2, 1, 1),
    _LagName_Type()
)
lagName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lagName.setStatus("current")
_LinkedInterfaces_Type = DisplayString
_LinkedInterfaces_Object = MibTableColumn
linkedInterfaces = _LinkedInterfaces_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 2, 1, 3, 1, 1, 2, 1, 2),
    _LinkedInterfaces_Type()
)
linkedInterfaces.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linkedInterfaces.setStatus("current")
_MgmntTitan_ObjectIdentity = ObjectIdentity
mgmntTitan = _MgmntTitan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11096, 6, 2, 1, 4)
)
_PackageMgmnt_ObjectIdentity = ObjectIdentity
packageMgmnt = _PackageMgmnt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11096, 6, 2, 1, 4, 1)
)


class _PackageNumber_Type(Integer32):
    """Custom type packageNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_PackageNumber_Type.__name__ = "Integer32"
_PackageNumber_Object = MibScalar
packageNumber = _PackageNumber_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 2, 1, 4, 1, 1),
    _PackageNumber_Type()
)
packageNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    packageNumber.setStatus("current")
_PackageTable_Object = MibTable
packageTable = _PackageTable_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 2, 1, 4, 1, 2)
)
if mibBuilder.loadTexts:
    packageTable.setStatus("current")
_PackageEntry_Object = MibTableRow
packageEntry = _PackageEntry_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 2, 1, 4, 1, 2, 1)
)
packageEntry.setIndexNames(
    (0, "BLUEARC-TITAN-MIB", "packageName"),
)
if mibBuilder.loadTexts:
    packageEntry.setStatus("current")
_PackageName_Type = DisplayString
_PackageName_Object = MibTableColumn
packageName = _PackageName_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 2, 1, 4, 1, 2, 1, 1),
    _PackageName_Type()
)
packageName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    packageName.setStatus("current")
_PackageDate_Type = DisplayString
_PackageDate_Object = MibTableColumn
packageDate = _PackageDate_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 2, 1, 4, 1, 2, 1, 2),
    _PackageDate_Type()
)
packageDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    packageDate.setStatus("current")


class _PackageSize_Type(Unsigned32):
    """Custom type packageSize based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_PackageSize_Type.__name__ = "Unsigned32"
_PackageSize_Object = MibTableColumn
packageSize = _PackageSize_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 2, 1, 4, 1, 2, 1, 3),
    _PackageSize_Type()
)
packageSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    packageSize.setStatus("current")


class _PackageDefault_Type(Integer32):
    """Custom type packageDefault based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("default", 0),
          ("notdefault", 1))
    )


_PackageDefault_Type.__name__ = "Integer32"
_PackageDefault_Object = MibTableColumn
packageDefault = _PackageDefault_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 2, 1, 4, 1, 2, 1, 4),
    _PackageDefault_Type()
)
packageDefault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    packageDefault.setStatus("current")


class _PackageCurrent_Type(Integer32):
    """Custom type packageCurrent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("current", 0),
          ("notcurrent", 1))
    )


_PackageCurrent_Type.__name__ = "Integer32"
_PackageCurrent_Object = MibTableColumn
packageCurrent = _PackageCurrent_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 2, 1, 4, 1, 2, 1, 5),
    _PackageCurrent_Type()
)
packageCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    packageCurrent.setStatus("current")


class _PackageFreeSpace_Type(Unsigned32):
    """Custom type packageFreeSpace based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_PackageFreeSpace_Type.__name__ = "Unsigned32"
_PackageFreeSpace_Object = MibScalar
packageFreeSpace = _PackageFreeSpace_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 2, 1, 4, 1, 3),
    _PackageFreeSpace_Type()
)
packageFreeSpace.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    packageFreeSpace.setStatus("current")
_FileProtocolTitan_ObjectIdentity = ObjectIdentity
fileProtocolTitan = _FileProtocolTitan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11096, 6, 2, 1, 5)
)
_FtpTitan_ObjectIdentity = ObjectIdentity
ftpTitan = _FtpTitan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11096, 6, 2, 1, 5, 1)
)
_FtpConfig_ObjectIdentity = ObjectIdentity
ftpConfig = _FtpConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11096, 6, 2, 1, 5, 1, 1)
)


class _FtpConfigServiceEnabled_Type(Integer32):
    """Custom type ftpConfigServiceEnabled based on Integer32"""
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
          ("unknown", 3))
    )


_FtpConfigServiceEnabled_Type.__name__ = "Integer32"
_FtpConfigServiceEnabled_Object = MibScalar
ftpConfigServiceEnabled = _FtpConfigServiceEnabled_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 2, 1, 5, 1, 1, 1),
    _FtpConfigServiceEnabled_Type()
)
ftpConfigServiceEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ftpConfigServiceEnabled.setStatus("obsolete")
_FtpConfigServiceMaxUsers_Type = Unsigned32
_FtpConfigServiceMaxUsers_Object = MibScalar
ftpConfigServiceMaxUsers = _FtpConfigServiceMaxUsers_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 2, 1, 5, 1, 1, 2),
    _FtpConfigServiceMaxUsers_Type()
)
ftpConfigServiceMaxUsers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ftpConfigServiceMaxUsers.setStatus("obsolete")
_FtpConfigTimeout_Type = Integer32
_FtpConfigTimeout_Object = MibScalar
ftpConfigTimeout = _FtpConfigTimeout_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 2, 1, 5, 1, 1, 3),
    _FtpConfigTimeout_Type()
)
ftpConfigTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ftpConfigTimeout.setStatus("obsolete")


class _FtpConfigNTPasswordEnabled_Type(Integer32):
    """Custom type ftpConfigNTPasswordEnabled based on Integer32"""
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
        *(("disabled", 2),
          ("enabled", 1),
          ("notavailable", 3),
          ("unknown", 4))
    )


_FtpConfigNTPasswordEnabled_Type.__name__ = "Integer32"
_FtpConfigNTPasswordEnabled_Object = MibScalar
ftpConfigNTPasswordEnabled = _FtpConfigNTPasswordEnabled_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 2, 1, 5, 1, 1, 4),
    _FtpConfigNTPasswordEnabled_Type()
)
ftpConfigNTPasswordEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ftpConfigNTPasswordEnabled.setStatus("obsolete")


class _FtpConfigNISPasswordEnabled_Type(Integer32):
    """Custom type ftpConfigNISPasswordEnabled based on Integer32"""
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
        *(("disabled", 2),
          ("enabled", 1),
          ("notavailable", 3),
          ("unknown", 4))
    )


_FtpConfigNISPasswordEnabled_Type.__name__ = "Integer32"
_FtpConfigNISPasswordEnabled_Object = MibScalar
ftpConfigNISPasswordEnabled = _FtpConfigNISPasswordEnabled_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 2, 1, 5, 1, 1, 5),
    _FtpConfigNISPasswordEnabled_Type()
)
ftpConfigNISPasswordEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ftpConfigNISPasswordEnabled.setStatus("obsolete")
_FtpAuditLoggingTable_Object = MibTable
ftpAuditLoggingTable = _FtpAuditLoggingTable_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 2, 1, 5, 1, 1, 6)
)
if mibBuilder.loadTexts:
    ftpAuditLoggingTable.setStatus("obsolete")
_FtpAuditLoggingEntry_Object = MibTableRow
ftpAuditLoggingEntry = _FtpAuditLoggingEntry_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 2, 1, 5, 1, 1, 6, 1)
)
ftpAuditLoggingEntry.setIndexNames(
    (0, "BLUEARC-TITAN-MIB", "ftpAuditLoggingEVS"),
)
if mibBuilder.loadTexts:
    ftpAuditLoggingEntry.setStatus("obsolete")


class _FtpAuditLoggingEVS_Type(Integer32):
    """Custom type ftpAuditLoggingEVS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_FtpAuditLoggingEVS_Type.__name__ = "Integer32"
_FtpAuditLoggingEVS_Object = MibTableColumn
ftpAuditLoggingEVS = _FtpAuditLoggingEVS_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 2, 1, 5, 1, 1, 6, 1, 1),
    _FtpAuditLoggingEVS_Type()
)
ftpAuditLoggingEVS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ftpAuditLoggingEVS.setStatus("obsolete")


class _FtpConfigAuditLogging_Type(Integer32):
    """Custom type ftpConfigAuditLogging based on Integer32"""
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
          ("unknown", 3))
    )


_FtpConfigAuditLogging_Type.__name__ = "Integer32"
_FtpConfigAuditLogging_Object = MibTableColumn
ftpConfigAuditLogging = _FtpConfigAuditLogging_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 2, 1, 5, 1, 1, 6, 1, 2),
    _FtpConfigAuditLogging_Type()
)
ftpConfigAuditLogging.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ftpConfigAuditLogging.setStatus("obsolete")
_FtpConfigAuditLogDeviceId_Type = Integer32
_FtpConfigAuditLogDeviceId_Object = MibTableColumn
ftpConfigAuditLogDeviceId = _FtpConfigAuditLogDeviceId_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 2, 1, 5, 1, 1, 6, 1, 3),
    _FtpConfigAuditLogDeviceId_Type()
)
ftpConfigAuditLogDeviceId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ftpConfigAuditLogDeviceId.setStatus("obsolete")
_FtpConfigAuditLogDirectory_Type = DisplayString
_FtpConfigAuditLogDirectory_Object = MibTableColumn
ftpConfigAuditLogDirectory = _FtpConfigAuditLogDirectory_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 2, 1, 5, 1, 1, 6, 1, 4),
    _FtpConfigAuditLogDirectory_Type()
)
ftpConfigAuditLogDirectory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ftpConfigAuditLogDirectory.setStatus("obsolete")
_FtpConfigAuditLogRecordsPerFile_Type = Unsigned32
_FtpConfigAuditLogRecordsPerFile_Object = MibTableColumn
ftpConfigAuditLogRecordsPerFile = _FtpConfigAuditLogRecordsPerFile_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 2, 1, 5, 1, 1, 6, 1, 5),
    _FtpConfigAuditLogRecordsPerFile_Type()
)
ftpConfigAuditLogRecordsPerFile.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ftpConfigAuditLogRecordsPerFile.setStatus("obsolete")
_FtpConfigAuditMaximumLogFiles_Type = Unsigned32
_FtpConfigAuditMaximumLogFiles_Object = MibTableColumn
ftpConfigAuditMaximumLogFiles = _FtpConfigAuditMaximumLogFiles_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 2, 1, 5, 1, 1, 6, 1, 6),
    _FtpConfigAuditMaximumLogFiles_Type()
)
ftpConfigAuditMaximumLogFiles.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ftpConfigAuditMaximumLogFiles.setStatus("obsolete")
_FtpMountpoints_ObjectIdentity = ObjectIdentity
ftpMountpoints = _FtpMountpoints_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11096, 6, 2, 1, 5, 1, 2)
)
_FtpMountpointNumber_Type = Integer32
_FtpMountpointNumber_Object = MibScalar
ftpMountpointNumber = _FtpMountpointNumber_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 2, 1, 5, 1, 2, 1),
    _FtpMountpointNumber_Type()
)
ftpMountpointNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ftpMountpointNumber.setStatus("obsolete")
_FtpMountpointTable_Object = MibTable
ftpMountpointTable = _FtpMountpointTable_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 2, 1, 5, 1, 2, 2)
)
if mibBuilder.loadTexts:
    ftpMountpointTable.setStatus("obsolete")
_FtpMountpointEntry_Object = MibTableRow
ftpMountpointEntry = _FtpMountpointEntry_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 2, 1, 5, 1, 2, 2, 1)
)
ftpMountpointEntry.setIndexNames(
    (0, "BLUEARC-TITAN-MIB", "ftpMountpointName"),
    (0, "BLUEARC-TITAN-MIB", "ftpMountpointEVS"),
)
if mibBuilder.loadTexts:
    ftpMountpointEntry.setStatus("obsolete")
_FtpMountpointName_Type = DisplayString
_FtpMountpointName_Object = MibTableColumn
ftpMountpointName = _FtpMountpointName_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 2, 1, 5, 1, 2, 2, 1, 1),
    _FtpMountpointName_Type()
)
ftpMountpointName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ftpMountpointName.setStatus("obsolete")


class _FtpMountpointEVS_Type(Integer32):
    """Custom type ftpMountpointEVS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_FtpMountpointEVS_Type.__name__ = "Integer32"
_FtpMountpointEVS_Object = MibTableColumn
ftpMountpointEVS = _FtpMountpointEVS_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 2, 1, 5, 1, 2, 2, 1, 2),
    _FtpMountpointEVS_Type()
)
ftpMountpointEVS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ftpMountpointEVS.setStatus("obsolete")


class _FtpMountpointDeviceId_Type(Integer32):
    """Custom type ftpMountpointDeviceId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_FtpMountpointDeviceId_Type.__name__ = "Integer32"
_FtpMountpointDeviceId_Object = MibTableColumn
ftpMountpointDeviceId = _FtpMountpointDeviceId_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 2, 1, 5, 1, 2, 2, 1, 3),
    _FtpMountpointDeviceId_Type()
)
ftpMountpointDeviceId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ftpMountpointDeviceId.setStatus("obsolete")
_FtpMountpointNumberUsers_Type = Unsigned32
_FtpMountpointNumberUsers_Object = MibTableColumn
ftpMountpointNumberUsers = _FtpMountpointNumberUsers_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 2, 1, 5, 1, 2, 2, 1, 4),
    _FtpMountpointNumberUsers_Type()
)
ftpMountpointNumberUsers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ftpMountpointNumberUsers.setStatus("obsolete")
_FtpUser_ObjectIdentity = ObjectIdentity
ftpUser = _FtpUser_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11096, 6, 2, 1, 5, 1, 3)
)
_FtpNumberUsers_Type = Integer32
_FtpNumberUsers_Object = MibScalar
ftpNumberUsers = _FtpNumberUsers_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 2, 1, 5, 1, 3, 1),
    _FtpNumberUsers_Type()
)
ftpNumberUsers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ftpNumberUsers.setStatus("obsolete")
_FtpUsersTable_Object = MibTable
ftpUsersTable = _FtpUsersTable_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 2, 1, 5, 1, 3, 2)
)
if mibBuilder.loadTexts:
    ftpUsersTable.setStatus("obsolete")
_FtpUsersEntry_Object = MibTableRow
ftpUsersEntry = _FtpUsersEntry_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 2, 1, 5, 1, 3, 2, 1)
)
ftpUsersEntry.setIndexNames(
    (0, "BLUEARC-TITAN-MIB", "ftpUsersName"),
    (0, "BLUEARC-TITAN-MIB", "ftpUsersEVS"),
)
if mibBuilder.loadTexts:
    ftpUsersEntry.setStatus("obsolete")
_FtpUsersName_Type = DisplayString
_FtpUsersName_Object = MibTableColumn
ftpUsersName = _FtpUsersName_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 2, 1, 5, 1, 3, 2, 1, 1),
    _FtpUsersName_Type()
)
ftpUsersName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ftpUsersName.setStatus("obsolete")


class _FtpUsersEVS_Type(Integer32):
    """Custom type ftpUsersEVS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_FtpUsersEVS_Type.__name__ = "Integer32"
_FtpUsersEVS_Object = MibTableColumn
ftpUsersEVS = _FtpUsersEVS_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 2, 1, 5, 1, 3, 2, 1, 2),
    _FtpUsersEVS_Type()
)
ftpUsersEVS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ftpUsersEVS.setStatus("obsolete")


class _FtpUsersMountPointExists_Type(Integer32):
    """Custom type ftpUsersMountPointExists based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("doesnotExist", 2),
          ("exists", 1))
    )


_FtpUsersMountPointExists_Type.__name__ = "Integer32"
_FtpUsersMountPointExists_Object = MibTableColumn
ftpUsersMountPointExists = _FtpUsersMountPointExists_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 2, 1, 5, 1, 3, 2, 1, 3),
    _FtpUsersMountPointExists_Type()
)
ftpUsersMountPointExists.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ftpUsersMountPointExists.setStatus("obsolete")
_FtpUsersMountPoint_Type = DisplayString
_FtpUsersMountPoint_Object = MibTableColumn
ftpUsersMountPoint = _FtpUsersMountPoint_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 2, 1, 5, 1, 3, 2, 1, 4),
    _FtpUsersMountPoint_Type()
)
ftpUsersMountPoint.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ftpUsersMountPoint.setStatus("obsolete")
_FtpUsersMountInitDirectory_Type = DisplayString
_FtpUsersMountInitDirectory_Object = MibTableColumn
ftpUsersMountInitDirectory = _FtpUsersMountInitDirectory_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 2, 1, 5, 1, 3, 2, 1, 5),
    _FtpUsersMountInitDirectory_Type()
)
ftpUsersMountInitDirectory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ftpUsersMountInitDirectory.setStatus("obsolete")
_FtpStatistics_ObjectIdentity = ObjectIdentity
ftpStatistics = _FtpStatistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11096, 6, 2, 1, 5, 1, 4)
)
_FtpStatisticsTable_Object = MibTable
ftpStatisticsTable = _FtpStatisticsTable_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 2, 1, 5, 1, 4, 1)
)
if mibBuilder.loadTexts:
    ftpStatisticsTable.setStatus("current")
_FtpStatisticsEntry_Object = MibTableRow
ftpStatisticsEntry = _FtpStatisticsEntry_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 2, 1, 5, 1, 4, 1, 1)
)
ftpStatisticsEntry.setIndexNames(
    (0, "BLUEARC-TITAN-MIB", "ftpStatisticsClusterNode"),
)
if mibBuilder.loadTexts:
    ftpStatisticsEntry.setStatus("current")


class _FtpStatisticsClusterNode_Type(Integer32):
    """Custom type ftpStatisticsClusterNode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_FtpStatisticsClusterNode_Type.__name__ = "Integer32"
_FtpStatisticsClusterNode_Object = MibTableColumn
ftpStatisticsClusterNode = _FtpStatisticsClusterNode_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 2, 1, 5, 1, 4, 1, 1, 1),
    _FtpStatisticsClusterNode_Type()
)
ftpStatisticsClusterNode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ftpStatisticsClusterNode.setStatus("current")
_FtpStatisticsTotalSess_Type = Counter32
_FtpStatisticsTotalSess_Object = MibTableColumn
ftpStatisticsTotalSess = _FtpStatisticsTotalSess_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 2, 1, 5, 1, 4, 1, 1, 2),
    _FtpStatisticsTotalSess_Type()
)
ftpStatisticsTotalSess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ftpStatisticsTotalSess.setStatus("current")
_FtpStatisticsTotalFtpXferIn_Type = Counter32
_FtpStatisticsTotalFtpXferIn_Object = MibTableColumn
ftpStatisticsTotalFtpXferIn = _FtpStatisticsTotalFtpXferIn_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 2, 1, 5, 1, 4, 1, 1, 3),
    _FtpStatisticsTotalFtpXferIn_Type()
)
ftpStatisticsTotalFtpXferIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ftpStatisticsTotalFtpXferIn.setStatus("current")
_FtpStatisticsBytesTotalXferIn_Type = Counter64
_FtpStatisticsBytesTotalXferIn_Object = MibTableColumn
ftpStatisticsBytesTotalXferIn = _FtpStatisticsBytesTotalXferIn_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 2, 1, 5, 1, 4, 1, 1, 4),
    _FtpStatisticsBytesTotalXferIn_Type()
)
ftpStatisticsBytesTotalXferIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ftpStatisticsBytesTotalXferIn.setStatus("current")
_FtpStatisticsTotalFtpXferOut_Type = Counter32
_FtpStatisticsTotalFtpXferOut_Object = MibTableColumn
ftpStatisticsTotalFtpXferOut = _FtpStatisticsTotalFtpXferOut_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 2, 1, 5, 1, 4, 1, 1, 5),
    _FtpStatisticsTotalFtpXferOut_Type()
)
ftpStatisticsTotalFtpXferOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ftpStatisticsTotalFtpXferOut.setStatus("current")
_FtpStatisticsBytesTotalXferOut_Type = Counter64
_FtpStatisticsBytesTotalXferOut_Object = MibTableColumn
ftpStatisticsBytesTotalXferOut = _FtpStatisticsBytesTotalXferOut_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 2, 1, 5, 1, 4, 1, 1, 6),
    _FtpStatisticsBytesTotalXferOut_Type()
)
ftpStatisticsBytesTotalXferOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ftpStatisticsBytesTotalXferOut.setStatus("current")
_FtpStatisticsTotalFtpCommands_Type = Counter32
_FtpStatisticsTotalFtpCommands_Object = MibTableColumn
ftpStatisticsTotalFtpCommands = _FtpStatisticsTotalFtpCommands_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 2, 1, 5, 1, 4, 1, 1, 7),
    _FtpStatisticsTotalFtpCommands_Type()
)
ftpStatisticsTotalFtpCommands.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ftpStatisticsTotalFtpCommands.setStatus("current")
_FtpStatisticsTotalFtpReplies_Type = Counter32
_FtpStatisticsTotalFtpReplies_Object = MibTableColumn
ftpStatisticsTotalFtpReplies = _FtpStatisticsTotalFtpReplies_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 2, 1, 5, 1, 4, 1, 1, 8),
    _FtpStatisticsTotalFtpReplies_Type()
)
ftpStatisticsTotalFtpReplies.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ftpStatisticsTotalFtpReplies.setStatus("current")
_FtpStatisticsTotalBytesCommands_Type = Counter64
_FtpStatisticsTotalBytesCommands_Object = MibTableColumn
ftpStatisticsTotalBytesCommands = _FtpStatisticsTotalBytesCommands_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 2, 1, 5, 1, 4, 1, 1, 9),
    _FtpStatisticsTotalBytesCommands_Type()
)
ftpStatisticsTotalBytesCommands.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ftpStatisticsTotalBytesCommands.setStatus("current")
_FtpStatisticsTotalBytesReplies_Type = Counter64
_FtpStatisticsTotalBytesReplies_Object = MibTableColumn
ftpStatisticsTotalBytesReplies = _FtpStatisticsTotalBytesReplies_Object(
    (1, 3, 6, 1, 4, 1, 11096, 6, 2, 1, 5, 1, 4, 1, 1, 10),
    _FtpStatisticsTotalBytesReplies_Type()
)
ftpStatisticsTotalBytesReplies.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ftpStatisticsTotalBytesReplies.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "BLUEARC-TITAN-MIB",
    **{"blueArcTitan": blueArcTitan,
       "blueArcTitanObjs": blueArcTitanObjs,
       "systemTitan": systemTitan,
       "storageTitan": storageTitan,
       "virtualVolumesTitan": virtualVolumesTitan,
       "virtualVolumeTitanNumber": virtualVolumeTitanNumber,
       "virtualVolumeTitanTable": virtualVolumeTitanTable,
       "virtualVolumeTitanEntry": virtualVolumeTitanEntry,
       "virtualVolumeTitanSpanId": virtualVolumeTitanSpanId,
       "virtualVolumeTitanName": virtualVolumeTitanName,
       "virtualVolumeTitanPath": virtualVolumeTitanPath,
       "virtualVolumeTitanEmailNumber": virtualVolumeTitanEmailNumber,
       "virtualVolumeTitanQuotaNumber": virtualVolumeTitanQuotaNumber,
       "virtualVolumeTitanEmailTable": virtualVolumeTitanEmailTable,
       "virtualVolumeTitanEmailEntry": virtualVolumeTitanEmailEntry,
       "virtualVolumeTitanEmailAddress": virtualVolumeTitanEmailAddress,
       "virtualVolumeTitanQuotaTemplateTable": virtualVolumeTitanQuotaTemplateTable,
       "virtualVolumeTitanQuotaTemplateEntry": virtualVolumeTitanQuotaTemplateEntry,
       "virtualVolumeQuotaTemplateTargetType": virtualVolumeQuotaTemplateTargetType,
       "virtualVolumeQuotaTemplateIgnoreWellKnownGroups": virtualVolumeQuotaTemplateIgnoreWellKnownGroups,
       "virtualVolumeTitanQuotaTemplateUsageLimit": virtualVolumeTitanQuotaTemplateUsageLimit,
       "virtualVolumeTitanQuotaTemplateUsageHardLimit": virtualVolumeTitanQuotaTemplateUsageHardLimit,
       "virtualVolumeTitanQuotaTemplateUsageReset": virtualVolumeTitanQuotaTemplateUsageReset,
       "virtualVolumeTitanQuotaTemplateUsageWarning": virtualVolumeTitanQuotaTemplateUsageWarning,
       "virtualVolumeTitanQuotaTemplateUsageCritical": virtualVolumeTitanQuotaTemplateUsageCritical,
       "virtualVolumeTitanQuotaTemplateFileCountLimit": virtualVolumeTitanQuotaTemplateFileCountLimit,
       "virtualVolumeTitanQuotaTemplateFileCountHardLimit": virtualVolumeTitanQuotaTemplateFileCountHardLimit,
       "virtualVolumeTitanQuotaTemplateFileCountReset": virtualVolumeTitanQuotaTemplateFileCountReset,
       "virtualVolumeTitanQuotaTemplateFileCountWarning": virtualVolumeTitanQuotaTemplateFileCountWarning,
       "virtualVolumeTitanQuotaTemplateFileCountCritical": virtualVolumeTitanQuotaTemplateFileCountCritical,
       "virtualVolumeTitanQuotaTable": virtualVolumeTitanQuotaTable,
       "virtualVolumeTitanQuotaEntry": virtualVolumeTitanQuotaEntry,
       "virtualVolumeTitanQuotaTarget": virtualVolumeTitanQuotaTarget,
       "virtualVolumeTitanQuotaType": virtualVolumeTitanQuotaType,
       "virtualVolumeTitanQuotaTargetType": virtualVolumeTitanQuotaTargetType,
       "virtualVolumeTitanQuotaUsage": virtualVolumeTitanQuotaUsage,
       "virtualVolumeTitanQuotaFileCount": virtualVolumeTitanQuotaFileCount,
       "virtualVolumeTitanQuotaUsageLimit": virtualVolumeTitanQuotaUsageLimit,
       "virtualVolumeTitanQuotaUsageHardLimit": virtualVolumeTitanQuotaUsageHardLimit,
       "virtualVolumeTitanQuotaUsageReset": virtualVolumeTitanQuotaUsageReset,
       "virtualVolumeTitanQuotaUsageWarning": virtualVolumeTitanQuotaUsageWarning,
       "virtualVolumeTitanQuotaUsageCritical": virtualVolumeTitanQuotaUsageCritical,
       "virtualVolumeTitanQuotaFileCountLimit": virtualVolumeTitanQuotaFileCountLimit,
       "virtualVolumeTitanQuotaFileCountHardLimit": virtualVolumeTitanQuotaFileCountHardLimit,
       "virtualVolumeTitanQuotaFileCountReset": virtualVolumeTitanQuotaFileCountReset,
       "virtualVolumeTitanQuotaFileCountWarning": virtualVolumeTitanQuotaFileCountWarning,
       "virtualVolumeTitanQuotaFileCountCritical": virtualVolumeTitanQuotaFileCountCritical,
       "virtualVolumeTitanQuotaDefaultTable": virtualVolumeTitanQuotaDefaultTable,
       "virtualVolumeTitanQuotaDefaultEntry": virtualVolumeTitanQuotaDefaultEntry,
       "virtualVolumeQuotaDefaultTargetType": virtualVolumeQuotaDefaultTargetType,
       "virtualVolumeQuotaDefaultIgnoreWellKnownGroups": virtualVolumeQuotaDefaultIgnoreWellKnownGroups,
       "virtualVolumeTitanQuotaDefaultUsageLimit": virtualVolumeTitanQuotaDefaultUsageLimit,
       "virtualVolumeTitanQuotaDefaultUsageHardLimit": virtualVolumeTitanQuotaDefaultUsageHardLimit,
       "virtualVolumeTitanQuotaDefaultUsageReset": virtualVolumeTitanQuotaDefaultUsageReset,
       "virtualVolumeTitanQuotaDefaultUsageWarning": virtualVolumeTitanQuotaDefaultUsageWarning,
       "virtualVolumeTitanQuotaDefaultUsageCritical": virtualVolumeTitanQuotaDefaultUsageCritical,
       "virtualVolumeTitanQuotaDefaultFileCountLimit": virtualVolumeTitanQuotaDefaultFileCountLimit,
       "virtualVolumeTitanQuotaDefaultFileCountHardLimit": virtualVolumeTitanQuotaDefaultFileCountHardLimit,
       "virtualVolumeTitanQuotaDefaultFileCountReset": virtualVolumeTitanQuotaDefaultFileCountReset,
       "virtualVolumeTitanQuotaDefaultFileCountWarning": virtualVolumeTitanQuotaDefaultFileCountWarning,
       "virtualVolumeTitanQuotaDefaultFileCountCritical": virtualVolumeTitanQuotaDefaultFileCountCritical,
       "virtualVolumeTitanQuotasTable": virtualVolumeTitanQuotasTable,
       "virtualVolumeTitanQuotasEntry": virtualVolumeTitanQuotasEntry,
       "virtualVolumeTitanQuotasTarget": virtualVolumeTitanQuotasTarget,
       "virtualVolumeTitanQuotasType": virtualVolumeTitanQuotasType,
       "virtualVolumeTitanQuotasTargetType": virtualVolumeTitanQuotasTargetType,
       "virtualVolumeTitanQuotasUsage": virtualVolumeTitanQuotasUsage,
       "virtualVolumeTitanQuotasFileCount": virtualVolumeTitanQuotasFileCount,
       "virtualVolumeTitanQuotasUsageLimit": virtualVolumeTitanQuotasUsageLimit,
       "virtualVolumeTitanQuotasUsageHardLimit": virtualVolumeTitanQuotasUsageHardLimit,
       "virtualVolumeTitanQuotasUsageReset": virtualVolumeTitanQuotasUsageReset,
       "virtualVolumeTitanQuotasUsageWarning": virtualVolumeTitanQuotasUsageWarning,
       "virtualVolumeTitanQuotasUsageCritical": virtualVolumeTitanQuotasUsageCritical,
       "virtualVolumeTitanQuotasFileCountLimit": virtualVolumeTitanQuotasFileCountLimit,
       "virtualVolumeTitanQuotasFileCountHardLimit": virtualVolumeTitanQuotasFileCountHardLimit,
       "virtualVolumeTitanQuotasFileCountReset": virtualVolumeTitanQuotasFileCountReset,
       "virtualVolumeTitanQuotasFileCountWarning": virtualVolumeTitanQuotasFileCountWarning,
       "virtualVolumeTitanQuotasFileCountCritical": virtualVolumeTitanQuotasFileCountCritical,
       "nvram": nvram,
       "nvramSize": nvramSize,
       "nvramMaximumUsed": nvramMaximumUsed,
       "nvramTotalCurrentUsage": nvramTotalCurrentUsage,
       "nvramNumber": nvramNumber,
       "nvramTable": nvramTable,
       "nvramEntry": nvramEntry,
       "spanId": spanId,
       "nvramCurrentUsage": nvramCurrentUsage,
       "nvramNumberCheckpoints": nvramNumberCheckpoints,
       "nvramNumberActivityCheckpoints": nvramNumberActivityCheckpoints,
       "nvramPoolTable": nvramPoolTable,
       "nvramPoolEntry": nvramPoolEntry,
       "clusterNodeId": clusterNodeId,
       "nvramPoolSize": nvramPoolSize,
       "nvramPoolMaximumUsed": nvramPoolMaximumUsed,
       "nvramPoolTotalCurrentUsage": nvramPoolTotalCurrentUsage,
       "networkTitan": networkTitan,
       "ethernetTitan": ethernetTitan,
       "linkAggregation": linkAggregation,
       "lagNumber": lagNumber,
       "lagTable": lagTable,
       "lagEntry": lagEntry,
       "lagName": lagName,
       "linkedInterfaces": linkedInterfaces,
       "mgmntTitan": mgmntTitan,
       "packageMgmnt": packageMgmnt,
       "packageNumber": packageNumber,
       "packageTable": packageTable,
       "packageEntry": packageEntry,
       "packageName": packageName,
       "packageDate": packageDate,
       "packageSize": packageSize,
       "packageDefault": packageDefault,
       "packageCurrent": packageCurrent,
       "packageFreeSpace": packageFreeSpace,
       "fileProtocolTitan": fileProtocolTitan,
       "ftpTitan": ftpTitan,
       "ftpConfig": ftpConfig,
       "ftpConfigServiceEnabled": ftpConfigServiceEnabled,
       "ftpConfigServiceMaxUsers": ftpConfigServiceMaxUsers,
       "ftpConfigTimeout": ftpConfigTimeout,
       "ftpConfigNTPasswordEnabled": ftpConfigNTPasswordEnabled,
       "ftpConfigNISPasswordEnabled": ftpConfigNISPasswordEnabled,
       "ftpAuditLoggingTable": ftpAuditLoggingTable,
       "ftpAuditLoggingEntry": ftpAuditLoggingEntry,
       "ftpAuditLoggingEVS": ftpAuditLoggingEVS,
       "ftpConfigAuditLogging": ftpConfigAuditLogging,
       "ftpConfigAuditLogDeviceId": ftpConfigAuditLogDeviceId,
       "ftpConfigAuditLogDirectory": ftpConfigAuditLogDirectory,
       "ftpConfigAuditLogRecordsPerFile": ftpConfigAuditLogRecordsPerFile,
       "ftpConfigAuditMaximumLogFiles": ftpConfigAuditMaximumLogFiles,
       "ftpMountpoints": ftpMountpoints,
       "ftpMountpointNumber": ftpMountpointNumber,
       "ftpMountpointTable": ftpMountpointTable,
       "ftpMountpointEntry": ftpMountpointEntry,
       "ftpMountpointName": ftpMountpointName,
       "ftpMountpointEVS": ftpMountpointEVS,
       "ftpMountpointDeviceId": ftpMountpointDeviceId,
       "ftpMountpointNumberUsers": ftpMountpointNumberUsers,
       "ftpUser": ftpUser,
       "ftpNumberUsers": ftpNumberUsers,
       "ftpUsersTable": ftpUsersTable,
       "ftpUsersEntry": ftpUsersEntry,
       "ftpUsersName": ftpUsersName,
       "ftpUsersEVS": ftpUsersEVS,
       "ftpUsersMountPointExists": ftpUsersMountPointExists,
       "ftpUsersMountPoint": ftpUsersMountPoint,
       "ftpUsersMountInitDirectory": ftpUsersMountInitDirectory,
       "ftpStatistics": ftpStatistics,
       "ftpStatisticsTable": ftpStatisticsTable,
       "ftpStatisticsEntry": ftpStatisticsEntry,
       "ftpStatisticsClusterNode": ftpStatisticsClusterNode,
       "ftpStatisticsTotalSess": ftpStatisticsTotalSess,
       "ftpStatisticsTotalFtpXferIn": ftpStatisticsTotalFtpXferIn,
       "ftpStatisticsBytesTotalXferIn": ftpStatisticsBytesTotalXferIn,
       "ftpStatisticsTotalFtpXferOut": ftpStatisticsTotalFtpXferOut,
       "ftpStatisticsBytesTotalXferOut": ftpStatisticsBytesTotalXferOut,
       "ftpStatisticsTotalFtpCommands": ftpStatisticsTotalFtpCommands,
       "ftpStatisticsTotalFtpReplies": ftpStatisticsTotalFtpReplies,
       "ftpStatisticsTotalBytesCommands": ftpStatisticsTotalBytesCommands,
       "ftpStatisticsTotalBytesReplies": ftpStatisticsTotalBytesReplies}
)
