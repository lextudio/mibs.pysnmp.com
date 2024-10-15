# SNMP MIB module (ES-1000-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ES-1000-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:40:39 2024
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



class TruthValue(Integer32):
    """Custom type TruthValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )





class Es1000SysOperStatus(Integer32):
    """Custom type Es1000SysOperStatus based on Integer32"""
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
        *(("major-failure", 4),
          ("minor-failure", 3),
          ("not-operational", 5),
          ("operational", 1),
          ("redundant-failure", 2))
    )





class Es1000SysState(Integer32):
    """Custom type Es1000SysState based on Integer32"""
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
        *(("coming-online", 2),
          ("going-offline", 4),
          ("offline", 3),
          ("online", 1))
    )





class Es1000CompCode(Integer32):
    """Custom type Es1000CompCode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              5,
              6,
              13,
              16,
              17,
              18,
              19,
              20,
              21,
              22,
              23)
        )
    )
    namedValues = NamedValues(
        *(("comp-ctp", 2),
          ("comp-fan", 5),
          ("comp-gbic-cu-db9", 17),
          ("comp-gbic-cu-hssdc", 18),
          ("comp-gbic-none", 16),
          ("comp-gbic-opt-lw-1g", 19),
          ("comp-gbic-opt-lw-2g", 22),
          ("comp-gbic-opt-sw-1g", 21),
          ("comp-gbic-opt-sw-2g", 23),
          ("comp-gbic-serial-id", 20),
          ("comp-power", 6),
          ("comp-thermal", 13))
    )





class Es1000CompPosition(Integer32):
    """Custom type Es1000CompPosition based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 9),
    )





class Es1000CompStatus(Integer32):
    """Custom type Es1000CompStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("failed", 3),
          ("update-busy", 2))
    )





class Es1000PortCount(Integer32):
    """Custom type Es1000PortCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 9),
    )





class Es1000PortIndex(Integer32):
    """Custom type Es1000PortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 9),
    )





class Es1000PortNumber(Integer32):
    """Custom type Es1000PortNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8),
    )





class Es1000PortPhyState(Integer32):
    """Custom type Es1000PortPhyState based on Integer32"""
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
              12,
              13,
              14,
              15,
              16,
              17,
              18,
              19,
              20,
              21,
              22,
              23,
              24,
              25)
        )
    )
    namedValues = NamedValues(
        *(("psAvailable", 2),
          ("psBBCredit", 24),
          ("psBlocked", 3),
          ("psExtLoop", 8),
          ("psFatalError", 25),
          ("psIntDiags", 7),
          ("psLR", 11),
          ("psLinkFailLOL", 6),
          ("psLinkFailLOSignal", 17),
          ("psLinkFailLOSync", 16),
          ("psLinkFailure", 5),
          ("psNotInstalled", 1),
          ("psPortBypassedCRCError", 15),
          ("psPortBypassedLipF7", 12),
          ("psPortBypassedLipF8", 13),
          ("psPortBypassedOSError", 14),
          ("psPortFail", 9),
          ("psProtocolError", 20),
          ("psRxLR", 23),
          ("psRxNOS", 22),
          ("psRxOLS", 21),
          ("psSR", 10),
          ("psTimeout", 19),
          ("psTxFault", 18),
          ("psUnavailable", 4))
    )





class Es1000PortStatus(Integer32):
    """Custom type Es1000PortStatus based on Integer32"""
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
        *(("faulty", 4),
          ("offline", 2),
          ("online", 1),
          ("testing", 3))
    )





class Es1000PortAdmStatus(Integer32):
    """Custom type Es1000PortAdmStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("offline", 2),
          ("online", 1),
          ("testing", 3))
    )





class Es1000LoopStatus(Integer32):
    """Custom type Es1000LoopStatus based on Integer32"""
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
        *(("loop-ACTIVE", 11),
          ("loop-DOWN", 1),
          ("loop-FAN", 10),
          ("loop-LIFA", 4),
          ("loop-LIHA", 6),
          ("loop-LILP", 9),
          ("loop-LIP", 2),
          ("loop-LIPA", 5),
          ("loop-LIRP", 8),
          ("loop-LISA", 7),
          ("loop-LISM", 3),
          ("loop-READY", 12))
    )





class Es1000LoopMasterWWN(OctetString):
    """Custom type Es1000LoopMasterWWN based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )





class Es1000LoopPortALPA(OctetString):
    """Custom type Es1000LoopPortALPA based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 126),
    )




# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_McData_ObjectIdentity = ObjectIdentity
mcData = _McData_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 289)
)
_CommDev_ObjectIdentity = ObjectIdentity
commDev = _CommDev_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 289, 2)
)
_FibreChannel_ObjectIdentity = ObjectIdentity
fibreChannel = _FibreChannel_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 289, 2, 1)
)
_FcSwitch_ObjectIdentity = ObjectIdentity
fcSwitch = _FcSwitch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 289, 2, 1, 1)
)
_Es_1000_ObjectIdentity = ObjectIdentity
es_1000 = _Es_1000_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 289, 2, 1, 1, 3)
)
_Es1000Sys_ObjectIdentity = ObjectIdentity
es1000Sys = _Es1000Sys_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 289, 2, 1, 1, 3, 1)
)


class _Es1000SysCurrentDate_Type(DisplayString):
    """Custom type es1000SysCurrentDate based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_Es1000SysCurrentDate_Type.__name__ = "DisplayString"
_Es1000SysCurrentDate_Object = MibScalar
es1000SysCurrentDate = _Es1000SysCurrentDate_Object(
    (1, 3, 6, 1, 4, 1, 289, 2, 1, 1, 3, 1, 1),
    _Es1000SysCurrentDate_Type()
)
es1000SysCurrentDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es1000SysCurrentDate.setStatus("mandatory")


class _Es1000SysBootDate_Type(DisplayString):
    """Custom type es1000SysBootDate based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_Es1000SysBootDate_Type.__name__ = "DisplayString"
_Es1000SysBootDate_Object = MibScalar
es1000SysBootDate = _Es1000SysBootDate_Object(
    (1, 3, 6, 1, 4, 1, 289, 2, 1, 1, 3, 1, 2),
    _Es1000SysBootDate_Type()
)
es1000SysBootDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es1000SysBootDate.setStatus("mandatory")


class _Es1000SysFirmwareVersion_Type(DisplayString):
    """Custom type es1000SysFirmwareVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_Es1000SysFirmwareVersion_Type.__name__ = "DisplayString"
_Es1000SysFirmwareVersion_Object = MibScalar
es1000SysFirmwareVersion = _Es1000SysFirmwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 289, 2, 1, 1, 3, 1, 3),
    _Es1000SysFirmwareVersion_Type()
)
es1000SysFirmwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es1000SysFirmwareVersion.setStatus("mandatory")


class _Es1000SysTypeNum_Type(DisplayString):
    """Custom type es1000SysTypeNum based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_Es1000SysTypeNum_Type.__name__ = "DisplayString"
_Es1000SysTypeNum_Object = MibScalar
es1000SysTypeNum = _Es1000SysTypeNum_Object(
    (1, 3, 6, 1, 4, 1, 289, 2, 1, 1, 3, 1, 4),
    _Es1000SysTypeNum_Type()
)
es1000SysTypeNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es1000SysTypeNum.setStatus("mandatory")


class _Es1000SysModelNum_Type(DisplayString):
    """Custom type es1000SysModelNum based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_Es1000SysModelNum_Type.__name__ = "DisplayString"
_Es1000SysModelNum_Object = MibScalar
es1000SysModelNum = _Es1000SysModelNum_Object(
    (1, 3, 6, 1, 4, 1, 289, 2, 1, 1, 3, 1, 5),
    _Es1000SysModelNum_Type()
)
es1000SysModelNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es1000SysModelNum.setStatus("mandatory")


class _Es1000SysMfg_Type(DisplayString):
    """Custom type es1000SysMfg based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_Es1000SysMfg_Type.__name__ = "DisplayString"
_Es1000SysMfg_Object = MibScalar
es1000SysMfg = _Es1000SysMfg_Object(
    (1, 3, 6, 1, 4, 1, 289, 2, 1, 1, 3, 1, 6),
    _Es1000SysMfg_Type()
)
es1000SysMfg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es1000SysMfg.setStatus("mandatory")


class _Es1000SysPlantOfMfg_Type(DisplayString):
    """Custom type es1000SysPlantOfMfg based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_Es1000SysPlantOfMfg_Type.__name__ = "DisplayString"
_Es1000SysPlantOfMfg_Object = MibScalar
es1000SysPlantOfMfg = _Es1000SysPlantOfMfg_Object(
    (1, 3, 6, 1, 4, 1, 289, 2, 1, 1, 3, 1, 7),
    _Es1000SysPlantOfMfg_Type()
)
es1000SysPlantOfMfg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es1000SysPlantOfMfg.setStatus("mandatory")


class _Es1000SysSeqNum_Type(DisplayString):
    """Custom type es1000SysSeqNum based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_Es1000SysSeqNum_Type.__name__ = "DisplayString"
_Es1000SysSeqNum_Object = MibScalar
es1000SysSeqNum = _Es1000SysSeqNum_Object(
    (1, 3, 6, 1, 4, 1, 289, 2, 1, 1, 3, 1, 8),
    _Es1000SysSeqNum_Type()
)
es1000SysSeqNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es1000SysSeqNum.setStatus("mandatory")


class _Es1000SysEcLevel_Type(DisplayString):
    """Custom type es1000SysEcLevel based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_Es1000SysEcLevel_Type.__name__ = "DisplayString"
_Es1000SysEcLevel_Object = MibScalar
es1000SysEcLevel = _Es1000SysEcLevel_Object(
    (1, 3, 6, 1, 4, 1, 289, 2, 1, 1, 3, 1, 9),
    _Es1000SysEcLevel_Type()
)
es1000SysEcLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es1000SysEcLevel.setStatus("mandatory")


class _Es1000SysOemSerialNum_Type(DisplayString):
    """Custom type es1000SysOemSerialNum based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_Es1000SysOemSerialNum_Type.__name__ = "DisplayString"
