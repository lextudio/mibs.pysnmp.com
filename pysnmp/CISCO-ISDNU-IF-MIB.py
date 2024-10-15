# SNMP MIB module (CISCO-ISDNU-IF-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-ISDNU-IF-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:03:10 2024
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

ciscoIsdnuIfMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 18)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CiuIfObjects_ObjectIdentity = ObjectIdentity
ciuIfObjects = _CiuIfObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 18, 1)
)
_CiuInterface_ObjectIdentity = ObjectIdentity
ciuInterface = _CiuInterface_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 18, 1, 1)
)
_CiuIfStaticConfigTable_Object = MibTable
ciuIfStaticConfigTable = _CiuIfStaticConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 18, 1, 1, 1)
)
if mibBuilder.loadTexts:
    ciuIfStaticConfigTable.setStatus("current")
_CiuIfStaticConfigEntry_Object = MibTableRow
ciuIfStaticConfigEntry = _CiuIfStaticConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 18, 1, 1, 1, 1)
)
ciuIfStaticConfigEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    ciuIfStaticConfigEntry.setStatus("current")


class _CiuIfType_Type(Integer32):
    """Custom type ciuIfType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("addOnIntegUandSTPort", 5),
          ("addOnU", 2),
          ("onBoardIntegUandSTPort", 4),
          ("onBoardU", 3),
          ("other", 1))
    )


_CiuIfType_Type.__name__ = "Integer32"
_CiuIfType_Object = MibTableColumn
ciuIfType = _CiuIfType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 18, 1, 1, 1, 1, 1),
    _CiuIfType_Type()
)
ciuIfType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciuIfType.setStatus("current")
_CiuIfStatusTable_Object = MibTable
ciuIfStatusTable = _CiuIfStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 18, 1, 1, 2)
)
if mibBuilder.loadTexts:
    ciuIfStatusTable.setStatus("current")
_CiuIfStatusEntry_Object = MibTableRow
ciuIfStatusEntry = _CiuIfStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 18, 1, 1, 2, 1)
)
ciuIfStatusEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    ciuIfStatusEntry.setStatus("current")


class _CiuIfStatus_Type(Integer32):
    """Custom type ciuIfStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("activated", 1),
          ("activationPending", 2),
          ("deactivated", 3))
    )


_CiuIfStatus_Type.__name__ = "Integer32"
_CiuIfStatus_Object = MibTableColumn
ciuIfStatus = _CiuIfStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 18, 1, 1, 2, 1, 1),
    _CiuIfStatus_Type()
)
ciuIfStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciuIfStatus.setStatus("current")


class _CiuIfEocCommand_Type(DisplayString):
    """Custom type ciuIfEocCommand based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 48),
    )


_CiuIfEocCommand_Type.__name__ = "DisplayString"
_CiuIfEocCommand_Object = MibTableColumn
ciuIfEocCommand = _CiuIfEocCommand_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 18, 1, 1, 2, 1, 2),
    _CiuIfEocCommand_Type()
)
ciuIfEocCommand.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciuIfEocCommand.setStatus("current")


class _CiuIfOverHeadBits_Type(OctetString):
    """Custom type ciuIfOverHeadBits based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_CiuIfOverHeadBits_Type.__name__ = "OctetString"
_CiuIfOverHeadBits_Object = MibTableColumn
ciuIfOverHeadBits = _CiuIfOverHeadBits_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 18, 1, 1, 2, 1, 3),
    _CiuIfOverHeadBits_Type()
)
ciuIfOverHeadBits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciuIfOverHeadBits.setStatus("current")
_CiuIfFebeErrors_Type = Counter32
_CiuIfFebeErrors_Object = MibTableColumn
ciuIfFebeErrors = _CiuIfFebeErrors_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 18, 1, 1, 2, 1, 4),
    _CiuIfFebeErrors_Type()
)
ciuIfFebeErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciuIfFebeErrors.setStatus("current")
_CiuIfNebeErrors_Type = Counter32
_CiuIfNebeErrors_Object = MibTableColumn
ciuIfNebeErrors = _CiuIfNebeErrors_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 18, 1, 1, 2, 1, 5),
    _CiuIfNebeErrors_Type()
)
ciuIfNebeErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciuIfNebeErrors.setStatus("current")


