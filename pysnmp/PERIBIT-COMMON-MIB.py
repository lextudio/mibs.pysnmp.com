# SNMP MIB module (PERIBIT-COMMON-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/PERIBIT-COMMON-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:38:25 2024
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

(pnCommonMib,
 pnModules) = mibBuilder.importSymbols(
    "PERIBIT-GLOBAL-REG",
    "pnCommonMib",
    "pnModules")

(TcChassisType,) = mibBuilder.importSymbols(
    "PERIBIT-GLOBAL-TC",
    "TcChassisType")

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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

pnCommonMibModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 8239, 1, 1, 3)
)
pnCommonMibModule.setRevisions(
        ("2003-09-30 08:45",
         "2003-04-01 00:00",
         "2003-03-10 00:00",
         "2002-06-03 00:00",
         "2002-03-27 00:00",
         "2002-02-22 00:00",
         "2002-01-23 00:00",
         "2002-01-17 00:00",
         "2001-08-07 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_PnCommonConfMib_ObjectIdentity = ObjectIdentity
pnCommonConfMib = _PnCommonConfMib_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8239, 2, 1, 1)
)
if mibBuilder.loadTexts:
    pnCommonConfMib.setStatus("current")
_PnCommonObjs_ObjectIdentity = ObjectIdentity
pnCommonObjs = _PnCommonObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8239, 2, 1, 2)
)
if mibBuilder.loadTexts:
    pnCommonObjs.setStatus("current")
_PnSys_ObjectIdentity = ObjectIdentity
pnSys = _PnSys_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8239, 2, 1, 2, 1)
)
if mibBuilder.loadTexts:
    pnSys.setStatus("current")


class _PnSysSwVersion_Type(DisplayString):
    """Custom type pnSysSwVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_PnSysSwVersion_Type.__name__ = "DisplayString"
_PnSysSwVersion_Object = MibScalar
pnSysSwVersion = _PnSysSwVersion_Object(
    (1, 3, 6, 1, 4, 1, 8239, 2, 1, 2, 1, 1),
    _PnSysSwVersion_Type()
)
pnSysSwVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pnSysSwVersion.setStatus("current")


class _PnSysHwVersion_Type(DisplayString):
    """Custom type pnSysHwVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_PnSysHwVersion_Type.__name__ = "DisplayString"
_PnSysHwVersion_Object = MibScalar
pnSysHwVersion = _PnSysHwVersion_Object(
    (1, 3, 6, 1, 4, 1, 8239, 2, 1, 2, 1, 2),
    _PnSysHwVersion_Type()
)
pnSysHwVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pnSysHwVersion.setStatus("current")


