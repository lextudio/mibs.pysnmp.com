# SNMP MIB module (GWADA-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/GWADA-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:49:21 2024
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

_Novell_ObjectIdentity = ObjectIdentity
novell = _Novell_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 23)
)
_MibDoc_ObjectIdentity = ObjectIdentity
mibDoc = _MibDoc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 23, 2)
)
_Gwada_ObjectIdentity = ObjectIdentity
gwada = _Gwada_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 23, 2, 39)
)
_Ada_ObjectIdentity = ObjectIdentity
ada = _Ada_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 23, 2, 39, 1)
)
_AdaTable_Object = MibTable
adaTable = _AdaTable_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 39, 1, 1)
)
if mibBuilder.loadTexts:
    adaTable.setStatus("mandatory")
_AdaEntry_Object = MibTableRow
adaEntry = _AdaEntry_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 39, 1, 1, 1)
)
adaEntry.setIndexNames(
    (0, "GWADA-MIB", "adaIndex"),
)
if mibBuilder.loadTexts:
    adaEntry.setStatus("mandatory")
_AdaIndex_Type = Integer32
_AdaIndex_Object = MibTableColumn
adaIndex = _AdaIndex_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 39, 1, 1, 1, 1),
    _AdaIndex_Type()
)
adaIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adaIndex.setStatus("mandatory")


class _AdaName_Type(DisplayString):
    """Custom type adaName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_AdaName_Type.__name__ = "DisplayString"
_AdaName_Object = MibTableColumn
adaName = _AdaName_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 39, 1, 1, 1, 2),
    _AdaName_Type()
)
adaName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adaName.setStatus("mandatory")


class _AdaOperationMode_Type(Integer32):
    """Custom type adaOperationMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("domain", 2),
          ("normal", 1),
          ("postOffice", 3))
    )


_AdaOperationMode_Type.__name__ = "Integer32"
_AdaOperationMode_Object = MibTableColumn
adaOperationMode = _AdaOperationMode_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 39, 1, 1, 1, 3),
    _AdaOperationMode_Type()
)
adaOperationMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adaOperationMode.setStatus("mandatory")
_AdaTotalPostOffices_Type = Gauge32
_AdaTotalPostOffices_Object = MibTableColumn
adaTotalPostOffices = _AdaTotalPostOffices_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 39, 1, 1, 1, 4),
    _AdaTotalPostOffices_Type()
)
adaTotalPostOffices.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adaTotalPostOffices.setStatus("mandatory")
_AdaClosedPostOffices_Type = Gauge32
_AdaClosedPostOffices_Object = MibTableColumn
adaClosedPostOffices = _AdaClosedPostOffices_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 39, 1, 1, 1, 5),
    _AdaClosedPostOffices_Type()
)
adaClosedPostOffices.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adaClosedPostOffices.setStatus("mandatory")
_AdaCompletedMsgs_Type = Counter32
_AdaCompletedMsgs_Object = MibTableColumn
adaCompletedMsgs = _AdaCompletedMsgs_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 39, 1, 1, 1, 6),
    _AdaCompletedMsgs_Type()
)
adaCompletedMsgs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adaCompletedMsgs.setStatus("mandatory")
_AdaErrorMsgs_Type = Counter32
_AdaErrorMsgs_Object = MibTableColumn
adaErrorMsgs = _AdaErrorMsgs_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 39, 1, 1, 1, 7),
    _AdaErrorMsgs_Type()
)
adaErrorMsgs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adaErrorMsgs.setStatus("mandatory")
_AdaUptime_Type = TimeTicks
_AdaUptime_Object = MibTableColumn
adaUptime = _AdaUptime_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 39, 1, 1, 1, 8),
    _AdaUptime_Type()
)
adaUptime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adaUptime.setStatus("mandatory")


class _AdaCurrentLogFile_Type(DisplayString):
    """Custom type adaCurrentLogFile based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_AdaCurrentLogFile_Type.__name__ = "DisplayString"
_AdaCurrentLogFile_Object = MibTableColumn
adaCurrentLogFile = _AdaCurrentLogFile_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 39, 1, 1, 1, 9),
    _AdaCurrentLogFile_Type()
)
adaCurrentLogFile.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adaCurrentLogFile.setStatus("mandatory")


class _AdaLogLevel_Type(Integer32):
    """Custom type adaLogLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("normal", 1),
          ("verbose", 2))
    )


_AdaLogLevel_Type.__name__ = "Integer32"
_AdaLogLevel_Object = MibTableColumn
adaLogLevel = _AdaLogLevel_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 39, 1, 1, 1, 10),
    _AdaLogLevel_Type()
)
adaLogLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adaLogLevel.setStatus("mandatory")


