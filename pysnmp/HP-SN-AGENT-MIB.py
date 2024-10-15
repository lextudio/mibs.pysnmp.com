# SNMP MIB module (HP-SN-AGENT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HP-SN-AGENT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:58:40 2024
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

(snAgentSys,
 snChassis,
 snStack) = mibBuilder.importSymbols(
    "HP-SN-ROOT-MIB",
    "snAgentSys",
    "snChassis",
    "snStack")

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


# MODULE-IDENTITY


# Types definitions



class DisplayString(OctetString):
    """Custom type DisplayString based on OctetString"""




class MacAddress(OctetString):
    """Custom type MacAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )




# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_SnChasGen_ObjectIdentity = ObjectIdentity
snChasGen = _SnChasGen_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 1, 1)
)


class _SnChasType_Type(DisplayString):
    """Custom type snChasType based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_SnChasType_Type.__name__ = "DisplayString"
_SnChasType_Object = MibScalar
snChasType = _SnChasType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 1, 1, 1),
    _SnChasType_Type()
)
snChasType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snChasType.setStatus("mandatory")


class _SnChasSerNum_Type(DisplayString):
    """Custom type snChasSerNum based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_SnChasSerNum_Type.__name__ = "DisplayString"
_SnChasSerNum_Object = MibScalar
snChasSerNum = _SnChasSerNum_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 1, 1, 2),
    _SnChasSerNum_Type()
)
snChasSerNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snChasSerNum.setStatus("mandatory")
_SnChasPwrSupplyStatus_Type = Integer32
_SnChasPwrSupplyStatus_Object = MibScalar
snChasPwrSupplyStatus = _SnChasPwrSupplyStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 1, 1, 3),
    _SnChasPwrSupplyStatus_Type()
)
snChasPwrSupplyStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snChasPwrSupplyStatus.setStatus("mandatory")
_SnChasFanStatus_Type = Integer32
_SnChasFanStatus_Object = MibScalar
snChasFanStatus = _SnChasFanStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 1, 1, 4),
    _SnChasFanStatus_Type()
)
snChasFanStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snChasFanStatus.setStatus("mandatory")


class _SnChasMainBrdDescription_Type(DisplayString):
    """Custom type snChasMainBrdDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_SnChasMainBrdDescription_Type.__name__ = "DisplayString"
_SnChasMainBrdDescription_Object = MibScalar
snChasMainBrdDescription = _SnChasMainBrdDescription_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 1, 1, 5),
    _SnChasMainBrdDescription_Type()
)
snChasMainBrdDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snChasMainBrdDescription.setStatus("mandatory")


class _SnChasMainPortTotal_Type(Integer32):
    """Custom type snChasMainPortTotal based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 24),
    )


_SnChasMainPortTotal_Type.__name__ = "Integer32"
_SnChasMainPortTotal_Object = MibScalar
snChasMainPortTotal = _SnChasMainPortTotal_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 1, 1, 6),
    _SnChasMainPortTotal_Type()
)
snChasMainPortTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snChasMainPortTotal.setStatus("mandatory")


class _SnChasExpBrdDescription_Type(DisplayString):
    """Custom type snChasExpBrdDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_SnChasExpBrdDescription_Type.__name__ = "DisplayString"
_SnChasExpBrdDescription_Object = MibScalar
snChasExpBrdDescription = _SnChasExpBrdDescription_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 1, 1, 7),
    _SnChasExpBrdDescription_Type()
)
snChasExpBrdDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snChasExpBrdDescription.setStatus("mandatory")


class _SnChasExpPortTotal_Type(Integer32):
    """Custom type snChasExpPortTotal based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 24),
    )


_SnChasExpPortTotal_Type.__name__ = "Integer32"
_SnChasExpPortTotal_Object = MibScalar
snChasExpPortTotal = _SnChasExpPortTotal_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 1, 1, 8),
    _SnChasExpPortTotal_Type()
)
snChasExpPortTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snChasExpPortTotal.setStatus("mandatory")
_SnChasStatusLeds_Type = Integer32
_SnChasStatusLeds_Object = MibScalar
snChasStatusLeds = _SnChasStatusLeds_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 1, 1, 9),
    _SnChasStatusLeds_Type()
)
snChasStatusLeds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snChasStatusLeds.setStatus("mandatory")
_SnChasTrafficLeds_Type = Integer32
_SnChasTrafficLeds_Object = MibScalar
snChasTrafficLeds = _SnChasTrafficLeds_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 1, 1, 10),
    _SnChasTrafficLeds_Type()
)
snChasTrafficLeds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snChasTrafficLeds.setStatus("mandatory")
_SnChasMediaLeds_Type = Integer32
_SnChasMediaLeds_Object = MibScalar
snChasMediaLeds = _SnChasMediaLeds_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 1, 1, 11),
    _SnChasMediaLeds_Type()
)
snChasMediaLeds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snChasMediaLeds.setStatus("mandatory")


class _SnChasEnablePwrSupplyTrap_Type(Integer32):
    """Custom type snChasEnablePwrSupplyTrap based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_SnChasEnablePwrSupplyTrap_Type.__name__ = "Integer32"
_SnChasEnablePwrSupplyTrap_Object = MibScalar
snChasEnablePwrSupplyTrap = _SnChasEnablePwrSupplyTrap_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 1, 1, 12),
    _SnChasEnablePwrSupplyTrap_Type()
)
snChasEnablePwrSupplyTrap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snChasEnablePwrSupplyTrap.setStatus("mandatory")
_SnChasMainBrdId_Type = OctetString
_SnChasMainBrdId_Object = MibScalar
snChasMainBrdId = _SnChasMainBrdId_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 1, 1, 13),
    _SnChasMainBrdId_Type()
)
snChasMainBrdId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snChasMainBrdId.setStatus("mandatory")
_SnChasExpBrdId_Type = OctetString
_SnChasExpBrdId_Object = MibScalar
snChasExpBrdId = _SnChasExpBrdId_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 1, 1, 14),
    _SnChasExpBrdId_Type()
)
snChasExpBrdId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snChasExpBrdId.setStatus("mandatory")
_SnChasSpeedLeds_Type = Integer32
_SnChasSpeedLeds_Object = MibScalar
snChasSpeedLeds = _SnChasSpeedLeds_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 1, 1, 15),
    _SnChasSpeedLeds_Type()
)
snChasSpeedLeds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snChasSpeedLeds.setStatus("mandatory")


class _SnChasEnableFanTrap_Type(Integer32):
    """Custom type snChasEnableFanTrap based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_SnChasEnableFanTrap_Type.__name__ = "Integer32"
_SnChasEnableFanTrap_Object = MibScalar
snChasEnableFanTrap = _SnChasEnableFanTrap_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 1, 1, 16),
    _SnChasEnableFanTrap_Type()
)
snChasEnableFanTrap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snChasEnableFanTrap.setStatus("mandatory")


class _SnChasIdNumber_Type(DisplayString):
    """Custom type snChasIdNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_SnChasIdNumber_Type.__name__ = "DisplayString"
_SnChasIdNumber_Object = MibScalar
snChasIdNumber = _SnChasIdNumber_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 1, 1, 17),
    _SnChasIdNumber_Type()
)
snChasIdNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snChasIdNumber.setStatus("mandatory")


class _SnChasActualTemperature_Type(Integer32):
    """Custom type snChasActualTemperature based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-110, 250),
    )


_SnChasActualTemperature_Type.__name__ = "Integer32"
_SnChasActualTemperature_Object = MibScalar
snChasActualTemperature = _SnChasActualTemperature_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 1, 1, 18),
    _SnChasActualTemperature_Type()
)
snChasActualTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snChasActualTemperature.setStatus("mandatory")


class _SnChasWarningTemperature_Type(Integer32):
    """Custom type snChasWarningTemperature based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 250),
    )


_SnChasWarningTemperature_Type.__name__ = "Integer32"
_SnChasWarningTemperature_Object = MibScalar
snChasWarningTemperature = _SnChasWarningTemperature_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 1, 1, 19),
    _SnChasWarningTemperature_Type()
)
snChasWarningTemperature.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snChasWarningTemperature.setStatus("mandatory")


class _SnChasShutdownTemperature_Type(Integer32):
    """Custom type snChasShutdownTemperature based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 250),
    )


_SnChasShutdownTemperature_Type.__name__ = "Integer32"
_SnChasShutdownTemperature_Object = MibScalar
snChasShutdownTemperature = _SnChasShutdownTemperature_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 1, 1, 20),
    _SnChasShutdownTemperature_Type()
)
snChasShutdownTemperature.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snChasShutdownTemperature.setStatus("mandatory")


class _SnChasEnableTempWarnTrap_Type(Integer32):
    """Custom type snChasEnableTempWarnTrap based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_SnChasEnableTempWarnTrap_Type.__name__ = "Integer32"
_SnChasEnableTempWarnTrap_Object = MibScalar
snChasEnableTempWarnTrap = _SnChasEnableTempWarnTrap_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 1, 1, 21),
    _SnChasEnableTempWarnTrap_Type()
)
snChasEnableTempWarnTrap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snChasEnableTempWarnTrap.setStatus("mandatory")
_SnChasPwr_ObjectIdentity = ObjectIdentity
snChasPwr = _SnChasPwr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 1, 2)
)
_SnChasPwrSupplyTable_Object = MibTable
snChasPwrSupplyTable = _SnChasPwrSupplyTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 1, 2, 1)
)
if mibBuilder.loadTexts:
    snChasPwrSupplyTable.setStatus("mandatory")
_SnChasPwrSupplyEntry_Object = MibTableRow
snChasPwrSupplyEntry = _SnChasPwrSupplyEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 1, 2, 1, 1)
)
snChasPwrSupplyEntry.setIndexNames(
    (0, "HP-SN-AGENT-MIB", "snChasPwrSupplyIndex"),
)
if mibBuilder.loadTexts:
    snChasPwrSupplyEntry.setStatus("mandatory")
_SnChasPwrSupplyIndex_Type = Integer32
_SnChasPwrSupplyIndex_Object = MibTableColumn
snChasPwrSupplyIndex = _SnChasPwrSupplyIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 1, 2, 1, 1, 1),
    _SnChasPwrSupplyIndex_Type()
)
snChasPwrSupplyIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snChasPwrSupplyIndex.setStatus("mandatory")


class _SnChasPwrSupplyDescription_Type(DisplayString):
    """Custom type snChasPwrSupplyDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_SnChasPwrSupplyDescription_Type.__name__ = "DisplayString"
_SnChasPwrSupplyDescription_Object = MibTableColumn
snChasPwrSupplyDescription = _SnChasPwrSupplyDescription_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 1, 2, 1, 1, 2),
    _SnChasPwrSupplyDescription_Type()
)
snChasPwrSupplyDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snChasPwrSupplyDescription.setStatus("mandatory")


class _SnChasPwrSupplyOperStatus_Type(Integer32):
    """Custom type snChasPwrSupplyOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("failure", 3),
          ("normal", 2),
          ("other", 1))
    )


_SnChasPwrSupplyOperStatus_Type.__name__ = "Integer32"
_SnChasPwrSupplyOperStatus_Object = MibTableColumn
snChasPwrSupplyOperStatus = _SnChasPwrSupplyOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 1, 2, 1, 1, 3),
    _SnChasPwrSupplyOperStatus_Type()
)
snChasPwrSupplyOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snChasPwrSupplyOperStatus.setStatus("mandatory")
_SnChasFan_ObjectIdentity = ObjectIdentity
snChasFan = _SnChasFan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 1, 3)
)
_SnChasFanTable_Object = MibTable
snChasFanTable = _SnChasFanTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 1, 3, 1)
)
if mibBuilder.loadTexts:
    snChasFanTable.setStatus("mandatory")
_SnChasFanEntry_Object = MibTableRow
snChasFanEntry = _SnChasFanEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 1, 3, 1, 1)
)
snChasFanEntry.setIndexNames(
    (0, "HP-SN-AGENT-MIB", "snChasFanIndex"),
)
if mibBuilder.loadTexts:
    snChasFanEntry.setStatus("mandatory")
_SnChasFanIndex_Type = Integer32
_SnChasFanIndex_Object = MibTableColumn
snChasFanIndex = _SnChasFanIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 1, 3, 1, 1, 1),
    _SnChasFanIndex_Type()
)
snChasFanIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snChasFanIndex.setStatus("mandatory")


class _SnChasFanDescription_Type(DisplayString):
    """Custom type snChasFanDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_SnChasFanDescription_Type.__name__ = "DisplayString"
_SnChasFanDescription_Object = MibTableColumn
snChasFanDescription = _SnChasFanDescription_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 1, 3, 1, 1, 2),
    _SnChasFanDescription_Type()
)
snChasFanDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snChasFanDescription.setStatus("mandatory")


class _SnChasFanOperStatus_Type(Integer32):
    """Custom type snChasFanOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("failure", 3),
          ("normal", 2),
          ("other", 1))
    )


_SnChasFanOperStatus_Type.__name__ = "Integer32"
_SnChasFanOperStatus_Object = MibTableColumn
snChasFanOperStatus = _SnChasFanOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 1, 3, 1, 1, 3),
    _SnChasFanOperStatus_Type()
)
snChasFanOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snChasFanOperStatus.setStatus("mandatory")
_SnAgentGbl_ObjectIdentity = ObjectIdentity
snAgentGbl = _SnAgentGbl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 2, 1)
)


