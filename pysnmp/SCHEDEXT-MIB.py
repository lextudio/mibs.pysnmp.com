# SNMP MIB module (SCHEDEXT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/SCHEDEXT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:50:02 2024
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

(schedExt,) = mibBuilder.importSymbols(
    "APENT-MIB",
    "schedExt")

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
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

schedExtMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2467, 1, 45, 1)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_ApSchedRecTable_Object = MibTable
apSchedRecTable = _ApSchedRecTable_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 45, 2)
)
if mibBuilder.loadTexts:
    apSchedRecTable.setStatus("current")
_ApSchedRecEntry_Object = MibTableRow
apSchedRecEntry = _ApSchedRecEntry_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 45, 2, 1)
)
apSchedRecEntry.setIndexNames(
    (0, "SCHEDEXT-MIB", "apSchedRecName"),
)
if mibBuilder.loadTexts:
    apSchedRecEntry.setStatus("current")


class _ApSchedRecName_Type(DisplayString):
    """Custom type apSchedRecName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_ApSchedRecName_Type.__name__ = "DisplayString"
_ApSchedRecName_Object = MibTableColumn
apSchedRecName = _ApSchedRecName_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 45, 2, 1, 1),
    _ApSchedRecName_Type()
)
apSchedRecName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    apSchedRecName.setStatus("current")


class _ApSchedRecMin_Type(DisplayString):
    """Custom type apSchedRecMin based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 40),
    )


_ApSchedRecMin_Type.__name__ = "DisplayString"
_ApSchedRecMin_Object = MibTableColumn
apSchedRecMin = _ApSchedRecMin_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 45, 2, 1, 2),
    _ApSchedRecMin_Type()
)
apSchedRecMin.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    apSchedRecMin.setStatus("current")


class _ApSchedRecHour_Type(DisplayString):
    """Custom type apSchedRecHour based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 40),
    )


_ApSchedRecHour_Type.__name__ = "DisplayString"
_ApSchedRecHour_Object = MibTableColumn
apSchedRecHour = _ApSchedRecHour_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 45, 2, 1, 3),
    _ApSchedRecHour_Type()
)
apSchedRecHour.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    apSchedRecHour.setStatus("current")


class _ApSchedRecDay_Type(DisplayString):
    """Custom type apSchedRecDay based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 40),
    )


_ApSchedRecDay_Type.__name__ = "DisplayString"
_ApSchedRecDay_Object = MibTableColumn
apSchedRecDay = _ApSchedRecDay_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 45, 2, 1, 4),
    _ApSchedRecDay_Type()
)
apSchedRecDay.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    apSchedRecDay.setStatus("current")


class _ApSchedRecMonth_Type(DisplayString):
    """Custom type apSchedRecMonth based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 40),
    )


_ApSchedRecMonth_Type.__name__ = "DisplayString"
_ApSchedRecMonth_Object = MibTableColumn
apSchedRecMonth = _ApSchedRecMonth_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 45, 2, 1, 5),
    _ApSchedRecMonth_Type()
)
apSchedRecMonth.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    apSchedRecMonth.setStatus("current")


class _ApSchedRecWDay_Type(DisplayString):
    """Custom type apSchedRecWDay based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 40),
    )


_ApSchedRecWDay_Type.__name__ = "DisplayString"
_ApSchedRecWDay_Object = MibTableColumn
apSchedRecWDay = _ApSchedRecWDay_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 45, 2, 1, 6),
    _ApSchedRecWDay_Type()
)
apSchedRecWDay.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    apSchedRecWDay.setStatus("current")


class _ApSchedRecCmd_Type(DisplayString):
    """Custom type apSchedRecCmd based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_ApSchedRecCmd_Type.__name__ = "DisplayString"
_ApSchedRecCmd_Object = MibTableColumn
apSchedRecCmd = _ApSchedRecCmd_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 45, 2, 1, 7),
    _ApSchedRecCmd_Type()
)
apSchedRecCmd.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    apSchedRecCmd.setStatus("current")


class _ApSchedRecLogFile_Type(DisplayString):
    """Custom type apSchedRecLogFile based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_ApSchedRecLogFile_Type.__name__ = "DisplayString"
_ApSchedRecLogFile_Object = MibTableColumn
apSchedRecLogFile = _ApSchedRecLogFile_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 45, 2, 1, 8),
    _ApSchedRecLogFile_Type()
)
apSchedRecLogFile.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    apSchedRecLogFile.setStatus("current")
_ApSchedRecId_Type = Integer32
_ApSchedRecId_Object = MibTableColumn
apSchedRecId = _ApSchedRecId_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 45, 2, 1, 9),
    _ApSchedRecId_Type()
)
apSchedRecId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apSchedRecId.setStatus("current")
_ApSchedRecStatus_Type = RowStatus
_ApSchedRecStatus_Object = MibTableColumn
apSchedRecStatus = _ApSchedRecStatus_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 45, 2, 1, 10),
    _ApSchedRecStatus_Type()
)
apSchedRecStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    apSchedRecStatus.setStatus("current")


class _ApSchedEnable_Type(Integer32):
    """Custom type apSchedEnable based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_ApSchedEnable_Type.__name__ = "Integer32"
_ApSchedEnable_Object = MibScalar
apSchedEnable = _ApSchedEnable_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 45, 3),
    _ApSchedEnable_Type()
)
apSchedEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apSchedEnable.setStatus("current")


class _ApSchedLogEnable_Type(Integer32):
    """Custom type apSchedLogEnable based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_ApSchedLogEnable_Type.__name__ = "Integer32"
_ApSchedLogEnable_Object = MibScalar
apSchedLogEnable = _ApSchedLogEnable_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 45, 4),
    _ApSchedLogEnable_Type()
)
apSchedLogEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apSchedLogEnable.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SCHEDEXT-MIB",
    **{"schedExtMib": schedExtMib,
       "apSchedRecTable": apSchedRecTable,
       "apSchedRecEntry": apSchedRecEntry,
       "apSchedRecName": apSchedRecName,
       "apSchedRecMin": apSchedRecMin,
       "apSchedRecHour": apSchedRecHour,
       "apSchedRecDay": apSchedRecDay,
       "apSchedRecMonth": apSchedRecMonth,
       "apSchedRecWDay": apSchedRecWDay,
       "apSchedRecCmd": apSchedRecCmd,
       "apSchedRecLogFile": apSchedRecLogFile,
       "apSchedRecId": apSchedRecId,
       "apSchedRecStatus": apSchedRecStatus,
       "apSchedEnable": apSchedEnable,
       "apSchedLogEnable": apSchedLogEnable}
)
