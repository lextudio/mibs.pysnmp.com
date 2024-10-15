# SNMP MIB module (HP-OPENCALL-SS7SNMPAGENT-BASE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HP-OPENCALL-SS7SNMPAGENT-BASE-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:58:37 2024
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

openCall = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 29, 2)
)
openCall.setRevisions(
        ("2004-09-09 00:00",
         "2003-09-09 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_OpenCallTraps_ObjectIdentity = ObjectIdentity
openCallTraps = _OpenCallTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 29, 2, 0)
)
_SourcePlatformEntity_Type = DisplayString
_SourcePlatformEntity_Object = MibScalar
sourcePlatformEntity = _SourcePlatformEntity_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 29, 2, 0, 1),
    _SourcePlatformEntity_Type()
)
sourcePlatformEntity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sourcePlatformEntity.setStatus("current")
_SourceObjectID_Type = DisplayString
_SourceObjectID_Object = MibScalar
sourceObjectID = _SourceObjectID_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 29, 2, 0, 2),
    _SourceObjectID_Type()
)
sourceObjectID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sourceObjectID.setStatus("current")
_PerceveidSeverity_Type = DisplayString
_PerceveidSeverity_Object = MibScalar
perceveidSeverity = _PerceveidSeverity_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 29, 2, 0, 3),
    _PerceveidSeverity_Type()
)
perceveidSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    perceveidSeverity.setStatus("current")
_AlarmText_Type = DisplayString
_AlarmText_Object = MibScalar
alarmText = _AlarmText_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 29, 2, 0, 4),
    _AlarmText_Type()
)
alarmText.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmText.setStatus("current")
_ProbableCause_Type = DisplayString
_ProbableCause_Object = MibScalar
probableCause = _ProbableCause_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 29, 2, 0, 5),
    _ProbableCause_Type()
)
probableCause.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    probableCause.setStatus("current")
_CorrectiveAction_Type = DisplayString
_CorrectiveAction_Object = MibScalar
correctiveAction = _CorrectiveAction_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 29, 2, 0, 6),
    _CorrectiveAction_Type()
)
correctiveAction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    correctiveAction.setStatus("current")
_HtimeStamp_Type = DisplayString
_HtimeStamp_Object = MibScalar
htimeStamp = _HtimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 29, 2, 0, 7),
    _HtimeStamp_Type()
)
htimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    htimeStamp.setStatus("current")

# Managed Objects groups


# Notification objects

hHPOC_3100155 = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 29, 2, 0, 3100155)
)
hHPOC_3100155.setObjects(
      *(("HP-OPENCALL-SS7SNMPAGENT-BASE-MIB", "sourcePlatformEntity"),
        ("HP-OPENCALL-SS7SNMPAGENT-BASE-MIB", "sourceObjectID"),
        ("HP-OPENCALL-SS7SNMPAGENT-BASE-MIB", "perceveidSeverity"),
        ("HP-OPENCALL-SS7SNMPAGENT-BASE-MIB", "alarmText"),
        ("HP-OPENCALL-SS7SNMPAGENT-BASE-MIB", "probableCause"),
        ("HP-OPENCALL-SS7SNMPAGENT-BASE-MIB", "correctiveAction"),
        ("HP-OPENCALL-SS7SNMPAGENT-BASE-MIB", "htimeStamp"))
)
if mibBuilder.loadTexts:
    hHPOC_3100155.setStatus(
        "current"
    )

hHPOC_8400042 = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 29, 2, 0, 8400042)
)
hHPOC_8400042.setObjects(
      *(("HP-OPENCALL-SS7SNMPAGENT-BASE-MIB", "sourcePlatformEntity"),
        ("HP-OPENCALL-SS7SNMPAGENT-BASE-MIB", "sourceObjectID"),
        ("HP-OPENCALL-SS7SNMPAGENT-BASE-MIB", "perceveidSeverity"),
        ("HP-OPENCALL-SS7SNMPAGENT-BASE-MIB", "alarmText"),
        ("HP-OPENCALL-SS7SNMPAGENT-BASE-MIB", "probableCause"),
        ("HP-OPENCALL-SS7SNMPAGENT-BASE-MIB", "correctiveAction"),
        ("HP-OPENCALL-SS7SNMPAGENT-BASE-MIB", "htimeStamp"))
)
if mibBuilder.loadTexts:
    hHPOC_8400042.setStatus(
        "current"
    )

hHPOC_8400084 = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 29, 2, 0, 8400084)
)
hHPOC_8400084.setObjects(
      *(("HP-OPENCALL-SS7SNMPAGENT-BASE-MIB", "sourcePlatformEntity"),
        ("HP-OPENCALL-SS7SNMPAGENT-BASE-MIB", "sourceObjectID"),
        ("HP-OPENCALL-SS7SNMPAGENT-BASE-MIB", "perceveidSeverity"),
        ("HP-OPENCALL-SS7SNMPAGENT-BASE-MIB", "alarmText"),
        ("HP-OPENCALL-SS7SNMPAGENT-BASE-MIB", "probableCause"),
        ("HP-OPENCALL-SS7SNMPAGENT-BASE-MIB", "correctiveAction"),
        ("HP-OPENCALL-SS7SNMPAGENT-BASE-MIB", "htimeStamp"))
)
if mibBuilder.loadTexts:
    hHPOC_8400084.setStatus(
        "current"
    )

hHPOC_8400085 = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 29, 2, 0, 8400085)
)
hHPOC_8400085.setObjects(
      *(("HP-OPENCALL-SS7SNMPAGENT-BASE-MIB", "sourcePlatformEntity"),
        ("HP-OPENCALL-SS7SNMPAGENT-BASE-MIB", "sourceObjectID"),
        ("HP-OPENCALL-SS7SNMPAGENT-BASE-MIB", "perceveidSeverity"),
        ("HP-OPENCALL-SS7SNMPAGENT-BASE-MIB", "alarmText"),
        ("HP-OPENCALL-SS7SNMPAGENT-BASE-MIB", "probableCause"),
        ("HP-OPENCALL-SS7SNMPAGENT-BASE-MIB", "correctiveAction"),
        ("HP-OPENCALL-SS7SNMPAGENT-BASE-MIB", "htimeStamp"))
)
if mibBuilder.loadTexts:
    hHPOC_8400085.setStatus(
        "current"
    )

hHPOC_8400086 = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 29, 2, 0, 8400086)
)
hHPOC_8400086.setObjects(
      *(("HP-OPENCALL-SS7SNMPAGENT-BASE-MIB", "sourcePlatformEntity"),
        ("HP-OPENCALL-SS7SNMPAGENT-BASE-MIB", "sourceObjectID"),
        ("HP-OPENCALL-SS7SNMPAGENT-BASE-MIB", "perceveidSeverity"),
        ("HP-OPENCALL-SS7SNMPAGENT-BASE-MIB", "alarmText"),
        ("HP-OPENCALL-SS7SNMPAGENT-BASE-MIB", "probableCause"),
        ("HP-OPENCALL-SS7SNMPAGENT-BASE-MIB", "correctiveAction"),
        ("HP-OPENCALL-SS7SNMPAGENT-BASE-MIB", "htimeStamp"))
)
if mibBuilder.loadTexts:
    hHPOC_8400086.setStatus(
        "current"
    )

hHPOC_8400087 = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 29, 2, 0, 8400087)
)
hHPOC_8400087.setObjects(
      *(("HP-OPENCALL-SS7SNMPAGENT-BASE-MIB", "sourcePlatformEntity"),
        ("HP-OPENCALL-SS7SNMPAGENT-BASE-MIB", "sourceObjectID"),
        ("HP-OPENCALL-SS7SNMPAGENT-BASE-MIB", "perceveidSeverity"),
        ("HP-OPENCALL-SS7SNMPAGENT-BASE-MIB", "alarmText"),
        ("HP-OPENCALL-SS7SNMPAGENT-BASE-MIB", "probableCause"),
        ("HP-OPENCALL-SS7SNMPAGENT-BASE-MIB", "correctiveAction"),
        ("HP-OPENCALL-SS7SNMPAGENT-BASE-MIB", "htimeStamp"))
)
if mibBuilder.loadTexts:
    hHPOC_8400087.setStatus(
        "current"
    )

hHPOC_8400088 = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 29, 2, 0, 8400088)
)
hHPOC_8400088.setObjects(
      *(("HP-OPENCALL-SS7SNMPAGENT-BASE-MIB", "sourcePlatformEntity"),
        ("HP-OPENCALL-SS7SNMPAGENT-BASE-MIB", "sourceObjectID"),
        ("HP-OPENCALL-SS7SNMPAGENT-BASE-MIB", "perceveidSeverity"),
        ("HP-OPENCALL-SS7SNMPAGENT-BASE-MIB", "alarmText"),
        ("HP-OPENCALL-SS7SNMPAGENT-BASE-MIB", "probableCause"),
        ("HP-OPENCALL-SS7SNMPAGENT-BASE-MIB", "correctiveAction"),
        ("HP-OPENCALL-SS7SNMPAGENT-BASE-MIB", "htimeStamp"))
)
if mibBuilder.loadTexts:
    hHPOC_8400088.setStatus(
        "current"
    )

