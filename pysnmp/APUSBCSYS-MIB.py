# SNMP MIB module (APUSBCSYS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/APUSBCSYS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:40:11 2024
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

(acmepacketMgmt,) = mibBuilder.importSymbols(
    "ACMEPACKET-SMI",
    "acmepacketMgmt")

(ApHardwareModuleFamily,
 ApPhyPortType,
 ApPresence,
 ApRedundancyState,
 ApServerStatus) = mibBuilder.importSymbols(
    "ACMEPACKET-TC",
    "ApHardwareModuleFamily",
    "ApPhyPortType",
    "ApPresence",
    "ApRedundancyState",
    "ApServerStatus")

(InetAddress,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType")

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

apUsbcSysModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9148, 3, 17)
)
apUsbcSysModule.setRevisions(
        ("2012-03-07 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class UsbcSysPercent(Gauge32, TextualConvention):
    status = "current"
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )



# MIB Managed Objects in the order of their OIDs

_ApUsbcSysMIBObjects_ObjectIdentity = ObjectIdentity
apUsbcSysMIBObjects = _ApUsbcSysMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9148, 3, 17, 1)
)
_ApUsbcSysObjects_ObjectIdentity = ObjectIdentity
apUsbcSysObjects = _ApUsbcSysObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9148, 3, 17, 1, 1)
)
_ApUsbcSysCpuUtilAll_Type = UsbcSysPercent
_ApUsbcSysCpuUtilAll_Object = MibScalar
apUsbcSysCpuUtilAll = _ApUsbcSysCpuUtilAll_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 17, 1, 1, 1),
    _ApUsbcSysCpuUtilAll_Type()
)
apUsbcSysCpuUtilAll.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apUsbcSysCpuUtilAll.setStatus("current")


