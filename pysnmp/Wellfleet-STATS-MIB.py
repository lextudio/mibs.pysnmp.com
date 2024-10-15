# SNMP MIB module (Wellfleet-STATS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/Wellfleet-STATS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:17:10 2024
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

(wfStatsDcGroup,) = mibBuilder.importSymbols(
    "Wellfleet-COMMON-MIB",
    "wfStatsDcGroup")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_WfStatsDc_ObjectIdentity = ObjectIdentity
wfStatsDc = _WfStatsDc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 17, 1)
)


class _WfStatsDcDisable_Type(Integer32):
    """Custom type wfStatsDcDisable based on Integer32"""
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


_WfStatsDcDisable_Type.__name__ = "Integer32"
_WfStatsDcDisable_Object = MibScalar
wfStatsDcDisable = _WfStatsDcDisable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 17, 1, 1),
    _WfStatsDcDisable_Type()
)
wfStatsDcDisable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfStatsDcDisable.setStatus("mandatory")


class _WfStatsDcVolume_Type(Integer32):
    """Custom type wfStatsDcVolume based on Integer32"""
    defaultValue = 4

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 14),
    )


_WfStatsDcVolume_Type.__name__ = "Integer32"
_WfStatsDcVolume_Object = MibScalar
wfStatsDcVolume = _WfStatsDcVolume_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 17, 1, 2),
    _WfStatsDcVolume_Type()
)
wfStatsDcVolume.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfStatsDcVolume.setStatus("mandatory")
_WfStatsDcFilePrefix_Type = DisplayString
_WfStatsDcFilePrefix_Object = MibScalar
wfStatsDcFilePrefix = _WfStatsDcFilePrefix_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 17, 1, 3),
    _WfStatsDcFilePrefix_Type()
)
wfStatsDcFilePrefix.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfStatsDcFilePrefix.setStatus("mandatory")


class _WfStatsDcUpdateInterval_Type(Integer32):
    """Custom type wfStatsDcUpdateInterval based on Integer32"""
    defaultValue = 60

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 2147483647),
    )


_WfStatsDcUpdateInterval_Type.__name__ = "Integer32"
_WfStatsDcUpdateInterval_Object = MibScalar
wfStatsDcUpdateInterval = _WfStatsDcUpdateInterval_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 17, 1, 4),
    _WfStatsDcUpdateInterval_Type()
)
wfStatsDcUpdateInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfStatsDcUpdateInterval.setStatus("obsolete")


class _WfStatsDcStoreInterval_Type(Integer32):
    """Custom type wfStatsDcStoreInterval based on Integer32"""
    defaultValue = 60

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 2147483647),
    )


_WfStatsDcStoreInterval_Type.__name__ = "Integer32"
_WfStatsDcStoreInterval_Object = MibScalar
wfStatsDcStoreInterval = _WfStatsDcStoreInterval_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 17, 1, 5),
    _WfStatsDcStoreInterval_Type()
)
wfStatsDcStoreInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfStatsDcStoreInterval.setStatus("mandatory")
_WfStatsDcUpdateData_Type = Integer32
_WfStatsDcUpdateData_Object = MibScalar
wfStatsDcUpdateData = _WfStatsDcUpdateData_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 17, 1, 6),
    _WfStatsDcUpdateData_Type()
)
wfStatsDcUpdateData.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfStatsDcUpdateData.setStatus("obsolete")
_WfStatsDcStoreData_Type = Integer32
_WfStatsDcStoreData_Object = MibScalar
wfStatsDcStoreData = _WfStatsDcStoreData_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 17, 1, 7),
    _WfStatsDcStoreData_Type()
)
wfStatsDcStoreData.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfStatsDcStoreData.setStatus("mandatory")
_WfStatsDcSwitchId_Type = DisplayString
_WfStatsDcSwitchId_Object = MibScalar
wfStatsDcSwitchId = _WfStatsDcSwitchId_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 17, 1, 8),
    _WfStatsDcSwitchId_Type()
)
wfStatsDcSwitchId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfStatsDcSwitchId.setStatus("mandatory")


class _WfStatsDcEnableAll_Type(Integer32):
    """Custom type wfStatsDcEnableAll based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 1))
    )


_WfStatsDcEnableAll_Type.__name__ = "Integer32"
_WfStatsDcEnableAll_Object = MibScalar
wfStatsDcEnableAll = _WfStatsDcEnableAll_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 17, 1, 9),
    _WfStatsDcEnableAll_Type()
)
wfStatsDcEnableAll.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfStatsDcEnableAll.setStatus("mandatory")


class _WfStatsDcMaxNumFiles_Type(Integer32):
    """Custom type wfStatsDcMaxNumFiles based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 144),
    )


_WfStatsDcMaxNumFiles_Type.__name__ = "Integer32"
_WfStatsDcMaxNumFiles_Object = MibScalar
wfStatsDcMaxNumFiles = _WfStatsDcMaxNumFiles_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 17, 1, 10),
    _WfStatsDcMaxNumFiles_Type()
)
wfStatsDcMaxNumFiles.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfStatsDcMaxNumFiles.setStatus("mandatory")


class _WfStatsDcFrVcDisable_Type(Integer32):
    """Custom type wfStatsDcFrVcDisable based on Integer32"""
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


_WfStatsDcFrVcDisable_Type.__name__ = "Integer32"
_WfStatsDcFrVcDisable_Object = MibScalar
wfStatsDcFrVcDisable = _WfStatsDcFrVcDisable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 17, 1, 11),
    _WfStatsDcFrVcDisable_Type()
)
wfStatsDcFrVcDisable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfStatsDcFrVcDisable.setStatus("mandatory")


class _WfStatsDcState_Type(Integer32):
    """Custom type wfStatsDcState based on Integer32"""
    defaultValue = 4

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
        *(("down", 2),
          ("init", 3),
          ("notpresent", 4),
          ("up", 1))
    )


_WfStatsDcState_Type.__name__ = "Integer32"
_WfStatsDcState_Object = MibScalar
wfStatsDcState = _WfStatsDcState_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 17, 1, 12),
    _WfStatsDcState_Type()
)
wfStatsDcState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfStatsDcState.setStatus("mandatory")


class _WfStatsDcHssiFields_Type(Gauge32):
    """Custom type wfStatsDcHssiFields based on Gauge32"""
    defaultValue = 4278190080


_WfStatsDcHssiFields_Object = MibScalar
wfStatsDcHssiFields = _WfStatsDcHssiFields_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 17, 1, 13),
    _WfStatsDcHssiFields_Type()
)
wfStatsDcHssiFields.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfStatsDcHssiFields.setStatus("mandatory")


