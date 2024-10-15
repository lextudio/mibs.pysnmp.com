# SNMP MIB module (OCMP311TRAP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/OCMP311TRAP-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:33:38 2024
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

_Hp_ObjectIdentity = ObjectIdentity
hp = _Hp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11)
)
_Nm_ObjectIdentity = ObjectIdentity
nm = _Nm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2)
)
_InNetElem_ObjectIdentity = ObjectIdentity
inNetElem = _InNetElem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 29)
)
_OpenCall_ObjectIdentity = ObjectIdentity
openCall = _OpenCall_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 29, 2)
)
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
    sourcePlatformEntity.setStatus("mandatory")
_SourceObjectID_Type = DisplayString
_SourceObjectID_Object = MibScalar
sourceObjectID = _SourceObjectID_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 29, 2, 0, 2),
    _SourceObjectID_Type()
)
sourceObjectID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sourceObjectID.setStatus("mandatory")
_PerceivedSeverity_Type = DisplayString
_PerceivedSeverity_Object = MibScalar
perceivedSeverity = _PerceivedSeverity_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 29, 2, 0, 3),
    _PerceivedSeverity_Type()
)
perceivedSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    perceivedSeverity.setStatus("mandatory")
_AlarmText_Type = DisplayString
_AlarmText_Object = MibScalar
alarmText = _AlarmText_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 29, 2, 0, 4),
    _AlarmText_Type()
)
alarmText.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmText.setStatus("mandatory")
_ProbableCause_Type = DisplayString
_ProbableCause_Object = MibScalar
probableCause = _ProbableCause_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 29, 2, 0, 5),
    _ProbableCause_Type()
)
probableCause.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    probableCause.setStatus("mandatory")
_CorrectiveAction_Type = DisplayString
_CorrectiveAction_Object = MibScalar
correctiveAction = _CorrectiveAction_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 29, 2, 0, 6),
    _CorrectiveAction_Type()
)
correctiveAction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    correctiveAction.setStatus("mandatory")
_TimeStamp_Type = DisplayString
_TimeStamp_Object = MibScalar
timeStamp = _TimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 29, 2, 0, 7),
    _TimeStamp_Type()
)
timeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    timeStamp.setStatus("mandatory")

# Managed Objects groups


# Notification objects

hHPOC_20000006 = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 29, 2, 0, 20000006)
)
hHPOC_20000006.setObjects(
      *(("OCMP311TRAP-MIB", "sourcePlatformEntity"),
        ("OCMP311TRAP-MIB", "sourceObjectID"),
        ("OCMP311TRAP-MIB", "perceivedSeverity"),
        ("OCMP311TRAP-MIB", "alarmText"),
        ("OCMP311TRAP-MIB", "probableCause"),
        ("OCMP311TRAP-MIB", "correctiveAction"),
        ("OCMP311TRAP-MIB", "timeStamp"))
)
if mibBuilder.loadTexts:
    hHPOC_20000006.setStatus(
        ""
    )

hHPOC_20000007 = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 29, 2, 0, 20000007)
)
hHPOC_20000007.setObjects(
      *(("OCMP311TRAP-MIB", "sourcePlatformEntity"),
        ("OCMP311TRAP-MIB", "sourceObjectID"),
        ("OCMP311TRAP-MIB", "perceivedSeverity"),
        ("OCMP311TRAP-MIB", "alarmText"),
        ("OCMP311TRAP-MIB", "probableCause"),
        ("OCMP311TRAP-MIB", "correctiveAction"),
        ("OCMP311TRAP-MIB", "timeStamp"))
)
if mibBuilder.loadTexts:
    hHPOC_20000007.setStatus(
        ""
    )

hHPOC_20000010 = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 29, 2, 0, 20000010)
)
hHPOC_20000010.setObjects(
      *(("OCMP311TRAP-MIB", "sourcePlatformEntity"),
        ("OCMP311TRAP-MIB", "sourceObjectID"),
        ("OCMP311TRAP-MIB", "perceivedSeverity"),
        ("OCMP311TRAP-MIB", "alarmText"),
        ("OCMP311TRAP-MIB", "probableCause"),
        ("OCMP311TRAP-MIB", "correctiveAction"),
        ("OCMP311TRAP-MIB", "timeStamp"))
)
if mibBuilder.loadTexts:
    hHPOC_20000010.setStatus(
        ""
    )

