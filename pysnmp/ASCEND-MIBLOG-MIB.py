# SNMP MIB module (ASCEND-MIBLOG-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ASCEND-MIBLOG-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:41:52 2024
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

(configuration,) = mibBuilder.importSymbols(
    "ASCEND-MIB",
    "configuration")

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



# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_MiblogProfile_ObjectIdentity = ObjectIdentity
miblogProfile = _MiblogProfile_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 529, 23, 93)
)
_MiblogProfileTable_Object = MibTable
miblogProfileTable = _MiblogProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 93, 1)
)
if mibBuilder.loadTexts:
    miblogProfileTable.setStatus("mandatory")
_MiblogProfileEntry_Object = MibTableRow
miblogProfileEntry = _MiblogProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 93, 1, 1)
)
miblogProfileEntry.setIndexNames(
    (0, "ASCEND-MIBLOG-MIB", "logProfile-Index-o"),
)
if mibBuilder.loadTexts:
    miblogProfileEntry.setStatus("mandatory")
_LogProfile_Index_o_Type = Integer32
_LogProfile_Index_o_Object = MibScalar
logProfile_Index_o = _LogProfile_Index_o_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 93, 1, 1, 1),
    _LogProfile_Index_o_Type()
)
logProfile_Index_o.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    logProfile_Index_o.setStatus("mandatory")


class _LogProfile_SaveLevel_Type(Integer32):
    """Custom type logProfile_SaveLevel based on Integer32"""
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
        *(("alert", 3),
          ("critical", 4),
          ("debug", 9),
          ("emergency", 2),
          ("error", 5),
          ("info", 8),
          ("none", 1),
          ("notice", 7),
          ("warning", 6))
    )


_LogProfile_SaveLevel_Type.__name__ = "Integer32"
_LogProfile_SaveLevel_Object = MibScalar
logProfile_SaveLevel = _LogProfile_SaveLevel_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 93, 1, 1, 2),
    _LogProfile_SaveLevel_Type()
)
logProfile_SaveLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    logProfile_SaveLevel.setStatus("mandatory")
_LogProfile_SaveNumber_Type = Integer32
_LogProfile_SaveNumber_Object = MibScalar
logProfile_SaveNumber = _LogProfile_SaveNumber_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 93, 1, 1, 3),
    _LogProfile_SaveNumber_Type()
)
logProfile_SaveNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    logProfile_SaveNumber.setStatus("mandatory")


class _LogProfile_CallInfo_Type(Integer32):
    """Custom type logProfile_CallInfo based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("endOfCall", 2),
          ("none", 1))
    )


_LogProfile_CallInfo_Type.__name__ = "Integer32"
_LogProfile_CallInfo_Object = MibScalar
logProfile_CallInfo = _LogProfile_CallInfo_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 93, 1, 1, 4),
    _LogProfile_CallInfo_Type()
)
logProfile_CallInfo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    logProfile_CallInfo.setStatus("mandatory")


class _LogProfile_SyslogEnabled_Type(Integer32):
    """Custom type logProfile_SyslogEnabled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_LogProfile_SyslogEnabled_Type.__name__ = "Integer32"
_LogProfile_SyslogEnabled_Object = MibScalar
logProfile_SyslogEnabled = _LogProfile_SyslogEnabled_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 93, 1, 1, 5),
    _LogProfile_SyslogEnabled_Type()
)
logProfile_SyslogEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    logProfile_SyslogEnabled.setStatus("mandatory")
_LogProfile_Host_Type = IpAddress
_LogProfile_Host_Object = MibScalar
logProfile_Host = _LogProfile_Host_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 93, 1, 1, 6),
    _LogProfile_Host_Type()
)
logProfile_Host.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    logProfile_Host.setStatus("mandatory")
_LogProfile_Port_Type = Integer32
_LogProfile_Port_Object = MibScalar
logProfile_Port = _LogProfile_Port_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 93, 1, 1, 7),
    _LogProfile_Port_Type()
)
logProfile_Port.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    logProfile_Port.setStatus("mandatory")


class _LogProfile_Facility_Type(Integer32):
    """Custom type logProfile_Facility based on Integer32"""
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
        *(("local0", 1),
          ("local1", 2),
          ("local2", 3),
          ("local3", 4),
          ("local4", 5),
          ("local5", 6),
          ("local6", 7),
          ("local7", 8))
    )


_LogProfile_Facility_Type.__name__ = "Integer32"
_LogProfile_Facility_Object = MibScalar
logProfile_Facility = _LogProfile_Facility_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 93, 1, 1, 8),
    _LogProfile_Facility_Type()
)
logProfile_Facility.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    logProfile_Facility.setStatus("mandatory")


class _LogProfile_SyslogFormat_Type(Integer32):
    """Custom type logProfile_SyslogFormat based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("max", 2),
          ("tnt", 1))
    )


_LogProfile_SyslogFormat_Type.__name__ = "Integer32"
_LogProfile_SyslogFormat_Object = MibScalar
logProfile_SyslogFormat = _LogProfile_SyslogFormat_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 93, 1, 1, 9),
    _LogProfile_SyslogFormat_Type()
)
logProfile_SyslogFormat.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    logProfile_SyslogFormat.setStatus("mandatory")


class _LogProfile_LogCallProgress_Type(Integer32):
    """Custom type logProfile_LogCallProgress based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_LogProfile_LogCallProgress_Type.__name__ = "Integer32"