class _WfStatsDcSyncFields_Type(Gauge32):
    """Custom type wfStatsDcSyncFields based on Gauge32"""
    defaultValue = 4278190080


_WfStatsDcSyncFields_Object = MibScalar
wfStatsDcSyncFields = _WfStatsDcSyncFields_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 17, 1, 14),
    _WfStatsDcSyncFields_Type()
)
wfStatsDcSyncFields.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfStatsDcSyncFields.setStatus("mandatory")


class _WfStatsDcDs1E1Fields_Type(Gauge32):
    """Custom type wfStatsDcDs1E1Fields based on Gauge32"""
    defaultValue = 4294836224


_WfStatsDcDs1E1Fields_Object = MibScalar
wfStatsDcDs1E1Fields = _WfStatsDcDs1E1Fields_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 17, 1, 15),
    _WfStatsDcDs1E1Fields_Type()
)
wfStatsDcDs1E1Fields.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfStatsDcDs1E1Fields.setStatus("mandatory")


class _WfStatsDcFrSwVcFields_Type(Gauge32):
    """Custom type wfStatsDcFrSwVcFields based on Gauge32"""
    defaultValue = 4294966272


_WfStatsDcFrSwVcFields_Object = MibScalar
wfStatsDcFrSwVcFields = _WfStatsDcFrSwVcFields_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 17, 1, 16),
    _WfStatsDcFrSwVcFields_Type()
)
wfStatsDcFrSwVcFields.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfStatsDcFrSwVcFields.setStatus("mandatory")


class _WfStatsDcCctCngcFields_Type(Gauge32):
    """Custom type wfStatsDcCctCngcFields based on Gauge32"""
    defaultValue = 4294901760


_WfStatsDcCctCngcFields_Object = MibScalar
wfStatsDcCctCngcFields = _WfStatsDcCctCngcFields_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 17, 1, 17),
    _WfStatsDcCctCngcFields_Type()
)
wfStatsDcCctCngcFields.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfStatsDcCctCngcFields.setStatus("mandatory")
_WfStatsDcFddiFields_Type = OctetString
_WfStatsDcFddiFields_Object = MibScalar
wfStatsDcFddiFields = _WfStatsDcFddiFields_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 17, 1, 18),
    _WfStatsDcFddiFields_Type()
)
wfStatsDcFddiFields.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfStatsDcFddiFields.setStatus("mandatory")


class _WfStatsDcCctCngcDisable_Type(Integer32):
    """Custom type wfStatsDcCctCngcDisable based on Integer32"""
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


_WfStatsDcCctCngcDisable_Type.__name__ = "Integer32"
_WfStatsDcCctCngcDisable_Object = MibScalar
wfStatsDcCctCngcDisable = _WfStatsDcCctCngcDisable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 17, 1, 19),
    _WfStatsDcCctCngcDisable_Type()
)
wfStatsDcCctCngcDisable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfStatsDcCctCngcDisable.setStatus("mandatory")


class _WfStatsDcLbcFileDisable_Type(Integer32):
    """Custom type wfStatsDcLbcFileDisable based on Integer32"""
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


_WfStatsDcLbcFileDisable_Type.__name__ = "Integer32"
_WfStatsDcLbcFileDisable_Object = MibScalar
wfStatsDcLbcFileDisable = _WfStatsDcLbcFileDisable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 17, 1, 20),
    _WfStatsDcLbcFileDisable_Type()
)
wfStatsDcLbcFileDisable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfStatsDcLbcFileDisable.setStatus("mandatory")


class _WfStatsDcAtmzPhyFields_Type(Gauge32):
    """Custom type wfStatsDcAtmzPhyFields based on Gauge32"""
    defaultValue = 4294967264


_WfStatsDcAtmzPhyFields_Object = MibScalar
wfStatsDcAtmzPhyFields = _WfStatsDcAtmzPhyFields_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 17, 1, 21),
    _WfStatsDcAtmzPhyFields_Type()
)
wfStatsDcAtmzPhyFields.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfStatsDcAtmzPhyFields.setStatus("mandatory")
_WfStatsDcMediaTable_Object = MibTable
wfStatsDcMediaTable = _WfStatsDcMediaTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 17, 2)
)
if mibBuilder.loadTexts:
    wfStatsDcMediaTable.setStatus("mandatory")
_WfStatsDcMediaEntry_Object = MibTableRow
wfStatsDcMediaEntry = _WfStatsDcMediaEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 17, 2, 1)
)
wfStatsDcMediaEntry.setIndexNames(
    (0, "Wellfleet-STATS-MIB", "wfStatsDcMediaLineNumber"),
)
if mibBuilder.loadTexts:
    wfStatsDcMediaEntry.setStatus("mandatory")


class _WfStatsDcMediaDelete_Type(Integer32):
    """Custom type wfStatsDcMediaDelete based on Integer32"""
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


_WfStatsDcMediaDelete_Type.__name__ = "Integer32"
_WfStatsDcMediaDelete_Object = MibTableColumn
wfStatsDcMediaDelete = _WfStatsDcMediaDelete_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 17, 2, 1, 1),
    _WfStatsDcMediaDelete_Type()
)
wfStatsDcMediaDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfStatsDcMediaDelete.setStatus("mandatory")
_WfStatsDcMediaLineNumber_Type = Integer32
_WfStatsDcMediaLineNumber_Object = MibTableColumn
wfStatsDcMediaLineNumber = _WfStatsDcMediaLineNumber_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 17, 2, 1, 2),
    _WfStatsDcMediaLineNumber_Type()
)
wfStatsDcMediaLineNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfStatsDcMediaLineNumber.setStatus("mandatory")
_WfStatsDcLbcTable_Object = MibTable
wfStatsDcLbcTable = _WfStatsDcLbcTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 17, 3)
)
if mibBuilder.loadTexts:
    wfStatsDcLbcTable.setStatus("mandatory")
_WfStatsDcLbcEntry_Object = MibTableRow
wfStatsDcLbcEntry = _WfStatsDcLbcEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 17, 3, 1)
)
wfStatsDcLbcEntry.setIndexNames(
    (0, "Wellfleet-STATS-MIB", "wfStatsDcLbcLineNumber"),
)
if mibBuilder.loadTexts:
    wfStatsDcLbcEntry.setStatus("mandatory")


class _WfStatsDcLbcDelete_Type(Integer32):
    """Custom type wfStatsDcLbcDelete based on Integer32"""
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


