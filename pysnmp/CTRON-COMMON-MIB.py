# SNMP MIB module (CTRON-COMMON-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CTRON-COMMON-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:18:39 2024
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

(commonRev1,
 dl,
 subSysDevice,
 subSysMMAC,
 ups) = mibBuilder.importSymbols(
    "IRM-OIDS",
    "commonRev1",
    "dl",
    "subSysDevice",
    "subSysMMAC",
    "ups")

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
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs



class _DeviceType_Type(Integer32):
    """Custom type deviceType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              176,
              177,
              178,
              179,
              180,
              185,
              187,
              190,
              65569,
              65570,
              65571,
              65572)
        )
    )
    namedValues = NamedValues(
        *(("emm-E", 185),
          ("iRBM", 177),
          ("iRM2", 176),
          ("iRM3", 178),
          ("mrxi22", 65570),
          ("mrxi24", 65569),
          ("mrxi34", 65571),
          ("mrxi38", 65572),
          ("other", 1),
          ("tRMBM-R", 179),
          ("tRMBM-S", 180),
          ("tRMM", 187),
          ("trmMim", 190))
    )


_DeviceType_Type.__name__ = "Integer32"
_DeviceType_Object = MibScalar
deviceType = _DeviceType_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 1, 1, 1),
    _DeviceType_Type()
)
deviceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deviceType.setStatus("mandatory")
_DeviceName_Type = DisplayString
_DeviceName_Object = MibScalar
deviceName = _DeviceName_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 1, 1, 2),
    _DeviceName_Type()
)
deviceName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    deviceName.setStatus("mandatory")
_DeviceIPAddress_Type = IpAddress
_DeviceIPAddress_Object = MibScalar
deviceIPAddress = _DeviceIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 1, 1, 3),
    _DeviceIPAddress_Type()
)
deviceIPAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    deviceIPAddress.setStatus("mandatory")


class _DeviceTime_Type(DisplayString):
    """Custom type deviceTime based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_DeviceTime_Type.__name__ = "DisplayString"
_DeviceTime_Object = MibScalar
deviceTime = _DeviceTime_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 1, 1, 4),
    _DeviceTime_Type()
)
deviceTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    deviceTime.setStatus("mandatory")


class _DeviceDate_Type(DisplayString):
    """Custom type deviceDate based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_DeviceDate_Type.__name__ = "DisplayString"
_DeviceDate_Object = MibScalar
deviceDate = _DeviceDate_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 1, 1, 5),
    _DeviceDate_Type()
)
deviceDate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    deviceDate.setStatus("mandatory")
_Fnb2_ObjectIdentity = ObjectIdentity
fnb2 = _Fnb2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 1, 6, 1, 2)
)
_FnbTR_ObjectIdentity = ObjectIdentity
fnbTR = _FnbTR_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 1, 6, 1, 2, 1)
)
_FnbTRTable_Object = MibTable
fnbTRTable = _FnbTRTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 6, 1, 2, 1, 1)
)
if mibBuilder.loadTexts:
    fnbTRTable.setStatus("mandatory")
_FnbTREntry_Object = MibTableRow
fnbTREntry = _FnbTREntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 6, 1, 2, 1, 1, 1)
)
fnbTREntry.setIndexNames(
    (0, "CTRON-COMMON-MIB", "fnbTRIndex"),
)
if mibBuilder.loadTexts:
    fnbTREntry.setStatus("mandatory")
_FnbTRIndex_Type = Integer32
_FnbTRIndex_Object = MibTableColumn
fnbTRIndex = _FnbTRIndex_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 6, 1, 2, 1, 1, 1, 1),
    _FnbTRIndex_Type()
)
fnbTRIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnbTRIndex.setStatus("mandatory")


class _FnbConnectLeft_Type(Integer32):
    """Custom type fnbConnectLeft based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("attached", 2),
          ("detached", 1),
          ("faulted", 3))
    )


_FnbConnectLeft_Type.__name__ = "Integer32"
_FnbConnectLeft_Object = MibTableColumn
fnbConnectLeft = _FnbConnectLeft_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 6, 1, 2, 1, 1, 1, 2),
    _FnbConnectLeft_Type()
)
fnbConnectLeft.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fnbConnectLeft.setStatus("mandatory")