_Es1000SysOemSerialNum_Object = MibScalar
es1000SysOemSerialNum = _Es1000SysOemSerialNum_Object(
    (1, 3, 6, 1, 4, 1, 289, 2, 1, 1, 3, 1, 10),
    _Es1000SysOemSerialNum_Type()
)
es1000SysOemSerialNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es1000SysOemSerialNum.setStatus("mandatory")
_Es1000SysOperStatus_Type = Es1000SysOperStatus
_Es1000SysOperStatus_Object = MibScalar
es1000SysOperStatus = _Es1000SysOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 289, 2, 1, 1, 3, 1, 11),
    _Es1000SysOperStatus_Type()
)
es1000SysOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es1000SysOperStatus.setStatus("mandatory")
_Es1000SysState_Type = Es1000SysState
_Es1000SysState_Object = MibScalar
es1000SysState = _Es1000SysState_Object(
    (1, 3, 6, 1, 4, 1, 289, 2, 1, 1, 3, 1, 12),
    _Es1000SysState_Type()
)
es1000SysState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es1000SysState.setStatus("mandatory")


class _Es1000SysAdmStatus_Type(Integer32):
    """Custom type es1000SysAdmStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("offline", 2),
          ("online", 1))
    )


_Es1000SysAdmStatus_Type.__name__ = "Integer32"
_Es1000SysAdmStatus_Object = MibScalar
es1000SysAdmStatus = _Es1000SysAdmStatus_Object(
    (1, 3, 6, 1, 4, 1, 289, 2, 1, 1, 3, 1, 13),
    _Es1000SysAdmStatus_Type()
)
es1000SysAdmStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es1000SysAdmStatus.setStatus("mandatory")
_Es1000Comp_ObjectIdentity = ObjectIdentity
es1000Comp = _Es1000Comp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 289, 2, 1, 1, 3, 2)
)
_Es1000CompTable_Object = MibTable
es1000CompTable = _Es1000CompTable_Object(
    (1, 3, 6, 1, 4, 1, 289, 2, 1, 1, 3, 2, 1)
)
if mibBuilder.loadTexts:
    es1000CompTable.setStatus("mandatory")
_Es1000CompEntry_Object = MibTableRow
es1000CompEntry = _Es1000CompEntry_Object(
    (1, 3, 6, 1, 4, 1, 289, 2, 1, 1, 3, 2, 1, 1)
)
es1000CompEntry.setIndexNames(
    (0, "ES-1000-MIB", "es1000CompCode"),
    (0, "ES-1000-MIB", "es1000CompPosition"),
)
if mibBuilder.loadTexts:
    es1000CompEntry.setStatus("mandatory")
_Es1000CompCode_Type = Es1000CompCode
_Es1000CompCode_Object = MibTableColumn
es1000CompCode = _Es1000CompCode_Object(
    (1, 3, 6, 1, 4, 1, 289, 2, 1, 1, 3, 2, 1, 1, 1),
    _Es1000CompCode_Type()
)
es1000CompCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es1000CompCode.setStatus("mandatory")
_Es1000CompPosition_Type = Es1000CompPosition
_Es1000CompPosition_Object = MibTableColumn
es1000CompPosition = _Es1000CompPosition_Object(
    (1, 3, 6, 1, 4, 1, 289, 2, 1, 1, 3, 2, 1, 1, 2),
    _Es1000CompPosition_Type()
)
es1000CompPosition.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es1000CompPosition.setStatus("mandatory")
_Es1000CompStatus_Type = Es1000CompStatus
_Es1000CompStatus_Object = MibTableColumn
es1000CompStatus = _Es1000CompStatus_Object(
    (1, 3, 6, 1, 4, 1, 289, 2, 1, 1, 3, 2, 1, 1, 3),
    _Es1000CompStatus_Type()
)
es1000CompStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es1000CompStatus.setStatus("mandatory")
_Es1000Port_ObjectIdentity = ObjectIdentity
es1000Port = _Es1000Port_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 289, 2, 1, 1, 3, 3)
)
_Es1000PortBportCount_Type = Es1000PortCount
_Es1000PortBportCount_Object = MibScalar
es1000PortBportCount = _Es1000PortBportCount_Object(
    (1, 3, 6, 1, 4, 1, 289, 2, 1, 1, 3, 3, 1),
    _Es1000PortBportCount_Type()
)
es1000PortBportCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es1000PortBportCount.setStatus("mandatory")
_Es1000PortHportCount_Type = Es1000PortCount
_Es1000PortHportCount_Object = MibScalar
es1000PortHportCount = _Es1000PortHportCount_Object(
    (1, 3, 6, 1, 4, 1, 289, 2, 1, 1, 3, 3, 2),
    _Es1000PortHportCount_Type()
)
es1000PortHportCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es1000PortHportCount.setStatus("mandatory")
_Es1000PortBportTable_Object = MibTable
es1000PortBportTable = _Es1000PortBportTable_Object(
    (1, 3, 6, 1, 4, 1, 289, 2, 1, 1, 3, 3, 3)
)
if mibBuilder.loadTexts:
    es1000PortBportTable.setStatus("mandatory")
_Es1000PortBportEntry_Object = MibTableRow
es1000PortBportEntry = _Es1000PortBportEntry_Object(
    (1, 3, 6, 1, 4, 1, 289, 2, 1, 1, 3, 3, 3, 1)
)
es1000PortBportEntry.setIndexNames(
    (0, "ES-1000-MIB", "es1000PortBportIndex"),
)
if mibBuilder.loadTexts:
    es1000PortBportEntry.setStatus("mandatory")
_Es1000PortBportIndex_Type = Es1000PortIndex
_Es1000PortBportIndex_Object = MibTableColumn
es1000PortBportIndex = _Es1000PortBportIndex_Object(
    (1, 3, 6, 1, 4, 1, 289, 2, 1, 1, 3, 3, 3, 1, 1),
    _Es1000PortBportIndex_Type()
)
es1000PortBportIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es1000PortBportIndex.setStatus("mandatory")
_Es1000PortBportNumber_Type = Es1000PortNumber
_Es1000PortBportNumber_Object = MibTableColumn
es1000PortBportNumber = _Es1000PortBportNumber_Object(
    (1, 3, 6, 1, 4, 1, 289, 2, 1, 1, 3, 3, 3, 1, 2),
    _Es1000PortBportNumber_Type()
)
es1000PortBportNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es1000PortBportNumber.setStatus("mandatory")
_Es1000PortBportPhyState_Type = Es1000PortPhyState
_Es1000PortBportPhyState_Object = MibTableColumn
es1000PortBportPhyState = _Es1000PortBportPhyState_Object(
    (1, 3, 6, 1, 4, 1, 289, 2, 1, 1, 3, 3, 3, 1, 3),
    _Es1000PortBportPhyState_Type()
)
es1000PortBportPhyState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es1000PortBportPhyState.setStatus("mandatory")
_Es1000PortBportOpStatus_Type = Es1000PortStatus
_Es1000PortBportOpStatus_Object = MibTableColumn
es1000PortBportOpStatus = _Es1000PortBportOpStatus_Object(
    (1, 3, 6, 1, 4, 1, 289, 2, 1, 1, 3, 3, 3, 1, 4),
    _Es1000PortBportOpStatus_Type()
)
es1000PortBportOpStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es1000PortBportOpStatus.setStatus("mandatory")
_Es1000PortBportAdmStatus_Type = Es1000PortAdmStatus
_Es1000PortBportAdmStatus_Object = MibTableColumn
es1000PortBportAdmStatus = _Es1000PortBportAdmStatus_Object(
    (1, 3, 6, 1, 4, 1, 289, 2, 1, 1, 3, 3, 3, 1, 5),
    _Es1000PortBportAdmStatus_Type()
)
es1000PortBportAdmStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es1000PortBportAdmStatus.setStatus("mandatory")


class _Es1000PortBportName_Type(DisplayString):
    """Custom type es1000PortBportName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 24),
    )


_Es1000PortBportName_Type.__name__ = "DisplayString"
_Es1000PortBportName_Object = MibTableColumn
es1000PortBportName = _Es1000PortBportName_Object(
    (1, 3, 6, 1, 4, 1, 289, 2, 1, 1, 3, 3, 3, 1, 6),
    _Es1000PortBportName_Type()
)
es1000PortBportName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es1000PortBportName.setStatus("mandatory")
_Es1000PortBportBlockedState_Type = TruthValue
_Es1000PortBportBlockedState_Object = MibTableColumn
es1000PortBportBlockedState = _Es1000PortBportBlockedState_Object(
    (1, 3, 6, 1, 4, 1, 289, 2, 1, 1, 3, 3, 3, 1, 7),
    _Es1000PortBportBlockedState_Type()
)
es1000PortBportBlockedState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es1000PortBportBlockedState.setStatus("mandatory")
_Es1000PortHportTable_Object = MibTable
es1000PortHportTable = _Es1000PortHportTable_Object(
    (1, 3, 6, 1, 4, 1, 289, 2, 1, 1, 3, 3, 4)
)
if mibBuilder.loadTexts:
    es1000PortHportTable.setStatus("mandatory")
_Es1000PortHportEntry_Object = MibTableRow
es1000PortHportEntry = _Es1000PortHportEntry_Object(
    (1, 3, 6, 1, 4, 1, 289, 2, 1, 1, 3, 3, 4, 1)
)
es1000PortHportEntry.setIndexNames(
    (0, "ES-1000-MIB", "es1000PortHportIndex"),
)
if mibBuilder.loadTexts:
    es1000PortHportEntry.setStatus("mandatory")