_WfStatsDcLbcDelete_Type.__name__ = "Integer32"
_WfStatsDcLbcDelete_Object = MibTableColumn
wfStatsDcLbcDelete = _WfStatsDcLbcDelete_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 17, 3, 1, 1),
    _WfStatsDcLbcDelete_Type()
)
wfStatsDcLbcDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfStatsDcLbcDelete.setStatus("mandatory")


class _WfStatsDcLbcDisable_Type(Integer32):
    """Custom type wfStatsDcLbcDisable based on Integer32"""
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


_WfStatsDcLbcDisable_Type.__name__ = "Integer32"
_WfStatsDcLbcDisable_Object = MibTableColumn
wfStatsDcLbcDisable = _WfStatsDcLbcDisable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 17, 3, 1, 2),
    _WfStatsDcLbcDisable_Type()
)
wfStatsDcLbcDisable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfStatsDcLbcDisable.setStatus("mandatory")
_WfStatsDcLbcLineNumber_Type = Integer32
_WfStatsDcLbcLineNumber_Object = MibTableColumn
wfStatsDcLbcLineNumber = _WfStatsDcLbcLineNumber_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 17, 3, 1, 3),
    _WfStatsDcLbcLineNumber_Type()
)
wfStatsDcLbcLineNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfStatsDcLbcLineNumber.setStatus("mandatory")


class _WfStatsDcLbcUpdateInterval_Type(Integer32):
    """Custom type wfStatsDcLbcUpdateInterval based on Integer32"""
    defaultValue = 5

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 60),
    )


_WfStatsDcLbcUpdateInterval_Type.__name__ = "Integer32"
_WfStatsDcLbcUpdateInterval_Object = MibTableColumn
wfStatsDcLbcUpdateInterval = _WfStatsDcLbcUpdateInterval_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 17, 3, 1, 4),
    _WfStatsDcLbcUpdateInterval_Type()
)
wfStatsDcLbcUpdateInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfStatsDcLbcUpdateInterval.setStatus("mandatory")


class _WfStatsDcLbcState_Type(Integer32):
    """Custom type wfStatsDcLbcState based on Integer32"""
    defaultValue = 4

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
        *(("down", 2),
          ("init", 3),
          ("notpresent", 4),
          ("up", 1))
    )


_WfStatsDcLbcState_Type.__name__ = "Integer32"
_WfStatsDcLbcState_Object = MibTableColumn
wfStatsDcLbcState = _WfStatsDcLbcState_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 17, 3, 1, 5),
    _WfStatsDcLbcState_Type()
)
wfStatsDcLbcState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfStatsDcLbcState.setStatus("mandatory")


class _WfStatsDcLbcRxMaxDelta0_Type(Gauge32):
    """Custom type wfStatsDcLbcRxMaxDelta0 based on Gauge32"""
    defaultValue = 0


_WfStatsDcLbcRxMaxDelta0_Object = MibTableColumn
wfStatsDcLbcRxMaxDelta0 = _WfStatsDcLbcRxMaxDelta0_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 17, 3, 1, 6),
    _WfStatsDcLbcRxMaxDelta0_Type()
)
wfStatsDcLbcRxMaxDelta0.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfStatsDcLbcRxMaxDelta0.setStatus("mandatory")


class _WfStatsDcLbcTxMaxDelta0_Type(Gauge32):
    """Custom type wfStatsDcLbcTxMaxDelta0 based on Gauge32"""
    defaultValue = 0


_WfStatsDcLbcTxMaxDelta0_Object = MibTableColumn
wfStatsDcLbcTxMaxDelta0 = _WfStatsDcLbcTxMaxDelta0_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 17, 3, 1, 7),
    _WfStatsDcLbcTxMaxDelta0_Type()
)
wfStatsDcLbcTxMaxDelta0.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfStatsDcLbcTxMaxDelta0.setStatus("mandatory")


class _WfStatsDcLbcRxMaxDelta1_Type(Gauge32):
    """Custom type wfStatsDcLbcRxMaxDelta1 based on Gauge32"""
    defaultValue = 0


_WfStatsDcLbcRxMaxDelta1_Object = MibTableColumn
wfStatsDcLbcRxMaxDelta1 = _WfStatsDcLbcRxMaxDelta1_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 17, 3, 1, 8),
    _WfStatsDcLbcRxMaxDelta1_Type()
)
wfStatsDcLbcRxMaxDelta1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfStatsDcLbcRxMaxDelta1.setStatus("mandatory")


class _WfStatsDcLbcTxMaxDelta1_Type(Gauge32):
    """Custom type wfStatsDcLbcTxMaxDelta1 based on Gauge32"""
    defaultValue = 0


_WfStatsDcLbcTxMaxDelta1_Object = MibTableColumn
wfStatsDcLbcTxMaxDelta1 = _WfStatsDcLbcTxMaxDelta1_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 17, 3, 1, 9),
    _WfStatsDcLbcTxMaxDelta1_Type()
)
wfStatsDcLbcTxMaxDelta1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfStatsDcLbcTxMaxDelta1.setStatus("mandatory")


class _WfStatsDcLbcRxMaxDelta2_Type(Gauge32):
    """Custom type wfStatsDcLbcRxMaxDelta2 based on Gauge32"""
    defaultValue = 0


_WfStatsDcLbcRxMaxDelta2_Object = MibTableColumn
wfStatsDcLbcRxMaxDelta2 = _WfStatsDcLbcRxMaxDelta2_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 17, 3, 1, 10),
    _WfStatsDcLbcRxMaxDelta2_Type()
)
wfStatsDcLbcRxMaxDelta2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfStatsDcLbcRxMaxDelta2.setStatus("mandatory")


class _WfStatsDcLbcTxMaxDelta2_Type(Gauge32):
    """Custom type wfStatsDcLbcTxMaxDelta2 based on Gauge32"""
    defaultValue = 0


_WfStatsDcLbcTxMaxDelta2_Object = MibTableColumn
wfStatsDcLbcTxMaxDelta2 = _WfStatsDcLbcTxMaxDelta2_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 17, 3, 1, 11),
    _WfStatsDcLbcTxMaxDelta2_Type()
)
wfStatsDcLbcTxMaxDelta2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfStatsDcLbcTxMaxDelta2.setStatus("mandatory")


class _WfStatsDcLbcRxMaxDelta3_Type(Gauge32):
    """Custom type wfStatsDcLbcRxMaxDelta3 based on Gauge32"""
    defaultValue = 0


_WfStatsDcLbcRxMaxDelta3_Object = MibTableColumn
wfStatsDcLbcRxMaxDelta3 = _WfStatsDcLbcRxMaxDelta3_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 17, 3, 1, 12),
    _WfStatsDcLbcRxMaxDelta3_Type()
)
wfStatsDcLbcRxMaxDelta3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfStatsDcLbcRxMaxDelta3.setStatus("mandatory")


