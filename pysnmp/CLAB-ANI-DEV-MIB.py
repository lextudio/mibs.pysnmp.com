# SNMP MIB module (CLAB-ANI-DEV-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CLAB-ANI-DEV-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:15:36 2024
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

(clabCommonMibs,) = mibBuilder.importSymbols(
    "CLAB-DEF-MIB",
    "clabCommonMibs")

(SnmpAdminString,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString")

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


# MODULE-IDENTITY

clabAniDevMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 4, 7)
)
clabAniDevMib.setRevisions(
        ("2017-04-27 00:00",
         "2017-02-21 00:00",
         "2016-05-19 00:00",
         "2016-03-17 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_ClabAniDevObjects_ObjectIdentity = ObjectIdentity
clabAniDevObjects = _ClabAniDevObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 4, 7, 1)
)
_AniDevResetNow_Type = TruthValue
_AniDevResetNow_Object = MibScalar
aniDevResetNow = _AniDevResetNow_Object(
    (1, 3, 6, 1, 4, 1, 4491, 4, 7, 1, 1),
    _AniDevResetNow_Type()
)
aniDevResetNow.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aniDevResetNow.setStatus("current")
_ClabAniDevSysLoggingObjects_ObjectIdentity = ObjectIdentity
clabAniDevSysLoggingObjects = _ClabAniDevSysLoggingObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 4, 7, 1, 2)
)


class _AniDevLoggingCtrlReset_Type(Integer32):
    """Custom type aniDevLoggingCtrlReset based on Integer32"""
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
        *(("pauseLog", 2),
          ("resetLog", 1),
          ("startLog", 3),
          ("useDefaultReporting", 4))
    )


_AniDevLoggingCtrlReset_Type.__name__ = "Integer32"
_AniDevLoggingCtrlReset_Object = MibScalar
aniDevLoggingCtrlReset = _AniDevLoggingCtrlReset_Object(
    (1, 3, 6, 1, 4, 1, 4491, 4, 7, 1, 2, 1),
    _AniDevLoggingCtrlReset_Type()
)
aniDevLoggingCtrlReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aniDevLoggingCtrlReset.setStatus("current")
_AniDevSysLoggingSize_Type = Unsigned32
_AniDevSysLoggingSize_Object = MibScalar
aniDevSysLoggingSize = _AniDevSysLoggingSize_Object(
    (1, 3, 6, 1, 4, 1, 4491, 4, 7, 1, 2, 2),
    _AniDevSysLoggingSize_Type()
)
aniDevSysLoggingSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aniDevSysLoggingSize.setStatus("current")
if mibBuilder.loadTexts:
    aniDevSysLoggingSize.setUnits("bytes")


class _AniDevSysLoggingLevelCtrl_Type(Integer32):
    """Custom type aniDevSysLoggingLevelCtrl based on Integer32"""
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
        *(("all", 1),
          ("debug", 3),
          ("error", 6),
          ("fatal", 7),
          ("info", 4),
          ("off", 8),
          ("trace", 2),
          ("warn", 5))
    )


_AniDevSysLoggingLevelCtrl_Type.__name__ = "Integer32"
_AniDevSysLoggingLevelCtrl_Object = MibScalar
aniDevSysLoggingLevelCtrl = _AniDevSysLoggingLevelCtrl_Object(
    (1, 3, 6, 1, 4, 1, 4491, 4, 7, 1, 2, 3),
    _AniDevSysLoggingLevelCtrl_Type()
)
aniDevSysLoggingLevelCtrl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aniDevSysLoggingLevelCtrl.setStatus("current")


class _AniDevSysLoggingGroupCtrl_Type(Bits):
    """Custom type aniDevSysLoggingGroupCtrl based on Bits"""
    defaultBinValue = "1"

    namedValues = NamedValues(
        *(("all", 1),
          ("group1", 2),
          ("group2", 3),
          ("group3", 4),
          ("group4", 5),
          ("group5", 6),
          ("none", 0))
    )

_AniDevSysLoggingGroupCtrl_Type.__name__ = "Bits"
_AniDevSysLoggingGroupCtrl_Object = MibScalar
aniDevSysLoggingGroupCtrl = _AniDevSysLoggingGroupCtrl_Object(
    (1, 3, 6, 1, 4, 1, 4491, 4, 7, 1, 2, 4),
    _AniDevSysLoggingGroupCtrl_Type()
)
aniDevSysLoggingGroupCtrl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aniDevSysLoggingGroupCtrl.setStatus("current")
_AniDevSysLoggingEventTable_Object = MibTable
aniDevSysLoggingEventTable = _AniDevSysLoggingEventTable_Object(
    (1, 3, 6, 1, 4, 1, 4491, 4, 7, 1, 2, 5)
)
if mibBuilder.loadTexts:
    aniDevSysLoggingEventTable.setStatus("current")