hHPOC_20000011 = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 29, 2, 0, 20000011)
)
hHPOC_20000011.setObjects(
      *(("OCMP311TRAP-MIB", "sourcePlatformEntity"),
        ("OCMP311TRAP-MIB", "sourceObjectID"),
        ("OCMP311TRAP-MIB", "perceivedSeverity"),
        ("OCMP311TRAP-MIB", "alarmText"),
        ("OCMP311TRAP-MIB", "probableCause"),
        ("OCMP311TRAP-MIB", "correctiveAction"),
        ("OCMP311TRAP-MIB", "timeStamp"))
)
if mibBuilder.loadTexts:
    hHPOC_20000011.setStatus(
        ""
    )

hHPOC_20000017 = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 29, 2, 0, 20000017)
)
hHPOC_20000017.setObjects(
      *(("OCMP311TRAP-MIB", "sourcePlatformEntity"),
        ("OCMP311TRAP-MIB", "sourceObjectID"),
        ("OCMP311TRAP-MIB", "perceivedSeverity"),
        ("OCMP311TRAP-MIB", "alarmText"),
        ("OCMP311TRAP-MIB", "probableCause"),
        ("OCMP311TRAP-MIB", "correctiveAction"),
        ("OCMP311TRAP-MIB", "timeStamp"))
)
if mibBuilder.loadTexts:
    hHPOC_20000017.setStatus(
        ""
    )

hHPOC_20000018 = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 29, 2, 0, 20000018)
)
hHPOC_20000018.setObjects(
      *(("OCMP311TRAP-MIB", "sourcePlatformEntity"),
        ("OCMP311TRAP-MIB", "sourceObjectID"),
        ("OCMP311TRAP-MIB", "perceivedSeverity"),
        ("OCMP311TRAP-MIB", "alarmText"),
        ("OCMP311TRAP-MIB", "probableCause"),
        ("OCMP311TRAP-MIB", "correctiveAction"),
        ("OCMP311TRAP-MIB", "timeStamp"))
)
if mibBuilder.loadTexts:
    hHPOC_20000018.setStatus(
        ""
    )

hHPOC_20000019 = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 29, 2, 0, 20000019)
)
hHPOC_20000019.setObjects(
      *(("OCMP311TRAP-MIB", "sourcePlatformEntity"),
        ("OCMP311TRAP-MIB", "sourceObjectID"),
        ("OCMP311TRAP-MIB", "perceivedSeverity"),
        ("OCMP311TRAP-MIB", "alarmText"),
        ("OCMP311TRAP-MIB", "probableCause"),
        ("OCMP311TRAP-MIB", "correctiveAction"),
        ("OCMP311TRAP-MIB", "timeStamp"))
)
if mibBuilder.loadTexts:
    hHPOC_20000019.setStatus(
        ""
    )

hHPOC_20000020 = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 29, 2, 0, 20000020)
)
hHPOC_20000020.setObjects(
      *(("OCMP311TRAP-MIB", "sourcePlatformEntity"),
        ("OCMP311TRAP-MIB", "sourceObjectID"),
        ("OCMP311TRAP-MIB", "perceivedSeverity"),
        ("OCMP311TRAP-MIB", "alarmText"),
        ("OCMP311TRAP-MIB", "probableCause"),
        ("OCMP311TRAP-MIB", "correctiveAction"),
        ("OCMP311TRAP-MIB", "timeStamp"))
)
if mibBuilder.loadTexts:
    hHPOC_20000020.setStatus(
        ""
    )

hHPOC_201000001 = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 29, 2, 0, 20100001)
)
hHPOC_201000001.setObjects(
      *(("OCMP311TRAP-MIB", "sourcePlatformEntity"),
        ("OCMP311TRAP-MIB", "sourceObjectID"),
        ("OCMP311TRAP-MIB", "perceivedSeverity"),
        ("OCMP311TRAP-MIB", "alarmText"),
        ("OCMP311TRAP-MIB", "probableCause"),
        ("OCMP311TRAP-MIB", "correctiveAction"),
        ("OCMP311TRAP-MIB", "timeStamp"))
)
if mibBuilder.loadTexts:
    hHPOC_201000001.setStatus(
        ""
    )

