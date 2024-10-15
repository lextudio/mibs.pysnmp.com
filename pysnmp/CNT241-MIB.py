# SNMP MIB module (CNT241-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CNT241-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:15:56 2024
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

(cnt2Subagent,) = mibBuilder.importSymbols(
    "CNT2-MIB",
    "cnt2Subagent")

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
 NotificationType,
 TimeTicks,
 Unsigned32,
 enterprises,
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
    "NotificationType",
    "TimeTicks",
    "Unsigned32",
    "enterprises",
    "iso")

(DisplayString,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Cnt2Sm_ObjectIdentity = ObjectIdentity
cnt2Sm = _Cnt2Sm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 333, 2, 4, 1)
)
_Cnt2SmHw_ObjectIdentity = ObjectIdentity
cnt2SmHw = _Cnt2SmHw_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 333, 2, 4, 1, 1)
)
_Cnt2SmHwTemperatureF_Type = Integer32
_Cnt2SmHwTemperatureF_Object = MibScalar
cnt2SmHwTemperatureF = _Cnt2SmHwTemperatureF_Object(
    (1, 3, 6, 1, 4, 1, 333, 2, 4, 1, 1, 1),
    _Cnt2SmHwTemperatureF_Type()
)
cnt2SmHwTemperatureF.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnt2SmHwTemperatureF.setStatus("mandatory")


class _Cnt2SmHwTapeDriveState_Type(Integer32):
    """Custom type cnt2SmHwTapeDriveState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("failed", 3),
          ("not-present", 1),
          ("ok", 2))
    )


_Cnt2SmHwTapeDriveState_Type.__name__ = "Integer32"
_Cnt2SmHwTapeDriveState_Object = MibScalar
cnt2SmHwTapeDriveState = _Cnt2SmHwTapeDriveState_Object(
    (1, 3, 6, 1, 4, 1, 333, 2, 4, 1, 1, 2),
    _Cnt2SmHwTapeDriveState_Type()
)
cnt2SmHwTapeDriveState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnt2SmHwTapeDriveState.setStatus("mandatory")


class _Cnt2SmHwCdRomDriveState_Type(Integer32):
    """Custom type cnt2SmHwCdRomDriveState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("failed", 3),
          ("not-present", 1),
          ("ok", 2))
    )


_Cnt2SmHwCdRomDriveState_Type.__name__ = "Integer32"
_Cnt2SmHwCdRomDriveState_Object = MibScalar
cnt2SmHwCdRomDriveState = _Cnt2SmHwCdRomDriveState_Object(
    (1, 3, 6, 1, 4, 1, 333, 2, 4, 1, 1, 3),
    _Cnt2SmHwCdRomDriveState_Type()
)
cnt2SmHwCdRomDriveState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnt2SmHwCdRomDriveState.setStatus("mandatory")


class _Cnt2SmHwTapeMounted_Type(Integer32):
    """Custom type cnt2SmHwTapeMounted based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("empty", 2),
          ("mounted", 3),
          ("not-applicable", 1))
    )


_Cnt2SmHwTapeMounted_Type.__name__ = "Integer32"
_Cnt2SmHwTapeMounted_Object = MibScalar
cnt2SmHwTapeMounted = _Cnt2SmHwTapeMounted_Object(
    (1, 3, 6, 1, 4, 1, 333, 2, 4, 1, 1, 4),
    _Cnt2SmHwTapeMounted_Type()
)
cnt2SmHwTapeMounted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnt2SmHwTapeMounted.setStatus("mandatory")


class _Cnt2SmHwCdRomMounted_Type(Integer32):
    """Custom type cnt2SmHwCdRomMounted based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("empty", 2),
          ("mounted", 3),
          ("not-applicable", 1))
    )


_Cnt2SmHwCdRomMounted_Type.__name__ = "Integer32"
_Cnt2SmHwCdRomMounted_Object = MibScalar
cnt2SmHwCdRomMounted = _Cnt2SmHwCdRomMounted_Object(
    (1, 3, 6, 1, 4, 1, 333, 2, 4, 1, 1, 5),
    _Cnt2SmHwCdRomMounted_Type()
)
cnt2SmHwCdRomMounted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnt2SmHwCdRomMounted.setStatus("mandatory")


class _Cnt2SmHwServiceLed_Type(Integer32):
    """Custom type cnt2SmHwServiceLed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2))
    )


_Cnt2SmHwServiceLed_Type.__name__ = "Integer32"
_Cnt2SmHwServiceLed_Object = MibScalar
cnt2SmHwServiceLed = _Cnt2SmHwServiceLed_Object(
    (1, 3, 6, 1, 4, 1, 333, 2, 4, 1, 1, 6),
    _Cnt2SmHwServiceLed_Type()
)
cnt2SmHwServiceLed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnt2SmHwServiceLed.setStatus("mandatory")


class _Cnt2SmHwIplSwitch_Type(Integer32):
    """Custom type cnt2SmHwIplSwitch based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2))
    )


_Cnt2SmHwIplSwitch_Type.__name__ = "Integer32"
_Cnt2SmHwIplSwitch_Object = MibScalar
cnt2SmHwIplSwitch = _Cnt2SmHwIplSwitch_Object(
    (1, 3, 6, 1, 4, 1, 333, 2, 4, 1, 1, 7),
    _Cnt2SmHwIplSwitch_Type()
)
cnt2SmHwIplSwitch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnt2SmHwIplSwitch.setStatus("mandatory")
_Cnt2SmHwAdapterTable_Object = MibTable
cnt2SmHwAdapterTable = _Cnt2SmHwAdapterTable_Object(
    (1, 3, 6, 1, 4, 1, 333, 2, 4, 1, 1, 8)
)
if mibBuilder.loadTexts:
    cnt2SmHwAdapterTable.setStatus("mandatory")