class _FnbConnectRight_Type(Integer32):
    """Custom type fnbConnectRight based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("attached", 2),
          ("detached", 1),
          ("faulted", 3))
    )


_FnbConnectRight_Type.__name__ = "Integer32"
_FnbConnectRight_Object = MibTableColumn
fnbConnectRight = _FnbConnectRight_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 6, 1, 2, 1, 1, 1, 3),
    _FnbConnectRight_Type()
)
fnbConnectRight.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fnbConnectRight.setStatus("mandatory")


class _FnbBypass_Type(Integer32):
    """Custom type fnbBypass based on Integer32"""
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


_FnbBypass_Type.__name__ = "Integer32"
_FnbBypass_Object = MibTableColumn
fnbBypass = _FnbBypass_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 6, 1, 2, 1, 1, 1, 4),
    _FnbBypass_Type()
)
fnbBypass.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fnbBypass.setStatus("mandatory")


class _FnbRPBypass_Type(Integer32):
    """Custom type fnbRPBypass based on Integer32"""
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
          ("enabled", 3),
          ("other", 1))
    )


_FnbRPBypass_Type.__name__ = "Integer32"
_FnbRPBypass_Object = MibTableColumn
fnbRPBypass = _FnbRPBypass_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 6, 1, 2, 1, 1, 1, 5),
    _FnbRPBypass_Type()
)
fnbRPBypass.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fnbRPBypass.setStatus("mandatory")
_FnbCSMACD_ObjectIdentity = ObjectIdentity
fnbCSMACD = _FnbCSMACD_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 1, 6, 1, 2, 2)
)
_FnbCSMACDTable_Object = MibTable
fnbCSMACDTable = _FnbCSMACDTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 6, 1, 2, 2, 1)
)
if mibBuilder.loadTexts:
    fnbCSMACDTable.setStatus("mandatory")
_FnbCSMACDEntry_Object = MibTableRow
fnbCSMACDEntry = _FnbCSMACDEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 6, 1, 2, 2, 1, 1)
)
fnbCSMACDEntry.setIndexNames(
    (0, "CTRON-COMMON-MIB", "fnbCSMACDIndex"),
)
if mibBuilder.loadTexts:
    fnbCSMACDEntry.setStatus("mandatory")
_FnbCSMACDIndex_Type = Integer32
_FnbCSMACDIndex_Object = MibTableColumn
fnbCSMACDIndex = _FnbCSMACDIndex_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 6, 1, 2, 2, 1, 1, 1),
    _FnbCSMACDIndex_Type()
)
fnbCSMACDIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fnbCSMACDIndex.setStatus("mandatory")


class _FnbConnect_Type(Integer32):
    """Custom type fnbConnect based on Integer32"""
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
        *(("connectA", 4),
          ("connectB", 1),
          ("connectC", 2),
          ("disconnect", 3),
          ("frontPanel", 8),
          ("multiChannel", 7),
          ("subnetB", 5),
          ("subnetC", 6))
    )


_FnbConnect_Type.__name__ = "Integer32"
_FnbConnect_Object = MibTableColumn
fnbConnect = _FnbConnect_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 6, 1, 2, 2, 1, 1, 2),
    _FnbConnect_Type()
)
fnbConnect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fnbConnect.setStatus("mandatory")
_FnbPortChanges_Type = Counter32
_FnbPortChanges_Object = MibTableColumn
fnbPortChanges = _FnbPortChanges_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 6, 1, 2, 2, 1, 1, 3),
    _FnbPortChanges_Type()
)
fnbPortChanges.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnbPortChanges.setStatus("mandatory")
_FnbPortConnect_ObjectIdentity = ObjectIdentity
fnbPortConnect = _FnbPortConnect_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 1, 6, 1, 2, 3)
)
_FnbPortConnectTable_Object = MibTable
fnbPortConnectTable = _FnbPortConnectTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 6, 1, 2, 3, 1)
)
if mibBuilder.loadTexts:
    fnbPortConnectTable.setStatus("mandatory")
_FnbPortConnectEntry_Object = MibTableRow
fnbPortConnectEntry = _FnbPortConnectEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 6, 1, 2, 3, 1, 1)
)
fnbPortConnectEntry.setIndexNames(
    (0, "CTRON-COMMON-MIB", "fnbPortConnectBoardIndex"),
    (0, "CTRON-COMMON-MIB", "fnbPortConnectPortIndex"),
)
if mibBuilder.loadTexts:
    fnbPortConnectEntry.setStatus("mandatory")
_FnbPortConnectBoardIndex_Type = Integer32
_FnbPortConnectBoardIndex_Object = MibTableColumn
fnbPortConnectBoardIndex = _FnbPortConnectBoardIndex_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 6, 1, 2, 3, 1, 1, 1),
    _FnbPortConnectBoardIndex_Type()
)
fnbPortConnectBoardIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnbPortConnectBoardIndex.setStatus("mandatory")
_FnbPortConnectPortIndex_Type = Integer32
_FnbPortConnectPortIndex_Object = MibTableColumn
fnbPortConnectPortIndex = _FnbPortConnectPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 6, 1, 2, 3, 1, 1, 2),
    _FnbPortConnectPortIndex_Type()
)
fnbPortConnectPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnbPortConnectPortIndex.setStatus("mandatory")


class _FnbPortConnectPortAssignment_Type(Integer32):
    """Custom type fnbPortConnectPortAssignment based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("connectA", 1),
          ("connectB", 2),
          ("connectC", 3))
    )


_FnbPortConnectPortAssignment_Type.__name__ = "Integer32"
_FnbPortConnectPortAssignment_Object = MibTableColumn
fnbPortConnectPortAssignment = _FnbPortConnectPortAssignment_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 6, 1, 2, 3, 1, 1, 3),
    _FnbPortConnectPortAssignment_Type()
)
fnbPortConnectPortAssignment.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fnbPortConnectPortAssignment.setStatus("mandatory")
_FnbPortConnectCompID_Type = Integer32
_FnbPortConnectCompID_Object = MibTableColumn
fnbPortConnectCompID = _FnbPortConnectCompID_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 6, 1, 2, 3, 1, 1, 4),
    _FnbPortConnectCompID_Type()
)
fnbPortConnectCompID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnbPortConnectCompID.setStatus("mandatory")
_FnbPortConnectionChanges_Type = Counter32
_FnbPortConnectionChanges_Object = MibScalar
fnbPortConnectionChanges = _FnbPortConnectionChanges_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 6, 1, 2, 3, 2),
    _FnbPortConnectionChanges_Type()
)
fnbPortConnectionChanges.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnbPortConnectionChanges.setStatus("mandatory")
_Chassis_ObjectIdentity = ObjectIdentity
chassis = _Chassis_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 1, 6, 1, 3)
)
_ChassisHWRev_Type = Integer32
_ChassisHWRev_Object = MibScalar
chassisHWRev = _ChassisHWRev_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 6, 1, 3, 1),
    _ChassisHWRev_Type()
)
chassisHWRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chassisHWRev.setStatus("mandatory")