class _SnAgReload_Type(Integer32):
    """Custom type snAgReload based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("reset", 3),
          ("running", 2))
    )


_SnAgReload_Type.__name__ = "Integer32"
_SnAgReload_Object = MibScalar
snAgReload = _SnAgReload_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 2, 1, 1),
    _SnAgReload_Type()
)
snAgReload.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snAgReload.setStatus("mandatory")


class _SnAgEraseNVRAM_Type(Integer32):
    """Custom type snAgEraseNVRAM based on Integer32"""
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
        *(("erase", 3),
          ("erasing", 4),
          ("error", 2),
          ("normal", 1))
    )


_SnAgEraseNVRAM_Type.__name__ = "Integer32"
_SnAgEraseNVRAM_Object = MibScalar
snAgEraseNVRAM = _SnAgEraseNVRAM_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 2, 1, 2),
    _SnAgEraseNVRAM_Type()
)
snAgEraseNVRAM.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snAgEraseNVRAM.setStatus("mandatory")


class _SnAgWriteNVRAM_Type(Integer32):
    """Custom type snAgWriteNVRAM based on Integer32"""
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
        *(("error", 2),
          ("normal", 1),
          ("write", 3),
          ("writing", 4))
    )


_SnAgWriteNVRAM_Type.__name__ = "Integer32"
_SnAgWriteNVRAM_Object = MibScalar
snAgWriteNVRAM = _SnAgWriteNVRAM_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 2, 1, 3),
    _SnAgWriteNVRAM_Type()
)
snAgWriteNVRAM.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snAgWriteNVRAM.setStatus("mandatory")


class _SnAgConfigFromNVRAM_Type(Integer32):
    """Custom type snAgConfigFromNVRAM based on Integer32"""
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
        *(("config", 3),
          ("configing", 4),
          ("error", 2),
          ("normal", 1))
    )


_SnAgConfigFromNVRAM_Type.__name__ = "Integer32"
_SnAgConfigFromNVRAM_Object = MibScalar
snAgConfigFromNVRAM = _SnAgConfigFromNVRAM_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 2, 1, 4),
    _SnAgConfigFromNVRAM_Type()
)
snAgConfigFromNVRAM.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    snAgConfigFromNVRAM.setStatus("mandatory")
_SnAgTftpServerIp_Type = IpAddress
_SnAgTftpServerIp_Object = MibScalar
snAgTftpServerIp = _SnAgTftpServerIp_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 2, 1, 5),
    _SnAgTftpServerIp_Type()
)
snAgTftpServerIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snAgTftpServerIp.setStatus("mandatory")


class _SnAgImgFname_Type(DisplayString):
    """Custom type snAgImgFname based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_SnAgImgFname_Type.__name__ = "DisplayString"
_SnAgImgFname_Object = MibScalar
snAgImgFname = _SnAgImgFname_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 2, 1, 6),
    _SnAgImgFname_Type()
)
snAgImgFname.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snAgImgFname.setStatus("mandatory")


class _SnAgImgLoad_Type(Integer32):
    """Custom type snAgImgLoad based on Integer32"""
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
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              17,
              18,
              19,
              20,
              21,
              22,
              23)
        )
    )
    namedValues = NamedValues(
        *(("downloadPrimary", 20),
          ("downloadSecondary", 22),
          ("flashPrepareReadFailure", 2),
          ("flashPrepareWriteFailure", 4),
          ("flashReadError", 3),
          ("flashWriteError", 5),
          ("loading", 18),
          ("normal", 1),
          ("operationError", 17),
          ("tftpBusy", 8),
          ("tftpOutOfBufferSpace", 7),
          ("tftpRemoteBadAccess", 11),
          ("tftpRemoteBadId", 14),
          ("tftpRemoteBadOperation", 13),
          ("tftpRemoteDiskFull", 12),
          ("tftpRemoteFileExists", 15),
          ("tftpRemoteNoFile", 10),
          ("tftpRemoteNoUser", 16),
          ("tftpRemoteOtherErrors", 9),
          ("tftpTimeoutError", 6),
          ("tftpWrongFileType", 23),
          ("uploadPrimary", 19),
          ("uploadSecondary", 21))
    )


_SnAgImgLoad_Type.__name__ = "Integer32"
_SnAgImgLoad_Object = MibScalar
snAgImgLoad = _SnAgImgLoad_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 2, 1, 7),
    _SnAgImgLoad_Type()
)
snAgImgLoad.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snAgImgLoad.setStatus("mandatory")


class _SnAgCfgFname_Type(DisplayString):
    """Custom type snAgCfgFname based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_SnAgCfgFname_Type.__name__ = "DisplayString"
_SnAgCfgFname_Object = MibScalar
snAgCfgFname = _SnAgCfgFname_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 2, 1, 8),
    _SnAgCfgFname_Type()
)
snAgCfgFname.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snAgCfgFname.setStatus("mandatory")


class _SnAgCfgLoad_Type(Integer32):
    """Custom type snAgCfgLoad based on Integer32"""
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
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              17,
              18,
              20,
              21,
              22,
              23,
              24,
              25,
              26,
              27,
              28,
              29)
        )
    )
    namedValues = NamedValues(
        *(("downloadToDramFromNMS", 27),
          ("downloadToDramFromServer", 23),
          ("downloadToFlashFromNMS", 25),
          ("downloadToFlashFromServer", 21),
          ("flashPrepareReadFailure", 2),
          ("flashPrepareWriteFailure", 4),
          ("flashReadError", 3),
          ("flashWriteError", 5),
          ("loading", 18),
          ("normal", 1),
          ("operationDoneWithNMS", 28),
          ("operationError", 17),
          ("tftpBusy", 8),
          ("tftpOutOfBufferSpace", 7),
          ("tftpRemoteBadAccess", 11),
          ("tftpRemoteBadId", 14),
          ("tftpRemoteBadOperation", 13),
          ("tftpRemoteDiskFull", 12),
          ("tftpRemoteFileExists", 15),
          ("tftpRemoteNoFile", 10),
          ("tftpRemoteNoUser", 16),
          ("tftpRemoteOtherErrors", 9),
          ("tftpTimeoutError", 6),
          ("tftpWrongFileType", 29),
          ("uploadFromDramToNMS", 26),
          ("uploadFromDramToServer", 22),
          ("uploadFromFlashToNMS", 24),
          ("uploadFromFlashToServer", 20))
    )


_SnAgCfgLoad_Type.__name__ = "Integer32"
_SnAgCfgLoad_Object = MibScalar
snAgCfgLoad = _SnAgCfgLoad_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 2, 1, 9),
    _SnAgCfgLoad_Type()
)
snAgCfgLoad.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snAgCfgLoad.setStatus("mandatory")
_SnAgDefGwayIp_Type = IpAddress
_SnAgDefGwayIp_Object = MibScalar
snAgDefGwayIp = _SnAgDefGwayIp_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 2, 1, 10),
    _SnAgDefGwayIp_Type()
)
snAgDefGwayIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snAgDefGwayIp.setStatus("mandatory")


class _SnAgImgVer_Type(DisplayString):
    """Custom type snAgImgVer based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_SnAgImgVer_Type.__name__ = "DisplayString"
_SnAgImgVer_Object = MibScalar
snAgImgVer = _SnAgImgVer_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 2, 1, 11),
    _SnAgImgVer_Type()
)
snAgImgVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snAgImgVer.setStatus("mandatory")


class _SnAgFlashImgVer_Type(DisplayString):
    """Custom type snAgFlashImgVer based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_SnAgFlashImgVer_Type.__name__ = "DisplayString"
_SnAgFlashImgVer_Object = MibScalar
snAgFlashImgVer = _SnAgFlashImgVer_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 2, 1, 12),
    _SnAgFlashImgVer_Type()
)
snAgFlashImgVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snAgFlashImgVer.setStatus("mandatory")
_SnAgGblIfIpAddr_Type = IpAddress
_SnAgGblIfIpAddr_Object = MibScalar
snAgGblIfIpAddr = _SnAgGblIfIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 2, 1, 13),
    _SnAgGblIfIpAddr_Type()
)
snAgGblIfIpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snAgGblIfIpAddr.setStatus("mandatory")
_SnAgGblIfIpMask_Type = IpAddress
_SnAgGblIfIpMask_Object = MibScalar
snAgGblIfIpMask = _SnAgGblIfIpMask_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 2, 1, 14),
    _SnAgGblIfIpMask_Type()
)
snAgGblIfIpMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snAgGblIfIpMask.setStatus("mandatory")


class _SnAgGblPassword_Type(DisplayString):
    """Custom type snAgGblPassword based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 48),
    )


_SnAgGblPassword_Type.__name__ = "DisplayString"
_SnAgGblPassword_Object = MibScalar
snAgGblPassword = _SnAgGblPassword_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 2, 1, 15),
    _SnAgGblPassword_Type()
)
snAgGblPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snAgGblPassword.setStatus("mandatory")


class _SnAgTrpRcvrCurEntry_Type(Integer32):
    """Custom type snAgTrpRcvrCurEntry based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_SnAgTrpRcvrCurEntry_Type.__name__ = "Integer32"
_SnAgTrpRcvrCurEntry_Object = MibScalar
snAgTrpRcvrCurEntry = _SnAgTrpRcvrCurEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 2, 1, 16),
    _SnAgTrpRcvrCurEntry_Type()
)
snAgTrpRcvrCurEntry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snAgTrpRcvrCurEntry.setStatus("mandatory")


class _SnAgGblDataRetrieveMode_Type(Integer32):
    """Custom type snAgGblDataRetrieveMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("nextbootCfg", 0),
          ("operationalData", 1))
    )


_SnAgGblDataRetrieveMode_Type.__name__ = "Integer32"
_SnAgGblDataRetrieveMode_Object = MibScalar
snAgGblDataRetrieveMode = _SnAgGblDataRetrieveMode_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 2, 1, 19),
    _SnAgGblDataRetrieveMode_Type()
)
snAgGblDataRetrieveMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snAgGblDataRetrieveMode.setStatus("mandatory")


class _SnAgSystemLog_Type(OctetString):
    """Custom type snAgSystemLog based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(5, 5),
    )


_SnAgSystemLog_Type.__name__ = "OctetString"
_SnAgSystemLog_Object = MibScalar
snAgSystemLog = _SnAgSystemLog_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 2, 1, 20),
    _SnAgSystemLog_Type()
)
snAgSystemLog.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snAgSystemLog.setStatus("mandatory")


class _SnAgGblEnableColdStartTrap_Type(Integer32):
    """Custom type snAgGblEnableColdStartTrap based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_SnAgGblEnableColdStartTrap_Type.__name__ = "Integer32"
_SnAgGblEnableColdStartTrap_Object = MibScalar
snAgGblEnableColdStartTrap = _SnAgGblEnableColdStartTrap_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 2, 1, 21),
    _SnAgGblEnableColdStartTrap_Type()
)
snAgGblEnableColdStartTrap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snAgGblEnableColdStartTrap.setStatus("mandatory")


class _SnAgGblEnableLinkUpTrap_Type(Integer32):
    """Custom type snAgGblEnableLinkUpTrap based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_SnAgGblEnableLinkUpTrap_Type.__name__ = "Integer32"
_SnAgGblEnableLinkUpTrap_Object = MibScalar
snAgGblEnableLinkUpTrap = _SnAgGblEnableLinkUpTrap_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 2, 1, 22),
    _SnAgGblEnableLinkUpTrap_Type()
)
snAgGblEnableLinkUpTrap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snAgGblEnableLinkUpTrap.setStatus("mandatory")


class _SnAgGblEnableLinkDownTrap_Type(Integer32):
    """Custom type snAgGblEnableLinkDownTrap based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_SnAgGblEnableLinkDownTrap_Type.__name__ = "Integer32"
_SnAgGblEnableLinkDownTrap_Object = MibScalar
snAgGblEnableLinkDownTrap = _SnAgGblEnableLinkDownTrap_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 2, 1, 23),
    _SnAgGblEnableLinkDownTrap_Type()
)
snAgGblEnableLinkDownTrap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snAgGblEnableLinkDownTrap.setStatus("mandatory")


class _SnAgGblPasswordChangeMode_Type(Integer32):
    """Custom type snAgGblPasswordChangeMode based on Integer32"""
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
        *(("anyMgmtEntity", 1),
          ("consoleAndTelnet", 2),
          ("consoleOnly", 3),
          ("telnetOnly", 4))
    )


_SnAgGblPasswordChangeMode_Type.__name__ = "Integer32"
_SnAgGblPasswordChangeMode_Object = MibScalar
snAgGblPasswordChangeMode = _SnAgGblPasswordChangeMode_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 2, 1, 24),
    _SnAgGblPasswordChangeMode_Type()
)
snAgGblPasswordChangeMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snAgGblPasswordChangeMode.setStatus("mandatory")


class _SnAgGblReadOnlyCommunity_Type(DisplayString):
    """Custom type snAgGblReadOnlyCommunity based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_SnAgGblReadOnlyCommunity_Type.__name__ = "DisplayString"
_SnAgGblReadOnlyCommunity_Object = MibScalar
snAgGblReadOnlyCommunity = _SnAgGblReadOnlyCommunity_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 2, 1, 25),
    _SnAgGblReadOnlyCommunity_Type()
)
snAgGblReadOnlyCommunity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snAgGblReadOnlyCommunity.setStatus("mandatory")


class _SnAgGblReadWriteCommunity_Type(DisplayString):
    """Custom type snAgGblReadWriteCommunity based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_SnAgGblReadWriteCommunity_Type.__name__ = "DisplayString"