_AniDevSysLoggingEventEntry_Object = MibTableRow
aniDevSysLoggingEventEntry = _AniDevSysLoggingEventEntry_Object(
    (1, 3, 6, 1, 4, 1, 4491, 4, 7, 1, 2, 5, 1)
)
aniDevSysLoggingEventEntry.setIndexNames(
    (0, "CLAB-ANI-DEV-MIB", "aniDevSysLoggingEventIndex"),
)
if mibBuilder.loadTexts:
    aniDevSysLoggingEventEntry.setStatus("current")
_AniDevSysLoggingEventIndex_Type = Unsigned32
_AniDevSysLoggingEventIndex_Object = MibTableColumn
aniDevSysLoggingEventIndex = _AniDevSysLoggingEventIndex_Object(
    (1, 3, 6, 1, 4, 1, 4491, 4, 7, 1, 2, 5, 1, 1),
    _AniDevSysLoggingEventIndex_Type()
)
aniDevSysLoggingEventIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    aniDevSysLoggingEventIndex.setStatus("current")
_AniDevSysLoggingEventTimeStamp_Type = DateAndTime
_AniDevSysLoggingEventTimeStamp_Object = MibTableColumn
aniDevSysLoggingEventTimeStamp = _AniDevSysLoggingEventTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 4491, 4, 7, 1, 2, 5, 1, 2),
    _AniDevSysLoggingEventTimeStamp_Type()
)
aniDevSysLoggingEventTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aniDevSysLoggingEventTimeStamp.setStatus("current")
_AniDevSysLoggingEventMessage_Type = SnmpAdminString
_AniDevSysLoggingEventMessage_Object = MibTableColumn
aniDevSysLoggingEventMessage = _AniDevSysLoggingEventMessage_Object(
    (1, 3, 6, 1, 4, 1, 4491, 4, 7, 1, 2, 5, 1, 3),
    _AniDevSysLoggingEventMessage_Type()
)
aniDevSysLoggingEventMessage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aniDevSysLoggingEventMessage.setStatus("current")
_ClabAniDevConformance_ObjectIdentity = ObjectIdentity
clabAniDevConformance = _ClabAniDevConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 4, 7, 2)
)
_ClabAniDevCompliances_ObjectIdentity = ObjectIdentity
clabAniDevCompliances = _ClabAniDevCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 4, 7, 2, 1)
)
_ClabAniDevGroups_ObjectIdentity = ObjectIdentity
clabAniDevGroups = _ClabAniDevGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 4, 7, 2, 2)
)

# Managed Objects groups

clabAniDevGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4491, 4, 7, 2, 2, 1)
)
clabAniDevGroup.setObjects(
      *(("CLAB-ANI-DEV-MIB", "aniDevResetNow"),
        ("CLAB-ANI-DEV-MIB", "aniDevLoggingCtrlReset"),
        ("CLAB-ANI-DEV-MIB", "aniDevSysLoggingSize"),
        ("CLAB-ANI-DEV-MIB", "aniDevSysLoggingLevelCtrl"),
        ("CLAB-ANI-DEV-MIB", "aniDevSysLoggingGroupCtrl"),
        ("CLAB-ANI-DEV-MIB", "aniDevSysLoggingEventTimeStamp"),
        ("CLAB-ANI-DEV-MIB", "aniDevSysLoggingEventMessage"))
)
if mibBuilder.loadTexts:
    clabAniDevGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

clabAniDevCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4491, 4, 7, 2, 1, 1)
)
if mibBuilder.loadTexts:
    clabAniDevCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CLAB-ANI-DEV-MIB",
    **{"clabAniDevMib": clabAniDevMib,
       "clabAniDevObjects": clabAniDevObjects,
       "aniDevResetNow": aniDevResetNow,
       "clabAniDevSysLoggingObjects": clabAniDevSysLoggingObjects,
       "aniDevLoggingCtrlReset": aniDevLoggingCtrlReset,
       "aniDevSysLoggingSize": aniDevSysLoggingSize,
       "aniDevSysLoggingLevelCtrl": aniDevSysLoggingLevelCtrl,
       "aniDevSysLoggingGroupCtrl": aniDevSysLoggingGroupCtrl,
       "aniDevSysLoggingEventTable": aniDevSysLoggingEventTable,
       "aniDevSysLoggingEventEntry": aniDevSysLoggingEventEntry,
       "aniDevSysLoggingEventIndex": aniDevSysLoggingEventIndex,
       "aniDevSysLoggingEventTimeStamp": aniDevSysLoggingEventTimeStamp,
       "aniDevSysLoggingEventMessage": aniDevSysLoggingEventMessage,
       "clabAniDevConformance": clabAniDevConformance,
       "clabAniDevCompliances": clabAniDevCompliances,
       "clabAniDevCompliance": clabAniDevCompliance,
       "clabAniDevGroups": clabAniDevGroups,
       "clabAniDevGroup": clabAniDevGroup}
)
