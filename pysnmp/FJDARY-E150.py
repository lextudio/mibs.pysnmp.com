# SNMP MIB module (FJDARY-E150) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/FJDARY-E150
# Produced by pysmi-1.5.4 at Mon Oct 14 21:44:58 2024
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
    "TimeTicks",
    "Unsigned32",
    "enterprises",
    "iso")

(DisplayString,
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

fjdarye150 = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150)
)
fjdarye150.setRevisions(
        ("2014-05-13 00:00",)
)


# Types definitions



class FjdaryComponentStatus(Integer32):
    """Custom type FjdaryComponentStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("alarm", 2),
          ("invalid", 4),
          ("maintenance", 5),
          ("normal", 1),
          ("undefined", 6),
          ("warning", 3))
    )




# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Fujitsu_ObjectIdentity = ObjectIdentity
fujitsu = _Fujitsu_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 211)
)
_Product_ObjectIdentity = ObjectIdentity
product = _Product_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 211, 1)
)
_Storage_ObjectIdentity = ObjectIdentity
storage = _Storage_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 211, 1, 21)
)
_Nsp_ObjectIdentity = ObjectIdentity
nsp = _Nsp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1)
)
_FjdarySsp_ObjectIdentity = ObjectIdentity
fjdarySsp = _FjdarySsp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 1)
)


class _FjdarySspMachineId_Type(OctetString):
    """Custom type fjdarySspMachineId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_FjdarySspMachineId_Type.__name__ = "OctetString"
_FjdarySspMachineId_Object = MibScalar
fjdarySspMachineId = _FjdarySspMachineId_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 1, 1),
    _FjdarySspMachineId_Type()
)
fjdarySspMachineId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fjdarySspMachineId.setStatus("current")
_FjdarySspConfigDate_Type = DisplayString
_FjdarySspConfigDate_Object = MibScalar
fjdarySspConfigDate = _FjdarySspConfigDate_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 1, 2),
    _FjdarySspConfigDate_Type()
)
fjdarySspConfigDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fjdarySspConfigDate.setStatus("current")


class _FjdarySspWwnn_Type(OctetString):
    """Custom type fjdarySspWwnn based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_FjdarySspWwnn_Type.__name__ = "OctetString"
_FjdarySspWwnn_Object = MibScalar
fjdarySspWwnn = _FjdarySspWwnn_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 1, 3),
    _FjdarySspWwnn_Type()
)
fjdarySspWwnn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fjdarySspWwnn.setStatus("current")


class _FjdarySspVenderId_Type(OctetString):
    """Custom type fjdarySspVenderId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_FjdarySspVenderId_Type.__name__ = "OctetString"
_FjdarySspVenderId_Object = MibScalar
fjdarySspVenderId = _FjdarySspVenderId_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 1, 4),
    _FjdarySspVenderId_Type()
)
fjdarySspVenderId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fjdarySspVenderId.setStatus("current")


class _FjdarySspProductId_Type(OctetString):
    """Custom type fjdarySspProductId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_FjdarySspProductId_Type.__name__ = "OctetString"
_FjdarySspProductId_Object = MibScalar
fjdarySspProductId = _FjdarySspProductId_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 1, 5),
    _FjdarySspProductId_Type()
)
fjdarySspProductId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fjdarySspProductId.setStatus("current")


class _FjdarySspBoxId_Type(OctetString):
    """Custom type fjdarySspBoxId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_FjdarySspBoxId_Type.__name__ = "OctetString"
_FjdarySspBoxId_Object = MibScalar
fjdarySspBoxId = _FjdarySspBoxId_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 1, 6),
    _FjdarySspBoxId_Type()
)
fjdarySspBoxId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fjdarySspBoxId.setStatus("current")


class _FjdarySspMaintenanceServiceLevel_Type(Integer32):
    """Custom type fjdarySspMaintenanceServiceLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("level1", 1),
          ("level2", 2))
    )


_FjdarySspMaintenanceServiceLevel_Type.__name__ = "Integer32"
_FjdarySspMaintenanceServiceLevel_Object = MibScalar
fjdarySspMaintenanceServiceLevel = _FjdarySspMaintenanceServiceLevel_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 1, 7),
    _FjdarySspMaintenanceServiceLevel_Type()
)
fjdarySspMaintenanceServiceLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fjdarySspMaintenanceServiceLevel.setStatus("current")
_FjdaryPconfig_ObjectIdentity = ObjectIdentity
fjdaryPconfig = _FjdaryPconfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 2)
)
_FjdaryCm_ObjectIdentity = ObjectIdentity
fjdaryCm = _FjdaryCm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 2, 1)
)


class _FjdaryCmCount_Type(Integer32):
    """Custom type fjdaryCmCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_FjdaryCmCount_Type.__name__ = "Integer32"
_FjdaryCmCount_Object = MibScalar
fjdaryCmCount = _FjdaryCmCount_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 2, 1, 1),
    _FjdaryCmCount_Type()
)
fjdaryCmCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fjdaryCmCount.setStatus("current")
_FjdaryCmTable_Object = MibTable
fjdaryCmTable = _FjdaryCmTable_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 2, 1, 2)
)
if mibBuilder.loadTexts:
    fjdaryCmTable.setStatus("current")
_FjdaryCmEntry_Object = MibTableRow
fjdaryCmEntry = _FjdaryCmEntry_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 2, 1, 2, 1)
)
fjdaryCmEntry.setIndexNames(
    (0, "FJDARY-E150", "fjdaryCmIndex"),
)
if mibBuilder.loadTexts:
    fjdaryCmEntry.setStatus("current")


class _FjdaryCmIndex_Type(Integer32):
    """Custom type fjdaryCmIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_FjdaryCmIndex_Type.__name__ = "Integer32"
_FjdaryCmIndex_Object = MibTableColumn
fjdaryCmIndex = _FjdaryCmIndex_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 2, 1, 2, 1, 1),
    _FjdaryCmIndex_Type()
)
fjdaryCmIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fjdaryCmIndex.setStatus("current")


class _FjdaryCmItemId_Type(Integer32):
    """Custom type fjdaryCmItemId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_FjdaryCmItemId_Type.__name__ = "Integer32"
_FjdaryCmItemId_Object = MibTableColumn
fjdaryCmItemId = _FjdaryCmItemId_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 2, 1, 2, 1, 2),
    _FjdaryCmItemId_Type()
)
fjdaryCmItemId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fjdaryCmItemId.setStatus("current")
_FjdaryCmStatus_Type = FjdaryComponentStatus
_FjdaryCmStatus_Object = MibTableColumn
fjdaryCmStatus = _FjdaryCmStatus_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 2, 1, 2, 1, 3),
    _FjdaryCmStatus_Type()
)
fjdaryCmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fjdaryCmStatus.setStatus("current")
_FjdaryCmSubStatus_Type = FjdaryComponentStatus
_FjdaryCmSubStatus_Object = MibTableColumn
fjdaryCmSubStatus = _FjdaryCmSubStatus_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 2, 1, 2, 1, 4),
    _FjdaryCmSubStatus_Type()
)
fjdaryCmSubStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fjdaryCmSubStatus.setStatus("current")


class _FjdaryCmModuleId_Type(Integer32):
    """Custom type fjdaryCmModuleId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_FjdaryCmModuleId_Type.__name__ = "Integer32"
_FjdaryCmModuleId_Object = MibTableColumn
fjdaryCmModuleId = _FjdaryCmModuleId_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 2, 1, 2, 1, 5),
    _FjdaryCmModuleId_Type()
)
fjdaryCmModuleId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fjdaryCmModuleId.setStatus("current")


class _FjdaryCmRole_Type(Integer32):
    """Custom type fjdaryCmRole based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("master", 1),
          ("slave", 2))
    )


_FjdaryCmRole_Type.__name__ = "Integer32"
_FjdaryCmRole_Object = MibTableColumn
fjdaryCmRole = _FjdaryCmRole_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 2, 1, 2, 1, 6),
    _FjdaryCmRole_Type()
)
fjdaryCmRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fjdaryCmRole.setStatus("current")


class _FjdaryCmPartNo_Type(OctetString):
    """Custom type fjdaryCmPartNo based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_FjdaryCmPartNo_Type.__name__ = "OctetString"
_FjdaryCmPartNo_Object = MibTableColumn
fjdaryCmPartNo = _FjdaryCmPartNo_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 2, 1, 2, 1, 7),
    _FjdaryCmPartNo_Type()
)
fjdaryCmPartNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fjdaryCmPartNo.setStatus("current")


class _FjdaryCmSerialNo_Type(OctetString):
    """Custom type fjdaryCmSerialNo based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_FjdaryCmSerialNo_Type.__name__ = "OctetString"
_FjdaryCmSerialNo_Object = MibTableColumn
fjdaryCmSerialNo = _FjdaryCmSerialNo_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 2, 1, 2, 1, 8),
    _FjdaryCmSerialNo_Type()
)
fjdaryCmSerialNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fjdaryCmSerialNo.setStatus("current")


class _FjdaryCmRevision_Type(OctetString):
    """Custom type fjdaryCmRevision based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_FjdaryCmRevision_Type.__name__ = "OctetString"
_FjdaryCmRevision_Object = MibTableColumn
fjdaryCmRevision = _FjdaryCmRevision_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 2, 1, 2, 1, 9),
    _FjdaryCmRevision_Type()
)
fjdaryCmRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fjdaryCmRevision.setStatus("current")
_FjdaryCmcpu_ObjectIdentity = ObjectIdentity
fjdaryCmcpu = _FjdaryCmcpu_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 2, 2)
)


class _FjdaryCmcpuCount_Type(Integer32):
    """Custom type fjdaryCmcpuCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_FjdaryCmcpuCount_Type.__name__ = "Integer32"
_FjdaryCmcpuCount_Object = MibScalar
fjdaryCmcpuCount = _FjdaryCmcpuCount_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 2, 2, 1),
    _FjdaryCmcpuCount_Type()
)
fjdaryCmcpuCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fjdaryCmcpuCount.setStatus("current")
_FjdaryCmcpuTable_Object = MibTable
fjdaryCmcpuTable = _FjdaryCmcpuTable_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 2, 2, 2)
)
if mibBuilder.loadTexts:
    fjdaryCmcpuTable.setStatus("current")
_FjdaryCmcpuEntry_Object = MibTableRow
fjdaryCmcpuEntry = _FjdaryCmcpuEntry_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 2, 2, 2, 1)
)
fjdaryCmcpuEntry.setIndexNames(
    (0, "FJDARY-E150", "fjdaryCmcpuIndex"),
)
if mibBuilder.loadTexts:
    fjdaryCmcpuEntry.setStatus("current")


class _FjdaryCmcpuIndex_Type(Integer32):
    """Custom type fjdaryCmcpuIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_FjdaryCmcpuIndex_Type.__name__ = "Integer32"
_FjdaryCmcpuIndex_Object = MibTableColumn
fjdaryCmcpuIndex = _FjdaryCmcpuIndex_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 2, 2, 2, 1, 1),
    _FjdaryCmcpuIndex_Type()
)
fjdaryCmcpuIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fjdaryCmcpuIndex.setStatus("current")


class _FjdaryCmcpuItemId_Type(Integer32):
    """Custom type fjdaryCmcpuItemId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_FjdaryCmcpuItemId_Type.__name__ = "Integer32"
_FjdaryCmcpuItemId_Object = MibTableColumn
fjdaryCmcpuItemId = _FjdaryCmcpuItemId_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 2, 2, 2, 1, 2),
    _FjdaryCmcpuItemId_Type()
)
fjdaryCmcpuItemId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fjdaryCmcpuItemId.setStatus("current")
_FjdaryCmcpuStatus_Type = FjdaryComponentStatus
_FjdaryCmcpuStatus_Object = MibTableColumn
fjdaryCmcpuStatus = _FjdaryCmcpuStatus_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 2, 2, 2, 1, 3),
    _FjdaryCmcpuStatus_Type()
)
fjdaryCmcpuStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fjdaryCmcpuStatus.setStatus("current")
_FjdaryCmcpuSubStatus_Type = FjdaryComponentStatus
_FjdaryCmcpuSubStatus_Object = MibTableColumn
fjdaryCmcpuSubStatus = _FjdaryCmcpuSubStatus_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 2, 2, 2, 1, 4),
    _FjdaryCmcpuSubStatus_Type()
)
fjdaryCmcpuSubStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fjdaryCmcpuSubStatus.setStatus("current")


class _FjdaryCmcpuModuleId_Type(Integer32):
    """Custom type fjdaryCmcpuModuleId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_FjdaryCmcpuModuleId_Type.__name__ = "Integer32"
_FjdaryCmcpuModuleId_Object = MibTableColumn
fjdaryCmcpuModuleId = _FjdaryCmcpuModuleId_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 2, 2, 2, 1, 5),
    _FjdaryCmcpuModuleId_Type()
)
fjdaryCmcpuModuleId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fjdaryCmcpuModuleId.setStatus("current")


class _FjdaryCmcpuRole_Type(Integer32):
    """Custom type fjdaryCmcpuRole based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("master", 1),
          ("slave", 2))
    )


_FjdaryCmcpuRole_Type.__name__ = "Integer32"
_FjdaryCmcpuRole_Object = MibTableColumn
fjdaryCmcpuRole = _FjdaryCmcpuRole_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 2, 2, 2, 1, 6),
    _FjdaryCmcpuRole_Type()
)
fjdaryCmcpuRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fjdaryCmcpuRole.setStatus("current")


class _FjdaryCmcpuClock_Type(Integer32):
    """Custom type fjdaryCmcpuClock based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_FjdaryCmcpuClock_Type.__name__ = "Integer32"
_FjdaryCmcpuClock_Object = MibTableColumn
fjdaryCmcpuClock = _FjdaryCmcpuClock_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 2, 2, 2, 1, 7),
    _FjdaryCmcpuClock_Type()
)
fjdaryCmcpuClock.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fjdaryCmcpuClock.setStatus("current")
_FjdaryCa_ObjectIdentity = ObjectIdentity
fjdaryCa = _FjdaryCa_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 2, 3)
)


class _FjdaryCaCount_Type(Integer32):
    """Custom type fjdaryCaCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_FjdaryCaCount_Type.__name__ = "Integer32"
_FjdaryCaCount_Object = MibScalar
fjdaryCaCount = _FjdaryCaCount_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 2, 3, 1),
    _FjdaryCaCount_Type()
)
fjdaryCaCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fjdaryCaCount.setStatus("current")
_FjdaryCaTable_Object = MibTable
fjdaryCaTable = _FjdaryCaTable_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 2, 3, 2)
)
if mibBuilder.loadTexts:
    fjdaryCaTable.setStatus("current")
_FjdaryCaEntry_Object = MibTableRow
fjdaryCaEntry = _FjdaryCaEntry_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 2, 3, 2, 1)
)
fjdaryCaEntry.setIndexNames(
    (0, "FJDARY-E150", "fjdaryCaIndex"),
)
if mibBuilder.loadTexts:
    fjdaryCaEntry.setStatus("current")


class _FjdaryCaIndex_Type(Integer32):
    """Custom type fjdaryCaIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_FjdaryCaIndex_Type.__name__ = "Integer32"
_FjdaryCaIndex_Object = MibTableColumn
fjdaryCaIndex = _FjdaryCaIndex_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 2, 3, 2, 1, 1),
    _FjdaryCaIndex_Type()
)
fjdaryCaIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fjdaryCaIndex.setStatus("current")


class _FjdaryCaItemId_Type(Integer32):
    """Custom type fjdaryCaItemId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_FjdaryCaItemId_Type.__name__ = "Integer32"
_FjdaryCaItemId_Object = MibTableColumn
fjdaryCaItemId = _FjdaryCaItemId_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 2, 3, 2, 1, 2),
    _FjdaryCaItemId_Type()
)
fjdaryCaItemId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fjdaryCaItemId.setStatus("current")
_FjdaryCaStatus_Type = FjdaryComponentStatus
_FjdaryCaStatus_Object = MibTableColumn
fjdaryCaStatus = _FjdaryCaStatus_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 2, 3, 2, 1, 3),
    _FjdaryCaStatus_Type()
)
fjdaryCaStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fjdaryCaStatus.setStatus("current")
_FjdaryCaSubStatus_Type = FjdaryComponentStatus
_FjdaryCaSubStatus_Object = MibTableColumn
fjdaryCaSubStatus = _FjdaryCaSubStatus_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 2, 3, 2, 1, 4),
    _FjdaryCaSubStatus_Type()
)
fjdaryCaSubStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fjdaryCaSubStatus.setStatus("current")


class _FjdaryCaModuleId_Type(Integer32):
    """Custom type fjdaryCaModuleId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_FjdaryCaModuleId_Type.__name__ = "Integer32"
_FjdaryCaModuleId_Object = MibTableColumn
fjdaryCaModuleId = _FjdaryCaModuleId_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 2, 3, 2, 1, 5),
    _FjdaryCaModuleId_Type()
)
fjdaryCaModuleId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fjdaryCaModuleId.setStatus("current")


class _FjdaryCaType_Type(Integer32):
    """Custom type fjdaryCaType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_FjdaryCaType_Type.__name__ = "Integer32"
_FjdaryCaType_Object = MibTableColumn
fjdaryCaType = _FjdaryCaType_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 2, 3, 2, 1, 6),
    _FjdaryCaType_Type()
)
fjdaryCaType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fjdaryCaType.setStatus("current")
_FjdaryCmmemory_ObjectIdentity = ObjectIdentity
fjdaryCmmemory = _FjdaryCmmemory_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 2, 4)
)


class _FjdaryCmmemoryCount_Type(Integer32):
    """Custom type fjdaryCmmemoryCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_FjdaryCmmemoryCount_Type.__name__ = "Integer32"
_FjdaryCmmemoryCount_Object = MibScalar
fjdaryCmmemoryCount = _FjdaryCmmemoryCount_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 2, 4, 1),
    _FjdaryCmmemoryCount_Type()
)
fjdaryCmmemoryCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fjdaryCmmemoryCount.setStatus("current")
_FjdaryCmmemoryTable_Object = MibTable
fjdaryCmmemoryTable = _FjdaryCmmemoryTable_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 2, 4, 2)
)
if mibBuilder.loadTexts:
    fjdaryCmmemoryTable.setStatus("current")
_FjdaryCmmemoryEntry_Object = MibTableRow
fjdaryCmmemoryEntry = _FjdaryCmmemoryEntry_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 2, 4, 2, 1)
)
fjdaryCmmemoryEntry.setIndexNames(
    (0, "FJDARY-E150", "fjdaryCmmemoryIndex"),
)
if mibBuilder.loadTexts:
    fjdaryCmmemoryEntry.setStatus("current")


class _FjdaryCmmemoryIndex_Type(Integer32):
    """Custom type fjdaryCmmemoryIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_FjdaryCmmemoryIndex_Type.__name__ = "Integer32"
_FjdaryCmmemoryIndex_Object = MibTableColumn
fjdaryCmmemoryIndex = _FjdaryCmmemoryIndex_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 2, 4, 2, 1, 1),
    _FjdaryCmmemoryIndex_Type()
)
fjdaryCmmemoryIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fjdaryCmmemoryIndex.setStatus("current")


class _FjdaryCmmemoryItemId_Type(Integer32):
    """Custom type fjdaryCmmemoryItemId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_FjdaryCmmemoryItemId_Type.__name__ = "Integer32"
_FjdaryCmmemoryItemId_Object = MibTableColumn
fjdaryCmmemoryItemId = _FjdaryCmmemoryItemId_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 2, 4, 2, 1, 2),
    _FjdaryCmmemoryItemId_Type()
)
fjdaryCmmemoryItemId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fjdaryCmmemoryItemId.setStatus("current")
_FjdaryCmmemoryStatus_Type = FjdaryComponentStatus
_FjdaryCmmemoryStatus_Object = MibTableColumn
fjdaryCmmemoryStatus = _FjdaryCmmemoryStatus_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 2, 4, 2, 1, 3),
    _FjdaryCmmemoryStatus_Type()
)
fjdaryCmmemoryStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fjdaryCmmemoryStatus.setStatus("current")
_FjdaryCmmemorySubStatus_Type = FjdaryComponentStatus
_FjdaryCmmemorySubStatus_Object = MibTableColumn
fjdaryCmmemorySubStatus = _FjdaryCmmemorySubStatus_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 2, 4, 2, 1, 4),
    _FjdaryCmmemorySubStatus_Type()
)
fjdaryCmmemorySubStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fjdaryCmmemorySubStatus.setStatus("current")


class _FjdaryCmmemoryCapacity_Type(Integer32):
    """Custom type fjdaryCmmemoryCapacity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_FjdaryCmmemoryCapacity_Type.__name__ = "Integer32"
_FjdaryCmmemoryCapacity_Object = MibTableColumn
fjdaryCmmemoryCapacity = _FjdaryCmmemoryCapacity_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 2, 4, 2, 1, 5),
    _FjdaryCmmemoryCapacity_Type()
)
fjdaryCmmemoryCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fjdaryCmmemoryCapacity.setStatus("current")


class _FjdaryCmmemoryPartNo_Type(OctetString):
    """Custom type fjdaryCmmemoryPartNo based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_FjdaryCmmemoryPartNo_Type.__name__ = "OctetString"
_FjdaryCmmemoryPartNo_Object = MibTableColumn
fjdaryCmmemoryPartNo = _FjdaryCmmemoryPartNo_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 2, 4, 2, 1, 6),
    _FjdaryCmmemoryPartNo_Type()
)
fjdaryCmmemoryPartNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fjdaryCmmemoryPartNo.setStatus("current")


class _FjdaryCmmemorySerialNo_Type(OctetString):
    """Custom type fjdaryCmmemorySerialNo based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_FjdaryCmmemorySerialNo_Type.__name__ = "OctetString"
_FjdaryCmmemorySerialNo_Object = MibTableColumn
fjdaryCmmemorySerialNo = _FjdaryCmmemorySerialNo_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 2, 4, 2, 1, 7),
    _FjdaryCmmemorySerialNo_Type()
)
fjdaryCmmemorySerialNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fjdaryCmmemorySerialNo.setStatus("current")
_FjdaryBud_ObjectIdentity = ObjectIdentity
fjdaryBud = _FjdaryBud_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 2, 5)
)


class _FjdaryBudCount_Type(Integer32):
    """Custom type fjdaryBudCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_FjdaryBudCount_Type.__name__ = "Integer32"
_FjdaryBudCount_Object = MibScalar
fjdaryBudCount = _FjdaryBudCount_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 2, 5, 1),
    _FjdaryBudCount_Type()
)
fjdaryBudCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fjdaryBudCount.setStatus("current")
_FjdaryBudTable_Object = MibTable
fjdaryBudTable = _FjdaryBudTable_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 2, 5, 2)
)
if mibBuilder.loadTexts:
    fjdaryBudTable.setStatus("current")
_FjdaryBudEntry_Object = MibTableRow
fjdaryBudEntry = _FjdaryBudEntry_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 2, 5, 2, 1)
)
fjdaryBudEntry.setIndexNames(
    (0, "FJDARY-E150", "fjdaryBudIndex"),
)
if mibBuilder.loadTexts:
    fjdaryBudEntry.setStatus("current")


class _FjdaryBudIndex_Type(Integer32):
    """Custom type fjdaryBudIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_FjdaryBudIndex_Type.__name__ = "Integer32"
_FjdaryBudIndex_Object = MibTableColumn
fjdaryBudIndex = _FjdaryBudIndex_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 2, 5, 2, 1, 1),
    _FjdaryBudIndex_Type()
)
fjdaryBudIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fjdaryBudIndex.setStatus("current")


class _FjdaryBudItemId_Type(Integer32):
    """Custom type fjdaryBudItemId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_FjdaryBudItemId_Type.__name__ = "Integer32"
_FjdaryBudItemId_Object = MibTableColumn
fjdaryBudItemId = _FjdaryBudItemId_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 2, 5, 2, 1, 2),
    _FjdaryBudItemId_Type()
)
fjdaryBudItemId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fjdaryBudItemId.setStatus("current")
_FjdaryBudStatus_Type = FjdaryComponentStatus
_FjdaryBudStatus_Object = MibTableColumn
fjdaryBudStatus = _FjdaryBudStatus_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 2, 5, 2, 1, 3),
    _FjdaryBudStatus_Type()
)
fjdaryBudStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fjdaryBudStatus.setStatus("current")
_FjdaryBudSubStatus_Type = FjdaryComponentStatus
_FjdaryBudSubStatus_Object = MibTableColumn
fjdaryBudSubStatus = _FjdaryBudSubStatus_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 2, 5, 2, 1, 4),
    _FjdaryBudSubStatus_Type()
)
fjdaryBudSubStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fjdaryBudSubStatus.setStatus("current")
_FjdaryCmfan_ObjectIdentity = ObjectIdentity
fjdaryCmfan = _FjdaryCmfan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 2, 6)
)


class _FjdaryCmfanCount_Type(Integer32):
    """Custom type fjdaryCmfanCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_FjdaryCmfanCount_Type.__name__ = "Integer32"
_FjdaryCmfanCount_Object = MibScalar
fjdaryCmfanCount = _FjdaryCmfanCount_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 2, 6, 1),
    _FjdaryCmfanCount_Type()
)
fjdaryCmfanCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fjdaryCmfanCount.setStatus("current")
_FjdaryCmfanTable_Object = MibTable
fjdaryCmfanTable = _FjdaryCmfanTable_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 2, 6, 2)
)
if mibBuilder.loadTexts:
    fjdaryCmfanTable.setStatus("current")
_FjdaryCmfanEntry_Object = MibTableRow
fjdaryCmfanEntry = _FjdaryCmfanEntry_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 2, 6, 2, 1)
)
fjdaryCmfanEntry.setIndexNames(
    (0, "FJDARY-E150", "fjdaryCmfanIndex"),
)
if mibBuilder.loadTexts:
    fjdaryCmfanEntry.setStatus("current")


class _FjdaryCmfanIndex_Type(Integer32):
    """Custom type fjdaryCmfanIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_FjdaryCmfanIndex_Type.__name__ = "Integer32"
_FjdaryCmfanIndex_Object = MibTableColumn
fjdaryCmfanIndex = _FjdaryCmfanIndex_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 2, 6, 2, 1, 1),
    _FjdaryCmfanIndex_Type()
)
fjdaryCmfanIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fjdaryCmfanIndex.setStatus("current")


class _FjdaryCmfanItemId_Type(Integer32):
    """Custom type fjdaryCmfanItemId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_FjdaryCmfanItemId_Type.__name__ = "Integer32"
_FjdaryCmfanItemId_Object = MibTableColumn
fjdaryCmfanItemId = _FjdaryCmfanItemId_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 2, 6, 2, 1, 2),
    _FjdaryCmfanItemId_Type()
)
fjdaryCmfanItemId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fjdaryCmfanItemId.setStatus("current")
_FjdaryCmfanStatus_Type = FjdaryComponentStatus
_FjdaryCmfanStatus_Object = MibTableColumn
fjdaryCmfanStatus = _FjdaryCmfanStatus_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 2, 6, 2, 1, 3),
    _FjdaryCmfanStatus_Type()
)
fjdaryCmfanStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fjdaryCmfanStatus.setStatus("current")
_FjdaryCmfanSubStatus_Type = FjdaryComponentStatus
_FjdaryCmfanSubStatus_Object = MibTableColumn
fjdaryCmfanSubStatus = _FjdaryCmfanSubStatus_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 2, 6, 2, 1, 4),
    _FjdaryCmfanSubStatus_Type()
)
fjdaryCmfanSubStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fjdaryCmfanSubStatus.setStatus("current")
_FjdaryBcu_ObjectIdentity = ObjectIdentity
fjdaryBcu = _FjdaryBcu_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 2, 7)
)


class _FjdaryBcuCount_Type(Integer32):
    """Custom type fjdaryBcuCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_FjdaryBcuCount_Type.__name__ = "Integer32"
_FjdaryBcuCount_Object = MibScalar
fjdaryBcuCount = _FjdaryBcuCount_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 2, 7, 1),
    _FjdaryBcuCount_Type()
)
fjdaryBcuCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fjdaryBcuCount.setStatus("current")
_FjdaryBcuTable_Object = MibTable
fjdaryBcuTable = _FjdaryBcuTable_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 2, 7, 2)
)
if mibBuilder.loadTexts:
    fjdaryBcuTable.setStatus("current")
_FjdaryBcuEntry_Object = MibTableRow
fjdaryBcuEntry = _FjdaryBcuEntry_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 2, 7, 2, 1)
)
fjdaryBcuEntry.setIndexNames(
    (0, "FJDARY-E150", "fjdaryBcuIndex"),
)
if mibBuilder.loadTexts:
    fjdaryBcuEntry.setStatus("current")


class _FjdaryBcuIndex_Type(Integer32):
    """Custom type fjdaryBcuIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_FjdaryBcuIndex_Type.__name__ = "Integer32"
_FjdaryBcuIndex_Object = MibTableColumn
fjdaryBcuIndex = _FjdaryBcuIndex_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 2, 7, 2, 1, 1),
    _FjdaryBcuIndex_Type()
)
fjdaryBcuIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fjdaryBcuIndex.setStatus("current")


class _FjdaryBcuItemId_Type(Integer32):
    """Custom type fjdaryBcuItemId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_FjdaryBcuItemId_Type.__name__ = "Integer32"
_FjdaryBcuItemId_Object = MibTableColumn
fjdaryBcuItemId = _FjdaryBcuItemId_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 2, 7, 2, 1, 2),
    _FjdaryBcuItemId_Type()
)
fjdaryBcuItemId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fjdaryBcuItemId.setStatus("current")
_FjdaryBcuStatus_Type = FjdaryComponentStatus
_FjdaryBcuStatus_Object = MibTableColumn
fjdaryBcuStatus = _FjdaryBcuStatus_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 2, 7, 2, 1, 3),
    _FjdaryBcuStatus_Type()
)
fjdaryBcuStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fjdaryBcuStatus.setStatus("current")
_FjdaryBcuSubStatus_Type = FjdaryComponentStatus
_FjdaryBcuSubStatus_Object = MibTableColumn
fjdaryBcuSubStatus = _FjdaryBcuSubStatus_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 2, 7, 2, 1, 4),
    _FjdaryBcuSubStatus_Type()
)
fjdaryBcuSubStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fjdaryBcuSubStatus.setStatus("current")
_FjdaryBtu_ObjectIdentity = ObjectIdentity
fjdaryBtu = _FjdaryBtu_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 2, 8)
)


class _FjdaryBtuCount_Type(Integer32):
    """Custom type fjdaryBtuCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_FjdaryBtuCount_Type.__name__ = "Integer32"
_FjdaryBtuCount_Object = MibScalar
fjdaryBtuCount = _FjdaryBtuCount_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 2, 8, 1),
    _FjdaryBtuCount_Type()
)
fjdaryBtuCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fjdaryBtuCount.setStatus("current")
_FjdaryBtuTable_Object = MibTable
fjdaryBtuTable = _FjdaryBtuTable_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 2, 8, 2)
)
if mibBuilder.loadTexts:
    fjdaryBtuTable.setStatus("current")
_FjdaryBtuEntry_Object = MibTableRow
fjdaryBtuEntry = _FjdaryBtuEntry_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 2, 8, 2, 1)
)
fjdaryBtuEntry.setIndexNames(
    (0, "FJDARY-E150", "fjdaryBtuIndex"),
)
if mibBuilder.loadTexts:
    fjdaryBtuEntry.setStatus("current")


class _FjdaryBtuIndex_Type(Integer32):
    """Custom type fjdaryBtuIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_FjdaryBtuIndex_Type.__name__ = "Integer32"
_FjdaryBtuIndex_Object = MibTableColumn
fjdaryBtuIndex = _FjdaryBtuIndex_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 2, 8, 2, 1, 1),
    _FjdaryBtuIndex_Type()
)
fjdaryBtuIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fjdaryBtuIndex.setStatus("current")


class _FjdaryBtuItemId_Type(Integer32):
    """Custom type fjdaryBtuItemId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_FjdaryBtuItemId_Type.__name__ = "Integer32"
_FjdaryBtuItemId_Object = MibTableColumn
fjdaryBtuItemId = _FjdaryBtuItemId_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 2, 8, 2, 1, 2),
    _FjdaryBtuItemId_Type()
)
fjdaryBtuItemId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fjdaryBtuItemId.setStatus("current")
_FjdaryBtuStatus_Type = FjdaryComponentStatus
_FjdaryBtuStatus_Object = MibTableColumn
fjdaryBtuStatus = _FjdaryBtuStatus_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 2, 8, 2, 1, 3),
    _FjdaryBtuStatus_Type()
)
fjdaryBtuStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fjdaryBtuStatus.setStatus("current")
_FjdaryBtuSubStatus_Type = FjdaryComponentStatus
_FjdaryBtuSubStatus_Object = MibTableColumn
fjdaryBtuSubStatus = _FjdaryBtuSubStatus_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 2, 8, 2, 1, 4),
    _FjdaryBtuSubStatus_Type()
)
fjdaryBtuSubStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fjdaryBtuSubStatus.setStatus("current")
_FjdaryScu_ObjectIdentity = ObjectIdentity
fjdaryScu = _FjdaryScu_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 2, 9)
)


class _FjdaryScuCount_Type(Integer32):
    """Custom type fjdaryScuCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_FjdaryScuCount_Type.__name__ = "Integer32"
_FjdaryScuCount_Object = MibScalar
fjdaryScuCount = _FjdaryScuCount_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 2, 9, 1),
    _FjdaryScuCount_Type()
)
fjdaryScuCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fjdaryScuCount.setStatus("current")
_FjdaryScuTable_Object = MibTable
fjdaryScuTable = _FjdaryScuTable_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 2, 9, 2)
)
if mibBuilder.loadTexts:
    fjdaryScuTable.setStatus("current")
_FjdaryScuEntry_Object = MibTableRow
fjdaryScuEntry = _FjdaryScuEntry_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 2, 9, 2, 1)
)
fjdaryScuEntry.setIndexNames(
    (0, "FJDARY-E150", "fjdaryScuIndex"),
)
if mibBuilder.loadTexts:
    fjdaryScuEntry.setStatus("current")


class _FjdaryScuIndex_Type(Integer32):
    """Custom type fjdaryScuIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_FjdaryScuIndex_Type.__name__ = "Integer32"
_FjdaryScuIndex_Object = MibTableColumn
fjdaryScuIndex = _FjdaryScuIndex_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 2, 9, 2, 1, 1),
    _FjdaryScuIndex_Type()
)
fjdaryScuIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fjdaryScuIndex.setStatus("current")


class _FjdaryScuItemId_Type(Integer32):
    """Custom type fjdaryScuItemId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_FjdaryScuItemId_Type.__name__ = "Integer32"
_FjdaryScuItemId_Object = MibTableColumn
fjdaryScuItemId = _FjdaryScuItemId_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 2, 9, 2, 1, 2),
    _FjdaryScuItemId_Type()
)
fjdaryScuItemId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fjdaryScuItemId.setStatus("current")
_FjdaryScuStatus_Type = FjdaryComponentStatus
_FjdaryScuStatus_Object = MibTableColumn
fjdaryScuStatus = _FjdaryScuStatus_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 2, 9, 2, 1, 3),
    _FjdaryScuStatus_Type()
)
fjdaryScuStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fjdaryScuStatus.setStatus("current")
_FjdaryScuSubStatus_Type = FjdaryComponentStatus
_FjdaryScuSubStatus_Object = MibTableColumn
fjdaryScuSubStatus = _FjdaryScuSubStatus_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 2, 9, 2, 1, 4),
    _FjdaryScuSubStatus_Type()
)
fjdaryScuSubStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fjdaryScuSubStatus.setStatus("current")


class _FjdaryScuVoltage_Type(Integer32):
    """Custom type fjdaryScuVoltage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_FjdaryScuVoltage_Type.__name__ = "Integer32"
_FjdaryScuVoltage_Object = MibTableColumn
fjdaryScuVoltage = _FjdaryScuVoltage_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 2, 9, 2, 1, 5),
    _FjdaryScuVoltage_Type()
)
fjdaryScuVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fjdaryScuVoltage.setStatus("current")


class _FjdaryScuPartNo_Type(OctetString):
    """Custom type fjdaryScuPartNo based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_FjdaryScuPartNo_Type.__name__ = "OctetString"
_FjdaryScuPartNo_Object = MibTableColumn
fjdaryScuPartNo = _FjdaryScuPartNo_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 2, 9, 2, 1, 6),
    _FjdaryScuPartNo_Type()
)
fjdaryScuPartNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fjdaryScuPartNo.setStatus("current")


class _FjdaryScuSerialNo_Type(OctetString):
    """Custom type fjdaryScuSerialNo based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_FjdaryScuSerialNo_Type.__name__ = "OctetString"
_FjdaryScuSerialNo_Object = MibTableColumn
fjdaryScuSerialNo = _FjdaryScuSerialNo_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 2, 9, 2, 1, 7),
    _FjdaryScuSerialNo_Type()
)
fjdaryScuSerialNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fjdaryScuSerialNo.setStatus("current")


class _FjdaryScuRevision_Type(OctetString):
    """Custom type fjdaryScuRevision based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_FjdaryScuRevision_Type.__name__ = "OctetString"
_FjdaryScuRevision_Object = MibTableColumn
fjdaryScuRevision = _FjdaryScuRevision_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 2, 9, 2, 1, 8),
    _FjdaryScuRevision_Type()
)
fjdaryScuRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fjdaryScuRevision.setStatus("current")
_FjdaryCe_ObjectIdentity = ObjectIdentity
fjdaryCe = _FjdaryCe_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 2, 10)
)


class _FjdaryCeCount_Type(Integer32):
    """Custom type fjdaryCeCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_FjdaryCeCount_Type.__name__ = "Integer32"
_FjdaryCeCount_Object = MibScalar
fjdaryCeCount = _FjdaryCeCount_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 2, 10, 1),
    _FjdaryCeCount_Type()
)
fjdaryCeCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fjdaryCeCount.setStatus("current")
_FjdaryCeTable_Object = MibTable
fjdaryCeTable = _FjdaryCeTable_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 2, 10, 2)
)
if mibBuilder.loadTexts:
    fjdaryCeTable.setStatus("current")
_FjdaryCeEntry_Object = MibTableRow
fjdaryCeEntry = _FjdaryCeEntry_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 2, 10, 2, 1)
)
fjdaryCeEntry.setIndexNames(
    (0, "FJDARY-E150", "fjdaryCeIndex"),
)
if mibBuilder.loadTexts:
    fjdaryCeEntry.setStatus("current")


class _FjdaryCeIndex_Type(Integer32):
    """Custom type fjdaryCeIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_FjdaryCeIndex_Type.__name__ = "Integer32"
_FjdaryCeIndex_Object = MibTableColumn
fjdaryCeIndex = _FjdaryCeIndex_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 2, 10, 2, 1, 1),
    _FjdaryCeIndex_Type()
)
fjdaryCeIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fjdaryCeIndex.setStatus("current")


class _FjdaryCeItemId_Type(Integer32):
    """Custom type fjdaryCeItemId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_FjdaryCeItemId_Type.__name__ = "Integer32"
_FjdaryCeItemId_Object = MibTableColumn
fjdaryCeItemId = _FjdaryCeItemId_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 2, 10, 2, 1, 2),
    _FjdaryCeItemId_Type()
)
fjdaryCeItemId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fjdaryCeItemId.setStatus("current")
_FjdaryCeStatus_Type = FjdaryComponentStatus
_FjdaryCeStatus_Object = MibTableColumn
fjdaryCeStatus = _FjdaryCeStatus_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 2, 10, 2, 1, 3),
    _FjdaryCeStatus_Type()
)
fjdaryCeStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fjdaryCeStatus.setStatus("current")
_FjdaryCeSubStatus_Type = FjdaryComponentStatus
_FjdaryCeSubStatus_Object = MibTableColumn
fjdaryCeSubStatus = _FjdaryCeSubStatus_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 2, 10, 2, 1, 4),
    _FjdaryCeSubStatus_Type()
)
fjdaryCeSubStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fjdaryCeSubStatus.setStatus("current")
_FjdaryCeinletthml_ObjectIdentity = ObjectIdentity
fjdaryCeinletthml = _FjdaryCeinletthml_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 2, 11)
)


class _FjdaryCeinletthmlCount_Type(Integer32):
    """Custom type fjdaryCeinletthmlCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_FjdaryCeinletthmlCount_Type.__name__ = "Integer32"
_FjdaryCeinletthmlCount_Object = MibScalar
fjdaryCeinletthmlCount = _FjdaryCeinletthmlCount_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 2, 11, 1),
    _FjdaryCeinletthmlCount_Type()
)
fjdaryCeinletthmlCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fjdaryCeinletthmlCount.setStatus("current")
_FjdaryCeinletthmlTable_Object = MibTable
fjdaryCeinletthmlTable = _FjdaryCeinletthmlTable_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 2, 11, 2)
)
if mibBuilder.loadTexts:
    fjdaryCeinletthmlTable.setStatus("current")
_FjdaryCeinletthmlEntry_Object = MibTableRow
fjdaryCeinletthmlEntry = _FjdaryCeinletthmlEntry_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 2, 11, 2, 1)
)
fjdaryCeinletthmlEntry.setIndexNames(
    (0, "FJDARY-E150", "fjdaryCeinletthmlIndex"),
)
if mibBuilder.loadTexts:
    fjdaryCeinletthmlEntry.setStatus("current")


class _FjdaryCeinletthmlIndex_Type(Integer32):
    """Custom type fjdaryCeinletthmlIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_FjdaryCeinletthmlIndex_Type.__name__ = "Integer32"
_FjdaryCeinletthmlIndex_Object = MibTableColumn
fjdaryCeinletthmlIndex = _FjdaryCeinletthmlIndex_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 2, 11, 2, 1, 1),
    _FjdaryCeinletthmlIndex_Type()
)
fjdaryCeinletthmlIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fjdaryCeinletthmlIndex.setStatus("current")


class _FjdaryCeinletthmlItemId_Type(Integer32):
    """Custom type fjdaryCeinletthmlItemId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_FjdaryCeinletthmlItemId_Type.__name__ = "Integer32"
_FjdaryCeinletthmlItemId_Object = MibTableColumn
fjdaryCeinletthmlItemId = _FjdaryCeinletthmlItemId_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 2, 11, 2, 1, 2),
    _FjdaryCeinletthmlItemId_Type()
)
fjdaryCeinletthmlItemId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fjdaryCeinletthmlItemId.setStatus("current")
_FjdaryCeinletthmlStatus_Type = FjdaryComponentStatus
_FjdaryCeinletthmlStatus_Object = MibTableColumn
fjdaryCeinletthmlStatus = _FjdaryCeinletthmlStatus_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 2, 11, 2, 1, 3),
    _FjdaryCeinletthmlStatus_Type()
)
fjdaryCeinletthmlStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fjdaryCeinletthmlStatus.setStatus("current")
_FjdaryCeinletthmlSubStatus_Type = FjdaryComponentStatus
_FjdaryCeinletthmlSubStatus_Object = MibTableColumn
fjdaryCeinletthmlSubStatus = _FjdaryCeinletthmlSubStatus_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 2, 11, 2, 1, 4),
    _FjdaryCeinletthmlSubStatus_Type()
)
fjdaryCeinletthmlSubStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fjdaryCeinletthmlSubStatus.setStatus("current")
_FjdaryCethml_ObjectIdentity = ObjectIdentity
fjdaryCethml = _FjdaryCethml_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 2, 12)
)


class _FjdaryCethmlCount_Type(Integer32):
    """Custom type fjdaryCethmlCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_FjdaryCethmlCount_Type.__name__ = "Integer32"
_FjdaryCethmlCount_Object = MibScalar
fjdaryCethmlCount = _FjdaryCethmlCount_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 2, 12, 1),
    _FjdaryCethmlCount_Type()
)
fjdaryCethmlCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fjdaryCethmlCount.setStatus("current")
_FjdaryCethmlTable_Object = MibTable
fjdaryCethmlTable = _FjdaryCethmlTable_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 2, 12, 2)
)
if mibBuilder.loadTexts:
    fjdaryCethmlTable.setStatus("current")
_FjdaryCethmlEntry_Object = MibTableRow
fjdaryCethmlEntry = _FjdaryCethmlEntry_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 2, 12, 2, 1)
)
fjdaryCethmlEntry.setIndexNames(
    (0, "FJDARY-E150", "fjdaryCethmlIndex"),
)
if mibBuilder.loadTexts:
    fjdaryCethmlEntry.setStatus("current")


class _FjdaryCethmlIndex_Type(Integer32):
    """Custom type fjdaryCethmlIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_FjdaryCethmlIndex_Type.__name__ = "Integer32"
_FjdaryCethmlIndex_Object = MibTableColumn
fjdaryCethmlIndex = _FjdaryCethmlIndex_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 2, 12, 2, 1, 1),
    _FjdaryCethmlIndex_Type()
)
fjdaryCethmlIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fjdaryCethmlIndex.setStatus("current")


class _FjdaryCethmlItemId_Type(Integer32):
    """Custom type fjdaryCethmlItemId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_FjdaryCethmlItemId_Type.__name__ = "Integer32"
_FjdaryCethmlItemId_Object = MibTableColumn
fjdaryCethmlItemId = _FjdaryCethmlItemId_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 2, 12, 2, 1, 2),
    _FjdaryCethmlItemId_Type()
)
fjdaryCethmlItemId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fjdaryCethmlItemId.setStatus("current")
_FjdaryCethmlStatus_Type = FjdaryComponentStatus
_FjdaryCethmlStatus_Object = MibTableColumn
fjdaryCethmlStatus = _FjdaryCethmlStatus_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 2, 12, 2, 1, 3),
    _FjdaryCethmlStatus_Type()
)
fjdaryCethmlStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fjdaryCethmlStatus.setStatus("current")
_FjdaryCethmlSubStatus_Type = FjdaryComponentStatus
_FjdaryCethmlSubStatus_Object = MibTableColumn
fjdaryCethmlSubStatus = _FjdaryCethmlSubStatus_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 2, 12, 2, 1, 4),
    _FjdaryCethmlSubStatus_Type()
)
fjdaryCethmlSubStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fjdaryCethmlSubStatus.setStatus("current")
_FjdaryCpsu_ObjectIdentity = ObjectIdentity
fjdaryCpsu = _FjdaryCpsu_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 2, 13)
)


class _FjdaryCpsuCount_Type(Integer32):
    """Custom type fjdaryCpsuCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_FjdaryCpsuCount_Type.__name__ = "Integer32"
_FjdaryCpsuCount_Object = MibScalar
fjdaryCpsuCount = _FjdaryCpsuCount_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 2, 13, 1),
    _FjdaryCpsuCount_Type()
)
fjdaryCpsuCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fjdaryCpsuCount.setStatus("current")
_FjdaryCpsuTable_Object = MibTable
fjdaryCpsuTable = _FjdaryCpsuTable_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 2, 13, 2)
)
if mibBuilder.loadTexts:
    fjdaryCpsuTable.setStatus("current")
_FjdaryCpsuEntry_Object = MibTableRow
fjdaryCpsuEntry = _FjdaryCpsuEntry_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 2, 13, 2, 1)
)
fjdaryCpsuEntry.setIndexNames(
    (0, "FJDARY-E150", "fjdaryCpsuIndex"),
)
if mibBuilder.loadTexts:
    fjdaryCpsuEntry.setStatus("current")


class _FjdaryCpsuIndex_Type(Integer32):
    """Custom type fjdaryCpsuIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_FjdaryCpsuIndex_Type.__name__ = "Integer32"
_FjdaryCpsuIndex_Object = MibTableColumn
fjdaryCpsuIndex = _FjdaryCpsuIndex_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 2, 13, 2, 1, 1),
    _FjdaryCpsuIndex_Type()
)
fjdaryCpsuIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fjdaryCpsuIndex.setStatus("current")


class _FjdaryCpsuItemId_Type(Integer32):
    """Custom type fjdaryCpsuItemId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_FjdaryCpsuItemId_Type.__name__ = "Integer32"
_FjdaryCpsuItemId_Object = MibTableColumn
fjdaryCpsuItemId = _FjdaryCpsuItemId_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 2, 13, 2, 1, 2),
    _FjdaryCpsuItemId_Type()
)
fjdaryCpsuItemId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fjdaryCpsuItemId.setStatus("current")
_FjdaryCpsuStatus_Type = FjdaryComponentStatus
_FjdaryCpsuStatus_Object = MibTableColumn
fjdaryCpsuStatus = _FjdaryCpsuStatus_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 2, 13, 2, 1, 3),
    _FjdaryCpsuStatus_Type()
)
fjdaryCpsuStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fjdaryCpsuStatus.setStatus("current")
_FjdaryCpsuSubStatus_Type = FjdaryComponentStatus
_FjdaryCpsuSubStatus_Object = MibTableColumn
fjdaryCpsuSubStatus = _FjdaryCpsuSubStatus_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 2, 13, 2, 1, 4),
    _FjdaryCpsuSubStatus_Type()
)
fjdaryCpsuSubStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fjdaryCpsuSubStatus.setStatus("current")


class _FjdaryCpsuPartNo_Type(OctetString):
    """Custom type fjdaryCpsuPartNo based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_FjdaryCpsuPartNo_Type.__name__ = "OctetString"
_FjdaryCpsuPartNo_Object = MibTableColumn
fjdaryCpsuPartNo = _FjdaryCpsuPartNo_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 2, 13, 2, 1, 5),
    _FjdaryCpsuPartNo_Type()
)
fjdaryCpsuPartNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fjdaryCpsuPartNo.setStatus("current")


class _FjdaryCpsuSerialNo_Type(OctetString):
    """Custom type fjdaryCpsuSerialNo based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_FjdaryCpsuSerialNo_Type.__name__ = "OctetString"
_FjdaryCpsuSerialNo_Object = MibTableColumn
fjdaryCpsuSerialNo = _FjdaryCpsuSerialNo_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 2, 13, 2, 1, 6),
    _FjdaryCpsuSerialNo_Type()
)
fjdaryCpsuSerialNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fjdaryCpsuSerialNo.setStatus("current")


class _FjdaryCpsuRevision_Type(OctetString):
    """Custom type fjdaryCpsuRevision based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_FjdaryCpsuRevision_Type.__name__ = "OctetString"
_FjdaryCpsuRevision_Object = MibTableColumn
fjdaryCpsuRevision = _FjdaryCpsuRevision_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 2, 13, 2, 1, 7),
    _FjdaryCpsuRevision_Type()
)
fjdaryCpsuRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fjdaryCpsuRevision.setStatus("current")
_FjdaryDe_ObjectIdentity = ObjectIdentity
fjdaryDe = _FjdaryDe_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 2, 14)
)


class _FjdaryDeCount_Type(Integer32):
    """Custom type fjdaryDeCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_FjdaryDeCount_Type.__name__ = "Integer32"
_FjdaryDeCount_Object = MibScalar
fjdaryDeCount = _FjdaryDeCount_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 2, 14, 1),
    _FjdaryDeCount_Type()
)
fjdaryDeCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fjdaryDeCount.setStatus("current")
_FjdaryDeTable_Object = MibTable
fjdaryDeTable = _FjdaryDeTable_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 2, 14, 2)
)
if mibBuilder.loadTexts:
    fjdaryDeTable.setStatus("current")
_FjdaryDeEntry_Object = MibTableRow
fjdaryDeEntry = _FjdaryDeEntry_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 2, 14, 2, 1)
)
fjdaryDeEntry.setIndexNames(
    (0, "FJDARY-E150", "fjdaryDeIndex"),
)
if mibBuilder.loadTexts:
    fjdaryDeEntry.setStatus("current")


class _FjdaryDeIndex_Type(Integer32):
    """Custom type fjdaryDeIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_FjdaryDeIndex_Type.__name__ = "Integer32"
_FjdaryDeIndex_Object = MibTableColumn
fjdaryDeIndex = _FjdaryDeIndex_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 2, 14, 2, 1, 1),
    _FjdaryDeIndex_Type()
)
fjdaryDeIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fjdaryDeIndex.setStatus("current")


class _FjdaryDeItemId_Type(Integer32):
    """Custom type fjdaryDeItemId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_FjdaryDeItemId_Type.__name__ = "Integer32"
_FjdaryDeItemId_Object = MibTableColumn
fjdaryDeItemId = _FjdaryDeItemId_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 2, 14, 2, 1, 2),
    _FjdaryDeItemId_Type()
)
fjdaryDeItemId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fjdaryDeItemId.setStatus("current")
_FjdaryDeStatus_Type = FjdaryComponentStatus
_FjdaryDeStatus_Object = MibTableColumn
fjdaryDeStatus = _FjdaryDeStatus_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 2, 14, 2, 1, 3),
    _FjdaryDeStatus_Type()
)
fjdaryDeStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fjdaryDeStatus.setStatus("current")
_FjdaryDeSubStatus_Type = FjdaryComponentStatus
_FjdaryDeSubStatus_Object = MibTableColumn
fjdaryDeSubStatus = _FjdaryDeSubStatus_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 2, 14, 2, 1, 4),
    _FjdaryDeSubStatus_Type()
)
fjdaryDeSubStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fjdaryDeSubStatus.setStatus("current")


class _FjdaryDeId_Type(Integer32):
    """Custom type fjdaryDeId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_FjdaryDeId_Type.__name__ = "Integer32"
_FjdaryDeId_Object = MibTableColumn
fjdaryDeId = _FjdaryDeId_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 2, 14, 2, 1, 5),
    _FjdaryDeId_Type()
)
fjdaryDeId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fjdaryDeId.setStatus("current")


class _FjdaryDeType_Type(Integer32):
    """Custom type fjdaryDeType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_FjdaryDeType_Type.__name__ = "Integer32"
_FjdaryDeType_Object = MibTableColumn
fjdaryDeType = _FjdaryDeType_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 2, 14, 2, 1, 6),
    _FjdaryDeType_Type()
)
fjdaryDeType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fjdaryDeType.setStatus("current")
_FjdaryIom_ObjectIdentity = ObjectIdentity
fjdaryIom = _FjdaryIom_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 2, 15)
)


class _FjdaryIomCount_Type(Integer32):
    """Custom type fjdaryIomCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_FjdaryIomCount_Type.__name__ = "Integer32"
_FjdaryIomCount_Object = MibScalar
fjdaryIomCount = _FjdaryIomCount_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 2, 15, 1),
    _FjdaryIomCount_Type()
)
fjdaryIomCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fjdaryIomCount.setStatus("current")
_FjdaryIomTable_Object = MibTable
fjdaryIomTable = _FjdaryIomTable_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 2, 15, 2)
)
if mibBuilder.loadTexts:
    fjdaryIomTable.setStatus("current")
_FjdaryIomEntry_Object = MibTableRow
fjdaryIomEntry = _FjdaryIomEntry_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 2, 15, 2, 1)
)
fjdaryIomEntry.setIndexNames(
    (0, "FJDARY-E150", "fjdaryIomIndex"),
)
if mibBuilder.loadTexts:
    fjdaryIomEntry.setStatus("current")


class _FjdaryIomIndex_Type(Integer32):
    """Custom type fjdaryIomIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_FjdaryIomIndex_Type.__name__ = "Integer32"
_FjdaryIomIndex_Object = MibTableColumn
fjdaryIomIndex = _FjdaryIomIndex_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 2, 15, 2, 1, 1),
    _FjdaryIomIndex_Type()
)
fjdaryIomIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fjdaryIomIndex.setStatus("current")


class _FjdaryIomItemId_Type(Integer32):
    """Custom type fjdaryIomItemId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_FjdaryIomItemId_Type.__name__ = "Integer32"
_FjdaryIomItemId_Object = MibTableColumn
fjdaryIomItemId = _FjdaryIomItemId_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 2, 15, 2, 1, 2),
    _FjdaryIomItemId_Type()
)
fjdaryIomItemId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fjdaryIomItemId.setStatus("current")
_FjdaryIomStatus_Type = FjdaryComponentStatus
_FjdaryIomStatus_Object = MibTableColumn
fjdaryIomStatus = _FjdaryIomStatus_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 2, 15, 2, 1, 3),
    _FjdaryIomStatus_Type()
)
fjdaryIomStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fjdaryIomStatus.setStatus("current")
_FjdaryIomSubStatus_Type = FjdaryComponentStatus
_FjdaryIomSubStatus_Object = MibTableColumn
fjdaryIomSubStatus = _FjdaryIomSubStatus_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 2, 15, 2, 1, 4),
    _FjdaryIomSubStatus_Type()
)
fjdaryIomSubStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fjdaryIomSubStatus.setStatus("current")


class _FjdaryIomFirmInfo_Type(OctetString):
    """Custom type fjdaryIomFirmInfo based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_FjdaryIomFirmInfo_Type.__name__ = "OctetString"
_FjdaryIomFirmInfo_Object = MibTableColumn
fjdaryIomFirmInfo = _FjdaryIomFirmInfo_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 2, 15, 2, 1, 5),
    _FjdaryIomFirmInfo_Type()
)
fjdaryIomFirmInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fjdaryIomFirmInfo.setStatus("current")


class _FjdaryIomPartNo_Type(OctetString):
    """Custom type fjdaryIomPartNo based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_FjdaryIomPartNo_Type.__name__ = "OctetString"
_FjdaryIomPartNo_Object = MibTableColumn
fjdaryIomPartNo = _FjdaryIomPartNo_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 2, 15, 2, 1, 6),
    _FjdaryIomPartNo_Type()
)
fjdaryIomPartNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fjdaryIomPartNo.setStatus("current")


class _FjdaryIomSerialNo_Type(OctetString):
    """Custom type fjdaryIomSerialNo based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_FjdaryIomSerialNo_Type.__name__ = "OctetString"
_FjdaryIomSerialNo_Object = MibTableColumn
fjdaryIomSerialNo = _FjdaryIomSerialNo_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 2, 15, 2, 1, 7),
    _FjdaryIomSerialNo_Type()
)
fjdaryIomSerialNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fjdaryIomSerialNo.setStatus("current")


class _FjdaryIomRevision_Type(OctetString):
    """Custom type fjdaryIomRevision based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_FjdaryIomRevision_Type.__name__ = "OctetString"
_FjdaryIomRevision_Object = MibTableColumn
fjdaryIomRevision = _FjdaryIomRevision_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 2, 15, 2, 1, 8),
    _FjdaryIomRevision_Type()
)
fjdaryIomRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fjdaryIomRevision.setStatus("current")
_FjdaryPsu_ObjectIdentity = ObjectIdentity
fjdaryPsu = _FjdaryPsu_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 2, 16)
)


class _FjdaryPsuCount_Type(Integer32):
    """Custom type fjdaryPsuCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_FjdaryPsuCount_Type.__name__ = "Integer32"
_FjdaryPsuCount_Object = MibScalar
fjdaryPsuCount = _FjdaryPsuCount_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 2, 16, 1),
    _FjdaryPsuCount_Type()
)
fjdaryPsuCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fjdaryPsuCount.setStatus("current")
_FjdaryPsuTable_Object = MibTable
fjdaryPsuTable = _FjdaryPsuTable_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 2, 16, 2)
)
if mibBuilder.loadTexts:
    fjdaryPsuTable.setStatus("current")
_FjdaryPsuEntry_Object = MibTableRow
fjdaryPsuEntry = _FjdaryPsuEntry_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 2, 16, 2, 1)
)
fjdaryPsuEntry.setIndexNames(
    (0, "FJDARY-E150", "fjdaryPsuIndex"),
)
if mibBuilder.loadTexts:
    fjdaryPsuEntry.setStatus("current")


class _FjdaryPsuIndex_Type(Integer32):
    """Custom type fjdaryPsuIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_FjdaryPsuIndex_Type.__name__ = "Integer32"
_FjdaryPsuIndex_Object = MibTableColumn
fjdaryPsuIndex = _FjdaryPsuIndex_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 2, 16, 2, 1, 1),
    _FjdaryPsuIndex_Type()
)
fjdaryPsuIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fjdaryPsuIndex.setStatus("current")


class _FjdaryPsuItemId_Type(Integer32):
    """Custom type fjdaryPsuItemId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_FjdaryPsuItemId_Type.__name__ = "Integer32"
_FjdaryPsuItemId_Object = MibTableColumn
fjdaryPsuItemId = _FjdaryPsuItemId_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 2, 16, 2, 1, 2),
    _FjdaryPsuItemId_Type()
)
fjdaryPsuItemId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fjdaryPsuItemId.setStatus("current")
_FjdaryPsuStatus_Type = FjdaryComponentStatus
_FjdaryPsuStatus_Object = MibTableColumn
fjdaryPsuStatus = _FjdaryPsuStatus_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 2, 16, 2, 1, 3),
    _FjdaryPsuStatus_Type()
)
fjdaryPsuStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fjdaryPsuStatus.setStatus("current")
_FjdaryPsuSubStatus_Type = FjdaryComponentStatus
_FjdaryPsuSubStatus_Object = MibTableColumn
fjdaryPsuSubStatus = _FjdaryPsuSubStatus_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 2, 16, 2, 1, 4),
    _FjdaryPsuSubStatus_Type()
)
fjdaryPsuSubStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fjdaryPsuSubStatus.setStatus("current")


class _FjdaryPsuPartNo_Type(OctetString):
    """Custom type fjdaryPsuPartNo based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_FjdaryPsuPartNo_Type.__name__ = "OctetString"
_FjdaryPsuPartNo_Object = MibTableColumn
fjdaryPsuPartNo = _FjdaryPsuPartNo_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 2, 16, 2, 1, 5),
    _FjdaryPsuPartNo_Type()
)
fjdaryPsuPartNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fjdaryPsuPartNo.setStatus("current")


class _FjdaryPsuSerialNo_Type(OctetString):
    """Custom type fjdaryPsuSerialNo based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_FjdaryPsuSerialNo_Type.__name__ = "OctetString"
_FjdaryPsuSerialNo_Object = MibTableColumn
fjdaryPsuSerialNo = _FjdaryPsuSerialNo_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 2, 16, 2, 1, 6),
    _FjdaryPsuSerialNo_Type()
)
fjdaryPsuSerialNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fjdaryPsuSerialNo.setStatus("current")


class _FjdaryPsuRevision_Type(OctetString):
    """Custom type fjdaryPsuRevision based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_FjdaryPsuRevision_Type.__name__ = "OctetString"
_FjdaryPsuRevision_Object = MibTableColumn
fjdaryPsuRevision = _FjdaryPsuRevision_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 2, 16, 2, 1, 7),
    _FjdaryPsuRevision_Type()
)
fjdaryPsuRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fjdaryPsuRevision.setStatus("current")
_FjdaryDeinletthml_ObjectIdentity = ObjectIdentity
fjdaryDeinletthml = _FjdaryDeinletthml_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 2, 17)
)


class _FjdaryDeinletthmlCount_Type(Integer32):
    """Custom type fjdaryDeinletthmlCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_FjdaryDeinletthmlCount_Type.__name__ = "Integer32"
_FjdaryDeinletthmlCount_Object = MibScalar
fjdaryDeinletthmlCount = _FjdaryDeinletthmlCount_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 2, 17, 1),
    _FjdaryDeinletthmlCount_Type()
)
fjdaryDeinletthmlCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fjdaryDeinletthmlCount.setStatus("current")
_FjdaryDeinletthmlTable_Object = MibTable
fjdaryDeinletthmlTable = _FjdaryDeinletthmlTable_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 2, 17, 2)
)
if mibBuilder.loadTexts:
    fjdaryDeinletthmlTable.setStatus("current")
_FjdaryDeinletthmlEntry_Object = MibTableRow
fjdaryDeinletthmlEntry = _FjdaryDeinletthmlEntry_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 2, 17, 2, 1)
)
fjdaryDeinletthmlEntry.setIndexNames(
    (0, "FJDARY-E150", "fjdaryDeinletthmlIndex"),
)
if mibBuilder.loadTexts:
    fjdaryDeinletthmlEntry.setStatus("current")


class _FjdaryDeinletthmlIndex_Type(Integer32):
    """Custom type fjdaryDeinletthmlIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_FjdaryDeinletthmlIndex_Type.__name__ = "Integer32"
_FjdaryDeinletthmlIndex_Object = MibTableColumn
fjdaryDeinletthmlIndex = _FjdaryDeinletthmlIndex_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 2, 17, 2, 1, 1),
    _FjdaryDeinletthmlIndex_Type()
)
fjdaryDeinletthmlIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fjdaryDeinletthmlIndex.setStatus("current")


class _FjdaryDeinletthmlItemId_Type(Integer32):
    """Custom type fjdaryDeinletthmlItemId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_FjdaryDeinletthmlItemId_Type.__name__ = "Integer32"
_FjdaryDeinletthmlItemId_Object = MibTableColumn
fjdaryDeinletthmlItemId = _FjdaryDeinletthmlItemId_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 2, 17, 2, 1, 2),
    _FjdaryDeinletthmlItemId_Type()
)
fjdaryDeinletthmlItemId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fjdaryDeinletthmlItemId.setStatus("current")
_FjdaryDeinletthmlStatus_Type = FjdaryComponentStatus
_FjdaryDeinletthmlStatus_Object = MibTableColumn
fjdaryDeinletthmlStatus = _FjdaryDeinletthmlStatus_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 2, 17, 2, 1, 3),
    _FjdaryDeinletthmlStatus_Type()
)
fjdaryDeinletthmlStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fjdaryDeinletthmlStatus.setStatus("current")
_FjdaryDeinletthmlSubStatus_Type = FjdaryComponentStatus
_FjdaryDeinletthmlSubStatus_Object = MibTableColumn
fjdaryDeinletthmlSubStatus = _FjdaryDeinletthmlSubStatus_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 2, 17, 2, 1, 4),
    _FjdaryDeinletthmlSubStatus_Type()
)
fjdaryDeinletthmlSubStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fjdaryDeinletthmlSubStatus.setStatus("current")
_FjdaryDethml_ObjectIdentity = ObjectIdentity
fjdaryDethml = _FjdaryDethml_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 2, 18)
)


class _FjdaryDethmlCount_Type(Integer32):
    """Custom type fjdaryDethmlCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_FjdaryDethmlCount_Type.__name__ = "Integer32"
_FjdaryDethmlCount_Object = MibScalar
fjdaryDethmlCount = _FjdaryDethmlCount_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 2, 18, 1),
    _FjdaryDethmlCount_Type()
)
fjdaryDethmlCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fjdaryDethmlCount.setStatus("current")
_FjdaryDethmlTable_Object = MibTable
fjdaryDethmlTable = _FjdaryDethmlTable_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 2, 18, 2)
)
if mibBuilder.loadTexts:
    fjdaryDethmlTable.setStatus("current")
_FjdaryDethmlEntry_Object = MibTableRow
fjdaryDethmlEntry = _FjdaryDethmlEntry_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 2, 18, 2, 1)
)
fjdaryDethmlEntry.setIndexNames(
    (0, "FJDARY-E150", "fjdaryDethmlIndex"),
)
if mibBuilder.loadTexts:
    fjdaryDethmlEntry.setStatus("current")


class _FjdaryDethmlIndex_Type(Integer32):
    """Custom type fjdaryDethmlIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_FjdaryDethmlIndex_Type.__name__ = "Integer32"
_FjdaryDethmlIndex_Object = MibTableColumn
fjdaryDethmlIndex = _FjdaryDethmlIndex_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 2, 18, 2, 1, 1),
    _FjdaryDethmlIndex_Type()
)
fjdaryDethmlIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fjdaryDethmlIndex.setStatus("current")


class _FjdaryDethmlItemId_Type(Integer32):
    """Custom type fjdaryDethmlItemId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_FjdaryDethmlItemId_Type.__name__ = "Integer32"
_FjdaryDethmlItemId_Object = MibTableColumn
fjdaryDethmlItemId = _FjdaryDethmlItemId_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 2, 18, 2, 1, 2),
    _FjdaryDethmlItemId_Type()
)
fjdaryDethmlItemId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fjdaryDethmlItemId.setStatus("current")
_FjdaryDethmlStatus_Type = FjdaryComponentStatus
_FjdaryDethmlStatus_Object = MibTableColumn
fjdaryDethmlStatus = _FjdaryDethmlStatus_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 2, 18, 2, 1, 3),
    _FjdaryDethmlStatus_Type()
)
fjdaryDethmlStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fjdaryDethmlStatus.setStatus("current")
_FjdaryDethmlSubStatus_Type = FjdaryComponentStatus
_FjdaryDethmlSubStatus_Object = MibTableColumn
fjdaryDethmlSubStatus = _FjdaryDethmlSubStatus_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 2, 18, 2, 1, 4),
    _FjdaryDethmlSubStatus_Type()
)
fjdaryDethmlSubStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fjdaryDethmlSubStatus.setStatus("current")
_FjdaryDisk_ObjectIdentity = ObjectIdentity
fjdaryDisk = _FjdaryDisk_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 2, 19)
)


class _FjdaryDiskCount_Type(Integer32):
    """Custom type fjdaryDiskCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_FjdaryDiskCount_Type.__name__ = "Integer32"
_FjdaryDiskCount_Object = MibScalar
fjdaryDiskCount = _FjdaryDiskCount_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 2, 19, 1),
    _FjdaryDiskCount_Type()
)
fjdaryDiskCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fjdaryDiskCount.setStatus("current")
_FjdaryDiskTable_Object = MibTable
fjdaryDiskTable = _FjdaryDiskTable_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 2, 19, 2)
)
if mibBuilder.loadTexts:
    fjdaryDiskTable.setStatus("current")
_FjdaryDiskEntry_Object = MibTableRow
fjdaryDiskEntry = _FjdaryDiskEntry_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 2, 19, 2, 1)
)
fjdaryDiskEntry.setIndexNames(
    (0, "FJDARY-E150", "fjdaryDiskIndex"),
)
if mibBuilder.loadTexts:
    fjdaryDiskEntry.setStatus("current")


class _FjdaryDiskIndex_Type(Integer32):
    """Custom type fjdaryDiskIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_FjdaryDiskIndex_Type.__name__ = "Integer32"
_FjdaryDiskIndex_Object = MibTableColumn
fjdaryDiskIndex = _FjdaryDiskIndex_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 2, 19, 2, 1, 1),
    _FjdaryDiskIndex_Type()
)
fjdaryDiskIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fjdaryDiskIndex.setStatus("current")


class _FjdaryDiskItemId_Type(Integer32):
    """Custom type fjdaryDiskItemId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_FjdaryDiskItemId_Type.__name__ = "Integer32"
_FjdaryDiskItemId_Object = MibTableColumn
fjdaryDiskItemId = _FjdaryDiskItemId_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 2, 19, 2, 1, 2),
    _FjdaryDiskItemId_Type()
)
fjdaryDiskItemId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fjdaryDiskItemId.setStatus("current")


class _FjdaryDiskStatus_Type(Integer32):
    """Custom type fjdaryDiskStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              64,
              65,
              66,
              67,
              68,
              69)
        )
    )
    namedValues = NamedValues(
        *(("available", 1),
          ("broken", 2),
          ("copying", 69),
          ("formatting", 66),
          ("notavailable", 3),
          ("notexist", 68),
          ("notsupported", 4),
          ("partbroken", 64),
          ("present", 5),
          ("readying", 6),
          ("recovering", 7),
          ("spare", 65),
          ("unformatted", 67))
    )


_FjdaryDiskStatus_Type.__name__ = "Integer32"
_FjdaryDiskStatus_Object = MibTableColumn
fjdaryDiskStatus = _FjdaryDiskStatus_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 2, 19, 2, 1, 3),
    _FjdaryDiskStatus_Type()
)
fjdaryDiskStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fjdaryDiskStatus.setStatus("current")


class _FjdaryDiskSubStatus_Type(Integer32):
    """Custom type fjdaryDiskSubStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              64,
              65,
              66,
              67,
              68,
              69)
        )
    )
    namedValues = NamedValues(
        *(("available", 1),
          ("broken", 2),
          ("copying", 69),
          ("formatting", 66),
          ("notavailable", 3),
          ("notexist", 68),
          ("notsupported", 4),
          ("partbroken", 64),
          ("present", 5),
          ("readying", 6),
          ("recovering", 7),
          ("spare", 65),
          ("unformatted", 67))
    )


_FjdaryDiskSubStatus_Type.__name__ = "Integer32"
_FjdaryDiskSubStatus_Object = MibTableColumn
fjdaryDiskSubStatus = _FjdaryDiskSubStatus_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 2, 19, 2, 1, 4),
    _FjdaryDiskSubStatus_Type()
)
fjdaryDiskSubStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fjdaryDiskSubStatus.setStatus("current")
_FjdaryDiskCompStatus_Type = FjdaryComponentStatus
_FjdaryDiskCompStatus_Object = MibTableColumn
fjdaryDiskCompStatus = _FjdaryDiskCompStatus_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 2, 19, 2, 1, 5),
    _FjdaryDiskCompStatus_Type()
)
fjdaryDiskCompStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fjdaryDiskCompStatus.setStatus("current")
_FjdaryDiskCompSubStatus_Type = FjdaryComponentStatus
_FjdaryDiskCompSubStatus_Object = MibTableColumn
fjdaryDiskCompSubStatus = _FjdaryDiskCompSubStatus_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 2, 19, 2, 1, 6),
    _FjdaryDiskCompSubStatus_Type()
)
fjdaryDiskCompSubStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fjdaryDiskCompSubStatus.setStatus("current")


class _FjdaryDiskPlun_Type(Integer32):
    """Custom type fjdaryDiskPlun based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_FjdaryDiskPlun_Type.__name__ = "Integer32"
_FjdaryDiskPlun_Object = MibTableColumn
fjdaryDiskPlun = _FjdaryDiskPlun_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 2, 19, 2, 1, 7),
    _FjdaryDiskPlun_Type()
)
fjdaryDiskPlun.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fjdaryDiskPlun.setStatus("current")


class _FjdaryDiskPurpose_Type(Integer32):
    """Custom type fjdaryDiskPurpose based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_FjdaryDiskPurpose_Type.__name__ = "Integer32"
_FjdaryDiskPurpose_Object = MibTableColumn
fjdaryDiskPurpose = _FjdaryDiskPurpose_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 2, 19, 2, 1, 8),
    _FjdaryDiskPurpose_Type()
)
fjdaryDiskPurpose.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fjdaryDiskPurpose.setStatus("current")


class _FjdaryDiskType_Type(Integer32):
    """Custom type fjdaryDiskType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_FjdaryDiskType_Type.__name__ = "Integer32"
_FjdaryDiskType_Object = MibTableColumn
fjdaryDiskType = _FjdaryDiskType_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 2, 19, 2, 1, 9),
    _FjdaryDiskType_Type()
)
fjdaryDiskType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fjdaryDiskType.setStatus("current")


class _FjdaryDiskWwn_Type(OctetString):
    """Custom type fjdaryDiskWwn based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_FjdaryDiskWwn_Type.__name__ = "OctetString"
_FjdaryDiskWwn_Object = MibTableColumn
fjdaryDiskWwn = _FjdaryDiskWwn_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 2, 19, 2, 1, 10),
    _FjdaryDiskWwn_Type()
)
fjdaryDiskWwn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fjdaryDiskWwn.setStatus("current")


class _FjdaryDiskVenderId_Type(OctetString):
    """Custom type fjdaryDiskVenderId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_FjdaryDiskVenderId_Type.__name__ = "OctetString"
_FjdaryDiskVenderId_Object = MibTableColumn
fjdaryDiskVenderId = _FjdaryDiskVenderId_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 2, 19, 2, 1, 11),
    _FjdaryDiskVenderId_Type()
)
fjdaryDiskVenderId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fjdaryDiskVenderId.setStatus("current")


class _FjdaryDiskProductId_Type(OctetString):
    """Custom type fjdaryDiskProductId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_FjdaryDiskProductId_Type.__name__ = "OctetString"
_FjdaryDiskProductId_Object = MibTableColumn
fjdaryDiskProductId = _FjdaryDiskProductId_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 2, 19, 2, 1, 12),
    _FjdaryDiskProductId_Type()
)
fjdaryDiskProductId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fjdaryDiskProductId.setStatus("current")


class _FjdaryDiskFwRevision_Type(OctetString):
    """Custom type fjdaryDiskFwRevision based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_FjdaryDiskFwRevision_Type.__name__ = "OctetString"
_FjdaryDiskFwRevision_Object = MibTableColumn
fjdaryDiskFwRevision = _FjdaryDiskFwRevision_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 2, 19, 2, 1, 13),
    _FjdaryDiskFwRevision_Type()
)
fjdaryDiskFwRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fjdaryDiskFwRevision.setStatus("current")


class _FjdaryDiskDateCode_Type(OctetString):
    """Custom type fjdaryDiskDateCode based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_FjdaryDiskDateCode_Type.__name__ = "OctetString"
_FjdaryDiskDateCode_Object = MibTableColumn
fjdaryDiskDateCode = _FjdaryDiskDateCode_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 2, 19, 2, 1, 14),
    _FjdaryDiskDateCode_Type()
)
fjdaryDiskDateCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fjdaryDiskDateCode.setStatus("current")


class _FjdaryDiskCfgRevision_Type(OctetString):
    """Custom type fjdaryDiskCfgRevision based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_FjdaryDiskCfgRevision_Type.__name__ = "OctetString"
_FjdaryDiskCfgRevision_Object = MibTableColumn
fjdaryDiskCfgRevision = _FjdaryDiskCfgRevision_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 2, 19, 2, 1, 15),
    _FjdaryDiskCfgRevision_Type()
)
fjdaryDiskCfgRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fjdaryDiskCfgRevision.setStatus("current")


class _FjdaryDiskSize_Type(Integer32):
    """Custom type fjdaryDiskSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_FjdaryDiskSize_Type.__name__ = "Integer32"
_FjdaryDiskSize_Object = MibTableColumn
fjdaryDiskSize = _FjdaryDiskSize_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 2, 19, 2, 1, 16),
    _FjdaryDiskSize_Type()
)
fjdaryDiskSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fjdaryDiskSize.setStatus("current")
_FjdaryLanport_ObjectIdentity = ObjectIdentity
fjdaryLanport = _FjdaryLanport_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 2, 20)
)


class _FjdaryLanportCount_Type(Integer32):
    """Custom type fjdaryLanportCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_FjdaryLanportCount_Type.__name__ = "Integer32"
_FjdaryLanportCount_Object = MibScalar
fjdaryLanportCount = _FjdaryLanportCount_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 2, 20, 1),
    _FjdaryLanportCount_Type()
)
fjdaryLanportCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fjdaryLanportCount.setStatus("current")
_FjdaryLanportTable_Object = MibTable
fjdaryLanportTable = _FjdaryLanportTable_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 2, 20, 2)
)
if mibBuilder.loadTexts:
    fjdaryLanportTable.setStatus("current")
_FjdaryLanportEntry_Object = MibTableRow
fjdaryLanportEntry = _FjdaryLanportEntry_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 2, 20, 2, 1)
)
fjdaryLanportEntry.setIndexNames(
    (0, "FJDARY-E150", "fjdaryLanportIndex"),
)
if mibBuilder.loadTexts:
    fjdaryLanportEntry.setStatus("current")


class _FjdaryLanportIndex_Type(Integer32):
    """Custom type fjdaryLanportIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_FjdaryLanportIndex_Type.__name__ = "Integer32"
_FjdaryLanportIndex_Object = MibTableColumn
fjdaryLanportIndex = _FjdaryLanportIndex_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 2, 20, 2, 1, 1),
    _FjdaryLanportIndex_Type()
)
fjdaryLanportIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fjdaryLanportIndex.setStatus("current")


class _FjdaryLanportStatus0_Type(Integer32):
    """Custom type fjdaryLanportStatus0 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              4,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("linkdown", 6),
          ("linkup", 1),
          ("undefined", 4),
          ("unknown", 7))
    )


_FjdaryLanportStatus0_Type.__name__ = "Integer32"
_FjdaryLanportStatus0_Object = MibTableColumn
fjdaryLanportStatus0 = _FjdaryLanportStatus0_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 2, 20, 2, 1, 2),
    _FjdaryLanportStatus0_Type()
)
fjdaryLanportStatus0.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fjdaryLanportStatus0.setStatus("current")


class _FjdaryLanportStatus1_Type(Integer32):
    """Custom type fjdaryLanportStatus1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              4,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("linkdown", 6),
          ("linkup", 1),
          ("undefined", 4),
          ("unknown", 7))
    )


_FjdaryLanportStatus1_Type.__name__ = "Integer32"
_FjdaryLanportStatus1_Object = MibTableColumn
fjdaryLanportStatus1 = _FjdaryLanportStatus1_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 2, 20, 2, 1, 3),
    _FjdaryLanportStatus1_Type()
)
fjdaryLanportStatus1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fjdaryLanportStatus1.setStatus("current")


class _FjdaryLanportStatus2_Type(Integer32):
    """Custom type fjdaryLanportStatus2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              4,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("linkdown", 6),
          ("linkup", 1),
          ("undefined", 4),
          ("unknown", 7))
    )


_FjdaryLanportStatus2_Type.__name__ = "Integer32"
_FjdaryLanportStatus2_Object = MibTableColumn
fjdaryLanportStatus2 = _FjdaryLanportStatus2_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 2, 20, 2, 1, 4),
    _FjdaryLanportStatus2_Type()
)
fjdaryLanportStatus2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fjdaryLanportStatus2.setStatus("current")
_FjdaryLanportHwAdTable_Object = MibTable
fjdaryLanportHwAdTable = _FjdaryLanportHwAdTable_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 2, 20, 3)
)
if mibBuilder.loadTexts:
    fjdaryLanportHwAdTable.setStatus("current")
_FjdaryLanportHwAdEntry_Object = MibTableRow
fjdaryLanportHwAdEntry = _FjdaryLanportHwAdEntry_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 2, 20, 3, 1)
)
fjdaryLanportHwAdEntry.setIndexNames(
    (0, "FJDARY-E150", "fjdaryLanportHwAdIndex"),
)
if mibBuilder.loadTexts:
    fjdaryLanportHwAdEntry.setStatus("current")


class _FjdaryLanportHwAdIndex_Type(Integer32):
    """Custom type fjdaryLanportHwAdIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_FjdaryLanportHwAdIndex_Type.__name__ = "Integer32"
_FjdaryLanportHwAdIndex_Object = MibTableColumn
fjdaryLanportHwAdIndex = _FjdaryLanportHwAdIndex_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 2, 20, 3, 1, 1),
    _FjdaryLanportHwAdIndex_Type()
)
fjdaryLanportHwAdIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fjdaryLanportHwAdIndex.setStatus("current")
_FjdaryLanportHwAddress0_Type = PhysAddress
_FjdaryLanportHwAddress0_Object = MibTableColumn
fjdaryLanportHwAddress0 = _FjdaryLanportHwAddress0_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 2, 20, 3, 1, 2),
    _FjdaryLanportHwAddress0_Type()
)
fjdaryLanportHwAddress0.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fjdaryLanportHwAddress0.setStatus("current")
_FjdaryLanportHwAddress1_Type = PhysAddress
_FjdaryLanportHwAddress1_Object = MibTableColumn
fjdaryLanportHwAddress1 = _FjdaryLanportHwAddress1_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 2, 20, 3, 1, 3),
    _FjdaryLanportHwAddress1_Type()
)
fjdaryLanportHwAddress1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fjdaryLanportHwAddress1.setStatus("current")
_FjdaryLanportHwAddress2_Type = PhysAddress
_FjdaryLanportHwAddress2_Object = MibTableColumn
fjdaryLanportHwAddress2 = _FjdaryLanportHwAddress2_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 2, 20, 3, 1, 4),
    _FjdaryLanportHwAddress2_Type()
)
fjdaryLanportHwAddress2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fjdaryLanportHwAddress2.setStatus("current")
_FjdaryFem_ObjectIdentity = ObjectIdentity
fjdaryFem = _FjdaryFem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 2, 21)
)


class _FjdaryFemCount_Type(Integer32):
    """Custom type fjdaryFemCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_FjdaryFemCount_Type.__name__ = "Integer32"
_FjdaryFemCount_Object = MibScalar
fjdaryFemCount = _FjdaryFemCount_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 2, 21, 1),
    _FjdaryFemCount_Type()
)
fjdaryFemCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fjdaryFemCount.setStatus("current")
_FjdaryFemTable_Object = MibTable
fjdaryFemTable = _FjdaryFemTable_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 2, 21, 2)
)
if mibBuilder.loadTexts:
    fjdaryFemTable.setStatus("current")
_FjdaryFemEntry_Object = MibTableRow
fjdaryFemEntry = _FjdaryFemEntry_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 2, 21, 2, 1)
)
fjdaryFemEntry.setIndexNames(
    (0, "FJDARY-E150", "fjdaryFemIndex"),
)
if mibBuilder.loadTexts:
    fjdaryFemEntry.setStatus("current")


class _FjdaryFemIndex_Type(Integer32):
    """Custom type fjdaryFemIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_FjdaryFemIndex_Type.__name__ = "Integer32"
_FjdaryFemIndex_Object = MibTableColumn
fjdaryFemIndex = _FjdaryFemIndex_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 2, 21, 2, 1, 1),
    _FjdaryFemIndex_Type()
)
fjdaryFemIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fjdaryFemIndex.setStatus("current")


class _FjdaryFemItemId_Type(Integer32):
    """Custom type fjdaryFemItemId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_FjdaryFemItemId_Type.__name__ = "Integer32"
_FjdaryFemItemId_Object = MibTableColumn
fjdaryFemItemId = _FjdaryFemItemId_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 2, 21, 2, 1, 2),
    _FjdaryFemItemId_Type()
)
fjdaryFemItemId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fjdaryFemItemId.setStatus("current")
_FjdaryFemStatus_Type = FjdaryComponentStatus
_FjdaryFemStatus_Object = MibTableColumn
fjdaryFemStatus = _FjdaryFemStatus_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 2, 21, 2, 1, 3),
    _FjdaryFemStatus_Type()
)
fjdaryFemStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fjdaryFemStatus.setStatus("current")
_FjdaryFemSubStatus_Type = FjdaryComponentStatus
_FjdaryFemSubStatus_Object = MibTableColumn
fjdaryFemSubStatus = _FjdaryFemSubStatus_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 2, 21, 2, 1, 4),
    _FjdaryFemSubStatus_Type()
)
fjdaryFemSubStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fjdaryFemSubStatus.setStatus("current")
_FjdaryPfm_ObjectIdentity = ObjectIdentity
fjdaryPfm = _FjdaryPfm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 2, 22)
)


class _FjdaryPfmCount_Type(Integer32):
    """Custom type fjdaryPfmCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_FjdaryPfmCount_Type.__name__ = "Integer32"
_FjdaryPfmCount_Object = MibScalar
fjdaryPfmCount = _FjdaryPfmCount_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 2, 22, 1),
    _FjdaryPfmCount_Type()
)
fjdaryPfmCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fjdaryPfmCount.setStatus("current")
_FjdaryPfmTable_Object = MibTable
fjdaryPfmTable = _FjdaryPfmTable_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 2, 22, 2)
)
if mibBuilder.loadTexts:
    fjdaryPfmTable.setStatus("current")
_FjdaryPfmEntry_Object = MibTableRow
fjdaryPfmEntry = _FjdaryPfmEntry_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 2, 22, 2, 1)
)
fjdaryPfmEntry.setIndexNames(
    (0, "FJDARY-E150", "fjdaryPfmIndex"),
)
if mibBuilder.loadTexts:
    fjdaryPfmEntry.setStatus("current")


class _FjdaryPfmIndex_Type(Integer32):
    """Custom type fjdaryPfmIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_FjdaryPfmIndex_Type.__name__ = "Integer32"
_FjdaryPfmIndex_Object = MibTableColumn
fjdaryPfmIndex = _FjdaryPfmIndex_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 2, 22, 2, 1, 1),
    _FjdaryPfmIndex_Type()
)
fjdaryPfmIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fjdaryPfmIndex.setStatus("current")


class _FjdaryPfmItemId_Type(Integer32):
    """Custom type fjdaryPfmItemId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_FjdaryPfmItemId_Type.__name__ = "Integer32"
_FjdaryPfmItemId_Object = MibTableColumn
fjdaryPfmItemId = _FjdaryPfmItemId_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 2, 22, 2, 1, 2),
    _FjdaryPfmItemId_Type()
)
fjdaryPfmItemId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fjdaryPfmItemId.setStatus("current")
_FjdaryPfmStatus_Type = FjdaryComponentStatus
_FjdaryPfmStatus_Object = MibTableColumn
fjdaryPfmStatus = _FjdaryPfmStatus_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 2, 22, 2, 1, 3),
    _FjdaryPfmStatus_Type()
)
fjdaryPfmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fjdaryPfmStatus.setStatus("current")
_FjdaryPfmSubStatus_Type = FjdaryComponentStatus
_FjdaryPfmSubStatus_Object = MibTableColumn
fjdaryPfmSubStatus = _FjdaryPfmSubStatus_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 2, 22, 2, 1, 4),
    _FjdaryPfmSubStatus_Type()
)
fjdaryPfmSubStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fjdaryPfmSubStatus.setStatus("current")
_FjdaryLconfig_ObjectIdentity = ObjectIdentity
fjdaryLconfig = _FjdaryLconfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 3)
)
_FjdaryCaPort_ObjectIdentity = ObjectIdentity
fjdaryCaPort = _FjdaryCaPort_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 3, 1)
)


class _FjdaryCaPortCount_Type(Integer32):
    """Custom type fjdaryCaPortCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_FjdaryCaPortCount_Type.__name__ = "Integer32"
_FjdaryCaPortCount_Object = MibScalar
fjdaryCaPortCount = _FjdaryCaPortCount_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 3, 1, 1),
    _FjdaryCaPortCount_Type()
)
fjdaryCaPortCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fjdaryCaPortCount.setStatus("current")
_FjdaryCaPortTable_Object = MibTable
fjdaryCaPortTable = _FjdaryCaPortTable_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 3, 1, 2)
)
if mibBuilder.loadTexts:
    fjdaryCaPortTable.setStatus("current")
_FjdaryCaPortEntry_Object = MibTableRow
fjdaryCaPortEntry = _FjdaryCaPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 3, 1, 2, 1)
)
fjdaryCaPortEntry.setIndexNames(
    (0, "FJDARY-E150", "fjdaryCaPortIndex"),
)
if mibBuilder.loadTexts:
    fjdaryCaPortEntry.setStatus("current")


class _FjdaryCaPortIndex_Type(Integer32):
    """Custom type fjdaryCaPortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_FjdaryCaPortIndex_Type.__name__ = "Integer32"
_FjdaryCaPortIndex_Object = MibTableColumn
fjdaryCaPortIndex = _FjdaryCaPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 3, 1, 2, 1, 1),
    _FjdaryCaPortIndex_Type()
)
fjdaryCaPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fjdaryCaPortIndex.setStatus("current")


class _FjdaryCaPortPortInfo_Type(OctetString):
    """Custom type fjdaryCaPortPortInfo based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_FjdaryCaPortPortInfo_Type.__name__ = "OctetString"
_FjdaryCaPortPortInfo_Object = MibTableColumn
fjdaryCaPortPortInfo = _FjdaryCaPortPortInfo_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 3, 1, 2, 1, 2),
    _FjdaryCaPortPortInfo_Type()
)
fjdaryCaPortPortInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fjdaryCaPortPortInfo.setStatus("current")


class _FjdaryCaPortiscsiInfo_Type(OctetString):
    """Custom type fjdaryCaPortiscsiInfo based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_FjdaryCaPortiscsiInfo_Type.__name__ = "OctetString"
_FjdaryCaPortiscsiInfo_Object = MibTableColumn
fjdaryCaPortiscsiInfo = _FjdaryCaPortiscsiInfo_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 3, 1, 2, 1, 3),
    _FjdaryCaPortiscsiInfo_Type()
)
fjdaryCaPortiscsiInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fjdaryCaPortiscsiInfo.setStatus("current")


class _FjdaryCaPortiscsiName_Type(OctetString):
    """Custom type fjdaryCaPortiscsiName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_FjdaryCaPortiscsiName_Type.__name__ = "OctetString"
_FjdaryCaPortiscsiName_Object = MibTableColumn
fjdaryCaPortiscsiName = _FjdaryCaPortiscsiName_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 3, 1, 2, 1, 4),
    _FjdaryCaPortiscsiName_Type()
)
fjdaryCaPortiscsiName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fjdaryCaPortiscsiName.setStatus("current")


class _FjdaryCaPortiscsiAliasName_Type(OctetString):
    """Custom type fjdaryCaPortiscsiAliasName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_FjdaryCaPortiscsiAliasName_Type.__name__ = "OctetString"
_FjdaryCaPortiscsiAliasName_Object = MibTableColumn
fjdaryCaPortiscsiAliasName = _FjdaryCaPortiscsiAliasName_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 3, 1, 2, 1, 5),
    _FjdaryCaPortiscsiAliasName_Type()
)
fjdaryCaPortiscsiAliasName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fjdaryCaPortiscsiAliasName.setStatus("current")
_FjdaryCaPortiscsiIpAddress_Type = IpAddress
_FjdaryCaPortiscsiIpAddress_Object = MibTableColumn
fjdaryCaPortiscsiIpAddress = _FjdaryCaPortiscsiIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 3, 1, 2, 1, 6),
    _FjdaryCaPortiscsiIpAddress_Type()
)
fjdaryCaPortiscsiIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fjdaryCaPortiscsiIpAddress.setStatus("current")
_FjdaryCaPortiscsiSubnetMask_Type = IpAddress
_FjdaryCaPortiscsiSubnetMask_Object = MibTableColumn
fjdaryCaPortiscsiSubnetMask = _FjdaryCaPortiscsiSubnetMask_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 3, 1, 2, 1, 7),
    _FjdaryCaPortiscsiSubnetMask_Type()
)
fjdaryCaPortiscsiSubnetMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fjdaryCaPortiscsiSubnetMask.setStatus("current")
_FjdaryCaPortiscsiIsnsServer_Type = IpAddress
_FjdaryCaPortiscsiIsnsServer_Object = MibTableColumn
fjdaryCaPortiscsiIsnsServer = _FjdaryCaPortiscsiIsnsServer_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 3, 1, 2, 1, 8),
    _FjdaryCaPortiscsiIsnsServer_Type()
)
fjdaryCaPortiscsiIsnsServer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fjdaryCaPortiscsiIsnsServer.setStatus("current")


class _FjdaryCaPortMode_Type(Integer32):
    """Custom type fjdaryCaPortMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(11,
              12,
              13,
              20)
        )
    )
    namedValues = NamedValues(
        *(("ca", 11),
          ("cara", 13),
          ("initiator", 20),
          ("ra", 12))
    )


_FjdaryCaPortMode_Type.__name__ = "Integer32"
_FjdaryCaPortMode_Object = MibTableColumn
fjdaryCaPortMode = _FjdaryCaPortMode_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 3, 1, 2, 1, 9),
    _FjdaryCaPortMode_Type()
)
fjdaryCaPortMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fjdaryCaPortMode.setStatus("current")
_FjdaryOlu_ObjectIdentity = ObjectIdentity
fjdaryOlu = _FjdaryOlu_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 3, 2)
)


class _FjdaryOluCount_Type(Integer32):
    """Custom type fjdaryOluCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_FjdaryOluCount_Type.__name__ = "Integer32"
_FjdaryOluCount_Object = MibScalar
fjdaryOluCount = _FjdaryOluCount_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 3, 2, 1),
    _FjdaryOluCount_Type()
)
fjdaryOluCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fjdaryOluCount.setStatus("current")
_FjdaryOluTable_Object = MibTable
fjdaryOluTable = _FjdaryOluTable_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 3, 2, 2)
)
if mibBuilder.loadTexts:
    fjdaryOluTable.setStatus("current")
_FjdaryOluEntry_Object = MibTableRow
fjdaryOluEntry = _FjdaryOluEntry_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 3, 2, 2, 1)
)
fjdaryOluEntry.setIndexNames(
    (0, "FJDARY-E150", "fjdaryOluIndex"),
)
if mibBuilder.loadTexts:
    fjdaryOluEntry.setStatus("current")


class _FjdaryOluIndex_Type(Integer32):
    """Custom type fjdaryOluIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_FjdaryOluIndex_Type.__name__ = "Integer32"
_FjdaryOluIndex_Object = MibTableColumn
fjdaryOluIndex = _FjdaryOluIndex_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 3, 2, 2, 1, 1),
    _FjdaryOluIndex_Type()
)
fjdaryOluIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fjdaryOluIndex.setStatus("current")


class _FjdaryOluInfoTable_Type(OctetString):
    """Custom type fjdaryOluInfoTable based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_FjdaryOluInfoTable_Type.__name__ = "OctetString"
_FjdaryOluInfoTable_Object = MibTableColumn
fjdaryOluInfoTable = _FjdaryOluInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 3, 2, 2, 1, 2),
    _FjdaryOluInfoTable_Type()
)
fjdaryOluInfoTable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fjdaryOluInfoTable.setStatus("current")
_FjdarySlu_ObjectIdentity = ObjectIdentity
fjdarySlu = _FjdarySlu_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 3, 3)
)


class _FjdarySluCount_Type(Integer32):
    """Custom type fjdarySluCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_FjdarySluCount_Type.__name__ = "Integer32"
_FjdarySluCount_Object = MibScalar
fjdarySluCount = _FjdarySluCount_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 3, 3, 1),
    _FjdarySluCount_Type()
)
fjdarySluCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fjdarySluCount.setStatus("current")
_FjdarySluTable_Object = MibTable
fjdarySluTable = _FjdarySluTable_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 3, 3, 2)
)
if mibBuilder.loadTexts:
    fjdarySluTable.setStatus("current")
_FjdarySluEntry_Object = MibTableRow
fjdarySluEntry = _FjdarySluEntry_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 3, 3, 2, 1)
)
fjdarySluEntry.setIndexNames(
    (0, "FJDARY-E150", "fjdarySluIndex"),
)
if mibBuilder.loadTexts:
    fjdarySluEntry.setStatus("current")


class _FjdarySluIndex_Type(Integer32):
    """Custom type fjdarySluIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_FjdarySluIndex_Type.__name__ = "Integer32"
_FjdarySluIndex_Object = MibTableColumn
fjdarySluIndex = _FjdarySluIndex_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 3, 3, 2, 1, 1),
    _FjdarySluIndex_Type()
)
fjdarySluIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fjdarySluIndex.setStatus("current")


class _FjdarySluInfoTable_Type(OctetString):
    """Custom type fjdarySluInfoTable based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_FjdarySluInfoTable_Type.__name__ = "OctetString"
_FjdarySluInfoTable_Object = MibTableColumn
fjdarySluInfoTable = _FjdarySluInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 3, 3, 2, 1, 2),
    _FjdarySluInfoTable_Type()
)
fjdarySluInfoTable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fjdarySluInfoTable.setStatus("current")
_FjdaryRlu_ObjectIdentity = ObjectIdentity
fjdaryRlu = _FjdaryRlu_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 3, 4)
)


class _FjdaryRluCount_Type(Integer32):
    """Custom type fjdaryRluCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_FjdaryRluCount_Type.__name__ = "Integer32"
_FjdaryRluCount_Object = MibScalar
fjdaryRluCount = _FjdaryRluCount_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 3, 4, 1),
    _FjdaryRluCount_Type()
)
fjdaryRluCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fjdaryRluCount.setStatus("current")
_FjdaryRluTable_Object = MibTable
fjdaryRluTable = _FjdaryRluTable_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 3, 4, 2)
)
if mibBuilder.loadTexts:
    fjdaryRluTable.setStatus("current")
_FjdaryRluEntry_Object = MibTableRow
fjdaryRluEntry = _FjdaryRluEntry_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 3, 4, 2, 1)
)
fjdaryRluEntry.setIndexNames(
    (0, "FJDARY-E150", "fjdaryRluIndex"),
)
if mibBuilder.loadTexts:
    fjdaryRluEntry.setStatus("current")


class _FjdaryRluIndex_Type(Integer32):
    """Custom type fjdaryRluIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_FjdaryRluIndex_Type.__name__ = "Integer32"
_FjdaryRluIndex_Object = MibTableColumn
fjdaryRluIndex = _FjdaryRluIndex_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 3, 4, 2, 1, 1),
    _FjdaryRluIndex_Type()
)
fjdaryRluIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fjdaryRluIndex.setStatus("current")


class _FjdaryRluInfoTable0_Type(OctetString):
    """Custom type fjdaryRluInfoTable0 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_FjdaryRluInfoTable0_Type.__name__ = "OctetString"
_FjdaryRluInfoTable0_Object = MibTableColumn
fjdaryRluInfoTable0 = _FjdaryRluInfoTable0_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 3, 4, 2, 1, 2),
    _FjdaryRluInfoTable0_Type()
)
fjdaryRluInfoTable0.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fjdaryRluInfoTable0.setStatus("current")


class _FjdaryRluInfoTable1_Type(OctetString):
    """Custom type fjdaryRluInfoTable1 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_FjdaryRluInfoTable1_Type.__name__ = "OctetString"
_FjdaryRluInfoTable1_Object = MibTableColumn
fjdaryRluInfoTable1 = _FjdaryRluInfoTable1_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 3, 4, 2, 1, 3),
    _FjdaryRluInfoTable1_Type()
)
fjdaryRluInfoTable1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fjdaryRluInfoTable1.setStatus("current")


class _FjdaryRluInfoTable2_Type(OctetString):
    """Custom type fjdaryRluInfoTable2 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_FjdaryRluInfoTable2_Type.__name__ = "OctetString"
_FjdaryRluInfoTable2_Object = MibTableColumn
fjdaryRluInfoTable2 = _FjdaryRluInfoTable2_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 3, 4, 2, 1, 4),
    _FjdaryRluInfoTable2_Type()
)
fjdaryRluInfoTable2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fjdaryRluInfoTable2.setStatus("current")


class _FjdaryRluInfoTable3_Type(OctetString):
    """Custom type fjdaryRluInfoTable3 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_FjdaryRluInfoTable3_Type.__name__ = "OctetString"
_FjdaryRluInfoTable3_Object = MibTableColumn
fjdaryRluInfoTable3 = _FjdaryRluInfoTable3_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 3, 4, 2, 1, 5),
    _FjdaryRluInfoTable3_Type()
)
fjdaryRluInfoTable3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fjdaryRluInfoTable3.setStatus("current")
_FjdaryDlu_ObjectIdentity = ObjectIdentity
fjdaryDlu = _FjdaryDlu_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 3, 5)
)


class _FjdaryDluCount_Type(Integer32):
    """Custom type fjdaryDluCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_FjdaryDluCount_Type.__name__ = "Integer32"
_FjdaryDluCount_Object = MibScalar
fjdaryDluCount = _FjdaryDluCount_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 3, 5, 1),
    _FjdaryDluCount_Type()
)
fjdaryDluCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fjdaryDluCount.setStatus("current")
_FjdaryDluTable_Object = MibTable
fjdaryDluTable = _FjdaryDluTable_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 3, 5, 2)
)
if mibBuilder.loadTexts:
    fjdaryDluTable.setStatus("current")
_FjdaryDluEntry_Object = MibTableRow
fjdaryDluEntry = _FjdaryDluEntry_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 3, 5, 2, 1)
)
fjdaryDluEntry.setIndexNames(
    (0, "FJDARY-E150", "fjdaryDluIndex"),
)
if mibBuilder.loadTexts:
    fjdaryDluEntry.setStatus("current")


class _FjdaryDluIndex_Type(Integer32):
    """Custom type fjdaryDluIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_FjdaryDluIndex_Type.__name__ = "Integer32"
_FjdaryDluIndex_Object = MibTableColumn
fjdaryDluIndex = _FjdaryDluIndex_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 3, 5, 2, 1, 1),
    _FjdaryDluIndex_Type()
)
fjdaryDluIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fjdaryDluIndex.setStatus("current")


class _FjdaryDluInfoTable_Type(OctetString):
    """Custom type fjdaryDluInfoTable based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_FjdaryDluInfoTable_Type.__name__ = "OctetString"
_FjdaryDluInfoTable_Object = MibTableColumn
fjdaryDluInfoTable = _FjdaryDluInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 3, 5, 2, 1, 2),
    _FjdaryDluInfoTable_Type()
)
fjdaryDluInfoTable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fjdaryDluInfoTable.setStatus("current")
_FjdaryMlu_ObjectIdentity = ObjectIdentity
fjdaryMlu = _FjdaryMlu_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 3, 6)
)


class _FjdaryMluCount_Type(Integer32):
    """Custom type fjdaryMluCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_FjdaryMluCount_Type.__name__ = "Integer32"
_FjdaryMluCount_Object = MibScalar
fjdaryMluCount = _FjdaryMluCount_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 3, 6, 1),
    _FjdaryMluCount_Type()
)
fjdaryMluCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fjdaryMluCount.setStatus("current")
_FjdaryMluTable_Object = MibTable
fjdaryMluTable = _FjdaryMluTable_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 3, 6, 2)
)
if mibBuilder.loadTexts:
    fjdaryMluTable.setStatus("current")
_FjdaryMluEntry_Object = MibTableRow
fjdaryMluEntry = _FjdaryMluEntry_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 3, 6, 2, 1)
)
fjdaryMluEntry.setIndexNames(
    (0, "FJDARY-E150", "fjdaryMluIndex"),
)
if mibBuilder.loadTexts:
    fjdaryMluEntry.setStatus("current")


class _FjdaryMluIndex_Type(Integer32):
    """Custom type fjdaryMluIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_FjdaryMluIndex_Type.__name__ = "Integer32"
_FjdaryMluIndex_Object = MibTableColumn
fjdaryMluIndex = _FjdaryMluIndex_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 3, 6, 2, 1, 1),
    _FjdaryMluIndex_Type()
)
fjdaryMluIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fjdaryMluIndex.setStatus("current")


class _FjdaryMluInfoTable_Type(OctetString):
    """Custom type fjdaryMluInfoTable based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_FjdaryMluInfoTable_Type.__name__ = "OctetString"
_FjdaryMluInfoTable_Object = MibTableColumn
fjdaryMluInfoTable = _FjdaryMluInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 3, 6, 2, 1, 2),
    _FjdaryMluInfoTable_Type()
)
fjdaryMluInfoTable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fjdaryMluInfoTable.setStatus("current")
_FjdaryOpenmap_ObjectIdentity = ObjectIdentity
fjdaryOpenmap = _FjdaryOpenmap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 3, 7)
)


class _FjdaryOpenmapCount_Type(Integer32):
    """Custom type fjdaryOpenmapCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_FjdaryOpenmapCount_Type.__name__ = "Integer32"
_FjdaryOpenmapCount_Object = MibScalar
fjdaryOpenmapCount = _FjdaryOpenmapCount_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 3, 7, 1),
    _FjdaryOpenmapCount_Type()
)
fjdaryOpenmapCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fjdaryOpenmapCount.setStatus("current")
_FjdaryOpenmapTable_Object = MibTable
fjdaryOpenmapTable = _FjdaryOpenmapTable_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 3, 7, 2)
)
if mibBuilder.loadTexts:
    fjdaryOpenmapTable.setStatus("current")
_FjdaryOpenmapEntry_Object = MibTableRow
fjdaryOpenmapEntry = _FjdaryOpenmapEntry_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 3, 7, 2, 1)
)
fjdaryOpenmapEntry.setIndexNames(
    (0, "FJDARY-E150", "fjdaryOpenmapIndex"),
)
if mibBuilder.loadTexts:
    fjdaryOpenmapEntry.setStatus("current")


class _FjdaryOpenmapIndex_Type(Integer32):
    """Custom type fjdaryOpenmapIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_FjdaryOpenmapIndex_Type.__name__ = "Integer32"
_FjdaryOpenmapIndex_Object = MibTableColumn
fjdaryOpenmapIndex = _FjdaryOpenmapIndex_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 3, 7, 2, 1, 1),
    _FjdaryOpenmapIndex_Type()
)
fjdaryOpenmapIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fjdaryOpenmapIndex.setStatus("current")


class _FjdaryOpenmapInfo_Type(OctetString):
    """Custom type fjdaryOpenmapInfo based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_FjdaryOpenmapInfo_Type.__name__ = "OctetString"
_FjdaryOpenmapInfo_Object = MibTableColumn
fjdaryOpenmapInfo = _FjdaryOpenmapInfo_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 3, 7, 2, 1, 2),
    _FjdaryOpenmapInfo_Type()
)
fjdaryOpenmapInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fjdaryOpenmapInfo.setStatus("current")


class _FjdaryOpenmapHostTable0_Type(OctetString):
    """Custom type fjdaryOpenmapHostTable0 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_FjdaryOpenmapHostTable0_Type.__name__ = "OctetString"
_FjdaryOpenmapHostTable0_Object = MibTableColumn
fjdaryOpenmapHostTable0 = _FjdaryOpenmapHostTable0_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 3, 7, 2, 1, 3),
    _FjdaryOpenmapHostTable0_Type()
)
fjdaryOpenmapHostTable0.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fjdaryOpenmapHostTable0.setStatus("current")


class _FjdaryOpenmapHostTable1_Type(OctetString):
    """Custom type fjdaryOpenmapHostTable1 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_FjdaryOpenmapHostTable1_Type.__name__ = "OctetString"
_FjdaryOpenmapHostTable1_Object = MibTableColumn
fjdaryOpenmapHostTable1 = _FjdaryOpenmapHostTable1_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 3, 7, 2, 1, 4),
    _FjdaryOpenmapHostTable1_Type()
)
fjdaryOpenmapHostTable1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fjdaryOpenmapHostTable1.setStatus("current")


class _FjdaryOpenmapHostTable2_Type(OctetString):
    """Custom type fjdaryOpenmapHostTable2 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_FjdaryOpenmapHostTable2_Type.__name__ = "OctetString"
_FjdaryOpenmapHostTable2_Object = MibTableColumn
fjdaryOpenmapHostTable2 = _FjdaryOpenmapHostTable2_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 3, 7, 2, 1, 5),
    _FjdaryOpenmapHostTable2_Type()
)
fjdaryOpenmapHostTable2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fjdaryOpenmapHostTable2.setStatus("current")


class _FjdaryOpenmapHostTable3_Type(OctetString):
    """Custom type fjdaryOpenmapHostTable3 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_FjdaryOpenmapHostTable3_Type.__name__ = "OctetString"
_FjdaryOpenmapHostTable3_Object = MibTableColumn
fjdaryOpenmapHostTable3 = _FjdaryOpenmapHostTable3_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 3, 7, 2, 1, 6),
    _FjdaryOpenmapHostTable3_Type()
)
fjdaryOpenmapHostTable3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fjdaryOpenmapHostTable3.setStatus("current")


class _FjdaryOpenmapHostTable4_Type(OctetString):
    """Custom type fjdaryOpenmapHostTable4 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_FjdaryOpenmapHostTable4_Type.__name__ = "OctetString"
_FjdaryOpenmapHostTable4_Object = MibTableColumn
fjdaryOpenmapHostTable4 = _FjdaryOpenmapHostTable4_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 3, 7, 2, 1, 7),
    _FjdaryOpenmapHostTable4_Type()
)
fjdaryOpenmapHostTable4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fjdaryOpenmapHostTable4.setStatus("current")


class _FjdaryOpenmapHostTable5_Type(OctetString):
    """Custom type fjdaryOpenmapHostTable5 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_FjdaryOpenmapHostTable5_Type.__name__ = "OctetString"
_FjdaryOpenmapHostTable5_Object = MibTableColumn
fjdaryOpenmapHostTable5 = _FjdaryOpenmapHostTable5_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 3, 7, 2, 1, 8),
    _FjdaryOpenmapHostTable5_Type()
)
fjdaryOpenmapHostTable5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fjdaryOpenmapHostTable5.setStatus("current")


class _FjdaryOpenmapHostTable6_Type(OctetString):
    """Custom type fjdaryOpenmapHostTable6 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_FjdaryOpenmapHostTable6_Type.__name__ = "OctetString"
_FjdaryOpenmapHostTable6_Object = MibTableColumn
fjdaryOpenmapHostTable6 = _FjdaryOpenmapHostTable6_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 3, 7, 2, 1, 9),
    _FjdaryOpenmapHostTable6_Type()
)
fjdaryOpenmapHostTable6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fjdaryOpenmapHostTable6.setStatus("current")


class _FjdaryOpenmapHostTable7_Type(OctetString):
    """Custom type fjdaryOpenmapHostTable7 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_FjdaryOpenmapHostTable7_Type.__name__ = "OctetString"
_FjdaryOpenmapHostTable7_Object = MibTableColumn
fjdaryOpenmapHostTable7 = _FjdaryOpenmapHostTable7_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 3, 7, 2, 1, 10),
    _FjdaryOpenmapHostTable7_Type()
)
fjdaryOpenmapHostTable7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fjdaryOpenmapHostTable7.setStatus("current")
_FjdaryLunmap_ObjectIdentity = ObjectIdentity
fjdaryLunmap = _FjdaryLunmap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 3, 8)
)


class _FjdaryLunmapCount_Type(Integer32):
    """Custom type fjdaryLunmapCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_FjdaryLunmapCount_Type.__name__ = "Integer32"
_FjdaryLunmapCount_Object = MibScalar
fjdaryLunmapCount = _FjdaryLunmapCount_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 3, 8, 1),
    _FjdaryLunmapCount_Type()
)
fjdaryLunmapCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fjdaryLunmapCount.setStatus("current")
_FjdaryLunmapTable_Object = MibTable
fjdaryLunmapTable = _FjdaryLunmapTable_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 3, 8, 2)
)
if mibBuilder.loadTexts:
    fjdaryLunmapTable.setStatus("current")
_FjdaryLunmapEntry_Object = MibTableRow
fjdaryLunmapEntry = _FjdaryLunmapEntry_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 3, 8, 2, 1)
)
fjdaryLunmapEntry.setIndexNames(
    (0, "FJDARY-E150", "fjdaryLunmapIndex"),
)
if mibBuilder.loadTexts:
    fjdaryLunmapEntry.setStatus("current")


class _FjdaryLunmapIndex_Type(Integer32):
    """Custom type fjdaryLunmapIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_FjdaryLunmapIndex_Type.__name__ = "Integer32"
_FjdaryLunmapIndex_Object = MibTableColumn
fjdaryLunmapIndex = _FjdaryLunmapIndex_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 3, 8, 2, 1, 1),
    _FjdaryLunmapIndex_Type()
)
fjdaryLunmapIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fjdaryLunmapIndex.setStatus("current")


class _FjdaryLunmapInfo_Type(OctetString):
    """Custom type fjdaryLunmapInfo based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_FjdaryLunmapInfo_Type.__name__ = "OctetString"
_FjdaryLunmapInfo_Object = MibTableColumn
fjdaryLunmapInfo = _FjdaryLunmapInfo_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 3, 8, 2, 1, 2),
    _FjdaryLunmapInfo_Type()
)
fjdaryLunmapInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fjdaryLunmapInfo.setStatus("current")


class _FjdaryLunmapTable0_Type(OctetString):
    """Custom type fjdaryLunmapTable0 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_FjdaryLunmapTable0_Type.__name__ = "OctetString"
_FjdaryLunmapTable0_Object = MibTableColumn
fjdaryLunmapTable0 = _FjdaryLunmapTable0_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 3, 8, 2, 1, 3),
    _FjdaryLunmapTable0_Type()
)
fjdaryLunmapTable0.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fjdaryLunmapTable0.setStatus("current")


class _FjdaryLunmapTable1_Type(OctetString):
    """Custom type fjdaryLunmapTable1 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_FjdaryLunmapTable1_Type.__name__ = "OctetString"
_FjdaryLunmapTable1_Object = MibTableColumn
fjdaryLunmapTable1 = _FjdaryLunmapTable1_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 3, 8, 2, 1, 4),
    _FjdaryLunmapTable1_Type()
)
fjdaryLunmapTable1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fjdaryLunmapTable1.setStatus("current")


class _FjdaryLunmapTable2_Type(OctetString):
    """Custom type fjdaryLunmapTable2 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_FjdaryLunmapTable2_Type.__name__ = "OctetString"
_FjdaryLunmapTable2_Object = MibTableColumn
fjdaryLunmapTable2 = _FjdaryLunmapTable2_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 3, 8, 2, 1, 5),
    _FjdaryLunmapTable2_Type()
)
fjdaryLunmapTable2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fjdaryLunmapTable2.setStatus("current")


class _FjdaryLunmapTable3_Type(OctetString):
    """Custom type fjdaryLunmapTable3 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_FjdaryLunmapTable3_Type.__name__ = "OctetString"
_FjdaryLunmapTable3_Object = MibTableColumn
fjdaryLunmapTable3 = _FjdaryLunmapTable3_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 3, 8, 2, 1, 6),
    _FjdaryLunmapTable3_Type()
)
fjdaryLunmapTable3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fjdaryLunmapTable3.setStatus("current")
_FjdaryAffinityGrp_ObjectIdentity = ObjectIdentity
fjdaryAffinityGrp = _FjdaryAffinityGrp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 3, 9)
)


class _FjdaryAffinityGrpCount_Type(Integer32):
    """Custom type fjdaryAffinityGrpCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_FjdaryAffinityGrpCount_Type.__name__ = "Integer32"
_FjdaryAffinityGrpCount_Object = MibScalar
fjdaryAffinityGrpCount = _FjdaryAffinityGrpCount_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 3, 9, 1),
    _FjdaryAffinityGrpCount_Type()
)
fjdaryAffinityGrpCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fjdaryAffinityGrpCount.setStatus("current")
_FjdaryAffinityGrpTable_Object = MibTable
fjdaryAffinityGrpTable = _FjdaryAffinityGrpTable_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 3, 9, 2)
)
if mibBuilder.loadTexts:
    fjdaryAffinityGrpTable.setStatus("current")
_FjdaryAffinityGrpEntry_Object = MibTableRow
fjdaryAffinityGrpEntry = _FjdaryAffinityGrpEntry_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 3, 9, 2, 1)
)
fjdaryAffinityGrpEntry.setIndexNames(
    (0, "FJDARY-E150", "fjdaryAffinityGrpIndex"),
)
if mibBuilder.loadTexts:
    fjdaryAffinityGrpEntry.setStatus("current")


class _FjdaryAffinityGrpIndex_Type(Integer32):
    """Custom type fjdaryAffinityGrpIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_FjdaryAffinityGrpIndex_Type.__name__ = "Integer32"
_FjdaryAffinityGrpIndex_Object = MibTableColumn
fjdaryAffinityGrpIndex = _FjdaryAffinityGrpIndex_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 3, 9, 2, 1, 1),
    _FjdaryAffinityGrpIndex_Type()
)
fjdaryAffinityGrpIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fjdaryAffinityGrpIndex.setStatus("current")


class _FjdaryAffinityGrpInfo_Type(OctetString):
    """Custom type fjdaryAffinityGrpInfo based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_FjdaryAffinityGrpInfo_Type.__name__ = "OctetString"
_FjdaryAffinityGrpInfo_Object = MibTableColumn
fjdaryAffinityGrpInfo = _FjdaryAffinityGrpInfo_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 3, 9, 2, 1, 2),
    _FjdaryAffinityGrpInfo_Type()
)
fjdaryAffinityGrpInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fjdaryAffinityGrpInfo.setStatus("current")


class _FjdaryAffinityGrpTable0_Type(OctetString):
    """Custom type fjdaryAffinityGrpTable0 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_FjdaryAffinityGrpTable0_Type.__name__ = "OctetString"
_FjdaryAffinityGrpTable0_Object = MibTableColumn
fjdaryAffinityGrpTable0 = _FjdaryAffinityGrpTable0_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 3, 9, 2, 1, 3),
    _FjdaryAffinityGrpTable0_Type()
)
fjdaryAffinityGrpTable0.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fjdaryAffinityGrpTable0.setStatus("current")


class _FjdaryAffinityGrpTable1_Type(OctetString):
    """Custom type fjdaryAffinityGrpTable1 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_FjdaryAffinityGrpTable1_Type.__name__ = "OctetString"
_FjdaryAffinityGrpTable1_Object = MibTableColumn
fjdaryAffinityGrpTable1 = _FjdaryAffinityGrpTable1_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 3, 9, 2, 1, 4),
    _FjdaryAffinityGrpTable1_Type()
)
fjdaryAffinityGrpTable1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fjdaryAffinityGrpTable1.setStatus("current")


class _FjdaryAffinityGrpTable2_Type(OctetString):
    """Custom type fjdaryAffinityGrpTable2 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_FjdaryAffinityGrpTable2_Type.__name__ = "OctetString"
_FjdaryAffinityGrpTable2_Object = MibTableColumn
fjdaryAffinityGrpTable2 = _FjdaryAffinityGrpTable2_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 3, 9, 2, 1, 5),
    _FjdaryAffinityGrpTable2_Type()
)
fjdaryAffinityGrpTable2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fjdaryAffinityGrpTable2.setStatus("current")


class _FjdaryAffinityGrpTable3_Type(OctetString):
    """Custom type fjdaryAffinityGrpTable3 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_FjdaryAffinityGrpTable3_Type.__name__ = "OctetString"
_FjdaryAffinityGrpTable3_Object = MibTableColumn
fjdaryAffinityGrpTable3 = _FjdaryAffinityGrpTable3_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 3, 9, 2, 1, 6),
    _FjdaryAffinityGrpTable3_Type()
)
fjdaryAffinityGrpTable3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fjdaryAffinityGrpTable3.setStatus("current")
_FjdaryHostwwn_ObjectIdentity = ObjectIdentity
fjdaryHostwwn = _FjdaryHostwwn_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 3, 10)
)


class _FjdaryHostwwnCount_Type(Integer32):
    """Custom type fjdaryHostwwnCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_FjdaryHostwwnCount_Type.__name__ = "Integer32"
_FjdaryHostwwnCount_Object = MibScalar
fjdaryHostwwnCount = _FjdaryHostwwnCount_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 3, 10, 1),
    _FjdaryHostwwnCount_Type()
)
fjdaryHostwwnCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fjdaryHostwwnCount.setStatus("current")
_FjdaryHostwwnTable_Object = MibTable
fjdaryHostwwnTable = _FjdaryHostwwnTable_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 3, 10, 2)
)
if mibBuilder.loadTexts:
    fjdaryHostwwnTable.setStatus("current")
_FjdaryHostwwnEntry_Object = MibTableRow
fjdaryHostwwnEntry = _FjdaryHostwwnEntry_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 3, 10, 2, 1)
)
fjdaryHostwwnEntry.setIndexNames(
    (0, "FJDARY-E150", "fjdaryHostwwnIndex"),
)
if mibBuilder.loadTexts:
    fjdaryHostwwnEntry.setStatus("current")


class _FjdaryHostwwnIndex_Type(Integer32):
    """Custom type fjdaryHostwwnIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_FjdaryHostwwnIndex_Type.__name__ = "Integer32"
_FjdaryHostwwnIndex_Object = MibTableColumn
fjdaryHostwwnIndex = _FjdaryHostwwnIndex_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 3, 10, 2, 1, 1),
    _FjdaryHostwwnIndex_Type()
)
fjdaryHostwwnIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fjdaryHostwwnIndex.setStatus("current")


class _FjdaryHostwwnWWN_Type(OctetString):
    """Custom type fjdaryHostwwnWWN based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_FjdaryHostwwnWWN_Type.__name__ = "OctetString"
_FjdaryHostwwnWWN_Object = MibTableColumn
fjdaryHostwwnWWN = _FjdaryHostwwnWWN_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 3, 10, 2, 1, 2),
    _FjdaryHostwwnWWN_Type()
)
fjdaryHostwwnWWN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fjdaryHostwwnWWN.setStatus("current")
_FjdaryResetpath_ObjectIdentity = ObjectIdentity
fjdaryResetpath = _FjdaryResetpath_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 3, 11)
)


class _FjdaryResetpathCount_Type(Integer32):
    """Custom type fjdaryResetpathCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_FjdaryResetpathCount_Type.__name__ = "Integer32"
_FjdaryResetpathCount_Object = MibScalar
fjdaryResetpathCount = _FjdaryResetpathCount_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 3, 11, 1),
    _FjdaryResetpathCount_Type()
)
fjdaryResetpathCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fjdaryResetpathCount.setStatus("current")
_FjdaryResetpathTable_Object = MibTable
fjdaryResetpathTable = _FjdaryResetpathTable_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 3, 11, 2)
)
if mibBuilder.loadTexts:
    fjdaryResetpathTable.setStatus("current")
_FjdaryResetpathEntry_Object = MibTableRow
fjdaryResetpathEntry = _FjdaryResetpathEntry_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 3, 11, 2, 1)
)
fjdaryResetpathEntry.setIndexNames(
    (0, "FJDARY-E150", "fjdaryResetpathIndex"),
)
if mibBuilder.loadTexts:
    fjdaryResetpathEntry.setStatus("current")


class _FjdaryResetpathIndex_Type(Integer32):
    """Custom type fjdaryResetpathIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_FjdaryResetpathIndex_Type.__name__ = "Integer32"
_FjdaryResetpathIndex_Object = MibTableColumn
fjdaryResetpathIndex = _FjdaryResetpathIndex_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 3, 11, 2, 1, 1),
    _FjdaryResetpathIndex_Type()
)
fjdaryResetpathIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fjdaryResetpathIndex.setStatus("current")


class _FjdaryResetpathGroup_Type(OctetString):
    """Custom type fjdaryResetpathGroup based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_FjdaryResetpathGroup_Type.__name__ = "OctetString"
_FjdaryResetpathGroup_Object = MibTableColumn
fjdaryResetpathGroup = _FjdaryResetpathGroup_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 3, 11, 2, 1, 2),
    _FjdaryResetpathGroup_Type()
)
fjdaryResetpathGroup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fjdaryResetpathGroup.setStatus("current")
_FjdaryHostiscsi_ObjectIdentity = ObjectIdentity
fjdaryHostiscsi = _FjdaryHostiscsi_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 3, 12)
)


class _FjdaryHostiscsiCount_Type(Integer32):
    """Custom type fjdaryHostiscsiCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_FjdaryHostiscsiCount_Type.__name__ = "Integer32"
_FjdaryHostiscsiCount_Object = MibScalar
fjdaryHostiscsiCount = _FjdaryHostiscsiCount_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 3, 12, 1),
    _FjdaryHostiscsiCount_Type()
)
fjdaryHostiscsiCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fjdaryHostiscsiCount.setStatus("current")
_FjdaryHostiscsiTable_Object = MibTable
fjdaryHostiscsiTable = _FjdaryHostiscsiTable_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 3, 12, 2)
)
if mibBuilder.loadTexts:
    fjdaryHostiscsiTable.setStatus("current")
_FjdaryHostiscsiEntry_Object = MibTableRow
fjdaryHostiscsiEntry = _FjdaryHostiscsiEntry_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 3, 12, 2, 1)
)
fjdaryHostiscsiEntry.setIndexNames(
    (0, "FJDARY-E150", "fjdaryHostiscsiIndex"),
)
if mibBuilder.loadTexts:
    fjdaryHostiscsiEntry.setStatus("current")


class _FjdaryHostiscsiIndex_Type(Integer32):
    """Custom type fjdaryHostiscsiIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_FjdaryHostiscsiIndex_Type.__name__ = "Integer32"
_FjdaryHostiscsiIndex_Object = MibTableColumn
fjdaryHostiscsiIndex = _FjdaryHostiscsiIndex_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 3, 12, 2, 1, 1),
    _FjdaryHostiscsiIndex_Type()
)
fjdaryHostiscsiIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fjdaryHostiscsiIndex.setStatus("current")


class _FjdaryHostiscsiDefine_Type(OctetString):
    """Custom type fjdaryHostiscsiDefine based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_FjdaryHostiscsiDefine_Type.__name__ = "OctetString"
_FjdaryHostiscsiDefine_Object = MibTableColumn
fjdaryHostiscsiDefine = _FjdaryHostiscsiDefine_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 3, 12, 2, 1, 2),
    _FjdaryHostiscsiDefine_Type()
)
fjdaryHostiscsiDefine.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fjdaryHostiscsiDefine.setStatus("current")


class _FjdaryHostiscsiName_Type(OctetString):
    """Custom type fjdaryHostiscsiName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_FjdaryHostiscsiName_Type.__name__ = "OctetString"
_FjdaryHostiscsiName_Object = MibTableColumn
fjdaryHostiscsiName = _FjdaryHostiscsiName_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 3, 12, 2, 1, 3),
    _FjdaryHostiscsiName_Type()
)
fjdaryHostiscsiName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fjdaryHostiscsiName.setStatus("current")


class _FjdaryHostiscsiAliasName_Type(OctetString):
    """Custom type fjdaryHostiscsiAliasName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_FjdaryHostiscsiAliasName_Type.__name__ = "OctetString"
_FjdaryHostiscsiAliasName_Object = MibTableColumn
fjdaryHostiscsiAliasName = _FjdaryHostiscsiAliasName_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 3, 12, 2, 1, 4),
    _FjdaryHostiscsiAliasName_Type()
)
fjdaryHostiscsiAliasName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fjdaryHostiscsiAliasName.setStatus("current")
_FjdaryHostiscsiIpAddress_Type = IpAddress
_FjdaryHostiscsiIpAddress_Object = MibTableColumn
fjdaryHostiscsiIpAddress = _FjdaryHostiscsiIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 3, 12, 2, 1, 5),
    _FjdaryHostiscsiIpAddress_Type()
)
fjdaryHostiscsiIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fjdaryHostiscsiIpAddress.setStatus("current")
_FjdaryHostResponse_ObjectIdentity = ObjectIdentity
fjdaryHostResponse = _FjdaryHostResponse_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 3, 13)
)


class _FjdaryHostResponseCount_Type(Integer32):
    """Custom type fjdaryHostResponseCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_FjdaryHostResponseCount_Type.__name__ = "Integer32"
_FjdaryHostResponseCount_Object = MibScalar
fjdaryHostResponseCount = _FjdaryHostResponseCount_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 3, 13, 1),
    _FjdaryHostResponseCount_Type()
)
fjdaryHostResponseCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fjdaryHostResponseCount.setStatus("current")
_FjdaryHostResponseTable_Object = MibTable
fjdaryHostResponseTable = _FjdaryHostResponseTable_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 3, 13, 2)
)
if mibBuilder.loadTexts:
    fjdaryHostResponseTable.setStatus("current")
_FjdaryHostResponseEntry_Object = MibTableRow
fjdaryHostResponseEntry = _FjdaryHostResponseEntry_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 3, 13, 2, 1)
)
fjdaryHostResponseEntry.setIndexNames(
    (0, "FJDARY-E150", "fjdaryHostResponseIndex"),
)
if mibBuilder.loadTexts:
    fjdaryHostResponseEntry.setStatus("current")


class _FjdaryHostResponseIndex_Type(Integer32):
    """Custom type fjdaryHostResponseIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_FjdaryHostResponseIndex_Type.__name__ = "Integer32"
_FjdaryHostResponseIndex_Object = MibTableColumn
fjdaryHostResponseIndex = _FjdaryHostResponseIndex_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 3, 13, 2, 1, 1),
    _FjdaryHostResponseIndex_Type()
)
fjdaryHostResponseIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fjdaryHostResponseIndex.setStatus("current")


class _FjdaryHostResponseInfoTable_Type(OctetString):
    """Custom type fjdaryHostResponseInfoTable based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_FjdaryHostResponseInfoTable_Type.__name__ = "OctetString"
_FjdaryHostResponseInfoTable_Object = MibTableColumn
fjdaryHostResponseInfoTable = _FjdaryHostResponseInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 3, 13, 2, 1, 2),
    _FjdaryHostResponseInfoTable_Type()
)
fjdaryHostResponseInfoTable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fjdaryHostResponseInfoTable.setStatus("current")
_FjdaryFirm_ObjectIdentity = ObjectIdentity
fjdaryFirm = _FjdaryFirm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 4)
)


class _FjdaryFirmTotal_Type(OctetString):
    """Custom type fjdaryFirmTotal based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_FjdaryFirmTotal_Type.__name__ = "OctetString"
_FjdaryFirmTotal_Object = MibScalar
fjdaryFirmTotal = _FjdaryFirmTotal_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 4, 1),
    _FjdaryFirmTotal_Type()
)
fjdaryFirmTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fjdaryFirmTotal.setStatus("current")
_FjdaryPerformance_ObjectIdentity = ObjectIdentity
fjdaryPerformance = _FjdaryPerformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 5)
)
_FjdaryPfInfo_ObjectIdentity = ObjectIdentity
fjdaryPfInfo = _FjdaryPfInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 5, 1)
)


class _FjdaryPfInfoVersion_Type(Integer32):
    """Custom type fjdaryPfInfoVersion based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_FjdaryPfInfoVersion_Type.__name__ = "Integer32"
_FjdaryPfInfoVersion_Object = MibScalar
fjdaryPfInfoVersion = _FjdaryPfInfoVersion_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 5, 1, 1),
    _FjdaryPfInfoVersion_Type()
)
fjdaryPfInfoVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fjdaryPfInfoVersion.setStatus("current")


class _FjdaryPfInfoLevel_Type(Integer32):
    """Custom type fjdaryPfInfoLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_FjdaryPfInfoLevel_Type.__name__ = "Integer32"
_FjdaryPfInfoLevel_Object = MibScalar
fjdaryPfInfoLevel = _FjdaryPfInfoLevel_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 5, 1, 2),
    _FjdaryPfInfoLevel_Type()
)
fjdaryPfInfoLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fjdaryPfInfoLevel.setStatus("current")


class _FjdaryPfInfoIntervalTime_Type(Integer32):
    """Custom type fjdaryPfInfoIntervalTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_FjdaryPfInfoIntervalTime_Type.__name__ = "Integer32"
_FjdaryPfInfoIntervalTime_Object = MibScalar
fjdaryPfInfoIntervalTime = _FjdaryPfInfoIntervalTime_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 5, 1, 3),
    _FjdaryPfInfoIntervalTime_Type()
)
fjdaryPfInfoIntervalTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fjdaryPfInfoIntervalTime.setStatus("current")


class _FjdaryPfInfoUpdateTime_Type(Integer32):
    """Custom type fjdaryPfInfoUpdateTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_FjdaryPfInfoUpdateTime_Type.__name__ = "Integer32"
_FjdaryPfInfoUpdateTime_Object = MibScalar
fjdaryPfInfoUpdateTime = _FjdaryPfInfoUpdateTime_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 5, 1, 4),
    _FjdaryPfInfoUpdateTime_Type()
)
fjdaryPfInfoUpdateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fjdaryPfInfoUpdateTime.setStatus("current")


class _FjdaryPfInfoDataValid_Type(Integer32):
    """Custom type fjdaryPfInfoDataValid based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              255)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 255),
          ("valid", 1))
    )


_FjdaryPfInfoDataValid_Type.__name__ = "Integer32"
_FjdaryPfInfoDataValid_Object = MibScalar
fjdaryPfInfoDataValid = _FjdaryPfInfoDataValid_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 5, 1, 5),
    _FjdaryPfInfoDataValid_Type()
)
fjdaryPfInfoDataValid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fjdaryPfInfoDataValid.setStatus("current")
_FjdaryPfOlu_ObjectIdentity = ObjectIdentity
fjdaryPfOlu = _FjdaryPfOlu_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 5, 2)
)


class _FjdaryPfOluCount_Type(Integer32):
    """Custom type fjdaryPfOluCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_FjdaryPfOluCount_Type.__name__ = "Integer32"
_FjdaryPfOluCount_Object = MibScalar
fjdaryPfOluCount = _FjdaryPfOluCount_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 5, 2, 1),
    _FjdaryPfOluCount_Type()
)
fjdaryPfOluCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fjdaryPfOluCount.setStatus("current")
_FjdaryPfOluTable_Object = MibTable
fjdaryPfOluTable = _FjdaryPfOluTable_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 5, 2, 2)
)
if mibBuilder.loadTexts:
    fjdaryPfOluTable.setStatus("current")
_FjdaryPfOluEntry_Object = MibTableRow
fjdaryPfOluEntry = _FjdaryPfOluEntry_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 5, 2, 2, 1)
)
fjdaryPfOluEntry.setIndexNames(
    (0, "FJDARY-E150", "fjdaryPfOluIndex"),
)
if mibBuilder.loadTexts:
    fjdaryPfOluEntry.setStatus("current")


class _FjdaryPfOluIndex_Type(Integer32):
    """Custom type fjdaryPfOluIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_FjdaryPfOluIndex_Type.__name__ = "Integer32"
_FjdaryPfOluIndex_Object = MibTableColumn
fjdaryPfOluIndex = _FjdaryPfOluIndex_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 5, 2, 2, 1, 1),
    _FjdaryPfOluIndex_Type()
)
fjdaryPfOluIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fjdaryPfOluIndex.setStatus("current")


class _FjdaryPfOluRdIOPS_Type(Integer32):
    """Custom type fjdaryPfOluRdIOPS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_FjdaryPfOluRdIOPS_Type.__name__ = "Integer32"
_FjdaryPfOluRdIOPS_Object = MibTableColumn
fjdaryPfOluRdIOPS = _FjdaryPfOluRdIOPS_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 5, 2, 2, 1, 2),
    _FjdaryPfOluRdIOPS_Type()
)
fjdaryPfOluRdIOPS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fjdaryPfOluRdIOPS.setStatus("current")


class _FjdaryPfOluWtIOPS_Type(Integer32):
    """Custom type fjdaryPfOluWtIOPS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_FjdaryPfOluWtIOPS_Type.__name__ = "Integer32"
_FjdaryPfOluWtIOPS_Object = MibTableColumn
fjdaryPfOluWtIOPS = _FjdaryPfOluWtIOPS_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 5, 2, 2, 1, 3),
    _FjdaryPfOluWtIOPS_Type()
)
fjdaryPfOluWtIOPS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fjdaryPfOluWtIOPS.setStatus("current")


class _FjdaryPfOluAdCpRdIOPS_Type(Integer32):
    """Custom type fjdaryPfOluAdCpRdIOPS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_FjdaryPfOluAdCpRdIOPS_Type.__name__ = "Integer32"
_FjdaryPfOluAdCpRdIOPS_Object = MibTableColumn
fjdaryPfOluAdCpRdIOPS = _FjdaryPfOluAdCpRdIOPS_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 5, 2, 2, 1, 4),
    _FjdaryPfOluAdCpRdIOPS_Type()
)
fjdaryPfOluAdCpRdIOPS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fjdaryPfOluAdCpRdIOPS.setStatus("current")


class _FjdaryPfOluAdCpWtIOPS_Type(Integer32):
    """Custom type fjdaryPfOluAdCpWtIOPS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_FjdaryPfOluAdCpWtIOPS_Type.__name__ = "Integer32"
_FjdaryPfOluAdCpWtIOPS_Object = MibTableColumn
fjdaryPfOluAdCpWtIOPS = _FjdaryPfOluAdCpWtIOPS_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 5, 2, 2, 1, 5),
    _FjdaryPfOluAdCpWtIOPS_Type()
)
fjdaryPfOluAdCpWtIOPS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fjdaryPfOluAdCpWtIOPS.setStatus("current")


class _FjdaryPfOluRdTp_Type(Integer32):
    """Custom type fjdaryPfOluRdTp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_FjdaryPfOluRdTp_Type.__name__ = "Integer32"
_FjdaryPfOluRdTp_Object = MibTableColumn
fjdaryPfOluRdTp = _FjdaryPfOluRdTp_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 5, 2, 2, 1, 6),
    _FjdaryPfOluRdTp_Type()
)
fjdaryPfOluRdTp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fjdaryPfOluRdTp.setStatus("current")


class _FjdaryPfOluWtTp_Type(Integer32):
    """Custom type fjdaryPfOluWtTp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_FjdaryPfOluWtTp_Type.__name__ = "Integer32"
_FjdaryPfOluWtTp_Object = MibTableColumn
fjdaryPfOluWtTp = _FjdaryPfOluWtTp_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 5, 2, 2, 1, 7),
    _FjdaryPfOluWtTp_Type()
)
fjdaryPfOluWtTp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fjdaryPfOluWtTp.setStatus("current")


class _FjdaryPfOluAdCpRdTp_Type(Integer32):
    """Custom type fjdaryPfOluAdCpRdTp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_FjdaryPfOluAdCpRdTp_Type.__name__ = "Integer32"
_FjdaryPfOluAdCpRdTp_Object = MibTableColumn
fjdaryPfOluAdCpRdTp = _FjdaryPfOluAdCpRdTp_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 5, 2, 2, 1, 8),
    _FjdaryPfOluAdCpRdTp_Type()
)
fjdaryPfOluAdCpRdTp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fjdaryPfOluAdCpRdTp.setStatus("current")


class _FjdaryPfOluAdCpWtTp_Type(Integer32):
    """Custom type fjdaryPfOluAdCpWtTp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_FjdaryPfOluAdCpWtTp_Type.__name__ = "Integer32"
_FjdaryPfOluAdCpWtTp_Object = MibTableColumn
fjdaryPfOluAdCpWtTp = _FjdaryPfOluAdCpWtTp_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 5, 2, 2, 1, 9),
    _FjdaryPfOluAdCpWtTp_Type()
)
fjdaryPfOluAdCpWtTp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fjdaryPfOluAdCpWtTp.setStatus("current")


class _FjdaryPfOluRdRspTime_Type(Integer32):
    """Custom type fjdaryPfOluRdRspTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_FjdaryPfOluRdRspTime_Type.__name__ = "Integer32"
_FjdaryPfOluRdRspTime_Object = MibTableColumn
fjdaryPfOluRdRspTime = _FjdaryPfOluRdRspTime_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 5, 2, 2, 1, 10),
    _FjdaryPfOluRdRspTime_Type()
)
fjdaryPfOluRdRspTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fjdaryPfOluRdRspTime.setStatus("current")


class _FjdaryPfOluWtRspTime_Type(Integer32):
    """Custom type fjdaryPfOluWtRspTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_FjdaryPfOluWtRspTime_Type.__name__ = "Integer32"
_FjdaryPfOluWtRspTime_Object = MibTableColumn
fjdaryPfOluWtRspTime = _FjdaryPfOluWtRspTime_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 5, 2, 2, 1, 11),
    _FjdaryPfOluWtRspTime_Type()
)
fjdaryPfOluWtRspTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fjdaryPfOluWtRspTime.setStatus("current")


class _FjdaryPfOluRdCacheHit_Type(Integer32):
    """Custom type fjdaryPfOluRdCacheHit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_FjdaryPfOluRdCacheHit_Type.__name__ = "Integer32"
_FjdaryPfOluRdCacheHit_Object = MibTableColumn
fjdaryPfOluRdCacheHit = _FjdaryPfOluRdCacheHit_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 5, 2, 2, 1, 12),
    _FjdaryPfOluRdCacheHit_Type()
)
fjdaryPfOluRdCacheHit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fjdaryPfOluRdCacheHit.setStatus("current")


class _FjdaryPfOluWtCacheHit_Type(Integer32):
    """Custom type fjdaryPfOluWtCacheHit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_FjdaryPfOluWtCacheHit_Type.__name__ = "Integer32"
_FjdaryPfOluWtCacheHit_Object = MibTableColumn
fjdaryPfOluWtCacheHit = _FjdaryPfOluWtCacheHit_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 5, 2, 2, 1, 13),
    _FjdaryPfOluWtCacheHit_Type()
)
fjdaryPfOluWtCacheHit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fjdaryPfOluWtCacheHit.setStatus("current")


class _FjdaryPfOluAdRdCacheHit_Type(Integer32):
    """Custom type fjdaryPfOluAdRdCacheHit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_FjdaryPfOluAdRdCacheHit_Type.__name__ = "Integer32"
_FjdaryPfOluAdRdCacheHit_Object = MibTableColumn
fjdaryPfOluAdRdCacheHit = _FjdaryPfOluAdRdCacheHit_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 5, 2, 2, 1, 14),
    _FjdaryPfOluAdRdCacheHit_Type()
)
fjdaryPfOluAdRdCacheHit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fjdaryPfOluAdRdCacheHit.setStatus("current")


class _FjdaryPfOluAdWtCacheHit_Type(Integer32):
    """Custom type fjdaryPfOluAdWtCacheHit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_FjdaryPfOluAdWtCacheHit_Type.__name__ = "Integer32"
_FjdaryPfOluAdWtCacheHit_Object = MibTableColumn
fjdaryPfOluAdWtCacheHit = _FjdaryPfOluAdWtCacheHit_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 5, 2, 2, 1, 15),
    _FjdaryPfOluAdWtCacheHit_Type()
)
fjdaryPfOluAdWtCacheHit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fjdaryPfOluAdWtCacheHit.setStatus("current")


class _FjdaryPfOluRdPreFetchHit_Type(Integer32):
    """Custom type fjdaryPfOluRdPreFetchHit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_FjdaryPfOluRdPreFetchHit_Type.__name__ = "Integer32"
_FjdaryPfOluRdPreFetchHit_Object = MibTableColumn
fjdaryPfOluRdPreFetchHit = _FjdaryPfOluRdPreFetchHit_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 5, 2, 2, 1, 16),
    _FjdaryPfOluRdPreFetchHit_Type()
)
fjdaryPfOluRdPreFetchHit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fjdaryPfOluRdPreFetchHit.setStatus("current")


class _FjdaryPfOluAdRdPreFetchHit_Type(Integer32):
    """Custom type fjdaryPfOluAdRdPreFetchHit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_FjdaryPfOluAdRdPreFetchHit_Type.__name__ = "Integer32"
_FjdaryPfOluAdRdPreFetchHit_Object = MibTableColumn
fjdaryPfOluAdRdPreFetchHit = _FjdaryPfOluAdRdPreFetchHit_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 5, 2, 2, 1, 17),
    _FjdaryPfOluAdRdPreFetchHit_Type()
)
fjdaryPfOluAdRdPreFetchHit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fjdaryPfOluAdRdPreFetchHit.setStatus("current")


class _FjdaryPfOluRdExcCacheHit_Type(Integer32):
    """Custom type fjdaryPfOluRdExcCacheHit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_FjdaryPfOluRdExcCacheHit_Type.__name__ = "Integer32"
_FjdaryPfOluRdExcCacheHit_Object = MibTableColumn
fjdaryPfOluRdExcCacheHit = _FjdaryPfOluRdExcCacheHit_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 5, 2, 2, 1, 18),
    _FjdaryPfOluRdExcCacheHit_Type()
)
fjdaryPfOluRdExcCacheHit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fjdaryPfOluRdExcCacheHit.setStatus("current")


class _FjdaryPfOluAdRdExcCacheHit_Type(Integer32):
    """Custom type fjdaryPfOluAdRdExcCacheHit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_FjdaryPfOluAdRdExcCacheHit_Type.__name__ = "Integer32"
_FjdaryPfOluAdRdExcCacheHit_Object = MibTableColumn
fjdaryPfOluAdRdExcCacheHit = _FjdaryPfOluAdRdExcCacheHit_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 5, 2, 2, 1, 19),
    _FjdaryPfOluAdRdExcCacheHit_Type()
)
fjdaryPfOluAdRdExcCacheHit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fjdaryPfOluAdRdExcCacheHit.setStatus("current")
_FjdaryPfDisk_ObjectIdentity = ObjectIdentity
fjdaryPfDisk = _FjdaryPfDisk_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 5, 3)
)


class _FjdaryPfDiskCount_Type(Integer32):
    """Custom type fjdaryPfDiskCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_FjdaryPfDiskCount_Type.__name__ = "Integer32"
_FjdaryPfDiskCount_Object = MibScalar
fjdaryPfDiskCount = _FjdaryPfDiskCount_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 5, 3, 1),
    _FjdaryPfDiskCount_Type()
)
fjdaryPfDiskCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fjdaryPfDiskCount.setStatus("current")
_FjdaryPfDiskTable_Object = MibTable
fjdaryPfDiskTable = _FjdaryPfDiskTable_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 5, 3, 2)
)
if mibBuilder.loadTexts:
    fjdaryPfDiskTable.setStatus("current")
_FjdaryPfDiskEntry_Object = MibTableRow
fjdaryPfDiskEntry = _FjdaryPfDiskEntry_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 5, 3, 2, 1)
)
fjdaryPfDiskEntry.setIndexNames(
    (0, "FJDARY-E150", "fjdaryPfDiskIndex"),
)
if mibBuilder.loadTexts:
    fjdaryPfDiskEntry.setStatus("current")


class _FjdaryPfDiskIndex_Type(Integer32):
    """Custom type fjdaryPfDiskIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_FjdaryPfDiskIndex_Type.__name__ = "Integer32"
_FjdaryPfDiskIndex_Object = MibTableColumn
fjdaryPfDiskIndex = _FjdaryPfDiskIndex_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 5, 3, 2, 1, 1),
    _FjdaryPfDiskIndex_Type()
)
fjdaryPfDiskIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fjdaryPfDiskIndex.setStatus("current")


class _FjdaryPfDiskPlun_Type(Integer32):
    """Custom type fjdaryPfDiskPlun based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_FjdaryPfDiskPlun_Type.__name__ = "Integer32"
_FjdaryPfDiskPlun_Object = MibTableColumn
fjdaryPfDiskPlun = _FjdaryPfDiskPlun_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 5, 3, 2, 1, 2),
    _FjdaryPfDiskPlun_Type()
)
fjdaryPfDiskPlun.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fjdaryPfDiskPlun.setStatus("current")


class _FjdaryPfDiskBusy_Type(Integer32):
    """Custom type fjdaryPfDiskBusy based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_FjdaryPfDiskBusy_Type.__name__ = "Integer32"
_FjdaryPfDiskBusy_Object = MibTableColumn
fjdaryPfDiskBusy = _FjdaryPfDiskBusy_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 5, 3, 2, 1, 3),
    _FjdaryPfDiskBusy_Type()
)
fjdaryPfDiskBusy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fjdaryPfDiskBusy.setStatus("current")
_FjdaryPfCm_ObjectIdentity = ObjectIdentity
fjdaryPfCm = _FjdaryPfCm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 5, 4)
)


class _FjdaryPfCmCount_Type(Integer32):
    """Custom type fjdaryPfCmCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_FjdaryPfCmCount_Type.__name__ = "Integer32"
_FjdaryPfCmCount_Object = MibScalar
fjdaryPfCmCount = _FjdaryPfCmCount_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 5, 4, 1),
    _FjdaryPfCmCount_Type()
)
fjdaryPfCmCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fjdaryPfCmCount.setStatus("current")
_FjdaryPfCmTable_Object = MibTable
fjdaryPfCmTable = _FjdaryPfCmTable_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 5, 4, 2)
)
if mibBuilder.loadTexts:
    fjdaryPfCmTable.setStatus("current")
_FjdaryPfCmEntry_Object = MibTableRow
fjdaryPfCmEntry = _FjdaryPfCmEntry_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 5, 4, 2, 1)
)
fjdaryPfCmEntry.setIndexNames(
    (0, "FJDARY-E150", "fjdaryPfCmIndex"),
)
if mibBuilder.loadTexts:
    fjdaryPfCmEntry.setStatus("current")


class _FjdaryPfCmIndex_Type(Integer32):
    """Custom type fjdaryPfCmIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_FjdaryPfCmIndex_Type.__name__ = "Integer32"
_FjdaryPfCmIndex_Object = MibTableColumn
fjdaryPfCmIndex = _FjdaryPfCmIndex_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 5, 4, 2, 1, 1),
    _FjdaryPfCmIndex_Type()
)
fjdaryPfCmIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fjdaryPfCmIndex.setStatus("current")


class _FjdaryPfCmBusy_Type(Integer32):
    """Custom type fjdaryPfCmBusy based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_FjdaryPfCmBusy_Type.__name__ = "Integer32"
_FjdaryPfCmBusy_Object = MibTableColumn
fjdaryPfCmBusy = _FjdaryPfCmBusy_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 5, 4, 2, 1, 2),
    _FjdaryPfCmBusy_Type()
)
fjdaryPfCmBusy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fjdaryPfCmBusy.setStatus("current")


class _FjdaryPfCmCpRemain_Type(OctetString):
    """Custom type fjdaryPfCmCpRemain based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_FjdaryPfCmCpRemain_Type.__name__ = "OctetString"
_FjdaryPfCmCpRemain_Object = MibTableColumn
fjdaryPfCmCpRemain = _FjdaryPfCmCpRemain_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 5, 4, 2, 1, 3),
    _FjdaryPfCmCpRemain_Type()
)
fjdaryPfCmCpRemain.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fjdaryPfCmCpRemain.setStatus("current")
_FjdaryPfCaPort_ObjectIdentity = ObjectIdentity
fjdaryPfCaPort = _FjdaryPfCaPort_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 5, 5)
)


class _FjdaryPfCaPortCount_Type(Integer32):
    """Custom type fjdaryPfCaPortCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_FjdaryPfCaPortCount_Type.__name__ = "Integer32"
_FjdaryPfCaPortCount_Object = MibScalar
fjdaryPfCaPortCount = _FjdaryPfCaPortCount_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 5, 5, 1),
    _FjdaryPfCaPortCount_Type()
)
fjdaryPfCaPortCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fjdaryPfCaPortCount.setStatus("current")
_FjdaryPfCaPortTable_Object = MibTable
fjdaryPfCaPortTable = _FjdaryPfCaPortTable_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 5, 5, 2)
)
if mibBuilder.loadTexts:
    fjdaryPfCaPortTable.setStatus("current")
_FjdaryPfCaPortEntry_Object = MibTableRow
fjdaryPfCaPortEntry = _FjdaryPfCaPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 5, 5, 2, 1)
)
fjdaryPfCaPortEntry.setIndexNames(
    (0, "FJDARY-E150", "fjdaryPfCaPortIndex"),
)
if mibBuilder.loadTexts:
    fjdaryPfCaPortEntry.setStatus("current")


class _FjdaryPfCaPortIndex_Type(Integer32):
    """Custom type fjdaryPfCaPortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_FjdaryPfCaPortIndex_Type.__name__ = "Integer32"
_FjdaryPfCaPortIndex_Object = MibTableColumn
fjdaryPfCaPortIndex = _FjdaryPfCaPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 5, 5, 2, 1, 1),
    _FjdaryPfCaPortIndex_Type()
)
fjdaryPfCaPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fjdaryPfCaPortIndex.setStatus("current")


class _FjdaryPfCaPortMode_Type(Integer32):
    """Custom type fjdaryPfCaPortMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(11,
              12,
              13,
              20)
        )
    )
    namedValues = NamedValues(
        *(("ca", 11),
          ("cara", 13),
          ("initiator", 20),
          ("ra", 12))
    )


_FjdaryPfCaPortMode_Type.__name__ = "Integer32"
_FjdaryPfCaPortMode_Object = MibTableColumn
fjdaryPfCaPortMode = _FjdaryPfCaPortMode_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 5, 5, 2, 1, 2),
    _FjdaryPfCaPortMode_Type()
)
fjdaryPfCaPortMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fjdaryPfCaPortMode.setStatus("current")


class _FjdaryPfCaPortRdIOPS_Type(Integer32):
    """Custom type fjdaryPfCaPortRdIOPS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_FjdaryPfCaPortRdIOPS_Type.__name__ = "Integer32"
_FjdaryPfCaPortRdIOPS_Object = MibTableColumn
fjdaryPfCaPortRdIOPS = _FjdaryPfCaPortRdIOPS_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 5, 5, 2, 1, 3),
    _FjdaryPfCaPortRdIOPS_Type()
)
fjdaryPfCaPortRdIOPS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fjdaryPfCaPortRdIOPS.setStatus("current")


class _FjdaryPfCaPortWtIOPS_Type(Integer32):
    """Custom type fjdaryPfCaPortWtIOPS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_FjdaryPfCaPortWtIOPS_Type.__name__ = "Integer32"
_FjdaryPfCaPortWtIOPS_Object = MibTableColumn
fjdaryPfCaPortWtIOPS = _FjdaryPfCaPortWtIOPS_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 5, 5, 2, 1, 4),
    _FjdaryPfCaPortWtIOPS_Type()
)
fjdaryPfCaPortWtIOPS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fjdaryPfCaPortWtIOPS.setStatus("current")


class _FjdaryPfCaPortRdTp_Type(Integer32):
    """Custom type fjdaryPfCaPortRdTp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_FjdaryPfCaPortRdTp_Type.__name__ = "Integer32"
_FjdaryPfCaPortRdTp_Object = MibTableColumn
fjdaryPfCaPortRdTp = _FjdaryPfCaPortRdTp_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 5, 5, 2, 1, 5),
    _FjdaryPfCaPortRdTp_Type()
)
fjdaryPfCaPortRdTp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fjdaryPfCaPortRdTp.setStatus("current")


class _FjdaryPfCaPortWtTp_Type(Integer32):
    """Custom type fjdaryPfCaPortWtTp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_FjdaryPfCaPortWtTp_Type.__name__ = "Integer32"
_FjdaryPfCaPortWtTp_Object = MibTableColumn
fjdaryPfCaPortWtTp = _FjdaryPfCaPortWtTp_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 5, 5, 2, 1, 6),
    _FjdaryPfCaPortWtTp_Type()
)
fjdaryPfCaPortWtTp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fjdaryPfCaPortWtTp.setStatus("current")
_FjdaryPfDtOlu_ObjectIdentity = ObjectIdentity
fjdaryPfDtOlu = _FjdaryPfDtOlu_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 5, 6)
)


class _FjdaryPfDtOluCount_Type(Integer32):
    """Custom type fjdaryPfDtOluCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_FjdaryPfDtOluCount_Type.__name__ = "Integer32"
_FjdaryPfDtOluCount_Object = MibScalar
fjdaryPfDtOluCount = _FjdaryPfDtOluCount_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 5, 6, 1),
    _FjdaryPfDtOluCount_Type()
)
fjdaryPfDtOluCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fjdaryPfDtOluCount.setStatus("current")
_FjdaryPfDtOluTable_Object = MibTable
fjdaryPfDtOluTable = _FjdaryPfDtOluTable_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 5, 6, 2)
)
if mibBuilder.loadTexts:
    fjdaryPfDtOluTable.setStatus("current")
_FjdaryPfDtOluEntry_Object = MibTableRow
fjdaryPfDtOluEntry = _FjdaryPfDtOluEntry_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 5, 6, 2, 1)
)
fjdaryPfDtOluEntry.setIndexNames(
    (0, "FJDARY-E150", "fjdaryPfDtOluIndex"),
)
if mibBuilder.loadTexts:
    fjdaryPfDtOluEntry.setStatus("current")


class _FjdaryPfDtOluIndex_Type(Integer32):
    """Custom type fjdaryPfDtOluIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_FjdaryPfDtOluIndex_Type.__name__ = "Integer32"
_FjdaryPfDtOluIndex_Object = MibTableColumn
fjdaryPfDtOluIndex = _FjdaryPfDtOluIndex_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 5, 6, 2, 1, 1),
    _FjdaryPfDtOluIndex_Type()
)
fjdaryPfDtOluIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fjdaryPfDtOluIndex.setStatus("current")


class _FjdaryPfDtOluInfo_Type(OctetString):
    """Custom type fjdaryPfDtOluInfo based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_FjdaryPfDtOluInfo_Type.__name__ = "OctetString"
_FjdaryPfDtOluInfo_Object = MibTableColumn
fjdaryPfDtOluInfo = _FjdaryPfDtOluInfo_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 5, 6, 2, 1, 2),
    _FjdaryPfDtOluInfo_Type()
)
fjdaryPfDtOluInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fjdaryPfDtOluInfo.setStatus("current")
_FjdaryPfDtDisk_ObjectIdentity = ObjectIdentity
fjdaryPfDtDisk = _FjdaryPfDtDisk_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 5, 7)
)


class _FjdaryPfDtDiskCount_Type(Integer32):
    """Custom type fjdaryPfDtDiskCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_FjdaryPfDtDiskCount_Type.__name__ = "Integer32"
_FjdaryPfDtDiskCount_Object = MibScalar
fjdaryPfDtDiskCount = _FjdaryPfDtDiskCount_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 5, 7, 1),
    _FjdaryPfDtDiskCount_Type()
)
fjdaryPfDtDiskCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fjdaryPfDtDiskCount.setStatus("current")
_FjdaryPfDtDiskTable_Object = MibTable
fjdaryPfDtDiskTable = _FjdaryPfDtDiskTable_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 5, 7, 2)
)
if mibBuilder.loadTexts:
    fjdaryPfDtDiskTable.setStatus("current")
_FjdaryPfDtDiskEntry_Object = MibTableRow
fjdaryPfDtDiskEntry = _FjdaryPfDtDiskEntry_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 5, 7, 2, 1)
)
fjdaryPfDtDiskEntry.setIndexNames(
    (0, "FJDARY-E150", "fjdaryPfDtDiskIndex"),
)
if mibBuilder.loadTexts:
    fjdaryPfDtDiskEntry.setStatus("current")


class _FjdaryPfDtDiskIndex_Type(Integer32):
    """Custom type fjdaryPfDtDiskIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_FjdaryPfDtDiskIndex_Type.__name__ = "Integer32"
_FjdaryPfDtDiskIndex_Object = MibTableColumn
fjdaryPfDtDiskIndex = _FjdaryPfDtDiskIndex_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 5, 7, 2, 1, 1),
    _FjdaryPfDtDiskIndex_Type()
)
fjdaryPfDtDiskIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fjdaryPfDtDiskIndex.setStatus("current")


class _FjdaryPfDtDiskInfo_Type(OctetString):
    """Custom type fjdaryPfDtDiskInfo based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_FjdaryPfDtDiskInfo_Type.__name__ = "OctetString"
_FjdaryPfDtDiskInfo_Object = MibTableColumn
fjdaryPfDtDiskInfo = _FjdaryPfDtDiskInfo_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 5, 7, 2, 1, 2),
    _FjdaryPfDtDiskInfo_Type()
)
fjdaryPfDtDiskInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fjdaryPfDtDiskInfo.setStatus("current")
_FjdaryPfDtCm_ObjectIdentity = ObjectIdentity
fjdaryPfDtCm = _FjdaryPfDtCm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 5, 8)
)


class _FjdaryPfDtCmCount_Type(Integer32):
    """Custom type fjdaryPfDtCmCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_FjdaryPfDtCmCount_Type.__name__ = "Integer32"
_FjdaryPfDtCmCount_Object = MibScalar
fjdaryPfDtCmCount = _FjdaryPfDtCmCount_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 5, 8, 1),
    _FjdaryPfDtCmCount_Type()
)
fjdaryPfDtCmCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fjdaryPfDtCmCount.setStatus("current")
_FjdaryPfDtCmTable_Object = MibTable
fjdaryPfDtCmTable = _FjdaryPfDtCmTable_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 5, 8, 2)
)
if mibBuilder.loadTexts:
    fjdaryPfDtCmTable.setStatus("current")
_FjdaryPfDtCmEntry_Object = MibTableRow
fjdaryPfDtCmEntry = _FjdaryPfDtCmEntry_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 5, 8, 2, 1)
)
fjdaryPfDtCmEntry.setIndexNames(
    (0, "FJDARY-E150", "fjdaryPfDtCmIndex"),
)
if mibBuilder.loadTexts:
    fjdaryPfDtCmEntry.setStatus("current")


class _FjdaryPfDtCmIndex_Type(Integer32):
    """Custom type fjdaryPfDtCmIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_FjdaryPfDtCmIndex_Type.__name__ = "Integer32"
_FjdaryPfDtCmIndex_Object = MibTableColumn
fjdaryPfDtCmIndex = _FjdaryPfDtCmIndex_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 5, 8, 2, 1, 1),
    _FjdaryPfDtCmIndex_Type()
)
fjdaryPfDtCmIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fjdaryPfDtCmIndex.setStatus("current")


class _FjdaryPfDtCmInfo_Type(OctetString):
    """Custom type fjdaryPfDtCmInfo based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_FjdaryPfDtCmInfo_Type.__name__ = "OctetString"
_FjdaryPfDtCmInfo_Object = MibTableColumn
fjdaryPfDtCmInfo = _FjdaryPfDtCmInfo_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 5, 8, 2, 1, 2),
    _FjdaryPfDtCmInfo_Type()
)
fjdaryPfDtCmInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fjdaryPfDtCmInfo.setStatus("current")
_FjdaryPfDtCaPort_ObjectIdentity = ObjectIdentity
fjdaryPfDtCaPort = _FjdaryPfDtCaPort_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 5, 9)
)


class _FjdaryPfDtCaPortCount_Type(Integer32):
    """Custom type fjdaryPfDtCaPortCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_FjdaryPfDtCaPortCount_Type.__name__ = "Integer32"
_FjdaryPfDtCaPortCount_Object = MibScalar
fjdaryPfDtCaPortCount = _FjdaryPfDtCaPortCount_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 5, 9, 1),
    _FjdaryPfDtCaPortCount_Type()
)
fjdaryPfDtCaPortCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fjdaryPfDtCaPortCount.setStatus("current")
_FjdaryPfDtCaPortTable_Object = MibTable
fjdaryPfDtCaPortTable = _FjdaryPfDtCaPortTable_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 5, 9, 2)
)
if mibBuilder.loadTexts:
    fjdaryPfDtCaPortTable.setStatus("current")
_FjdaryPfDtCaPortEntry_Object = MibTableRow
fjdaryPfDtCaPortEntry = _FjdaryPfDtCaPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 5, 9, 2, 1)
)
fjdaryPfDtCaPortEntry.setIndexNames(
    (0, "FJDARY-E150", "fjdaryPfDtCaPortIndex"),
)
if mibBuilder.loadTexts:
    fjdaryPfDtCaPortEntry.setStatus("current")


class _FjdaryPfDtCaPortIndex_Type(Integer32):
    """Custom type fjdaryPfDtCaPortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_FjdaryPfDtCaPortIndex_Type.__name__ = "Integer32"
_FjdaryPfDtCaPortIndex_Object = MibTableColumn
fjdaryPfDtCaPortIndex = _FjdaryPfDtCaPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 5, 9, 2, 1, 1),
    _FjdaryPfDtCaPortIndex_Type()
)
fjdaryPfDtCaPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fjdaryPfDtCaPortIndex.setStatus("current")


class _FjdaryPfDtCaPortInfo_Type(OctetString):
    """Custom type fjdaryPfDtCaPortInfo based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_FjdaryPfDtCaPortInfo_Type.__name__ = "OctetString"
_FjdaryPfDtCaPortInfo_Object = MibTableColumn
fjdaryPfDtCaPortInfo = _FjdaryPfDtCaPortInfo_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 5, 9, 2, 1, 2),
    _FjdaryPfDtCaPortInfo_Type()
)
fjdaryPfDtCaPortInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fjdaryPfDtCaPortInfo.setStatus("current")
_FjdaryPfRaPort_ObjectIdentity = ObjectIdentity
fjdaryPfRaPort = _FjdaryPfRaPort_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 5, 10)
)


class _FjdaryPfRaPortCount_Type(Integer32):
    """Custom type fjdaryPfRaPortCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_FjdaryPfRaPortCount_Type.__name__ = "Integer32"
_FjdaryPfRaPortCount_Object = MibScalar
fjdaryPfRaPortCount = _FjdaryPfRaPortCount_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 5, 10, 1),
    _FjdaryPfRaPortCount_Type()
)
fjdaryPfRaPortCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fjdaryPfRaPortCount.setStatus("current")
_FjdaryPfRaPortTable_Object = MibTable
fjdaryPfRaPortTable = _FjdaryPfRaPortTable_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 5, 10, 2)
)
if mibBuilder.loadTexts:
    fjdaryPfRaPortTable.setStatus("current")
_FjdaryPfRaPortEntry_Object = MibTableRow
fjdaryPfRaPortEntry = _FjdaryPfRaPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 5, 10, 2, 1)
)
fjdaryPfRaPortEntry.setIndexNames(
    (0, "FJDARY-E150", "fjdaryPfRaPortIndex"),
)
if mibBuilder.loadTexts:
    fjdaryPfRaPortEntry.setStatus("current")


class _FjdaryPfRaPortIndex_Type(Integer32):
    """Custom type fjdaryPfRaPortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_FjdaryPfRaPortIndex_Type.__name__ = "Integer32"
_FjdaryPfRaPortIndex_Object = MibTableColumn
fjdaryPfRaPortIndex = _FjdaryPfRaPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 5, 10, 2, 1, 1),
    _FjdaryPfRaPortIndex_Type()
)
fjdaryPfRaPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fjdaryPfRaPortIndex.setStatus("current")


class _FjdaryPfRaPortMode_Type(Integer32):
    """Custom type fjdaryPfRaPortMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(11,
              12,
              13,
              20)
        )
    )
    namedValues = NamedValues(
        *(("ca", 11),
          ("cara", 13),
          ("initiator", 20),
          ("ra", 12))
    )


_FjdaryPfRaPortMode_Type.__name__ = "Integer32"
_FjdaryPfRaPortMode_Object = MibTableColumn
fjdaryPfRaPortMode = _FjdaryPfRaPortMode_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 5, 10, 2, 1, 2),
    _FjdaryPfRaPortMode_Type()
)
fjdaryPfRaPortMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fjdaryPfRaPortMode.setStatus("current")


class _FjdaryPfRaPortRdIOPS_Type(Integer32):
    """Custom type fjdaryPfRaPortRdIOPS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_FjdaryPfRaPortRdIOPS_Type.__name__ = "Integer32"
_FjdaryPfRaPortRdIOPS_Object = MibTableColumn
fjdaryPfRaPortRdIOPS = _FjdaryPfRaPortRdIOPS_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 5, 10, 2, 1, 3),
    _FjdaryPfRaPortRdIOPS_Type()
)
fjdaryPfRaPortRdIOPS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fjdaryPfRaPortRdIOPS.setStatus("current")


class _FjdaryPfRaPortWtIOPS_Type(Integer32):
    """Custom type fjdaryPfRaPortWtIOPS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_FjdaryPfRaPortWtIOPS_Type.__name__ = "Integer32"
_FjdaryPfRaPortWtIOPS_Object = MibTableColumn
fjdaryPfRaPortWtIOPS = _FjdaryPfRaPortWtIOPS_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 5, 10, 2, 1, 4),
    _FjdaryPfRaPortWtIOPS_Type()
)
fjdaryPfRaPortWtIOPS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fjdaryPfRaPortWtIOPS.setStatus("current")


class _FjdaryPfRaPortRdTp_Type(Integer32):
    """Custom type fjdaryPfRaPortRdTp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_FjdaryPfRaPortRdTp_Type.__name__ = "Integer32"
_FjdaryPfRaPortRdTp_Object = MibTableColumn
fjdaryPfRaPortRdTp = _FjdaryPfRaPortRdTp_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 5, 10, 2, 1, 5),
    _FjdaryPfRaPortRdTp_Type()
)
fjdaryPfRaPortRdTp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fjdaryPfRaPortRdTp.setStatus("current")


class _FjdaryPfRaPortWtTp_Type(Integer32):
    """Custom type fjdaryPfRaPortWtTp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_FjdaryPfRaPortWtTp_Type.__name__ = "Integer32"
_FjdaryPfRaPortWtTp_Object = MibTableColumn
fjdaryPfRaPortWtTp = _FjdaryPfRaPortWtTp_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 5, 10, 2, 1, 6),
    _FjdaryPfRaPortWtTp_Type()
)
fjdaryPfRaPortWtTp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fjdaryPfRaPortWtTp.setStatus("current")
_FjdaryPfDtRaPort_ObjectIdentity = ObjectIdentity
fjdaryPfDtRaPort = _FjdaryPfDtRaPort_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 5, 11)
)


class _FjdaryPfDtRaPortCount_Type(Integer32):
    """Custom type fjdaryPfDtRaPortCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_FjdaryPfDtRaPortCount_Type.__name__ = "Integer32"
_FjdaryPfDtRaPortCount_Object = MibScalar
fjdaryPfDtRaPortCount = _FjdaryPfDtRaPortCount_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 5, 11, 1),
    _FjdaryPfDtRaPortCount_Type()
)
fjdaryPfDtRaPortCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fjdaryPfDtRaPortCount.setStatus("current")
_FjdaryPfDtRaPortTable_Object = MibTable
fjdaryPfDtRaPortTable = _FjdaryPfDtRaPortTable_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 5, 11, 2)
)
if mibBuilder.loadTexts:
    fjdaryPfDtRaPortTable.setStatus("current")
_FjdaryPfDtRaPortEntry_Object = MibTableRow
fjdaryPfDtRaPortEntry = _FjdaryPfDtRaPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 5, 11, 2, 1)
)
fjdaryPfDtRaPortEntry.setIndexNames(
    (0, "FJDARY-E150", "fjdaryPfDtRaPortIndex"),
)
if mibBuilder.loadTexts:
    fjdaryPfDtRaPortEntry.setStatus("current")


class _FjdaryPfDtRaPortIndex_Type(Integer32):
    """Custom type fjdaryPfDtRaPortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_FjdaryPfDtRaPortIndex_Type.__name__ = "Integer32"
_FjdaryPfDtRaPortIndex_Object = MibTableColumn
fjdaryPfDtRaPortIndex = _FjdaryPfDtRaPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 5, 11, 2, 1, 1),
    _FjdaryPfDtRaPortIndex_Type()
)
fjdaryPfDtRaPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fjdaryPfDtRaPortIndex.setStatus("current")


class _FjdaryPfDtRaPortInfo_Type(OctetString):
    """Custom type fjdaryPfDtRaPortInfo based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_FjdaryPfDtRaPortInfo_Type.__name__ = "OctetString"
_FjdaryPfDtRaPortInfo_Object = MibTableColumn
fjdaryPfDtRaPortInfo = _FjdaryPfDtRaPortInfo_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 5, 11, 2, 1, 2),
    _FjdaryPfDtRaPortInfo_Type()
)
fjdaryPfDtRaPortInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fjdaryPfDtRaPortInfo.setStatus("current")
_FjdaryPfPfm_ObjectIdentity = ObjectIdentity
fjdaryPfPfm = _FjdaryPfPfm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 5, 12)
)


class _FjdaryPfPfmCount_Type(Integer32):
    """Custom type fjdaryPfPfmCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_FjdaryPfPfmCount_Type.__name__ = "Integer32"
_FjdaryPfPfmCount_Object = MibScalar
fjdaryPfPfmCount = _FjdaryPfPfmCount_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 5, 12, 1),
    _FjdaryPfPfmCount_Type()
)
fjdaryPfPfmCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fjdaryPfPfmCount.setStatus("current")
_FjdaryPfPfmTable_Object = MibTable
fjdaryPfPfmTable = _FjdaryPfPfmTable_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 5, 12, 2)
)
if mibBuilder.loadTexts:
    fjdaryPfPfmTable.setStatus("current")
_FjdaryPfPfmEntry_Object = MibTableRow
fjdaryPfPfmEntry = _FjdaryPfPfmEntry_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 5, 12, 2, 1)
)
fjdaryPfPfmEntry.setIndexNames(
    (0, "FJDARY-E150", "fjdaryPfPfmIndex"),
)
if mibBuilder.loadTexts:
    fjdaryPfPfmEntry.setStatus("current")


class _FjdaryPfPfmIndex_Type(Integer32):
    """Custom type fjdaryPfPfmIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_FjdaryPfPfmIndex_Type.__name__ = "Integer32"
_FjdaryPfPfmIndex_Object = MibTableColumn
fjdaryPfPfmIndex = _FjdaryPfPfmIndex_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 5, 12, 2, 1, 1),
    _FjdaryPfPfmIndex_Type()
)
fjdaryPfPfmIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fjdaryPfPfmIndex.setStatus("current")


class _FjdaryPfPfmBusy_Type(Integer32):
    """Custom type fjdaryPfPfmBusy based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_FjdaryPfPfmBusy_Type.__name__ = "Integer32"
_FjdaryPfPfmBusy_Object = MibTableColumn
fjdaryPfPfmBusy = _FjdaryPfPfmBusy_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 5, 12, 2, 1, 2),
    _FjdaryPfPfmBusy_Type()
)
fjdaryPfPfmBusy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fjdaryPfPfmBusy.setStatus("current")
_FjdaryPfDtPfm_ObjectIdentity = ObjectIdentity
fjdaryPfDtPfm = _FjdaryPfDtPfm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 5, 13)
)


class _FjdaryPfDPfmCount_Type(Integer32):
    """Custom type fjdaryPfDPfmCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_FjdaryPfDPfmCount_Type.__name__ = "Integer32"
_FjdaryPfDPfmCount_Object = MibScalar
fjdaryPfDPfmCount = _FjdaryPfDPfmCount_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 5, 13, 1),
    _FjdaryPfDPfmCount_Type()
)
fjdaryPfDPfmCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fjdaryPfDPfmCount.setStatus("current")
_FjdaryPfDtPfmTable_Object = MibTable
fjdaryPfDtPfmTable = _FjdaryPfDtPfmTable_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 5, 13, 2)
)
if mibBuilder.loadTexts:
    fjdaryPfDtPfmTable.setStatus("current")
_FjdaryPfDtPfmEntry_Object = MibTableRow
fjdaryPfDtPfmEntry = _FjdaryPfDtPfmEntry_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 5, 13, 2, 1)
)
fjdaryPfDtPfmEntry.setIndexNames(
    (0, "FJDARY-E150", "fjdaryPfDtPfmIndex"),
)
if mibBuilder.loadTexts:
    fjdaryPfDtPfmEntry.setStatus("current")


class _FjdaryPfDtPfmIndex_Type(Integer32):
    """Custom type fjdaryPfDtPfmIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_FjdaryPfDtPfmIndex_Type.__name__ = "Integer32"
_FjdaryPfDtPfmIndex_Object = MibTableColumn
fjdaryPfDtPfmIndex = _FjdaryPfDtPfmIndex_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 5, 13, 2, 1, 1),
    _FjdaryPfDtPfmIndex_Type()
)
fjdaryPfDtPfmIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fjdaryPfDtPfmIndex.setStatus("current")


class _FjdaryPfDtPfmInfo_Type(OctetString):
    """Custom type fjdaryPfDtPfmInfo based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_FjdaryPfDtPfmInfo_Type.__name__ = "OctetString"
_FjdaryPfDtPfmInfo_Object = MibTableColumn
fjdaryPfDtPfmInfo = _FjdaryPfDtPfmInfo_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 5, 13, 2, 1, 2),
    _FjdaryPfDtPfmInfo_Type()
)
fjdaryPfDtPfmInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fjdaryPfDtPfmInfo.setStatus("current")
_FjdaryPfCmCore_ObjectIdentity = ObjectIdentity
fjdaryPfCmCore = _FjdaryPfCmCore_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 5, 14)
)


class _FjdaryPfCmCoreCount_Type(Integer32):
    """Custom type fjdaryPfCmCoreCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_FjdaryPfCmCoreCount_Type.__name__ = "Integer32"
_FjdaryPfCmCoreCount_Object = MibScalar
fjdaryPfCmCoreCount = _FjdaryPfCmCoreCount_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 5, 14, 1),
    _FjdaryPfCmCoreCount_Type()
)
fjdaryPfCmCoreCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fjdaryPfCmCoreCount.setStatus("current")
_FjdaryPfCmCoreTable_Object = MibTable
fjdaryPfCmCoreTable = _FjdaryPfCmCoreTable_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 5, 14, 2)
)
if mibBuilder.loadTexts:
    fjdaryPfCmCoreTable.setStatus("current")
_FjdaryPfCmCoreEntry_Object = MibTableRow
fjdaryPfCmCoreEntry = _FjdaryPfCmCoreEntry_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 5, 14, 2, 1)
)
fjdaryPfCmCoreEntry.setIndexNames(
    (0, "FJDARY-E150", "fjdaryPfCmCoreIndex"),
)
if mibBuilder.loadTexts:
    fjdaryPfCmCoreEntry.setStatus("current")


class _FjdaryPfCmCoreIndex_Type(Integer32):
    """Custom type fjdaryPfCmCoreIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_FjdaryPfCmCoreIndex_Type.__name__ = "Integer32"
_FjdaryPfCmCoreIndex_Object = MibTableColumn
fjdaryPfCmCoreIndex = _FjdaryPfCmCoreIndex_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 5, 14, 2, 1, 1),
    _FjdaryPfCmCoreIndex_Type()
)
fjdaryPfCmCoreIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fjdaryPfCmCoreIndex.setStatus("current")


class _FjdaryPfCmCoreValidCount_Type(Integer32):
    """Custom type fjdaryPfCmCoreValidCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_FjdaryPfCmCoreValidCount_Type.__name__ = "Integer32"
_FjdaryPfCmCoreValidCount_Object = MibTableColumn
fjdaryPfCmCoreValidCount = _FjdaryPfCmCoreValidCount_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 5, 14, 2, 1, 2),
    _FjdaryPfCmCoreValidCount_Type()
)
fjdaryPfCmCoreValidCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fjdaryPfCmCoreValidCount.setStatus("current")


class _FjdaryPfCmCoreBusy0_Type(Integer32):
    """Custom type fjdaryPfCmCoreBusy0 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_FjdaryPfCmCoreBusy0_Type.__name__ = "Integer32"
_FjdaryPfCmCoreBusy0_Object = MibTableColumn
fjdaryPfCmCoreBusy0 = _FjdaryPfCmCoreBusy0_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 5, 14, 2, 1, 3),
    _FjdaryPfCmCoreBusy0_Type()
)
fjdaryPfCmCoreBusy0.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fjdaryPfCmCoreBusy0.setStatus("current")


class _FjdaryPfCmCoreBusy1_Type(Integer32):
    """Custom type fjdaryPfCmCoreBusy1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_FjdaryPfCmCoreBusy1_Type.__name__ = "Integer32"
_FjdaryPfCmCoreBusy1_Object = MibTableColumn
fjdaryPfCmCoreBusy1 = _FjdaryPfCmCoreBusy1_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 5, 14, 2, 1, 4),
    _FjdaryPfCmCoreBusy1_Type()
)
fjdaryPfCmCoreBusy1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fjdaryPfCmCoreBusy1.setStatus("current")


class _FjdaryPfCmCoreBusy2_Type(Integer32):
    """Custom type fjdaryPfCmCoreBusy2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_FjdaryPfCmCoreBusy2_Type.__name__ = "Integer32"
_FjdaryPfCmCoreBusy2_Object = MibTableColumn
fjdaryPfCmCoreBusy2 = _FjdaryPfCmCoreBusy2_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 5, 14, 2, 1, 5),
    _FjdaryPfCmCoreBusy2_Type()
)
fjdaryPfCmCoreBusy2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fjdaryPfCmCoreBusy2.setStatus("current")


class _FjdaryPfCmCoreBusy3_Type(Integer32):
    """Custom type fjdaryPfCmCoreBusy3 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_FjdaryPfCmCoreBusy3_Type.__name__ = "Integer32"
_FjdaryPfCmCoreBusy3_Object = MibTableColumn
fjdaryPfCmCoreBusy3 = _FjdaryPfCmCoreBusy3_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 5, 14, 2, 1, 6),
    _FjdaryPfCmCoreBusy3_Type()
)
fjdaryPfCmCoreBusy3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fjdaryPfCmCoreBusy3.setStatus("current")


class _FjdaryPfCmCoreBusy4_Type(Integer32):
    """Custom type fjdaryPfCmCoreBusy4 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_FjdaryPfCmCoreBusy4_Type.__name__ = "Integer32"
_FjdaryPfCmCoreBusy4_Object = MibTableColumn
fjdaryPfCmCoreBusy4 = _FjdaryPfCmCoreBusy4_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 5, 14, 2, 1, 7),
    _FjdaryPfCmCoreBusy4_Type()
)
fjdaryPfCmCoreBusy4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fjdaryPfCmCoreBusy4.setStatus("current")


class _FjdaryPfCmCoreBusy5_Type(Integer32):
    """Custom type fjdaryPfCmCoreBusy5 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_FjdaryPfCmCoreBusy5_Type.__name__ = "Integer32"
_FjdaryPfCmCoreBusy5_Object = MibTableColumn
fjdaryPfCmCoreBusy5 = _FjdaryPfCmCoreBusy5_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 5, 14, 2, 1, 8),
    _FjdaryPfCmCoreBusy5_Type()
)
fjdaryPfCmCoreBusy5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fjdaryPfCmCoreBusy5.setStatus("current")


class _FjdaryPfCmCoreBusy6_Type(Integer32):
    """Custom type fjdaryPfCmCoreBusy6 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_FjdaryPfCmCoreBusy6_Type.__name__ = "Integer32"
_FjdaryPfCmCoreBusy6_Object = MibTableColumn
fjdaryPfCmCoreBusy6 = _FjdaryPfCmCoreBusy6_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 5, 14, 2, 1, 9),
    _FjdaryPfCmCoreBusy6_Type()
)
fjdaryPfCmCoreBusy6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fjdaryPfCmCoreBusy6.setStatus("current")


class _FjdaryPfCmCoreBusy7_Type(Integer32):
    """Custom type fjdaryPfCmCoreBusy7 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_FjdaryPfCmCoreBusy7_Type.__name__ = "Integer32"
_FjdaryPfCmCoreBusy7_Object = MibTableColumn
fjdaryPfCmCoreBusy7 = _FjdaryPfCmCoreBusy7_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 5, 14, 2, 1, 10),
    _FjdaryPfCmCoreBusy7_Type()
)
fjdaryPfCmCoreBusy7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fjdaryPfCmCoreBusy7.setStatus("current")


class _FjdaryPfCmCoreBusy8_Type(Integer32):
    """Custom type fjdaryPfCmCoreBusy8 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_FjdaryPfCmCoreBusy8_Type.__name__ = "Integer32"
_FjdaryPfCmCoreBusy8_Object = MibTableColumn
fjdaryPfCmCoreBusy8 = _FjdaryPfCmCoreBusy8_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 5, 14, 2, 1, 11),
    _FjdaryPfCmCoreBusy8_Type()
)
fjdaryPfCmCoreBusy8.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fjdaryPfCmCoreBusy8.setStatus("current")


class _FjdaryPfCmCoreBusy9_Type(Integer32):
    """Custom type fjdaryPfCmCoreBusy9 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_FjdaryPfCmCoreBusy9_Type.__name__ = "Integer32"
_FjdaryPfCmCoreBusy9_Object = MibTableColumn
fjdaryPfCmCoreBusy9 = _FjdaryPfCmCoreBusy9_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 5, 14, 2, 1, 12),
    _FjdaryPfCmCoreBusy9_Type()
)
fjdaryPfCmCoreBusy9.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fjdaryPfCmCoreBusy9.setStatus("current")


class _FjdaryPfCmCoreBusy10_Type(Integer32):
    """Custom type fjdaryPfCmCoreBusy10 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_FjdaryPfCmCoreBusy10_Type.__name__ = "Integer32"
_FjdaryPfCmCoreBusy10_Object = MibTableColumn
fjdaryPfCmCoreBusy10 = _FjdaryPfCmCoreBusy10_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 5, 14, 2, 1, 13),
    _FjdaryPfCmCoreBusy10_Type()
)
fjdaryPfCmCoreBusy10.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fjdaryPfCmCoreBusy10.setStatus("current")


class _FjdaryPfCmCoreBusy11_Type(Integer32):
    """Custom type fjdaryPfCmCoreBusy11 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_FjdaryPfCmCoreBusy11_Type.__name__ = "Integer32"
_FjdaryPfCmCoreBusy11_Object = MibTableColumn
fjdaryPfCmCoreBusy11 = _FjdaryPfCmCoreBusy11_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 5, 14, 2, 1, 14),
    _FjdaryPfCmCoreBusy11_Type()
)
fjdaryPfCmCoreBusy11.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fjdaryPfCmCoreBusy11.setStatus("current")


class _FjdaryPfCmCoreBusy12_Type(Integer32):
    """Custom type fjdaryPfCmCoreBusy12 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_FjdaryPfCmCoreBusy12_Type.__name__ = "Integer32"
_FjdaryPfCmCoreBusy12_Object = MibTableColumn
fjdaryPfCmCoreBusy12 = _FjdaryPfCmCoreBusy12_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 5, 14, 2, 1, 15),
    _FjdaryPfCmCoreBusy12_Type()
)
fjdaryPfCmCoreBusy12.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fjdaryPfCmCoreBusy12.setStatus("current")


class _FjdaryPfCmCoreBusy13_Type(Integer32):
    """Custom type fjdaryPfCmCoreBusy13 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_FjdaryPfCmCoreBusy13_Type.__name__ = "Integer32"
_FjdaryPfCmCoreBusy13_Object = MibTableColumn
fjdaryPfCmCoreBusy13 = _FjdaryPfCmCoreBusy13_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 5, 14, 2, 1, 16),
    _FjdaryPfCmCoreBusy13_Type()
)
fjdaryPfCmCoreBusy13.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fjdaryPfCmCoreBusy13.setStatus("current")


class _FjdaryPfCmCoreBusy14_Type(Integer32):
    """Custom type fjdaryPfCmCoreBusy14 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_FjdaryPfCmCoreBusy14_Type.__name__ = "Integer32"
_FjdaryPfCmCoreBusy14_Object = MibTableColumn
fjdaryPfCmCoreBusy14 = _FjdaryPfCmCoreBusy14_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 5, 14, 2, 1, 17),
    _FjdaryPfCmCoreBusy14_Type()
)
fjdaryPfCmCoreBusy14.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fjdaryPfCmCoreBusy14.setStatus("current")


class _FjdaryPfCmCoreBusy15_Type(Integer32):
    """Custom type fjdaryPfCmCoreBusy15 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_FjdaryPfCmCoreBusy15_Type.__name__ = "Integer32"
_FjdaryPfCmCoreBusy15_Object = MibTableColumn
fjdaryPfCmCoreBusy15 = _FjdaryPfCmCoreBusy15_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 5, 14, 2, 1, 18),
    _FjdaryPfCmCoreBusy15_Type()
)
fjdaryPfCmCoreBusy15.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fjdaryPfCmCoreBusy15.setStatus("current")


class _FjdaryPfCmCoreBusy16_Type(Integer32):
    """Custom type fjdaryPfCmCoreBusy16 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_FjdaryPfCmCoreBusy16_Type.__name__ = "Integer32"
_FjdaryPfCmCoreBusy16_Object = MibTableColumn
fjdaryPfCmCoreBusy16 = _FjdaryPfCmCoreBusy16_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 5, 14, 2, 1, 19),
    _FjdaryPfCmCoreBusy16_Type()
)
fjdaryPfCmCoreBusy16.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fjdaryPfCmCoreBusy16.setStatus("current")


class _FjdaryPfCmCoreBusy17_Type(Integer32):
    """Custom type fjdaryPfCmCoreBusy17 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_FjdaryPfCmCoreBusy17_Type.__name__ = "Integer32"
_FjdaryPfCmCoreBusy17_Object = MibTableColumn
fjdaryPfCmCoreBusy17 = _FjdaryPfCmCoreBusy17_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 5, 14, 2, 1, 20),
    _FjdaryPfCmCoreBusy17_Type()
)
fjdaryPfCmCoreBusy17.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fjdaryPfCmCoreBusy17.setStatus("current")


class _FjdaryPfCmCoreBusy18_Type(Integer32):
    """Custom type fjdaryPfCmCoreBusy18 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_FjdaryPfCmCoreBusy18_Type.__name__ = "Integer32"
_FjdaryPfCmCoreBusy18_Object = MibTableColumn
fjdaryPfCmCoreBusy18 = _FjdaryPfCmCoreBusy18_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 5, 14, 2, 1, 21),
    _FjdaryPfCmCoreBusy18_Type()
)
fjdaryPfCmCoreBusy18.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fjdaryPfCmCoreBusy18.setStatus("current")


class _FjdaryPfCmCoreBusy19_Type(Integer32):
    """Custom type fjdaryPfCmCoreBusy19 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_FjdaryPfCmCoreBusy19_Type.__name__ = "Integer32"
_FjdaryPfCmCoreBusy19_Object = MibTableColumn
fjdaryPfCmCoreBusy19 = _FjdaryPfCmCoreBusy19_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 5, 14, 2, 1, 22),
    _FjdaryPfCmCoreBusy19_Type()
)
fjdaryPfCmCoreBusy19.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fjdaryPfCmCoreBusy19.setStatus("current")
_FjdaryPfDtCmCore_ObjectIdentity = ObjectIdentity
fjdaryPfDtCmCore = _FjdaryPfDtCmCore_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 5, 15)
)


class _FjdaryPfDtCmCoreCount_Type(Integer32):
    """Custom type fjdaryPfDtCmCoreCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_FjdaryPfDtCmCoreCount_Type.__name__ = "Integer32"
_FjdaryPfDtCmCoreCount_Object = MibScalar
fjdaryPfDtCmCoreCount = _FjdaryPfDtCmCoreCount_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 5, 15, 1),
    _FjdaryPfDtCmCoreCount_Type()
)
fjdaryPfDtCmCoreCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fjdaryPfDtCmCoreCount.setStatus("current")
_FjdaryPfDtCmCoreTable_Object = MibTable
fjdaryPfDtCmCoreTable = _FjdaryPfDtCmCoreTable_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 5, 15, 2)
)
if mibBuilder.loadTexts:
    fjdaryPfDtCmCoreTable.setStatus("current")
_FjdaryPfDtCmCoreEntry_Object = MibTableRow
fjdaryPfDtCmCoreEntry = _FjdaryPfDtCmCoreEntry_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 5, 15, 2, 1)
)
fjdaryPfDtCmCoreEntry.setIndexNames(
    (0, "FJDARY-E150", "fjdaryPfDtCmCoreIndex"),
)
if mibBuilder.loadTexts:
    fjdaryPfDtCmCoreEntry.setStatus("current")


class _FjdaryPfDtCmCoreIndex_Type(Integer32):
    """Custom type fjdaryPfDtCmCoreIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_FjdaryPfDtCmCoreIndex_Type.__name__ = "Integer32"
_FjdaryPfDtCmCoreIndex_Object = MibTableColumn
fjdaryPfDtCmCoreIndex = _FjdaryPfDtCmCoreIndex_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 5, 15, 2, 1, 1),
    _FjdaryPfDtCmCoreIndex_Type()
)
fjdaryPfDtCmCoreIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fjdaryPfDtCmCoreIndex.setStatus("current")


class _FjdaryPfDtCmCoreInfo_Type(OctetString):
    """Custom type fjdaryPfDtCmCoreInfo based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_FjdaryPfDtCmCoreInfo_Type.__name__ = "OctetString"
_FjdaryPfDtCmCoreInfo_Object = MibTableColumn
fjdaryPfDtCmCoreInfo = _FjdaryPfDtCmCoreInfo_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 5, 15, 2, 1, 2),
    _FjdaryPfDtCmCoreInfo_Type()
)
fjdaryPfDtCmCoreInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fjdaryPfDtCmCoreInfo.setStatus("current")
_FjdaryPfCmNas_ObjectIdentity = ObjectIdentity
fjdaryPfCmNas = _FjdaryPfCmNas_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 5, 16)
)


class _FjdaryPfCmNasCount_Type(Integer32):
    """Custom type fjdaryPfCmNasCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_FjdaryPfCmNasCount_Type.__name__ = "Integer32"
_FjdaryPfCmNasCount_Object = MibScalar
fjdaryPfCmNasCount = _FjdaryPfCmNasCount_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 5, 16, 1),
    _FjdaryPfCmNasCount_Type()
)
fjdaryPfCmNasCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fjdaryPfCmNasCount.setStatus("current")
_FjdaryPfCmNasTable_Object = MibTable
fjdaryPfCmNasTable = _FjdaryPfCmNasTable_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 5, 16, 2)
)
if mibBuilder.loadTexts:
    fjdaryPfCmNasTable.setStatus("current")
_FjdaryPfCmNasEntry_Object = MibTableRow
fjdaryPfCmNasEntry = _FjdaryPfCmNasEntry_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 5, 16, 2, 1)
)
fjdaryPfCmNasEntry.setIndexNames(
    (0, "FJDARY-E150", "fjdaryPfCmNasIndex"),
)
if mibBuilder.loadTexts:
    fjdaryPfCmNasEntry.setStatus("current")


class _FjdaryPfCmNasIndex_Type(Integer32):
    """Custom type fjdaryPfCmNasIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_FjdaryPfCmNasIndex_Type.__name__ = "Integer32"
_FjdaryPfCmNasIndex_Object = MibTableColumn
fjdaryPfCmNasIndex = _FjdaryPfCmNasIndex_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 5, 16, 2, 1, 1),
    _FjdaryPfCmNasIndex_Type()
)
fjdaryPfCmNasIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fjdaryPfCmNasIndex.setStatus("current")


class _FjdaryPfCmNasIOWaitTime_Type(Integer32):
    """Custom type fjdaryPfCmNasIOWaitTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_FjdaryPfCmNasIOWaitTime_Type.__name__ = "Integer32"
_FjdaryPfCmNasIOWaitTime_Object = MibTableColumn
fjdaryPfCmNasIOWaitTime = _FjdaryPfCmNasIOWaitTime_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 5, 16, 2, 1, 2),
    _FjdaryPfCmNasIOWaitTime_Type()
)
fjdaryPfCmNasIOWaitTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fjdaryPfCmNasIOWaitTime.setStatus("current")


class _FjdaryPfCmNasRdThroughput_Type(Integer32):
    """Custom type fjdaryPfCmNasRdThroughput based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_FjdaryPfCmNasRdThroughput_Type.__name__ = "Integer32"
_FjdaryPfCmNasRdThroughput_Object = MibTableColumn
fjdaryPfCmNasRdThroughput = _FjdaryPfCmNasRdThroughput_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 5, 16, 2, 1, 3),
    _FjdaryPfCmNasRdThroughput_Type()
)
fjdaryPfCmNasRdThroughput.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fjdaryPfCmNasRdThroughput.setStatus("current")


class _FjdaryPfCmNasWtThroughput_Type(Integer32):
    """Custom type fjdaryPfCmNasWtThroughput based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_FjdaryPfCmNasWtThroughput_Type.__name__ = "Integer32"
_FjdaryPfCmNasWtThroughput_Object = MibTableColumn
fjdaryPfCmNasWtThroughput = _FjdaryPfCmNasWtThroughput_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 5, 16, 2, 1, 4),
    _FjdaryPfCmNasWtThroughput_Type()
)
fjdaryPfCmNasWtThroughput.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fjdaryPfCmNasWtThroughput.setStatus("current")


class _FjdaryPfCmNasIOCPUBusy_Type(Integer32):
    """Custom type fjdaryPfCmNasIOCPUBusy based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_FjdaryPfCmNasIOCPUBusy_Type.__name__ = "Integer32"
_FjdaryPfCmNasIOCPUBusy_Object = MibTableColumn
fjdaryPfCmNasIOCPUBusy = _FjdaryPfCmNasIOCPUBusy_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 5, 16, 2, 1, 5),
    _FjdaryPfCmNasIOCPUBusy_Type()
)
fjdaryPfCmNasIOCPUBusy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fjdaryPfCmNasIOCPUBusy.setStatus("current")


class _FjdaryPfCmNasUsageRate_Type(Integer32):
    """Custom type fjdaryPfCmNasUsageRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_FjdaryPfCmNasUsageRate_Type.__name__ = "Integer32"
_FjdaryPfCmNasUsageRate_Object = MibTableColumn
fjdaryPfCmNasUsageRate = _FjdaryPfCmNasUsageRate_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 5, 16, 2, 1, 6),
    _FjdaryPfCmNasUsageRate_Type()
)
fjdaryPfCmNasUsageRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fjdaryPfCmNasUsageRate.setStatus("current")


class _FjdaryPfCmNasUsedAmount_Type(Integer32):
    """Custom type fjdaryPfCmNasUsedAmount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_FjdaryPfCmNasUsedAmount_Type.__name__ = "Integer32"
_FjdaryPfCmNasUsedAmount_Object = MibTableColumn
fjdaryPfCmNasUsedAmount = _FjdaryPfCmNasUsedAmount_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 5, 16, 2, 1, 7),
    _FjdaryPfCmNasUsedAmount_Type()
)
fjdaryPfCmNasUsedAmount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fjdaryPfCmNasUsedAmount.setStatus("current")


class _FjdaryPfCmNasSambaOpCount_Type(Integer32):
    """Custom type fjdaryPfCmNasSambaOpCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_FjdaryPfCmNasSambaOpCount_Type.__name__ = "Integer32"
_FjdaryPfCmNasSambaOpCount_Object = MibTableColumn
fjdaryPfCmNasSambaOpCount = _FjdaryPfCmNasSambaOpCount_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 5, 16, 2, 1, 8),
    _FjdaryPfCmNasSambaOpCount_Type()
)
fjdaryPfCmNasSambaOpCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fjdaryPfCmNasSambaOpCount.setStatus("current")


class _FjdaryPfCmNasNFSOpCount_Type(Integer32):
    """Custom type fjdaryPfCmNasNFSOpCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_FjdaryPfCmNasNFSOpCount_Type.__name__ = "Integer32"
_FjdaryPfCmNasNFSOpCount_Object = MibTableColumn
fjdaryPfCmNasNFSOpCount = _FjdaryPfCmNasNFSOpCount_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 5, 16, 2, 1, 9),
    _FjdaryPfCmNasNFSOpCount_Type()
)
fjdaryPfCmNasNFSOpCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fjdaryPfCmNasNFSOpCount.setStatus("current")


class _FjdaryPfCmNasNtInThroughput_Type(Integer32):
    """Custom type fjdaryPfCmNasNtInThroughput based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_FjdaryPfCmNasNtInThroughput_Type.__name__ = "Integer32"
_FjdaryPfCmNasNtInThroughput_Object = MibTableColumn
fjdaryPfCmNasNtInThroughput = _FjdaryPfCmNasNtInThroughput_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 5, 16, 2, 1, 10),
    _FjdaryPfCmNasNtInThroughput_Type()
)
fjdaryPfCmNasNtInThroughput.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fjdaryPfCmNasNtInThroughput.setStatus("current")


class _FjdaryPfCmNasNtOutThroughput_Type(Integer32):
    """Custom type fjdaryPfCmNasNtOutThroughput based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_FjdaryPfCmNasNtOutThroughput_Type.__name__ = "Integer32"
_FjdaryPfCmNasNtOutThroughput_Object = MibTableColumn
fjdaryPfCmNasNtOutThroughput = _FjdaryPfCmNasNtOutThroughput_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 5, 16, 2, 1, 11),
    _FjdaryPfCmNasNtOutThroughput_Type()
)
fjdaryPfCmNasNtOutThroughput.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fjdaryPfCmNasNtOutThroughput.setStatus("current")


class _FjdaryPfCmNasCPUBusy_Type(Integer32):
    """Custom type fjdaryPfCmNasCPUBusy based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_FjdaryPfCmNasCPUBusy_Type.__name__ = "Integer32"
_FjdaryPfCmNasCPUBusy_Object = MibTableColumn
fjdaryPfCmNasCPUBusy = _FjdaryPfCmNasCPUBusy_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 5, 16, 2, 1, 12),
    _FjdaryPfCmNasCPUBusy_Type()
)
fjdaryPfCmNasCPUBusy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fjdaryPfCmNasCPUBusy.setStatus("current")


class _FjdaryPfCmNasFreeMemory_Type(Integer32):
    """Custom type fjdaryPfCmNasFreeMemory based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_FjdaryPfCmNasFreeMemory_Type.__name__ = "Integer32"
_FjdaryPfCmNasFreeMemory_Object = MibTableColumn
fjdaryPfCmNasFreeMemory = _FjdaryPfCmNasFreeMemory_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 5, 16, 2, 1, 13),
    _FjdaryPfCmNasFreeMemory_Type()
)
fjdaryPfCmNasFreeMemory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fjdaryPfCmNasFreeMemory.setStatus("current")


class _FjdaryPfCmNasCachedMemory_Type(Integer32):
    """Custom type fjdaryPfCmNasCachedMemory based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_FjdaryPfCmNasCachedMemory_Type.__name__ = "Integer32"
_FjdaryPfCmNasCachedMemory_Object = MibTableColumn
fjdaryPfCmNasCachedMemory = _FjdaryPfCmNasCachedMemory_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 5, 16, 2, 1, 14),
    _FjdaryPfCmNasCachedMemory_Type()
)
fjdaryPfCmNasCachedMemory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fjdaryPfCmNasCachedMemory.setStatus("current")


class _FjdaryPfCmNasCPUIOWait_Type(Integer32):
    """Custom type fjdaryPfCmNasCPUIOWait based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_FjdaryPfCmNasCPUIOWait_Type.__name__ = "Integer32"
_FjdaryPfCmNasCPUIOWait_Object = MibTableColumn
fjdaryPfCmNasCPUIOWait = _FjdaryPfCmNasCPUIOWait_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 5, 16, 2, 1, 15),
    _FjdaryPfCmNasCPUIOWait_Type()
)
fjdaryPfCmNasCPUIOWait.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fjdaryPfCmNasCPUIOWait.setStatus("current")
_FjdaryPfDtCmNas_ObjectIdentity = ObjectIdentity
fjdaryPfDtCmNas = _FjdaryPfDtCmNas_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 5, 17)
)


class _FjdaryPfDtCmNasCount_Type(Integer32):
    """Custom type fjdaryPfDtCmNasCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_FjdaryPfDtCmNasCount_Type.__name__ = "Integer32"
_FjdaryPfDtCmNasCount_Object = MibScalar
fjdaryPfDtCmNasCount = _FjdaryPfDtCmNasCount_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 5, 17, 1),
    _FjdaryPfDtCmNasCount_Type()
)
fjdaryPfDtCmNasCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fjdaryPfDtCmNasCount.setStatus("current")
_FjdaryPfDtCmNasTable_Object = MibTable
fjdaryPfDtCmNasTable = _FjdaryPfDtCmNasTable_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 5, 17, 2)
)
if mibBuilder.loadTexts:
    fjdaryPfDtCmNasTable.setStatus("current")
_FjdaryPfDtCmNasEntry_Object = MibTableRow
fjdaryPfDtCmNasEntry = _FjdaryPfDtCmNasEntry_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 5, 17, 2, 1)
)
fjdaryPfDtCmNasEntry.setIndexNames(
    (0, "FJDARY-E150", "fjdaryPfDtCmNasIndex"),
)
if mibBuilder.loadTexts:
    fjdaryPfDtCmNasEntry.setStatus("current")


class _FjdaryPfDtCmNasIndex_Type(Integer32):
    """Custom type fjdaryPfDtCmNasIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_FjdaryPfDtCmNasIndex_Type.__name__ = "Integer32"
_FjdaryPfDtCmNasIndex_Object = MibTableColumn
fjdaryPfDtCmNasIndex = _FjdaryPfDtCmNasIndex_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 5, 17, 2, 1, 1),
    _FjdaryPfDtCmNasIndex_Type()
)
fjdaryPfDtCmNasIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fjdaryPfDtCmNasIndex.setStatus("current")


class _FjdaryPfDtCmNasInfo_Type(OctetString):
    """Custom type fjdaryPfDtCmNasInfo based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_FjdaryPfDtCmNasInfo_Type.__name__ = "OctetString"
_FjdaryPfDtCmNasInfo_Object = MibTableColumn
fjdaryPfDtCmNasInfo = _FjdaryPfDtCmNasInfo_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 5, 17, 2, 1, 2),
    _FjdaryPfDtCmNasInfo_Type()
)
fjdaryPfDtCmNasInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fjdaryPfDtCmNasInfo.setStatus("current")
_FjdaryPfCmNasCore_ObjectIdentity = ObjectIdentity
fjdaryPfCmNasCore = _FjdaryPfCmNasCore_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 5, 18)
)


class _FjdaryPfCmNasCoreCount_Type(Integer32):
    """Custom type fjdaryPfCmNasCoreCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_FjdaryPfCmNasCoreCount_Type.__name__ = "Integer32"
_FjdaryPfCmNasCoreCount_Object = MibScalar
fjdaryPfCmNasCoreCount = _FjdaryPfCmNasCoreCount_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 5, 18, 1),
    _FjdaryPfCmNasCoreCount_Type()
)
fjdaryPfCmNasCoreCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fjdaryPfCmNasCoreCount.setStatus("current")
_FjdaryPfCmNasCoreTable_Object = MibTable
fjdaryPfCmNasCoreTable = _FjdaryPfCmNasCoreTable_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 5, 18, 2)
)
if mibBuilder.loadTexts:
    fjdaryPfCmNasCoreTable.setStatus("current")
_FjdaryPfCmNasCoreEntry_Object = MibTableRow
fjdaryPfCmNasCoreEntry = _FjdaryPfCmNasCoreEntry_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 5, 18, 2, 1)
)
fjdaryPfCmNasCoreEntry.setIndexNames(
    (0, "FJDARY-E150", "fjdaryPfCmNasCoreIndex"),
)
if mibBuilder.loadTexts:
    fjdaryPfCmNasCoreEntry.setStatus("current")


class _FjdaryPfCmNasCoreIndex_Type(Integer32):
    """Custom type fjdaryPfCmNasCoreIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_FjdaryPfCmNasCoreIndex_Type.__name__ = "Integer32"
_FjdaryPfCmNasCoreIndex_Object = MibTableColumn
fjdaryPfCmNasCoreIndex = _FjdaryPfCmNasCoreIndex_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 5, 18, 2, 1, 1),
    _FjdaryPfCmNasCoreIndex_Type()
)
fjdaryPfCmNasCoreIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fjdaryPfCmNasCoreIndex.setStatus("current")


class _FjdaryPfCmNasCoreValidCount_Type(Integer32):
    """Custom type fjdaryPfCmNasCoreValidCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_FjdaryPfCmNasCoreValidCount_Type.__name__ = "Integer32"
_FjdaryPfCmNasCoreValidCount_Object = MibTableColumn
fjdaryPfCmNasCoreValidCount = _FjdaryPfCmNasCoreValidCount_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 5, 18, 2, 1, 2),
    _FjdaryPfCmNasCoreValidCount_Type()
)
fjdaryPfCmNasCoreValidCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fjdaryPfCmNasCoreValidCount.setStatus("current")


class _FjdaryPfCmNasCoreBusy0_Type(Integer32):
    """Custom type fjdaryPfCmNasCoreBusy0 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_FjdaryPfCmNasCoreBusy0_Type.__name__ = "Integer32"
_FjdaryPfCmNasCoreBusy0_Object = MibTableColumn
fjdaryPfCmNasCoreBusy0 = _FjdaryPfCmNasCoreBusy0_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 5, 18, 2, 1, 3),
    _FjdaryPfCmNasCoreBusy0_Type()
)
fjdaryPfCmNasCoreBusy0.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fjdaryPfCmNasCoreBusy0.setStatus("current")


class _FjdaryPfCmNasCoreBusy1_Type(Integer32):
    """Custom type fjdaryPfCmNasCoreBusy1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_FjdaryPfCmNasCoreBusy1_Type.__name__ = "Integer32"
_FjdaryPfCmNasCoreBusy1_Object = MibTableColumn
fjdaryPfCmNasCoreBusy1 = _FjdaryPfCmNasCoreBusy1_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 5, 18, 2, 1, 4),
    _FjdaryPfCmNasCoreBusy1_Type()
)
fjdaryPfCmNasCoreBusy1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fjdaryPfCmNasCoreBusy1.setStatus("current")


class _FjdaryPfCmNasCoreBusy2_Type(Integer32):
    """Custom type fjdaryPfCmNasCoreBusy2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_FjdaryPfCmNasCoreBusy2_Type.__name__ = "Integer32"
_FjdaryPfCmNasCoreBusy2_Object = MibTableColumn
fjdaryPfCmNasCoreBusy2 = _FjdaryPfCmNasCoreBusy2_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 5, 18, 2, 1, 5),
    _FjdaryPfCmNasCoreBusy2_Type()
)
fjdaryPfCmNasCoreBusy2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fjdaryPfCmNasCoreBusy2.setStatus("current")


class _FjdaryPfCmNasCoreBusy3_Type(Integer32):
    """Custom type fjdaryPfCmNasCoreBusy3 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_FjdaryPfCmNasCoreBusy3_Type.__name__ = "Integer32"
_FjdaryPfCmNasCoreBusy3_Object = MibTableColumn
fjdaryPfCmNasCoreBusy3 = _FjdaryPfCmNasCoreBusy3_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 5, 18, 2, 1, 6),
    _FjdaryPfCmNasCoreBusy3_Type()
)
fjdaryPfCmNasCoreBusy3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fjdaryPfCmNasCoreBusy3.setStatus("current")


class _FjdaryPfCmNasCoreBusy4_Type(Integer32):
    """Custom type fjdaryPfCmNasCoreBusy4 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_FjdaryPfCmNasCoreBusy4_Type.__name__ = "Integer32"
_FjdaryPfCmNasCoreBusy4_Object = MibTableColumn
fjdaryPfCmNasCoreBusy4 = _FjdaryPfCmNasCoreBusy4_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 5, 18, 2, 1, 7),
    _FjdaryPfCmNasCoreBusy4_Type()
)
fjdaryPfCmNasCoreBusy4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fjdaryPfCmNasCoreBusy4.setStatus("current")


class _FjdaryPfCmNasCoreBusy5_Type(Integer32):
    """Custom type fjdaryPfCmNasCoreBusy5 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_FjdaryPfCmNasCoreBusy5_Type.__name__ = "Integer32"
_FjdaryPfCmNasCoreBusy5_Object = MibTableColumn
fjdaryPfCmNasCoreBusy5 = _FjdaryPfCmNasCoreBusy5_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 5, 18, 2, 1, 8),
    _FjdaryPfCmNasCoreBusy5_Type()
)
fjdaryPfCmNasCoreBusy5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fjdaryPfCmNasCoreBusy5.setStatus("current")


class _FjdaryPfCmNasCoreBusy6_Type(Integer32):
    """Custom type fjdaryPfCmNasCoreBusy6 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_FjdaryPfCmNasCoreBusy6_Type.__name__ = "Integer32"
_FjdaryPfCmNasCoreBusy6_Object = MibTableColumn
fjdaryPfCmNasCoreBusy6 = _FjdaryPfCmNasCoreBusy6_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 5, 18, 2, 1, 9),
    _FjdaryPfCmNasCoreBusy6_Type()
)
fjdaryPfCmNasCoreBusy6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fjdaryPfCmNasCoreBusy6.setStatus("current")


class _FjdaryPfCmNasCoreBusy7_Type(Integer32):
    """Custom type fjdaryPfCmNasCoreBusy7 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_FjdaryPfCmNasCoreBusy7_Type.__name__ = "Integer32"
_FjdaryPfCmNasCoreBusy7_Object = MibTableColumn
fjdaryPfCmNasCoreBusy7 = _FjdaryPfCmNasCoreBusy7_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 5, 18, 2, 1, 10),
    _FjdaryPfCmNasCoreBusy7_Type()
)
fjdaryPfCmNasCoreBusy7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fjdaryPfCmNasCoreBusy7.setStatus("current")


class _FjdaryPfCmNasCoreBusy8_Type(Integer32):
    """Custom type fjdaryPfCmNasCoreBusy8 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_FjdaryPfCmNasCoreBusy8_Type.__name__ = "Integer32"
_FjdaryPfCmNasCoreBusy8_Object = MibTableColumn
fjdaryPfCmNasCoreBusy8 = _FjdaryPfCmNasCoreBusy8_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 5, 18, 2, 1, 11),
    _FjdaryPfCmNasCoreBusy8_Type()
)
fjdaryPfCmNasCoreBusy8.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fjdaryPfCmNasCoreBusy8.setStatus("current")


class _FjdaryPfCmNasCoreBusy9_Type(Integer32):
    """Custom type fjdaryPfCmNasCoreBusy9 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_FjdaryPfCmNasCoreBusy9_Type.__name__ = "Integer32"
_FjdaryPfCmNasCoreBusy9_Object = MibTableColumn
fjdaryPfCmNasCoreBusy9 = _FjdaryPfCmNasCoreBusy9_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 5, 18, 2, 1, 12),
    _FjdaryPfCmNasCoreBusy9_Type()
)
fjdaryPfCmNasCoreBusy9.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fjdaryPfCmNasCoreBusy9.setStatus("current")


class _FjdaryPfCmNasCoreBusy10_Type(Integer32):
    """Custom type fjdaryPfCmNasCoreBusy10 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_FjdaryPfCmNasCoreBusy10_Type.__name__ = "Integer32"
_FjdaryPfCmNasCoreBusy10_Object = MibTableColumn
fjdaryPfCmNasCoreBusy10 = _FjdaryPfCmNasCoreBusy10_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 5, 18, 2, 1, 13),
    _FjdaryPfCmNasCoreBusy10_Type()
)
fjdaryPfCmNasCoreBusy10.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fjdaryPfCmNasCoreBusy10.setStatus("current")


class _FjdaryPfCmNasCoreBusy11_Type(Integer32):
    """Custom type fjdaryPfCmNasCoreBusy11 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_FjdaryPfCmNasCoreBusy11_Type.__name__ = "Integer32"
_FjdaryPfCmNasCoreBusy11_Object = MibTableColumn
fjdaryPfCmNasCoreBusy11 = _FjdaryPfCmNasCoreBusy11_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 5, 18, 2, 1, 14),
    _FjdaryPfCmNasCoreBusy11_Type()
)
fjdaryPfCmNasCoreBusy11.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fjdaryPfCmNasCoreBusy11.setStatus("current")


class _FjdaryPfCmNasCoreBusy12_Type(Integer32):
    """Custom type fjdaryPfCmNasCoreBusy12 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_FjdaryPfCmNasCoreBusy12_Type.__name__ = "Integer32"
_FjdaryPfCmNasCoreBusy12_Object = MibTableColumn
fjdaryPfCmNasCoreBusy12 = _FjdaryPfCmNasCoreBusy12_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 5, 18, 2, 1, 15),
    _FjdaryPfCmNasCoreBusy12_Type()
)
fjdaryPfCmNasCoreBusy12.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fjdaryPfCmNasCoreBusy12.setStatus("current")


class _FjdaryPfCmNasCoreBusy13_Type(Integer32):
    """Custom type fjdaryPfCmNasCoreBusy13 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_FjdaryPfCmNasCoreBusy13_Type.__name__ = "Integer32"
_FjdaryPfCmNasCoreBusy13_Object = MibTableColumn
fjdaryPfCmNasCoreBusy13 = _FjdaryPfCmNasCoreBusy13_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 5, 18, 2, 1, 16),
    _FjdaryPfCmNasCoreBusy13_Type()
)
fjdaryPfCmNasCoreBusy13.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fjdaryPfCmNasCoreBusy13.setStatus("current")


class _FjdaryPfCmNasCoreBusy14_Type(Integer32):
    """Custom type fjdaryPfCmNasCoreBusy14 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_FjdaryPfCmNasCoreBusy14_Type.__name__ = "Integer32"
_FjdaryPfCmNasCoreBusy14_Object = MibTableColumn
fjdaryPfCmNasCoreBusy14 = _FjdaryPfCmNasCoreBusy14_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 5, 18, 2, 1, 17),
    _FjdaryPfCmNasCoreBusy14_Type()
)
fjdaryPfCmNasCoreBusy14.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fjdaryPfCmNasCoreBusy14.setStatus("current")


class _FjdaryPfCmNasCoreBusy15_Type(Integer32):
    """Custom type fjdaryPfCmNasCoreBusy15 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_FjdaryPfCmNasCoreBusy15_Type.__name__ = "Integer32"
_FjdaryPfCmNasCoreBusy15_Object = MibTableColumn
fjdaryPfCmNasCoreBusy15 = _FjdaryPfCmNasCoreBusy15_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 5, 18, 2, 1, 18),
    _FjdaryPfCmNasCoreBusy15_Type()
)
fjdaryPfCmNasCoreBusy15.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fjdaryPfCmNasCoreBusy15.setStatus("current")


class _FjdaryPfCmNasCoreBusy16_Type(Integer32):
    """Custom type fjdaryPfCmNasCoreBusy16 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_FjdaryPfCmNasCoreBusy16_Type.__name__ = "Integer32"
_FjdaryPfCmNasCoreBusy16_Object = MibTableColumn
fjdaryPfCmNasCoreBusy16 = _FjdaryPfCmNasCoreBusy16_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 5, 18, 2, 1, 19),
    _FjdaryPfCmNasCoreBusy16_Type()
)
fjdaryPfCmNasCoreBusy16.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fjdaryPfCmNasCoreBusy16.setStatus("current")


class _FjdaryPfCmNasCoreBusy17_Type(Integer32):
    """Custom type fjdaryPfCmNasCoreBusy17 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_FjdaryPfCmNasCoreBusy17_Type.__name__ = "Integer32"
_FjdaryPfCmNasCoreBusy17_Object = MibTableColumn
fjdaryPfCmNasCoreBusy17 = _FjdaryPfCmNasCoreBusy17_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 5, 18, 2, 1, 20),
    _FjdaryPfCmNasCoreBusy17_Type()
)
fjdaryPfCmNasCoreBusy17.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fjdaryPfCmNasCoreBusy17.setStatus("current")


class _FjdaryPfCmNasCoreBusy18_Type(Integer32):
    """Custom type fjdaryPfCmNasCoreBusy18 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_FjdaryPfCmNasCoreBusy18_Type.__name__ = "Integer32"
_FjdaryPfCmNasCoreBusy18_Object = MibTableColumn
fjdaryPfCmNasCoreBusy18 = _FjdaryPfCmNasCoreBusy18_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 5, 18, 2, 1, 21),
    _FjdaryPfCmNasCoreBusy18_Type()
)
fjdaryPfCmNasCoreBusy18.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fjdaryPfCmNasCoreBusy18.setStatus("current")


class _FjdaryPfCmNasCoreBusy19_Type(Integer32):
    """Custom type fjdaryPfCmNasCoreBusy19 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_FjdaryPfCmNasCoreBusy19_Type.__name__ = "Integer32"
_FjdaryPfCmNasCoreBusy19_Object = MibTableColumn
fjdaryPfCmNasCoreBusy19 = _FjdaryPfCmNasCoreBusy19_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 5, 18, 2, 1, 22),
    _FjdaryPfCmNasCoreBusy19_Type()
)
fjdaryPfCmNasCoreBusy19.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fjdaryPfCmNasCoreBusy19.setStatus("current")
_FjdaryPfDtCmNasCore_ObjectIdentity = ObjectIdentity
fjdaryPfDtCmNasCore = _FjdaryPfDtCmNasCore_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 5, 19)
)


class _FjdaryPfDtCmNasCoreCount_Type(Integer32):
    """Custom type fjdaryPfDtCmNasCoreCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_FjdaryPfDtCmNasCoreCount_Type.__name__ = "Integer32"
_FjdaryPfDtCmNasCoreCount_Object = MibScalar
fjdaryPfDtCmNasCoreCount = _FjdaryPfDtCmNasCoreCount_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 5, 19, 1),
    _FjdaryPfDtCmNasCoreCount_Type()
)
fjdaryPfDtCmNasCoreCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fjdaryPfDtCmNasCoreCount.setStatus("current")
_FjdaryPfDtCmNasCoreTable_Object = MibTable
fjdaryPfDtCmNasCoreTable = _FjdaryPfDtCmNasCoreTable_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 5, 19, 2)
)
if mibBuilder.loadTexts:
    fjdaryPfDtCmNasCoreTable.setStatus("current")
_FjdaryPfDtCmNasCoreEntry_Object = MibTableRow
fjdaryPfDtCmNasCoreEntry = _FjdaryPfDtCmNasCoreEntry_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 5, 19, 2, 1)
)
fjdaryPfDtCmNasCoreEntry.setIndexNames(
    (0, "FJDARY-E150", "fjdaryPfDtCmNasCoreIndex"),
)
if mibBuilder.loadTexts:
    fjdaryPfDtCmNasCoreEntry.setStatus("current")


class _FjdaryPfDtCmNasCoreIndex_Type(Integer32):
    """Custom type fjdaryPfDtCmNasCoreIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_FjdaryPfDtCmNasCoreIndex_Type.__name__ = "Integer32"
_FjdaryPfDtCmNasCoreIndex_Object = MibTableColumn
fjdaryPfDtCmNasCoreIndex = _FjdaryPfDtCmNasCoreIndex_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 5, 19, 2, 1, 1),
    _FjdaryPfDtCmNasCoreIndex_Type()
)
fjdaryPfDtCmNasCoreIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fjdaryPfDtCmNasCoreIndex.setStatus("current")


class _FjdaryPfDtCmNasCoreInfo_Type(OctetString):
    """Custom type fjdaryPfDtCmNasCoreInfo based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_FjdaryPfDtCmNasCoreInfo_Type.__name__ = "OctetString"
_FjdaryPfDtCmNasCoreInfo_Object = MibTableColumn
fjdaryPfDtCmNasCoreInfo = _FjdaryPfDtCmNasCoreInfo_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 5, 19, 2, 1, 2),
    _FjdaryPfDtCmNasCoreInfo_Type()
)
fjdaryPfDtCmNasCoreInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fjdaryPfDtCmNasCoreInfo.setStatus("current")
_FjdaryPfCmNasCoreIOWait_ObjectIdentity = ObjectIdentity
fjdaryPfCmNasCoreIOWait = _FjdaryPfCmNasCoreIOWait_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 5, 20)
)


class _FjdaryPfCmNasCoreIOWaitCount_Type(Integer32):
    """Custom type fjdaryPfCmNasCoreIOWaitCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_FjdaryPfCmNasCoreIOWaitCount_Type.__name__ = "Integer32"
_FjdaryPfCmNasCoreIOWaitCount_Object = MibScalar
fjdaryPfCmNasCoreIOWaitCount = _FjdaryPfCmNasCoreIOWaitCount_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 5, 20, 1),
    _FjdaryPfCmNasCoreIOWaitCount_Type()
)
fjdaryPfCmNasCoreIOWaitCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fjdaryPfCmNasCoreIOWaitCount.setStatus("current")
_FjdaryPfCmNasCoreIOWaitTable_Object = MibTable
fjdaryPfCmNasCoreIOWaitTable = _FjdaryPfCmNasCoreIOWaitTable_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 5, 20, 2)
)
if mibBuilder.loadTexts:
    fjdaryPfCmNasCoreIOWaitTable.setStatus("current")
_FjdaryPfCmNasCoreIOWaitEntry_Object = MibTableRow
fjdaryPfCmNasCoreIOWaitEntry = _FjdaryPfCmNasCoreIOWaitEntry_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 5, 20, 2, 1)
)
fjdaryPfCmNasCoreIOWaitEntry.setIndexNames(
    (0, "FJDARY-E150", "fjdaryPfCmNasCoreIOWaitIndex"),
)
if mibBuilder.loadTexts:
    fjdaryPfCmNasCoreIOWaitEntry.setStatus("current")


class _FjdaryPfCmNasCoreIOWaitIndex_Type(Integer32):
    """Custom type fjdaryPfCmNasCoreIOWaitIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_FjdaryPfCmNasCoreIOWaitIndex_Type.__name__ = "Integer32"
_FjdaryPfCmNasCoreIOWaitIndex_Object = MibTableColumn
fjdaryPfCmNasCoreIOWaitIndex = _FjdaryPfCmNasCoreIOWaitIndex_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 5, 20, 2, 1, 1),
    _FjdaryPfCmNasCoreIOWaitIndex_Type()
)
fjdaryPfCmNasCoreIOWaitIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fjdaryPfCmNasCoreIOWaitIndex.setStatus("current")


class _FjdaryPfCmNasCoreIOWaitValidCount_Type(Integer32):
    """Custom type fjdaryPfCmNasCoreIOWaitValidCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_FjdaryPfCmNasCoreIOWaitValidCount_Type.__name__ = "Integer32"
_FjdaryPfCmNasCoreIOWaitValidCount_Object = MibTableColumn
fjdaryPfCmNasCoreIOWaitValidCount = _FjdaryPfCmNasCoreIOWaitValidCount_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 5, 20, 2, 1, 2),
    _FjdaryPfCmNasCoreIOWaitValidCount_Type()
)
fjdaryPfCmNasCoreIOWaitValidCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fjdaryPfCmNasCoreIOWaitValidCount.setStatus("current")


class _FjdaryPfCmNasCoreIOWait0_Type(Integer32):
    """Custom type fjdaryPfCmNasCoreIOWait0 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_FjdaryPfCmNasCoreIOWait0_Type.__name__ = "Integer32"
_FjdaryPfCmNasCoreIOWait0_Object = MibTableColumn
fjdaryPfCmNasCoreIOWait0 = _FjdaryPfCmNasCoreIOWait0_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 5, 20, 2, 1, 3),
    _FjdaryPfCmNasCoreIOWait0_Type()
)
fjdaryPfCmNasCoreIOWait0.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fjdaryPfCmNasCoreIOWait0.setStatus("current")


class _FjdaryPfCmNasCoreIOWait1_Type(Integer32):
    """Custom type fjdaryPfCmNasCoreIOWait1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_FjdaryPfCmNasCoreIOWait1_Type.__name__ = "Integer32"
_FjdaryPfCmNasCoreIOWait1_Object = MibTableColumn
fjdaryPfCmNasCoreIOWait1 = _FjdaryPfCmNasCoreIOWait1_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 5, 20, 2, 1, 4),
    _FjdaryPfCmNasCoreIOWait1_Type()
)
fjdaryPfCmNasCoreIOWait1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fjdaryPfCmNasCoreIOWait1.setStatus("current")


class _FjdaryPfCmNasCoreIOWait2_Type(Integer32):
    """Custom type fjdaryPfCmNasCoreIOWait2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_FjdaryPfCmNasCoreIOWait2_Type.__name__ = "Integer32"
_FjdaryPfCmNasCoreIOWait2_Object = MibTableColumn
fjdaryPfCmNasCoreIOWait2 = _FjdaryPfCmNasCoreIOWait2_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 5, 20, 2, 1, 5),
    _FjdaryPfCmNasCoreIOWait2_Type()
)
fjdaryPfCmNasCoreIOWait2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fjdaryPfCmNasCoreIOWait2.setStatus("current")


class _FjdaryPfCmNasCoreIOWait3_Type(Integer32):
    """Custom type fjdaryPfCmNasCoreIOWait3 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_FjdaryPfCmNasCoreIOWait3_Type.__name__ = "Integer32"
_FjdaryPfCmNasCoreIOWait3_Object = MibTableColumn
fjdaryPfCmNasCoreIOWait3 = _FjdaryPfCmNasCoreIOWait3_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 5, 20, 2, 1, 6),
    _FjdaryPfCmNasCoreIOWait3_Type()
)
fjdaryPfCmNasCoreIOWait3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fjdaryPfCmNasCoreIOWait3.setStatus("current")


class _FjdaryPfCmNasCoreIOWait4_Type(Integer32):
    """Custom type fjdaryPfCmNasCoreIOWait4 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_FjdaryPfCmNasCoreIOWait4_Type.__name__ = "Integer32"
_FjdaryPfCmNasCoreIOWait4_Object = MibTableColumn
fjdaryPfCmNasCoreIOWait4 = _FjdaryPfCmNasCoreIOWait4_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 5, 20, 2, 1, 7),
    _FjdaryPfCmNasCoreIOWait4_Type()
)
fjdaryPfCmNasCoreIOWait4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fjdaryPfCmNasCoreIOWait4.setStatus("current")


class _FjdaryPfCmNasCoreIOWait5_Type(Integer32):
    """Custom type fjdaryPfCmNasCoreIOWait5 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_FjdaryPfCmNasCoreIOWait5_Type.__name__ = "Integer32"
_FjdaryPfCmNasCoreIOWait5_Object = MibTableColumn
fjdaryPfCmNasCoreIOWait5 = _FjdaryPfCmNasCoreIOWait5_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 5, 20, 2, 1, 8),
    _FjdaryPfCmNasCoreIOWait5_Type()
)
fjdaryPfCmNasCoreIOWait5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fjdaryPfCmNasCoreIOWait5.setStatus("current")


class _FjdaryPfCmNasCoreIOWait6_Type(Integer32):
    """Custom type fjdaryPfCmNasCoreIOWait6 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_FjdaryPfCmNasCoreIOWait6_Type.__name__ = "Integer32"
_FjdaryPfCmNasCoreIOWait6_Object = MibTableColumn
fjdaryPfCmNasCoreIOWait6 = _FjdaryPfCmNasCoreIOWait6_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 5, 20, 2, 1, 9),
    _FjdaryPfCmNasCoreIOWait6_Type()
)
fjdaryPfCmNasCoreIOWait6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fjdaryPfCmNasCoreIOWait6.setStatus("current")


class _FjdaryPfCmNasCoreIOWait7_Type(Integer32):
    """Custom type fjdaryPfCmNasCoreIOWait7 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_FjdaryPfCmNasCoreIOWait7_Type.__name__ = "Integer32"
_FjdaryPfCmNasCoreIOWait7_Object = MibTableColumn
fjdaryPfCmNasCoreIOWait7 = _FjdaryPfCmNasCoreIOWait7_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 5, 20, 2, 1, 10),
    _FjdaryPfCmNasCoreIOWait7_Type()
)
fjdaryPfCmNasCoreIOWait7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fjdaryPfCmNasCoreIOWait7.setStatus("current")


class _FjdaryPfCmNasCoreIOWait8_Type(Integer32):
    """Custom type fjdaryPfCmNasCoreIOWait8 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_FjdaryPfCmNasCoreIOWait8_Type.__name__ = "Integer32"
_FjdaryPfCmNasCoreIOWait8_Object = MibTableColumn
fjdaryPfCmNasCoreIOWait8 = _FjdaryPfCmNasCoreIOWait8_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 5, 20, 2, 1, 11),
    _FjdaryPfCmNasCoreIOWait8_Type()
)
fjdaryPfCmNasCoreIOWait8.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fjdaryPfCmNasCoreIOWait8.setStatus("current")


class _FjdaryPfCmNasCoreIOWait9_Type(Integer32):
    """Custom type fjdaryPfCmNasCoreIOWait9 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_FjdaryPfCmNasCoreIOWait9_Type.__name__ = "Integer32"
_FjdaryPfCmNasCoreIOWait9_Object = MibTableColumn
fjdaryPfCmNasCoreIOWait9 = _FjdaryPfCmNasCoreIOWait9_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 5, 20, 2, 1, 12),
    _FjdaryPfCmNasCoreIOWait9_Type()
)
fjdaryPfCmNasCoreIOWait9.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fjdaryPfCmNasCoreIOWait9.setStatus("current")


class _FjdaryPfCmNasCoreIOWait10_Type(Integer32):
    """Custom type fjdaryPfCmNasCoreIOWait10 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_FjdaryPfCmNasCoreIOWait10_Type.__name__ = "Integer32"
_FjdaryPfCmNasCoreIOWait10_Object = MibTableColumn
fjdaryPfCmNasCoreIOWait10 = _FjdaryPfCmNasCoreIOWait10_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 5, 20, 2, 1, 13),
    _FjdaryPfCmNasCoreIOWait10_Type()
)
fjdaryPfCmNasCoreIOWait10.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fjdaryPfCmNasCoreIOWait10.setStatus("current")


class _FjdaryPfCmNasCoreIOWait11_Type(Integer32):
    """Custom type fjdaryPfCmNasCoreIOWait11 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_FjdaryPfCmNasCoreIOWait11_Type.__name__ = "Integer32"
_FjdaryPfCmNasCoreIOWait11_Object = MibTableColumn
fjdaryPfCmNasCoreIOWait11 = _FjdaryPfCmNasCoreIOWait11_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 5, 20, 2, 1, 14),
    _FjdaryPfCmNasCoreIOWait11_Type()
)
fjdaryPfCmNasCoreIOWait11.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fjdaryPfCmNasCoreIOWait11.setStatus("current")


class _FjdaryPfCmNasCoreIOWait12_Type(Integer32):
    """Custom type fjdaryPfCmNasCoreIOWait12 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_FjdaryPfCmNasCoreIOWait12_Type.__name__ = "Integer32"
_FjdaryPfCmNasCoreIOWait12_Object = MibTableColumn
fjdaryPfCmNasCoreIOWait12 = _FjdaryPfCmNasCoreIOWait12_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 5, 20, 2, 1, 15),
    _FjdaryPfCmNasCoreIOWait12_Type()
)
fjdaryPfCmNasCoreIOWait12.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fjdaryPfCmNasCoreIOWait12.setStatus("current")


class _FjdaryPfCmNasCoreIOWait13_Type(Integer32):
    """Custom type fjdaryPfCmNasCoreIOWait13 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_FjdaryPfCmNasCoreIOWait13_Type.__name__ = "Integer32"
_FjdaryPfCmNasCoreIOWait13_Object = MibTableColumn
fjdaryPfCmNasCoreIOWait13 = _FjdaryPfCmNasCoreIOWait13_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 5, 20, 2, 1, 16),
    _FjdaryPfCmNasCoreIOWait13_Type()
)
fjdaryPfCmNasCoreIOWait13.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fjdaryPfCmNasCoreIOWait13.setStatus("current")


class _FjdaryPfCmNasCoreIOWait14_Type(Integer32):
    """Custom type fjdaryPfCmNasCoreIOWait14 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_FjdaryPfCmNasCoreIOWait14_Type.__name__ = "Integer32"
_FjdaryPfCmNasCoreIOWait14_Object = MibTableColumn
fjdaryPfCmNasCoreIOWait14 = _FjdaryPfCmNasCoreIOWait14_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 5, 20, 2, 1, 17),
    _FjdaryPfCmNasCoreIOWait14_Type()
)
fjdaryPfCmNasCoreIOWait14.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fjdaryPfCmNasCoreIOWait14.setStatus("current")


class _FjdaryPfCmNasCoreIOWait15_Type(Integer32):
    """Custom type fjdaryPfCmNasCoreIOWait15 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_FjdaryPfCmNasCoreIOWait15_Type.__name__ = "Integer32"
_FjdaryPfCmNasCoreIOWait15_Object = MibTableColumn
fjdaryPfCmNasCoreIOWait15 = _FjdaryPfCmNasCoreIOWait15_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 5, 20, 2, 1, 18),
    _FjdaryPfCmNasCoreIOWait15_Type()
)
fjdaryPfCmNasCoreIOWait15.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fjdaryPfCmNasCoreIOWait15.setStatus("current")


class _FjdaryPfCmNasCoreIOWait16_Type(Integer32):
    """Custom type fjdaryPfCmNasCoreIOWait16 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_FjdaryPfCmNasCoreIOWait16_Type.__name__ = "Integer32"
_FjdaryPfCmNasCoreIOWait16_Object = MibTableColumn
fjdaryPfCmNasCoreIOWait16 = _FjdaryPfCmNasCoreIOWait16_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 5, 20, 2, 1, 19),
    _FjdaryPfCmNasCoreIOWait16_Type()
)
fjdaryPfCmNasCoreIOWait16.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fjdaryPfCmNasCoreIOWait16.setStatus("current")


class _FjdaryPfCmNasCoreIOWait17_Type(Integer32):
    """Custom type fjdaryPfCmNasCoreIOWait17 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_FjdaryPfCmNasCoreIOWait17_Type.__name__ = "Integer32"
_FjdaryPfCmNasCoreIOWait17_Object = MibTableColumn
fjdaryPfCmNasCoreIOWait17 = _FjdaryPfCmNasCoreIOWait17_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 5, 20, 2, 1, 20),
    _FjdaryPfCmNasCoreIOWait17_Type()
)
fjdaryPfCmNasCoreIOWait17.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fjdaryPfCmNasCoreIOWait17.setStatus("current")


class _FjdaryPfCmNasCoreIOWait18_Type(Integer32):
    """Custom type fjdaryPfCmNasCoreIOWait18 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_FjdaryPfCmNasCoreIOWait18_Type.__name__ = "Integer32"
_FjdaryPfCmNasCoreIOWait18_Object = MibTableColumn
fjdaryPfCmNasCoreIOWait18 = _FjdaryPfCmNasCoreIOWait18_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 5, 20, 2, 1, 21),
    _FjdaryPfCmNasCoreIOWait18_Type()
)
fjdaryPfCmNasCoreIOWait18.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fjdaryPfCmNasCoreIOWait18.setStatus("current")


class _FjdaryPfCmNasCoreIOWait19_Type(Integer32):
    """Custom type fjdaryPfCmNasCoreIOWait19 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_FjdaryPfCmNasCoreIOWait19_Type.__name__ = "Integer32"
_FjdaryPfCmNasCoreIOWait19_Object = MibTableColumn
fjdaryPfCmNasCoreIOWait19 = _FjdaryPfCmNasCoreIOWait19_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 5, 20, 2, 1, 22),
    _FjdaryPfCmNasCoreIOWait19_Type()
)
fjdaryPfCmNasCoreIOWait19.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fjdaryPfCmNasCoreIOWait19.setStatus("current")
_FjdaryPfDtCmNasCoreIOWait_ObjectIdentity = ObjectIdentity
fjdaryPfDtCmNasCoreIOWait = _FjdaryPfDtCmNasCoreIOWait_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 5, 21)
)


class _FjdaryPfDtCmNasCoreIOWaitCount_Type(Integer32):
    """Custom type fjdaryPfDtCmNasCoreIOWaitCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_FjdaryPfDtCmNasCoreIOWaitCount_Type.__name__ = "Integer32"
_FjdaryPfDtCmNasCoreIOWaitCount_Object = MibScalar
fjdaryPfDtCmNasCoreIOWaitCount = _FjdaryPfDtCmNasCoreIOWaitCount_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 5, 21, 1),
    _FjdaryPfDtCmNasCoreIOWaitCount_Type()
)
fjdaryPfDtCmNasCoreIOWaitCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fjdaryPfDtCmNasCoreIOWaitCount.setStatus("current")
_FjdaryPfDtCmNasCoreIOWaitTable_Object = MibTable
fjdaryPfDtCmNasCoreIOWaitTable = _FjdaryPfDtCmNasCoreIOWaitTable_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 5, 21, 2)
)
if mibBuilder.loadTexts:
    fjdaryPfDtCmNasCoreIOWaitTable.setStatus("current")
_FjdaryPfDtCmNasCoreIOWaitEntry_Object = MibTableRow
fjdaryPfDtCmNasCoreIOWaitEntry = _FjdaryPfDtCmNasCoreIOWaitEntry_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 5, 21, 2, 1)
)
fjdaryPfDtCmNasCoreIOWaitEntry.setIndexNames(
    (0, "FJDARY-E150", "fjdaryPfDtCmNasCoreIOWaitIndex"),
)
if mibBuilder.loadTexts:
    fjdaryPfDtCmNasCoreIOWaitEntry.setStatus("current")


class _FjdaryPfDtCmNasCoreIOWaitIndex_Type(Integer32):
    """Custom type fjdaryPfDtCmNasCoreIOWaitIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_FjdaryPfDtCmNasCoreIOWaitIndex_Type.__name__ = "Integer32"
_FjdaryPfDtCmNasCoreIOWaitIndex_Object = MibTableColumn
fjdaryPfDtCmNasCoreIOWaitIndex = _FjdaryPfDtCmNasCoreIOWaitIndex_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 5, 21, 2, 1, 1),
    _FjdaryPfDtCmNasCoreIOWaitIndex_Type()
)
fjdaryPfDtCmNasCoreIOWaitIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fjdaryPfDtCmNasCoreIOWaitIndex.setStatus("current")


class _FjdaryPfDtCmNasCoreIOWaitInfo_Type(OctetString):
    """Custom type fjdaryPfDtCmNasCoreIOWaitInfo based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_FjdaryPfDtCmNasCoreIOWaitInfo_Type.__name__ = "OctetString"
_FjdaryPfDtCmNasCoreIOWaitInfo_Object = MibTableColumn
fjdaryPfDtCmNasCoreIOWaitInfo = _FjdaryPfDtCmNasCoreIOWaitInfo_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 5, 21, 2, 1, 2),
    _FjdaryPfDtCmNasCoreIOWaitInfo_Type()
)
fjdaryPfDtCmNasCoreIOWaitInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fjdaryPfDtCmNasCoreIOWaitInfo.setStatus("current")
_FjdaryPfCaPortNas_ObjectIdentity = ObjectIdentity
fjdaryPfCaPortNas = _FjdaryPfCaPortNas_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 5, 22)
)


class _FjdaryPfCaPortNasCount_Type(Integer32):
    """Custom type fjdaryPfCaPortNasCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_FjdaryPfCaPortNasCount_Type.__name__ = "Integer32"
_FjdaryPfCaPortNasCount_Object = MibScalar
fjdaryPfCaPortNasCount = _FjdaryPfCaPortNasCount_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 5, 22, 1),
    _FjdaryPfCaPortNasCount_Type()
)
fjdaryPfCaPortNasCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fjdaryPfCaPortNasCount.setStatus("current")
_FjdaryPfCaPortNasTable_Object = MibTable
fjdaryPfCaPortNasTable = _FjdaryPfCaPortNasTable_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 5, 22, 2)
)
if mibBuilder.loadTexts:
    fjdaryPfCaPortNasTable.setStatus("current")
_FjdaryPfCaPortNasEntry_Object = MibTableRow
fjdaryPfCaPortNasEntry = _FjdaryPfCaPortNasEntry_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 5, 22, 2, 1)
)
fjdaryPfCaPortNasEntry.setIndexNames(
    (0, "FJDARY-E150", "fjdaryPfCaPortNasIndex"),
)
if mibBuilder.loadTexts:
    fjdaryPfCaPortNasEntry.setStatus("current")


class _FjdaryPfCaPortNasIndex_Type(Integer32):
    """Custom type fjdaryPfCaPortNasIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_FjdaryPfCaPortNasIndex_Type.__name__ = "Integer32"
_FjdaryPfCaPortNasIndex_Object = MibTableColumn
fjdaryPfCaPortNasIndex = _FjdaryPfCaPortNasIndex_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 5, 22, 2, 1, 1),
    _FjdaryPfCaPortNasIndex_Type()
)
fjdaryPfCaPortNasIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fjdaryPfCaPortNasIndex.setStatus("current")


class _FjdaryPfCaPortNasNtInThroughput_Type(Integer32):
    """Custom type fjdaryPfCaPortNasNtInThroughput based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_FjdaryPfCaPortNasNtInThroughput_Type.__name__ = "Integer32"
_FjdaryPfCaPortNasNtInThroughput_Object = MibTableColumn
fjdaryPfCaPortNasNtInThroughput = _FjdaryPfCaPortNasNtInThroughput_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 5, 22, 2, 1, 2),
    _FjdaryPfCaPortNasNtInThroughput_Type()
)
fjdaryPfCaPortNasNtInThroughput.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fjdaryPfCaPortNasNtInThroughput.setStatus("current")


class _FjdaryPfCaPortNasNtOutThroughput_Type(Integer32):
    """Custom type fjdaryPfCaPortNasNtOutThroughput based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_FjdaryPfCaPortNasNtOutThroughput_Type.__name__ = "Integer32"
_FjdaryPfCaPortNasNtOutThroughput_Object = MibTableColumn
fjdaryPfCaPortNasNtOutThroughput = _FjdaryPfCaPortNasNtOutThroughput_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 5, 22, 2, 1, 3),
    _FjdaryPfCaPortNasNtOutThroughput_Type()
)
fjdaryPfCaPortNasNtOutThroughput.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fjdaryPfCaPortNasNtOutThroughput.setStatus("current")
_FjdaryPfDtCaPortNas_ObjectIdentity = ObjectIdentity
fjdaryPfDtCaPortNas = _FjdaryPfDtCaPortNas_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 5, 23)
)


class _FjdaryPfDtCaPortNasCount_Type(Integer32):
    """Custom type fjdaryPfDtCaPortNasCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_FjdaryPfDtCaPortNasCount_Type.__name__ = "Integer32"
_FjdaryPfDtCaPortNasCount_Object = MibScalar
fjdaryPfDtCaPortNasCount = _FjdaryPfDtCaPortNasCount_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 5, 23, 1),
    _FjdaryPfDtCaPortNasCount_Type()
)
fjdaryPfDtCaPortNasCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fjdaryPfDtCaPortNasCount.setStatus("current")
_FjdaryPfDtCaPortNasTable_Object = MibTable
fjdaryPfDtCaPortNasTable = _FjdaryPfDtCaPortNasTable_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 5, 23, 2)
)
if mibBuilder.loadTexts:
    fjdaryPfDtCaPortNasTable.setStatus("current")
_FjdaryPfDtCaPortNasEntry_Object = MibTableRow
fjdaryPfDtCaPortNasEntry = _FjdaryPfDtCaPortNasEntry_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 5, 23, 2, 1)
)
fjdaryPfDtCaPortNasEntry.setIndexNames(
    (0, "FJDARY-E150", "fjdaryPfDtCaPortNasIndex"),
)
if mibBuilder.loadTexts:
    fjdaryPfDtCaPortNasEntry.setStatus("current")


class _FjdaryPfDtCaPortNasIndex_Type(Integer32):
    """Custom type fjdaryPfDtCaPortNasIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_FjdaryPfDtCaPortNasIndex_Type.__name__ = "Integer32"
_FjdaryPfDtCaPortNasIndex_Object = MibTableColumn
fjdaryPfDtCaPortNasIndex = _FjdaryPfDtCaPortNasIndex_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 5, 23, 2, 1, 1),
    _FjdaryPfDtCaPortNasIndex_Type()
)
fjdaryPfDtCaPortNasIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fjdaryPfDtCaPortNasIndex.setStatus("current")


class _FjdaryPfDtCaPortNasInfo_Type(OctetString):
    """Custom type fjdaryPfDtCaPortNasInfo based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_FjdaryPfDtCaPortNasInfo_Type.__name__ = "OctetString"
_FjdaryPfDtCaPortNasInfo_Object = MibTableColumn
fjdaryPfDtCaPortNasInfo = _FjdaryPfDtCaPortNasInfo_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 5, 23, 2, 1, 2),
    _FjdaryPfDtCaPortNasInfo_Type()
)
fjdaryPfDtCaPortNasInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fjdaryPfDtCaPortNasInfo.setStatus("current")
_FjdaryPfCmNasVol_ObjectIdentity = ObjectIdentity
fjdaryPfCmNasVol = _FjdaryPfCmNasVol_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 5, 24)
)


class _FjdaryPfCmNasVolCount_Type(Integer32):
    """Custom type fjdaryPfCmNasVolCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_FjdaryPfCmNasVolCount_Type.__name__ = "Integer32"
_FjdaryPfCmNasVolCount_Object = MibScalar
fjdaryPfCmNasVolCount = _FjdaryPfCmNasVolCount_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 5, 24, 1),
    _FjdaryPfCmNasVolCount_Type()
)
fjdaryPfCmNasVolCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fjdaryPfCmNasVolCount.setStatus("current")
_FjdaryPfCmNasVolTable_Object = MibTable
fjdaryPfCmNasVolTable = _FjdaryPfCmNasVolTable_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 5, 24, 2)
)
if mibBuilder.loadTexts:
    fjdaryPfCmNasVolTable.setStatus("current")
_FjdaryPfCmNasVolEntry_Object = MibTableRow
fjdaryPfCmNasVolEntry = _FjdaryPfCmNasVolEntry_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 5, 24, 2, 1)
)
fjdaryPfCmNasVolEntry.setIndexNames(
    (0, "FJDARY-E150", "fjdaryPfCmNasVolIndex"),
)
if mibBuilder.loadTexts:
    fjdaryPfCmNasVolEntry.setStatus("current")


class _FjdaryPfCmNasVolIndex_Type(Integer32):
    """Custom type fjdaryPfCmNasVolIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_FjdaryPfCmNasVolIndex_Type.__name__ = "Integer32"
_FjdaryPfCmNasVolIndex_Object = MibTableColumn
fjdaryPfCmNasVolIndex = _FjdaryPfCmNasVolIndex_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 5, 24, 2, 1, 1),
    _FjdaryPfCmNasVolIndex_Type()
)
fjdaryPfCmNasVolIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fjdaryPfCmNasVolIndex.setStatus("current")


class _FjdaryPfCmNasVolOluNo_Type(Integer32):
    """Custom type fjdaryPfCmNasVolOluNo based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_FjdaryPfCmNasVolOluNo_Type.__name__ = "Integer32"
_FjdaryPfCmNasVolOluNo_Object = MibTableColumn
fjdaryPfCmNasVolOluNo = _FjdaryPfCmNasVolOluNo_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 5, 24, 2, 1, 2),
    _FjdaryPfCmNasVolOluNo_Type()
)
fjdaryPfCmNasVolOluNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fjdaryPfCmNasVolOluNo.setStatus("current")


class _FjdaryPfCmNasVolIOWaitTime_Type(Integer32):
    """Custom type fjdaryPfCmNasVolIOWaitTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_FjdaryPfCmNasVolIOWaitTime_Type.__name__ = "Integer32"
_FjdaryPfCmNasVolIOWaitTime_Object = MibTableColumn
fjdaryPfCmNasVolIOWaitTime = _FjdaryPfCmNasVolIOWaitTime_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 5, 24, 2, 1, 3),
    _FjdaryPfCmNasVolIOWaitTime_Type()
)
fjdaryPfCmNasVolIOWaitTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fjdaryPfCmNasVolIOWaitTime.setStatus("current")


class _FjdaryPfCmNasVolRdTp_Type(Integer32):
    """Custom type fjdaryPfCmNasVolRdTp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_FjdaryPfCmNasVolRdTp_Type.__name__ = "Integer32"
_FjdaryPfCmNasVolRdTp_Object = MibTableColumn
fjdaryPfCmNasVolRdTp = _FjdaryPfCmNasVolRdTp_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 5, 24, 2, 1, 4),
    _FjdaryPfCmNasVolRdTp_Type()
)
fjdaryPfCmNasVolRdTp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fjdaryPfCmNasVolRdTp.setStatus("current")


class _FjdaryPfCmNasVolWtTp_Type(Integer32):
    """Custom type fjdaryPfCmNasVolWtTp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_FjdaryPfCmNasVolWtTp_Type.__name__ = "Integer32"
_FjdaryPfCmNasVolWtTp_Object = MibTableColumn
fjdaryPfCmNasVolWtTp = _FjdaryPfCmNasVolWtTp_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 5, 24, 2, 1, 5),
    _FjdaryPfCmNasVolWtTp_Type()
)
fjdaryPfCmNasVolWtTp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fjdaryPfCmNasVolWtTp.setStatus("current")


class _FjdaryPfCmNasVolIOCPUBusy_Type(Integer32):
    """Custom type fjdaryPfCmNasVolIOCPUBusy based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_FjdaryPfCmNasVolIOCPUBusy_Type.__name__ = "Integer32"
_FjdaryPfCmNasVolIOCPUBusy_Object = MibTableColumn
fjdaryPfCmNasVolIOCPUBusy = _FjdaryPfCmNasVolIOCPUBusy_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 5, 24, 2, 1, 6),
    _FjdaryPfCmNasVolIOCPUBusy_Type()
)
fjdaryPfCmNasVolIOCPUBusy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fjdaryPfCmNasVolIOCPUBusy.setStatus("current")


class _FjdaryPfCmNasVolUsageRate_Type(Integer32):
    """Custom type fjdaryPfCmNasVolUsageRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_FjdaryPfCmNasVolUsageRate_Type.__name__ = "Integer32"
_FjdaryPfCmNasVolUsageRate_Object = MibTableColumn
fjdaryPfCmNasVolUsageRate = _FjdaryPfCmNasVolUsageRate_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 5, 24, 2, 1, 7),
    _FjdaryPfCmNasVolUsageRate_Type()
)
fjdaryPfCmNasVolUsageRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fjdaryPfCmNasVolUsageRate.setStatus("current")


class _FjdaryPfCmNasVolUsedAmount_Type(Integer32):
    """Custom type fjdaryPfCmNasVolUsedAmount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_FjdaryPfCmNasVolUsedAmount_Type.__name__ = "Integer32"
_FjdaryPfCmNasVolUsedAmount_Object = MibTableColumn
fjdaryPfCmNasVolUsedAmount = _FjdaryPfCmNasVolUsedAmount_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 5, 24, 2, 1, 8),
    _FjdaryPfCmNasVolUsedAmount_Type()
)
fjdaryPfCmNasVolUsedAmount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fjdaryPfCmNasVolUsedAmount.setStatus("current")
_FjdaryPfDtCmNasVol_ObjectIdentity = ObjectIdentity
fjdaryPfDtCmNasVol = _FjdaryPfDtCmNasVol_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 5, 25)
)


class _FjdaryPfDtCmNasVolCount_Type(Integer32):
    """Custom type fjdaryPfDtCmNasVolCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_FjdaryPfDtCmNasVolCount_Type.__name__ = "Integer32"
_FjdaryPfDtCmNasVolCount_Object = MibScalar
fjdaryPfDtCmNasVolCount = _FjdaryPfDtCmNasVolCount_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 5, 25, 1),
    _FjdaryPfDtCmNasVolCount_Type()
)
fjdaryPfDtCmNasVolCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fjdaryPfDtCmNasVolCount.setStatus("current")
_FjdaryPfDtCmNasVolTable_Object = MibTable
fjdaryPfDtCmNasVolTable = _FjdaryPfDtCmNasVolTable_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 5, 25, 2)
)
if mibBuilder.loadTexts:
    fjdaryPfDtCmNasVolTable.setStatus("current")
_FjdaryPfDtCmNasVolEntry_Object = MibTableRow
fjdaryPfDtCmNasVolEntry = _FjdaryPfDtCmNasVolEntry_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 5, 25, 2, 1)
)
fjdaryPfDtCmNasVolEntry.setIndexNames(
    (0, "FJDARY-E150", "fjdaryPfDtCmNasVolIndex"),
)
if mibBuilder.loadTexts:
    fjdaryPfDtCmNasVolEntry.setStatus("current")


class _FjdaryPfDtCmNasVolIndex_Type(Integer32):
    """Custom type fjdaryPfDtCmNasVolIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_FjdaryPfDtCmNasVolIndex_Type.__name__ = "Integer32"
_FjdaryPfDtCmNasVolIndex_Object = MibTableColumn
fjdaryPfDtCmNasVolIndex = _FjdaryPfDtCmNasVolIndex_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 5, 25, 2, 1, 1),
    _FjdaryPfDtCmNasVolIndex_Type()
)
fjdaryPfDtCmNasVolIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fjdaryPfDtCmNasVolIndex.setStatus("current")


class _FjdaryPfDtCmNasVolInfo_Type(OctetString):
    """Custom type fjdaryPfDtCmNasVolInfo based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_FjdaryPfDtCmNasVolInfo_Type.__name__ = "OctetString"
_FjdaryPfDtCmNasVolInfo_Object = MibTableColumn
fjdaryPfDtCmNasVolInfo = _FjdaryPfDtCmNasVolInfo_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 5, 25, 2, 1, 2),
    _FjdaryPfDtCmNasVolInfo_Type()
)
fjdaryPfDtCmNasVolInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fjdaryPfDtCmNasVolInfo.setStatus("current")


class _FjdaryUnitStatus_Type(Integer32):
    """Custom type fjdaryUnitStatus based on Integer32"""
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
        *(("failed", 5),
          ("ok", 3),
          ("unknown", 1),
          ("unused", 2),
          ("warning", 4))
    )


_FjdaryUnitStatus_Type.__name__ = "Integer32"
_FjdaryUnitStatus_Object = MibScalar
fjdaryUnitStatus = _FjdaryUnitStatus_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 6),
    _FjdaryUnitStatus_Type()
)
fjdaryUnitStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fjdaryUnitStatus.setStatus("current")


class _FjdaryTrapItemId_Type(Integer32):
    """Custom type fjdaryTrapItemId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_FjdaryTrapItemId_Type.__name__ = "Integer32"
_FjdaryTrapItemId_Object = MibScalar
fjdaryTrapItemId = _FjdaryTrapItemId_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 7),
    _FjdaryTrapItemId_Type()
)
fjdaryTrapItemId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fjdaryTrapItemId.setStatus("current")


class _FjdaryTrapSensorInfo_Type(Integer32):
    """Custom type fjdaryTrapSensorInfo based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_FjdaryTrapSensorInfo_Type.__name__ = "Integer32"
_FjdaryTrapSensorInfo_Object = MibScalar
fjdaryTrapSensorInfo = _FjdaryTrapSensorInfo_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 8),
    _FjdaryTrapSensorInfo_Type()
)
fjdaryTrapSensorInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fjdaryTrapSensorInfo.setStatus("current")


class _FjdaryTrapMaintenanceInfo_Type(Integer32):
    """Custom type fjdaryTrapMaintenanceInfo based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_FjdaryTrapMaintenanceInfo_Type.__name__ = "Integer32"
_FjdaryTrapMaintenanceInfo_Object = MibScalar
fjdaryTrapMaintenanceInfo = _FjdaryTrapMaintenanceInfo_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 9),
    _FjdaryTrapMaintenanceInfo_Type()
)
fjdaryTrapMaintenanceInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fjdaryTrapMaintenanceInfo.setStatus("current")


class _FjdaryTrapWarningInfo_Type(Integer32):
    """Custom type fjdaryTrapWarningInfo based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_FjdaryTrapWarningInfo_Type.__name__ = "Integer32"
_FjdaryTrapWarningInfo_Object = MibScalar
fjdaryTrapWarningInfo = _FjdaryTrapWarningInfo_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 10),
    _FjdaryTrapWarningInfo_Type()
)
fjdaryTrapWarningInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fjdaryTrapWarningInfo.setStatus("current")
_FjdaryTrapMessage_Type = DisplayString
_FjdaryTrapMessage_Object = MibScalar
fjdaryTrapMessage = _FjdaryTrapMessage_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 11),
    _FjdaryTrapMessage_Type()
)
fjdaryTrapMessage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fjdaryTrapMessage.setStatus("current")
_FjdaryMIBversion_Type = DisplayString
_FjdaryMIBversion_Object = MibScalar
fjdaryMIBversion = _FjdaryMIBversion_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 12),
    _FjdaryMIBversion_Type()
)
fjdaryMIBversion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fjdaryMIBversion.setStatus("current")
_FjdarySensor_ObjectIdentity = ObjectIdentity
fjdarySensor = _FjdarySensor_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 13)
)
_FjdaryMachinePower_ObjectIdentity = ObjectIdentity
fjdaryMachinePower = _FjdaryMachinePower_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 13, 1)
)


class _FjdaryMachinePowerCount_Type(Integer32):
    """Custom type fjdaryMachinePowerCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_FjdaryMachinePowerCount_Type.__name__ = "Integer32"
_FjdaryMachinePowerCount_Object = MibScalar
fjdaryMachinePowerCount = _FjdaryMachinePowerCount_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 13, 1, 1),
    _FjdaryMachinePowerCount_Type()
)
fjdaryMachinePowerCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fjdaryMachinePowerCount.setStatus("current")
_FjdaryMachinePowerTable_Object = MibTable
fjdaryMachinePowerTable = _FjdaryMachinePowerTable_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 13, 1, 2)
)
if mibBuilder.loadTexts:
    fjdaryMachinePowerTable.setStatus("current")
_FjdaryMachinePowerEntry_Object = MibTableRow
fjdaryMachinePowerEntry = _FjdaryMachinePowerEntry_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 13, 1, 2, 1)
)
fjdaryMachinePowerEntry.setIndexNames(
    (0, "FJDARY-E150", "fjdaryMachinePowerIndex"),
)
if mibBuilder.loadTexts:
    fjdaryMachinePowerEntry.setStatus("current")


class _FjdaryMachinePowerIndex_Type(Integer32):
    """Custom type fjdaryMachinePowerIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_FjdaryMachinePowerIndex_Type.__name__ = "Integer32"
_FjdaryMachinePowerIndex_Object = MibTableColumn
fjdaryMachinePowerIndex = _FjdaryMachinePowerIndex_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 13, 1, 2, 1, 1),
    _FjdaryMachinePowerIndex_Type()
)
fjdaryMachinePowerIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fjdaryMachinePowerIndex.setStatus("current")


class _FjdaryMachinePowerFlag_Type(Integer32):
    """Custom type fjdaryMachinePowerFlag based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              255)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 255),
          ("updating", 1),
          ("valid", 2))
    )


_FjdaryMachinePowerFlag_Type.__name__ = "Integer32"
_FjdaryMachinePowerFlag_Object = MibTableColumn
fjdaryMachinePowerFlag = _FjdaryMachinePowerFlag_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 13, 1, 2, 1, 2),
    _FjdaryMachinePowerFlag_Type()
)
fjdaryMachinePowerFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fjdaryMachinePowerFlag.setStatus("current")


class _FjdaryMachinePowerCmNum_Type(Integer32):
    """Custom type fjdaryMachinePowerCmNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_FjdaryMachinePowerCmNum_Type.__name__ = "Integer32"
_FjdaryMachinePowerCmNum_Object = MibTableColumn
fjdaryMachinePowerCmNum = _FjdaryMachinePowerCmNum_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 13, 1, 2, 1, 3),
    _FjdaryMachinePowerCmNum_Type()
)
fjdaryMachinePowerCmNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fjdaryMachinePowerCmNum.setStatus("current")


class _FjdaryMachinePowerTime_Type(Integer32):
    """Custom type fjdaryMachinePowerTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_FjdaryMachinePowerTime_Type.__name__ = "Integer32"
_FjdaryMachinePowerTime_Object = MibTableColumn
fjdaryMachinePowerTime = _FjdaryMachinePowerTime_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 13, 1, 2, 1, 4),
    _FjdaryMachinePowerTime_Type()
)
fjdaryMachinePowerTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fjdaryMachinePowerTime.setStatus("current")


class _FjdaryMachinePowerInfo0_Type(Integer32):
    """Custom type fjdaryMachinePowerInfo0 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_FjdaryMachinePowerInfo0_Type.__name__ = "Integer32"
_FjdaryMachinePowerInfo0_Object = MibTableColumn
fjdaryMachinePowerInfo0 = _FjdaryMachinePowerInfo0_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 13, 1, 2, 1, 5),
    _FjdaryMachinePowerInfo0_Type()
)
fjdaryMachinePowerInfo0.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fjdaryMachinePowerInfo0.setStatus("current")


class _FjdaryMachinePowerInfo1_Type(Integer32):
    """Custom type fjdaryMachinePowerInfo1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_FjdaryMachinePowerInfo1_Type.__name__ = "Integer32"
_FjdaryMachinePowerInfo1_Object = MibTableColumn
fjdaryMachinePowerInfo1 = _FjdaryMachinePowerInfo1_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 13, 1, 2, 1, 6),
    _FjdaryMachinePowerInfo1_Type()
)
fjdaryMachinePowerInfo1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fjdaryMachinePowerInfo1.setStatus("current")


class _FjdaryMachinePowerInfo2_Type(Integer32):
    """Custom type fjdaryMachinePowerInfo2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_FjdaryMachinePowerInfo2_Type.__name__ = "Integer32"
_FjdaryMachinePowerInfo2_Object = MibTableColumn
fjdaryMachinePowerInfo2 = _FjdaryMachinePowerInfo2_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 13, 1, 2, 1, 7),
    _FjdaryMachinePowerInfo2_Type()
)
fjdaryMachinePowerInfo2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fjdaryMachinePowerInfo2.setStatus("current")


class _FjdaryMachinePowerInfo3_Type(Integer32):
    """Custom type fjdaryMachinePowerInfo3 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_FjdaryMachinePowerInfo3_Type.__name__ = "Integer32"
_FjdaryMachinePowerInfo3_Object = MibTableColumn
fjdaryMachinePowerInfo3 = _FjdaryMachinePowerInfo3_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 13, 1, 2, 1, 8),
    _FjdaryMachinePowerInfo3_Type()
)
fjdaryMachinePowerInfo3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fjdaryMachinePowerInfo3.setStatus("current")


class _FjdaryMachinePowerInfo4_Type(Integer32):
    """Custom type fjdaryMachinePowerInfo4 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_FjdaryMachinePowerInfo4_Type.__name__ = "Integer32"
_FjdaryMachinePowerInfo4_Object = MibTableColumn
fjdaryMachinePowerInfo4 = _FjdaryMachinePowerInfo4_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 13, 1, 2, 1, 9),
    _FjdaryMachinePowerInfo4_Type()
)
fjdaryMachinePowerInfo4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fjdaryMachinePowerInfo4.setStatus("current")


class _FjdaryMachinePowerInfo5_Type(Integer32):
    """Custom type fjdaryMachinePowerInfo5 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_FjdaryMachinePowerInfo5_Type.__name__ = "Integer32"
_FjdaryMachinePowerInfo5_Object = MibTableColumn
fjdaryMachinePowerInfo5 = _FjdaryMachinePowerInfo5_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 13, 1, 2, 1, 10),
    _FjdaryMachinePowerInfo5_Type()
)
fjdaryMachinePowerInfo5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fjdaryMachinePowerInfo5.setStatus("current")


class _FjdaryMachinePowerInfo6_Type(Integer32):
    """Custom type fjdaryMachinePowerInfo6 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_FjdaryMachinePowerInfo6_Type.__name__ = "Integer32"
_FjdaryMachinePowerInfo6_Object = MibTableColumn
fjdaryMachinePowerInfo6 = _FjdaryMachinePowerInfo6_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 13, 1, 2, 1, 11),
    _FjdaryMachinePowerInfo6_Type()
)
fjdaryMachinePowerInfo6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fjdaryMachinePowerInfo6.setStatus("current")


class _FjdaryMachinePowerInfo7_Type(Integer32):
    """Custom type fjdaryMachinePowerInfo7 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_FjdaryMachinePowerInfo7_Type.__name__ = "Integer32"
_FjdaryMachinePowerInfo7_Object = MibTableColumn
fjdaryMachinePowerInfo7 = _FjdaryMachinePowerInfo7_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 13, 1, 2, 1, 12),
    _FjdaryMachinePowerInfo7_Type()
)
fjdaryMachinePowerInfo7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fjdaryMachinePowerInfo7.setStatus("current")


class _FjdaryMachinePowerInfo8_Type(Integer32):
    """Custom type fjdaryMachinePowerInfo8 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_FjdaryMachinePowerInfo8_Type.__name__ = "Integer32"
_FjdaryMachinePowerInfo8_Object = MibTableColumn
fjdaryMachinePowerInfo8 = _FjdaryMachinePowerInfo8_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 13, 1, 2, 1, 13),
    _FjdaryMachinePowerInfo8_Type()
)
fjdaryMachinePowerInfo8.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fjdaryMachinePowerInfo8.setStatus("current")


class _FjdaryMachinePowerInfo9_Type(Integer32):
    """Custom type fjdaryMachinePowerInfo9 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_FjdaryMachinePowerInfo9_Type.__name__ = "Integer32"
_FjdaryMachinePowerInfo9_Object = MibTableColumn
fjdaryMachinePowerInfo9 = _FjdaryMachinePowerInfo9_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 13, 1, 2, 1, 14),
    _FjdaryMachinePowerInfo9_Type()
)
fjdaryMachinePowerInfo9.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fjdaryMachinePowerInfo9.setStatus("current")


class _FjdaryMachinePowerInfo10_Type(Integer32):
    """Custom type fjdaryMachinePowerInfo10 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_FjdaryMachinePowerInfo10_Type.__name__ = "Integer32"
_FjdaryMachinePowerInfo10_Object = MibTableColumn
fjdaryMachinePowerInfo10 = _FjdaryMachinePowerInfo10_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 13, 1, 2, 1, 15),
    _FjdaryMachinePowerInfo10_Type()
)
fjdaryMachinePowerInfo10.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fjdaryMachinePowerInfo10.setStatus("current")


class _FjdaryMachinePowerInfo11_Type(Integer32):
    """Custom type fjdaryMachinePowerInfo11 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_FjdaryMachinePowerInfo11_Type.__name__ = "Integer32"
_FjdaryMachinePowerInfo11_Object = MibTableColumn
fjdaryMachinePowerInfo11 = _FjdaryMachinePowerInfo11_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 13, 1, 2, 1, 16),
    _FjdaryMachinePowerInfo11_Type()
)
fjdaryMachinePowerInfo11.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fjdaryMachinePowerInfo11.setStatus("current")


class _FjdaryMachinePowerInfo12_Type(Integer32):
    """Custom type fjdaryMachinePowerInfo12 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_FjdaryMachinePowerInfo12_Type.__name__ = "Integer32"
_FjdaryMachinePowerInfo12_Object = MibTableColumn
fjdaryMachinePowerInfo12 = _FjdaryMachinePowerInfo12_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 13, 1, 2, 1, 17),
    _FjdaryMachinePowerInfo12_Type()
)
fjdaryMachinePowerInfo12.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fjdaryMachinePowerInfo12.setStatus("current")


class _FjdaryMachinePowerInfo13_Type(Integer32):
    """Custom type fjdaryMachinePowerInfo13 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_FjdaryMachinePowerInfo13_Type.__name__ = "Integer32"
_FjdaryMachinePowerInfo13_Object = MibTableColumn
fjdaryMachinePowerInfo13 = _FjdaryMachinePowerInfo13_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 13, 1, 2, 1, 18),
    _FjdaryMachinePowerInfo13_Type()
)
fjdaryMachinePowerInfo13.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fjdaryMachinePowerInfo13.setStatus("current")


class _FjdaryMachinePowerInfo14_Type(Integer32):
    """Custom type fjdaryMachinePowerInfo14 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_FjdaryMachinePowerInfo14_Type.__name__ = "Integer32"
_FjdaryMachinePowerInfo14_Object = MibTableColumn
fjdaryMachinePowerInfo14 = _FjdaryMachinePowerInfo14_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 13, 1, 2, 1, 19),
    _FjdaryMachinePowerInfo14_Type()
)
fjdaryMachinePowerInfo14.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fjdaryMachinePowerInfo14.setStatus("current")


class _FjdaryMachinePowerInfo15_Type(Integer32):
    """Custom type fjdaryMachinePowerInfo15 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_FjdaryMachinePowerInfo15_Type.__name__ = "Integer32"
_FjdaryMachinePowerInfo15_Object = MibTableColumn
fjdaryMachinePowerInfo15 = _FjdaryMachinePowerInfo15_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 13, 1, 2, 1, 20),
    _FjdaryMachinePowerInfo15_Type()
)
fjdaryMachinePowerInfo15.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fjdaryMachinePowerInfo15.setStatus("current")


class _FjdaryMachinePowerInfo16_Type(Integer32):
    """Custom type fjdaryMachinePowerInfo16 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_FjdaryMachinePowerInfo16_Type.__name__ = "Integer32"
_FjdaryMachinePowerInfo16_Object = MibTableColumn
fjdaryMachinePowerInfo16 = _FjdaryMachinePowerInfo16_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 13, 1, 2, 1, 21),
    _FjdaryMachinePowerInfo16_Type()
)
fjdaryMachinePowerInfo16.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fjdaryMachinePowerInfo16.setStatus("current")


class _FjdaryMachinePowerInfo17_Type(Integer32):
    """Custom type fjdaryMachinePowerInfo17 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_FjdaryMachinePowerInfo17_Type.__name__ = "Integer32"
_FjdaryMachinePowerInfo17_Object = MibTableColumn
fjdaryMachinePowerInfo17 = _FjdaryMachinePowerInfo17_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 13, 1, 2, 1, 22),
    _FjdaryMachinePowerInfo17_Type()
)
fjdaryMachinePowerInfo17.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fjdaryMachinePowerInfo17.setStatus("current")


class _FjdaryMachinePowerInfo18_Type(Integer32):
    """Custom type fjdaryMachinePowerInfo18 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_FjdaryMachinePowerInfo18_Type.__name__ = "Integer32"
_FjdaryMachinePowerInfo18_Object = MibTableColumn
fjdaryMachinePowerInfo18 = _FjdaryMachinePowerInfo18_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 13, 1, 2, 1, 23),
    _FjdaryMachinePowerInfo18_Type()
)
fjdaryMachinePowerInfo18.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fjdaryMachinePowerInfo18.setStatus("current")


class _FjdaryMachinePowerInfo19_Type(Integer32):
    """Custom type fjdaryMachinePowerInfo19 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_FjdaryMachinePowerInfo19_Type.__name__ = "Integer32"
_FjdaryMachinePowerInfo19_Object = MibTableColumn
fjdaryMachinePowerInfo19 = _FjdaryMachinePowerInfo19_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 13, 1, 2, 1, 24),
    _FjdaryMachinePowerInfo19_Type()
)
fjdaryMachinePowerInfo19.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fjdaryMachinePowerInfo19.setStatus("current")


class _FjdaryMachinePowerInfo20_Type(Integer32):
    """Custom type fjdaryMachinePowerInfo20 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_FjdaryMachinePowerInfo20_Type.__name__ = "Integer32"
_FjdaryMachinePowerInfo20_Object = MibTableColumn
fjdaryMachinePowerInfo20 = _FjdaryMachinePowerInfo20_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 13, 1, 2, 1, 25),
    _FjdaryMachinePowerInfo20_Type()
)
fjdaryMachinePowerInfo20.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fjdaryMachinePowerInfo20.setStatus("current")


class _FjdaryMachinePowerInfo21_Type(Integer32):
    """Custom type fjdaryMachinePowerInfo21 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_FjdaryMachinePowerInfo21_Type.__name__ = "Integer32"
_FjdaryMachinePowerInfo21_Object = MibTableColumn
fjdaryMachinePowerInfo21 = _FjdaryMachinePowerInfo21_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 13, 1, 2, 1, 26),
    _FjdaryMachinePowerInfo21_Type()
)
fjdaryMachinePowerInfo21.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fjdaryMachinePowerInfo21.setStatus("current")


class _FjdaryMachinePowerInfo22_Type(Integer32):
    """Custom type fjdaryMachinePowerInfo22 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_FjdaryMachinePowerInfo22_Type.__name__ = "Integer32"
_FjdaryMachinePowerInfo22_Object = MibTableColumn
fjdaryMachinePowerInfo22 = _FjdaryMachinePowerInfo22_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 13, 1, 2, 1, 27),
    _FjdaryMachinePowerInfo22_Type()
)
fjdaryMachinePowerInfo22.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fjdaryMachinePowerInfo22.setStatus("current")


class _FjdaryMachinePowerInfo23_Type(Integer32):
    """Custom type fjdaryMachinePowerInfo23 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_FjdaryMachinePowerInfo23_Type.__name__ = "Integer32"
_FjdaryMachinePowerInfo23_Object = MibTableColumn
fjdaryMachinePowerInfo23 = _FjdaryMachinePowerInfo23_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 13, 1, 2, 1, 28),
    _FjdaryMachinePowerInfo23_Type()
)
fjdaryMachinePowerInfo23.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fjdaryMachinePowerInfo23.setStatus("current")


class _FjdaryMachinePowerInfo24_Type(Integer32):
    """Custom type fjdaryMachinePowerInfo24 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_FjdaryMachinePowerInfo24_Type.__name__ = "Integer32"
_FjdaryMachinePowerInfo24_Object = MibTableColumn
fjdaryMachinePowerInfo24 = _FjdaryMachinePowerInfo24_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 13, 1, 2, 1, 29),
    _FjdaryMachinePowerInfo24_Type()
)
fjdaryMachinePowerInfo24.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fjdaryMachinePowerInfo24.setStatus("current")
_FjdaryEncPower_ObjectIdentity = ObjectIdentity
fjdaryEncPower = _FjdaryEncPower_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 13, 2)
)


class _FjdaryEncPowerCount_Type(Integer32):
    """Custom type fjdaryEncPowerCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_FjdaryEncPowerCount_Type.__name__ = "Integer32"
_FjdaryEncPowerCount_Object = MibScalar
fjdaryEncPowerCount = _FjdaryEncPowerCount_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 13, 2, 1),
    _FjdaryEncPowerCount_Type()
)
fjdaryEncPowerCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fjdaryEncPowerCount.setStatus("current")
_FjdaryEncPowerTable_Object = MibTable
fjdaryEncPowerTable = _FjdaryEncPowerTable_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 13, 2, 2)
)
if mibBuilder.loadTexts:
    fjdaryEncPowerTable.setStatus("current")
_FjdaryEncPowerEntry_Object = MibTableRow
fjdaryEncPowerEntry = _FjdaryEncPowerEntry_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 13, 2, 2, 1)
)
fjdaryEncPowerEntry.setIndexNames(
    (0, "FJDARY-E150", "fjdaryEncPowerIndex"),
)
if mibBuilder.loadTexts:
    fjdaryEncPowerEntry.setStatus("current")


class _FjdaryEncPowerIndex_Type(Integer32):
    """Custom type fjdaryEncPowerIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_FjdaryEncPowerIndex_Type.__name__ = "Integer32"
_FjdaryEncPowerIndex_Object = MibTableColumn
fjdaryEncPowerIndex = _FjdaryEncPowerIndex_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 13, 2, 2, 1, 1),
    _FjdaryEncPowerIndex_Type()
)
fjdaryEncPowerIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fjdaryEncPowerIndex.setStatus("current")


class _FjdaryEncPowerFlag_Type(Integer32):
    """Custom type fjdaryEncPowerFlag based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              255)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 255),
          ("updating", 1),
          ("valid", 2))
    )


_FjdaryEncPowerFlag_Type.__name__ = "Integer32"
_FjdaryEncPowerFlag_Object = MibTableColumn
fjdaryEncPowerFlag = _FjdaryEncPowerFlag_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 13, 2, 2, 1, 2),
    _FjdaryEncPowerFlag_Type()
)
fjdaryEncPowerFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fjdaryEncPowerFlag.setStatus("current")


class _FjdaryEncPowerCmNum_Type(Integer32):
    """Custom type fjdaryEncPowerCmNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_FjdaryEncPowerCmNum_Type.__name__ = "Integer32"
_FjdaryEncPowerCmNum_Object = MibTableColumn
fjdaryEncPowerCmNum = _FjdaryEncPowerCmNum_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 13, 2, 2, 1, 3),
    _FjdaryEncPowerCmNum_Type()
)
fjdaryEncPowerCmNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fjdaryEncPowerCmNum.setStatus("current")


class _FjdaryEncPowerDeId_Type(Integer32):
    """Custom type fjdaryEncPowerDeId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_FjdaryEncPowerDeId_Type.__name__ = "Integer32"
_FjdaryEncPowerDeId_Object = MibTableColumn
fjdaryEncPowerDeId = _FjdaryEncPowerDeId_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 13, 2, 2, 1, 4),
    _FjdaryEncPowerDeId_Type()
)
fjdaryEncPowerDeId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fjdaryEncPowerDeId.setStatus("current")


class _FjdaryEncPowerTime_Type(Integer32):
    """Custom type fjdaryEncPowerTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_FjdaryEncPowerTime_Type.__name__ = "Integer32"
_FjdaryEncPowerTime_Object = MibTableColumn
fjdaryEncPowerTime = _FjdaryEncPowerTime_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 13, 2, 2, 1, 5),
    _FjdaryEncPowerTime_Type()
)
fjdaryEncPowerTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fjdaryEncPowerTime.setStatus("current")


class _FjdaryEncPowerType_Type(Integer32):
    """Custom type fjdaryEncPowerType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(16,
              32)
        )
    )
    namedValues = NamedValues(
        *(("ce", 16),
          ("de", 32))
    )


_FjdaryEncPowerType_Type.__name__ = "Integer32"
_FjdaryEncPowerType_Object = MibTableColumn
fjdaryEncPowerType = _FjdaryEncPowerType_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 13, 2, 2, 1, 6),
    _FjdaryEncPowerType_Type()
)
fjdaryEncPowerType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fjdaryEncPowerType.setStatus("current")


class _FjdaryEncPowerInfo0_Type(Integer32):
    """Custom type fjdaryEncPowerInfo0 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_FjdaryEncPowerInfo0_Type.__name__ = "Integer32"
_FjdaryEncPowerInfo0_Object = MibTableColumn
fjdaryEncPowerInfo0 = _FjdaryEncPowerInfo0_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 13, 2, 2, 1, 7),
    _FjdaryEncPowerInfo0_Type()
)
fjdaryEncPowerInfo0.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fjdaryEncPowerInfo0.setStatus("current")


class _FjdaryEncPowerInfo1_Type(Integer32):
    """Custom type fjdaryEncPowerInfo1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_FjdaryEncPowerInfo1_Type.__name__ = "Integer32"
_FjdaryEncPowerInfo1_Object = MibTableColumn
fjdaryEncPowerInfo1 = _FjdaryEncPowerInfo1_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 13, 2, 2, 1, 8),
    _FjdaryEncPowerInfo1_Type()
)
fjdaryEncPowerInfo1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fjdaryEncPowerInfo1.setStatus("current")


class _FjdaryEncPowerInfo2_Type(Integer32):
    """Custom type fjdaryEncPowerInfo2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_FjdaryEncPowerInfo2_Type.__name__ = "Integer32"
_FjdaryEncPowerInfo2_Object = MibTableColumn
fjdaryEncPowerInfo2 = _FjdaryEncPowerInfo2_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 13, 2, 2, 1, 9),
    _FjdaryEncPowerInfo2_Type()
)
fjdaryEncPowerInfo2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fjdaryEncPowerInfo2.setStatus("current")


class _FjdaryEncPowerInfo3_Type(Integer32):
    """Custom type fjdaryEncPowerInfo3 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_FjdaryEncPowerInfo3_Type.__name__ = "Integer32"
_FjdaryEncPowerInfo3_Object = MibTableColumn
fjdaryEncPowerInfo3 = _FjdaryEncPowerInfo3_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 13, 2, 2, 1, 10),
    _FjdaryEncPowerInfo3_Type()
)
fjdaryEncPowerInfo3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fjdaryEncPowerInfo3.setStatus("current")


class _FjdaryEncPowerInfo4_Type(Integer32):
    """Custom type fjdaryEncPowerInfo4 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_FjdaryEncPowerInfo4_Type.__name__ = "Integer32"
_FjdaryEncPowerInfo4_Object = MibTableColumn
fjdaryEncPowerInfo4 = _FjdaryEncPowerInfo4_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 13, 2, 2, 1, 11),
    _FjdaryEncPowerInfo4_Type()
)
fjdaryEncPowerInfo4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fjdaryEncPowerInfo4.setStatus("current")


class _FjdaryEncPowerInfo5_Type(Integer32):
    """Custom type fjdaryEncPowerInfo5 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_FjdaryEncPowerInfo5_Type.__name__ = "Integer32"
_FjdaryEncPowerInfo5_Object = MibTableColumn
fjdaryEncPowerInfo5 = _FjdaryEncPowerInfo5_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 13, 2, 2, 1, 12),
    _FjdaryEncPowerInfo5_Type()
)
fjdaryEncPowerInfo5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fjdaryEncPowerInfo5.setStatus("current")


class _FjdaryEncPowerInfo6_Type(Integer32):
    """Custom type fjdaryEncPowerInfo6 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_FjdaryEncPowerInfo6_Type.__name__ = "Integer32"
_FjdaryEncPowerInfo6_Object = MibTableColumn
fjdaryEncPowerInfo6 = _FjdaryEncPowerInfo6_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 13, 2, 2, 1, 13),
    _FjdaryEncPowerInfo6_Type()
)
fjdaryEncPowerInfo6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fjdaryEncPowerInfo6.setStatus("current")


class _FjdaryEncPowerInfo7_Type(Integer32):
    """Custom type fjdaryEncPowerInfo7 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_FjdaryEncPowerInfo7_Type.__name__ = "Integer32"
_FjdaryEncPowerInfo7_Object = MibTableColumn
fjdaryEncPowerInfo7 = _FjdaryEncPowerInfo7_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 13, 2, 2, 1, 14),
    _FjdaryEncPowerInfo7_Type()
)
fjdaryEncPowerInfo7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fjdaryEncPowerInfo7.setStatus("current")


class _FjdaryEncPowerInfo8_Type(Integer32):
    """Custom type fjdaryEncPowerInfo8 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_FjdaryEncPowerInfo8_Type.__name__ = "Integer32"
_FjdaryEncPowerInfo8_Object = MibTableColumn
fjdaryEncPowerInfo8 = _FjdaryEncPowerInfo8_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 13, 2, 2, 1, 15),
    _FjdaryEncPowerInfo8_Type()
)
fjdaryEncPowerInfo8.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fjdaryEncPowerInfo8.setStatus("current")


class _FjdaryEncPowerInfo9_Type(Integer32):
    """Custom type fjdaryEncPowerInfo9 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_FjdaryEncPowerInfo9_Type.__name__ = "Integer32"
_FjdaryEncPowerInfo9_Object = MibTableColumn
fjdaryEncPowerInfo9 = _FjdaryEncPowerInfo9_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 13, 2, 2, 1, 16),
    _FjdaryEncPowerInfo9_Type()
)
fjdaryEncPowerInfo9.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fjdaryEncPowerInfo9.setStatus("current")


class _FjdaryEncPowerInfo10_Type(Integer32):
    """Custom type fjdaryEncPowerInfo10 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_FjdaryEncPowerInfo10_Type.__name__ = "Integer32"
_FjdaryEncPowerInfo10_Object = MibTableColumn
fjdaryEncPowerInfo10 = _FjdaryEncPowerInfo10_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 13, 2, 2, 1, 17),
    _FjdaryEncPowerInfo10_Type()
)
fjdaryEncPowerInfo10.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fjdaryEncPowerInfo10.setStatus("current")


class _FjdaryEncPowerInfo11_Type(Integer32):
    """Custom type fjdaryEncPowerInfo11 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_FjdaryEncPowerInfo11_Type.__name__ = "Integer32"
_FjdaryEncPowerInfo11_Object = MibTableColumn
fjdaryEncPowerInfo11 = _FjdaryEncPowerInfo11_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 13, 2, 2, 1, 18),
    _FjdaryEncPowerInfo11_Type()
)
fjdaryEncPowerInfo11.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fjdaryEncPowerInfo11.setStatus("current")


class _FjdaryEncPowerInfo12_Type(Integer32):
    """Custom type fjdaryEncPowerInfo12 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_FjdaryEncPowerInfo12_Type.__name__ = "Integer32"
_FjdaryEncPowerInfo12_Object = MibTableColumn
fjdaryEncPowerInfo12 = _FjdaryEncPowerInfo12_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 13, 2, 2, 1, 19),
    _FjdaryEncPowerInfo12_Type()
)
fjdaryEncPowerInfo12.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fjdaryEncPowerInfo12.setStatus("current")


class _FjdaryEncPowerInfo13_Type(Integer32):
    """Custom type fjdaryEncPowerInfo13 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_FjdaryEncPowerInfo13_Type.__name__ = "Integer32"
_FjdaryEncPowerInfo13_Object = MibTableColumn
fjdaryEncPowerInfo13 = _FjdaryEncPowerInfo13_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 13, 2, 2, 1, 20),
    _FjdaryEncPowerInfo13_Type()
)
fjdaryEncPowerInfo13.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fjdaryEncPowerInfo13.setStatus("current")


class _FjdaryEncPowerInfo14_Type(Integer32):
    """Custom type fjdaryEncPowerInfo14 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_FjdaryEncPowerInfo14_Type.__name__ = "Integer32"
_FjdaryEncPowerInfo14_Object = MibTableColumn
fjdaryEncPowerInfo14 = _FjdaryEncPowerInfo14_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 13, 2, 2, 1, 21),
    _FjdaryEncPowerInfo14_Type()
)
fjdaryEncPowerInfo14.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fjdaryEncPowerInfo14.setStatus("current")


class _FjdaryEncPowerInfo15_Type(Integer32):
    """Custom type fjdaryEncPowerInfo15 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_FjdaryEncPowerInfo15_Type.__name__ = "Integer32"
_FjdaryEncPowerInfo15_Object = MibTableColumn
fjdaryEncPowerInfo15 = _FjdaryEncPowerInfo15_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 13, 2, 2, 1, 22),
    _FjdaryEncPowerInfo15_Type()
)
fjdaryEncPowerInfo15.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fjdaryEncPowerInfo15.setStatus("current")


class _FjdaryEncPowerInfo16_Type(Integer32):
    """Custom type fjdaryEncPowerInfo16 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_FjdaryEncPowerInfo16_Type.__name__ = "Integer32"
_FjdaryEncPowerInfo16_Object = MibTableColumn
fjdaryEncPowerInfo16 = _FjdaryEncPowerInfo16_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 13, 2, 2, 1, 23),
    _FjdaryEncPowerInfo16_Type()
)
fjdaryEncPowerInfo16.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fjdaryEncPowerInfo16.setStatus("current")


class _FjdaryEncPowerInfo17_Type(Integer32):
    """Custom type fjdaryEncPowerInfo17 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_FjdaryEncPowerInfo17_Type.__name__ = "Integer32"
_FjdaryEncPowerInfo17_Object = MibTableColumn
fjdaryEncPowerInfo17 = _FjdaryEncPowerInfo17_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 13, 2, 2, 1, 24),
    _FjdaryEncPowerInfo17_Type()
)
fjdaryEncPowerInfo17.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fjdaryEncPowerInfo17.setStatus("current")


class _FjdaryEncPowerInfo18_Type(Integer32):
    """Custom type fjdaryEncPowerInfo18 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_FjdaryEncPowerInfo18_Type.__name__ = "Integer32"
_FjdaryEncPowerInfo18_Object = MibTableColumn
fjdaryEncPowerInfo18 = _FjdaryEncPowerInfo18_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 13, 2, 2, 1, 25),
    _FjdaryEncPowerInfo18_Type()
)
fjdaryEncPowerInfo18.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fjdaryEncPowerInfo18.setStatus("current")


class _FjdaryEncPowerInfo19_Type(Integer32):
    """Custom type fjdaryEncPowerInfo19 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_FjdaryEncPowerInfo19_Type.__name__ = "Integer32"
_FjdaryEncPowerInfo19_Object = MibTableColumn
fjdaryEncPowerInfo19 = _FjdaryEncPowerInfo19_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 13, 2, 2, 1, 26),
    _FjdaryEncPowerInfo19_Type()
)
fjdaryEncPowerInfo19.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fjdaryEncPowerInfo19.setStatus("current")


class _FjdaryEncPowerInfo20_Type(Integer32):
    """Custom type fjdaryEncPowerInfo20 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_FjdaryEncPowerInfo20_Type.__name__ = "Integer32"
_FjdaryEncPowerInfo20_Object = MibTableColumn
fjdaryEncPowerInfo20 = _FjdaryEncPowerInfo20_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 13, 2, 2, 1, 27),
    _FjdaryEncPowerInfo20_Type()
)
fjdaryEncPowerInfo20.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fjdaryEncPowerInfo20.setStatus("current")


class _FjdaryEncPowerInfo21_Type(Integer32):
    """Custom type fjdaryEncPowerInfo21 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_FjdaryEncPowerInfo21_Type.__name__ = "Integer32"
_FjdaryEncPowerInfo21_Object = MibTableColumn
fjdaryEncPowerInfo21 = _FjdaryEncPowerInfo21_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 13, 2, 2, 1, 28),
    _FjdaryEncPowerInfo21_Type()
)
fjdaryEncPowerInfo21.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fjdaryEncPowerInfo21.setStatus("current")


class _FjdaryEncPowerInfo22_Type(Integer32):
    """Custom type fjdaryEncPowerInfo22 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_FjdaryEncPowerInfo22_Type.__name__ = "Integer32"
_FjdaryEncPowerInfo22_Object = MibTableColumn
fjdaryEncPowerInfo22 = _FjdaryEncPowerInfo22_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 13, 2, 2, 1, 29),
    _FjdaryEncPowerInfo22_Type()
)
fjdaryEncPowerInfo22.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fjdaryEncPowerInfo22.setStatus("current")


class _FjdaryEncPowerInfo23_Type(Integer32):
    """Custom type fjdaryEncPowerInfo23 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_FjdaryEncPowerInfo23_Type.__name__ = "Integer32"
_FjdaryEncPowerInfo23_Object = MibTableColumn
fjdaryEncPowerInfo23 = _FjdaryEncPowerInfo23_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 13, 2, 2, 1, 30),
    _FjdaryEncPowerInfo23_Type()
)
fjdaryEncPowerInfo23.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fjdaryEncPowerInfo23.setStatus("current")


class _FjdaryEncPowerInfo24_Type(Integer32):
    """Custom type fjdaryEncPowerInfo24 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_FjdaryEncPowerInfo24_Type.__name__ = "Integer32"
_FjdaryEncPowerInfo24_Object = MibTableColumn
fjdaryEncPowerInfo24 = _FjdaryEncPowerInfo24_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 13, 2, 2, 1, 31),
    _FjdaryEncPowerInfo24_Type()
)
fjdaryEncPowerInfo24.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fjdaryEncPowerInfo24.setStatus("current")
_FjdaryMachineTemp_ObjectIdentity = ObjectIdentity
fjdaryMachineTemp = _FjdaryMachineTemp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 13, 3)
)


class _FjdaryMachineTempCount_Type(Integer32):
    """Custom type fjdaryMachineTempCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_FjdaryMachineTempCount_Type.__name__ = "Integer32"
_FjdaryMachineTempCount_Object = MibScalar
fjdaryMachineTempCount = _FjdaryMachineTempCount_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 13, 3, 1),
    _FjdaryMachineTempCount_Type()
)
fjdaryMachineTempCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fjdaryMachineTempCount.setStatus("current")
_FjdaryMachineTempTable_Object = MibTable
fjdaryMachineTempTable = _FjdaryMachineTempTable_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 13, 3, 2)
)
if mibBuilder.loadTexts:
    fjdaryMachineTempTable.setStatus("current")
_FjdaryMachineTempEntry_Object = MibTableRow
fjdaryMachineTempEntry = _FjdaryMachineTempEntry_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 13, 3, 2, 1)
)
fjdaryMachineTempEntry.setIndexNames(
    (0, "FJDARY-E150", "fjdaryMachineTempIndex"),
)
if mibBuilder.loadTexts:
    fjdaryMachineTempEntry.setStatus("current")


class _FjdaryMachineTempIndex_Type(Integer32):
    """Custom type fjdaryMachineTempIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_FjdaryMachineTempIndex_Type.__name__ = "Integer32"
_FjdaryMachineTempIndex_Object = MibTableColumn
fjdaryMachineTempIndex = _FjdaryMachineTempIndex_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 13, 3, 2, 1, 1),
    _FjdaryMachineTempIndex_Type()
)
fjdaryMachineTempIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fjdaryMachineTempIndex.setStatus("current")


class _FjdaryMachineTempFlag_Type(Integer32):
    """Custom type fjdaryMachineTempFlag based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              255)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 255),
          ("updating", 1),
          ("valid", 2))
    )


_FjdaryMachineTempFlag_Type.__name__ = "Integer32"
_FjdaryMachineTempFlag_Object = MibTableColumn
fjdaryMachineTempFlag = _FjdaryMachineTempFlag_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 13, 3, 2, 1, 2),
    _FjdaryMachineTempFlag_Type()
)
fjdaryMachineTempFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fjdaryMachineTempFlag.setStatus("current")


class _FjdaryMachineTempCmNum_Type(Integer32):
    """Custom type fjdaryMachineTempCmNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_FjdaryMachineTempCmNum_Type.__name__ = "Integer32"
_FjdaryMachineTempCmNum_Object = MibTableColumn
fjdaryMachineTempCmNum = _FjdaryMachineTempCmNum_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 13, 3, 2, 1, 3),
    _FjdaryMachineTempCmNum_Type()
)
fjdaryMachineTempCmNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fjdaryMachineTempCmNum.setStatus("current")


class _FjdaryMachineTempTime_Type(Integer32):
    """Custom type fjdaryMachineTempTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_FjdaryMachineTempTime_Type.__name__ = "Integer32"
_FjdaryMachineTempTime_Object = MibTableColumn
fjdaryMachineTempTime = _FjdaryMachineTempTime_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 13, 3, 2, 1, 4),
    _FjdaryMachineTempTime_Type()
)
fjdaryMachineTempTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fjdaryMachineTempTime.setStatus("current")


class _FjdaryMachineTempInfo0_Type(Integer32):
    """Custom type fjdaryMachineTempInfo0 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_FjdaryMachineTempInfo0_Type.__name__ = "Integer32"
_FjdaryMachineTempInfo0_Object = MibTableColumn
fjdaryMachineTempInfo0 = _FjdaryMachineTempInfo0_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 13, 3, 2, 1, 5),
    _FjdaryMachineTempInfo0_Type()
)
fjdaryMachineTempInfo0.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fjdaryMachineTempInfo0.setStatus("current")


class _FjdaryMachineTempInfo1_Type(Integer32):
    """Custom type fjdaryMachineTempInfo1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_FjdaryMachineTempInfo1_Type.__name__ = "Integer32"
_FjdaryMachineTempInfo1_Object = MibTableColumn
fjdaryMachineTempInfo1 = _FjdaryMachineTempInfo1_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 13, 3, 2, 1, 6),
    _FjdaryMachineTempInfo1_Type()
)
fjdaryMachineTempInfo1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fjdaryMachineTempInfo1.setStatus("current")


class _FjdaryMachineTempInfo2_Type(Integer32):
    """Custom type fjdaryMachineTempInfo2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_FjdaryMachineTempInfo2_Type.__name__ = "Integer32"
_FjdaryMachineTempInfo2_Object = MibTableColumn
fjdaryMachineTempInfo2 = _FjdaryMachineTempInfo2_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 13, 3, 2, 1, 7),
    _FjdaryMachineTempInfo2_Type()
)
fjdaryMachineTempInfo2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fjdaryMachineTempInfo2.setStatus("current")


class _FjdaryMachineTempInfo3_Type(Integer32):
    """Custom type fjdaryMachineTempInfo3 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_FjdaryMachineTempInfo3_Type.__name__ = "Integer32"
_FjdaryMachineTempInfo3_Object = MibTableColumn
fjdaryMachineTempInfo3 = _FjdaryMachineTempInfo3_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 13, 3, 2, 1, 8),
    _FjdaryMachineTempInfo3_Type()
)
fjdaryMachineTempInfo3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fjdaryMachineTempInfo3.setStatus("current")


class _FjdaryMachineTempInfo4_Type(Integer32):
    """Custom type fjdaryMachineTempInfo4 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_FjdaryMachineTempInfo4_Type.__name__ = "Integer32"
_FjdaryMachineTempInfo4_Object = MibTableColumn
fjdaryMachineTempInfo4 = _FjdaryMachineTempInfo4_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 13, 3, 2, 1, 9),
    _FjdaryMachineTempInfo4_Type()
)
fjdaryMachineTempInfo4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fjdaryMachineTempInfo4.setStatus("current")


class _FjdaryMachineTempInfo5_Type(Integer32):
    """Custom type fjdaryMachineTempInfo5 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_FjdaryMachineTempInfo5_Type.__name__ = "Integer32"
_FjdaryMachineTempInfo5_Object = MibTableColumn
fjdaryMachineTempInfo5 = _FjdaryMachineTempInfo5_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 13, 3, 2, 1, 10),
    _FjdaryMachineTempInfo5_Type()
)
fjdaryMachineTempInfo5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fjdaryMachineTempInfo5.setStatus("current")


class _FjdaryMachineTempInfo6_Type(Integer32):
    """Custom type fjdaryMachineTempInfo6 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_FjdaryMachineTempInfo6_Type.__name__ = "Integer32"
_FjdaryMachineTempInfo6_Object = MibTableColumn
fjdaryMachineTempInfo6 = _FjdaryMachineTempInfo6_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 13, 3, 2, 1, 11),
    _FjdaryMachineTempInfo6_Type()
)
fjdaryMachineTempInfo6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fjdaryMachineTempInfo6.setStatus("current")


class _FjdaryMachineTempInfo7_Type(Integer32):
    """Custom type fjdaryMachineTempInfo7 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_FjdaryMachineTempInfo7_Type.__name__ = "Integer32"
_FjdaryMachineTempInfo7_Object = MibTableColumn
fjdaryMachineTempInfo7 = _FjdaryMachineTempInfo7_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 13, 3, 2, 1, 12),
    _FjdaryMachineTempInfo7_Type()
)
fjdaryMachineTempInfo7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fjdaryMachineTempInfo7.setStatus("current")


class _FjdaryMachineTempInfo8_Type(Integer32):
    """Custom type fjdaryMachineTempInfo8 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_FjdaryMachineTempInfo8_Type.__name__ = "Integer32"
_FjdaryMachineTempInfo8_Object = MibTableColumn
fjdaryMachineTempInfo8 = _FjdaryMachineTempInfo8_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 13, 3, 2, 1, 13),
    _FjdaryMachineTempInfo8_Type()
)
fjdaryMachineTempInfo8.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fjdaryMachineTempInfo8.setStatus("current")


class _FjdaryMachineTempInfo9_Type(Integer32):
    """Custom type fjdaryMachineTempInfo9 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_FjdaryMachineTempInfo9_Type.__name__ = "Integer32"
_FjdaryMachineTempInfo9_Object = MibTableColumn
fjdaryMachineTempInfo9 = _FjdaryMachineTempInfo9_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 13, 3, 2, 1, 14),
    _FjdaryMachineTempInfo9_Type()
)
fjdaryMachineTempInfo9.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fjdaryMachineTempInfo9.setStatus("current")


class _FjdaryMachineTempInfo10_Type(Integer32):
    """Custom type fjdaryMachineTempInfo10 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_FjdaryMachineTempInfo10_Type.__name__ = "Integer32"
_FjdaryMachineTempInfo10_Object = MibTableColumn
fjdaryMachineTempInfo10 = _FjdaryMachineTempInfo10_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 13, 3, 2, 1, 15),
    _FjdaryMachineTempInfo10_Type()
)
fjdaryMachineTempInfo10.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fjdaryMachineTempInfo10.setStatus("current")


class _FjdaryMachineTempInfo11_Type(Integer32):
    """Custom type fjdaryMachineTempInfo11 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_FjdaryMachineTempInfo11_Type.__name__ = "Integer32"
_FjdaryMachineTempInfo11_Object = MibTableColumn
fjdaryMachineTempInfo11 = _FjdaryMachineTempInfo11_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 13, 3, 2, 1, 16),
    _FjdaryMachineTempInfo11_Type()
)
fjdaryMachineTempInfo11.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fjdaryMachineTempInfo11.setStatus("current")


class _FjdaryMachineTempInfo12_Type(Integer32):
    """Custom type fjdaryMachineTempInfo12 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_FjdaryMachineTempInfo12_Type.__name__ = "Integer32"
_FjdaryMachineTempInfo12_Object = MibTableColumn
fjdaryMachineTempInfo12 = _FjdaryMachineTempInfo12_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 13, 3, 2, 1, 17),
    _FjdaryMachineTempInfo12_Type()
)
fjdaryMachineTempInfo12.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fjdaryMachineTempInfo12.setStatus("current")


class _FjdaryMachineTempInfo13_Type(Integer32):
    """Custom type fjdaryMachineTempInfo13 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_FjdaryMachineTempInfo13_Type.__name__ = "Integer32"
_FjdaryMachineTempInfo13_Object = MibTableColumn
fjdaryMachineTempInfo13 = _FjdaryMachineTempInfo13_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 13, 3, 2, 1, 18),
    _FjdaryMachineTempInfo13_Type()
)
fjdaryMachineTempInfo13.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fjdaryMachineTempInfo13.setStatus("current")


class _FjdaryMachineTempInfo14_Type(Integer32):
    """Custom type fjdaryMachineTempInfo14 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_FjdaryMachineTempInfo14_Type.__name__ = "Integer32"
_FjdaryMachineTempInfo14_Object = MibTableColumn
fjdaryMachineTempInfo14 = _FjdaryMachineTempInfo14_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 13, 3, 2, 1, 19),
    _FjdaryMachineTempInfo14_Type()
)
fjdaryMachineTempInfo14.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fjdaryMachineTempInfo14.setStatus("current")


class _FjdaryMachineTempInfo15_Type(Integer32):
    """Custom type fjdaryMachineTempInfo15 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_FjdaryMachineTempInfo15_Type.__name__ = "Integer32"
_FjdaryMachineTempInfo15_Object = MibTableColumn
fjdaryMachineTempInfo15 = _FjdaryMachineTempInfo15_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 13, 3, 2, 1, 20),
    _FjdaryMachineTempInfo15_Type()
)
fjdaryMachineTempInfo15.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fjdaryMachineTempInfo15.setStatus("current")


class _FjdaryMachineTempInfo16_Type(Integer32):
    """Custom type fjdaryMachineTempInfo16 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_FjdaryMachineTempInfo16_Type.__name__ = "Integer32"
_FjdaryMachineTempInfo16_Object = MibTableColumn
fjdaryMachineTempInfo16 = _FjdaryMachineTempInfo16_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 13, 3, 2, 1, 21),
    _FjdaryMachineTempInfo16_Type()
)
fjdaryMachineTempInfo16.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fjdaryMachineTempInfo16.setStatus("current")


class _FjdaryMachineTempInfo17_Type(Integer32):
    """Custom type fjdaryMachineTempInfo17 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_FjdaryMachineTempInfo17_Type.__name__ = "Integer32"
_FjdaryMachineTempInfo17_Object = MibTableColumn
fjdaryMachineTempInfo17 = _FjdaryMachineTempInfo17_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 13, 3, 2, 1, 22),
    _FjdaryMachineTempInfo17_Type()
)
fjdaryMachineTempInfo17.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fjdaryMachineTempInfo17.setStatus("current")


class _FjdaryMachineTempInfo18_Type(Integer32):
    """Custom type fjdaryMachineTempInfo18 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_FjdaryMachineTempInfo18_Type.__name__ = "Integer32"
_FjdaryMachineTempInfo18_Object = MibTableColumn
fjdaryMachineTempInfo18 = _FjdaryMachineTempInfo18_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 13, 3, 2, 1, 23),
    _FjdaryMachineTempInfo18_Type()
)
fjdaryMachineTempInfo18.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fjdaryMachineTempInfo18.setStatus("current")


class _FjdaryMachineTempInfo19_Type(Integer32):
    """Custom type fjdaryMachineTempInfo19 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_FjdaryMachineTempInfo19_Type.__name__ = "Integer32"
_FjdaryMachineTempInfo19_Object = MibTableColumn
fjdaryMachineTempInfo19 = _FjdaryMachineTempInfo19_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 13, 3, 2, 1, 24),
    _FjdaryMachineTempInfo19_Type()
)
fjdaryMachineTempInfo19.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fjdaryMachineTempInfo19.setStatus("current")


class _FjdaryMachineTempInfo20_Type(Integer32):
    """Custom type fjdaryMachineTempInfo20 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_FjdaryMachineTempInfo20_Type.__name__ = "Integer32"
_FjdaryMachineTempInfo20_Object = MibTableColumn
fjdaryMachineTempInfo20 = _FjdaryMachineTempInfo20_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 13, 3, 2, 1, 25),
    _FjdaryMachineTempInfo20_Type()
)
fjdaryMachineTempInfo20.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fjdaryMachineTempInfo20.setStatus("current")


class _FjdaryMachineTempInfo21_Type(Integer32):
    """Custom type fjdaryMachineTempInfo21 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_FjdaryMachineTempInfo21_Type.__name__ = "Integer32"
_FjdaryMachineTempInfo21_Object = MibTableColumn
fjdaryMachineTempInfo21 = _FjdaryMachineTempInfo21_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 13, 3, 2, 1, 26),
    _FjdaryMachineTempInfo21_Type()
)
fjdaryMachineTempInfo21.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fjdaryMachineTempInfo21.setStatus("current")


class _FjdaryMachineTempInfo22_Type(Integer32):
    """Custom type fjdaryMachineTempInfo22 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_FjdaryMachineTempInfo22_Type.__name__ = "Integer32"
_FjdaryMachineTempInfo22_Object = MibTableColumn
fjdaryMachineTempInfo22 = _FjdaryMachineTempInfo22_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 13, 3, 2, 1, 27),
    _FjdaryMachineTempInfo22_Type()
)
fjdaryMachineTempInfo22.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fjdaryMachineTempInfo22.setStatus("current")


class _FjdaryMachineTempInfo23_Type(Integer32):
    """Custom type fjdaryMachineTempInfo23 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_FjdaryMachineTempInfo23_Type.__name__ = "Integer32"
_FjdaryMachineTempInfo23_Object = MibTableColumn
fjdaryMachineTempInfo23 = _FjdaryMachineTempInfo23_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 13, 3, 2, 1, 28),
    _FjdaryMachineTempInfo23_Type()
)
fjdaryMachineTempInfo23.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fjdaryMachineTempInfo23.setStatus("current")


class _FjdaryMachineTempInfo24_Type(Integer32):
    """Custom type fjdaryMachineTempInfo24 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_FjdaryMachineTempInfo24_Type.__name__ = "Integer32"
_FjdaryMachineTempInfo24_Object = MibTableColumn
fjdaryMachineTempInfo24 = _FjdaryMachineTempInfo24_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 13, 3, 2, 1, 29),
    _FjdaryMachineTempInfo24_Type()
)
fjdaryMachineTempInfo24.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fjdaryMachineTempInfo24.setStatus("current")
_FjdaryEncTemp_ObjectIdentity = ObjectIdentity
fjdaryEncTemp = _FjdaryEncTemp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 13, 4)
)


class _FjdaryEncTempCount_Type(Integer32):
    """Custom type fjdaryEncTempCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_FjdaryEncTempCount_Type.__name__ = "Integer32"
_FjdaryEncTempCount_Object = MibScalar
fjdaryEncTempCount = _FjdaryEncTempCount_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 13, 4, 1),
    _FjdaryEncTempCount_Type()
)
fjdaryEncTempCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fjdaryEncTempCount.setStatus("current")
_FjdaryEncTempTable_Object = MibTable
fjdaryEncTempTable = _FjdaryEncTempTable_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 13, 4, 2)
)
if mibBuilder.loadTexts:
    fjdaryEncTempTable.setStatus("current")
_FjdaryEncTempEntry_Object = MibTableRow
fjdaryEncTempEntry = _FjdaryEncTempEntry_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 13, 4, 2, 1)
)
fjdaryEncTempEntry.setIndexNames(
    (0, "FJDARY-E150", "fjdaryEncTempIndex"),
)
if mibBuilder.loadTexts:
    fjdaryEncTempEntry.setStatus("current")


class _FjdaryEncTempIndex_Type(Integer32):
    """Custom type fjdaryEncTempIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_FjdaryEncTempIndex_Type.__name__ = "Integer32"
_FjdaryEncTempIndex_Object = MibTableColumn
fjdaryEncTempIndex = _FjdaryEncTempIndex_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 13, 4, 2, 1, 1),
    _FjdaryEncTempIndex_Type()
)
fjdaryEncTempIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fjdaryEncTempIndex.setStatus("current")


class _FjdaryEncTempFlag_Type(Integer32):
    """Custom type fjdaryEncTempFlag based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              255)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 255),
          ("updating", 1),
          ("valid", 2))
    )


_FjdaryEncTempFlag_Type.__name__ = "Integer32"
_FjdaryEncTempFlag_Object = MibTableColumn
fjdaryEncTempFlag = _FjdaryEncTempFlag_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 13, 4, 2, 1, 2),
    _FjdaryEncTempFlag_Type()
)
fjdaryEncTempFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fjdaryEncTempFlag.setStatus("current")


class _FjdaryEncTempCmNum_Type(Integer32):
    """Custom type fjdaryEncTempCmNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_FjdaryEncTempCmNum_Type.__name__ = "Integer32"
_FjdaryEncTempCmNum_Object = MibTableColumn
fjdaryEncTempCmNum = _FjdaryEncTempCmNum_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 13, 4, 2, 1, 3),
    _FjdaryEncTempCmNum_Type()
)
fjdaryEncTempCmNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fjdaryEncTempCmNum.setStatus("current")


class _FjdaryEncTempDeId_Type(Integer32):
    """Custom type fjdaryEncTempDeId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_FjdaryEncTempDeId_Type.__name__ = "Integer32"
_FjdaryEncTempDeId_Object = MibTableColumn
fjdaryEncTempDeId = _FjdaryEncTempDeId_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 13, 4, 2, 1, 4),
    _FjdaryEncTempDeId_Type()
)
fjdaryEncTempDeId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fjdaryEncTempDeId.setStatus("current")


class _FjdaryEncTempTime_Type(Integer32):
    """Custom type fjdaryEncTempTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_FjdaryEncTempTime_Type.__name__ = "Integer32"
_FjdaryEncTempTime_Object = MibTableColumn
fjdaryEncTempTime = _FjdaryEncTempTime_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 13, 4, 2, 1, 5),
    _FjdaryEncTempTime_Type()
)
fjdaryEncTempTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fjdaryEncTempTime.setStatus("current")


class _FjdaryEncTempType_Type(Integer32):
    """Custom type fjdaryEncTempType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(16,
              32)
        )
    )
    namedValues = NamedValues(
        *(("ce", 16),
          ("de", 32))
    )


_FjdaryEncTempType_Type.__name__ = "Integer32"
_FjdaryEncTempType_Object = MibTableColumn
fjdaryEncTempType = _FjdaryEncTempType_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 13, 4, 2, 1, 6),
    _FjdaryEncTempType_Type()
)
fjdaryEncTempType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fjdaryEncTempType.setStatus("current")


class _FjdaryEncTempInfo0_Type(Integer32):
    """Custom type fjdaryEncTempInfo0 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_FjdaryEncTempInfo0_Type.__name__ = "Integer32"
_FjdaryEncTempInfo0_Object = MibTableColumn
fjdaryEncTempInfo0 = _FjdaryEncTempInfo0_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 13, 4, 2, 1, 7),
    _FjdaryEncTempInfo0_Type()
)
fjdaryEncTempInfo0.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fjdaryEncTempInfo0.setStatus("current")


class _FjdaryEncTempInfo1_Type(Integer32):
    """Custom type fjdaryEncTempInfo1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_FjdaryEncTempInfo1_Type.__name__ = "Integer32"
_FjdaryEncTempInfo1_Object = MibTableColumn
fjdaryEncTempInfo1 = _FjdaryEncTempInfo1_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 13, 4, 2, 1, 8),
    _FjdaryEncTempInfo1_Type()
)
fjdaryEncTempInfo1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fjdaryEncTempInfo1.setStatus("current")


class _FjdaryEncTempInfo2_Type(Integer32):
    """Custom type fjdaryEncTempInfo2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_FjdaryEncTempInfo2_Type.__name__ = "Integer32"
_FjdaryEncTempInfo2_Object = MibTableColumn
fjdaryEncTempInfo2 = _FjdaryEncTempInfo2_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 13, 4, 2, 1, 9),
    _FjdaryEncTempInfo2_Type()
)
fjdaryEncTempInfo2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fjdaryEncTempInfo2.setStatus("current")


class _FjdaryEncTempInfo3_Type(Integer32):
    """Custom type fjdaryEncTempInfo3 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_FjdaryEncTempInfo3_Type.__name__ = "Integer32"
_FjdaryEncTempInfo3_Object = MibTableColumn
fjdaryEncTempInfo3 = _FjdaryEncTempInfo3_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 13, 4, 2, 1, 10),
    _FjdaryEncTempInfo3_Type()
)
fjdaryEncTempInfo3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fjdaryEncTempInfo3.setStatus("current")


class _FjdaryEncTempInfo4_Type(Integer32):
    """Custom type fjdaryEncTempInfo4 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_FjdaryEncTempInfo4_Type.__name__ = "Integer32"
_FjdaryEncTempInfo4_Object = MibTableColumn
fjdaryEncTempInfo4 = _FjdaryEncTempInfo4_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 13, 4, 2, 1, 11),
    _FjdaryEncTempInfo4_Type()
)
fjdaryEncTempInfo4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fjdaryEncTempInfo4.setStatus("current")


class _FjdaryEncTempInfo5_Type(Integer32):
    """Custom type fjdaryEncTempInfo5 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_FjdaryEncTempInfo5_Type.__name__ = "Integer32"
_FjdaryEncTempInfo5_Object = MibTableColumn
fjdaryEncTempInfo5 = _FjdaryEncTempInfo5_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 13, 4, 2, 1, 12),
    _FjdaryEncTempInfo5_Type()
)
fjdaryEncTempInfo5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fjdaryEncTempInfo5.setStatus("current")


class _FjdaryEncTempInfo6_Type(Integer32):
    """Custom type fjdaryEncTempInfo6 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_FjdaryEncTempInfo6_Type.__name__ = "Integer32"
_FjdaryEncTempInfo6_Object = MibTableColumn
fjdaryEncTempInfo6 = _FjdaryEncTempInfo6_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 13, 4, 2, 1, 13),
    _FjdaryEncTempInfo6_Type()
)
fjdaryEncTempInfo6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fjdaryEncTempInfo6.setStatus("current")


class _FjdaryEncTempInfo7_Type(Integer32):
    """Custom type fjdaryEncTempInfo7 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_FjdaryEncTempInfo7_Type.__name__ = "Integer32"
_FjdaryEncTempInfo7_Object = MibTableColumn
fjdaryEncTempInfo7 = _FjdaryEncTempInfo7_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 13, 4, 2, 1, 14),
    _FjdaryEncTempInfo7_Type()
)
fjdaryEncTempInfo7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fjdaryEncTempInfo7.setStatus("current")


class _FjdaryEncTempInfo8_Type(Integer32):
    """Custom type fjdaryEncTempInfo8 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_FjdaryEncTempInfo8_Type.__name__ = "Integer32"
_FjdaryEncTempInfo8_Object = MibTableColumn
fjdaryEncTempInfo8 = _FjdaryEncTempInfo8_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 13, 4, 2, 1, 15),
    _FjdaryEncTempInfo8_Type()
)
fjdaryEncTempInfo8.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fjdaryEncTempInfo8.setStatus("current")


class _FjdaryEncTempInfo9_Type(Integer32):
    """Custom type fjdaryEncTempInfo9 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_FjdaryEncTempInfo9_Type.__name__ = "Integer32"
_FjdaryEncTempInfo9_Object = MibTableColumn
fjdaryEncTempInfo9 = _FjdaryEncTempInfo9_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 13, 4, 2, 1, 16),
    _FjdaryEncTempInfo9_Type()
)
fjdaryEncTempInfo9.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fjdaryEncTempInfo9.setStatus("current")


class _FjdaryEncTempInfo10_Type(Integer32):
    """Custom type fjdaryEncTempInfo10 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_FjdaryEncTempInfo10_Type.__name__ = "Integer32"
_FjdaryEncTempInfo10_Object = MibTableColumn
fjdaryEncTempInfo10 = _FjdaryEncTempInfo10_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 13, 4, 2, 1, 17),
    _FjdaryEncTempInfo10_Type()
)
fjdaryEncTempInfo10.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fjdaryEncTempInfo10.setStatus("current")


class _FjdaryEncTempInfo11_Type(Integer32):
    """Custom type fjdaryEncTempInfo11 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_FjdaryEncTempInfo11_Type.__name__ = "Integer32"
_FjdaryEncTempInfo11_Object = MibTableColumn
fjdaryEncTempInfo11 = _FjdaryEncTempInfo11_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 13, 4, 2, 1, 18),
    _FjdaryEncTempInfo11_Type()
)
fjdaryEncTempInfo11.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fjdaryEncTempInfo11.setStatus("current")


class _FjdaryEncTempInfo12_Type(Integer32):
    """Custom type fjdaryEncTempInfo12 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_FjdaryEncTempInfo12_Type.__name__ = "Integer32"
_FjdaryEncTempInfo12_Object = MibTableColumn
fjdaryEncTempInfo12 = _FjdaryEncTempInfo12_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 13, 4, 2, 1, 19),
    _FjdaryEncTempInfo12_Type()
)
fjdaryEncTempInfo12.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fjdaryEncTempInfo12.setStatus("current")


class _FjdaryEncTempInfo13_Type(Integer32):
    """Custom type fjdaryEncTempInfo13 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_FjdaryEncTempInfo13_Type.__name__ = "Integer32"
_FjdaryEncTempInfo13_Object = MibTableColumn
fjdaryEncTempInfo13 = _FjdaryEncTempInfo13_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 13, 4, 2, 1, 20),
    _FjdaryEncTempInfo13_Type()
)
fjdaryEncTempInfo13.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fjdaryEncTempInfo13.setStatus("current")


class _FjdaryEncTempInfo14_Type(Integer32):
    """Custom type fjdaryEncTempInfo14 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_FjdaryEncTempInfo14_Type.__name__ = "Integer32"
_FjdaryEncTempInfo14_Object = MibTableColumn
fjdaryEncTempInfo14 = _FjdaryEncTempInfo14_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 13, 4, 2, 1, 21),
    _FjdaryEncTempInfo14_Type()
)
fjdaryEncTempInfo14.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fjdaryEncTempInfo14.setStatus("current")


class _FjdaryEncTempInfo15_Type(Integer32):
    """Custom type fjdaryEncTempInfo15 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_FjdaryEncTempInfo15_Type.__name__ = "Integer32"
_FjdaryEncTempInfo15_Object = MibTableColumn
fjdaryEncTempInfo15 = _FjdaryEncTempInfo15_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 13, 4, 2, 1, 22),
    _FjdaryEncTempInfo15_Type()
)
fjdaryEncTempInfo15.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fjdaryEncTempInfo15.setStatus("current")


class _FjdaryEncTempInfo16_Type(Integer32):
    """Custom type fjdaryEncTempInfo16 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_FjdaryEncTempInfo16_Type.__name__ = "Integer32"
_FjdaryEncTempInfo16_Object = MibTableColumn
fjdaryEncTempInfo16 = _FjdaryEncTempInfo16_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 13, 4, 2, 1, 23),
    _FjdaryEncTempInfo16_Type()
)
fjdaryEncTempInfo16.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fjdaryEncTempInfo16.setStatus("current")


class _FjdaryEncTempInfo17_Type(Integer32):
    """Custom type fjdaryEncTempInfo17 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_FjdaryEncTempInfo17_Type.__name__ = "Integer32"
_FjdaryEncTempInfo17_Object = MibTableColumn
fjdaryEncTempInfo17 = _FjdaryEncTempInfo17_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 13, 4, 2, 1, 24),
    _FjdaryEncTempInfo17_Type()
)
fjdaryEncTempInfo17.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fjdaryEncTempInfo17.setStatus("current")


class _FjdaryEncTempInfo18_Type(Integer32):
    """Custom type fjdaryEncTempInfo18 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_FjdaryEncTempInfo18_Type.__name__ = "Integer32"
_FjdaryEncTempInfo18_Object = MibTableColumn
fjdaryEncTempInfo18 = _FjdaryEncTempInfo18_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 13, 4, 2, 1, 25),
    _FjdaryEncTempInfo18_Type()
)
fjdaryEncTempInfo18.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fjdaryEncTempInfo18.setStatus("current")


class _FjdaryEncTempInfo19_Type(Integer32):
    """Custom type fjdaryEncTempInfo19 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_FjdaryEncTempInfo19_Type.__name__ = "Integer32"
_FjdaryEncTempInfo19_Object = MibTableColumn
fjdaryEncTempInfo19 = _FjdaryEncTempInfo19_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 13, 4, 2, 1, 26),
    _FjdaryEncTempInfo19_Type()
)
fjdaryEncTempInfo19.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fjdaryEncTempInfo19.setStatus("current")


class _FjdaryEncTempInfo20_Type(Integer32):
    """Custom type fjdaryEncTempInfo20 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_FjdaryEncTempInfo20_Type.__name__ = "Integer32"
_FjdaryEncTempInfo20_Object = MibTableColumn
fjdaryEncTempInfo20 = _FjdaryEncTempInfo20_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 13, 4, 2, 1, 27),
    _FjdaryEncTempInfo20_Type()
)
fjdaryEncTempInfo20.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fjdaryEncTempInfo20.setStatus("current")


class _FjdaryEncTempInfo21_Type(Integer32):
    """Custom type fjdaryEncTempInfo21 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_FjdaryEncTempInfo21_Type.__name__ = "Integer32"
_FjdaryEncTempInfo21_Object = MibTableColumn
fjdaryEncTempInfo21 = _FjdaryEncTempInfo21_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 13, 4, 2, 1, 28),
    _FjdaryEncTempInfo21_Type()
)
fjdaryEncTempInfo21.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fjdaryEncTempInfo21.setStatus("current")


class _FjdaryEncTempInfo22_Type(Integer32):
    """Custom type fjdaryEncTempInfo22 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_FjdaryEncTempInfo22_Type.__name__ = "Integer32"
_FjdaryEncTempInfo22_Object = MibTableColumn
fjdaryEncTempInfo22 = _FjdaryEncTempInfo22_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 13, 4, 2, 1, 29),
    _FjdaryEncTempInfo22_Type()
)
fjdaryEncTempInfo22.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fjdaryEncTempInfo22.setStatus("current")


class _FjdaryEncTempInfo23_Type(Integer32):
    """Custom type fjdaryEncTempInfo23 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_FjdaryEncTempInfo23_Type.__name__ = "Integer32"
_FjdaryEncTempInfo23_Object = MibTableColumn
fjdaryEncTempInfo23 = _FjdaryEncTempInfo23_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 13, 4, 2, 1, 30),
    _FjdaryEncTempInfo23_Type()
)
fjdaryEncTempInfo23.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fjdaryEncTempInfo23.setStatus("current")


class _FjdaryEncTempInfo24_Type(Integer32):
    """Custom type fjdaryEncTempInfo24 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_FjdaryEncTempInfo24_Type.__name__ = "Integer32"
_FjdaryEncTempInfo24_Object = MibTableColumn
fjdaryEncTempInfo24 = _FjdaryEncTempInfo24_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 13, 4, 2, 1, 31),
    _FjdaryEncTempInfo24_Type()
)
fjdaryEncTempInfo24.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fjdaryEncTempInfo24.setStatus("current")
_FjdaryManagement_ObjectIdentity = ObjectIdentity
fjdaryManagement = _FjdaryManagement_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 14)
)
_FjdaryMgtMachineInfo_ObjectIdentity = ObjectIdentity
fjdaryMgtMachineInfo = _FjdaryMgtMachineInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 14, 1)
)


class _FjdaryMgtMachineStatus_Type(Integer32):
    """Custom type fjdaryMgtMachineStatus based on Integer32"""
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
        *(("failed", 5),
          ("ok", 3),
          ("unknown", 1),
          ("unused", 2),
          ("warning", 4))
    )


_FjdaryMgtMachineStatus_Type.__name__ = "Integer32"
_FjdaryMgtMachineStatus_Object = MibScalar
fjdaryMgtMachineStatus = _FjdaryMgtMachineStatus_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 14, 1, 1),
    _FjdaryMgtMachineStatus_Type()
)
fjdaryMgtMachineStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fjdaryMgtMachineStatus.setStatus("current")


class _FjdaryMgtMachineSubStatus_Type(Integer32):
    """Custom type fjdaryMgtMachineSubStatus based on Integer32"""
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
        *(("failed", 5),
          ("ok", 3),
          ("unknown", 1),
          ("unused", 2),
          ("warning", 4))
    )


_FjdaryMgtMachineSubStatus_Type.__name__ = "Integer32"
_FjdaryMgtMachineSubStatus_Object = MibScalar
fjdaryMgtMachineSubStatus = _FjdaryMgtMachineSubStatus_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 14, 1, 2),
    _FjdaryMgtMachineSubStatus_Type()
)
fjdaryMgtMachineSubStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fjdaryMgtMachineSubStatus.setStatus("current")


class _FjdaryMgtMaintenanceMode_Type(Integer32):
    """Custom type fjdaryMgtMaintenanceMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2))
    )


_FjdaryMgtMaintenanceMode_Type.__name__ = "Integer32"
_FjdaryMgtMaintenanceMode_Object = MibScalar
fjdaryMgtMaintenanceMode = _FjdaryMgtMaintenanceMode_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 14, 1, 3),
    _FjdaryMgtMaintenanceMode_Type()
)
fjdaryMgtMaintenanceMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fjdaryMgtMaintenanceMode.setStatus("current")


class _FjdaryMgtConfigInfo_Type(OctetString):
    """Custom type fjdaryMgtConfigInfo based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_FjdaryMgtConfigInfo_Type.__name__ = "OctetString"
_FjdaryMgtConfigInfo_Object = MibScalar
fjdaryMgtConfigInfo = _FjdaryMgtConfigInfo_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 14, 1, 4),
    _FjdaryMgtConfigInfo_Type()
)
fjdaryMgtConfigInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fjdaryMgtConfigInfo.setStatus("current")
_FjdaryMgtOpVolume_ObjectIdentity = ObjectIdentity
fjdaryMgtOpVolume = _FjdaryMgtOpVolume_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 14, 2)
)
_FjdaryMgtOpVolumeTable_Object = MibTable
fjdaryMgtOpVolumeTable = _FjdaryMgtOpVolumeTable_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 14, 2, 2)
)
if mibBuilder.loadTexts:
    fjdaryMgtOpVolumeTable.setStatus("current")
_FjdaryMgtOpVolumeEntry_Object = MibTableRow
fjdaryMgtOpVolumeEntry = _FjdaryMgtOpVolumeEntry_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 14, 2, 2, 1)
)
fjdaryMgtOpVolumeEntry.setIndexNames(
    (0, "FJDARY-E150", "fjdaryMgtOpVolumeNumber"),
)
if mibBuilder.loadTexts:
    fjdaryMgtOpVolumeEntry.setStatus("current")


class _FjdaryMgtOpVolumeNumber_Type(Integer32):
    """Custom type fjdaryMgtOpVolumeNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_FjdaryMgtOpVolumeNumber_Type.__name__ = "Integer32"
_FjdaryMgtOpVolumeNumber_Object = MibTableColumn
fjdaryMgtOpVolumeNumber = _FjdaryMgtOpVolumeNumber_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 14, 2, 2, 1, 1),
    _FjdaryMgtOpVolumeNumber_Type()
)
fjdaryMgtOpVolumeNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fjdaryMgtOpVolumeNumber.setStatus("current")


class _FjdaryMgtOpVolumeStatus_Type(Integer32):
    """Custom type fjdaryMgtOpVolumeStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              6,
              15)
        )
    )
    namedValues = NamedValues(
        *(("degraded", 3),
          ("dormant", 15),
          ("error", 6),
          ("ok", 2),
          ("unknown", 1))
    )


_FjdaryMgtOpVolumeStatus_Type.__name__ = "Integer32"
_FjdaryMgtOpVolumeStatus_Object = MibTableColumn
fjdaryMgtOpVolumeStatus = _FjdaryMgtOpVolumeStatus_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 14, 2, 2, 1, 2),
    _FjdaryMgtOpVolumeStatus_Type()
)
fjdaryMgtOpVolumeStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fjdaryMgtOpVolumeStatus.setStatus("current")


class _FjdaryMgtOpVolumeType_Type(Integer32):
    """Custom type fjdaryMgtOpVolumeType based on Integer32"""
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
        *(("open", 2),
          ("sdpv", 5),
          ("sdv", 3),
          ("tpv", 4),
          ("unknown", 1))
    )


_FjdaryMgtOpVolumeType_Type.__name__ = "Integer32"
_FjdaryMgtOpVolumeType_Object = MibTableColumn
fjdaryMgtOpVolumeType = _FjdaryMgtOpVolumeType_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 14, 2, 2, 1, 3),
    _FjdaryMgtOpVolumeType_Type()
)
fjdaryMgtOpVolumeType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fjdaryMgtOpVolumeType.setStatus("current")


class _FjdaryMgtOpVolumeCapacity_Type(Integer32):
    """Custom type fjdaryMgtOpVolumeCapacity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_FjdaryMgtOpVolumeCapacity_Type.__name__ = "Integer32"
_FjdaryMgtOpVolumeCapacity_Object = MibTableColumn
fjdaryMgtOpVolumeCapacity = _FjdaryMgtOpVolumeCapacity_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 14, 2, 2, 1, 4),
    _FjdaryMgtOpVolumeCapacity_Type()
)
fjdaryMgtOpVolumeCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fjdaryMgtOpVolumeCapacity.setStatus("current")


class _FjdaryMgtOpVolumeType2_Type(Integer32):
    """Custom type fjdaryMgtOpVolumeType2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("ftv", 6),
          ("open", 2),
          ("other", 1),
          ("sdpv", 5),
          ("sdv", 3),
          ("tpv", 4),
          ("wsv", 7))
    )


_FjdaryMgtOpVolumeType2_Type.__name__ = "Integer32"
_FjdaryMgtOpVolumeType2_Object = MibTableColumn
fjdaryMgtOpVolumeType2 = _FjdaryMgtOpVolumeType2_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 14, 2, 2, 1, 5),
    _FjdaryMgtOpVolumeType2_Type()
)
fjdaryMgtOpVolumeType2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fjdaryMgtOpVolumeType2.setStatus("current")


class _FjdaryMgtOpVolumeAttribute_Type(Integer32):
    """Custom type fjdaryMgtOpVolumeAttribute based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_FjdaryMgtOpVolumeAttribute_Type.__name__ = "Integer32"
_FjdaryMgtOpVolumeAttribute_Object = MibTableColumn
fjdaryMgtOpVolumeAttribute = _FjdaryMgtOpVolumeAttribute_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 14, 2, 2, 1, 6),
    _FjdaryMgtOpVolumeAttribute_Type()
)
fjdaryMgtOpVolumeAttribute.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fjdaryMgtOpVolumeAttribute.setStatus("current")
_FjdaryMgtRaidGrp_ObjectIdentity = ObjectIdentity
fjdaryMgtRaidGrp = _FjdaryMgtRaidGrp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 14, 3)
)
_FjdaryMgtRaidGrpTable_Object = MibTable
fjdaryMgtRaidGrpTable = _FjdaryMgtRaidGrpTable_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 14, 3, 2)
)
if mibBuilder.loadTexts:
    fjdaryMgtRaidGrpTable.setStatus("current")
_FjdaryMgtRaidGrpEntry_Object = MibTableRow
fjdaryMgtRaidGrpEntry = _FjdaryMgtRaidGrpEntry_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 14, 3, 2, 1)
)
fjdaryMgtRaidGrpEntry.setIndexNames(
    (0, "FJDARY-E150", "fjdaryMgtRaidGrpNumber"),
)
if mibBuilder.loadTexts:
    fjdaryMgtRaidGrpEntry.setStatus("current")


class _FjdaryMgtRaidGrpNumber_Type(Integer32):
    """Custom type fjdaryMgtRaidGrpNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_FjdaryMgtRaidGrpNumber_Type.__name__ = "Integer32"
_FjdaryMgtRaidGrpNumber_Object = MibTableColumn
fjdaryMgtRaidGrpNumber = _FjdaryMgtRaidGrpNumber_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 14, 3, 2, 1, 1),
    _FjdaryMgtRaidGrpNumber_Type()
)
fjdaryMgtRaidGrpNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fjdaryMgtRaidGrpNumber.setStatus("current")


class _FjdaryMgtRaidGrpStatus_Type(Integer32):
    """Custom type fjdaryMgtRaidGrpStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              6,
              15)
        )
    )
    namedValues = NamedValues(
        *(("degraded", 3),
          ("dormant", 15),
          ("error", 6),
          ("ok", 2),
          ("unknown", 1))
    )


_FjdaryMgtRaidGrpStatus_Type.__name__ = "Integer32"
_FjdaryMgtRaidGrpStatus_Object = MibTableColumn
fjdaryMgtRaidGrpStatus = _FjdaryMgtRaidGrpStatus_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 14, 3, 2, 1, 2),
    _FjdaryMgtRaidGrpStatus_Type()
)
fjdaryMgtRaidGrpStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fjdaryMgtRaidGrpStatus.setStatus("current")


class _FjdaryMgtRaidGrpRaidLevel_Type(Integer32):
    """Custom type fjdaryMgtRaidGrpRaidLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              5,
              6,
              10,
              50,
              100,
              106,
              255)
        )
    )
    namedValues = NamedValues(
        *(("raid0", 100),
          ("raid1", 1),
          ("raid10", 10),
          ("raid5", 5),
          ("raid50", 50),
          ("raid6", 6),
          ("raid6-fr", 106),
          ("unknown", 255))
    )


_FjdaryMgtRaidGrpRaidLevel_Type.__name__ = "Integer32"
_FjdaryMgtRaidGrpRaidLevel_Object = MibTableColumn
fjdaryMgtRaidGrpRaidLevel = _FjdaryMgtRaidGrpRaidLevel_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 14, 3, 2, 1, 3),
    _FjdaryMgtRaidGrpRaidLevel_Type()
)
fjdaryMgtRaidGrpRaidLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fjdaryMgtRaidGrpRaidLevel.setStatus("current")


class _FjdaryMgtRaidGrpCapacity_Type(Integer32):
    """Custom type fjdaryMgtRaidGrpCapacity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_FjdaryMgtRaidGrpCapacity_Type.__name__ = "Integer32"
_FjdaryMgtRaidGrpCapacity_Object = MibTableColumn
fjdaryMgtRaidGrpCapacity = _FjdaryMgtRaidGrpCapacity_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 14, 3, 2, 1, 4),
    _FjdaryMgtRaidGrpCapacity_Type()
)
fjdaryMgtRaidGrpCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fjdaryMgtRaidGrpCapacity.setStatus("current")


class _FjdaryTrapLinkStatusInfo_Type(Integer32):
    """Custom type fjdaryTrapLinkStatusInfo based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("linkdown", 2),
          ("linkup", 1))
    )


_FjdaryTrapLinkStatusInfo_Type.__name__ = "Integer32"
_FjdaryTrapLinkStatusInfo_Object = MibScalar
fjdaryTrapLinkStatusInfo = _FjdaryTrapLinkStatusInfo_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 21, 1, 150, 15),
    _FjdaryTrapLinkStatusInfo_Type()
)
fjdaryTrapLinkStatusInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fjdaryTrapLinkStatusInfo.setStatus("current")
_Application_ObjectIdentity = ObjectIdentity
application = _Application_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 211, 4)
)
_AplNetwork_ObjectIdentity = ObjectIdentity
aplNetwork = _AplNetwork_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 211, 4, 1)
)
_AplNetDevice_ObjectIdentity = ObjectIdentity
aplNetDevice = _AplNetDevice_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 211, 4, 1, 1)
)
_AplNetStorage_ObjectIdentity = ObjectIdentity
aplNetStorage = _AplNetStorage_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 211, 4, 1, 1, 126)
)
_AplNetNsp_ObjectIdentity = ObjectIdentity
aplNetNsp = _AplNetNsp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 211, 4, 1, 1, 126, 1)
)
_AplNetFjdarye150_ObjectIdentity = ObjectIdentity
aplNetFjdarye150 = _AplNetFjdarye150_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 211, 4, 1, 1, 126, 1, 150)
)
_AplNetFjdarye150Traps_ObjectIdentity = ObjectIdentity
aplNetFjdarye150Traps = _AplNetFjdarye150Traps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 211, 4, 1, 1, 126, 1, 150, 0)
)

# Managed Objects groups


# Notification objects

fjdarye150ItemFault = NotificationType(
    (1, 3, 6, 1, 4, 1, 211, 4, 1, 1, 126, 1, 150, 0, 2)
)
fjdarye150ItemFault.setObjects(
      *(("FJDARY-E150", "fjdaryTrapItemId"),
        ("FJDARY-E150", "fjdarySspMachineId"),
        ("FJDARY-E150", "fjdaryTrapMessage"))
)
if mibBuilder.loadTexts:
    fjdarye150ItemFault.setStatus(
        "current"
    )

fjdarye150BatteryExpiration = NotificationType(
    (1, 3, 6, 1, 4, 1, 211, 4, 1, 1, 126, 1, 150, 0, 3)
)
fjdarye150BatteryExpiration.setObjects(
      *(("FJDARY-E150", "fjdaryTrapItemId"),
        ("FJDARY-E150", "fjdarySspMachineId"),
        ("FJDARY-E150", "fjdaryTrapMessage"))
)
if mibBuilder.loadTexts:
    fjdarye150BatteryExpiration.setStatus(
        "current"
    )

fjdarye150ItemWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 211, 4, 1, 1, 126, 1, 150, 0, 5)
)
fjdarye150ItemWarning.setObjects(
      *(("FJDARY-E150", "fjdaryTrapItemId"),
        ("FJDARY-E150", "fjdarySspMachineId"),
        ("FJDARY-E150", "fjdaryTrapMessage"),
        ("FJDARY-E150", "fjdaryTrapWarningInfo"))
)
if mibBuilder.loadTexts:
    fjdarye150ItemWarning.setStatus(
        "current"
    )

fjdarye150SensorStatusChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 211, 4, 1, 1, 126, 1, 150, 0, 6)
)
fjdarye150SensorStatusChange.setObjects(
      *(("FJDARY-E150", "fjdaryTrapItemId"),
        ("FJDARY-E150", "fjdarySspMachineId"),
        ("FJDARY-E150", "fjdaryTrapSensorInfo"),
        ("FJDARY-E150", "fjdaryTrapMessage"))
)
if mibBuilder.loadTexts:
    fjdarye150SensorStatusChange.setStatus(
        "current"
    )

fjdarye150MaintenanceRequired = NotificationType(
    (1, 3, 6, 1, 4, 1, 211, 4, 1, 1, 126, 1, 150, 0, 7)
)
fjdarye150MaintenanceRequired.setObjects(
      *(("FJDARY-E150", "fjdarySspMachineId"),
        ("FJDARY-E150", "fjdaryTrapMaintenanceInfo"),
        ("FJDARY-E150", "fjdaryTrapMessage"))
)
if mibBuilder.loadTexts:
    fjdarye150MaintenanceRequired.setStatus(
        "current"
    )

fjdarye150Information = NotificationType(
    (1, 3, 6, 1, 4, 1, 211, 4, 1, 1, 126, 1, 150, 0, 9)
)
fjdarye150Information.setObjects(
      *(("FJDARY-E150", "fjdarySspMachineId"),
        ("FJDARY-E150", "fjdaryTrapMessage"))
)
if mibBuilder.loadTexts:
    fjdarye150Information.setStatus(
        "current"
    )

fjdarye150CaPortLinkStatusChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 211, 4, 1, 1, 126, 1, 150, 0, 10)
)
fjdarye150CaPortLinkStatusChange.setObjects(
      *(("FJDARY-E150", "fjdaryTrapItemId"),
        ("FJDARY-E150", "fjdarySspMachineId"),
        ("FJDARY-E150", "fjdaryTrapLinkStatusInfo"),
        ("FJDARY-E150", "fjdaryTrapMessage"))
)
if mibBuilder.loadTexts:
    fjdarye150CaPortLinkStatusChange.setStatus(
        "current"
    )

fjdarye150StorageClusterEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 211, 4, 1, 1, 126, 1, 150, 0, 11)
)
fjdarye150StorageClusterEvent.setObjects(
      *(("FJDARY-E150", "fjdarySspMachineId"),
        ("FJDARY-E150", "fjdaryTrapMaintenanceInfo"),
        ("FJDARY-E150", "fjdaryTrapMessage"))
)
if mibBuilder.loadTexts:
    fjdarye150StorageClusterEvent.setStatus(
        "current"
    )

fjdarye150StorageClusterInformation = NotificationType(
    (1, 3, 6, 1, 4, 1, 211, 4, 1, 1, 126, 1, 150, 0, 12)
)
fjdarye150StorageClusterInformation.setObjects(
      *(("FJDARY-E150", "fjdarySspMachineId"),
        ("FJDARY-E150", "fjdaryTrapMessage"))
)
if mibBuilder.loadTexts:
    fjdarye150StorageClusterInformation.setStatus(
        "current"
    )

fjdarye150ItemFaultToNormal = NotificationType(
    (1, 3, 6, 1, 4, 1, 211, 4, 1, 1, 126, 1, 150, 0, 22)
)
fjdarye150ItemFaultToNormal.setObjects(
      *(("FJDARY-E150", "fjdaryTrapItemId"),
        ("FJDARY-E150", "fjdarySspMachineId"),
        ("FJDARY-E150", "fjdaryTrapMessage"))
)
if mibBuilder.loadTexts:
    fjdarye150ItemFaultToNormal.setStatus(
        "current"
    )

fjdarye150ItemWarningToNormal = NotificationType(
    (1, 3, 6, 1, 4, 1, 211, 4, 1, 1, 126, 1, 150, 0, 25)
)
fjdarye150ItemWarningToNormal.setObjects(
      *(("FJDARY-E150", "fjdaryTrapItemId"),
        ("FJDARY-E150", "fjdarySspMachineId"),
        ("FJDARY-E150", "fjdaryTrapMessage"),
        ("FJDARY-E150", "fjdaryTrapWarningInfo"))
)
if mibBuilder.loadTexts:
    fjdarye150ItemWarningToNormal.setStatus(
        "current"
    )

fjdarye150SensorStatusChangeToNormal = NotificationType(
    (1, 3, 6, 1, 4, 1, 211, 4, 1, 1, 126, 1, 150, 0, 26)
)
fjdarye150SensorStatusChangeToNormal.setObjects(
      *(("FJDARY-E150", "fjdaryTrapItemId"),
        ("FJDARY-E150", "fjdarySspMachineId"),
        ("FJDARY-E150", "fjdaryTrapSensorInfo"),
        ("FJDARY-E150", "fjdaryTrapMessage"))
)
if mibBuilder.loadTexts:
    fjdarye150SensorStatusChangeToNormal.setStatus(
        "current"
    )

fjdarye150Error = NotificationType(
    (1, 3, 6, 1, 4, 1, 211, 4, 1, 1, 126, 1, 150, 0, 50)
)
fjdarye150Error.setObjects(
      *(("FJDARY-E150", "fjdarySspMachineId"),
        ("FJDARY-E150", "fjdaryTrapMessage"))
)
if mibBuilder.loadTexts:
    fjdarye150Error.setStatus(
        "current"
    )

fjdarye150Warning = NotificationType(
    (1, 3, 6, 1, 4, 1, 211, 4, 1, 1, 126, 1, 150, 0, 51)
)
fjdarye150Warning.setObjects(
      *(("FJDARY-E150", "fjdarySspMachineId"),
        ("FJDARY-E150", "fjdaryTrapMessage"))
)
if mibBuilder.loadTexts:
    fjdarye150Warning.setStatus(
        "current"
    )

fjdarye150QuotaLimitExceeded = NotificationType(
    (1, 3, 6, 1, 4, 1, 211, 4, 1, 1, 126, 1, 150, 0, 60)
)
fjdarye150QuotaLimitExceeded.setObjects(
      *(("FJDARY-E150", "fjdarySspMachineId"),
        ("FJDARY-E150", "fjdaryTrapMessage"))
)
if mibBuilder.loadTexts:
    fjdarye150QuotaLimitExceeded.setStatus(
        "current"
    )

fjdarye150QuotaWarningExceeded = NotificationType(
    (1, 3, 6, 1, 4, 1, 211, 4, 1, 1, 126, 1, 150, 0, 61)
)
fjdarye150QuotaWarningExceeded.setObjects(
      *(("FJDARY-E150", "fjdarySspMachineId"),
        ("FJDARY-E150", "fjdaryTrapMessage"))
)
if mibBuilder.loadTexts:
    fjdarye150QuotaWarningExceeded.setStatus(
        "current"
    )

fjdarye150QuotaNormal = NotificationType(
    (1, 3, 6, 1, 4, 1, 211, 4, 1, 1, 126, 1, 150, 0, 62)
)
fjdarye150QuotaNormal.setObjects(
      *(("FJDARY-E150", "fjdarySspMachineId"),
        ("FJDARY-E150", "fjdaryTrapMessage"))
)
if mibBuilder.loadTexts:
    fjdarye150QuotaNormal.setStatus(
        "current"
    )

fjdarye150SnapshotInformation = NotificationType(
    (1, 3, 6, 1, 4, 1, 211, 4, 1, 1, 126, 1, 150, 0, 63)
)
fjdarye150SnapshotInformation.setObjects(
      *(("FJDARY-E150", "fjdarySspMachineId"),
        ("FJDARY-E150", "fjdaryTrapMessage"))
)
if mibBuilder.loadTexts:
    fjdarye150SnapshotInformation.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "FJDARY-E150",
    **{"FjdaryComponentStatus": FjdaryComponentStatus,
       "fujitsu": fujitsu,
       "product": product,
       "storage": storage,
       "nsp": nsp,
       "fjdarye150": fjdarye150,
       "fjdarySsp": fjdarySsp,
       "fjdarySspMachineId": fjdarySspMachineId,
       "fjdarySspConfigDate": fjdarySspConfigDate,
       "fjdarySspWwnn": fjdarySspWwnn,
       "fjdarySspVenderId": fjdarySspVenderId,
       "fjdarySspProductId": fjdarySspProductId,
       "fjdarySspBoxId": fjdarySspBoxId,
       "fjdarySspMaintenanceServiceLevel": fjdarySspMaintenanceServiceLevel,
       "fjdaryPconfig": fjdaryPconfig,
       "fjdaryCm": fjdaryCm,
       "fjdaryCmCount": fjdaryCmCount,
       "fjdaryCmTable": fjdaryCmTable,
       "fjdaryCmEntry": fjdaryCmEntry,
       "fjdaryCmIndex": fjdaryCmIndex,
       "fjdaryCmItemId": fjdaryCmItemId,
       "fjdaryCmStatus": fjdaryCmStatus,
       "fjdaryCmSubStatus": fjdaryCmSubStatus,
       "fjdaryCmModuleId": fjdaryCmModuleId,
       "fjdaryCmRole": fjdaryCmRole,
       "fjdaryCmPartNo": fjdaryCmPartNo,
       "fjdaryCmSerialNo": fjdaryCmSerialNo,
       "fjdaryCmRevision": fjdaryCmRevision,
       "fjdaryCmcpu": fjdaryCmcpu,
       "fjdaryCmcpuCount": fjdaryCmcpuCount,
       "fjdaryCmcpuTable": fjdaryCmcpuTable,
       "fjdaryCmcpuEntry": fjdaryCmcpuEntry,
       "fjdaryCmcpuIndex": fjdaryCmcpuIndex,
       "fjdaryCmcpuItemId": fjdaryCmcpuItemId,
       "fjdaryCmcpuStatus": fjdaryCmcpuStatus,
       "fjdaryCmcpuSubStatus": fjdaryCmcpuSubStatus,
       "fjdaryCmcpuModuleId": fjdaryCmcpuModuleId,
       "fjdaryCmcpuRole": fjdaryCmcpuRole,
       "fjdaryCmcpuClock": fjdaryCmcpuClock,
       "fjdaryCa": fjdaryCa,
       "fjdaryCaCount": fjdaryCaCount,
       "fjdaryCaTable": fjdaryCaTable,
       "fjdaryCaEntry": fjdaryCaEntry,
       "fjdaryCaIndex": fjdaryCaIndex,
       "fjdaryCaItemId": fjdaryCaItemId,
       "fjdaryCaStatus": fjdaryCaStatus,
       "fjdaryCaSubStatus": fjdaryCaSubStatus,
       "fjdaryCaModuleId": fjdaryCaModuleId,
       "fjdaryCaType": fjdaryCaType,
       "fjdaryCmmemory": fjdaryCmmemory,
       "fjdaryCmmemoryCount": fjdaryCmmemoryCount,
       "fjdaryCmmemoryTable": fjdaryCmmemoryTable,
       "fjdaryCmmemoryEntry": fjdaryCmmemoryEntry,
       "fjdaryCmmemoryIndex": fjdaryCmmemoryIndex,
       "fjdaryCmmemoryItemId": fjdaryCmmemoryItemId,
       "fjdaryCmmemoryStatus": fjdaryCmmemoryStatus,
       "fjdaryCmmemorySubStatus": fjdaryCmmemorySubStatus,
       "fjdaryCmmemoryCapacity": fjdaryCmmemoryCapacity,
       "fjdaryCmmemoryPartNo": fjdaryCmmemoryPartNo,
       "fjdaryCmmemorySerialNo": fjdaryCmmemorySerialNo,
       "fjdaryBud": fjdaryBud,
       "fjdaryBudCount": fjdaryBudCount,
       "fjdaryBudTable": fjdaryBudTable,
       "fjdaryBudEntry": fjdaryBudEntry,
       "fjdaryBudIndex": fjdaryBudIndex,
       "fjdaryBudItemId": fjdaryBudItemId,
       "fjdaryBudStatus": fjdaryBudStatus,
       "fjdaryBudSubStatus": fjdaryBudSubStatus,
       "fjdaryCmfan": fjdaryCmfan,
       "fjdaryCmfanCount": fjdaryCmfanCount,
       "fjdaryCmfanTable": fjdaryCmfanTable,
       "fjdaryCmfanEntry": fjdaryCmfanEntry,
       "fjdaryCmfanIndex": fjdaryCmfanIndex,
       "fjdaryCmfanItemId": fjdaryCmfanItemId,
       "fjdaryCmfanStatus": fjdaryCmfanStatus,
       "fjdaryCmfanSubStatus": fjdaryCmfanSubStatus,
       "fjdaryBcu": fjdaryBcu,
       "fjdaryBcuCount": fjdaryBcuCount,
       "fjdaryBcuTable": fjdaryBcuTable,
       "fjdaryBcuEntry": fjdaryBcuEntry,
       "fjdaryBcuIndex": fjdaryBcuIndex,
       "fjdaryBcuItemId": fjdaryBcuItemId,
       "fjdaryBcuStatus": fjdaryBcuStatus,
       "fjdaryBcuSubStatus": fjdaryBcuSubStatus,
       "fjdaryBtu": fjdaryBtu,
       "fjdaryBtuCount": fjdaryBtuCount,
       "fjdaryBtuTable": fjdaryBtuTable,
       "fjdaryBtuEntry": fjdaryBtuEntry,
       "fjdaryBtuIndex": fjdaryBtuIndex,
       "fjdaryBtuItemId": fjdaryBtuItemId,
       "fjdaryBtuStatus": fjdaryBtuStatus,
       "fjdaryBtuSubStatus": fjdaryBtuSubStatus,
       "fjdaryScu": fjdaryScu,
       "fjdaryScuCount": fjdaryScuCount,
       "fjdaryScuTable": fjdaryScuTable,
       "fjdaryScuEntry": fjdaryScuEntry,
       "fjdaryScuIndex": fjdaryScuIndex,
       "fjdaryScuItemId": fjdaryScuItemId,
       "fjdaryScuStatus": fjdaryScuStatus,
       "fjdaryScuSubStatus": fjdaryScuSubStatus,
       "fjdaryScuVoltage": fjdaryScuVoltage,
       "fjdaryScuPartNo": fjdaryScuPartNo,
       "fjdaryScuSerialNo": fjdaryScuSerialNo,
       "fjdaryScuRevision": fjdaryScuRevision,
       "fjdaryCe": fjdaryCe,
       "fjdaryCeCount": fjdaryCeCount,
       "fjdaryCeTable": fjdaryCeTable,
       "fjdaryCeEntry": fjdaryCeEntry,
       "fjdaryCeIndex": fjdaryCeIndex,
       "fjdaryCeItemId": fjdaryCeItemId,
       "fjdaryCeStatus": fjdaryCeStatus,
       "fjdaryCeSubStatus": fjdaryCeSubStatus,
       "fjdaryCeinletthml": fjdaryCeinletthml,
       "fjdaryCeinletthmlCount": fjdaryCeinletthmlCount,
       "fjdaryCeinletthmlTable": fjdaryCeinletthmlTable,
       "fjdaryCeinletthmlEntry": fjdaryCeinletthmlEntry,
       "fjdaryCeinletthmlIndex": fjdaryCeinletthmlIndex,
       "fjdaryCeinletthmlItemId": fjdaryCeinletthmlItemId,
       "fjdaryCeinletthmlStatus": fjdaryCeinletthmlStatus,
       "fjdaryCeinletthmlSubStatus": fjdaryCeinletthmlSubStatus,
       "fjdaryCethml": fjdaryCethml,
       "fjdaryCethmlCount": fjdaryCethmlCount,
       "fjdaryCethmlTable": fjdaryCethmlTable,
       "fjdaryCethmlEntry": fjdaryCethmlEntry,
       "fjdaryCethmlIndex": fjdaryCethmlIndex,
       "fjdaryCethmlItemId": fjdaryCethmlItemId,
       "fjdaryCethmlStatus": fjdaryCethmlStatus,
       "fjdaryCethmlSubStatus": fjdaryCethmlSubStatus,
       "fjdaryCpsu": fjdaryCpsu,
       "fjdaryCpsuCount": fjdaryCpsuCount,
       "fjdaryCpsuTable": fjdaryCpsuTable,
       "fjdaryCpsuEntry": fjdaryCpsuEntry,
       "fjdaryCpsuIndex": fjdaryCpsuIndex,
       "fjdaryCpsuItemId": fjdaryCpsuItemId,
       "fjdaryCpsuStatus": fjdaryCpsuStatus,
       "fjdaryCpsuSubStatus": fjdaryCpsuSubStatus,
       "fjdaryCpsuPartNo": fjdaryCpsuPartNo,
       "fjdaryCpsuSerialNo": fjdaryCpsuSerialNo,
       "fjdaryCpsuRevision": fjdaryCpsuRevision,
       "fjdaryDe": fjdaryDe,
       "fjdaryDeCount": fjdaryDeCount,
       "fjdaryDeTable": fjdaryDeTable,
       "fjdaryDeEntry": fjdaryDeEntry,
       "fjdaryDeIndex": fjdaryDeIndex,
       "fjdaryDeItemId": fjdaryDeItemId,
       "fjdaryDeStatus": fjdaryDeStatus,
       "fjdaryDeSubStatus": fjdaryDeSubStatus,
       "fjdaryDeId": fjdaryDeId,
       "fjdaryDeType": fjdaryDeType,
       "fjdaryIom": fjdaryIom,
       "fjdaryIomCount": fjdaryIomCount,
       "fjdaryIomTable": fjdaryIomTable,
       "fjdaryIomEntry": fjdaryIomEntry,
       "fjdaryIomIndex": fjdaryIomIndex,
       "fjdaryIomItemId": fjdaryIomItemId,
       "fjdaryIomStatus": fjdaryIomStatus,
       "fjdaryIomSubStatus": fjdaryIomSubStatus,
       "fjdaryIomFirmInfo": fjdaryIomFirmInfo,
       "fjdaryIomPartNo": fjdaryIomPartNo,
       "fjdaryIomSerialNo": fjdaryIomSerialNo,
       "fjdaryIomRevision": fjdaryIomRevision,
       "fjdaryPsu": fjdaryPsu,
       "fjdaryPsuCount": fjdaryPsuCount,
       "fjdaryPsuTable": fjdaryPsuTable,
       "fjdaryPsuEntry": fjdaryPsuEntry,
       "fjdaryPsuIndex": fjdaryPsuIndex,
       "fjdaryPsuItemId": fjdaryPsuItemId,
       "fjdaryPsuStatus": fjdaryPsuStatus,
       "fjdaryPsuSubStatus": fjdaryPsuSubStatus,
       "fjdaryPsuPartNo": fjdaryPsuPartNo,
       "fjdaryPsuSerialNo": fjdaryPsuSerialNo,
       "fjdaryPsuRevision": fjdaryPsuRevision,
       "fjdaryDeinletthml": fjdaryDeinletthml,
       "fjdaryDeinletthmlCount": fjdaryDeinletthmlCount,
       "fjdaryDeinletthmlTable": fjdaryDeinletthmlTable,
       "fjdaryDeinletthmlEntry": fjdaryDeinletthmlEntry,
       "fjdaryDeinletthmlIndex": fjdaryDeinletthmlIndex,
       "fjdaryDeinletthmlItemId": fjdaryDeinletthmlItemId,
       "fjdaryDeinletthmlStatus": fjdaryDeinletthmlStatus,
       "fjdaryDeinletthmlSubStatus": fjdaryDeinletthmlSubStatus,
       "fjdaryDethml": fjdaryDethml,
       "fjdaryDethmlCount": fjdaryDethmlCount,
       "fjdaryDethmlTable": fjdaryDethmlTable,
       "fjdaryDethmlEntry": fjdaryDethmlEntry,
       "fjdaryDethmlIndex": fjdaryDethmlIndex,
       "fjdaryDethmlItemId": fjdaryDethmlItemId,
       "fjdaryDethmlStatus": fjdaryDethmlStatus,
       "fjdaryDethmlSubStatus": fjdaryDethmlSubStatus,
       "fjdaryDisk": fjdaryDisk,
       "fjdaryDiskCount": fjdaryDiskCount,
       "fjdaryDiskTable": fjdaryDiskTable,
       "fjdaryDiskEntry": fjdaryDiskEntry,
       "fjdaryDiskIndex": fjdaryDiskIndex,
       "fjdaryDiskItemId": fjdaryDiskItemId,
       "fjdaryDiskStatus": fjdaryDiskStatus,
       "fjdaryDiskSubStatus": fjdaryDiskSubStatus,
       "fjdaryDiskCompStatus": fjdaryDiskCompStatus,
       "fjdaryDiskCompSubStatus": fjdaryDiskCompSubStatus,
       "fjdaryDiskPlun": fjdaryDiskPlun,
       "fjdaryDiskPurpose": fjdaryDiskPurpose,
       "fjdaryDiskType": fjdaryDiskType,
       "fjdaryDiskWwn": fjdaryDiskWwn,
       "fjdaryDiskVenderId": fjdaryDiskVenderId,
       "fjdaryDiskProductId": fjdaryDiskProductId,
       "fjdaryDiskFwRevision": fjdaryDiskFwRevision,
       "fjdaryDiskDateCode": fjdaryDiskDateCode,
       "fjdaryDiskCfgRevision": fjdaryDiskCfgRevision,
       "fjdaryDiskSize": fjdaryDiskSize,
       "fjdaryLanport": fjdaryLanport,
       "fjdaryLanportCount": fjdaryLanportCount,
       "fjdaryLanportTable": fjdaryLanportTable,
       "fjdaryLanportEntry": fjdaryLanportEntry,
       "fjdaryLanportIndex": fjdaryLanportIndex,
       "fjdaryLanportStatus0": fjdaryLanportStatus0,
       "fjdaryLanportStatus1": fjdaryLanportStatus1,
       "fjdaryLanportStatus2": fjdaryLanportStatus2,
       "fjdaryLanportHwAdTable": fjdaryLanportHwAdTable,
       "fjdaryLanportHwAdEntry": fjdaryLanportHwAdEntry,
       "fjdaryLanportHwAdIndex": fjdaryLanportHwAdIndex,
       "fjdaryLanportHwAddress0": fjdaryLanportHwAddress0,
       "fjdaryLanportHwAddress1": fjdaryLanportHwAddress1,
       "fjdaryLanportHwAddress2": fjdaryLanportHwAddress2,
       "fjdaryFem": fjdaryFem,
       "fjdaryFemCount": fjdaryFemCount,
       "fjdaryFemTable": fjdaryFemTable,
       "fjdaryFemEntry": fjdaryFemEntry,
       "fjdaryFemIndex": fjdaryFemIndex,
       "fjdaryFemItemId": fjdaryFemItemId,
       "fjdaryFemStatus": fjdaryFemStatus,
       "fjdaryFemSubStatus": fjdaryFemSubStatus,
       "fjdaryPfm": fjdaryPfm,
       "fjdaryPfmCount": fjdaryPfmCount,
       "fjdaryPfmTable": fjdaryPfmTable,
       "fjdaryPfmEntry": fjdaryPfmEntry,
       "fjdaryPfmIndex": fjdaryPfmIndex,
       "fjdaryPfmItemId": fjdaryPfmItemId,
       "fjdaryPfmStatus": fjdaryPfmStatus,
       "fjdaryPfmSubStatus": fjdaryPfmSubStatus,
       "fjdaryLconfig": fjdaryLconfig,
       "fjdaryCaPort": fjdaryCaPort,
       "fjdaryCaPortCount": fjdaryCaPortCount,
       "fjdaryCaPortTable": fjdaryCaPortTable,
       "fjdaryCaPortEntry": fjdaryCaPortEntry,
       "fjdaryCaPortIndex": fjdaryCaPortIndex,
       "fjdaryCaPortPortInfo": fjdaryCaPortPortInfo,
       "fjdaryCaPortiscsiInfo": fjdaryCaPortiscsiInfo,
       "fjdaryCaPortiscsiName": fjdaryCaPortiscsiName,
       "fjdaryCaPortiscsiAliasName": fjdaryCaPortiscsiAliasName,
       "fjdaryCaPortiscsiIpAddress": fjdaryCaPortiscsiIpAddress,
       "fjdaryCaPortiscsiSubnetMask": fjdaryCaPortiscsiSubnetMask,
       "fjdaryCaPortiscsiIsnsServer": fjdaryCaPortiscsiIsnsServer,
       "fjdaryCaPortMode": fjdaryCaPortMode,
       "fjdaryOlu": fjdaryOlu,
       "fjdaryOluCount": fjdaryOluCount,
       "fjdaryOluTable": fjdaryOluTable,
       "fjdaryOluEntry": fjdaryOluEntry,
       "fjdaryOluIndex": fjdaryOluIndex,
       "fjdaryOluInfoTable": fjdaryOluInfoTable,
       "fjdarySlu": fjdarySlu,
       "fjdarySluCount": fjdarySluCount,
       "fjdarySluTable": fjdarySluTable,
       "fjdarySluEntry": fjdarySluEntry,
       "fjdarySluIndex": fjdarySluIndex,
       "fjdarySluInfoTable": fjdarySluInfoTable,
       "fjdaryRlu": fjdaryRlu,
       "fjdaryRluCount": fjdaryRluCount,
       "fjdaryRluTable": fjdaryRluTable,
       "fjdaryRluEntry": fjdaryRluEntry,
       "fjdaryRluIndex": fjdaryRluIndex,
       "fjdaryRluInfoTable0": fjdaryRluInfoTable0,
       "fjdaryRluInfoTable1": fjdaryRluInfoTable1,
       "fjdaryRluInfoTable2": fjdaryRluInfoTable2,
       "fjdaryRluInfoTable3": fjdaryRluInfoTable3,
       "fjdaryDlu": fjdaryDlu,
       "fjdaryDluCount": fjdaryDluCount,
       "fjdaryDluTable": fjdaryDluTable,
       "fjdaryDluEntry": fjdaryDluEntry,
       "fjdaryDluIndex": fjdaryDluIndex,
       "fjdaryDluInfoTable": fjdaryDluInfoTable,
       "fjdaryMlu": fjdaryMlu,
       "fjdaryMluCount": fjdaryMluCount,
       "fjdaryMluTable": fjdaryMluTable,
       "fjdaryMluEntry": fjdaryMluEntry,
       "fjdaryMluIndex": fjdaryMluIndex,
       "fjdaryMluInfoTable": fjdaryMluInfoTable,
       "fjdaryOpenmap": fjdaryOpenmap,
       "fjdaryOpenmapCount": fjdaryOpenmapCount,
       "fjdaryOpenmapTable": fjdaryOpenmapTable,
       "fjdaryOpenmapEntry": fjdaryOpenmapEntry,
       "fjdaryOpenmapIndex": fjdaryOpenmapIndex,
       "fjdaryOpenmapInfo": fjdaryOpenmapInfo,
       "fjdaryOpenmapHostTable0": fjdaryOpenmapHostTable0,
       "fjdaryOpenmapHostTable1": fjdaryOpenmapHostTable1,
       "fjdaryOpenmapHostTable2": fjdaryOpenmapHostTable2,
       "fjdaryOpenmapHostTable3": fjdaryOpenmapHostTable3,
       "fjdaryOpenmapHostTable4": fjdaryOpenmapHostTable4,
       "fjdaryOpenmapHostTable5": fjdaryOpenmapHostTable5,
       "fjdaryOpenmapHostTable6": fjdaryOpenmapHostTable6,
       "fjdaryOpenmapHostTable7": fjdaryOpenmapHostTable7,
       "fjdaryLunmap": fjdaryLunmap,
       "fjdaryLunmapCount": fjdaryLunmapCount,
       "fjdaryLunmapTable": fjdaryLunmapTable,
       "fjdaryLunmapEntry": fjdaryLunmapEntry,
       "fjdaryLunmapIndex": fjdaryLunmapIndex,
       "fjdaryLunmapInfo": fjdaryLunmapInfo,
       "fjdaryLunmapTable0": fjdaryLunmapTable0,
       "fjdaryLunmapTable1": fjdaryLunmapTable1,
       "fjdaryLunmapTable2": fjdaryLunmapTable2,
       "fjdaryLunmapTable3": fjdaryLunmapTable3,
       "fjdaryAffinityGrp": fjdaryAffinityGrp,
       "fjdaryAffinityGrpCount": fjdaryAffinityGrpCount,
       "fjdaryAffinityGrpTable": fjdaryAffinityGrpTable,
       "fjdaryAffinityGrpEntry": fjdaryAffinityGrpEntry,
       "fjdaryAffinityGrpIndex": fjdaryAffinityGrpIndex,
       "fjdaryAffinityGrpInfo": fjdaryAffinityGrpInfo,
       "fjdaryAffinityGrpTable0": fjdaryAffinityGrpTable0,
       "fjdaryAffinityGrpTable1": fjdaryAffinityGrpTable1,
       "fjdaryAffinityGrpTable2": fjdaryAffinityGrpTable2,
       "fjdaryAffinityGrpTable3": fjdaryAffinityGrpTable3,
       "fjdaryHostwwn": fjdaryHostwwn,
       "fjdaryHostwwnCount": fjdaryHostwwnCount,
       "fjdaryHostwwnTable": fjdaryHostwwnTable,
       "fjdaryHostwwnEntry": fjdaryHostwwnEntry,
       "fjdaryHostwwnIndex": fjdaryHostwwnIndex,
       "fjdaryHostwwnWWN": fjdaryHostwwnWWN,
       "fjdaryResetpath": fjdaryResetpath,
       "fjdaryResetpathCount": fjdaryResetpathCount,
       "fjdaryResetpathTable": fjdaryResetpathTable,
       "fjdaryResetpathEntry": fjdaryResetpathEntry,
       "fjdaryResetpathIndex": fjdaryResetpathIndex,
       "fjdaryResetpathGroup": fjdaryResetpathGroup,
       "fjdaryHostiscsi": fjdaryHostiscsi,
       "fjdaryHostiscsiCount": fjdaryHostiscsiCount,
       "fjdaryHostiscsiTable": fjdaryHostiscsiTable,
       "fjdaryHostiscsiEntry": fjdaryHostiscsiEntry,
       "fjdaryHostiscsiIndex": fjdaryHostiscsiIndex,
       "fjdaryHostiscsiDefine": fjdaryHostiscsiDefine,
       "fjdaryHostiscsiName": fjdaryHostiscsiName,
       "fjdaryHostiscsiAliasName": fjdaryHostiscsiAliasName,
       "fjdaryHostiscsiIpAddress": fjdaryHostiscsiIpAddress,
       "fjdaryHostResponse": fjdaryHostResponse,
       "fjdaryHostResponseCount": fjdaryHostResponseCount,
       "fjdaryHostResponseTable": fjdaryHostResponseTable,
       "fjdaryHostResponseEntry": fjdaryHostResponseEntry,
       "fjdaryHostResponseIndex": fjdaryHostResponseIndex,
       "fjdaryHostResponseInfoTable": fjdaryHostResponseInfoTable,
       "fjdaryFirm": fjdaryFirm,
       "fjdaryFirmTotal": fjdaryFirmTotal,
       "fjdaryPerformance": fjdaryPerformance,
       "fjdaryPfInfo": fjdaryPfInfo,
       "fjdaryPfInfoVersion": fjdaryPfInfoVersion,
       "fjdaryPfInfoLevel": fjdaryPfInfoLevel,
       "fjdaryPfInfoIntervalTime": fjdaryPfInfoIntervalTime,
       "fjdaryPfInfoUpdateTime": fjdaryPfInfoUpdateTime,
       "fjdaryPfInfoDataValid": fjdaryPfInfoDataValid,
       "fjdaryPfOlu": fjdaryPfOlu,
       "fjdaryPfOluCount": fjdaryPfOluCount,
       "fjdaryPfOluTable": fjdaryPfOluTable,
       "fjdaryPfOluEntry": fjdaryPfOluEntry,
       "fjdaryPfOluIndex": fjdaryPfOluIndex,
       "fjdaryPfOluRdIOPS": fjdaryPfOluRdIOPS,
       "fjdaryPfOluWtIOPS": fjdaryPfOluWtIOPS,
       "fjdaryPfOluAdCpRdIOPS": fjdaryPfOluAdCpRdIOPS,
       "fjdaryPfOluAdCpWtIOPS": fjdaryPfOluAdCpWtIOPS,
       "fjdaryPfOluRdTp": fjdaryPfOluRdTp,
       "fjdaryPfOluWtTp": fjdaryPfOluWtTp,
       "fjdaryPfOluAdCpRdTp": fjdaryPfOluAdCpRdTp,
       "fjdaryPfOluAdCpWtTp": fjdaryPfOluAdCpWtTp,
       "fjdaryPfOluRdRspTime": fjdaryPfOluRdRspTime,
       "fjdaryPfOluWtRspTime": fjdaryPfOluWtRspTime,
       "fjdaryPfOluRdCacheHit": fjdaryPfOluRdCacheHit,
       "fjdaryPfOluWtCacheHit": fjdaryPfOluWtCacheHit,
       "fjdaryPfOluAdRdCacheHit": fjdaryPfOluAdRdCacheHit,
       "fjdaryPfOluAdWtCacheHit": fjdaryPfOluAdWtCacheHit,
       "fjdaryPfOluRdPreFetchHit": fjdaryPfOluRdPreFetchHit,
       "fjdaryPfOluAdRdPreFetchHit": fjdaryPfOluAdRdPreFetchHit,
       "fjdaryPfOluRdExcCacheHit": fjdaryPfOluRdExcCacheHit,
       "fjdaryPfOluAdRdExcCacheHit": fjdaryPfOluAdRdExcCacheHit,
       "fjdaryPfDisk": fjdaryPfDisk,
       "fjdaryPfDiskCount": fjdaryPfDiskCount,
       "fjdaryPfDiskTable": fjdaryPfDiskTable,
       "fjdaryPfDiskEntry": fjdaryPfDiskEntry,
       "fjdaryPfDiskIndex": fjdaryPfDiskIndex,
       "fjdaryPfDiskPlun": fjdaryPfDiskPlun,
       "fjdaryPfDiskBusy": fjdaryPfDiskBusy,
       "fjdaryPfCm": fjdaryPfCm,
       "fjdaryPfCmCount": fjdaryPfCmCount,
       "fjdaryPfCmTable": fjdaryPfCmTable,
       "fjdaryPfCmEntry": fjdaryPfCmEntry,
       "fjdaryPfCmIndex": fjdaryPfCmIndex,
       "fjdaryPfCmBusy": fjdaryPfCmBusy,
       "fjdaryPfCmCpRemain": fjdaryPfCmCpRemain,
       "fjdaryPfCaPort": fjdaryPfCaPort,
       "fjdaryPfCaPortCount": fjdaryPfCaPortCount,
       "fjdaryPfCaPortTable": fjdaryPfCaPortTable,
       "fjdaryPfCaPortEntry": fjdaryPfCaPortEntry,
       "fjdaryPfCaPortIndex": fjdaryPfCaPortIndex,
       "fjdaryPfCaPortMode": fjdaryPfCaPortMode,
       "fjdaryPfCaPortRdIOPS": fjdaryPfCaPortRdIOPS,
       "fjdaryPfCaPortWtIOPS": fjdaryPfCaPortWtIOPS,
       "fjdaryPfCaPortRdTp": fjdaryPfCaPortRdTp,
       "fjdaryPfCaPortWtTp": fjdaryPfCaPortWtTp,
       "fjdaryPfDtOlu": fjdaryPfDtOlu,
       "fjdaryPfDtOluCount": fjdaryPfDtOluCount,
       "fjdaryPfDtOluTable": fjdaryPfDtOluTable,
       "fjdaryPfDtOluEntry": fjdaryPfDtOluEntry,
       "fjdaryPfDtOluIndex": fjdaryPfDtOluIndex,
       "fjdaryPfDtOluInfo": fjdaryPfDtOluInfo,
       "fjdaryPfDtDisk": fjdaryPfDtDisk,
       "fjdaryPfDtDiskCount": fjdaryPfDtDiskCount,
       "fjdaryPfDtDiskTable": fjdaryPfDtDiskTable,
       "fjdaryPfDtDiskEntry": fjdaryPfDtDiskEntry,
       "fjdaryPfDtDiskIndex": fjdaryPfDtDiskIndex,
       "fjdaryPfDtDiskInfo": fjdaryPfDtDiskInfo,
       "fjdaryPfDtCm": fjdaryPfDtCm,
       "fjdaryPfDtCmCount": fjdaryPfDtCmCount,
       "fjdaryPfDtCmTable": fjdaryPfDtCmTable,
       "fjdaryPfDtCmEntry": fjdaryPfDtCmEntry,
       "fjdaryPfDtCmIndex": fjdaryPfDtCmIndex,
       "fjdaryPfDtCmInfo": fjdaryPfDtCmInfo,
       "fjdaryPfDtCaPort": fjdaryPfDtCaPort,
       "fjdaryPfDtCaPortCount": fjdaryPfDtCaPortCount,
       "fjdaryPfDtCaPortTable": fjdaryPfDtCaPortTable,
       "fjdaryPfDtCaPortEntry": fjdaryPfDtCaPortEntry,
       "fjdaryPfDtCaPortIndex": fjdaryPfDtCaPortIndex,
       "fjdaryPfDtCaPortInfo": fjdaryPfDtCaPortInfo,
       "fjdaryPfRaPort": fjdaryPfRaPort,
       "fjdaryPfRaPortCount": fjdaryPfRaPortCount,
       "fjdaryPfRaPortTable": fjdaryPfRaPortTable,
       "fjdaryPfRaPortEntry": fjdaryPfRaPortEntry,
       "fjdaryPfRaPortIndex": fjdaryPfRaPortIndex,
       "fjdaryPfRaPortMode": fjdaryPfRaPortMode,
       "fjdaryPfRaPortRdIOPS": fjdaryPfRaPortRdIOPS,
       "fjdaryPfRaPortWtIOPS": fjdaryPfRaPortWtIOPS,
       "fjdaryPfRaPortRdTp": fjdaryPfRaPortRdTp,
       "fjdaryPfRaPortWtTp": fjdaryPfRaPortWtTp,
       "fjdaryPfDtRaPort": fjdaryPfDtRaPort,
       "fjdaryPfDtRaPortCount": fjdaryPfDtRaPortCount,
       "fjdaryPfDtRaPortTable": fjdaryPfDtRaPortTable,
       "fjdaryPfDtRaPortEntry": fjdaryPfDtRaPortEntry,
       "fjdaryPfDtRaPortIndex": fjdaryPfDtRaPortIndex,
       "fjdaryPfDtRaPortInfo": fjdaryPfDtRaPortInfo,
       "fjdaryPfPfm": fjdaryPfPfm,
       "fjdaryPfPfmCount": fjdaryPfPfmCount,
       "fjdaryPfPfmTable": fjdaryPfPfmTable,
       "fjdaryPfPfmEntry": fjdaryPfPfmEntry,
       "fjdaryPfPfmIndex": fjdaryPfPfmIndex,
       "fjdaryPfPfmBusy": fjdaryPfPfmBusy,
       "fjdaryPfDtPfm": fjdaryPfDtPfm,
       "fjdaryPfDPfmCount": fjdaryPfDPfmCount,
       "fjdaryPfDtPfmTable": fjdaryPfDtPfmTable,
       "fjdaryPfDtPfmEntry": fjdaryPfDtPfmEntry,
       "fjdaryPfDtPfmIndex": fjdaryPfDtPfmIndex,
       "fjdaryPfDtPfmInfo": fjdaryPfDtPfmInfo,
       "fjdaryPfCmCore": fjdaryPfCmCore,
       "fjdaryPfCmCoreCount": fjdaryPfCmCoreCount,
       "fjdaryPfCmCoreTable": fjdaryPfCmCoreTable,
       "fjdaryPfCmCoreEntry": fjdaryPfCmCoreEntry,
       "fjdaryPfCmCoreIndex": fjdaryPfCmCoreIndex,
       "fjdaryPfCmCoreValidCount": fjdaryPfCmCoreValidCount,
       "fjdaryPfCmCoreBusy0": fjdaryPfCmCoreBusy0,
       "fjdaryPfCmCoreBusy1": fjdaryPfCmCoreBusy1,
       "fjdaryPfCmCoreBusy2": fjdaryPfCmCoreBusy2,
       "fjdaryPfCmCoreBusy3": fjdaryPfCmCoreBusy3,
       "fjdaryPfCmCoreBusy4": fjdaryPfCmCoreBusy4,
       "fjdaryPfCmCoreBusy5": fjdaryPfCmCoreBusy5,
       "fjdaryPfCmCoreBusy6": fjdaryPfCmCoreBusy6,
       "fjdaryPfCmCoreBusy7": fjdaryPfCmCoreBusy7,
       "fjdaryPfCmCoreBusy8": fjdaryPfCmCoreBusy8,
       "fjdaryPfCmCoreBusy9": fjdaryPfCmCoreBusy9,
       "fjdaryPfCmCoreBusy10": fjdaryPfCmCoreBusy10,
       "fjdaryPfCmCoreBusy11": fjdaryPfCmCoreBusy11,
       "fjdaryPfCmCoreBusy12": fjdaryPfCmCoreBusy12,
       "fjdaryPfCmCoreBusy13": fjdaryPfCmCoreBusy13,
       "fjdaryPfCmCoreBusy14": fjdaryPfCmCoreBusy14,
       "fjdaryPfCmCoreBusy15": fjdaryPfCmCoreBusy15,
       "fjdaryPfCmCoreBusy16": fjdaryPfCmCoreBusy16,
       "fjdaryPfCmCoreBusy17": fjdaryPfCmCoreBusy17,
       "fjdaryPfCmCoreBusy18": fjdaryPfCmCoreBusy18,
       "fjdaryPfCmCoreBusy19": fjdaryPfCmCoreBusy19,
       "fjdaryPfDtCmCore": fjdaryPfDtCmCore,
       "fjdaryPfDtCmCoreCount": fjdaryPfDtCmCoreCount,
       "fjdaryPfDtCmCoreTable": fjdaryPfDtCmCoreTable,
       "fjdaryPfDtCmCoreEntry": fjdaryPfDtCmCoreEntry,
       "fjdaryPfDtCmCoreIndex": fjdaryPfDtCmCoreIndex,
       "fjdaryPfDtCmCoreInfo": fjdaryPfDtCmCoreInfo,
       "fjdaryPfCmNas": fjdaryPfCmNas,
       "fjdaryPfCmNasCount": fjdaryPfCmNasCount,
       "fjdaryPfCmNasTable": fjdaryPfCmNasTable,
       "fjdaryPfCmNasEntry": fjdaryPfCmNasEntry,
       "fjdaryPfCmNasIndex": fjdaryPfCmNasIndex,
       "fjdaryPfCmNasIOWaitTime": fjdaryPfCmNasIOWaitTime,
       "fjdaryPfCmNasRdThroughput": fjdaryPfCmNasRdThroughput,
       "fjdaryPfCmNasWtThroughput": fjdaryPfCmNasWtThroughput,
       "fjdaryPfCmNasIOCPUBusy": fjdaryPfCmNasIOCPUBusy,
       "fjdaryPfCmNasUsageRate": fjdaryPfCmNasUsageRate,
       "fjdaryPfCmNasUsedAmount": fjdaryPfCmNasUsedAmount,
       "fjdaryPfCmNasSambaOpCount": fjdaryPfCmNasSambaOpCount,
       "fjdaryPfCmNasNFSOpCount": fjdaryPfCmNasNFSOpCount,
       "fjdaryPfCmNasNtInThroughput": fjdaryPfCmNasNtInThroughput,
       "fjdaryPfCmNasNtOutThroughput": fjdaryPfCmNasNtOutThroughput,
       "fjdaryPfCmNasCPUBusy": fjdaryPfCmNasCPUBusy,
       "fjdaryPfCmNasFreeMemory": fjdaryPfCmNasFreeMemory,
       "fjdaryPfCmNasCachedMemory": fjdaryPfCmNasCachedMemory,
       "fjdaryPfCmNasCPUIOWait": fjdaryPfCmNasCPUIOWait,
       "fjdaryPfDtCmNas": fjdaryPfDtCmNas,
       "fjdaryPfDtCmNasCount": fjdaryPfDtCmNasCount,
       "fjdaryPfDtCmNasTable": fjdaryPfDtCmNasTable,
       "fjdaryPfDtCmNasEntry": fjdaryPfDtCmNasEntry,
       "fjdaryPfDtCmNasIndex": fjdaryPfDtCmNasIndex,
       "fjdaryPfDtCmNasInfo": fjdaryPfDtCmNasInfo,
       "fjdaryPfCmNasCore": fjdaryPfCmNasCore,
       "fjdaryPfCmNasCoreCount": fjdaryPfCmNasCoreCount,
       "fjdaryPfCmNasCoreTable": fjdaryPfCmNasCoreTable,
       "fjdaryPfCmNasCoreEntry": fjdaryPfCmNasCoreEntry,
       "fjdaryPfCmNasCoreIndex": fjdaryPfCmNasCoreIndex,
       "fjdaryPfCmNasCoreValidCount": fjdaryPfCmNasCoreValidCount,
       "fjdaryPfCmNasCoreBusy0": fjdaryPfCmNasCoreBusy0,
       "fjdaryPfCmNasCoreBusy1": fjdaryPfCmNasCoreBusy1,
       "fjdaryPfCmNasCoreBusy2": fjdaryPfCmNasCoreBusy2,
       "fjdaryPfCmNasCoreBusy3": fjdaryPfCmNasCoreBusy3,
       "fjdaryPfCmNasCoreBusy4": fjdaryPfCmNasCoreBusy4,
       "fjdaryPfCmNasCoreBusy5": fjdaryPfCmNasCoreBusy5,
       "fjdaryPfCmNasCoreBusy6": fjdaryPfCmNasCoreBusy6,
       "fjdaryPfCmNasCoreBusy7": fjdaryPfCmNasCoreBusy7,
       "fjdaryPfCmNasCoreBusy8": fjdaryPfCmNasCoreBusy8,
       "fjdaryPfCmNasCoreBusy9": fjdaryPfCmNasCoreBusy9,
       "fjdaryPfCmNasCoreBusy10": fjdaryPfCmNasCoreBusy10,
       "fjdaryPfCmNasCoreBusy11": fjdaryPfCmNasCoreBusy11,
       "fjdaryPfCmNasCoreBusy12": fjdaryPfCmNasCoreBusy12,
       "fjdaryPfCmNasCoreBusy13": fjdaryPfCmNasCoreBusy13,
       "fjdaryPfCmNasCoreBusy14": fjdaryPfCmNasCoreBusy14,
       "fjdaryPfCmNasCoreBusy15": fjdaryPfCmNasCoreBusy15,
       "fjdaryPfCmNasCoreBusy16": fjdaryPfCmNasCoreBusy16,
       "fjdaryPfCmNasCoreBusy17": fjdaryPfCmNasCoreBusy17,
       "fjdaryPfCmNasCoreBusy18": fjdaryPfCmNasCoreBusy18,
       "fjdaryPfCmNasCoreBusy19": fjdaryPfCmNasCoreBusy19,
       "fjdaryPfDtCmNasCore": fjdaryPfDtCmNasCore,
       "fjdaryPfDtCmNasCoreCount": fjdaryPfDtCmNasCoreCount,
       "fjdaryPfDtCmNasCoreTable": fjdaryPfDtCmNasCoreTable,
       "fjdaryPfDtCmNasCoreEntry": fjdaryPfDtCmNasCoreEntry,
       "fjdaryPfDtCmNasCoreIndex": fjdaryPfDtCmNasCoreIndex,
       "fjdaryPfDtCmNasCoreInfo": fjdaryPfDtCmNasCoreInfo,
       "fjdaryPfCmNasCoreIOWait": fjdaryPfCmNasCoreIOWait,
       "fjdaryPfCmNasCoreIOWaitCount": fjdaryPfCmNasCoreIOWaitCount,
       "fjdaryPfCmNasCoreIOWaitTable": fjdaryPfCmNasCoreIOWaitTable,
       "fjdaryPfCmNasCoreIOWaitEntry": fjdaryPfCmNasCoreIOWaitEntry,
       "fjdaryPfCmNasCoreIOWaitIndex": fjdaryPfCmNasCoreIOWaitIndex,
       "fjdaryPfCmNasCoreIOWaitValidCount": fjdaryPfCmNasCoreIOWaitValidCount,
       "fjdaryPfCmNasCoreIOWait0": fjdaryPfCmNasCoreIOWait0,
       "fjdaryPfCmNasCoreIOWait1": fjdaryPfCmNasCoreIOWait1,
       "fjdaryPfCmNasCoreIOWait2": fjdaryPfCmNasCoreIOWait2,
       "fjdaryPfCmNasCoreIOWait3": fjdaryPfCmNasCoreIOWait3,
       "fjdaryPfCmNasCoreIOWait4": fjdaryPfCmNasCoreIOWait4,
       "fjdaryPfCmNasCoreIOWait5": fjdaryPfCmNasCoreIOWait5,
       "fjdaryPfCmNasCoreIOWait6": fjdaryPfCmNasCoreIOWait6,
       "fjdaryPfCmNasCoreIOWait7": fjdaryPfCmNasCoreIOWait7,
       "fjdaryPfCmNasCoreIOWait8": fjdaryPfCmNasCoreIOWait8,
       "fjdaryPfCmNasCoreIOWait9": fjdaryPfCmNasCoreIOWait9,
       "fjdaryPfCmNasCoreIOWait10": fjdaryPfCmNasCoreIOWait10,
       "fjdaryPfCmNasCoreIOWait11": fjdaryPfCmNasCoreIOWait11,
       "fjdaryPfCmNasCoreIOWait12": fjdaryPfCmNasCoreIOWait12,
       "fjdaryPfCmNasCoreIOWait13": fjdaryPfCmNasCoreIOWait13,
       "fjdaryPfCmNasCoreIOWait14": fjdaryPfCmNasCoreIOWait14,
       "fjdaryPfCmNasCoreIOWait15": fjdaryPfCmNasCoreIOWait15,
       "fjdaryPfCmNasCoreIOWait16": fjdaryPfCmNasCoreIOWait16,
       "fjdaryPfCmNasCoreIOWait17": fjdaryPfCmNasCoreIOWait17,
       "fjdaryPfCmNasCoreIOWait18": fjdaryPfCmNasCoreIOWait18,
       "fjdaryPfCmNasCoreIOWait19": fjdaryPfCmNasCoreIOWait19,
       "fjdaryPfDtCmNasCoreIOWait": fjdaryPfDtCmNasCoreIOWait,
       "fjdaryPfDtCmNasCoreIOWaitCount": fjdaryPfDtCmNasCoreIOWaitCount,
       "fjdaryPfDtCmNasCoreIOWaitTable": fjdaryPfDtCmNasCoreIOWaitTable,
       "fjdaryPfDtCmNasCoreIOWaitEntry": fjdaryPfDtCmNasCoreIOWaitEntry,
       "fjdaryPfDtCmNasCoreIOWaitIndex": fjdaryPfDtCmNasCoreIOWaitIndex,
       "fjdaryPfDtCmNasCoreIOWaitInfo": fjdaryPfDtCmNasCoreIOWaitInfo,
       "fjdaryPfCaPortNas": fjdaryPfCaPortNas,
       "fjdaryPfCaPortNasCount": fjdaryPfCaPortNasCount,
       "fjdaryPfCaPortNasTable": fjdaryPfCaPortNasTable,
       "fjdaryPfCaPortNasEntry": fjdaryPfCaPortNasEntry,
       "fjdaryPfCaPortNasIndex": fjdaryPfCaPortNasIndex,
       "fjdaryPfCaPortNasNtInThroughput": fjdaryPfCaPortNasNtInThroughput,
       "fjdaryPfCaPortNasNtOutThroughput": fjdaryPfCaPortNasNtOutThroughput,
       "fjdaryPfDtCaPortNas": fjdaryPfDtCaPortNas,
       "fjdaryPfDtCaPortNasCount": fjdaryPfDtCaPortNasCount,
       "fjdaryPfDtCaPortNasTable": fjdaryPfDtCaPortNasTable,
       "fjdaryPfDtCaPortNasEntry": fjdaryPfDtCaPortNasEntry,
       "fjdaryPfDtCaPortNasIndex": fjdaryPfDtCaPortNasIndex,
       "fjdaryPfDtCaPortNasInfo": fjdaryPfDtCaPortNasInfo,
       "fjdaryPfCmNasVol": fjdaryPfCmNasVol,
       "fjdaryPfCmNasVolCount": fjdaryPfCmNasVolCount,
       "fjdaryPfCmNasVolTable": fjdaryPfCmNasVolTable,
       "fjdaryPfCmNasVolEntry": fjdaryPfCmNasVolEntry,
       "fjdaryPfCmNasVolIndex": fjdaryPfCmNasVolIndex,
       "fjdaryPfCmNasVolOluNo": fjdaryPfCmNasVolOluNo,
       "fjdaryPfCmNasVolIOWaitTime": fjdaryPfCmNasVolIOWaitTime,
       "fjdaryPfCmNasVolRdTp": fjdaryPfCmNasVolRdTp,
       "fjdaryPfCmNasVolWtTp": fjdaryPfCmNasVolWtTp,
       "fjdaryPfCmNasVolIOCPUBusy": fjdaryPfCmNasVolIOCPUBusy,
       "fjdaryPfCmNasVolUsageRate": fjdaryPfCmNasVolUsageRate,
       "fjdaryPfCmNasVolUsedAmount": fjdaryPfCmNasVolUsedAmount,
       "fjdaryPfDtCmNasVol": fjdaryPfDtCmNasVol,
       "fjdaryPfDtCmNasVolCount": fjdaryPfDtCmNasVolCount,
       "fjdaryPfDtCmNasVolTable": fjdaryPfDtCmNasVolTable,
       "fjdaryPfDtCmNasVolEntry": fjdaryPfDtCmNasVolEntry,
       "fjdaryPfDtCmNasVolIndex": fjdaryPfDtCmNasVolIndex,
       "fjdaryPfDtCmNasVolInfo": fjdaryPfDtCmNasVolInfo,
       "fjdaryUnitStatus": fjdaryUnitStatus,
       "fjdaryTrapItemId": fjdaryTrapItemId,
       "fjdaryTrapSensorInfo": fjdaryTrapSensorInfo,
       "fjdaryTrapMaintenanceInfo": fjdaryTrapMaintenanceInfo,
       "fjdaryTrapWarningInfo": fjdaryTrapWarningInfo,
       "fjdaryTrapMessage": fjdaryTrapMessage,
       "fjdaryMIBversion": fjdaryMIBversion,
       "fjdarySensor": fjdarySensor,
       "fjdaryMachinePower": fjdaryMachinePower,
       "fjdaryMachinePowerCount": fjdaryMachinePowerCount,
       "fjdaryMachinePowerTable": fjdaryMachinePowerTable,
       "fjdaryMachinePowerEntry": fjdaryMachinePowerEntry,
       "fjdaryMachinePowerIndex": fjdaryMachinePowerIndex,
       "fjdaryMachinePowerFlag": fjdaryMachinePowerFlag,
       "fjdaryMachinePowerCmNum": fjdaryMachinePowerCmNum,
       "fjdaryMachinePowerTime": fjdaryMachinePowerTime,
       "fjdaryMachinePowerInfo0": fjdaryMachinePowerInfo0,
       "fjdaryMachinePowerInfo1": fjdaryMachinePowerInfo1,
       "fjdaryMachinePowerInfo2": fjdaryMachinePowerInfo2,
       "fjdaryMachinePowerInfo3": fjdaryMachinePowerInfo3,
       "fjdaryMachinePowerInfo4": fjdaryMachinePowerInfo4,
       "fjdaryMachinePowerInfo5": fjdaryMachinePowerInfo5,
       "fjdaryMachinePowerInfo6": fjdaryMachinePowerInfo6,
       "fjdaryMachinePowerInfo7": fjdaryMachinePowerInfo7,
       "fjdaryMachinePowerInfo8": fjdaryMachinePowerInfo8,
       "fjdaryMachinePowerInfo9": fjdaryMachinePowerInfo9,
       "fjdaryMachinePowerInfo10": fjdaryMachinePowerInfo10,
       "fjdaryMachinePowerInfo11": fjdaryMachinePowerInfo11,
       "fjdaryMachinePowerInfo12": fjdaryMachinePowerInfo12,
       "fjdaryMachinePowerInfo13": fjdaryMachinePowerInfo13,
       "fjdaryMachinePowerInfo14": fjdaryMachinePowerInfo14,
       "fjdaryMachinePowerInfo15": fjdaryMachinePowerInfo15,
       "fjdaryMachinePowerInfo16": fjdaryMachinePowerInfo16,
       "fjdaryMachinePowerInfo17": fjdaryMachinePowerInfo17,
       "fjdaryMachinePowerInfo18": fjdaryMachinePowerInfo18,
       "fjdaryMachinePowerInfo19": fjdaryMachinePowerInfo19,
       "fjdaryMachinePowerInfo20": fjdaryMachinePowerInfo20,
       "fjdaryMachinePowerInfo21": fjdaryMachinePowerInfo21,
       "fjdaryMachinePowerInfo22": fjdaryMachinePowerInfo22,
       "fjdaryMachinePowerInfo23": fjdaryMachinePowerInfo23,
       "fjdaryMachinePowerInfo24": fjdaryMachinePowerInfo24,
       "fjdaryEncPower": fjdaryEncPower,
       "fjdaryEncPowerCount": fjdaryEncPowerCount,
       "fjdaryEncPowerTable": fjdaryEncPowerTable,
       "fjdaryEncPowerEntry": fjdaryEncPowerEntry,
       "fjdaryEncPowerIndex": fjdaryEncPowerIndex,
       "fjdaryEncPowerFlag": fjdaryEncPowerFlag,
       "fjdaryEncPowerCmNum": fjdaryEncPowerCmNum,
       "fjdaryEncPowerDeId": fjdaryEncPowerDeId,
       "fjdaryEncPowerTime": fjdaryEncPowerTime,
       "fjdaryEncPowerType": fjdaryEncPowerType,
       "fjdaryEncPowerInfo0": fjdaryEncPowerInfo0,
       "fjdaryEncPowerInfo1": fjdaryEncPowerInfo1,
       "fjdaryEncPowerInfo2": fjdaryEncPowerInfo2,
       "fjdaryEncPowerInfo3": fjdaryEncPowerInfo3,
       "fjdaryEncPowerInfo4": fjdaryEncPowerInfo4,
       "fjdaryEncPowerInfo5": fjdaryEncPowerInfo5,
       "fjdaryEncPowerInfo6": fjdaryEncPowerInfo6,
       "fjdaryEncPowerInfo7": fjdaryEncPowerInfo7,
       "fjdaryEncPowerInfo8": fjdaryEncPowerInfo8,
       "fjdaryEncPowerInfo9": fjdaryEncPowerInfo9,
       "fjdaryEncPowerInfo10": fjdaryEncPowerInfo10,
       "fjdaryEncPowerInfo11": fjdaryEncPowerInfo11,
       "fjdaryEncPowerInfo12": fjdaryEncPowerInfo12,
       "fjdaryEncPowerInfo13": fjdaryEncPowerInfo13,
       "fjdaryEncPowerInfo14": fjdaryEncPowerInfo14,
       "fjdaryEncPowerInfo15": fjdaryEncPowerInfo15,
       "fjdaryEncPowerInfo16": fjdaryEncPowerInfo16,
       "fjdaryEncPowerInfo17": fjdaryEncPowerInfo17,
       "fjdaryEncPowerInfo18": fjdaryEncPowerInfo18,
       "fjdaryEncPowerInfo19": fjdaryEncPowerInfo19,
       "fjdaryEncPowerInfo20": fjdaryEncPowerInfo20,
       "fjdaryEncPowerInfo21": fjdaryEncPowerInfo21,
       "fjdaryEncPowerInfo22": fjdaryEncPowerInfo22,
       "fjdaryEncPowerInfo23": fjdaryEncPowerInfo23,
       "fjdaryEncPowerInfo24": fjdaryEncPowerInfo24,
       "fjdaryMachineTemp": fjdaryMachineTemp,
       "fjdaryMachineTempCount": fjdaryMachineTempCount,
       "fjdaryMachineTempTable": fjdaryMachineTempTable,
       "fjdaryMachineTempEntry": fjdaryMachineTempEntry,
       "fjdaryMachineTempIndex": fjdaryMachineTempIndex,
       "fjdaryMachineTempFlag": fjdaryMachineTempFlag,
       "fjdaryMachineTempCmNum": fjdaryMachineTempCmNum,
       "fjdaryMachineTempTime": fjdaryMachineTempTime,
       "fjdaryMachineTempInfo0": fjdaryMachineTempInfo0,
       "fjdaryMachineTempInfo1": fjdaryMachineTempInfo1,
       "fjdaryMachineTempInfo2": fjdaryMachineTempInfo2,
       "fjdaryMachineTempInfo3": fjdaryMachineTempInfo3,
       "fjdaryMachineTempInfo4": fjdaryMachineTempInfo4,
       "fjdaryMachineTempInfo5": fjdaryMachineTempInfo5,
       "fjdaryMachineTempInfo6": fjdaryMachineTempInfo6,
       "fjdaryMachineTempInfo7": fjdaryMachineTempInfo7,
       "fjdaryMachineTempInfo8": fjdaryMachineTempInfo8,
       "fjdaryMachineTempInfo9": fjdaryMachineTempInfo9,
       "fjdaryMachineTempInfo10": fjdaryMachineTempInfo10,
       "fjdaryMachineTempInfo11": fjdaryMachineTempInfo11,
       "fjdaryMachineTempInfo12": fjdaryMachineTempInfo12,
       "fjdaryMachineTempInfo13": fjdaryMachineTempInfo13,
       "fjdaryMachineTempInfo14": fjdaryMachineTempInfo14,
       "fjdaryMachineTempInfo15": fjdaryMachineTempInfo15,
       "fjdaryMachineTempInfo16": fjdaryMachineTempInfo16,
       "fjdaryMachineTempInfo17": fjdaryMachineTempInfo17,
       "fjdaryMachineTempInfo18": fjdaryMachineTempInfo18,
       "fjdaryMachineTempInfo19": fjdaryMachineTempInfo19,
       "fjdaryMachineTempInfo20": fjdaryMachineTempInfo20,
       "fjdaryMachineTempInfo21": fjdaryMachineTempInfo21,
       "fjdaryMachineTempInfo22": fjdaryMachineTempInfo22,
       "fjdaryMachineTempInfo23": fjdaryMachineTempInfo23,
       "fjdaryMachineTempInfo24": fjdaryMachineTempInfo24,
       "fjdaryEncTemp": fjdaryEncTemp,
       "fjdaryEncTempCount": fjdaryEncTempCount,
       "fjdaryEncTempTable": fjdaryEncTempTable,
       "fjdaryEncTempEntry": fjdaryEncTempEntry,
       "fjdaryEncTempIndex": fjdaryEncTempIndex,
       "fjdaryEncTempFlag": fjdaryEncTempFlag,
       "fjdaryEncTempCmNum": fjdaryEncTempCmNum,
       "fjdaryEncTempDeId": fjdaryEncTempDeId,
       "fjdaryEncTempTime": fjdaryEncTempTime,
       "fjdaryEncTempType": fjdaryEncTempType,
       "fjdaryEncTempInfo0": fjdaryEncTempInfo0,
       "fjdaryEncTempInfo1": fjdaryEncTempInfo1,
       "fjdaryEncTempInfo2": fjdaryEncTempInfo2,
       "fjdaryEncTempInfo3": fjdaryEncTempInfo3,
       "fjdaryEncTempInfo4": fjdaryEncTempInfo4,
       "fjdaryEncTempInfo5": fjdaryEncTempInfo5,
       "fjdaryEncTempInfo6": fjdaryEncTempInfo6,
       "fjdaryEncTempInfo7": fjdaryEncTempInfo7,
       "fjdaryEncTempInfo8": fjdaryEncTempInfo8,
       "fjdaryEncTempInfo9": fjdaryEncTempInfo9,
       "fjdaryEncTempInfo10": fjdaryEncTempInfo10,
       "fjdaryEncTempInfo11": fjdaryEncTempInfo11,
       "fjdaryEncTempInfo12": fjdaryEncTempInfo12,
       "fjdaryEncTempInfo13": fjdaryEncTempInfo13,
       "fjdaryEncTempInfo14": fjdaryEncTempInfo14,
       "fjdaryEncTempInfo15": fjdaryEncTempInfo15,
       "fjdaryEncTempInfo16": fjdaryEncTempInfo16,
       "fjdaryEncTempInfo17": fjdaryEncTempInfo17,
       "fjdaryEncTempInfo18": fjdaryEncTempInfo18,
       "fjdaryEncTempInfo19": fjdaryEncTempInfo19,
       "fjdaryEncTempInfo20": fjdaryEncTempInfo20,
       "fjdaryEncTempInfo21": fjdaryEncTempInfo21,
       "fjdaryEncTempInfo22": fjdaryEncTempInfo22,
       "fjdaryEncTempInfo23": fjdaryEncTempInfo23,
       "fjdaryEncTempInfo24": fjdaryEncTempInfo24,
       "fjdaryManagement": fjdaryManagement,
       "fjdaryMgtMachineInfo": fjdaryMgtMachineInfo,
       "fjdaryMgtMachineStatus": fjdaryMgtMachineStatus,
       "fjdaryMgtMachineSubStatus": fjdaryMgtMachineSubStatus,
       "fjdaryMgtMaintenanceMode": fjdaryMgtMaintenanceMode,
       "fjdaryMgtConfigInfo": fjdaryMgtConfigInfo,
       "fjdaryMgtOpVolume": fjdaryMgtOpVolume,
       "fjdaryMgtOpVolumeTable": fjdaryMgtOpVolumeTable,
       "fjdaryMgtOpVolumeEntry": fjdaryMgtOpVolumeEntry,
       "fjdaryMgtOpVolumeNumber": fjdaryMgtOpVolumeNumber,
       "fjdaryMgtOpVolumeStatus": fjdaryMgtOpVolumeStatus,
       "fjdaryMgtOpVolumeType": fjdaryMgtOpVolumeType,
       "fjdaryMgtOpVolumeCapacity": fjdaryMgtOpVolumeCapacity,
       "fjdaryMgtOpVolumeType2": fjdaryMgtOpVolumeType2,
       "fjdaryMgtOpVolumeAttribute": fjdaryMgtOpVolumeAttribute,
       "fjdaryMgtRaidGrp": fjdaryMgtRaidGrp,
       "fjdaryMgtRaidGrpTable": fjdaryMgtRaidGrpTable,
       "fjdaryMgtRaidGrpEntry": fjdaryMgtRaidGrpEntry,
       "fjdaryMgtRaidGrpNumber": fjdaryMgtRaidGrpNumber,
       "fjdaryMgtRaidGrpStatus": fjdaryMgtRaidGrpStatus,
       "fjdaryMgtRaidGrpRaidLevel": fjdaryMgtRaidGrpRaidLevel,
       "fjdaryMgtRaidGrpCapacity": fjdaryMgtRaidGrpCapacity,
       "fjdaryTrapLinkStatusInfo": fjdaryTrapLinkStatusInfo,
       "application": application,
       "aplNetwork": aplNetwork,
       "aplNetDevice": aplNetDevice,
       "aplNetStorage": aplNetStorage,
       "aplNetNsp": aplNetNsp,
       "aplNetFjdarye150": aplNetFjdarye150,
       "aplNetFjdarye150Traps": aplNetFjdarye150Traps,
       "fjdarye150ItemFault": fjdarye150ItemFault,
       "fjdarye150BatteryExpiration": fjdarye150BatteryExpiration,
       "fjdarye150ItemWarning": fjdarye150ItemWarning,
       "fjdarye150SensorStatusChange": fjdarye150SensorStatusChange,
       "fjdarye150MaintenanceRequired": fjdarye150MaintenanceRequired,
       "fjdarye150Information": fjdarye150Information,
       "fjdarye150CaPortLinkStatusChange": fjdarye150CaPortLinkStatusChange,
       "fjdarye150StorageClusterEvent": fjdarye150StorageClusterEvent,
       "fjdarye150StorageClusterInformation": fjdarye150StorageClusterInformation,
       "fjdarye150ItemFaultToNormal": fjdarye150ItemFaultToNormal,
       "fjdarye150ItemWarningToNormal": fjdarye150ItemWarningToNormal,
       "fjdarye150SensorStatusChangeToNormal": fjdarye150SensorStatusChangeToNormal,
       "fjdarye150Error": fjdarye150Error,
       "fjdarye150Warning": fjdarye150Warning,
       "fjdarye150QuotaLimitExceeded": fjdarye150QuotaLimitExceeded,
       "fjdarye150QuotaWarningExceeded": fjdarye150QuotaWarningExceeded,
       "fjdarye150QuotaNormal": fjdarye150QuotaNormal,
       "fjdarye150SnapshotInformation": fjdarye150SnapshotInformation}
)
