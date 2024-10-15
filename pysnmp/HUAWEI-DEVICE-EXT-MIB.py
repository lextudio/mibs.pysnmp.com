# SNMP MIB module (HUAWEI-DEVICE-EXT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HUAWEI-DEVICE-EXT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:03:28 2024
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

(hwDatacomm,) = mibBuilder.importSymbols(
    "HUAWEI-MIB",
    "hwDatacomm")

(SnmpAdminString,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString")

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

(DateAndTime,
 DisplayString,
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

hwDeviceExt = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 188)
)
hwDeviceExt.setRevisions(
        ("2008-12-17 14:14",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_HwDeviceExtObject_ObjectIdentity = ObjectIdentity
hwDeviceExtObject = _HwDeviceExtObject_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 188, 1)
)
_HwDeviceEsn_Type = OctetString
_HwDeviceEsn_Object = MibScalar
hwDeviceEsn = _HwDeviceEsn_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 188, 1, 1),
    _HwDeviceEsn_Type()
)
hwDeviceEsn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwDeviceEsn.setStatus("current")
_HwPlatformName_Type = OctetString
_HwPlatformName_Object = MibScalar
hwPlatformName = _HwPlatformName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 188, 1, 2),
    _HwPlatformName_Type()
)
hwPlatformName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwPlatformName.setStatus("current")
_HwPlatformVersion_Type = OctetString
_HwPlatformVersion_Object = MibScalar
hwPlatformVersion = _HwPlatformVersion_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 188, 1, 3),
    _HwPlatformVersion_Type()
)
hwPlatformVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwPlatformVersion.setStatus("current")
_HwProductName_Type = OctetString
_HwProductName_Object = MibScalar
hwProductName = _HwProductName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 188, 1, 4),
    _HwProductName_Type()
)
hwProductName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwProductName.setStatus("current")
_HwProductVersion_Type = OctetString
_HwProductVersion_Object = MibScalar
hwProductVersion = _HwProductVersion_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 188, 1, 5),
    _HwProductVersion_Type()
)
hwProductVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwProductVersion.setStatus("current")
_HwDeviceExtConformance_ObjectIdentity = ObjectIdentity
hwDeviceExtConformance = _HwDeviceExtConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 188, 4)
)
_HwDeviceExtCompliances_ObjectIdentity = ObjectIdentity
hwDeviceExtCompliances = _HwDeviceExtCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 188, 4, 1)
)
_HwDeviceExtGroups_ObjectIdentity = ObjectIdentity
hwDeviceExtGroups = _HwDeviceExtGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 188, 4, 2)
)

# Managed Objects groups

hwDeviceInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 188, 4, 2, 1)
)
hwDeviceInfoGroup.setObjects(
      *(("HUAWEI-DEVICE-EXT-MIB", "hwDeviceEsn"),
        ("HUAWEI-DEVICE-EXT-MIB", "hwPlatformName"),
        ("HUAWEI-DEVICE-EXT-MIB", "hwPlatformVersion"),
        ("HUAWEI-DEVICE-EXT-MIB", "hwProductName"),
        ("HUAWEI-DEVICE-EXT-MIB", "hwProductVersion"))
)
if mibBuilder.loadTexts:
    hwDeviceInfoGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

hwDeviceExtCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 188, 4, 1, 1)
)
if mibBuilder.loadTexts:
    hwDeviceExtCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HUAWEI-DEVICE-EXT-MIB",
    **{"hwDeviceExt": hwDeviceExt,
       "hwDeviceExtObject": hwDeviceExtObject,
       "hwDeviceEsn": hwDeviceEsn,
       "hwPlatformName": hwPlatformName,
       "hwPlatformVersion": hwPlatformVersion,
       "hwProductName": hwProductName,
       "hwProductVersion": hwProductVersion,
       "hwDeviceExtConformance": hwDeviceExtConformance,
       "hwDeviceExtCompliances": hwDeviceExtCompliances,
       "hwDeviceExtCompliance": hwDeviceExtCompliance,
       "hwDeviceExtGroups": hwDeviceExtGroups,
       "hwDeviceInfoGroup": hwDeviceInfoGroup}
)