_Cnt2SmHwAdapterEntry_Object = MibTableRow
cnt2SmHwAdapterEntry = _Cnt2SmHwAdapterEntry_Object(
    (1, 3, 6, 1, 4, 1, 333, 2, 4, 1, 1, 8, 1)
)
cnt2SmHwAdapterEntry.setIndexNames(
    (0, "CNT241-MIB", "cnt2SmHwAdapterIndex"),
)
if mibBuilder.loadTexts:
    cnt2SmHwAdapterEntry.setStatus("mandatory")
_Cnt2SmHwAdapterIndex_Type = Integer32
_Cnt2SmHwAdapterIndex_Object = MibTableColumn
cnt2SmHwAdapterIndex = _Cnt2SmHwAdapterIndex_Object(
    (1, 3, 6, 1, 4, 1, 333, 2, 4, 1, 1, 8, 1, 1),
    _Cnt2SmHwAdapterIndex_Type()
)
cnt2SmHwAdapterIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnt2SmHwAdapterIndex.setStatus("mandatory")


class _Cnt2SmHwAdapterOperState_Type(Integer32):
    """Custom type cnt2SmHwAdapterOperState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("not-ok", 2),
          ("ok", 1))
    )


_Cnt2SmHwAdapterOperState_Type.__name__ = "Integer32"
_Cnt2SmHwAdapterOperState_Object = MibTableColumn
cnt2SmHwAdapterOperState = _Cnt2SmHwAdapterOperState_Object(
    (1, 3, 6, 1, 4, 1, 333, 2, 4, 1, 1, 8, 1, 2),
    _Cnt2SmHwAdapterOperState_Type()
)
cnt2SmHwAdapterOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnt2SmHwAdapterOperState.setStatus("mandatory")


class _Cnt2SmHwAdapterAdminState_Type(Integer32):
    """Custom type cnt2SmHwAdapterAdminState based on Integer32"""
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
          ("reset", 3))
    )


_Cnt2SmHwAdapterAdminState_Type.__name__ = "Integer32"
_Cnt2SmHwAdapterAdminState_Object = MibTableColumn
cnt2SmHwAdapterAdminState = _Cnt2SmHwAdapterAdminState_Object(
    (1, 3, 6, 1, 4, 1, 333, 2, 4, 1, 1, 8, 1, 3),
    _Cnt2SmHwAdapterAdminState_Type()
)
cnt2SmHwAdapterAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cnt2SmHwAdapterAdminState.setStatus("mandatory")
_Cnt2SmHwCardTable_Object = MibTable
cnt2SmHwCardTable = _Cnt2SmHwCardTable_Object(
    (1, 3, 6, 1, 4, 1, 333, 2, 4, 1, 1, 9)
)
if mibBuilder.loadTexts:
    cnt2SmHwCardTable.setStatus("mandatory")
_Cnt2SmHwCardEntry_Object = MibTableRow
cnt2SmHwCardEntry = _Cnt2SmHwCardEntry_Object(
    (1, 3, 6, 1, 4, 1, 333, 2, 4, 1, 1, 9, 1)
)
cnt2SmHwCardEntry.setIndexNames(
    (0, "CNT241-MIB", "cnt2SmCardAdapterIndex"),
    (0, "CNT241-MIB", "cnt2SmHwCardIndex"),
)
if mibBuilder.loadTexts:
    cnt2SmHwCardEntry.setStatus("mandatory")
_Cnt2SmCardAdapterIndex_Type = Integer32
_Cnt2SmCardAdapterIndex_Object = MibTableColumn
cnt2SmCardAdapterIndex = _Cnt2SmCardAdapterIndex_Object(
    (1, 3, 6, 1, 4, 1, 333, 2, 4, 1, 1, 9, 1, 1),
    _Cnt2SmCardAdapterIndex_Type()
)
cnt2SmCardAdapterIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnt2SmCardAdapterIndex.setStatus("mandatory")
_Cnt2SmHwCardIndex_Type = Integer32
_Cnt2SmHwCardIndex_Object = MibTableColumn
cnt2SmHwCardIndex = _Cnt2SmHwCardIndex_Object(
    (1, 3, 6, 1, 4, 1, 333, 2, 4, 1, 1, 9, 1, 2),
    _Cnt2SmHwCardIndex_Type()
)
cnt2SmHwCardIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnt2SmHwCardIndex.setStatus("mandatory")


class _Cnt2SmHwCardOperState_Type(Integer32):
    """Custom type cnt2SmHwCardOperState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("not-ok", 2),
          ("ok", 1))
    )


_Cnt2SmHwCardOperState_Type.__name__ = "Integer32"
_Cnt2SmHwCardOperState_Object = MibTableColumn
cnt2SmHwCardOperState = _Cnt2SmHwCardOperState_Object(
    (1, 3, 6, 1, 4, 1, 333, 2, 4, 1, 1, 9, 1, 3),
    _Cnt2SmHwCardOperState_Type()
)
cnt2SmHwCardOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnt2SmHwCardOperState.setStatus("mandatory")


class _Cnt2SmHwCardAdminState_Type(Integer32):
    """Custom type cnt2SmHwCardAdminState based on Integer32"""
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
          ("reset", 3))
    )