class _WfStatsDcLbcTxMaxDelta3_Type(Gauge32):
    """Custom type wfStatsDcLbcTxMaxDelta3 based on Gauge32"""
    defaultValue = 0


_WfStatsDcLbcTxMaxDelta3_Object = MibTableColumn
wfStatsDcLbcTxMaxDelta3 = _WfStatsDcLbcTxMaxDelta3_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 17, 3, 1, 13),
    _WfStatsDcLbcTxMaxDelta3_Type()
)
wfStatsDcLbcTxMaxDelta3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfStatsDcLbcTxMaxDelta3.setStatus("mandatory")


class _WfStatsDcLbcRxMaxDelta4_Type(Gauge32):
    """Custom type wfStatsDcLbcRxMaxDelta4 based on Gauge32"""
    defaultValue = 0


_WfStatsDcLbcRxMaxDelta4_Object = MibTableColumn
wfStatsDcLbcRxMaxDelta4 = _WfStatsDcLbcRxMaxDelta4_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 17, 3, 1, 14),
    _WfStatsDcLbcRxMaxDelta4_Type()
)
wfStatsDcLbcRxMaxDelta4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfStatsDcLbcRxMaxDelta4.setStatus("mandatory")


class _WfStatsDcLbcTxMaxDelta4_Type(Gauge32):
    """Custom type wfStatsDcLbcTxMaxDelta4 based on Gauge32"""
    defaultValue = 0


_WfStatsDcLbcTxMaxDelta4_Object = MibTableColumn
wfStatsDcLbcTxMaxDelta4 = _WfStatsDcLbcTxMaxDelta4_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 17, 3, 1, 15),
    _WfStatsDcLbcTxMaxDelta4_Type()
)
wfStatsDcLbcTxMaxDelta4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfStatsDcLbcTxMaxDelta4.setStatus("mandatory")


class _WfStatsDcLbcRxMaxDelta5_Type(Gauge32):
    """Custom type wfStatsDcLbcRxMaxDelta5 based on Gauge32"""
    defaultValue = 0


_WfStatsDcLbcRxMaxDelta5_Object = MibTableColumn
wfStatsDcLbcRxMaxDelta5 = _WfStatsDcLbcRxMaxDelta5_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 17, 3, 1, 16),
    _WfStatsDcLbcRxMaxDelta5_Type()
)
wfStatsDcLbcRxMaxDelta5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfStatsDcLbcRxMaxDelta5.setStatus("mandatory")


class _WfStatsDcLbcTxMaxDelta5_Type(Gauge32):
    """Custom type wfStatsDcLbcTxMaxDelta5 based on Gauge32"""
    defaultValue = 0


_WfStatsDcLbcTxMaxDelta5_Object = MibTableColumn
wfStatsDcLbcTxMaxDelta5 = _WfStatsDcLbcTxMaxDelta5_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 17, 3, 1, 17),
    _WfStatsDcLbcTxMaxDelta5_Type()
)
wfStatsDcLbcTxMaxDelta5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfStatsDcLbcTxMaxDelta5.setStatus("mandatory")


class _WfStatsDcLbcRxMaxDelta6_Type(Gauge32):
    """Custom type wfStatsDcLbcRxMaxDelta6 based on Gauge32"""
    defaultValue = 0


_WfStatsDcLbcRxMaxDelta6_Object = MibTableColumn
wfStatsDcLbcRxMaxDelta6 = _WfStatsDcLbcRxMaxDelta6_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 17, 3, 1, 18),
    _WfStatsDcLbcRxMaxDelta6_Type()
)
wfStatsDcLbcRxMaxDelta6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfStatsDcLbcRxMaxDelta6.setStatus("mandatory")


class _WfStatsDcLbcTxMaxDelta6_Type(Gauge32):
    """Custom type wfStatsDcLbcTxMaxDelta6 based on Gauge32"""
    defaultValue = 0


_WfStatsDcLbcTxMaxDelta6_Object = MibTableColumn
wfStatsDcLbcTxMaxDelta6 = _WfStatsDcLbcTxMaxDelta6_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 17, 3, 1, 19),
    _WfStatsDcLbcTxMaxDelta6_Type()
)
wfStatsDcLbcTxMaxDelta6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfStatsDcLbcTxMaxDelta6.setStatus("mandatory")


class _WfStatsDcLbcRxMaxDelta7_Type(Gauge32):
    """Custom type wfStatsDcLbcRxMaxDelta7 based on Gauge32"""
    defaultValue = 0


_WfStatsDcLbcRxMaxDelta7_Object = MibTableColumn
wfStatsDcLbcRxMaxDelta7 = _WfStatsDcLbcRxMaxDelta7_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 17, 3, 1, 20),
    _WfStatsDcLbcRxMaxDelta7_Type()
)
wfStatsDcLbcRxMaxDelta7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfStatsDcLbcRxMaxDelta7.setStatus("mandatory")


class _WfStatsDcLbcTxMaxDelta7_Type(Gauge32):
    """Custom type wfStatsDcLbcTxMaxDelta7 based on Gauge32"""
    defaultValue = 0


_WfStatsDcLbcTxMaxDelta7_Object = MibTableColumn
wfStatsDcLbcTxMaxDelta7 = _WfStatsDcLbcTxMaxDelta7_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 17, 3, 1, 21),
    _WfStatsDcLbcTxMaxDelta7_Type()
)
wfStatsDcLbcTxMaxDelta7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfStatsDcLbcTxMaxDelta7.setStatus("mandatory")


class _WfStatsDcLbcRxMaxDelta8_Type(Gauge32):
    """Custom type wfStatsDcLbcRxMaxDelta8 based on Gauge32"""
    defaultValue = 0


_WfStatsDcLbcRxMaxDelta8_Object = MibTableColumn
wfStatsDcLbcRxMaxDelta8 = _WfStatsDcLbcRxMaxDelta8_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 17, 3, 1, 22),
    _WfStatsDcLbcRxMaxDelta8_Type()
)
wfStatsDcLbcRxMaxDelta8.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfStatsDcLbcRxMaxDelta8.setStatus("mandatory")


class _WfStatsDcLbcTxMaxDelta8_Type(Gauge32):
    """Custom type wfStatsDcLbcTxMaxDelta8 based on Gauge32"""
    defaultValue = 0