class _PnSysSerialNumber_Type(DisplayString):
    """Custom type pnSysSerialNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_PnSysSerialNumber_Type.__name__ = "DisplayString"
_PnSysSerialNumber_Object = MibScalar
pnSysSerialNumber = _PnSysSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 8239, 2, 1, 2, 1, 3),
    _PnSysSerialNumber_Type()
)
pnSysSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pnSysSerialNumber.setStatus("current")
_PnSysTimeZoneOffset_Type = Integer32
_PnSysTimeZoneOffset_Object = MibScalar
pnSysTimeZoneOffset = _PnSysTimeZoneOffset_Object(
    (1, 3, 6, 1, 4, 1, 8239, 2, 1, 2, 1, 4),
    _PnSysTimeZoneOffset_Type()
)
pnSysTimeZoneOffset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pnSysTimeZoneOffset.setStatus("current")
_PnSysDaylightSaving_Type = TruthValue
_PnSysDaylightSaving_Object = MibScalar
pnSysDaylightSaving = _PnSysDaylightSaving_Object(
    (1, 3, 6, 1, 4, 1, 8239, 2, 1, 2, 1, 5),
    _PnSysDaylightSaving_Type()
)
pnSysDaylightSaving.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pnSysDaylightSaving.setStatus("current")
_PnChassis_ObjectIdentity = ObjectIdentity
pnChassis = _PnChassis_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8239, 2, 1, 2, 2)
)
if mibBuilder.loadTexts:
    pnChassis.setStatus("current")
_PnChassisType_Type = TcChassisType
_PnChassisType_Object = MibScalar
pnChassisType = _PnChassisType_Object(
    (1, 3, 6, 1, 4, 1, 8239, 2, 1, 2, 2, 1),
    _PnChassisType_Type()
)
pnChassisType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pnChassisType.setStatus("current")
_PnCommonEvents_ObjectIdentity = ObjectIdentity
pnCommonEvents = _PnCommonEvents_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8239, 2, 1, 3)
)
if mibBuilder.loadTexts:
    pnCommonEvents.setStatus("current")
_PnCommonEventObjs_ObjectIdentity = ObjectIdentity
pnCommonEventObjs = _PnCommonEventObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8239, 2, 1, 3, 1)
)
if mibBuilder.loadTexts:
    pnCommonEventObjs.setStatus("current")
_PnCommonEventDescr_Type = DisplayString
_PnCommonEventDescr_Object = MibScalar
pnCommonEventDescr = _PnCommonEventDescr_Object(
    (1, 3, 6, 1, 4, 1, 8239, 2, 1, 3, 1, 1),
    _PnCommonEventDescr_Type()
)
pnCommonEventDescr.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    pnCommonEventDescr.setStatus("current")
_PnCommonEventEvents_ObjectIdentity = ObjectIdentity
pnCommonEventEvents = _PnCommonEventEvents_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8239, 2, 1, 3, 2)
)
if mibBuilder.loadTexts:
    pnCommonEventEvents.setStatus("current")
_PnCommonEventEventsV2_ObjectIdentity = ObjectIdentity
pnCommonEventEventsV2 = _PnCommonEventEventsV2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8239, 2, 1, 3, 2, 0)
)
if mibBuilder.loadTexts:
    pnCommonEventEventsV2.setStatus("current")

# Managed Objects groups


# Notification objects

pnCommonEventInFailSafeMode = NotificationType(
    (1, 3, 6, 1, 4, 1, 8239, 2, 1, 3, 2, 0, 1)
)
if mibBuilder.loadTexts:
    pnCommonEventInFailSafeMode.setStatus(
        "current"
    )

pnCommonEventPowerSupplyFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 8239, 2, 1, 3, 2, 0, 2)
)
if mibBuilder.loadTexts:
    pnCommonEventPowerSupplyFailure.setStatus(
        "current"
    )

pnCommonEventPowerSupplyOk = NotificationType(
    (1, 3, 6, 1, 4, 1, 8239, 2, 1, 3, 2, 0, 3)
)
if mibBuilder.loadTexts:
    pnCommonEventPowerSupplyOk.setStatus(
        "current"
    )

pnCommonEventLicenseExpired = NotificationType(
    (1, 3, 6, 1, 4, 1, 8239, 2, 1, 3, 2, 0, 4)
)
pnCommonEventLicenseExpired.setObjects(
    ("PERIBIT-COMMON-MIB", "pnCommonEventDescr")
)
if mibBuilder.loadTexts:
    pnCommonEventLicenseExpired.setStatus(
        "current"
    )

pnCommonEventThruputLimitExceeded = NotificationType(
    (1, 3, 6, 1, 4, 1, 8239, 2, 1, 3, 2, 0, 5)
)
pnCommonEventThruputLimitExceeded.setObjects(
    ("PERIBIT-COMMON-MIB", "pnCommonEventDescr")
)
if mibBuilder.loadTexts:
    pnCommonEventThruputLimitExceeded.setStatus(
        "current"
    )

pnCommonEventLicenseWillExpire = NotificationType(
    (1, 3, 6, 1, 4, 1, 8239, 2, 1, 3, 2, 0, 6)
)
pnCommonEventLicenseWillExpire.setObjects(
    ("PERIBIT-COMMON-MIB", "pnCommonEventDescr")
)
if mibBuilder.loadTexts:
    pnCommonEventLicenseWillExpire.setStatus(
        "current"
    )

pnCommonEventLoginFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 8239, 2, 1, 3, 2, 0, 7)
)
pnCommonEventLoginFailure.setObjects(
    ("PERIBIT-COMMON-MIB", "pnCommonEventDescr")
)
if mibBuilder.loadTexts:
    pnCommonEventLoginFailure.setStatus(
        "current"
    )

pnCommonEventFaultTolerantPassThrough = NotificationType(
    (1, 3, 6, 1, 4, 1, 8239, 2, 1, 3, 2, 0, 8)
)
pnCommonEventFaultTolerantPassThrough.setObjects(
    ("PERIBIT-COMMON-MIB", "pnCommonEventDescr")
)
if mibBuilder.loadTexts:
    pnCommonEventFaultTolerantPassThrough.setStatus(
        "current"
    )

pnCommonEventFanFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 8239, 2, 1, 3, 2, 0, 9)
)
pnCommonEventFanFailure.setObjects(
    ("PERIBIT-COMMON-MIB", "pnCommonEventDescr")
)
if mibBuilder.loadTexts:
    pnCommonEventFanFailure.setStatus(
        "current"
    )

pnCommonEventFanSpeedVariation = NotificationType(
    (1, 3, 6, 1, 4, 1, 8239, 2, 1, 3, 2, 0, 10)
)
pnCommonEventFanSpeedVariation.setObjects(
    ("PERIBIT-COMMON-MIB", "pnCommonEventDescr")
)
if mibBuilder.loadTexts:
    pnCommonEventFanSpeedVariation.setStatus(
        "current"
    )

pnCommonEventFanOk = NotificationType(
    (1, 3, 6, 1, 4, 1, 8239, 2, 1, 3, 2, 0, 11)
)
pnCommonEventFanOk.setObjects(
    ("PERIBIT-COMMON-MIB", "pnCommonEventDescr")
)
if mibBuilder.loadTexts:
    pnCommonEventFanOk.setStatus(
        "current"
    )

pnCommonEventInterfaceSpeedMismatch = NotificationType(
    (1, 3, 6, 1, 4, 1, 8239, 2, 1, 3, 2, 0, 12)
)
pnCommonEventInterfaceSpeedMismatch.setObjects(
    ("PERIBIT-COMMON-MIB", "pnCommonEventDescr")
)
if mibBuilder.loadTexts:
    pnCommonEventInterfaceSpeedMismatch.setStatus(
        "current"
    )

pnCommonEventInterfaceSpeedOk = NotificationType(
    (1, 3, 6, 1, 4, 1, 8239, 2, 1, 3, 2, 0, 13)
)
pnCommonEventInterfaceSpeedOk.setObjects(
    ("PERIBIT-COMMON-MIB", "pnCommonEventDescr")
)
if mibBuilder.loadTexts:
    pnCommonEventInterfaceSpeedOk.setStatus(
        "current"
    )

pnCommonEventInterfaceDuplexMismatch = NotificationType(
    (1, 3, 6, 1, 4, 1, 8239, 2, 1, 3, 2, 0, 14)
)
pnCommonEventInterfaceDuplexMismatch.setObjects(
    ("PERIBIT-COMMON-MIB", "pnCommonEventDescr")
)
if mibBuilder.loadTexts:
    pnCommonEventInterfaceDuplexMismatch.setStatus(
        "current"
    )

pnCommonEventIpsecSecurityAssociationAdded = NotificationType(
    (1, 3, 6, 1, 4, 1, 8239, 2, 1, 3, 2, 0, 15)
)
pnCommonEventIpsecSecurityAssociationAdded.setObjects(
    ("PERIBIT-COMMON-MIB", "pnCommonEventDescr")
)
if mibBuilder.loadTexts:
    pnCommonEventIpsecSecurityAssociationAdded.setStatus(
        "current"
    )

pnCommonEventIpsecSecurityAssociationExpired = NotificationType(
    (1, 3, 6, 1, 4, 1, 8239, 2, 1, 3, 2, 0, 16)
)
pnCommonEventIpsecSecurityAssociationExpired.setObjects(
    ("PERIBIT-COMMON-MIB", "pnCommonEventDescr")
)
if mibBuilder.loadTexts:
    pnCommonEventIpsecSecurityAssociationExpired.setStatus(
        "current"
    )

pnCommonEventIpsecSecurityAssociationDeleted = NotificationType(
    (1, 3, 6, 1, 4, 1, 8239, 2, 1, 3, 2, 0, 17)
)
pnCommonEventIpsecSecurityAssociationDeleted.setObjects(
    ("PERIBIT-COMMON-MIB", "pnCommonEventDescr")
)
if mibBuilder.loadTexts:
    pnCommonEventIpsecSecurityAssociationDeleted.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "PERIBIT-COMMON-MIB",
    **{"pnCommonMibModule": pnCommonMibModule,
       "pnCommonConfMib": pnCommonConfMib,
       "pnCommonObjs": pnCommonObjs,
       "pnSys": pnSys,
       "pnSysSwVersion": pnSysSwVersion,
       "pnSysHwVersion": pnSysHwVersion,
       "pnSysSerialNumber": pnSysSerialNumber,
       "pnSysTimeZoneOffset": pnSysTimeZoneOffset,
       "pnSysDaylightSaving": pnSysDaylightSaving,
       "pnChassis": pnChassis,
       "pnChassisType": pnChassisType,
       "pnCommonEvents": pnCommonEvents,
       "pnCommonEventObjs": pnCommonEventObjs,
       "pnCommonEventDescr": pnCommonEventDescr,
       "pnCommonEventEvents": pnCommonEventEvents,
       "pnCommonEventEventsV2": pnCommonEventEventsV2,
       "pnCommonEventInFailSafeMode": pnCommonEventInFailSafeMode,
       "pnCommonEventPowerSupplyFailure": pnCommonEventPowerSupplyFailure,
       "pnCommonEventPowerSupplyOk": pnCommonEventPowerSupplyOk,
       "pnCommonEventLicenseExpired": pnCommonEventLicenseExpired,
       "pnCommonEventThruputLimitExceeded": pnCommonEventThruputLimitExceeded,
       "pnCommonEventLicenseWillExpire": pnCommonEventLicenseWillExpire,
       "pnCommonEventLoginFailure": pnCommonEventLoginFailure,
       "pnCommonEventFaultTolerantPassThrough": pnCommonEventFaultTolerantPassThrough,
       "pnCommonEventFanFailure": pnCommonEventFanFailure,
       "pnCommonEventFanSpeedVariation": pnCommonEventFanSpeedVariation,
       "pnCommonEventFanOk": pnCommonEventFanOk,
       "pnCommonEventInterfaceSpeedMismatch": pnCommonEventInterfaceSpeedMismatch,
       "pnCommonEventInterfaceSpeedOk": pnCommonEventInterfaceSpeedOk,
       "pnCommonEventInterfaceDuplexMismatch": pnCommonEventInterfaceDuplexMismatch,
       "pnCommonEventIpsecSecurityAssociationAdded": pnCommonEventIpsecSecurityAssociationAdded,
       "pnCommonEventIpsecSecurityAssociationExpired": pnCommonEventIpsecSecurityAssociationExpired,
       "pnCommonEventIpsecSecurityAssociationDeleted": pnCommonEventIpsecSecurityAssociationDeleted}
)