class _ChassisType_Type(Integer32):
    """Custom type chassisType based on Integer32"""
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
              14)
        )
    )
    namedValues = NamedValues(
        *(("m3FNB", 7),
          ("m5FNB", 8),
          ("m8FNB", 9),
          ("m8FNBS", 14),
          ("mINIMMAC", 5),
          ("mMAC3FNB", 4),
          ("mMAC3FNBS", 11),
          ("mMAC5FNB", 3),
          ("mMAC5FNBS", 12),
          ("mMAC8FNB", 2),
          ("mMAC8FNBS", 13),
          ("mRXI", 6),
          ("nonFNB", 10),
          ("other", 1))
    )


_ChassisType_Type.__name__ = "Integer32"
_ChassisType_Object = MibScalar
chassisType = _ChassisType_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 6, 1, 3, 2),
    _ChassisType_Type()
)
chassisType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chassisType.setStatus("mandatory")
_ChassisSlots_Type = Integer32
_ChassisSlots_Object = MibScalar
chassisSlots = _ChassisSlots_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 6, 1, 3, 3),
    _ChassisSlots_Type()
)
chassisSlots.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chassisSlots.setStatus("mandatory")


class _ChassisFNB_Type(Integer32):
    """Custom type chassisFNB based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("absent", 1),
          ("present", 2))
    )


_ChassisFNB_Type.__name__ = "Integer32"
_ChassisFNB_Object = MibScalar
chassisFNB = _ChassisFNB_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 6, 1, 3, 4),
    _ChassisFNB_Type()
)
chassisFNB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chassisFNB.setStatus("mandatory")


class _ChassisAlarmEna_Type(Integer32):
    """Custom type chassisAlarmEna based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_ChassisAlarmEna_Type.__name__ = "Integer32"
_ChassisAlarmEna_Object = MibScalar
chassisAlarmEna = _ChassisAlarmEna_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 6, 1, 3, 5),
    _ChassisAlarmEna_Type()
)
chassisAlarmEna.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    chassisAlarmEna.setStatus("mandatory")


class _ChassisAlarmState_Type(Integer32):
    """Custom type chassisAlarmState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("chassisFaultCondition", 2),
          ("chassisNoFaultCondition", 1))
    )


_ChassisAlarmState_Type.__name__ = "Integer32"
_ChassisAlarmState_Object = MibScalar
chassisAlarmState = _ChassisAlarmState_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 6, 1, 3, 6),
    _ChassisAlarmState_Type()
)
chassisAlarmState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    chassisAlarmState.setStatus("mandatory")
_Environment_ObjectIdentity = ObjectIdentity
environment = _Environment_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 1, 6, 1, 4)
)
_PowerTable_Object = MibTable
powerTable = _PowerTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 6, 1, 4, 1)
)
if mibBuilder.loadTexts:
    powerTable.setStatus("mandatory")
_PowerEntry_Object = MibTableRow
powerEntry = _PowerEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 6, 1, 4, 1, 1)
)
powerEntry.setIndexNames(
    (0, "CTRON-COMMON-MIB", "powerSupplyNum"),
)
if mibBuilder.loadTexts:
    powerEntry.setStatus("mandatory")
_PowerSupplyNum_Type = Integer32
_PowerSupplyNum_Object = MibTableColumn
powerSupplyNum = _PowerSupplyNum_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 6, 1, 4, 1, 1, 1),
    _PowerSupplyNum_Type()
)
powerSupplyNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerSupplyNum.setStatus("mandatory")


class _PowerSupplyState_Type(Integer32):
    """Custom type powerSupplyState based on Integer32"""
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
        *(("infoNotAvailable", 1),
          ("installedAndNotOperating", 4),
          ("installedAndOperating", 3),
          ("notInstalled", 2))
    )


_PowerSupplyState_Type.__name__ = "Integer32"
_PowerSupplyState_Object = MibTableColumn
powerSupplyState = _PowerSupplyState_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 6, 1, 4, 1, 1, 2),
    _PowerSupplyState_Type()
)
powerSupplyState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerSupplyState.setStatus("mandatory")
_PowerSupplyId_Type = ObjectIdentifier
_PowerSupplyId_Object = MibTableColumn
powerSupplyId = _PowerSupplyId_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 6, 1, 4, 1, 1, 3),
    _PowerSupplyId_Type()
)
powerSupplyId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerSupplyId.setStatus("mandatory")


class _PowerSupplyRedun_Type(Integer32):
    """Custom type powerSupplyRedun based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("infoNotAvailable", 3),
          ("redundancyAvail", 1),
          ("redundancyNotAvail", 2))
    )


_PowerSupplyRedun_Type.__name__ = "Integer32"
_PowerSupplyRedun_Object = MibTableColumn
powerSupplyRedun = _PowerSupplyRedun_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 6, 1, 4, 1, 1, 4),
    _PowerSupplyRedun_Type()
)
powerSupplyRedun.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerSupplyRedun.setStatus("mandatory")


