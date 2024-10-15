# SNMP MIB module (INFORMANT-MBM) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/INFORMANT-MBM
# Produced by pysmi-1.5.4 at Mon Oct 14 22:09:16 2024
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

(DateAndTime,
 DisplayString,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "TextualConvention",
    "TruthValue")

(WtcsDisplayString,
 informant) = mibBuilder.importSymbols(
    "WTCS",
    "WtcsDisplayString",
    "informant")


# MODULE-IDENTITY

motherBoardMonitor = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9600, 1, 10)
)
motherBoardMonitor.setRevisions(
        ("2004-06-23 20:39",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_MbmBusType_Type = DisplayString
_MbmBusType_Object = MibScalar
mbmBusType = _MbmBusType_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 10, 1),
    _MbmBusType_Type()
)
mbmBusType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mbmBusType.setStatus("current")


class _MbmPath_Type(DisplayString):
    """Custom type mbmPath based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_MbmPath_Type.__name__ = "DisplayString"
_MbmPath_Object = MibScalar
mbmPath = _MbmPath_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 10, 2),
    _MbmPath_Type()
)
mbmPath.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mbmPath.setStatus("current")


class _MbmSmbName_Type(DisplayString):
    """Custom type mbmSmbName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_MbmSmbName_Type.__name__ = "DisplayString"
_MbmSmbName_Object = MibScalar
mbmSmbName = _MbmSmbName_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 10, 3),
    _MbmSmbName_Type()
)
mbmSmbName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mbmSmbName.setStatus("current")
_MbmSmbType_Type = DisplayString
_MbmSmbType_Object = MibScalar
mbmSmbType = _MbmSmbType_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 10, 4),
    _MbmSmbType_Type()
)
mbmSmbType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mbmSmbType.setStatus("current")
_MbmVersion_Type = DisplayString
_MbmVersion_Object = MibScalar
mbmVersion = _MbmVersion_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 10, 5),
    _MbmVersion_Type()
)
mbmVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mbmVersion.setStatus("current")
_MbmSensorTable_Object = MibTable
mbmSensorTable = _MbmSensorTable_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 10, 6)
)
if mibBuilder.loadTexts:
    mbmSensorTable.setStatus("current")
_MbmSensorEntry_Object = MibTableRow
mbmSensorEntry = _MbmSensorEntry_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 10, 6, 1)
)
mbmSensorEntry.setIndexNames(
    (0, "INFORMANT-MBM", "mbmSensorIndex"),
)
if mibBuilder.loadTexts:
    mbmSensorEntry.setStatus("current")


class _MbmSensorIndex_Type(Integer32):
    """Custom type mbmSensorIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 99),
    )


_MbmSensorIndex_Type.__name__ = "Integer32"
_MbmSensorIndex_Object = MibTableColumn
mbmSensorIndex = _MbmSensorIndex_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 10, 6, 1, 1),
    _MbmSensorIndex_Type()
)
mbmSensorIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mbmSensorIndex.setStatus("current")


class _MbmSensorName_Type(DisplayString):
    """Custom type mbmSensorName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 11),
    )


_MbmSensorName_Type.__name__ = "DisplayString"
_MbmSensorName_Object = MibTableColumn
mbmSensorName = _MbmSensorName_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 10, 6, 1, 2),
    _MbmSensorName_Type()
)
mbmSensorName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mbmSensorName.setStatus("current")


class _MbmSensorType_Type(Integer32):
    """Custom type mbmSensorType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("stFan", 3),
          ("stMhz", 4),
          ("stPercentage", 5),
          ("stTemperature", 1),
          ("stUnknown", 0),
          ("stVoltage", 2))
    )


_MbmSensorType_Type.__name__ = "Integer32"
_MbmSensorType_Object = MibTableColumn
mbmSensorType = _MbmSensorType_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 10, 6, 1, 3),
    _MbmSensorType_Type()
)
mbmSensorType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mbmSensorType.setStatus("current")
_MbmSensorReadout_Type = Integer32
_MbmSensorReadout_Object = MibTableColumn
mbmSensorReadout = _MbmSensorReadout_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 10, 6, 1, 4),
    _MbmSensorReadout_Type()
)
mbmSensorReadout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mbmSensorReadout.setStatus("current")
_MbmSensorCurrentI_Type = Integer32
_MbmSensorCurrentI_Object = MibTableColumn
mbmSensorCurrentI = _MbmSensorCurrentI_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 10, 6, 1, 5),
    _MbmSensorCurrentI_Type()
)
mbmSensorCurrentI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mbmSensorCurrentI.setStatus("current")


class _MbmSensorCurrentS_Type(DisplayString):
    """Custom type mbmSensorCurrentS based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 50),
    )


