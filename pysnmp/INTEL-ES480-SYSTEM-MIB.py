# SNMP MIB module (INTEL-ES480-SYSTEM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/INTEL-ES480-SYSTEM-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:09:38 2024
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

(es480tAgent,) = mibBuilder.importSymbols(
    "INTEL-ES480-MIB",
    "es480tAgent")

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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

es480tSystem = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 343, 6, 60, 1)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs



class _Es480tSaveConfiguration_Type(Integer32):
    """Custom type es480tSaveConfiguration based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("saveToPrimary", 1),
          ("saveToSecondary", 2))
    )


_Es480tSaveConfiguration_Type.__name__ = "Integer32"
_Es480tSaveConfiguration_Object = MibScalar
es480tSaveConfiguration = _Es480tSaveConfiguration_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 60, 1, 3),
    _Es480tSaveConfiguration_Type()
)
es480tSaveConfiguration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es480tSaveConfiguration.setStatus("current")


class _Es480tSaveStatus_Type(Integer32):
    """Custom type es480tSaveStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("saveInProgress", 1),
          ("saveNotInProgress", 2))
    )


_Es480tSaveStatus_Type.__name__ = "Integer32"
_Es480tSaveStatus_Object = MibScalar
es480tSaveStatus = _Es480tSaveStatus_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 60, 1, 4),
    _Es480tSaveStatus_Type()
)
es480tSaveStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es480tSaveStatus.setStatus("current")


class _Es480tCurrentConfigInUse_Type(Integer32):
    """Custom type es480tCurrentConfigInUse based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("primary", 1),
          ("secondary", 2))
    )


_Es480tCurrentConfigInUse_Type.__name__ = "Integer32"
_Es480tCurrentConfigInUse_Object = MibScalar
es480tCurrentConfigInUse = _Es480tCurrentConfigInUse_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 60, 1, 5),
    _Es480tCurrentConfigInUse_Type()
)
es480tCurrentConfigInUse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es480tCurrentConfigInUse.setStatus("current")


class _Es480tConfigToUseOnReboot_Type(Integer32):
    """Custom type es480tConfigToUseOnReboot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("primary", 1),
          ("secondary", 2))
    )


_Es480tConfigToUseOnReboot_Type.__name__ = "Integer32"
_Es480tConfigToUseOnReboot_Object = MibScalar
es480tConfigToUseOnReboot = _Es480tConfigToUseOnReboot_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 60, 1, 6),
    _Es480tConfigToUseOnReboot_Type()
)
es480tConfigToUseOnReboot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es480tConfigToUseOnReboot.setStatus("current")
_Es480tOverTemperatureAlarm_Type = TruthValue
_Es480tOverTemperatureAlarm_Object = MibScalar
es480tOverTemperatureAlarm = _Es480tOverTemperatureAlarm_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 60, 1, 7),
    _Es480tOverTemperatureAlarm_Type()
)
es480tOverTemperatureAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es480tOverTemperatureAlarm.setStatus("current")


class _Es480tCurrentTemperature_Type(Integer32):
    """Custom type es480tCurrentTemperature based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_Es480tCurrentTemperature_Type.__name__ = "Integer32"
_Es480tCurrentTemperature_Object = MibScalar
es480tCurrentTemperature = _Es480tCurrentTemperature_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 60, 1, 8),
    _Es480tCurrentTemperature_Type()
)
es480tCurrentTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es480tCurrentTemperature.setStatus("current")
_Es480tFanStatusTable_Object = MibTable
es480tFanStatusTable = _Es480tFanStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 60, 1, 9)
)
if mibBuilder.loadTexts:
    es480tFanStatusTable.setStatus("current")
_Es480tFanStatusEntry_Object = MibTableRow
es480tFanStatusEntry = _Es480tFanStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 60, 1, 9, 1)
)
es480tFanStatusEntry.setIndexNames(
    (0, "INTEL-ES480-SYSTEM-MIB", "es480tFanNumber"),
)
if mibBuilder.loadTexts:
    es480tFanStatusEntry.setStatus("current")
_Es480tFanNumber_Type = Integer32
_Es480tFanNumber_Object = MibTableColumn
es480tFanNumber = _Es480tFanNumber_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 60, 1, 9, 1, 1),
    _Es480tFanNumber_Type()
)
es480tFanNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es480tFanNumber.setStatus("current")
_Es480tFanOperational_Type = TruthValue
_Es480tFanOperational_Object = MibTableColumn
es480tFanOperational = _Es480tFanOperational_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 60, 1, 9, 1, 2),
    _Es480tFanOperational_Type()
)
es480tFanOperational.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es480tFanOperational.setStatus("current")
_Es480tPrimaryPowerOperational_Type = TruthValue
_Es480tPrimaryPowerOperational_Object = MibScalar
es480tPrimaryPowerOperational = _Es480tPrimaryPowerOperational_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 60, 1, 10),
    _Es480tPrimaryPowerOperational_Type()
)
es480tPrimaryPowerOperational.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es480tPrimaryPowerOperational.setStatus("current")


class _Es480tRedundantPowerStatus_Type(Integer32):
    """Custom type es480tRedundantPowerStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("notPresent", 1),
          ("presentNotOK", 3),
          ("presentOK", 2))
    )


