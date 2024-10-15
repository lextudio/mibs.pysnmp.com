# SNMP MIB module (SYMTRAP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/SYMTRAP-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:59:57 2024
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
 enterprises,
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
    "enterprises",
    "iso")

(DisplayString,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Symbios_ObjectIdentity = ObjectIdentity
symbios = _Symbios_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1123)
)
_Coloradosprings_ObjectIdentity = ObjectIdentity
coloradosprings = _Coloradosprings_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1123, 3)
)
_Scsi_ObjectIdentity = ObjectIdentity
scsi = _Scsi_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1123, 3, 1)
)
_Symc8xx_ObjectIdentity = ObjectIdentity
symc8xx = _Symc8xx_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1123, 3, 1, 2)
)
_SymTrap_ObjectIdentity = ObjectIdentity
symTrap = _SymTrap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1123, 3, 1, 2, 2)
)


class _SymTrapMajor_Type(Integer32):
    """Custom type symTrapMajor based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_SymTrapMajor_Type.__name__ = "Integer32"
_SymTrapMajor_Object = MibScalar
symTrapMajor = _SymTrapMajor_Object(
    (1, 3, 6, 1, 4, 1, 1123, 3, 1, 2, 2, 1),
    _SymTrapMajor_Type()
)
symTrapMajor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    symTrapMajor.setStatus("mandatory")


class _SymTrapMinor_Type(Integer32):
    """Custom type symTrapMinor based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SymTrapMinor_Type.__name__ = "Integer32"
_SymTrapMinor_Object = MibScalar
symTrapMinor = _SymTrapMinor_Object(
    (1, 3, 6, 1, 4, 1, 1123, 3, 1, 2, 2, 2),
    _SymTrapMinor_Type()
)
symTrapMinor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    symTrapMinor.setStatus("mandatory")


class _ManagerName_Type(DisplayString):
    """Custom type managerName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_ManagerName_Type.__name__ = "DisplayString"
_ManagerName_Object = MibScalar
managerName = _ManagerName_Object(
    (1, 3, 6, 1, 4, 1, 1123, 3, 1, 2, 2, 501),
    _ManagerName_Type()
)
managerName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    managerName.setStatus("mandatory")
_ManagerVersion_Type = Integer32
_ManagerVersion_Object = MibScalar
managerVersion = _ManagerVersion_Object(
    (1, 3, 6, 1, 4, 1, 1123, 3, 1, 2, 2, 502),
    _ManagerVersion_Type()
)
managerVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    managerVersion.setStatus("mandatory")


class _ControllerName_Type(DisplayString):
    """Custom type controllerName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_ControllerName_Type.__name__ = "DisplayString"
_ControllerName_Object = MibScalar
controllerName = _ControllerName_Object(
    (1, 3, 6, 1, 4, 1, 1123, 3, 1, 2, 2, 503),
    _ControllerName_Type()
)
controllerName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controllerName.setStatus("mandatory")
_ScsiController_Type = Integer32
_ScsiController_Object = MibScalar
scsiController = _ScsiController_Object(
    (1, 3, 6, 1, 4, 1, 1123, 3, 1, 2, 2, 504),
    _ScsiController_Type()
)
scsiController.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scsiController.setStatus("mandatory")
_ScsiChannel_Type = Integer32
_ScsiChannel_Object = MibScalar
scsiChannel = _ScsiChannel_Object(
    (1, 3, 6, 1, 4, 1, 1123, 3, 1, 2, 2, 505),
    _ScsiChannel_Type()
)
scsiChannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scsiChannel.setStatus("mandatory")
_ScsiTarget_Type = Integer32
_ScsiTarget_Object = MibScalar
scsiTarget = _ScsiTarget_Object(
    (1, 3, 6, 1, 4, 1, 1123, 3, 1, 2, 2, 506),
    _ScsiTarget_Type()
)
scsiTarget.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scsiTarget.setStatus("mandatory")
_ScsiLun_Type = Integer32
_ScsiLun_Object = MibScalar
scsiLun = _ScsiLun_Object(
    (1, 3, 6, 1, 4, 1, 1123, 3, 1, 2, 2, 507),
    _ScsiLun_Type()
)
scsiLun.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scsiLun.setStatus("mandatory")