hHPOC_8400089 = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 29, 2, 0, 8400089)
)
hHPOC_8400089.setObjects(
      *(("HP-OPENCALL-SS7SNMPAGENT-BASE-MIB", "sourcePlatformEntity"),
        ("HP-OPENCALL-SS7SNMPAGENT-BASE-MIB", "sourceObjectID"),
        ("HP-OPENCALL-SS7SNMPAGENT-BASE-MIB", "perceveidSeverity"),
        ("HP-OPENCALL-SS7SNMPAGENT-BASE-MIB", "alarmText"),
        ("HP-OPENCALL-SS7SNMPAGENT-BASE-MIB", "probableCause"),
        ("HP-OPENCALL-SS7SNMPAGENT-BASE-MIB", "correctiveAction"),
        ("HP-OPENCALL-SS7SNMPAGENT-BASE-MIB", "htimeStamp"))
)
if mibBuilder.loadTexts:
    hHPOC_8400089.setStatus(
        "current"
    )

hHPOC_9000332 = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 29, 2, 0, 9000332)
)
hHPOC_9000332.setObjects(
      *(("HP-OPENCALL-SS7SNMPAGENT-BASE-MIB", "sourcePlatformEntity"),
        ("HP-OPENCALL-SS7SNMPAGENT-BASE-MIB", "sourceObjectID"),
        ("HP-OPENCALL-SS7SNMPAGENT-BASE-MIB", "perceveidSeverity"),
        ("HP-OPENCALL-SS7SNMPAGENT-BASE-MIB", "alarmText"),
        ("HP-OPENCALL-SS7SNMPAGENT-BASE-MIB", "probableCause"),
        ("HP-OPENCALL-SS7SNMPAGENT-BASE-MIB", "correctiveAction"),
        ("HP-OPENCALL-SS7SNMPAGENT-BASE-MIB", "htimeStamp"))
)
if mibBuilder.loadTexts:
    hHPOC_9000332.setStatus(
        "current"
    )

hHPOC_9000334 = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 29, 2, 0, 9000334)
)
hHPOC_9000334.setObjects(
      *(("HP-OPENCALL-SS7SNMPAGENT-BASE-MIB", "sourcePlatformEntity"),
        ("HP-OPENCALL-SS7SNMPAGENT-BASE-MIB", "sourceObjectID"),
        ("HP-OPENCALL-SS7SNMPAGENT-BASE-MIB", "perceveidSeverity"),
        ("HP-OPENCALL-SS7SNMPAGENT-BASE-MIB", "alarmText"),
        ("HP-OPENCALL-SS7SNMPAGENT-BASE-MIB", "probableCause"),
        ("HP-OPENCALL-SS7SNMPAGENT-BASE-MIB", "correctiveAction"),
        ("HP-OPENCALL-SS7SNMPAGENT-BASE-MIB", "htimeStamp"))
)
if mibBuilder.loadTexts:
    hHPOC_9000334.setStatus(
        "current"
    )

hHPOC_9000336 = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 29, 2, 0, 9000336)
)
hHPOC_9000336.setObjects(
      *(("HP-OPENCALL-SS7SNMPAGENT-BASE-MIB", "sourcePlatformEntity"),
        ("HP-OPENCALL-SS7SNMPAGENT-BASE-MIB", "sourceObjectID"),
        ("HP-OPENCALL-SS7SNMPAGENT-BASE-MIB", "perceveidSeverity"),
        ("HP-OPENCALL-SS7SNMPAGENT-BASE-MIB", "alarmText"),
        ("HP-OPENCALL-SS7SNMPAGENT-BASE-MIB", "probableCause"),
        ("HP-OPENCALL-SS7SNMPAGENT-BASE-MIB", "correctiveAction"),
        ("HP-OPENCALL-SS7SNMPAGENT-BASE-MIB", "htimeStamp"))
)
if mibBuilder.loadTexts:
    hHPOC_9000336.setStatus(
        "current"
    )

hHPOC_9000341 = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 29, 2, 0, 9000341)
)
hHPOC_9000341.setObjects(
      *(("HP-OPENCALL-SS7SNMPAGENT-BASE-MIB", "sourcePlatformEntity"),
        ("HP-OPENCALL-SS7SNMPAGENT-BASE-MIB", "sourceObjectID"),
        ("HP-OPENCALL-SS7SNMPAGENT-BASE-MIB", "perceveidSeverity"),
        ("HP-OPENCALL-SS7SNMPAGENT-BASE-MIB", "alarmText"),
        ("HP-OPENCALL-SS7SNMPAGENT-BASE-MIB", "probableCause"),
        ("HP-OPENCALL-SS7SNMPAGENT-BASE-MIB", "correctiveAction"),
        ("HP-OPENCALL-SS7SNMPAGENT-BASE-MIB", "htimeStamp"))
)
if mibBuilder.loadTexts:
    hHPOC_9000341.setStatus(
        "current"
    )

hHPOC_9000342 = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 29, 2, 0, 9000342)
)
hHPOC_9000342.setObjects(
      *(("HP-OPENCALL-SS7SNMPAGENT-BASE-MIB", "sourcePlatformEntity"),
        ("HP-OPENCALL-SS7SNMPAGENT-BASE-MIB", "sourceObjectID"),
        ("HP-OPENCALL-SS7SNMPAGENT-BASE-MIB", "perceveidSeverity"),
        ("HP-OPENCALL-SS7SNMPAGENT-BASE-MIB", "alarmText"),
        ("HP-OPENCALL-SS7SNMPAGENT-BASE-MIB", "probableCause"),
        ("HP-OPENCALL-SS7SNMPAGENT-BASE-MIB", "correctiveAction"),
        ("HP-OPENCALL-SS7SNMPAGENT-BASE-MIB", "htimeStamp"))
)
if mibBuilder.loadTexts:
    hHPOC_9000342.setStatus(
        "current"
    )

hHPOC_9000343 = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 29, 2, 0, 9000343)
)
hHPOC_9000343.setObjects(
      *(("HP-OPENCALL-SS7SNMPAGENT-BASE-MIB", "sourcePlatformEntity"),
        ("HP-OPENCALL-SS7SNMPAGENT-BASE-MIB", "sourceObjectID"),
        ("HP-OPENCALL-SS7SNMPAGENT-BASE-MIB", "perceveidSeverity"),
        ("HP-OPENCALL-SS7SNMPAGENT-BASE-MIB", "alarmText"),
        ("HP-OPENCALL-SS7SNMPAGENT-BASE-MIB", "probableCause"),
        ("HP-OPENCALL-SS7SNMPAGENT-BASE-MIB", "correctiveAction"),
        ("HP-OPENCALL-SS7SNMPAGENT-BASE-MIB", "htimeStamp"))
)
if mibBuilder.loadTexts:
    hHPOC_9000343.setStatus(
        "current"
    )

hHPOC_9000344 = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 29, 2, 0, 9000344)
)
hHPOC_9000344.setObjects(
      *(("HP-OPENCALL-SS7SNMPAGENT-BASE-MIB", "sourcePlatformEntity"),
        ("HP-OPENCALL-SS7SNMPAGENT-BASE-MIB", "sourceObjectID"),
        ("HP-OPENCALL-SS7SNMPAGENT-BASE-MIB", "perceveidSeverity"),
        ("HP-OPENCALL-SS7SNMPAGENT-BASE-MIB", "alarmText"),
        ("HP-OPENCALL-SS7SNMPAGENT-BASE-MIB", "probableCause"),
        ("HP-OPENCALL-SS7SNMPAGENT-BASE-MIB", "correctiveAction"),
        ("HP-OPENCALL-SS7SNMPAGENT-BASE-MIB", "htimeStamp"))
)
if mibBuilder.loadTexts:
    hHPOC_9000344.setStatus(
        "current"
    )

hHPOC_9000345 = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 29, 2, 0, 9000345)
)
hHPOC_9000345.setObjects(
      *(("HP-OPENCALL-SS7SNMPAGENT-BASE-MIB", "sourcePlatformEntity"),
        ("HP-OPENCALL-SS7SNMPAGENT-BASE-MIB", "sourceObjectID"),
        ("HP-OPENCALL-SS7SNMPAGENT-BASE-MIB", "perceveidSeverity"),
        ("HP-OPENCALL-SS7SNMPAGENT-BASE-MIB", "alarmText"),
        ("HP-OPENCALL-SS7SNMPAGENT-BASE-MIB", "probableCause"),
        ("HP-OPENCALL-SS7SNMPAGENT-BASE-MIB", "correctiveAction"),
        ("HP-OPENCALL-SS7SNMPAGENT-BASE-MIB", "htimeStamp"))
)
if mibBuilder.loadTexts:
    hHPOC_9000345.setStatus(
        "current"
    )

hHPOC_9000346 = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 29, 2, 0, 9000346)
)
hHPOC_9000346.setObjects(
      *(("HP-OPENCALL-SS7SNMPAGENT-BASE-MIB", "sourcePlatformEntity"),
        ("HP-OPENCALL-SS7SNMPAGENT-BASE-MIB", "sourceObjectID"),
        ("HP-OPENCALL-SS7SNMPAGENT-BASE-MIB", "perceveidSeverity"),
        ("HP-OPENCALL-SS7SNMPAGENT-BASE-MIB", "alarmText"),
        ("HP-OPENCALL-SS7SNMPAGENT-BASE-MIB", "probableCause"),
        ("HP-OPENCALL-SS7SNMPAGENT-BASE-MIB", "correctiveAction"),
        ("HP-OPENCALL-SS7SNMPAGENT-BASE-MIB", "htimeStamp"))
)
if mibBuilder.loadTexts:
    hHPOC_9000346.setStatus(
        "current"
    )

