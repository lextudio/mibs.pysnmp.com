# SNMP MIB module (INFOSIM-TRAPMIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/INFOSIM-TRAPMIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:09:23 2024
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

(DateAndTime,
 DisplayString,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Infosim_ObjectIdentity = ObjectIdentity
infosim = _Infosim_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9611)
)
_SnAgent_ObjectIdentity = ObjectIdentity
snAgent = _SnAgent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9611, 1)
)
_SnAgentObjects_ObjectIdentity = ObjectIdentity
snAgentObjects = _SnAgentObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9611, 1, 1)
)
_SnAgentEventTable_Object = MibTable
snAgentEventTable = _SnAgentEventTable_Object(
    (1, 3, 6, 1, 4, 1, 9611, 1, 1, 1)
)
if mibBuilder.loadTexts:
    snAgentEventTable.setStatus("mandatory")
_SnAgentEventEntry_Object = MibTableRow
snAgentEventEntry = _SnAgentEventEntry_Object(
    (1, 3, 6, 1, 4, 1, 9611, 1, 1, 1, 1)
)
snAgentEventEntry.setIndexNames(
    (0, "INFOSIM-TRAPMIB", "snAgentEventIndex"),
)
if mibBuilder.loadTexts:
    snAgentEventEntry.setStatus("mandatory")
_SnAgentEventIndex_Type = Integer32
_SnAgentEventIndex_Object = MibTableColumn
snAgentEventIndex = _SnAgentEventIndex_Object(
    (1, 3, 6, 1, 4, 1, 9611, 1, 1, 1, 1, 1),
    _SnAgentEventIndex_Type()
)
snAgentEventIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snAgentEventIndex.setStatus("mandatory")
_SnMonitorName_Type = DisplayString
_SnMonitorName_Object = MibTableColumn
snMonitorName = _SnMonitorName_Object(
    (1, 3, 6, 1, 4, 1, 9611, 1, 1, 1, 1, 2),
    _SnMonitorName_Type()
)
snMonitorName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snMonitorName.setStatus("mandatory")
_SnMonitorIP_Type = DisplayString
_SnMonitorIP_Object = MibTableColumn
snMonitorIP = _SnMonitorIP_Object(
    (1, 3, 6, 1, 4, 1, 9611, 1, 1, 1, 1, 3),
    _SnMonitorIP_Type()
)
snMonitorIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snMonitorIP.setStatus("mandatory")
_SnEventStateString_Type = DisplayString
_SnEventStateString_Object = MibTableColumn
snEventStateString = _SnEventStateString_Object(
    (1, 3, 6, 1, 4, 1, 9611, 1, 1, 1, 1, 4),
    _SnEventStateString_Type()
)
snEventStateString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snEventStateString.setStatus("mandatory")
_SnEventState_Type = Integer32
_SnEventState_Object = MibTableColumn
snEventState = _SnEventState_Object(
    (1, 3, 6, 1, 4, 1, 9611, 1, 1, 1, 1, 5),
    _SnEventState_Type()
)
snEventState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snEventState.setStatus("mandatory")
_SnAlarmTime_Type = DateAndTime
_SnAlarmTime_Object = MibTableColumn
snAlarmTime = _SnAlarmTime_Object(
    (1, 3, 6, 1, 4, 1, 9611, 1, 1, 1, 1, 6),
    _SnAlarmTime_Type()
)
snAlarmTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snAlarmTime.setStatus("mandatory")