hHPOC_201000002 = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 29, 2, 0, 20100002)
)
hHPOC_201000002.setObjects(
      *(("OCMP311TRAP-MIB", "sourcePlatformEntity"),
        ("OCMP311TRAP-MIB", "sourceObjectID"),
        ("OCMP311TRAP-MIB", "perceivedSeverity"),
        ("OCMP311TRAP-MIB", "alarmText"),
        ("OCMP311TRAP-MIB", "probableCause"),
        ("OCMP311TRAP-MIB", "correctiveAction"),
        ("OCMP311TRAP-MIB", "timeStamp"))
)
if mibBuilder.loadTexts:
    hHPOC_201000002.setStatus(
        ""
    )

hHPOC_20200005 = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 29, 2, 0, 20200005)
)
hHPOC_20200005.setObjects(
      *(("OCMP311TRAP-MIB", "sourcePlatformEntity"),
        ("OCMP311TRAP-MIB", "sourceObjectID"),
        ("OCMP311TRAP-MIB", "perceivedSeverity"),
        ("OCMP311TRAP-MIB", "alarmText"),
        ("OCMP311TRAP-MIB", "probableCause"),
        ("OCMP311TRAP-MIB", "correctiveAction"),
        ("OCMP311TRAP-MIB", "timeStamp"))
)
if mibBuilder.loadTexts:
    hHPOC_20200005.setStatus(
        ""
    )

hHPOC_20200006 = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 29, 2, 0, 20200006)
)
hHPOC_20200006.setObjects(
      *(("OCMP311TRAP-MIB", "sourcePlatformEntity"),
        ("OCMP311TRAP-MIB", "sourceObjectID"),
        ("OCMP311TRAP-MIB", "perceivedSeverity"),
        ("OCMP311TRAP-MIB", "alarmText"),
        ("OCMP311TRAP-MIB", "probableCause"),
        ("OCMP311TRAP-MIB", "correctiveAction"),
        ("OCMP311TRAP-MIB", "timeStamp"))
)
if mibBuilder.loadTexts:
    hHPOC_20200006.setStatus(
        ""
    )

hHPOC_20200010 = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 29, 2, 0, 20200010)
)
hHPOC_20200010.setObjects(
      *(("OCMP311TRAP-MIB", "sourcePlatformEntity"),
        ("OCMP311TRAP-MIB", "sourceObjectID"),
        ("OCMP311TRAP-MIB", "perceivedSeverity"),
        ("OCMP311TRAP-MIB", "alarmText"),
        ("OCMP311TRAP-MIB", "probableCause"),
        ("OCMP311TRAP-MIB", "correctiveAction"),
        ("OCMP311TRAP-MIB", "timeStamp"))
)
if mibBuilder.loadTexts:
    hHPOC_20200010.setStatus(
        ""
    )

hHPOC_20200011 = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 29, 2, 0, 20200011)
)
hHPOC_20200011.setObjects(
      *(("OCMP311TRAP-MIB", "sourcePlatformEntity"),
        ("OCMP311TRAP-MIB", "sourceObjectID"),
        ("OCMP311TRAP-MIB", "perceivedSeverity"),
        ("OCMP311TRAP-MIB", "alarmText"),
        ("OCMP311TRAP-MIB", "probableCause"),
        ("OCMP311TRAP-MIB", "correctiveAction"),
        ("OCMP311TRAP-MIB", "timeStamp"))
)
if mibBuilder.loadTexts:
    hHPOC_20200011.setStatus(
        ""
    )

hHPOC_20300001 = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 29, 2, 0, 20300001)
)
hHPOC_20300001.setObjects(
      *(("OCMP311TRAP-MIB", "sourcePlatformEntity"),
        ("OCMP311TRAP-MIB", "sourceObjectID"),
        ("OCMP311TRAP-MIB", "perceivedSeverity"),
        ("OCMP311TRAP-MIB", "alarmText"),
        ("OCMP311TRAP-MIB", "probableCause"),
        ("OCMP311TRAP-MIB", "correctiveAction"),
        ("OCMP311TRAP-MIB", "timeStamp"))
)
if mibBuilder.loadTexts:
    hHPOC_20300001.setStatus(
        ""
    )

