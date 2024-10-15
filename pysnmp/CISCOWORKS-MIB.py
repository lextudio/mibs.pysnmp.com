# SNMP MIB module (CISCOWORKS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCOWORKS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:15:27 2024
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

(ciscoworks,) = mibBuilder.importSymbols(
    "CISCO-SMI",
    "ciscoworks")

(ModuleCompliance,
 NotificationGroup,
 ObjectGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup",
    "ObjectGroup")

(sysUpTime,) = mibBuilder.importSymbols(
    "SNMPv2-MIB",
    "sysUpTime")

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

cwLogMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 14, 1)
)
cwLogMIB.setRevisions(
        ("2003-02-18 00:00",
         "1995-04-02 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CwLog_ObjectIdentity = ObjectIdentity
cwLog = _CwLog_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 14, 1, 1)
)


class _CwLogDate_Type(DisplayString):
    """Custom type cwLogDate based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(15, 15),
    )


_CwLogDate_Type.__name__ = "DisplayString"
_CwLogDate_Object = MibScalar
cwLogDate = _CwLogDate_Object(
    (1, 3, 6, 1, 4, 1, 9, 14, 1, 1, 1),
    _CwLogDate_Type()
)
cwLogDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwLogDate.setStatus("current")


class _CwLogSource_Type(Integer32):
    """Custom type cwLogSource based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("ciscoworks", 2),
          ("device", 3),
          ("other", 1))
    )


_CwLogSource_Type.__name__ = "Integer32"
_CwLogSource_Object = MibScalar
cwLogSource = _CwLogSource_Object(
    (1, 3, 6, 1, 4, 1, 9, 14, 1, 1, 2),
    _CwLogSource_Type()
)
cwLogSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwLogSource.setStatus("current")


class _CwLogApp_Type(DisplayString):
    """Custom type cwLogApp based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_CwLogApp_Type.__name__ = "DisplayString"
_CwLogApp_Object = MibScalar
cwLogApp = _CwLogApp_Object(
    (1, 3, 6, 1, 4, 1, 9, 14, 1, 1, 3),
    _CwLogApp_Type()
)
cwLogApp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwLogApp.setStatus("current")


class _CwLogMsg_Type(DisplayString):
    """Custom type cwLogMsg based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CwLogMsg_Type.__name__ = "DisplayString"
_CwLogMsg_Object = MibScalar
cwLogMsg = _CwLogMsg_Object(
    (1, 3, 6, 1, 4, 1, 9, 14, 1, 1, 4),
    _CwLogMsg_Type()
)
cwLogMsg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwLogMsg.setStatus("current")
_CwTrapsPrefix_ObjectIdentity = ObjectIdentity
cwTrapsPrefix = _CwTrapsPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 14, 1, 2)
)
_CwTraps_ObjectIdentity = ObjectIdentity
cwTraps = _CwTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 14, 1, 2, 0)
)
_CwMIBConform_ObjectIdentity = ObjectIdentity
cwMIBConform = _CwMIBConform_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 14, 1, 3)
)
_CiscoCwMIBCompliances_ObjectIdentity = ObjectIdentity
ciscoCwMIBCompliances = _CiscoCwMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 14, 1, 3, 1)
)
_CiscoCwMIBGroups_ObjectIdentity = ObjectIdentity
ciscoCwMIBGroups = _CiscoCwMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 14, 1, 3, 2)
)

# Managed Objects groups

ciscoCwObjectsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 14, 1, 3, 2, 7)
)
ciscoCwObjectsGroup.setObjects(
      *(("CISCOWORKS-MIB", "cwLogDate"),
        ("CISCOWORKS-MIB", "cwLogSource"),
        ("CISCOWORKS-MIB", "cwLogApp"),
        ("CISCOWORKS-MIB", "cwLogMsg"))
)
if mibBuilder.loadTexts:
    ciscoCwObjectsGroup.setStatus("current")


# Notification objects

cwAppLogTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 14, 1, 2, 0, 1)
)
cwAppLogTrap.setObjects(
      *(("SNMPv2-MIB", "sysUpTime"),
        ("CISCOWORKS-MIB", "cwLogDate"),
        ("CISCOWORKS-MIB", "cwLogSource"),
        ("CISCOWORKS-MIB", "cwLogApp"),
        ("CISCOWORKS-MIB", "cwLogMsg"))
)
if mibBuilder.loadTexts:
    cwAppLogTrap.setStatus(
        "current"
    )

cwDevLogTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 14, 1, 2, 0, 2)
)
cwDevLogTrap.setObjects(
      *(("SNMPv2-MIB", "sysUpTime"),
        ("CISCOWORKS-MIB", "cwLogDate"),
        ("CISCOWORKS-MIB", "cwLogSource"),
        ("CISCOWORKS-MIB", "cwLogMsg"))
)
if mibBuilder.loadTexts:
    cwDevLogTrap.setStatus(
        "current"
    )


# Notifications groups

ciscoCwNotificationsGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9, 14, 1, 3, 2, 12)
)
ciscoCwNotificationsGroup.setObjects(
      *(("CISCOWORKS-MIB", "cwAppLogTrap"),
        ("CISCOWORKS-MIB", "cwDevLogTrap"))
)
if mibBuilder.loadTexts:
    ciscoCwNotificationsGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

ciscoCwMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 14, 1, 3, 1, 1)
)
if mibBuilder.loadTexts:
    ciscoCwMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCOWORKS-MIB",
    **{"cwLogMIB": cwLogMIB,
       "cwLog": cwLog,
       "cwLogDate": cwLogDate,
       "cwLogSource": cwLogSource,
       "cwLogApp": cwLogApp,
       "cwLogMsg": cwLogMsg,
       "cwTrapsPrefix": cwTrapsPrefix,
       "cwTraps": cwTraps,
       "cwAppLogTrap": cwAppLogTrap,
       "cwDevLogTrap": cwDevLogTrap,
       "cwMIBConform": cwMIBConform,
       "ciscoCwMIBCompliances": ciscoCwMIBCompliances,
       "ciscoCwMIBCompliance": ciscoCwMIBCompliance,
       "ciscoCwMIBGroups": ciscoCwMIBGroups,
       "ciscoCwObjectsGroup": ciscoCwObjectsGroup,
       "ciscoCwNotificationsGroup": ciscoCwNotificationsGroup}
)