class _SnAlarmLevel_Type(Integer32):
    """Custom type snAlarmLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1000,
              2000,
              3000,
              4000,
              5000)
        )
    )
    namedValues = NamedValues(
        *(("critical", 5000),
          ("informational", 1000),
          ("major", 4000),
          ("marginal", 2000),
          ("minor", 3000))
    )


_SnAlarmLevel_Type.__name__ = "Integer32"
_SnAlarmLevel_Object = MibTableColumn
snAlarmLevel = _SnAlarmLevel_Object(
    (1, 3, 6, 1, 4, 1, 9611, 1, 1, 1, 1, 7),
    _SnAlarmLevel_Type()
)
snAlarmLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snAlarmLevel.setStatus("mandatory")
_SnAlarmDescription_Type = DisplayString
_SnAlarmDescription_Object = MibTableColumn
snAlarmDescription = _SnAlarmDescription_Object(
    (1, 3, 6, 1, 4, 1, 9611, 1, 1, 1, 1, 8),
    _SnAlarmDescription_Type()
)
snAlarmDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snAlarmDescription.setStatus("mandatory")
_SnMonitorId_Type = Integer32
_SnMonitorId_Object = MibTableColumn
snMonitorId = _SnMonitorId_Object(
    (1, 3, 6, 1, 4, 1, 9611, 1, 1, 1, 1, 9),
    _SnMonitorId_Type()
)
snMonitorId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snMonitorId.setStatus("mandatory")
_SnSeverityLevel_Type = Integer32
_SnSeverityLevel_Object = MibTableColumn
snSeverityLevel = _SnSeverityLevel_Object(
    (1, 3, 6, 1, 4, 1, 9611, 1, 1, 1, 1, 10),
    _SnSeverityLevel_Type()
)
snSeverityLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snSeverityLevel.setStatus("mandatory")
_SnValue_Type = DisplayString
_SnValue_Object = MibTableColumn
snValue = _SnValue_Object(
    (1, 3, 6, 1, 4, 1, 9611, 1, 1, 1, 1, 11),
    _SnValue_Type()
)
snValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snValue.setStatus("mandatory")
_SnValueText_Type = DisplayString
_SnValueText_Object = MibTableColumn
snValueText = _SnValueText_Object(
    (1, 3, 6, 1, 4, 1, 9611, 1, 1, 1, 1, 12),
    _SnValueText_Type()
)
snValueText.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snValueText.setStatus("mandatory")
_SnCategory0_Type = DisplayString
_SnCategory0_Object = MibTableColumn
snCategory0 = _SnCategory0_Object(
    (1, 3, 6, 1, 4, 1, 9611, 1, 1, 1, 1, 13),
    _SnCategory0_Type()
)
snCategory0.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snCategory0.setStatus("mandatory")
_SnCategory1_Type = DisplayString
_SnCategory1_Object = MibTableColumn
snCategory1 = _SnCategory1_Object(
    (1, 3, 6, 1, 4, 1, 9611, 1, 1, 1, 1, 14),
    _SnCategory1_Type()
)
snCategory1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snCategory1.setStatus("mandatory")
_SnCategory2_Type = DisplayString
_SnCategory2_Object = MibTableColumn
snCategory2 = _SnCategory2_Object(
    (1, 3, 6, 1, 4, 1, 9611, 1, 1, 1, 1, 15),
    _SnCategory2_Type()
)
snCategory2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snCategory2.setStatus("mandatory")
_SnCategory3_Type = DisplayString
_SnCategory3_Object = MibTableColumn
snCategory3 = _SnCategory3_Object(
    (1, 3, 6, 1, 4, 1, 9611, 1, 1, 1, 1, 16),
    _SnCategory3_Type()
)
snCategory3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snCategory3.setStatus("mandatory")
_SnCategory4_Type = DisplayString
_SnCategory4_Object = MibTableColumn
snCategory4 = _SnCategory4_Object(
    (1, 3, 6, 1, 4, 1, 9611, 1, 1, 1, 1, 17),
    _SnCategory4_Type()
)
snCategory4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snCategory4.setStatus("mandatory")
_SnCategory5_Type = DisplayString
_SnCategory5_Object = MibTableColumn
snCategory5 = _SnCategory5_Object(
    (1, 3, 6, 1, 4, 1, 9611, 1, 1, 1, 1, 18),
    _SnCategory5_Type()
)
snCategory5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snCategory5.setStatus("mandatory")
_SnCategory6_Type = DisplayString
_SnCategory6_Object = MibTableColumn
snCategory6 = _SnCategory6_Object(
    (1, 3, 6, 1, 4, 1, 9611, 1, 1, 1, 1, 19),
    _SnCategory6_Type()
)
snCategory6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snCategory6.setStatus("mandatory")
_SnCategory7_Type = DisplayString
_SnCategory7_Object = MibTableColumn
snCategory7 = _SnCategory7_Object(
    (1, 3, 6, 1, 4, 1, 9611, 1, 1, 1, 1, 20),
    _SnCategory7_Type()
)
snCategory7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snCategory7.setStatus("mandatory")
_SnCategory8_Type = DisplayString
_SnCategory8_Object = MibTableColumn
snCategory8 = _SnCategory8_Object(
    (1, 3, 6, 1, 4, 1, 9611, 1, 1, 1, 1, 21),
    _SnCategory8_Type()
)
snCategory8.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snCategory8.setStatus("mandatory")
_SnCategory9_Type = DisplayString
_SnCategory9_Object = MibTableColumn
snCategory9 = _SnCategory9_Object(
    (1, 3, 6, 1, 4, 1, 9611, 1, 1, 1, 1, 22),
    _SnCategory9_Type()
)
snCategory9.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snCategory9.setStatus("mandatory")
_SnCategory10_Type = DisplayString
_SnCategory10_Object = MibTableColumn
snCategory10 = _SnCategory10_Object(
    (1, 3, 6, 1, 4, 1, 9611, 1, 1, 1, 1, 23),
    _SnCategory10_Type()
)
snCategory10.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snCategory10.setStatus("mandatory")
_SnCategory11_Type = DisplayString
_SnCategory11_Object = MibTableColumn
snCategory11 = _SnCategory11_Object(
    (1, 3, 6, 1, 4, 1, 9611, 1, 1, 1, 1, 24),
    _SnCategory11_Type()
)
snCategory11.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snCategory11.setStatus("mandatory")
_SnCategory12_Type = DisplayString
_SnCategory12_Object = MibTableColumn
snCategory12 = _SnCategory12_Object(
    (1, 3, 6, 1, 4, 1, 9611, 1, 1, 1, 1, 25),
    _SnCategory12_Type()
)
snCategory12.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snCategory12.setStatus("mandatory")
_SnCategory13_Type = DisplayString
_SnCategory13_Object = MibTableColumn
snCategory13 = _SnCategory13_Object(
    (1, 3, 6, 1, 4, 1, 9611, 1, 1, 1, 1, 26),
    _SnCategory13_Type()
)
snCategory13.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snCategory13.setStatus("mandatory")
_SnCategory14_Type = DisplayString
_SnCategory14_Object = MibTableColumn
snCategory14 = _SnCategory14_Object(
    (1, 3, 6, 1, 4, 1, 9611, 1, 1, 1, 1, 27),
    _SnCategory14_Type()
)
snCategory14.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snCategory14.setStatus("mandatory")
_SnAgentTraps_ObjectIdentity = ObjectIdentity
snAgentTraps = _SnAgentTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9611, 1, 2)
)

# Managed Objects groups


# Notification objects

snAgentEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 9611, 1, 2, 0, 1)
)
snAgentEvent.setObjects(
      *(("INFOSIM-TRAPMIB", "snMonitorName"),
        ("INFOSIM-TRAPMIB", "snMonitorIP"),
        ("INFOSIM-TRAPMIB", "snEventStateString"),
        ("INFOSIM-TRAPMIB", "snEventState"),
        ("INFOSIM-TRAPMIB", "snAlarmTime"),
        ("INFOSIM-TRAPMIB", "snAlarmLevel"),
        ("INFOSIM-TRAPMIB", "snAlarmDescription"),
        ("INFOSIM-TRAPMIB", "snMonitorId"),
        ("INFOSIM-TRAPMIB", "snSeverityLevel"),
        ("INFOSIM-TRAPMIB", "snValue"),
        ("INFOSIM-TRAPMIB", "snValueText"),
        ("INFOSIM-TRAPMIB", "snCategory0"),
        ("INFOSIM-TRAPMIB", "snCategory1"),
        ("INFOSIM-TRAPMIB", "snCategory2"),
        ("INFOSIM-TRAPMIB", "snCategory3"),
        ("INFOSIM-TRAPMIB", "snCategory4"),
        ("INFOSIM-TRAPMIB", "snCategory5"),
        ("INFOSIM-TRAPMIB", "snCategory6"),
        ("INFOSIM-TRAPMIB", "snCategory7"),
        ("INFOSIM-TRAPMIB", "snCategory8"),
        ("INFOSIM-TRAPMIB", "snCategory9"),
        ("INFOSIM-TRAPMIB", "snCategory10"),
        ("INFOSIM-TRAPMIB", "snCategory11"),
        ("INFOSIM-TRAPMIB", "snCategory12"),
        ("INFOSIM-TRAPMIB", "snCategory13"),
        ("INFOSIM-TRAPMIB", "snCategory14"))
)
if mibBuilder.loadTexts:
    snAgentEvent.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "INFOSIM-TRAPMIB",
    **{"infosim": infosim,
       "snAgent": snAgent,
       "snAgentObjects": snAgentObjects,
       "snAgentEventTable": snAgentEventTable,
       "snAgentEventEntry": snAgentEventEntry,
       "snAgentEventIndex": snAgentEventIndex,
       "snMonitorName": snMonitorName,
       "snMonitorIP": snMonitorIP,
       "snEventStateString": snEventStateString,
       "snEventState": snEventState,
       "snAlarmTime": snAlarmTime,
       "snAlarmLevel": snAlarmLevel,
       "snAlarmDescription": snAlarmDescription,
       "snMonitorId": snMonitorId,
       "snSeverityLevel": snSeverityLevel,
       "snValue": snValue,
       "snValueText": snValueText,
       "snCategory0": snCategory0,
       "snCategory1": snCategory1,
       "snCategory2": snCategory2,
       "snCategory3": snCategory3,
       "snCategory4": snCategory4,
       "snCategory5": snCategory5,
       "snCategory6": snCategory6,
       "snCategory7": snCategory7,
       "snCategory8": snCategory8,
       "snCategory9": snCategory9,
       "snCategory10": snCategory10,
       "snCategory11": snCategory11,
       "snCategory12": snCategory12,
       "snCategory13": snCategory13,
       "snCategory14": snCategory14,
       "snAgentTraps": snAgentTraps,
       "snAgentEvent": snAgentEvent}
)