class _ApUsbcSysCpuCount_Type(Integer32):
    """Custom type apUsbcSysCpuCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_ApUsbcSysCpuCount_Type.__name__ = "Integer32"
_ApUsbcSysCpuCount_Object = MibScalar
apUsbcSysCpuCount = _ApUsbcSysCpuCount_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 17, 1, 1, 2),
    _ApUsbcSysCpuCount_Type()
)
apUsbcSysCpuCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apUsbcSysCpuCount.setStatus("current")
_ApUsbcSysCpuSpeedMHz_Type = Integer32
_ApUsbcSysCpuSpeedMHz_Object = MibScalar
apUsbcSysCpuSpeedMHz = _ApUsbcSysCpuSpeedMHz_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 17, 1, 1, 3),
    _ApUsbcSysCpuSpeedMHz_Type()
)
apUsbcSysCpuSpeedMHz.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apUsbcSysCpuSpeedMHz.setStatus("current")
_ApUsbcSysMemSzMB_Type = Integer32
_ApUsbcSysMemSzMB_Object = MibScalar
apUsbcSysMemSzMB = _ApUsbcSysMemSzMB_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 17, 1, 1, 4),
    _ApUsbcSysMemSzMB_Type()
)
apUsbcSysMemSzMB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apUsbcSysMemSzMB.setStatus("current")
_ApUsbcSysMemSzGB_Type = Integer32
_ApUsbcSysMemSzGB_Object = MibScalar
apUsbcSysMemSzGB = _ApUsbcSysMemSzGB_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 17, 1, 1, 5),
    _ApUsbcSysMemSzGB_Type()
)
apUsbcSysMemSzGB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apUsbcSysMemSzGB.setStatus("current")
_ApUsbcSysAppMemUtil_Type = UsbcSysPercent
_ApUsbcSysAppMemUtil_Object = MibScalar
apUsbcSysAppMemUtil = _ApUsbcSysAppMemUtil_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 17, 1, 1, 6),
    _ApUsbcSysAppMemUtil_Type()
)
apUsbcSysAppMemUtil.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apUsbcSysAppMemUtil.setStatus("current")
_ApUsbcSysKernelMemUtil_Type = UsbcSysPercent
_ApUsbcSysKernelMemUtil_Object = MibScalar
apUsbcSysKernelMemUtil = _ApUsbcSysKernelMemUtil_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 17, 1, 1, 7),
    _ApUsbcSysKernelMemUtil_Type()
)
apUsbcSysKernelMemUtil.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apUsbcSysKernelMemUtil.setStatus("current")
_ApUsbcSysMyBogoMips_Type = Integer32
_ApUsbcSysMyBogoMips_Object = MibScalar
apUsbcSysMyBogoMips = _ApUsbcSysMyBogoMips_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 17, 1, 1, 8),
    _ApUsbcSysMyBogoMips_Type()
)
apUsbcSysMyBogoMips.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apUsbcSysMyBogoMips.setStatus("current")
_ApUsbcSysAllBogoMips_Type = Integer32
_ApUsbcSysAllBogoMips_Object = MibScalar
apUsbcSysAllBogoMips = _ApUsbcSysAllBogoMips_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 17, 1, 1, 9),
    _ApUsbcSysAllBogoMips_Type()
)
apUsbcSysAllBogoMips.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apUsbcSysAllBogoMips.setStatus("current")
_ApUsbcSysCpuTblObjects_ObjectIdentity = ObjectIdentity
apUsbcSysCpuTblObjects = _ApUsbcSysCpuTblObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9148, 3, 17, 1, 1, 10)
)
_ApUsbcSysCpuTable_Object = MibTable
apUsbcSysCpuTable = _ApUsbcSysCpuTable_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 17, 1, 1, 10, 1)
)
if mibBuilder.loadTexts:
    apUsbcSysCpuTable.setStatus("current")
_ApUsbcSysCpuEntry_Object = MibTableRow
apUsbcSysCpuEntry = _ApUsbcSysCpuEntry_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 17, 1, 1, 10, 1, 1)
)
apUsbcSysCpuEntry.setIndexNames(
    (0, "APUSBCSYS-MIB", "apUsbcSysCpuNum"),
)
if mibBuilder.loadTexts:
    apUsbcSysCpuEntry.setStatus("current")


class _ApUsbcSysCpuNum_Type(Integer32):
    """Custom type apUsbcSysCpuNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_ApUsbcSysCpuNum_Type.__name__ = "Integer32"
_ApUsbcSysCpuNum_Object = MibTableColumn
apUsbcSysCpuNum = _ApUsbcSysCpuNum_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 17, 1, 1, 10, 1, 1, 1),
    _ApUsbcSysCpuNum_Type()
)
apUsbcSysCpuNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apUsbcSysCpuNum.setStatus("current")
_ApUsbcSysCpuUtil_Type = UsbcSysPercent
_ApUsbcSysCpuUtil_Object = MibTableColumn
apUsbcSysCpuUtil = _ApUsbcSysCpuUtil_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 17, 1, 1, 10, 1, 1, 2),
    _ApUsbcSysCpuUtil_Type()
)
apUsbcSysCpuUtil.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apUsbcSysCpuUtil.setStatus("current")
_ApUsbcSysNotificationObjects_ObjectIdentity = ObjectIdentity
apUsbcSysNotificationObjects = _ApUsbcSysNotificationObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9148, 3, 17, 2)
)
_ApUsbcSysNotifObjects_ObjectIdentity = ObjectIdentity
apUsbcSysNotifObjects = _ApUsbcSysNotifObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9148, 3, 17, 2, 1)
)
_ApUsbcSysNotifPrefix_ObjectIdentity = ObjectIdentity
apUsbcSysNotifPrefix = _ApUsbcSysNotifPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9148, 3, 17, 2, 2)
)
_ApUsbcSysCpuNotifications_ObjectIdentity = ObjectIdentity
apUsbcSysCpuNotifications = _ApUsbcSysCpuNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9148, 3, 17, 2, 2, 1, 0)
)
_ApUsbcSysConformance_ObjectIdentity = ObjectIdentity
apUsbcSysConformance = _ApUsbcSysConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9148, 3, 17, 3)
)
_ApUsbcSysObjectGroups_ObjectIdentity = ObjectIdentity
apUsbcSysObjectGroups = _ApUsbcSysObjectGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9148, 3, 17, 3, 1)
)
_ApUsbcSysNotificationGroups_ObjectIdentity = ObjectIdentity
apUsbcSysNotificationGroups = _ApUsbcSysNotificationGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9148, 3, 17, 3, 2)
)

