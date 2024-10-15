# SNMP MIB module (CISCO-CDSTV-BWMGR-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-CDSTV-BWMGR-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:57:16 2024
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

(TimeIntervalSec,) = mibBuilder.importSymbols(
    "CISCO-TC",
    "TimeIntervalSec")

(InetAddress,
 InetAddressType,
 InetPortNumber) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType",
    "InetPortNumber")

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

ciscoCdstvBwmgrMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 749)
)
ciscoCdstvBwmgrMIB.setRevisions(
        ("2010-06-24 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CiscoCdstvBWMgrMIBNotifs_ObjectIdentity = ObjectIdentity
ciscoCdstvBWMgrMIBNotifs = _CiscoCdstvBWMgrMIBNotifs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 749, 0)
)
_CiscoCdstvBWMgrMIBObjects_ObjectIdentity = ObjectIdentity
ciscoCdstvBWMgrMIBObjects = _CiscoCdstvBWMgrMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 749, 1)
)
_CdstvBWMgrAddressType_Type = InetAddressType
_CdstvBWMgrAddressType_Object = MibScalar
cdstvBWMgrAddressType = _CdstvBWMgrAddressType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 749, 1, 1),
    _CdstvBWMgrAddressType_Type()
)
cdstvBWMgrAddressType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdstvBWMgrAddressType.setStatus("current")
_CdstvBWMgrAddress_Type = InetAddress
_CdstvBWMgrAddress_Object = MibScalar
cdstvBWMgrAddress = _CdstvBWMgrAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 749, 1, 2),
    _CdstvBWMgrAddress_Type()
)
cdstvBWMgrAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdstvBWMgrAddress.setStatus("current")


class _CdstvBWMgrPort_Type(InetPortNumber):
    """Custom type cdstvBWMgrPort based on InetPortNumber"""
    defaultValue = 7791

    subtypeSpec = InetPortNumber.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CdstvBWMgrPort_Type.__name__ = "InetPortNumber"
_CdstvBWMgrPort_Object = MibScalar
cdstvBWMgrPort = _CdstvBWMgrPort_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 749, 1, 3),
    _CdstvBWMgrPort_Type()
)
cdstvBWMgrPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdstvBWMgrPort.setStatus("current")


class _CdstvBWMgrDatabaseThreadPool_Type(Unsigned32):
    """Custom type cdstvBWMgrDatabaseThreadPool based on Unsigned32"""
    defaultValue = 10

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10000),
    )


_CdstvBWMgrDatabaseThreadPool_Type.__name__ = "Unsigned32"
_CdstvBWMgrDatabaseThreadPool_Object = MibScalar
cdstvBWMgrDatabaseThreadPool = _CdstvBWMgrDatabaseThreadPool_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 749, 1, 4),
    _CdstvBWMgrDatabaseThreadPool_Type()
)
cdstvBWMgrDatabaseThreadPool.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdstvBWMgrDatabaseThreadPool.setStatus("current")


class _CdstvBWMgrServerThreadPool_Type(Unsigned32):
    """Custom type cdstvBWMgrServerThreadPool based on Unsigned32"""
    defaultValue = 5

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10000),
    )


_CdstvBWMgrServerThreadPool_Type.__name__ = "Unsigned32"
_CdstvBWMgrServerThreadPool_Object = MibScalar
cdstvBWMgrServerThreadPool = _CdstvBWMgrServerThreadPool_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 749, 1, 5),
    _CdstvBWMgrServerThreadPool_Type()
)
cdstvBWMgrServerThreadPool.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdstvBWMgrServerThreadPool.setStatus("current")