_Cnt2SmHwCardAdminState_Type.__name__ = "Integer32"
_Cnt2SmHwCardAdminState_Object = MibTableColumn
cnt2SmHwCardAdminState = _Cnt2SmHwCardAdminState_Object(
    (1, 3, 6, 1, 4, 1, 333, 2, 4, 1, 1, 9, 1, 4),
    _Cnt2SmHwCardAdminState_Type()
)
cnt2SmHwCardAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnt2SmHwCardAdminState.setStatus("mandatory")
_Cnt2SmHwPowerSupplyTable_Object = MibTable
cnt2SmHwPowerSupplyTable = _Cnt2SmHwPowerSupplyTable_Object(
    (1, 3, 6, 1, 4, 1, 333, 2, 4, 1, 1, 10)
)
if mibBuilder.loadTexts:
    cnt2SmHwPowerSupplyTable.setStatus("mandatory")
_Cnt2SmHwPowerSupplyEntry_Object = MibTableRow
cnt2SmHwPowerSupplyEntry = _Cnt2SmHwPowerSupplyEntry_Object(
    (1, 3, 6, 1, 4, 1, 333, 2, 4, 1, 1, 10, 1)
)
cnt2SmHwPowerSupplyEntry.setIndexNames(
    (0, "CNT241-MIB", "cnt2SmHwPowerSupplyIndex"),
)
if mibBuilder.loadTexts:
    cnt2SmHwPowerSupplyEntry.setStatus("mandatory")
_Cnt2SmHwPowerSupplyIndex_Type = Integer32
_Cnt2SmHwPowerSupplyIndex_Object = MibTableColumn
cnt2SmHwPowerSupplyIndex = _Cnt2SmHwPowerSupplyIndex_Object(
    (1, 3, 6, 1, 4, 1, 333, 2, 4, 1, 1, 10, 1, 1),
    _Cnt2SmHwPowerSupplyIndex_Type()
)
cnt2SmHwPowerSupplyIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnt2SmHwPowerSupplyIndex.setStatus("mandatory")


class _Cnt2SmHwPowerSupplyACState_Type(Integer32):
    """Custom type cnt2SmHwPowerSupplyACState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("absent", 3),
          ("not-ok", 2),
          ("ok", 1))
    )


_Cnt2SmHwPowerSupplyACState_Type.__name__ = "Integer32"
_Cnt2SmHwPowerSupplyACState_Object = MibTableColumn
cnt2SmHwPowerSupplyACState = _Cnt2SmHwPowerSupplyACState_Object(
    (1, 3, 6, 1, 4, 1, 333, 2, 4, 1, 1, 10, 1, 2),
    _Cnt2SmHwPowerSupplyACState_Type()
)
cnt2SmHwPowerSupplyACState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnt2SmHwPowerSupplyACState.setStatus("mandatory")


class _Cnt2SmHwPowerSupplyDCState_Type(Integer32):
    """Custom type cnt2SmHwPowerSupplyDCState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("absent", 3),
          ("not-ok", 2),
          ("ok", 1))
    )


_Cnt2SmHwPowerSupplyDCState_Type.__name__ = "Integer32"
_Cnt2SmHwPowerSupplyDCState_Object = MibTableColumn
cnt2SmHwPowerSupplyDCState = _Cnt2SmHwPowerSupplyDCState_Object(
    (1, 3, 6, 1, 4, 1, 333, 2, 4, 1, 1, 10, 1, 3),
    _Cnt2SmHwPowerSupplyDCState_Type()
)
cnt2SmHwPowerSupplyDCState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnt2SmHwPowerSupplyDCState.setStatus("mandatory")
_Cnt2SmHwFanTable_Object = MibTable
cnt2SmHwFanTable = _Cnt2SmHwFanTable_Object(
    (1, 3, 6, 1, 4, 1, 333, 2, 4, 1, 1, 11)
)
if mibBuilder.loadTexts:
    cnt2SmHwFanTable.setStatus("mandatory")
_Cnt2SmHwFanEntry_Object = MibTableRow
cnt2SmHwFanEntry = _Cnt2SmHwFanEntry_Object(
    (1, 3, 6, 1, 4, 1, 333, 2, 4, 1, 1, 11, 1)
)
cnt2SmHwFanEntry.setIndexNames(
    (0, "CNT241-MIB", "cnt2SmHwFanIndex"),
)
if mibBuilder.loadTexts:
    cnt2SmHwFanEntry.setStatus("mandatory")
_Cnt2SmHwFanIndex_Type = Integer32
_Cnt2SmHwFanIndex_Object = MibTableColumn
cnt2SmHwFanIndex = _Cnt2SmHwFanIndex_Object(
    (1, 3, 6, 1, 4, 1, 333, 2, 4, 1, 1, 11, 1, 1),
    _Cnt2SmHwFanIndex_Type()
)
cnt2SmHwFanIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnt2SmHwFanIndex.setStatus("mandatory")