hHPOC_9000347 = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 29, 2, 0, 9000347)
)
hHPOC_9000347.setObjects(
      *(("HP-OPENCALL-SS7SNMPAGENT-BASE-MIB", "sourcePlatformEntity"),
        ("HP-OPENCALL-SS7SNMPAGENT-BASE-MIB", "sourceObjectID"),
        ("HP-OPENCALL-SS7SNMPAGENT-BASE-MIB", "perceveidSeverity"),
        ("HP-OPENCALL-SS7SNMPAGENT-BASE-MIB", "alarmText"),
        ("HP-OPENCALL-SS7SNMPAGENT-BASE-MIB", "probableCause"),
        ("HP-OPENCALL-SS7SNMPAGENT-BASE-MIB", "correctiveAction"),
        ("HP-OPENCALL-SS7SNMPAGENT-BASE-MIB", "htimeStamp"))
)
if mibBuilder.loadTexts:
    hHPOC_9000347.setStatus(
        "current"
    )

hHPOC_9000348 = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 29, 2, 0, 9000348)
)
hHPOC_9000348.setObjects(
      *(("HP-OPENCALL-SS7SNMPAGENT-BASE-MIB", "sourcePlatformEntity"),
        ("HP-OPENCALL-SS7SNMPAGENT-BASE-MIB", "sourceObjectID"),
        ("HP-OPENCALL-SS7SNMPAGENT-BASE-MIB", "perceveidSeverity"),
        ("HP-OPENCALL-SS7SNMPAGENT-BASE-MIB", "alarmText"),
        ("HP-OPENCALL-SS7SNMPAGENT-BASE-MIB", "probableCause"),
        ("HP-OPENCALL-SS7SNMPAGENT-BASE-MIB", "correctiveAction"),
        ("HP-OPENCALL-SS7SNMPAGENT-BASE-MIB", "htimeStamp"))
)
if mibBuilder.loadTexts:
    hHPOC_9000348.setStatus(
        "current"
    )

hHPOC_9000349 = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 29, 2, 0, 9000349)
)
hHPOC_9000349.setObjects(
      *(("HP-OPENCALL-SS7SNMPAGENT-BASE-MIB", "sourcePlatformEntity"),
        ("HP-OPENCALL-SS7SNMPAGENT-BASE-MIB", "sourceObjectID"),
        ("HP-OPENCALL-SS7SNMPAGENT-BASE-MIB", "perceveidSeverity"),
        ("HP-OPENCALL-SS7SNMPAGENT-BASE-MIB", "alarmText"),
        ("HP-OPENCALL-SS7SNMPAGENT-BASE-MIB", "probableCause"),
        ("HP-OPENCALL-SS7SNMPAGENT-BASE-MIB", "correctiveAction"),
        ("HP-OPENCALL-SS7SNMPAGENT-BASE-MIB", "htimeStamp"))
)
if mibBuilder.loadTexts:
    hHPOC_9000349.setStatus(
        "current"
    )

hHPOC_9000350 = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 29, 2, 0, 9000350)
)
hHPOC_9000350.setObjects(
      *(("HP-OPENCALL-SS7SNMPAGENT-BASE-MIB", "sourcePlatformEntity"),
        ("HP-OPENCALL-SS7SNMPAGENT-BASE-MIB", "sourceObjectID"),
        ("HP-OPENCALL-SS7SNMPAGENT-BASE-MIB", "perceveidSeverity"),
        ("HP-OPENCALL-SS7SNMPAGENT-BASE-MIB", "alarmText"),
        ("HP-OPENCALL-SS7SNMPAGENT-BASE-MIB", "probableCause"),
        ("HP-OPENCALL-SS7SNMPAGENT-BASE-MIB", "correctiveAction"),
        ("HP-OPENCALL-SS7SNMPAGENT-BASE-MIB", "htimeStamp"))
)
if mibBuilder.loadTexts:
    hHPOC_9000350.setStatus(
        "current"
    )

hHPOC_9000354 = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 29, 2, 0, 9000354)
)
hHPOC_9000354.setObjects(
      *(("HP-OPENCALL-SS7SNMPAGENT-BASE-MIB", "sourcePlatformEntity"),
        ("HP-OPENCALL-SS7SNMPAGENT-BASE-MIB", "sourceObjectID"),
        ("HP-OPENCALL-SS7SNMPAGENT-BASE-MIB", "perceveidSeverity"),
        ("HP-OPENCALL-SS7SNMPAGENT-BASE-MIB", "alarmText"),
        ("HP-OPENCALL-SS7SNMPAGENT-BASE-MIB", "probableCause"),
        ("HP-OPENCALL-SS7SNMPAGENT-BASE-MIB", "correctiveAction"),
        ("HP-OPENCALL-SS7SNMPAGENT-BASE-MIB", "htimeStamp"))
)
if mibBuilder.loadTexts:
    hHPOC_9000354.setStatus(
        "current"
    )

hHPOC_9000355 = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 29, 2, 0, 9000355)
)
hHPOC_9000355.setObjects(
      *(("HP-OPENCALL-SS7SNMPAGENT-BASE-MIB", "sourcePlatformEntity"),
        ("HP-OPENCALL-SS7SNMPAGENT-BASE-MIB", "sourceObjectID"),
        ("HP-OPENCALL-SS7SNMPAGENT-BASE-MIB", "perceveidSeverity"),
        ("HP-OPENCALL-SS7SNMPAGENT-BASE-MIB", "alarmText"),
        ("HP-OPENCALL-SS7SNMPAGENT-BASE-MIB", "probableCause"),
        ("HP-OPENCALL-SS7SNMPAGENT-BASE-MIB", "correctiveAction"),
        ("HP-OPENCALL-SS7SNMPAGENT-BASE-MIB", "htimeStamp"))
)
if mibBuilder.loadTexts:
    hHPOC_9000355.setStatus(
        "current"
    )

hHPOC_9000356 = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 29, 2, 0, 9000356)
)
hHPOC_9000356.setObjects(
      *(("HP-OPENCALL-SS7SNMPAGENT-BASE-MIB", "sourcePlatformEntity"),
        ("HP-OPENCALL-SS7SNMPAGENT-BASE-MIB", "sourceObjectID"),
        ("HP-OPENCALL-SS7SNMPAGENT-BASE-MIB", "perceveidSeverity"),
        ("HP-OPENCALL-SS7SNMPAGENT-BASE-MIB", "alarmText"),
        ("HP-OPENCALL-SS7SNMPAGENT-BASE-MIB", "probableCause"),
        ("HP-OPENCALL-SS7SNMPAGENT-BASE-MIB", "correctiveAction"),
        ("HP-OPENCALL-SS7SNMPAGENT-BASE-MIB", "htimeStamp"))
)
if mibBuilder.loadTexts:
    hHPOC_9000356.setStatus(
        "current"
    )

hHPOC_9000357 = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 29, 2, 0, 9000357)
)
hHPOC_9000357.setObjects(
      *(("HP-OPENCALL-SS7SNMPAGENT-BASE-MIB", "sourcePlatformEntity"),
        ("HP-OPENCALL-SS7SNMPAGENT-BASE-MIB", "sourceObjectID"),
        ("HP-OPENCALL-SS7SNMPAGENT-BASE-MIB", "perceveidSeverity"),
        ("HP-OPENCALL-SS7SNMPAGENT-BASE-MIB", "alarmText"),
        ("HP-OPENCALL-SS7SNMPAGENT-BASE-MIB", "probableCause"),
        ("HP-OPENCALL-SS7SNMPAGENT-BASE-MIB", "correctiveAction"),
        ("HP-OPENCALL-SS7SNMPAGENT-BASE-MIB", "htimeStamp"))
)
if mibBuilder.loadTexts:
    hHPOC_9000357.setStatus(
        "current"
    )

hHPOC_9000635 = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 29, 2, 0, 9000635)
)
hHPOC_9000635.setObjects(
      *(("HP-OPENCALL-SS7SNMPAGENT-BASE-MIB", "sourcePlatformEntity"),
        ("HP-OPENCALL-SS7SNMPAGENT-BASE-MIB", "sourceObjectID"),
        ("HP-OPENCALL-SS7SNMPAGENT-BASE-MIB", "perceveidSeverity"),
        ("HP-OPENCALL-SS7SNMPAGENT-BASE-MIB", "alarmText"),
        ("HP-OPENCALL-SS7SNMPAGENT-BASE-MIB", "probableCause"),
        ("HP-OPENCALL-SS7SNMPAGENT-BASE-MIB", "correctiveAction"),
        ("HP-OPENCALL-SS7SNMPAGENT-BASE-MIB", "htimeStamp"))
)
if mibBuilder.loadTexts:
    hHPOC_9000635.setStatus(
        "current"
    )