class _VendorName_Type(DisplayString):
    """Custom type vendorName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 8),
    )


_VendorName_Type.__name__ = "DisplayString"
_VendorName_Object = MibScalar
vendorName = _VendorName_Object(
    (1, 3, 6, 1, 4, 1, 1123, 3, 1, 2, 2, 508),
    _VendorName_Type()
)
vendorName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vendorName.setStatus("mandatory")


class _ProductName_Type(DisplayString):
    """Custom type productName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_ProductName_Type.__name__ = "DisplayString"
_ProductName_Object = MibScalar
productName = _ProductName_Object(
    (1, 3, 6, 1, 4, 1, 1123, 3, 1, 2, 2, 509),
    _ProductName_Type()
)
productName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    productName.setStatus("mandatory")


class _ControllerModel_Type(DisplayString):
    """Custom type controllerModel based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_ControllerModel_Type.__name__ = "DisplayString"
_ControllerModel_Object = MibScalar
controllerModel = _ControllerModel_Object(
    (1, 3, 6, 1, 4, 1, 1123, 3, 1, 2, 2, 510),
    _ControllerModel_Type()
)
controllerModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controllerModel.setStatus("mandatory")
_PciBusNumber_Type = Integer32
_PciBusNumber_Object = MibScalar
pciBusNumber = _PciBusNumber_Object(
    (1, 3, 6, 1, 4, 1, 1123, 3, 1, 2, 2, 511),
    _PciBusNumber_Type()
)
pciBusNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pciBusNumber.setStatus("mandatory")
_ScsiSmartData_Type = Integer32
_ScsiSmartData_Object = MibScalar
scsiSmartData = _ScsiSmartData_Object(
    (1, 3, 6, 1, 4, 1, 1123, 3, 1, 2, 2, 512),
    _ScsiSmartData_Type()
)
scsiSmartData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scsiSmartData.setStatus("mandatory")
_ErrorType_Type = Integer32
_ErrorType_Object = MibScalar
errorType = _ErrorType_Object(
    (1, 3, 6, 1, 4, 1, 1123, 3, 1, 2, 2, 513),
    _ErrorType_Type()
)
errorType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    errorType.setStatus("mandatory")

# Managed Objects groups


# Notification objects

symSCSI1 = NotificationType(
    (1, 3, 6, 1, 4, 1, 1123, 3, 1, 2, 2, 0, 101)
)
if mibBuilder.loadTexts:
    symSCSI1.setStatus(
        ""
    )

symSCSI2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 1123, 3, 1, 2, 2, 0, 102)
)
if mibBuilder.loadTexts:
    symSCSI2.setStatus(
        ""
    )

symSCSI3 = NotificationType(
    (1, 3, 6, 1, 4, 1, 1123, 3, 1, 2, 2, 0, 108)
)
symSCSI3.setObjects(
      *(("SYMTRAP-MIB", "scsiController"),
        ("SYMTRAP-MIB", "controllerName"),
        ("SYMTRAP-MIB", "managerName"))
)
if mibBuilder.loadTexts:
    symSCSI3.setStatus(
        ""
    )

symSCSI4 = NotificationType(
    (1, 3, 6, 1, 4, 1, 1123, 3, 1, 2, 2, 0, 109)
)
symSCSI4.setObjects(
      *(("SYMTRAP-MIB", "scsiController"),
        ("SYMTRAP-MIB", "controllerName"),
        ("SYMTRAP-MIB", "managerName"))
)
if mibBuilder.loadTexts:
    symSCSI4.setStatus(
        ""
    )

symSCSI5 = NotificationType(
    (1, 3, 6, 1, 4, 1, 1123, 3, 1, 2, 2, 0, 110)
)
symSCSI5.setObjects(
    ("SYMTRAP-MIB", "scsiController")
)
if mibBuilder.loadTexts:
    symSCSI5.setStatus(
        ""
    )

symSCSI6 = NotificationType(
    (1, 3, 6, 1, 4, 1, 1123, 3, 1, 2, 2, 0, 111)
)
symSCSI6.setObjects(
    ("SYMTRAP-MIB", "scsiController")
)
if mibBuilder.loadTexts:
    symSCSI6.setStatus(
        ""
    )

symSCSI7 = NotificationType(
    (1, 3, 6, 1, 4, 1, 1123, 3, 1, 2, 2, 0, 112)
)
symSCSI7.setObjects(
      *(("SYMTRAP-MIB", "scsiController"),
        ("SYMTRAP-MIB", "scsiTarget"),
        ("SYMTRAP-MIB", "scsiLun"))
)
if mibBuilder.loadTexts:
    symSCSI7.setStatus(
        ""
    )

symSCSI8 = NotificationType(
    (1, 3, 6, 1, 4, 1, 1123, 3, 1, 2, 2, 0, 113)
)
symSCSI8.setObjects(
      *(("SYMTRAP-MIB", "scsiController"),
        ("SYMTRAP-MIB", "scsiTarget"),
        ("SYMTRAP-MIB", "scsiLun"),
        ("SYMTRAP-MIB", "vendorName"),
        ("SYMTRAP-MIB", "productName"))
)
if mibBuilder.loadTexts:
    symSCSI8.setStatus(
        ""
    )

symSCSI9 = NotificationType(
    (1, 3, 6, 1, 4, 1, 1123, 3, 1, 2, 2, 0, 114)
)
symSCSI9.setObjects(
      *(("SYMTRAP-MIB", "scsiController"),
        ("SYMTRAP-MIB", "scsiTarget"),
        ("SYMTRAP-MIB", "scsiLun"))
)
if mibBuilder.loadTexts:
    symSCSI9.setStatus(
        ""
    )

symSCSI10 = NotificationType(
    (1, 3, 6, 1, 4, 1, 1123, 3, 1, 2, 2, 0, 115)
)
symSCSI10.setObjects(
      *(("SYMTRAP-MIB", "scsiController"),
        ("SYMTRAP-MIB", "scsiTarget"),
        ("SYMTRAP-MIB", "scsiLun"),
        ("SYMTRAP-MIB", "vendorName"),
        ("SYMTRAP-MIB", "productName"))
)
if mibBuilder.loadTexts:
    symSCSI10.setStatus(
        ""
    )

symSCSI11 = NotificationType(
    (1, 3, 6, 1, 4, 1, 1123, 3, 1, 2, 2, 0, 116)
)
symSCSI11.setObjects(
      *(("SYMTRAP-MIB", "scsiController"),
        ("SYMTRAP-MIB", "scsiTarget"),
        ("SYMTRAP-MIB", "scsiLun"),
        ("SYMTRAP-MIB", "vendorName"),
        ("SYMTRAP-MIB", "productName"),
        ("SYMTRAP-MIB", "scsiSmartData"))
)
if mibBuilder.loadTexts:
    symSCSI11.setStatus(
        ""
    )

symSCSI12 = NotificationType(
    (1, 3, 6, 1, 4, 1, 1123, 3, 1, 2, 2, 0, 117)
)
symSCSI12.setObjects(
    ("SYMTRAP-MIB", "errorType")
)
if mibBuilder.loadTexts:
    symSCSI12.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SYMTRAP-MIB",
    **{"symbios": symbios,
       "coloradosprings": coloradosprings,
       "scsi": scsi,
       "symc8xx": symc8xx,
       "symTrap": symTrap,
       "symSCSI1": symSCSI1,
       "symSCSI2": symSCSI2,
       "symSCSI3": symSCSI3,
       "symSCSI4": symSCSI4,
       "symSCSI5": symSCSI5,
       "symSCSI6": symSCSI6,
       "symSCSI7": symSCSI7,
       "symSCSI8": symSCSI8,
       "symSCSI9": symSCSI9,
       "symSCSI10": symSCSI10,
       "symSCSI11": symSCSI11,
       "symSCSI12": symSCSI12,
       "symTrapMajor": symTrapMajor,
       "symTrapMinor": symTrapMinor,
       "managerName": managerName,
       "managerVersion": managerVersion,
       "controllerName": controllerName,
       "scsiController": scsiController,
       "scsiChannel": scsiChannel,
       "scsiTarget": scsiTarget,
       "scsiLun": scsiLun,
       "vendorName": vendorName,
       "productName": productName,
       "controllerModel": controllerModel,
       "pciBusNumber": pciBusNumber,
       "scsiSmartData": scsiSmartData,
       "errorType": errorType}
)