_Es1000PortHportIndex_Type = Es1000PortIndex
_Es1000PortHportIndex_Object = MibTableColumn
es1000PortHportIndex = _Es1000PortHportIndex_Object(
    (1, 3, 6, 1, 4, 1, 289, 2, 1, 1, 3, 3, 4, 1, 1),
    _Es1000PortHportIndex_Type()
)
es1000PortHportIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es1000PortHportIndex.setStatus("mandatory")
_Es1000PortHportNumber_Type = Es1000PortNumber
_Es1000PortHportNumber_Object = MibTableColumn
es1000PortHportNumber = _Es1000PortHportNumber_Object(
    (1, 3, 6, 1, 4, 1, 289, 2, 1, 1, 3, 3, 4, 1, 2),
    _Es1000PortHportNumber_Type()
)
es1000PortHportNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es1000PortHportNumber.setStatus("mandatory")
_Es1000PortHportPhyState_Type = Es1000PortPhyState
_Es1000PortHportPhyState_Object = MibTableColumn
es1000PortHportPhyState = _Es1000PortHportPhyState_Object(
    (1, 3, 6, 1, 4, 1, 289, 2, 1, 1, 3, 3, 4, 1, 3),
    _Es1000PortHportPhyState_Type()
)
es1000PortHportPhyState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es1000PortHportPhyState.setStatus("mandatory")
_Es1000PortHportOpStatus_Type = Es1000PortStatus
_Es1000PortHportOpStatus_Object = MibTableColumn
es1000PortHportOpStatus = _Es1000PortHportOpStatus_Object(
    (1, 3, 6, 1, 4, 1, 289, 2, 1, 1, 3, 3, 4, 1, 4),
    _Es1000PortHportOpStatus_Type()
)
es1000PortHportOpStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es1000PortHportOpStatus.setStatus("mandatory")
_Es1000PortHportAdmStatus_Type = Es1000PortAdmStatus
_Es1000PortHportAdmStatus_Object = MibTableColumn
es1000PortHportAdmStatus = _Es1000PortHportAdmStatus_Object(
    (1, 3, 6, 1, 4, 1, 289, 2, 1, 1, 3, 3, 4, 1, 5),
    _Es1000PortHportAdmStatus_Type()
)
es1000PortHportAdmStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es1000PortHportAdmStatus.setStatus("mandatory")