class _PowerSupplyRemoteDisable_Type(Integer32):
    """Custom type powerSupplyRemoteDisable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1),
          ("infoNotAvailable", 3))
    )


_PowerSupplyRemoteDisable_Type.__name__ = "Integer32"
_PowerSupplyRemoteDisable_Object = MibTableColumn
powerSupplyRemoteDisable = _PowerSupplyRemoteDisable_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 6, 1, 4, 1, 1, 5),
    _PowerSupplyRemoteDisable_Type()
)
powerSupplyRemoteDisable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    powerSupplyRemoteDisable.setStatus("mandatory")
_NB55_ObjectIdentity = ObjectIdentity
nB55 = _NB55_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 1, 6, 2, 3)
)
_NB55HWAddress_Type = PhysAddress
_NB55HWAddress_Object = MibScalar
nB55HWAddress = _NB55HWAddress_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 6, 2, 3, 1),
    _NB55HWAddress_Type()
)
nB55HWAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nB55HWAddress.setStatus("mandatory")
_NB55HWRev_Type = Integer32
_NB55HWRev_Object = MibScalar
nB55HWRev = _NB55HWRev_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 6, 2, 3, 2),
    _NB55HWRev_Type()
)
nB55HWRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nB55HWRev.setStatus("mandatory")


class _NB55FWRev_Type(OctetString):
    """Custom type nB55FWRev based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_NB55FWRev_Type.__name__ = "OctetString"
_NB55FWRev_Object = MibScalar
nB55FWRev = _NB55FWRev_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 6, 2, 3, 3),
    _NB55FWRev_Type()
)
nB55FWRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nB55FWRev.setStatus("mandatory")
_MRXI_ObjectIdentity = ObjectIdentity
mRXI = _MRXI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 1, 6, 2, 6)
)
_MRXIHWAddress_Type = PhysAddress
_MRXIHWAddress_Object = MibScalar
mRXIHWAddress = _MRXIHWAddress_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 6, 2, 6, 1),
    _MRXIHWAddress_Type()
)
mRXIHWAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mRXIHWAddress.setStatus("mandatory")
_MRXIHWRev_Type = Integer32
_MRXIHWRev_Object = MibScalar
mRXIHWRev = _MRXIHWRev_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 6, 2, 6, 2),
    _MRXIHWRev_Type()
)
mRXIHWRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mRXIHWRev.setStatus("mandatory")


class _MRXIFWRev_Type(OctetString):
    """Custom type mRXIFWRev based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_MRXIFWRev_Type.__name__ = "OctetString"
_MRXIFWRev_Object = MibScalar
mRXIFWRev = _MRXIFWRev_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 6, 2, 6, 3),
    _MRXIFWRev_Type()
)
mRXIFWRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mRXIFWRev.setStatus("mandatory")
_IRM3_ObjectIdentity = ObjectIdentity
iRM3 = _IRM3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 1, 6, 2, 7)
)
_IRM3HWAddress_Type = PhysAddress
_IRM3HWAddress_Object = MibScalar
iRM3HWAddress = _IRM3HWAddress_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 6, 2, 7, 1),
    _IRM3HWAddress_Type()
)
iRM3HWAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iRM3HWAddress.setStatus("mandatory")
_IRM3HWRev_Type = Integer32
_IRM3HWRev_Object = MibScalar
iRM3HWRev = _IRM3HWRev_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 6, 2, 7, 2),
    _IRM3HWRev_Type()
)
iRM3HWRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iRM3HWRev.setStatus("mandatory")


class _IRM3FWRev_Type(OctetString):
    """Custom type iRM3FWRev based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_IRM3FWRev_Type.__name__ = "OctetString"
_IRM3FWRev_Object = MibScalar
iRM3FWRev = _IRM3FWRev_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 6, 2, 7, 3),
    _IRM3FWRev_Type()
)
iRM3FWRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iRM3FWRev.setStatus("mandatory")


class _IRM3PortAssoc_Type(Integer32):
    """Custom type iRM3PortAssoc based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("aoffFrp", 5),
          ("arpFoff", 6))
    )


_IRM3PortAssoc_Type.__name__ = "Integer32"
_IRM3PortAssoc_Object = MibScalar
iRM3PortAssoc = _IRM3PortAssoc_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 6, 2, 7, 4),
    _IRM3PortAssoc_Type()
)
iRM3PortAssoc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iRM3PortAssoc.setStatus("mandatory")


class _IRM3BPSupport_Type(Integer32):
    """Custom type iRM3BPSupport based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("notSupported", 1),
          ("supported", 2))
    )


_IRM3BPSupport_Type.__name__ = "Integer32"
_IRM3BPSupport_Object = MibScalar
iRM3BPSupport = _IRM3BPSupport_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 6, 2, 7, 5),
    _IRM3BPSupport_Type()
)
iRM3BPSupport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iRM3BPSupport.setStatus("mandatory")
_TRMM_ObjectIdentity = ObjectIdentity
tRMM = _TRMM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 1, 6, 2, 8)
)
_TRMMHWAddress_Type = PhysAddress
_TRMMHWAddress_Object = MibScalar
tRMMHWAddress = _TRMMHWAddress_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 6, 2, 8, 1),
    _TRMMHWAddress_Type()
)
tRMMHWAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tRMMHWAddress.setStatus("mandatory")
_TRMMHWRev_Type = Integer32
_TRMMHWRev_Object = MibScalar
tRMMHWRev = _TRMMHWRev_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 6, 2, 8, 2),
    _TRMMHWRev_Type()
)
tRMMHWRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tRMMHWRev.setStatus("mandatory")