hHPOC_9000636 = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 29, 2, 0, 9000636)
)
hHPOC_9000636.setObjects(
      *(("HP-OPENCALL-SS7SNMPAGENT-BASE-MIB", "sourcePlatformEntity"),
        ("HP-OPENCALL-SS7SNMPAGENT-BASE-MIB", "sourceObjectID"),
        ("HP-OPENCALL-SS7SNMPAGENT-BASE-MIB", "perceveidSeverity"),
        ("HP-OPENCALL-SS7SNMPAGENT-BASE-MIB", "alarmText"),
        ("HP-OPENCALL-SS7SNMPAGENT-BASE-MIB", "probableCause"),
        ("HP-OPENCALL-SS7SNMPAGENT-BASE-MIB", "correctiveAction"),
        ("HP-OPENCALL-SS7SNMPAGENT-BASE-MIB", "htimeStamp"))
)
if mibBuilder.loadTexts:
    hHPOC_9000636.setStatus(
        "current"
    )

hHPOC_9000681 = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 29, 2, 0, 9000681)
)
hHPOC_9000681.setObjects(
      *(("HP-OPENCALL-SS7SNMPAGENT-BASE-MIB", "sourcePlatformEntity"),
        ("HP-OPENCALL-SS7SNMPAGENT-BASE-MIB", "sourceObjectID"),
        ("HP-OPENCALL-SS7SNMPAGENT-BASE-MIB", "perceveidSeverity"),
        ("HP-OPENCALL-SS7SNMPAGENT-BASE-MIB", "alarmText"),
        ("HP-OPENCALL-SS7SNMPAGENT-BASE-MIB", "probableCause"),
        ("HP-OPENCALL-SS7SNMPAGENT-BASE-MIB", "correctiveAction"),
        ("HP-OPENCALL-SS7SNMPAGENT-BASE-MIB", "htimeStamp"))
)
if mibBuilder.loadTexts:
    hHPOC_9000681.setStatus(
        "current"
    )

hHPOC_9000682 = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 29, 2, 0, 9000682)
)
hHPOC_9000682.setObjects(
      *(("HP-OPENCALL-SS7SNMPAGENT-BASE-MIB", "sourcePlatformEntity"),
        ("HP-OPENCALL-SS7SNMPAGENT-BASE-MIB", "sourceObjectID"),
        ("HP-OPENCALL-SS7SNMPAGENT-BASE-MIB", "perceveidSeverity"),
        ("HP-OPENCALL-SS7SNMPAGENT-BASE-MIB", "alarmText"),
        ("HP-OPENCALL-SS7SNMPAGENT-BASE-MIB", "probableCause"),
        ("HP-OPENCALL-SS7SNMPAGENT-BASE-MIB", "correctiveAction"),
        ("HP-OPENCALL-SS7SNMPAGENT-BASE-MIB", "htimeStamp"))
)
if mibBuilder.loadTexts:
    hHPOC_9000682.setStatus(
        "current"
    )

hHPOC_9001260 = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 29, 2, 0, 9001260)
)
hHPOC_9001260.setObjects(
      *(("HP-OPENCALL-SS7SNMPAGENT-BASE-MIB", "sourcePlatformEntity"),
        ("HP-OPENCALL-SS7SNMPAGENT-BASE-MIB", "sourceObjectID"),
        ("HP-OPENCALL-SS7SNMPAGENT-BASE-MIB", "perceveidSeverity"),
        ("HP-OPENCALL-SS7SNMPAGENT-BASE-MIB", "alarmText"),
        ("HP-OPENCALL-SS7SNMPAGENT-BASE-MIB", "probableCause"),
        ("HP-OPENCALL-SS7SNMPAGENT-BASE-MIB", "correctiveAction"),
        ("HP-OPENCALL-SS7SNMPAGENT-BASE-MIB", "htimeStamp"))
)
if mibBuilder.loadTexts:
    hHPOC_9001260.setStatus(
        "current"
    )

hHPOC_9001262 = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 29, 2, 0, 9001262)
)
hHPOC_9001262.setObjects(
      *(("HP-OPENCALL-SS7SNMPAGENT-BASE-MIB", "sourcePlatformEntity"),
        ("HP-OPENCALL-SS7SNMPAGENT-BASE-MIB", "sourceObjectID"),
        ("HP-OPENCALL-SS7SNMPAGENT-BASE-MIB", "perceveidSeverity"),
        ("HP-OPENCALL-SS7SNMPAGENT-BASE-MIB", "alarmText"),
        ("HP-OPENCALL-SS7SNMPAGENT-BASE-MIB", "probableCause"),
        ("HP-OPENCALL-SS7SNMPAGENT-BASE-MIB", "correctiveAction"),
        ("HP-OPENCALL-SS7SNMPAGENT-BASE-MIB", "htimeStamp"))
)
if mibBuilder.loadTexts:
    hHPOC_9001262.setStatus(
        "current"
    )

hHPOC_9001268 = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 29, 2, 0, 9001268)
)
hHPOC_9001268.setObjects(
      *(("HP-OPENCALL-SS7SNMPAGENT-BASE-MIB", "sourcePlatformEntity"),
        ("HP-OPENCALL-SS7SNMPAGENT-BASE-MIB", "sourceObjectID"),
        ("HP-OPENCALL-SS7SNMPAGENT-BASE-MIB", "perceveidSeverity"),
        ("HP-OPENCALL-SS7SNMPAGENT-BASE-MIB", "alarmText"),
        ("HP-OPENCALL-SS7SNMPAGENT-BASE-MIB", "probableCause"),
        ("HP-OPENCALL-SS7SNMPAGENT-BASE-MIB", "correctiveAction"),
        ("HP-OPENCALL-SS7SNMPAGENT-BASE-MIB", "htimeStamp"))
)
if mibBuilder.loadTexts:
    hHPOC_9001268.setStatus(
        "current"
    )

hHPOC_9001269 = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 29, 2, 0, 9001269)
)
hHPOC_9001269.setObjects(
      *(("HP-OPENCALL-SS7SNMPAGENT-BASE-MIB", "sourcePlatformEntity"),
        ("HP-OPENCALL-SS7SNMPAGENT-BASE-MIB", "sourceObjectID"),
        ("HP-OPENCALL-SS7SNMPAGENT-BASE-MIB", "perceveidSeverity"),
        ("HP-OPENCALL-SS7SNMPAGENT-BASE-MIB", "alarmText"),
        ("HP-OPENCALL-SS7SNMPAGENT-BASE-MIB", "probableCause"),
        ("HP-OPENCALL-SS7SNMPAGENT-BASE-MIB", "correctiveAction"),
        ("HP-OPENCALL-SS7SNMPAGENT-BASE-MIB", "htimeStamp"))
)
if mibBuilder.loadTexts:
    hHPOC_9001269.setStatus(
        "current"
    )

hHPOC_9001270 = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 29, 2, 0, 9001270)
)
hHPOC_9001270.setObjects(
      *(("HP-OPENCALL-SS7SNMPAGENT-BASE-MIB", "sourcePlatformEntity"),
        ("HP-OPENCALL-SS7SNMPAGENT-BASE-MIB", "sourceObjectID"),
        ("HP-OPENCALL-SS7SNMPAGENT-BASE-MIB", "perceveidSeverity"),
        ("HP-OPENCALL-SS7SNMPAGENT-BASE-MIB", "alarmText"),
        ("HP-OPENCALL-SS7SNMPAGENT-BASE-MIB", "probableCause"),
        ("HP-OPENCALL-SS7SNMPAGENT-BASE-MIB", "correctiveAction"),
        ("HP-OPENCALL-SS7SNMPAGENT-BASE-MIB", "htimeStamp"))
)
if mibBuilder.loadTexts:
    hHPOC_9001270.setStatus(
        "current"
    )

hHPOC_9001271 = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 29, 2, 0, 9001271)
)
hHPOC_9001271.setObjects(
      *(("HP-OPENCALL-SS7SNMPAGENT-BASE-MIB", "sourcePlatformEntity"),
        ("HP-OPENCALL-SS7SNMPAGENT-BASE-MIB", "sourceObjectID"),
        ("HP-OPENCALL-SS7SNMPAGENT-BASE-MIB", "perceveidSeverity"),
        ("HP-OPENCALL-SS7SNMPAGENT-BASE-MIB", "alarmText"),
        ("HP-OPENCALL-SS7SNMPAGENT-BASE-MIB", "probableCause"),
        ("HP-OPENCALL-SS7SNMPAGENT-BASE-MIB", "correctiveAction"),
        ("HP-OPENCALL-SS7SNMPAGENT-BASE-MIB", "htimeStamp"))
)
if mibBuilder.loadTexts:
    hHPOC_9001271.setStatus(
        "current"
    )

hHPOC_9001272 = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 29, 2, 0, 9001272)
)
hHPOC_9001272.setObjects(
      *(("HP-OPENCALL-SS7SNMPAGENT-BASE-MIB", "sourcePlatformEntity"),
        ("HP-OPENCALL-SS7SNMPAGENT-BASE-MIB", "sourceObjectID"),
        ("HP-OPENCALL-SS7SNMPAGENT-BASE-MIB", "perceveidSeverity"),
        ("HP-OPENCALL-SS7SNMPAGENT-BASE-MIB", "alarmText"),
        ("HP-OPENCALL-SS7SNMPAGENT-BASE-MIB", "probableCause"),
        ("HP-OPENCALL-SS7SNMPAGENT-BASE-MIB", "correctiveAction"),
        ("HP-OPENCALL-SS7SNMPAGENT-BASE-MIB", "htimeStamp"))
)
if mibBuilder.loadTexts:
    hHPOC_9001272.setStatus(
        "current"
    )

