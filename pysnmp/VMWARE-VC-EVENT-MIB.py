# SNMP MIB module (VMWARE-VC-EVENT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/VMWARE-VC-EVENT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:12:59 2024
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

(DisplayString,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")

(vmwVC,) = mibBuilder.importSymbols(
    "VMWARE-PRODUCTS-MIB",
    "vmwVC")

(VmwLongSnmpAdminString,) = mibBuilder.importSymbols(
    "VMWARE-TC-MIB",
    "VmwLongSnmpAdminString")


# MODULE-IDENTITY

vmwVCMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6876, 4, 3, 1)
)
vmwVCMIB.setRevisions(
        ("2009-12-15 00:00",
         "2009-09-08 00:00",
         "2009-05-27 00:00",
         "2009-04-06 00:00",
         "2009-03-17 00:00",
         "2008-02-22 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_VmwVCNotifications_ObjectIdentity = ObjectIdentity
vmwVCNotifications = _VmwVCNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6876, 4, 3, 0)
)
_VmwVCMIBConformance_ObjectIdentity = ObjectIdentity
vmwVCMIBConformance = _VmwVCMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6876, 4, 3, 1, 2)
)
_VmwVCMIBCompliances_ObjectIdentity = ObjectIdentity
vmwVCMIBCompliances = _VmwVCMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6876, 4, 3, 1, 2, 1)
)
_VmwVCMIBGroups_ObjectIdentity = ObjectIdentity
vmwVCMIBGroups = _VmwVCMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6876, 4, 3, 1, 2, 2)
)
_VmwVpxdTrapType_Type = SnmpAdminString
_VmwVpxdTrapType_Object = MibScalar
vmwVpxdTrapType = _VmwVpxdTrapType_Object(
    (1, 3, 6, 1, 4, 1, 6876, 4, 3, 301),
    _VmwVpxdTrapType_Type()
)
vmwVpxdTrapType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    vmwVpxdTrapType.setStatus("obsolete")
_VmwVpxdHostName_Type = SnmpAdminString
_VmwVpxdHostName_Object = MibScalar
vmwVpxdHostName = _VmwVpxdHostName_Object(
    (1, 3, 6, 1, 4, 1, 6876, 4, 3, 302),
    _VmwVpxdHostName_Type()
)
vmwVpxdHostName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    vmwVpxdHostName.setStatus("obsolete")
_VmwVpxdVMName_Type = SnmpAdminString
_VmwVpxdVMName_Object = MibScalar
vmwVpxdVMName = _VmwVpxdVMName_Object(
    (1, 3, 6, 1, 4, 1, 6876, 4, 3, 303),
    _VmwVpxdVMName_Type()
)
vmwVpxdVMName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    vmwVpxdVMName.setStatus("obsolete")
_VmwVpxdOldStatus_Type = SnmpAdminString
_VmwVpxdOldStatus_Object = MibScalar
vmwVpxdOldStatus = _VmwVpxdOldStatus_Object(
    (1, 3, 6, 1, 4, 1, 6876, 4, 3, 304),
    _VmwVpxdOldStatus_Type()
)
vmwVpxdOldStatus.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    vmwVpxdOldStatus.setStatus("current")
_VmwVpxdNewStatus_Type = SnmpAdminString
_VmwVpxdNewStatus_Object = MibScalar
vmwVpxdNewStatus = _VmwVpxdNewStatus_Object(
    (1, 3, 6, 1, 4, 1, 6876, 4, 3, 305),
    _VmwVpxdNewStatus_Type()
)
vmwVpxdNewStatus.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    vmwVpxdNewStatus.setStatus("current")
_VmwVpxdObjValue_Type = VmwLongSnmpAdminString
_VmwVpxdObjValue_Object = MibScalar
vmwVpxdObjValue = _VmwVpxdObjValue_Object(
    (1, 3, 6, 1, 4, 1, 6876, 4, 3, 306),
    _VmwVpxdObjValue_Type()
)
vmwVpxdObjValue.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    vmwVpxdObjValue.setStatus("current")
_VmwVpxdTargetObj_Type = SnmpAdminString
_VmwVpxdTargetObj_Object = MibScalar
vmwVpxdTargetObj = _VmwVpxdTargetObj_Object(
    (1, 3, 6, 1, 4, 1, 6876, 4, 3, 307),
    _VmwVpxdTargetObj_Type()
)
vmwVpxdTargetObj.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    vmwVpxdTargetObj.setStatus("current")