class _CiuIfLoopStatus_Type(Integer32):
    """Custom type ciuIfLoopStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("ilmtMode", 5),
          ("none", 1),
          ("ntQuietMode", 4),
          ("type2Loopback", 2),
          ("type3Loopback", 3))
    )


_CiuIfLoopStatus_Type.__name__ = "Integer32"
_CiuIfLoopStatus_Object = MibTableColumn
ciuIfLoopStatus = _CiuIfLoopStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 18, 1, 1, 2, 1, 6),
    _CiuIfLoopStatus_Type()
)
ciuIfLoopStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciuIfLoopStatus.setStatus("current")
_CiuIfExternalSTPort_ObjectIdentity = ObjectIdentity
ciuIfExternalSTPort = _CiuIfExternalSTPort_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 18, 1, 2)
)
_CiuIfExternalSTPortStatusTable_Object = MibTable
ciuIfExternalSTPortStatusTable = _CiuIfExternalSTPortStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 18, 1, 2, 1)
)
if mibBuilder.loadTexts:
    ciuIfExternalSTPortStatusTable.setStatus("current")
_CiuIfExternalSTPortStatusEntry_Object = MibTableRow
ciuIfExternalSTPortStatusEntry = _CiuIfExternalSTPortStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 18, 1, 2, 1, 1)
)
ciuIfExternalSTPortStatusEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "CISCO-ISDNU-IF-MIB", "ciuIfExternalSTPortNumber"),
)
if mibBuilder.loadTexts:
    ciuIfExternalSTPortStatusEntry.setStatus("current")


class _CiuIfExternalSTPortNumber_Type(Integer32):
    """Custom type ciuIfExternalSTPortNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_CiuIfExternalSTPortNumber_Type.__name__ = "Integer32"
_CiuIfExternalSTPortNumber_Object = MibTableColumn
ciuIfExternalSTPortNumber = _CiuIfExternalSTPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 18, 1, 2, 1, 1, 1),
    _CiuIfExternalSTPortNumber_Type()
)
ciuIfExternalSTPortNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ciuIfExternalSTPortNumber.setStatus("current")