hHPOC_9001273 = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 29, 2, 0, 9001273)
)
hHPOC_9001273.setObjects(
      *(("HP-OPENCALL-SS7SNMPAGENT-BASE-MIB", "sourcePlatformEntity"),
        ("HP-OPENCALL-SS7SNMPAGENT-BASE-MIB", "sourceObjectID"),
        ("HP-OPENCALL-SS7SNMPAGENT-BASE-MIB", "perceveidSeverity"),
        ("HP-OPENCALL-SS7SNMPAGENT-BASE-MIB", "alarmText"),
        ("HP-OPENCALL-SS7SNMPAGENT-BASE-MIB", "probableCause"),
        ("HP-OPENCALL-SS7SNMPAGENT-BASE-MIB", "correctiveAction"),
        ("HP-OPENCALL-SS7SNMPAGENT-BASE-MIB", "htimeStamp"))
)
if mibBuilder.loadTexts:
    hHPOC_9001273.setStatus(
        "current"
    )

hHPOC_9001274 = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 29, 2, 0, 9001274)
)
hHPOC_9001274.setObjects(
      *(("HP-OPENCALL-SS7SNMPAGENT-BASE-MIB", "sourcePlatformEntity"),
        ("HP-OPENCALL-SS7SNMPAGENT-BASE-MIB", "sourceObjectID"),
        ("HP-OPENCALL-SS7SNMPAGENT-BASE-MIB", "perceveidSeverity"),
        ("HP-OPENCALL-SS7SNMPAGENT-BASE-MIB", "alarmText"),
        ("HP-OPENCALL-SS7SNMPAGENT-BASE-MIB", "probableCause"),
        ("HP-OPENCALL-SS7SNMPAGENT-BASE-MIB", "correctiveAction"),
        ("HP-OPENCALL-SS7SNMPAGENT-BASE-MIB", "htimeStamp"))
)
if mibBuilder.loadTexts:
    hHPOC_9001274.setStatus(
        "current"
    )

hHPOC_9001275 = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 29, 2, 0, 9001275)
)
hHPOC_9001275.setObjects(
      *(("HP-OPENCALL-SS7SNMPAGENT-BASE-MIB", "sourcePlatformEntity"),
        ("HP-OPENCALL-SS7SNMPAGENT-BASE-MIB", "sourceObjectID"),
        ("HP-OPENCALL-SS7SNMPAGENT-BASE-MIB", "perceveidSeverity"),
        ("HP-OPENCALL-SS7SNMPAGENT-BASE-MIB", "alarmText"),
        ("HP-OPENCALL-SS7SNMPAGENT-BASE-MIB", "probableCause"),
        ("HP-OPENCALL-SS7SNMPAGENT-BASE-MIB", "correctiveAction"),
        ("HP-OPENCALL-SS7SNMPAGENT-BASE-MIB", "htimeStamp"))
)
if mibBuilder.loadTexts:
    hHPOC_9001275.setStatus(
        "current"
    )

hHPOC_9001276 = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 29, 2, 0, 9001276)
)
hHPOC_9001276.setObjects(
      *(("HP-OPENCALL-SS7SNMPAGENT-BASE-MIB", "sourcePlatformEntity"),
        ("HP-OPENCALL-SS7SNMPAGENT-BASE-MIB", "sourceObjectID"),
        ("HP-OPENCALL-SS7SNMPAGENT-BASE-MIB", "perceveidSeverity"),
        ("HP-OPENCALL-SS7SNMPAGENT-BASE-MIB", "alarmText"),
        ("HP-OPENCALL-SS7SNMPAGENT-BASE-MIB", "probableCause"),
        ("HP-OPENCALL-SS7SNMPAGENT-BASE-MIB", "correctiveAction"),
        ("HP-OPENCALL-SS7SNMPAGENT-BASE-MIB", "htimeStamp"))
)
if mibBuilder.loadTexts:
    hHPOC_9001276.setStatus(
        "current"
    )

hHPOC_9001277 = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 29, 2, 0, 9001277)
)
hHPOC_9001277.setObjects(
      *(("HP-OPENCALL-SS7SNMPAGENT-BASE-MIB", "sourcePlatformEntity"),
        ("HP-OPENCALL-SS7SNMPAGENT-BASE-MIB", "sourceObjectID"),
        ("HP-OPENCALL-SS7SNMPAGENT-BASE-MIB", "perceveidSeverity"),
        ("HP-OPENCALL-SS7SNMPAGENT-BASE-MIB", "alarmText"),
        ("HP-OPENCALL-SS7SNMPAGENT-BASE-MIB", "probableCause"),
        ("HP-OPENCALL-SS7SNMPAGENT-BASE-MIB", "correctiveAction"),
        ("HP-OPENCALL-SS7SNMPAGENT-BASE-MIB", "htimeStamp"))
)
if mibBuilder.loadTexts:
    hHPOC_9001277.setStatus(
        "current"
    )

hHPOC_9001278 = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 29, 2, 0, 9001278)
)
hHPOC_9001278.setObjects(
      *(("HP-OPENCALL-SS7SNMPAGENT-BASE-MIB", "sourcePlatformEntity"),
        ("HP-OPENCALL-SS7SNMPAGENT-BASE-MIB", "sourceObjectID"),
        ("HP-OPENCALL-SS7SNMPAGENT-BASE-MIB", "perceveidSeverity"),
        ("HP-OPENCALL-SS7SNMPAGENT-BASE-MIB", "alarmText"),
        ("HP-OPENCALL-SS7SNMPAGENT-BASE-MIB", "probableCause"),
        ("HP-OPENCALL-SS7SNMPAGENT-BASE-MIB", "correctiveAction"),
        ("HP-OPENCALL-SS7SNMPAGENT-BASE-MIB", "htimeStamp"))
)
if mibBuilder.loadTexts:
    hHPOC_9001278.setStatus(
        "current"
    )

hHPOC_9001279 = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 29, 2, 0, 9001279)
)
hHPOC_9001279.setObjects(
      *(("HP-OPENCALL-SS7SNMPAGENT-BASE-MIB", "sourcePlatformEntity"),
        ("HP-OPENCALL-SS7SNMPAGENT-BASE-MIB", "sourceObjectID"),
        ("HP-OPENCALL-SS7SNMPAGENT-BASE-MIB", "perceveidSeverity"),
        ("HP-OPENCALL-SS7SNMPAGENT-BASE-MIB", "alarmText"),
        ("HP-OPENCALL-SS7SNMPAGENT-BASE-MIB", "probableCause"),
        ("HP-OPENCALL-SS7SNMPAGENT-BASE-MIB", "correctiveAction"),
        ("HP-OPENCALL-SS7SNMPAGENT-BASE-MIB", "htimeStamp"))
)
if mibBuilder.loadTexts:
    hHPOC_9001279.setStatus(
        "current"
    )

hHPOC_9001280 = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 29, 2, 0, 9001280)
)
hHPOC_9001280.setObjects(
      *(("HP-OPENCALL-SS7SNMPAGENT-BASE-MIB", "sourcePlatformEntity"),
        ("HP-OPENCALL-SS7SNMPAGENT-BASE-MIB", "sourceObjectID"),
        ("HP-OPENCALL-SS7SNMPAGENT-BASE-MIB", "perceveidSeverity"),
        ("HP-OPENCALL-SS7SNMPAGENT-BASE-MIB", "alarmText"),
        ("HP-OPENCALL-SS7SNMPAGENT-BASE-MIB", "probableCause"),
        ("HP-OPENCALL-SS7SNMPAGENT-BASE-MIB", "correctiveAction"),
        ("HP-OPENCALL-SS7SNMPAGENT-BASE-MIB", "htimeStamp"))
)
if mibBuilder.loadTexts:
    hHPOC_9001280.setStatus(
        "current"
    )

hHPOC_40100001 = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 29, 2, 0, 40100001)
)
hHPOC_40100001.setObjects(
      *(("HP-OPENCALL-SS7SNMPAGENT-BASE-MIB", "sourcePlatformEntity"),
        ("HP-OPENCALL-SS7SNMPAGENT-BASE-MIB", "sourceObjectID"),
        ("HP-OPENCALL-SS7SNMPAGENT-BASE-MIB", "perceveidSeverity"),
        ("HP-OPENCALL-SS7SNMPAGENT-BASE-MIB", "alarmText"),
        ("HP-OPENCALL-SS7SNMPAGENT-BASE-MIB", "probableCause"),
        ("HP-OPENCALL-SS7SNMPAGENT-BASE-MIB", "correctiveAction"),
        ("HP-OPENCALL-SS7SNMPAGENT-BASE-MIB", "htimeStamp"))
)
if mibBuilder.loadTexts:
    hHPOC_40100001.setStatus(
        "current"
    )

hHPOC_40100011 = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 29, 2, 0, 40100011)
)
hHPOC_40100011.setObjects(
      *(("HP-OPENCALL-SS7SNMPAGENT-BASE-MIB", "sourcePlatformEntity"),
        ("HP-OPENCALL-SS7SNMPAGENT-BASE-MIB", "sourceObjectID"),
        ("HP-OPENCALL-SS7SNMPAGENT-BASE-MIB", "perceveidSeverity"),
        ("HP-OPENCALL-SS7SNMPAGENT-BASE-MIB", "alarmText"),
        ("HP-OPENCALL-SS7SNMPAGENT-BASE-MIB", "probableCause"),
        ("HP-OPENCALL-SS7SNMPAGENT-BASE-MIB", "correctiveAction"),
        ("HP-OPENCALL-SS7SNMPAGENT-BASE-MIB", "htimeStamp"))
)
if mibBuilder.loadTexts:
    hHPOC_40100011.setStatus(
        "current"
    )