class _Cnt2SmHwFanState_Type(Integer32):
    """Custom type cnt2SmHwFanState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("not-ok", 2),
          ("ok", 1))
    )


_Cnt2SmHwFanState_Type.__name__ = "Integer32"
_Cnt2SmHwFanState_Object = MibTableColumn
cnt2SmHwFanState = _Cnt2SmHwFanState_Object(
    (1, 3, 6, 1, 4, 1, 333, 2, 4, 1, 1, 11, 1, 2),
    _Cnt2SmHwFanState_Type()
)
cnt2SmHwFanState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnt2SmHwFanState.setStatus("mandatory")
_Cnt2SmSw_ObjectIdentity = ObjectIdentity
cnt2SmSw = _Cnt2SmSw_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 333, 2, 4, 1, 2)
)
_Cnt2SmNumModules_Type = Integer32
_Cnt2SmNumModules_Object = MibScalar
cnt2SmNumModules = _Cnt2SmNumModules_Object(
    (1, 3, 6, 1, 4, 1, 333, 2, 4, 1, 2, 1),
    _Cnt2SmNumModules_Type()
)
cnt2SmNumModules.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnt2SmNumModules.setStatus("mandatory")
_Cnt2SmSwTable_Object = MibTable
cnt2SmSwTable = _Cnt2SmSwTable_Object(
    (1, 3, 6, 1, 4, 1, 333, 2, 4, 1, 2, 2)
)
if mibBuilder.loadTexts:
    cnt2SmSwTable.setStatus("mandatory")
_Cnt2SmSwEntry_Object = MibTableRow
cnt2SmSwEntry = _Cnt2SmSwEntry_Object(
    (1, 3, 6, 1, 4, 1, 333, 2, 4, 1, 2, 2, 1)
)
cnt2SmSwEntry.setIndexNames(
    (0, "CNT241-MIB", "cnt2SmSwIndex"),
)
if mibBuilder.loadTexts:
    cnt2SmSwEntry.setStatus("mandatory")
_Cnt2SmSwIndex_Type = Integer32
_Cnt2SmSwIndex_Object = MibTableColumn
cnt2SmSwIndex = _Cnt2SmSwIndex_Object(
    (1, 3, 6, 1, 4, 1, 333, 2, 4, 1, 2, 2, 1, 1),
    _Cnt2SmSwIndex_Type()
)
cnt2SmSwIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnt2SmSwIndex.setStatus("mandatory")
_Cnt2SmSwName_Type = DisplayString
_Cnt2SmSwName_Object = MibTableColumn
cnt2SmSwName = _Cnt2SmSwName_Object(
    (1, 3, 6, 1, 4, 1, 333, 2, 4, 1, 2, 2, 1, 2),
    _Cnt2SmSwName_Type()
)
cnt2SmSwName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnt2SmSwName.setStatus("mandatory")


class _Cnt2SmSwFunction_Type(Integer32):
    """Custom type cnt2SmSwFunction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9)
        )
    )
    namedValues = NamedValues(
        *(("configuration", 3),
          ("console", 8),
          ("dumping", 2),
          ("hw-monitoring", 5),
          ("loading", 1),
          ("messages", 4),
          ("snmp-master-agent", 7),
          ("tracing", 6),
          ("utilities", 9))
    )


_Cnt2SmSwFunction_Type.__name__ = "Integer32"
_Cnt2SmSwFunction_Object = MibTableColumn
cnt2SmSwFunction = _Cnt2SmSwFunction_Object(
    (1, 3, 6, 1, 4, 1, 333, 2, 4, 1, 2, 2, 1, 3),
    _Cnt2SmSwFunction_Type()
)
cnt2SmSwFunction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnt2SmSwFunction.setStatus("mandatory")
_Cnt2SmSwMajorVersion_Type = Integer32
_Cnt2SmSwMajorVersion_Object = MibTableColumn
cnt2SmSwMajorVersion = _Cnt2SmSwMajorVersion_Object(
    (1, 3, 6, 1, 4, 1, 333, 2, 4, 1, 2, 2, 1, 4),
    _Cnt2SmSwMajorVersion_Type()
)
cnt2SmSwMajorVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnt2SmSwMajorVersion.setStatus("mandatory")
_Cnt2SmSwMinorVersion_Type = Integer32
_Cnt2SmSwMinorVersion_Object = MibTableColumn
cnt2SmSwMinorVersion = _Cnt2SmSwMinorVersion_Object(
    (1, 3, 6, 1, 4, 1, 333, 2, 4, 1, 2, 2, 1, 5),
    _Cnt2SmSwMinorVersion_Type()
)
cnt2SmSwMinorVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnt2SmSwMinorVersion.setStatus("mandatory")
_Cnt2SmSwSlot_Type = Integer32
_Cnt2SmSwSlot_Object = MibScalar
cnt2SmSwSlot = _Cnt2SmSwSlot_Object(
    (1, 3, 6, 1, 4, 1, 333, 2, 4, 1, 2, 3),
    _Cnt2SmSwSlot_Type()
)
cnt2SmSwSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnt2SmSwSlot.setStatus("mandatory")