_WfStatsDcLbcTxMaxDelta8_Object = MibTableColumn
wfStatsDcLbcTxMaxDelta8 = _WfStatsDcLbcTxMaxDelta8_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 17, 3, 1, 23),
    _WfStatsDcLbcTxMaxDelta8_Type()
)
wfStatsDcLbcTxMaxDelta8.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfStatsDcLbcTxMaxDelta8.setStatus("mandatory")


class _WfStatsDcLbcRxMaxDelta9_Type(Gauge32):
    """Custom type wfStatsDcLbcRxMaxDelta9 based on Gauge32"""
    defaultValue = 0


_WfStatsDcLbcRxMaxDelta9_Object = MibTableColumn
wfStatsDcLbcRxMaxDelta9 = _WfStatsDcLbcRxMaxDelta9_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 17, 3, 1, 24),
    _WfStatsDcLbcRxMaxDelta9_Type()
)
wfStatsDcLbcRxMaxDelta9.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfStatsDcLbcRxMaxDelta9.setStatus("mandatory")


class _WfStatsDcLbcTxMaxDelta9_Type(Gauge32):
    """Custom type wfStatsDcLbcTxMaxDelta9 based on Gauge32"""
    defaultValue = 0


_WfStatsDcLbcTxMaxDelta9_Object = MibTableColumn
wfStatsDcLbcTxMaxDelta9 = _WfStatsDcLbcTxMaxDelta9_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 17, 3, 1, 25),
    _WfStatsDcLbcTxMaxDelta9_Type()
)
wfStatsDcLbcTxMaxDelta9.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfStatsDcLbcTxMaxDelta9.setStatus("mandatory")


class _WfStatsDcLbcRxMaxDelta10_Type(Gauge32):
    """Custom type wfStatsDcLbcRxMaxDelta10 based on Gauge32"""
    defaultValue = 0


_WfStatsDcLbcRxMaxDelta10_Object = MibTableColumn
wfStatsDcLbcRxMaxDelta10 = _WfStatsDcLbcRxMaxDelta10_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 17, 3, 1, 26),
    _WfStatsDcLbcRxMaxDelta10_Type()
)
wfStatsDcLbcRxMaxDelta10.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfStatsDcLbcRxMaxDelta10.setStatus("mandatory")


class _WfStatsDcLbcTxMaxDelta10_Type(Gauge32):
    """Custom type wfStatsDcLbcTxMaxDelta10 based on Gauge32"""
    defaultValue = 0


_WfStatsDcLbcTxMaxDelta10_Object = MibTableColumn
wfStatsDcLbcTxMaxDelta10 = _WfStatsDcLbcTxMaxDelta10_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 17, 3, 1, 27),
    _WfStatsDcLbcTxMaxDelta10_Type()
)
wfStatsDcLbcTxMaxDelta10.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfStatsDcLbcTxMaxDelta10.setStatus("mandatory")


class _WfStatsDcLbcRxMaxDelta11_Type(Gauge32):
    """Custom type wfStatsDcLbcRxMaxDelta11 based on Gauge32"""
    defaultValue = 0


_WfStatsDcLbcRxMaxDelta11_Object = MibTableColumn
wfStatsDcLbcRxMaxDelta11 = _WfStatsDcLbcRxMaxDelta11_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 17, 3, 1, 28),
    _WfStatsDcLbcRxMaxDelta11_Type()
)
wfStatsDcLbcRxMaxDelta11.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfStatsDcLbcRxMaxDelta11.setStatus("mandatory")


class _WfStatsDcLbcTxMaxDelta11_Type(Gauge32):
    """Custom type wfStatsDcLbcTxMaxDelta11 based on Gauge32"""
    defaultValue = 0


_WfStatsDcLbcTxMaxDelta11_Object = MibTableColumn
wfStatsDcLbcTxMaxDelta11 = _WfStatsDcLbcTxMaxDelta11_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 17, 3, 1, 29),
    _WfStatsDcLbcTxMaxDelta11_Type()
)
wfStatsDcLbcTxMaxDelta11.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfStatsDcLbcTxMaxDelta11.setStatus("mandatory")


class _WfStatsDcLbcRxMaxDelta12_Type(Gauge32):
    """Custom type wfStatsDcLbcRxMaxDelta12 based on Gauge32"""
    defaultValue = 0


_WfStatsDcLbcRxMaxDelta12_Object = MibTableColumn
wfStatsDcLbcRxMaxDelta12 = _WfStatsDcLbcRxMaxDelta12_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 17, 3, 1, 30),
    _WfStatsDcLbcRxMaxDelta12_Type()
)
wfStatsDcLbcRxMaxDelta12.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfStatsDcLbcRxMaxDelta12.setStatus("mandatory")


class _WfStatsDcLbcTxMaxDelta12_Type(Gauge32):
    """Custom type wfStatsDcLbcTxMaxDelta12 based on Gauge32"""
    defaultValue = 0


_WfStatsDcLbcTxMaxDelta12_Object = MibTableColumn
wfStatsDcLbcTxMaxDelta12 = _WfStatsDcLbcTxMaxDelta12_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 17, 3, 1, 31),
    _WfStatsDcLbcTxMaxDelta12_Type()
)
wfStatsDcLbcTxMaxDelta12.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfStatsDcLbcTxMaxDelta12.setStatus("mandatory")


class _WfStatsDcLbcRxMaxDelta13_Type(Gauge32):
    """Custom type wfStatsDcLbcRxMaxDelta13 based on Gauge32"""
    defaultValue = 0


_WfStatsDcLbcRxMaxDelta13_Object = MibTableColumn
wfStatsDcLbcRxMaxDelta13 = _WfStatsDcLbcRxMaxDelta13_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 17, 3, 1, 32),
    _WfStatsDcLbcRxMaxDelta13_Type()
)
wfStatsDcLbcRxMaxDelta13.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfStatsDcLbcRxMaxDelta13.setStatus("mandatory")


class _WfStatsDcLbcTxMaxDelta13_Type(Gauge32):
    """Custom type wfStatsDcLbcTxMaxDelta13 based on Gauge32"""
    defaultValue = 0


_WfStatsDcLbcTxMaxDelta13_Object = MibTableColumn
wfStatsDcLbcTxMaxDelta13 = _WfStatsDcLbcTxMaxDelta13_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 17, 3, 1, 33),
    _WfStatsDcLbcTxMaxDelta13_Type()
)
wfStatsDcLbcTxMaxDelta13.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfStatsDcLbcTxMaxDelta13.setStatus("mandatory")


class _WfStatsDcLbcRxMaxDelta14_Type(Gauge32):
    """Custom type wfStatsDcLbcRxMaxDelta14 based on Gauge32"""
    defaultValue = 0