_SnAgGblReadWriteCommunity_Object = MibScalar
snAgGblReadWriteCommunity = _SnAgGblReadWriteCommunity_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 2, 1, 26),
    _SnAgGblReadWriteCommunity_Type()
)
snAgGblReadWriteCommunity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snAgGblReadWriteCommunity.setStatus("mandatory")


class _SnAgGblCurrentSecurityLevel_Type(Integer32):
    """Custom type snAgGblCurrentSecurityLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5),
    )


_SnAgGblCurrentSecurityLevel_Type.__name__ = "Integer32"
_SnAgGblCurrentSecurityLevel_Object = MibScalar
snAgGblCurrentSecurityLevel = _SnAgGblCurrentSecurityLevel_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 2, 1, 27),
    _SnAgGblCurrentSecurityLevel_Type()
)
snAgGblCurrentSecurityLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snAgGblCurrentSecurityLevel.setStatus("mandatory")


class _SnAgGblSecurityLevelSet_Type(Integer32):
    """Custom type snAgGblSecurityLevelSet based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5),
    )


_SnAgGblSecurityLevelSet_Type.__name__ = "Integer32"
_SnAgGblSecurityLevelSet_Object = MibScalar
snAgGblSecurityLevelSet = _SnAgGblSecurityLevelSet_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 2, 1, 28),
    _SnAgGblSecurityLevelSet_Type()
)
snAgGblSecurityLevelSet.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snAgGblSecurityLevelSet.setStatus("mandatory")
_SnAgGblLevelPasswordsMask_Type = Integer32
_SnAgGblLevelPasswordsMask_Object = MibScalar
snAgGblLevelPasswordsMask = _SnAgGblLevelPasswordsMask_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 2, 1, 29),
    _SnAgGblLevelPasswordsMask_Type()
)
snAgGblLevelPasswordsMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snAgGblLevelPasswordsMask.setStatus("mandatory")


class _SnAgGblQueueOverflow_Type(Integer32):
    """Custom type snAgGblQueueOverflow based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("false", 0),
          ("true", 1))
    )


_SnAgGblQueueOverflow_Type.__name__ = "Integer32"
_SnAgGblQueueOverflow_Object = MibScalar
snAgGblQueueOverflow = _SnAgGblQueueOverflow_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 2, 1, 30),
    _SnAgGblQueueOverflow_Type()
)
snAgGblQueueOverflow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snAgGblQueueOverflow.setStatus("mandatory")


class _SnAgGblBufferShortage_Type(Integer32):
    """Custom type snAgGblBufferShortage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("false", 0),
          ("true", 1))
    )


_SnAgGblBufferShortage_Type.__name__ = "Integer32"
_SnAgGblBufferShortage_Object = MibScalar
snAgGblBufferShortage = _SnAgGblBufferShortage_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 2, 1, 31),
    _SnAgGblBufferShortage_Type()
)
snAgGblBufferShortage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snAgGblBufferShortage.setStatus("mandatory")


class _SnAgGblDmaFailure_Type(Integer32):
    """Custom type snAgGblDmaFailure based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("false", 0),
          ("true", 1))
    )


_SnAgGblDmaFailure_Type.__name__ = "Integer32"
_SnAgGblDmaFailure_Object = MibScalar
snAgGblDmaFailure = _SnAgGblDmaFailure_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 2, 1, 32),
    _SnAgGblDmaFailure_Type()
)
snAgGblDmaFailure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snAgGblDmaFailure.setStatus("mandatory")


class _SnAgGblResourceLowWarning_Type(Integer32):
    """Custom type snAgGblResourceLowWarning based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("false", 0),
          ("true", 1))
    )


_SnAgGblResourceLowWarning_Type.__name__ = "Integer32"
_SnAgGblResourceLowWarning_Object = MibScalar
snAgGblResourceLowWarning = _SnAgGblResourceLowWarning_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 2, 1, 33),
    _SnAgGblResourceLowWarning_Type()
)
snAgGblResourceLowWarning.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snAgGblResourceLowWarning.setStatus("mandatory")


class _SnAgGblExcessiveErrorWarning_Type(Integer32):
    """Custom type snAgGblExcessiveErrorWarning based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("false", 0),
          ("true", 1))
    )


_SnAgGblExcessiveErrorWarning_Type.__name__ = "Integer32"
_SnAgGblExcessiveErrorWarning_Object = MibScalar
snAgGblExcessiveErrorWarning = _SnAgGblExcessiveErrorWarning_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 2, 1, 34),
    _SnAgGblExcessiveErrorWarning_Type()
)
snAgGblExcessiveErrorWarning.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snAgGblExcessiveErrorWarning.setStatus("mandatory")
_SnAgGblCpuUtilData_Type = Gauge32
_SnAgGblCpuUtilData_Object = MibScalar
snAgGblCpuUtilData = _SnAgGblCpuUtilData_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 2, 1, 35),
    _SnAgGblCpuUtilData_Type()
)
snAgGblCpuUtilData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snAgGblCpuUtilData.setStatus("mandatory")


class _SnAgGblCpuUtilCollect_Type(Integer32):
    """Custom type snAgGblCpuUtilCollect based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_SnAgGblCpuUtilCollect_Type.__name__ = "Integer32"
_SnAgGblCpuUtilCollect_Object = MibScalar
snAgGblCpuUtilCollect = _SnAgGblCpuUtilCollect_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 2, 1, 36),
    _SnAgGblCpuUtilCollect_Type()
)
snAgGblCpuUtilCollect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snAgGblCpuUtilCollect.setStatus("mandatory")


class _SnAgGblTelnetTimeout_Type(Integer32):
    """Custom type snAgGblTelnetTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 240),
    )


_SnAgGblTelnetTimeout_Type.__name__ = "Integer32"
_SnAgGblTelnetTimeout_Object = MibScalar
snAgGblTelnetTimeout = _SnAgGblTelnetTimeout_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 2, 1, 37),
    _SnAgGblTelnetTimeout_Type()
)
snAgGblTelnetTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snAgGblTelnetTimeout.setStatus("mandatory")


class _SnAgGblEnableWebMgmt_Type(Integer32):
    """Custom type snAgGblEnableWebMgmt based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_SnAgGblEnableWebMgmt_Type.__name__ = "Integer32"
_SnAgGblEnableWebMgmt_Object = MibScalar
snAgGblEnableWebMgmt = _SnAgGblEnableWebMgmt_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 2, 1, 38),
    _SnAgGblEnableWebMgmt_Type()
)
snAgGblEnableWebMgmt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snAgGblEnableWebMgmt.setStatus("mandatory")
_SnAgGblSecurityLevelBinding_Type = Integer32
_SnAgGblSecurityLevelBinding_Object = MibScalar
snAgGblSecurityLevelBinding = _SnAgGblSecurityLevelBinding_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 2, 1, 39),
    _SnAgGblSecurityLevelBinding_Type()
)
snAgGblSecurityLevelBinding.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snAgGblSecurityLevelBinding.setStatus("mandatory")


class _SnAgGblEnableSLB_Type(Integer32):
    """Custom type snAgGblEnableSLB based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_SnAgGblEnableSLB_Type.__name__ = "Integer32"
_SnAgGblEnableSLB_Object = MibScalar
snAgGblEnableSLB = _SnAgGblEnableSLB_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 2, 1, 40),
    _SnAgGblEnableSLB_Type()
)
snAgGblEnableSLB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snAgGblEnableSLB.setStatus("mandatory")
_SnAgSoftwareFeature_Type = OctetString
_SnAgSoftwareFeature_Object = MibScalar
snAgSoftwareFeature = _SnAgSoftwareFeature_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 2, 1, 41),
    _SnAgSoftwareFeature_Type()
)
snAgSoftwareFeature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snAgSoftwareFeature.setStatus("mandatory")


class _SnAgGblEnableModuleInsertedTrap_Type(Integer32):
    """Custom type snAgGblEnableModuleInsertedTrap based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_SnAgGblEnableModuleInsertedTrap_Type.__name__ = "Integer32"
_SnAgGblEnableModuleInsertedTrap_Object = MibScalar
snAgGblEnableModuleInsertedTrap = _SnAgGblEnableModuleInsertedTrap_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 2, 1, 42),
    _SnAgGblEnableModuleInsertedTrap_Type()
)
snAgGblEnableModuleInsertedTrap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snAgGblEnableModuleInsertedTrap.setStatus("mandatory")


class _SnAgGblEnableModuleRemovedTrap_Type(Integer32):
    """Custom type snAgGblEnableModuleRemovedTrap based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_SnAgGblEnableModuleRemovedTrap_Type.__name__ = "Integer32"
_SnAgGblEnableModuleRemovedTrap_Object = MibScalar
snAgGblEnableModuleRemovedTrap = _SnAgGblEnableModuleRemovedTrap_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 2, 1, 43),
    _SnAgGblEnableModuleRemovedTrap_Type()
)
snAgGblEnableModuleRemovedTrap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snAgGblEnableModuleRemovedTrap.setStatus("mandatory")
_SnAgGblTrapMessage_Type = DisplayString
_SnAgGblTrapMessage_Object = MibScalar
snAgGblTrapMessage = _SnAgGblTrapMessage_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 2, 1, 44),
    _SnAgGblTrapMessage_Type()
)
snAgGblTrapMessage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snAgGblTrapMessage.setStatus("mandatory")


class _SnAgGblEnableTelnetServer_Type(Integer32):
    """Custom type snAgGblEnableTelnetServer based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_SnAgGblEnableTelnetServer_Type.__name__ = "Integer32"
_SnAgGblEnableTelnetServer_Object = MibScalar
snAgGblEnableTelnetServer = _SnAgGblEnableTelnetServer_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 2, 1, 45),
    _SnAgGblEnableTelnetServer_Type()
)
snAgGblEnableTelnetServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snAgGblEnableTelnetServer.setStatus("mandatory")


class _SnAgGblTelnetPassword_Type(DisplayString):
    """Custom type snAgGblTelnetPassword based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 48),
    )


_SnAgGblTelnetPassword_Type.__name__ = "DisplayString"
_SnAgGblTelnetPassword_Object = MibScalar
snAgGblTelnetPassword = _SnAgGblTelnetPassword_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 2, 1, 46),
    _SnAgGblTelnetPassword_Type()
)
snAgGblTelnetPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snAgGblTelnetPassword.setStatus("mandatory")


class _SnAgBuildDate_Type(DisplayString):
    """Custom type snAgBuildDate based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_SnAgBuildDate_Type.__name__ = "DisplayString"
_SnAgBuildDate_Object = MibScalar
snAgBuildDate = _SnAgBuildDate_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 2, 1, 47),
    _SnAgBuildDate_Type()
)
snAgBuildDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snAgBuildDate.setStatus("mandatory")


class _SnAgBuildtime_Type(DisplayString):
    """Custom type snAgBuildtime based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_SnAgBuildtime_Type.__name__ = "DisplayString"
_SnAgBuildtime_Object = MibScalar
snAgBuildtime = _SnAgBuildtime_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 2, 1, 48),
    _SnAgBuildtime_Type()
)
snAgBuildtime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snAgBuildtime.setStatus("mandatory")


class _SnAgBuildVer_Type(DisplayString):
    """Custom type snAgBuildVer based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_SnAgBuildVer_Type.__name__ = "DisplayString"
_SnAgBuildVer_Object = MibScalar
snAgBuildVer = _SnAgBuildVer_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 2, 1, 49),
    _SnAgBuildVer_Type()
)
snAgBuildVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snAgBuildVer.setStatus("mandatory")
_SnAgentBrd_ObjectIdentity = ObjectIdentity
snAgentBrd = _SnAgentBrd_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 2, 2)
)
_SnAgentBrdTable_Object = MibTable
snAgentBrdTable = _SnAgentBrdTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 2, 2, 1)
)
if mibBuilder.loadTexts:
    snAgentBrdTable.setStatus("mandatory")
_SnAgentBrdEntry_Object = MibTableRow
snAgentBrdEntry = _SnAgentBrdEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 2, 2, 1, 1)
)
snAgentBrdEntry.setIndexNames(
    (0, "HP-SN-AGENT-MIB", "snAgentBrdIndex"),
)
if mibBuilder.loadTexts:
    snAgentBrdEntry.setStatus("mandatory")


class _SnAgentBrdIndex_Type(Integer32):
    """Custom type snAgentBrdIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_SnAgentBrdIndex_Type.__name__ = "Integer32"
_SnAgentBrdIndex_Object = MibTableColumn
snAgentBrdIndex = _SnAgentBrdIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 2, 2, 1, 1, 1),
    _SnAgentBrdIndex_Type()
)
snAgentBrdIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snAgentBrdIndex.setStatus("mandatory")


class _SnAgentBrdMainBrdDescription_Type(DisplayString):
    """Custom type snAgentBrdMainBrdDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_SnAgentBrdMainBrdDescription_Type.__name__ = "DisplayString"