hHPOC_20300003 = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 29, 2, 0, 20300003)
)
hHPOC_20300003.setObjects(
      *(("OCMP311TRAP-MIB", "sourcePlatformEntity"),
        ("OCMP311TRAP-MIB", "sourceObjectID"),
        ("OCMP311TRAP-MIB", "perceivedSeverity"),
        ("OCMP311TRAP-MIB", "alarmText"),
        ("OCMP311TRAP-MIB", "probableCause"),
        ("OCMP311TRAP-MIB", "correctiveAction"),
        ("OCMP311TRAP-MIB", "timeStamp"))
)
if mibBuilder.loadTexts:
    hHPOC_20300003.setStatus(
        ""
    )

hHPOC_20300069 = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 29, 2, 0, 20300069)
)
hHPOC_20300069.setObjects(
      *(("OCMP311TRAP-MIB", "sourcePlatformEntity"),
        ("OCMP311TRAP-MIB", "sourceObjectID"),
        ("OCMP311TRAP-MIB", "perceivedSeverity"),
        ("OCMP311TRAP-MIB", "alarmText"),
        ("OCMP311TRAP-MIB", "probableCause"),
        ("OCMP311TRAP-MIB", "correctiveAction"),
        ("OCMP311TRAP-MIB", "timeStamp"))
)
if mibBuilder.loadTexts:
    hHPOC_20300069.setStatus(
        ""
    )

hHPOC_20300070 = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 29, 2, 0, 20300070)
)
hHPOC_20300070.setObjects(
      *(("OCMP311TRAP-MIB", "sourcePlatformEntity"),
        ("OCMP311TRAP-MIB", "sourceObjectID"),
        ("OCMP311TRAP-MIB", "perceivedSeverity"),
        ("OCMP311TRAP-MIB", "alarmText"),
        ("OCMP311TRAP-MIB", "probableCause"),
        ("OCMP311TRAP-MIB", "correctiveAction"),
        ("OCMP311TRAP-MIB", "timeStamp"))
)
if mibBuilder.loadTexts:
    hHPOC_20300070.setStatus(
        ""
    )

hHPOC_20300085 = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 29, 2, 0, 20300085)
)
hHPOC_20300085.setObjects(
      *(("OCMP311TRAP-MIB", "sourcePlatformEntity"),
        ("OCMP311TRAP-MIB", "sourceObjectID"),
        ("OCMP311TRAP-MIB", "perceivedSeverity"),
        ("OCMP311TRAP-MIB", "alarmText"),
        ("OCMP311TRAP-MIB", "probableCause"),
        ("OCMP311TRAP-MIB", "correctiveAction"),
        ("OCMP311TRAP-MIB", "timeStamp"))
)
if mibBuilder.loadTexts:
    hHPOC_20300085.setStatus(
        ""
    )

hHPOC_20300086 = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 29, 2, 0, 20300086)
)
hHPOC_20300086.setObjects(
      *(("OCMP311TRAP-MIB", "sourcePlatformEntity"),
        ("OCMP311TRAP-MIB", "sourceObjectID"),
        ("OCMP311TRAP-MIB", "perceivedSeverity"),
        ("OCMP311TRAP-MIB", "alarmText"),
        ("OCMP311TRAP-MIB", "probableCause"),
        ("OCMP311TRAP-MIB", "correctiveAction"),
        ("OCMP311TRAP-MIB", "timeStamp"))
)
if mibBuilder.loadTexts:
    hHPOC_20300086.setStatus(
        ""
    )

hHPOC_20400003 = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 29, 2, 0, 20400003)
)
hHPOC_20400003.setObjects(
      *(("OCMP311TRAP-MIB", "sourcePlatformEntity"),
        ("OCMP311TRAP-MIB", "sourceObjectID"),
        ("OCMP311TRAP-MIB", "perceivedSeverity"),
        ("OCMP311TRAP-MIB", "alarmText"),
        ("OCMP311TRAP-MIB", "probableCause"),
        ("OCMP311TRAP-MIB", "correctiveAction"),
        ("OCMP311TRAP-MIB", "timeStamp"))
)
if mibBuilder.loadTexts:
    hHPOC_20400003.setStatus(
        ""
    )

hHPOC_20500003 = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 29, 2, 0, 20500003)
)
hHPOC_20500003.setObjects(
      *(("OCMP311TRAP-MIB", "sourcePlatformEntity"),
        ("OCMP311TRAP-MIB", "sourceObjectID"),
        ("OCMP311TRAP-MIB", "perceivedSeverity"),
        ("OCMP311TRAP-MIB", "alarmText"),
        ("OCMP311TRAP-MIB", "probableCause"),
        ("OCMP311TRAP-MIB", "correctiveAction"),
        ("OCMP311TRAP-MIB", "timeStamp"))
)
if mibBuilder.loadTexts:
    hHPOC_20500003.setStatus(
        ""
    )