class _CdstvBWMgrSyncThreadPool_Type(Unsigned32):
    """Custom type cdstvBWMgrSyncThreadPool based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10000),
    )


_CdstvBWMgrSyncThreadPool_Type.__name__ = "Unsigned32"
_CdstvBWMgrSyncThreadPool_Object = MibScalar
cdstvBWMgrSyncThreadPool = _CdstvBWMgrSyncThreadPool_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 749, 1, 6),
    _CdstvBWMgrSyncThreadPool_Type()
)
cdstvBWMgrSyncThreadPool.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdstvBWMgrSyncThreadPool.setStatus("current")


class _CdstvBWMgrSyncAlarm_Type(TimeIntervalSec):
    """Custom type cdstvBWMgrSyncAlarm based on TimeIntervalSec"""
    defaultValue = 864000

    subtypeSpec = TimeIntervalSec.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2400, 4294967295),
    )


_CdstvBWMgrSyncAlarm_Type.__name__ = "TimeIntervalSec"
_CdstvBWMgrSyncAlarm_Object = MibScalar
cdstvBWMgrSyncAlarm = _CdstvBWMgrSyncAlarm_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 749, 1, 7),
    _CdstvBWMgrSyncAlarm_Type()
)
cdstvBWMgrSyncAlarm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdstvBWMgrSyncAlarm.setStatus("current")
if mibBuilder.loadTexts:
    cdstvBWMgrSyncAlarm.setUnits("seconds")
_CiscoCdstvBWMgrMIBConform_ObjectIdentity = ObjectIdentity
ciscoCdstvBWMgrMIBConform = _CiscoCdstvBWMgrMIBConform_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 749, 2)
)
_CiscoCdstvBWMgrMIBCompliances_ObjectIdentity = ObjectIdentity
ciscoCdstvBWMgrMIBCompliances = _CiscoCdstvBWMgrMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 749, 2, 1)
)
_CiscoCdstvBWMgrMIBGroups_ObjectIdentity = ObjectIdentity
ciscoCdstvBWMgrMIBGroups = _CiscoCdstvBWMgrMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 749, 2, 2)
)

# Managed Objects groups

ciscoCdstvBWMgrMIBMainObjectGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 749, 2, 2, 1)
)
ciscoCdstvBWMgrMIBMainObjectGroup.setObjects(
      *(("CISCO-CDSTV-BWMGR-MIB", "cdstvBWMgrAddress"),
        ("CISCO-CDSTV-BWMGR-MIB", "cdstvBWMgrPort"),
        ("CISCO-CDSTV-BWMGR-MIB", "cdstvBWMgrDatabaseThreadPool"),
        ("CISCO-CDSTV-BWMGR-MIB", "cdstvBWMgrServerThreadPool"),
        ("CISCO-CDSTV-BWMGR-MIB", "cdstvBWMgrSyncThreadPool"),
        ("CISCO-CDSTV-BWMGR-MIB", "cdstvBWMgrSyncAlarm"),
        ("CISCO-CDSTV-BWMGR-MIB", "cdstvBWMgrAddressType"))
)
if mibBuilder.loadTexts:
    ciscoCdstvBWMgrMIBMainObjectGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

ciscoCdstvBWMgrMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 749, 2, 1, 1)
)
if mibBuilder.loadTexts:
    ciscoCdstvBWMgrMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-CDSTV-BWMGR-MIB",
    **{"ciscoCdstvBwmgrMIB": ciscoCdstvBwmgrMIB,
       "ciscoCdstvBWMgrMIBNotifs": ciscoCdstvBWMgrMIBNotifs,
       "ciscoCdstvBWMgrMIBObjects": ciscoCdstvBWMgrMIBObjects,
       "cdstvBWMgrAddressType": cdstvBWMgrAddressType,
       "cdstvBWMgrAddress": cdstvBWMgrAddress,
       "cdstvBWMgrPort": cdstvBWMgrPort,
       "cdstvBWMgrDatabaseThreadPool": cdstvBWMgrDatabaseThreadPool,
       "cdstvBWMgrServerThreadPool": cdstvBWMgrServerThreadPool,
       "cdstvBWMgrSyncThreadPool": cdstvBWMgrSyncThreadPool,
       "cdstvBWMgrSyncAlarm": cdstvBWMgrSyncAlarm,
       "ciscoCdstvBWMgrMIBConform": ciscoCdstvBWMgrMIBConform,
       "ciscoCdstvBWMgrMIBCompliances": ciscoCdstvBWMgrMIBCompliances,
       "ciscoCdstvBWMgrMIBCompliance": ciscoCdstvBWMgrMIBCompliance,
       "ciscoCdstvBWMgrMIBGroups": ciscoCdstvBWMgrMIBGroups,
       "ciscoCdstvBWMgrMIBMainObjectGroup": ciscoCdstvBWMgrMIBMainObjectGroup}
)