_WfStatsDcLbcRxMaxDelta14_Object = MibTableColumn
wfStatsDcLbcRxMaxDelta14 = _WfStatsDcLbcRxMaxDelta14_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 17, 3, 1, 34),
    _WfStatsDcLbcRxMaxDelta14_Type()
)
wfStatsDcLbcRxMaxDelta14.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfStatsDcLbcRxMaxDelta14.setStatus("mandatory")


class _WfStatsDcLbcTxMaxDelta14_Type(Gauge32):
    """Custom type wfStatsDcLbcTxMaxDelta14 based on Gauge32"""
    defaultValue = 0


_WfStatsDcLbcTxMaxDelta14_Object = MibTableColumn
wfStatsDcLbcTxMaxDelta14 = _WfStatsDcLbcTxMaxDelta14_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 17, 3, 1, 35),
    _WfStatsDcLbcTxMaxDelta14_Type()
)
wfStatsDcLbcTxMaxDelta14.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfStatsDcLbcTxMaxDelta14.setStatus("mandatory")


class _WfStatsDcLbcRxMaxDelta15_Type(Gauge32):
    """Custom type wfStatsDcLbcRxMaxDelta15 based on Gauge32"""
    defaultValue = 0


_WfStatsDcLbcRxMaxDelta15_Object = MibTableColumn
wfStatsDcLbcRxMaxDelta15 = _WfStatsDcLbcRxMaxDelta15_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 17, 3, 1, 36),
    _WfStatsDcLbcRxMaxDelta15_Type()
)
wfStatsDcLbcRxMaxDelta15.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfStatsDcLbcRxMaxDelta15.setStatus("mandatory")


class _WfStatsDcLbcTxMaxDelta15_Type(Gauge32):
    """Custom type wfStatsDcLbcTxMaxDelta15 based on Gauge32"""
    defaultValue = 0


_WfStatsDcLbcTxMaxDelta15_Object = MibTableColumn
wfStatsDcLbcTxMaxDelta15 = _WfStatsDcLbcTxMaxDelta15_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 17, 3, 1, 37),
    _WfStatsDcLbcTxMaxDelta15_Type()
)
wfStatsDcLbcTxMaxDelta15.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfStatsDcLbcTxMaxDelta15.setStatus("mandatory")


class _WfStatsDcLbcRxMaxDelta16_Type(Gauge32):
    """Custom type wfStatsDcLbcRxMaxDelta16 based on Gauge32"""
    defaultValue = 0


_WfStatsDcLbcRxMaxDelta16_Object = MibTableColumn
wfStatsDcLbcRxMaxDelta16 = _WfStatsDcLbcRxMaxDelta16_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 17, 3, 1, 38),
    _WfStatsDcLbcRxMaxDelta16_Type()
)
wfStatsDcLbcRxMaxDelta16.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfStatsDcLbcRxMaxDelta16.setStatus("mandatory")


class _WfStatsDcLbcTxMaxDelta16_Type(Gauge32):
    """Custom type wfStatsDcLbcTxMaxDelta16 based on Gauge32"""
    defaultValue = 0


_WfStatsDcLbcTxMaxDelta16_Object = MibTableColumn
wfStatsDcLbcTxMaxDelta16 = _WfStatsDcLbcTxMaxDelta16_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 17, 3, 1, 39),
    _WfStatsDcLbcTxMaxDelta16_Type()
)
wfStatsDcLbcTxMaxDelta16.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfStatsDcLbcTxMaxDelta16.setStatus("mandatory")


class _WfStatsDcLbcRxMaxDelta17_Type(Gauge32):
    """Custom type wfStatsDcLbcRxMaxDelta17 based on Gauge32"""
    defaultValue = 0


_WfStatsDcLbcRxMaxDelta17_Object = MibTableColumn
wfStatsDcLbcRxMaxDelta17 = _WfStatsDcLbcRxMaxDelta17_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 17, 3, 1, 40),
    _WfStatsDcLbcRxMaxDelta17_Type()
)
wfStatsDcLbcRxMaxDelta17.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfStatsDcLbcRxMaxDelta17.setStatus("mandatory")


class _WfStatsDcLbcTxMaxDelta17_Type(Gauge32):
    """Custom type wfStatsDcLbcTxMaxDelta17 based on Gauge32"""
    defaultValue = 0


_WfStatsDcLbcTxMaxDelta17_Object = MibTableColumn
wfStatsDcLbcTxMaxDelta17 = _WfStatsDcLbcTxMaxDelta17_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 17, 3, 1, 41),
    _WfStatsDcLbcTxMaxDelta17_Type()
)
wfStatsDcLbcTxMaxDelta17.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfStatsDcLbcTxMaxDelta17.setStatus("mandatory")


class _WfStatsDcLbcRxMaxDelta18_Type(Gauge32):
    """Custom type wfStatsDcLbcRxMaxDelta18 based on Gauge32"""
    defaultValue = 0


_WfStatsDcLbcRxMaxDelta18_Object = MibTableColumn
wfStatsDcLbcRxMaxDelta18 = _WfStatsDcLbcRxMaxDelta18_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 17, 3, 1, 42),
    _WfStatsDcLbcRxMaxDelta18_Type()
)
wfStatsDcLbcRxMaxDelta18.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfStatsDcLbcRxMaxDelta18.setStatus("mandatory")


class _WfStatsDcLbcTxMaxDelta18_Type(Gauge32):
    """Custom type wfStatsDcLbcTxMaxDelta18 based on Gauge32"""
    defaultValue = 0


_WfStatsDcLbcTxMaxDelta18_Object = MibTableColumn
wfStatsDcLbcTxMaxDelta18 = _WfStatsDcLbcTxMaxDelta18_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 17, 3, 1, 43),
    _WfStatsDcLbcTxMaxDelta18_Type()
)
wfStatsDcLbcTxMaxDelta18.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfStatsDcLbcTxMaxDelta18.setStatus("mandatory")


class _WfStatsDcLbcRxMaxDelta19_Type(Gauge32):
    """Custom type wfStatsDcLbcRxMaxDelta19 based on Gauge32"""
    defaultValue = 0


_WfStatsDcLbcRxMaxDelta19_Object = MibTableColumn
wfStatsDcLbcRxMaxDelta19 = _WfStatsDcLbcRxMaxDelta19_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 17, 3, 1, 44),
    _WfStatsDcLbcRxMaxDelta19_Type()
)
wfStatsDcLbcRxMaxDelta19.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfStatsDcLbcRxMaxDelta19.setStatus("mandatory")