_SnAgentBrdMainBrdDescription_Object = MibTableColumn
snAgentBrdMainBrdDescription = _SnAgentBrdMainBrdDescription_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 2, 2, 1, 1, 2),
    _SnAgentBrdMainBrdDescription_Type()
)
snAgentBrdMainBrdDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snAgentBrdMainBrdDescription.setStatus("mandatory")
_SnAgentBrdMainBrdId_Type = OctetString
_SnAgentBrdMainBrdId_Object = MibTableColumn
snAgentBrdMainBrdId = _SnAgentBrdMainBrdId_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 2, 2, 1, 1, 3),
    _SnAgentBrdMainBrdId_Type()
)
snAgentBrdMainBrdId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snAgentBrdMainBrdId.setStatus("mandatory")


class _SnAgentBrdMainPortTotal_Type(Integer32):
    """Custom type snAgentBrdMainPortTotal based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_SnAgentBrdMainPortTotal_Type.__name__ = "Integer32"
_SnAgentBrdMainPortTotal_Object = MibTableColumn
snAgentBrdMainPortTotal = _SnAgentBrdMainPortTotal_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 2, 2, 1, 1, 4),
    _SnAgentBrdMainPortTotal_Type()
)
snAgentBrdMainPortTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snAgentBrdMainPortTotal.setStatus("mandatory")


class _SnAgentBrdExpBrdDescription_Type(DisplayString):
    """Custom type snAgentBrdExpBrdDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_SnAgentBrdExpBrdDescription_Type.__name__ = "DisplayString"
_SnAgentBrdExpBrdDescription_Object = MibTableColumn
snAgentBrdExpBrdDescription = _SnAgentBrdExpBrdDescription_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 2, 2, 1, 1, 5),
    _SnAgentBrdExpBrdDescription_Type()
)
snAgentBrdExpBrdDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snAgentBrdExpBrdDescription.setStatus("mandatory")
_SnAgentBrdExpBrdId_Type = OctetString
_SnAgentBrdExpBrdId_Object = MibTableColumn
snAgentBrdExpBrdId = _SnAgentBrdExpBrdId_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 2, 2, 1, 1, 6),
    _SnAgentBrdExpBrdId_Type()
)
snAgentBrdExpBrdId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snAgentBrdExpBrdId.setStatus("mandatory")


class _SnAgentBrdExpPortTotal_Type(Integer32):
    """Custom type snAgentBrdExpPortTotal based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 24),
    )


_SnAgentBrdExpPortTotal_Type.__name__ = "Integer32"
_SnAgentBrdExpPortTotal_Object = MibTableColumn
snAgentBrdExpPortTotal = _SnAgentBrdExpPortTotal_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 2, 2, 1, 1, 7),
    _SnAgentBrdExpPortTotal_Type()
)
snAgentBrdExpPortTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snAgentBrdExpPortTotal.setStatus("mandatory")
_SnAgentBrdStatusLeds_Type = Integer32
_SnAgentBrdStatusLeds_Object = MibTableColumn
snAgentBrdStatusLeds = _SnAgentBrdStatusLeds_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 2, 2, 1, 1, 8),
    _SnAgentBrdStatusLeds_Type()
)
snAgentBrdStatusLeds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snAgentBrdStatusLeds.setStatus("mandatory")
_SnAgentBrdTrafficLeds_Type = Integer32
_SnAgentBrdTrafficLeds_Object = MibTableColumn
snAgentBrdTrafficLeds = _SnAgentBrdTrafficLeds_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 2, 2, 1, 1, 9),
    _SnAgentBrdTrafficLeds_Type()
)
snAgentBrdTrafficLeds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snAgentBrdTrafficLeds.setStatus("mandatory")
_SnAgentBrdMediaLeds_Type = Integer32
_SnAgentBrdMediaLeds_Object = MibTableColumn
snAgentBrdMediaLeds = _SnAgentBrdMediaLeds_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 2, 2, 1, 1, 10),
    _SnAgentBrdMediaLeds_Type()
)
snAgentBrdMediaLeds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snAgentBrdMediaLeds.setStatus("mandatory")
_SnAgentBrdSpeedLeds_Type = Integer32
_SnAgentBrdSpeedLeds_Object = MibTableColumn
snAgentBrdSpeedLeds = _SnAgentBrdSpeedLeds_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 2, 2, 1, 1, 11),
    _SnAgentBrdSpeedLeds_Type()
)
snAgentBrdSpeedLeds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snAgentBrdSpeedLeds.setStatus("mandatory")


class _SnAgentBrdModuleStatus_Type(Integer32):
    """Custom type snAgentBrdModuleStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              2,
              3,
              4,
              9,
              10)
        )
    )
    namedValues = NamedValues(
        *(("moduleBad", 4),
          ("moduleComingUp", 9),
          ("moduleEmpty", 0),
          ("moduleGoingDown", 2),
          ("moduleRejected", 3),
          ("moduleRunning", 10))
    )


_SnAgentBrdModuleStatus_Type.__name__ = "Integer32"
_SnAgentBrdModuleStatus_Object = MibTableColumn
snAgentBrdModuleStatus = _SnAgentBrdModuleStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 2, 2, 1, 1, 12),
    _SnAgentBrdModuleStatus_Type()
)
snAgentBrdModuleStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snAgentBrdModuleStatus.setStatus("mandatory")


class _SnAgentBrdRedundantStatus_Type(Integer32):
    """Custom type snAgentBrdRedundantStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("active", 2),
          ("comingUp", 5),
          ("crashed", 4),
          ("other", 1),
          ("standby", 3))
    )


_SnAgentBrdRedundantStatus_Type.__name__ = "Integer32"
_SnAgentBrdRedundantStatus_Object = MibTableColumn
snAgentBrdRedundantStatus = _SnAgentBrdRedundantStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 2, 2, 1, 1, 13),
    _SnAgentBrdRedundantStatus_Type()
)
snAgentBrdRedundantStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snAgentBrdRedundantStatus.setStatus("mandatory")
_SnAgentBrdAlarmLeds_Type = Integer32
_SnAgentBrdAlarmLeds_Object = MibTableColumn
snAgentBrdAlarmLeds = _SnAgentBrdAlarmLeds_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 2, 2, 1, 1, 14),
    _SnAgentBrdAlarmLeds_Type()
)
snAgentBrdAlarmLeds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snAgentBrdAlarmLeds.setStatus("mandatory")
_SnAgentBrdTxTrafficLeds_Type = Integer32
_SnAgentBrdTxTrafficLeds_Object = MibTableColumn
snAgentBrdTxTrafficLeds = _SnAgentBrdTxTrafficLeds_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 2, 2, 1, 1, 15),
    _SnAgentBrdTxTrafficLeds_Type()
)
snAgentBrdTxTrafficLeds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snAgentBrdTxTrafficLeds.setStatus("mandatory")
_SnAgentBrdRxTrafficLeds_Type = Integer32
_SnAgentBrdRxTrafficLeds_Object = MibTableColumn
snAgentBrdRxTrafficLeds = _SnAgentBrdRxTrafficLeds_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 2, 2, 1, 1, 16),
    _SnAgentBrdRxTrafficLeds_Type()
)
snAgentBrdRxTrafficLeds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snAgentBrdRxTrafficLeds.setStatus("mandatory")
_SnAgentTrp_ObjectIdentity = ObjectIdentity
snAgentTrp = _SnAgentTrp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 2, 3)
)
_SnAgTrpRcvrTable_Object = MibTable
snAgTrpRcvrTable = _SnAgTrpRcvrTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 2, 3, 1)
)
if mibBuilder.loadTexts:
    snAgTrpRcvrTable.setStatus("mandatory")
_SnAgTrpRcvrEntry_Object = MibTableRow
snAgTrpRcvrEntry = _SnAgTrpRcvrEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 2, 3, 1, 1)
)
snAgTrpRcvrEntry.setIndexNames(
    (0, "HP-SN-AGENT-MIB", "snAgTrpRcvrIndex"),
)
if mibBuilder.loadTexts:
    snAgTrpRcvrEntry.setStatus("mandatory")


class _SnAgTrpRcvrIndex_Type(Integer32):
    """Custom type snAgTrpRcvrIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_SnAgTrpRcvrIndex_Type.__name__ = "Integer32"
_SnAgTrpRcvrIndex_Object = MibTableColumn
snAgTrpRcvrIndex = _SnAgTrpRcvrIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 2, 3, 1, 1, 1),
    _SnAgTrpRcvrIndex_Type()
)
snAgTrpRcvrIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snAgTrpRcvrIndex.setStatus("mandatory")
_SnAgTrpRcvrIpAddr_Type = IpAddress
_SnAgTrpRcvrIpAddr_Object = MibTableColumn
snAgTrpRcvrIpAddr = _SnAgTrpRcvrIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 2, 3, 1, 1, 2),
    _SnAgTrpRcvrIpAddr_Type()
)
snAgTrpRcvrIpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snAgTrpRcvrIpAddr.setStatus("mandatory")


class _SnAgTrpRcvrComm_Type(OctetString):
    """Custom type snAgTrpRcvrComm based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_SnAgTrpRcvrComm_Type.__name__ = "OctetString"
_SnAgTrpRcvrComm_Object = MibTableColumn
snAgTrpRcvrComm = _SnAgTrpRcvrComm_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 2, 3, 1, 1, 3),
    _SnAgTrpRcvrComm_Type()
)
snAgTrpRcvrComm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snAgTrpRcvrComm.setStatus("mandatory")


class _SnAgTrpRcvrStatus_Type(Integer32):
    """Custom type snAgTrpRcvrStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("create", 4),
          ("delete", 3),
          ("ignore", 5),
          ("other", 1),
          ("valid", 2))
    )


_SnAgTrpRcvrStatus_Type.__name__ = "Integer32"
_SnAgTrpRcvrStatus_Object = MibTableColumn
snAgTrpRcvrStatus = _SnAgTrpRcvrStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 2, 3, 1, 1, 4),
    _SnAgTrpRcvrStatus_Type()
)
snAgTrpRcvrStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snAgTrpRcvrStatus.setStatus("mandatory")
_SnAgentBoot_ObjectIdentity = ObjectIdentity
snAgentBoot = _SnAgentBoot_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 2, 4)
)
_SnAgBootSeqTable_Object = MibTable
snAgBootSeqTable = _SnAgBootSeqTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 2, 4, 1)
)
if mibBuilder.loadTexts:
    snAgBootSeqTable.setStatus("mandatory")
_SnAgBootSeqEntry_Object = MibTableRow
snAgBootSeqEntry = _SnAgBootSeqEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 2, 4, 1, 1)
)
snAgBootSeqEntry.setIndexNames(
    (0, "HP-SN-AGENT-MIB", "snAgBootSeqIndex"),
)
if mibBuilder.loadTexts:
    snAgBootSeqEntry.setStatus("mandatory")


class _SnAgBootSeqIndex_Type(Integer32):
    """Custom type snAgBootSeqIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_SnAgBootSeqIndex_Type.__name__ = "Integer32"
_SnAgBootSeqIndex_Object = MibTableColumn
snAgBootSeqIndex = _SnAgBootSeqIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 2, 4, 1, 1, 1),
    _SnAgBootSeqIndex_Type()
)
snAgBootSeqIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snAgBootSeqIndex.setStatus("mandatory")


class _SnAgBootSeqInstruction_Type(Integer32):
    """Custom type snAgBootSeqInstruction based on Integer32"""
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
        *(("fromBootpServer", 4),
          ("fromPrimaryFlash", 1),
          ("fromSecondaryFlash", 2),
          ("fromTftpServer", 3))
    )


_SnAgBootSeqInstruction_Type.__name__ = "Integer32"
_SnAgBootSeqInstruction_Object = MibTableColumn
snAgBootSeqInstruction = _SnAgBootSeqInstruction_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 2, 4, 1, 1, 2),
    _SnAgBootSeqInstruction_Type()
)
snAgBootSeqInstruction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snAgBootSeqInstruction.setStatus("mandatory")
_SnAgBootSeqIpAddr_Type = IpAddress
_SnAgBootSeqIpAddr_Object = MibTableColumn
snAgBootSeqIpAddr = _SnAgBootSeqIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 2, 4, 1, 1, 3),
    _SnAgBootSeqIpAddr_Type()
)
snAgBootSeqIpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snAgBootSeqIpAddr.setStatus("mandatory")


class _SnAgBootSeqFilename_Type(DisplayString):
    """Custom type snAgBootSeqFilename based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_SnAgBootSeqFilename_Type.__name__ = "DisplayString"
_SnAgBootSeqFilename_Object = MibTableColumn
snAgBootSeqFilename = _SnAgBootSeqFilename_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 2, 4, 1, 1, 4),
    _SnAgBootSeqFilename_Type()
)
snAgBootSeqFilename.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snAgBootSeqFilename.setStatus("mandatory")


class _SnAgBootSeqRowStatus_Type(Integer32):
    """Custom type snAgBootSeqRowStatus based on Integer32"""
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
        *(("create", 4),
          ("delete", 3),
          ("other", 1),
          ("valid", 2))
    )


_SnAgBootSeqRowStatus_Type.__name__ = "Integer32"
_SnAgBootSeqRowStatus_Object = MibTableColumn
snAgBootSeqRowStatus = _SnAgBootSeqRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 2, 4, 1, 1, 5),
    _SnAgBootSeqRowStatus_Type()
)
snAgBootSeqRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snAgBootSeqRowStatus.setStatus("mandatory")
_SnAgCfgEos_ObjectIdentity = ObjectIdentity
snAgCfgEos = _SnAgCfgEos_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 2, 5)
)
_SnAgCfgEosTable_Object = MibTable
snAgCfgEosTable = _SnAgCfgEosTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 2, 5, 1)
)
if mibBuilder.loadTexts:
    snAgCfgEosTable.setStatus("mandatory")