_Es480tRedundantPowerStatus_Type.__name__ = "Integer32"
_Es480tRedundantPowerStatus_Object = MibScalar
es480tRedundantPowerStatus = _Es480tRedundantPowerStatus_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 60, 1, 11),
    _Es480tRedundantPowerStatus_Type()
)
es480tRedundantPowerStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es480tRedundantPowerStatus.setStatus("current")
_Es480tRedundantPowerAlarm_Type = TruthValue
_Es480tRedundantPowerAlarm_Object = MibScalar
es480tRedundantPowerAlarm = _Es480tRedundantPowerAlarm_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 60, 1, 12),
    _Es480tRedundantPowerAlarm_Type()
)
es480tRedundantPowerAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es480tRedundantPowerAlarm.setStatus("current")


class _Es480tPrimarySoftwareRev_Type(DisplayString):
    """Custom type es480tPrimarySoftwareRev based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_Es480tPrimarySoftwareRev_Type.__name__ = "DisplayString"
_Es480tPrimarySoftwareRev_Object = MibScalar
es480tPrimarySoftwareRev = _Es480tPrimarySoftwareRev_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 60, 1, 13),
    _Es480tPrimarySoftwareRev_Type()
)
es480tPrimarySoftwareRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es480tPrimarySoftwareRev.setStatus("current")


class _Es480tSecondarySoftwareRev_Type(DisplayString):
    """Custom type es480tSecondarySoftwareRev based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_Es480tSecondarySoftwareRev_Type.__name__ = "DisplayString"
_Es480tSecondarySoftwareRev_Object = MibScalar
es480tSecondarySoftwareRev = _Es480tSecondarySoftwareRev_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 60, 1, 14),
    _Es480tSecondarySoftwareRev_Type()
)
es480tSecondarySoftwareRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es480tSecondarySoftwareRev.setStatus("current")


class _Es480tImageToUseOnReboot_Type(Integer32):
    """Custom type es480tImageToUseOnReboot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("primary", 1),
          ("secondary", 2))
    )


_Es480tImageToUseOnReboot_Type.__name__ = "Integer32"
_Es480tImageToUseOnReboot_Object = MibScalar
es480tImageToUseOnReboot = _Es480tImageToUseOnReboot_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 60, 1, 15),
    _Es480tImageToUseOnReboot_Type()
)
es480tImageToUseOnReboot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es480tImageToUseOnReboot.setStatus("current")


class _Es480tSystemID_Type(DisplayString):
    """Custom type es480tSystemID based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 126),
    )


_Es480tSystemID_Type.__name__ = "DisplayString"
_Es480tSystemID_Object = MibScalar
es480tSystemID = _Es480tSystemID_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 60, 1, 16),
    _Es480tSystemID_Type()
)
es480tSystemID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es480tSystemID.setStatus("current")


class _Es480tSystemBoardID_Type(DisplayString):
    """Custom type es480tSystemBoardID based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 126),
    )


_Es480tSystemBoardID_Type.__name__ = "DisplayString"
_Es480tSystemBoardID_Object = MibScalar
es480tSystemBoardID = _Es480tSystemBoardID_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 60, 1, 17),
    _Es480tSystemBoardID_Type()
)
es480tSystemBoardID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es480tSystemBoardID.setStatus("current")


class _Es480tSystemLeftBoardID_Type(DisplayString):
    """Custom type es480tSystemLeftBoardID based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 126),
    )