class _Cnt2SmSwAccess_Type(Integer32):
    """Custom type cnt2SmSwAccess based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("read-only-access", 2),
          ("read-write-access", 1))
    )


_Cnt2SmSwAccess_Type.__name__ = "Integer32"
_Cnt2SmSwAccess_Object = MibScalar
cnt2SmSwAccess = _Cnt2SmSwAccess_Object(
    (1, 3, 6, 1, 4, 1, 333, 2, 4, 1, 2, 4),
    _Cnt2SmSwAccess_Type()
)
cnt2SmSwAccess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnt2SmSwAccess.setStatus("mandatory")
_Cnt2SmMsg_ObjectIdentity = ObjectIdentity
cnt2SmMsg = _Cnt2SmMsg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 333, 2, 4, 1, 3)
)
_Cnt2SmNumMsgs_Type = Integer32
_Cnt2SmNumMsgs_Object = MibScalar
cnt2SmNumMsgs = _Cnt2SmNumMsgs_Object(
    (1, 3, 6, 1, 4, 1, 333, 2, 4, 1, 3, 1),
    _Cnt2SmNumMsgs_Type()
)
cnt2SmNumMsgs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnt2SmNumMsgs.setStatus("deprecated")
_Cnt2SmMsgTable_Object = MibTable
cnt2SmMsgTable = _Cnt2SmMsgTable_Object(
    (1, 3, 6, 1, 4, 1, 333, 2, 4, 1, 3, 2)
)
if mibBuilder.loadTexts:
    cnt2SmMsgTable.setStatus("deprecated")
_Cnt2SmMsgEntry_Object = MibTableRow
cnt2SmMsgEntry = _Cnt2SmMsgEntry_Object(
    (1, 3, 6, 1, 4, 1, 333, 2, 4, 1, 3, 2, 1)
)
cnt2SmMsgEntry.setIndexNames(
    (0, "CNT241-MIB", "cnt2SmMsgIndex"),
)
if mibBuilder.loadTexts:
    cnt2SmMsgEntry.setStatus("deprecated")
_Cnt2SmMsgIndex_Type = Integer32
_Cnt2SmMsgIndex_Object = MibTableColumn
cnt2SmMsgIndex = _Cnt2SmMsgIndex_Object(
    (1, 3, 6, 1, 4, 1, 333, 2, 4, 1, 3, 2, 1, 1),
    _Cnt2SmMsgIndex_Type()
)
cnt2SmMsgIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnt2SmMsgIndex.setStatus("deprecated")


class _Cnt2SmMsgSeverity_Type(Integer32):
    """Custom type cnt2SmMsgSeverity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8)
        )
    )
    namedValues = NamedValues(
        *(("alert", 2),
          ("criticial", 3),
          ("debug", 8),
          ("emergency", 1),
          ("error", 4),
          ("information", 7),
          ("notice", 6),
          ("warning", 5))
    )


_Cnt2SmMsgSeverity_Type.__name__ = "Integer32"
_Cnt2SmMsgSeverity_Object = MibTableColumn
cnt2SmMsgSeverity = _Cnt2SmMsgSeverity_Object(
    (1, 3, 6, 1, 4, 1, 333, 2, 4, 1, 3, 2, 1, 2),
    _Cnt2SmMsgSeverity_Type()
)
cnt2SmMsgSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnt2SmMsgSeverity.setStatus("deprecated")
_Cnt2SmMsgProcessName_Type = DisplayString
_Cnt2SmMsgProcessName_Object = MibTableColumn
cnt2SmMsgProcessName = _Cnt2SmMsgProcessName_Object(
    (1, 3, 6, 1, 4, 1, 333, 2, 4, 1, 3, 2, 1, 3),
    _Cnt2SmMsgProcessName_Type()
)
cnt2SmMsgProcessName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnt2SmMsgProcessName.setStatus("deprecated")
_Cnt2SmMsgNumber_Type = Integer32
_Cnt2SmMsgNumber_Object = MibTableColumn
cnt2SmMsgNumber = _Cnt2SmMsgNumber_Object(
    (1, 3, 6, 1, 4, 1, 333, 2, 4, 1, 3, 2, 1, 4),
    _Cnt2SmMsgNumber_Type()
)
cnt2SmMsgNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnt2SmMsgNumber.setStatus("deprecated")
_Cnt2SmMsgSlotNumber_Type = DisplayString
_Cnt2SmMsgSlotNumber_Object = MibTableColumn
cnt2SmMsgSlotNumber = _Cnt2SmMsgSlotNumber_Object(
    (1, 3, 6, 1, 4, 1, 333, 2, 4, 1, 3, 2, 1, 5),
    _Cnt2SmMsgSlotNumber_Type()
)
cnt2SmMsgSlotNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnt2SmMsgSlotNumber.setStatus("deprecated")
_Cnt2SmMsgDateTime_Type = DisplayString
_Cnt2SmMsgDateTime_Object = MibTableColumn
cnt2SmMsgDateTime = _Cnt2SmMsgDateTime_Object(
    (1, 3, 6, 1, 4, 1, 333, 2, 4, 1, 3, 2, 1, 6),
    _Cnt2SmMsgDateTime_Type()
)
cnt2SmMsgDateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnt2SmMsgDateTime.setStatus("deprecated")
_Cnt2SmMsgErrorNumber_Type = Integer32
_Cnt2SmMsgErrorNumber_Object = MibTableColumn
cnt2SmMsgErrorNumber = _Cnt2SmMsgErrorNumber_Object(
    (1, 3, 6, 1, 4, 1, 333, 2, 4, 1, 3, 2, 1, 7),
    _Cnt2SmMsgErrorNumber_Type()
)
cnt2SmMsgErrorNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnt2SmMsgErrorNumber.setStatus("deprecated")
_Cnt2SmMsgContent_Type = DisplayString
_Cnt2SmMsgContent_Object = MibTableColumn
cnt2SmMsgContent = _Cnt2SmMsgContent_Object(
    (1, 3, 6, 1, 4, 1, 333, 2, 4, 1, 3, 2, 1, 8),
    _Cnt2SmMsgContent_Type()
)
cnt2SmMsgContent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnt2SmMsgContent.setStatus("deprecated")
_Cnt2SmMessage_ObjectIdentity = ObjectIdentity
cnt2SmMessage = _Cnt2SmMessage_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 333, 2, 4, 1, 4)
)
_Cnt2SmMsgTableSize_Type = Integer32
_Cnt2SmMsgTableSize_Object = MibScalar
cnt2SmMsgTableSize = _Cnt2SmMsgTableSize_Object(
    (1, 3, 6, 1, 4, 1, 333, 2, 4, 1, 4, 1),
    _Cnt2SmMsgTableSize_Type()
)
cnt2SmMsgTableSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cnt2SmMsgTableSize.setStatus("mandatory")
_Cnt2SmMessageTable_Object = MibTable
cnt2SmMessageTable = _Cnt2SmMessageTable_Object(
    (1, 3, 6, 1, 4, 1, 333, 2, 4, 1, 4, 2)
)
if mibBuilder.loadTexts:
    cnt2SmMessageTable.setStatus("mandatory")