hHPOC_40100040 = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 29, 2, 0, 40100040)
)
hHPOC_40100040.setObjects(
      *(("HP-OPENCALL-SS7SNMPAGENT-BASE-MIB", "sourcePlatformEntity"),
        ("HP-OPENCALL-SS7SNMPAGENT-BASE-MIB", "sourceObjectID"),
        ("HP-OPENCALL-SS7SNMPAGENT-BASE-MIB", "perceveidSeverity"),
        ("HP-OPENCALL-SS7SNMPAGENT-BASE-MIB", "alarmText"),
        ("HP-OPENCALL-SS7SNMPAGENT-BASE-MIB", "probableCause"),
        ("HP-OPENCALL-SS7SNMPAGENT-BASE-MIB", "correctiveAction"),
        ("HP-OPENCALL-SS7SNMPAGENT-BASE-MIB", "htimeStamp"))
)
if mibBuilder.loadTexts:
    hHPOC_40100040.setStatus(
        "current"
    )

hHPOC_40100501 = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 29, 2, 0, 40100501)
)
hHPOC_40100501.setObjects(
      *(("HP-OPENCALL-SS7SNMPAGENT-BASE-MIB", "sourcePlatformEntity"),
        ("HP-OPENCALL-SS7SNMPAGENT-BASE-MIB", "sourceObjectID"),
        ("HP-OPENCALL-SS7SNMPAGENT-BASE-MIB", "perceveidSeverity"),
        ("HP-OPENCALL-SS7SNMPAGENT-BASE-MIB", "alarmText"),
        ("HP-OPENCALL-SS7SNMPAGENT-BASE-MIB", "probableCause"),
        ("HP-OPENCALL-SS7SNMPAGENT-BASE-MIB", "correctiveAction"),
        ("HP-OPENCALL-SS7SNMPAGENT-BASE-MIB", "htimeStamp"))
)
if mibBuilder.loadTexts:
    hHPOC_40100501.setStatus(
        "current"
    )

hHPOC_40100502 = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 29, 2, 0, 40100502)
)
hHPOC_40100502.setObjects(
      *(("HP-OPENCALL-SS7SNMPAGENT-BASE-MIB", "sourcePlatformEntity"),
        ("HP-OPENCALL-SS7SNMPAGENT-BASE-MIB", "sourceObjectID"),
        ("HP-OPENCALL-SS7SNMPAGENT-BASE-MIB", "perceveidSeverity"),
        ("HP-OPENCALL-SS7SNMPAGENT-BASE-MIB", "alarmText"),
        ("HP-OPENCALL-SS7SNMPAGENT-BASE-MIB", "probableCause"),
        ("HP-OPENCALL-SS7SNMPAGENT-BASE-MIB", "correctiveAction"),
        ("HP-OPENCALL-SS7SNMPAGENT-BASE-MIB", "htimeStamp"))
)
if mibBuilder.loadTexts:
    hHPOC_40100502.setStatus(
        "current"
    )

hHPOC_40100601 = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 29, 2, 0, 40100601)
)
hHPOC_40100601.setObjects(
      *(("HP-OPENCALL-SS7SNMPAGENT-BASE-MIB", "sourcePlatformEntity"),
        ("HP-OPENCALL-SS7SNMPAGENT-BASE-MIB", "sourceObjectID"),
        ("HP-OPENCALL-SS7SNMPAGENT-BASE-MIB", "perceveidSeverity"),
        ("HP-OPENCALL-SS7SNMPAGENT-BASE-MIB", "alarmText"),
        ("HP-OPENCALL-SS7SNMPAGENT-BASE-MIB", "probableCause"),
        ("HP-OPENCALL-SS7SNMPAGENT-BASE-MIB", "correctiveAction"),
        ("HP-OPENCALL-SS7SNMPAGENT-BASE-MIB", "htimeStamp"))
)
if mibBuilder.loadTexts:
    hHPOC_40100601.setStatus(
        "current"
    )

hHPOC_40100607 = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 29, 2, 0, 40100607)
)
hHPOC_40100607.setObjects(
      *(("HP-OPENCALL-SS7SNMPAGENT-BASE-MIB", "sourcePlatformEntity"),
        ("HP-OPENCALL-SS7SNMPAGENT-BASE-MIB", "sourceObjectID"),
        ("HP-OPENCALL-SS7SNMPAGENT-BASE-MIB", "perceveidSeverity"),
        ("HP-OPENCALL-SS7SNMPAGENT-BASE-MIB", "alarmText"),
        ("HP-OPENCALL-SS7SNMPAGENT-BASE-MIB", "probableCause"),
        ("HP-OPENCALL-SS7SNMPAGENT-BASE-MIB", "correctiveAction"),
        ("HP-OPENCALL-SS7SNMPAGENT-BASE-MIB", "htimeStamp"))
)
if mibBuilder.loadTexts:
    hHPOC_40100607.setStatus(
        "current"
    )

hHPOC_40100608 = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 29, 2, 0, 40100608)
)
hHPOC_40100608.setObjects(
      *(("HP-OPENCALL-SS7SNMPAGENT-BASE-MIB", "sourcePlatformEntity"),
        ("HP-OPENCALL-SS7SNMPAGENT-BASE-MIB", "sourceObjectID"),
        ("HP-OPENCALL-SS7SNMPAGENT-BASE-MIB", "perceveidSeverity"),
        ("HP-OPENCALL-SS7SNMPAGENT-BASE-MIB", "alarmText"),
        ("HP-OPENCALL-SS7SNMPAGENT-BASE-MIB", "probableCause"),
        ("HP-OPENCALL-SS7SNMPAGENT-BASE-MIB", "correctiveAction"),
        ("HP-OPENCALL-SS7SNMPAGENT-BASE-MIB", "htimeStamp"))
)
if mibBuilder.loadTexts:
    hHPOC_40100608.setStatus(
        "current"
    )

hHPOC_40100801 = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 29, 2, 0, 40100801)
)
hHPOC_40100801.setObjects(
      *(("HP-OPENCALL-SS7SNMPAGENT-BASE-MIB", "sourcePlatformEntity"),
        ("HP-OPENCALL-SS7SNMPAGENT-BASE-MIB", "sourceObjectID"),
        ("HP-OPENCALL-SS7SNMPAGENT-BASE-MIB", "perceveidSeverity"),
        ("HP-OPENCALL-SS7SNMPAGENT-BASE-MIB", "alarmText"),
        ("HP-OPENCALL-SS7SNMPAGENT-BASE-MIB", "probableCause"),
        ("HP-OPENCALL-SS7SNMPAGENT-BASE-MIB", "correctiveAction"),
        ("HP-OPENCALL-SS7SNMPAGENT-BASE-MIB", "htimeStamp"))
)
if mibBuilder.loadTexts:
    hHPOC_40100801.setStatus(
        "current"
    )

hHPOC_40100802 = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 29, 2, 0, 40100802)
)
hHPOC_40100802.setObjects(
      *(("HP-OPENCALL-SS7SNMPAGENT-BASE-MIB", "sourcePlatformEntity"),
        ("HP-OPENCALL-SS7SNMPAGENT-BASE-MIB", "sourceObjectID"),
        ("HP-OPENCALL-SS7SNMPAGENT-BASE-MIB", "perceveidSeverity"),
        ("HP-OPENCALL-SS7SNMPAGENT-BASE-MIB", "alarmText"),
        ("HP-OPENCALL-SS7SNMPAGENT-BASE-MIB", "probableCause"),
        ("HP-OPENCALL-SS7SNMPAGENT-BASE-MIB", "correctiveAction"),
        ("HP-OPENCALL-SS7SNMPAGENT-BASE-MIB", "htimeStamp"))
)
if mibBuilder.loadTexts:
    hHPOC_40100802.setStatus(
        "current"
    )

hHPOC_40100803 = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 29, 2, 0, 40100803)
)
hHPOC_40100803.setObjects(
      *(("HP-OPENCALL-SS7SNMPAGENT-BASE-MIB", "sourcePlatformEntity"),
        ("HP-OPENCALL-SS7SNMPAGENT-BASE-MIB", "sourceObjectID"),
        ("HP-OPENCALL-SS7SNMPAGENT-BASE-MIB", "perceveidSeverity"),
        ("HP-OPENCALL-SS7SNMPAGENT-BASE-MIB", "alarmText"),
        ("HP-OPENCALL-SS7SNMPAGENT-BASE-MIB", "probableCause"),
        ("HP-OPENCALL-SS7SNMPAGENT-BASE-MIB", "correctiveAction"),
        ("HP-OPENCALL-SS7SNMPAGENT-BASE-MIB", "htimeStamp"))
)
if mibBuilder.loadTexts:
    hHPOC_40100803.setStatus(
        "current"
    )