class _WfStatsDcLbcTxMaxDelta19_Type(Gauge32):
    """Custom type wfStatsDcLbcTxMaxDelta19 based on Gauge32"""
    defaultValue = 0


_WfStatsDcLbcTxMaxDelta19_Object = MibTableColumn
wfStatsDcLbcTxMaxDelta19 = _WfStatsDcLbcTxMaxDelta19_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 17, 3, 1, 45),
    _WfStatsDcLbcTxMaxDelta19_Type()
)
wfStatsDcLbcTxMaxDelta19.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfStatsDcLbcTxMaxDelta19.setStatus("mandatory")


class _WfStatsDcLbcRxMaxDelta20_Type(Gauge32):
    """Custom type wfStatsDcLbcRxMaxDelta20 based on Gauge32"""
    defaultValue = 0


_WfStatsDcLbcRxMaxDelta20_Object = MibTableColumn
wfStatsDcLbcRxMaxDelta20 = _WfStatsDcLbcRxMaxDelta20_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 17, 3, 1, 46),
    _WfStatsDcLbcRxMaxDelta20_Type()
)
wfStatsDcLbcRxMaxDelta20.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfStatsDcLbcRxMaxDelta20.setStatus("mandatory")


class _WfStatsDcLbcTxMaxDelta20_Type(Gauge32):
    """Custom type wfStatsDcLbcTxMaxDelta20 based on Gauge32"""
    defaultValue = 0


_WfStatsDcLbcTxMaxDelta20_Object = MibTableColumn
wfStatsDcLbcTxMaxDelta20 = _WfStatsDcLbcTxMaxDelta20_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 17, 3, 1, 47),
    _WfStatsDcLbcTxMaxDelta20_Type()
)
wfStatsDcLbcTxMaxDelta20.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfStatsDcLbcTxMaxDelta20.setStatus("mandatory")


class _WfStatsDcLbcRxMaxDelta21_Type(Gauge32):
    """Custom type wfStatsDcLbcRxMaxDelta21 based on Gauge32"""
    defaultValue = 0


_WfStatsDcLbcRxMaxDelta21_Object = MibTableColumn
wfStatsDcLbcRxMaxDelta21 = _WfStatsDcLbcRxMaxDelta21_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 17, 3, 1, 48),
    _WfStatsDcLbcRxMaxDelta21_Type()
)
wfStatsDcLbcRxMaxDelta21.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfStatsDcLbcRxMaxDelta21.setStatus("mandatory")


class _WfStatsDcLbcTxMaxDelta21_Type(Gauge32):
    """Custom type wfStatsDcLbcTxMaxDelta21 based on Gauge32"""
    defaultValue = 0


_WfStatsDcLbcTxMaxDelta21_Object = MibTableColumn
wfStatsDcLbcTxMaxDelta21 = _WfStatsDcLbcTxMaxDelta21_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 17, 3, 1, 49),
    _WfStatsDcLbcTxMaxDelta21_Type()
)
wfStatsDcLbcTxMaxDelta21.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfStatsDcLbcTxMaxDelta21.setStatus("mandatory")


class _WfStatsDcLbcRxMaxDelta22_Type(Gauge32):
    """Custom type wfStatsDcLbcRxMaxDelta22 based on Gauge32"""
    defaultValue = 0


_WfStatsDcLbcRxMaxDelta22_Object = MibTableColumn
wfStatsDcLbcRxMaxDelta22 = _WfStatsDcLbcRxMaxDelta22_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 17, 3, 1, 50),
    _WfStatsDcLbcRxMaxDelta22_Type()
)
wfStatsDcLbcRxMaxDelta22.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfStatsDcLbcRxMaxDelta22.setStatus("mandatory")


class _WfStatsDcLbcTxMaxDelta22_Type(Gauge32):
    """Custom type wfStatsDcLbcTxMaxDelta22 based on Gauge32"""
    defaultValue = 0


_WfStatsDcLbcTxMaxDelta22_Object = MibTableColumn
wfStatsDcLbcTxMaxDelta22 = _WfStatsDcLbcTxMaxDelta22_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 17, 3, 1, 51),
    _WfStatsDcLbcTxMaxDelta22_Type()
)
wfStatsDcLbcTxMaxDelta22.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfStatsDcLbcTxMaxDelta22.setStatus("mandatory")


class _WfStatsDcLbcRxMaxDelta23_Type(Gauge32):
    """Custom type wfStatsDcLbcRxMaxDelta23 based on Gauge32"""
    defaultValue = 0


_WfStatsDcLbcRxMaxDelta23_Object = MibTableColumn
wfStatsDcLbcRxMaxDelta23 = _WfStatsDcLbcRxMaxDelta23_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 17, 3, 1, 52),
    _WfStatsDcLbcRxMaxDelta23_Type()
)
wfStatsDcLbcRxMaxDelta23.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfStatsDcLbcRxMaxDelta23.setStatus("mandatory")


class _WfStatsDcLbcTxMaxDelta23_Type(Gauge32):
    """Custom type wfStatsDcLbcTxMaxDelta23 based on Gauge32"""
    defaultValue = 0