# Managed Objects groups

apUsbcSysGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9148, 3, 17, 3, 1, 1)
)
apUsbcSysGroup.setObjects(
      *(("APUSBCSYS-MIB", "apUsbcSysCpuUtilAll"),
        ("APUSBCSYS-MIB", "apUsbcSysCpuCount"),
        ("APUSBCSYS-MIB", "apUsbcSysCpuSpeedMHz"),
        ("APUSBCSYS-MIB", "apUsbcSysMemSzMB"),
        ("APUSBCSYS-MIB", "apUsbcSysMemSzGB"),
        ("APUSBCSYS-MIB", "apUsbcSysAppMemUtil"),
        ("APUSBCSYS-MIB", "apUsbcSysKernelMemUtil"),
        ("APUSBCSYS-MIB", "apUsbcSysMyBogoMips"),
        ("APUSBCSYS-MIB", "apUsbcSysAllBogoMips"))
)
if mibBuilder.loadTexts:
    apUsbcSysGroup.setStatus("current")

apUsbcSysCpuTblGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9148, 3, 17, 3, 1, 2)
)
apUsbcSysCpuTblGroup.setObjects(
      *(("APUSBCSYS-MIB", "apUsbcSysCpuNum"),
        ("APUSBCSYS-MIB", "apUsbcSysCpuUtil"))
)
if mibBuilder.loadTexts:
    apUsbcSysCpuTblGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "APUSBCSYS-MIB",
    **{"UsbcSysPercent": UsbcSysPercent,
       "apUsbcSysModule": apUsbcSysModule,
       "apUsbcSysMIBObjects": apUsbcSysMIBObjects,
       "apUsbcSysObjects": apUsbcSysObjects,
       "apUsbcSysCpuUtilAll": apUsbcSysCpuUtilAll,
       "apUsbcSysCpuCount": apUsbcSysCpuCount,
       "apUsbcSysCpuSpeedMHz": apUsbcSysCpuSpeedMHz,
       "apUsbcSysMemSzMB": apUsbcSysMemSzMB,
       "apUsbcSysMemSzGB": apUsbcSysMemSzGB,
       "apUsbcSysAppMemUtil": apUsbcSysAppMemUtil,
       "apUsbcSysKernelMemUtil": apUsbcSysKernelMemUtil,
       "apUsbcSysMyBogoMips": apUsbcSysMyBogoMips,
       "apUsbcSysAllBogoMips": apUsbcSysAllBogoMips,
       "apUsbcSysCpuTblObjects": apUsbcSysCpuTblObjects,
       "apUsbcSysCpuTable": apUsbcSysCpuTable,
       "apUsbcSysCpuEntry": apUsbcSysCpuEntry,
       "apUsbcSysCpuNum": apUsbcSysCpuNum,
       "apUsbcSysCpuUtil": apUsbcSysCpuUtil,
       "apUsbcSysNotificationObjects": apUsbcSysNotificationObjects,
       "apUsbcSysNotifObjects": apUsbcSysNotifObjects,
       "apUsbcSysNotifPrefix": apUsbcSysNotifPrefix,
       "apUsbcSysCpuNotifications": apUsbcSysCpuNotifications,
       "apUsbcSysConformance": apUsbcSysConformance,
       "apUsbcSysObjectGroups": apUsbcSysObjectGroups,
       "apUsbcSysGroup": apUsbcSysGroup,
       "apUsbcSysCpuTblGroup": apUsbcSysCpuTblGroup,
       "apUsbcSysNotificationGroups": apUsbcSysNotificationGroups}
)