hHPOC_20500004 = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 29, 2, 0, 20500004)
)
hHPOC_20500004.setObjects(
      *(("OCMP311TRAP-MIB", "sourcePlatformEntity"),
        ("OCMP311TRAP-MIB", "sourceObjectID"),
        ("OCMP311TRAP-MIB", "perceivedSeverity"),
        ("OCMP311TRAP-MIB", "alarmText"),
        ("OCMP311TRAP-MIB", "probableCause"),
        ("OCMP311TRAP-MIB", "correctiveAction"),
        ("OCMP311TRAP-MIB", "timeStamp"))
)
if mibBuilder.loadTexts:
    hHPOC_20500004.setStatus(
        ""
    )

hHPOC_20600002 = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 29, 2, 0, 20600002)
)
hHPOC_20600002.setObjects(
      *(("OCMP311TRAP-MIB", "sourcePlatformEntity"),
        ("OCMP311TRAP-MIB", "sourceObjectID"),
        ("OCMP311TRAP-MIB", "perceivedSeverity"),
        ("OCMP311TRAP-MIB", "alarmText"),
        ("OCMP311TRAP-MIB", "probableCause"),
        ("OCMP311TRAP-MIB", "correctiveAction"),
        ("OCMP311TRAP-MIB", "timeStamp"))
)
if mibBuilder.loadTexts:
    hHPOC_20600002.setStatus(
        ""
    )

hHPOC_20600005 = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 29, 2, 0, 20600005)
)
hHPOC_20600005.setObjects(
      *(("OCMP311TRAP-MIB", "sourcePlatformEntity"),
        ("OCMP311TRAP-MIB", "sourceObjectID"),
        ("OCMP311TRAP-MIB", "perceivedSeverity"),
        ("OCMP311TRAP-MIB", "alarmText"),
        ("OCMP311TRAP-MIB", "probableCause"),
        ("OCMP311TRAP-MIB", "correctiveAction"),
        ("OCMP311TRAP-MIB", "timeStamp"))
)
if mibBuilder.loadTexts:
    hHPOC_20600005.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "OCMP311TRAP-MIB",
    **{"hp": hp,
       "nm": nm,
       "inNetElem": inNetElem,
       "openCall": openCall,
       "openCallTraps": openCallTraps,
       "sourcePlatformEntity": sourcePlatformEntity,
       "sourceObjectID": sourceObjectID,
       "perceivedSeverity": perceivedSeverity,
       "alarmText": alarmText,
       "probableCause": probableCause,
       "correctiveAction": correctiveAction,
       "timeStamp": timeStamp,
       "hHPOC-20000006": hHPOC_20000006,
       "hHPOC-20000007": hHPOC_20000007,
       "hHPOC-20000010": hHPOC_20000010,
       "hHPOC-20000011": hHPOC_20000011,
       "hHPOC-20000017": hHPOC_20000017,
       "hHPOC-20000018": hHPOC_20000018,
       "hHPOC-20000019": hHPOC_20000019,
       "hHPOC-20000020": hHPOC_20000020,
       "hHPOC-201000001": hHPOC_201000001,
       "hHPOC-201000002": hHPOC_201000002,
       "hHPOC-20200005": hHPOC_20200005,
       "hHPOC-20200006": hHPOC_20200006,
       "hHPOC-20200010": hHPOC_20200010,
       "hHPOC-20200011": hHPOC_20200011,
       "hHPOC-20300001": hHPOC_20300001,
       "hHPOC-20300003": hHPOC_20300003,
       "hHPOC-20300069": hHPOC_20300069,
       "hHPOC-20300070": hHPOC_20300070,
       "hHPOC-20300085": hHPOC_20300085,
       "hHPOC-20300086": hHPOC_20300086,
       "hHPOC-20400003": hHPOC_20400003,
       "hHPOC-20500003": hHPOC_20500003,
       "hHPOC-20500004": hHPOC_20500004,
       "hHPOC-20600002": hHPOC_20600002,
       "hHPOC-20600005": hHPOC_20600005}
)