class _AdaFileLogging_Type(Integer32):
    """Custom type adaFileLogging based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("no", 0),
          ("yes", 1))
    )


_AdaFileLogging_Type.__name__ = "Integer32"
_AdaFileLogging_Object = MibTableColumn
adaFileLogging = _AdaFileLogging_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 39, 1, 1, 1, 11),
    _AdaFileLogging_Type()
)
adaFileLogging.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adaFileLogging.setStatus("mandatory")
_AdaMaxLogFileAge_Type = Integer32
_AdaMaxLogFileAge_Object = MibTableColumn
adaMaxLogFileAge = _AdaMaxLogFileAge_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 39, 1, 1, 1, 12),
    _AdaMaxLogFileAge_Type()
)
adaMaxLogFileAge.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adaMaxLogFileAge.setStatus("mandatory")
_AdaMaxLogDiskSpace_Type = Integer32
_AdaMaxLogDiskSpace_Object = MibTableColumn
adaMaxLogDiskSpace = _AdaMaxLogDiskSpace_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 39, 1, 1, 1, 13),
    _AdaMaxLogDiskSpace_Type()
)
adaMaxLogDiskSpace.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adaMaxLogDiskSpace.setStatus("mandatory")


class _AdaRestart_Type(Integer32):
    """Custom type adaRestart based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("no", 0),
          ("yes", 1))
    )


_AdaRestart_Type.__name__ = "Integer32"
_AdaRestart_Object = MibTableColumn
adaRestart = _AdaRestart_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 39, 1, 1, 1, 14),
    _AdaRestart_Type()
)
adaRestart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adaRestart.setStatus("mandatory")


class _AdaGUID_Type(DisplayString):
    """Custom type adaGUID based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 36),
    )


_AdaGUID_Type.__name__ = "DisplayString"
_AdaGUID_Object = MibTableColumn
adaGUID = _AdaGUID_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 39, 1, 1, 1, 15),
    _AdaGUID_Type()
)
adaGUID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adaGUID.setStatus("mandatory")


class _AdaOS_Type(DisplayString):
    """Custom type adaOS based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_AdaOS_Type.__name__ = "DisplayString"
_AdaOS_Object = MibTableColumn
adaOS = _AdaOS_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 39, 1, 1, 1, 16),
    _AdaOS_Type()
)
adaOS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adaOS.setStatus("mandatory")


class _AdaVersion_Type(DisplayString):
    """Custom type adaVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_AdaVersion_Type.__name__ = "DisplayString"
_AdaVersion_Object = MibTableColumn
adaVersion = _AdaVersion_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 39, 1, 1, 1, 17),
    _AdaVersion_Type()
)
adaVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adaVersion.setStatus("mandatory")
_AdaTrapInfo_ObjectIdentity = ObjectIdentity
adaTrapInfo = _AdaTrapInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 23, 2, 39, 2)
)
_AdaTrapTime_Type = Integer32
_AdaTrapTime_Object = MibScalar
adaTrapTime = _AdaTrapTime_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 39, 2, 1),
    _AdaTrapTime_Type()
)
adaTrapTime.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    adaTrapTime.setStatus("mandatory")


class _AdaFacilityName_Type(DisplayString):
    """Custom type adaFacilityName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_AdaFacilityName_Type.__name__ = "DisplayString"
_AdaFacilityName_Object = MibScalar
adaFacilityName = _AdaFacilityName_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 39, 2, 2),
    _AdaFacilityName_Type()
)
adaFacilityName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    adaFacilityName.setStatus("mandatory")


class _AdaFacilityLink_Type(DisplayString):
    """Custom type adaFacilityLink based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_AdaFacilityLink_Type.__name__ = "DisplayString"
_AdaFacilityLink_Object = MibScalar
adaFacilityLink = _AdaFacilityLink_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 39, 2, 3),
    _AdaFacilityLink_Type()
)
adaFacilityLink.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    adaFacilityLink.setStatus("mandatory")


class _AdaRecoveredDB_Type(DisplayString):
    """Custom type adaRecoveredDB based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_AdaRecoveredDB_Type.__name__ = "DisplayString"
_AdaRecoveredDB_Object = MibScalar
adaRecoveredDB = _AdaRecoveredDB_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 39, 2, 4),
    _AdaRecoveredDB_Type()
)
adaRecoveredDB.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    adaRecoveredDB.setStatus("mandatory")
_AdaTraps_ObjectIdentity = ObjectIdentity
adaTraps = _AdaTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 23, 2, 39, 3)
)

# Managed Objects groups


# Notification objects

adaStartTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 23, 2, 39, 3, 0, 1)
)
adaStartTrap.setObjects(
      *(("GWADA-MIB", "adaTrapTime"),
        ("GWADA-MIB", "adaName"),
        ("GWADA-MIB", "adaGUID"))
)
if mibBuilder.loadTexts:
    adaStartTrap.setStatus(
        ""
    )

adaShutdownTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 23, 2, 39, 3, 0, 2)
)
adaShutdownTrap.setObjects(
      *(("GWADA-MIB", "adaTrapTime"),
        ("GWADA-MIB", "adaName"),
        ("GWADA-MIB", "adaGUID"))
)
if mibBuilder.loadTexts:
    adaShutdownTrap.setStatus(
        ""
    )

adaFacilityBlockedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 23, 2, 39, 3, 0, 3)
)
adaFacilityBlockedTrap.setObjects(
      *(("GWADA-MIB", "adaTrapTime"),
        ("GWADA-MIB", "adaFacilityLink"),
        ("GWADA-MIB", "adaFacilityName"),
        ("GWADA-MIB", "adaGUID"))
)
if mibBuilder.loadTexts:
    adaFacilityBlockedTrap.setStatus(
        ""
    )

adaFacilityOpenTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 23, 2, 39, 3, 0, 4)
)
adaFacilityOpenTrap.setObjects(
      *(("GWADA-MIB", "adaTrapTime"),
        ("GWADA-MIB", "adaFacilityLink"),
        ("GWADA-MIB", "adaFacilityName"),
        ("GWADA-MIB", "adaGUID"))
)
if mibBuilder.loadTexts:
    adaFacilityOpenTrap.setStatus(
        ""
    )

adaDBRecoverOkay = NotificationType(
    (1, 3, 6, 1, 4, 1, 23, 2, 39, 3, 0, 5)
)
adaDBRecoverOkay.setObjects(
      *(("GWADA-MIB", "adaTrapTime"),
        ("GWADA-MIB", "adaRecoveredDB"),
        ("GWADA-MIB", "adaGUID"))
)
if mibBuilder.loadTexts:
    adaDBRecoverOkay.setStatus(
        ""
    )

adaDBRecoverError = NotificationType(
    (1, 3, 6, 1, 4, 1, 23, 2, 39, 3, 0, 6)
)
adaDBRecoverError.setObjects(
      *(("GWADA-MIB", "adaTrapTime"),
        ("GWADA-MIB", "adaRecoveredDB"),
        ("GWADA-MIB", "adaGUID"))
)
if mibBuilder.loadTexts:
    adaDBRecoverError.setStatus(
        ""
    )

adaDBRecoverWarn = NotificationType(
    (1, 3, 6, 1, 4, 1, 23, 2, 39, 3, 0, 7)
)
adaDBRecoverWarn.setObjects(
      *(("GWADA-MIB", "adaTrapTime"),
        ("GWADA-MIB", "adaRecoveredDB"),
        ("GWADA-MIB", "adaGUID"))
)
if mibBuilder.loadTexts:
    adaDBRecoverWarn.setStatus(
        ""
    )

adaRestartTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 23, 2, 39, 3, 0, 8)
)
adaRestartTrap.setObjects(
      *(("GWADA-MIB", "adaTrapTime"),
        ("GWADA-MIB", "adaFacilityName"),
        ("GWADA-MIB", "adaGUID"))
)
if mibBuilder.loadTexts:
    adaRestartTrap.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "GWADA-MIB",
    **{"novell": novell,
       "mibDoc": mibDoc,
       "gwada": gwada,
       "ada": ada,
       "adaTable": adaTable,
       "adaEntry": adaEntry,
       "adaIndex": adaIndex,
       "adaName": adaName,
       "adaOperationMode": adaOperationMode,
       "adaTotalPostOffices": adaTotalPostOffices,
       "adaClosedPostOffices": adaClosedPostOffices,
       "adaCompletedMsgs": adaCompletedMsgs,
       "adaErrorMsgs": adaErrorMsgs,
       "adaUptime": adaUptime,
       "adaCurrentLogFile": adaCurrentLogFile,
       "adaLogLevel": adaLogLevel,
       "adaFileLogging": adaFileLogging,
       "adaMaxLogFileAge": adaMaxLogFileAge,
       "adaMaxLogDiskSpace": adaMaxLogDiskSpace,
       "adaRestart": adaRestart,
       "adaGUID": adaGUID,
       "adaOS": adaOS,
       "adaVersion": adaVersion,
       "adaTrapInfo": adaTrapInfo,
       "adaTrapTime": adaTrapTime,
       "adaFacilityName": adaFacilityName,
       "adaFacilityLink": adaFacilityLink,
       "adaRecoveredDB": adaRecoveredDB,
       "adaTraps": adaTraps,
       "adaStartTrap": adaStartTrap,
       "adaShutdownTrap": adaShutdownTrap,
       "adaFacilityBlockedTrap": adaFacilityBlockedTrap,
       "adaFacilityOpenTrap": adaFacilityOpenTrap,
       "adaDBRecoverOkay": adaDBRecoverOkay,
       "adaDBRecoverError": adaDBRecoverError,
       "adaDBRecoverWarn": adaDBRecoverWarn,
       "adaRestartTrap": adaRestartTrap}
)