hHPOC_40100804 = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 29, 2, 0, 40100804)
)
hHPOC_40100804.setObjects(
      *(("HP-OPENCALL-SS7SNMPAGENT-BASE-MIB", "sourcePlatformEntity"),
        ("HP-OPENCALL-SS7SNMPAGENT-BASE-MIB", "sourceObjectID"),
        ("HP-OPENCALL-SS7SNMPAGENT-BASE-MIB", "perceveidSeverity"),
        ("HP-OPENCALL-SS7SNMPAGENT-BASE-MIB", "alarmText"),
        ("HP-OPENCALL-SS7SNMPAGENT-BASE-MIB", "probableCause"),
        ("HP-OPENCALL-SS7SNMPAGENT-BASE-MIB", "correctiveAction"),
        ("HP-OPENCALL-SS7SNMPAGENT-BASE-MIB", "htimeStamp"))
)
if mibBuilder.loadTexts:
    hHPOC_40100804.setStatus(
        "current"
    )

hHPOC_40100806 = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 29, 2, 0, 40100806)
)
hHPOC_40100806.setObjects(
      *(("HP-OPENCALL-SS7SNMPAGENT-BASE-MIB", "sourcePlatformEntity"),
        ("HP-OPENCALL-SS7SNMPAGENT-BASE-MIB", "sourceObjectID"),
        ("HP-OPENCALL-SS7SNMPAGENT-BASE-MIB", "perceveidSeverity"),
        ("HP-OPENCALL-SS7SNMPAGENT-BASE-MIB", "alarmText"),
        ("HP-OPENCALL-SS7SNMPAGENT-BASE-MIB", "probableCause"),
        ("HP-OPENCALL-SS7SNMPAGENT-BASE-MIB", "correctiveAction"),
        ("HP-OPENCALL-SS7SNMPAGENT-BASE-MIB", "htimeStamp"))
)
if mibBuilder.loadTexts:
    hHPOC_40100806.setStatus(
        "current"
    )

hHPOC_40100807 = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 29, 2, 0, 40100807)
)
hHPOC_40100807.setObjects(
      *(("HP-OPENCALL-SS7SNMPAGENT-BASE-MIB", "sourcePlatformEntity"),
        ("HP-OPENCALL-SS7SNMPAGENT-BASE-MIB", "sourceObjectID"),
        ("HP-OPENCALL-SS7SNMPAGENT-BASE-MIB", "perceveidSeverity"),
        ("HP-OPENCALL-SS7SNMPAGENT-BASE-MIB", "alarmText"),
        ("HP-OPENCALL-SS7SNMPAGENT-BASE-MIB", "probableCause"),
        ("HP-OPENCALL-SS7SNMPAGENT-BASE-MIB", "correctiveAction"),
        ("HP-OPENCALL-SS7SNMPAGENT-BASE-MIB", "htimeStamp"))
)
if mibBuilder.loadTexts:
    hHPOC_40100807.setStatus(
        "current"
    )

hHPOC_40100809 = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 29, 2, 0, 40100809)
)
hHPOC_40100809.setObjects(
      *(("HP-OPENCALL-SS7SNMPAGENT-BASE-MIB", "sourcePlatformEntity"),
        ("HP-OPENCALL-SS7SNMPAGENT-BASE-MIB", "sourceObjectID"),
        ("HP-OPENCALL-SS7SNMPAGENT-BASE-MIB", "perceveidSeverity"),
        ("HP-OPENCALL-SS7SNMPAGENT-BASE-MIB", "alarmText"),
        ("HP-OPENCALL-SS7SNMPAGENT-BASE-MIB", "probableCause"),
        ("HP-OPENCALL-SS7SNMPAGENT-BASE-MIB", "correctiveAction"),
        ("HP-OPENCALL-SS7SNMPAGENT-BASE-MIB", "htimeStamp"))
)
if mibBuilder.loadTexts:
    hHPOC_40100809.setStatus(
        "current"
    )

hHPOC_40100810 = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 29, 2, 0, 40100810)
)
hHPOC_40100810.setObjects(
      *(("HP-OPENCALL-SS7SNMPAGENT-BASE-MIB", "sourcePlatformEntity"),
        ("HP-OPENCALL-SS7SNMPAGENT-BASE-MIB", "sourceObjectID"),
        ("HP-OPENCALL-SS7SNMPAGENT-BASE-MIB", "perceveidSeverity"),
        ("HP-OPENCALL-SS7SNMPAGENT-BASE-MIB", "alarmText"),
        ("HP-OPENCALL-SS7SNMPAGENT-BASE-MIB", "probableCause"),
        ("HP-OPENCALL-SS7SNMPAGENT-BASE-MIB", "correctiveAction"),
        ("HP-OPENCALL-SS7SNMPAGENT-BASE-MIB", "htimeStamp"))
)
if mibBuilder.loadTexts:
    hHPOC_40100810.setStatus(
        "current"
    )

hHPOC_40300002 = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 29, 2, 0, 40300002)
)
hHPOC_40300002.setObjects(
      *(("HP-OPENCALL-SS7SNMPAGENT-BASE-MIB", "sourcePlatformEntity"),
        ("HP-OPENCALL-SS7SNMPAGENT-BASE-MIB", "sourceObjectID"),
        ("HP-OPENCALL-SS7SNMPAGENT-BASE-MIB", "perceveidSeverity"),
        ("HP-OPENCALL-SS7SNMPAGENT-BASE-MIB", "alarmText"),
        ("HP-OPENCALL-SS7SNMPAGENT-BASE-MIB", "probableCause"),
        ("HP-OPENCALL-SS7SNMPAGENT-BASE-MIB", "correctiveAction"),
        ("HP-OPENCALL-SS7SNMPAGENT-BASE-MIB", "htimeStamp"))
)
if mibBuilder.loadTexts:
    hHPOC_40300002.setStatus(
        "current"
    )

hHPOC_40300003 = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 29, 2, 0, 40300003)
)
hHPOC_40300003.setObjects(
      *(("HP-OPENCALL-SS7SNMPAGENT-BASE-MIB", "sourcePlatformEntity"),
        ("HP-OPENCALL-SS7SNMPAGENT-BASE-MIB", "sourceObjectID"),
        ("HP-OPENCALL-SS7SNMPAGENT-BASE-MIB", "perceveidSeverity"),
        ("HP-OPENCALL-SS7SNMPAGENT-BASE-MIB", "alarmText"),
        ("HP-OPENCALL-SS7SNMPAGENT-BASE-MIB", "probableCause"),
        ("HP-OPENCALL-SS7SNMPAGENT-BASE-MIB", "correctiveAction"),
        ("HP-OPENCALL-SS7SNMPAGENT-BASE-MIB", "htimeStamp"))
)
if mibBuilder.loadTexts:
    hHPOC_40300003.setStatus(
        "current"
    )

hHPOC_40300006 = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 29, 2, 0, 40300006)
)
hHPOC_40300006.setObjects(
      *(("HP-OPENCALL-SS7SNMPAGENT-BASE-MIB", "sourcePlatformEntity"),
        ("HP-OPENCALL-SS7SNMPAGENT-BASE-MIB", "sourceObjectID"),
        ("HP-OPENCALL-SS7SNMPAGENT-BASE-MIB", "perceveidSeverity"),
        ("HP-OPENCALL-SS7SNMPAGENT-BASE-MIB", "alarmText"),
        ("HP-OPENCALL-SS7SNMPAGENT-BASE-MIB", "probableCause"),
        ("HP-OPENCALL-SS7SNMPAGENT-BASE-MIB", "correctiveAction"),
        ("HP-OPENCALL-SS7SNMPAGENT-BASE-MIB", "htimeStamp"))
)
if mibBuilder.loadTexts:
    hHPOC_40300006.setStatus(
        "current"
    )

hHPOC_40400001 = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 29, 2, 0, 40400001)
)
hHPOC_40400001.setObjects(
      *(("HP-OPENCALL-SS7SNMPAGENT-BASE-MIB", "sourcePlatformEntity"),
        ("HP-OPENCALL-SS7SNMPAGENT-BASE-MIB", "sourceObjectID"),
        ("HP-OPENCALL-SS7SNMPAGENT-BASE-MIB", "perceveidSeverity"),
        ("HP-OPENCALL-SS7SNMPAGENT-BASE-MIB", "alarmText"),
        ("HP-OPENCALL-SS7SNMPAGENT-BASE-MIB", "probableCause"),
        ("HP-OPENCALL-SS7SNMPAGENT-BASE-MIB", "correctiveAction"),
        ("HP-OPENCALL-SS7SNMPAGENT-BASE-MIB", "htimeStamp"))
)
if mibBuilder.loadTexts:
    hHPOC_40400001.setStatus(
        "current"
    )

hHPOC_40400002 = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 29, 2, 0, 40400002)
)
hHPOC_40400002.setObjects(
      *(("HP-OPENCALL-SS7SNMPAGENT-BASE-MIB", "sourcePlatformEntity"),
        ("HP-OPENCALL-SS7SNMPAGENT-BASE-MIB", "sourceObjectID"),
        ("HP-OPENCALL-SS7SNMPAGENT-BASE-MIB", "perceveidSeverity"),
        ("HP-OPENCALL-SS7SNMPAGENT-BASE-MIB", "alarmText"),
        ("HP-OPENCALL-SS7SNMPAGENT-BASE-MIB", "probableCause"),
        ("HP-OPENCALL-SS7SNMPAGENT-BASE-MIB", "correctiveAction"),
        ("HP-OPENCALL-SS7SNMPAGENT-BASE-MIB", "htimeStamp"))
)
if mibBuilder.loadTexts:
    hHPOC_40400002.setStatus(
        "current"
    )