_LogProfile_LogCallProgress_Object = MibScalar
logProfile_LogCallProgress = _LogProfile_LogCallProgress_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 93, 1, 1, 10),
    _LogProfile_LogCallProgress_Type()
)
logProfile_LogCallProgress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    logProfile_LogCallProgress.setStatus("mandatory")


class _LogProfile_LogSoftwareVersion_Type(Integer32):
    """Custom type logProfile_LogSoftwareVersion based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_LogProfile_LogSoftwareVersion_Type.__name__ = "Integer32"
_LogProfile_LogSoftwareVersion_Object = MibScalar
logProfile_LogSoftwareVersion = _LogProfile_LogSoftwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 93, 1, 1, 11),
    _LogProfile_LogSoftwareVersion_Type()
)
logProfile_LogSoftwareVersion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    logProfile_LogSoftwareVersion.setStatus("mandatory")


class _LogProfile_SyslogLevel_Type(Integer32):
    """Custom type logProfile_SyslogLevel based on Integer32"""
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
        *(("alert", 3),
          ("critical", 4),
          ("debug", 9),
          ("emergency", 2),
          ("error", 5),
          ("info", 8),
          ("none", 1),
          ("notice", 7),
          ("warning", 6))
    )


_LogProfile_SyslogLevel_Type.__name__ = "Integer32"
_LogProfile_SyslogLevel_Object = MibScalar
logProfile_SyslogLevel = _LogProfile_SyslogLevel_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 93, 1, 1, 12),
    _LogProfile_SyslogLevel_Type()
)
logProfile_SyslogLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    logProfile_SyslogLevel.setStatus("mandatory")


class _LogProfile_Action_o_Type(Integer32):
    """Custom type logProfile_Action_o based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("createProfile", 2),
          ("deleteProfile", 3),
          ("noAction", 1))
    )


_LogProfile_Action_o_Type.__name__ = "Integer32"
_LogProfile_Action_o_Object = MibScalar
logProfile_Action_o = _LogProfile_Action_o_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 93, 1, 1, 13),
    _LogProfile_Action_o_Type()
)
logProfile_Action_o.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    logProfile_Action_o.setStatus("mandatory")
_MiblogProfile_AuxiliarySyslogTable_Object = MibTable
miblogProfile_AuxiliarySyslogTable = _MiblogProfile_AuxiliarySyslogTable_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 93, 2)
)
if mibBuilder.loadTexts:
    miblogProfile_AuxiliarySyslogTable.setStatus("mandatory")
_MiblogProfile_AuxiliarySyslogEntry_Object = MibTableRow
miblogProfile_AuxiliarySyslogEntry = _MiblogProfile_AuxiliarySyslogEntry_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 93, 2, 1)
)
miblogProfile_AuxiliarySyslogEntry.setIndexNames(
    (0, "ASCEND-MIBLOG-MIB", "logProfile-AuxiliarySyslog-Index-o"),
    (0, "ASCEND-MIBLOG-MIB", "logProfile-AuxiliarySyslog-Index1-o"),
)
if mibBuilder.loadTexts:
    miblogProfile_AuxiliarySyslogEntry.setStatus("mandatory")
_LogProfile_AuxiliarySyslog_Index_o_Type = Integer32
_LogProfile_AuxiliarySyslog_Index_o_Object = MibScalar
logProfile_AuxiliarySyslog_Index_o = _LogProfile_AuxiliarySyslog_Index_o_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 93, 2, 1, 1),
    _LogProfile_AuxiliarySyslog_Index_o_Type()
)
logProfile_AuxiliarySyslog_Index_o.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    logProfile_AuxiliarySyslog_Index_o.setStatus("mandatory")
_LogProfile_AuxiliarySyslog_Index1_o_Type = Integer32
_LogProfile_AuxiliarySyslog_Index1_o_Object = MibScalar
logProfile_AuxiliarySyslog_Index1_o = _LogProfile_AuxiliarySyslog_Index1_o_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 93, 2, 1, 2),
    _LogProfile_AuxiliarySyslog_Index1_o_Type()
)
logProfile_AuxiliarySyslog_Index1_o.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    logProfile_AuxiliarySyslog_Index1_o.setStatus("mandatory")