_Es480tSystemLeftBoardID_Type.__name__ = "DisplayString"
_Es480tSystemLeftBoardID_Object = MibScalar
es480tSystemLeftBoardID = _Es480tSystemLeftBoardID_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 60, 1, 18),
    _Es480tSystemLeftBoardID_Type()
)
es480tSystemLeftBoardID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es480tSystemLeftBoardID.setStatus("current")


class _Es480tSystemRightBoardID_Type(DisplayString):
    """Custom type es480tSystemRightBoardID based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 126),
    )


_Es480tSystemRightBoardID_Type.__name__ = "DisplayString"
_Es480tSystemRightBoardID_Object = MibScalar
es480tSystemRightBoardID = _Es480tSystemRightBoardID_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 60, 1, 19),
    _Es480tSystemRightBoardID_Type()
)
es480tSystemRightBoardID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es480tSystemRightBoardID.setStatus("current")


class _Es480tInputPowerVoltage_Type(Integer32):
    """Custom type es480tInputPowerVoltage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("v110", 1),
          ("v220", 2),
          ("v48DC", 3))
    )


_Es480tInputPowerVoltage_Type.__name__ = "Integer32"
_Es480tInputPowerVoltage_Object = MibScalar
es480tInputPowerVoltage = _Es480tInputPowerVoltage_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 60, 1, 20),
    _Es480tInputPowerVoltage_Type()
)
es480tInputPowerVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es480tInputPowerVoltage.setStatus("current")


class _Es480tPowerStatus_Type(Integer32):
    """Custom type es480tPowerStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("notPresent", 1),
          ("presentNotOK", 3),
          ("presentOK", 2))
    )


_Es480tPowerStatus_Type.__name__ = "Integer32"
_Es480tPowerStatus_Object = MibScalar
es480tPowerStatus = _Es480tPowerStatus_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 60, 1, 21),
    _Es480tPowerStatus_Type()
)
es480tPowerStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es480tPowerStatus.setStatus("current")
_Es480tPowerAlarm_Type = TruthValue
_Es480tPowerAlarm_Object = MibScalar
es480tPowerAlarm = _Es480tPowerAlarm_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 60, 1, 22),
    _Es480tPowerAlarm_Type()
)
es480tPowerAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es480tPowerAlarm.setStatus("current")
_Es480tRmonEnable_Type = TruthValue
_Es480tRmonEnable_Object = MibScalar
es480tRmonEnable = _Es480tRmonEnable_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 60, 1, 23),
    _Es480tRmonEnable_Type()
)
es480tRmonEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es480tRmonEnable.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "INTEL-ES480-SYSTEM-MIB",
    **{"es480tSystem": es480tSystem,
       "es480tSaveConfiguration": es480tSaveConfiguration,
       "es480tSaveStatus": es480tSaveStatus,
       "es480tCurrentConfigInUse": es480tCurrentConfigInUse,
       "es480tConfigToUseOnReboot": es480tConfigToUseOnReboot,
       "es480tOverTemperatureAlarm": es480tOverTemperatureAlarm,
       "es480tCurrentTemperature": es480tCurrentTemperature,
       "es480tFanStatusTable": es480tFanStatusTable,
       "es480tFanStatusEntry": es480tFanStatusEntry,
       "es480tFanNumber": es480tFanNumber,
       "es480tFanOperational": es480tFanOperational,
       "es480tPrimaryPowerOperational": es480tPrimaryPowerOperational,
       "es480tRedundantPowerStatus": es480tRedundantPowerStatus,
       "es480tRedundantPowerAlarm": es480tRedundantPowerAlarm,
       "es480tPrimarySoftwareRev": es480tPrimarySoftwareRev,
       "es480tSecondarySoftwareRev": es480tSecondarySoftwareRev,
       "es480tImageToUseOnReboot": es480tImageToUseOnReboot,
       "es480tSystemID": es480tSystemID,
       "es480tSystemBoardID": es480tSystemBoardID,
       "es480tSystemLeftBoardID": es480tSystemLeftBoardID,
       "es480tSystemRightBoardID": es480tSystemRightBoardID,
       "es480tInputPowerVoltage": es480tInputPowerVoltage,
       "es480tPowerStatus": es480tPowerStatus,
       "es480tPowerAlarm": es480tPowerAlarm,
       "es480tRmonEnable": es480tRmonEnable}
)
