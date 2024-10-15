# SNMP MIB module (SYSLOG-MSG-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/SYSLOG-MSG-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:00:13 2024
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
    "iso",
    "mib-2")

(DisplayString,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention",
    "TruthValue")

(SyslogFacility,
 SyslogSeverity) = mibBuilder.importSymbols(
    "SYSLOG-TC-MIB",
    "SyslogFacility",
    "SyslogSeverity")


# MODULE-IDENTITY

syslogMsgMib = ModuleIdentity(
    (1, 3, 6, 1, 2, 1, 192)
)
syslogMsgMib.setRevisions(
        ("2009-08-13 08:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class SyslogTimeStamp(OctetString, TextualConvention):
    status = "current"
    displayHint = "2d-1d-1d,1d:1d:1d.3d,1a1d:1d"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(10, 10),
        ValueSizeConstraint(13, 13),
    )



class SyslogParamValueString(OctetString, TextualConvention):
    status = "current"
    displayHint = "65535t"


# MIB Managed Objects in the order of their OIDs

_SyslogMsgNotifications_ObjectIdentity = ObjectIdentity
syslogMsgNotifications = _SyslogMsgNotifications_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 192, 0)
)
_SyslogMsgObjects_ObjectIdentity = ObjectIdentity
syslogMsgObjects = _SyslogMsgObjects_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 192, 1)
)
_SyslogMsgControl_ObjectIdentity = ObjectIdentity
syslogMsgControl = _SyslogMsgControl_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 192, 1, 1)
)


class _SyslogMsgTableMaxSize_Type(Unsigned32):
    """Custom type syslogMsgTableMaxSize based on Unsigned32"""
    defaultValue = 0


_SyslogMsgTableMaxSize_Object = MibScalar
syslogMsgTableMaxSize = _SyslogMsgTableMaxSize_Object(
    (1, 3, 6, 1, 2, 1, 192, 1, 1, 1),
    _SyslogMsgTableMaxSize_Type()
)
syslogMsgTableMaxSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    syslogMsgTableMaxSize.setStatus("current")


class _SyslogMsgEnableNotifications_Type(TruthValue):
    """Custom type syslogMsgEnableNotifications based on TruthValue"""


_SyslogMsgEnableNotifications_Object = MibScalar
syslogMsgEnableNotifications = _SyslogMsgEnableNotifications_Object(
    (1, 3, 6, 1, 2, 1, 192, 1, 1, 2),
    _SyslogMsgEnableNotifications_Type()
)
syslogMsgEnableNotifications.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    syslogMsgEnableNotifications.setStatus("current")
_SyslogMsgTable_Object = MibTable
syslogMsgTable = _SyslogMsgTable_Object(
    (1, 3, 6, 1, 2, 1, 192, 1, 2)
)
if mibBuilder.loadTexts:
    syslogMsgTable.setStatus("current")
_SyslogMsgEntry_Object = MibTableRow
syslogMsgEntry = _SyslogMsgEntry_Object(
    (1, 3, 6, 1, 2, 1, 192, 1, 2, 1)
)
syslogMsgEntry.setIndexNames(
    (0, "SYSLOG-MSG-MIB", "syslogMsgIndex"),
)
if mibBuilder.loadTexts:
    syslogMsgEntry.setStatus("current")


class _SyslogMsgIndex_Type(Unsigned32):
    """Custom type syslogMsgIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_SyslogMsgIndex_Type.__name__ = "Unsigned32"
_SyslogMsgIndex_Object = MibTableColumn
syslogMsgIndex = _SyslogMsgIndex_Object(
    (1, 3, 6, 1, 2, 1, 192, 1, 2, 1, 1),
    _SyslogMsgIndex_Type()
)
syslogMsgIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    syslogMsgIndex.setStatus("current")
_SyslogMsgFacility_Type = SyslogFacility
_SyslogMsgFacility_Object = MibTableColumn
syslogMsgFacility = _SyslogMsgFacility_Object(
    (1, 3, 6, 1, 2, 1, 192, 1, 2, 1, 2),
    _SyslogMsgFacility_Type()
)
syslogMsgFacility.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    syslogMsgFacility.setStatus("current")
_SyslogMsgSeverity_Type = SyslogSeverity
_SyslogMsgSeverity_Object = MibTableColumn
syslogMsgSeverity = _SyslogMsgSeverity_Object(
    (1, 3, 6, 1, 2, 1, 192, 1, 2, 1, 3),
    _SyslogMsgSeverity_Type()
)
syslogMsgSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    syslogMsgSeverity.setStatus("current")


class _SyslogMsgVersion_Type(Unsigned32):
    """Custom type syslogMsgVersion based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 999),
    )