class _TRMMFWRev_Type(OctetString):
    """Custom type tRMMFWRev based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_TRMMFWRev_Type.__name__ = "OctetString"
_TRMMFWRev_Object = MibScalar
tRMMFWRev = _TRMMFWRev_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 6, 2, 8, 3),
    _TRMMFWRev_Type()
)
tRMMFWRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tRMMFWRev.setStatus("mandatory")
_EMME_ObjectIdentity = ObjectIdentity
eMME = _EMME_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 1, 6, 2, 9)
)
_EMMEHWAddress_Type = PhysAddress
_EMMEHWAddress_Object = MibScalar
eMMEHWAddress = _EMMEHWAddress_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 6, 2, 9, 1),
    _EMMEHWAddress_Type()
)
eMMEHWAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eMMEHWAddress.setStatus("mandatory")
_EMMEHWRev_Type = Integer32
_EMMEHWRev_Object = MibScalar
eMMEHWRev = _EMMEHWRev_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 6, 2, 9, 2),
    _EMMEHWRev_Type()
)
eMMEHWRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eMMEHWRev.setStatus("mandatory")


class _EMMEFWRev_Type(OctetString):
    """Custom type eMMEFWRev based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 10),
    )


_EMMEFWRev_Type.__name__ = "OctetString"
_EMMEFWRev_Object = MibScalar
eMMEFWRev = _EMMEFWRev_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 6, 2, 9, 3),
    _EMMEFWRev_Type()
)
eMMEFWRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eMMEFWRev.setStatus("mandatory")
_EMMEBoardMap_Type = Integer32
_EMMEBoardMap_Object = MibScalar
eMMEBoardMap = _EMMEBoardMap_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 6, 2, 9, 4),
    _EMMEBoardMap_Type()
)
eMMEBoardMap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eMMEBoardMap.setStatus("mandatory")
_FPRedundancy_ObjectIdentity = ObjectIdentity
fPRedundancy = _FPRedundancy_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 1, 6, 2, 10)
)
_FPRedund_ObjectIdentity = ObjectIdentity
fPRedund = _FPRedund_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 1, 6, 2, 10, 1)
)


class _FPRedundReset_Type(Integer32):
    """Custom type fPRedundReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noReset", 1),
          ("reset", 2))
    )


_FPRedundReset_Type.__name__ = "Integer32"
_FPRedundReset_Object = MibScalar
fPRedundReset = _FPRedundReset_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 6, 2, 10, 1, 1),
    _FPRedundReset_Type()
)
fPRedundReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fPRedundReset.setStatus("mandatory")
_FPRedundPollInterval_Type = Integer32
_FPRedundPollInterval_Object = MibScalar
fPRedundPollInterval = _FPRedundPollInterval_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 6, 2, 10, 1, 2),
    _FPRedundPollInterval_Type()
)
fPRedundPollInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fPRedundPollInterval.setStatus("mandatory")
_FPRedundRetrys_Type = Integer32
_FPRedundRetrys_Object = MibScalar
fPRedundRetrys = _FPRedundRetrys_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 6, 2, 10, 1, 3),
    _FPRedundRetrys_Type()
)
fPRedundRetrys.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fPRedundRetrys.setStatus("mandatory")
_FPRedundNumAddr_Type = Integer32
_FPRedundNumAddr_Object = MibScalar
fPRedundNumAddr = _FPRedundNumAddr_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 6, 2, 10, 1, 4),
    _FPRedundNumAddr_Type()
)
fPRedundNumAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fPRedundNumAddr.setStatus("mandatory")
_FPRedundAddAddr_Type = IpAddress
_FPRedundAddAddr_Object = MibScalar
fPRedundAddAddr = _FPRedundAddAddr_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 6, 2, 10, 1, 5),
    _FPRedundAddAddr_Type()
)
fPRedundAddAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fPRedundAddAddr.setStatus("mandatory")
_FPRedundDelAddr_Type = IpAddress
_FPRedundDelAddr_Object = MibScalar
fPRedundDelAddr = _FPRedundDelAddr_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 6, 2, 10, 1, 6),
    _FPRedundDelAddr_Type()
)
fPRedundDelAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fPRedundDelAddr.setStatus("mandatory")
_FPRedundActivePort_Type = Integer32
_FPRedundActivePort_Object = MibScalar
fPRedundActivePort = _FPRedundActivePort_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 6, 2, 10, 1, 7),
    _FPRedundActivePort_Type()
)
fPRedundActivePort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fPRedundActivePort.setStatus("mandatory")


class _FPRedundEnable_Type(Integer32):
    """Custom type fPRedundEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_FPRedundEnable_Type.__name__ = "Integer32"
_FPRedundEnable_Object = MibScalar
fPRedundEnable = _FPRedundEnable_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 6, 2, 10, 1, 8),
    _FPRedundEnable_Type()
)
fPRedundEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fPRedundEnable.setStatus("mandatory")
_FPRedundAddrTable_Object = MibTable
fPRedundAddrTable = _FPRedundAddrTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 6, 2, 10, 2)
)
if mibBuilder.loadTexts:
    fPRedundAddrTable.setStatus("mandatory")
_FPRedundAddrEntry_Object = MibTableRow
fPRedundAddrEntry = _FPRedundAddrEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 6, 2, 10, 2, 1)
)
fPRedundAddrEntry.setIndexNames(
    (0, "CTRON-COMMON-MIB", "fPRedundAddrId"),
)
if mibBuilder.loadTexts:
    fPRedundAddrEntry.setStatus("mandatory")
