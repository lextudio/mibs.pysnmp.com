# SNMP MIB module (VMWARE-TRAPS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/VMWARE-TRAPS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:12:57 2024
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
    "iso")

(DisplayString,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")

(vmwTraps,
 vmware) = mibBuilder.importSymbols(
    "VMWARE-ROOT-MIB",
    "vmwTraps",
    "vmware")

(vmDisplayName,) = mibBuilder.importSymbols(
    "VMWARE-VMINFO-MIB",
    "vmDisplayName")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_VmID_Type = Integer32
_VmID_Object = MibScalar
vmID = _VmID_Object(
    (1, 3, 6, 1, 4, 1, 6876, 50, 101),
    _VmID_Type()
)
vmID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vmID.setStatus("mandatory")
_VmConfigFile_Type = DisplayString
_VmConfigFile_Object = MibScalar
vmConfigFile = _VmConfigFile_Object(
    (1, 3, 6, 1, 4, 1, 6876, 50, 102),
    _VmConfigFile_Type()
)
vmConfigFile.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vmConfigFile.setStatus("mandatory")
_VpxdTrapType_Type = DisplayString
_VpxdTrapType_Object = MibScalar
vpxdTrapType = _VpxdTrapType_Object(
    (1, 3, 6, 1, 4, 1, 6876, 50, 301),
    _VpxdTrapType_Type()
)
vpxdTrapType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vpxdTrapType.setStatus("mandatory")
_VpxdHostName_Type = DisplayString
_VpxdHostName_Object = MibScalar
vpxdHostName = _VpxdHostName_Object(
    (1, 3, 6, 1, 4, 1, 6876, 50, 302),
    _VpxdHostName_Type()
)
vpxdHostName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vpxdHostName.setStatus("mandatory")
_VpxdVMName_Type = DisplayString
_VpxdVMName_Object = MibScalar
vpxdVMName = _VpxdVMName_Object(
    (1, 3, 6, 1, 4, 1, 6876, 50, 303),
    _VpxdVMName_Type()
)
vpxdVMName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vpxdVMName.setStatus("mandatory")
_VpxdOldStatus_Type = DisplayString
_VpxdOldStatus_Object = MibScalar
vpxdOldStatus = _VpxdOldStatus_Object(
    (1, 3, 6, 1, 4, 1, 6876, 50, 304),
    _VpxdOldStatus_Type()
)
vpxdOldStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vpxdOldStatus.setStatus("mandatory")
_VpxdNewStatus_Type = DisplayString
_VpxdNewStatus_Object = MibScalar
vpxdNewStatus = _VpxdNewStatus_Object(
    (1, 3, 6, 1, 4, 1, 6876, 50, 305),
    _VpxdNewStatus_Type()
)
vpxdNewStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vpxdNewStatus.setStatus("mandatory")
_VpxdObjValue_Type = DisplayString
_VpxdObjValue_Object = MibScalar
vpxdObjValue = _VpxdObjValue_Object(
    (1, 3, 6, 1, 4, 1, 6876, 50, 306),
    _VpxdObjValue_Type()
)
vpxdObjValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vpxdObjValue.setStatus("mandatory")

# Managed Objects groups


# Notification objects

vmPoweredOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 0, 1)
)
vmPoweredOn.setObjects(
      *(("VMWARE-TRAPS-MIB", "vmID"),
        ("VMWARE-TRAPS-MIB", "vmConfigFile"),
        ("VMWARE-VMINFO-MIB", "vmDisplayName"))
)
if mibBuilder.loadTexts:
    vmPoweredOn.setStatus(
        ""
    )

vmPoweredOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 0, 2)
)
vmPoweredOff.setObjects(
      *(("VMWARE-TRAPS-MIB", "vmID"),
        ("VMWARE-TRAPS-MIB", "vmConfigFile"),
        ("VMWARE-VMINFO-MIB", "vmDisplayName"))
)
if mibBuilder.loadTexts:
    vmPoweredOff.setStatus(
        ""
    )

vmHBLost = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 0, 3)
)
vmHBLost.setObjects(
      *(("VMWARE-TRAPS-MIB", "vmID"),
        ("VMWARE-TRAPS-MIB", "vmConfigFile"),
        ("VMWARE-VMINFO-MIB", "vmDisplayName"))
)
if mibBuilder.loadTexts:
    vmHBLost.setStatus(
        ""
    )

vmHBDetected = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 0, 4)
)
vmHBDetected.setObjects(
      *(("VMWARE-TRAPS-MIB", "vmID"),
        ("VMWARE-TRAPS-MIB", "vmConfigFile"),
        ("VMWARE-VMINFO-MIB", "vmDisplayName"))
)
if mibBuilder.loadTexts:
    vmHBDetected.setStatus(
        ""
    )

vmSuspended = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 0, 5)
)
vmSuspended.setObjects(
      *(("VMWARE-TRAPS-MIB", "vmID"),
        ("VMWARE-TRAPS-MIB", "vmConfigFile"),
        ("VMWARE-VMINFO-MIB", "vmDisplayName"))
)
if mibBuilder.loadTexts:
    vmSuspended.setStatus(
        ""
    )

vpxdTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 50, 0, 201)
)
vpxdTrap.setObjects(
      *(("VMWARE-TRAPS-MIB", "vpxdTrapType"),
        ("VMWARE-TRAPS-MIB", "vpxdHostName"),
        ("VMWARE-TRAPS-MIB", "vpxdVMName"),
        ("VMWARE-TRAPS-MIB", "vpxdNewStatus"),
        ("VMWARE-TRAPS-MIB", "vpxdOldStatus"),
        ("VMWARE-TRAPS-MIB", "vpxdObjValue"))
)
if mibBuilder.loadTexts:
    vpxdTrap.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "VMWARE-TRAPS-MIB",
    **{"vmPoweredOn": vmPoweredOn,
       "vmPoweredOff": vmPoweredOff,
       "vmHBLost": vmHBLost,
       "vmHBDetected": vmHBDetected,
       "vmSuspended": vmSuspended,
       "vpxdTrap": vpxdTrap,
       "vmID": vmID,
       "vmConfigFile": vmConfigFile,
       "vpxdTrapType": vpxdTrapType,
       "vpxdHostName": vpxdHostName,
       "vpxdVMName": vpxdVMName,
       "vpxdOldStatus": vpxdOldStatus,
       "vpxdNewStatus": vpxdNewStatus,
       "vpxdObjValue": vpxdObjValue}
)