class _CiuIfExternalSTPortStatus_Type(Integer32):
    """Custom type ciuIfExternalSTPortStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("activated", 1),
          ("activationPending", 2),
          ("deactivated", 3))
    )


_CiuIfExternalSTPortStatus_Type.__name__ = "Integer32"
_CiuIfExternalSTPortStatus_Object = MibTableColumn
ciuIfExternalSTPortStatus = _CiuIfExternalSTPortStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 18, 1, 2, 1, 1, 2),
    _CiuIfExternalSTPortStatus_Type()
)
ciuIfExternalSTPortStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciuIfExternalSTPortStatus.setStatus("current")
_CiuIfMIBNotificationEnables_ObjectIdentity = ObjectIdentity
ciuIfMIBNotificationEnables = _CiuIfMIBNotificationEnables_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 18, 1, 3)
)


class _CiuIfEnableULoopStatusNotification_Type(TruthValue):
    """Custom type ciuIfEnableULoopStatusNotification based on TruthValue"""


_CiuIfEnableULoopStatusNotification_Object = MibScalar
ciuIfEnableULoopStatusNotification = _CiuIfEnableULoopStatusNotification_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 18, 1, 3, 1),
    _CiuIfEnableULoopStatusNotification_Type()
)
ciuIfEnableULoopStatusNotification.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ciuIfEnableULoopStatusNotification.setStatus("current")
_CiuIfMIBNotificationPrefix_ObjectIdentity = ObjectIdentity
ciuIfMIBNotificationPrefix = _CiuIfMIBNotificationPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 18, 2)
)
_CiuIfMIBNotifications_ObjectIdentity = ObjectIdentity
ciuIfMIBNotifications = _CiuIfMIBNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 18, 2, 0)
)
_CiuIfMIBConformance_ObjectIdentity = ObjectIdentity
ciuIfMIBConformance = _CiuIfMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 18, 3)
)
_CiuIfMIBCompliances_ObjectIdentity = ObjectIdentity
ciuIfMIBCompliances = _CiuIfMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 18, 3, 1)
)
_CiuIfMIBGroups_ObjectIdentity = ObjectIdentity
ciuIfMIBGroups = _CiuIfMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 18, 3, 2)
)

# Managed Objects groups

ciuIfMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 18, 3, 2, 1)
)
ciuIfMIBGroup.setObjects(
      *(("CISCO-ISDNU-IF-MIB", "ciuIfType"),
        ("CISCO-ISDNU-IF-MIB", "ciuIfStatus"),
        ("CISCO-ISDNU-IF-MIB", "ciuIfEocCommand"),
        ("CISCO-ISDNU-IF-MIB", "ciuIfOverHeadBits"),
        ("CISCO-ISDNU-IF-MIB", "ciuIfFebeErrors"),
        ("CISCO-ISDNU-IF-MIB", "ciuIfNebeErrors"),
        ("CISCO-ISDNU-IF-MIB", "ciuIfLoopStatus"),
        ("CISCO-ISDNU-IF-MIB", "ciuIfExternalSTPortStatus"),
        ("CISCO-ISDNU-IF-MIB", "ciuIfEnableULoopStatusNotification"))
)
if mibBuilder.loadTexts:
    ciuIfMIBGroup.setStatus("current")


# Notification objects

ciuIfLoopStatusNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 18, 2, 0, 1)
)
ciuIfLoopStatusNotification.setObjects(
    ("CISCO-ISDNU-IF-MIB", "ciuIfLoopStatus")
)
if mibBuilder.loadTexts:
    ciuIfLoopStatusNotification.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance

ciuIfMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 18, 3, 1, 1)
)
if mibBuilder.loadTexts:
    ciuIfMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-ISDNU-IF-MIB",
    **{"ciscoIsdnuIfMIB": ciscoIsdnuIfMIB,
       "ciuIfObjects": ciuIfObjects,
       "ciuInterface": ciuInterface,
       "ciuIfStaticConfigTable": ciuIfStaticConfigTable,
       "ciuIfStaticConfigEntry": ciuIfStaticConfigEntry,
       "ciuIfType": ciuIfType,
       "ciuIfStatusTable": ciuIfStatusTable,
       "ciuIfStatusEntry": ciuIfStatusEntry,
       "ciuIfStatus": ciuIfStatus,
       "ciuIfEocCommand": ciuIfEocCommand,
       "ciuIfOverHeadBits": ciuIfOverHeadBits,
       "ciuIfFebeErrors": ciuIfFebeErrors,
       "ciuIfNebeErrors": ciuIfNebeErrors,
       "ciuIfLoopStatus": ciuIfLoopStatus,
       "ciuIfExternalSTPort": ciuIfExternalSTPort,
       "ciuIfExternalSTPortStatusTable": ciuIfExternalSTPortStatusTable,
       "ciuIfExternalSTPortStatusEntry": ciuIfExternalSTPortStatusEntry,
       "ciuIfExternalSTPortNumber": ciuIfExternalSTPortNumber,
       "ciuIfExternalSTPortStatus": ciuIfExternalSTPortStatus,
       "ciuIfMIBNotificationEnables": ciuIfMIBNotificationEnables,
       "ciuIfEnableULoopStatusNotification": ciuIfEnableULoopStatusNotification,
       "ciuIfMIBNotificationPrefix": ciuIfMIBNotificationPrefix,
       "ciuIfMIBNotifications": ciuIfMIBNotifications,
       "ciuIfLoopStatusNotification": ciuIfLoopStatusNotification,
       "ciuIfMIBConformance": ciuIfMIBConformance,
       "ciuIfMIBCompliances": ciuIfMIBCompliances,
       "ciuIfMIBCompliance": ciuIfMIBCompliance,
       "ciuIfMIBGroups": ciuIfMIBGroups,
       "ciuIfMIBGroup": ciuIfMIBGroup}
)
