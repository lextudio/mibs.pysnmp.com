# SNMP MIB module (CISCO-LINK-ERROR-MONITOR-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-LINK-ERROR-MONITOR-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:04:03 2024
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

(ciscoMgmt,) = mibBuilder.importSymbols(
    "CISCO-SMI",
    "ciscoMgmt")

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

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

(DisplayString,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

ciscoLinkErrorMonitorMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 426)
)
ciscoLinkErrorMonitorMIB.setRevisions(
        ("2004-11-19 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class ClemCounterType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("inerrors", 3),
          ("rxcrc", 1),
          ("txcrc", 2))
    )



# MIB Managed Objects in the order of their OIDs

_CiscoLinkErrMonMIBNotifs_ObjectIdentity = ObjectIdentity
ciscoLinkErrMonMIBNotifs = _CiscoLinkErrMonMIBNotifs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 426, 0)
)
_CiscoLinkErrMonMIBObjects_ObjectIdentity = ObjectIdentity
ciscoLinkErrMonMIBObjects = _CiscoLinkErrMonMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 426, 1)
)
_ClemGlobalObjects_ObjectIdentity = ObjectIdentity
clemGlobalObjects = _ClemGlobalObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 426, 1, 1)
)
_ClemEnabled_Type = TruthValue
_ClemEnabled_Object = MibScalar
clemEnabled = _ClemEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 426, 1, 1, 1),
    _ClemEnabled_Type()
)
clemEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clemEnabled.setStatus("current")
_ClemSamplingInterval_Type = Unsigned32
_ClemSamplingInterval_Object = MibScalar
clemSamplingInterval = _ClemSamplingInterval_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 426, 1, 1, 2),
    _ClemSamplingInterval_Type()
)
clemSamplingInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clemSamplingInterval.setStatus("current")
if mibBuilder.loadTexts:
    clemSamplingInterval.setUnits("seconds")
_ClemSamplingTimes_Type = Unsigned32
_ClemSamplingTimes_Object = MibScalar
clemSamplingTimes = _ClemSamplingTimes_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 426, 1, 1, 3),
    _ClemSamplingTimes_Type()
)
clemSamplingTimes.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clemSamplingTimes.setStatus("current")