_SnAgCfgEosEntry_Object = MibTableRow
snAgCfgEosEntry = _SnAgCfgEosEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 2, 5, 1, 1)
)
snAgCfgEosEntry.setIndexNames(
    (0, "HP-SN-AGENT-MIB", "snAgCfgEosIndex"),
)
if mibBuilder.loadTexts:
    snAgCfgEosEntry.setStatus("mandatory")
_SnAgCfgEosIndex_Type = Integer32
_SnAgCfgEosIndex_Object = MibTableColumn
snAgCfgEosIndex = _SnAgCfgEosIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 2, 5, 1, 1, 1),
    _SnAgCfgEosIndex_Type()
)
snAgCfgEosIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snAgCfgEosIndex.setStatus("mandatory")


class _SnAgCfgEosPacket_Type(OctetString):
    """Custom type snAgCfgEosPacket based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 1000),
    )


_SnAgCfgEosPacket_Type.__name__ = "OctetString"
_SnAgCfgEosPacket_Object = MibTableColumn
snAgCfgEosPacket = _SnAgCfgEosPacket_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 2, 5, 1, 1, 2),
    _SnAgCfgEosPacket_Type()
)
snAgCfgEosPacket.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snAgCfgEosPacket.setStatus("mandatory")
_SnAgCfgEosChkSum_Type = Integer32
_SnAgCfgEosChkSum_Object = MibTableColumn
snAgCfgEosChkSum = _SnAgCfgEosChkSum_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 2, 5, 1, 1, 3),
    _SnAgCfgEosChkSum_Type()
)
snAgCfgEosChkSum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snAgCfgEosChkSum.setStatus("mandatory")
_SnAgentLog_ObjectIdentity = ObjectIdentity
snAgentLog = _SnAgentLog_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 2, 6)
)
_SnAgSysLogGbl_ObjectIdentity = ObjectIdentity
snAgSysLogGbl = _SnAgSysLogGbl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 2, 6, 1)
)


class _SnAgSysLogGblEnable_Type(Integer32):
    """Custom type snAgSysLogGblEnable based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_SnAgSysLogGblEnable_Type.__name__ = "Integer32"
_SnAgSysLogGblEnable_Object = MibScalar
snAgSysLogGblEnable = _SnAgSysLogGblEnable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 2, 6, 1, 1),
    _SnAgSysLogGblEnable_Type()
)
snAgSysLogGblEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snAgSysLogGblEnable.setStatus("mandatory")


class _SnAgSysLogGblBufferSize_Type(Integer32):
    """Custom type snAgSysLogGblBufferSize based on Integer32"""
    defaultValue = 50

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_SnAgSysLogGblBufferSize_Type.__name__ = "Integer32"
_SnAgSysLogGblBufferSize_Object = MibScalar
snAgSysLogGblBufferSize = _SnAgSysLogGblBufferSize_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 2, 6, 1, 2),
    _SnAgSysLogGblBufferSize_Type()
)
snAgSysLogGblBufferSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snAgSysLogGblBufferSize.setStatus("mandatory")


class _SnAgSysLogGblClear_Type(Integer32):
    """Custom type snAgSysLogGblClear based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("clearAll", 1),
          ("clearDynamic", 2),
          ("clearStatic", 3),
          ("normal", 0))
    )


_SnAgSysLogGblClear_Type.__name__ = "Integer32"
_SnAgSysLogGblClear_Object = MibScalar
snAgSysLogGblClear = _SnAgSysLogGblClear_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 2, 6, 1, 3),
    _SnAgSysLogGblClear_Type()
)
snAgSysLogGblClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snAgSysLogGblClear.setStatus("mandatory")


class _SnAgSysLogGblCriticalLevel_Type(Integer32):
    """Custom type snAgSysLogGblCriticalLevel based on Integer32"""
    defaultValue = 255


_SnAgSysLogGblCriticalLevel_Object = MibScalar
snAgSysLogGblCriticalLevel = _SnAgSysLogGblCriticalLevel_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 2, 6, 1, 4),
    _SnAgSysLogGblCriticalLevel_Type()
)
snAgSysLogGblCriticalLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snAgSysLogGblCriticalLevel.setStatus("mandatory")
_SnAgSysLogGblLoggedCount_Type = Counter32
_SnAgSysLogGblLoggedCount_Object = MibScalar
snAgSysLogGblLoggedCount = _SnAgSysLogGblLoggedCount_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 2, 6, 1, 5),
    _SnAgSysLogGblLoggedCount_Type()
)
snAgSysLogGblLoggedCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snAgSysLogGblLoggedCount.setStatus("mandatory")
_SnAgSysLogGblDroppedCount_Type = Counter32
_SnAgSysLogGblDroppedCount_Object = MibScalar
snAgSysLogGblDroppedCount = _SnAgSysLogGblDroppedCount_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 2, 6, 1, 6),
    _SnAgSysLogGblDroppedCount_Type()
)
snAgSysLogGblDroppedCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snAgSysLogGblDroppedCount.setStatus("mandatory")
_SnAgSysLogGblFlushedCount_Type = Counter32
_SnAgSysLogGblFlushedCount_Object = MibScalar
snAgSysLogGblFlushedCount = _SnAgSysLogGblFlushedCount_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 2, 6, 1, 7),
    _SnAgSysLogGblFlushedCount_Type()
)
snAgSysLogGblFlushedCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snAgSysLogGblFlushedCount.setStatus("mandatory")
_SnAgSysLogGblOverrunCount_Type = Counter32
_SnAgSysLogGblOverrunCount_Object = MibScalar
snAgSysLogGblOverrunCount = _SnAgSysLogGblOverrunCount_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 2, 6, 1, 8),
    _SnAgSysLogGblOverrunCount_Type()
)
snAgSysLogGblOverrunCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snAgSysLogGblOverrunCount.setStatus("mandatory")
_SnAgSysLogGblServer_Type = IpAddress
_SnAgSysLogGblServer_Object = MibScalar
snAgSysLogGblServer = _SnAgSysLogGblServer_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 2, 6, 1, 9),
    _SnAgSysLogGblServer_Type()
)
snAgSysLogGblServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snAgSysLogGblServer.setStatus("mandatory")


class _SnAgSysLogGblFacility_Type(Integer32):
    """Custom type snAgSysLogGblFacility based on Integer32"""
    defaultValue = 2

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
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              17,
              18,
              19,
              20,
              21,
              22,
              23,
              24)
        )
    )
    namedValues = NamedValues(
        *(("auth", 5),
          ("cron", 16),
          ("daemon", 4),
          ("kern", 1),
          ("local0", 17),
          ("local1", 18),
          ("local2", 19),
          ("local3", 20),
          ("local4", 21),
          ("local5", 22),
          ("local6", 23),
          ("local7", 24),
          ("lpr", 7),
          ("mail", 3),
          ("news", 8),
          ("sys10", 11),
          ("sys11", 12),
          ("sys12", 13),
          ("sys13", 14),
          ("sys14", 15),
          ("sys9", 10),
          ("syslog", 6),
          ("user", 2),
          ("uucp", 9))
    )


_SnAgSysLogGblFacility_Type.__name__ = "Integer32"
_SnAgSysLogGblFacility_Object = MibScalar
snAgSysLogGblFacility = _SnAgSysLogGblFacility_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 2, 6, 1, 10),
    _SnAgSysLogGblFacility_Type()
)
snAgSysLogGblFacility.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snAgSysLogGblFacility.setStatus("mandatory")
_SnAgSysLogBufferTable_Object = MibTable
snAgSysLogBufferTable = _SnAgSysLogBufferTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 2, 6, 2)
)
if mibBuilder.loadTexts:
    snAgSysLogBufferTable.setStatus("mandatory")
_SnAgSysLogBufferEntry_Object = MibTableRow
snAgSysLogBufferEntry = _SnAgSysLogBufferEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 2, 6, 2, 1)
)
snAgSysLogBufferEntry.setIndexNames(
    (0, "HP-SN-AGENT-MIB", "snAgSysLogBufferIndex"),
)
if mibBuilder.loadTexts:
    snAgSysLogBufferEntry.setStatus("mandatory")


class _SnAgSysLogBufferIndex_Type(Integer32):
    """Custom type snAgSysLogBufferIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_SnAgSysLogBufferIndex_Type.__name__ = "Integer32"
_SnAgSysLogBufferIndex_Object = MibTableColumn
snAgSysLogBufferIndex = _SnAgSysLogBufferIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 2, 6, 2, 1, 1),
    _SnAgSysLogBufferIndex_Type()
)
snAgSysLogBufferIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snAgSysLogBufferIndex.setStatus("mandatory")
_SnAgSysLogBufferTimeStamp_Type = TimeTicks
_SnAgSysLogBufferTimeStamp_Object = MibTableColumn
snAgSysLogBufferTimeStamp = _SnAgSysLogBufferTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 2, 6, 2, 1, 2),
    _SnAgSysLogBufferTimeStamp_Type()
)
snAgSysLogBufferTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snAgSysLogBufferTimeStamp.setStatus("mandatory")


class _SnAgSysLogBufferCriticalLevel_Type(Integer32):
    """Custom type snAgSysLogBufferCriticalLevel based on Integer32"""
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
        *(("alert", 2),
          ("critical", 3),
          ("debugging", 4),
          ("emergency", 5),
          ("error", 6),
          ("informational", 7),
          ("notification", 8),
          ("other", 1),
          ("warning", 9))
    )


_SnAgSysLogBufferCriticalLevel_Type.__name__ = "Integer32"
_SnAgSysLogBufferCriticalLevel_Object = MibTableColumn
snAgSysLogBufferCriticalLevel = _SnAgSysLogBufferCriticalLevel_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 2, 6, 2, 1, 3),
    _SnAgSysLogBufferCriticalLevel_Type()
)
snAgSysLogBufferCriticalLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snAgSysLogBufferCriticalLevel.setStatus("mandatory")
_SnAgSysLogBufferMessage_Type = DisplayString
_SnAgSysLogBufferMessage_Object = MibTableColumn
snAgSysLogBufferMessage = _SnAgSysLogBufferMessage_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 2, 6, 2, 1, 4),
    _SnAgSysLogBufferMessage_Type()
)
snAgSysLogBufferMessage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snAgSysLogBufferMessage.setStatus("mandatory")
_SnAgSysLogBufferCalTimeStamp_Type = DisplayString
_SnAgSysLogBufferCalTimeStamp_Object = MibTableColumn
snAgSysLogBufferCalTimeStamp = _SnAgSysLogBufferCalTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 2, 6, 2, 1, 5),
    _SnAgSysLogBufferCalTimeStamp_Type()
)
snAgSysLogBufferCalTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snAgSysLogBufferCalTimeStamp.setStatus("mandatory")
_SnAgStaticSysLogBufferTable_Object = MibTable
snAgStaticSysLogBufferTable = _SnAgStaticSysLogBufferTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 2, 6, 3)
)
if mibBuilder.loadTexts:
    snAgStaticSysLogBufferTable.setStatus("mandatory")
_SnAgStaticSysLogBufferEntry_Object = MibTableRow
snAgStaticSysLogBufferEntry = _SnAgStaticSysLogBufferEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 2, 6, 3, 1)
)
snAgStaticSysLogBufferEntry.setIndexNames(
    (0, "HP-SN-AGENT-MIB", "snAgStaticSysLogBufferIndex"),
)
if mibBuilder.loadTexts:
    snAgStaticSysLogBufferEntry.setStatus("mandatory")