class _LogProfile_AuxiliarySyslog_SyslogEnabled_Type(Integer32):
    """Custom type logProfile_AuxiliarySyslog_SyslogEnabled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_LogProfile_AuxiliarySyslog_SyslogEnabled_Type.__name__ = "Integer32"
_LogProfile_AuxiliarySyslog_SyslogEnabled_Object = MibScalar
logProfile_AuxiliarySyslog_SyslogEnabled = _LogProfile_AuxiliarySyslog_SyslogEnabled_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 93, 2, 1, 3),
    _LogProfile_AuxiliarySyslog_SyslogEnabled_Type()
)
logProfile_AuxiliarySyslog_SyslogEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    logProfile_AuxiliarySyslog_SyslogEnabled.setStatus("mandatory")


class _LogProfile_AuxiliarySyslog_SyslogLevel_Type(Integer32):
    """Custom type logProfile_AuxiliarySyslog_SyslogLevel based on Integer32"""
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
        *(("alert", 3),
          ("critical", 4),
          ("debug", 9),
          ("emergency", 2),
          ("error", 5),
          ("info", 8),
          ("none", 1),
          ("notice", 7),
          ("warning", 6))
    )


_LogProfile_AuxiliarySyslog_SyslogLevel_Type.__name__ = "Integer32"
_LogProfile_AuxiliarySyslog_SyslogLevel_Object = MibScalar
logProfile_AuxiliarySyslog_SyslogLevel = _LogProfile_AuxiliarySyslog_SyslogLevel_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 93, 2, 1, 4),
    _LogProfile_AuxiliarySyslog_SyslogLevel_Type()
)
logProfile_AuxiliarySyslog_SyslogLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    logProfile_AuxiliarySyslog_SyslogLevel.setStatus("mandatory")
_LogProfile_AuxiliarySyslog_Host_Type = IpAddress
_LogProfile_AuxiliarySyslog_Host_Object = MibScalar
logProfile_AuxiliarySyslog_Host = _LogProfile_AuxiliarySyslog_Host_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 93, 2, 1, 5),
    _LogProfile_AuxiliarySyslog_Host_Type()
)
logProfile_AuxiliarySyslog_Host.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    logProfile_AuxiliarySyslog_Host.setStatus("mandatory")
_LogProfile_AuxiliarySyslog_Port_Type = Integer32
_LogProfile_AuxiliarySyslog_Port_Object = MibScalar
logProfile_AuxiliarySyslog_Port = _LogProfile_AuxiliarySyslog_Port_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 93, 2, 1, 6),
    _LogProfile_AuxiliarySyslog_Port_Type()
)
logProfile_AuxiliarySyslog_Port.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    logProfile_AuxiliarySyslog_Port.setStatus("mandatory")


class _LogProfile_AuxiliarySyslog_Facility_Type(Integer32):
    """Custom type logProfile_AuxiliarySyslog_Facility based on Integer32"""
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
        *(("local0", 1),
          ("local1", 2),
          ("local2", 3),
          ("local3", 4),
          ("local4", 5),
          ("local5", 6),
          ("local6", 7),
          ("local7", 8))
    )


_LogProfile_AuxiliarySyslog_Facility_Type.__name__ = "Integer32"
_LogProfile_AuxiliarySyslog_Facility_Object = MibScalar
logProfile_AuxiliarySyslog_Facility = _LogProfile_AuxiliarySyslog_Facility_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 93, 2, 1, 7),
    _LogProfile_AuxiliarySyslog_Facility_Type()
)
logProfile_AuxiliarySyslog_Facility.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    logProfile_AuxiliarySyslog_Facility.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ASCEND-MIBLOG-MIB",
    **{"DisplayString": DisplayString,
       "miblogProfile": miblogProfile,
       "miblogProfileTable": miblogProfileTable,
       "miblogProfileEntry": miblogProfileEntry,
       "logProfile-Index-o": logProfile_Index_o,
       "logProfile-SaveLevel": logProfile_SaveLevel,
       "logProfile-SaveNumber": logProfile_SaveNumber,
       "logProfile-CallInfo": logProfile_CallInfo,
       "logProfile-SyslogEnabled": logProfile_SyslogEnabled,
       "logProfile-Host": logProfile_Host,
       "logProfile-Port": logProfile_Port,
       "logProfile-Facility": logProfile_Facility,
       "logProfile-SyslogFormat": logProfile_SyslogFormat,
       "logProfile-LogCallProgress": logProfile_LogCallProgress,
       "logProfile-LogSoftwareVersion": logProfile_LogSoftwareVersion,
       "logProfile-SyslogLevel": logProfile_SyslogLevel,
       "logProfile-Action-o": logProfile_Action_o,
       "miblogProfile-AuxiliarySyslogTable": miblogProfile_AuxiliarySyslogTable,
       "miblogProfile-AuxiliarySyslogEntry": miblogProfile_AuxiliarySyslogEntry,
       "logProfile-AuxiliarySyslog-Index-o": logProfile_AuxiliarySyslog_Index_o,
       "logProfile-AuxiliarySyslog-Index1-o": logProfile_AuxiliarySyslog_Index1_o,
       "logProfile-AuxiliarySyslog-SyslogEnabled": logProfile_AuxiliarySyslog_SyslogEnabled,
       "logProfile-AuxiliarySyslog-SyslogLevel": logProfile_AuxiliarySyslog_SyslogLevel,
       "logProfile-AuxiliarySyslog-Host": logProfile_AuxiliarySyslog_Host,
       "logProfile-AuxiliarySyslog-Port": logProfile_AuxiliarySyslog_Port,
       "logProfile-AuxiliarySyslog-Facility": logProfile_AuxiliarySyslog_Facility}
)