class _ClemAction_Type(Integer32):
    """Custom type clemAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("errdisable", 1),
          ("failover", 2))
    )


_ClemAction_Type.__name__ = "Integer32"
_ClemAction_Object = MibScalar
clemAction = _ClemAction_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 426, 1, 1, 4),
    _ClemAction_Type()
)
clemAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clemAction.setStatus("current")
_ClemThresholdTable_Object = MibTable
clemThresholdTable = _ClemThresholdTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 426, 1, 1, 5)
)
if mibBuilder.loadTexts:
    clemThresholdTable.setStatus("current")
_ClemThresholdEntry_Object = MibTableRow
clemThresholdEntry = _ClemThresholdEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 426, 1, 1, 5, 1)
)
clemThresholdEntry.setIndexNames(
    (0, "CISCO-LINK-ERROR-MONITOR-MIB", "clemThresholdCounterType"),
)
if mibBuilder.loadTexts:
    clemThresholdEntry.setStatus("current")
_ClemThresholdCounterType_Type = ClemCounterType
_ClemThresholdCounterType_Object = MibTableColumn
clemThresholdCounterType = _ClemThresholdCounterType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 426, 1, 1, 5, 1, 1),
    _ClemThresholdCounterType_Type()
)
clemThresholdCounterType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    clemThresholdCounterType.setStatus("current")
_ClemThresholdLow_Type = Unsigned32
_ClemThresholdLow_Object = MibTableColumn
clemThresholdLow = _ClemThresholdLow_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 426, 1, 1, 5, 1, 2),
    _ClemThresholdLow_Type()
)
clemThresholdLow.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clemThresholdLow.setStatus("current")
_ClemThresholdHigh_Type = Unsigned32
_ClemThresholdHigh_Object = MibTableColumn
clemThresholdHigh = _ClemThresholdHigh_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 426, 1, 1, 5, 1, 3),
    _ClemThresholdHigh_Type()
)
clemThresholdHigh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clemThresholdHigh.setStatus("current")


class _ClemNotifEnable_Type(Bits):
    """Custom type clemNotifEnable based on Bits"""
    namedValues = NamedValues(
        *(("highThresholdExceeded", 1),
          ("lowThresholdExceeded", 0))
    )

_ClemNotifEnable_Type.__name__ = "Bits"
_ClemNotifEnable_Object = MibScalar
clemNotifEnable = _ClemNotifEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 426, 1, 1, 6),
    _ClemNotifEnable_Type()
)
clemNotifEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clemNotifEnable.setStatus("current")
_ClemInterfaceObjects_ObjectIdentity = ObjectIdentity
clemInterfaceObjects = _ClemInterfaceObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 426, 1, 2)
)
_ClemIfCounterTable_Object = MibTable
clemIfCounterTable = _ClemIfCounterTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 426, 1, 2, 1)
)
if mibBuilder.loadTexts:
    clemIfCounterTable.setStatus("current")
_ClemIfCounterEntry_Object = MibTableRow
clemIfCounterEntry = _ClemIfCounterEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 426, 1, 2, 1, 1)
)
clemIfCounterEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "CISCO-LINK-ERROR-MONITOR-MIB", "clemIfCounterType"),
)
if mibBuilder.loadTexts:
    clemIfCounterEntry.setStatus("current")
_ClemIfCounterType_Type = ClemCounterType
_ClemIfCounterType_Object = MibTableColumn
clemIfCounterType = _ClemIfCounterType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 426, 1, 2, 1, 1, 1),
    _ClemIfCounterType_Type()
)
clemIfCounterType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    clemIfCounterType.setStatus("current")
_ClemIfCounterEnable_Type = TruthValue
_ClemIfCounterEnable_Object = MibTableColumn
clemIfCounterEnable = _ClemIfCounterEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 426, 1, 2, 1, 1, 2),
    _ClemIfCounterEnable_Type()
)
clemIfCounterEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clemIfCounterEnable.setStatus("current")
_CiscoLinkErrMonMIBConform_ObjectIdentity = ObjectIdentity
ciscoLinkErrMonMIBConform = _CiscoLinkErrMonMIBConform_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 426, 2)
)
_CiscoLinkErrMonMIBCompliances_ObjectIdentity = ObjectIdentity
ciscoLinkErrMonMIBCompliances = _CiscoLinkErrMonMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 426, 2, 1)
)
_CiscoLinkErrMonMIBGroups_ObjectIdentity = ObjectIdentity
ciscoLinkErrMonMIBGroups = _CiscoLinkErrMonMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 426, 2, 2)
)

# Managed Objects groups

clemGlobalGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 426, 2, 2, 1)
)
clemGlobalGroup.setObjects(
      *(("CISCO-LINK-ERROR-MONITOR-MIB", "clemEnabled"),
        ("CISCO-LINK-ERROR-MONITOR-MIB", "clemSamplingInterval"),
        ("CISCO-LINK-ERROR-MONITOR-MIB", "clemSamplingTimes"),
        ("CISCO-LINK-ERROR-MONITOR-MIB", "clemAction"))
)
if mibBuilder.loadTexts:
    clemGlobalGroup.setStatus("current")

clemThresholdGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 426, 2, 2, 2)
)
clemThresholdGroup.setObjects(
      *(("CISCO-LINK-ERROR-MONITOR-MIB", "clemThresholdLow"),
        ("CISCO-LINK-ERROR-MONITOR-MIB", "clemThresholdHigh"))
)
if mibBuilder.loadTexts:
    clemThresholdGroup.setStatus("current")

clemIfCounterGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 426, 2, 2, 3)
)
clemIfCounterGroup.setObjects(
    ("CISCO-LINK-ERROR-MONITOR-MIB", "clemIfCounterEnable")
)
if mibBuilder.loadTexts:
    clemIfCounterGroup.setStatus("current")

clemNotificationControlGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 426, 2, 2, 5)
)
clemNotificationControlGroup.setObjects(
    ("CISCO-LINK-ERROR-MONITOR-MIB", "clemNotifEnable")
)
if mibBuilder.loadTexts:
    clemNotificationControlGroup.setStatus("current")


# Notification objects

clemLowThresholdExceeded = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 426, 0, 1)
)
clemLowThresholdExceeded.setObjects(
      *(("CISCO-LINK-ERROR-MONITOR-MIB", "clemThresholdLow"),
        ("IF-MIB", "ifIndex"))
)
if mibBuilder.loadTexts:
    clemLowThresholdExceeded.setStatus(
        "current"
    )

clemHighThresholdExceeded = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 426, 0, 2)
)
clemHighThresholdExceeded.setObjects(
      *(("CISCO-LINK-ERROR-MONITOR-MIB", "clemThresholdHigh"),
        ("IF-MIB", "ifIndex"))
)
if mibBuilder.loadTexts:
    clemHighThresholdExceeded.setStatus(
        "current"
    )


# Notifications groups

clemNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 426, 2, 2, 4)
)
clemNotificationGroup.setObjects(
      *(("CISCO-LINK-ERROR-MONITOR-MIB", "clemLowThresholdExceeded"),
        ("CISCO-LINK-ERROR-MONITOR-MIB", "clemHighThresholdExceeded"))
)
if mibBuilder.loadTexts:
    clemNotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

ciscoLinkErrMonMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 426, 2, 1, 1)
)
if mibBuilder.loadTexts:
    ciscoLinkErrMonMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-LINK-ERROR-MONITOR-MIB",
    **{"ClemCounterType": ClemCounterType,
       "ciscoLinkErrorMonitorMIB": ciscoLinkErrorMonitorMIB,
       "ciscoLinkErrMonMIBNotifs": ciscoLinkErrMonMIBNotifs,
       "clemLowThresholdExceeded": clemLowThresholdExceeded,
       "clemHighThresholdExceeded": clemHighThresholdExceeded,
       "ciscoLinkErrMonMIBObjects": ciscoLinkErrMonMIBObjects,
       "clemGlobalObjects": clemGlobalObjects,
       "clemEnabled": clemEnabled,
       "clemSamplingInterval": clemSamplingInterval,
       "clemSamplingTimes": clemSamplingTimes,
       "clemAction": clemAction,
       "clemThresholdTable": clemThresholdTable,
       "clemThresholdEntry": clemThresholdEntry,
       "clemThresholdCounterType": clemThresholdCounterType,
       "clemThresholdLow": clemThresholdLow,
       "clemThresholdHigh": clemThresholdHigh,
       "clemNotifEnable": clemNotifEnable,
       "clemInterfaceObjects": clemInterfaceObjects,
       "clemIfCounterTable": clemIfCounterTable,
       "clemIfCounterEntry": clemIfCounterEntry,
       "clemIfCounterType": clemIfCounterType,
       "clemIfCounterEnable": clemIfCounterEnable,
       "ciscoLinkErrMonMIBConform": ciscoLinkErrMonMIBConform,
       "ciscoLinkErrMonMIBCompliances": ciscoLinkErrMonMIBCompliances,
       "ciscoLinkErrMonMIBCompliance": ciscoLinkErrMonMIBCompliance,
       "ciscoLinkErrMonMIBGroups": ciscoLinkErrMonMIBGroups,
       "clemGlobalGroup": clemGlobalGroup,
       "clemThresholdGroup": clemThresholdGroup,
       "clemIfCounterGroup": clemIfCounterGroup,
       "clemNotificationGroup": clemNotificationGroup,
       "clemNotificationControlGroup": clemNotificationControlGroup}
)