_MbmSensorCurrentS_Type.__name__ = "DisplayString"
_MbmSensorCurrentS_Object = MibTableColumn
mbmSensorCurrentS = _MbmSensorCurrentS_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 10, 6, 1, 6),
    _MbmSensorCurrentS_Type()
)
mbmSensorCurrentS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mbmSensorCurrentS.setStatus("current")
_MbmSensorLowI_Type = Integer32
_MbmSensorLowI_Object = MibTableColumn
mbmSensorLowI = _MbmSensorLowI_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 10, 6, 1, 7),
    _MbmSensorLowI_Type()
)
mbmSensorLowI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mbmSensorLowI.setStatus("current")


class _MbmSensorLowS_Type(DisplayString):
    """Custom type mbmSensorLowS based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 50),
    )


_MbmSensorLowS_Type.__name__ = "DisplayString"
_MbmSensorLowS_Object = MibTableColumn
mbmSensorLowS = _MbmSensorLowS_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 10, 6, 1, 8),
    _MbmSensorLowS_Type()
)
mbmSensorLowS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mbmSensorLowS.setStatus("current")
_MbmSensorHighI_Type = Integer32
_MbmSensorHighI_Object = MibTableColumn
mbmSensorHighI = _MbmSensorHighI_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 10, 6, 1, 9),
    _MbmSensorHighI_Type()
)
mbmSensorHighI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mbmSensorHighI.setStatus("current")


class _MbmSensorHighS_Type(DisplayString):
    """Custom type mbmSensorHighS based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 50),
    )


_MbmSensorHighS_Type.__name__ = "DisplayString"
_MbmSensorHighS_Object = MibTableColumn
mbmSensorHighS = _MbmSensorHighS_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 10, 6, 1, 10),
    _MbmSensorHighS_Type()
)
mbmSensorHighS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mbmSensorHighS.setStatus("current")
_MbmSensorAlarm1I_Type = Integer32
_MbmSensorAlarm1I_Object = MibTableColumn
mbmSensorAlarm1I = _MbmSensorAlarm1I_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 10, 6, 1, 11),
    _MbmSensorAlarm1I_Type()
)
mbmSensorAlarm1I.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mbmSensorAlarm1I.setStatus("current")


class _MbmSensorAlarm1S_Type(DisplayString):
    """Custom type mbmSensorAlarm1S based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 50),
    )


_MbmSensorAlarm1S_Type.__name__ = "DisplayString"
_MbmSensorAlarm1S_Object = MibTableColumn
mbmSensorAlarm1S = _MbmSensorAlarm1S_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 10, 6, 1, 12),
    _MbmSensorAlarm1S_Type()
)
mbmSensorAlarm1S.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mbmSensorAlarm1S.setStatus("current")
_MbmSensorAlarm2I_Type = Integer32
_MbmSensorAlarm2I_Object = MibTableColumn
mbmSensorAlarm2I = _MbmSensorAlarm2I_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 10, 6, 1, 13),
    _MbmSensorAlarm2I_Type()
)
mbmSensorAlarm2I.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mbmSensorAlarm2I.setStatus("current")


class _MbmSensorAlarm2S_Type(DisplayString):
    """Custom type mbmSensorAlarm2S based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 50),
    )


_MbmSensorAlarm2S_Type.__name__ = "DisplayString"
_MbmSensorAlarm2S_Object = MibTableColumn
mbmSensorAlarm2S = _MbmSensorAlarm2S_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 10, 6, 1, 14),
    _MbmSensorAlarm2S_Type()
)
mbmSensorAlarm2S.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mbmSensorAlarm2S.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "INFORMANT-MBM",
    **{"motherBoardMonitor": motherBoardMonitor,
       "mbmBusType": mbmBusType,
       "mbmPath": mbmPath,
       "mbmSmbName": mbmSmbName,
       "mbmSmbType": mbmSmbType,
       "mbmVersion": mbmVersion,
       "mbmSensorTable": mbmSensorTable,
       "mbmSensorEntry": mbmSensorEntry,
       "mbmSensorIndex": mbmSensorIndex,
       "mbmSensorName": mbmSensorName,
       "mbmSensorType": mbmSensorType,
       "mbmSensorReadout": mbmSensorReadout,
       "mbmSensorCurrentI": mbmSensorCurrentI,
       "mbmSensorCurrentS": mbmSensorCurrentS,
       "mbmSensorLowI": mbmSensorLowI,
       "mbmSensorLowS": mbmSensorLowS,
       "mbmSensorHighI": mbmSensorHighI,
       "mbmSensorHighS": mbmSensorHighS,
       "mbmSensorAlarm1I": mbmSensorAlarm1I,
       "mbmSensorAlarm1S": mbmSensorAlarm1S,
       "mbmSensorAlarm2I": mbmSensorAlarm2I,
       "mbmSensorAlarm2S": mbmSensorAlarm2S}
)