class _SnAgStaticSysLogBufferIndex_Type(Integer32):
    """Custom type snAgStaticSysLogBufferIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_SnAgStaticSysLogBufferIndex_Type.__name__ = "Integer32"
_SnAgStaticSysLogBufferIndex_Object = MibTableColumn
snAgStaticSysLogBufferIndex = _SnAgStaticSysLogBufferIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 2, 6, 3, 1, 1),
    _SnAgStaticSysLogBufferIndex_Type()
)
snAgStaticSysLogBufferIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snAgStaticSysLogBufferIndex.setStatus("mandatory")
_SnAgStaticSysLogBufferTimeStamp_Type = TimeTicks
_SnAgStaticSysLogBufferTimeStamp_Object = MibTableColumn
snAgStaticSysLogBufferTimeStamp = _SnAgStaticSysLogBufferTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 2, 6, 3, 1, 2),
    _SnAgStaticSysLogBufferTimeStamp_Type()
)
snAgStaticSysLogBufferTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snAgStaticSysLogBufferTimeStamp.setStatus("mandatory")


class _SnAgStaticSysLogBufferCriticalLevel_Type(Integer32):
    """Custom type snAgStaticSysLogBufferCriticalLevel based on Integer32"""
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
        *(("alert", 2),
          ("critical", 3),
          ("debugging", 4),
          ("emergency", 5),
          ("error", 6),
          ("informational", 7),
          ("notification", 8),
          ("other", 1),
          ("warning", 9))
    )


_SnAgStaticSysLogBufferCriticalLevel_Type.__name__ = "Integer32"
_SnAgStaticSysLogBufferCriticalLevel_Object = MibTableColumn
snAgStaticSysLogBufferCriticalLevel = _SnAgStaticSysLogBufferCriticalLevel_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 2, 6, 3, 1, 3),
    _SnAgStaticSysLogBufferCriticalLevel_Type()
)
snAgStaticSysLogBufferCriticalLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snAgStaticSysLogBufferCriticalLevel.setStatus("mandatory")
_SnAgStaticSysLogBufferMessage_Type = DisplayString
_SnAgStaticSysLogBufferMessage_Object = MibTableColumn
snAgStaticSysLogBufferMessage = _SnAgStaticSysLogBufferMessage_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 2, 6, 3, 1, 4),
    _SnAgStaticSysLogBufferMessage_Type()
)
snAgStaticSysLogBufferMessage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snAgStaticSysLogBufferMessage.setStatus("mandatory")
_SnAgStaticSysLogBufferCalTimeStamp_Type = DisplayString
_SnAgStaticSysLogBufferCalTimeStamp_Object = MibTableColumn
snAgStaticSysLogBufferCalTimeStamp = _SnAgStaticSysLogBufferCalTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 2, 6, 3, 1, 5),
    _SnAgStaticSysLogBufferCalTimeStamp_Type()
)
snAgStaticSysLogBufferCalTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snAgStaticSysLogBufferCalTimeStamp.setStatus("mandatory")
_SnAgentSysParaConfig_ObjectIdentity = ObjectIdentity
snAgentSysParaConfig = _SnAgentSysParaConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 2, 7)
)
_SnAgentSysParaConfigTable_Object = MibTable
snAgentSysParaConfigTable = _SnAgentSysParaConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 2, 7, 1)
)
if mibBuilder.loadTexts:
    snAgentSysParaConfigTable.setStatus("mandatory")
_SnAgentSysParaConfigEntry_Object = MibTableRow
snAgentSysParaConfigEntry = _SnAgentSysParaConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 2, 7, 1, 1)
)
snAgentSysParaConfigEntry.setIndexNames(
    (0, "HP-SN-AGENT-MIB", "snAgentSysParaConfigIndex"),
)
if mibBuilder.loadTexts:
    snAgentSysParaConfigEntry.setStatus("mandatory")
_SnAgentSysParaConfigIndex_Type = Integer32
_SnAgentSysParaConfigIndex_Object = MibTableColumn
snAgentSysParaConfigIndex = _SnAgentSysParaConfigIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 2, 7, 1, 1, 1),
    _SnAgentSysParaConfigIndex_Type()
)
snAgentSysParaConfigIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snAgentSysParaConfigIndex.setStatus("mandatory")


class _SnAgentSysParaConfigDescription_Type(DisplayString):
    """Custom type snAgentSysParaConfigDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_SnAgentSysParaConfigDescription_Type.__name__ = "DisplayString"
_SnAgentSysParaConfigDescription_Object = MibTableColumn
snAgentSysParaConfigDescription = _SnAgentSysParaConfigDescription_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 2, 7, 1, 1, 2),
    _SnAgentSysParaConfigDescription_Type()
)
snAgentSysParaConfigDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snAgentSysParaConfigDescription.setStatus("mandatory")
_SnAgentSysParaConfigMin_Type = Integer32
_SnAgentSysParaConfigMin_Object = MibTableColumn
snAgentSysParaConfigMin = _SnAgentSysParaConfigMin_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 2, 7, 1, 1, 3),
    _SnAgentSysParaConfigMin_Type()
)
snAgentSysParaConfigMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snAgentSysParaConfigMin.setStatus("mandatory")
_SnAgentSysParaConfigMax_Type = Integer32
_SnAgentSysParaConfigMax_Object = MibTableColumn
snAgentSysParaConfigMax = _SnAgentSysParaConfigMax_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 2, 7, 1, 1, 4),
    _SnAgentSysParaConfigMax_Type()
)
snAgentSysParaConfigMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snAgentSysParaConfigMax.setStatus("mandatory")
_SnAgentSysParaConfigDefault_Type = Integer32
_SnAgentSysParaConfigDefault_Object = MibTableColumn
snAgentSysParaConfigDefault = _SnAgentSysParaConfigDefault_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 2, 7, 1, 1, 5),
    _SnAgentSysParaConfigDefault_Type()
)
snAgentSysParaConfigDefault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snAgentSysParaConfigDefault.setStatus("mandatory")
_SnAgentSysParaConfigCurrent_Type = Integer32
_SnAgentSysParaConfigCurrent_Object = MibTableColumn
snAgentSysParaConfigCurrent = _SnAgentSysParaConfigCurrent_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 2, 7, 1, 1, 6),
    _SnAgentSysParaConfigCurrent_Type()
)
snAgentSysParaConfigCurrent.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snAgentSysParaConfigCurrent.setStatus("mandatory")
_SnAgentConfigModule_ObjectIdentity = ObjectIdentity
snAgentConfigModule = _SnAgentConfigModule_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 2, 8)
)
_SnAgentConfigModuleTable_Object = MibTable
snAgentConfigModuleTable = _SnAgentConfigModuleTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 2, 8, 1)
)
if mibBuilder.loadTexts:
    snAgentConfigModuleTable.setStatus("mandatory")
_SnAgentConfigModuleEntry_Object = MibTableRow
snAgentConfigModuleEntry = _SnAgentConfigModuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 2, 8, 1, 1)
)
snAgentConfigModuleEntry.setIndexNames(
    (0, "HP-SN-AGENT-MIB", "snAgentConfigModuleIndex"),
)
if mibBuilder.loadTexts:
    snAgentConfigModuleEntry.setStatus("mandatory")


class _SnAgentConfigModuleIndex_Type(Integer32):
    """Custom type snAgentConfigModuleIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_SnAgentConfigModuleIndex_Type.__name__ = "Integer32"
_SnAgentConfigModuleIndex_Object = MibTableColumn
snAgentConfigModuleIndex = _SnAgentConfigModuleIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 2, 8, 1, 1, 1),
    _SnAgentConfigModuleIndex_Type()
)
snAgentConfigModuleIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snAgentConfigModuleIndex.setStatus("mandatory")


class _SnAgentConfigModuleType_Type(Integer32):
    """Custom type snAgentConfigModuleType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              10,
              11,
              12,
              13,
              14,
              18,
              19,
              20,
              21,
              22,
              23,
              24,
              25,
              26,
              27,
              28,
              29,
              30,
              31,
              32,
              33,
              34)
        )
    )
    namedValues = NamedValues(
        *(("bi0PortManagementModule", 20),
          ("bi16Port100FXModule", 12),
          ("bi16PortCopperManagementModule", 2),
          ("bi24Port100FXModule", 19),
          ("bi24PortCopperModule", 10),
          ("bi2PortGigCopperManagementModule", 34),
          ("bi2PortGigCopperModule", 24),
          ("bi2PortGigManagementModule", 18),
          ("bi2PortGigModule", 23),
          ("bi4PortGigCopperManagementModule", 33),
          ("bi4PortGigManagementModule", 1),
          ("bi4PortGigModule", 3),
          ("bi8Port100FXModule", 13),
          ("bi8PortGigCopperManagementModule", 6),
          ("bi8PortGigCopperModule", 14),
          ("bi8PortGigManagementModule", 0),
          ("bi8PortGigModule", 8),
          ("fi24PortCopperModule", 11),
          ("fi2PortGigCopperManagementModule", 31),
          ("fi2PortGigManagementModule", 4),
          ("fi2PortGigModule", 25),
          ("fi4PortGigCopperManagementModule", 32),
          ("fi4PortGigManagementModule", 5),
          ("fi4PortGigModule", 26),
          ("fi8PortGigCopperManagementModule", 29),
          ("fi8PortGigCopperModule", 28),
          ("fi8PortGigManagementModule", 7),
          ("fi8PortGigModule", 27),
          ("pos155Mbs2PModule", 30),
          ("pos155MbsModule", 22),
          ("pos622MbsModule", 21))
    )


_SnAgentConfigModuleType_Type.__name__ = "Integer32"
_SnAgentConfigModuleType_Object = MibTableColumn
snAgentConfigModuleType = _SnAgentConfigModuleType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 2, 8, 1, 1, 2),
    _SnAgentConfigModuleType_Type()
)
snAgentConfigModuleType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snAgentConfigModuleType.setStatus("mandatory")


class _SnAgentConfigModuleRowStatus_Type(Integer32):
    """Custom type snAgentConfigModuleRowStatus based on Integer32"""
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
        *(("create", 4),
          ("delete", 3),
          ("other", 1),
          ("valid", 2))
    )


_SnAgentConfigModuleRowStatus_Type.__name__ = "Integer32"
_SnAgentConfigModuleRowStatus_Object = MibTableColumn
snAgentConfigModuleRowStatus = _SnAgentConfigModuleRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 2, 8, 1, 1, 3),
    _SnAgentConfigModuleRowStatus_Type()
)
snAgentConfigModuleRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snAgentConfigModuleRowStatus.setStatus("mandatory")
_SnAgentUser_ObjectIdentity = ObjectIdentity
snAgentUser = _SnAgentUser_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 2, 9)
)
_SnAgentUserGbl_ObjectIdentity = ObjectIdentity
snAgentUserGbl = _SnAgentUserGbl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 2, 9, 1)
)
_SnAgentUserMaxAccnt_Type = Integer32
_SnAgentUserMaxAccnt_Object = MibScalar
snAgentUserMaxAccnt = _SnAgentUserMaxAccnt_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 2, 9, 1, 1),
    _SnAgentUserMaxAccnt_Type()
)
snAgentUserMaxAccnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snAgentUserMaxAccnt.setStatus("mandatory")
_SnAgentUserAccntTable_Object = MibTable
snAgentUserAccntTable = _SnAgentUserAccntTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 2, 9, 2)
)
if mibBuilder.loadTexts:
    snAgentUserAccntTable.setStatus("mandatory")
_SnAgentUserAccntEntry_Object = MibTableRow
snAgentUserAccntEntry = _SnAgentUserAccntEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 2, 9, 2, 1)
)
snAgentUserAccntEntry.setIndexNames(
    (0, "HP-SN-AGENT-MIB", "snAgentUserAccntName"),
)
if mibBuilder.loadTexts:
    snAgentUserAccntEntry.setStatus("mandatory")


class _SnAgentUserAccntName_Type(DisplayString):
    """Custom type snAgentUserAccntName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 48),
    )


_SnAgentUserAccntName_Type.__name__ = "DisplayString"
_SnAgentUserAccntName_Object = MibTableColumn
snAgentUserAccntName = _SnAgentUserAccntName_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 2, 9, 2, 1, 1),
    _SnAgentUserAccntName_Type()
)
snAgentUserAccntName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snAgentUserAccntName.setStatus("mandatory")


class _SnAgentUserAccntPassword_Type(DisplayString):
    """Custom type snAgentUserAccntPassword based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 48),
    )


_SnAgentUserAccntPassword_Type.__name__ = "DisplayString"
_SnAgentUserAccntPassword_Object = MibTableColumn
snAgentUserAccntPassword = _SnAgentUserAccntPassword_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 2, 9, 2, 1, 2),
    _SnAgentUserAccntPassword_Type()
)
snAgentUserAccntPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snAgentUserAccntPassword.setStatus("mandatory")
_SnAgentUserAccntEncryptCode_Type = Integer32
_SnAgentUserAccntEncryptCode_Object = MibTableColumn
snAgentUserAccntEncryptCode = _SnAgentUserAccntEncryptCode_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 2, 9, 2, 1, 3),
    _SnAgentUserAccntEncryptCode_Type()
)
snAgentUserAccntEncryptCode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snAgentUserAccntEncryptCode.setStatus("mandatory")
_SnAgentUserAccntPrivilege_Type = Integer32
_SnAgentUserAccntPrivilege_Object = MibTableColumn
snAgentUserAccntPrivilege = _SnAgentUserAccntPrivilege_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 2, 9, 2, 1, 4),
    _SnAgentUserAccntPrivilege_Type()
)
snAgentUserAccntPrivilege.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snAgentUserAccntPrivilege.setStatus("mandatory")


class _SnAgentUserAccntRowStatus_Type(Integer32):
    """Custom type snAgentUserAccntRowStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("create", 4),
          ("delete", 3),
          ("modify", 5),
          ("other", 1),
          ("valid", 2))
    )


_SnAgentUserAccntRowStatus_Type.__name__ = "Integer32"
_SnAgentUserAccntRowStatus_Object = MibTableColumn
snAgentUserAccntRowStatus = _SnAgentUserAccntRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 2, 9, 2, 1, 5),
    _SnAgentUserAccntRowStatus_Type()
)
snAgentUserAccntRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snAgentUserAccntRowStatus.setStatus("mandatory")
_SnAgentRedundant_ObjectIdentity = ObjectIdentity
snAgentRedundant = _SnAgentRedundant_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 2, 10)
)
_SnAgentRedunGbl_ObjectIdentity = ObjectIdentity
snAgentRedunGbl = _SnAgentRedunGbl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 2, 10, 1)
)


class _SnAgentRedunActiveMgmtMod_Type(Integer32):
    """Custom type snAgentRedunActiveMgmtMod based on Integer32"""
    defaultValue = 0


_SnAgentRedunActiveMgmtMod_Object = MibScalar
snAgentRedunActiveMgmtMod = _SnAgentRedunActiveMgmtMod_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 2, 10, 1, 1),
    _SnAgentRedunActiveMgmtMod_Type()
)
snAgentRedunActiveMgmtMod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snAgentRedunActiveMgmtMod.setStatus("mandatory")


class _SnAgentRedunSyncConfig_Type(Integer32):
    """Custom type snAgentRedunSyncConfig based on Integer32"""
    defaultValue = 10


_SnAgentRedunSyncConfig_Object = MibScalar
snAgentRedunSyncConfig = _SnAgentRedunSyncConfig_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 2, 10, 1, 2),
    _SnAgentRedunSyncConfig_Type()
)
snAgentRedunSyncConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snAgentRedunSyncConfig.setStatus("mandatory")


class _SnAgentRedunBkupCopyBootCode_Type(Integer32):
    """Custom type snAgentRedunBkupCopyBootCode based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_SnAgentRedunBkupCopyBootCode_Type.__name__ = "Integer32"