class _VmwVpxdTargetObjType_Type(Integer32):
    """Custom type vmwVpxdTargetObjType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("host", 2),
          ("other", 4),
          ("unknown", 1),
          ("vm", 3))
    )


_VmwVpxdTargetObjType_Type.__name__ = "Integer32"
_VmwVpxdTargetObjType_Object = MibScalar
vmwVpxdTargetObjType = _VmwVpxdTargetObjType_Object(
    (1, 3, 6, 1, 4, 1, 6876, 4, 3, 308),
    _VmwVpxdTargetObjType_Type()
)
vmwVpxdTargetObjType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    vmwVpxdTargetObjType.setStatus("current")

# Managed Objects groups

vmwVCAlarmInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6876, 4, 3, 1, 2, 2, 1)
)
vmwVCAlarmInfoGroup.setObjects(
      *(("VMWARE-VC-EVENT-MIB", "vmwVpxdTrapType"),
        ("VMWARE-VC-EVENT-MIB", "vmwVpxdHostName"),
        ("VMWARE-VC-EVENT-MIB", "vmwVpxdVMName"),
        ("VMWARE-VC-EVENT-MIB", "vmwVpxdOldStatus"),
        ("VMWARE-VC-EVENT-MIB", "vmwVpxdNewStatus"),
        ("VMWARE-VC-EVENT-MIB", "vmwVpxdObjValue"))
)
if mibBuilder.loadTexts:
    vmwVCAlarmInfoGroup.setStatus("obsolete")

vmwVCAlarmGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6876, 4, 3, 1, 2, 2, 3)
)
vmwVCAlarmGroup.setObjects(
      *(("VMWARE-VC-EVENT-MIB", "vmwVpxdTargetObjType"),
        ("VMWARE-VC-EVENT-MIB", "vmwVpxdOldStatus"),
        ("VMWARE-VC-EVENT-MIB", "vmwVpxdNewStatus"),
        ("VMWARE-VC-EVENT-MIB", "vmwVpxdObjValue"),
        ("VMWARE-VC-EVENT-MIB", "vmwVpxdTargetObj"))
)
if mibBuilder.loadTexts:
    vmwVCAlarmGroup.setStatus("current")


# Notification objects

vpxdAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 4, 3, 0, 201)
)
vpxdAlarm.setObjects(
      *(("VMWARE-VC-EVENT-MIB", "vmwVpxdTrapType"),
        ("VMWARE-VC-EVENT-MIB", "vmwVpxdHostName"),
        ("VMWARE-VC-EVENT-MIB", "vmwVpxdVMName"),
        ("VMWARE-VC-EVENT-MIB", "vmwVpxdOldStatus"),
        ("VMWARE-VC-EVENT-MIB", "vmwVpxdNewStatus"),
        ("VMWARE-VC-EVENT-MIB", "vmwVpxdObjValue"))
)
if mibBuilder.loadTexts:
    vpxdAlarm.setStatus(
        "obsolete"
    )

vpxdDiagnostic = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 4, 3, 0, 202)
)
if mibBuilder.loadTexts:
    vpxdDiagnostic.setStatus(
        "current"
    )

vpxdAlarmInfo = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 4, 3, 0, 203)
)
vpxdAlarmInfo.setObjects(
      *(("VMWARE-VC-EVENT-MIB", "vmwVpxdTargetObjType"),
        ("VMWARE-VC-EVENT-MIB", "vmwVpxdOldStatus"),
        ("VMWARE-VC-EVENT-MIB", "vmwVpxdNewStatus"),
        ("VMWARE-VC-EVENT-MIB", "vmwVpxdObjValue"),
        ("VMWARE-VC-EVENT-MIB", "vmwVpxdTargetObj"))
)
if mibBuilder.loadTexts:
    vpxdAlarmInfo.setStatus(
        "current"
    )


# Notifications groups

vmwVCNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6876, 4, 3, 1, 2, 2, 2)
)
vmwVCNotificationGroup.setObjects(
      *(("VMWARE-VC-EVENT-MIB", "vpxdAlarm"),
        ("VMWARE-VC-EVENT-MIB", "vpxdDiagnostic"))
)
if mibBuilder.loadTexts:
    vmwVCNotificationGroup.setStatus(
        "obsolete"
    )

vmwVCAlarmNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6876, 4, 3, 1, 2, 2, 4)
)
vmwVCAlarmNotificationGroup.setObjects(
      *(("VMWARE-VC-EVENT-MIB", "vpxdAlarmInfo"),
        ("VMWARE-VC-EVENT-MIB", "vpxdDiagnostic"))
)
if mibBuilder.loadTexts:
    vmwVCAlarmNotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

vmwVCMIBBasicCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6876, 4, 3, 1, 2, 1, 2)
)
if mibBuilder.loadTexts:
    vmwVCMIBBasicCompliance.setStatus(
        "obsolete"
    )

vmwVCMIBBasicComplianceRev2 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6876, 4, 3, 1, 2, 1, 3)
)
if mibBuilder.loadTexts:
    vmwVCMIBBasicComplianceRev2.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "VMWARE-VC-EVENT-MIB",
    **{"vmwVCNotifications": vmwVCNotifications,
       "vpxdAlarm": vpxdAlarm,
       "vpxdDiagnostic": vpxdDiagnostic,
       "vpxdAlarmInfo": vpxdAlarmInfo,
       "vmwVCMIB": vmwVCMIB,
       "vmwVCMIBConformance": vmwVCMIBConformance,
       "vmwVCMIBCompliances": vmwVCMIBCompliances,
       "vmwVCMIBBasicCompliance": vmwVCMIBBasicCompliance,
       "vmwVCMIBBasicComplianceRev2": vmwVCMIBBasicComplianceRev2,
       "vmwVCMIBGroups": vmwVCMIBGroups,
       "vmwVCAlarmInfoGroup": vmwVCAlarmInfoGroup,
       "vmwVCNotificationGroup": vmwVCNotificationGroup,
       "vmwVCAlarmGroup": vmwVCAlarmGroup,
       "vmwVCAlarmNotificationGroup": vmwVCAlarmNotificationGroup,
       "vmwVpxdTrapType": vmwVpxdTrapType,
       "vmwVpxdHostName": vmwVpxdHostName,
       "vmwVpxdVMName": vmwVpxdVMName,
       "vmwVpxdOldStatus": vmwVpxdOldStatus,
       "vmwVpxdNewStatus": vmwVpxdNewStatus,
       "vmwVpxdObjValue": vmwVpxdObjValue,
       "vmwVpxdTargetObj": vmwVpxdTargetObj,
       "vmwVpxdTargetObjType": vmwVpxdTargetObjType}
)