_FPRedundAddrId_Type = Integer32
_FPRedundAddrId_Object = MibTableColumn
fPRedundAddrId = _FPRedundAddrId_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 6, 2, 10, 2, 1, 1),
    _FPRedundAddrId_Type()
)
fPRedundAddrId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fPRedundAddrId.setStatus("mandatory")
_FPRedundAddrIPAddr_Type = IpAddress
_FPRedundAddrIPAddr_Object = MibTableColumn
fPRedundAddrIPAddr = _FPRedundAddrIPAddr_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 6, 2, 10, 2, 1, 2),
    _FPRedundAddrIPAddr_Type()
)
fPRedundAddrIPAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fPRedundAddrIPAddr.setStatus("mandatory")
_UpsVersion_ObjectIdentity = ObjectIdentity
upsVersion = _UpsVersion_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 1, 6, 3, 1)
)
_UpsRevision_ObjectIdentity = ObjectIdentity
upsRevision = _UpsRevision_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 1, 6, 3, 1, 1)
)


class _UpsID_Type(Integer32):
    """Custom type upsID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              257,
              258,
              259,
              260,
              261,
              262)
        )
    )
    namedValues = NamedValues(
        *(("aPCModel1250", 261),
          ("aPCModel2000", 262),
          ("aPCModel370", 257),
          ("aPCModel400", 258),
          ("aPCModel600", 259),
          ("aPCModel900", 260),
          ("other", 1))
    )


_UpsID_Type.__name__ = "Integer32"
_UpsID_Object = MibScalar
upsID = _UpsID_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 6, 3, 1, 1, 1),
    _UpsID_Type()
)
upsID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsID.setStatus("mandatory")
_UpsUpTime_Type = Integer32
_UpsUpTime_Object = MibScalar
upsUpTime = _UpsUpTime_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 6, 3, 1, 1, 2),
    _UpsUpTime_Type()
)
upsUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsUpTime.setStatus("mandatory")
_UpsDisable_Type = Integer32
_UpsDisable_Object = MibScalar
upsDisable = _UpsDisable_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 6, 3, 1, 1, 3),
    _UpsDisable_Type()
)
upsDisable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsDisable.setStatus("deprecated")
_UpsDisconnect_Type = Integer32
_UpsDisconnect_Object = MibScalar
upsDisconnect = _UpsDisconnect_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 6, 3, 1, 1, 4),
    _UpsDisconnect_Type()
)
upsDisconnect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsDisconnect.setStatus("mandatory")


class _UpsTest_Type(Integer32):
    """Custom type upsTest based on Integer32"""
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
        *(("badBattery", 3),
          ("noRecentTest", 4),
          ("underTest", 5),
          ("unitFailed", 2),
          ("unitOK", 1))
    )


_UpsTest_Type.__name__ = "Integer32"
_UpsTest_Object = MibScalar
upsTest = _UpsTest_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 6, 3, 1, 1, 5),
    _UpsTest_Type()
)
upsTest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsTest.setStatus("mandatory")
_UpsBatteryCapacity_Type = Integer32
_UpsBatteryCapacity_Object = MibScalar
upsBatteryCapacity = _UpsBatteryCapacity_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 6, 3, 1, 1, 6),
    _UpsBatteryCapacity_Type()
)
upsBatteryCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsBatteryCapacity.setStatus("mandatory")
_UpsACLineVoltsIn_Type = Integer32
_UpsACLineVoltsIn_Object = MibScalar
upsACLineVoltsIn = _UpsACLineVoltsIn_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 6, 3, 1, 1, 7),
    _UpsACLineVoltsIn_Type()
)
upsACLineVoltsIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsACLineVoltsIn.setStatus("mandatory")
_UpsBatteryVoltsOut_Type = Integer32
_UpsBatteryVoltsOut_Object = MibScalar
upsBatteryVoltsOut = _UpsBatteryVoltsOut_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 6, 3, 1, 1, 8),
    _UpsBatteryVoltsOut_Type()
)
upsBatteryVoltsOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsBatteryVoltsOut.setStatus("mandatory")
_DlForceOnBoot_Type = Integer32
_DlForceOnBoot_Object = MibScalar
dlForceOnBoot = _DlForceOnBoot_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 6, 4, 1),
    _DlForceOnBoot_Type()
)
dlForceOnBoot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dlForceOnBoot.setStatus("mandatory")
_DlCommitRAMToFlash_Type = Integer32
_DlCommitRAMToFlash_Object = MibScalar
dlCommitRAMToFlash = _DlCommitRAMToFlash_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 6, 4, 2),
    _DlCommitRAMToFlash_Type()
)
dlCommitRAMToFlash.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dlCommitRAMToFlash.setStatus("mandatory")
_DlInitiateColdBoot_Type = Integer32
_DlInitiateColdBoot_Object = MibScalar
dlInitiateColdBoot = _DlInitiateColdBoot_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 6, 4, 3),
    _DlInitiateColdBoot_Type()
)
dlInitiateColdBoot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dlInitiateColdBoot.setStatus("mandatory")
_DlTFTPRequestHost_Type = IpAddress
_DlTFTPRequestHost_Object = MibScalar
dlTFTPRequestHost = _DlTFTPRequestHost_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 6, 4, 4),
    _DlTFTPRequestHost_Type()
)
dlTFTPRequestHost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dlTFTPRequestHost.setStatus("mandatory")
_DlTFTPRequest_Type = DisplayString
_DlTFTPRequest_Object = MibScalar
dlTFTPRequest = _DlTFTPRequest_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 6, 4, 5),
    _DlTFTPRequest_Type()
)
dlTFTPRequest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dlTFTPRequest.setStatus("mandatory")
_DlLastImageFilename_Type = DisplayString
_DlLastImageFilename_Object = MibScalar
dlLastImageFilename = _DlLastImageFilename_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 6, 4, 6),
    _DlLastImageFilename_Type()
)
dlLastImageFilename.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlLastImageFilename.setStatus("mandatory")
_DlLastServerIPAddress_Type = IpAddress
_DlLastServerIPAddress_Object = MibScalar
dlLastServerIPAddress = _DlLastServerIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 6, 4, 7),
    _DlLastServerIPAddress_Type()
)
dlLastServerIPAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlLastServerIPAddress.setStatus("mandatory")
_DlFlashSize_Type = Integer32
_DlFlashSize_Object = MibScalar
dlFlashSize = _DlFlashSize_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 6, 4, 8),
    _DlFlashSize_Type()
)
dlFlashSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlFlashSize.setStatus("mandatory")
_DlFlashCount_Type = Integer32
_DlFlashCount_Object = MibScalar
dlFlashCount = _DlFlashCount_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 6, 4, 9),
    _DlFlashCount_Type()
)
dlFlashCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlFlashCount.setStatus("mandatory")
_DlFirmwareBase_Type = Integer32
_DlFirmwareBase_Object = MibScalar
dlFirmwareBase = _DlFirmwareBase_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 6, 4, 10),
    _DlFirmwareBase_Type()
)
dlFirmwareBase.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlFirmwareBase.setStatus("mandatory")
_DlFirmwareTop_Type = Integer32
_DlFirmwareTop_Object = MibScalar
dlFirmwareTop = _DlFirmwareTop_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 6, 4, 11),
    _DlFirmwareTop_Type()
)
dlFirmwareTop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlFirmwareTop.setStatus("mandatory")
_DlFirmwareStart_Type = Integer32
_DlFirmwareStart_Object = MibScalar
dlFirmwareStart = _DlFirmwareStart_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 6, 4, 12),
    _DlFirmwareStart_Type()
)
dlFirmwareStart.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlFirmwareStart.setStatus("mandatory")


class _DlBootRev_Type(OctetString):
    """Custom type dlBootRev based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_DlBootRev_Type.__name__ = "OctetString"