_SnAgentRedunBkupCopyBootCode_Object = MibScalar
snAgentRedunBkupCopyBootCode = _SnAgentRedunBkupCopyBootCode_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 2, 10, 1, 3),
    _SnAgentRedunBkupCopyBootCode_Type()
)
snAgentRedunBkupCopyBootCode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snAgentRedunBkupCopyBootCode.setStatus("mandatory")


class _SnAgentEnableMgmtModRedunStateChangeTrap_Type(Integer32):
    """Custom type snAgentEnableMgmtModRedunStateChangeTrap based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_SnAgentEnableMgmtModRedunStateChangeTrap_Type.__name__ = "Integer32"
_SnAgentEnableMgmtModRedunStateChangeTrap_Object = MibScalar
snAgentEnableMgmtModRedunStateChangeTrap = _SnAgentEnableMgmtModRedunStateChangeTrap_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 2, 10, 1, 4),
    _SnAgentEnableMgmtModRedunStateChangeTrap_Type()
)
snAgentEnableMgmtModRedunStateChangeTrap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snAgentEnableMgmtModRedunStateChangeTrap.setStatus("mandatory")


class _SnAgentRedunBkupBootLoad_Type(Integer32):
    """Custom type snAgentRedunBkupBootLoad based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              17,
              20)
        )
    )
    namedValues = NamedValues(
        *(("downloadBackup", 20),
          ("normal", 1),
          ("operationError", 17))
    )


_SnAgentRedunBkupBootLoad_Type.__name__ = "Integer32"
_SnAgentRedunBkupBootLoad_Object = MibScalar
snAgentRedunBkupBootLoad = _SnAgentRedunBkupBootLoad_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 2, 10, 1, 5),
    _SnAgentRedunBkupBootLoad_Type()
)
snAgentRedunBkupBootLoad.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snAgentRedunBkupBootLoad.setStatus("mandatory")


class _SnAgentRedunSwitchOver_Type(Integer32):
    """Custom type snAgentRedunSwitchOver based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("reset", 2))
    )


_SnAgentRedunSwitchOver_Type.__name__ = "Integer32"
_SnAgentRedunSwitchOver_Object = MibScalar
snAgentRedunSwitchOver = _SnAgentRedunSwitchOver_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 2, 10, 1, 6),
    _SnAgentRedunSwitchOver_Type()
)
snAgentRedunSwitchOver.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snAgentRedunSwitchOver.setStatus("mandatory")
_SnStackGen_ObjectIdentity = ObjectIdentity
snStackGen = _SnStackGen_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 5, 1)
)


class _SnStackPriSwitchMode_Type(Integer32):
    """Custom type snStackPriSwitchMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_SnStackPriSwitchMode_Type.__name__ = "Integer32"
_SnStackPriSwitchMode_Object = MibScalar
snStackPriSwitchMode = _SnStackPriSwitchMode_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 5, 1, 1),
    _SnStackPriSwitchMode_Type()
)
snStackPriSwitchMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snStackPriSwitchMode.setStatus("mandatory")
_SnStackMaxSecSwitch_Type = Integer32
_SnStackMaxSecSwitch_Object = MibScalar
snStackMaxSecSwitch = _SnStackMaxSecSwitch_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 5, 1, 2),
    _SnStackMaxSecSwitch_Type()
)
snStackMaxSecSwitch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snStackMaxSecSwitch.setStatus("mandatory")
_SnStackTotalSecSwitch_Type = Integer32
_SnStackTotalSecSwitch_Object = MibScalar
snStackTotalSecSwitch = _SnStackTotalSecSwitch_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 5, 1, 3),
    _SnStackTotalSecSwitch_Type()
)
snStackTotalSecSwitch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snStackTotalSecSwitch.setStatus("mandatory")


class _SnStackSyncAllSecSwitch_Type(Integer32):
    """Custom type snStackSyncAllSecSwitch based on Integer32"""
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
        *(("device", 2),
          ("global", 3),
          ("invalid", 1),
          ("local", 4),
          ("normal", 0))
    )


_SnStackSyncAllSecSwitch_Type.__name__ = "Integer32"
_SnStackSyncAllSecSwitch_Object = MibScalar
snStackSyncAllSecSwitch = _SnStackSyncAllSecSwitch_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 5, 1, 4),
    _SnStackSyncAllSecSwitch_Type()
)
snStackSyncAllSecSwitch.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snStackSyncAllSecSwitch.setStatus("mandatory")


class _SnStackSmSlotIndex_Type(Integer32):
    """Custom type snStackSmSlotIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8),
    )


_SnStackSmSlotIndex_Type.__name__ = "Integer32"
_SnStackSmSlotIndex_Object = MibScalar
snStackSmSlotIndex = _SnStackSmSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 5, 1, 5),
    _SnStackSmSlotIndex_Type()
)
snStackSmSlotIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snStackSmSlotIndex.setStatus("mandatory")


class _SnStackFmpSetProcess_Type(Integer32):
    """Custom type snStackFmpSetProcess based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("failure", 2),
          ("normal", 0),
          ("pending", 1))
    )


_SnStackFmpSetProcess_Type.__name__ = "Integer32"
_SnStackFmpSetProcess_Object = MibScalar
snStackFmpSetProcess = _SnStackFmpSetProcess_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 5, 1, 6),
    _SnStackFmpSetProcess_Type()
)
snStackFmpSetProcess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snStackFmpSetProcess.setStatus("mandatory")
_SnStackSecSwitchInfo_ObjectIdentity = ObjectIdentity
snStackSecSwitchInfo = _SnStackSecSwitchInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 5, 2)
)
_SnStackSecSwitchTable_Object = MibTable
snStackSecSwitchTable = _SnStackSecSwitchTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 5, 2, 1)
)
if mibBuilder.loadTexts:
    snStackSecSwitchTable.setStatus("mandatory")
_SnStackSecSwitchEntry_Object = MibTableRow
snStackSecSwitchEntry = _SnStackSecSwitchEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 5, 2, 1, 1)
)
snStackSecSwitchEntry.setIndexNames(
    (0, "HP-SN-AGENT-MIB", "snStackSecSwitchIndex"),
)
if mibBuilder.loadTexts:
    snStackSecSwitchEntry.setStatus("mandatory")


class _SnStackSecSwitchIndex_Type(Integer32):
    """Custom type snStackSecSwitchIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 26),
    )


_SnStackSecSwitchIndex_Type.__name__ = "Integer32"
_SnStackSecSwitchIndex_Object = MibTableColumn
snStackSecSwitchIndex = _SnStackSecSwitchIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 5, 2, 1, 1, 1),
    _SnStackSecSwitchIndex_Type()
)
snStackSecSwitchIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snStackSecSwitchIndex.setStatus("mandatory")


class _SnStackSecSwitchSlotId_Type(Integer32):
    """Custom type snStackSecSwitchSlotId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 26),
    )


_SnStackSecSwitchSlotId_Type.__name__ = "Integer32"
_SnStackSecSwitchSlotId_Object = MibTableColumn
snStackSecSwitchSlotId = _SnStackSecSwitchSlotId_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 5, 2, 1, 1, 2),
    _SnStackSecSwitchSlotId_Type()
)
snStackSecSwitchSlotId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snStackSecSwitchSlotId.setStatus("mandatory")


class _SnStackSecSwitchPortCnts_Type(Integer32):
    """Custom type snStackSecSwitchPortCnts based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 26),
    )


_SnStackSecSwitchPortCnts_Type.__name__ = "Integer32"
_SnStackSecSwitchPortCnts_Object = MibTableColumn
snStackSecSwitchPortCnts = _SnStackSecSwitchPortCnts_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 5, 2, 1, 1, 3),
    _SnStackSecSwitchPortCnts_Type()
)
snStackSecSwitchPortCnts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snStackSecSwitchPortCnts.setStatus("mandatory")


class _SnStackSecSwitchEnabled_Type(Integer32):
    """Custom type snStackSecSwitchEnabled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_SnStackSecSwitchEnabled_Type.__name__ = "Integer32"
_SnStackSecSwitchEnabled_Object = MibTableColumn
snStackSecSwitchEnabled = _SnStackSecSwitchEnabled_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 5, 2, 1, 1, 4),
    _SnStackSecSwitchEnabled_Type()
)
snStackSecSwitchEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snStackSecSwitchEnabled.setStatus("mandatory")


class _SnStackSecSwitchAck_Type(Integer32):
    """Custom type snStackSecSwitchAck based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_SnStackSecSwitchAck_Type.__name__ = "Integer32"
_SnStackSecSwitchAck_Object = MibTableColumn
snStackSecSwitchAck = _SnStackSecSwitchAck_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 5, 2, 1, 1, 5),
    _SnStackSecSwitchAck_Type()
)
snStackSecSwitchAck.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snStackSecSwitchAck.setStatus("mandatory")
_SnStackSecSwitchMacAddr_Type = MacAddress
_SnStackSecSwitchMacAddr_Object = MibTableColumn
snStackSecSwitchMacAddr = _SnStackSecSwitchMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 5, 2, 1, 1, 6),
    _SnStackSecSwitchMacAddr_Type()
)
snStackSecSwitchMacAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snStackSecSwitchMacAddr.setStatus("mandatory")


class _SnStackSecSwitchSyncCmd_Type(Integer32):
    """Custom type snStackSecSwitchSyncCmd based on Integer32"""
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
        *(("device", 2),
          ("global", 3),
          ("invalid", 1),
          ("local", 4),
          ("normal", 0))
    )


_SnStackSecSwitchSyncCmd_Type.__name__ = "Integer32"
_SnStackSecSwitchSyncCmd_Object = MibTableColumn
snStackSecSwitchSyncCmd = _SnStackSecSwitchSyncCmd_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 5, 2, 1, 1, 7),
    _SnStackSecSwitchSyncCmd_Type()
)
snStackSecSwitchSyncCmd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snStackSecSwitchSyncCmd.setStatus("mandatory")
_SnStackSecSwitchIpAddr_Type = IpAddress
_SnStackSecSwitchIpAddr_Object = MibTableColumn
snStackSecSwitchIpAddr = _SnStackSecSwitchIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 5, 2, 1, 1, 8),
    _SnStackSecSwitchIpAddr_Type()
)
snStackSecSwitchIpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snStackSecSwitchIpAddr.setStatus("mandatory")
_SnStackSecSwitchSubnetMask_Type = IpAddress
_SnStackSecSwitchSubnetMask_Object = MibTableColumn
snStackSecSwitchSubnetMask = _SnStackSecSwitchSubnetMask_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 5, 2, 1, 1, 9),
    _SnStackSecSwitchSubnetMask_Type()
)
snStackSecSwitchSubnetMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snStackSecSwitchSubnetMask.setStatus("mandatory")


class _SnStackSecSwitchCfgCmd_Type(Integer32):
    """Custom type snStackSecSwitchCfgCmd based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("auto", 2),
          ("invalid", 1),
          ("manual", 3),
          ("normal", 0))
    )