_WfStatsDcLbcTxMaxDelta23_Object = MibTableColumn
wfStatsDcLbcTxMaxDelta23 = _WfStatsDcLbcTxMaxDelta23_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 17, 3, 1, 53),
    _WfStatsDcLbcTxMaxDelta23_Type()
)
wfStatsDcLbcTxMaxDelta23.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfStatsDcLbcTxMaxDelta23.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Wellfleet-STATS-MIB",
    **{"wfStatsDc": wfStatsDc,
       "wfStatsDcDisable": wfStatsDcDisable,
       "wfStatsDcVolume": wfStatsDcVolume,
       "wfStatsDcFilePrefix": wfStatsDcFilePrefix,
       "wfStatsDcUpdateInterval": wfStatsDcUpdateInterval,
       "wfStatsDcStoreInterval": wfStatsDcStoreInterval,
       "wfStatsDcUpdateData": wfStatsDcUpdateData,
       "wfStatsDcStoreData": wfStatsDcStoreData,
       "wfStatsDcSwitchId": wfStatsDcSwitchId,
       "wfStatsDcEnableAll": wfStatsDcEnableAll,
       "wfStatsDcMaxNumFiles": wfStatsDcMaxNumFiles,
       "wfStatsDcFrVcDisable": wfStatsDcFrVcDisable,
       "wfStatsDcState": wfStatsDcState,
       "wfStatsDcHssiFields": wfStatsDcHssiFields,
       "wfStatsDcSyncFields": wfStatsDcSyncFields,
       "wfStatsDcDs1E1Fields": wfStatsDcDs1E1Fields,
       "wfStatsDcFrSwVcFields": wfStatsDcFrSwVcFields,
       "wfStatsDcCctCngcFields": wfStatsDcCctCngcFields,
       "wfStatsDcFddiFields": wfStatsDcFddiFields,
       "wfStatsDcCctCngcDisable": wfStatsDcCctCngcDisable,
       "wfStatsDcLbcFileDisable": wfStatsDcLbcFileDisable,
       "wfStatsDcAtmzPhyFields": wfStatsDcAtmzPhyFields,
       "wfStatsDcMediaTable": wfStatsDcMediaTable,
       "wfStatsDcMediaEntry": wfStatsDcMediaEntry,
       "wfStatsDcMediaDelete": wfStatsDcMediaDelete,
       "wfStatsDcMediaLineNumber": wfStatsDcMediaLineNumber,
       "wfStatsDcLbcTable": wfStatsDcLbcTable,
       "wfStatsDcLbcEntry": wfStatsDcLbcEntry,
       "wfStatsDcLbcDelete": wfStatsDcLbcDelete,
       "wfStatsDcLbcDisable": wfStatsDcLbcDisable,
       "wfStatsDcLbcLineNumber": wfStatsDcLbcLineNumber,
       "wfStatsDcLbcUpdateInterval": wfStatsDcLbcUpdateInterval,
       "wfStatsDcLbcState": wfStatsDcLbcState,
       "wfStatsDcLbcRxMaxDelta0": wfStatsDcLbcRxMaxDelta0,
       "wfStatsDcLbcTxMaxDelta0": wfStatsDcLbcTxMaxDelta0,
       "wfStatsDcLbcRxMaxDelta1": wfStatsDcLbcRxMaxDelta1,
       "wfStatsDcLbcTxMaxDelta1": wfStatsDcLbcTxMaxDelta1,
       "wfStatsDcLbcRxMaxDelta2": wfStatsDcLbcRxMaxDelta2,
       "wfStatsDcLbcTxMaxDelta2": wfStatsDcLbcTxMaxDelta2,
       "wfStatsDcLbcRxMaxDelta3": wfStatsDcLbcRxMaxDelta3,
       "wfStatsDcLbcTxMaxDelta3": wfStatsDcLbcTxMaxDelta3,
       "wfStatsDcLbcRxMaxDelta4": wfStatsDcLbcRxMaxDelta4,
       "wfStatsDcLbcTxMaxDelta4": wfStatsDcLbcTxMaxDelta4,
       "wfStatsDcLbcRxMaxDelta5": wfStatsDcLbcRxMaxDelta5,
       "wfStatsDcLbcTxMaxDelta5": wfStatsDcLbcTxMaxDelta5,
       "wfStatsDcLbcRxMaxDelta6": wfStatsDcLbcRxMaxDelta6,
       "wfStatsDcLbcTxMaxDelta6": wfStatsDcLbcTxMaxDelta6,
       "wfStatsDcLbcRxMaxDelta7": wfStatsDcLbcRxMaxDelta7,
       "wfStatsDcLbcTxMaxDelta7": wfStatsDcLbcTxMaxDelta7,
       "wfStatsDcLbcRxMaxDelta8": wfStatsDcLbcRxMaxDelta8,
       "wfStatsDcLbcTxMaxDelta8": wfStatsDcLbcTxMaxDelta8,
       "wfStatsDcLbcRxMaxDelta9": wfStatsDcLbcRxMaxDelta9,
       "wfStatsDcLbcTxMaxDelta9": wfStatsDcLbcTxMaxDelta9,
       "wfStatsDcLbcRxMaxDelta10": wfStatsDcLbcRxMaxDelta10,
       "wfStatsDcLbcTxMaxDelta10": wfStatsDcLbcTxMaxDelta10,
       "wfStatsDcLbcRxMaxDelta11": wfStatsDcLbcRxMaxDelta11,
       "wfStatsDcLbcTxMaxDelta11": wfStatsDcLbcTxMaxDelta11,
       "wfStatsDcLbcRxMaxDelta12": wfStatsDcLbcRxMaxDelta12,
       "wfStatsDcLbcTxMaxDelta12": wfStatsDcLbcTxMaxDelta12,
       "wfStatsDcLbcRxMaxDelta13": wfStatsDcLbcRxMaxDelta13,
       "wfStatsDcLbcTxMaxDelta13": wfStatsDcLbcTxMaxDelta13,
       "wfStatsDcLbcRxMaxDelta14": wfStatsDcLbcRxMaxDelta14,
       "wfStatsDcLbcTxMaxDelta14": wfStatsDcLbcTxMaxDelta14,
       "wfStatsDcLbcRxMaxDelta15": wfStatsDcLbcRxMaxDelta15,
       "wfStatsDcLbcTxMaxDelta15": wfStatsDcLbcTxMaxDelta15,
       "wfStatsDcLbcRxMaxDelta16": wfStatsDcLbcRxMaxDelta16,
       "wfStatsDcLbcTxMaxDelta16": wfStatsDcLbcTxMaxDelta16,
       "wfStatsDcLbcRxMaxDelta17": wfStatsDcLbcRxMaxDelta17,
       "wfStatsDcLbcTxMaxDelta17": wfStatsDcLbcTxMaxDelta17,
       "wfStatsDcLbcRxMaxDelta18": wfStatsDcLbcRxMaxDelta18,
       "wfStatsDcLbcTxMaxDelta18": wfStatsDcLbcTxMaxDelta18,
       "wfStatsDcLbcRxMaxDelta19": wfStatsDcLbcRxMaxDelta19,
       "wfStatsDcLbcTxMaxDelta19": wfStatsDcLbcTxMaxDelta19,
       "wfStatsDcLbcRxMaxDelta20": wfStatsDcLbcRxMaxDelta20,
       "wfStatsDcLbcTxMaxDelta20": wfStatsDcLbcTxMaxDelta20,
       "wfStatsDcLbcRxMaxDelta21": wfStatsDcLbcRxMaxDelta21,
       "wfStatsDcLbcTxMaxDelta21": wfStatsDcLbcTxMaxDelta21,
       "wfStatsDcLbcRxMaxDelta22": wfStatsDcLbcRxMaxDelta22,
       "wfStatsDcLbcTxMaxDelta22": wfStatsDcLbcTxMaxDelta22,
       "wfStatsDcLbcRxMaxDelta23": wfStatsDcLbcRxMaxDelta23,
       "wfStatsDcLbcTxMaxDelta23": wfStatsDcLbcTxMaxDelta23}
)