_DlBootRev_Object = MibScalar
dlBootRev = _DlBootRev_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 6, 4, 13),
    _DlBootRev_Type()
)
dlBootRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlBootRev.setStatus("mandatory")
_DlForceBootp_Type = Integer32
_DlForceBootp_Object = MibScalar
dlForceBootp = _DlForceBootp_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 6, 4, 14),
    _DlForceBootp_Type()
)
dlForceBootp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dlForceBootp.setStatus("mandatory")
_DlServerName_Type = OctetString
_DlServerName_Object = MibScalar
dlServerName = _DlServerName_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 6, 4, 15),
    _DlServerName_Type()
)
dlServerName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dlServerName.setStatus("mandatory")


class _DlOnLineDownLoad_Type(Integer32):
    """Custom type dlOnLineDownLoad based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("forceDownLoad", 2),
          ("forceDownLoadReset", 3),
          ("normalOperation", 1))
    )


_DlOnLineDownLoad_Type.__name__ = "Integer32"
_DlOnLineDownLoad_Object = MibScalar
dlOnLineDownLoad = _DlOnLineDownLoad_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 6, 4, 16),
    _DlOnLineDownLoad_Type()
)
dlOnLineDownLoad.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dlOnLineDownLoad.setStatus("mandatory")


class _DlOperStatus_Type(Integer32):
    """Custom type dlOperStatus based on Integer32"""
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
        *(("downLoadActive", 4),
          ("downLoadCompleteError", 5),
          ("normalOperation", 3),
          ("other", 1),
          ("unknown", 2))
    )


_DlOperStatus_Type.__name__ = "Integer32"
_DlOperStatus_Object = MibScalar
dlOperStatus = _DlOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 6, 4, 17),
    _DlOperStatus_Type()
)
dlOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlOperStatus.setStatus("mandatory")
_DlNetAddress_Type = IpAddress
_DlNetAddress_Object = MibScalar
dlNetAddress = _DlNetAddress_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 6, 4, 18),
    _DlNetAddress_Type()
)
dlNetAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dlNetAddress.setStatus("mandatory")


class _DlFileName_Type(OctetString):
    """Custom type dlFileName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_DlFileName_Type.__name__ = "OctetString"
