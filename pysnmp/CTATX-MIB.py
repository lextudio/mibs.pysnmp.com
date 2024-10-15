# SNMP MIB module (CTATX-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CTATX-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:18:22 2024
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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY


# Types definitions



class Boolean(Integer32):
    """Custom type Boolean based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 2),
          ("true", 1))
    )




# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Sigma_ObjectIdentity = ObjectIdentity
sigma = _Sigma_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 97)
)
_Sys_ObjectIdentity = ObjectIdentity
sys = _Sys_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 97, 1)
)


class _SysID_Type(Integer32):
    """Custom type sysID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              3)
        )
    )
    namedValues = NamedValues(
        *(("es-1-atx-br-router", 3),
          ("es-1-bridge-router", 1))
    )


_SysID_Type.__name__ = "Integer32"
_SysID_Object = MibScalar
sysID = _SysID_Object(
    (1, 3, 6, 1, 4, 1, 97, 1, 1),
    _SysID_Type()
)
sysID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysID.setStatus("mandatory")
_SysReset_Type = TimeTicks
_SysReset_Object = MibScalar
sysReset = _SysReset_Object(
    (1, 3, 6, 1, 4, 1, 97, 1, 2),
    _SysReset_Type()
)
sysReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysReset.setStatus("mandatory")


class _SysTrapAck_Type(Integer32):
    """Custom type sysTrapAck based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("traps-need-acks", 1),
          ("traps-not-acked", 2))
    )


_SysTrapAck_Type.__name__ = "Integer32"
_SysTrapAck_Object = MibScalar
sysTrapAck = _SysTrapAck_Object(
    (1, 3, 6, 1, 4, 1, 97, 1, 3),
    _SysTrapAck_Type()
)
sysTrapAck.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysTrapAck.setStatus("mandatory")
_SysTrapTime_Type = TimeTicks
_SysTrapTime_Object = MibScalar
sysTrapTime = _SysTrapTime_Object(
    (1, 3, 6, 1, 4, 1, 97, 1, 4),
    _SysTrapTime_Type()
)
sysTrapTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysTrapTime.setStatus("mandatory")
_SysTrapRetry_Type = TimeTicks
_SysTrapRetry_Object = MibScalar
sysTrapRetry = _SysTrapRetry_Object(
    (1, 3, 6, 1, 4, 1, 97, 1, 5),
    _SysTrapRetry_Type()
)
sysTrapRetry.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysTrapRetry.setStatus("mandatory")
_SysTrapPort_Type = Integer32
_SysTrapPort_Object = MibScalar
sysTrapPort = _SysTrapPort_Object(
    (1, 3, 6, 1, 4, 1, 97, 1, 6),
    _SysTrapPort_Type()
)
sysTrapPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysTrapPort.setStatus("mandatory")
_Ecs_1_ObjectIdentity = ObjectIdentity
ecs_1 = _Ecs_1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 97, 3)
)
_Hw_ObjectIdentity = ObjectIdentity
hw = _Hw_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 97, 3, 1)
)
_HwNumber_Type = Integer32
_HwNumber_Object = MibScalar
hwNumber = _HwNumber_Object(
    (1, 3, 6, 1, 4, 1, 97, 3, 1, 1),
    _HwNumber_Type()
)
hwNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwNumber.setStatus("mandatory")
_HwSlotTable_Object = MibTable
hwSlotTable = _HwSlotTable_Object(
    (1, 3, 6, 1, 4, 1, 97, 3, 1, 2)
)
if mibBuilder.loadTexts:
    hwSlotTable.setStatus("mandatory")
_HwEntry_Object = MibTableRow
hwEntry = _HwEntry_Object(
    (1, 3, 6, 1, 4, 1, 97, 3, 1, 2, 1)
)
hwEntry.setIndexNames(
    (0, "CTATX-MIB", "hwIndex"),
)
if mibBuilder.loadTexts:
    hwEntry.setStatus("mandatory")
_HwIndex_Type = Integer32
_HwIndex_Object = MibTableColumn
hwIndex = _HwIndex_Object(
    (1, 3, 6, 1, 4, 1, 97, 3, 1, 2, 1, 1),
    _HwIndex_Type()
)
hwIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwIndex.setStatus("mandatory")


class _HwType_Type(Integer32):
    """Custom type hwType based on Integer32"""
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
              8,
              9,
              10,
              11,
              12)
        )
    )
    namedValues = NamedValues(
        *(("csma-iom", 5),
          ("eiom8-iom", 11),
          ("fddi-iom", 8),
          ("feiom-iom", 12),
          ("hssi-iom", 6),
          ("ifddi-iom", 9),
          ("packet-processing-engine", 3),
          ("tpr-iom", 7),
          ("ttpr-iom", 10),
          ("turbo", 4),
          ("unknown", 2),
          ("vacant", 1))
    )


_HwType_Type.__name__ = "Integer32"
_HwType_Object = MibTableColumn
hwType = _HwType_Object(
    (1, 3, 6, 1, 4, 1, 97, 3, 1, 2, 1, 2),
    _HwType_Type()
)
hwType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwType.setStatus("mandatory")


class _HwUseMod_Type(Integer32):
    """Custom type hwUseMod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("reset", 1),
          ("run", 3),
          ("run-diagnostics", 2))
    )


_HwUseMod_Type.__name__ = "Integer32"
_HwUseMod_Object = MibTableColumn
hwUseMod = _HwUseMod_Object(
    (1, 3, 6, 1, 4, 1, 97, 3, 1, 2, 1, 3),
    _HwUseMod_Type()
)
hwUseMod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwUseMod.setStatus("mandatory")


class _HwDefType_Type(Integer32):
    """Custom type hwDefType based on Integer32"""
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
              8,
              9,
              10,
              11,
              12)
        )
    )
    namedValues = NamedValues(
        *(("csma-iom", 5),
          ("eiom8-iom", 11),
          ("fddi-iom", 8),
          ("feiom-iom", 12),
          ("hssi-iom", 6),
          ("ifddi-iom", 9),
          ("packet-processing-engine", 3),
          ("tpr-iom", 7),
          ("ttpr-iom", 10),
          ("turbo", 4),
          ("unknown", 2),
          ("vacant", 1))
    )


_HwDefType_Type.__name__ = "Integer32"
_HwDefType_Object = MibTableColumn
hwDefType = _HwDefType_Object(
    (1, 3, 6, 1, 4, 1, 97, 3, 1, 2, 1, 4),
    _HwDefType_Type()
)
hwDefType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwDefType.setStatus("mandatory")


class _HwDiagStatus_Type(Integer32):
    """Custom type hwDiagStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("diag-failed", 1),
          ("diag-not-present", 2),
          ("diag-passed", 3))
    )


_HwDiagStatus_Type.__name__ = "Integer32"
_HwDiagStatus_Object = MibTableColumn
hwDiagStatus = _HwDiagStatus_Object(
    (1, 3, 6, 1, 4, 1, 97, 3, 1, 2, 1, 5),
    _HwDiagStatus_Type()
)
hwDiagStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwDiagStatus.setStatus("mandatory")


class _HwInuse_Type(Integer32):
    """Custom type hwInuse based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 2),
          ("true", 1))
    )


_HwInuse_Type.__name__ = "Integer32"
_HwInuse_Object = MibTableColumn
hwInuse = _HwInuse_Object(
    (1, 3, 6, 1, 4, 1, 97, 3, 1, 2, 1, 6),
    _HwInuse_Type()
)
hwInuse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwInuse.setStatus("mandatory")
_HwDiagCode_Type = Integer32
_HwDiagCode_Object = MibTableColumn
hwDiagCode = _HwDiagCode_Object(
    (1, 3, 6, 1, 4, 1, 97, 3, 1, 2, 1, 7),
    _HwDiagCode_Type()
)
hwDiagCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwDiagCode.setStatus("mandatory")
_HwManufData_Type = OctetString
_HwManufData_Object = MibTableColumn
hwManufData = _HwManufData_Object(
    (1, 3, 6, 1, 4, 1, 97, 3, 1, 2, 1, 8),
    _HwManufData_Type()
)
hwManufData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwManufData.setStatus("mandatory")
_HwPortType_Type = OctetString
_HwPortType_Object = MibTableColumn
hwPortType = _HwPortType_Object(
    (1, 3, 6, 1, 4, 1, 97, 3, 1, 2, 1, 9),
    _HwPortType_Type()
)
hwPortType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwPortType.setStatus("mandatory")
_HwPortStatus_Type = OctetString
_HwPortStatus_Object = MibTableColumn
hwPortStatus = _HwPortStatus_Object(
    (1, 3, 6, 1, 4, 1, 97, 3, 1, 2, 1, 10),
    _HwPortStatus_Type()
)
hwPortStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwPortStatus.setStatus("mandatory")
_HwUsePort_Type = OctetString
_HwUsePort_Object = MibTableColumn
hwUsePort = _HwUsePort_Object(
    (1, 3, 6, 1, 4, 1, 97, 3, 1, 2, 1, 11),
    _HwUsePort_Type()
)
hwUsePort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwUsePort.setStatus("mandatory")
_HwDefPortType_Type = OctetString
_HwDefPortType_Object = MibTableColumn
hwDefPortType = _HwDefPortType_Object(
    (1, 3, 6, 1, 4, 1, 97, 3, 1, 2, 1, 12),
    _HwDefPortType_Type()
)
hwDefPortType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwDefPortType.setStatus("mandatory")
_HwAddr1_Type = OctetString
_HwAddr1_Object = MibTableColumn
hwAddr1 = _HwAddr1_Object(
    (1, 3, 6, 1, 4, 1, 97, 3, 1, 2, 1, 13),
    _HwAddr1_Type()
)
hwAddr1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwAddr1.setStatus("mandatory")
_HwAddr2_Type = OctetString
_HwAddr2_Object = MibTableColumn
hwAddr2 = _HwAddr2_Object(
    (1, 3, 6, 1, 4, 1, 97, 3, 1, 2, 1, 14),
    _HwAddr2_Type()
)
hwAddr2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwAddr2.setStatus("mandatory")
_HwAddr3_Type = OctetString
_HwAddr3_Object = MibTableColumn
hwAddr3 = _HwAddr3_Object(
    (1, 3, 6, 1, 4, 1, 97, 3, 1, 2, 1, 15),
    _HwAddr3_Type()
)
hwAddr3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwAddr3.setStatus("mandatory")
_HwAddr4_Type = OctetString
_HwAddr4_Object = MibTableColumn
hwAddr4 = _HwAddr4_Object(
    (1, 3, 6, 1, 4, 1, 97, 3, 1, 2, 1, 16),
    _HwAddr4_Type()
)
hwAddr4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwAddr4.setStatus("mandatory")


class _HwTempOK_Type(Integer32):
    """Custom type hwTempOK based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("temperature-normal", 1),
          ("temperature-too-hot", 2))
    )


_HwTempOK_Type.__name__ = "Integer32"
_HwTempOK_Object = MibTableColumn
hwTempOK = _HwTempOK_Object(
    (1, 3, 6, 1, 4, 1, 97, 3, 1, 2, 1, 17),
    _HwTempOK_Type()
)
hwTempOK.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwTempOK.setStatus("mandatory")
_HwFirstPort_Type = Integer32
_HwFirstPort_Object = MibTableColumn
hwFirstPort = _HwFirstPort_Object(
    (1, 3, 6, 1, 4, 1, 97, 3, 1, 2, 1, 18),
    _HwFirstPort_Type()
)
hwFirstPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwFirstPort.setStatus("mandatory")
_HwFatalErr_Type = OctetString
_HwFatalErr_Object = MibTableColumn
hwFatalErr = _HwFatalErr_Object(
    (1, 3, 6, 1, 4, 1, 97, 3, 1, 2, 1, 19),
    _HwFatalErr_Type()
)
hwFatalErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwFatalErr.setStatus("mandatory")
_HwRptrPorts_Type = OctetString
_HwRptrPorts_Object = MibTableColumn
hwRptrPorts = _HwRptrPorts_Object(
    (1, 3, 6, 1, 4, 1, 97, 3, 1, 2, 1, 20),
    _HwRptrPorts_Type()
)
hwRptrPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwRptrPorts.setStatus("mandatory")
_HwPortSubType_Type = OctetString
_HwPortSubType_Object = MibTableColumn
hwPortSubType = _HwPortSubType_Object(
    (1, 3, 6, 1, 4, 1, 97, 3, 1, 2, 1, 21),
    _HwPortSubType_Type()
)
hwPortSubType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwPortSubType.setStatus("mandatory")
_HwAddr5_Type = OctetString
_HwAddr5_Object = MibTableColumn
hwAddr5 = _HwAddr5_Object(
    (1, 3, 6, 1, 4, 1, 97, 3, 1, 2, 1, 22),
    _HwAddr5_Type()
)
hwAddr5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwAddr5.setStatus("mandatory")
_HwAddr6_Type = OctetString
_HwAddr6_Object = MibTableColumn
hwAddr6 = _HwAddr6_Object(
    (1, 3, 6, 1, 4, 1, 97, 3, 1, 2, 1, 23),
    _HwAddr6_Type()
)
hwAddr6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwAddr6.setStatus("mandatory")
_HwAddr7_Type = OctetString
_HwAddr7_Object = MibTableColumn
hwAddr7 = _HwAddr7_Object(
    (1, 3, 6, 1, 4, 1, 97, 3, 1, 2, 1, 24),
    _HwAddr7_Type()
)
hwAddr7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwAddr7.setStatus("mandatory")
_HwAddr8_Type = OctetString
_HwAddr8_Object = MibTableColumn
hwAddr8 = _HwAddr8_Object(
    (1, 3, 6, 1, 4, 1, 97, 3, 1, 2, 1, 25),
    _HwAddr8_Type()
)
hwAddr8.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwAddr8.setStatus("mandatory")


class _HwSysBus_Type(Integer32):
    """Custom type hwSysBus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("bus-1p6-gbit", 2),
          ("bus-800-mbit", 1))
    )


_HwSysBus_Type.__name__ = "Integer32"
_HwSysBus_Object = MibScalar
hwSysBus = _HwSysBus_Object(
    (1, 3, 6, 1, 4, 1, 97, 3, 1, 3),
    _HwSysBus_Type()
)
hwSysBus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwSysBus.setStatus("mandatory")


class _HwPpeType_Type(Integer32):
    """Custom type hwPpeType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ppe2", 1),
          ("ppe3", 2))
    )


_HwPpeType_Type.__name__ = "Integer32"
_HwPpeType_Object = MibScalar
hwPpeType = _HwPpeType_Object(
    (1, 3, 6, 1, 4, 1, 97, 3, 1, 4),
    _HwPpeType_Type()
)
hwPpeType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwPpeType.setStatus("mandatory")


class _HwSysProcessor_Type(Integer32):
    """Custom type hwSysProcessor based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dual-29000", 1),
          ("dual-29030", 2))
    )


_HwSysProcessor_Type.__name__ = "Integer32"
_HwSysProcessor_Object = MibScalar
hwSysProcessor = _HwSysProcessor_Object(
    (1, 3, 6, 1, 4, 1, 97, 3, 1, 5),
    _HwSysProcessor_Type()
)
hwSysProcessor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwSysProcessor.setStatus("mandatory")
_Sw_ObjectIdentity = ObjectIdentity
sw = _Sw_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 97, 3, 2)
)
_SwNumber_Type = Integer32
_SwNumber_Object = MibScalar
swNumber = _SwNumber_Object(
    (1, 3, 6, 1, 4, 1, 97, 3, 2, 1),
    _SwNumber_Type()
)
swNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swNumber.setStatus("mandatory")
_SwFilesetTable_Object = MibTable
swFilesetTable = _SwFilesetTable_Object(
    (1, 3, 6, 1, 4, 1, 97, 3, 2, 2)
)
if mibBuilder.loadTexts:
    swFilesetTable.setStatus("mandatory")
_SwFileset_Object = MibTableRow
swFileset = _SwFileset_Object(
    (1, 3, 6, 1, 4, 1, 97, 3, 2, 2, 1)
)
swFileset.setIndexNames(
    (0, "CTATX-MIB", "swIndex"),
)
if mibBuilder.loadTexts:
    swFileset.setStatus("mandatory")


class _SwIndex_Type(Integer32):
    """Custom type swIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("currently-executing", 1),
          ("next-boot", 2))
    )


_SwIndex_Type.__name__ = "Integer32"
_SwIndex_Object = MibTableColumn
swIndex = _SwIndex_Object(
    (1, 3, 6, 1, 4, 1, 97, 3, 2, 2, 1, 1),
    _SwIndex_Type()
)
swIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swIndex.setStatus("mandatory")
_SwDesc_Type = DisplayString
_SwDesc_Object = MibTableColumn
swDesc = _SwDesc_Object(
    (1, 3, 6, 1, 4, 1, 97, 3, 2, 2, 1, 3),
    _SwDesc_Type()
)
swDesc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swDesc.setStatus("mandatory")
_SwCount_Type = Integer32
_SwCount_Object = MibTableColumn
swCount = _SwCount_Object(
    (1, 3, 6, 1, 4, 1, 97, 3, 2, 2, 1, 4),
    _SwCount_Type()
)
swCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swCount.setStatus("mandatory")
_SwTypes_Type = OctetString
_SwTypes_Object = MibTableColumn
swTypes = _SwTypes_Object(
    (1, 3, 6, 1, 4, 1, 97, 3, 2, 2, 1, 5),
    _SwTypes_Type()
)
swTypes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swTypes.setStatus("mandatory")
_SwSizes_Type = OctetString
_SwSizes_Object = MibTableColumn
swSizes = _SwSizes_Object(
    (1, 3, 6, 1, 4, 1, 97, 3, 2, 2, 1, 6),
    _SwSizes_Type()
)
swSizes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swSizes.setStatus("mandatory")
_SwStarts_Type = OctetString
_SwStarts_Object = MibTableColumn
swStarts = _SwStarts_Object(
    (1, 3, 6, 1, 4, 1, 97, 3, 2, 2, 1, 7),
    _SwStarts_Type()
)
swStarts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swStarts.setStatus("mandatory")
_SwBases_Type = OctetString
_SwBases_Object = MibTableColumn
swBases = _SwBases_Object(
    (1, 3, 6, 1, 4, 1, 97, 3, 2, 2, 1, 8),
    _SwBases_Type()
)
swBases.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swBases.setStatus("mandatory")


class _SwFlashBank_Type(Integer32):
    """Custom type swFlashBank based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("first-bank", 1),
          ("second-bank", 2))
    )


_SwFlashBank_Type.__name__ = "Integer32"
_SwFlashBank_Object = MibTableColumn
swFlashBank = _SwFlashBank_Object(
    (1, 3, 6, 1, 4, 1, 97, 3, 2, 2, 1, 9),
    _SwFlashBank_Type()
)
swFlashBank.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swFlashBank.setStatus("mandatory")
_Admin_ObjectIdentity = ObjectIdentity
admin = _Admin_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 97, 3, 3)
)
_Config_ObjectIdentity = ObjectIdentity
config = _Config_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 97, 3, 3, 1)
)
_ConfigFatalErr_Type = OctetString
_ConfigFatalErr_Object = MibScalar
configFatalErr = _ConfigFatalErr_Object(
    (1, 3, 6, 1, 4, 1, 97, 3, 3, 1, 1),
    _ConfigFatalErr_Type()
)
configFatalErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    configFatalErr.setStatus("mandatory")
_ConfigAnyPass_Type = OctetString
_ConfigAnyPass_Object = MibScalar
configAnyPass = _ConfigAnyPass_Object(
    (1, 3, 6, 1, 4, 1, 97, 3, 3, 1, 2),
    _ConfigAnyPass_Type()
)
configAnyPass.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configAnyPass.setStatus("mandatory")
_ConfigGetPass_Type = OctetString
_ConfigGetPass_Object = MibScalar
configGetPass = _ConfigGetPass_Object(
    (1, 3, 6, 1, 4, 1, 97, 3, 3, 1, 3),
    _ConfigGetPass_Type()
)
configGetPass.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configGetPass.setStatus("mandatory")
_ConfigNMSAddress_Type = IpAddress
_ConfigNMSAddress_Object = MibScalar
configNMSAddress = _ConfigNMSAddress_Object(
    (1, 3, 6, 1, 4, 1, 97, 3, 3, 1, 4),
    _ConfigNMSAddress_Type()
)
configNMSAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configNMSAddress.setStatus("mandatory")
_ConfigFunctions_Type = Integer32
_ConfigFunctions_Object = MibScalar
configFunctions = _ConfigFunctions_Object(
    (1, 3, 6, 1, 4, 1, 97, 3, 3, 1, 5),
    _ConfigFunctions_Type()
)
configFunctions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    configFunctions.setStatus("mandatory")


class _ConfigPowerAc1_Type(Integer32):
    """Custom type configPowerAc1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ac-bad", 2),
          ("ac-good", 1))
    )


_ConfigPowerAc1_Type.__name__ = "Integer32"
_ConfigPowerAc1_Object = MibScalar
configPowerAc1 = _ConfigPowerAc1_Object(
    (1, 3, 6, 1, 4, 1, 97, 3, 3, 1, 6),
    _ConfigPowerAc1_Type()
)
configPowerAc1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    configPowerAc1.setStatus("mandatory")


class _ConfigPowerAc2_Type(Integer32):
    """Custom type configPowerAc2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ac-bad", 2),
          ("ac-good", 1))
    )


_ConfigPowerAc2_Type.__name__ = "Integer32"
_ConfigPowerAc2_Object = MibScalar
configPowerAc2 = _ConfigPowerAc2_Object(
    (1, 3, 6, 1, 4, 1, 97, 3, 3, 1, 7),
    _ConfigPowerAc2_Type()
)
configPowerAc2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    configPowerAc2.setStatus("mandatory")


class _ConfigPowerDc1_Type(Integer32):
    """Custom type configPowerDc1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dc-bad", 2),
          ("dc-good", 1))
    )


_ConfigPowerDc1_Type.__name__ = "Integer32"
_ConfigPowerDc1_Object = MibScalar
configPowerDc1 = _ConfigPowerDc1_Object(
    (1, 3, 6, 1, 4, 1, 97, 3, 3, 1, 8),
    _ConfigPowerDc1_Type()
)
configPowerDc1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    configPowerDc1.setStatus("mandatory")


class _ConfigPowerDc2_Type(Integer32):
    """Custom type configPowerDc2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dc-bad", 2),
          ("dc-good", 1))
    )


_ConfigPowerDc2_Type.__name__ = "Integer32"
_ConfigPowerDc2_Object = MibScalar
configPowerDc2 = _ConfigPowerDc2_Object(
    (1, 3, 6, 1, 4, 1, 97, 3, 3, 1, 9),
    _ConfigPowerDc2_Type()
)
configPowerDc2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    configPowerDc2.setStatus("mandatory")


class _ConfigPowerPresent1_Type(Integer32):
    """Custom type configPowerPresent1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("supply-absent", 2),
          ("supply-present", 1))
    )


_ConfigPowerPresent1_Type.__name__ = "Integer32"
_ConfigPowerPresent1_Object = MibScalar
configPowerPresent1 = _ConfigPowerPresent1_Object(
    (1, 3, 6, 1, 4, 1, 97, 3, 3, 1, 10),
    _ConfigPowerPresent1_Type()
)
configPowerPresent1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    configPowerPresent1.setStatus("mandatory")


class _ConfigPowerPresent2_Type(Integer32):
    """Custom type configPowerPresent2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("supply-absent", 2),
          ("supply-present", 1))
    )


_ConfigPowerPresent2_Type.__name__ = "Integer32"
_ConfigPowerPresent2_Object = MibScalar
configPowerPresent2 = _ConfigPowerPresent2_Object(
    (1, 3, 6, 1, 4, 1, 97, 3, 3, 1, 11),
    _ConfigPowerPresent2_Type()
)
configPowerPresent2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    configPowerPresent2.setStatus("mandatory")


class _ConfigAlarmDynamic_Type(Integer32):
    """Custom type configAlarmDynamic based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 2),
          ("true", 1))
    )


_ConfigAlarmDynamic_Type.__name__ = "Integer32"
_ConfigAlarmDynamic_Object = MibScalar
configAlarmDynamic = _ConfigAlarmDynamic_Object(
    (1, 3, 6, 1, 4, 1, 97, 3, 3, 1, 12),
    _ConfigAlarmDynamic_Type()
)
configAlarmDynamic.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configAlarmDynamic.setStatus("mandatory")


class _ConfigAlarmAddresses_Type(Integer32):
    """Custom type configAlarmAddresses based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 2),
          ("true", 1))
    )


_ConfigAlarmAddresses_Type.__name__ = "Integer32"
_ConfigAlarmAddresses_Object = MibScalar
configAlarmAddresses = _ConfigAlarmAddresses_Object(
    (1, 3, 6, 1, 4, 1, 97, 3, 3, 1, 13),
    _ConfigAlarmAddresses_Type()
)
configAlarmAddresses.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configAlarmAddresses.setStatus("mandatory")


class _ConfigStorageFailure_Type(Integer32):
    """Custom type configStorageFailure based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 2),
          ("true", 1))
    )


_ConfigStorageFailure_Type.__name__ = "Integer32"
_ConfigStorageFailure_Object = MibScalar
configStorageFailure = _ConfigStorageFailure_Object(
    (1, 3, 6, 1, 4, 1, 97, 3, 3, 1, 14),
    _ConfigStorageFailure_Type()
)
configStorageFailure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    configStorageFailure.setStatus("mandatory")
_ConfigAuthenticationFailure_Type = IpAddress
_ConfigAuthenticationFailure_Object = MibScalar
configAuthenticationFailure = _ConfigAuthenticationFailure_Object(
    (1, 3, 6, 1, 4, 1, 97, 3, 3, 1, 15),
    _ConfigAuthenticationFailure_Type()
)
configAuthenticationFailure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    configAuthenticationFailure.setStatus("mandatory")
_ConfigFddiPriority_Type = Integer32
_ConfigFddiPriority_Object = MibScalar
configFddiPriority = _ConfigFddiPriority_Object(
    (1, 3, 6, 1, 4, 1, 97, 3, 3, 1, 16),
    _ConfigFddiPriority_Type()
)
configFddiPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configFddiPriority.setStatus("mandatory")
_ConfigTprPriority_Type = Integer32
_ConfigTprPriority_Object = MibScalar
configTprPriority = _ConfigTprPriority_Object(
    (1, 3, 6, 1, 4, 1, 97, 3, 3, 1, 17),
    _ConfigTprPriority_Type()
)
configTprPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configTprPriority.setStatus("mandatory")
_ConfigDumpModule_Type = Integer32
_ConfigDumpModule_Object = MibScalar
configDumpModule = _ConfigDumpModule_Object(
    (1, 3, 6, 1, 4, 1, 97, 3, 3, 1, 19),
    _ConfigDumpModule_Type()
)
configDumpModule.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configDumpModule.setStatus("mandatory")
_ConfigDumpStart_Type = Integer32
_ConfigDumpStart_Object = MibScalar
configDumpStart = _ConfigDumpStart_Object(
    (1, 3, 6, 1, 4, 1, 97, 3, 3, 1, 20),
    _ConfigDumpStart_Type()
)
configDumpStart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configDumpStart.setStatus("mandatory")
_ConfigDumpEnd_Type = Integer32
_ConfigDumpEnd_Object = MibScalar
configDumpEnd = _ConfigDumpEnd_Object(
    (1, 3, 6, 1, 4, 1, 97, 3, 3, 1, 21),
    _ConfigDumpEnd_Type()
)
configDumpEnd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configDumpEnd.setStatus("mandatory")
_Lma_ObjectIdentity = ObjectIdentity
lma = _Lma_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 97, 3, 3, 2)
)
_LmaAllAddr_Type = OctetString
_LmaAllAddr_Object = MibScalar
lmaAllAddr = _LmaAllAddr_Object(
    (1, 3, 6, 1, 4, 1, 97, 3, 3, 2, 1),
    _LmaAllAddr_Type()
)
lmaAllAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lmaAllAddr.setStatus("mandatory")
_LmaAnyAddr_Type = OctetString
_LmaAnyAddr_Object = MibScalar
lmaAnyAddr = _LmaAnyAddr_Object(
    (1, 3, 6, 1, 4, 1, 97, 3, 3, 2, 2),
    _LmaAnyAddr_Type()
)
lmaAnyAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lmaAnyAddr.setStatus("mandatory")
_Ppe_ObjectIdentity = ObjectIdentity
ppe = _Ppe_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 97, 3, 3, 3)
)
_PpeLrgUxRxCnt_Type = Integer32
_PpeLrgUxRxCnt_Object = MibScalar
ppeLrgUxRxCnt = _PpeLrgUxRxCnt_Object(
    (1, 3, 6, 1, 4, 1, 97, 3, 3, 3, 1),
    _PpeLrgUxRxCnt_Type()
)
ppeLrgUxRxCnt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ppeLrgUxRxCnt.setStatus("mandatory")
_PpeSmlUxRxCnt_Type = Integer32
_PpeSmlUxRxCnt_Object = MibScalar
ppeSmlUxRxCnt = _PpeSmlUxRxCnt_Object(
    (1, 3, 6, 1, 4, 1, 97, 3, 3, 3, 2),
    _PpeSmlUxRxCnt_Type()
)
ppeSmlUxRxCnt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ppeSmlUxRxCnt.setStatus("mandatory")
_PpeUxTxCnt_Type = Integer32
_PpeUxTxCnt_Object = MibScalar
ppeUxTxCnt = _PpeUxTxCnt_Object(
    (1, 3, 6, 1, 4, 1, 97, 3, 3, 3, 3),
    _PpeUxTxCnt_Type()
)
ppeUxTxCnt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ppeUxTxCnt.setStatus("mandatory")
_PpeSmlBuffSize_Type = Integer32
_PpeSmlBuffSize_Object = MibScalar
ppeSmlBuffSize = _PpeSmlBuffSize_Object(
    (1, 3, 6, 1, 4, 1, 97, 3, 3, 3, 4),
    _PpeSmlBuffSize_Type()
)
ppeSmlBuffSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ppeSmlBuffSize.setStatus("mandatory")
_PpeBridgingMemory_Type = Integer32
_PpeBridgingMemory_Object = MibScalar
ppeBridgingMemory = _PpeBridgingMemory_Object(
    (1, 3, 6, 1, 4, 1, 97, 3, 3, 3, 5),
    _PpeBridgingMemory_Type()
)
ppeBridgingMemory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ppeBridgingMemory.setStatus("mandatory")


class _PpeExtendStats_Type(Integer32):
    """Custom type ppeExtendStats based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 2),
          ("true", 1))
    )


_PpeExtendStats_Type.__name__ = "Integer32"
_PpeExtendStats_Object = MibScalar
ppeExtendStats = _PpeExtendStats_Object(
    (1, 3, 6, 1, 4, 1, 97, 3, 3, 3, 6),
    _PpeExtendStats_Type()
)
ppeExtendStats.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ppeExtendStats.setStatus("mandatory")
_PpeBAddrLimit_Type = Integer32
_PpeBAddrLimit_Object = MibScalar
ppeBAddrLimit = _PpeBAddrLimit_Object(
    (1, 3, 6, 1, 4, 1, 97, 3, 3, 3, 7),
    _PpeBAddrLimit_Type()
)
ppeBAddrLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ppeBAddrLimit.setStatus("mandatory")
_PpeTxCongests_Type = Counter32
_PpeTxCongests_Object = MibScalar
ppeTxCongests = _PpeTxCongests_Object(
    (1, 3, 6, 1, 4, 1, 97, 3, 3, 3, 8),
    _PpeTxCongests_Type()
)
ppeTxCongests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ppeTxCongests.setStatus("mandatory")
_PpeArpEntries_Type = Counter32
_PpeArpEntries_Object = MibScalar
ppeArpEntries = _PpeArpEntries_Object(
    (1, 3, 6, 1, 4, 1, 97, 3, 3, 3, 9),
    _PpeArpEntries_Type()
)
ppeArpEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ppeArpEntries.setStatus("mandatory")
_PpeArpStatics_Type = Counter32
_PpeArpStatics_Object = MibScalar
ppeArpStatics = _PpeArpStatics_Object(
    (1, 3, 6, 1, 4, 1, 97, 3, 3, 3, 10),
    _PpeArpStatics_Type()
)
ppeArpStatics.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ppeArpStatics.setStatus("mandatory")
_PpeArpOverflows_Type = Counter32
_PpeArpOverflows_Object = MibScalar
ppeArpOverflows = _PpeArpOverflows_Object(
    (1, 3, 6, 1, 4, 1, 97, 3, 3, 3, 11),
    _PpeArpOverflows_Type()
)
ppeArpOverflows.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ppeArpOverflows.setStatus("mandatory")
_PpeIpEntries_Type = Counter32
_PpeIpEntries_Object = MibScalar
ppeIpEntries = _PpeIpEntries_Object(
    (1, 3, 6, 1, 4, 1, 97, 3, 3, 3, 12),
    _PpeIpEntries_Type()
)
ppeIpEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ppeIpEntries.setStatus("mandatory")
_PpeIpStatics_Type = Counter32
_PpeIpStatics_Object = MibScalar
ppeIpStatics = _PpeIpStatics_Object(
    (1, 3, 6, 1, 4, 1, 97, 3, 3, 3, 13),
    _PpeIpStatics_Type()
)
ppeIpStatics.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ppeIpStatics.setStatus("mandatory")
_PpeStaticPreference_Type = Integer32
_PpeStaticPreference_Object = MibScalar
ppeStaticPreference = _PpeStaticPreference_Object(
    (1, 3, 6, 1, 4, 1, 97, 3, 3, 3, 14),
    _PpeStaticPreference_Type()
)
ppeStaticPreference.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ppeStaticPreference.setStatus("mandatory")
_PpeOspfPreference_Type = Integer32
_PpeOspfPreference_Object = MibScalar
ppeOspfPreference = _PpeOspfPreference_Object(
    (1, 3, 6, 1, 4, 1, 97, 3, 3, 3, 15),
    _PpeOspfPreference_Type()
)
ppeOspfPreference.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ppeOspfPreference.setStatus("mandatory")
_PpeRipPreference_Type = Integer32
_PpeRipPreference_Object = MibScalar
ppeRipPreference = _PpeRipPreference_Object(
    (1, 3, 6, 1, 4, 1, 97, 3, 3, 3, 16),
    _PpeRipPreference_Type()
)
ppeRipPreference.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ppeRipPreference.setStatus("mandatory")
_PpeEgpPreference_Type = Integer32
_PpeEgpPreference_Object = MibScalar
ppeEgpPreference = _PpeEgpPreference_Object(
    (1, 3, 6, 1, 4, 1, 97, 3, 3, 3, 17),
    _PpeEgpPreference_Type()
)
ppeEgpPreference.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ppeEgpPreference.setStatus("mandatory")


class _PpeCpuUtilization_Type(Integer32):
    """Custom type ppeCpuUtilization based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("high-cpu", 3),
          ("low-cpu", 1),
          ("medium-cpu", 2))
    )


_PpeCpuUtilization_Type.__name__ = "Integer32"
_PpeCpuUtilization_Object = MibScalar
ppeCpuUtilization = _PpeCpuUtilization_Object(
    (1, 3, 6, 1, 4, 1, 97, 3, 3, 3, 18),
    _PpeCpuUtilization_Type()
)
ppeCpuUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ppeCpuUtilization.setStatus("mandatory")
_PpeRipRouteDiscards_Type = Counter32
_PpeRipRouteDiscards_Object = MibScalar
ppeRipRouteDiscards = _PpeRipRouteDiscards_Object(
    (1, 3, 6, 1, 4, 1, 97, 3, 3, 3, 19),
    _PpeRipRouteDiscards_Type()
)
ppeRipRouteDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ppeRipRouteDiscards.setStatus("mandatory")
_PpeOspfRouteDiscards_Type = Counter32
_PpeOspfRouteDiscards_Object = MibScalar
ppeOspfRouteDiscards = _PpeOspfRouteDiscards_Object(
    (1, 3, 6, 1, 4, 1, 97, 3, 3, 3, 20),
    _PpeOspfRouteDiscards_Type()
)
ppeOspfRouteDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ppeOspfRouteDiscards.setStatus("mandatory")
_PpeRouteMemorySize_Type = Counter32
_PpeRouteMemorySize_Object = MibScalar
ppeRouteMemorySize = _PpeRouteMemorySize_Object(
    (1, 3, 6, 1, 4, 1, 97, 3, 3, 3, 21),
    _PpeRouteMemorySize_Type()
)
ppeRouteMemorySize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ppeRouteMemorySize.setStatus("mandatory")
_PpeRouteMemoryAvail_Type = Counter32
_PpeRouteMemoryAvail_Object = MibScalar
ppeRouteMemoryAvail = _PpeRouteMemoryAvail_Object(
    (1, 3, 6, 1, 4, 1, 97, 3, 3, 3, 22),
    _PpeRouteMemoryAvail_Type()
)
ppeRouteMemoryAvail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ppeRouteMemoryAvail.setStatus("mandatory")
_PpeRouteMemoryFailures_Type = Counter32
_PpeRouteMemoryFailures_Object = MibScalar
ppeRouteMemoryFailures = _PpeRouteMemoryFailures_Object(
    (1, 3, 6, 1, 4, 1, 97, 3, 3, 3, 23),
    _PpeRouteMemoryFailures_Type()
)
ppeRouteMemoryFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ppeRouteMemoryFailures.setStatus("mandatory")
_PpePacketMemorySize_Type = Counter32
_PpePacketMemorySize_Object = MibScalar
ppePacketMemorySize = _PpePacketMemorySize_Object(
    (1, 3, 6, 1, 4, 1, 97, 3, 3, 3, 24),
    _PpePacketMemorySize_Type()
)
ppePacketMemorySize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ppePacketMemorySize.setStatus("mandatory")
_PpePacketMemoryAvail_Type = Counter32
_PpePacketMemoryAvail_Object = MibScalar
ppePacketMemoryAvail = _PpePacketMemoryAvail_Object(
    (1, 3, 6, 1, 4, 1, 97, 3, 3, 3, 25),
    _PpePacketMemoryAvail_Type()
)
ppePacketMemoryAvail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ppePacketMemoryAvail.setStatus("mandatory")
_PpePacketMemoryFailures_Type = Counter32
_PpePacketMemoryFailures_Object = MibScalar
ppePacketMemoryFailures = _PpePacketMemoryFailures_Object(
    (1, 3, 6, 1, 4, 1, 97, 3, 3, 3, 26),
    _PpePacketMemoryFailures_Type()
)
ppePacketMemoryFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ppePacketMemoryFailures.setStatus("mandatory")
_PpeOspfPduMemoryFailures_Type = Counter32
_PpeOspfPduMemoryFailures_Object = MibScalar
ppeOspfPduMemoryFailures = _PpeOspfPduMemoryFailures_Object(
    (1, 3, 6, 1, 4, 1, 97, 3, 3, 3, 27),
    _PpeOspfPduMemoryFailures_Type()
)
ppeOspfPduMemoryFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ppeOspfPduMemoryFailures.setStatus("mandatory")
_PpeOspfPduMemoryAllocs_Type = Counter32
_PpeOspfPduMemoryAllocs_Object = MibScalar
ppeOspfPduMemoryAllocs = _PpeOspfPduMemoryAllocs_Object(
    (1, 3, 6, 1, 4, 1, 97, 3, 3, 3, 28),
    _PpeOspfPduMemoryAllocs_Type()
)
ppeOspfPduMemoryAllocs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ppeOspfPduMemoryAllocs.setStatus("mandatory")
_PpeIcmpPduMemoryFailures_Type = Counter32
_PpeIcmpPduMemoryFailures_Object = MibScalar
ppeIcmpPduMemoryFailures = _PpeIcmpPduMemoryFailures_Object(
    (1, 3, 6, 1, 4, 1, 97, 3, 3, 3, 29),
    _PpeIcmpPduMemoryFailures_Type()
)
ppeIcmpPduMemoryFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ppeIcmpPduMemoryFailures.setStatus("mandatory")
_PpeIcmpPduMemoryAllocs_Type = Counter32
_PpeIcmpPduMemoryAllocs_Object = MibScalar
ppeIcmpPduMemoryAllocs = _PpeIcmpPduMemoryAllocs_Object(
    (1, 3, 6, 1, 4, 1, 97, 3, 3, 3, 30),
    _PpeIcmpPduMemoryAllocs_Type()
)
ppeIcmpPduMemoryAllocs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ppeIcmpPduMemoryAllocs.setStatus("mandatory")
_PpeRipPduMemoryFailures_Type = Counter32
_PpeRipPduMemoryFailures_Object = MibScalar
ppeRipPduMemoryFailures = _PpeRipPduMemoryFailures_Object(
    (1, 3, 6, 1, 4, 1, 97, 3, 3, 3, 31),
    _PpeRipPduMemoryFailures_Type()
)
ppeRipPduMemoryFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ppeRipPduMemoryFailures.setStatus("mandatory")
_PpeRipPduMemoryAllocs_Type = Counter32
_PpeRipPduMemoryAllocs_Object = MibScalar
ppeRipPduMemoryAllocs = _PpeRipPduMemoryAllocs_Object(
    (1, 3, 6, 1, 4, 1, 97, 3, 3, 3, 32),
    _PpeRipPduMemoryAllocs_Type()
)
ppeRipPduMemoryAllocs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ppeRipPduMemoryAllocs.setStatus("mandatory")
_PpeBootpPduMemoryFailures_Type = Counter32
_PpeBootpPduMemoryFailures_Object = MibScalar
ppeBootpPduMemoryFailures = _PpeBootpPduMemoryFailures_Object(
    (1, 3, 6, 1, 4, 1, 97, 3, 3, 3, 33),
    _PpeBootpPduMemoryFailures_Type()
)
ppeBootpPduMemoryFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ppeBootpPduMemoryFailures.setStatus("mandatory")
_PpeBootpPduMemoryAllocs_Type = Counter32
_PpeBootpPduMemoryAllocs_Object = MibScalar
ppeBootpPduMemoryAllocs = _PpeBootpPduMemoryAllocs_Object(
    (1, 3, 6, 1, 4, 1, 97, 3, 3, 3, 34),
    _PpeBootpPduMemoryAllocs_Type()
)
ppeBootpPduMemoryAllocs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ppeBootpPduMemoryAllocs.setStatus("mandatory")
_PpeSnmpPduMemoryFailures_Type = Counter32
_PpeSnmpPduMemoryFailures_Object = MibScalar
ppeSnmpPduMemoryFailures = _PpeSnmpPduMemoryFailures_Object(
    (1, 3, 6, 1, 4, 1, 97, 3, 3, 3, 35),
    _PpeSnmpPduMemoryFailures_Type()
)
ppeSnmpPduMemoryFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ppeSnmpPduMemoryFailures.setStatus("mandatory")
_PpeSnmpPduMemoryAllocs_Type = Counter32
_PpeSnmpPduMemoryAllocs_Object = MibScalar
ppeSnmpPduMemoryAllocs = _PpeSnmpPduMemoryAllocs_Object(
    (1, 3, 6, 1, 4, 1, 97, 3, 3, 3, 36),
    _PpeSnmpPduMemoryAllocs_Type()
)
ppeSnmpPduMemoryAllocs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ppeSnmpPduMemoryAllocs.setStatus("mandatory")
_PpeTftpPduMemoryFailures_Type = Counter32
_PpeTftpPduMemoryFailures_Object = MibScalar
ppeTftpPduMemoryFailures = _PpeTftpPduMemoryFailures_Object(
    (1, 3, 6, 1, 4, 1, 97, 3, 3, 3, 37),
    _PpeTftpPduMemoryFailures_Type()
)
ppeTftpPduMemoryFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ppeTftpPduMemoryFailures.setStatus("mandatory")
_PpeTftpPduMemoryAllocs_Type = Counter32
_PpeTftpPduMemoryAllocs_Object = MibScalar
ppeTftpPduMemoryAllocs = _PpeTftpPduMemoryAllocs_Object(
    (1, 3, 6, 1, 4, 1, 97, 3, 3, 3, 38),
    _PpeTftpPduMemoryAllocs_Type()
)
ppeTftpPduMemoryAllocs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ppeTftpPduMemoryAllocs.setStatus("mandatory")
_PpeTraceroutePduMemoryFailures_Type = Counter32
_PpeTraceroutePduMemoryFailures_Object = MibScalar
ppeTraceroutePduMemoryFailures = _PpeTraceroutePduMemoryFailures_Object(
    (1, 3, 6, 1, 4, 1, 97, 3, 3, 3, 39),
    _PpeTraceroutePduMemoryFailures_Type()
)
ppeTraceroutePduMemoryFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ppeTraceroutePduMemoryFailures.setStatus("mandatory")
_PpeTraceroutePduMemoryAllocs_Type = Counter32
_PpeTraceroutePduMemoryAllocs_Object = MibScalar
ppeTraceroutePduMemoryAllocs = _PpeTraceroutePduMemoryAllocs_Object(
    (1, 3, 6, 1, 4, 1, 97, 3, 3, 3, 40),
    _PpeTraceroutePduMemoryAllocs_Type()
)
ppeTraceroutePduMemoryAllocs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ppeTraceroutePduMemoryAllocs.setStatus("mandatory")
_PpeArpPduMemoryFailures_Type = Counter32
_PpeArpPduMemoryFailures_Object = MibScalar
ppeArpPduMemoryFailures = _PpeArpPduMemoryFailures_Object(
    (1, 3, 6, 1, 4, 1, 97, 3, 3, 3, 41),
    _PpeArpPduMemoryFailures_Type()
)
ppeArpPduMemoryFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ppeArpPduMemoryFailures.setStatus("mandatory")
_PpeArpPduMemoryAllocs_Type = Counter32
_PpeArpPduMemoryAllocs_Object = MibScalar
ppeArpPduMemoryAllocs = _PpeArpPduMemoryAllocs_Object(
    (1, 3, 6, 1, 4, 1, 97, 3, 3, 3, 42),
    _PpeArpPduMemoryAllocs_Type()
)
ppeArpPduMemoryAllocs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ppeArpPduMemoryAllocs.setStatus("mandatory")
_PpeIgmpPduMemoryFailures_Type = Counter32
_PpeIgmpPduMemoryFailures_Object = MibScalar
ppeIgmpPduMemoryFailures = _PpeIgmpPduMemoryFailures_Object(
    (1, 3, 6, 1, 4, 1, 97, 3, 3, 3, 43),
    _PpeIgmpPduMemoryFailures_Type()
)
ppeIgmpPduMemoryFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ppeIgmpPduMemoryFailures.setStatus("mandatory")
_PpeIgmpPduMemoryAllocs_Type = Counter32
_PpeIgmpPduMemoryAllocs_Object = MibScalar
ppeIgmpPduMemoryAllocs = _PpeIgmpPduMemoryAllocs_Object(
    (1, 3, 6, 1, 4, 1, 97, 3, 3, 3, 44),
    _PpeIgmpPduMemoryAllocs_Type()
)
ppeIgmpPduMemoryAllocs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ppeIgmpPduMemoryAllocs.setStatus("mandatory")


class _PpeAresAsStes_Type(Integer32):
    """Custom type ppeAresAsStes based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 2),
          ("true", 1))
    )


_PpeAresAsStes_Type.__name__ = "Integer32"
_PpeAresAsStes_Object = MibScalar
ppeAresAsStes = _PpeAresAsStes_Object(
    (1, 3, 6, 1, 4, 1, 97, 3, 3, 3, 45),
    _PpeAresAsStes_Type()
)
ppeAresAsStes.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ppeAresAsStes.setStatus("mandatory")
_PpeRoutePercent_Type = Integer32
_PpeRoutePercent_Object = MibScalar
ppeRoutePercent = _PpeRoutePercent_Object(
    (1, 3, 6, 1, 4, 1, 97, 3, 3, 3, 46),
    _PpeRoutePercent_Type()
)
ppeRoutePercent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ppeRoutePercent.setStatus("mandatory")
_PpeMgtMemorySize_Type = Counter32
_PpeMgtMemorySize_Object = MibScalar
ppeMgtMemorySize = _PpeMgtMemorySize_Object(
    (1, 3, 6, 1, 4, 1, 97, 3, 3, 3, 48),
    _PpeMgtMemorySize_Type()
)
ppeMgtMemorySize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ppeMgtMemorySize.setStatus("mandatory")
_PpeMgtMemoryAvail_Type = Counter32
_PpeMgtMemoryAvail_Object = MibScalar
ppeMgtMemoryAvail = _PpeMgtMemoryAvail_Object(
    (1, 3, 6, 1, 4, 1, 97, 3, 3, 3, 49),
    _PpeMgtMemoryAvail_Type()
)
ppeMgtMemoryAvail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ppeMgtMemoryAvail.setStatus("mandatory")
_PpeMgtMemoryFailures_Type = Counter32
_PpeMgtMemoryFailures_Object = MibScalar
ppeMgtMemoryFailures = _PpeMgtMemoryFailures_Object(
    (1, 3, 6, 1, 4, 1, 97, 3, 3, 3, 50),
    _PpeMgtMemoryFailures_Type()
)
ppeMgtMemoryFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ppeMgtMemoryFailures.setStatus("mandatory")
_St_ObjectIdentity = ObjectIdentity
st = _St_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 97, 3, 3, 4)
)
_StGroupAddr_Type = OctetString
_StGroupAddr_Object = MibScalar
stGroupAddr = _StGroupAddr_Object(
    (1, 3, 6, 1, 4, 1, 97, 3, 3, 4, 1),
    _StGroupAddr_Type()
)
stGroupAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    stGroupAddr.setStatus("mandatory")
_StResAddr_Type = OctetString
_StResAddr_Object = MibScalar
stResAddr = _StResAddr_Object(
    (1, 3, 6, 1, 4, 1, 97, 3, 3, 4, 2),
    _StResAddr_Type()
)
stResAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    stResAddr.setStatus("mandatory")
_StBridgeId_Type = OctetString
_StBridgeId_Object = MibScalar
stBridgeId = _StBridgeId_Object(
    (1, 3, 6, 1, 4, 1, 97, 3, 3, 4, 3),
    _StBridgeId_Type()
)
stBridgeId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    stBridgeId.setStatus("mandatory")
_StRootMaxAge_Type = TimeTicks
_StRootMaxAge_Object = MibScalar
stRootMaxAge = _StRootMaxAge_Object(
    (1, 3, 6, 1, 4, 1, 97, 3, 3, 4, 4),
    _StRootMaxAge_Type()
)
stRootMaxAge.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    stRootMaxAge.setStatus("mandatory")
_StRootHello_Type = TimeTicks
_StRootHello_Object = MibScalar
stRootHello = _StRootHello_Object(
    (1, 3, 6, 1, 4, 1, 97, 3, 3, 4, 5),
    _StRootHello_Type()
)
stRootHello.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    stRootHello.setStatus("mandatory")
_StRootDelay_Type = TimeTicks
_StRootDelay_Object = MibScalar
stRootDelay = _StRootDelay_Object(
    (1, 3, 6, 1, 4, 1, 97, 3, 3, 4, 6),
    _StRootDelay_Type()
)
stRootDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    stRootDelay.setStatus("mandatory")
_StRootID_Type = OctetString
_StRootID_Object = MibScalar
stRootID = _StRootID_Object(
    (1, 3, 6, 1, 4, 1, 97, 3, 3, 4, 7),
    _StRootID_Type()
)
stRootID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stRootID.setStatus("mandatory")
_StRootCost_Type = Integer32
_StRootCost_Object = MibScalar
stRootCost = _StRootCost_Object(
    (1, 3, 6, 1, 4, 1, 97, 3, 3, 4, 8),
    _StRootCost_Type()
)
stRootCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stRootCost.setStatus("mandatory")
_StRootPort_Type = Integer32
_StRootPort_Object = MibScalar
stRootPort = _StRootPort_Object(
    (1, 3, 6, 1, 4, 1, 97, 3, 3, 4, 9),
    _StRootPort_Type()
)
stRootPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stRootPort.setStatus("mandatory")


class _StTopChange_Type(Integer32):
    """Custom type stTopChange based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 2),
          ("true", 1))
    )


_StTopChange_Type.__name__ = "Integer32"
_StTopChange_Object = MibScalar
stTopChange = _StTopChange_Object(
    (1, 3, 6, 1, 4, 1, 97, 3, 3, 4, 10),
    _StTopChange_Type()
)
stTopChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stTopChange.setStatus("mandatory")
_StActMaxAge_Type = TimeTicks
_StActMaxAge_Object = MibScalar
stActMaxAge = _StActMaxAge_Object(
    (1, 3, 6, 1, 4, 1, 97, 3, 3, 4, 11),
    _StActMaxAge_Type()
)
stActMaxAge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stActMaxAge.setStatus("mandatory")
_StActHello_Type = TimeTicks
_StActHello_Object = MibScalar
stActHello = _StActHello_Object(
    (1, 3, 6, 1, 4, 1, 97, 3, 3, 4, 12),
    _StActHello_Type()
)
stActHello.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stActHello.setStatus("mandatory")
_StActDelay_Type = TimeTicks
_StActDelay_Object = MibScalar
stActDelay = _StActDelay_Object(
    (1, 3, 6, 1, 4, 1, 97, 3, 3, 4, 13),
    _StActDelay_Type()
)
stActDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stActDelay.setStatus("mandatory")
_StTopChangeCount_Type = Integer32
_StTopChangeCount_Object = MibScalar
stTopChangeCount = _StTopChangeCount_Object(
    (1, 3, 6, 1, 4, 1, 97, 3, 3, 4, 14),
    _StTopChangeCount_Type()
)
stTopChangeCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    stTopChangeCount.setStatus("mandatory")
_StTopChangeTime_Type = TimeTicks
_StTopChangeTime_Object = MibScalar
stTopChangeTime = _StTopChangeTime_Object(
    (1, 3, 6, 1, 4, 1, 97, 3, 3, 4, 15),
    _StTopChangeTime_Type()
)
stTopChangeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stTopChangeTime.setStatus("mandatory")
_StAgeTime_Type = Integer32
_StAgeTime_Object = MibScalar
stAgeTime = _StAgeTime_Object(
    (1, 3, 6, 1, 4, 1, 97, 3, 3, 4, 16),
    _StAgeTime_Type()
)
stAgeTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    stAgeTime.setStatus("mandatory")
_Mesh_ObjectIdentity = ObjectIdentity
mesh = _Mesh_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 97, 3, 3, 5)
)
_MeshCostPercent_Type = Integer32
_MeshCostPercent_Object = MibScalar
meshCostPercent = _MeshCostPercent_Object(
    (1, 3, 6, 1, 4, 1, 97, 3, 3, 5, 1),
    _MeshCostPercent_Type()
)
meshCostPercent.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    meshCostPercent.setStatus("mandatory")
_MeshCost_Type = Integer32
_MeshCost_Object = MibScalar
meshCost = _MeshCost_Object(
    (1, 3, 6, 1, 4, 1, 97, 3, 3, 5, 2),
    _MeshCost_Type()
)
meshCost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    meshCost.setStatus("mandatory")


class _MeshCostChange_Type(Integer32):
    """Custom type meshCostChange based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 2),
          ("true", 1))
    )


_MeshCostChange_Type.__name__ = "Integer32"
_MeshCostChange_Object = MibScalar
meshCostChange = _MeshCostChange_Object(
    (1, 3, 6, 1, 4, 1, 97, 3, 3, 5, 3),
    _MeshCostChange_Type()
)
meshCostChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    meshCostChange.setStatus("mandatory")
_MeshCostChangeCount_Type = Integer32
_MeshCostChangeCount_Object = MibScalar
meshCostChangeCount = _MeshCostChangeCount_Object(
    (1, 3, 6, 1, 4, 1, 97, 3, 3, 5, 4),
    _MeshCostChangeCount_Type()
)
meshCostChangeCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    meshCostChangeCount.setStatus("mandatory")
_MeshCostChangeTime_Type = TimeTicks
_MeshCostChangeTime_Object = MibScalar
meshCostChangeTime = _MeshCostChangeTime_Object(
    (1, 3, 6, 1, 4, 1, 97, 3, 3, 5, 5),
    _MeshCostChangeTime_Type()
)
meshCostChangeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    meshCostChangeTime.setStatus("mandatory")
_MeshSubnet_Type = OctetString
_MeshSubnet_Object = MibScalar
meshSubnet = _MeshSubnet_Object(
    (1, 3, 6, 1, 4, 1, 97, 3, 3, 5, 6),
    _MeshSubnet_Type()
)
meshSubnet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    meshSubnet.setStatus("mandatory")
_Swdis_ObjectIdentity = ObjectIdentity
swdis = _Swdis_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 97, 3, 4)
)
_SwdisDesc_Type = OctetString
_SwdisDesc_Object = MibScalar
swdisDesc = _SwdisDesc_Object(
    (1, 3, 6, 1, 4, 1, 97, 3, 4, 1),
    _SwdisDesc_Type()
)
swdisDesc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swdisDesc.setStatus("mandatory")


class _SwdisAccess_Type(Integer32):
    """Custom type swdisAccess based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("any-software", 2),
          ("protected", 1))
    )


_SwdisAccess_Type.__name__ = "Integer32"
_SwdisAccess_Object = MibScalar
swdisAccess = _SwdisAccess_Object(
    (1, 3, 6, 1, 4, 1, 97, 3, 4, 2),
    _SwdisAccess_Type()
)
swdisAccess.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swdisAccess.setStatus("mandatory")


class _SwdisWriteStatus_Type(Integer32):
    """Custom type swdisWriteStatus based on Integer32"""
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
        *(("config-and-flash-errors", 5),
          ("config-error", 3),
          ("flash-error", 4),
          ("in-progress", 1),
          ("success", 2))
    )


_SwdisWriteStatus_Type.__name__ = "Integer32"
_SwdisWriteStatus_Object = MibScalar
swdisWriteStatus = _SwdisWriteStatus_Object(
    (1, 3, 6, 1, 4, 1, 97, 3, 4, 3),
    _SwdisWriteStatus_Type()
)
swdisWriteStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swdisWriteStatus.setStatus("mandatory")
_SwdisConfigIp_Type = IpAddress
_SwdisConfigIp_Object = MibScalar
swdisConfigIp = _SwdisConfigIp_Object(
    (1, 3, 6, 1, 4, 1, 97, 3, 4, 4),
    _SwdisConfigIp_Type()
)
swdisConfigIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swdisConfigIp.setStatus("mandatory")
_SwdisConfigRetryTime_Type = Integer32
_SwdisConfigRetryTime_Object = MibScalar
swdisConfigRetryTime = _SwdisConfigRetryTime_Object(
    (1, 3, 6, 1, 4, 1, 97, 3, 4, 5),
    _SwdisConfigRetryTime_Type()
)
swdisConfigRetryTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swdisConfigRetryTime.setStatus("mandatory")
_SwdisConfigTotalTimeout_Type = Integer32
_SwdisConfigTotalTimeout_Object = MibScalar
swdisConfigTotalTimeout = _SwdisConfigTotalTimeout_Object(
    (1, 3, 6, 1, 4, 1, 97, 3, 4, 6),
    _SwdisConfigTotalTimeout_Type()
)
swdisConfigTotalTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swdisConfigTotalTimeout.setStatus("mandatory")
_Addr_ObjectIdentity = ObjectIdentity
addr = _Addr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 97, 3, 5)
)
_AddrStatics_Type = Counter32
_AddrStatics_Object = MibScalar
addrStatics = _AddrStatics_Object(
    (1, 3, 6, 1, 4, 1, 97, 3, 5, 1),
    _AddrStatics_Type()
)
addrStatics.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    addrStatics.setStatus("mandatory")
_AddrDynamics_Type = Counter32
_AddrDynamics_Object = MibScalar
addrDynamics = _AddrDynamics_Object(
    (1, 3, 6, 1, 4, 1, 97, 3, 5, 2),
    _AddrDynamics_Type()
)
addrDynamics.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    addrDynamics.setStatus("mandatory")
_AddrDynamicMax_Type = Gauge32
_AddrDynamicMax_Object = MibScalar
addrDynamicMax = _AddrDynamicMax_Object(
    (1, 3, 6, 1, 4, 1, 97, 3, 5, 3),
    _AddrDynamicMax_Type()
)
addrDynamicMax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    addrDynamicMax.setStatus("mandatory")
_AddrMeshs_Type = Counter32
_AddrMeshs_Object = MibScalar
addrMeshs = _AddrMeshs_Object(
    (1, 3, 6, 1, 4, 1, 97, 3, 5, 4),
    _AddrMeshs_Type()
)
addrMeshs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    addrMeshs.setStatus("mandatory")
_AddrDynamicOverflows_Type = Counter32
_AddrDynamicOverflows_Object = MibScalar
addrDynamicOverflows = _AddrDynamicOverflows_Object(
    (1, 3, 6, 1, 4, 1, 97, 3, 5, 5),
    _AddrDynamicOverflows_Type()
)
addrDynamicOverflows.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    addrDynamicOverflows.setStatus("mandatory")
_AddrMeshOverflows_Type = Counter32
_AddrMeshOverflows_Object = MibScalar
addrMeshOverflows = _AddrMeshOverflows_Object(
    (1, 3, 6, 1, 4, 1, 97, 3, 5, 6),
    _AddrMeshOverflows_Type()
)
addrMeshOverflows.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    addrMeshOverflows.setStatus("mandatory")
_AddrFlags_Type = Integer32
_AddrFlags_Object = MibScalar
addrFlags = _AddrFlags_Object(
    (1, 3, 6, 1, 4, 1, 97, 3, 5, 7),
    _AddrFlags_Type()
)
addrFlags.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    addrFlags.setStatus("mandatory")
_AddrMAC_Type = OctetString
_AddrMAC_Object = MibScalar
addrMAC = _AddrMAC_Object(
    (1, 3, 6, 1, 4, 1, 97, 3, 5, 8),
    _AddrMAC_Type()
)
addrMAC.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    addrMAC.setStatus("mandatory")
_AddrPort_Type = Integer32
_AddrPort_Object = MibScalar
addrPort = _AddrPort_Object(
    (1, 3, 6, 1, 4, 1, 97, 3, 5, 9),
    _AddrPort_Type()
)
addrPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    addrPort.setStatus("mandatory")
_AddrPortMap_Type = OctetString
_AddrPortMap_Object = MibScalar
addrPortMap = _AddrPortMap_Object(
    (1, 3, 6, 1, 4, 1, 97, 3, 5, 10),
    _AddrPortMap_Type()
)
addrPortMap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    addrPortMap.setStatus("obsolete")


class _AddrOperation_Type(Integer32):
    """Custom type addrOperation based on Integer32"""
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
        *(("delete", 5),
          ("read-block", 6),
          ("read-next", 2),
          ("read-random", 1),
          ("update", 4),
          ("zero-stats", 3))
    )


_AddrOperation_Type.__name__ = "Integer32"
_AddrOperation_Object = MibScalar
addrOperation = _AddrOperation_Object(
    (1, 3, 6, 1, 4, 1, 97, 3, 5, 41),
    _AddrOperation_Type()
)
addrOperation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    addrOperation.setStatus("mandatory")
_AddrIndex_Type = Integer32
_AddrIndex_Object = MibScalar
addrIndex = _AddrIndex_Object(
    (1, 3, 6, 1, 4, 1, 97, 3, 5, 42),
    _AddrIndex_Type()
)
addrIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    addrIndex.setStatus("mandatory")
_AddrNext_Type = Integer32
_AddrNext_Object = MibScalar
addrNext = _AddrNext_Object(
    (1, 3, 6, 1, 4, 1, 97, 3, 5, 44),
    _AddrNext_Type()
)
addrNext.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    addrNext.setStatus("mandatory")
_AddrAge_Type = TimeTicks
_AddrAge_Object = MibScalar
addrAge = _AddrAge_Object(
    (1, 3, 6, 1, 4, 1, 97, 3, 5, 45),
    _AddrAge_Type()
)
addrAge.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    addrAge.setStatus("mandatory")
_AddrRxPkts_Type = Counter32
_AddrRxPkts_Object = MibScalar
addrRxPkts = _AddrRxPkts_Object(
    (1, 3, 6, 1, 4, 1, 97, 3, 5, 46),
    _AddrRxPkts_Type()
)
addrRxPkts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    addrRxPkts.setStatus("mandatory")
_AddrRxChars_Type = Counter32
_AddrRxChars_Object = MibScalar
addrRxChars = _AddrRxChars_Object(
    (1, 3, 6, 1, 4, 1, 97, 3, 5, 47),
    _AddrRxChars_Type()
)
addrRxChars.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    addrRxChars.setStatus("mandatory")
_AddrRxMultiPkts_Type = Counter32
_AddrRxMultiPkts_Object = MibScalar
addrRxMultiPkts = _AddrRxMultiPkts_Object(
    (1, 3, 6, 1, 4, 1, 97, 3, 5, 48),
    _AddrRxMultiPkts_Type()
)
addrRxMultiPkts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    addrRxMultiPkts.setStatus("mandatory")
_AddrRxFwdPkts_Type = Counter32
_AddrRxFwdPkts_Object = MibScalar
addrRxFwdPkts = _AddrRxFwdPkts_Object(
    (1, 3, 6, 1, 4, 1, 97, 3, 5, 49),
    _AddrRxFwdPkts_Type()
)
addrRxFwdPkts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    addrRxFwdPkts.setStatus("mandatory")
_AddrTxPkts_Type = Counter32
_AddrTxPkts_Object = MibScalar
addrTxPkts = _AddrTxPkts_Object(
    (1, 3, 6, 1, 4, 1, 97, 3, 5, 50),
    _AddrTxPkts_Type()
)
addrTxPkts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    addrTxPkts.setStatus("mandatory")
_AddrTxChars_Type = Counter32
_AddrTxChars_Object = MibScalar
addrTxChars = _AddrTxChars_Object(
    (1, 3, 6, 1, 4, 1, 97, 3, 5, 51),
    _AddrTxChars_Type()
)
addrTxChars.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    addrTxChars.setStatus("mandatory")
_AddrBlockSize_Type = Integer32
_AddrBlockSize_Object = MibScalar
addrBlockSize = _AddrBlockSize_Object(
    (1, 3, 6, 1, 4, 1, 97, 3, 5, 52),
    _AddrBlockSize_Type()
)
addrBlockSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    addrBlockSize.setStatus("mandatory")
_AddrBlock_Type = OctetString
_AddrBlock_Object = MibScalar
addrBlock = _AddrBlock_Object(
    (1, 3, 6, 1, 4, 1, 97, 3, 5, 53),
    _AddrBlock_Type()
)
addrBlock.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    addrBlock.setStatus("mandatory")
_AddrAlarmMAC_Type = OctetString
_AddrAlarmMAC_Object = MibScalar
addrAlarmMAC = _AddrAlarmMAC_Object(
    (1, 3, 6, 1, 4, 1, 97, 3, 5, 54),
    _AddrAlarmMAC_Type()
)
addrAlarmMAC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    addrAlarmMAC.setStatus("mandatory")
_AddrRptrPort_Type = Integer32
_AddrRptrPort_Object = MibScalar
addrRptrPort = _AddrRptrPort_Object(
    (1, 3, 6, 1, 4, 1, 97, 3, 5, 55),
    _AddrRptrPort_Type()
)
addrRptrPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    addrRptrPort.setStatus("mandatory")
_Snmpsmt_ObjectIdentity = ObjectIdentity
snmpsmt = _Snmpsmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 97, 3, 6)
)
_SnmpsmtUpstreamReq_Type = OctetString
_SnmpsmtUpstreamReq_Object = MibScalar
snmpsmtUpstreamReq = _SnmpsmtUpstreamReq_Object(
    (1, 3, 6, 1, 4, 1, 97, 3, 6, 1),
    _SnmpsmtUpstreamReq_Type()
)
snmpsmtUpstreamReq.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpsmtUpstreamReq.setStatus("mandatory")
_SnmpsmtUpstreamRsp_Type = OctetString
_SnmpsmtUpstreamRsp_Object = MibScalar
snmpsmtUpstreamRsp = _SnmpsmtUpstreamRsp_Object(
    (1, 3, 6, 1, 4, 1, 97, 3, 6, 2),
    _SnmpsmtUpstreamRsp_Type()
)
snmpsmtUpstreamRsp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snmpsmtUpstreamRsp.setStatus("mandatory")
_SnmpsmtUpstreamDescriptor_Type = OctetString
_SnmpsmtUpstreamDescriptor_Object = MibScalar
snmpsmtUpstreamDescriptor = _SnmpsmtUpstreamDescriptor_Object(
    (1, 3, 6, 1, 4, 1, 97, 3, 6, 3),
    _SnmpsmtUpstreamDescriptor_Type()
)
snmpsmtUpstreamDescriptor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snmpsmtUpstreamDescriptor.setStatus("mandatory")
_SnmpsmtUpstreamState_Type = OctetString
_SnmpsmtUpstreamState_Object = MibScalar
snmpsmtUpstreamState = _SnmpsmtUpstreamState_Object(
    (1, 3, 6, 1, 4, 1, 97, 3, 6, 4),
    _SnmpsmtUpstreamState_Type()
)
snmpsmtUpstreamState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snmpsmtUpstreamState.setStatus("mandatory")
_FddismtTable_Object = MibTable
fddismtTable = _FddismtTable_Object(
    (1, 3, 6, 1, 4, 1, 97, 3, 6, 5)
)
if mibBuilder.loadTexts:
    fddismtTable.setStatus("mandatory")
_FddismtEntry_Object = MibTableRow
fddismtEntry = _FddismtEntry_Object(
    (1, 3, 6, 1, 4, 1, 97, 3, 6, 5, 1)
)
fddismtEntry.setIndexNames(
    (0, "CTATX-MIB", "fddismtIndex"),
)
if mibBuilder.loadTexts:
    fddismtEntry.setStatus("mandatory")
_FddismtIndex_Type = Integer32
_FddismtIndex_Object = MibTableColumn
fddismtIndex = _FddismtIndex_Object(
    (1, 3, 6, 1, 4, 1, 97, 3, 6, 5, 1, 1),
    _FddismtIndex_Type()
)
fddismtIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fddismtIndex.setStatus("mandatory")
_FddismtUpstreamReq_Type = OctetString
_FddismtUpstreamReq_Object = MibTableColumn
fddismtUpstreamReq = _FddismtUpstreamReq_Object(
    (1, 3, 6, 1, 4, 1, 97, 3, 6, 5, 1, 2),
    _FddismtUpstreamReq_Type()
)
fddismtUpstreamReq.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fddismtUpstreamReq.setStatus("mandatory")
_FddismtUpstreamRsp_Type = OctetString
_FddismtUpstreamRsp_Object = MibTableColumn
fddismtUpstreamRsp = _FddismtUpstreamRsp_Object(
    (1, 3, 6, 1, 4, 1, 97, 3, 6, 5, 1, 3),
    _FddismtUpstreamRsp_Type()
)
fddismtUpstreamRsp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fddismtUpstreamRsp.setStatus("mandatory")
_FddismtUpstreamDescriptor_Type = OctetString
_FddismtUpstreamDescriptor_Object = MibTableColumn
fddismtUpstreamDescriptor = _FddismtUpstreamDescriptor_Object(
    (1, 3, 6, 1, 4, 1, 97, 3, 6, 5, 1, 4),
    _FddismtUpstreamDescriptor_Type()
)
fddismtUpstreamDescriptor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fddismtUpstreamDescriptor.setStatus("mandatory")
_FddismtUpstreamState_Type = OctetString
_FddismtUpstreamState_Object = MibTableColumn
fddismtUpstreamState = _FddismtUpstreamState_Object(
    (1, 3, 6, 1, 4, 1, 97, 3, 6, 5, 1, 5),
    _FddismtUpstreamState_Type()
)
fddismtUpstreamState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fddismtUpstreamState.setStatus("mandatory")
_Sinterfaces_ObjectIdentity = ObjectIdentity
sinterfaces = _Sinterfaces_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 97, 3, 7)
)
_SifUX_Type = Integer32
_SifUX_Object = MibScalar
sifUX = _SifUX_Object(
    (1, 3, 6, 1, 4, 1, 97, 3, 7, 1),
    _SifUX_Type()
)
sifUX.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sifUX.setStatus("mandatory")
_SifTable_Object = MibTable
sifTable = _SifTable_Object(
    (1, 3, 6, 1, 4, 1, 97, 3, 7, 2)
)
if mibBuilder.loadTexts:
    sifTable.setStatus("mandatory")
_SifEntry_Object = MibTableRow
sifEntry = _SifEntry_Object(
    (1, 3, 6, 1, 4, 1, 97, 3, 7, 2, 1)
)
sifEntry.setIndexNames(
    (0, "CTATX-MIB", "sifIndex"),
)
if mibBuilder.loadTexts:
    sifEntry.setStatus("mandatory")
_SifIndex_Type = Integer32
_SifIndex_Object = MibTableColumn
sifIndex = _SifIndex_Object(
    (1, 3, 6, 1, 4, 1, 97, 3, 7, 2, 1, 1),
    _SifIndex_Type()
)
sifIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sifIndex.setStatus("mandatory")
_SifSmlRxCnt_Type = Integer32
_SifSmlRxCnt_Object = MibTableColumn
sifSmlRxCnt = _SifSmlRxCnt_Object(
    (1, 3, 6, 1, 4, 1, 97, 3, 7, 2, 1, 2),
    _SifSmlRxCnt_Type()
)
sifSmlRxCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sifSmlRxCnt.setStatus("mandatory")
_SifLrgRxCnt_Type = Integer32
_SifLrgRxCnt_Object = MibTableColumn
sifLrgRxCnt = _SifLrgRxCnt_Object(
    (1, 3, 6, 1, 4, 1, 97, 3, 7, 2, 1, 3),
    _SifLrgRxCnt_Type()
)
sifLrgRxCnt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sifLrgRxCnt.setStatus("mandatory")
_SifUxTxCnt_Type = Integer32
_SifUxTxCnt_Object = MibTableColumn
sifUxTxCnt = _SifUxTxCnt_Object(
    (1, 3, 6, 1, 4, 1, 97, 3, 7, 2, 1, 4),
    _SifUxTxCnt_Type()
)
sifUxTxCnt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sifUxTxCnt.setStatus("mandatory")
_SifThreshold_Type = Integer32
_SifThreshold_Object = MibTableColumn
sifThreshold = _SifThreshold_Object(
    (1, 3, 6, 1, 4, 1, 97, 3, 7, 2, 1, 5),
    _SifThreshold_Type()
)
sifThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sifThreshold.setStatus("mandatory")
_SifThresholdTime_Type = Integer32
_SifThresholdTime_Object = MibTableColumn
sifThresholdTime = _SifThresholdTime_Object(
    (1, 3, 6, 1, 4, 1, 97, 3, 7, 2, 1, 6),
    _SifThresholdTime_Type()
)
sifThresholdTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sifThresholdTime.setStatus("mandatory")
_SifRxQueueThresh_Type = Integer32
_SifRxQueueThresh_Object = MibTableColumn
sifRxQueueThresh = _SifRxQueueThresh_Object(
    (1, 3, 6, 1, 4, 1, 97, 3, 7, 2, 1, 7),
    _SifRxQueueThresh_Type()
)
sifRxQueueThresh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sifRxQueueThresh.setStatus("mandatory")
_SifRxQueueThreshTime_Type = Integer32
_SifRxQueueThreshTime_Object = MibTableColumn
sifRxQueueThreshTime = _SifRxQueueThreshTime_Object(
    (1, 3, 6, 1, 4, 1, 97, 3, 7, 2, 1, 8),
    _SifRxQueueThreshTime_Type()
)
sifRxQueueThreshTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sifRxQueueThreshTime.setStatus("mandatory")
_SifTxStormCnt_Type = Integer32
_SifTxStormCnt_Object = MibTableColumn
sifTxStormCnt = _SifTxStormCnt_Object(
    (1, 3, 6, 1, 4, 1, 97, 3, 7, 2, 1, 9),
    _SifTxStormCnt_Type()
)
sifTxStormCnt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sifTxStormCnt.setStatus("mandatory")
_SifTxStormTime_Type = TimeTicks
_SifTxStormTime_Object = MibTableColumn
sifTxStormTime = _SifTxStormTime_Object(
    (1, 3, 6, 1, 4, 1, 97, 3, 7, 2, 1, 10),
    _SifTxStormTime_Type()
)
sifTxStormTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sifTxStormTime.setStatus("mandatory")
_SifFilterFlags_Type = Integer32
_SifFilterFlags_Object = MibTableColumn
sifFilterFlags = _SifFilterFlags_Object(
    (1, 3, 6, 1, 4, 1, 97, 3, 7, 2, 1, 11),
    _SifFilterFlags_Type()
)
sifFilterFlags.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sifFilterFlags.setStatus("mandatory")
_SifCongestTime_Type = TimeTicks
_SifCongestTime_Object = MibTableColumn
sifCongestTime = _SifCongestTime_Object(
    (1, 3, 6, 1, 4, 1, 97, 3, 7, 2, 1, 12),
    _SifCongestTime_Type()
)
sifCongestTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sifCongestTime.setStatus("mandatory")
_SifQueueTime_Type = TimeTicks
_SifQueueTime_Object = MibTableColumn
sifQueueTime = _SifQueueTime_Object(
    (1, 3, 6, 1, 4, 1, 97, 3, 7, 2, 1, 13),
    _SifQueueTime_Type()
)
sifQueueTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sifQueueTime.setStatus("mandatory")
_SifPortCost_Type = Integer32
_SifPortCost_Object = MibTableColumn
sifPortCost = _SifPortCost_Object(
    (1, 3, 6, 1, 4, 1, 97, 3, 7, 2, 1, 14),
    _SifPortCost_Type()
)
sifPortCost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sifPortCost.setStatus("mandatory")
_SifStPriority_Type = Integer32
_SifStPriority_Object = MibTableColumn
sifStPriority = _SifStPriority_Object(
    (1, 3, 6, 1, 4, 1, 97, 3, 7, 2, 1, 15),
    _SifStPriority_Type()
)
sifStPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sifStPriority.setStatus("mandatory")
_SifFunctions_Type = Integer32
_SifFunctions_Object = MibTableColumn
sifFunctions = _SifFunctions_Object(
    (1, 3, 6, 1, 4, 1, 97, 3, 7, 2, 1, 16),
    _SifFunctions_Type()
)
sifFunctions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sifFunctions.setStatus("mandatory")


class _SifCongested_Type(Integer32):
    """Custom type sifCongested based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 2),
          ("true", 1))
    )


_SifCongested_Type.__name__ = "Integer32"
_SifCongested_Object = MibTableColumn
sifCongested = _SifCongested_Object(
    (1, 3, 6, 1, 4, 1, 97, 3, 7, 2, 1, 17),
    _SifCongested_Type()
)
sifCongested.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sifCongested.setStatus("mandatory")


class _SifState_Type(Integer32):
    """Custom type sifState based on Integer32"""
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
        *(("spanning-tree-blocking", 5),
          ("spanning-tree-disabled", 1),
          ("spanning-tree-forwarding", 4),
          ("spanning-tree-learning", 3),
          ("spanning-tree-listening", 2))
    )


_SifState_Type.__name__ = "Integer32"
_SifState_Object = MibTableColumn
sifState = _SifState_Object(
    (1, 3, 6, 1, 4, 1, 97, 3, 7, 2, 1, 18),
    _SifState_Type()
)
sifState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sifState.setStatus("mandatory")
_SifDesigCost_Type = Integer32
_SifDesigCost_Object = MibTableColumn
sifDesigCost = _SifDesigCost_Object(
    (1, 3, 6, 1, 4, 1, 97, 3, 7, 2, 1, 19),
    _SifDesigCost_Type()
)
sifDesigCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sifDesigCost.setStatus("mandatory")
_SifDesigRoot_Type = OctetString
_SifDesigRoot_Object = MibTableColumn
sifDesigRoot = _SifDesigRoot_Object(
    (1, 3, 6, 1, 4, 1, 97, 3, 7, 2, 1, 20),
    _SifDesigRoot_Type()
)
sifDesigRoot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sifDesigRoot.setStatus("mandatory")
_SifDesigBridge_Type = OctetString
_SifDesigBridge_Object = MibTableColumn
sifDesigBridge = _SifDesigBridge_Object(
    (1, 3, 6, 1, 4, 1, 97, 3, 7, 2, 1, 21),
    _SifDesigBridge_Type()
)
sifDesigBridge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sifDesigBridge.setStatus("mandatory")
_SifDesigPort_Type = OctetString
_SifDesigPort_Object = MibTableColumn
sifDesigPort = _SifDesigPort_Object(
    (1, 3, 6, 1, 4, 1, 97, 3, 7, 2, 1, 22),
    _SifDesigPort_Type()
)
sifDesigPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sifDesigPort.setStatus("mandatory")
_SifRxPackets_Type = OctetString
_SifRxPackets_Object = MibTableColumn
sifRxPackets = _SifRxPackets_Object(
    (1, 3, 6, 1, 4, 1, 97, 3, 7, 2, 1, 23),
    _SifRxPackets_Type()
)
sifRxPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sifRxPackets.setStatus("mandatory")
_SifRxChar0s_Type = Counter32
_SifRxChar0s_Object = MibTableColumn
sifRxChar0s = _SifRxChar0s_Object(
    (1, 3, 6, 1, 4, 1, 97, 3, 7, 2, 1, 24),
    _SifRxChar0s_Type()
)
sifRxChar0s.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sifRxChar0s.setStatus("mandatory")
_SifRxChar1s_Type = Counter32
_SifRxChar1s_Object = MibTableColumn
sifRxChar1s = _SifRxChar1s_Object(
    (1, 3, 6, 1, 4, 1, 97, 3, 7, 2, 1, 25),
    _SifRxChar1s_Type()
)
sifRxChar1s.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sifRxChar1s.setStatus("mandatory")
_SifRxSizeErrors_Type = Counter32
_SifRxSizeErrors_Object = MibTableColumn
sifRxSizeErrors = _SifRxSizeErrors_Object(
    (1, 3, 6, 1, 4, 1, 97, 3, 7, 2, 1, 26),
    _SifRxSizeErrors_Type()
)
sifRxSizeErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sifRxSizeErrors.setStatus("mandatory")
_SifRxHwFCSs_Type = Counter32
_SifRxHwFCSs_Object = MibTableColumn
sifRxHwFCSs = _SifRxHwFCSs_Object(
    (1, 3, 6, 1, 4, 1, 97, 3, 7, 2, 1, 27),
    _SifRxHwFCSs_Type()
)
sifRxHwFCSs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sifRxHwFCSs.setStatus("mandatory")
_SifRxQueues_Type = Counter32
_SifRxQueues_Object = MibTableColumn
sifRxQueues = _SifRxQueues_Object(
    (1, 3, 6, 1, 4, 1, 97, 3, 7, 2, 1, 28),
    _SifRxQueues_Type()
)
sifRxQueues.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sifRxQueues.setStatus("mandatory")
_SifTxPackets_Type = OctetString
_SifTxPackets_Object = MibTableColumn
sifTxPackets = _SifTxPackets_Object(
    (1, 3, 6, 1, 4, 1, 97, 3, 7, 2, 1, 30),
    _SifTxPackets_Type()
)
sifTxPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sifTxPackets.setStatus("mandatory")
_SifTxCongests_Type = Counter32
_SifTxCongests_Object = MibTableColumn
sifTxCongests = _SifTxCongests_Object(
    (1, 3, 6, 1, 4, 1, 97, 3, 7, 2, 1, 31),
    _SifTxCongests_Type()
)
sifTxCongests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sifTxCongests.setStatus("obsolete")
_SifTxStorms_Type = Counter32
_SifTxStorms_Object = MibTableColumn
sifTxStorms = _SifTxStorms_Object(
    (1, 3, 6, 1, 4, 1, 97, 3, 7, 2, 1, 32),
    _SifTxStorms_Type()
)
sifTxStorms.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sifTxStorms.setStatus("mandatory")
_SifTxDests_Type = Counter32
_SifTxDests_Object = MibTableColumn
sifTxDests = _SifTxDests_Object(
    (1, 3, 6, 1, 4, 1, 97, 3, 7, 2, 1, 33),
    _SifTxDests_Type()
)
sifTxDests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sifTxDests.setStatus("mandatory")


class _SifErrorsFlag_Type(Integer32):
    """Custom type sifErrorsFlag based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 2),
          ("true", 1))
    )


_SifErrorsFlag_Type.__name__ = "Integer32"
_SifErrorsFlag_Object = MibTableColumn
sifErrorsFlag = _SifErrorsFlag_Object(
    (1, 3, 6, 1, 4, 1, 97, 3, 7, 2, 1, 34),
    _SifErrorsFlag_Type()
)
sifErrorsFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sifErrorsFlag.setStatus("mandatory")


class _SifTxStormFlag_Type(Integer32):
    """Custom type sifTxStormFlag based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 2),
          ("true", 1))
    )


_SifTxStormFlag_Type.__name__ = "Integer32"
_SifTxStormFlag_Object = MibTableColumn
sifTxStormFlag = _SifTxStormFlag_Object(
    (1, 3, 6, 1, 4, 1, 97, 3, 7, 2, 1, 35),
    _SifTxStormFlag_Type()
)
sifTxStormFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sifTxStormFlag.setStatus("mandatory")
_SifTxSizes_Type = Counter32
_SifTxSizes_Object = MibTableColumn
sifTxSizes = _SifTxSizes_Object(
    (1, 3, 6, 1, 4, 1, 97, 3, 7, 2, 1, 36),
    _SifTxSizes_Type()
)
sifTxSizes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sifTxSizes.setStatus("mandatory")
_SifTxAddr_Type = OctetString
_SifTxAddr_Object = MibTableColumn
sifTxAddr = _SifTxAddr_Object(
    (1, 3, 6, 1, 4, 1, 97, 3, 7, 2, 1, 37),
    _SifTxAddr_Type()
)
sifTxAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sifTxAddr.setStatus("mandatory")
_SifLan_Type = Integer32
_SifLan_Object = MibTableColumn
sifLan = _SifLan_Object(
    (1, 3, 6, 1, 4, 1, 97, 3, 7, 2, 1, 38),
    _SifLan_Type()
)
sifLan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sifLan.setStatus("mandatory")
_SifStatisticsTime_Type = TimeTicks
_SifStatisticsTime_Object = MibTableColumn
sifStatisticsTime = _SifStatisticsTime_Object(
    (1, 3, 6, 1, 4, 1, 97, 3, 7, 2, 1, 39),
    _SifStatisticsTime_Type()
)
sifStatisticsTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sifStatisticsTime.setStatus("mandatory")
_SifIpAddress_Type = IpAddress
_SifIpAddress_Object = MibTableColumn
sifIpAddress = _SifIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 97, 3, 7, 2, 1, 40),
    _SifIpAddress_Type()
)
sifIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sifIpAddress.setStatus("mandatory")
_SifIpGroupAddress_Type = IpAddress
_SifIpGroupAddress_Object = MibTableColumn
sifIpGroupAddress = _SifIpGroupAddress_Object(
    (1, 3, 6, 1, 4, 1, 97, 3, 7, 2, 1, 41),
    _SifIpGroupAddress_Type()
)
sifIpGroupAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sifIpGroupAddress.setStatus("mandatory")
_SifMaxPacketSize_Type = Integer32
_SifMaxPacketSize_Object = MibTableColumn
sifMaxPacketSize = _SifMaxPacketSize_Object(
    (1, 3, 6, 1, 4, 1, 97, 3, 7, 2, 1, 42),
    _SifMaxPacketSize_Type()
)
sifMaxPacketSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sifMaxPacketSize.setStatus("mandatory")


class _SifExpectSqe_Type(Integer32):
    """Custom type sifExpectSqe based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 2),
          ("true", 1))
    )


_SifExpectSqe_Type.__name__ = "Integer32"
_SifExpectSqe_Object = MibTableColumn
sifExpectSqe = _SifExpectSqe_Object(
    (1, 3, 6, 1, 4, 1, 97, 3, 7, 2, 1, 43),
    _SifExpectSqe_Type()
)
sifExpectSqe.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sifExpectSqe.setStatus("mandatory")


class _SifFilterLocal_Type(Integer32):
    """Custom type sifFilterLocal based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 2),
          ("true", 1))
    )


_SifFilterLocal_Type.__name__ = "Integer32"
_SifFilterLocal_Object = MibTableColumn
sifFilterLocal = _SifFilterLocal_Object(
    (1, 3, 6, 1, 4, 1, 97, 3, 7, 2, 1, 44),
    _SifFilterLocal_Type()
)
sifFilterLocal.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sifFilterLocal.setStatus("mandatory")
_SifInQLen_Type = Gauge32
_SifInQLen_Object = MibTableColumn
sifInQLen = _SifInQLen_Object(
    (1, 3, 6, 1, 4, 1, 97, 3, 7, 2, 1, 45),
    _SifInQLen_Type()
)
sifInQLen.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sifInQLen.setStatus("mandatory")


class _SifFrameSwitching_Type(Integer32):
    """Custom type sifFrameSwitching based on Integer32"""
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


_SifFrameSwitching_Type.__name__ = "Integer32"
_SifFrameSwitching_Object = MibTableColumn
sifFrameSwitching = _SifFrameSwitching_Object(
    (1, 3, 6, 1, 4, 1, 97, 3, 7, 2, 1, 46),
    _SifFrameSwitching_Type()
)
sifFrameSwitching.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sifFrameSwitching.setStatus("mandatory")
_SifRingDrops_Type = Counter32
_SifRingDrops_Object = MibTableColumn
sifRingDrops = _SifRingDrops_Object(
    (1, 3, 6, 1, 4, 1, 97, 3, 7, 2, 1, 47),
    _SifRingDrops_Type()
)
sifRingDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sifRingDrops.setStatus("mandatory")
_SifAdapterChecks_Type = Counter32
_SifAdapterChecks_Object = MibTableColumn
sifAdapterChecks = _SifAdapterChecks_Object(
    (1, 3, 6, 1, 4, 1, 97, 3, 7, 2, 1, 48),
    _SifAdapterChecks_Type()
)
sifAdapterChecks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sifAdapterChecks.setStatus("mandatory")
_SifIpRipPortMetric_Type = Integer32
_SifIpRipPortMetric_Object = MibTableColumn
sifIpRipPortMetric = _SifIpRipPortMetric_Object(
    (1, 3, 6, 1, 4, 1, 97, 3, 7, 2, 1, 49),
    _SifIpRipPortMetric_Type()
)
sifIpRipPortMetric.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sifIpRipPortMetric.setStatus("mandatory")
_SifDescr_Type = OctetString
_SifDescr_Object = MibTableColumn
sifDescr = _SifDescr_Object(
    (1, 3, 6, 1, 4, 1, 97, 3, 7, 2, 1, 50),
    _SifDescr_Type()
)
sifDescr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sifDescr.setStatus("mandatory")
_SifUtilInterval_Type = Integer32
_SifUtilInterval_Object = MibScalar
sifUtilInterval = _SifUtilInterval_Object(
    (1, 3, 6, 1, 4, 1, 97, 3, 7, 3),
    _SifUtilInterval_Type()
)
sifUtilInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sifUtilInterval.setStatus("mandatory")
_SifUtilCount_Type = Integer32
_SifUtilCount_Object = MibScalar
sifUtilCount = _SifUtilCount_Object(
    (1, 3, 6, 1, 4, 1, 97, 3, 7, 4),
    _SifUtilCount_Type()
)
sifUtilCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sifUtilCount.setStatus("mandatory")


class _SifUtilPortPeakReset_Type(Integer32):
    """Custom type sifUtilPortPeakReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("true", 1)
    )


_SifUtilPortPeakReset_Type.__name__ = "Integer32"
_SifUtilPortPeakReset_Object = MibScalar
sifUtilPortPeakReset = _SifUtilPortPeakReset_Object(
    (1, 3, 6, 1, 4, 1, 97, 3, 7, 5),
    _SifUtilPortPeakReset_Type()
)
sifUtilPortPeakReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sifUtilPortPeakReset.setStatus("mandatory")
_SifUtilPortPeakTable_Object = MibTable
sifUtilPortPeakTable = _SifUtilPortPeakTable_Object(
    (1, 3, 6, 1, 4, 1, 97, 3, 7, 6)
)
if mibBuilder.loadTexts:
    sifUtilPortPeakTable.setStatus("mandatory")
_SifUtilPortPeakEntry_Object = MibTableRow
sifUtilPortPeakEntry = _SifUtilPortPeakEntry_Object(
    (1, 3, 6, 1, 4, 1, 97, 3, 7, 6, 1)
)
sifUtilPortPeakEntry.setIndexNames(
    (0, "CTATX-MIB", "sifUtilPortPeakIndex"),
    (0, "CTATX-MIB", "sifUtilPortPeakOrdinal"),
)
if mibBuilder.loadTexts:
    sifUtilPortPeakEntry.setStatus("mandatory")
_SifUtilPortPeakIndex_Type = Integer32
_SifUtilPortPeakIndex_Object = MibTableColumn
sifUtilPortPeakIndex = _SifUtilPortPeakIndex_Object(
    (1, 3, 6, 1, 4, 1, 97, 3, 7, 6, 1, 1),
    _SifUtilPortPeakIndex_Type()
)
sifUtilPortPeakIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sifUtilPortPeakIndex.setStatus("mandatory")
_SifUtilPortPeakOrdinal_Type = Integer32
_SifUtilPortPeakOrdinal_Object = MibTableColumn
sifUtilPortPeakOrdinal = _SifUtilPortPeakOrdinal_Object(
    (1, 3, 6, 1, 4, 1, 97, 3, 7, 6, 1, 2),
    _SifUtilPortPeakOrdinal_Type()
)
sifUtilPortPeakOrdinal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sifUtilPortPeakOrdinal.setStatus("mandatory")
_SifUtilPortPeakBRTimestamp_Type = TimeTicks
_SifUtilPortPeakBRTimestamp_Object = MibTableColumn
sifUtilPortPeakBRTimestamp = _SifUtilPortPeakBRTimestamp_Object(
    (1, 3, 6, 1, 4, 1, 97, 3, 7, 6, 1, 3),
    _SifUtilPortPeakBRTimestamp_Type()
)
sifUtilPortPeakBRTimestamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sifUtilPortPeakBRTimestamp.setStatus("mandatory")


class _SifUtilPortPeakTBitRate_Type(Integer32):
    """Custom type sifUtilPortPeakTBitRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 99),
    )


_SifUtilPortPeakTBitRate_Type.__name__ = "Integer32"
_SifUtilPortPeakTBitRate_Object = MibTableColumn
sifUtilPortPeakTBitRate = _SifUtilPortPeakTBitRate_Object(
    (1, 3, 6, 1, 4, 1, 97, 3, 7, 6, 1, 4),
    _SifUtilPortPeakTBitRate_Type()
)
sifUtilPortPeakTBitRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sifUtilPortPeakTBitRate.setStatus("mandatory")


class _SifUtilPortPeakRBitRate_Type(Integer32):
    """Custom type sifUtilPortPeakRBitRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 99),
    )


_SifUtilPortPeakRBitRate_Type.__name__ = "Integer32"
_SifUtilPortPeakRBitRate_Object = MibTableColumn
sifUtilPortPeakRBitRate = _SifUtilPortPeakRBitRate_Object(
    (1, 3, 6, 1, 4, 1, 97, 3, 7, 6, 1, 5),
    _SifUtilPortPeakRBitRate_Type()
)
sifUtilPortPeakRBitRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sifUtilPortPeakRBitRate.setStatus("mandatory")


class _SifUtilSysPeakReset_Type(Integer32):
    """Custom type sifUtilSysPeakReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("true", 1)
    )


_SifUtilSysPeakReset_Type.__name__ = "Integer32"
_SifUtilSysPeakReset_Object = MibScalar
sifUtilSysPeakReset = _SifUtilSysPeakReset_Object(
    (1, 3, 6, 1, 4, 1, 97, 3, 7, 7),
    _SifUtilSysPeakReset_Type()
)
sifUtilSysPeakReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sifUtilSysPeakReset.setStatus("mandatory")
_SifUtilSysPeakTable_Object = MibTable
sifUtilSysPeakTable = _SifUtilSysPeakTable_Object(
    (1, 3, 6, 1, 4, 1, 97, 3, 7, 8)
)
if mibBuilder.loadTexts:
    sifUtilSysPeakTable.setStatus("mandatory")
_SifUtilSysPeakEntry_Object = MibTableRow
sifUtilSysPeakEntry = _SifUtilSysPeakEntry_Object(
    (1, 3, 6, 1, 4, 1, 97, 3, 7, 8, 1)
)
sifUtilSysPeakEntry.setIndexNames(
    (0, "CTATX-MIB", "sifUtilSysPeakIndex"),
    (0, "CTATX-MIB", "sifUtilSysPeakOrdinal"),
)
if mibBuilder.loadTexts:
    sifUtilSysPeakEntry.setStatus("mandatory")
_SifUtilSysPeakIndex_Type = Integer32
_SifUtilSysPeakIndex_Object = MibTableColumn
sifUtilSysPeakIndex = _SifUtilSysPeakIndex_Object(
    (1, 3, 6, 1, 4, 1, 97, 3, 7, 8, 1, 1),
    _SifUtilSysPeakIndex_Type()
)
sifUtilSysPeakIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sifUtilSysPeakIndex.setStatus("mandatory")
_SifUtilSysPeakOrdinal_Type = Integer32
_SifUtilSysPeakOrdinal_Object = MibTableColumn
sifUtilSysPeakOrdinal = _SifUtilSysPeakOrdinal_Object(
    (1, 3, 6, 1, 4, 1, 97, 3, 7, 8, 1, 2),
    _SifUtilSysPeakOrdinal_Type()
)
sifUtilSysPeakOrdinal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sifUtilSysPeakOrdinal.setStatus("mandatory")
_SifUtilSysPeakTimestamp_Type = TimeTicks
_SifUtilSysPeakTimestamp_Object = MibTableColumn
sifUtilSysPeakTimestamp = _SifUtilSysPeakTimestamp_Object(
    (1, 3, 6, 1, 4, 1, 97, 3, 7, 8, 1, 3),
    _SifUtilSysPeakTimestamp_Type()
)
sifUtilSysPeakTimestamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sifUtilSysPeakTimestamp.setStatus("mandatory")


class _SifUtilSysPeakTBitRate_Type(Integer32):
    """Custom type sifUtilSysPeakTBitRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 99),
    )


_SifUtilSysPeakTBitRate_Type.__name__ = "Integer32"
_SifUtilSysPeakTBitRate_Object = MibTableColumn
sifUtilSysPeakTBitRate = _SifUtilSysPeakTBitRate_Object(
    (1, 3, 6, 1, 4, 1, 97, 3, 7, 8, 1, 4),
    _SifUtilSysPeakTBitRate_Type()
)
sifUtilSysPeakTBitRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sifUtilSysPeakTBitRate.setStatus("mandatory")


class _SifUtilSysPeakRBitRate_Type(Integer32):
    """Custom type sifUtilSysPeakRBitRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 99),
    )


_SifUtilSysPeakRBitRate_Type.__name__ = "Integer32"
_SifUtilSysPeakRBitRate_Object = MibTableColumn
sifUtilSysPeakRBitRate = _SifUtilSysPeakRBitRate_Object(
    (1, 3, 6, 1, 4, 1, 97, 3, 7, 8, 1, 5),
    _SifUtilSysPeakRBitRate_Type()
)
sifUtilSysPeakRBitRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sifUtilSysPeakRBitRate.setStatus("mandatory")
_Sfddi_ObjectIdentity = ObjectIdentity
sfddi = _Sfddi_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 97, 3, 8)
)
_SfddiTable_Object = MibTable
sfddiTable = _SfddiTable_Object(
    (1, 3, 6, 1, 4, 1, 97, 3, 8, 1)
)
if mibBuilder.loadTexts:
    sfddiTable.setStatus("mandatory")
_SfddiEntry_Object = MibTableRow
sfddiEntry = _SfddiEntry_Object(
    (1, 3, 6, 1, 4, 1, 97, 3, 8, 1, 1)
)
sfddiEntry.setIndexNames(
    (0, "CTATX-MIB", "sfddiIndex"),
)
if mibBuilder.loadTexts:
    sfddiEntry.setStatus("mandatory")
_SfddiIndex_Type = Integer32
_SfddiIndex_Object = MibTableColumn
sfddiIndex = _SfddiIndex_Object(
    (1, 3, 6, 1, 4, 1, 97, 3, 8, 1, 1, 1),
    _SfddiIndex_Type()
)
sfddiIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfddiIndex.setStatus("mandatory")
_SfddiRxHwAborts_Type = Counter32
_SfddiRxHwAborts_Object = MibTableColumn
sfddiRxHwAborts = _SfddiRxHwAborts_Object(
    (1, 3, 6, 1, 4, 1, 97, 3, 8, 1, 1, 2),
    _SfddiRxHwAborts_Type()
)
sfddiRxHwAborts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfddiRxHwAborts.setStatus("mandatory")
_SfddiRxParitys_Type = Counter32
_SfddiRxParitys_Object = MibTableColumn
sfddiRxParitys = _SfddiRxParitys_Object(
    (1, 3, 6, 1, 4, 1, 97, 3, 8, 1, 1, 3),
    _SfddiRxParitys_Type()
)
sfddiRxParitys.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfddiRxParitys.setStatus("mandatory")
_SfddiRxShorts_Type = Counter32
_SfddiRxShorts_Object = MibTableColumn
sfddiRxShorts = _SfddiRxShorts_Object(
    (1, 3, 6, 1, 4, 1, 97, 3, 8, 1, 1, 4),
    _SfddiRxShorts_Type()
)
sfddiRxShorts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfddiRxShorts.setStatus("mandatory")
_SfddiDpcErrCnts_Type = Counter32
_SfddiDpcErrCnts_Object = MibTableColumn
sfddiDpcErrCnts = _SfddiDpcErrCnts_Object(
    (1, 3, 6, 1, 4, 1, 97, 3, 8, 1, 1, 5),
    _SfddiDpcErrCnts_Type()
)
sfddiDpcErrCnts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfddiDpcErrCnts.setStatus("mandatory")
_SfddiDpcErrValue_Type = Integer32
_SfddiDpcErrValue_Object = MibTableColumn
sfddiDpcErrValue = _SfddiDpcErrValue_Object(
    (1, 3, 6, 1, 4, 1, 97, 3, 8, 1, 1, 6),
    _SfddiDpcErrValue_Type()
)
sfddiDpcErrValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfddiDpcErrValue.setStatus("mandatory")
_SfddiRbcErrCnts_Type = Counter32
_SfddiRbcErrCnts_Object = MibTableColumn
sfddiRbcErrCnts = _SfddiRbcErrCnts_Object(
    (1, 3, 6, 1, 4, 1, 97, 3, 8, 1, 1, 7),
    _SfddiRbcErrCnts_Type()
)
sfddiRbcErrCnts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfddiRbcErrCnts.setStatus("mandatory")
_SfddiRbcErrValue_Type = Integer32
_SfddiRbcErrValue_Object = MibTableColumn
sfddiRbcErrValue = _SfddiRbcErrValue_Object(
    (1, 3, 6, 1, 4, 1, 97, 3, 8, 1, 1, 8),
    _SfddiRbcErrValue_Type()
)
sfddiRbcErrValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfddiRbcErrValue.setStatus("mandatory")
_SfddiTxAsync_Type = Integer32
_SfddiTxAsync_Object = MibTableColumn
sfddiTxAsync = _SfddiTxAsync_Object(
    (1, 3, 6, 1, 4, 1, 97, 3, 8, 1, 1, 9),
    _SfddiTxAsync_Type()
)
sfddiTxAsync.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfddiTxAsync.setStatus("mandatory")


class _SfddiShortAddressing_Type(Integer32):
    """Custom type sfddiShortAddressing based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 2),
          ("true", 1))
    )


_SfddiShortAddressing_Type.__name__ = "Integer32"
_SfddiShortAddressing_Object = MibTableColumn
sfddiShortAddressing = _SfddiShortAddressing_Object(
    (1, 3, 6, 1, 4, 1, 97, 3, 8, 1, 1, 10),
    _SfddiShortAddressing_Type()
)
sfddiShortAddressing.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfddiShortAddressing.setStatus("mandatory")
_SfddiSmtConditions_Type = Integer32
_SfddiSmtConditions_Object = MibTableColumn
sfddiSmtConditions = _SfddiSmtConditions_Object(
    (1, 3, 6, 1, 4, 1, 97, 3, 8, 1, 1, 11),
    _SfddiSmtConditions_Type()
)
sfddiSmtConditions.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfddiSmtConditions.setStatus("mandatory")
_SfddiSrfConditions_Type = Integer32
_SfddiSrfConditions_Object = MibTableColumn
sfddiSrfConditions = _SfddiSrfConditions_Object(
    (1, 3, 6, 1, 4, 1, 97, 3, 8, 1, 1, 12),
    _SfddiSrfConditions_Type()
)
sfddiSrfConditions.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfddiSrfConditions.setStatus("mandatory")
_SfddiSmtConditionsStatus_Type = Integer32
_SfddiSmtConditionsStatus_Object = MibTableColumn
sfddiSmtConditionsStatus = _SfddiSmtConditionsStatus_Object(
    (1, 3, 6, 1, 4, 1, 97, 3, 8, 1, 1, 13),
    _SfddiSmtConditionsStatus_Type()
)
sfddiSmtConditionsStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfddiSmtConditionsStatus.setStatus("mandatory")
_SfddiSrfConditionsStatus_Type = Integer32
_SfddiSrfConditionsStatus_Object = MibTableColumn
sfddiSrfConditionsStatus = _SfddiSrfConditionsStatus_Object(
    (1, 3, 6, 1, 4, 1, 97, 3, 8, 1, 1, 14),
    _SfddiSrfConditionsStatus_Type()
)
sfddiSrfConditionsStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfddiSrfConditionsStatus.setStatus("mandatory")
_SfddiSrfReportLimit_Type = Integer32
_SfddiSrfReportLimit_Object = MibTableColumn
sfddiSrfReportLimit = _SfddiSrfReportLimit_Object(
    (1, 3, 6, 1, 4, 1, 97, 3, 8, 1, 1, 15),
    _SfddiSrfReportLimit_Type()
)
sfddiSrfReportLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfddiSrfReportLimit.setStatus("mandatory")
_SfddiFrameErrorThreshold_Type = Integer32
_SfddiFrameErrorThreshold_Object = MibTableColumn
sfddiFrameErrorThreshold = _SfddiFrameErrorThreshold_Object(
    (1, 3, 6, 1, 4, 1, 97, 3, 8, 1, 1, 16),
    _SfddiFrameErrorThreshold_Type()
)
sfddiFrameErrorThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfddiFrameErrorThreshold.setStatus("mandatory")
_SfddiNotCopiedThreshold_Type = Integer32
_SfddiNotCopiedThreshold_Object = MibTableColumn
sfddiNotCopiedThreshold = _SfddiNotCopiedThreshold_Object(
    (1, 3, 6, 1, 4, 1, 97, 3, 8, 1, 1, 17),
    _SfddiNotCopiedThreshold_Type()
)
sfddiNotCopiedThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfddiNotCopiedThreshold.setStatus("mandatory")


class _SfddiSBFlag_Type(Integer32):
    """Custom type sfddiSBFlag based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 2),
          ("true", 1))
    )


_SfddiSBFlag_Type.__name__ = "Integer32"
_SfddiSBFlag_Object = MibTableColumn
sfddiSBFlag = _SfddiSBFlag_Object(
    (1, 3, 6, 1, 4, 1, 97, 3, 8, 1, 1, 18),
    _SfddiSBFlag_Type()
)
sfddiSBFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfddiSBFlag.setStatus("mandatory")
_SfddiRxEbits_Type = Counter32
_SfddiRxEbits_Object = MibTableColumn
sfddiRxEbits = _SfddiRxEbits_Object(
    (1, 3, 6, 1, 4, 1, 97, 3, 8, 1, 1, 19),
    _SfddiRxEbits_Type()
)
sfddiRxEbits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfddiRxEbits.setStatus("mandatory")


class _SfddiOBSFuseBad_Type(Integer32):
    """Custom type sfddiOBSFuseBad based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 2),
          ("true", 1))
    )


_SfddiOBSFuseBad_Type.__name__ = "Integer32"
_SfddiOBSFuseBad_Object = MibTableColumn
sfddiOBSFuseBad = _SfddiOBSFuseBad_Object(
    (1, 3, 6, 1, 4, 1, 97, 3, 8, 1, 1, 20),
    _SfddiOBSFuseBad_Type()
)
sfddiOBSFuseBad.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfddiOBSFuseBad.setStatus("mandatory")


class _SfddiThruB_Type(Integer32):
    """Custom type sfddiThruB based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 2),
          ("true", 1))
    )


_SfddiThruB_Type.__name__ = "Integer32"
_SfddiThruB_Object = MibTableColumn
sfddiThruB = _SfddiThruB_Object(
    (1, 3, 6, 1, 4, 1, 97, 3, 8, 1, 1, 21),
    _SfddiThruB_Type()
)
sfddiThruB.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfddiThruB.setStatus("mandatory")
_SfddiStationDescriptor_Type = OctetString
_SfddiStationDescriptor_Object = MibTableColumn
sfddiStationDescriptor = _SfddiStationDescriptor_Object(
    (1, 3, 6, 1, 4, 1, 97, 3, 8, 1, 1, 22),
    _SfddiStationDescriptor_Type()
)
sfddiStationDescriptor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfddiStationDescriptor.setStatus("mandatory")
_SfddiStationState_Type = OctetString
_SfddiStationState_Object = MibTableColumn
sfddiStationState = _SfddiStationState_Object(
    (1, 3, 6, 1, 4, 1, 97, 3, 8, 1, 1, 23),
    _SfddiStationState_Type()
)
sfddiStationState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfddiStationState.setStatus("mandatory")
_SfddiDownstreamNbr_Type = OctetString
_SfddiDownstreamNbr_Object = MibTableColumn
sfddiDownstreamNbr = _SfddiDownstreamNbr_Object(
    (1, 3, 6, 1, 4, 1, 97, 3, 8, 1, 1, 24),
    _SfddiDownstreamNbr_Type()
)
sfddiDownstreamNbr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfddiDownstreamNbr.setStatus("mandatory")
_SfddiSMTBufferSize_Type = Integer32
_SfddiSMTBufferSize_Object = MibTableColumn
sfddiSMTBufferSize = _SfddiSMTBufferSize_Object(
    (1, 3, 6, 1, 4, 1, 97, 3, 8, 1, 1, 25),
    _SfddiSMTBufferSize_Type()
)
sfddiSMTBufferSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfddiSMTBufferSize.setStatus("mandatory")
_Suart_ObjectIdentity = ObjectIdentity
suart = _Suart_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 97, 3, 9)
)
_SuartTable_Object = MibTable
suartTable = _SuartTable_Object(
    (1, 3, 6, 1, 4, 1, 97, 3, 9, 1)
)
if mibBuilder.loadTexts:
    suartTable.setStatus("mandatory")
_SuartEntry_Object = MibTableRow
suartEntry = _SuartEntry_Object(
    (1, 3, 6, 1, 4, 1, 97, 3, 9, 1, 1)
)
suartEntry.setIndexNames(
    (0, "CTATX-MIB", "suartIndex"),
)
if mibBuilder.loadTexts:
    suartEntry.setStatus("mandatory")
_SuartIndex_Type = Integer32
_SuartIndex_Object = MibTableColumn
suartIndex = _SuartIndex_Object(
    (1, 3, 6, 1, 4, 1, 97, 3, 9, 1, 1, 1),
    _SuartIndex_Type()
)
suartIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    suartIndex.setStatus("mandatory")


class _SuartBaud_Type(Integer32):
    """Custom type suartBaud based on Integer32"""
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
              8,
              9,
              10,
              11)
        )
    )
    namedValues = NamedValues(
        *(("b1200-baud", 2),
          ("b1544-kilobits", 9),
          ("b19200-baud", 6),
          ("b2048-kilobits", 10),
          ("b2400-baud", 3),
          ("b38400-baud", 7),
          ("b45-megabits", 11),
          ("b4800-baud", 4),
          ("b56-kilobits", 8),
          ("b9600-baud", 5),
          ("external-clock", 1))
    )


_SuartBaud_Type.__name__ = "Integer32"
_SuartBaud_Object = MibTableColumn
suartBaud = _SuartBaud_Object(
    (1, 3, 6, 1, 4, 1, 97, 3, 9, 1, 1, 2),
    _SuartBaud_Type()
)
suartBaud.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    suartBaud.setStatus("mandatory")
_SuartModem_Type = Integer32
_SuartModem_Object = MibTableColumn
suartModem = _SuartModem_Object(
    (1, 3, 6, 1, 4, 1, 97, 3, 9, 1, 1, 3),
    _SuartModem_Type()
)
suartModem.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    suartModem.setStatus("mandatory")
_SuartIpNeighborAddress_Type = IpAddress
_SuartIpNeighborAddress_Object = MibTableColumn
suartIpNeighborAddress = _SuartIpNeighborAddress_Object(
    (1, 3, 6, 1, 4, 1, 97, 3, 9, 1, 1, 4),
    _SuartIpNeighborAddress_Type()
)
suartIpNeighborAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    suartIpNeighborAddress.setStatus("mandatory")


class _SuartPPPActive_Type(Integer32):
    """Custom type suartPPPActive based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 2),
          ("true", 1))
    )


_SuartPPPActive_Type.__name__ = "Integer32"
_SuartPPPActive_Object = MibTableColumn
suartPPPActive = _SuartPPPActive_Object(
    (1, 3, 6, 1, 4, 1, 97, 3, 9, 1, 1, 5),
    _SuartPPPActive_Type()
)
suartPPPActive.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    suartPPPActive.setStatus("mandatory")
_SuartAlignmentErrors_Type = Counter32
_SuartAlignmentErrors_Object = MibTableColumn
suartAlignmentErrors = _SuartAlignmentErrors_Object(
    (1, 3, 6, 1, 4, 1, 97, 3, 9, 1, 1, 6),
    _SuartAlignmentErrors_Type()
)
suartAlignmentErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    suartAlignmentErrors.setStatus("mandatory")
_SuartOverrunErrors_Type = Counter32
_SuartOverrunErrors_Object = MibTableColumn
suartOverrunErrors = _SuartOverrunErrors_Object(
    (1, 3, 6, 1, 4, 1, 97, 3, 9, 1, 1, 7),
    _SuartOverrunErrors_Type()
)
suartOverrunErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    suartOverrunErrors.setStatus("mandatory")
_Filter_ObjectIdentity = ObjectIdentity
filter = _Filter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 97, 3, 10)
)
_FilterMaxCount_Type = Integer32
_FilterMaxCount_Object = MibScalar
filterMaxCount = _FilterMaxCount_Object(
    (1, 3, 6, 1, 4, 1, 97, 3, 10, 1),
    _FilterMaxCount_Type()
)
filterMaxCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    filterMaxCount.setStatus("mandatory")
_FilterCurrentCount_Type = Integer32
_FilterCurrentCount_Object = MibScalar
filterCurrentCount = _FilterCurrentCount_Object(
    (1, 3, 6, 1, 4, 1, 97, 3, 10, 2),
    _FilterCurrentCount_Type()
)
filterCurrentCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    filterCurrentCount.setStatus("mandatory")
_FilterDeleteID_Type = Integer32
_FilterDeleteID_Object = MibScalar
filterDeleteID = _FilterDeleteID_Object(
    (1, 3, 6, 1, 4, 1, 97, 3, 10, 3),
    _FilterDeleteID_Type()
)
filterDeleteID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    filterDeleteID.setStatus("mandatory")
_FilterNextID_Type = Integer32
_FilterNextID_Object = MibScalar
filterNextID = _FilterNextID_Object(
    (1, 3, 6, 1, 4, 1, 97, 3, 10, 4),
    _FilterNextID_Type()
)
filterNextID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    filterNextID.setStatus("mandatory")
_FilterAddID_Type = Integer32
_FilterAddID_Object = MibScalar
filterAddID = _FilterAddID_Object(
    (1, 3, 6, 1, 4, 1, 97, 3, 10, 5),
    _FilterAddID_Type()
)
filterAddID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    filterAddID.setStatus("mandatory")
_FilterAddIndex_Type = Integer32
_FilterAddIndex_Object = MibScalar
filterAddIndex = _FilterAddIndex_Object(
    (1, 3, 6, 1, 4, 1, 97, 3, 10, 6),
    _FilterAddIndex_Type()
)
filterAddIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    filterAddIndex.setStatus("mandatory")
_FilterTable_Object = MibTable
filterTable = _FilterTable_Object(
    (1, 3, 6, 1, 4, 1, 97, 3, 10, 7)
)
if mibBuilder.loadTexts:
    filterTable.setStatus("mandatory")
_FilterEntry_Object = MibTableRow
filterEntry = _FilterEntry_Object(
    (1, 3, 6, 1, 4, 1, 97, 3, 10, 7, 1)
)
filterEntry.setIndexNames(
    (0, "CTATX-MIB", "filterIndex"),
)
if mibBuilder.loadTexts:
    filterEntry.setStatus("mandatory")
_FilterIndex_Type = Integer32
_FilterIndex_Object = MibTableColumn
filterIndex = _FilterIndex_Object(
    (1, 3, 6, 1, 4, 1, 97, 3, 10, 7, 1, 1),
    _FilterIndex_Type()
)
filterIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    filterIndex.setStatus("mandatory")
_FilterID_Type = Integer32
_FilterID_Object = MibTableColumn
filterID = _FilterID_Object(
    (1, 3, 6, 1, 4, 1, 97, 3, 10, 7, 1, 2),
    _FilterID_Type()
)
filterID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    filterID.setStatus("mandatory")
_FilterPortNo_Type = Integer32
_FilterPortNo_Object = MibTableColumn
filterPortNo = _FilterPortNo_Object(
    (1, 3, 6, 1, 4, 1, 97, 3, 10, 7, 1, 3),
    _FilterPortNo_Type()
)
filterPortNo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    filterPortNo.setStatus("mandatory")
_FilterComboType_Type = Integer32
_FilterComboType_Object = MibTableColumn
filterComboType = _FilterComboType_Object(
    (1, 3, 6, 1, 4, 1, 97, 3, 10, 7, 1, 4),
    _FilterComboType_Type()
)
filterComboType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    filterComboType.setStatus("mandatory")
_FilterFlags_Type = Integer32
_FilterFlags_Object = MibTableColumn
filterFlags = _FilterFlags_Object(
    (1, 3, 6, 1, 4, 1, 97, 3, 10, 7, 1, 5),
    _FilterFlags_Type()
)
filterFlags.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    filterFlags.setStatus("mandatory")
_FilterFrame_Type = Integer32
_FilterFrame_Object = MibTableColumn
filterFrame = _FilterFrame_Object(
    (1, 3, 6, 1, 4, 1, 97, 3, 10, 7, 1, 6),
    _FilterFrame_Type()
)
filterFrame.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    filterFrame.setStatus("mandatory")
_FilterSource_Type = OctetString
_FilterSource_Object = MibTableColumn
filterSource = _FilterSource_Object(
    (1, 3, 6, 1, 4, 1, 97, 3, 10, 7, 1, 7),
    _FilterSource_Type()
)
filterSource.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    filterSource.setStatus("mandatory")
_FilterSourceEnd_Type = OctetString
_FilterSourceEnd_Object = MibTableColumn
filterSourceEnd = _FilterSourceEnd_Object(
    (1, 3, 6, 1, 4, 1, 97, 3, 10, 7, 1, 8),
    _FilterSourceEnd_Type()
)
filterSourceEnd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    filterSourceEnd.setStatus("mandatory")
_FilterDest_Type = OctetString
_FilterDest_Object = MibTableColumn
filterDest = _FilterDest_Object(
    (1, 3, 6, 1, 4, 1, 97, 3, 10, 7, 1, 9),
    _FilterDest_Type()
)
filterDest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    filterDest.setStatus("mandatory")
_FilterDestEnd_Type = OctetString
_FilterDestEnd_Object = MibTableColumn
filterDestEnd = _FilterDestEnd_Object(
    (1, 3, 6, 1, 4, 1, 97, 3, 10, 7, 1, 10),
    _FilterDestEnd_Type()
)
filterDestEnd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    filterDestEnd.setStatus("mandatory")
_FilterSourceMask_Type = OctetString
_FilterSourceMask_Object = MibTableColumn
filterSourceMask = _FilterSourceMask_Object(
    (1, 3, 6, 1, 4, 1, 97, 3, 10, 7, 1, 11),
    _FilterSourceMask_Type()
)
filterSourceMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    filterSourceMask.setStatus("mandatory")
_FilterDestMask_Type = OctetString
_FilterDestMask_Object = MibTableColumn
filterDestMask = _FilterDestMask_Object(
    (1, 3, 6, 1, 4, 1, 97, 3, 10, 7, 1, 12),
    _FilterDestMask_Type()
)
filterDestMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    filterDestMask.setStatus("mandatory")
_FilterSrcLan_Type = Integer32
_FilterSrcLan_Object = MibTableColumn
filterSrcLan = _FilterSrcLan_Object(
    (1, 3, 6, 1, 4, 1, 97, 3, 10, 7, 1, 13),
    _FilterSrcLan_Type()
)
filterSrcLan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    filterSrcLan.setStatus("mandatory")
_FilterOffset_Type = Integer32
_FilterOffset_Object = MibTableColumn
filterOffset = _FilterOffset_Object(
    (1, 3, 6, 1, 4, 1, 97, 3, 10, 7, 1, 14),
    _FilterOffset_Type()
)
filterOffset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    filterOffset.setStatus("mandatory")
_FilterField_Type = OctetString
_FilterField_Object = MibTableColumn
filterField = _FilterField_Object(
    (1, 3, 6, 1, 4, 1, 97, 3, 10, 7, 1, 15),
    _FilterField_Type()
)
filterField.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    filterField.setStatus("mandatory")
_FilterMask_Type = OctetString
_FilterMask_Object = MibTableColumn
filterMask = _FilterMask_Object(
    (1, 3, 6, 1, 4, 1, 97, 3, 10, 7, 1, 16),
    _FilterMask_Type()
)
filterMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    filterMask.setStatus("mandatory")
_FilterThreshold_Type = Integer32
_FilterThreshold_Object = MibTableColumn
filterThreshold = _FilterThreshold_Object(
    (1, 3, 6, 1, 4, 1, 97, 3, 10, 7, 1, 17),
    _FilterThreshold_Type()
)
filterThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    filterThreshold.setStatus("mandatory")
_FilterThreshTime_Type = Integer32
_FilterThreshTime_Object = MibTableColumn
filterThreshTime = _FilterThreshTime_Object(
    (1, 3, 6, 1, 4, 1, 97, 3, 10, 7, 1, 18),
    _FilterThreshTime_Type()
)
filterThreshTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    filterThreshTime.setStatus("mandatory")


class _FilterThreshFlag_Type(Integer32):
    """Custom type filterThreshFlag based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 2),
          ("true", 1))
    )


_FilterThreshFlag_Type.__name__ = "Integer32"
_FilterThreshFlag_Object = MibTableColumn
filterThreshFlag = _FilterThreshFlag_Object(
    (1, 3, 6, 1, 4, 1, 97, 3, 10, 7, 1, 19),
    _FilterThreshFlag_Type()
)
filterThreshFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    filterThreshFlag.setStatus("mandatory")
_FilterPktCnts_Type = Counter32
_FilterPktCnts_Object = MibTableColumn
filterPktCnts = _FilterPktCnts_Object(
    (1, 3, 6, 1, 4, 1, 97, 3, 10, 7, 1, 20),
    _FilterPktCnts_Type()
)
filterPktCnts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    filterPktCnts.setStatus("mandatory")
_FilterLastSrc_Type = OctetString
_FilterLastSrc_Object = MibTableColumn
filterLastSrc = _FilterLastSrc_Object(
    (1, 3, 6, 1, 4, 1, 97, 3, 10, 7, 1, 21),
    _FilterLastSrc_Type()
)
filterLastSrc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    filterLastSrc.setStatus("mandatory")
_Reboot_ObjectIdentity = ObjectIdentity
reboot = _Reboot_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 97, 3, 11)
)
_RebootBridgingMemory_Type = Integer32
_RebootBridgingMemory_Object = MibScalar
rebootBridgingMemory = _RebootBridgingMemory_Object(
    (1, 3, 6, 1, 4, 1, 97, 3, 11, 1),
    _RebootBridgingMemory_Type()
)
rebootBridgingMemory.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rebootBridgingMemory.setStatus("mandatory")
_RebootSlotTable_Object = MibTable
rebootSlotTable = _RebootSlotTable_Object(
    (1, 3, 6, 1, 4, 1, 97, 3, 11, 2)
)
if mibBuilder.loadTexts:
    rebootSlotTable.setStatus("mandatory")
_RebootEntry_Object = MibTableRow
rebootEntry = _RebootEntry_Object(
    (1, 3, 6, 1, 4, 1, 97, 3, 11, 2, 1)
)
rebootEntry.setIndexNames(
    (0, "CTATX-MIB", "rebootIndex"),
)
if mibBuilder.loadTexts:
    rebootEntry.setStatus("mandatory")
_RebootIndex_Type = Integer32
_RebootIndex_Object = MibTableColumn
rebootIndex = _RebootIndex_Object(
    (1, 3, 6, 1, 4, 1, 97, 3, 11, 2, 1, 1),
    _RebootIndex_Type()
)
rebootIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rebootIndex.setStatus("mandatory")


class _RebootType_Type(Integer32):
    """Custom type rebootType based on Integer32"""
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
              8,
              9,
              10,
              11,
              12)
        )
    )
    namedValues = NamedValues(
        *(("csma-iom", 5),
          ("eiom8-iom", 11),
          ("fddi-iom", 8),
          ("feiom-iom", 12),
          ("hssi-iom", 6),
          ("ifddi-iom", 9),
          ("packet-processing-engine", 3),
          ("tpr-iom", 7),
          ("ttpr-iom", 10),
          ("turbo", 4),
          ("unknown", 2),
          ("vacant", 1))
    )


_RebootType_Type.__name__ = "Integer32"
_RebootType_Object = MibTableColumn
rebootType = _RebootType_Object(
    (1, 3, 6, 1, 4, 1, 97, 3, 11, 2, 1, 2),
    _RebootType_Type()
)
rebootType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rebootType.setStatus("mandatory")


class _RebootUseMod_Type(Integer32):
    """Custom type rebootUseMod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              3)
        )
    )
    namedValues = NamedValues(
        *(("reset", 1),
          ("run", 3))
    )


_RebootUseMod_Type.__name__ = "Integer32"
_RebootUseMod_Object = MibTableColumn
rebootUseMod = _RebootUseMod_Object(
    (1, 3, 6, 1, 4, 1, 97, 3, 11, 2, 1, 3),
    _RebootUseMod_Type()
)
rebootUseMod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rebootUseMod.setStatus("mandatory")
_RebootPortType_Type = OctetString
_RebootPortType_Object = MibTableColumn
rebootPortType = _RebootPortType_Object(
    (1, 3, 6, 1, 4, 1, 97, 3, 11, 2, 1, 4),
    _RebootPortType_Type()
)
rebootPortType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rebootPortType.setStatus("mandatory")


class _RebootConfig_Type(Integer32):
    """Custom type rebootConfig based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("no-change", 1),
          ("revert-to-defaults", 3),
          ("tftp-config", 2))
    )


_RebootConfig_Type.__name__ = "Integer32"
_RebootConfig_Object = MibScalar
rebootConfig = _RebootConfig_Object(
    (1, 3, 6, 1, 4, 1, 97, 3, 11, 3),
    _RebootConfig_Type()
)
rebootConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rebootConfig.setStatus("mandatory")
_RebootRouteMemory_Type = Integer32
_RebootRouteMemory_Object = MibScalar
rebootRouteMemory = _RebootRouteMemory_Object(
    (1, 3, 6, 1, 4, 1, 97, 3, 11, 4),
    _RebootRouteMemory_Type()
)
rebootRouteMemory.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rebootRouteMemory.setStatus("mandatory")
_Debug_ObjectIdentity = ObjectIdentity
debug = _Debug_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 97, 3, 12)
)
_DebugStringID_Type = Integer32
_DebugStringID_Object = MibScalar
debugStringID = _DebugStringID_Object(
    (1, 3, 6, 1, 4, 1, 97, 3, 12, 1),
    _DebugStringID_Type()
)
debugStringID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    debugStringID.setStatus("mandatory")
_DebugString_Type = OctetString
_DebugString_Object = MibScalar
debugString = _DebugString_Object(
    (1, 3, 6, 1, 4, 1, 97, 3, 12, 2),
    _DebugString_Type()
)
debugString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    debugString.setStatus("mandatory")
_DebugTable_Object = MibTable
debugTable = _DebugTable_Object(
    (1, 3, 6, 1, 4, 1, 97, 3, 12, 3)
)
if mibBuilder.loadTexts:
    debugTable.setStatus("mandatory")
_DebugEntry_Object = MibTableRow
debugEntry = _DebugEntry_Object(
    (1, 3, 6, 1, 4, 1, 97, 3, 12, 3, 1)
)
debugEntry.setIndexNames(
    (0, "CTATX-MIB", "debugIndex"),
)
if mibBuilder.loadTexts:
    debugEntry.setStatus("mandatory")
_DebugIndex_Type = Integer32
_DebugIndex_Object = MibTableColumn
debugIndex = _DebugIndex_Object(
    (1, 3, 6, 1, 4, 1, 97, 3, 12, 3, 1, 1),
    _DebugIndex_Type()
)
debugIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    debugIndex.setStatus("mandatory")


class _DebugOperation_Type(Integer32):
    """Custom type debugOperation based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("examine", 1),
          ("modify", 2))
    )


_DebugOperation_Type.__name__ = "Integer32"
_DebugOperation_Object = MibTableColumn
debugOperation = _DebugOperation_Object(
    (1, 3, 6, 1, 4, 1, 97, 3, 12, 3, 1, 2),
    _DebugOperation_Type()
)
debugOperation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    debugOperation.setStatus("mandatory")
_DebugBase_Type = Integer32
_DebugBase_Object = MibTableColumn
debugBase = _DebugBase_Object(
    (1, 3, 6, 1, 4, 1, 97, 3, 12, 3, 1, 3),
    _DebugBase_Type()
)
debugBase.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    debugBase.setStatus("mandatory")
_DebugLength_Type = Integer32
_DebugLength_Object = MibTableColumn
debugLength = _DebugLength_Object(
    (1, 3, 6, 1, 4, 1, 97, 3, 12, 3, 1, 4),
    _DebugLength_Type()
)
debugLength.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    debugLength.setStatus("mandatory")
_DebugData_Type = OctetString
_DebugData_Object = MibTableColumn
debugData = _DebugData_Object(
    (1, 3, 6, 1, 4, 1, 97, 3, 12, 3, 1, 5),
    _DebugData_Type()
)
debugData.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    debugData.setStatus("mandatory")
_Lpbk_ObjectIdentity = ObjectIdentity
lpbk = _Lpbk_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 97, 3, 13)
)
_LpbkTable_Object = MibTable
lpbkTable = _LpbkTable_Object(
    (1, 3, 6, 1, 4, 1, 97, 3, 13, 1)
)
if mibBuilder.loadTexts:
    lpbkTable.setStatus("mandatory")
_LpbkEntry_Object = MibTableRow
lpbkEntry = _LpbkEntry_Object(
    (1, 3, 6, 1, 4, 1, 97, 3, 13, 1, 1)
)
lpbkEntry.setIndexNames(
    (0, "CTATX-MIB", "lpbkIndex"),
)
if mibBuilder.loadTexts:
    lpbkEntry.setStatus("mandatory")
_LpbkIndex_Type = Integer32
_LpbkIndex_Object = MibTableColumn
lpbkIndex = _LpbkIndex_Object(
    (1, 3, 6, 1, 4, 1, 97, 3, 13, 1, 1, 1),
    _LpbkIndex_Type()
)
lpbkIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpbkIndex.setStatus("mandatory")


class _LpbkOperation_Type(Integer32):
    """Custom type lpbkOperation based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("loopback-local", 2),
          ("loopback-off", 1),
          ("loopback-remote", 3))
    )


_LpbkOperation_Type.__name__ = "Integer32"
_LpbkOperation_Object = MibTableColumn
lpbkOperation = _LpbkOperation_Object(
    (1, 3, 6, 1, 4, 1, 97, 3, 13, 1, 1, 2),
    _LpbkOperation_Type()
)
lpbkOperation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lpbkOperation.setStatus("mandatory")
_LpbkDestAddr_Type = OctetString
_LpbkDestAddr_Object = MibTableColumn
lpbkDestAddr = _LpbkDestAddr_Object(
    (1, 3, 6, 1, 4, 1, 97, 3, 13, 1, 1, 3),
    _LpbkDestAddr_Type()
)
lpbkDestAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lpbkDestAddr.setStatus("mandatory")
_LpbkPktNum_Type = Integer32
_LpbkPktNum_Object = MibTableColumn
lpbkPktNum = _LpbkPktNum_Object(
    (1, 3, 6, 1, 4, 1, 97, 3, 13, 1, 1, 4),
    _LpbkPktNum_Type()
)
lpbkPktNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lpbkPktNum.setStatus("mandatory")
_LpbkInterval_Type = TimeTicks
_LpbkInterval_Object = MibTableColumn
lpbkInterval = _LpbkInterval_Object(
    (1, 3, 6, 1, 4, 1, 97, 3, 13, 1, 1, 5),
    _LpbkInterval_Type()
)
lpbkInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lpbkInterval.setStatus("mandatory")
_LpbkPktLength_Type = Integer32
_LpbkPktLength_Object = MibTableColumn
lpbkPktLength = _LpbkPktLength_Object(
    (1, 3, 6, 1, 4, 1, 97, 3, 13, 1, 1, 6),
    _LpbkPktLength_Type()
)
lpbkPktLength.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lpbkPktLength.setStatus("mandatory")
_LpbkIncrements_Type = Integer32
_LpbkIncrements_Object = MibTableColumn
lpbkIncrements = _LpbkIncrements_Object(
    (1, 3, 6, 1, 4, 1, 97, 3, 13, 1, 1, 7),
    _LpbkIncrements_Type()
)
lpbkIncrements.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lpbkIncrements.setStatus("mandatory")
_LpbkGoods_Type = Counter32
_LpbkGoods_Object = MibTableColumn
lpbkGoods = _LpbkGoods_Object(
    (1, 3, 6, 1, 4, 1, 97, 3, 13, 1, 1, 8),
    _LpbkGoods_Type()
)
lpbkGoods.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpbkGoods.setStatus("mandatory")
_LpbkErrorNoReceives_Type = Counter32
_LpbkErrorNoReceives_Object = MibTableColumn
lpbkErrorNoReceives = _LpbkErrorNoReceives_Object(
    (1, 3, 6, 1, 4, 1, 97, 3, 13, 1, 1, 9),
    _LpbkErrorNoReceives_Type()
)
lpbkErrorNoReceives.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpbkErrorNoReceives.setStatus("mandatory")
_LpbkErrorBadReceives_Type = Counter32
_LpbkErrorBadReceives_Object = MibTableColumn
lpbkErrorBadReceives = _LpbkErrorBadReceives_Object(
    (1, 3, 6, 1, 4, 1, 97, 3, 13, 1, 1, 10),
    _LpbkErrorBadReceives_Type()
)
lpbkErrorBadReceives.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpbkErrorBadReceives.setStatus("mandatory")
_LpbkErrorSize_Type = Integer32
_LpbkErrorSize_Object = MibTableColumn
lpbkErrorSize = _LpbkErrorSize_Object(
    (1, 3, 6, 1, 4, 1, 97, 3, 13, 1, 1, 11),
    _LpbkErrorSize_Type()
)
lpbkErrorSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpbkErrorSize.setStatus("mandatory")
_LpbkErrorSent_Type = OctetString
_LpbkErrorSent_Object = MibTableColumn
lpbkErrorSent = _LpbkErrorSent_Object(
    (1, 3, 6, 1, 4, 1, 97, 3, 13, 1, 1, 12),
    _LpbkErrorSent_Type()
)
lpbkErrorSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpbkErrorSent.setStatus("mandatory")
_LpbkErrorReceived_Type = OctetString
_LpbkErrorReceived_Object = MibTableColumn
lpbkErrorReceived = _LpbkErrorReceived_Object(
    (1, 3, 6, 1, 4, 1, 97, 3, 13, 1, 1, 13),
    _LpbkErrorReceived_Type()
)
lpbkErrorReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpbkErrorReceived.setStatus("mandatory")
_LpbkErrorOffset_Type = Integer32
_LpbkErrorOffset_Object = MibTableColumn
lpbkErrorOffset = _LpbkErrorOffset_Object(
    (1, 3, 6, 1, 4, 1, 97, 3, 13, 1, 1, 14),
    _LpbkErrorOffset_Type()
)
lpbkErrorOffset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpbkErrorOffset.setStatus("mandatory")
_Swan_ObjectIdentity = ObjectIdentity
swan = _Swan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 97, 3, 14)
)
_SwanTable_Object = MibTable
swanTable = _SwanTable_Object(
    (1, 3, 6, 1, 4, 1, 97, 3, 14, 1)
)
if mibBuilder.loadTexts:
    swanTable.setStatus("mandatory")
_SwanEntry_Object = MibTableRow
swanEntry = _SwanEntry_Object(
    (1, 3, 6, 1, 4, 1, 97, 3, 14, 1, 1)
)
swanEntry.setIndexNames(
    (0, "CTATX-MIB", "swanIndex"),
)
if mibBuilder.loadTexts:
    swanEntry.setStatus("mandatory")
_SwanIndex_Type = Integer32
_SwanIndex_Object = MibTableColumn
swanIndex = _SwanIndex_Object(
    (1, 3, 6, 1, 4, 1, 97, 3, 14, 1, 1, 1),
    _SwanIndex_Type()
)
swanIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swanIndex.setStatus("mandatory")
_SwanDesiredSpeed_Type = Integer32
_SwanDesiredSpeed_Object = MibTableColumn
swanDesiredSpeed = _SwanDesiredSpeed_Object(
    (1, 3, 6, 1, 4, 1, 97, 3, 14, 1, 1, 2),
    _SwanDesiredSpeed_Type()
)
swanDesiredSpeed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swanDesiredSpeed.setStatus("mandatory")


class _SwanActualSpeed_Type(Integer32):
    """Custom type swanActualSpeed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11)
        )
    )
    namedValues = NamedValues(
        *(("b1200-baud", 2),
          ("b1544-kilobits", 9),
          ("b19200-baud", 6),
          ("b2048-kilobits", 10),
          ("b2400-baud", 3),
          ("b38400-baud", 7),
          ("b45-megabits", 11),
          ("b4800-baud", 4),
          ("b56-kilobits", 8),
          ("b9600-baud", 5))
    )


_SwanActualSpeed_Type.__name__ = "Integer32"
_SwanActualSpeed_Object = MibTableColumn
swanActualSpeed = _SwanActualSpeed_Object(
    (1, 3, 6, 1, 4, 1, 97, 3, 14, 1, 1, 3),
    _SwanActualSpeed_Type()
)
swanActualSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swanActualSpeed.setStatus("mandatory")
_SwanIpNeighborAddress_Type = IpAddress
_SwanIpNeighborAddress_Object = MibTableColumn
swanIpNeighborAddress = _SwanIpNeighborAddress_Object(
    (1, 3, 6, 1, 4, 1, 97, 3, 14, 1, 1, 4),
    _SwanIpNeighborAddress_Type()
)
swanIpNeighborAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swanIpNeighborAddress.setStatus("mandatory")


class _SwanPPPActive_Type(Integer32):
    """Custom type swanPPPActive based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 2),
          ("true", 1))
    )


_SwanPPPActive_Type.__name__ = "Integer32"
_SwanPPPActive_Object = MibTableColumn
swanPPPActive = _SwanPPPActive_Object(
    (1, 3, 6, 1, 4, 1, 97, 3, 14, 1, 1, 5),
    _SwanPPPActive_Type()
)
swanPPPActive.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swanPPPActive.setStatus("mandatory")
_SwanAlignmentErrors_Type = Counter32
_SwanAlignmentErrors_Object = MibTableColumn
swanAlignmentErrors = _SwanAlignmentErrors_Object(
    (1, 3, 6, 1, 4, 1, 97, 3, 14, 1, 1, 6),
    _SwanAlignmentErrors_Type()
)
swanAlignmentErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swanAlignmentErrors.setStatus("mandatory")
_SwanOverrunErrors_Type = Counter32
_SwanOverrunErrors_Object = MibTableColumn
swanOverrunErrors = _SwanOverrunErrors_Object(
    (1, 3, 6, 1, 4, 1, 97, 3, 14, 1, 1, 7),
    _SwanOverrunErrors_Type()
)
swanOverrunErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swanOverrunErrors.setStatus("mandatory")


class _SwanPortType_Type(Integer32):
    """Custom type swanPortType based on Integer32"""
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
              8)
        )
    )
    namedValues = NamedValues(
        *(("wan-e1", 5),
          ("wan-rs530", 7),
          ("wan-t1", 6),
          ("wan-t3", 8),
          ("wan-unknown", 1),
          ("wan-v11", 2),
          ("wan-v24", 3),
          ("wan-v35", 4))
    )


_SwanPortType_Type.__name__ = "Integer32"
_SwanPortType_Object = MibTableColumn
swanPortType = _SwanPortType_Object(
    (1, 3, 6, 1, 4, 1, 97, 3, 14, 1, 1, 8),
    _SwanPortType_Type()
)
swanPortType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swanPortType.setStatus("mandatory")
_SwanLinkCost_Type = Integer32
_SwanLinkCost_Object = MibTableColumn
swanLinkCost = _SwanLinkCost_Object(
    (1, 3, 6, 1, 4, 1, 97, 3, 14, 1, 1, 9),
    _SwanLinkCost_Type()
)
swanLinkCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swanLinkCost.setStatus("mandatory")


class _SwanMeshState_Type(Integer32):
    """Custom type swanMeshState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 2),
          ("true", 1))
    )


_SwanMeshState_Type.__name__ = "Integer32"
_SwanMeshState_Object = MibTableColumn
swanMeshState = _SwanMeshState_Object(
    (1, 3, 6, 1, 4, 1, 97, 3, 14, 1, 1, 10),
    _SwanMeshState_Type()
)
swanMeshState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swanMeshState.setStatus("mandatory")
_SwanLinkSubnet_Type = OctetString
_SwanLinkSubnet_Object = MibTableColumn
swanLinkSubnet = _SwanLinkSubnet_Object(
    (1, 3, 6, 1, 4, 1, 97, 3, 14, 1, 1, 11),
    _SwanLinkSubnet_Type()
)
swanLinkSubnet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swanLinkSubnet.setStatus("mandatory")
_SwanLinkBridge_Type = OctetString
_SwanLinkBridge_Object = MibTableColumn
swanLinkBridge = _SwanLinkBridge_Object(
    (1, 3, 6, 1, 4, 1, 97, 3, 14, 1, 1, 12),
    _SwanLinkBridge_Type()
)
swanLinkBridge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swanLinkBridge.setStatus("mandatory")
_SwanLinkPort_Type = Integer32
_SwanLinkPort_Object = MibTableColumn
swanLinkPort = _SwanLinkPort_Object(
    (1, 3, 6, 1, 4, 1, 97, 3, 14, 1, 1, 13),
    _SwanLinkPort_Type()
)
swanLinkPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swanLinkPort.setStatus("mandatory")


class _SwanNegotiate_Type(Integer32):
    """Custom type swanNegotiate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 2),
          ("true", 1))
    )


_SwanNegotiate_Type.__name__ = "Integer32"
_SwanNegotiate_Object = MibTableColumn
swanNegotiate = _SwanNegotiate_Object(
    (1, 3, 6, 1, 4, 1, 97, 3, 14, 1, 1, 14),
    _SwanNegotiate_Type()
)
swanNegotiate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swanNegotiate.setStatus("mandatory")


class _SwanSwitches_Type(Integer32):
    """Custom type swanSwitches based on Integer32"""
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
        *(("wan-hssi", 1),
          ("wan-hssi-switching-disabled", 3),
          ("wan-t1", 2),
          ("wan-t1-switching-disabled", 4))
    )


_SwanSwitches_Type.__name__ = "Integer32"
_SwanSwitches_Object = MibTableColumn
swanSwitches = _SwanSwitches_Object(
    (1, 3, 6, 1, 4, 1, 97, 3, 14, 1, 1, 15),
    _SwanSwitches_Type()
)
swanSwitches.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swanSwitches.setStatus("mandatory")
_SwanDCEDrops_Type = Counter32
_SwanDCEDrops_Object = MibTableColumn
swanDCEDrops = _SwanDCEDrops_Object(
    (1, 3, 6, 1, 4, 1, 97, 3, 14, 1, 1, 16),
    _SwanDCEDrops_Type()
)
swanDCEDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swanDCEDrops.setStatus("mandatory")


class _SwanOutPacketType_Type(Integer32):
    """Custom type swanOutPacketType based on Integer32"""
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
        *(("ethernet-with-FCS", 4),
          ("ethernet-without-FCS", 3),
          ("token-ring-with-FCS", 2),
          ("token-ring-without-FCS", 1))
    )


_SwanOutPacketType_Type.__name__ = "Integer32"
_SwanOutPacketType_Object = MibTableColumn
swanOutPacketType = _SwanOutPacketType_Object(
    (1, 3, 6, 1, 4, 1, 97, 3, 14, 1, 1, 17),
    _SwanOutPacketType_Type()
)
swanOutPacketType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swanOutPacketType.setStatus("mandatory")


class _SwanLinkErrorPercentage_Type(Integer32):
    """Custom type swanLinkErrorPercentage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10000),
    )


_SwanLinkErrorPercentage_Type.__name__ = "Integer32"
_SwanLinkErrorPercentage_Object = MibTableColumn
swanLinkErrorPercentage = _SwanLinkErrorPercentage_Object(
    (1, 3, 6, 1, 4, 1, 97, 3, 14, 1, 1, 18),
    _SwanLinkErrorPercentage_Type()
)
swanLinkErrorPercentage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swanLinkErrorPercentage.setStatus("mandatory")


class _SwanLinkErrorDuration_Type(Integer32):
    """Custom type swanLinkErrorDuration based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10000),
    )


_SwanLinkErrorDuration_Type.__name__ = "Integer32"
_SwanLinkErrorDuration_Object = MibTableColumn
swanLinkErrorDuration = _SwanLinkErrorDuration_Object(
    (1, 3, 6, 1, 4, 1, 97, 3, 14, 1, 1, 19),
    _SwanLinkErrorDuration_Type()
)
swanLinkErrorDuration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swanLinkErrorDuration.setStatus("mandatory")


class _SwanLinkErrorFailPeriods_Type(Integer32):
    """Custom type swanLinkErrorFailPeriods based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 20),
    )


_SwanLinkErrorFailPeriods_Type.__name__ = "Integer32"
_SwanLinkErrorFailPeriods_Object = MibTableColumn
swanLinkErrorFailPeriods = _SwanLinkErrorFailPeriods_Object(
    (1, 3, 6, 1, 4, 1, 97, 3, 14, 1, 1, 20),
    _SwanLinkErrorFailPeriods_Type()
)
swanLinkErrorFailPeriods.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swanLinkErrorFailPeriods.setStatus("mandatory")


class _SwanLinkErrorMaxPeriods_Type(Integer32):
    """Custom type swanLinkErrorMaxPeriods based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 20),
    )


_SwanLinkErrorMaxPeriods_Type.__name__ = "Integer32"
_SwanLinkErrorMaxPeriods_Object = MibTableColumn
swanLinkErrorMaxPeriods = _SwanLinkErrorMaxPeriods_Object(
    (1, 3, 6, 1, 4, 1, 97, 3, 14, 1, 1, 21),
    _SwanLinkErrorMaxPeriods_Type()
)
swanLinkErrorMaxPeriods.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swanLinkErrorMaxPeriods.setStatus("mandatory")


class _SwanLinkRestartTime_Type(Integer32):
    """Custom type swanLinkRestartTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10000),
    )


_SwanLinkRestartTime_Type.__name__ = "Integer32"
_SwanLinkRestartTime_Object = MibTableColumn
swanLinkRestartTime = _SwanLinkRestartTime_Object(
    (1, 3, 6, 1, 4, 1, 97, 3, 14, 1, 1, 22),
    _SwanLinkRestartTime_Type()
)
swanLinkRestartTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swanLinkRestartTime.setStatus("mandatory")


class _SwanPreserveFCS_Type(Integer32):
    """Custom type swanPreserveFCS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 2),
          ("true", 1))
    )


_SwanPreserveFCS_Type.__name__ = "Integer32"
_SwanPreserveFCS_Object = MibTableColumn
swanPreserveFCS = _SwanPreserveFCS_Object(
    (1, 3, 6, 1, 4, 1, 97, 3, 14, 1, 1, 23),
    _SwanPreserveFCS_Type()
)
swanPreserveFCS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swanPreserveFCS.setStatus("mandatory")
_Srepeater_ObjectIdentity = ObjectIdentity
srepeater = _Srepeater_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 97, 3, 16)
)
_SrepeaterTable_Object = MibTable
srepeaterTable = _SrepeaterTable_Object(
    (1, 3, 6, 1, 4, 1, 97, 3, 16, 1)
)
if mibBuilder.loadTexts:
    srepeaterTable.setStatus("mandatory")
_SrepeaterEntry_Object = MibTableRow
srepeaterEntry = _SrepeaterEntry_Object(
    (1, 3, 6, 1, 4, 1, 97, 3, 16, 1, 1)
)
srepeaterEntry.setIndexNames(
    (0, "CTATX-MIB", "srepeaterGroupID"),
)
if mibBuilder.loadTexts:
    srepeaterEntry.setStatus("mandatory")


class _SrepeaterGroupID_Type(Integer32):
    """Custom type srepeaterGroupID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_SrepeaterGroupID_Type.__name__ = "Integer32"
_SrepeaterGroupID_Object = MibTableColumn
srepeaterGroupID = _SrepeaterGroupID_Object(
    (1, 3, 6, 1, 4, 1, 97, 3, 16, 1, 1, 1),
    _SrepeaterGroupID_Type()
)
srepeaterGroupID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    srepeaterGroupID.setStatus("mandatory")
_SrepeaterLinkStatusMask_Type = Integer32
_SrepeaterLinkStatusMask_Object = MibTableColumn
srepeaterLinkStatusMask = _SrepeaterLinkStatusMask_Object(
    (1, 3, 6, 1, 4, 1, 97, 3, 16, 1, 1, 2),
    _SrepeaterLinkStatusMask_Type()
)
srepeaterLinkStatusMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    srepeaterLinkStatusMask.setStatus("mandatory")


class _SrepeaterExtendedStats_Type(Integer32):
    """Custom type srepeaterExtendedStats based on Integer32"""
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


_SrepeaterExtendedStats_Type.__name__ = "Integer32"
_SrepeaterExtendedStats_Object = MibTableColumn
srepeaterExtendedStats = _SrepeaterExtendedStats_Object(
    (1, 3, 6, 1, 4, 1, 97, 3, 16, 1, 1, 3),
    _SrepeaterExtendedStats_Type()
)
srepeaterExtendedStats.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    srepeaterExtendedStats.setStatus("mandatory")
_SrepeaterPortTable_Object = MibTable
srepeaterPortTable = _SrepeaterPortTable_Object(
    (1, 3, 6, 1, 4, 1, 97, 3, 16, 2)
)
if mibBuilder.loadTexts:
    srepeaterPortTable.setStatus("mandatory")
_SrepeaterPortEntry_Object = MibTableRow
srepeaterPortEntry = _SrepeaterPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 97, 3, 16, 2, 1)
)
srepeaterPortEntry.setIndexNames(
    (0, "CTATX-MIB", "srepeaterPortGroupID"),
    (0, "CTATX-MIB", "srepeaterPortPortID"),
)
if mibBuilder.loadTexts:
    srepeaterPortEntry.setStatus("mandatory")


class _SrepeaterPortGroupID_Type(Integer32):
    """Custom type srepeaterPortGroupID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_SrepeaterPortGroupID_Type.__name__ = "Integer32"
_SrepeaterPortGroupID_Object = MibTableColumn
srepeaterPortGroupID = _SrepeaterPortGroupID_Object(
    (1, 3, 6, 1, 4, 1, 97, 3, 16, 2, 1, 1),
    _SrepeaterPortGroupID_Type()
)
srepeaterPortGroupID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    srepeaterPortGroupID.setStatus("mandatory")
_SrepeaterPortPortID_Type = Integer32
_SrepeaterPortPortID_Object = MibTableColumn
srepeaterPortPortID = _SrepeaterPortPortID_Object(
    (1, 3, 6, 1, 4, 1, 97, 3, 16, 2, 1, 2),
    _SrepeaterPortPortID_Type()
)
srepeaterPortPortID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    srepeaterPortPortID.setStatus("mandatory")


class _SrepeaterPortLinkPulse_Type(Integer32):
    """Custom type srepeaterPortLinkPulse based on Integer32"""
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


_SrepeaterPortLinkPulse_Type.__name__ = "Integer32"
_SrepeaterPortLinkPulse_Object = MibTableColumn
srepeaterPortLinkPulse = _SrepeaterPortLinkPulse_Object(
    (1, 3, 6, 1, 4, 1, 97, 3, 16, 2, 1, 3),
    _SrepeaterPortLinkPulse_Type()
)
srepeaterPortLinkPulse.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    srepeaterPortLinkPulse.setStatus("mandatory")
_Sproto_ObjectIdentity = ObjectIdentity
sproto = _Sproto_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 97, 3, 17)
)
_SprotoTable_Object = MibTable
sprotoTable = _SprotoTable_Object(
    (1, 3, 6, 1, 4, 1, 97, 3, 17, 1)
)
if mibBuilder.loadTexts:
    sprotoTable.setStatus("mandatory")
_SprotoEntry_Object = MibTableRow
sprotoEntry = _SprotoEntry_Object(
    (1, 3, 6, 1, 4, 1, 97, 3, 17, 1, 1)
)
sprotoEntry.setIndexNames(
    (0, "CTATX-MIB", "sprotoIfIndex"),
)
if mibBuilder.loadTexts:
    sprotoEntry.setStatus("mandatory")
_SprotoIfIndex_Type = Integer32
_SprotoIfIndex_Object = MibTableColumn
sprotoIfIndex = _SprotoIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 97, 3, 17, 1, 1, 1),
    _SprotoIfIndex_Type()
)
sprotoIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sprotoIfIndex.setStatus("mandatory")


class _SprotoBridge_Type(Integer32):
    """Custom type sprotoBridge based on Integer32"""
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
        *(("none", 4),
          ("sr", 2),
          ("srt", 3),
          ("transparent", 1))
    )


_SprotoBridge_Type.__name__ = "Integer32"
_SprotoBridge_Object = MibTableColumn
sprotoBridge = _SprotoBridge_Object(
    (1, 3, 6, 1, 4, 1, 97, 3, 17, 1, 1, 2),
    _SprotoBridge_Type()
)
sprotoBridge.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sprotoBridge.setStatus("mandatory")


class _SprotoSuppressBpdus_Type(Integer32):
    """Custom type sprotoSuppressBpdus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("normal", 1),
          ("suppressed", 2))
    )


_SprotoSuppressBpdus_Type.__name__ = "Integer32"
_SprotoSuppressBpdus_Object = MibTableColumn
sprotoSuppressBpdus = _SprotoSuppressBpdus_Object(
    (1, 3, 6, 1, 4, 1, 97, 3, 17, 1, 1, 3),
    _SprotoSuppressBpdus_Type()
)
sprotoSuppressBpdus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sprotoSuppressBpdus.setStatus("mandatory")


class _SprotoIpRoute_Type(Integer32):
    """Custom type sprotoIpRoute based on Integer32"""
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


_SprotoIpRoute_Type.__name__ = "Integer32"
_SprotoIpRoute_Object = MibTableColumn
sprotoIpRoute = _SprotoIpRoute_Object(
    (1, 3, 6, 1, 4, 1, 97, 3, 17, 1, 1, 4),
    _SprotoIpRoute_Type()
)
sprotoIpRoute.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sprotoIpRoute.setStatus("mandatory")


class _SprotoIpxRoute_Type(Integer32):
    """Custom type sprotoIpxRoute based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1),
          ("ipxsr", 3))
    )


_SprotoIpxRoute_Type.__name__ = "Integer32"
_SprotoIpxRoute_Object = MibTableColumn
sprotoIpxRoute = _SprotoIpxRoute_Object(
    (1, 3, 6, 1, 4, 1, 97, 3, 17, 1, 1, 5),
    _SprotoIpxRoute_Type()
)
sprotoIpxRoute.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sprotoIpxRoute.setStatus("mandatory")


class _SprotoAppleRoute_Type(Integer32):
    """Custom type sprotoAppleRoute based on Integer32"""
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


_SprotoAppleRoute_Type.__name__ = "Integer32"
_SprotoAppleRoute_Object = MibTableColumn
sprotoAppleRoute = _SprotoAppleRoute_Object(
    (1, 3, 6, 1, 4, 1, 97, 3, 17, 1, 1, 6),
    _SprotoAppleRoute_Type()
)
sprotoAppleRoute.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sprotoAppleRoute.setStatus("mandatory")


class _SprotoArpTranslate_Type(Integer32):
    """Custom type sprotoArpTranslate based on Integer32"""
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
        *(("bitswap1", 2),
          ("bitswap6", 3),
          ("bitswap61", 4),
          ("none", 1),
          ("oneto6", 5),
          ("oneto6swap", 6))
    )


_SprotoArpTranslate_Type.__name__ = "Integer32"
_SprotoArpTranslate_Object = MibTableColumn
sprotoArpTranslate = _SprotoArpTranslate_Object(
    (1, 3, 6, 1, 4, 1, 97, 3, 17, 1, 1, 7),
    _SprotoArpTranslate_Type()
)
sprotoArpTranslate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sprotoArpTranslate.setStatus("mandatory")


class _SprotoArpSourceRoute_Type(Integer32):
    """Custom type sprotoArpSourceRoute based on Integer32"""
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
        *(("none", 4),
          ("passBoth", 3),
          ("passRif", 1),
          ("stripRif", 2))
    )


_SprotoArpSourceRoute_Type.__name__ = "Integer32"
_SprotoArpSourceRoute_Object = MibTableColumn
sprotoArpSourceRoute = _SprotoArpSourceRoute_Object(
    (1, 3, 6, 1, 4, 1, 97, 3, 17, 1, 1, 8),
    _SprotoArpSourceRoute_Type()
)
sprotoArpSourceRoute.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sprotoArpSourceRoute.setStatus("mandatory")


class _SprotoIpxTranslate_Type(Integer32):
    """Custom type sprotoIpxTranslate based on Integer32"""
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


_SprotoIpxTranslate_Type.__name__ = "Integer32"
_SprotoIpxTranslate_Object = MibTableColumn
sprotoIpxTranslate = _SprotoIpxTranslate_Object(
    (1, 3, 6, 1, 4, 1, 97, 3, 17, 1, 1, 9),
    _SprotoIpxTranslate_Type()
)
sprotoIpxTranslate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sprotoIpxTranslate.setStatus("mandatory")


class _SprotoAppleTranslate_Type(Integer32):
    """Custom type sprotoAppleTranslate based on Integer32"""
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


_SprotoAppleTranslate_Type.__name__ = "Integer32"
_SprotoAppleTranslate_Object = MibTableColumn
sprotoAppleTranslate = _SprotoAppleTranslate_Object(
    (1, 3, 6, 1, 4, 1, 97, 3, 17, 1, 1, 10),
    _SprotoAppleTranslate_Type()
)
sprotoAppleTranslate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sprotoAppleTranslate.setStatus("mandatory")


class _SprotoIbmLlcTranslate_Type(Integer32):
    """Custom type sprotoIbmLlcTranslate based on Integer32"""
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


_SprotoIbmLlcTranslate_Type.__name__ = "Integer32"
_SprotoIbmLlcTranslate_Object = MibTableColumn
sprotoIbmLlcTranslate = _SprotoIbmLlcTranslate_Object(
    (1, 3, 6, 1, 4, 1, 97, 3, 17, 1, 1, 11),
    _SprotoIbmLlcTranslate_Type()
)
sprotoIbmLlcTranslate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sprotoIbmLlcTranslate.setStatus("mandatory")


class _SprotoRip_Type(Integer32):
    """Custom type sprotoRip based on Integer32"""
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


_SprotoRip_Type.__name__ = "Integer32"
_SprotoRip_Object = MibTableColumn
sprotoRip = _SprotoRip_Object(
    (1, 3, 6, 1, 4, 1, 97, 3, 17, 1, 1, 12),
    _SprotoRip_Type()
)
sprotoRip.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sprotoRip.setStatus("mandatory")


class _SprotoEgp_Type(Integer32):
    """Custom type sprotoEgp based on Integer32"""
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


_SprotoEgp_Type.__name__ = "Integer32"
_SprotoEgp_Object = MibTableColumn
sprotoEgp = _SprotoEgp_Object(
    (1, 3, 6, 1, 4, 1, 97, 3, 17, 1, 1, 13),
    _SprotoEgp_Type()
)
sprotoEgp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sprotoEgp.setStatus("mandatory")


class _SprotoOspf_Type(Integer32):
    """Custom type sprotoOspf based on Integer32"""
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


_SprotoOspf_Type.__name__ = "Integer32"
_SprotoOspf_Object = MibTableColumn
sprotoOspf = _SprotoOspf_Object(
    (1, 3, 6, 1, 4, 1, 97, 3, 17, 1, 1, 14),
    _SprotoOspf_Type()
)
sprotoOspf.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sprotoOspf.setStatus("mandatory")


class _SprotoArpProxy_Type(Integer32):
    """Custom type sprotoArpProxy based on Integer32"""
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


_SprotoArpProxy_Type.__name__ = "Integer32"
_SprotoArpProxy_Object = MibTableColumn
sprotoArpProxy = _SprotoArpProxy_Object(
    (1, 3, 6, 1, 4, 1, 97, 3, 17, 1, 1, 15),
    _SprotoArpProxy_Type()
)
sprotoArpProxy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sprotoArpProxy.setStatus("mandatory")
_SprotoIbm8209Lsaps_Type = OctetString
_SprotoIbm8209Lsaps_Object = MibTableColumn
sprotoIbm8209Lsaps = _SprotoIbm8209Lsaps_Object(
    (1, 3, 6, 1, 4, 1, 97, 3, 17, 1, 1, 16),
    _SprotoIbm8209Lsaps_Type()
)
sprotoIbm8209Lsaps.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sprotoIbm8209Lsaps.setStatus("mandatory")


class _SprotoBootpRelay_Type(Integer32):
    """Custom type sprotoBootpRelay based on Integer32"""
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


_SprotoBootpRelay_Type.__name__ = "Integer32"
_SprotoBootpRelay_Object = MibTableColumn
sprotoBootpRelay = _SprotoBootpRelay_Object(
    (1, 3, 6, 1, 4, 1, 97, 3, 17, 1, 1, 17),
    _SprotoBootpRelay_Type()
)
sprotoBootpRelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sprotoBootpRelay.setStatus("mandatory")


class _SprotoNetbiosTranslate_Type(Integer32):
    """Custom type sprotoNetbiosTranslate based on Integer32"""
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
        *(("none", 4),
          ("passBoth", 3),
          ("passRif", 1),
          ("stripRif", 2))
    )


_SprotoNetbiosTranslate_Type.__name__ = "Integer32"
_SprotoNetbiosTranslate_Object = MibTableColumn
sprotoNetbiosTranslate = _SprotoNetbiosTranslate_Object(
    (1, 3, 6, 1, 4, 1, 97, 3, 17, 1, 1, 18),
    _SprotoNetbiosTranslate_Type()
)
sprotoNetbiosTranslate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sprotoNetbiosTranslate.setStatus("mandatory")


class _SprotoIpMulticast_Type(Integer32):
    """Custom type sprotoIpMulticast based on Integer32"""
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


_SprotoIpMulticast_Type.__name__ = "Integer32"
_SprotoIpMulticast_Object = MibTableColumn
sprotoIpMulticast = _SprotoIpMulticast_Object(
    (1, 3, 6, 1, 4, 1, 97, 3, 17, 1, 1, 19),
    _SprotoIpMulticast_Type()
)
sprotoIpMulticast.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sprotoIpMulticast.setStatus("mandatory")


class _SprotoTrunking_Type(Integer32):
    """Custom type sprotoTrunking based on Integer32"""
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


_SprotoTrunking_Type.__name__ = "Integer32"
_SprotoTrunking_Object = MibTableColumn
sprotoTrunking = _SprotoTrunking_Object(
    (1, 3, 6, 1, 4, 1, 97, 3, 17, 1, 1, 20),
    _SprotoTrunking_Type()
)
sprotoTrunking.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sprotoTrunking.setStatus("mandatory")


class _SprotoIpxSrTranslate_Type(Integer32):
    """Custom type sprotoIpxSrTranslate based on Integer32"""
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
        *(("none", 4),
          ("passBoth", 3),
          ("passRif", 1),
          ("stripRif", 2))
    )


_SprotoIpxSrTranslate_Type.__name__ = "Integer32"
_SprotoIpxSrTranslate_Object = MibTableColumn
sprotoIpxSrTranslate = _SprotoIpxSrTranslate_Object(
    (1, 3, 6, 1, 4, 1, 97, 3, 17, 1, 1, 22),
    _SprotoIpxSrTranslate_Type()
)
sprotoIpxSrTranslate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sprotoIpxSrTranslate.setStatus("mandatory")


class _SprotoAllTranslate_Type(Integer32):
    """Custom type sprotoAllTranslate based on Integer32"""
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
        *(("none", 4),
          ("passBoth", 3),
          ("passRif", 1),
          ("stripRif", 2))
    )


_SprotoAllTranslate_Type.__name__ = "Integer32"
_SprotoAllTranslate_Object = MibTableColumn
sprotoAllTranslate = _SprotoAllTranslate_Object(
    (1, 3, 6, 1, 4, 1, 97, 3, 17, 1, 1, 23),
    _SprotoAllTranslate_Type()
)
sprotoAllTranslate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sprotoAllTranslate.setStatus("mandatory")


class _SprotoSteHopCountAppliedRule_Type(Integer32):
    """Custom type sprotoSteHopCountAppliedRule based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("hopcountapplied", 2),
          ("hopcountnotapplied", 1))
    )


_SprotoSteHopCountAppliedRule_Type.__name__ = "Integer32"
_SprotoSteHopCountAppliedRule_Object = MibTableColumn
sprotoSteHopCountAppliedRule = _SprotoSteHopCountAppliedRule_Object(
    (1, 3, 6, 1, 4, 1, 97, 3, 17, 1, 1, 24),
    _SprotoSteHopCountAppliedRule_Type()
)
sprotoSteHopCountAppliedRule.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sprotoSteHopCountAppliedRule.setStatus("mandatory")


class _SprotoIpxDot3Framing_Type(Integer32):
    """Custom type sprotoIpxDot3Framing based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("ethernet2", 2),
          ("ethernet8022", 3),
          ("ethernet8023", 1))
    )


_SprotoIpxDot3Framing_Type.__name__ = "Integer32"
_SprotoIpxDot3Framing_Object = MibScalar
sprotoIpxDot3Framing = _SprotoIpxDot3Framing_Object(
    (1, 3, 6, 1, 4, 1, 97, 3, 17, 2),
    _SprotoIpxDot3Framing_Type()
)
sprotoIpxDot3Framing.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sprotoIpxDot3Framing.setStatus("mandatory")
_Sipx_ObjectIdentity = ObjectIdentity
sipx = _Sipx_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 97, 3, 18)
)
_SipxIfTable_Object = MibTable
sipxIfTable = _SipxIfTable_Object(
    (1, 3, 6, 1, 4, 1, 97, 3, 18, 1)
)
if mibBuilder.loadTexts:
    sipxIfTable.setStatus("mandatory")
_SipxIfEntry_Object = MibTableRow
sipxIfEntry = _SipxIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 97, 3, 18, 1, 1)
)
sipxIfEntry.setIndexNames(
    (0, "CTATX-MIB", "sipxIfIndex"),
)
if mibBuilder.loadTexts:
    sipxIfEntry.setStatus("mandatory")
_SipxIfIndex_Type = Integer32
_SipxIfIndex_Object = MibTableColumn
sipxIfIndex = _SipxIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 97, 3, 18, 1, 1, 1),
    _SipxIfIndex_Type()
)
sipxIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sipxIfIndex.setStatus("mandatory")
_SipxIfNetwork_Type = OctetString
_SipxIfNetwork_Object = MibTableColumn
sipxIfNetwork = _SipxIfNetwork_Object(
    (1, 3, 6, 1, 4, 1, 97, 3, 18, 1, 1, 2),
    _SipxIfNetwork_Type()
)
sipxIfNetwork.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sipxIfNetwork.setStatus("mandatory")


class _SipxIfFraming_Type(Integer32):
    """Custom type sipxIfFraming based on Integer32"""
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
        *(("ethernet2", 2),
          ("ethernet8023", 1),
          ("ieee8022", 3),
          ("ppp", 6),
          ("rawfddi", 5),
          ("snap", 4))
    )


_SipxIfFraming_Type.__name__ = "Integer32"
_SipxIfFraming_Object = MibTableColumn
sipxIfFraming = _SipxIfFraming_Object(
    (1, 3, 6, 1, 4, 1, 97, 3, 18, 1, 1, 3),
    _SipxIfFraming_Type()
)
sipxIfFraming.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sipxIfFraming.setStatus("mandatory")
_SipxIfInRipPkts_Type = Counter32
_SipxIfInRipPkts_Object = MibTableColumn
sipxIfInRipPkts = _SipxIfInRipPkts_Object(
    (1, 3, 6, 1, 4, 1, 97, 3, 18, 1, 1, 4),
    _SipxIfInRipPkts_Type()
)
sipxIfInRipPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sipxIfInRipPkts.setStatus("mandatory")
_SipxIfOutRipPkts_Type = Counter32
_SipxIfOutRipPkts_Object = MibTableColumn
sipxIfOutRipPkts = _SipxIfOutRipPkts_Object(
    (1, 3, 6, 1, 4, 1, 97, 3, 18, 1, 1, 5),
    _SipxIfOutRipPkts_Type()
)
sipxIfOutRipPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sipxIfOutRipPkts.setStatus("mandatory")
_SipxIfInSapPkts_Type = Counter32
_SipxIfInSapPkts_Object = MibTableColumn
sipxIfInSapPkts = _SipxIfInSapPkts_Object(
    (1, 3, 6, 1, 4, 1, 97, 3, 18, 1, 1, 6),
    _SipxIfInSapPkts_Type()
)
sipxIfInSapPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sipxIfInSapPkts.setStatus("mandatory")
_SipxIfOutSapPkts_Type = Counter32
_SipxIfOutSapPkts_Object = MibTableColumn
sipxIfOutSapPkts = _SipxIfOutSapPkts_Object(
    (1, 3, 6, 1, 4, 1, 97, 3, 18, 1, 1, 7),
    _SipxIfOutSapPkts_Type()
)
sipxIfOutSapPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sipxIfOutSapPkts.setStatus("mandatory")
_SipxRouteTable_Object = MibTable
sipxRouteTable = _SipxRouteTable_Object(
    (1, 3, 6, 1, 4, 1, 97, 3, 18, 2)
)
if mibBuilder.loadTexts:
    sipxRouteTable.setStatus("mandatory")
_SipxRouteEntry_Object = MibTableRow
sipxRouteEntry = _SipxRouteEntry_Object(
    (1, 3, 6, 1, 4, 1, 97, 3, 18, 2, 1)
)
sipxRouteEntry.setIndexNames(
    (0, "CTATX-MIB", "sipxRouteDest"),
)
if mibBuilder.loadTexts:
    sipxRouteEntry.setStatus("mandatory")
_SipxRouteDest_Type = OctetString
_SipxRouteDest_Object = MibTableColumn
sipxRouteDest = _SipxRouteDest_Object(
    (1, 3, 6, 1, 4, 1, 97, 3, 18, 2, 1, 1),
    _SipxRouteDest_Type()
)
sipxRouteDest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sipxRouteDest.setStatus("mandatory")
_SipxRouteIfIndex_Type = Integer32
_SipxRouteIfIndex_Object = MibTableColumn
sipxRouteIfIndex = _SipxRouteIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 97, 3, 18, 2, 1, 2),
    _SipxRouteIfIndex_Type()
)
sipxRouteIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sipxRouteIfIndex.setStatus("mandatory")
_SipxRouteTickCount_Type = Integer32
_SipxRouteTickCount_Object = MibTableColumn
sipxRouteTickCount = _SipxRouteTickCount_Object(
    (1, 3, 6, 1, 4, 1, 97, 3, 18, 2, 1, 3),
    _SipxRouteTickCount_Type()
)
sipxRouteTickCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sipxRouteTickCount.setStatus("mandatory")
_SipxRouteHopCount_Type = Integer32
_SipxRouteHopCount_Object = MibTableColumn
sipxRouteHopCount = _SipxRouteHopCount_Object(
    (1, 3, 6, 1, 4, 1, 97, 3, 18, 2, 1, 4),
    _SipxRouteHopCount_Type()
)
sipxRouteHopCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sipxRouteHopCount.setStatus("mandatory")
_SipxRouteNextHop_Type = OctetString
_SipxRouteNextHop_Object = MibTableColumn
sipxRouteNextHop = _SipxRouteNextHop_Object(
    (1, 3, 6, 1, 4, 1, 97, 3, 18, 2, 1, 5),
    _SipxRouteNextHop_Type()
)
sipxRouteNextHop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sipxRouteNextHop.setStatus("mandatory")
_SipxRouteAge_Type = Integer32
_SipxRouteAge_Object = MibTableColumn
sipxRouteAge = _SipxRouteAge_Object(
    (1, 3, 6, 1, 4, 1, 97, 3, 18, 2, 1, 6),
    _SipxRouteAge_Type()
)
sipxRouteAge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sipxRouteAge.setStatus("mandatory")
_SipxSapTable_Object = MibTable
sipxSapTable = _SipxSapTable_Object(
    (1, 3, 6, 1, 4, 1, 97, 3, 18, 3)
)
if mibBuilder.loadTexts:
    sipxSapTable.setStatus("mandatory")
_SipxSapEntry_Object = MibTableRow
sipxSapEntry = _SipxSapEntry_Object(
    (1, 3, 6, 1, 4, 1, 97, 3, 18, 3, 1)
)
sipxSapEntry.setIndexNames(
    (0, "CTATX-MIB", "sipxSapIndex"),
)
if mibBuilder.loadTexts:
    sipxSapEntry.setStatus("mandatory")
_SipxSapIndex_Type = Integer32
_SipxSapIndex_Object = MibTableColumn
sipxSapIndex = _SipxSapIndex_Object(
    (1, 3, 6, 1, 4, 1, 97, 3, 18, 3, 1, 1),
    _SipxSapIndex_Type()
)
sipxSapIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sipxSapIndex.setStatus("mandatory")
_SipxSapType_Type = Integer32
_SipxSapType_Object = MibTableColumn
sipxSapType = _SipxSapType_Object(
    (1, 3, 6, 1, 4, 1, 97, 3, 18, 3, 1, 2),
    _SipxSapType_Type()
)
sipxSapType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sipxSapType.setStatus("mandatory")
_SipxSapName_Type = OctetString
_SipxSapName_Object = MibTableColumn
sipxSapName = _SipxSapName_Object(
    (1, 3, 6, 1, 4, 1, 97, 3, 18, 3, 1, 3),
    _SipxSapName_Type()
)
sipxSapName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sipxSapName.setStatus("mandatory")
_SipxSapNetwork_Type = OctetString
_SipxSapNetwork_Object = MibTableColumn
sipxSapNetwork = _SipxSapNetwork_Object(
    (1, 3, 6, 1, 4, 1, 97, 3, 18, 3, 1, 4),
    _SipxSapNetwork_Type()
)
sipxSapNetwork.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sipxSapNetwork.setStatus("mandatory")
_SipxSapNodeId_Type = OctetString
_SipxSapNodeId_Object = MibTableColumn
sipxSapNodeId = _SipxSapNodeId_Object(
    (1, 3, 6, 1, 4, 1, 97, 3, 18, 3, 1, 5),
    _SipxSapNodeId_Type()
)
sipxSapNodeId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sipxSapNodeId.setStatus("mandatory")
_SipxSapSocket_Type = Integer32
_SipxSapSocket_Object = MibTableColumn
sipxSapSocket = _SipxSapSocket_Object(
    (1, 3, 6, 1, 4, 1, 97, 3, 18, 3, 1, 6),
    _SipxSapSocket_Type()
)
sipxSapSocket.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sipxSapSocket.setStatus("mandatory")
_SipxSapHopCount_Type = Integer32
_SipxSapHopCount_Object = MibTableColumn
sipxSapHopCount = _SipxSapHopCount_Object(
    (1, 3, 6, 1, 4, 1, 97, 3, 18, 3, 1, 7),
    _SipxSapHopCount_Type()
)
sipxSapHopCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sipxSapHopCount.setStatus("mandatory")
_SipxDiscardedRoutes_Type = Counter32
_SipxDiscardedRoutes_Object = MibScalar
sipxDiscardedRoutes = _SipxDiscardedRoutes_Object(
    (1, 3, 6, 1, 4, 1, 97, 3, 18, 4),
    _SipxDiscardedRoutes_Type()
)
sipxDiscardedRoutes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sipxDiscardedRoutes.setStatus("mandatory")
_SipxDiscardedServices_Type = Counter32
_SipxDiscardedServices_Object = MibScalar
sipxDiscardedServices = _SipxDiscardedServices_Object(
    (1, 3, 6, 1, 4, 1, 97, 3, 18, 5),
    _SipxDiscardedServices_Type()
)
sipxDiscardedServices.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sipxDiscardedServices.setStatus("mandatory")
_SipxsfGrp_ObjectIdentity = ObjectIdentity
sipxsfGrp = _SipxsfGrp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 97, 3, 18, 6)
)
_SipxsfNextIndex_Type = Integer32
_SipxsfNextIndex_Object = MibScalar
sipxsfNextIndex = _SipxsfNextIndex_Object(
    (1, 3, 6, 1, 4, 1, 97, 3, 18, 6, 1),
    _SipxsfNextIndex_Type()
)
sipxsfNextIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sipxsfNextIndex.setStatus("mandatory")
_SipxsfTable_Object = MibTable
sipxsfTable = _SipxsfTable_Object(
    (1, 3, 6, 1, 4, 1, 97, 3, 18, 6, 2)
)
if mibBuilder.loadTexts:
    sipxsfTable.setStatus("mandatory")
_SipxsfEntry_Object = MibTableRow
sipxsfEntry = _SipxsfEntry_Object(
    (1, 3, 6, 1, 4, 1, 97, 3, 18, 6, 2, 1)
)
sipxsfEntry.setIndexNames(
    (0, "CTATX-MIB", "sipxsfIndex"),
)
if mibBuilder.loadTexts:
    sipxsfEntry.setStatus("mandatory")
_SipxsfIndex_Type = Integer32
_SipxsfIndex_Object = MibTableColumn
sipxsfIndex = _SipxsfIndex_Object(
    (1, 3, 6, 1, 4, 1, 97, 3, 18, 6, 2, 1, 1),
    _SipxsfIndex_Type()
)
sipxsfIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sipxsfIndex.setStatus("mandatory")
_SipxsfSAPName_Type = OctetString
_SipxsfSAPName_Object = MibTableColumn
sipxsfSAPName = _SipxsfSAPName_Object(
    (1, 3, 6, 1, 4, 1, 97, 3, 18, 6, 2, 1, 2),
    _SipxsfSAPName_Type()
)
sipxsfSAPName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sipxsfSAPName.setStatus("mandatory")
_SipxsfSAPType_Type = Integer32
_SipxsfSAPType_Object = MibTableColumn
sipxsfSAPType = _SipxsfSAPType_Object(
    (1, 3, 6, 1, 4, 1, 97, 3, 18, 6, 2, 1, 3),
    _SipxsfSAPType_Type()
)
sipxsfSAPType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sipxsfSAPType.setStatus("mandatory")


class _SipxsfAccessMode_Type(Integer32):
    """Custom type sipxsfAccessMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("denied", 2),
          ("invalid", 3),
          ("permitted", 1))
    )


_SipxsfAccessMode_Type.__name__ = "Integer32"
_SipxsfAccessMode_Object = MibTableColumn
sipxsfAccessMode = _SipxsfAccessMode_Object(
    (1, 3, 6, 1, 4, 1, 97, 3, 18, 6, 2, 1, 4),
    _SipxsfAccessMode_Type()
)
sipxsfAccessMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sipxsfAccessMode.setStatus("mandatory")


class _SipxsfFilterType_Type(Integer32):
    """Custom type sipxsfFilterType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("entry", 1),
          ("exit", 2))
    )


_SipxsfFilterType_Type.__name__ = "Integer32"
_SipxsfFilterType_Object = MibTableColumn
sipxsfFilterType = _SipxsfFilterType_Object(
    (1, 3, 6, 1, 4, 1, 97, 3, 18, 6, 2, 1, 5),
    _SipxsfFilterType_Type()
)
sipxsfFilterType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sipxsfFilterType.setStatus("mandatory")
_SipxsfPortMap_Type = OctetString
_SipxsfPortMap_Object = MibTableColumn
sipxsfPortMap = _SipxsfPortMap_Object(
    (1, 3, 6, 1, 4, 1, 97, 3, 18, 6, 2, 1, 6),
    _SipxsfPortMap_Type()
)
sipxsfPortMap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sipxsfPortMap.setStatus("mandatory")
_SipxsfNetworks_Type = OctetString
_SipxsfNetworks_Object = MibTableColumn
sipxsfNetworks = _SipxsfNetworks_Object(
    (1, 3, 6, 1, 4, 1, 97, 3, 18, 6, 2, 1, 7),
    _SipxsfNetworks_Type()
)
sipxsfNetworks.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sipxsfNetworks.setStatus("mandatory")
_SipxsfFiltered_Type = Counter32
_SipxsfFiltered_Object = MibTableColumn
sipxsfFiltered = _SipxsfFiltered_Object(
    (1, 3, 6, 1, 4, 1, 97, 3, 18, 6, 2, 1, 8),
    _SipxsfFiltered_Type()
)
sipxsfFiltered.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sipxsfFiltered.setStatus("mandatory")
_SipxsrGrp_ObjectIdentity = ObjectIdentity
sipxsrGrp = _SipxsrGrp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 97, 3, 18, 7)
)
_SipxsrAgingTime_Type = Integer32
_SipxsrAgingTime_Object = MibScalar
sipxsrAgingTime = _SipxsrAgingTime_Object(
    (1, 3, 6, 1, 4, 1, 97, 3, 18, 7, 1),
    _SipxsrAgingTime_Type()
)
sipxsrAgingTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sipxsrAgingTime.setStatus("mandatory")
_SipxsrExplorerTable_Object = MibTable
sipxsrExplorerTable = _SipxsrExplorerTable_Object(
    (1, 3, 6, 1, 4, 1, 97, 3, 18, 7, 2)
)
if mibBuilder.loadTexts:
    sipxsrExplorerTable.setStatus("mandatory")
_SipxsrExplorerEntry_Object = MibTableRow
sipxsrExplorerEntry = _SipxsrExplorerEntry_Object(
    (1, 3, 6, 1, 4, 1, 97, 3, 18, 7, 2, 1)
)
sipxsrExplorerEntry.setIndexNames(
    (0, "CTATX-MIB", "sipxsrPort"),
)
if mibBuilder.loadTexts:
    sipxsrExplorerEntry.setStatus("mandatory")
_SipxsrPort_Type = Integer32
_SipxsrPort_Object = MibTableColumn
sipxsrPort = _SipxsrPort_Object(
    (1, 3, 6, 1, 4, 1, 97, 3, 18, 7, 2, 1, 1),
    _SipxsrPort_Type()
)
sipxsrPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sipxsrPort.setStatus("mandatory")


class _SipxsrStatus_Type(Integer32):
    """Custom type sipxsrStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 2),
          ("valid", 1))
    )


_SipxsrStatus_Type.__name__ = "Integer32"
_SipxsrStatus_Object = MibTableColumn
sipxsrStatus = _SipxsrStatus_Object(
    (1, 3, 6, 1, 4, 1, 97, 3, 18, 7, 2, 1, 2),
    _SipxsrStatus_Type()
)
sipxsrStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sipxsrStatus.setStatus("mandatory")


class _SipxsrExplorerType_Type(Integer32):
    """Custom type sipxsrExplorerType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("are", 1),
          ("ste", 2))
    )


_SipxsrExplorerType_Type.__name__ = "Integer32"
_SipxsrExplorerType_Object = MibTableColumn
sipxsrExplorerType = _SipxsrExplorerType_Object(
    (1, 3, 6, 1, 4, 1, 97, 3, 18, 7, 2, 1, 3),
    _SipxsrExplorerType_Type()
)
sipxsrExplorerType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sipxsrExplorerType.setStatus("mandatory")
_Srtrdisc_ObjectIdentity = ObjectIdentity
srtrdisc = _Srtrdisc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 97, 3, 19)
)
_SrtrdiscTable_Object = MibTable
srtrdiscTable = _SrtrdiscTable_Object(
    (1, 3, 6, 1, 4, 1, 97, 3, 19, 1)
)
if mibBuilder.loadTexts:
    srtrdiscTable.setStatus("mandatory")
_SrtrdiscEntry_Object = MibTableRow
srtrdiscEntry = _SrtrdiscEntry_Object(
    (1, 3, 6, 1, 4, 1, 97, 3, 19, 1, 1)
)
srtrdiscEntry.setIndexNames(
    (0, "CTATX-MIB", "srtrdiscIfIndex"),
)
if mibBuilder.loadTexts:
    srtrdiscEntry.setStatus("mandatory")
_SrtrdiscIfIndex_Type = Integer32
_SrtrdiscIfIndex_Object = MibTableColumn
srtrdiscIfIndex = _SrtrdiscIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 97, 3, 19, 1, 1, 1),
    _SrtrdiscIfIndex_Type()
)
srtrdiscIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    srtrdiscIfIndex.setStatus("mandatory")


class _SrtrdiscState_Type(Integer32):
    """Custom type srtrdiscState based on Integer32"""
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


_SrtrdiscState_Type.__name__ = "Integer32"
_SrtrdiscState_Object = MibTableColumn
srtrdiscState = _SrtrdiscState_Object(
    (1, 3, 6, 1, 4, 1, 97, 3, 19, 1, 1, 2),
    _SrtrdiscState_Type()
)
srtrdiscState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    srtrdiscState.setStatus("mandatory")


class _SrtrdiscAdvertisementAddress_Type(Integer32):
    """Custom type srtrdiscAdvertisementAddress based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("broadcast", 2),
          ("multicast", 1))
    )


_SrtrdiscAdvertisementAddress_Type.__name__ = "Integer32"
_SrtrdiscAdvertisementAddress_Object = MibTableColumn
srtrdiscAdvertisementAddress = _SrtrdiscAdvertisementAddress_Object(
    (1, 3, 6, 1, 4, 1, 97, 3, 19, 1, 1, 3),
    _SrtrdiscAdvertisementAddress_Type()
)
srtrdiscAdvertisementAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    srtrdiscAdvertisementAddress.setStatus("mandatory")
_SrtrdiscAdvertisementInterval_Type = Integer32
_SrtrdiscAdvertisementInterval_Object = MibTableColumn
srtrdiscAdvertisementInterval = _SrtrdiscAdvertisementInterval_Object(
    (1, 3, 6, 1, 4, 1, 97, 3, 19, 1, 1, 4),
    _SrtrdiscAdvertisementInterval_Type()
)
srtrdiscAdvertisementInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    srtrdiscAdvertisementInterval.setStatus("mandatory")
_SrtrdiscLifetime_Type = Integer32
_SrtrdiscLifetime_Object = MibTableColumn
srtrdiscLifetime = _SrtrdiscLifetime_Object(
    (1, 3, 6, 1, 4, 1, 97, 3, 19, 1, 1, 5),
    _SrtrdiscLifetime_Type()
)
srtrdiscLifetime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    srtrdiscLifetime.setStatus("mandatory")
_SrtrdiscPreference_Type = Integer32
_SrtrdiscPreference_Object = MibTableColumn
srtrdiscPreference = _SrtrdiscPreference_Object(
    (1, 3, 6, 1, 4, 1, 97, 3, 19, 1, 1, 6),
    _SrtrdiscPreference_Type()
)
srtrdiscPreference.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    srtrdiscPreference.setStatus("mandatory")
_Sipm_ObjectIdentity = ObjectIdentity
sipm = _Sipm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 97, 3, 20)
)
_Sipmroute_ObjectIdentity = ObjectIdentity
sipmroute = _Sipmroute_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 97, 3, 20, 1)
)
_SipmRouteTable_Object = MibTable
sipmRouteTable = _SipmRouteTable_Object(
    (1, 3, 6, 1, 4, 1, 97, 3, 20, 1, 1)
)
if mibBuilder.loadTexts:
    sipmRouteTable.setStatus("mandatory")
_SipmRouteEntry_Object = MibTableRow
sipmRouteEntry = _SipmRouteEntry_Object(
    (1, 3, 6, 1, 4, 1, 97, 3, 20, 1, 1, 1)
)
sipmRouteEntry.setIndexNames(
    (0, "CTATX-MIB", "sipmRouteOrigin"),
    (0, "CTATX-MIB", "sipmRouteOriginMask"),
)
if mibBuilder.loadTexts:
    sipmRouteEntry.setStatus("mandatory")
_SipmRouteOrigin_Type = IpAddress
_SipmRouteOrigin_Object = MibTableColumn
sipmRouteOrigin = _SipmRouteOrigin_Object(
    (1, 3, 6, 1, 4, 1, 97, 3, 20, 1, 1, 1, 1),
    _SipmRouteOrigin_Type()
)
sipmRouteOrigin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sipmRouteOrigin.setStatus("mandatory")
_SipmRouteOriginMask_Type = IpAddress
_SipmRouteOriginMask_Object = MibTableColumn
sipmRouteOriginMask = _SipmRouteOriginMask_Object(
    (1, 3, 6, 1, 4, 1, 97, 3, 20, 1, 1, 1, 2),
    _SipmRouteOriginMask_Type()
)
sipmRouteOriginMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sipmRouteOriginMask.setStatus("mandatory")
_SipmRouteGateway_Type = IpAddress
_SipmRouteGateway_Object = MibTableColumn
sipmRouteGateway = _SipmRouteGateway_Object(
    (1, 3, 6, 1, 4, 1, 97, 3, 20, 1, 1, 1, 3),
    _SipmRouteGateway_Type()
)
sipmRouteGateway.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sipmRouteGateway.setStatus("mandatory")
_SipmRouteMetric_Type = Integer32
_SipmRouteMetric_Object = MibTableColumn
sipmRouteMetric = _SipmRouteMetric_Object(
    (1, 3, 6, 1, 4, 1, 97, 3, 20, 1, 1, 1, 4),
    _SipmRouteMetric_Type()
)
sipmRouteMetric.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sipmRouteMetric.setStatus("mandatory")
_SipmRouteAge_Type = TimeTicks
_SipmRouteAge_Object = MibTableColumn
sipmRouteAge = _SipmRouteAge_Object(
    (1, 3, 6, 1, 4, 1, 97, 3, 20, 1, 1, 1, 5),
    _SipmRouteAge_Type()
)
sipmRouteAge.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sipmRouteAge.setStatus("mandatory")
_SipmRouteParents_Type = OctetString
_SipmRouteParents_Object = MibTableColumn
sipmRouteParents = _SipmRouteParents_Object(
    (1, 3, 6, 1, 4, 1, 97, 3, 20, 1, 1, 1, 6),
    _SipmRouteParents_Type()
)
sipmRouteParents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sipmRouteParents.setStatus("mandatory")
_Sipmgroup_ObjectIdentity = ObjectIdentity
sipmgroup = _Sipmgroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 97, 3, 20, 2)
)
_Sipmneighbor_ObjectIdentity = ObjectIdentity
sipmneighbor = _Sipmneighbor_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 97, 3, 20, 3)
)
_SipmNeighborTable_Object = MibTable
sipmNeighborTable = _SipmNeighborTable_Object(
    (1, 3, 6, 1, 4, 1, 97, 3, 20, 3, 1)
)
if mibBuilder.loadTexts:
    sipmNeighborTable.setStatus("mandatory")
_SipmNeighborEntry_Object = MibTableRow
sipmNeighborEntry = _SipmNeighborEntry_Object(
    (1, 3, 6, 1, 4, 1, 97, 3, 20, 3, 1, 1)
)
sipmNeighborEntry.setIndexNames(
    (0, "CTATX-MIB", "sipmNeighborIfIndex"),
    (0, "CTATX-MIB", "sipmNeighbors"),
)
if mibBuilder.loadTexts:
    sipmNeighborEntry.setStatus("mandatory")
_SipmNeighborIfIndex_Type = Integer32
_SipmNeighborIfIndex_Object = MibTableColumn
sipmNeighborIfIndex = _SipmNeighborIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 97, 3, 20, 3, 1, 1, 1),
    _SipmNeighborIfIndex_Type()
)
sipmNeighborIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sipmNeighborIfIndex.setStatus("mandatory")
_SipmNeighbors_Type = IpAddress
_SipmNeighbors_Object = MibTableColumn
sipmNeighbors = _SipmNeighbors_Object(
    (1, 3, 6, 1, 4, 1, 97, 3, 20, 3, 1, 1, 2),
    _SipmNeighbors_Type()
)
sipmNeighbors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sipmNeighbors.setStatus("mandatory")
_SipmNeighborLastHeard_Type = TimeTicks
_SipmNeighborLastHeard_Object = MibTableColumn
sipmNeighborLastHeard = _SipmNeighborLastHeard_Object(
    (1, 3, 6, 1, 4, 1, 97, 3, 20, 3, 1, 1, 3),
    _SipmNeighborLastHeard_Type()
)
sipmNeighborLastHeard.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sipmNeighborLastHeard.setStatus("mandatory")
_Sipmstat_ObjectIdentity = ObjectIdentity
sipmstat = _Sipmstat_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 97, 3, 20, 4)
)
_SipmOutOfMemory_Type = Counter32
_SipmOutOfMemory_Object = MibScalar
sipmOutOfMemory = _SipmOutOfMemory_Object(
    (1, 3, 6, 1, 4, 1, 97, 3, 20, 4, 1),
    _SipmOutOfMemory_Type()
)
sipmOutOfMemory.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sipmOutOfMemory.setStatus("mandatory")
_SipmStatTable_Object = MibTable
sipmStatTable = _SipmStatTable_Object(
    (1, 3, 6, 1, 4, 1, 97, 3, 20, 4, 2)
)
if mibBuilder.loadTexts:
    sipmStatTable.setStatus("mandatory")
_SipmStatEntry_Object = MibTableRow
sipmStatEntry = _SipmStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 97, 3, 20, 4, 2, 1)
)
sipmStatEntry.setIndexNames(
    (0, "CTATX-MIB", "sipmStatIfIndex"),
)
if mibBuilder.loadTexts:
    sipmStatEntry.setStatus("mandatory")
_SipmStatIfIndex_Type = Integer32
_SipmStatIfIndex_Object = MibTableColumn
sipmStatIfIndex = _SipmStatIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 97, 3, 20, 4, 2, 1, 1),
    _SipmStatIfIndex_Type()
)
sipmStatIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sipmStatIfIndex.setStatus("mandatory")
_SipmInBadPackets_Type = Counter32
_SipmInBadPackets_Object = MibTableColumn
sipmInBadPackets = _SipmInBadPackets_Object(
    (1, 3, 6, 1, 4, 1, 97, 3, 20, 4, 2, 1, 2),
    _SipmInBadPackets_Type()
)
sipmInBadPackets.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sipmInBadPackets.setStatus("mandatory")
_SipmCacheMiss_Type = Counter32
_SipmCacheMiss_Object = MibTableColumn
sipmCacheMiss = _SipmCacheMiss_Object(
    (1, 3, 6, 1, 4, 1, 97, 3, 20, 4, 2, 1, 3),
    _SipmCacheMiss_Type()
)
sipmCacheMiss.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sipmCacheMiss.setStatus("mandatory")
_Sipckt_ObjectIdentity = ObjectIdentity
sipckt = _Sipckt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 97, 3, 21)
)
_SipcktTable_Object = MibTable
sipcktTable = _SipcktTable_Object(
    (1, 3, 6, 1, 4, 1, 97, 3, 21, 1)
)
if mibBuilder.loadTexts:
    sipcktTable.setStatus("mandatory")
_SipcktEntry_Object = MibTableRow
sipcktEntry = _SipcktEntry_Object(
    (1, 3, 6, 1, 4, 1, 97, 3, 21, 1, 1)
)
sipcktEntry.setIndexNames(
    (0, "CTATX-MIB", "sipcktIndex"),
    (0, "CTATX-MIB", "sipcktIpAddress"),
)
if mibBuilder.loadTexts:
    sipcktEntry.setStatus("mandatory")
_SipcktIndex_Type = Integer32
_SipcktIndex_Object = MibTableColumn
sipcktIndex = _SipcktIndex_Object(
    (1, 3, 6, 1, 4, 1, 97, 3, 21, 1, 1, 1),
    _SipcktIndex_Type()
)
sipcktIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sipcktIndex.setStatus("mandatory")
_SipcktIpAddress_Type = IpAddress
_SipcktIpAddress_Object = MibTableColumn
sipcktIpAddress = _SipcktIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 97, 3, 21, 1, 1, 2),
    _SipcktIpAddress_Type()
)
sipcktIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sipcktIpAddress.setStatus("mandatory")


class _SipcktState_Type(Integer32):
    """Custom type sipcktState based on Integer32"""
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
        *(("invalid", 2),
          ("invalid-all", 3),
          ("netmask-conflict", 4),
          ("valid", 1))
    )


_SipcktState_Type.__name__ = "Integer32"
_SipcktState_Object = MibTableColumn
sipcktState = _SipcktState_Object(
    (1, 3, 6, 1, 4, 1, 97, 3, 21, 1, 1, 3),
    _SipcktState_Type()
)
sipcktState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sipcktState.setStatus("mandatory")
_SipcktNetMask_Type = IpAddress
_SipcktNetMask_Object = MibTableColumn
sipcktNetMask = _SipcktNetMask_Object(
    (1, 3, 6, 1, 4, 1, 97, 3, 21, 1, 1, 4),
    _SipcktNetMask_Type()
)
sipcktNetMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sipcktNetMask.setStatus("mandatory")


class _SipcktSourceRoute_Type(Integer32):
    """Custom type sipcktSourceRoute based on Integer32"""
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
        *(("both", 4),
          ("default", 1),
          ("no-sr", 3),
          ("sr", 2))
    )


_SipcktSourceRoute_Type.__name__ = "Integer32"
_SipcktSourceRoute_Object = MibTableColumn
sipcktSourceRoute = _SipcktSourceRoute_Object(
    (1, 3, 6, 1, 4, 1, 97, 3, 21, 1, 1, 5),
    _SipcktSourceRoute_Type()
)
sipcktSourceRoute.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sipcktSourceRoute.setStatus("mandatory")
_SipNetToMediaTable_Object = MibTable
sipNetToMediaTable = _SipNetToMediaTable_Object(
    (1, 3, 6, 1, 4, 1, 97, 3, 22)
)
if mibBuilder.loadTexts:
    sipNetToMediaTable.setStatus("mandatory")
_SipNetToMediaEntry_Object = MibTableRow
sipNetToMediaEntry = _SipNetToMediaEntry_Object(
    (1, 3, 6, 1, 4, 1, 97, 3, 22, 1)
)
sipNetToMediaEntry.setIndexNames(
    (0, "CTATX-MIB", "sipNetToMediaIfIndex"),
    (0, "CTATX-MIB", "sipNetToMediaNetAddress"),
)
if mibBuilder.loadTexts:
    sipNetToMediaEntry.setStatus("mandatory")
_SipNetToMediaIfIndex_Type = Integer32
_SipNetToMediaIfIndex_Object = MibTableColumn
sipNetToMediaIfIndex = _SipNetToMediaIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 97, 3, 22, 1, 1),
    _SipNetToMediaIfIndex_Type()
)
sipNetToMediaIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sipNetToMediaIfIndex.setStatus("mandatory")
_SipNetToMediaNetAddress_Type = IpAddress
_SipNetToMediaNetAddress_Object = MibTableColumn
sipNetToMediaNetAddress = _SipNetToMediaNetAddress_Object(
    (1, 3, 6, 1, 4, 1, 97, 3, 22, 1, 2),
    _SipNetToMediaNetAddress_Type()
)
sipNetToMediaNetAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sipNetToMediaNetAddress.setStatus("mandatory")
_SipNetToMediaSourceRoute_Type = OctetString
_SipNetToMediaSourceRoute_Object = MibTableColumn
sipNetToMediaSourceRoute = _SipNetToMediaSourceRoute_Object(
    (1, 3, 6, 1, 4, 1, 97, 3, 22, 1, 3),
    _SipNetToMediaSourceRoute_Type()
)
sipNetToMediaSourceRoute.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sipNetToMediaSourceRoute.setStatus("mandatory")
_SipNetToMediaAge_Type = Integer32
_SipNetToMediaAge_Object = MibTableColumn
sipNetToMediaAge = _SipNetToMediaAge_Object(
    (1, 3, 6, 1, 4, 1, 97, 3, 22, 1, 4),
    _SipNetToMediaAge_Type()
)
sipNetToMediaAge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sipNetToMediaAge.setStatus("mandatory")
_Ssecure_ObjectIdentity = ObjectIdentity
ssecure = _Ssecure_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 97, 3, 23)
)
_ProfileTable_Object = MibTable
profileTable = _ProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 97, 3, 23, 1)
)
if mibBuilder.loadTexts:
    profileTable.setStatus("mandatory")
_ProfileEntry_Object = MibTableRow
profileEntry = _ProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 97, 3, 23, 1, 1)
)
profileEntry.setIndexNames(
    (0, "CTATX-MIB", "profileIndex"),
    (0, "CTATX-MIB", "profileSourceStart"),
    (0, "CTATX-MIB", "profileSourceEnd"),
    (0, "CTATX-MIB", "profileDestStart"),
    (0, "CTATX-MIB", "profileDestEnd"),
)
if mibBuilder.loadTexts:
    profileEntry.setStatus("mandatory")
_ProfileIndex_Type = Integer32
_ProfileIndex_Object = MibTableColumn
profileIndex = _ProfileIndex_Object(
    (1, 3, 6, 1, 4, 1, 97, 3, 23, 1, 1, 1),
    _ProfileIndex_Type()
)
profileIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    profileIndex.setStatus("mandatory")


class _ProfileSourceStart_Type(Integer32):
    """Custom type profileSourceStart based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_ProfileSourceStart_Type.__name__ = "Integer32"
_ProfileSourceStart_Object = MibTableColumn
profileSourceStart = _ProfileSourceStart_Object(
    (1, 3, 6, 1, 4, 1, 97, 3, 23, 1, 1, 2),
    _ProfileSourceStart_Type()
)
profileSourceStart.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    profileSourceStart.setStatus("mandatory")


class _ProfileSourceEnd_Type(Integer32):
    """Custom type profileSourceEnd based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_ProfileSourceEnd_Type.__name__ = "Integer32"
_ProfileSourceEnd_Object = MibTableColumn
profileSourceEnd = _ProfileSourceEnd_Object(
    (1, 3, 6, 1, 4, 1, 97, 3, 23, 1, 1, 3),
    _ProfileSourceEnd_Type()
)
profileSourceEnd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    profileSourceEnd.setStatus("mandatory")


class _ProfileDestStart_Type(Integer32):
    """Custom type profileDestStart based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_ProfileDestStart_Type.__name__ = "Integer32"
_ProfileDestStart_Object = MibTableColumn
profileDestStart = _ProfileDestStart_Object(
    (1, 3, 6, 1, 4, 1, 97, 3, 23, 1, 1, 4),
    _ProfileDestStart_Type()
)
profileDestStart.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    profileDestStart.setStatus("mandatory")


class _ProfileDestEnd_Type(Integer32):
    """Custom type profileDestEnd based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_ProfileDestEnd_Type.__name__ = "Integer32"
_ProfileDestEnd_Object = MibTableColumn
profileDestEnd = _ProfileDestEnd_Object(
    (1, 3, 6, 1, 4, 1, 97, 3, 23, 1, 1, 5),
    _ProfileDestEnd_Type()
)
profileDestEnd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    profileDestEnd.setStatus("mandatory")


class _ProfileType_Type(Integer32):
    """Custom type profileType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 2),
          ("valid", 1))
    )


_ProfileType_Type.__name__ = "Integer32"
_ProfileType_Object = MibTableColumn
profileType = _ProfileType_Object(
    (1, 3, 6, 1, 4, 1, 97, 3, 23, 1, 1, 6),
    _ProfileType_Type()
)
profileType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    profileType.setStatus("mandatory")
_RuleTable_Object = MibTable
ruleTable = _RuleTable_Object(
    (1, 3, 6, 1, 4, 1, 97, 3, 23, 2)
)
if mibBuilder.loadTexts:
    ruleTable.setStatus("mandatory")
_RuleEntry_Object = MibTableRow
ruleEntry = _RuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 97, 3, 23, 2, 1)
)
ruleEntry.setIndexNames(
    (0, "CTATX-MIB", "ruleIndex"),
    (0, "CTATX-MIB", "ruleSourceIp"),
    (0, "CTATX-MIB", "ruleDestIp"),
    (0, "CTATX-MIB", "ruleSourceIpMask"),
    (0, "CTATX-MIB", "ruleDestIpMask"),
)
if mibBuilder.loadTexts:
    ruleEntry.setStatus("mandatory")
_RuleIndex_Type = Integer32
_RuleIndex_Object = MibTableColumn
ruleIndex = _RuleIndex_Object(
    (1, 3, 6, 1, 4, 1, 97, 3, 23, 2, 1, 1),
    _RuleIndex_Type()
)
ruleIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruleIndex.setStatus("mandatory")
_RuleSourceIp_Type = IpAddress
_RuleSourceIp_Object = MibTableColumn
ruleSourceIp = _RuleSourceIp_Object(
    (1, 3, 6, 1, 4, 1, 97, 3, 23, 2, 1, 2),
    _RuleSourceIp_Type()
)
ruleSourceIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruleSourceIp.setStatus("mandatory")
_RuleDestIp_Type = IpAddress
_RuleDestIp_Object = MibTableColumn
ruleDestIp = _RuleDestIp_Object(
    (1, 3, 6, 1, 4, 1, 97, 3, 23, 2, 1, 3),
    _RuleDestIp_Type()
)
ruleDestIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruleDestIp.setStatus("mandatory")
_RuleSourceIpMask_Type = IpAddress
_RuleSourceIpMask_Object = MibTableColumn
ruleSourceIpMask = _RuleSourceIpMask_Object(
    (1, 3, 6, 1, 4, 1, 97, 3, 23, 2, 1, 4),
    _RuleSourceIpMask_Type()
)
ruleSourceIpMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruleSourceIpMask.setStatus("mandatory")
_RuleDestIpMask_Type = IpAddress
_RuleDestIpMask_Object = MibTableColumn
ruleDestIpMask = _RuleDestIpMask_Object(
    (1, 3, 6, 1, 4, 1, 97, 3, 23, 2, 1, 5),
    _RuleDestIpMask_Type()
)
ruleDestIpMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruleDestIpMask.setStatus("mandatory")


class _RuleType_Type(Integer32):
    """Custom type ruleType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 2),
          ("valid", 1))
    )


_RuleType_Type.__name__ = "Integer32"
_RuleType_Object = MibTableColumn
ruleType = _RuleType_Object(
    (1, 3, 6, 1, 4, 1, 97, 3, 23, 2, 1, 6),
    _RuleType_Type()
)
ruleType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruleType.setStatus("mandatory")


class _RuleUdpProfile_Type(Integer32):
    """Custom type ruleUdpProfile based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1023),
    )


_RuleUdpProfile_Type.__name__ = "Integer32"
_RuleUdpProfile_Object = MibTableColumn
ruleUdpProfile = _RuleUdpProfile_Object(
    (1, 3, 6, 1, 4, 1, 97, 3, 23, 2, 1, 7),
    _RuleUdpProfile_Type()
)
ruleUdpProfile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruleUdpProfile.setStatus("mandatory")


class _RuleTcpProfile_Type(Integer32):
    """Custom type ruleTcpProfile based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1023),
    )


_RuleTcpProfile_Type.__name__ = "Integer32"
_RuleTcpProfile_Object = MibTableColumn
ruleTcpProfile = _RuleTcpProfile_Object(
    (1, 3, 6, 1, 4, 1, 97, 3, 23, 2, 1, 8),
    _RuleTcpProfile_Type()
)
ruleTcpProfile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruleTcpProfile.setStatus("mandatory")


class _RuleTcpEstProfile_Type(Integer32):
    """Custom type ruleTcpEstProfile based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1023),
    )


_RuleTcpEstProfile_Type.__name__ = "Integer32"
_RuleTcpEstProfile_Object = MibTableColumn
ruleTcpEstProfile = _RuleTcpEstProfile_Object(
    (1, 3, 6, 1, 4, 1, 97, 3, 23, 2, 1, 9),
    _RuleTcpEstProfile_Type()
)
ruleTcpEstProfile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruleTcpEstProfile.setStatus("mandatory")
_RuleFilterUdpFragment_Type = Boolean
_RuleFilterUdpFragment_Object = MibTableColumn
ruleFilterUdpFragment = _RuleFilterUdpFragment_Object(
    (1, 3, 6, 1, 4, 1, 97, 3, 23, 2, 1, 10),
    _RuleFilterUdpFragment_Type()
)
ruleFilterUdpFragment.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruleFilterUdpFragment.setStatus("mandatory")
_RuleFilterTcpFragment_Type = Boolean
_RuleFilterTcpFragment_Object = MibTableColumn
ruleFilterTcpFragment = _RuleFilterTcpFragment_Object(
    (1, 3, 6, 1, 4, 1, 97, 3, 23, 2, 1, 11),
    _RuleFilterTcpFragment_Type()
)
ruleFilterTcpFragment.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruleFilterTcpFragment.setStatus("mandatory")
_RuleFilterIpOption_Type = Boolean
_RuleFilterIpOption_Object = MibTableColumn
ruleFilterIpOption = _RuleFilterIpOption_Object(
    (1, 3, 6, 1, 4, 1, 97, 3, 23, 2, 1, 12),
    _RuleFilterIpOption_Type()
)
ruleFilterIpOption.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruleFilterIpOption.setStatus("mandatory")
_RuleAllowIcmp_Type = Boolean
_RuleAllowIcmp_Object = MibTableColumn
ruleAllowIcmp = _RuleAllowIcmp_Object(
    (1, 3, 6, 1, 4, 1, 97, 3, 23, 2, 1, 13),
    _RuleAllowIcmp_Type()
)
ruleAllowIcmp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruleAllowIcmp.setStatus("mandatory")
_RuleAllowIpWithinIp_Type = Boolean
_RuleAllowIpWithinIp_Object = MibTableColumn
ruleAllowIpWithinIp = _RuleAllowIpWithinIp_Object(
    (1, 3, 6, 1, 4, 1, 97, 3, 23, 2, 1, 14),
    _RuleAllowIpWithinIp_Type()
)
ruleAllowIpWithinIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruleAllowIpWithinIp.setStatus("mandatory")
_RuleAllowEgp_Type = Boolean
_RuleAllowEgp_Object = MibTableColumn
ruleAllowEgp = _RuleAllowEgp_Object(
    (1, 3, 6, 1, 4, 1, 97, 3, 23, 2, 1, 15),
    _RuleAllowEgp_Type()
)
ruleAllowEgp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruleAllowEgp.setStatus("mandatory")
_RuleAllowIgp_Type = Boolean
_RuleAllowIgp_Object = MibTableColumn
ruleAllowIgp = _RuleAllowIgp_Object(
    (1, 3, 6, 1, 4, 1, 97, 3, 23, 2, 1, 16),
    _RuleAllowIgp_Type()
)
ruleAllowIgp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruleAllowIgp.setStatus("mandatory")
_RuleAllowIgrp_Type = Boolean
_RuleAllowIgrp_Object = MibTableColumn
ruleAllowIgrp = _RuleAllowIgrp_Object(
    (1, 3, 6, 1, 4, 1, 97, 3, 23, 2, 1, 17),
    _RuleAllowIgrp_Type()
)
ruleAllowIgrp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruleAllowIgrp.setStatus("mandatory")
_RuleAllowOspf_Type = Boolean
_RuleAllowOspf_Object = MibTableColumn
ruleAllowOspf = _RuleAllowOspf_Object(
    (1, 3, 6, 1, 4, 1, 97, 3, 23, 2, 1, 18),
    _RuleAllowOspf_Type()
)
ruleAllowOspf.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruleAllowOspf.setStatus("mandatory")
_RuleAllowAnyOther_Type = Boolean
_RuleAllowAnyOther_Object = MibTableColumn
ruleAllowAnyOther = _RuleAllowAnyOther_Object(
    (1, 3, 6, 1, 4, 1, 97, 3, 23, 2, 1, 19),
    _RuleAllowAnyOther_Type()
)
ruleAllowAnyOther.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruleAllowAnyOther.setStatus("mandatory")
_Spvc_ObjectIdentity = ObjectIdentity
spvc = _Spvc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 97, 3, 24)
)
_SpvcTable_Object = MibTable
spvcTable = _SpvcTable_Object(
    (1, 3, 6, 1, 4, 1, 97, 3, 24, 1)
)
if mibBuilder.loadTexts:
    spvcTable.setStatus("mandatory")
_SpvcEntry_Object = MibTableRow
spvcEntry = _SpvcEntry_Object(
    (1, 3, 6, 1, 4, 1, 97, 3, 24, 1, 1)
)
spvcEntry.setIndexNames(
    (0, "CTATX-MIB", "spvcIfIndex"),
)
if mibBuilder.loadTexts:
    spvcEntry.setStatus("mandatory")
_SpvcIfIndex_Type = Integer32
_SpvcIfIndex_Object = MibTableColumn
spvcIfIndex = _SpvcIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 97, 3, 24, 1, 1, 1),
    _SpvcIfIndex_Type()
)
spvcIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    spvcIfIndex.setStatus("mandatory")
_SpvcPathRX_Type = Integer32
_SpvcPathRX_Object = MibTableColumn
spvcPathRX = _SpvcPathRX_Object(
    (1, 3, 6, 1, 4, 1, 97, 3, 24, 1, 1, 2),
    _SpvcPathRX_Type()
)
spvcPathRX.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    spvcPathRX.setStatus("mandatory")
_SpvcCircuitRX_Type = Integer32
_SpvcCircuitRX_Object = MibTableColumn
spvcCircuitRX = _SpvcCircuitRX_Object(
    (1, 3, 6, 1, 4, 1, 97, 3, 24, 1, 1, 3),
    _SpvcCircuitRX_Type()
)
spvcCircuitRX.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    spvcCircuitRX.setStatus("mandatory")
_SpvcPathTX_Type = Integer32
_SpvcPathTX_Object = MibTableColumn
spvcPathTX = _SpvcPathTX_Object(
    (1, 3, 6, 1, 4, 1, 97, 3, 24, 1, 1, 4),
    _SpvcPathTX_Type()
)
spvcPathTX.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    spvcPathTX.setStatus("mandatory")
_SpvcCircuitTX_Type = Integer32
_SpvcCircuitTX_Object = MibTableColumn
spvcCircuitTX = _SpvcCircuitTX_Object(
    (1, 3, 6, 1, 4, 1, 97, 3, 24, 1, 1, 5),
    _SpvcCircuitTX_Type()
)
spvcCircuitTX.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    spvcCircuitTX.setStatus("mandatory")


class _SpvcState_Type(Integer32):
    """Custom type spvcState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("exists", 1),
          ("removed", 2))
    )


_SpvcState_Type.__name__ = "Integer32"
_SpvcState_Object = MibTableColumn
spvcState = _SpvcState_Object(
    (1, 3, 6, 1, 4, 1, 97, 3, 24, 1, 1, 6),
    _SpvcState_Type()
)
spvcState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    spvcState.setStatus("mandatory")
_SpvcPhysPort_Type = Integer32
_SpvcPhysPort_Object = MibTableColumn
spvcPhysPort = _SpvcPhysPort_Object(
    (1, 3, 6, 1, 4, 1, 97, 3, 24, 1, 1, 7),
    _SpvcPhysPort_Type()
)
spvcPhysPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    spvcPhysPort.setStatus("mandatory")
_SpvcMinPort_Type = Integer32
_SpvcMinPort_Object = MibScalar
spvcMinPort = _SpvcMinPort_Object(
    (1, 3, 6, 1, 4, 1, 97, 3, 24, 2),
    _SpvcMinPort_Type()
)
spvcMinPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    spvcMinPort.setStatus("mandatory")
_SpvcMaxPort_Type = Integer32
_SpvcMaxPort_Object = MibScalar
spvcMaxPort = _SpvcMaxPort_Object(
    (1, 3, 6, 1, 4, 1, 97, 3, 24, 3),
    _SpvcMaxPort_Type()
)
spvcMaxPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    spvcMaxPort.setStatus("mandatory")
_Strunk_ObjectIdentity = ObjectIdentity
strunk = _Strunk_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 97, 3, 25)
)
_StrunkTable_Object = MibTable
strunkTable = _StrunkTable_Object(
    (1, 3, 6, 1, 4, 1, 97, 3, 25, 1)
)
if mibBuilder.loadTexts:
    strunkTable.setStatus("mandatory")
_StrunkEntry_Object = MibTableRow
strunkEntry = _StrunkEntry_Object(
    (1, 3, 6, 1, 4, 1, 97, 3, 25, 1, 1)
)
strunkEntry.setIndexNames(
    (0, "CTATX-MIB", "strunkIfIndex"),
)
if mibBuilder.loadTexts:
    strunkEntry.setStatus("mandatory")
_StrunkIfIndex_Type = Integer32
_StrunkIfIndex_Object = MibTableColumn
strunkIfIndex = _StrunkIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 97, 3, 25, 1, 1, 1),
    _StrunkIfIndex_Type()
)
strunkIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    strunkIfIndex.setStatus("mandatory")


class _StrunkState_Type(Integer32):
    """Custom type strunkState based on Integer32"""
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
        *(("broken", 7),
          ("closed", 2),
          ("helddown", 6),
          ("joined", 4),
          ("off", 1),
          ("oneway", 3),
          ("perturbed", 5))
    )


_StrunkState_Type.__name__ = "Integer32"
_StrunkState_Object = MibTableColumn
strunkState = _StrunkState_Object(
    (1, 3, 6, 1, 4, 1, 97, 3, 25, 1, 1, 2),
    _StrunkState_Type()
)
strunkState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    strunkState.setStatus("mandatory")
_StrunkRemoteBridgeAddr_Type = OctetString
_StrunkRemoteBridgeAddr_Object = MibTableColumn
strunkRemoteBridgeAddr = _StrunkRemoteBridgeAddr_Object(
    (1, 3, 6, 1, 4, 1, 97, 3, 25, 1, 1, 3),
    _StrunkRemoteBridgeAddr_Type()
)
strunkRemoteBridgeAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    strunkRemoteBridgeAddr.setStatus("mandatory")
_StrunkRemoteIp_Type = IpAddress
_StrunkRemoteIp_Object = MibTableColumn
strunkRemoteIp = _StrunkRemoteIp_Object(
    (1, 3, 6, 1, 4, 1, 97, 3, 25, 1, 1, 4),
    _StrunkRemoteIp_Type()
)
strunkRemoteIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    strunkRemoteIp.setStatus("mandatory")


class _StrunkLastError_Type(Integer32):
    """Custom type strunkLastError based on Integer32"""
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
              8,
              9,
              10,
              11)
        )
    )
    namedValues = NamedValues(
        *(("ack-lost", 4),
          ("in-bpdu", 2),
          ("multiple-bridges", 3),
          ("multiple-lan-types", 11),
          ("no-ack", 7),
          ("none", 1),
          ("perturbed-threshold", 8),
          ("port-moved", 10),
          ("self-connect", 9),
          ("standby", 5),
          ("too-many-groups", 6))
    )


_StrunkLastError_Type.__name__ = "Integer32"
_StrunkLastError_Object = MibTableColumn
strunkLastError = _StrunkLastError_Object(
    (1, 3, 6, 1, 4, 1, 97, 3, 25, 1, 1, 5),
    _StrunkLastError_Type()
)
strunkLastError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    strunkLastError.setStatus("mandatory")
_StrunkLinkOrdinal_Type = Integer32
_StrunkLinkOrdinal_Object = MibTableColumn
strunkLinkOrdinal = _StrunkLinkOrdinal_Object(
    (1, 3, 6, 1, 4, 1, 97, 3, 25, 1, 1, 6),
    _StrunkLinkOrdinal_Type()
)
strunkLinkOrdinal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    strunkLinkOrdinal.setStatus("mandatory")
_StrunkLinkCount_Type = Integer32
_StrunkLinkCount_Object = MibTableColumn
strunkLinkCount = _StrunkLinkCount_Object(
    (1, 3, 6, 1, 4, 1, 97, 3, 25, 1, 1, 7),
    _StrunkLinkCount_Type()
)
strunkLinkCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    strunkLinkCount.setStatus("mandatory")
_StrunkLastChange_Type = Integer32
_StrunkLastChange_Object = MibTableColumn
strunkLastChange = _StrunkLastChange_Object(
    (1, 3, 6, 1, 4, 1, 97, 3, 25, 1, 1, 8),
    _StrunkLastChange_Type()
)
strunkLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    strunkLastChange.setStatus("mandatory")
_IpMRouteMIB_ObjectIdentity = ObjectIdentity
ipMRouteMIB = _IpMRouteMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 97, 3, 26)
)
_IpMRouteMIBObjects_ObjectIdentity = ObjectIdentity
ipMRouteMIBObjects = _IpMRouteMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 97, 3, 26, 1)
)
_IpMRoute_ObjectIdentity = ObjectIdentity
ipMRoute = _IpMRoute_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 97, 3, 26, 1, 1)
)


class _IpMRouteEnable_Type(Integer32):
    """Custom type ipMRouteEnable based on Integer32"""
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


_IpMRouteEnable_Type.__name__ = "Integer32"
_IpMRouteEnable_Object = MibScalar
ipMRouteEnable = _IpMRouteEnable_Object(
    (1, 3, 6, 1, 4, 1, 97, 3, 26, 1, 1, 1),
    _IpMRouteEnable_Type()
)
ipMRouteEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipMRouteEnable.setStatus("mandatory")
_IpMRouteTable_Object = MibTable
ipMRouteTable = _IpMRouteTable_Object(
    (1, 3, 6, 1, 4, 1, 97, 3, 26, 1, 1, 2)
)
if mibBuilder.loadTexts:
    ipMRouteTable.setStatus("mandatory")
_IpMRouteEntry_Object = MibTableRow
ipMRouteEntry = _IpMRouteEntry_Object(
    (1, 3, 6, 1, 4, 1, 97, 3, 26, 1, 1, 2, 1)
)
ipMRouteEntry.setIndexNames(
    (0, "CTATX-MIB", "ipMRouteGroup"),
    (0, "CTATX-MIB", "ipMRouteSource"),
    (0, "CTATX-MIB", "ipMRouteSourceMask"),
)
if mibBuilder.loadTexts:
    ipMRouteEntry.setStatus("mandatory")
_IpMRouteGroup_Type = IpAddress
_IpMRouteGroup_Object = MibTableColumn
ipMRouteGroup = _IpMRouteGroup_Object(
    (1, 3, 6, 1, 4, 1, 97, 3, 26, 1, 1, 2, 1, 1),
    _IpMRouteGroup_Type()
)
ipMRouteGroup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipMRouteGroup.setStatus("mandatory")
_IpMRouteSource_Type = IpAddress
_IpMRouteSource_Object = MibTableColumn
ipMRouteSource = _IpMRouteSource_Object(
    (1, 3, 6, 1, 4, 1, 97, 3, 26, 1, 1, 2, 1, 2),
    _IpMRouteSource_Type()
)
ipMRouteSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipMRouteSource.setStatus("mandatory")
_IpMRouteSourceMask_Type = IpAddress
_IpMRouteSourceMask_Object = MibTableColumn
ipMRouteSourceMask = _IpMRouteSourceMask_Object(
    (1, 3, 6, 1, 4, 1, 97, 3, 26, 1, 1, 2, 1, 3),
    _IpMRouteSourceMask_Type()
)
ipMRouteSourceMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipMRouteSourceMask.setStatus("mandatory")
_IpMRouteRpfNeighbor_Type = IpAddress
_IpMRouteRpfNeighbor_Object = MibTableColumn
ipMRouteRpfNeighbor = _IpMRouteRpfNeighbor_Object(
    (1, 3, 6, 1, 4, 1, 97, 3, 26, 1, 1, 2, 1, 4),
    _IpMRouteRpfNeighbor_Type()
)
ipMRouteRpfNeighbor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipMRouteRpfNeighbor.setStatus("mandatory")
_IpMRouteInIfIndex_Type = Integer32
_IpMRouteInIfIndex_Object = MibTableColumn
ipMRouteInIfIndex = _IpMRouteInIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 97, 3, 26, 1, 1, 2, 1, 5),
    _IpMRouteInIfIndex_Type()
)
ipMRouteInIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipMRouteInIfIndex.setStatus("mandatory")
_IpMRouteOutList_Type = OctetString
_IpMRouteOutList_Object = MibTableColumn
ipMRouteOutList = _IpMRouteOutList_Object(
    (1, 3, 6, 1, 4, 1, 97, 3, 26, 1, 1, 2, 1, 6),
    _IpMRouteOutList_Type()
)
ipMRouteOutList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipMRouteOutList.setStatus("mandatory")
_IpMRouteUpTime_Type = TimeTicks
_IpMRouteUpTime_Object = MibTableColumn
ipMRouteUpTime = _IpMRouteUpTime_Object(
    (1, 3, 6, 1, 4, 1, 97, 3, 26, 1, 1, 2, 1, 7),
    _IpMRouteUpTime_Type()
)
ipMRouteUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipMRouteUpTime.setStatus("mandatory")
_IpMRouteExpiryTime_Type = TimeTicks
_IpMRouteExpiryTime_Object = MibTableColumn
ipMRouteExpiryTime = _IpMRouteExpiryTime_Object(
    (1, 3, 6, 1, 4, 1, 97, 3, 26, 1, 1, 2, 1, 8),
    _IpMRouteExpiryTime_Type()
)
ipMRouteExpiryTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipMRouteExpiryTime.setStatus("mandatory")
_IpMRoutePkts_Type = Counter32
_IpMRoutePkts_Object = MibTableColumn
ipMRoutePkts = _IpMRoutePkts_Object(
    (1, 3, 6, 1, 4, 1, 97, 3, 26, 1, 1, 2, 1, 9),
    _IpMRoutePkts_Type()
)
ipMRoutePkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipMRoutePkts.setStatus("mandatory")
_IpMRouteRpfFails_Type = Counter32
_IpMRouteRpfFails_Object = MibTableColumn
ipMRouteRpfFails = _IpMRouteRpfFails_Object(
    (1, 3, 6, 1, 4, 1, 97, 3, 26, 1, 1, 2, 1, 10),
    _IpMRouteRpfFails_Type()
)
ipMRouteRpfFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipMRouteRpfFails.setStatus("mandatory")
_IpMRouteOctets_Type = Counter32
_IpMRouteOctets_Object = MibTableColumn
ipMRouteOctets = _IpMRouteOctets_Object(
    (1, 3, 6, 1, 4, 1, 97, 3, 26, 1, 1, 2, 1, 11),
    _IpMRouteOctets_Type()
)
ipMRouteOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipMRouteOctets.setStatus("mandatory")


class _IpMRouteNextHopState_Type(Integer32):
    """Custom type ipMRouteNextHopState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("forwarding", 2),
          ("pruned", 1))
    )


_IpMRouteNextHopState_Type.__name__ = "Integer32"
_IpMRouteNextHopState_Object = MibTableColumn
ipMRouteNextHopState = _IpMRouteNextHopState_Object(
    (1, 3, 6, 1, 4, 1, 97, 3, 26, 1, 1, 2, 1, 12),
    _IpMRouteNextHopState_Type()
)
ipMRouteNextHopState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipMRouteNextHopState.setStatus("mandatory")
_IpMRouteInterfaceTable_Object = MibTable
ipMRouteInterfaceTable = _IpMRouteInterfaceTable_Object(
    (1, 3, 6, 1, 4, 1, 97, 3, 26, 1, 1, 3)
)
if mibBuilder.loadTexts:
    ipMRouteInterfaceTable.setStatus("mandatory")
_IpMRouteInterfaceEntry_Object = MibTableRow
ipMRouteInterfaceEntry = _IpMRouteInterfaceEntry_Object(
    (1, 3, 6, 1, 4, 1, 97, 3, 26, 1, 1, 3, 1)
)
ipMRouteInterfaceEntry.setIndexNames(
    (0, "CTATX-MIB", "ipMRouteInterfaceIfIndex"),
)
if mibBuilder.loadTexts:
    ipMRouteInterfaceEntry.setStatus("mandatory")
_IpMRouteInterfaceIfIndex_Type = Integer32
_IpMRouteInterfaceIfIndex_Object = MibTableColumn
ipMRouteInterfaceIfIndex = _IpMRouteInterfaceIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 97, 3, 26, 1, 1, 3, 1, 1),
    _IpMRouteInterfaceIfIndex_Type()
)
ipMRouteInterfaceIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipMRouteInterfaceIfIndex.setStatus("mandatory")
_IpMRouteInterfaceTtl_Type = Integer32
_IpMRouteInterfaceTtl_Object = MibTableColumn
ipMRouteInterfaceTtl = _IpMRouteInterfaceTtl_Object(
    (1, 3, 6, 1, 4, 1, 97, 3, 26, 1, 1, 3, 1, 2),
    _IpMRouteInterfaceTtl_Type()
)
ipMRouteInterfaceTtl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipMRouteInterfaceTtl.setStatus("mandatory")
_IgmpMIB_ObjectIdentity = ObjectIdentity
igmpMIB = _IgmpMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 97, 3, 27)
)
_IgmpMIBObjects_ObjectIdentity = ObjectIdentity
igmpMIBObjects = _IgmpMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 97, 3, 27, 1)
)
_Igmp_ObjectIdentity = ObjectIdentity
igmp = _Igmp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 97, 3, 27, 1, 1)
)
_IgmpInterfaceTable_Object = MibTable
igmpInterfaceTable = _IgmpInterfaceTable_Object(
    (1, 3, 6, 1, 4, 1, 97, 3, 27, 1, 1, 1)
)
if mibBuilder.loadTexts:
    igmpInterfaceTable.setStatus("mandatory")
_IgmpInterfaceEntry_Object = MibTableRow
igmpInterfaceEntry = _IgmpInterfaceEntry_Object(
    (1, 3, 6, 1, 4, 1, 97, 3, 27, 1, 1, 1, 1)
)
igmpInterfaceEntry.setIndexNames(
    (0, "CTATX-MIB", "igmpInterfaceIfIndex"),
)
if mibBuilder.loadTexts:
    igmpInterfaceEntry.setStatus("mandatory")
_IgmpInterfaceIfIndex_Type = Integer32
_IgmpInterfaceIfIndex_Object = MibTableColumn
igmpInterfaceIfIndex = _IgmpInterfaceIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 97, 3, 27, 1, 1, 1, 1, 1),
    _IgmpInterfaceIfIndex_Type()
)
igmpInterfaceIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igmpInterfaceIfIndex.setStatus("mandatory")
_IgmpInterfaceQueryInterval_Type = Integer32
_IgmpInterfaceQueryInterval_Object = MibTableColumn
igmpInterfaceQueryInterval = _IgmpInterfaceQueryInterval_Object(
    (1, 3, 6, 1, 4, 1, 97, 3, 27, 1, 1, 1, 1, 2),
    _IgmpInterfaceQueryInterval_Type()
)
igmpInterfaceQueryInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    igmpInterfaceQueryInterval.setStatus("mandatory")
_IgmpInterfaceStatus_Type = Integer32
_IgmpInterfaceStatus_Object = MibTableColumn
igmpInterfaceStatus = _IgmpInterfaceStatus_Object(
    (1, 3, 6, 1, 4, 1, 97, 3, 27, 1, 1, 1, 1, 3),
    _IgmpInterfaceStatus_Type()
)
igmpInterfaceStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    igmpInterfaceStatus.setStatus("mandatory")
_IgmpCacheTable_Object = MibTable
igmpCacheTable = _IgmpCacheTable_Object(
    (1, 3, 6, 1, 4, 1, 97, 3, 27, 1, 1, 2)
)
if mibBuilder.loadTexts:
    igmpCacheTable.setStatus("mandatory")
_IgmpCacheEntry_Object = MibTableRow
igmpCacheEntry = _IgmpCacheEntry_Object(
    (1, 3, 6, 1, 4, 1, 97, 3, 27, 1, 1, 2, 1)
)
igmpCacheEntry.setIndexNames(
    (0, "CTATX-MIB", "igmpCacheAddress"),
    (0, "CTATX-MIB", "igmpCacheIfIndex"),
)
if mibBuilder.loadTexts:
    igmpCacheEntry.setStatus("mandatory")
_IgmpCacheAddress_Type = IpAddress
_IgmpCacheAddress_Object = MibTableColumn
igmpCacheAddress = _IgmpCacheAddress_Object(
    (1, 3, 6, 1, 4, 1, 97, 3, 27, 1, 1, 2, 1, 1),
    _IgmpCacheAddress_Type()
)
igmpCacheAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igmpCacheAddress.setStatus("mandatory")
_IgmpCacheIfIndex_Type = Integer32
_IgmpCacheIfIndex_Object = MibTableColumn
igmpCacheIfIndex = _IgmpCacheIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 97, 3, 27, 1, 1, 2, 1, 2),
    _IgmpCacheIfIndex_Type()
)
igmpCacheIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igmpCacheIfIndex.setStatus("mandatory")
_IgmpCacheSelf_Type = Integer32
_IgmpCacheSelf_Object = MibTableColumn
igmpCacheSelf = _IgmpCacheSelf_Object(
    (1, 3, 6, 1, 4, 1, 97, 3, 27, 1, 1, 2, 1, 3),
    _IgmpCacheSelf_Type()
)
igmpCacheSelf.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    igmpCacheSelf.setStatus("mandatory")
_IgmpCacheLastReporter_Type = IpAddress
_IgmpCacheLastReporter_Object = MibTableColumn
igmpCacheLastReporter = _IgmpCacheLastReporter_Object(
    (1, 3, 6, 1, 4, 1, 97, 3, 27, 1, 1, 2, 1, 4),
    _IgmpCacheLastReporter_Type()
)
igmpCacheLastReporter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igmpCacheLastReporter.setStatus("mandatory")
_IgmpCacheUpTime_Type = TimeTicks
_IgmpCacheUpTime_Object = MibTableColumn
igmpCacheUpTime = _IgmpCacheUpTime_Object(
    (1, 3, 6, 1, 4, 1, 97, 3, 27, 1, 1, 2, 1, 5),
    _IgmpCacheUpTime_Type()
)
igmpCacheUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igmpCacheUpTime.setStatus("mandatory")
_IgmpCacheExpiryTime_Type = TimeTicks
_IgmpCacheExpiryTime_Object = MibTableColumn
igmpCacheExpiryTime = _IgmpCacheExpiryTime_Object(
    (1, 3, 6, 1, 4, 1, 97, 3, 27, 1, 1, 2, 1, 6),
    _IgmpCacheExpiryTime_Type()
)
igmpCacheExpiryTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igmpCacheExpiryTime.setStatus("mandatory")
_IgmpCacheStatus_Type = Integer32
_IgmpCacheStatus_Object = MibTableColumn
igmpCacheStatus = _IgmpCacheStatus_Object(
    (1, 3, 6, 1, 4, 1, 97, 3, 27, 1, 1, 2, 1, 7),
    _IgmpCacheStatus_Type()
)
igmpCacheStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    igmpCacheStatus.setStatus("mandatory")
_Slog_ObjectIdentity = ObjectIdentity
slog = _Slog_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 97, 3, 28)
)
_SlogFilter_Type = OctetString
_SlogFilter_Object = MibScalar
slogFilter = _SlogFilter_Object(
    (1, 3, 6, 1, 4, 1, 97, 3, 28, 1),
    _SlogFilter_Type()
)
slogFilter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slogFilter.setStatus("mandatory")


class _SlogTrap_Type(Integer32):
    """Custom type slogTrap based on Integer32"""
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


_SlogTrap_Type.__name__ = "Integer32"
_SlogTrap_Object = MibScalar
slogTrap = _SlogTrap_Object(
    (1, 3, 6, 1, 4, 1, 97, 3, 28, 2),
    _SlogTrap_Type()
)
slogTrap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slogTrap.setStatus("mandatory")


class _SlogOverwrite_Type(Integer32):
    """Custom type slogOverwrite based on Integer32"""
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


_SlogOverwrite_Type.__name__ = "Integer32"
_SlogOverwrite_Object = MibScalar
slogOverwrite = _SlogOverwrite_Object(
    (1, 3, 6, 1, 4, 1, 97, 3, 28, 3),
    _SlogOverwrite_Type()
)
slogOverwrite.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slogOverwrite.setStatus("mandatory")
_SlogEntryNumber_Type = Integer32
_SlogEntryNumber_Object = MibScalar
slogEntryNumber = _SlogEntryNumber_Object(
    (1, 3, 6, 1, 4, 1, 97, 3, 28, 4),
    _SlogEntryNumber_Type()
)
slogEntryNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slogEntryNumber.setStatus("mandatory")
_SlogEntryTable_Object = MibTable
slogEntryTable = _SlogEntryTable_Object(
    (1, 3, 6, 1, 4, 1, 97, 3, 28, 5)
)
if mibBuilder.loadTexts:
    slogEntryTable.setStatus("mandatory")
_SlogEntry_Object = MibTableRow
slogEntry = _SlogEntry_Object(
    (1, 3, 6, 1, 4, 1, 97, 3, 28, 5, 1)
)
slogEntry.setIndexNames(
    (0, "CTATX-MIB", "slogIndex"),
)
if mibBuilder.loadTexts:
    slogEntry.setStatus("mandatory")
_SlogIndex_Type = Integer32
_SlogIndex_Object = MibTableColumn
slogIndex = _SlogIndex_Object(
    (1, 3, 6, 1, 4, 1, 97, 3, 28, 5, 1, 1),
    _SlogIndex_Type()
)
slogIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slogIndex.setStatus("mandatory")
_SlogEntryTimeStamp_Type = TimeTicks
_SlogEntryTimeStamp_Object = MibTableColumn
slogEntryTimeStamp = _SlogEntryTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 97, 3, 28, 5, 1, 2),
    _SlogEntryTimeStamp_Type()
)
slogEntryTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slogEntryTimeStamp.setStatus("mandatory")
_SlogEntryMessageText_Type = DisplayString
_SlogEntryMessageText_Object = MibTableColumn
slogEntryMessageText = _SlogEntryMessageText_Object(
    (1, 3, 6, 1, 4, 1, 97, 3, 28, 5, 1, 3),
    _SlogEntryMessageText_Type()
)
slogEntryMessageText.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slogEntryMessageText.setStatus("mandatory")
_SlogEntryName_Type = DisplayString
_SlogEntryName_Object = MibTableColumn
slogEntryName = _SlogEntryName_Object(
    (1, 3, 6, 1, 4, 1, 97, 3, 28, 5, 1, 4),
    _SlogEntryName_Type()
)
slogEntryName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slogEntryName.setStatus("mandatory")
_Strap_ObjectIdentity = ObjectIdentity
strap = _Strap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 97, 3, 29)
)
_StrapControlTable_Object = MibTable
strapControlTable = _StrapControlTable_Object(
    (1, 3, 6, 1, 4, 1, 97, 3, 29, 1)
)
if mibBuilder.loadTexts:
    strapControlTable.setStatus("mandatory")
_StrapControl_Object = MibTableRow
strapControl = _StrapControl_Object(
    (1, 3, 6, 1, 4, 1, 97, 3, 29, 1, 1)
)
strapControl.setIndexNames(
    (0, "CTATX-MIB", "strapIndex"),
)
if mibBuilder.loadTexts:
    strapControl.setStatus("mandatory")
_StrapIndex_Type = Integer32
_StrapIndex_Object = MibTableColumn
strapIndex = _StrapIndex_Object(
    (1, 3, 6, 1, 4, 1, 97, 3, 29, 1, 1, 1),
    _StrapIndex_Type()
)
strapIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    strapIndex.setStatus("mandatory")


class _StrapEnabled_Type(Integer32):
    """Custom type strapEnabled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 2),
          ("true", 1))
    )


_StrapEnabled_Type.__name__ = "Integer32"
_StrapEnabled_Object = MibTableColumn
strapEnabled = _StrapEnabled_Object(
    (1, 3, 6, 1, 4, 1, 97, 3, 29, 1, 1, 2),
    _StrapEnabled_Type()
)
strapEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    strapEnabled.setStatus("mandatory")


class _StrapSeverity_Type(Integer32):
    """Custom type strapSeverity based on Integer32"""
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
        *(("critical", 5),
          ("informational", 1),
          ("major", 4),
          ("minor", 3),
          ("warning", 2))
    )


_StrapSeverity_Type.__name__ = "Integer32"
_StrapSeverity_Object = MibTableColumn
strapSeverity = _StrapSeverity_Object(
    (1, 3, 6, 1, 4, 1, 97, 3, 29, 1, 1, 3),
    _StrapSeverity_Type()
)
strapSeverity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    strapSeverity.setStatus("mandatory")
_StrapText_Type = DisplayString
_StrapText_Object = MibTableColumn
strapText = _StrapText_Object(
    (1, 3, 6, 1, 4, 1, 97, 3, 29, 1, 1, 4),
    _StrapText_Type()
)
strapText.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    strapText.setStatus("mandatory")
_StrapSeverityControlTable_Object = MibTable
strapSeverityControlTable = _StrapSeverityControlTable_Object(
    (1, 3, 6, 1, 4, 1, 97, 3, 29, 2)
)
if mibBuilder.loadTexts:
    strapSeverityControlTable.setStatus("mandatory")
_StrapSeverityControl_Object = MibTableRow
strapSeverityControl = _StrapSeverityControl_Object(
    (1, 3, 6, 1, 4, 1, 97, 3, 29, 2, 1)
)
strapSeverityControl.setIndexNames(
    (0, "CTATX-MIB", "strapSeveritySeverity"),
)
if mibBuilder.loadTexts:
    strapSeverityControl.setStatus("mandatory")


class _StrapSeveritySeverity_Type(Integer32):
    """Custom type strapSeveritySeverity based on Integer32"""
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
        *(("critical", 5),
          ("informational", 1),
          ("major", 4),
          ("minor", 3),
          ("warning", 2))
    )


_StrapSeveritySeverity_Type.__name__ = "Integer32"
_StrapSeveritySeverity_Object = MibTableColumn
strapSeveritySeverity = _StrapSeveritySeverity_Object(
    (1, 3, 6, 1, 4, 1, 97, 3, 29, 2, 1, 1),
    _StrapSeveritySeverity_Type()
)
strapSeveritySeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    strapSeveritySeverity.setStatus("mandatory")


class _StrapSeverityEnable_Type(Integer32):
    """Custom type strapSeverityEnable based on Integer32"""
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


_StrapSeverityEnable_Type.__name__ = "Integer32"
_StrapSeverityEnable_Object = MibTableColumn
strapSeverityEnable = _StrapSeverityEnable_Object(
    (1, 3, 6, 1, 4, 1, 97, 3, 29, 2, 1, 2),
    _StrapSeverityEnable_Type()
)
strapSeverityEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    strapSeverityEnable.setStatus("mandatory")


class _StrapIncludeText_Type(Integer32):
    """Custom type strapIncludeText based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 2),
          ("true", 1))
    )


_StrapIncludeText_Type.__name__ = "Integer32"
_StrapIncludeText_Object = MibScalar
strapIncludeText = _StrapIncludeText_Object(
    (1, 3, 6, 1, 4, 1, 97, 3, 29, 3),
    _StrapIncludeText_Type()
)
strapIncludeText.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    strapIncludeText.setStatus("mandatory")
_StrapTime_Type = TimeTicks
_StrapTime_Object = MibScalar
strapTime = _StrapTime_Object(
    (1, 3, 6, 1, 4, 1, 97, 3, 29, 4),
    _StrapTime_Type()
)
strapTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    strapTime.setStatus("mandatory")
_StrapRetry_Type = Integer32
_StrapRetry_Object = MibScalar
strapRetry = _StrapRetry_Object(
    (1, 3, 6, 1, 4, 1, 97, 3, 29, 5),
    _StrapRetry_Type()
)
strapRetry.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    strapRetry.setStatus("mandatory")
_StrapEntryNumber_Type = Integer32
_StrapEntryNumber_Object = MibScalar
strapEntryNumber = _StrapEntryNumber_Object(
    (1, 3, 6, 1, 4, 1, 97, 3, 29, 6),
    _StrapEntryNumber_Type()
)
strapEntryNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    strapEntryNumber.setStatus("mandatory")
_StrapTable_Object = MibTable
strapTable = _StrapTable_Object(
    (1, 3, 6, 1, 4, 1, 97, 3, 29, 7)
)
if mibBuilder.loadTexts:
    strapTable.setStatus("mandatory")
_StrapEntry_Object = MibTableRow
strapEntry = _StrapEntry_Object(
    (1, 3, 6, 1, 4, 1, 97, 3, 29, 7, 1)
)
strapEntry.setIndexNames(
    (0, "CTATX-MIB", "strapEntryIndex"),
)
if mibBuilder.loadTexts:
    strapEntry.setStatus("mandatory")
_StrapEntryIndex_Type = Integer32
_StrapEntryIndex_Object = MibTableColumn
strapEntryIndex = _StrapEntryIndex_Object(
    (1, 3, 6, 1, 4, 1, 97, 3, 29, 7, 1, 1),
    _StrapEntryIndex_Type()
)
strapEntryIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    strapEntryIndex.setStatus("mandatory")
_StrapEntryTimeStamp_Type = TimeTicks
_StrapEntryTimeStamp_Object = MibTableColumn
strapEntryTimeStamp = _StrapEntryTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 97, 3, 29, 7, 1, 2),
    _StrapEntryTimeStamp_Type()
)
strapEntryTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    strapEntryTimeStamp.setStatus("mandatory")
_StrapEntryText_Type = DisplayString
_StrapEntryText_Object = MibTableColumn
strapEntryText = _StrapEntryText_Object(
    (1, 3, 6, 1, 4, 1, 97, 3, 29, 7, 1, 3),
    _StrapEntryText_Type()
)
strapEntryText.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    strapEntryText.setStatus("mandatory")
_StrapNumber_Type = Integer32
_StrapNumber_Object = MibTableColumn
strapNumber = _StrapNumber_Object(
    (1, 3, 6, 1, 4, 1, 97, 3, 29, 7, 1, 4),
    _StrapNumber_Type()
)
strapNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    strapNumber.setStatus("mandatory")


class _StrapEntrySeverity_Type(Integer32):
    """Custom type strapEntrySeverity based on Integer32"""
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
        *(("critical", 5),
          ("informational", 1),
          ("major", 4),
          ("minor", 3),
          ("warning", 2))
    )


_StrapEntrySeverity_Type.__name__ = "Integer32"
_StrapEntrySeverity_Object = MibTableColumn
strapEntrySeverity = _StrapEntrySeverity_Object(
    (1, 3, 6, 1, 4, 1, 97, 3, 29, 7, 1, 5),
    _StrapEntrySeverity_Type()
)
strapEntrySeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    strapEntrySeverity.setStatus("mandatory")
_Smirror_ObjectIdentity = ObjectIdentity
smirror = _Smirror_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 97, 3, 30)
)


class _SmirrorStatus_Type(Integer32):
    """Custom type smirrorStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 1),
          ("local", 2),
          ("remote", 3))
    )


_SmirrorStatus_Type.__name__ = "Integer32"
_SmirrorStatus_Object = MibScalar
smirrorStatus = _SmirrorStatus_Object(
    (1, 3, 6, 1, 4, 1, 97, 3, 30, 1),
    _SmirrorStatus_Type()
)
smirrorStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    smirrorStatus.setStatus("mandatory")
_SmirrorDiagPort_Type = Integer32
_SmirrorDiagPort_Object = MibScalar
smirrorDiagPort = _SmirrorDiagPort_Object(
    (1, 3, 6, 1, 4, 1, 97, 3, 30, 2),
    _SmirrorDiagPort_Type()
)
smirrorDiagPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    smirrorDiagPort.setStatus("mandatory")
_SmirrorIPaddr_Type = IpAddress
_SmirrorIPaddr_Object = MibScalar
smirrorIPaddr = _SmirrorIPaddr_Object(
    (1, 3, 6, 1, 4, 1, 97, 3, 30, 3),
    _SmirrorIPaddr_Type()
)
smirrorIPaddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    smirrorIPaddr.setStatus("mandatory")
_SmirrorTargetPortLists_Type = OctetString
_SmirrorTargetPortLists_Object = MibScalar
smirrorTargetPortLists = _SmirrorTargetPortLists_Object(
    (1, 3, 6, 1, 4, 1, 97, 3, 30, 4),
    _SmirrorTargetPortLists_Type()
)
smirrorTargetPortLists.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    smirrorTargetPortLists.setStatus("mandatory")


class _SmirrorOversizePkt_Type(Integer32):
    """Custom type smirrorOversizePkt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("discard", 1),
          ("truncate", 2))
    )


_SmirrorOversizePkt_Type.__name__ = "Integer32"
_SmirrorOversizePkt_Object = MibScalar
smirrorOversizePkt = _SmirrorOversizePkt_Object(
    (1, 3, 6, 1, 4, 1, 97, 3, 30, 5),
    _SmirrorOversizePkt_Type()
)
smirrorOversizePkt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    smirrorOversizePkt.setStatus("mandatory")
_SmirrorEntryMirroredPkts_Type = Counter32
_SmirrorEntryMirroredPkts_Object = MibScalar
smirrorEntryMirroredPkts = _SmirrorEntryMirroredPkts_Object(
    (1, 3, 6, 1, 4, 1, 97, 3, 30, 6),
    _SmirrorEntryMirroredPkts_Type()
)
smirrorEntryMirroredPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smirrorEntryMirroredPkts.setStatus("mandatory")
_SmirrorExitMirroredPkts_Type = Counter32
_SmirrorExitMirroredPkts_Object = MibScalar
smirrorExitMirroredPkts = _SmirrorExitMirroredPkts_Object(
    (1, 3, 6, 1, 4, 1, 97, 3, 30, 7),
    _SmirrorExitMirroredPkts_Type()
)
smirrorExitMirroredPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smirrorExitMirroredPkts.setStatus("mandatory")
_SmirrorNotreadyDroppedPkts_Type = Counter32
_SmirrorNotreadyDroppedPkts_Object = MibScalar
smirrorNotreadyDroppedPkts = _SmirrorNotreadyDroppedPkts_Object(
    (1, 3, 6, 1, 4, 1, 97, 3, 30, 8),
    _SmirrorNotreadyDroppedPkts_Type()
)
smirrorNotreadyDroppedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smirrorNotreadyDroppedPkts.setStatus("mandatory")
_SmirrorOversizeDroppedPkts_Type = Counter32
_SmirrorOversizeDroppedPkts_Object = MibScalar
smirrorOversizeDroppedPkts = _SmirrorOversizeDroppedPkts_Object(
    (1, 3, 6, 1, 4, 1, 97, 3, 30, 9),
    _SmirrorOversizeDroppedPkts_Type()
)
smirrorOversizeDroppedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smirrorOversizeDroppedPkts.setStatus("mandatory")
_SmirrorEntryFilteredPkts_Type = Counter32
_SmirrorEntryFilteredPkts_Object = MibScalar
smirrorEntryFilteredPkts = _SmirrorEntryFilteredPkts_Object(
    (1, 3, 6, 1, 4, 1, 97, 3, 30, 10),
    _SmirrorEntryFilteredPkts_Type()
)
smirrorEntryFilteredPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smirrorEntryFilteredPkts.setStatus("mandatory")
_SmirrorExitFilteredPkts_Type = Counter32
_SmirrorExitFilteredPkts_Object = MibScalar
smirrorExitFilteredPkts = _SmirrorExitFilteredPkts_Object(
    (1, 3, 6, 1, 4, 1, 97, 3, 30, 11),
    _SmirrorExitFilteredPkts_Type()
)
smirrorExitFilteredPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smirrorExitFilteredPkts.setStatus("mandatory")
_SmirrorCongestionDroppedPkts_Type = Counter32
_SmirrorCongestionDroppedPkts_Object = MibScalar
smirrorCongestionDroppedPkts = _SmirrorCongestionDroppedPkts_Object(
    (1, 3, 6, 1, 4, 1, 97, 3, 30, 12),
    _SmirrorCongestionDroppedPkts_Type()
)
smirrorCongestionDroppedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smirrorCongestionDroppedPkts.setStatus("mandatory")
_SmirrorNowrapperDroppedPkts_Type = Counter32
_SmirrorNowrapperDroppedPkts_Object = MibScalar
smirrorNowrapperDroppedPkts = _SmirrorNowrapperDroppedPkts_Object(
    (1, 3, 6, 1, 4, 1, 97, 3, 30, 13),
    _SmirrorNowrapperDroppedPkts_Type()
)
smirrorNowrapperDroppedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smirrorNowrapperDroppedPkts.setStatus("mandatory")


class _SmirrorRemoteStatus_Type(Integer32):
    """Custom type smirrorRemoteStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              6,
              7,
              8,
              9)
        )
    )
    namedValues = NamedValues(
        *(("arpRefreshInProgress", 2),
          ("handshakeInProgress", 1),
          ("mirrorOff", 0),
          ("mirroring", 6),
          ("remoteDiagnosticPortBroken", 8),
          ("remoteHostUnreachable", 3),
          ("remoteMirrorNotOn", 9),
          ("versionIncompatible", 7))
    )


_SmirrorRemoteStatus_Type.__name__ = "Integer32"
_SmirrorRemoteStatus_Object = MibScalar
smirrorRemoteStatus = _SmirrorRemoteStatus_Object(
    (1, 3, 6, 1, 4, 1, 97, 3, 30, 14),
    _SmirrorRemoteStatus_Type()
)
smirrorRemoteStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smirrorRemoteStatus.setStatus("mandatory")
_SmirrorRemoteExitPort_Type = Integer32
_SmirrorRemoteExitPort_Object = MibScalar
smirrorRemoteExitPort = _SmirrorRemoteExitPort_Object(
    (1, 3, 6, 1, 4, 1, 97, 3, 30, 15),
    _SmirrorRemoteExitPort_Type()
)
smirrorRemoteExitPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smirrorRemoteExitPort.setStatus("mandatory")
_Sworkgroup_ObjectIdentity = ObjectIdentity
sworkgroup = _Sworkgroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 97, 3, 31)
)
_SWorkGroupNextNumber_Type = Integer32
_SWorkGroupNextNumber_Object = MibScalar
sWorkGroupNextNumber = _SWorkGroupNextNumber_Object(
    (1, 3, 6, 1, 4, 1, 97, 3, 31, 1),
    _SWorkGroupNextNumber_Type()
)
sWorkGroupNextNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sWorkGroupNextNumber.setStatus("mandatory")
_SWorkGroupCurrentCount_Type = Integer32
_SWorkGroupCurrentCount_Object = MibScalar
sWorkGroupCurrentCount = _SWorkGroupCurrentCount_Object(
    (1, 3, 6, 1, 4, 1, 97, 3, 31, 2),
    _SWorkGroupCurrentCount_Type()
)
sWorkGroupCurrentCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sWorkGroupCurrentCount.setStatus("mandatory")
_SWorkGroupMaxCount_Type = Integer32
_SWorkGroupMaxCount_Object = MibScalar
sWorkGroupMaxCount = _SWorkGroupMaxCount_Object(
    (1, 3, 6, 1, 4, 1, 97, 3, 31, 3),
    _SWorkGroupMaxCount_Type()
)
sWorkGroupMaxCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sWorkGroupMaxCount.setStatus("mandatory")
_SWorkGroupTable_Object = MibTable
sWorkGroupTable = _SWorkGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 97, 3, 31, 4)
)
if mibBuilder.loadTexts:
    sWorkGroupTable.setStatus("mandatory")
_SWorkGroupEntry_Object = MibTableRow
sWorkGroupEntry = _SWorkGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 97, 3, 31, 4, 1)
)
sWorkGroupEntry.setIndexNames(
    (0, "CTATX-MIB", "sWorkGroupNumber"),
)
if mibBuilder.loadTexts:
    sWorkGroupEntry.setStatus("mandatory")
_SWorkGroupNumber_Type = Integer32
_SWorkGroupNumber_Object = MibTableColumn
sWorkGroupNumber = _SWorkGroupNumber_Object(
    (1, 3, 6, 1, 4, 1, 97, 3, 31, 4, 1, 1),
    _SWorkGroupNumber_Type()
)
sWorkGroupNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sWorkGroupNumber.setStatus("mandatory")
_SWorkGroupName_Type = DisplayString
_SWorkGroupName_Object = MibTableColumn
sWorkGroupName = _SWorkGroupName_Object(
    (1, 3, 6, 1, 4, 1, 97, 3, 31, 4, 1, 2),
    _SWorkGroupName_Type()
)
sWorkGroupName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sWorkGroupName.setStatus("mandatory")
_SWorkGroupPorts_Type = OctetString
_SWorkGroupPorts_Object = MibTableColumn
sWorkGroupPorts = _SWorkGroupPorts_Object(
    (1, 3, 6, 1, 4, 1, 97, 3, 31, 4, 1, 3),
    _SWorkGroupPorts_Type()
)
sWorkGroupPorts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sWorkGroupPorts.setStatus("mandatory")


class _SWorkGroupType_Type(Integer32):
    """Custom type sWorkGroupType based on Integer32"""
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
        *(("all", 3),
          ("invalid", 4),
          ("ip", 1),
          ("ipx", 2))
    )


_SWorkGroupType_Type.__name__ = "Integer32"
_SWorkGroupType_Object = MibTableColumn
sWorkGroupType = _SWorkGroupType_Object(
    (1, 3, 6, 1, 4, 1, 97, 3, 31, 4, 1, 4),
    _SWorkGroupType_Type()
)
sWorkGroupType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sWorkGroupType.setStatus("mandatory")
_SWorkGroupIpAddress_Type = IpAddress
_SWorkGroupIpAddress_Object = MibTableColumn
sWorkGroupIpAddress = _SWorkGroupIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 97, 3, 31, 4, 1, 5),
    _SWorkGroupIpAddress_Type()
)
sWorkGroupIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sWorkGroupIpAddress.setStatus("mandatory")
_SWorkGroupIpMask_Type = IpAddress
_SWorkGroupIpMask_Object = MibTableColumn
sWorkGroupIpMask = _SWorkGroupIpMask_Object(
    (1, 3, 6, 1, 4, 1, 97, 3, 31, 4, 1, 6),
    _SWorkGroupIpMask_Type()
)
sWorkGroupIpMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sWorkGroupIpMask.setStatus("mandatory")
_SWorkGroupIpxNetwork_Type = OctetString
_SWorkGroupIpxNetwork_Object = MibTableColumn
sWorkGroupIpxNetwork = _SWorkGroupIpxNetwork_Object(
    (1, 3, 6, 1, 4, 1, 97, 3, 31, 4, 1, 7),
    _SWorkGroupIpxNetwork_Type()
)
sWorkGroupIpxNetwork.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sWorkGroupIpxNetwork.setStatus("mandatory")
_Sping_ObjectIdentity = ObjectIdentity
sping = _Sping_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 97, 3, 32)
)
_SpingDataTimeout_Type = TimeTicks
_SpingDataTimeout_Object = MibScalar
spingDataTimeout = _SpingDataTimeout_Object(
    (1, 3, 6, 1, 4, 1, 97, 3, 32, 1),
    _SpingDataTimeout_Type()
)
spingDataTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    spingDataTimeout.setStatus("mandatory")
_SpingTable_Object = MibTable
spingTable = _SpingTable_Object(
    (1, 3, 6, 1, 4, 1, 97, 3, 32, 2)
)
if mibBuilder.loadTexts:
    spingTable.setStatus("mandatory")
_SpingEntry_Object = MibTableRow
spingEntry = _SpingEntry_Object(
    (1, 3, 6, 1, 4, 1, 97, 3, 32, 2, 1)
)
spingEntry.setIndexNames(
    (0, "CTATX-MIB", "spingNMSAddr"),
    (0, "CTATX-MIB", "spingDestAddr"),
)
if mibBuilder.loadTexts:
    spingEntry.setStatus("mandatory")
_SpingNMSAddr_Type = IpAddress
_SpingNMSAddr_Object = MibTableColumn
spingNMSAddr = _SpingNMSAddr_Object(
    (1, 3, 6, 1, 4, 1, 97, 3, 32, 2, 1, 1),
    _SpingNMSAddr_Type()
)
spingNMSAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    spingNMSAddr.setStatus("mandatory")
_SpingDestAddr_Type = IpAddress
_SpingDestAddr_Object = MibTableColumn
spingDestAddr = _SpingDestAddr_Object(
    (1, 3, 6, 1, 4, 1, 97, 3, 32, 2, 1, 2),
    _SpingDestAddr_Type()
)
spingDestAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    spingDestAddr.setStatus("mandatory")


class _SpingState_Type(Integer32):
    """Custom type spingState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("completed", 3),
          ("not-started", 0),
          ("timed-out", 2))
    )


_SpingState_Type.__name__ = "Integer32"
_SpingState_Object = MibTableColumn
spingState = _SpingState_Object(
    (1, 3, 6, 1, 4, 1, 97, 3, 32, 2, 1, 3),
    _SpingState_Type()
)
spingState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    spingState.setStatus("mandatory")
_SpingCount_Type = Integer32
_SpingCount_Object = MibTableColumn
spingCount = _SpingCount_Object(
    (1, 3, 6, 1, 4, 1, 97, 3, 32, 2, 1, 4),
    _SpingCount_Type()
)
spingCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    spingCount.setStatus("mandatory")
_SpingDataSize_Type = Integer32
_SpingDataSize_Object = MibTableColumn
spingDataSize = _SpingDataSize_Object(
    (1, 3, 6, 1, 4, 1, 97, 3, 32, 2, 1, 5),
    _SpingDataSize_Type()
)
spingDataSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    spingDataSize.setStatus("mandatory")
_SpingWait_Type = TimeTicks
_SpingWait_Object = MibTableColumn
spingWait = _SpingWait_Object(
    (1, 3, 6, 1, 4, 1, 97, 3, 32, 2, 1, 6),
    _SpingWait_Type()
)
spingWait.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    spingWait.setStatus("mandatory")
_SpingTimeout_Type = TimeTicks
_SpingTimeout_Object = MibTableColumn
spingTimeout = _SpingTimeout_Object(
    (1, 3, 6, 1, 4, 1, 97, 3, 32, 2, 1, 7),
    _SpingTimeout_Type()
)
spingTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    spingTimeout.setStatus("mandatory")


class _SpingOperation_Type(Integer32):
    """Custom type spingOperation based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 1))
    )


_SpingOperation_Type.__name__ = "Integer32"
_SpingOperation_Object = MibTableColumn
spingOperation = _SpingOperation_Object(
    (1, 3, 6, 1, 4, 1, 97, 3, 32, 2, 1, 8),
    _SpingOperation_Type()
)
spingOperation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    spingOperation.setStatus("mandatory")
_SpingMin_Type = TimeTicks
_SpingMin_Object = MibTableColumn
spingMin = _SpingMin_Object(
    (1, 3, 6, 1, 4, 1, 97, 3, 32, 2, 1, 9),
    _SpingMin_Type()
)
spingMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    spingMin.setStatus("mandatory")
_SpingMax_Type = TimeTicks
_SpingMax_Object = MibTableColumn
spingMax = _SpingMax_Object(
    (1, 3, 6, 1, 4, 1, 97, 3, 32, 2, 1, 10),
    _SpingMax_Type()
)
spingMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    spingMax.setStatus("mandatory")
_SpingAvg_Type = TimeTicks
_SpingAvg_Object = MibTableColumn
spingAvg = _SpingAvg_Object(
    (1, 3, 6, 1, 4, 1, 97, 3, 32, 2, 1, 11),
    _SpingAvg_Type()
)
spingAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    spingAvg.setStatus("mandatory")
_SpingNumTransmitted_Type = Integer32
_SpingNumTransmitted_Object = MibTableColumn
spingNumTransmitted = _SpingNumTransmitted_Object(
    (1, 3, 6, 1, 4, 1, 97, 3, 32, 2, 1, 12),
    _SpingNumTransmitted_Type()
)
spingNumTransmitted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    spingNumTransmitted.setStatus("mandatory")
_SpingNumReceived_Type = Integer32
_SpingNumReceived_Object = MibTableColumn
spingNumReceived = _SpingNumReceived_Object(
    (1, 3, 6, 1, 4, 1, 97, 3, 32, 2, 1, 13),
    _SpingNumReceived_Type()
)
spingNumReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    spingNumReceived.setStatus("mandatory")
_Strace_ObjectIdentity = ObjectIdentity
strace = _Strace_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 97, 3, 33)
)
_StraceDataTimeout_Type = TimeTicks
_StraceDataTimeout_Object = MibScalar
straceDataTimeout = _StraceDataTimeout_Object(
    (1, 3, 6, 1, 4, 1, 97, 3, 33, 1),
    _StraceDataTimeout_Type()
)
straceDataTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    straceDataTimeout.setStatus("mandatory")
_StraceTable_Object = MibTable
straceTable = _StraceTable_Object(
    (1, 3, 6, 1, 4, 1, 97, 3, 33, 2)
)
if mibBuilder.loadTexts:
    straceTable.setStatus("mandatory")
_StraceEntry_Object = MibTableRow
straceEntry = _StraceEntry_Object(
    (1, 3, 6, 1, 4, 1, 97, 3, 33, 2, 1)
)
straceEntry.setIndexNames(
    (0, "CTATX-MIB", "straceNMSAddr"),
    (0, "CTATX-MIB", "straceDestAddr"),
    (0, "CTATX-MIB", "straceHop"),
    (0, "CTATX-MIB", "straceProbe"),
)
if mibBuilder.loadTexts:
    straceEntry.setStatus("mandatory")
_StraceNMSAddr_Type = IpAddress
_StraceNMSAddr_Object = MibTableColumn
straceNMSAddr = _StraceNMSAddr_Object(
    (1, 3, 6, 1, 4, 1, 97, 3, 33, 2, 1, 1),
    _StraceNMSAddr_Type()
)
straceNMSAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    straceNMSAddr.setStatus("mandatory")
_StraceDestAddr_Type = IpAddress
_StraceDestAddr_Object = MibTableColumn
straceDestAddr = _StraceDestAddr_Object(
    (1, 3, 6, 1, 4, 1, 97, 3, 33, 2, 1, 2),
    _StraceDestAddr_Type()
)
straceDestAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    straceDestAddr.setStatus("mandatory")
_StraceMaxTTL_Type = Integer32
_StraceMaxTTL_Object = MibTableColumn
straceMaxTTL = _StraceMaxTTL_Object(
    (1, 3, 6, 1, 4, 1, 97, 3, 33, 2, 1, 3),
    _StraceMaxTTL_Type()
)
straceMaxTTL.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    straceMaxTTL.setStatus("mandatory")
_StraceDataSize_Type = Integer32
_StraceDataSize_Object = MibTableColumn
straceDataSize = _StraceDataSize_Object(
    (1, 3, 6, 1, 4, 1, 97, 3, 33, 2, 1, 4),
    _StraceDataSize_Type()
)
straceDataSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    straceDataSize.setStatus("mandatory")
_StraceNumProbes_Type = Integer32
_StraceNumProbes_Object = MibTableColumn
straceNumProbes = _StraceNumProbes_Object(
    (1, 3, 6, 1, 4, 1, 97, 3, 33, 2, 1, 5),
    _StraceNumProbes_Type()
)
straceNumProbes.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    straceNumProbes.setStatus("mandatory")
_StraceWait_Type = TimeTicks
_StraceWait_Object = MibTableColumn
straceWait = _StraceWait_Object(
    (1, 3, 6, 1, 4, 1, 97, 3, 33, 2, 1, 6),
    _StraceWait_Type()
)
straceWait.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    straceWait.setStatus("mandatory")


class _StraceOperation_Type(Integer32):
    """Custom type straceOperation based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 1))
    )


_StraceOperation_Type.__name__ = "Integer32"
_StraceOperation_Object = MibTableColumn
straceOperation = _StraceOperation_Object(
    (1, 3, 6, 1, 4, 1, 97, 3, 33, 2, 1, 7),
    _StraceOperation_Type()
)
straceOperation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    straceOperation.setStatus("mandatory")
_StraceHop_Type = Integer32
_StraceHop_Object = MibTableColumn
straceHop = _StraceHop_Object(
    (1, 3, 6, 1, 4, 1, 97, 3, 33, 2, 1, 8),
    _StraceHop_Type()
)
straceHop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    straceHop.setStatus("mandatory")
_StraceHopAddress_Type = IpAddress
_StraceHopAddress_Object = MibTableColumn
straceHopAddress = _StraceHopAddress_Object(
    (1, 3, 6, 1, 4, 1, 97, 3, 33, 2, 1, 9),
    _StraceHopAddress_Type()
)
straceHopAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    straceHopAddress.setStatus("mandatory")
_StraceProbe_Type = Integer32
_StraceProbe_Object = MibTableColumn
straceProbe = _StraceProbe_Object(
    (1, 3, 6, 1, 4, 1, 97, 3, 33, 2, 1, 10),
    _StraceProbe_Type()
)
straceProbe.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    straceProbe.setStatus("mandatory")


class _StraceState_Type(Integer32):
    """Custom type straceState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("completed", 5),
          ("host-unreachable", 3),
          ("net-unreachable", 4),
          ("not-started", 0),
          ("time-exceeded", 2))
    )


_StraceState_Type.__name__ = "Integer32"
_StraceState_Object = MibTableColumn
straceState = _StraceState_Object(
    (1, 3, 6, 1, 4, 1, 97, 3, 33, 2, 1, 11),
    _StraceState_Type()
)
straceState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    straceState.setStatus("mandatory")
_StraceTime_Type = TimeTicks
_StraceTime_Object = MibTableColumn
straceTime = _StraceTime_Object(
    (1, 3, 6, 1, 4, 1, 97, 3, 33, 2, 1, 12),
    _StraceTime_Type()
)
straceTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    straceTime.setStatus("mandatory")
_Srtb_ObjectIdentity = ObjectIdentity
srtb = _Srtb_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 97, 3, 34)
)


class _SrtbProto_Type(Integer32):
    """Custom type srtbProto based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              7)
        )
    )
    namedValues = NamedValues(
        *(("all", 7),
          ("ip", 1),
          ("ipx", 2),
          ("off", 0),
          ("others", 3))
    )


_SrtbProto_Type.__name__ = "Integer32"
_SrtbProto_Object = MibScalar
srtbProto = _SrtbProto_Object(
    (1, 3, 6, 1, 4, 1, 97, 3, 34, 1),
    _SrtbProto_Type()
)
srtbProto.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    srtbProto.setStatus("mandatory")


class _SrtbExplorer_Type(Integer32):
    """Custom type srtbExplorer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("are", 1),
          ("ste", 2))
    )


_SrtbExplorer_Type.__name__ = "Integer32"
_SrtbExplorer_Object = MibScalar
srtbExplorer = _SrtbExplorer_Object(
    (1, 3, 6, 1, 4, 1, 97, 3, 34, 2),
    _SrtbExplorer_Type()
)
srtbExplorer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    srtbExplorer.setStatus("mandatory")
_SrtbAgingTime_Type = Integer32
_SrtbAgingTime_Object = MibScalar
srtbAgingTime = _SrtbAgingTime_Object(
    (1, 3, 6, 1, 4, 1, 97, 3, 34, 3),
    _SrtbAgingTime_Type()
)
srtbAgingTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    srtbAgingTime.setStatus("mandatory")
_Nbcache_ObjectIdentity = ObjectIdentity
nbcache = _Nbcache_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 97, 3, 35)
)
_NbCacheifTable_Object = MibTable
nbCacheifTable = _NbCacheifTable_Object(
    (1, 3, 6, 1, 4, 1, 97, 3, 35, 3)
)
if mibBuilder.loadTexts:
    nbCacheifTable.setStatus("mandatory")
_NbCacheifEntry_Object = MibTableRow
nbCacheifEntry = _NbCacheifEntry_Object(
    (1, 3, 6, 1, 4, 1, 97, 3, 35, 3, 1)
)
nbCacheifEntry.setIndexNames(
    (0, "CTATX-MIB", "nbCacheIfIndex"),
)
if mibBuilder.loadTexts:
    nbCacheifEntry.setStatus("mandatory")
_NbCacheIfIndex_Type = Integer32
_NbCacheIfIndex_Object = MibTableColumn
nbCacheIfIndex = _NbCacheIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 97, 3, 35, 3, 1, 1),
    _NbCacheIfIndex_Type()
)
nbCacheIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbCacheIfIndex.setStatus("mandatory")


class _NbCacheIfOperStatus_Type(Integer32):
    """Custom type nbCacheIfOperStatus based on Integer32"""
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


_NbCacheIfOperStatus_Type.__name__ = "Integer32"
_NbCacheIfOperStatus_Object = MibTableColumn
nbCacheIfOperStatus = _NbCacheIfOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 97, 3, 35, 3, 1, 2),
    _NbCacheIfOperStatus_Type()
)
nbCacheIfOperStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbCacheIfOperStatus.setStatus("mandatory")
_Atext_ObjectIdentity = ObjectIdentity
atext = _Atext_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 97, 6)
)
_Atextsystem_ObjectIdentity = ObjectIdentity
atextsystem = _Atextsystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 97, 6, 1)
)


class _AtextsysOperState_Type(Integer32):
    """Custom type atextsysOperState based on Integer32"""
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


_AtextsysOperState_Type.__name__ = "Integer32"
_AtextsysOperState_Object = MibScalar
atextsysOperState = _AtextsysOperState_Object(
    (1, 3, 6, 1, 4, 1, 97, 6, 1, 1),
    _AtextsysOperState_Type()
)
atextsysOperState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atextsysOperState.setStatus("mandatory")
_Atextport_ObjectIdentity = ObjectIdentity
atextport = _Atextport_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 97, 6, 2)
)
_AtextportTable_Object = MibTable
atextportTable = _AtextportTable_Object(
    (1, 3, 6, 1, 4, 1, 97, 6, 2, 1)
)
if mibBuilder.loadTexts:
    atextportTable.setStatus("mandatory")
_AtextportEntry_Object = MibTableRow
atextportEntry = _AtextportEntry_Object(
    (1, 3, 6, 1, 4, 1, 97, 6, 2, 1, 1)
)
atextportEntry.setIndexNames(
    (0, "CTATX-MIB", "atextportIndex"),
)
if mibBuilder.loadTexts:
    atextportEntry.setStatus("mandatory")
_AtextportIndex_Type = Integer32
_AtextportIndex_Object = MibTableColumn
atextportIndex = _AtextportIndex_Object(
    (1, 3, 6, 1, 4, 1, 97, 6, 2, 1, 1, 1),
    _AtextportIndex_Type()
)
atextportIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atextportIndex.setStatus("mandatory")
_AtextportNetStart_Type = OctetString
_AtextportNetStart_Object = MibTableColumn
atextportNetStart = _AtextportNetStart_Object(
    (1, 3, 6, 1, 4, 1, 97, 6, 2, 1, 1, 2),
    _AtextportNetStart_Type()
)
atextportNetStart.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atextportNetStart.setStatus("mandatory")
_AtextportNetEnd_Type = OctetString
_AtextportNetEnd_Object = MibTableColumn
atextportNetEnd = _AtextportNetEnd_Object(
    (1, 3, 6, 1, 4, 1, 97, 6, 2, 1, 1, 3),
    _AtextportNetEnd_Type()
)
atextportNetEnd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atextportNetEnd.setStatus("mandatory")
_AtextportNetAddress_Type = OctetString
_AtextportNetAddress_Object = MibTableColumn
atextportNetAddress = _AtextportNetAddress_Object(
    (1, 3, 6, 1, 4, 1, 97, 6, 2, 1, 1, 4),
    _AtextportNetAddress_Type()
)
atextportNetAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atextportNetAddress.setStatus("mandatory")
_AtextportZone_Type = OctetString
_AtextportZone_Object = MibTableColumn
atextportZone = _AtextportZone_Object(
    (1, 3, 6, 1, 4, 1, 97, 6, 2, 1, 1, 5),
    _AtextportZone_Type()
)
atextportZone.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atextportZone.setStatus("mandatory")
_AtextportzipTable_Object = MibTable
atextportzipTable = _AtextportzipTable_Object(
    (1, 3, 6, 1, 4, 1, 97, 6, 2, 2)
)
if mibBuilder.loadTexts:
    atextportzipTable.setStatus("mandatory")
_AtextportzipEntry_Object = MibTableRow
atextportzipEntry = _AtextportzipEntry_Object(
    (1, 3, 6, 1, 4, 1, 97, 6, 2, 2, 1)
)
atextportzipEntry.setIndexNames(
    (0, "CTATX-MIB", "atextportZonePort"),
    (0, "CTATX-MIB", "atextportZoneIndex"),
)
if mibBuilder.loadTexts:
    atextportzipEntry.setStatus("mandatory")
_AtextportZonePort_Type = Integer32
_AtextportZonePort_Object = MibTableColumn
atextportZonePort = _AtextportZonePort_Object(
    (1, 3, 6, 1, 4, 1, 97, 6, 2, 2, 1, 1),
    _AtextportZonePort_Type()
)
atextportZonePort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atextportZonePort.setStatus("mandatory")
_AtextportZoneIndex_Type = Integer32
_AtextportZoneIndex_Object = MibTableColumn
atextportZoneIndex = _AtextportZoneIndex_Object(
    (1, 3, 6, 1, 4, 1, 97, 6, 2, 2, 1, 2),
    _AtextportZoneIndex_Type()
)
atextportZoneIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atextportZoneIndex.setStatus("mandatory")
_AtextportZoneName_Type = OctetString
_AtextportZoneName_Object = MibTableColumn
atextportZoneName = _AtextportZoneName_Object(
    (1, 3, 6, 1, 4, 1, 97, 6, 2, 2, 1, 3),
    _AtextportZoneName_Type()
)
atextportZoneName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atextportZoneName.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CTATX-MIB",
    **{"Boolean": Boolean,
       "sigma": sigma,
       "sys": sys,
       "sysID": sysID,
       "sysReset": sysReset,
       "sysTrapAck": sysTrapAck,
       "sysTrapTime": sysTrapTime,
       "sysTrapRetry": sysTrapRetry,
       "sysTrapPort": sysTrapPort,
       "ecs-1": ecs_1,
       "hw": hw,
       "hwNumber": hwNumber,
       "hwSlotTable": hwSlotTable,
       "hwEntry": hwEntry,
       "hwIndex": hwIndex,
       "hwType": hwType,
       "hwUseMod": hwUseMod,
       "hwDefType": hwDefType,
       "hwDiagStatus": hwDiagStatus,
       "hwInuse": hwInuse,
       "hwDiagCode": hwDiagCode,
       "hwManufData": hwManufData,
       "hwPortType": hwPortType,
       "hwPortStatus": hwPortStatus,
       "hwUsePort": hwUsePort,
       "hwDefPortType": hwDefPortType,
       "hwAddr1": hwAddr1,
       "hwAddr2": hwAddr2,
       "hwAddr3": hwAddr3,
       "hwAddr4": hwAddr4,
       "hwTempOK": hwTempOK,
       "hwFirstPort": hwFirstPort,
       "hwFatalErr": hwFatalErr,
       "hwRptrPorts": hwRptrPorts,
       "hwPortSubType": hwPortSubType,
       "hwAddr5": hwAddr5,
       "hwAddr6": hwAddr6,
       "hwAddr7": hwAddr7,
       "hwAddr8": hwAddr8,
       "hwSysBus": hwSysBus,
       "hwPpeType": hwPpeType,
       "hwSysProcessor": hwSysProcessor,
       "sw": sw,
       "swNumber": swNumber,
       "swFilesetTable": swFilesetTable,
       "swFileset": swFileset,
       "swIndex": swIndex,
       "swDesc": swDesc,
       "swCount": swCount,
       "swTypes": swTypes,
       "swSizes": swSizes,
       "swStarts": swStarts,
       "swBases": swBases,
       "swFlashBank": swFlashBank,
       "admin": admin,
       "config": config,
       "configFatalErr": configFatalErr,
       "configAnyPass": configAnyPass,
       "configGetPass": configGetPass,
       "configNMSAddress": configNMSAddress,
       "configFunctions": configFunctions,
       "configPowerAc1": configPowerAc1,
       "configPowerAc2": configPowerAc2,
       "configPowerDc1": configPowerDc1,
       "configPowerDc2": configPowerDc2,
       "configPowerPresent1": configPowerPresent1,
       "configPowerPresent2": configPowerPresent2,
       "configAlarmDynamic": configAlarmDynamic,
       "configAlarmAddresses": configAlarmAddresses,
       "configStorageFailure": configStorageFailure,
       "configAuthenticationFailure": configAuthenticationFailure,
       "configFddiPriority": configFddiPriority,
       "configTprPriority": configTprPriority,
       "configDumpModule": configDumpModule,
       "configDumpStart": configDumpStart,
       "configDumpEnd": configDumpEnd,
       "lma": lma,
       "lmaAllAddr": lmaAllAddr,
       "lmaAnyAddr": lmaAnyAddr,
       "ppe": ppe,
       "ppeLrgUxRxCnt": ppeLrgUxRxCnt,
       "ppeSmlUxRxCnt": ppeSmlUxRxCnt,
       "ppeUxTxCnt": ppeUxTxCnt,
       "ppeSmlBuffSize": ppeSmlBuffSize,
       "ppeBridgingMemory": ppeBridgingMemory,
       "ppeExtendStats": ppeExtendStats,
       "ppeBAddrLimit": ppeBAddrLimit,
       "ppeTxCongests": ppeTxCongests,
       "ppeArpEntries": ppeArpEntries,
       "ppeArpStatics": ppeArpStatics,
       "ppeArpOverflows": ppeArpOverflows,
       "ppeIpEntries": ppeIpEntries,
       "ppeIpStatics": ppeIpStatics,
       "ppeStaticPreference": ppeStaticPreference,
       "ppeOspfPreference": ppeOspfPreference,
       "ppeRipPreference": ppeRipPreference,
       "ppeEgpPreference": ppeEgpPreference,
       "ppeCpuUtilization": ppeCpuUtilization,
       "ppeRipRouteDiscards": ppeRipRouteDiscards,
       "ppeOspfRouteDiscards": ppeOspfRouteDiscards,
       "ppeRouteMemorySize": ppeRouteMemorySize,
       "ppeRouteMemoryAvail": ppeRouteMemoryAvail,
       "ppeRouteMemoryFailures": ppeRouteMemoryFailures,
       "ppePacketMemorySize": ppePacketMemorySize,
       "ppePacketMemoryAvail": ppePacketMemoryAvail,
       "ppePacketMemoryFailures": ppePacketMemoryFailures,
       "ppeOspfPduMemoryFailures": ppeOspfPduMemoryFailures,
       "ppeOspfPduMemoryAllocs": ppeOspfPduMemoryAllocs,
       "ppeIcmpPduMemoryFailures": ppeIcmpPduMemoryFailures,
       "ppeIcmpPduMemoryAllocs": ppeIcmpPduMemoryAllocs,
       "ppeRipPduMemoryFailures": ppeRipPduMemoryFailures,
       "ppeRipPduMemoryAllocs": ppeRipPduMemoryAllocs,
       "ppeBootpPduMemoryFailures": ppeBootpPduMemoryFailures,
       "ppeBootpPduMemoryAllocs": ppeBootpPduMemoryAllocs,
       "ppeSnmpPduMemoryFailures": ppeSnmpPduMemoryFailures,
       "ppeSnmpPduMemoryAllocs": ppeSnmpPduMemoryAllocs,
       "ppeTftpPduMemoryFailures": ppeTftpPduMemoryFailures,
       "ppeTftpPduMemoryAllocs": ppeTftpPduMemoryAllocs,
       "ppeTraceroutePduMemoryFailures": ppeTraceroutePduMemoryFailures,
       "ppeTraceroutePduMemoryAllocs": ppeTraceroutePduMemoryAllocs,
       "ppeArpPduMemoryFailures": ppeArpPduMemoryFailures,
       "ppeArpPduMemoryAllocs": ppeArpPduMemoryAllocs,
       "ppeIgmpPduMemoryFailures": ppeIgmpPduMemoryFailures,
       "ppeIgmpPduMemoryAllocs": ppeIgmpPduMemoryAllocs,
       "ppeAresAsStes": ppeAresAsStes,
       "ppeRoutePercent": ppeRoutePercent,
       "ppeMgtMemorySize": ppeMgtMemorySize,
       "ppeMgtMemoryAvail": ppeMgtMemoryAvail,
       "ppeMgtMemoryFailures": ppeMgtMemoryFailures,
       "st": st,
       "stGroupAddr": stGroupAddr,
       "stResAddr": stResAddr,
       "stBridgeId": stBridgeId,
       "stRootMaxAge": stRootMaxAge,
       "stRootHello": stRootHello,
       "stRootDelay": stRootDelay,
       "stRootID": stRootID,
       "stRootCost": stRootCost,
       "stRootPort": stRootPort,
       "stTopChange": stTopChange,
       "stActMaxAge": stActMaxAge,
       "stActHello": stActHello,
       "stActDelay": stActDelay,
       "stTopChangeCount": stTopChangeCount,
       "stTopChangeTime": stTopChangeTime,
       "stAgeTime": stAgeTime,
       "mesh": mesh,
       "meshCostPercent": meshCostPercent,
       "meshCost": meshCost,
       "meshCostChange": meshCostChange,
       "meshCostChangeCount": meshCostChangeCount,
       "meshCostChangeTime": meshCostChangeTime,
       "meshSubnet": meshSubnet,
       "swdis": swdis,
       "swdisDesc": swdisDesc,
       "swdisAccess": swdisAccess,
       "swdisWriteStatus": swdisWriteStatus,
       "swdisConfigIp": swdisConfigIp,
       "swdisConfigRetryTime": swdisConfigRetryTime,
       "swdisConfigTotalTimeout": swdisConfigTotalTimeout,
       "addr": addr,
       "addrStatics": addrStatics,
       "addrDynamics": addrDynamics,
       "addrDynamicMax": addrDynamicMax,
       "addrMeshs": addrMeshs,
       "addrDynamicOverflows": addrDynamicOverflows,
       "addrMeshOverflows": addrMeshOverflows,
       "addrFlags": addrFlags,
       "addrMAC": addrMAC,
       "addrPort": addrPort,
       "addrPortMap": addrPortMap,
       "addrOperation": addrOperation,
       "addrIndex": addrIndex,
       "addrNext": addrNext,
       "addrAge": addrAge,
       "addrRxPkts": addrRxPkts,
       "addrRxChars": addrRxChars,
       "addrRxMultiPkts": addrRxMultiPkts,
       "addrRxFwdPkts": addrRxFwdPkts,
       "addrTxPkts": addrTxPkts,
       "addrTxChars": addrTxChars,
       "addrBlockSize": addrBlockSize,
       "addrBlock": addrBlock,
       "addrAlarmMAC": addrAlarmMAC,
       "addrRptrPort": addrRptrPort,
       "snmpsmt": snmpsmt,
       "snmpsmtUpstreamReq": snmpsmtUpstreamReq,
       "snmpsmtUpstreamRsp": snmpsmtUpstreamRsp,
       "snmpsmtUpstreamDescriptor": snmpsmtUpstreamDescriptor,
       "snmpsmtUpstreamState": snmpsmtUpstreamState,
       "fddismtTable": fddismtTable,
       "fddismtEntry": fddismtEntry,
       "fddismtIndex": fddismtIndex,
       "fddismtUpstreamReq": fddismtUpstreamReq,
       "fddismtUpstreamRsp": fddismtUpstreamRsp,
       "fddismtUpstreamDescriptor": fddismtUpstreamDescriptor,
       "fddismtUpstreamState": fddismtUpstreamState,
       "sinterfaces": sinterfaces,
       "sifUX": sifUX,
       "sifTable": sifTable,
       "sifEntry": sifEntry,
       "sifIndex": sifIndex,
       "sifSmlRxCnt": sifSmlRxCnt,
       "sifLrgRxCnt": sifLrgRxCnt,
       "sifUxTxCnt": sifUxTxCnt,
       "sifThreshold": sifThreshold,
       "sifThresholdTime": sifThresholdTime,
       "sifRxQueueThresh": sifRxQueueThresh,
       "sifRxQueueThreshTime": sifRxQueueThreshTime,
       "sifTxStormCnt": sifTxStormCnt,
       "sifTxStormTime": sifTxStormTime,
       "sifFilterFlags": sifFilterFlags,
       "sifCongestTime": sifCongestTime,
       "sifQueueTime": sifQueueTime,
       "sifPortCost": sifPortCost,
       "sifStPriority": sifStPriority,
       "sifFunctions": sifFunctions,
       "sifCongested": sifCongested,
       "sifState": sifState,
       "sifDesigCost": sifDesigCost,
       "sifDesigRoot": sifDesigRoot,
       "sifDesigBridge": sifDesigBridge,
       "sifDesigPort": sifDesigPort,
       "sifRxPackets": sifRxPackets,
       "sifRxChar0s": sifRxChar0s,
       "sifRxChar1s": sifRxChar1s,
       "sifRxSizeErrors": sifRxSizeErrors,
       "sifRxHwFCSs": sifRxHwFCSs,
       "sifRxQueues": sifRxQueues,
       "sifTxPackets": sifTxPackets,
       "sifTxCongests": sifTxCongests,
       "sifTxStorms": sifTxStorms,
       "sifTxDests": sifTxDests,
       "sifErrorsFlag": sifErrorsFlag,
       "sifTxStormFlag": sifTxStormFlag,
       "sifTxSizes": sifTxSizes,
       "sifTxAddr": sifTxAddr,
       "sifLan": sifLan,
       "sifStatisticsTime": sifStatisticsTime,
       "sifIpAddress": sifIpAddress,
       "sifIpGroupAddress": sifIpGroupAddress,
       "sifMaxPacketSize": sifMaxPacketSize,
       "sifExpectSqe": sifExpectSqe,
       "sifFilterLocal": sifFilterLocal,
       "sifInQLen": sifInQLen,
       "sifFrameSwitching": sifFrameSwitching,
       "sifRingDrops": sifRingDrops,
       "sifAdapterChecks": sifAdapterChecks,
       "sifIpRipPortMetric": sifIpRipPortMetric,
       "sifDescr": sifDescr,
       "sifUtilInterval": sifUtilInterval,
       "sifUtilCount": sifUtilCount,
       "sifUtilPortPeakReset": sifUtilPortPeakReset,
       "sifUtilPortPeakTable": sifUtilPortPeakTable,
       "sifUtilPortPeakEntry": sifUtilPortPeakEntry,
       "sifUtilPortPeakIndex": sifUtilPortPeakIndex,
       "sifUtilPortPeakOrdinal": sifUtilPortPeakOrdinal,
       "sifUtilPortPeakBRTimestamp": sifUtilPortPeakBRTimestamp,
       "sifUtilPortPeakTBitRate": sifUtilPortPeakTBitRate,
       "sifUtilPortPeakRBitRate": sifUtilPortPeakRBitRate,
       "sifUtilSysPeakReset": sifUtilSysPeakReset,
       "sifUtilSysPeakTable": sifUtilSysPeakTable,
       "sifUtilSysPeakEntry": sifUtilSysPeakEntry,
       "sifUtilSysPeakIndex": sifUtilSysPeakIndex,
       "sifUtilSysPeakOrdinal": sifUtilSysPeakOrdinal,
       "sifUtilSysPeakTimestamp": sifUtilSysPeakTimestamp,
       "sifUtilSysPeakTBitRate": sifUtilSysPeakTBitRate,
       "sifUtilSysPeakRBitRate": sifUtilSysPeakRBitRate,
       "sfddi": sfddi,
       "sfddiTable": sfddiTable,
       "sfddiEntry": sfddiEntry,
       "sfddiIndex": sfddiIndex,
       "sfddiRxHwAborts": sfddiRxHwAborts,
       "sfddiRxParitys": sfddiRxParitys,
       "sfddiRxShorts": sfddiRxShorts,
       "sfddiDpcErrCnts": sfddiDpcErrCnts,
       "sfddiDpcErrValue": sfddiDpcErrValue,
       "sfddiRbcErrCnts": sfddiRbcErrCnts,
       "sfddiRbcErrValue": sfddiRbcErrValue,
       "sfddiTxAsync": sfddiTxAsync,
       "sfddiShortAddressing": sfddiShortAddressing,
       "sfddiSmtConditions": sfddiSmtConditions,
       "sfddiSrfConditions": sfddiSrfConditions,
       "sfddiSmtConditionsStatus": sfddiSmtConditionsStatus,
       "sfddiSrfConditionsStatus": sfddiSrfConditionsStatus,
       "sfddiSrfReportLimit": sfddiSrfReportLimit,
       "sfddiFrameErrorThreshold": sfddiFrameErrorThreshold,
       "sfddiNotCopiedThreshold": sfddiNotCopiedThreshold,
       "sfddiSBFlag": sfddiSBFlag,
       "sfddiRxEbits": sfddiRxEbits,
       "sfddiOBSFuseBad": sfddiOBSFuseBad,
       "sfddiThruB": sfddiThruB,
       "sfddiStationDescriptor": sfddiStationDescriptor,
       "sfddiStationState": sfddiStationState,
       "sfddiDownstreamNbr": sfddiDownstreamNbr,
       "sfddiSMTBufferSize": sfddiSMTBufferSize,
       "suart": suart,
       "suartTable": suartTable,
       "suartEntry": suartEntry,
       "suartIndex": suartIndex,
       "suartBaud": suartBaud,
       "suartModem": suartModem,
       "suartIpNeighborAddress": suartIpNeighborAddress,
       "suartPPPActive": suartPPPActive,
       "suartAlignmentErrors": suartAlignmentErrors,
       "suartOverrunErrors": suartOverrunErrors,
       "filter": filter,
       "filterMaxCount": filterMaxCount,
       "filterCurrentCount": filterCurrentCount,
       "filterDeleteID": filterDeleteID,
       "filterNextID": filterNextID,
       "filterAddID": filterAddID,
       "filterAddIndex": filterAddIndex,
       "filterTable": filterTable,
       "filterEntry": filterEntry,
       "filterIndex": filterIndex,
       "filterID": filterID,
       "filterPortNo": filterPortNo,
       "filterComboType": filterComboType,
       "filterFlags": filterFlags,
       "filterFrame": filterFrame,
       "filterSource": filterSource,
       "filterSourceEnd": filterSourceEnd,
       "filterDest": filterDest,
       "filterDestEnd": filterDestEnd,
       "filterSourceMask": filterSourceMask,
       "filterDestMask": filterDestMask,
       "filterSrcLan": filterSrcLan,
       "filterOffset": filterOffset,
       "filterField": filterField,
       "filterMask": filterMask,
       "filterThreshold": filterThreshold,
       "filterThreshTime": filterThreshTime,
       "filterThreshFlag": filterThreshFlag,
       "filterPktCnts": filterPktCnts,
       "filterLastSrc": filterLastSrc,
       "reboot": reboot,
       "rebootBridgingMemory": rebootBridgingMemory,
       "rebootSlotTable": rebootSlotTable,
       "rebootEntry": rebootEntry,
       "rebootIndex": rebootIndex,
       "rebootType": rebootType,
       "rebootUseMod": rebootUseMod,
       "rebootPortType": rebootPortType,
       "rebootConfig": rebootConfig,
       "rebootRouteMemory": rebootRouteMemory,
       "debug": debug,
       "debugStringID": debugStringID,
       "debugString": debugString,
       "debugTable": debugTable,
       "debugEntry": debugEntry,
       "debugIndex": debugIndex,
       "debugOperation": debugOperation,
       "debugBase": debugBase,
       "debugLength": debugLength,
       "debugData": debugData,
       "lpbk": lpbk,
       "lpbkTable": lpbkTable,
       "lpbkEntry": lpbkEntry,
       "lpbkIndex": lpbkIndex,
       "lpbkOperation": lpbkOperation,
       "lpbkDestAddr": lpbkDestAddr,
       "lpbkPktNum": lpbkPktNum,
       "lpbkInterval": lpbkInterval,
       "lpbkPktLength": lpbkPktLength,
       "lpbkIncrements": lpbkIncrements,
       "lpbkGoods": lpbkGoods,
       "lpbkErrorNoReceives": lpbkErrorNoReceives,
       "lpbkErrorBadReceives": lpbkErrorBadReceives,
       "lpbkErrorSize": lpbkErrorSize,
       "lpbkErrorSent": lpbkErrorSent,
       "lpbkErrorReceived": lpbkErrorReceived,
       "lpbkErrorOffset": lpbkErrorOffset,
       "swan": swan,
       "swanTable": swanTable,
       "swanEntry": swanEntry,
       "swanIndex": swanIndex,
       "swanDesiredSpeed": swanDesiredSpeed,
       "swanActualSpeed": swanActualSpeed,
       "swanIpNeighborAddress": swanIpNeighborAddress,
       "swanPPPActive": swanPPPActive,
       "swanAlignmentErrors": swanAlignmentErrors,
       "swanOverrunErrors": swanOverrunErrors,
       "swanPortType": swanPortType,
       "swanLinkCost": swanLinkCost,
       "swanMeshState": swanMeshState,
       "swanLinkSubnet": swanLinkSubnet,
       "swanLinkBridge": swanLinkBridge,
       "swanLinkPort": swanLinkPort,
       "swanNegotiate": swanNegotiate,
       "swanSwitches": swanSwitches,
       "swanDCEDrops": swanDCEDrops,
       "swanOutPacketType": swanOutPacketType,
       "swanLinkErrorPercentage": swanLinkErrorPercentage,
       "swanLinkErrorDuration": swanLinkErrorDuration,
       "swanLinkErrorFailPeriods": swanLinkErrorFailPeriods,
       "swanLinkErrorMaxPeriods": swanLinkErrorMaxPeriods,
       "swanLinkRestartTime": swanLinkRestartTime,
       "swanPreserveFCS": swanPreserveFCS,
       "srepeater": srepeater,
       "srepeaterTable": srepeaterTable,
       "srepeaterEntry": srepeaterEntry,
       "srepeaterGroupID": srepeaterGroupID,
       "srepeaterLinkStatusMask": srepeaterLinkStatusMask,
       "srepeaterExtendedStats": srepeaterExtendedStats,
       "srepeaterPortTable": srepeaterPortTable,
       "srepeaterPortEntry": srepeaterPortEntry,
       "srepeaterPortGroupID": srepeaterPortGroupID,
       "srepeaterPortPortID": srepeaterPortPortID,
       "srepeaterPortLinkPulse": srepeaterPortLinkPulse,
       "sproto": sproto,
       "sprotoTable": sprotoTable,
       "sprotoEntry": sprotoEntry,
       "sprotoIfIndex": sprotoIfIndex,
       "sprotoBridge": sprotoBridge,
       "sprotoSuppressBpdus": sprotoSuppressBpdus,
       "sprotoIpRoute": sprotoIpRoute,
       "sprotoIpxRoute": sprotoIpxRoute,
       "sprotoAppleRoute": sprotoAppleRoute,
       "sprotoArpTranslate": sprotoArpTranslate,
       "sprotoArpSourceRoute": sprotoArpSourceRoute,
       "sprotoIpxTranslate": sprotoIpxTranslate,
       "sprotoAppleTranslate": sprotoAppleTranslate,
       "sprotoIbmLlcTranslate": sprotoIbmLlcTranslate,
       "sprotoRip": sprotoRip,
       "sprotoEgp": sprotoEgp,
       "sprotoOspf": sprotoOspf,
       "sprotoArpProxy": sprotoArpProxy,
       "sprotoIbm8209Lsaps": sprotoIbm8209Lsaps,
       "sprotoBootpRelay": sprotoBootpRelay,
       "sprotoNetbiosTranslate": sprotoNetbiosTranslate,
       "sprotoIpMulticast": sprotoIpMulticast,
       "sprotoTrunking": sprotoTrunking,
       "sprotoIpxSrTranslate": sprotoIpxSrTranslate,
       "sprotoAllTranslate": sprotoAllTranslate,
       "sprotoSteHopCountAppliedRule": sprotoSteHopCountAppliedRule,
       "sprotoIpxDot3Framing": sprotoIpxDot3Framing,
       "sipx": sipx,
       "sipxIfTable": sipxIfTable,
       "sipxIfEntry": sipxIfEntry,
       "sipxIfIndex": sipxIfIndex,
       "sipxIfNetwork": sipxIfNetwork,
       "sipxIfFraming": sipxIfFraming,
       "sipxIfInRipPkts": sipxIfInRipPkts,
       "sipxIfOutRipPkts": sipxIfOutRipPkts,
       "sipxIfInSapPkts": sipxIfInSapPkts,
       "sipxIfOutSapPkts": sipxIfOutSapPkts,
       "sipxRouteTable": sipxRouteTable,
       "sipxRouteEntry": sipxRouteEntry,
       "sipxRouteDest": sipxRouteDest,
       "sipxRouteIfIndex": sipxRouteIfIndex,
       "sipxRouteTickCount": sipxRouteTickCount,
       "sipxRouteHopCount": sipxRouteHopCount,
       "sipxRouteNextHop": sipxRouteNextHop,
       "sipxRouteAge": sipxRouteAge,
       "sipxSapTable": sipxSapTable,
       "sipxSapEntry": sipxSapEntry,
       "sipxSapIndex": sipxSapIndex,
       "sipxSapType": sipxSapType,
       "sipxSapName": sipxSapName,
       "sipxSapNetwork": sipxSapNetwork,
       "sipxSapNodeId": sipxSapNodeId,
       "sipxSapSocket": sipxSapSocket,
       "sipxSapHopCount": sipxSapHopCount,
       "sipxDiscardedRoutes": sipxDiscardedRoutes,
       "sipxDiscardedServices": sipxDiscardedServices,
       "sipxsfGrp": sipxsfGrp,
       "sipxsfNextIndex": sipxsfNextIndex,
       "sipxsfTable": sipxsfTable,
       "sipxsfEntry": sipxsfEntry,
       "sipxsfIndex": sipxsfIndex,
       "sipxsfSAPName": sipxsfSAPName,
       "sipxsfSAPType": sipxsfSAPType,
       "sipxsfAccessMode": sipxsfAccessMode,
       "sipxsfFilterType": sipxsfFilterType,
       "sipxsfPortMap": sipxsfPortMap,
       "sipxsfNetworks": sipxsfNetworks,
       "sipxsfFiltered": sipxsfFiltered,
       "sipxsrGrp": sipxsrGrp,
       "sipxsrAgingTime": sipxsrAgingTime,
       "sipxsrExplorerTable": sipxsrExplorerTable,
       "sipxsrExplorerEntry": sipxsrExplorerEntry,
       "sipxsrPort": sipxsrPort,
       "sipxsrStatus": sipxsrStatus,
       "sipxsrExplorerType": sipxsrExplorerType,
       "srtrdisc": srtrdisc,
       "srtrdiscTable": srtrdiscTable,
       "srtrdiscEntry": srtrdiscEntry,
       "srtrdiscIfIndex": srtrdiscIfIndex,
       "srtrdiscState": srtrdiscState,
       "srtrdiscAdvertisementAddress": srtrdiscAdvertisementAddress,
       "srtrdiscAdvertisementInterval": srtrdiscAdvertisementInterval,
       "srtrdiscLifetime": srtrdiscLifetime,
       "srtrdiscPreference": srtrdiscPreference,
       "sipm": sipm,
       "sipmroute": sipmroute,
       "sipmRouteTable": sipmRouteTable,
       "sipmRouteEntry": sipmRouteEntry,
       "sipmRouteOrigin": sipmRouteOrigin,
       "sipmRouteOriginMask": sipmRouteOriginMask,
       "sipmRouteGateway": sipmRouteGateway,
       "sipmRouteMetric": sipmRouteMetric,
       "sipmRouteAge": sipmRouteAge,
       "sipmRouteParents": sipmRouteParents,
       "sipmgroup": sipmgroup,
       "sipmneighbor": sipmneighbor,
       "sipmNeighborTable": sipmNeighborTable,
       "sipmNeighborEntry": sipmNeighborEntry,
       "sipmNeighborIfIndex": sipmNeighborIfIndex,
       "sipmNeighbors": sipmNeighbors,
       "sipmNeighborLastHeard": sipmNeighborLastHeard,
       "sipmstat": sipmstat,
       "sipmOutOfMemory": sipmOutOfMemory,
       "sipmStatTable": sipmStatTable,
       "sipmStatEntry": sipmStatEntry,
       "sipmStatIfIndex": sipmStatIfIndex,
       "sipmInBadPackets": sipmInBadPackets,
       "sipmCacheMiss": sipmCacheMiss,
       "sipckt": sipckt,
       "sipcktTable": sipcktTable,
       "sipcktEntry": sipcktEntry,
       "sipcktIndex": sipcktIndex,
       "sipcktIpAddress": sipcktIpAddress,
       "sipcktState": sipcktState,
       "sipcktNetMask": sipcktNetMask,
       "sipcktSourceRoute": sipcktSourceRoute,
       "sipNetToMediaTable": sipNetToMediaTable,
       "sipNetToMediaEntry": sipNetToMediaEntry,
       "sipNetToMediaIfIndex": sipNetToMediaIfIndex,
       "sipNetToMediaNetAddress": sipNetToMediaNetAddress,
       "sipNetToMediaSourceRoute": sipNetToMediaSourceRoute,
       "sipNetToMediaAge": sipNetToMediaAge,
       "ssecure": ssecure,
       "profileTable": profileTable,
       "profileEntry": profileEntry,
       "profileIndex": profileIndex,
       "profileSourceStart": profileSourceStart,
       "profileSourceEnd": profileSourceEnd,
       "profileDestStart": profileDestStart,
       "profileDestEnd": profileDestEnd,
       "profileType": profileType,
       "ruleTable": ruleTable,
       "ruleEntry": ruleEntry,
       "ruleIndex": ruleIndex,
       "ruleSourceIp": ruleSourceIp,
       "ruleDestIp": ruleDestIp,
       "ruleSourceIpMask": ruleSourceIpMask,
       "ruleDestIpMask": ruleDestIpMask,
       "ruleType": ruleType,
       "ruleUdpProfile": ruleUdpProfile,
       "ruleTcpProfile": ruleTcpProfile,
       "ruleTcpEstProfile": ruleTcpEstProfile,
       "ruleFilterUdpFragment": ruleFilterUdpFragment,
       "ruleFilterTcpFragment": ruleFilterTcpFragment,
       "ruleFilterIpOption": ruleFilterIpOption,
       "ruleAllowIcmp": ruleAllowIcmp,
       "ruleAllowIpWithinIp": ruleAllowIpWithinIp,
       "ruleAllowEgp": ruleAllowEgp,
       "ruleAllowIgp": ruleAllowIgp,
       "ruleAllowIgrp": ruleAllowIgrp,
       "ruleAllowOspf": ruleAllowOspf,
       "ruleAllowAnyOther": ruleAllowAnyOther,
       "spvc": spvc,
       "spvcTable": spvcTable,
       "spvcEntry": spvcEntry,
       "spvcIfIndex": spvcIfIndex,
       "spvcPathRX": spvcPathRX,
       "spvcCircuitRX": spvcCircuitRX,
       "spvcPathTX": spvcPathTX,
       "spvcCircuitTX": spvcCircuitTX,
       "spvcState": spvcState,
       "spvcPhysPort": spvcPhysPort,
       "spvcMinPort": spvcMinPort,
       "spvcMaxPort": spvcMaxPort,
       "strunk": strunk,
       "strunkTable": strunkTable,
       "strunkEntry": strunkEntry,
       "strunkIfIndex": strunkIfIndex,
       "strunkState": strunkState,
       "strunkRemoteBridgeAddr": strunkRemoteBridgeAddr,
       "strunkRemoteIp": strunkRemoteIp,
       "strunkLastError": strunkLastError,
       "strunkLinkOrdinal": strunkLinkOrdinal,
       "strunkLinkCount": strunkLinkCount,
       "strunkLastChange": strunkLastChange,
       "ipMRouteMIB": ipMRouteMIB,
       "ipMRouteMIBObjects": ipMRouteMIBObjects,
       "ipMRoute": ipMRoute,
       "ipMRouteEnable": ipMRouteEnable,
       "ipMRouteTable": ipMRouteTable,
       "ipMRouteEntry": ipMRouteEntry,
       "ipMRouteGroup": ipMRouteGroup,
       "ipMRouteSource": ipMRouteSource,
       "ipMRouteSourceMask": ipMRouteSourceMask,
       "ipMRouteRpfNeighbor": ipMRouteRpfNeighbor,
       "ipMRouteInIfIndex": ipMRouteInIfIndex,
       "ipMRouteOutList": ipMRouteOutList,
       "ipMRouteUpTime": ipMRouteUpTime,
       "ipMRouteExpiryTime": ipMRouteExpiryTime,
       "ipMRoutePkts": ipMRoutePkts,
       "ipMRouteRpfFails": ipMRouteRpfFails,
       "ipMRouteOctets": ipMRouteOctets,
       "ipMRouteNextHopState": ipMRouteNextHopState,
       "ipMRouteInterfaceTable": ipMRouteInterfaceTable,
       "ipMRouteInterfaceEntry": ipMRouteInterfaceEntry,
       "ipMRouteInterfaceIfIndex": ipMRouteInterfaceIfIndex,
       "ipMRouteInterfaceTtl": ipMRouteInterfaceTtl,
       "igmpMIB": igmpMIB,
       "igmpMIBObjects": igmpMIBObjects,
       "igmp": igmp,
       "igmpInterfaceTable": igmpInterfaceTable,
       "igmpInterfaceEntry": igmpInterfaceEntry,
       "igmpInterfaceIfIndex": igmpInterfaceIfIndex,
       "igmpInterfaceQueryInterval": igmpInterfaceQueryInterval,
       "igmpInterfaceStatus": igmpInterfaceStatus,
       "igmpCacheTable": igmpCacheTable,
       "igmpCacheEntry": igmpCacheEntry,
       "igmpCacheAddress": igmpCacheAddress,
       "igmpCacheIfIndex": igmpCacheIfIndex,
       "igmpCacheSelf": igmpCacheSelf,
       "igmpCacheLastReporter": igmpCacheLastReporter,
       "igmpCacheUpTime": igmpCacheUpTime,
       "igmpCacheExpiryTime": igmpCacheExpiryTime,
       "igmpCacheStatus": igmpCacheStatus,
       "slog": slog,
       "slogFilter": slogFilter,
       "slogTrap": slogTrap,
       "slogOverwrite": slogOverwrite,
       "slogEntryNumber": slogEntryNumber,
       "slogEntryTable": slogEntryTable,
       "slogEntry": slogEntry,
       "slogIndex": slogIndex,
       "slogEntryTimeStamp": slogEntryTimeStamp,
       "slogEntryMessageText": slogEntryMessageText,
       "slogEntryName": slogEntryName,
       "strap": strap,
       "strapControlTable": strapControlTable,
       "strapControl": strapControl,
       "strapIndex": strapIndex,
       "strapEnabled": strapEnabled,
       "strapSeverity": strapSeverity,
       "strapText": strapText,
       "strapSeverityControlTable": strapSeverityControlTable,
       "strapSeverityControl": strapSeverityControl,
       "strapSeveritySeverity": strapSeveritySeverity,
       "strapSeverityEnable": strapSeverityEnable,
       "strapIncludeText": strapIncludeText,
       "strapTime": strapTime,
       "strapRetry": strapRetry,
       "strapEntryNumber": strapEntryNumber,
       "strapTable": strapTable,
       "strapEntry": strapEntry,
       "strapEntryIndex": strapEntryIndex,
       "strapEntryTimeStamp": strapEntryTimeStamp,
       "strapEntryText": strapEntryText,
       "strapNumber": strapNumber,
       "strapEntrySeverity": strapEntrySeverity,
       "smirror": smirror,
       "smirrorStatus": smirrorStatus,
       "smirrorDiagPort": smirrorDiagPort,
       "smirrorIPaddr": smirrorIPaddr,
       "smirrorTargetPortLists": smirrorTargetPortLists,
       "smirrorOversizePkt": smirrorOversizePkt,
       "smirrorEntryMirroredPkts": smirrorEntryMirroredPkts,
       "smirrorExitMirroredPkts": smirrorExitMirroredPkts,
       "smirrorNotreadyDroppedPkts": smirrorNotreadyDroppedPkts,
       "smirrorOversizeDroppedPkts": smirrorOversizeDroppedPkts,
       "smirrorEntryFilteredPkts": smirrorEntryFilteredPkts,
       "smirrorExitFilteredPkts": smirrorExitFilteredPkts,
       "smirrorCongestionDroppedPkts": smirrorCongestionDroppedPkts,
       "smirrorNowrapperDroppedPkts": smirrorNowrapperDroppedPkts,
       "smirrorRemoteStatus": smirrorRemoteStatus,
       "smirrorRemoteExitPort": smirrorRemoteExitPort,
       "sworkgroup": sworkgroup,
       "sWorkGroupNextNumber": sWorkGroupNextNumber,
       "sWorkGroupCurrentCount": sWorkGroupCurrentCount,
       "sWorkGroupMaxCount": sWorkGroupMaxCount,
       "sWorkGroupTable": sWorkGroupTable,
       "sWorkGroupEntry": sWorkGroupEntry,
       "sWorkGroupNumber": sWorkGroupNumber,
       "sWorkGroupName": sWorkGroupName,
       "sWorkGroupPorts": sWorkGroupPorts,
       "sWorkGroupType": sWorkGroupType,
       "sWorkGroupIpAddress": sWorkGroupIpAddress,
       "sWorkGroupIpMask": sWorkGroupIpMask,
       "sWorkGroupIpxNetwork": sWorkGroupIpxNetwork,
       "sping": sping,
       "spingDataTimeout": spingDataTimeout,
       "spingTable": spingTable,
       "spingEntry": spingEntry,
       "spingNMSAddr": spingNMSAddr,
       "spingDestAddr": spingDestAddr,
       "spingState": spingState,
       "spingCount": spingCount,
       "spingDataSize": spingDataSize,
       "spingWait": spingWait,
       "spingTimeout": spingTimeout,
       "spingOperation": spingOperation,
       "spingMin": spingMin,
       "spingMax": spingMax,
       "spingAvg": spingAvg,
       "spingNumTransmitted": spingNumTransmitted,
       "spingNumReceived": spingNumReceived,
       "strace": strace,
       "straceDataTimeout": straceDataTimeout,
       "straceTable": straceTable,
       "straceEntry": straceEntry,
       "straceNMSAddr": straceNMSAddr,
       "straceDestAddr": straceDestAddr,
       "straceMaxTTL": straceMaxTTL,
       "straceDataSize": straceDataSize,
       "straceNumProbes": straceNumProbes,
       "straceWait": straceWait,
       "straceOperation": straceOperation,
       "straceHop": straceHop,
       "straceHopAddress": straceHopAddress,
       "straceProbe": straceProbe,
       "straceState": straceState,
       "straceTime": straceTime,
       "srtb": srtb,
       "srtbProto": srtbProto,
       "srtbExplorer": srtbExplorer,
       "srtbAgingTime": srtbAgingTime,
       "nbcache": nbcache,
       "nbCacheifTable": nbCacheifTable,
       "nbCacheifEntry": nbCacheifEntry,
       "nbCacheIfIndex": nbCacheIfIndex,
       "nbCacheIfOperStatus": nbCacheIfOperStatus,
       "atext": atext,
       "atextsystem": atextsystem,
       "atextsysOperState": atextsysOperState,
       "atextport": atextport,
       "atextportTable": atextportTable,
       "atextportEntry": atextportEntry,
       "atextportIndex": atextportIndex,
       "atextportNetStart": atextportNetStart,
       "atextportNetEnd": atextportNetEnd,
       "atextportNetAddress": atextportNetAddress,
       "atextportZone": atextportZone,
       "atextportzipTable": atextportzipTable,
       "atextportzipEntry": atextportzipEntry,
       "atextportZonePort": atextportZonePort,
       "atextportZoneIndex": atextportZoneIndex,
       "atextportZoneName": atextportZoneName}
)
