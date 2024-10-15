# SNMP MIB module (ADTRAN-AOS-NETWORK-SYNC-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ADTRAN-AOS-NETWORK-SYNC-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:34:09 2024
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

(adGenAOSCommon,
 adGenAOSConformance) = mibBuilder.importSymbols(
    "ADTRAN-AOS",
    "adGenAOSCommon",
    "adGenAOSConformance")

(adIdentity,) = mibBuilder.importSymbols(
    "ADTRAN-MIB",
    "adIdentity")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY

adGenAOSNetSyncMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 53, 1, 9)
)
adGenAOSNetSyncMib.setRevisions(
        ("2015-09-18 00:00",
         "2014-03-05 00:00",
         "2013-11-07 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_AdGenAOSNetSync_ObjectIdentity = ObjectIdentity
adGenAOSNetSync = _AdGenAOSNetSync_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 9)
)
_AdGenAOSNetSyncTrap_ObjectIdentity = ObjectIdentity
adGenAOSNetSyncTrap = _AdGenAOSNetSyncTrap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 9, 0)
)
_AdGenAOSNetSyncTrapControl_ObjectIdentity = ObjectIdentity
adGenAOSNetSyncTrapControl = _AdGenAOSNetSyncTrapControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 9, 1)
)


class _AdGenAOSNetSyncTrapEnable_Type(Integer32):
    """Custom type adGenAOSNetSyncTrapEnable based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_AdGenAOSNetSyncTrapEnable_Type.__name__ = "Integer32"
_AdGenAOSNetSyncTrapEnable_Object = MibScalar
adGenAOSNetSyncTrapEnable = _AdGenAOSNetSyncTrapEnable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 9, 1, 1),
    _AdGenAOSNetSyncTrapEnable_Type()
)
adGenAOSNetSyncTrapEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenAOSNetSyncTrapEnable.setStatus("current")
_AdGenAOSNetSyncInfo_ObjectIdentity = ObjectIdentity
adGenAOSNetSyncInfo = _AdGenAOSNetSyncInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 9, 2)
)


class _AdGenAOSNetSyncLTIState_Type(Integer32):
    """Custom type adGenAOSNetSyncLTIState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 2),
          ("inactive", 1))
    )


_AdGenAOSNetSyncLTIState_Type.__name__ = "Integer32"
_AdGenAOSNetSyncLTIState_Object = MibScalar
adGenAOSNetSyncLTIState = _AdGenAOSNetSyncLTIState_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 9, 2, 1),
    _AdGenAOSNetSyncLTIState_Type()
)
adGenAOSNetSyncLTIState.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    adGenAOSNetSyncLTIState.setStatus("current")


class _AdGenAOSNetSyncClockNumber_Type(Integer32):
    """Custom type adGenAOSNetSyncClockNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("primary", 1),
          ("secondary", 2))
    )


_AdGenAOSNetSyncClockNumber_Type.__name__ = "Integer32"
_AdGenAOSNetSyncClockNumber_Object = MibScalar
adGenAOSNetSyncClockNumber = _AdGenAOSNetSyncClockNumber_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 9, 2, 2),
    _AdGenAOSNetSyncClockNumber_Type()
)
adGenAOSNetSyncClockNumber.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    adGenAOSNetSyncClockNumber.setStatus("current")
_AdGenAOSNetSyncClockDefectStatus_Type = Integer32
_AdGenAOSNetSyncClockDefectStatus_Object = MibScalar
adGenAOSNetSyncClockDefectStatus = _AdGenAOSNetSyncClockDefectStatus_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 9, 2, 3),
    _AdGenAOSNetSyncClockDefectStatus_Type()
)
adGenAOSNetSyncClockDefectStatus.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    adGenAOSNetSyncClockDefectStatus.setStatus("current")


class _AdGenAOSNetSyncT4SquelchState_Type(Integer32):
    """Custom type adGenAOSNetSyncT4SquelchState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 2),
          ("inactive", 1))
    )


_AdGenAOSNetSyncT4SquelchState_Type.__name__ = "Integer32"
_AdGenAOSNetSyncT4SquelchState_Object = MibScalar
adGenAOSNetSyncT4SquelchState = _AdGenAOSNetSyncT4SquelchState_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 9, 2, 4),
    _AdGenAOSNetSyncT4SquelchState_Type()
)
adGenAOSNetSyncT4SquelchState.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    adGenAOSNetSyncT4SquelchState.setStatus("current")
_AdGenAOSNetSyncConformance_ObjectIdentity = ObjectIdentity
adGenAOSNetSyncConformance = _AdGenAOSNetSyncConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 99, 18)
)
_AdGenAOSNetSyncGroups_ObjectIdentity = ObjectIdentity
adGenAOSNetSyncGroups = _AdGenAOSNetSyncGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 99, 18, 1)
)
_AdGenAOSNetSyncCompliances_ObjectIdentity = ObjectIdentity
adGenAOSNetSyncCompliances = _AdGenAOSNetSyncCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 99, 18, 2)
)

# Managed Objects groups

adGenAOSNetSyncTrapCfgGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 99, 18, 1, 1)
)
adGenAOSNetSyncTrapCfgGroup.setObjects(
    ("ADTRAN-AOS-NETWORK-SYNC-MIB", "adGenAOSNetSyncTrapEnable")
)
if mibBuilder.loadTexts:
    adGenAOSNetSyncTrapCfgGroup.setStatus("current")

adGenAOSNetSyncTrapGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 99, 18, 1, 2)
)
adGenAOSNetSyncTrapGroup.setObjects(
      *(("ADTRAN-AOS-NETWORK-SYNC-MIB", "adGenAOSNetSyncLTIState"),
        ("ADTRAN-AOS-NETWORK-SYNC-MIB", "adGenAOSNetSyncClockNumber"),
        ("ADTRAN-AOS-NETWORK-SYNC-MIB", "adGenAOSNetSyncClockDefectStatus"),
        ("ADTRAN-AOS-NETWORK-SYNC-MIB", "adGenAOSNetSyncT4SquelchState"))
)
if mibBuilder.loadTexts:
    adGenAOSNetSyncTrapGroup.setStatus("current")


# Notification objects

adGenAOSNetSyncClockDefectTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 9, 0, 1)
)
adGenAOSNetSyncClockDefectTrap.setObjects(
      *(("ADTRAN-AOS-NETWORK-SYNC-MIB", "adGenAOSNetSyncClockNumber"),
        ("ADTRAN-AOS-NETWORK-SYNC-MIB", "adGenAOSNetSyncClockDefectStatus"))
)
if mibBuilder.loadTexts:
    adGenAOSNetSyncClockDefectTrap.setStatus(
        "current"
    )

adGenAOSNetSyncLTIStateChangeTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 9, 0, 2)
)
adGenAOSNetSyncLTIStateChangeTrap.setObjects(
    ("ADTRAN-AOS-NETWORK-SYNC-MIB", "adGenAOSNetSyncLTIState")
)
if mibBuilder.loadTexts:
    adGenAOSNetSyncLTIStateChangeTrap.setStatus(
        "current"
    )

adGenAOSNetSyncT4SquelchStateChangeTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 9, 0, 3)
)
adGenAOSNetSyncT4SquelchStateChangeTrap.setObjects(
    ("ADTRAN-AOS-NETWORK-SYNC-MIB", "adGenAOSNetSyncT4SquelchState")
)
if mibBuilder.loadTexts:
    adGenAOSNetSyncT4SquelchStateChangeTrap.setStatus(
        "current"
    )


# Notifications groups

adGenAOSNetSyncNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 99, 18, 1, 3)
)
adGenAOSNetSyncNotificationGroup.setObjects(
      *(("ADTRAN-AOS-NETWORK-SYNC-MIB", "adGenAOSNetSyncClockDefectTrap"),
        ("ADTRAN-AOS-NETWORK-SYNC-MIB", "adGenAOSNetSyncLTIStateChangeTrap"),
        ("ADTRAN-AOS-NETWORK-SYNC-MIB", "adGenAOSNetSyncT4SquelchStateChangeTrap"))
)
if mibBuilder.loadTexts:
    adGenAOSNetSyncNotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

adGenAOSNetSyncFullCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 99, 18, 2, 1)
)
if mibBuilder.loadTexts:
    adGenAOSNetSyncFullCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ADTRAN-AOS-NETWORK-SYNC-MIB",
    **{"adGenAOSNetSync": adGenAOSNetSync,
       "adGenAOSNetSyncTrap": adGenAOSNetSyncTrap,
       "adGenAOSNetSyncClockDefectTrap": adGenAOSNetSyncClockDefectTrap,
       "adGenAOSNetSyncLTIStateChangeTrap": adGenAOSNetSyncLTIStateChangeTrap,
       "adGenAOSNetSyncT4SquelchStateChangeTrap": adGenAOSNetSyncT4SquelchStateChangeTrap,
       "adGenAOSNetSyncTrapControl": adGenAOSNetSyncTrapControl,
       "adGenAOSNetSyncTrapEnable": adGenAOSNetSyncTrapEnable,
       "adGenAOSNetSyncInfo": adGenAOSNetSyncInfo,
       "adGenAOSNetSyncLTIState": adGenAOSNetSyncLTIState,
       "adGenAOSNetSyncClockNumber": adGenAOSNetSyncClockNumber,
       "adGenAOSNetSyncClockDefectStatus": adGenAOSNetSyncClockDefectStatus,
       "adGenAOSNetSyncT4SquelchState": adGenAOSNetSyncT4SquelchState,
       "adGenAOSNetSyncConformance": adGenAOSNetSyncConformance,
       "adGenAOSNetSyncGroups": adGenAOSNetSyncGroups,
       "adGenAOSNetSyncTrapCfgGroup": adGenAOSNetSyncTrapCfgGroup,
       "adGenAOSNetSyncTrapGroup": adGenAOSNetSyncTrapGroup,
       "adGenAOSNetSyncNotificationGroup": adGenAOSNetSyncNotificationGroup,
       "adGenAOSNetSyncCompliances": adGenAOSNetSyncCompliances,
       "adGenAOSNetSyncFullCompliance": adGenAOSNetSyncFullCompliance,
       "adGenAOSNetSyncMib": adGenAOSNetSyncMib}
)