_DlFileName_Object = MibScalar
dlFileName = _DlFileName_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 6, 4, 19),
    _DlFileName_Type()
)
dlFileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dlFileName.setStatus("mandatory")
_DlErrorString_Type = DisplayString
_DlErrorString_Object = MibScalar
dlErrorString = _DlErrorString_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 6, 4, 20),
    _DlErrorString_Type()
)
dlErrorString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlErrorString.setStatus("mandatory")
_DlTftpServerGatewayIPAddress_Type = IpAddress
_DlTftpServerGatewayIPAddress_Object = MibScalar
dlTftpServerGatewayIPAddress = _DlTftpServerGatewayIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 6, 4, 21),
    _DlTftpServerGatewayIPAddress_Type()
)
dlTftpServerGatewayIPAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dlTftpServerGatewayIPAddress.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CTRON-COMMON-MIB",
    **{"deviceType": deviceType,
       "deviceName": deviceName,
       "deviceIPAddress": deviceIPAddress,
       "deviceTime": deviceTime,
       "deviceDate": deviceDate,
       "fnb2": fnb2,
       "fnbTR": fnbTR,
       "fnbTRTable": fnbTRTable,
       "fnbTREntry": fnbTREntry,
       "fnbTRIndex": fnbTRIndex,
       "fnbConnectLeft": fnbConnectLeft,
       "fnbConnectRight": fnbConnectRight,
       "fnbBypass": fnbBypass,
       "fnbRPBypass": fnbRPBypass,
       "fnbCSMACD": fnbCSMACD,
       "fnbCSMACDTable": fnbCSMACDTable,
       "fnbCSMACDEntry": fnbCSMACDEntry,
       "fnbCSMACDIndex": fnbCSMACDIndex,
       "fnbConnect": fnbConnect,
       "fnbPortChanges": fnbPortChanges,
       "fnbPortConnect": fnbPortConnect,
       "fnbPortConnectTable": fnbPortConnectTable,
       "fnbPortConnectEntry": fnbPortConnectEntry,
       "fnbPortConnectBoardIndex": fnbPortConnectBoardIndex,
       "fnbPortConnectPortIndex": fnbPortConnectPortIndex,
       "fnbPortConnectPortAssignment": fnbPortConnectPortAssignment,
       "fnbPortConnectCompID": fnbPortConnectCompID,
       "fnbPortConnectionChanges": fnbPortConnectionChanges,
       "chassis": chassis,
       "chassisHWRev": chassisHWRev,
       "chassisType": chassisType,
       "chassisSlots": chassisSlots,
       "chassisFNB": chassisFNB,
       "chassisAlarmEna": chassisAlarmEna,
       "chassisAlarmState": chassisAlarmState,
       "environment": environment,
       "powerTable": powerTable,
       "powerEntry": powerEntry,
       "powerSupplyNum": powerSupplyNum,
       "powerSupplyState": powerSupplyState,
       "powerSupplyId": powerSupplyId,
       "powerSupplyRedun": powerSupplyRedun,
       "powerSupplyRemoteDisable": powerSupplyRemoteDisable,
       "nB55": nB55,
       "nB55HWAddress": nB55HWAddress,
       "nB55HWRev": nB55HWRev,
       "nB55FWRev": nB55FWRev,
       "mRXI": mRXI,
       "mRXIHWAddress": mRXIHWAddress,
       "mRXIHWRev": mRXIHWRev,
       "mRXIFWRev": mRXIFWRev,
       "iRM3": iRM3,
       "iRM3HWAddress": iRM3HWAddress,
       "iRM3HWRev": iRM3HWRev,
       "iRM3FWRev": iRM3FWRev,
       "iRM3PortAssoc": iRM3PortAssoc,
       "iRM3BPSupport": iRM3BPSupport,
       "tRMM": tRMM,
       "tRMMHWAddress": tRMMHWAddress,
       "tRMMHWRev": tRMMHWRev,
       "tRMMFWRev": tRMMFWRev,
       "eMME": eMME,
       "eMMEHWAddress": eMMEHWAddress,
       "eMMEHWRev": eMMEHWRev,
       "eMMEFWRev": eMMEFWRev,
       "eMMEBoardMap": eMMEBoardMap,
       "fPRedundancy": fPRedundancy,
       "fPRedund": fPRedund,
       "fPRedundReset": fPRedundReset,
       "fPRedundPollInterval": fPRedundPollInterval,
       "fPRedundRetrys": fPRedundRetrys,
       "fPRedundNumAddr": fPRedundNumAddr,
       "fPRedundAddAddr": fPRedundAddAddr,
       "fPRedundDelAddr": fPRedundDelAddr,
       "fPRedundActivePort": fPRedundActivePort,
       "fPRedundEnable": fPRedundEnable,
       "fPRedundAddrTable": fPRedundAddrTable,
       "fPRedundAddrEntry": fPRedundAddrEntry,
       "fPRedundAddrId": fPRedundAddrId,
       "fPRedundAddrIPAddr": fPRedundAddrIPAddr,
       "upsVersion": upsVersion,
       "upsRevision": upsRevision,
       "upsID": upsID,
       "upsUpTime": upsUpTime,
       "upsDisable": upsDisable,
       "upsDisconnect": upsDisconnect,
       "upsTest": upsTest,
       "upsBatteryCapacity": upsBatteryCapacity,
       "upsACLineVoltsIn": upsACLineVoltsIn,
       "upsBatteryVoltsOut": upsBatteryVoltsOut,
       "dlForceOnBoot": dlForceOnBoot,
       "dlCommitRAMToFlash": dlCommitRAMToFlash,
       "dlInitiateColdBoot": dlInitiateColdBoot,
       "dlTFTPRequestHost": dlTFTPRequestHost,
       "dlTFTPRequest": dlTFTPRequest,
       "dlLastImageFilename": dlLastImageFilename,
       "dlLastServerIPAddress": dlLastServerIPAddress,
       "dlFlashSize": dlFlashSize,
       "dlFlashCount": dlFlashCount,
       "dlFirmwareBase": dlFirmwareBase,
       "dlFirmwareTop": dlFirmwareTop,
       "dlFirmwareStart": dlFirmwareStart,
       "dlBootRev": dlBootRev,
       "dlForceBootp": dlForceBootp,
       "dlServerName": dlServerName,
       "dlOnLineDownLoad": dlOnLineDownLoad,
       "dlOperStatus": dlOperStatus,
       "dlNetAddress": dlNetAddress,
       "dlFileName": dlFileName,
       "dlErrorString": dlErrorString,
       "dlTftpServerGatewayIPAddress": dlTftpServerGatewayIPAddress}
)