hHPOC_40400003 = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 29, 2, 0, 40400003)
)
hHPOC_40400003.setObjects(
      *(("HP-OPENCALL-SS7SNMPAGENT-BASE-MIB", "sourcePlatformEntity"),
        ("HP-OPENCALL-SS7SNMPAGENT-BASE-MIB", "sourceObjectID"),
        ("HP-OPENCALL-SS7SNMPAGENT-BASE-MIB", "perceveidSeverity"),
        ("HP-OPENCALL-SS7SNMPAGENT-BASE-MIB", "alarmText"),
        ("HP-OPENCALL-SS7SNMPAGENT-BASE-MIB", "probableCause"),
        ("HP-OPENCALL-SS7SNMPAGENT-BASE-MIB", "correctiveAction"),
        ("HP-OPENCALL-SS7SNMPAGENT-BASE-MIB", "htimeStamp"))
)
if mibBuilder.loadTexts:
    hHPOC_40400003.setStatus(
        "current"
    )

hHPOC_40300011 = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 29, 2, 0, 403000011)
)
hHPOC_40300011.setObjects(
      *(("HP-OPENCALL-SS7SNMPAGENT-BASE-MIB", "sourcePlatformEntity"),
        ("HP-OPENCALL-SS7SNMPAGENT-BASE-MIB", "sourceObjectID"),
        ("HP-OPENCALL-SS7SNMPAGENT-BASE-MIB", "perceveidSeverity"),
        ("HP-OPENCALL-SS7SNMPAGENT-BASE-MIB", "alarmText"),
        ("HP-OPENCALL-SS7SNMPAGENT-BASE-MIB", "probableCause"),
        ("HP-OPENCALL-SS7SNMPAGENT-BASE-MIB", "correctiveAction"),
        ("HP-OPENCALL-SS7SNMPAGENT-BASE-MIB", "htimeStamp"))
)
if mibBuilder.loadTexts:
    hHPOC_40300011.setStatus(
        "current"
    )

hHPOC_40300015 = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 29, 2, 0, 403000015)
)
hHPOC_40300015.setObjects(
      *(("HP-OPENCALL-SS7SNMPAGENT-BASE-MIB", "sourcePlatformEntity"),
        ("HP-OPENCALL-SS7SNMPAGENT-BASE-MIB", "sourceObjectID"),
        ("HP-OPENCALL-SS7SNMPAGENT-BASE-MIB", "perceveidSeverity"),
        ("HP-OPENCALL-SS7SNMPAGENT-BASE-MIB", "alarmText"),
        ("HP-OPENCALL-SS7SNMPAGENT-BASE-MIB", "probableCause"),
        ("HP-OPENCALL-SS7SNMPAGENT-BASE-MIB", "correctiveAction"),
        ("HP-OPENCALL-SS7SNMPAGENT-BASE-MIB", "htimeStamp"))
)
if mibBuilder.loadTexts:
    hHPOC_40300015.setStatus(
        "current"
    )

hHPOC_40300016 = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 29, 2, 0, 403000016)
)
hHPOC_40300016.setObjects(
      *(("HP-OPENCALL-SS7SNMPAGENT-BASE-MIB", "sourcePlatformEntity"),
        ("HP-OPENCALL-SS7SNMPAGENT-BASE-MIB", "sourceObjectID"),
        ("HP-OPENCALL-SS7SNMPAGENT-BASE-MIB", "perceveidSeverity"),
        ("HP-OPENCALL-SS7SNMPAGENT-BASE-MIB", "alarmText"),
        ("HP-OPENCALL-SS7SNMPAGENT-BASE-MIB", "probableCause"),
        ("HP-OPENCALL-SS7SNMPAGENT-BASE-MIB", "correctiveAction"),
        ("HP-OPENCALL-SS7SNMPAGENT-BASE-MIB", "htimeStamp"))
)
if mibBuilder.loadTexts:
    hHPOC_40300016.setStatus(
        "current"
    )

hHPOC_40300017 = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 29, 2, 0, 403000017)
)
hHPOC_40300017.setObjects(
      *(("HP-OPENCALL-SS7SNMPAGENT-BASE-MIB", "sourcePlatformEntity"),
        ("HP-OPENCALL-SS7SNMPAGENT-BASE-MIB", "sourceObjectID"),
        ("HP-OPENCALL-SS7SNMPAGENT-BASE-MIB", "perceveidSeverity"),
        ("HP-OPENCALL-SS7SNMPAGENT-BASE-MIB", "alarmText"),
        ("HP-OPENCALL-SS7SNMPAGENT-BASE-MIB", "probableCause"),
        ("HP-OPENCALL-SS7SNMPAGENT-BASE-MIB", "correctiveAction"),
        ("HP-OPENCALL-SS7SNMPAGENT-BASE-MIB", "htimeStamp"))
)
if mibBuilder.loadTexts:
    hHPOC_40300017.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HP-OPENCALL-SS7SNMPAGENT-BASE-MIB",
    **{"openCall": openCall,
       "openCallTraps": openCallTraps,
       "sourcePlatformEntity": sourcePlatformEntity,
       "sourceObjectID": sourceObjectID,
       "perceveidSeverity": perceveidSeverity,
       "alarmText": alarmText,
       "probableCause": probableCause,
       "correctiveAction": correctiveAction,
       "htimeStamp": htimeStamp,
       "hHPOC-3100155": hHPOC_3100155,
       "hHPOC-8400042": hHPOC_8400042,
       "hHPOC-8400084": hHPOC_8400084,
       "hHPOC-8400085": hHPOC_8400085,
       "hHPOC-8400086": hHPOC_8400086,
       "hHPOC-8400087": hHPOC_8400087,
       "hHPOC-8400088": hHPOC_8400088,
       "hHPOC-8400089": hHPOC_8400089,
       "hHPOC-9000332": hHPOC_9000332,
       "hHPOC-9000334": hHPOC_9000334,
       "hHPOC-9000336": hHPOC_9000336,
       "hHPOC-9000341": hHPOC_9000341,
       "hHPOC-9000342": hHPOC_9000342,
       "hHPOC-9000343": hHPOC_9000343,
       "hHPOC-9000344": hHPOC_9000344,
       "hHPOC-9000345": hHPOC_9000345,
       "hHPOC-9000346": hHPOC_9000346,
       "hHPOC-9000347": hHPOC_9000347,
       "hHPOC-9000348": hHPOC_9000348,
       "hHPOC-9000349": hHPOC_9000349,
       "hHPOC-9000350": hHPOC_9000350,
       "hHPOC-9000354": hHPOC_9000354,
       "hHPOC-9000355": hHPOC_9000355,
       "hHPOC-9000356": hHPOC_9000356,
       "hHPOC-9000357": hHPOC_9000357,
       "hHPOC-9000635": hHPOC_9000635,
       "hHPOC-9000636": hHPOC_9000636,
       "hHPOC-9000681": hHPOC_9000681,
       "hHPOC-9000682": hHPOC_9000682,
       "hHPOC-9001260": hHPOC_9001260,
       "hHPOC-9001262": hHPOC_9001262,
       "hHPOC-9001268": hHPOC_9001268,
       "hHPOC-9001269": hHPOC_9001269,
       "hHPOC-9001270": hHPOC_9001270,
       "hHPOC-9001271": hHPOC_9001271,
       "hHPOC-9001272": hHPOC_9001272,
       "hHPOC-9001273": hHPOC_9001273,
       "hHPOC-9001274": hHPOC_9001274,
       "hHPOC-9001275": hHPOC_9001275,
       "hHPOC-9001276": hHPOC_9001276,
       "hHPOC-9001277": hHPOC_9001277,
       "hHPOC-9001278": hHPOC_9001278,
       "hHPOC-9001279": hHPOC_9001279,
       "hHPOC-9001280": hHPOC_9001280,
       "hHPOC-40100001": hHPOC_40100001,
       "hHPOC-40100011": hHPOC_40100011,
       "hHPOC-40100040": hHPOC_40100040,
       "hHPOC-40100501": hHPOC_40100501,
       "hHPOC-40100502": hHPOC_40100502,
       "hHPOC-40100601": hHPOC_40100601,
       "hHPOC-40100607": hHPOC_40100607,
       "hHPOC-40100608": hHPOC_40100608,
       "hHPOC-40100801": hHPOC_40100801,
       "hHPOC-40100802": hHPOC_40100802,
       "hHPOC-40100803": hHPOC_40100803,
       "hHPOC-40100804": hHPOC_40100804,
       "hHPOC-40100806": hHPOC_40100806,
       "hHPOC-40100807": hHPOC_40100807,
       "hHPOC-40100809": hHPOC_40100809,
       "hHPOC-40100810": hHPOC_40100810,
       "hHPOC-40300002": hHPOC_40300002,
       "hHPOC-40300003": hHPOC_40300003,
       "hHPOC-40300006": hHPOC_40300006,
       "hHPOC-40400001": hHPOC_40400001,
       "hHPOC-40400002": hHPOC_40400002,
       "hHPOC-40400003": hHPOC_40400003,
       "hHPOC-40300011": hHPOC_40300011,
       "hHPOC-40300015": hHPOC_40300015,
       "hHPOC-40300016": hHPOC_40300016,
       "hHPOC-40300017": hHPOC_40300017}
)