_SyslogMsgVersion_Type.__name__ = "Unsigned32"
_SyslogMsgVersion_Object = MibTableColumn
syslogMsgVersion = _SyslogMsgVersion_Object(
    (1, 3, 6, 1, 2, 1, 192, 1, 2, 1, 4),
    _SyslogMsgVersion_Type()
)
syslogMsgVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    syslogMsgVersion.setStatus("current")
_SyslogMsgTimeStamp_Type = SyslogTimeStamp
_SyslogMsgTimeStamp_Object = MibTableColumn
syslogMsgTimeStamp = _SyslogMsgTimeStamp_Object(
    (1, 3, 6, 1, 2, 1, 192, 1, 2, 1, 5),
    _SyslogMsgTimeStamp_Type()
)
syslogMsgTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    syslogMsgTimeStamp.setStatus("current")


class _SyslogMsgHostName_Type(DisplayString):
    """Custom type syslogMsgHostName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SyslogMsgHostName_Type.__name__ = "DisplayString"
_SyslogMsgHostName_Object = MibTableColumn
syslogMsgHostName = _SyslogMsgHostName_Object(
    (1, 3, 6, 1, 2, 1, 192, 1, 2, 1, 6),
    _SyslogMsgHostName_Type()
)
syslogMsgHostName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    syslogMsgHostName.setStatus("current")


class _SyslogMsgAppName_Type(DisplayString):
    """Custom type syslogMsgAppName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 48),
    )


_SyslogMsgAppName_Type.__name__ = "DisplayString"
_SyslogMsgAppName_Object = MibTableColumn
syslogMsgAppName = _SyslogMsgAppName_Object(
    (1, 3, 6, 1, 2, 1, 192, 1, 2, 1, 7),
    _SyslogMsgAppName_Type()
)
syslogMsgAppName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    syslogMsgAppName.setStatus("current")


class _SyslogMsgProcID_Type(DisplayString):
    """Custom type syslogMsgProcID based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_SyslogMsgProcID_Type.__name__ = "DisplayString"
_SyslogMsgProcID_Object = MibTableColumn
syslogMsgProcID = _SyslogMsgProcID_Object(
    (1, 3, 6, 1, 2, 1, 192, 1, 2, 1, 8),
    _SyslogMsgProcID_Type()
)
syslogMsgProcID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    syslogMsgProcID.setStatus("current")


class _SyslogMsgMsgID_Type(DisplayString):
    """Custom type syslogMsgMsgID based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_SyslogMsgMsgID_Type.__name__ = "DisplayString"
_SyslogMsgMsgID_Object = MibTableColumn
syslogMsgMsgID = _SyslogMsgMsgID_Object(
    (1, 3, 6, 1, 2, 1, 192, 1, 2, 1, 9),
    _SyslogMsgMsgID_Type()
)
syslogMsgMsgID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    syslogMsgMsgID.setStatus("current")
_SyslogMsgSDParams_Type = Unsigned32
_SyslogMsgSDParams_Object = MibTableColumn
syslogMsgSDParams = _SyslogMsgSDParams_Object(
    (1, 3, 6, 1, 2, 1, 192, 1, 2, 1, 10),
    _SyslogMsgSDParams_Type()
)
syslogMsgSDParams.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    syslogMsgSDParams.setStatus("current")
_SyslogMsgMsg_Type = OctetString
_SyslogMsgMsg_Object = MibTableColumn
syslogMsgMsg = _SyslogMsgMsg_Object(
    (1, 3, 6, 1, 2, 1, 192, 1, 2, 1, 11),
    _SyslogMsgMsg_Type()
)
syslogMsgMsg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    syslogMsgMsg.setStatus("current")
_SyslogMsgSDTable_Object = MibTable
syslogMsgSDTable = _SyslogMsgSDTable_Object(
    (1, 3, 6, 1, 2, 1, 192, 1, 3)
)
if mibBuilder.loadTexts:
    syslogMsgSDTable.setStatus("current")
_SyslogMsgSDEntry_Object = MibTableRow
syslogMsgSDEntry = _SyslogMsgSDEntry_Object(
    (1, 3, 6, 1, 2, 1, 192, 1, 3, 1)
)
syslogMsgSDEntry.setIndexNames(
    (0, "SYSLOG-MSG-MIB", "syslogMsgIndex"),
    (0, "SYSLOG-MSG-MIB", "syslogMsgSDParamIndex"),
    (0, "SYSLOG-MSG-MIB", "syslogMsgSDID"),
    (0, "SYSLOG-MSG-MIB", "syslogMsgSDParamName"),
)
if mibBuilder.loadTexts:
    syslogMsgSDEntry.setStatus("current")