_Cnt2SmMessageEntry_Object = MibTableRow
cnt2SmMessageEntry = _Cnt2SmMessageEntry_Object(
    (1, 3, 6, 1, 4, 1, 333, 2, 4, 1, 4, 2, 1)
)
cnt2SmMessageEntry.setIndexNames(
    (0, "CNT241-MIB", "cnt2SmMessageText"),
)
if mibBuilder.loadTexts:
    cnt2SmMessageEntry.setStatus("mandatory")
_Cnt2SmMessageText_Type = DisplayString
_Cnt2SmMessageText_Object = MibTableColumn
cnt2SmMessageText = _Cnt2SmMessageText_Object(
    (1, 3, 6, 1, 4, 1, 333, 2, 4, 1, 4, 2, 1, 1),
    _Cnt2SmMessageText_Type()
)
cnt2SmMessageText.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnt2SmMessageText.setStatus("mandatory")
_Cnt2SmMessageIndex_Type = Integer32
_Cnt2SmMessageIndex_Object = MibTableColumn
cnt2SmMessageIndex = _Cnt2SmMessageIndex_Object(
    (1, 3, 6, 1, 4, 1, 333, 2, 4, 1, 4, 2, 1, 2),
    _Cnt2SmMessageIndex_Type()
)
cnt2SmMessageIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnt2SmMessageIndex.setStatus("mandatory")