_SnStackSecSwitchCfgCmd_Type.__name__ = "Integer32"
_SnStackSecSwitchCfgCmd_Object = MibTableColumn
snStackSecSwitchCfgCmd = _SnStackSecSwitchCfgCmd_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 1, 5, 2, 1, 1, 10),
    _SnStackSecSwitchCfgCmd_Type()
)
snStackSecSwitchCfgCmd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snStackSecSwitchCfgCmd.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HP-SN-AGENT-MIB",
    **{"DisplayString": DisplayString,
       "MacAddress": MacAddress,
       "snChasGen": snChasGen,
       "snChasType": snChasType,
       "snChasSerNum": snChasSerNum,
       "snChasPwrSupplyStatus": snChasPwrSupplyStatus,
       "snChasFanStatus": snChasFanStatus,
       "snChasMainBrdDescription": snChasMainBrdDescription,
       "snChasMainPortTotal": snChasMainPortTotal,
       "snChasExpBrdDescription": snChasExpBrdDescription,
       "snChasExpPortTotal": snChasExpPortTotal,
       "snChasStatusLeds": snChasStatusLeds,
       "snChasTrafficLeds": snChasTrafficLeds,
       "snChasMediaLeds": snChasMediaLeds,
       "snChasEnablePwrSupplyTrap": snChasEnablePwrSupplyTrap,
       "snChasMainBrdId": snChasMainBrdId,
       "snChasExpBrdId": snChasExpBrdId,
       "snChasSpeedLeds": snChasSpeedLeds,
       "snChasEnableFanTrap": snChasEnableFanTrap,
       "snChasIdNumber": snChasIdNumber,
       "snChasActualTemperature": snChasActualTemperature,
       "snChasWarningTemperature": snChasWarningTemperature,
       "snChasShutdownTemperature": snChasShutdownTemperature,
       "snChasEnableTempWarnTrap": snChasEnableTempWarnTrap,
       "snChasPwr": snChasPwr,
       "snChasPwrSupplyTable": snChasPwrSupplyTable,
       "snChasPwrSupplyEntry": snChasPwrSupplyEntry,
       "snChasPwrSupplyIndex": snChasPwrSupplyIndex,
       "snChasPwrSupplyDescription": snChasPwrSupplyDescription,
       "snChasPwrSupplyOperStatus": snChasPwrSupplyOperStatus,
       "snChasFan": snChasFan,
       "snChasFanTable": snChasFanTable,
       "snChasFanEntry": snChasFanEntry,
       "snChasFanIndex": snChasFanIndex,
       "snChasFanDescription": snChasFanDescription,
       "snChasFanOperStatus": snChasFanOperStatus,
       "snAgentGbl": snAgentGbl,
       "snAgReload": snAgReload,
       "snAgEraseNVRAM": snAgEraseNVRAM,
       "snAgWriteNVRAM": snAgWriteNVRAM,
       "snAgConfigFromNVRAM": snAgConfigFromNVRAM,
       "snAgTftpServerIp": snAgTftpServerIp,
       "snAgImgFname": snAgImgFname,
       "snAgImgLoad": snAgImgLoad,
       "snAgCfgFname": snAgCfgFname,
       "snAgCfgLoad": snAgCfgLoad,
       "snAgDefGwayIp": snAgDefGwayIp,
       "snAgImgVer": snAgImgVer,
       "snAgFlashImgVer": snAgFlashImgVer,
       "snAgGblIfIpAddr": snAgGblIfIpAddr,
       "snAgGblIfIpMask": snAgGblIfIpMask,
       "snAgGblPassword": snAgGblPassword,
       "snAgTrpRcvrCurEntry": snAgTrpRcvrCurEntry,
       "snAgGblDataRetrieveMode": snAgGblDataRetrieveMode,
       "snAgSystemLog": snAgSystemLog,
       "snAgGblEnableColdStartTrap": snAgGblEnableColdStartTrap,
       "snAgGblEnableLinkUpTrap": snAgGblEnableLinkUpTrap,
       "snAgGblEnableLinkDownTrap": snAgGblEnableLinkDownTrap,
       "snAgGblPasswordChangeMode": snAgGblPasswordChangeMode,
       "snAgGblReadOnlyCommunity": snAgGblReadOnlyCommunity,
       "snAgGblReadWriteCommunity": snAgGblReadWriteCommunity,
       "snAgGblCurrentSecurityLevel": snAgGblCurrentSecurityLevel,
       "snAgGblSecurityLevelSet": snAgGblSecurityLevelSet,
       "snAgGblLevelPasswordsMask": snAgGblLevelPasswordsMask,
       "snAgGblQueueOverflow": snAgGblQueueOverflow,
       "snAgGblBufferShortage": snAgGblBufferShortage,
       "snAgGblDmaFailure": snAgGblDmaFailure,
       "snAgGblResourceLowWarning": snAgGblResourceLowWarning,
       "snAgGblExcessiveErrorWarning": snAgGblExcessiveErrorWarning,
       "snAgGblCpuUtilData": snAgGblCpuUtilData,
       "snAgGblCpuUtilCollect": snAgGblCpuUtilCollect,
       "snAgGblTelnetTimeout": snAgGblTelnetTimeout,
       "snAgGblEnableWebMgmt": snAgGblEnableWebMgmt,
       "snAgGblSecurityLevelBinding": snAgGblSecurityLevelBinding,
       "snAgGblEnableSLB": snAgGblEnableSLB,
       "snAgSoftwareFeature": snAgSoftwareFeature,
       "snAgGblEnableModuleInsertedTrap": snAgGblEnableModuleInsertedTrap,
       "snAgGblEnableModuleRemovedTrap": snAgGblEnableModuleRemovedTrap,
       "snAgGblTrapMessage": snAgGblTrapMessage,
       "snAgGblEnableTelnetServer": snAgGblEnableTelnetServer,
       "snAgGblTelnetPassword": snAgGblTelnetPassword,
       "snAgBuildDate": snAgBuildDate,
       "snAgBuildtime": snAgBuildtime,
       "snAgBuildVer": snAgBuildVer,
       "snAgentBrd": snAgentBrd,
       "snAgentBrdTable": snAgentBrdTable,
       "snAgentBrdEntry": snAgentBrdEntry,
       "snAgentBrdIndex": snAgentBrdIndex,
       "snAgentBrdMainBrdDescription": snAgentBrdMainBrdDescription,
       "snAgentBrdMainBrdId": snAgentBrdMainBrdId,
       "snAgentBrdMainPortTotal": snAgentBrdMainPortTotal,
       "snAgentBrdExpBrdDescription": snAgentBrdExpBrdDescription,
       "snAgentBrdExpBrdId": snAgentBrdExpBrdId,
       "snAgentBrdExpPortTotal": snAgentBrdExpPortTotal,
       "snAgentBrdStatusLeds": snAgentBrdStatusLeds,
       "snAgentBrdTrafficLeds": snAgentBrdTrafficLeds,
       "snAgentBrdMediaLeds": snAgentBrdMediaLeds,
       "snAgentBrdSpeedLeds": snAgentBrdSpeedLeds,
       "snAgentBrdModuleStatus": snAgentBrdModuleStatus,
       "snAgentBrdRedundantStatus": snAgentBrdRedundantStatus,
       "snAgentBrdAlarmLeds": snAgentBrdAlarmLeds,
       "snAgentBrdTxTrafficLeds": snAgentBrdTxTrafficLeds,
       "snAgentBrdRxTrafficLeds": snAgentBrdRxTrafficLeds,
       "snAgentTrp": snAgentTrp,
       "snAgTrpRcvrTable": snAgTrpRcvrTable,
       "snAgTrpRcvrEntry": snAgTrpRcvrEntry,
       "snAgTrpRcvrIndex": snAgTrpRcvrIndex,
       "snAgTrpRcvrIpAddr": snAgTrpRcvrIpAddr,
       "snAgTrpRcvrComm": snAgTrpRcvrComm,
       "snAgTrpRcvrStatus": snAgTrpRcvrStatus,
       "snAgentBoot": snAgentBoot,
       "snAgBootSeqTable": snAgBootSeqTable,
       "snAgBootSeqEntry": snAgBootSeqEntry,
       "snAgBootSeqIndex": snAgBootSeqIndex,
       "snAgBootSeqInstruction": snAgBootSeqInstruction,
       "snAgBootSeqIpAddr": snAgBootSeqIpAddr,
       "snAgBootSeqFilename": snAgBootSeqFilename,
       "snAgBootSeqRowStatus": snAgBootSeqRowStatus,
       "snAgCfgEos": snAgCfgEos,
       "snAgCfgEosTable": snAgCfgEosTable,
       "snAgCfgEosEntry": snAgCfgEosEntry,
       "snAgCfgEosIndex": snAgCfgEosIndex,
       "snAgCfgEosPacket": snAgCfgEosPacket,
       "snAgCfgEosChkSum": snAgCfgEosChkSum,
       "snAgentLog": snAgentLog,
       "snAgSysLogGbl": snAgSysLogGbl,
       "snAgSysLogGblEnable": snAgSysLogGblEnable,
       "snAgSysLogGblBufferSize": snAgSysLogGblBufferSize,
       "snAgSysLogGblClear": snAgSysLogGblClear,
       "snAgSysLogGblCriticalLevel": snAgSysLogGblCriticalLevel,
       "snAgSysLogGblLoggedCount": snAgSysLogGblLoggedCount,
       "snAgSysLogGblDroppedCount": snAgSysLogGblDroppedCount,
       "snAgSysLogGblFlushedCount": snAgSysLogGblFlushedCount,
       "snAgSysLogGblOverrunCount": snAgSysLogGblOverrunCount,
       "snAgSysLogGblServer": snAgSysLogGblServer,
       "snAgSysLogGblFacility": snAgSysLogGblFacility,
       "snAgSysLogBufferTable": snAgSysLogBufferTable,
       "snAgSysLogBufferEntry": snAgSysLogBufferEntry,
       "snAgSysLogBufferIndex": snAgSysLogBufferIndex,
       "snAgSysLogBufferTimeStamp": snAgSysLogBufferTimeStamp,
       "snAgSysLogBufferCriticalLevel": snAgSysLogBufferCriticalLevel,
       "snAgSysLogBufferMessage": snAgSysLogBufferMessage,
       "snAgSysLogBufferCalTimeStamp": snAgSysLogBufferCalTimeStamp,
       "snAgStaticSysLogBufferTable": snAgStaticSysLogBufferTable,
       "snAgStaticSysLogBufferEntry": snAgStaticSysLogBufferEntry,
       "snAgStaticSysLogBufferIndex": snAgStaticSysLogBufferIndex,
       "snAgStaticSysLogBufferTimeStamp": snAgStaticSysLogBufferTimeStamp,
       "snAgStaticSysLogBufferCriticalLevel": snAgStaticSysLogBufferCriticalLevel,
       "snAgStaticSysLogBufferMessage": snAgStaticSysLogBufferMessage,
       "snAgStaticSysLogBufferCalTimeStamp": snAgStaticSysLogBufferCalTimeStamp,
       "snAgentSysParaConfig": snAgentSysParaConfig,
       "snAgentSysParaConfigTable": snAgentSysParaConfigTable,
       "snAgentSysParaConfigEntry": snAgentSysParaConfigEntry,
       "snAgentSysParaConfigIndex": snAgentSysParaConfigIndex,
       "snAgentSysParaConfigDescription": snAgentSysParaConfigDescription,
       "snAgentSysParaConfigMin": snAgentSysParaConfigMin,
       "snAgentSysParaConfigMax": snAgentSysParaConfigMax,
       "snAgentSysParaConfigDefault": snAgentSysParaConfigDefault,
       "snAgentSysParaConfigCurrent": snAgentSysParaConfigCurrent,
       "snAgentConfigModule": snAgentConfigModule,
       "snAgentConfigModuleTable": snAgentConfigModuleTable,
       "snAgentConfigModuleEntry": snAgentConfigModuleEntry,
       "snAgentConfigModuleIndex": snAgentConfigModuleIndex,
       "snAgentConfigModuleType": snAgentConfigModuleType,
       "snAgentConfigModuleRowStatus": snAgentConfigModuleRowStatus,
       "snAgentUser": snAgentUser,
       "snAgentUserGbl": snAgentUserGbl,
       "snAgentUserMaxAccnt": snAgentUserMaxAccnt,
       "snAgentUserAccntTable": snAgentUserAccntTable,
       "snAgentUserAccntEntry": snAgentUserAccntEntry,
       "snAgentUserAccntName": snAgentUserAccntName,
       "snAgentUserAccntPassword": snAgentUserAccntPassword,
       "snAgentUserAccntEncryptCode": snAgentUserAccntEncryptCode,
       "snAgentUserAccntPrivilege": snAgentUserAccntPrivilege,
       "snAgentUserAccntRowStatus": snAgentUserAccntRowStatus,
       "snAgentRedundant": snAgentRedundant,
       "snAgentRedunGbl": snAgentRedunGbl,
       "snAgentRedunActiveMgmtMod": snAgentRedunActiveMgmtMod,
       "snAgentRedunSyncConfig": snAgentRedunSyncConfig,
       "snAgentRedunBkupCopyBootCode": snAgentRedunBkupCopyBootCode,
       "snAgentEnableMgmtModRedunStateChangeTrap": snAgentEnableMgmtModRedunStateChangeTrap,
       "snAgentRedunBkupBootLoad": snAgentRedunBkupBootLoad,
       "snAgentRedunSwitchOver": snAgentRedunSwitchOver,
       "snStackGen": snStackGen,
       "snStackPriSwitchMode": snStackPriSwitchMode,
       "snStackMaxSecSwitch": snStackMaxSecSwitch,
       "snStackTotalSecSwitch": snStackTotalSecSwitch,
       "snStackSyncAllSecSwitch": snStackSyncAllSecSwitch,
       "snStackSmSlotIndex": snStackSmSlotIndex,
       "snStackFmpSetProcess": snStackFmpSetProcess,
       "snStackSecSwitchInfo": snStackSecSwitchInfo,
       "snStackSecSwitchTable": snStackSecSwitchTable,
       "snStackSecSwitchEntry": snStackSecSwitchEntry,
       "snStackSecSwitchIndex": snStackSecSwitchIndex,
       "snStackSecSwitchSlotId": snStackSecSwitchSlotId,
       "snStackSecSwitchPortCnts": snStackSecSwitchPortCnts,
       "snStackSecSwitchEnabled": snStackSecSwitchEnabled,
       "snStackSecSwitchAck": snStackSecSwitchAck,
       "snStackSecSwitchMacAddr": snStackSecSwitchMacAddr,
       "snStackSecSwitchSyncCmd": snStackSecSwitchSyncCmd,
       "snStackSecSwitchIpAddr": snStackSecSwitchIpAddr,
       "snStackSecSwitchSubnetMask": snStackSecSwitchSubnetMask,
       "snStackSecSwitchCfgCmd": snStackSecSwitchCfgCmd}
)