class _SyslogMsgSDParamIndex_Type(Unsigned32):
    """Custom type syslogMsgSDParamIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_SyslogMsgSDParamIndex_Type.__name__ = "Unsigned32"
_SyslogMsgSDParamIndex_Object = MibTableColumn
syslogMsgSDParamIndex = _SyslogMsgSDParamIndex_Object(
    (1, 3, 6, 1, 2, 1, 192, 1, 3, 1, 1),
    _SyslogMsgSDParamIndex_Type()
)
syslogMsgSDParamIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    syslogMsgSDParamIndex.setStatus("current")


class _SyslogMsgSDID_Type(DisplayString):
    """Custom type syslogMsgSDID based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_SyslogMsgSDID_Type.__name__ = "DisplayString"
_SyslogMsgSDID_Object = MibTableColumn
syslogMsgSDID = _SyslogMsgSDID_Object(
    (1, 3, 6, 1, 2, 1, 192, 1, 3, 1, 2),
    _SyslogMsgSDID_Type()
)
syslogMsgSDID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    syslogMsgSDID.setStatus("current")


class _SyslogMsgSDParamName_Type(DisplayString):
    """Custom type syslogMsgSDParamName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_SyslogMsgSDParamName_Type.__name__ = "DisplayString"
_SyslogMsgSDParamName_Object = MibTableColumn
syslogMsgSDParamName = _SyslogMsgSDParamName_Object(
    (1, 3, 6, 1, 2, 1, 192, 1, 3, 1, 3),
    _SyslogMsgSDParamName_Type()
)
syslogMsgSDParamName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    syslogMsgSDParamName.setStatus("current")
_SyslogMsgSDParamValue_Type = SyslogParamValueString
_SyslogMsgSDParamValue_Object = MibTableColumn
syslogMsgSDParamValue = _SyslogMsgSDParamValue_Object(
    (1, 3, 6, 1, 2, 1, 192, 1, 3, 1, 4),
    _SyslogMsgSDParamValue_Type()
)
syslogMsgSDParamValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    syslogMsgSDParamValue.setStatus("current")
_SyslogMsgConformance_ObjectIdentity = ObjectIdentity
syslogMsgConformance = _SyslogMsgConformance_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 192, 2)
)
_SyslogMsgGroups_ObjectIdentity = ObjectIdentity
syslogMsgGroups = _SyslogMsgGroups_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 192, 2, 1)
)
_SyslogMsgCompliances_ObjectIdentity = ObjectIdentity
syslogMsgCompliances = _SyslogMsgCompliances_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 192, 2, 2)
)

# Managed Objects groups

syslogMsgGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 192, 2, 1, 2)
)
syslogMsgGroup.setObjects(
      *(("SYSLOG-MSG-MIB", "syslogMsgFacility"),
        ("SYSLOG-MSG-MIB", "syslogMsgSeverity"),
        ("SYSLOG-MSG-MIB", "syslogMsgVersion"),
        ("SYSLOG-MSG-MIB", "syslogMsgTimeStamp"),
        ("SYSLOG-MSG-MIB", "syslogMsgHostName"),
        ("SYSLOG-MSG-MIB", "syslogMsgAppName"),
        ("SYSLOG-MSG-MIB", "syslogMsgProcID"),
        ("SYSLOG-MSG-MIB", "syslogMsgMsgID"),
        ("SYSLOG-MSG-MIB", "syslogMsgSDParams"),
        ("SYSLOG-MSG-MIB", "syslogMsgMsg"))
)
if mibBuilder.loadTexts:
    syslogMsgGroup.setStatus("current")

syslogMsgSDGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 192, 2, 1, 3)
)
syslogMsgSDGroup.setObjects(
    ("SYSLOG-MSG-MIB", "syslogMsgSDParamValue")
)
if mibBuilder.loadTexts:
    syslogMsgSDGroup.setStatus("current")

syslogMsgControlGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 192, 2, 1, 4)
)
syslogMsgControlGroup.setObjects(
      *(("SYSLOG-MSG-MIB", "syslogMsgTableMaxSize"),
        ("SYSLOG-MSG-MIB", "syslogMsgEnableNotifications"))
)
if mibBuilder.loadTexts:
    syslogMsgControlGroup.setStatus("current")


# Notification objects

syslogMsgNotification = NotificationType(
    (1, 3, 6, 1, 2, 1, 192, 0, 1)
)
syslogMsgNotification.setObjects(
      *(("SYSLOG-MSG-MIB", "syslogMsgFacility"),
        ("SYSLOG-MSG-MIB", "syslogMsgSeverity"),
        ("SYSLOG-MSG-MIB", "syslogMsgVersion"),
        ("SYSLOG-MSG-MIB", "syslogMsgTimeStamp"),
        ("SYSLOG-MSG-MIB", "syslogMsgHostName"),
        ("SYSLOG-MSG-MIB", "syslogMsgAppName"),
        ("SYSLOG-MSG-MIB", "syslogMsgProcID"),
        ("SYSLOG-MSG-MIB", "syslogMsgMsgID"),
        ("SYSLOG-MSG-MIB", "syslogMsgSDParams"),
        ("SYSLOG-MSG-MIB", "syslogMsgMsg"))
)
if mibBuilder.loadTexts:
    syslogMsgNotification.setStatus(
        "current"
    )


# Notifications groups

syslogMsgNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 2, 1, 192, 2, 1, 1)
)
syslogMsgNotificationGroup.setObjects(
    ("SYSLOG-MSG-MIB", "syslogMsgNotification")
)
if mibBuilder.loadTexts:
    syslogMsgNotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

syslogMsgFullCompliance = ModuleCompliance(
    (1, 3, 6, 1, 2, 1, 192, 2, 2, 1)
)
if mibBuilder.loadTexts:
    syslogMsgFullCompliance.setStatus(
        "current"
    )

syslogMsgReadOnlyCompliance = ModuleCompliance(
    (1, 3, 6, 1, 2, 1, 192, 2, 2, 2)
)
if mibBuilder.loadTexts:
    syslogMsgReadOnlyCompliance.setStatus(
        "current"
    )

syslogMsgNotificationCompliance = ModuleCompliance(
    (1, 3, 6, 1, 2, 1, 192, 2, 2, 3)
)
if mibBuilder.loadTexts:
    syslogMsgNotificationCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SYSLOG-MSG-MIB",
    **{"SyslogTimeStamp": SyslogTimeStamp,
       "SyslogParamValueString": SyslogParamValueString,
       "syslogMsgMib": syslogMsgMib,
       "syslogMsgNotifications": syslogMsgNotifications,
       "syslogMsgNotification": syslogMsgNotification,
       "syslogMsgObjects": syslogMsgObjects,
       "syslogMsgControl": syslogMsgControl,
       "syslogMsgTableMaxSize": syslogMsgTableMaxSize,
       "syslogMsgEnableNotifications": syslogMsgEnableNotifications,
       "syslogMsgTable": syslogMsgTable,
       "syslogMsgEntry": syslogMsgEntry,
       "syslogMsgIndex": syslogMsgIndex,
       "syslogMsgFacility": syslogMsgFacility,
       "syslogMsgSeverity": syslogMsgSeverity,
       "syslogMsgVersion": syslogMsgVersion,
       "syslogMsgTimeStamp": syslogMsgTimeStamp,
       "syslogMsgHostName": syslogMsgHostName,
       "syslogMsgAppName": syslogMsgAppName,
       "syslogMsgProcID": syslogMsgProcID,
       "syslogMsgMsgID": syslogMsgMsgID,
       "syslogMsgSDParams": syslogMsgSDParams,
       "syslogMsgMsg": syslogMsgMsg,
       "syslogMsgSDTable": syslogMsgSDTable,
       "syslogMsgSDEntry": syslogMsgSDEntry,
       "syslogMsgSDParamIndex": syslogMsgSDParamIndex,
       "syslogMsgSDID": syslogMsgSDID,
       "syslogMsgSDParamName": syslogMsgSDParamName,
       "syslogMsgSDParamValue": syslogMsgSDParamValue,
       "syslogMsgConformance": syslogMsgConformance,
       "syslogMsgGroups": syslogMsgGroups,
       "syslogMsgNotificationGroup": syslogMsgNotificationGroup,
       "syslogMsgGroup": syslogMsgGroup,
       "syslogMsgSDGroup": syslogMsgSDGroup,
       "syslogMsgControlGroup": syslogMsgControlGroup,
       "syslogMsgCompliances": syslogMsgCompliances,
       "syslogMsgFullCompliance": syslogMsgFullCompliance,
       "syslogMsgReadOnlyCompliance": syslogMsgReadOnlyCompliance,
       "syslogMsgNotificationCompliance": syslogMsgNotificationCompliance}
)