class _Es1000PortHportName_Type(DisplayString):
    """Custom type es1000PortHportName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 24),
    )


_Es1000PortHportName_Type.__name__ = "DisplayString"
_Es1000PortHportName_Object = MibTableColumn
es1000PortHportName = _Es1000PortHportName_Object(
    (1, 3, 6, 1, 4, 1, 289, 2, 1, 1, 3, 3, 4, 1, 6),
    _Es1000PortHportName_Type()
)
es1000PortHportName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es1000PortHportName.setStatus("mandatory")
_Es1000PortHportBypassedState_Type = TruthValue
_Es1000PortHportBypassedState_Object = MibTableColumn
es1000PortHportBypassedState = _Es1000PortHportBypassedState_Object(
    (1, 3, 6, 1, 4, 1, 289, 2, 1, 1, 3, 3, 4, 1, 7),
    _Es1000PortHportBypassedState_Type()
)
es1000PortHportBypassedState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es1000PortHportBypassedState.setStatus("mandatory")
_Es1000PortHportValidation_Type = TruthValue
_Es1000PortHportValidation_Object = MibTableColumn
es1000PortHportValidation = _Es1000PortHportValidation_Object(
    (1, 3, 6, 1, 4, 1, 289, 2, 1, 1, 3, 3, 4, 1, 8),
    _Es1000PortHportValidation_Type()
)
es1000PortHportValidation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es1000PortHportValidation.setStatus("mandatory")
_Es1000PortHportLipOnInsertion_Type = TruthValue
_Es1000PortHportLipOnInsertion_Object = MibTableColumn
es1000PortHportLipOnInsertion = _Es1000PortHportLipOnInsertion_Object(
    (1, 3, 6, 1, 4, 1, 289, 2, 1, 1, 3, 3, 4, 1, 9),
    _Es1000PortHportLipOnInsertion_Type()
)
es1000PortHportLipOnInsertion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es1000PortHportLipOnInsertion.setStatus("mandatory")
_Es1000Loop_ObjectIdentity = ObjectIdentity
es1000Loop = _Es1000Loop_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 289, 2, 1, 1, 3, 4)
)
_Es1000LoopStatus_Type = Es1000LoopStatus
_Es1000LoopStatus_Object = MibScalar
es1000LoopStatus = _Es1000LoopStatus_Object(
    (1, 3, 6, 1, 4, 1, 289, 2, 1, 1, 3, 4, 1),
    _Es1000LoopStatus_Type()
)
es1000LoopStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es1000LoopStatus.setStatus("mandatory")
_Es1000LoopMasterWWN_Type = Es1000LoopMasterWWN
_Es1000LoopMasterWWN_Object = MibScalar
es1000LoopMasterWWN = _Es1000LoopMasterWWN_Object(
    (1, 3, 6, 1, 4, 1, 289, 2, 1, 1, 3, 4, 2),
    _Es1000LoopMasterWWN_Type()
)
es1000LoopMasterWWN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es1000LoopMasterWWN.setStatus("mandatory")
_Es1000LoopSwitched_Type = TruthValue
_Es1000LoopSwitched_Object = MibScalar
es1000LoopSwitched = _Es1000LoopSwitched_Object(
    (1, 3, 6, 1, 4, 1, 289, 2, 1, 1, 3, 4, 3),
    _Es1000LoopSwitched_Type()
)
es1000LoopSwitched.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es1000LoopSwitched.setStatus("mandatory")
_Es1000LoopPrincipal_Type = TruthValue
_Es1000LoopPrincipal_Object = MibScalar
es1000LoopPrincipal = _Es1000LoopPrincipal_Object(
    (1, 3, 6, 1, 4, 1, 289, 2, 1, 1, 3, 4, 4),
    _Es1000LoopPrincipal_Type()
)
es1000LoopPrincipal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es1000LoopPrincipal.setStatus("mandatory")
_Es1000LoopPortTable_Object = MibTable
es1000LoopPortTable = _Es1000LoopPortTable_Object(
    (1, 3, 6, 1, 4, 1, 289, 2, 1, 1, 3, 4, 5)
)
if mibBuilder.loadTexts:
    es1000LoopPortTable.setStatus("mandatory")
_Es1000LoopPortEntry_Object = MibTableRow
es1000LoopPortEntry = _Es1000LoopPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 289, 2, 1, 1, 3, 4, 5, 1)
)
es1000LoopPortEntry.setIndexNames(
    (0, "ES-1000-MIB", "es1000LoopPortIndex"),
)
if mibBuilder.loadTexts:
    es1000LoopPortEntry.setStatus("mandatory")
_Es1000LoopPortIndex_Type = Es1000PortIndex
_Es1000LoopPortIndex_Object = MibTableColumn
es1000LoopPortIndex = _Es1000LoopPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 289, 2, 1, 1, 3, 4, 5, 1, 1),
    _Es1000LoopPortIndex_Type()
)
es1000LoopPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es1000LoopPortIndex.setStatus("mandatory")
_Es1000LoopPortNumber_Type = Es1000PortNumber
_Es1000LoopPortNumber_Object = MibTableColumn
es1000LoopPortNumber = _Es1000LoopPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 289, 2, 1, 1, 3, 4, 5, 1, 2),
    _Es1000LoopPortNumber_Type()
)
es1000LoopPortNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es1000LoopPortNumber.setStatus("mandatory")
_Es1000LoopPortALPA_Type = Es1000LoopPortALPA
_Es1000LoopPortALPA_Object = MibTableColumn
es1000LoopPortALPA = _Es1000LoopPortALPA_Object(
    (1, 3, 6, 1, 4, 1, 289, 2, 1, 1, 3, 4, 5, 1, 3),
    _Es1000LoopPortALPA_Type()
)
es1000LoopPortALPA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es1000LoopPortALPA.setStatus("mandatory")
_Es1000Acct_ObjectIdentity = ObjectIdentity
es1000Acct = _Es1000Acct_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 289, 2, 1, 1, 3, 5)
)
_Es1000AcctBportTable_Object = MibTable
es1000AcctBportTable = _Es1000AcctBportTable_Object(
    (1, 3, 6, 1, 4, 1, 289, 2, 1, 1, 3, 5, 1)
)
if mibBuilder.loadTexts:
    es1000AcctBportTable.setStatus("mandatory")
_Es1000AcctBportEntry_Object = MibTableRow
es1000AcctBportEntry = _Es1000AcctBportEntry_Object(
    (1, 3, 6, 1, 4, 1, 289, 2, 1, 1, 3, 5, 1, 1)
)
es1000AcctBportEntry.setIndexNames(
    (0, "ES-1000-MIB", "es1000AcctBportIndex"),
)
if mibBuilder.loadTexts:
    es1000AcctBportEntry.setStatus("mandatory")
_Es1000AcctBportIndex_Type = Es1000PortIndex
_Es1000AcctBportIndex_Object = MibTableColumn
es1000AcctBportIndex = _Es1000AcctBportIndex_Object(
    (1, 3, 6, 1, 4, 1, 289, 2, 1, 1, 3, 5, 1, 1, 1),
    _Es1000AcctBportIndex_Type()
)
es1000AcctBportIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es1000AcctBportIndex.setStatus("mandatory")
_Es1000AcctBportNumber_Type = Es1000PortNumber
_Es1000AcctBportNumber_Object = MibTableColumn
es1000AcctBportNumber = _Es1000AcctBportNumber_Object(
    (1, 3, 6, 1, 4, 1, 289, 2, 1, 1, 3, 5, 1, 1, 2),
    _Es1000AcctBportNumber_Type()
)
es1000AcctBportNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es1000AcctBportNumber.setStatus("mandatory")
_Es1000AcctBportLinkFailures_Type = Counter32
_Es1000AcctBportLinkFailures_Object = MibTableColumn
es1000AcctBportLinkFailures = _Es1000AcctBportLinkFailures_Object(
    (1, 3, 6, 1, 4, 1, 289, 2, 1, 1, 3, 5, 1, 1, 3),
    _Es1000AcctBportLinkFailures_Type()
)
es1000AcctBportLinkFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es1000AcctBportLinkFailures.setStatus("mandatory")
_Es1000AcctBportSyncLosses_Type = Counter32
_Es1000AcctBportSyncLosses_Object = MibTableColumn
es1000AcctBportSyncLosses = _Es1000AcctBportSyncLosses_Object(
    (1, 3, 6, 1, 4, 1, 289, 2, 1, 1, 3, 5, 1, 1, 4),
    _Es1000AcctBportSyncLosses_Type()
)
es1000AcctBportSyncLosses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es1000AcctBportSyncLosses.setStatus("mandatory")
_Es1000AcctBportSigLosses_Type = Counter32
_Es1000AcctBportSigLosses_Object = MibTableColumn
es1000AcctBportSigLosses = _Es1000AcctBportSigLosses_Object(
    (1, 3, 6, 1, 4, 1, 289, 2, 1, 1, 3, 5, 1, 1, 5),
    _Es1000AcctBportSigLosses_Type()
)
es1000AcctBportSigLosses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es1000AcctBportSigLosses.setStatus("mandatory")
_Es1000AcctBportPrimSeqProtoErrors_Type = Counter32
_Es1000AcctBportPrimSeqProtoErrors_Object = MibTableColumn
es1000AcctBportPrimSeqProtoErrors = _Es1000AcctBportPrimSeqProtoErrors_Object(
    (1, 3, 6, 1, 4, 1, 289, 2, 1, 1, 3, 5, 1, 1, 6),
    _Es1000AcctBportPrimSeqProtoErrors_Type()
)
es1000AcctBportPrimSeqProtoErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es1000AcctBportPrimSeqProtoErrors.setStatus("mandatory")
_Es1000AcctBportInvalidTxWords_Type = Counter32
_Es1000AcctBportInvalidTxWords_Object = MibTableColumn
es1000AcctBportInvalidTxWords = _Es1000AcctBportInvalidTxWords_Object(
    (1, 3, 6, 1, 4, 1, 289, 2, 1, 1, 3, 5, 1, 1, 7),
    _Es1000AcctBportInvalidTxWords_Type()
)
es1000AcctBportInvalidTxWords.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es1000AcctBportInvalidTxWords.setStatus("mandatory")
_Es1000AcctBportInvalidCrcs_Type = Counter32
_Es1000AcctBportInvalidCrcs_Object = MibTableColumn
es1000AcctBportInvalidCrcs = _Es1000AcctBportInvalidCrcs_Object(
    (1, 3, 6, 1, 4, 1, 289, 2, 1, 1, 3, 5, 1, 1, 8),
    _Es1000AcctBportInvalidCrcs_Type()
)
es1000AcctBportInvalidCrcs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es1000AcctBportInvalidCrcs.setStatus("mandatory")
_Es1000AcctBportLinkResetIns_Type = Counter32
_Es1000AcctBportLinkResetIns_Object = MibTableColumn
es1000AcctBportLinkResetIns = _Es1000AcctBportLinkResetIns_Object(
    (1, 3, 6, 1, 4, 1, 289, 2, 1, 1, 3, 5, 1, 1, 9),
    _Es1000AcctBportLinkResetIns_Type()
)
es1000AcctBportLinkResetIns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es1000AcctBportLinkResetIns.setStatus("mandatory")
_Es1000AcctBportLinkResetOuts_Type = Counter32
_Es1000AcctBportLinkResetOuts_Object = MibTableColumn
es1000AcctBportLinkResetOuts = _Es1000AcctBportLinkResetOuts_Object(
    (1, 3, 6, 1, 4, 1, 289, 2, 1, 1, 3, 5, 1, 1, 10),
    _Es1000AcctBportLinkResetOuts_Type()
)
es1000AcctBportLinkResetOuts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es1000AcctBportLinkResetOuts.setStatus("mandatory")
_Es1000AcctBportOlsIns_Type = Counter32
_Es1000AcctBportOlsIns_Object = MibTableColumn
es1000AcctBportOlsIns = _Es1000AcctBportOlsIns_Object(
    (1, 3, 6, 1, 4, 1, 289, 2, 1, 1, 3, 5, 1, 1, 11),
    _Es1000AcctBportOlsIns_Type()
)
es1000AcctBportOlsIns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es1000AcctBportOlsIns.setStatus("mandatory")
_Es1000AcctBportOlsOuts_Type = Counter32
_Es1000AcctBportOlsOuts_Object = MibTableColumn
es1000AcctBportOlsOuts = _Es1000AcctBportOlsOuts_Object(
    (1, 3, 6, 1, 4, 1, 289, 2, 1, 1, 3, 5, 1, 1, 12),
    _Es1000AcctBportOlsOuts_Type()
)
es1000AcctBportOlsOuts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es1000AcctBportOlsOuts.setStatus("mandatory")
_Es1000AcctBportC2InFrames_Type = Counter32
_Es1000AcctBportC2InFrames_Object = MibTableColumn
es1000AcctBportC2InFrames = _Es1000AcctBportC2InFrames_Object(
    (1, 3, 6, 1, 4, 1, 289, 2, 1, 1, 3, 5, 1, 1, 13),
    _Es1000AcctBportC2InFrames_Type()
)
es1000AcctBportC2InFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es1000AcctBportC2InFrames.setStatus("mandatory")
_Es1000AcctBportC2OutFrames_Type = Counter32
_Es1000AcctBportC2OutFrames_Object = MibTableColumn
es1000AcctBportC2OutFrames = _Es1000AcctBportC2OutFrames_Object(
    (1, 3, 6, 1, 4, 1, 289, 2, 1, 1, 3, 5, 1, 1, 14),
    _Es1000AcctBportC2OutFrames_Type()
)
es1000AcctBportC2OutFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es1000AcctBportC2OutFrames.setStatus("mandatory")
_Es1000AcctBportC2Discards_Type = Counter32
_Es1000AcctBportC2Discards_Object = MibTableColumn
es1000AcctBportC2Discards = _Es1000AcctBportC2Discards_Object(
    (1, 3, 6, 1, 4, 1, 289, 2, 1, 1, 3, 5, 1, 1, 15),
    _Es1000AcctBportC2Discards_Type()
)
es1000AcctBportC2Discards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es1000AcctBportC2Discards.setStatus("mandatory")
_Es1000AcctBportC2InOctets_Type = Counter32
_Es1000AcctBportC2InOctets_Object = MibTableColumn
es1000AcctBportC2InOctets = _Es1000AcctBportC2InOctets_Object(
    (1, 3, 6, 1, 4, 1, 289, 2, 1, 1, 3, 5, 1, 1, 16),
    _Es1000AcctBportC2InOctets_Type()
)
es1000AcctBportC2InOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es1000AcctBportC2InOctets.setStatus("mandatory")
_Es1000AcctBportC2OutOctets_Type = Counter32
_Es1000AcctBportC2OutOctets_Object = MibTableColumn
es1000AcctBportC2OutOctets = _Es1000AcctBportC2OutOctets_Object(
    (1, 3, 6, 1, 4, 1, 289, 2, 1, 1, 3, 5, 1, 1, 17),
    _Es1000AcctBportC2OutOctets_Type()
)
es1000AcctBportC2OutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es1000AcctBportC2OutOctets.setStatus("mandatory")
_Es1000AcctBportC3InFrames_Type = Counter32
_Es1000AcctBportC3InFrames_Object = MibTableColumn
es1000AcctBportC3InFrames = _Es1000AcctBportC3InFrames_Object(
    (1, 3, 6, 1, 4, 1, 289, 2, 1, 1, 3, 5, 1, 1, 18),
    _Es1000AcctBportC3InFrames_Type()
)
es1000AcctBportC3InFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es1000AcctBportC3InFrames.setStatus("mandatory")
_Es1000AcctBportC3OutFrames_Type = Counter32
_Es1000AcctBportC3OutFrames_Object = MibTableColumn
es1000AcctBportC3OutFrames = _Es1000AcctBportC3OutFrames_Object(
    (1, 3, 6, 1, 4, 1, 289, 2, 1, 1, 3, 5, 1, 1, 19),
    _Es1000AcctBportC3OutFrames_Type()
)
es1000AcctBportC3OutFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es1000AcctBportC3OutFrames.setStatus("mandatory")
_Es1000AcctBportC3InOctets_Type = Counter32
_Es1000AcctBportC3InOctets_Object = MibTableColumn
es1000AcctBportC3InOctets = _Es1000AcctBportC3InOctets_Object(
    (1, 3, 6, 1, 4, 1, 289, 2, 1, 1, 3, 5, 1, 1, 20),
    _Es1000AcctBportC3InOctets_Type()
)
es1000AcctBportC3InOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es1000AcctBportC3InOctets.setStatus("mandatory")
_Es1000AcctBportC3OutOctets_Type = Counter32
_Es1000AcctBportC3OutOctets_Object = MibTableColumn
es1000AcctBportC3OutOctets = _Es1000AcctBportC3OutOctets_Object(
    (1, 3, 6, 1, 4, 1, 289, 2, 1, 1, 3, 5, 1, 1, 21),
    _Es1000AcctBportC3OutOctets_Type()
)
es1000AcctBportC3OutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es1000AcctBportC3OutOctets.setStatus("mandatory")
_Es1000AcctBportC3Discards_Type = Counter32
_Es1000AcctBportC3Discards_Object = MibTableColumn
es1000AcctBportC3Discards = _Es1000AcctBportC3Discards_Object(
    (1, 3, 6, 1, 4, 1, 289, 2, 1, 1, 3, 5, 1, 1, 22),
    _Es1000AcctBportC3Discards_Type()
)
es1000AcctBportC3Discards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es1000AcctBportC3Discards.setStatus("mandatory")
_Es1000AcctBportRxWords_Type = Counter32
_Es1000AcctBportRxWords_Object = MibTableColumn
es1000AcctBportRxWords = _Es1000AcctBportRxWords_Object(
    (1, 3, 6, 1, 4, 1, 289, 2, 1, 1, 3, 5, 1, 1, 23),
    _Es1000AcctBportRxWords_Type()
)
es1000AcctBportRxWords.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es1000AcctBportRxWords.setStatus("mandatory")
_Es1000AcctBportTxWords_Type = Counter32
_Es1000AcctBportTxWords_Object = MibTableColumn
es1000AcctBportTxWords = _Es1000AcctBportTxWords_Object(
    (1, 3, 6, 1, 4, 1, 289, 2, 1, 1, 3, 5, 1, 1, 24),
    _Es1000AcctBportTxWords_Type()
)
es1000AcctBportTxWords.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es1000AcctBportTxWords.setStatus("mandatory")
_Es1000AcctBportRxFrames_Type = Counter32
_Es1000AcctBportRxFrames_Object = MibTableColumn
es1000AcctBportRxFrames = _Es1000AcctBportRxFrames_Object(
    (1, 3, 6, 1, 4, 1, 289, 2, 1, 1, 3, 5, 1, 1, 25),
    _Es1000AcctBportRxFrames_Type()
)
es1000AcctBportRxFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es1000AcctBportRxFrames.setStatus("mandatory")
_Es1000AcctBportTxFrames_Type = Counter32
_Es1000AcctBportTxFrames_Object = MibTableColumn
es1000AcctBportTxFrames = _Es1000AcctBportTxFrames_Object(
    (1, 3, 6, 1, 4, 1, 289, 2, 1, 1, 3, 5, 1, 1, 26),
    _Es1000AcctBportTxFrames_Type()
)
es1000AcctBportTxFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es1000AcctBportTxFrames.setStatus("mandatory")
_Es1000AcctBportInvalidOrderedSets_Type = Counter32
_Es1000AcctBportInvalidOrderedSets_Object = MibTableColumn
es1000AcctBportInvalidOrderedSets = _Es1000AcctBportInvalidOrderedSets_Object(
    (1, 3, 6, 1, 4, 1, 289, 2, 1, 1, 3, 5, 1, 1, 27),
    _Es1000AcctBportInvalidOrderedSets_Type()
)
es1000AcctBportInvalidOrderedSets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es1000AcctBportInvalidOrderedSets.setStatus("mandatory")
_Es1000AcctBportFramesTooLong_Type = Counter32
_Es1000AcctBportFramesTooLong_Object = MibTableColumn
es1000AcctBportFramesTooLong = _Es1000AcctBportFramesTooLong_Object(
    (1, 3, 6, 1, 4, 1, 289, 2, 1, 1, 3, 5, 1, 1, 28),
    _Es1000AcctBportFramesTooLong_Type()
)
es1000AcctBportFramesTooLong.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es1000AcctBportFramesTooLong.setStatus("mandatory")
_Es1000AcctBportFramesTooShort_Type = Counter32
_Es1000AcctBportFramesTooShort_Object = MibTableColumn
es1000AcctBportFramesTooShort = _Es1000AcctBportFramesTooShort_Object(
    (1, 3, 6, 1, 4, 1, 289, 2, 1, 1, 3, 5, 1, 1, 29),
    _Es1000AcctBportFramesTooShort_Type()
)
es1000AcctBportFramesTooShort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es1000AcctBportFramesTooShort.setStatus("mandatory")
_Es1000AcctBportTxThroughput_Type = Counter32
_Es1000AcctBportTxThroughput_Object = MibTableColumn
es1000AcctBportTxThroughput = _Es1000AcctBportTxThroughput_Object(
    (1, 3, 6, 1, 4, 1, 289, 2, 1, 1, 3, 5, 1, 1, 30),
    _Es1000AcctBportTxThroughput_Type()
)
es1000AcctBportTxThroughput.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es1000AcctBportTxThroughput.setStatus("mandatory")
_Es1000AcctBportRxThroughput_Type = Counter32
_Es1000AcctBportRxThroughput_Object = MibTableColumn
es1000AcctBportRxThroughput = _Es1000AcctBportRxThroughput_Object(
    (1, 3, 6, 1, 4, 1, 289, 2, 1, 1, 3, 5, 1, 1, 31),
    _Es1000AcctBportRxThroughput_Type()
)
es1000AcctBportRxThroughput.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es1000AcctBportRxThroughput.setStatus("mandatory")
_Es1000AcctBportAddressErrors_Type = Counter32
_Es1000AcctBportAddressErrors_Object = MibTableColumn
es1000AcctBportAddressErrors = _Es1000AcctBportAddressErrors_Object(
    (1, 3, 6, 1, 4, 1, 289, 2, 1, 1, 3, 5, 1, 1, 32),
    _Es1000AcctBportAddressErrors_Type()
)
es1000AcctBportAddressErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es1000AcctBportAddressErrors.setStatus("mandatory")
_Es1000AcctBportC2FbsyFrames_Type = Counter32
_Es1000AcctBportC2FbsyFrames_Object = MibTableColumn
es1000AcctBportC2FbsyFrames = _Es1000AcctBportC2FbsyFrames_Object(
    (1, 3, 6, 1, 4, 1, 289, 2, 1, 1, 3, 5, 1, 1, 33),
    _Es1000AcctBportC2FbsyFrames_Type()
)
es1000AcctBportC2FbsyFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es1000AcctBportC2FbsyFrames.setStatus("mandatory")
_Es1000AcctBportC2FrjtFrames_Type = Counter32
_Es1000AcctBportC2FrjtFrames_Object = MibTableColumn
es1000AcctBportC2FrjtFrames = _Es1000AcctBportC2FrjtFrames_Object(
    (1, 3, 6, 1, 4, 1, 289, 2, 1, 1, 3, 5, 1, 1, 34),
    _Es1000AcctBportC2FrjtFrames_Type()
)
es1000AcctBportC2FrjtFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es1000AcctBportC2FrjtFrames.setStatus("mandatory")
_Es1000AcctBportCFInFrames_Type = Counter32
_Es1000AcctBportCFInFrames_Object = MibTableColumn
es1000AcctBportCFInFrames = _Es1000AcctBportCFInFrames_Object(
    (1, 3, 6, 1, 4, 1, 289, 2, 1, 1, 3, 5, 1, 1, 35),
    _Es1000AcctBportCFInFrames_Type()
)
es1000AcctBportCFInFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es1000AcctBportCFInFrames.setStatus("mandatory")
_Es1000AcctBportFramesDiscarded_Type = Counter32
_Es1000AcctBportFramesDiscarded_Object = MibTableColumn
es1000AcctBportFramesDiscarded = _Es1000AcctBportFramesDiscarded_Object(
    (1, 3, 6, 1, 4, 1, 289, 2, 1, 1, 3, 5, 1, 1, 36),
    _Es1000AcctBportFramesDiscarded_Type()
)
es1000AcctBportFramesDiscarded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es1000AcctBportFramesDiscarded.setStatus("mandatory")
_Es1000AcctBportInvalidClassofFrame_Type = Counter32
_Es1000AcctBportInvalidClassofFrame_Object = MibTableColumn
es1000AcctBportInvalidClassofFrame = _Es1000AcctBportInvalidClassofFrame_Object(
    (1, 3, 6, 1, 4, 1, 289, 2, 1, 1, 3, 5, 1, 1, 37),
    _Es1000AcctBportInvalidClassofFrame_Type()
)
es1000AcctBportInvalidClassofFrame.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es1000AcctBportInvalidClassofFrame.setStatus("mandatory")
_Es1000AcctBportC2RxWords_Type = Counter32
_Es1000AcctBportC2RxWords_Object = MibTableColumn
es1000AcctBportC2RxWords = _Es1000AcctBportC2RxWords_Object(
    (1, 3, 6, 1, 4, 1, 289, 2, 1, 1, 3, 5, 1, 1, 38),
    _Es1000AcctBportC2RxWords_Type()
)
es1000AcctBportC2RxWords.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es1000AcctBportC2RxWords.setStatus("mandatory")
_Es1000AcctBportC2TxWords_Type = Counter32
_Es1000AcctBportC2TxWords_Object = MibTableColumn
es1000AcctBportC2TxWords = _Es1000AcctBportC2TxWords_Object(
    (1, 3, 6, 1, 4, 1, 289, 2, 1, 1, 3, 5, 1, 1, 39),
    _Es1000AcctBportC2TxWords_Type()
)
es1000AcctBportC2TxWords.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es1000AcctBportC2TxWords.setStatus("mandatory")
_Es1000AcctBportC3RxWords_Type = Counter32
_Es1000AcctBportC3RxWords_Object = MibTableColumn
es1000AcctBportC3RxWords = _Es1000AcctBportC3RxWords_Object(
    (1, 3, 6, 1, 4, 1, 289, 2, 1, 1, 3, 5, 1, 1, 40),
    _Es1000AcctBportC3RxWords_Type()
)
es1000AcctBportC3RxWords.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es1000AcctBportC3RxWords.setStatus("mandatory")
_Es1000AcctBportC3TxWords_Type = Counter32
_Es1000AcctBportC3TxWords_Object = MibTableColumn
es1000AcctBportC3TxWords = _Es1000AcctBportC3TxWords_Object(
    (1, 3, 6, 1, 4, 1, 289, 2, 1, 1, 3, 5, 1, 1, 41),
    _Es1000AcctBportC3TxWords_Type()
)
es1000AcctBportC3TxWords.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es1000AcctBportC3TxWords.setStatus("mandatory")
_Es1000AcctBportTxThroughputPercent_Type = Counter32
_Es1000AcctBportTxThroughputPercent_Object = MibTableColumn
es1000AcctBportTxThroughputPercent = _Es1000AcctBportTxThroughputPercent_Object(
    (1, 3, 6, 1, 4, 1, 289, 2, 1, 1, 3, 5, 1, 1, 42),
    _Es1000AcctBportTxThroughputPercent_Type()
)
es1000AcctBportTxThroughputPercent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es1000AcctBportTxThroughputPercent.setStatus("mandatory")
_Es1000AcctBportRxThroughputPercent_Type = Counter32
_Es1000AcctBportRxThroughputPercent_Object = MibTableColumn
es1000AcctBportRxThroughputPercent = _Es1000AcctBportRxThroughputPercent_Object(
    (1, 3, 6, 1, 4, 1, 289, 2, 1, 1, 3, 5, 1, 1, 43),
    _Es1000AcctBportRxThroughputPercent_Type()
)
es1000AcctBportRxThroughputPercent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es1000AcctBportRxThroughputPercent.setStatus("mandatory")
_Es1000AcctBportLinkDown_Type = Counter32
_Es1000AcctBportLinkDown_Object = MibTableColumn
es1000AcctBportLinkDown = _Es1000AcctBportLinkDown_Object(
    (1, 3, 6, 1, 4, 1, 289, 2, 1, 1, 3, 5, 1, 1, 44),
    _Es1000AcctBportLinkDown_Type()
)
es1000AcctBportLinkDown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es1000AcctBportLinkDown.setStatus("mandatory")
_Es1000AcctHportTable_Object = MibTable
es1000AcctHportTable = _Es1000AcctHportTable_Object(
    (1, 3, 6, 1, 4, 1, 289, 2, 1, 1, 3, 5, 2)
)
if mibBuilder.loadTexts:
    es1000AcctHportTable.setStatus("mandatory")
_Es1000AcctHportEntry_Object = MibTableRow
es1000AcctHportEntry = _Es1000AcctHportEntry_Object(
    (1, 3, 6, 1, 4, 1, 289, 2, 1, 1, 3, 5, 2, 1)
)
es1000AcctHportEntry.setIndexNames(
    (0, "ES-1000-MIB", "es1000AcctHportIndex"),
)
if mibBuilder.loadTexts:
    es1000AcctHportEntry.setStatus("mandatory")
_Es1000AcctHportIndex_Type = Es1000PortIndex
_Es1000AcctHportIndex_Object = MibTableColumn
es1000AcctHportIndex = _Es1000AcctHportIndex_Object(
    (1, 3, 6, 1, 4, 1, 289, 2, 1, 1, 3, 5, 2, 1, 1),
    _Es1000AcctHportIndex_Type()
)
es1000AcctHportIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es1000AcctHportIndex.setStatus("mandatory")
_Es1000AcctHportNumber_Type = Es1000PortNumber
_Es1000AcctHportNumber_Object = MibTableColumn
es1000AcctHportNumber = _Es1000AcctHportNumber_Object(
    (1, 3, 6, 1, 4, 1, 289, 2, 1, 1, 3, 5, 2, 1, 2),
    _Es1000AcctHportNumber_Type()
)
es1000AcctHportNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es1000AcctHportNumber.setStatus("mandatory")
_Es1000AcctHportLinkFailures_Type = Counter32
_Es1000AcctHportLinkFailures_Object = MibTableColumn
es1000AcctHportLinkFailures = _Es1000AcctHportLinkFailures_Object(
    (1, 3, 6, 1, 4, 1, 289, 2, 1, 1, 3, 5, 2, 1, 3),
    _Es1000AcctHportLinkFailures_Type()
)
es1000AcctHportLinkFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es1000AcctHportLinkFailures.setStatus("mandatory")
_Es1000AcctHportSyncLosses_Type = Counter32
_Es1000AcctHportSyncLosses_Object = MibTableColumn
es1000AcctHportSyncLosses = _Es1000AcctHportSyncLosses_Object(
    (1, 3, 6, 1, 4, 1, 289, 2, 1, 1, 3, 5, 2, 1, 4),
    _Es1000AcctHportSyncLosses_Type()
)
es1000AcctHportSyncLosses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es1000AcctHportSyncLosses.setStatus("mandatory")
_Es1000AcctHportSigLosses_Type = Counter32
_Es1000AcctHportSigLosses_Object = MibTableColumn
es1000AcctHportSigLosses = _Es1000AcctHportSigLosses_Object(
    (1, 3, 6, 1, 4, 1, 289, 2, 1, 1, 3, 5, 2, 1, 5),
    _Es1000AcctHportSigLosses_Type()
)
es1000AcctHportSigLosses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es1000AcctHportSigLosses.setStatus("mandatory")
_Es1000AcctHportInvalidTxWords_Type = Counter32
_Es1000AcctHportInvalidTxWords_Object = MibTableColumn
es1000AcctHportInvalidTxWords = _Es1000AcctHportInvalidTxWords_Object(
    (1, 3, 6, 1, 4, 1, 289, 2, 1, 1, 3, 5, 2, 1, 6),
    _Es1000AcctHportInvalidTxWords_Type()
)
es1000AcctHportInvalidTxWords.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es1000AcctHportInvalidTxWords.setStatus("mandatory")
_Es1000AcctHportInvalidCrcs_Type = Counter32
_Es1000AcctHportInvalidCrcs_Object = MibTableColumn
es1000AcctHportInvalidCrcs = _Es1000AcctHportInvalidCrcs_Object(
    (1, 3, 6, 1, 4, 1, 289, 2, 1, 1, 3, 5, 2, 1, 7),
    _Es1000AcctHportInvalidCrcs_Type()
)
es1000AcctHportInvalidCrcs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es1000AcctHportInvalidCrcs.setStatus("mandatory")
_Es1000AcctHportC2InFrames_Type = Counter32
_Es1000AcctHportC2InFrames_Object = MibTableColumn
es1000AcctHportC2InFrames = _Es1000AcctHportC2InFrames_Object(
    (1, 3, 6, 1, 4, 1, 289, 2, 1, 1, 3, 5, 2, 1, 8),
    _Es1000AcctHportC2InFrames_Type()
)
es1000AcctHportC2InFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es1000AcctHportC2InFrames.setStatus("mandatory")
_Es1000AcctHportC2OutFrames_Type = Counter32
_Es1000AcctHportC2OutFrames_Object = MibTableColumn
es1000AcctHportC2OutFrames = _Es1000AcctHportC2OutFrames_Object(
    (1, 3, 6, 1, 4, 1, 289, 2, 1, 1, 3, 5, 2, 1, 9),
    _Es1000AcctHportC2OutFrames_Type()
)
es1000AcctHportC2OutFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es1000AcctHportC2OutFrames.setStatus("mandatory")
_Es1000AcctHportC2InOctets_Type = Counter32
_Es1000AcctHportC2InOctets_Object = MibTableColumn
es1000AcctHportC2InOctets = _Es1000AcctHportC2InOctets_Object(
    (1, 3, 6, 1, 4, 1, 289, 2, 1, 1, 3, 5, 2, 1, 10),
    _Es1000AcctHportC2InOctets_Type()
)
es1000AcctHportC2InOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es1000AcctHportC2InOctets.setStatus("mandatory")
_Es1000AcctHportC2OutOctets_Type = Counter32
_Es1000AcctHportC2OutOctets_Object = MibTableColumn
es1000AcctHportC2OutOctets = _Es1000AcctHportC2OutOctets_Object(
    (1, 3, 6, 1, 4, 1, 289, 2, 1, 1, 3, 5, 2, 1, 11),
    _Es1000AcctHportC2OutOctets_Type()
)
es1000AcctHportC2OutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es1000AcctHportC2OutOctets.setStatus("mandatory")
_Es1000AcctHportC3InFrames_Type = Counter32
_Es1000AcctHportC3InFrames_Object = MibTableColumn
es1000AcctHportC3InFrames = _Es1000AcctHportC3InFrames_Object(
    (1, 3, 6, 1, 4, 1, 289, 2, 1, 1, 3, 5, 2, 1, 12),
    _Es1000AcctHportC3InFrames_Type()
)
es1000AcctHportC3InFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es1000AcctHportC3InFrames.setStatus("mandatory")
_Es1000AcctHportC3OutFrames_Type = Counter32
_Es1000AcctHportC3OutFrames_Object = MibTableColumn
es1000AcctHportC3OutFrames = _Es1000AcctHportC3OutFrames_Object(
    (1, 3, 6, 1, 4, 1, 289, 2, 1, 1, 3, 5, 2, 1, 13),
    _Es1000AcctHportC3OutFrames_Type()
)
es1000AcctHportC3OutFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es1000AcctHportC3OutFrames.setStatus("mandatory")
_Es1000AcctHportC3InOctets_Type = Counter32
_Es1000AcctHportC3InOctets_Object = MibTableColumn
es1000AcctHportC3InOctets = _Es1000AcctHportC3InOctets_Object(
    (1, 3, 6, 1, 4, 1, 289, 2, 1, 1, 3, 5, 2, 1, 14),
    _Es1000AcctHportC3InOctets_Type()
)
es1000AcctHportC3InOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es1000AcctHportC3InOctets.setStatus("mandatory")
_Es1000AcctHportC3OutOctets_Type = Counter32
_Es1000AcctHportC3OutOctets_Object = MibTableColumn
es1000AcctHportC3OutOctets = _Es1000AcctHportC3OutOctets_Object(
    (1, 3, 6, 1, 4, 1, 289, 2, 1, 1, 3, 5, 2, 1, 15),
    _Es1000AcctHportC3OutOctets_Type()
)
es1000AcctHportC3OutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es1000AcctHportC3OutOctets.setStatus("mandatory")
_Es1000AcctHportRxWords_Type = Counter32
_Es1000AcctHportRxWords_Object = MibTableColumn
es1000AcctHportRxWords = _Es1000AcctHportRxWords_Object(
    (1, 3, 6, 1, 4, 1, 289, 2, 1, 1, 3, 5, 2, 1, 16),
    _Es1000AcctHportRxWords_Type()
)
es1000AcctHportRxWords.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es1000AcctHportRxWords.setStatus("mandatory")
_Es1000AcctHportTxWords_Type = Counter32
_Es1000AcctHportTxWords_Object = MibTableColumn
es1000AcctHportTxWords = _Es1000AcctHportTxWords_Object(
    (1, 3, 6, 1, 4, 1, 289, 2, 1, 1, 3, 5, 2, 1, 17),
    _Es1000AcctHportTxWords_Type()
)
es1000AcctHportTxWords.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es1000AcctHportTxWords.setStatus("mandatory")
_Es1000AcctHportRxFrames_Type = Counter32
_Es1000AcctHportRxFrames_Object = MibTableColumn
es1000AcctHportRxFrames = _Es1000AcctHportRxFrames_Object(
    (1, 3, 6, 1, 4, 1, 289, 2, 1, 1, 3, 5, 2, 1, 18),
    _Es1000AcctHportRxFrames_Type()
)
es1000AcctHportRxFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es1000AcctHportRxFrames.setStatus("mandatory")
_Es1000AcctHportTxFrames_Type = Counter32
_Es1000AcctHportTxFrames_Object = MibTableColumn
es1000AcctHportTxFrames = _Es1000AcctHportTxFrames_Object(
    (1, 3, 6, 1, 4, 1, 289, 2, 1, 1, 3, 5, 2, 1, 19),
    _Es1000AcctHportTxFrames_Type()
)
es1000AcctHportTxFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es1000AcctHportTxFrames.setStatus("mandatory")
_Es1000AcctHportTxThroughput_Type = Counter32
_Es1000AcctHportTxThroughput_Object = MibTableColumn
es1000AcctHportTxThroughput = _Es1000AcctHportTxThroughput_Object(
    (1, 3, 6, 1, 4, 1, 289, 2, 1, 1, 3, 5, 2, 1, 20),
    _Es1000AcctHportTxThroughput_Type()
)
es1000AcctHportTxThroughput.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es1000AcctHportTxThroughput.setStatus("mandatory")
_Es1000AcctHportRxThroughput_Type = Counter32
_Es1000AcctHportRxThroughput_Object = MibTableColumn
es1000AcctHportRxThroughput = _Es1000AcctHportRxThroughput_Object(
    (1, 3, 6, 1, 4, 1, 289, 2, 1, 1, 3, 5, 2, 1, 21),
    _Es1000AcctHportRxThroughput_Type()
)
es1000AcctHportRxThroughput.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es1000AcctHportRxThroughput.setStatus("mandatory")
_Es1000AcctHportC2RxWords_Type = Counter32
_Es1000AcctHportC2RxWords_Object = MibTableColumn
es1000AcctHportC2RxWords = _Es1000AcctHportC2RxWords_Object(
    (1, 3, 6, 1, 4, 1, 289, 2, 1, 1, 3, 5, 2, 1, 22),
    _Es1000AcctHportC2RxWords_Type()
)
es1000AcctHportC2RxWords.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es1000AcctHportC2RxWords.setStatus("mandatory")
_Es1000AcctHportC2TxWords_Type = Counter32
_Es1000AcctHportC2TxWords_Object = MibTableColumn
es1000AcctHportC2TxWords = _Es1000AcctHportC2TxWords_Object(
    (1, 3, 6, 1, 4, 1, 289, 2, 1, 1, 3, 5, 2, 1, 23),
    _Es1000AcctHportC2TxWords_Type()
)
es1000AcctHportC2TxWords.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es1000AcctHportC2TxWords.setStatus("mandatory")
_Es1000AcctHportC3RxWords_Type = Counter32
_Es1000AcctHportC3RxWords_Object = MibTableColumn
es1000AcctHportC3RxWords = _Es1000AcctHportC3RxWords_Object(
    (1, 3, 6, 1, 4, 1, 289, 2, 1, 1, 3, 5, 2, 1, 24),
    _Es1000AcctHportC3RxWords_Type()
)
es1000AcctHportC3RxWords.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es1000AcctHportC3RxWords.setStatus("mandatory")
_Es1000AcctHportC3TxWords_Type = Counter32
_Es1000AcctHportC3TxWords_Object = MibTableColumn
es1000AcctHportC3TxWords = _Es1000AcctHportC3TxWords_Object(
    (1, 3, 6, 1, 4, 1, 289, 2, 1, 1, 3, 5, 2, 1, 25),
    _Es1000AcctHportC3TxWords_Type()
)
es1000AcctHportC3TxWords.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es1000AcctHportC3TxWords.setStatus("mandatory")
_Es1000AcctHportTxThroughputPercent_Type = Counter32
_Es1000AcctHportTxThroughputPercent_Object = MibTableColumn
es1000AcctHportTxThroughputPercent = _Es1000AcctHportTxThroughputPercent_Object(
    (1, 3, 6, 1, 4, 1, 289, 2, 1, 1, 3, 5, 2, 1, 26),
    _Es1000AcctHportTxThroughputPercent_Type()
)
es1000AcctHportTxThroughputPercent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es1000AcctHportTxThroughputPercent.setStatus("mandatory")
_Es1000AcctHportRxThroughputPercent_Type = Counter32
_Es1000AcctHportRxThroughputPercent_Object = MibTableColumn
es1000AcctHportRxThroughputPercent = _Es1000AcctHportRxThroughputPercent_Object(
    (1, 3, 6, 1, 4, 1, 289, 2, 1, 1, 3, 5, 2, 1, 27),
    _Es1000AcctHportRxThroughputPercent_Type()
)
es1000AcctHportRxThroughputPercent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es1000AcctHportRxThroughputPercent.setStatus("mandatory")
_Es1000AcctHportLIPCount_Type = Counter32
_Es1000AcctHportLIPCount_Object = MibTableColumn
es1000AcctHportLIPCount = _Es1000AcctHportLIPCount_Object(
    (1, 3, 6, 1, 4, 1, 289, 2, 1, 1, 3, 5, 2, 1, 28),
    _Es1000AcctHportLIPCount_Type()
)
es1000AcctHportLIPCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es1000AcctHportLIPCount.setStatus("mandatory")
_Es1000AcctHportConnectionsMade_Type = Counter32
_Es1000AcctHportConnectionsMade_Object = MibTableColumn
es1000AcctHportConnectionsMade = _Es1000AcctHportConnectionsMade_Object(
    (1, 3, 6, 1, 4, 1, 289, 2, 1, 1, 3, 5, 2, 1, 29),
    _Es1000AcctHportConnectionsMade_Type()
)
es1000AcctHportConnectionsMade.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es1000AcctHportConnectionsMade.setStatus("mandatory")
_Es1000AcctHportConnectionsStalled_Type = Counter32
_Es1000AcctHportConnectionsStalled_Object = MibTableColumn
es1000AcctHportConnectionsStalled = _Es1000AcctHportConnectionsStalled_Object(
    (1, 3, 6, 1, 4, 1, 289, 2, 1, 1, 3, 5, 2, 1, 30),
    _Es1000AcctHportConnectionsStalled_Type()
)
es1000AcctHportConnectionsStalled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es1000AcctHportConnectionsStalled.setStatus("mandatory")
_Es1000AcctHportConnectionsAborted_Type = Counter32
_Es1000AcctHportConnectionsAborted_Object = MibTableColumn
es1000AcctHportConnectionsAborted = _Es1000AcctHportConnectionsAborted_Object(
    (1, 3, 6, 1, 4, 1, 289, 2, 1, 1, 3, 5, 2, 1, 31),
    _Es1000AcctHportConnectionsAborted_Type()
)
es1000AcctHportConnectionsAborted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es1000AcctHportConnectionsAborted.setStatus("mandatory")
_Es1000AcctHportConnectionsAccepted_Type = Counter32
_Es1000AcctHportConnectionsAccepted_Object = MibTableColumn
es1000AcctHportConnectionsAccepted = _Es1000AcctHportConnectionsAccepted_Object(
    (1, 3, 6, 1, 4, 1, 289, 2, 1, 1, 3, 5, 2, 1, 32),
    _Es1000AcctHportConnectionsAccepted_Type()
)
es1000AcctHportConnectionsAccepted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es1000AcctHportConnectionsAccepted.setStatus("mandatory")

# Managed Objects groups


# Notification objects

es1000PortBportScn = NotificationType(
    (1, 3, 6, 1, 4, 1, 289, 0, 1)
)
es1000PortBportScn.setObjects(
    ("ES-1000-MIB", "es1000PortBportOpStatus")
)
if mibBuilder.loadTexts:
    es1000PortBportScn.setStatus(
        ""
    )

es1000PortHportScn = NotificationType(
    (1, 3, 6, 1, 4, 1, 289, 0, 2)
)
es1000PortHportScn.setObjects(
    ("ES-1000-MIB", "es1000PortHportOpStatus")
)
if mibBuilder.loadTexts:
    es1000PortHportScn.setStatus(
        ""
    )

es1000CompScn = NotificationType(
    (1, 3, 6, 1, 4, 1, 289, 0, 3)
)
es1000CompScn.setObjects(
    ("ES-1000-MIB", "es1000CompStatus")
)
if mibBuilder.loadTexts:
    es1000CompScn.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ES-1000-MIB",
    **{"TruthValue": TruthValue,
       "Es1000SysOperStatus": Es1000SysOperStatus,
       "Es1000SysState": Es1000SysState,
       "Es1000CompCode": Es1000CompCode,
       "Es1000CompPosition": Es1000CompPosition,
       "Es1000CompStatus": Es1000CompStatus,
       "Es1000PortCount": Es1000PortCount,
       "Es1000PortIndex": Es1000PortIndex,
       "Es1000PortNumber": Es1000PortNumber,
       "Es1000PortPhyState": Es1000PortPhyState,
       "Es1000PortStatus": Es1000PortStatus,
       "Es1000PortAdmStatus": Es1000PortAdmStatus,
       "Es1000LoopStatus": Es1000LoopStatus,
       "Es1000LoopMasterWWN": Es1000LoopMasterWWN,
       "Es1000LoopPortALPA": Es1000LoopPortALPA,
       "mcData": mcData,
       "es1000PortBportScn": es1000PortBportScn,
       "es1000PortHportScn": es1000PortHportScn,
       "es1000CompScn": es1000CompScn,
       "commDev": commDev,
       "fibreChannel": fibreChannel,
       "fcSwitch": fcSwitch,
       "es-1000": es_1000,
       "es1000Sys": es1000Sys,
       "es1000SysCurrentDate": es1000SysCurrentDate,
       "es1000SysBootDate": es1000SysBootDate,
       "es1000SysFirmwareVersion": es1000SysFirmwareVersion,
       "es1000SysTypeNum": es1000SysTypeNum,
       "es1000SysModelNum": es1000SysModelNum,
       "es1000SysMfg": es1000SysMfg,
       "es1000SysPlantOfMfg": es1000SysPlantOfMfg,
       "es1000SysSeqNum": es1000SysSeqNum,
       "es1000SysEcLevel": es1000SysEcLevel,
       "es1000SysOemSerialNum": es1000SysOemSerialNum,
       "es1000SysOperStatus": es1000SysOperStatus,
       "es1000SysState": es1000SysState,
       "es1000SysAdmStatus": es1000SysAdmStatus,
       "es1000Comp": es1000Comp,
       "es1000CompTable": es1000CompTable,
       "es1000CompEntry": es1000CompEntry,
       "es1000CompCode": es1000CompCode,
       "es1000CompPosition": es1000CompPosition,
       "es1000CompStatus": es1000CompStatus,
       "es1000Port": es1000Port,
       "es1000PortBportCount": es1000PortBportCount,
       "es1000PortHportCount": es1000PortHportCount,
       "es1000PortBportTable": es1000PortBportTable,
       "es1000PortBportEntry": es1000PortBportEntry,
       "es1000PortBportIndex": es1000PortBportIndex,
       "es1000PortBportNumber": es1000PortBportNumber,
       "es1000PortBportPhyState": es1000PortBportPhyState,
       "es1000PortBportOpStatus": es1000PortBportOpStatus,
       "es1000PortBportAdmStatus": es1000PortBportAdmStatus,
       "es1000PortBportName": es1000PortBportName,
       "es1000PortBportBlockedState": es1000PortBportBlockedState,
       "es1000PortHportTable": es1000PortHportTable,
       "es1000PortHportEntry": es1000PortHportEntry,
       "es1000PortHportIndex": es1000PortHportIndex,
       "es1000PortHportNumber": es1000PortHportNumber,
       "es1000PortHportPhyState": es1000PortHportPhyState,
       "es1000PortHportOpStatus": es1000PortHportOpStatus,
       "es1000PortHportAdmStatus": es1000PortHportAdmStatus,
       "es1000PortHportName": es1000PortHportName,
       "es1000PortHportBypassedState": es1000PortHportBypassedState,
       "es1000PortHportValidation": es1000PortHportValidation,
       "es1000PortHportLipOnInsertion": es1000PortHportLipOnInsertion,
       "es1000Loop": es1000Loop,
       "es1000LoopStatus": es1000LoopStatus,
       "es1000LoopMasterWWN": es1000LoopMasterWWN,
       "es1000LoopSwitched": es1000LoopSwitched,
       "es1000LoopPrincipal": es1000LoopPrincipal,
       "es1000LoopPortTable": es1000LoopPortTable,
       "es1000LoopPortEntry": es1000LoopPortEntry,
       "es1000LoopPortIndex": es1000LoopPortIndex,
       "es1000LoopPortNumber": es1000LoopPortNumber,
       "es1000LoopPortALPA": es1000LoopPortALPA,
       "es1000Acct": es1000Acct,
       "es1000AcctBportTable": es1000AcctBportTable,
       "es1000AcctBportEntry": es1000AcctBportEntry,
       "es1000AcctBportIndex": es1000AcctBportIndex,
       "es1000AcctBportNumber": es1000AcctBportNumber,
       "es1000AcctBportLinkFailures": es1000AcctBportLinkFailures,
       "es1000AcctBportSyncLosses": es1000AcctBportSyncLosses,
       "es1000AcctBportSigLosses": es1000AcctBportSigLosses,
       "es1000AcctBportPrimSeqProtoErrors": es1000AcctBportPrimSeqProtoErrors,
       "es1000AcctBportInvalidTxWords": es1000AcctBportInvalidTxWords,
       "es1000AcctBportInvalidCrcs": es1000AcctBportInvalidCrcs,
       "es1000AcctBportLinkResetIns": es1000AcctBportLinkResetIns,
       "es1000AcctBportLinkResetOuts": es1000AcctBportLinkResetOuts,
       "es1000AcctBportOlsIns": es1000AcctBportOlsIns,
       "es1000AcctBportOlsOuts": es1000AcctBportOlsOuts,
       "es1000AcctBportC2InFrames": es1000AcctBportC2InFrames,
       "es1000AcctBportC2OutFrames": es1000AcctBportC2OutFrames,
       "es1000AcctBportC2Discards": es1000AcctBportC2Discards,
       "es1000AcctBportC2InOctets": es1000AcctBportC2InOctets,
       "es1000AcctBportC2OutOctets": es1000AcctBportC2OutOctets,
       "es1000AcctBportC3InFrames": es1000AcctBportC3InFrames,
       "es1000AcctBportC3OutFrames": es1000AcctBportC3OutFrames,
       "es1000AcctBportC3InOctets": es1000AcctBportC3InOctets,
       "es1000AcctBportC3OutOctets": es1000AcctBportC3OutOctets,
       "es1000AcctBportC3Discards": es1000AcctBportC3Discards,
       "es1000AcctBportRxWords": es1000AcctBportRxWords,
       "es1000AcctBportTxWords": es1000AcctBportTxWords,
       "es1000AcctBportRxFrames": es1000AcctBportRxFrames,
       "es1000AcctBportTxFrames": es1000AcctBportTxFrames,
       "es1000AcctBportInvalidOrderedSets": es1000AcctBportInvalidOrderedSets,
       "es1000AcctBportFramesTooLong": es1000AcctBportFramesTooLong,
       "es1000AcctBportFramesTooShort": es1000AcctBportFramesTooShort,
       "es1000AcctBportTxThroughput": es1000AcctBportTxThroughput,
       "es1000AcctBportRxThroughput": es1000AcctBportRxThroughput,
       "es1000AcctBportAddressErrors": es1000AcctBportAddressErrors,
       "es1000AcctBportC2FbsyFrames": es1000AcctBportC2FbsyFrames,
       "es1000AcctBportC2FrjtFrames": es1000AcctBportC2FrjtFrames,
       "es1000AcctBportCFInFrames": es1000AcctBportCFInFrames,
       "es1000AcctBportFramesDiscarded": es1000AcctBportFramesDiscarded,
       "es1000AcctBportInvalidClassofFrame": es1000AcctBportInvalidClassofFrame,
       "es1000AcctBportC2RxWords": es1000AcctBportC2RxWords,
       "es1000AcctBportC2TxWords": es1000AcctBportC2TxWords,
       "es1000AcctBportC3RxWords": es1000AcctBportC3RxWords,
       "es1000AcctBportC3TxWords": es1000AcctBportC3TxWords,
       "es1000AcctBportTxThroughputPercent": es1000AcctBportTxThroughputPercent,
       "es1000AcctBportRxThroughputPercent": es1000AcctBportRxThroughputPercent,
       "es1000AcctBportLinkDown": es1000AcctBportLinkDown,
       "es1000AcctHportTable": es1000AcctHportTable,
       "es1000AcctHportEntry": es1000AcctHportEntry,
       "es1000AcctHportIndex": es1000AcctHportIndex,
       "es1000AcctHportNumber": es1000AcctHportNumber,
       "es1000AcctHportLinkFailures": es1000AcctHportLinkFailures,
       "es1000AcctHportSyncLosses": es1000AcctHportSyncLosses,
       "es1000AcctHportSigLosses": es1000AcctHportSigLosses,
       "es1000AcctHportInvalidTxWords": es1000AcctHportInvalidTxWords,
       "es1000AcctHportInvalidCrcs": es1000AcctHportInvalidCrcs,
       "es1000AcctHportC2InFrames": es1000AcctHportC2InFrames,
       "es1000AcctHportC2OutFrames": es1000AcctHportC2OutFrames,
       "es1000AcctHportC2InOctets": es1000AcctHportC2InOctets,
       "es1000AcctHportC2OutOctets": es1000AcctHportC2OutOctets,
       "es1000AcctHportC3InFrames": es1000AcctHportC3InFrames,
       "es1000AcctHportC3OutFrames": es1000AcctHportC3OutFrames,
       "es1000AcctHportC3InOctets": es1000AcctHportC3InOctets,
       "es1000AcctHportC3OutOctets": es1000AcctHportC3OutOctets,
       "es1000AcctHportRxWords": es1000AcctHportRxWords,
       "es1000AcctHportTxWords": es1000AcctHportTxWords,
       "es1000AcctHportRxFrames": es1000AcctHportRxFrames,
       "es1000AcctHportTxFrames": es1000AcctHportTxFrames,
       "es1000AcctHportTxThroughput": es1000AcctHportTxThroughput,
       "es1000AcctHportRxThroughput": es1000AcctHportRxThroughput,
       "es1000AcctHportC2RxWords": es1000AcctHportC2RxWords,
       "es1000AcctHportC2TxWords": es1000AcctHportC2TxWords,
       "es1000AcctHportC3RxWords": es1000AcctHportC3RxWords,
       "es1000AcctHportC3TxWords": es1000AcctHportC3TxWords,
       "es1000AcctHportTxThroughputPercent": es1000AcctHportTxThroughputPercent,
       "es1000AcctHportRxThroughputPercent": es1000AcctHportRxThroughputPercent,
       "es1000AcctHportLIPCount": es1000AcctHportLIPCount,
       "es1000AcctHportConnectionsMade": es1000AcctHportConnectionsMade,
       "es1000AcctHportConnectionsStalled": es1000AcctHportConnectionsStalled,
       "es1000AcctHportConnectionsAborted": es1000AcctHportConnectionsAborted,
       "es1000AcctHportConnectionsAccepted": es1000AcctHportConnectionsAccepted}
)