class _Cnt2SmMsgToTrapFilter_Type(Integer32):
    """Custom type cnt2SmMsgToTrapFilter based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8)
        )
    )
    namedValues = NamedValues(
        *(("alert", 2),
          ("criticial", 3),
          ("emergency", 1),
          ("error", 4),
          ("information", 7),
          ("none", 8),
          ("notice", 6),
          ("warning", 5))
    )


_Cnt2SmMsgToTrapFilter_Type.__name__ = "Integer32"
_Cnt2SmMsgToTrapFilter_Object = MibScalar
cnt2SmMsgToTrapFilter = _Cnt2SmMsgToTrapFilter_Object(
    (1, 3, 6, 1, 4, 1, 333, 2, 4, 1, 4, 3),
    _Cnt2SmMsgToTrapFilter_Type()
)
cnt2SmMsgToTrapFilter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cnt2SmMsgToTrapFilter.setStatus("mandatory")

# Managed Objects groups


# Notification objects

cnt2smEmergencyMsg = NotificationType(
    (1, 3, 6, 1, 4, 1, 333, 2, 4, 1, 0, 1)
)
cnt2smEmergencyMsg.setObjects(
      *(("CNT241-MIB", "cnt2SmMsgProcessName"),
        ("CNT241-MIB", "cnt2SmMsgNumber"),
        ("CNT241-MIB", "cnt2SmMsgSlotNumber"),
        ("CNT241-MIB", "cnt2SmMsgDateTime"),
        ("CNT241-MIB", "cnt2SmMsgErrorNumber"),
        ("CNT241-MIB", "cnt2SmMsgContent"))
)
if mibBuilder.loadTexts:
    cnt2smEmergencyMsg.setStatus(
        ""
    )

cnt2smAlertMsg = NotificationType(
    (1, 3, 6, 1, 4, 1, 333, 2, 4, 1, 0, 2)
)
cnt2smAlertMsg.setObjects(
      *(("CNT241-MIB", "cnt2SmMsgProcessName"),
        ("CNT241-MIB", "cnt2SmMsgNumber"),
        ("CNT241-MIB", "cnt2SmMsgSlotNumber"),
        ("CNT241-MIB", "cnt2SmMsgDateTime"),
        ("CNT241-MIB", "cnt2SmMsgErrorNumber"),
        ("CNT241-MIB", "cnt2SmMsgContent"))
)
if mibBuilder.loadTexts:
    cnt2smAlertMsg.setStatus(
        ""
    )

cnt2smCriticalMsg = NotificationType(
    (1, 3, 6, 1, 4, 1, 333, 2, 4, 1, 0, 3)
)
cnt2smCriticalMsg.setObjects(
      *(("CNT241-MIB", "cnt2SmMsgProcessName"),
        ("CNT241-MIB", "cnt2SmMsgNumber"),
        ("CNT241-MIB", "cnt2SmMsgSlotNumber"),
        ("CNT241-MIB", "cnt2SmMsgDateTime"),
        ("CNT241-MIB", "cnt2SmMsgErrorNumber"),
        ("CNT241-MIB", "cnt2SmMsgContent"))
)
if mibBuilder.loadTexts:
    cnt2smCriticalMsg.setStatus(
        ""
    )

cnt2smErrorMsg = NotificationType(
    (1, 3, 6, 1, 4, 1, 333, 2, 4, 1, 0, 4)
)
cnt2smErrorMsg.setObjects(
      *(("CNT241-MIB", "cnt2SmMsgProcessName"),
        ("CNT241-MIB", "cnt2SmMsgNumber"),
        ("CNT241-MIB", "cnt2SmMsgSlotNumber"),
        ("CNT241-MIB", "cnt2SmMsgDateTime"),
        ("CNT241-MIB", "cnt2SmMsgErrorNumber"),
        ("CNT241-MIB", "cnt2SmMsgContent"))
)
if mibBuilder.loadTexts:
    cnt2smErrorMsg.setStatus(
        ""
    )

cnt2smWarningMsg = NotificationType(
    (1, 3, 6, 1, 4, 1, 333, 2, 4, 1, 0, 5)
)
cnt2smWarningMsg.setObjects(
      *(("CNT241-MIB", "cnt2SmMsgProcessName"),
        ("CNT241-MIB", "cnt2SmMsgNumber"),
        ("CNT241-MIB", "cnt2SmMsgSlotNumber"),
        ("CNT241-MIB", "cnt2SmMsgDateTime"),
        ("CNT241-MIB", "cnt2SmMsgErrorNumber"),
        ("CNT241-MIB", "cnt2SmMsgContent"))
)
if mibBuilder.loadTexts:
    cnt2smWarningMsg.setStatus(
        ""
    )

cnt2smNoticeMsg = NotificationType(
    (1, 3, 6, 1, 4, 1, 333, 2, 4, 1, 0, 6)
)
cnt2smNoticeMsg.setObjects(
      *(("CNT241-MIB", "cnt2SmMsgProcessName"),
        ("CNT241-MIB", "cnt2SmMsgNumber"),
        ("CNT241-MIB", "cnt2SmMsgSlotNumber"),
        ("CNT241-MIB", "cnt2SmMsgDateTime"),
        ("CNT241-MIB", "cnt2SmMsgErrorNumber"),
        ("CNT241-MIB", "cnt2SmMsgContent"))
)
if mibBuilder.loadTexts:
    cnt2smNoticeMsg.setStatus(
        ""
    )

cnt2smInfoMsg = NotificationType(
    (1, 3, 6, 1, 4, 1, 333, 2, 4, 1, 0, 7)
)
cnt2smInfoMsg.setObjects(
      *(("CNT241-MIB", "cnt2SmMsgProcessName"),
        ("CNT241-MIB", "cnt2SmMsgNumber"),
        ("CNT241-MIB", "cnt2SmMsgSlotNumber"),
        ("CNT241-MIB", "cnt2SmMsgDateTime"),
        ("CNT241-MIB", "cnt2SmMsgErrorNumber"),
        ("CNT241-MIB", "cnt2SmMsgContent"))
)
if mibBuilder.loadTexts:
    cnt2smInfoMsg.setStatus(
        ""
    )

cnt2smDebugMsg = NotificationType(
    (1, 3, 6, 1, 4, 1, 333, 2, 4, 1, 0, 8)
)
cnt2smDebugMsg.setObjects(
      *(("CNT241-MIB", "cnt2SmMsgProcessName"),
        ("CNT241-MIB", "cnt2SmMsgNumber"),
        ("CNT241-MIB", "cnt2SmMsgSlotNumber"),
        ("CNT241-MIB", "cnt2SmMsgDateTime"),
        ("CNT241-MIB", "cnt2SmMsgErrorNumber"),
        ("CNT241-MIB", "cnt2SmMsgContent"))
)
if mibBuilder.loadTexts:
    cnt2smDebugMsg.setStatus(
        ""
    )

cnt2smEmergencyTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 333, 2, 4, 1, 0, 9)
)
cnt2smEmergencyTrap.setObjects(
    ("CNT241-MIB", "cnt2SmMessageText")
)
if mibBuilder.loadTexts:
    cnt2smEmergencyTrap.setStatus(
        ""
    )

cnt2smAlertTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 333, 2, 4, 1, 0, 10)
)
cnt2smAlertTrap.setObjects(
    ("CNT241-MIB", "cnt2SmMessageText")
)
if mibBuilder.loadTexts:
    cnt2smAlertTrap.setStatus(
        ""
    )

cnt2smCriticalTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 333, 2, 4, 1, 0, 11)
)
cnt2smCriticalTrap.setObjects(
    ("CNT241-MIB", "cnt2SmMessageText")
)
if mibBuilder.loadTexts:
    cnt2smCriticalTrap.setStatus(
        ""
    )

cnt2smErrorTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 333, 2, 4, 1, 0, 12)
)
cnt2smErrorTrap.setObjects(
    ("CNT241-MIB", "cnt2SmMessageText")
)
if mibBuilder.loadTexts:
    cnt2smErrorTrap.setStatus(
        ""
    )

cnt2smWarningTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 333, 2, 4, 1, 0, 13)
)
cnt2smWarningTrap.setObjects(
    ("CNT241-MIB", "cnt2SmMessageText")
)
if mibBuilder.loadTexts:
    cnt2smWarningTrap.setStatus(
        ""
    )

cnt2smNoticeTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 333, 2, 4, 1, 0, 14)
)
cnt2smNoticeTrap.setObjects(
    ("CNT241-MIB", "cnt2SmMessageText")
)
if mibBuilder.loadTexts:
    cnt2smNoticeTrap.setStatus(
        ""
    )

cnt2smInfoTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 333, 2, 4, 1, 0, 15)
)
cnt2smInfoTrap.setObjects(
    ("CNT241-MIB", "cnt2SmMessageText")
)
if mibBuilder.loadTexts:
    cnt2smInfoTrap.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CNT241-MIB",
    **{"cnt2Sm": cnt2Sm,
       "cnt2smEmergencyMsg": cnt2smEmergencyMsg,
       "cnt2smAlertMsg": cnt2smAlertMsg,
       "cnt2smCriticalMsg": cnt2smCriticalMsg,
       "cnt2smErrorMsg": cnt2smErrorMsg,
       "cnt2smWarningMsg": cnt2smWarningMsg,
       "cnt2smNoticeMsg": cnt2smNoticeMsg,
       "cnt2smInfoMsg": cnt2smInfoMsg,
       "cnt2smDebugMsg": cnt2smDebugMsg,
       "cnt2smEmergencyTrap": cnt2smEmergencyTrap,
       "cnt2smAlertTrap": cnt2smAlertTrap,
       "cnt2smCriticalTrap": cnt2smCriticalTrap,
       "cnt2smErrorTrap": cnt2smErrorTrap,
       "cnt2smWarningTrap": cnt2smWarningTrap,
       "cnt2smNoticeTrap": cnt2smNoticeTrap,
       "cnt2smInfoTrap": cnt2smInfoTrap,
       "cnt2SmHw": cnt2SmHw,
       "cnt2SmHwTemperatureF": cnt2SmHwTemperatureF,
       "cnt2SmHwTapeDriveState": cnt2SmHwTapeDriveState,
       "cnt2SmHwCdRomDriveState": cnt2SmHwCdRomDriveState,
       "cnt2SmHwTapeMounted": cnt2SmHwTapeMounted,
       "cnt2SmHwCdRomMounted": cnt2SmHwCdRomMounted,
       "cnt2SmHwServiceLed": cnt2SmHwServiceLed,
       "cnt2SmHwIplSwitch": cnt2SmHwIplSwitch,
       "cnt2SmHwAdapterTable": cnt2SmHwAdapterTable,
       "cnt2SmHwAdapterEntry": cnt2SmHwAdapterEntry,
       "cnt2SmHwAdapterIndex": cnt2SmHwAdapterIndex,
       "cnt2SmHwAdapterOperState": cnt2SmHwAdapterOperState,
       "cnt2SmHwAdapterAdminState": cnt2SmHwAdapterAdminState,
       "cnt2SmHwCardTable": cnt2SmHwCardTable,
       "cnt2SmHwCardEntry": cnt2SmHwCardEntry,
       "cnt2SmCardAdapterIndex": cnt2SmCardAdapterIndex,
       "cnt2SmHwCardIndex": cnt2SmHwCardIndex,
       "cnt2SmHwCardOperState": cnt2SmHwCardOperState,
       "cnt2SmHwCardAdminState": cnt2SmHwCardAdminState,
       "cnt2SmHwPowerSupplyTable": cnt2SmHwPowerSupplyTable,
       "cnt2SmHwPowerSupplyEntry": cnt2SmHwPowerSupplyEntry,
       "cnt2SmHwPowerSupplyIndex": cnt2SmHwPowerSupplyIndex,
       "cnt2SmHwPowerSupplyACState": cnt2SmHwPowerSupplyACState,
       "cnt2SmHwPowerSupplyDCState": cnt2SmHwPowerSupplyDCState,
       "cnt2SmHwFanTable": cnt2SmHwFanTable,
       "cnt2SmHwFanEntry": cnt2SmHwFanEntry,
       "cnt2SmHwFanIndex": cnt2SmHwFanIndex,
       "cnt2SmHwFanState": cnt2SmHwFanState,
       "cnt2SmSw": cnt2SmSw,
       "cnt2SmNumModules": cnt2SmNumModules,
       "cnt2SmSwTable": cnt2SmSwTable,
       "cnt2SmSwEntry": cnt2SmSwEntry,
       "cnt2SmSwIndex": cnt2SmSwIndex,
       "cnt2SmSwName": cnt2SmSwName,
       "cnt2SmSwFunction": cnt2SmSwFunction,
       "cnt2SmSwMajorVersion": cnt2SmSwMajorVersion,
       "cnt2SmSwMinorVersion": cnt2SmSwMinorVersion,
       "cnt2SmSwSlot": cnt2SmSwSlot,
       "cnt2SmSwAccess": cnt2SmSwAccess,
       "cnt2SmMsg": cnt2SmMsg,
       "cnt2SmNumMsgs": cnt2SmNumMsgs,
       "cnt2SmMsgTable": cnt2SmMsgTable,
       "cnt2SmMsgEntry": cnt2SmMsgEntry,
       "cnt2SmMsgIndex": cnt2SmMsgIndex,
       "cnt2SmMsgSeverity": cnt2SmMsgSeverity,
       "cnt2SmMsgProcessName": cnt2SmMsgProcessName,
       "cnt2SmMsgNumber": cnt2SmMsgNumber,
       "cnt2SmMsgSlotNumber": cnt2SmMsgSlotNumber,
       "cnt2SmMsgDateTime": cnt2SmMsgDateTime,
       "cnt2SmMsgErrorNumber": cnt2SmMsgErrorNumber,
       "cnt2SmMsgContent": cnt2SmMsgContent,
       "cnt2SmMessage": cnt2SmMessage,
       "cnt2SmMsgTableSize": cnt2SmMsgTableSize,
       "cnt2SmMessageTable": cnt2SmMessageTable,
       "cnt2SmMessageEntry": cnt2SmMessageEntry,
       "cnt2SmMessageText": cnt2SmMessageText,
       "cnt2SmMessageIndex": cnt2SmMessageIndex,
       "cnt2SmMsgToTrapFilter": cnt2SmMsgToTrapFilter}
)
