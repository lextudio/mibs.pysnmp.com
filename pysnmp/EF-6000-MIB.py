# SNMP MIB module (EF-6000-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/EF-6000-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:36:37 2024
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



class DisplayString(OctetString):
    """Custom type DisplayString based on OctetString"""




class Ef6000SysOperStatus(Integer32):
    """Custom type Ef6000SysOperStatus based on Integer32"""
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





class Ef6000FruCode(Integer32):
    """Custom type Ef6000FruCode based on Integer32"""
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
              16)
        )
    )
    namedValues = NamedValues(
        *(("fru-bkplane", 1),
          ("fru-ctp", 2),
          ("fru-fan", 5),
          ("fru-fan2", 4),
          ("fru-fint1", 16),
          ("fru-glsl", 8),
          ("fru-glsr", 13),
          ("fru-gsf1", 11),
          ("fru-gsf2", 12),
          ("fru-gsml", 9),
          ("fru-gsmr", 14),
          ("fru-gxxl", 10),
          ("fru-gxxr", 15),
          ("fru-power", 6),
          ("fru-reserved", 7),
          ("fru-sbar", 3))
    )





class Ef6000FruPosition(Integer32):
    """Custom type Ef6000FruPosition based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )





class Ef6000PortIndex(Integer32):
    """Custom type Ef6000PortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2048),
    )





class Ef6000PortPhyState(Integer32):
    """Custom type Ef6000PortPhyState based on Integer32"""
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
              13)
        )
    )
    namedValues = NamedValues(
        *(("psAvailable", 2),
          ("psBlocked", 3),
          ("psExtLoop", 8),
          ("psInaccessible", 12),
          ("psInactive", 13),
          ("psIntDiags", 7),
          ("psLR", 11),
          ("psLinkFailLOL", 6),
          ("psLinkFailure", 5),
          ("psNotInstalled", 1),
          ("psPortFail", 9),
          ("psSR", 10),
          ("psUnavailable", 4))
    )





class Ef6000PortWWN(OctetString):
    """Custom type Ef6000PortWWN based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )





class Ef6000PortList(OctetString):
    """Custom type Ef6000PortList based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(32, 32),
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
_Ef_6000_ObjectIdentity = ObjectIdentity
ef_6000 = _Ef_6000_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 289, 2, 1, 1, 2)
)
_Ef6000Sys_ObjectIdentity = ObjectIdentity
ef6000Sys = _Ef6000Sys_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 289, 2, 1, 1, 2, 1)
)


class _Ef6000SysCurrentDate_Type(DisplayString):
    """Custom type ef6000SysCurrentDate based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_Ef6000SysCurrentDate_Type.__name__ = "DisplayString"
_Ef6000SysCurrentDate_Object = MibScalar
ef6000SysCurrentDate = _Ef6000SysCurrentDate_Object(
    (1, 3, 6, 1, 4, 1, 289, 2, 1, 1, 2, 1, 1),
    _Ef6000SysCurrentDate_Type()
)
ef6000SysCurrentDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ef6000SysCurrentDate.setStatus("mandatory")


class _Ef6000SysBootDate_Type(DisplayString):
    """Custom type ef6000SysBootDate based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_Ef6000SysBootDate_Type.__name__ = "DisplayString"
_Ef6000SysBootDate_Object = MibScalar
ef6000SysBootDate = _Ef6000SysBootDate_Object(
    (1, 3, 6, 1, 4, 1, 289, 2, 1, 1, 2, 1, 2),
    _Ef6000SysBootDate_Type()
)
ef6000SysBootDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ef6000SysBootDate.setStatus("mandatory")


class _Ef6000SysFirmwareVersion_Type(DisplayString):
    """Custom type ef6000SysFirmwareVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 24),
    )


_Ef6000SysFirmwareVersion_Type.__name__ = "DisplayString"
_Ef6000SysFirmwareVersion_Object = MibScalar
ef6000SysFirmwareVersion = _Ef6000SysFirmwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 289, 2, 1, 1, 2, 1, 3),
    _Ef6000SysFirmwareVersion_Type()
)
ef6000SysFirmwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ef6000SysFirmwareVersion.setStatus("mandatory")


class _Ef6000SysTypeNum_Type(DisplayString):
    """Custom type ef6000SysTypeNum based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_Ef6000SysTypeNum_Type.__name__ = "DisplayString"
_Ef6000SysTypeNum_Object = MibScalar
ef6000SysTypeNum = _Ef6000SysTypeNum_Object(
    (1, 3, 6, 1, 4, 1, 289, 2, 1, 1, 2, 1, 4),
    _Ef6000SysTypeNum_Type()
)
ef6000SysTypeNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ef6000SysTypeNum.setStatus("mandatory")


class _Ef6000SysModelNum_Type(DisplayString):
    """Custom type ef6000SysModelNum based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_Ef6000SysModelNum_Type.__name__ = "DisplayString"
_Ef6000SysModelNum_Object = MibScalar
ef6000SysModelNum = _Ef6000SysModelNum_Object(
    (1, 3, 6, 1, 4, 1, 289, 2, 1, 1, 2, 1, 5),
    _Ef6000SysModelNum_Type()
)
ef6000SysModelNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ef6000SysModelNum.setStatus("mandatory")


class _Ef6000SysMfg_Type(DisplayString):
    """Custom type ef6000SysMfg based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_Ef6000SysMfg_Type.__name__ = "DisplayString"
_Ef6000SysMfg_Object = MibScalar
ef6000SysMfg = _Ef6000SysMfg_Object(
    (1, 3, 6, 1, 4, 1, 289, 2, 1, 1, 2, 1, 6),
    _Ef6000SysMfg_Type()
)
ef6000SysMfg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ef6000SysMfg.setStatus("mandatory")


class _Ef6000SysPlantOfMfg_Type(DisplayString):
    """Custom type ef6000SysPlantOfMfg based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_Ef6000SysPlantOfMfg_Type.__name__ = "DisplayString"
_Ef6000SysPlantOfMfg_Object = MibScalar
ef6000SysPlantOfMfg = _Ef6000SysPlantOfMfg_Object(
    (1, 3, 6, 1, 4, 1, 289, 2, 1, 1, 2, 1, 7),
    _Ef6000SysPlantOfMfg_Type()
)
ef6000SysPlantOfMfg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ef6000SysPlantOfMfg.setStatus("mandatory")


class _Ef6000SysEcLevel_Type(DisplayString):
    """Custom type ef6000SysEcLevel based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_Ef6000SysEcLevel_Type.__name__ = "DisplayString"
_Ef6000SysEcLevel_Object = MibScalar
ef6000SysEcLevel = _Ef6000SysEcLevel_Object(
    (1, 3, 6, 1, 4, 1, 289, 2, 1, 1, 2, 1, 8),
    _Ef6000SysEcLevel_Type()
)
ef6000SysEcLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ef6000SysEcLevel.setStatus("mandatory")


class _Ef6000SysSerialNum_Type(DisplayString):
    """Custom type ef6000SysSerialNum based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_Ef6000SysSerialNum_Type.__name__ = "DisplayString"
_Ef6000SysSerialNum_Object = MibScalar
ef6000SysSerialNum = _Ef6000SysSerialNum_Object(
    (1, 3, 6, 1, 4, 1, 289, 2, 1, 1, 2, 1, 9),
    _Ef6000SysSerialNum_Type()
)
ef6000SysSerialNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ef6000SysSerialNum.setStatus("mandatory")
_Ef6000SysOperStatus_Type = Ef6000SysOperStatus
_Ef6000SysOperStatus_Object = MibScalar
ef6000SysOperStatus = _Ef6000SysOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 289, 2, 1, 1, 2, 1, 10),
    _Ef6000SysOperStatus_Type()
)
ef6000SysOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ef6000SysOperStatus.setStatus("mandatory")


class _Ef6000SysState_Type(Integer32):
    """Custom type ef6000SysState based on Integer32"""
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


_Ef6000SysState_Type.__name__ = "Integer32"
_Ef6000SysState_Object = MibScalar
ef6000SysState = _Ef6000SysState_Object(
    (1, 3, 6, 1, 4, 1, 289, 2, 1, 1, 2, 1, 11),
    _Ef6000SysState_Type()
)
ef6000SysState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ef6000SysState.setStatus("mandatory")


class _Ef6000SysAdmStatus_Type(Integer32):
    """Custom type ef6000SysAdmStatus based on Integer32"""
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


_Ef6000SysAdmStatus_Type.__name__ = "Integer32"
_Ef6000SysAdmStatus_Object = MibScalar
ef6000SysAdmStatus = _Ef6000SysAdmStatus_Object(
    (1, 3, 6, 1, 4, 1, 289, 2, 1, 1, 2, 1, 12),
    _Ef6000SysAdmStatus_Type()
)
ef6000SysAdmStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ef6000SysAdmStatus.setStatus("mandatory")


class _Ef6000SysConfigSpeed_Type(Integer32):
    """Custom type ef6000SysConfigSpeed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("one-gig", 1),
          ("two-gig", 2))
    )


_Ef6000SysConfigSpeed_Type.__name__ = "Integer32"
_Ef6000SysConfigSpeed_Object = MibScalar
ef6000SysConfigSpeed = _Ef6000SysConfigSpeed_Object(
    (1, 3, 6, 1, 4, 1, 289, 2, 1, 1, 2, 1, 13),
    _Ef6000SysConfigSpeed_Type()
)
ef6000SysConfigSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ef6000SysConfigSpeed.setStatus("mandatory")
_Ef6000Fru_ObjectIdentity = ObjectIdentity
ef6000Fru = _Ef6000Fru_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 289, 2, 1, 1, 2, 2)
)
_Ef6000FruTable_Object = MibTable
ef6000FruTable = _Ef6000FruTable_Object(
    (1, 3, 6, 1, 4, 1, 289, 2, 1, 1, 2, 2, 1)
)
if mibBuilder.loadTexts:
    ef6000FruTable.setStatus("mandatory")
_Ef6000FruEntry_Object = MibTableRow
ef6000FruEntry = _Ef6000FruEntry_Object(
    (1, 3, 6, 1, 4, 1, 289, 2, 1, 1, 2, 2, 1, 1)
)
ef6000FruEntry.setIndexNames(
    (0, "EF-6000-MIB", "ef6000FruCode"),
    (0, "EF-6000-MIB", "ef6000FruPosition"),
)
if mibBuilder.loadTexts:
    ef6000FruEntry.setStatus("mandatory")
_Ef6000FruCode_Type = Ef6000FruCode
_Ef6000FruCode_Object = MibTableColumn
ef6000FruCode = _Ef6000FruCode_Object(
    (1, 3, 6, 1, 4, 1, 289, 2, 1, 1, 2, 2, 1, 1, 1),
    _Ef6000FruCode_Type()
)
ef6000FruCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ef6000FruCode.setStatus("mandatory")
_Ef6000FruPosition_Type = Ef6000FruPosition
_Ef6000FruPosition_Object = MibTableColumn
ef6000FruPosition = _Ef6000FruPosition_Object(
    (1, 3, 6, 1, 4, 1, 289, 2, 1, 1, 2, 2, 1, 1, 2),
    _Ef6000FruPosition_Type()
)
ef6000FruPosition.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ef6000FruPosition.setStatus("mandatory")


class _Ef6000FruStatus_Type(Integer32):
    """Custom type ef6000FruStatus based on Integer32"""
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
        *(("active", 1),
          ("backup", 2),
          ("failed", 4),
          ("update-busy", 3))
    )


_Ef6000FruStatus_Type.__name__ = "Integer32"
_Ef6000FruStatus_Object = MibTableColumn
ef6000FruStatus = _Ef6000FruStatus_Object(
    (1, 3, 6, 1, 4, 1, 289, 2, 1, 1, 2, 2, 1, 1, 3),
    _Ef6000FruStatus_Type()
)
ef6000FruStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ef6000FruStatus.setStatus("mandatory")


class _Ef6000FruPartNumber_Type(DisplayString):
    """Custom type ef6000FruPartNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_Ef6000FruPartNumber_Type.__name__ = "DisplayString"
_Ef6000FruPartNumber_Object = MibTableColumn
ef6000FruPartNumber = _Ef6000FruPartNumber_Object(
    (1, 3, 6, 1, 4, 1, 289, 2, 1, 1, 2, 2, 1, 1, 4),
    _Ef6000FruPartNumber_Type()
)
ef6000FruPartNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ef6000FruPartNumber.setStatus("mandatory")


class _Ef6000FruSerialNumber_Type(DisplayString):
    """Custom type ef6000FruSerialNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_Ef6000FruSerialNumber_Type.__name__ = "DisplayString"
_Ef6000FruSerialNumber_Object = MibTableColumn
ef6000FruSerialNumber = _Ef6000FruSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 289, 2, 1, 1, 2, 2, 1, 1, 5),
    _Ef6000FruSerialNumber_Type()
)
ef6000FruSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ef6000FruSerialNumber.setStatus("mandatory")
_Ef6000FruPowerOnHours_Type = Counter32
_Ef6000FruPowerOnHours_Object = MibTableColumn
ef6000FruPowerOnHours = _Ef6000FruPowerOnHours_Object(
    (1, 3, 6, 1, 4, 1, 289, 2, 1, 1, 2, 2, 1, 1, 6),
    _Ef6000FruPowerOnHours_Type()
)
ef6000FruPowerOnHours.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ef6000FruPowerOnHours.setStatus("mandatory")


class _Ef6000FruTestDate_Type(DisplayString):
    """Custom type ef6000FruTestDate based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_Ef6000FruTestDate_Type.__name__ = "DisplayString"
_Ef6000FruTestDate_Object = MibTableColumn
ef6000FruTestDate = _Ef6000FruTestDate_Object(
    (1, 3, 6, 1, 4, 1, 289, 2, 1, 1, 2, 2, 1, 1, 7),
    _Ef6000FruTestDate_Type()
)
ef6000FruTestDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ef6000FruTestDate.setStatus("mandatory")
_Ef6000Port_ObjectIdentity = ObjectIdentity
ef6000Port = _Ef6000Port_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 289, 2, 1, 1, 2, 3)
)
_Ef6000PortTable_Object = MibTable
ef6000PortTable = _Ef6000PortTable_Object(
    (1, 3, 6, 1, 4, 1, 289, 2, 1, 1, 2, 3, 1)
)
if mibBuilder.loadTexts:
    ef6000PortTable.setStatus("mandatory")
_Ef6000PortEntry_Object = MibTableRow
ef6000PortEntry = _Ef6000PortEntry_Object(
    (1, 3, 6, 1, 4, 1, 289, 2, 1, 1, 2, 3, 1, 1)
)
ef6000PortEntry.setIndexNames(
    (0, "EF-6000-MIB", "ef6000PortIndex"),
)
if mibBuilder.loadTexts:
    ef6000PortEntry.setStatus("mandatory")
_Ef6000PortIndex_Type = Ef6000PortIndex
_Ef6000PortIndex_Object = MibTableColumn
ef6000PortIndex = _Ef6000PortIndex_Object(
    (1, 3, 6, 1, 4, 1, 289, 2, 1, 1, 2, 3, 1, 1, 1),
    _Ef6000PortIndex_Type()
)
ef6000PortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ef6000PortIndex.setStatus("mandatory")
_Ef6000PortPhyState_Type = Ef6000PortPhyState
_Ef6000PortPhyState_Object = MibTableColumn
ef6000PortPhyState = _Ef6000PortPhyState_Object(
    (1, 3, 6, 1, 4, 1, 289, 2, 1, 1, 2, 3, 1, 1, 2),
    _Ef6000PortPhyState_Type()
)
ef6000PortPhyState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ef6000PortPhyState.setStatus("mandatory")


class _Ef6000PortOpStatus_Type(Integer32):
    """Custom type ef6000PortOpStatus based on Integer32"""
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


_Ef6000PortOpStatus_Type.__name__ = "Integer32"
_Ef6000PortOpStatus_Object = MibTableColumn
ef6000PortOpStatus = _Ef6000PortOpStatus_Object(
    (1, 3, 6, 1, 4, 1, 289, 2, 1, 1, 2, 3, 1, 1, 3),
    _Ef6000PortOpStatus_Type()
)
ef6000PortOpStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ef6000PortOpStatus.setStatus("mandatory")


class _Ef6000PortAdmStatus_Type(Integer32):
    """Custom type ef6000PortAdmStatus based on Integer32"""
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


_Ef6000PortAdmStatus_Type.__name__ = "Integer32"
_Ef6000PortAdmStatus_Object = MibTableColumn
ef6000PortAdmStatus = _Ef6000PortAdmStatus_Object(
    (1, 3, 6, 1, 4, 1, 289, 2, 1, 1, 2, 3, 1, 1, 4),
    _Ef6000PortAdmStatus_Type()
)
ef6000PortAdmStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ef6000PortAdmStatus.setStatus("mandatory")


class _Ef6000PortConnector_Type(Integer32):
    """Custom type ef6000PortConnector based on Integer32"""
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
        *(("internal-port", 5),
          ("lc", 2),
          ("mt-rj", 3),
          ("mu", 4),
          ("unknown", 1))
    )


_Ef6000PortConnector_Type.__name__ = "Integer32"
_Ef6000PortConnector_Object = MibTableColumn
ef6000PortConnector = _Ef6000PortConnector_Object(
    (1, 3, 6, 1, 4, 1, 289, 2, 1, 1, 2, 3, 1, 1, 5),
    _Ef6000PortConnector_Type()
)
ef6000PortConnector.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ef6000PortConnector.setStatus("mandatory")


class _Ef6000PortDistance_Type(Integer32):
    """Custom type ef6000PortDistance based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 127),
    )


_Ef6000PortDistance_Type.__name__ = "Integer32"
_Ef6000PortDistance_Object = MibTableColumn
ef6000PortDistance = _Ef6000PortDistance_Object(
    (1, 3, 6, 1, 4, 1, 289, 2, 1, 1, 2, 3, 1, 1, 6),
    _Ef6000PortDistance_Type()
)
ef6000PortDistance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ef6000PortDistance.setStatus("mandatory")


class _Ef6000PortType_Type(Integer32):
    """Custom type ef6000PortType based on Integer32"""
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
        *(("longDistance", 2),
          ("longWaveLaser-LC", 6),
          ("longWaveLaser-LL", 3),
          ("shortWaveLaser-OFC", 4),
          ("shortWaveLaser-noOFC", 5),
          ("unknown", 1))
    )


_Ef6000PortType_Type.__name__ = "Integer32"
_Ef6000PortType_Object = MibTableColumn
ef6000PortType = _Ef6000PortType_Object(
    (1, 3, 6, 1, 4, 1, 289, 2, 1, 1, 2, 3, 1, 1, 7),
    _Ef6000PortType_Type()
)
ef6000PortType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ef6000PortType.setStatus("mandatory")


class _Ef6000PortMedia_Type(Integer32):
    """Custom type ef6000PortMedia based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 127),
    )


_Ef6000PortMedia_Type.__name__ = "Integer32"
_Ef6000PortMedia_Object = MibTableColumn
ef6000PortMedia = _Ef6000PortMedia_Object(
    (1, 3, 6, 1, 4, 1, 289, 2, 1, 1, 2, 3, 1, 1, 8),
    _Ef6000PortMedia_Type()
)
ef6000PortMedia.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ef6000PortMedia.setStatus("mandatory")


class _Ef6000PortSpeedCap_Type(Integer32):
    """Custom type ef6000PortSpeedCap based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 127),
    )


_Ef6000PortSpeedCap_Type.__name__ = "Integer32"
_Ef6000PortSpeedCap_Object = MibTableColumn
ef6000PortSpeedCap = _Ef6000PortSpeedCap_Object(
    (1, 3, 6, 1, 4, 1, 289, 2, 1, 1, 2, 3, 1, 1, 9),
    _Ef6000PortSpeedCap_Type()
)
ef6000PortSpeedCap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ef6000PortSpeedCap.setStatus("mandatory")


class _Ef6000PortConfigSpeed_Type(Integer32):
    """Custom type ef6000PortConfigSpeed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("negotiate", 3),
          ("one-gig", 1),
          ("two-gig", 2))
    )


_Ef6000PortConfigSpeed_Type.__name__ = "Integer32"
_Ef6000PortConfigSpeed_Object = MibTableColumn
ef6000PortConfigSpeed = _Ef6000PortConfigSpeed_Object(
    (1, 3, 6, 1, 4, 1, 289, 2, 1, 1, 2, 3, 1, 1, 10),
    _Ef6000PortConfigSpeed_Type()
)
ef6000PortConfigSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ef6000PortConfigSpeed.setStatus("mandatory")


class _Ef6000PortSpeed_Type(Integer32):
    """Custom type ef6000PortSpeed based on Integer32"""
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
        *(("negotiate", 4),
          ("one-gig", 2),
          ("two-gig", 3),
          ("unknown", 1))
    )


_Ef6000PortSpeed_Type.__name__ = "Integer32"
_Ef6000PortSpeed_Object = MibTableColumn
ef6000PortSpeed = _Ef6000PortSpeed_Object(
    (1, 3, 6, 1, 4, 1, 289, 2, 1, 1, 2, 3, 1, 1, 11),
    _Ef6000PortSpeed_Type()
)
ef6000PortSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ef6000PortSpeed.setStatus("mandatory")
_Ef6000PortTxWords32_Type = Counter32
_Ef6000PortTxWords32_Object = MibTableColumn
ef6000PortTxWords32 = _Ef6000PortTxWords32_Object(
    (1, 3, 6, 1, 4, 1, 289, 2, 1, 1, 2, 3, 1, 1, 20),
    _Ef6000PortTxWords32_Type()
)
ef6000PortTxWords32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ef6000PortTxWords32.setStatus("mandatory")
_Ef6000PortRxWords32_Type = Counter32
_Ef6000PortRxWords32_Object = MibTableColumn
ef6000PortRxWords32 = _Ef6000PortRxWords32_Object(
    (1, 3, 6, 1, 4, 1, 289, 2, 1, 1, 2, 3, 1, 1, 21),
    _Ef6000PortRxWords32_Type()
)
ef6000PortRxWords32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ef6000PortRxWords32.setStatus("mandatory")
_Ef6000PortTxFrames32_Type = Counter32
_Ef6000PortTxFrames32_Object = MibTableColumn
ef6000PortTxFrames32 = _Ef6000PortTxFrames32_Object(
    (1, 3, 6, 1, 4, 1, 289, 2, 1, 1, 2, 3, 1, 1, 22),
    _Ef6000PortTxFrames32_Type()
)
ef6000PortTxFrames32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ef6000PortTxFrames32.setStatus("mandatory")
_Ef6000PortRxFrames32_Type = Counter32
_Ef6000PortRxFrames32_Object = MibTableColumn
ef6000PortRxFrames32 = _Ef6000PortRxFrames32_Object(
    (1, 3, 6, 1, 4, 1, 289, 2, 1, 1, 2, 3, 1, 1, 23),
    _Ef6000PortRxFrames32_Type()
)
ef6000PortRxFrames32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ef6000PortRxFrames32.setStatus("mandatory")
_Ef6000PortTxThroughput_Type = Counter32
_Ef6000PortTxThroughput_Object = MibTableColumn
ef6000PortTxThroughput = _Ef6000PortTxThroughput_Object(
    (1, 3, 6, 1, 4, 1, 289, 2, 1, 1, 2, 3, 1, 1, 24),
    _Ef6000PortTxThroughput_Type()
)
ef6000PortTxThroughput.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ef6000PortTxThroughput.setStatus("mandatory")
_Ef6000PortRxThroughput_Type = Counter32
_Ef6000PortRxThroughput_Object = MibTableColumn
ef6000PortRxThroughput = _Ef6000PortRxThroughput_Object(
    (1, 3, 6, 1, 4, 1, 289, 2, 1, 1, 2, 3, 1, 1, 25),
    _Ef6000PortRxThroughput_Type()
)
ef6000PortRxThroughput.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ef6000PortRxThroughput.setStatus("mandatory")
_Ef6000PortTxC2Words32_Type = Counter32
_Ef6000PortTxC2Words32_Object = MibTableColumn
ef6000PortTxC2Words32 = _Ef6000PortTxC2Words32_Object(
    (1, 3, 6, 1, 4, 1, 289, 2, 1, 1, 2, 3, 1, 1, 30),
    _Ef6000PortTxC2Words32_Type()
)
ef6000PortTxC2Words32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ef6000PortTxC2Words32.setStatus("mandatory")
_Ef6000PortRxC2Words32_Type = Counter32
_Ef6000PortRxC2Words32_Object = MibTableColumn
ef6000PortRxC2Words32 = _Ef6000PortRxC2Words32_Object(
    (1, 3, 6, 1, 4, 1, 289, 2, 1, 1, 2, 3, 1, 1, 31),
    _Ef6000PortRxC2Words32_Type()
)
ef6000PortRxC2Words32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ef6000PortRxC2Words32.setStatus("mandatory")
_Ef6000PortTxC2Frames32_Type = Counter32
_Ef6000PortTxC2Frames32_Object = MibTableColumn
ef6000PortTxC2Frames32 = _Ef6000PortTxC2Frames32_Object(
    (1, 3, 6, 1, 4, 1, 289, 2, 1, 1, 2, 3, 1, 1, 32),
    _Ef6000PortTxC2Frames32_Type()
)
ef6000PortTxC2Frames32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ef6000PortTxC2Frames32.setStatus("mandatory")
_Ef6000PortRxC2Frames32_Type = Counter32
_Ef6000PortRxC2Frames32_Object = MibTableColumn
ef6000PortRxC2Frames32 = _Ef6000PortRxC2Frames32_Object(
    (1, 3, 6, 1, 4, 1, 289, 2, 1, 1, 2, 3, 1, 1, 33),
    _Ef6000PortRxC2Frames32_Type()
)
ef6000PortRxC2Frames32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ef6000PortRxC2Frames32.setStatus("mandatory")
_Ef6000PortTxC2Octets32_Type = Counter32
_Ef6000PortTxC2Octets32_Object = MibTableColumn
ef6000PortTxC2Octets32 = _Ef6000PortTxC2Octets32_Object(
    (1, 3, 6, 1, 4, 1, 289, 2, 1, 1, 2, 3, 1, 1, 34),
    _Ef6000PortTxC2Octets32_Type()
)
ef6000PortTxC2Octets32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ef6000PortTxC2Octets32.setStatus("mandatory")
_Ef6000PortRxC2Octets32_Type = Counter32
_Ef6000PortRxC2Octets32_Object = MibTableColumn
ef6000PortRxC2Octets32 = _Ef6000PortRxC2Octets32_Object(
    (1, 3, 6, 1, 4, 1, 289, 2, 1, 1, 2, 3, 1, 1, 35),
    _Ef6000PortRxC2Octets32_Type()
)
ef6000PortRxC2Octets32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ef6000PortRxC2Octets32.setStatus("mandatory")
_Ef6000PortTxC3Words32_Type = Counter32
_Ef6000PortTxC3Words32_Object = MibTableColumn
ef6000PortTxC3Words32 = _Ef6000PortTxC3Words32_Object(
    (1, 3, 6, 1, 4, 1, 289, 2, 1, 1, 2, 3, 1, 1, 40),
    _Ef6000PortTxC3Words32_Type()
)
ef6000PortTxC3Words32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ef6000PortTxC3Words32.setStatus("mandatory")
_Ef6000PortRxC3Words32_Type = Counter32
_Ef6000PortRxC3Words32_Object = MibTableColumn
ef6000PortRxC3Words32 = _Ef6000PortRxC3Words32_Object(
    (1, 3, 6, 1, 4, 1, 289, 2, 1, 1, 2, 3, 1, 1, 41),
    _Ef6000PortRxC3Words32_Type()
)
ef6000PortRxC3Words32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ef6000PortRxC3Words32.setStatus("mandatory")
_Ef6000PortTxC3Frames32_Type = Counter32
_Ef6000PortTxC3Frames32_Object = MibTableColumn
ef6000PortTxC3Frames32 = _Ef6000PortTxC3Frames32_Object(
    (1, 3, 6, 1, 4, 1, 289, 2, 1, 1, 2, 3, 1, 1, 42),
    _Ef6000PortTxC3Frames32_Type()
)
ef6000PortTxC3Frames32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ef6000PortTxC3Frames32.setStatus("mandatory")
_Ef6000PortRxC3Frames32_Type = Counter32
_Ef6000PortRxC3Frames32_Object = MibTableColumn
ef6000PortRxC3Frames32 = _Ef6000PortRxC3Frames32_Object(
    (1, 3, 6, 1, 4, 1, 289, 2, 1, 1, 2, 3, 1, 1, 43),
    _Ef6000PortRxC3Frames32_Type()
)
ef6000PortRxC3Frames32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ef6000PortRxC3Frames32.setStatus("mandatory")
_Ef6000PortTxC3Octets32_Type = Counter32
_Ef6000PortTxC3Octets32_Object = MibTableColumn
ef6000PortTxC3Octets32 = _Ef6000PortTxC3Octets32_Object(
    (1, 3, 6, 1, 4, 1, 289, 2, 1, 1, 2, 3, 1, 1, 44),
    _Ef6000PortTxC3Octets32_Type()
)
ef6000PortTxC3Octets32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ef6000PortTxC3Octets32.setStatus("mandatory")
_Ef6000PortRxC3Octets32_Type = Counter32
_Ef6000PortRxC3Octets32_Object = MibTableColumn
ef6000PortRxC3Octets32 = _Ef6000PortRxC3Octets32_Object(
    (1, 3, 6, 1, 4, 1, 289, 2, 1, 1, 2, 3, 1, 1, 45),
    _Ef6000PortRxC3Octets32_Type()
)
ef6000PortRxC3Octets32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ef6000PortRxC3Octets32.setStatus("mandatory")
_Ef6000PortC3Discards32_Type = Counter32
_Ef6000PortC3Discards32_Object = MibTableColumn
ef6000PortC3Discards32 = _Ef6000PortC3Discards32_Object(
    (1, 3, 6, 1, 4, 1, 289, 2, 1, 1, 2, 3, 1, 1, 46),
    _Ef6000PortC3Discards32_Type()
)
ef6000PortC3Discards32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ef6000PortC3Discards32.setStatus("mandatory")
_Ef6000PortDiscardFrames_Type = Counter32
_Ef6000PortDiscardFrames_Object = MibTableColumn
ef6000PortDiscardFrames = _Ef6000PortDiscardFrames_Object(
    (1, 3, 6, 1, 4, 1, 289, 2, 1, 1, 2, 3, 1, 1, 50),
    _Ef6000PortDiscardFrames_Type()
)
ef6000PortDiscardFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ef6000PortDiscardFrames.setStatus("mandatory")
_Ef6000PortTxLinkResets_Type = Counter32
_Ef6000PortTxLinkResets_Object = MibTableColumn
ef6000PortTxLinkResets = _Ef6000PortTxLinkResets_Object(
    (1, 3, 6, 1, 4, 1, 289, 2, 1, 1, 2, 3, 1, 1, 51),
    _Ef6000PortTxLinkResets_Type()
)
ef6000PortTxLinkResets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ef6000PortTxLinkResets.setStatus("mandatory")
_Ef6000PortRxLinkResets_Type = Counter32
_Ef6000PortRxLinkResets_Object = MibTableColumn
ef6000PortRxLinkResets = _Ef6000PortRxLinkResets_Object(
    (1, 3, 6, 1, 4, 1, 289, 2, 1, 1, 2, 3, 1, 1, 52),
    _Ef6000PortRxLinkResets_Type()
)
ef6000PortRxLinkResets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ef6000PortRxLinkResets.setStatus("mandatory")
_Ef6000PortTxOLSs_Type = Counter32
_Ef6000PortTxOLSs_Object = MibTableColumn
ef6000PortTxOLSs = _Ef6000PortTxOLSs_Object(
    (1, 3, 6, 1, 4, 1, 289, 2, 1, 1, 2, 3, 1, 1, 53),
    _Ef6000PortTxOLSs_Type()
)
ef6000PortTxOLSs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ef6000PortTxOLSs.setStatus("mandatory")
_Ef6000PortRxOLSs_Type = Counter32
_Ef6000PortRxOLSs_Object = MibTableColumn
ef6000PortRxOLSs = _Ef6000PortRxOLSs_Object(
    (1, 3, 6, 1, 4, 1, 289, 2, 1, 1, 2, 3, 1, 1, 54),
    _Ef6000PortRxOLSs_Type()
)
ef6000PortRxOLSs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ef6000PortRxOLSs.setStatus("mandatory")
_Ef6000PortSyncLosses_Type = Counter32
_Ef6000PortSyncLosses_Object = MibTableColumn
ef6000PortSyncLosses = _Ef6000PortSyncLosses_Object(
    (1, 3, 6, 1, 4, 1, 289, 2, 1, 1, 2, 3, 1, 1, 60),
    _Ef6000PortSyncLosses_Type()
)
ef6000PortSyncLosses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ef6000PortSyncLosses.setStatus("mandatory")
_Ef6000PortSigLosses_Type = Counter32
_Ef6000PortSigLosses_Object = MibTableColumn
ef6000PortSigLosses = _Ef6000PortSigLosses_Object(
    (1, 3, 6, 1, 4, 1, 289, 2, 1, 1, 2, 3, 1, 1, 61),
    _Ef6000PortSigLosses_Type()
)
ef6000PortSigLosses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ef6000PortSigLosses.setStatus("mandatory")
_Ef6000PortProtocolErrors_Type = Counter32
_Ef6000PortProtocolErrors_Object = MibTableColumn
ef6000PortProtocolErrors = _Ef6000PortProtocolErrors_Object(
    (1, 3, 6, 1, 4, 1, 289, 2, 1, 1, 2, 3, 1, 1, 62),
    _Ef6000PortProtocolErrors_Type()
)
ef6000PortProtocolErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ef6000PortProtocolErrors.setStatus("mandatory")
_Ef6000PortInvalidTxWords_Type = Counter32
_Ef6000PortInvalidTxWords_Object = MibTableColumn
ef6000PortInvalidTxWords = _Ef6000PortInvalidTxWords_Object(
    (1, 3, 6, 1, 4, 1, 289, 2, 1, 1, 2, 3, 1, 1, 63),
    _Ef6000PortInvalidTxWords_Type()
)
ef6000PortInvalidTxWords.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ef6000PortInvalidTxWords.setStatus("mandatory")
_Ef6000PortLinkFailures_Type = Counter32
_Ef6000PortLinkFailures_Object = MibTableColumn
ef6000PortLinkFailures = _Ef6000PortLinkFailures_Object(
    (1, 3, 6, 1, 4, 1, 289, 2, 1, 1, 2, 3, 1, 1, 64),
    _Ef6000PortLinkFailures_Type()
)
ef6000PortLinkFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ef6000PortLinkFailures.setStatus("mandatory")
_Ef6000PortCrcs_Type = Counter32
_Ef6000PortCrcs_Object = MibTableColumn
ef6000PortCrcs = _Ef6000PortCrcs_Object(
    (1, 3, 6, 1, 4, 1, 289, 2, 1, 1, 2, 3, 1, 1, 65),
    _Ef6000PortCrcs_Type()
)
ef6000PortCrcs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ef6000PortCrcs.setStatus("mandatory")
_Ef6000PortTruncs_Type = Counter32
_Ef6000PortTruncs_Object = MibTableColumn
ef6000PortTruncs = _Ef6000PortTruncs_Object(
    (1, 3, 6, 1, 4, 1, 289, 2, 1, 1, 2, 3, 1, 1, 66),
    _Ef6000PortTruncs_Type()
)
ef6000PortTruncs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ef6000PortTruncs.setStatus("mandatory")


class _Ef6000PortTxWords64_Type(OctetString):
    """Custom type ef6000PortTxWords64 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_Ef6000PortTxWords64_Type.__name__ = "OctetString"
_Ef6000PortTxWords64_Object = MibTableColumn
ef6000PortTxWords64 = _Ef6000PortTxWords64_Object(
    (1, 3, 6, 1, 4, 1, 289, 2, 1, 1, 2, 3, 1, 1, 67),
    _Ef6000PortTxWords64_Type()
)
ef6000PortTxWords64.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ef6000PortTxWords64.setStatus("mandatory")


class _Ef6000PortRxWords64_Type(OctetString):
    """Custom type ef6000PortRxWords64 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_Ef6000PortRxWords64_Type.__name__ = "OctetString"
_Ef6000PortRxWords64_Object = MibTableColumn
ef6000PortRxWords64 = _Ef6000PortRxWords64_Object(
    (1, 3, 6, 1, 4, 1, 289, 2, 1, 1, 2, 3, 1, 1, 68),
    _Ef6000PortRxWords64_Type()
)
ef6000PortRxWords64.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ef6000PortRxWords64.setStatus("mandatory")


class _Ef6000PortTxFrames64_Type(OctetString):
    """Custom type ef6000PortTxFrames64 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_Ef6000PortTxFrames64_Type.__name__ = "OctetString"
_Ef6000PortTxFrames64_Object = MibTableColumn
ef6000PortTxFrames64 = _Ef6000PortTxFrames64_Object(
    (1, 3, 6, 1, 4, 1, 289, 2, 1, 1, 2, 3, 1, 1, 69),
    _Ef6000PortTxFrames64_Type()
)
ef6000PortTxFrames64.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ef6000PortTxFrames64.setStatus("mandatory")


class _Ef6000PortRxFrames64_Type(OctetString):
    """Custom type ef6000PortRxFrames64 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_Ef6000PortRxFrames64_Type.__name__ = "OctetString"
_Ef6000PortRxFrames64_Object = MibTableColumn
ef6000PortRxFrames64 = _Ef6000PortRxFrames64_Object(
    (1, 3, 6, 1, 4, 1, 289, 2, 1, 1, 2, 3, 1, 1, 70),
    _Ef6000PortRxFrames64_Type()
)
ef6000PortRxFrames64.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ef6000PortRxFrames64.setStatus("mandatory")


class _Ef6000PortTxC2Words64_Type(OctetString):
    """Custom type ef6000PortTxC2Words64 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_Ef6000PortTxC2Words64_Type.__name__ = "OctetString"
_Ef6000PortTxC2Words64_Object = MibTableColumn
ef6000PortTxC2Words64 = _Ef6000PortTxC2Words64_Object(
    (1, 3, 6, 1, 4, 1, 289, 2, 1, 1, 2, 3, 1, 1, 71),
    _Ef6000PortTxC2Words64_Type()
)
ef6000PortTxC2Words64.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ef6000PortTxC2Words64.setStatus("mandatory")


class _Ef6000PortRxC2Words64_Type(OctetString):
    """Custom type ef6000PortRxC2Words64 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_Ef6000PortRxC2Words64_Type.__name__ = "OctetString"
_Ef6000PortRxC2Words64_Object = MibTableColumn
ef6000PortRxC2Words64 = _Ef6000PortRxC2Words64_Object(
    (1, 3, 6, 1, 4, 1, 289, 2, 1, 1, 2, 3, 1, 1, 72),
    _Ef6000PortRxC2Words64_Type()
)
ef6000PortRxC2Words64.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ef6000PortRxC2Words64.setStatus("mandatory")


class _Ef6000PortTxC2Frames64_Type(OctetString):
    """Custom type ef6000PortTxC2Frames64 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_Ef6000PortTxC2Frames64_Type.__name__ = "OctetString"
_Ef6000PortTxC2Frames64_Object = MibTableColumn
ef6000PortTxC2Frames64 = _Ef6000PortTxC2Frames64_Object(
    (1, 3, 6, 1, 4, 1, 289, 2, 1, 1, 2, 3, 1, 1, 73),
    _Ef6000PortTxC2Frames64_Type()
)
ef6000PortTxC2Frames64.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ef6000PortTxC2Frames64.setStatus("mandatory")


class _Ef6000PortRxC2Frames64_Type(OctetString):
    """Custom type ef6000PortRxC2Frames64 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_Ef6000PortRxC2Frames64_Type.__name__ = "OctetString"
_Ef6000PortRxC2Frames64_Object = MibTableColumn
ef6000PortRxC2Frames64 = _Ef6000PortRxC2Frames64_Object(
    (1, 3, 6, 1, 4, 1, 289, 2, 1, 1, 2, 3, 1, 1, 74),
    _Ef6000PortRxC2Frames64_Type()
)
ef6000PortRxC2Frames64.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ef6000PortRxC2Frames64.setStatus("mandatory")


class _Ef6000PortTxC2Octets64_Type(OctetString):
    """Custom type ef6000PortTxC2Octets64 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_Ef6000PortTxC2Octets64_Type.__name__ = "OctetString"
_Ef6000PortTxC2Octets64_Object = MibTableColumn
ef6000PortTxC2Octets64 = _Ef6000PortTxC2Octets64_Object(
    (1, 3, 6, 1, 4, 1, 289, 2, 1, 1, 2, 3, 1, 1, 75),
    _Ef6000PortTxC2Octets64_Type()
)
ef6000PortTxC2Octets64.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ef6000PortTxC2Octets64.setStatus("mandatory")


class _Ef6000PortRxC2Octets64_Type(OctetString):
    """Custom type ef6000PortRxC2Octets64 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_Ef6000PortRxC2Octets64_Type.__name__ = "OctetString"
_Ef6000PortRxC2Octets64_Object = MibTableColumn
ef6000PortRxC2Octets64 = _Ef6000PortRxC2Octets64_Object(
    (1, 3, 6, 1, 4, 1, 289, 2, 1, 1, 2, 3, 1, 1, 76),
    _Ef6000PortRxC2Octets64_Type()
)
ef6000PortRxC2Octets64.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ef6000PortRxC2Octets64.setStatus("mandatory")


class _Ef6000PortTxC3Words64_Type(OctetString):
    """Custom type ef6000PortTxC3Words64 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_Ef6000PortTxC3Words64_Type.__name__ = "OctetString"
_Ef6000PortTxC3Words64_Object = MibTableColumn
ef6000PortTxC3Words64 = _Ef6000PortTxC3Words64_Object(
    (1, 3, 6, 1, 4, 1, 289, 2, 1, 1, 2, 3, 1, 1, 77),
    _Ef6000PortTxC3Words64_Type()
)
ef6000PortTxC3Words64.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ef6000PortTxC3Words64.setStatus("mandatory")


class _Ef6000PortRxC3Words64_Type(OctetString):
    """Custom type ef6000PortRxC3Words64 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_Ef6000PortRxC3Words64_Type.__name__ = "OctetString"
_Ef6000PortRxC3Words64_Object = MibTableColumn
ef6000PortRxC3Words64 = _Ef6000PortRxC3Words64_Object(
    (1, 3, 6, 1, 4, 1, 289, 2, 1, 1, 2, 3, 1, 1, 78),
    _Ef6000PortRxC3Words64_Type()
)
ef6000PortRxC3Words64.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ef6000PortRxC3Words64.setStatus("mandatory")


class _Ef6000PortTxC3Frames64_Type(OctetString):
    """Custom type ef6000PortTxC3Frames64 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_Ef6000PortTxC3Frames64_Type.__name__ = "OctetString"
_Ef6000PortTxC3Frames64_Object = MibTableColumn
ef6000PortTxC3Frames64 = _Ef6000PortTxC3Frames64_Object(
    (1, 3, 6, 1, 4, 1, 289, 2, 1, 1, 2, 3, 1, 1, 79),
    _Ef6000PortTxC3Frames64_Type()
)
ef6000PortTxC3Frames64.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ef6000PortTxC3Frames64.setStatus("mandatory")


class _Ef6000PortRxC3Frames64_Type(OctetString):
    """Custom type ef6000PortRxC3Frames64 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_Ef6000PortRxC3Frames64_Type.__name__ = "OctetString"
_Ef6000PortRxC3Frames64_Object = MibTableColumn
ef6000PortRxC3Frames64 = _Ef6000PortRxC3Frames64_Object(
    (1, 3, 6, 1, 4, 1, 289, 2, 1, 1, 2, 3, 1, 1, 80),
    _Ef6000PortRxC3Frames64_Type()
)
ef6000PortRxC3Frames64.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ef6000PortRxC3Frames64.setStatus("mandatory")


class _Ef6000PortTxC3Octets64_Type(OctetString):
    """Custom type ef6000PortTxC3Octets64 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_Ef6000PortTxC3Octets64_Type.__name__ = "OctetString"
_Ef6000PortTxC3Octets64_Object = MibTableColumn
ef6000PortTxC3Octets64 = _Ef6000PortTxC3Octets64_Object(
    (1, 3, 6, 1, 4, 1, 289, 2, 1, 1, 2, 3, 1, 1, 81),
    _Ef6000PortTxC3Octets64_Type()
)
ef6000PortTxC3Octets64.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ef6000PortTxC3Octets64.setStatus("mandatory")


class _Ef6000PortRxC3Octets64_Type(OctetString):
    """Custom type ef6000PortRxC3Octets64 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_Ef6000PortRxC3Octets64_Type.__name__ = "OctetString"
_Ef6000PortRxC3Octets64_Object = MibTableColumn
ef6000PortRxC3Octets64 = _Ef6000PortRxC3Octets64_Object(
    (1, 3, 6, 1, 4, 1, 289, 2, 1, 1, 2, 3, 1, 1, 82),
    _Ef6000PortRxC3Octets64_Type()
)
ef6000PortRxC3Octets64.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ef6000PortRxC3Octets64.setStatus("mandatory")


class _Ef6000PortC3Discards64_Type(OctetString):
    """Custom type ef6000PortC3Discards64 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_Ef6000PortC3Discards64_Type.__name__ = "OctetString"
_Ef6000PortC3Discards64_Object = MibTableColumn
ef6000PortC3Discards64 = _Ef6000PortC3Discards64_Object(
    (1, 3, 6, 1, 4, 1, 289, 2, 1, 1, 2, 3, 1, 1, 83),
    _Ef6000PortC3Discards64_Type()
)
ef6000PortC3Discards64.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ef6000PortC3Discards64.setStatus("mandatory")
_Ef6000PortBinding_ObjectIdentity = ObjectIdentity
ef6000PortBinding = _Ef6000PortBinding_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 289, 2, 1, 1, 2, 4)
)
_Ef6000PortBindingTable_Object = MibTable
ef6000PortBindingTable = _Ef6000PortBindingTable_Object(
    (1, 3, 6, 1, 4, 1, 289, 2, 1, 1, 2, 4, 1)
)
if mibBuilder.loadTexts:
    ef6000PortBindingTable.setStatus("mandatory")
_Ef6000PortBindingEntry_Object = MibTableRow
ef6000PortBindingEntry = _Ef6000PortBindingEntry_Object(
    (1, 3, 6, 1, 4, 1, 289, 2, 1, 1, 2, 4, 1, 1)
)
ef6000PortBindingEntry.setIndexNames(
    (0, "EF-6000-MIB", "ef6000PortBindingIndex"),
)
if mibBuilder.loadTexts:
    ef6000PortBindingEntry.setStatus("mandatory")
_Ef6000PortBindingIndex_Type = Ef6000PortIndex
_Ef6000PortBindingIndex_Object = MibTableColumn
ef6000PortBindingIndex = _Ef6000PortBindingIndex_Object(
    (1, 3, 6, 1, 4, 1, 289, 2, 1, 1, 2, 4, 1, 1, 1),
    _Ef6000PortBindingIndex_Type()
)
ef6000PortBindingIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ef6000PortBindingIndex.setStatus("mandatory")


class _Ef6000PortBindingFlag_Type(Integer32):
    """Custom type ef6000PortBindingFlag based on Integer32"""
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


_Ef6000PortBindingFlag_Type.__name__ = "Integer32"
_Ef6000PortBindingFlag_Object = MibTableColumn
ef6000PortBindingFlag = _Ef6000PortBindingFlag_Object(
    (1, 3, 6, 1, 4, 1, 289, 2, 1, 1, 2, 4, 1, 1, 2),
    _Ef6000PortBindingFlag_Type()
)
ef6000PortBindingFlag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ef6000PortBindingFlag.setStatus("mandatory")
_Ef6000PortConfiguredWWN_Type = Ef6000PortWWN
_Ef6000PortConfiguredWWN_Object = MibTableColumn
ef6000PortConfiguredWWN = _Ef6000PortConfiguredWWN_Object(
    (1, 3, 6, 1, 4, 1, 289, 2, 1, 1, 2, 4, 1, 1, 3),
    _Ef6000PortConfiguredWWN_Type()
)
ef6000PortConfiguredWWN.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ef6000PortConfiguredWWN.setStatus("mandatory")
_Ef6000PortAttachedWWN_Type = Ef6000PortWWN
_Ef6000PortAttachedWWN_Object = MibTableColumn
ef6000PortAttachedWWN = _Ef6000PortAttachedWWN_Object(
    (1, 3, 6, 1, 4, 1, 289, 2, 1, 1, 2, 4, 1, 1, 4),
    _Ef6000PortAttachedWWN_Type()
)
ef6000PortAttachedWWN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ef6000PortAttachedWWN.setStatus("mandatory")
_Ef6000Zoning_ObjectIdentity = ObjectIdentity
ef6000Zoning = _Ef6000Zoning_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 289, 2, 1, 1, 2, 5)
)
_Ef6000ActiveZoneSetName_Type = DisplayString
_Ef6000ActiveZoneSetName_Object = MibScalar
ef6000ActiveZoneSetName = _Ef6000ActiveZoneSetName_Object(
    (1, 3, 6, 1, 4, 1, 289, 2, 1, 1, 2, 5, 1),
    _Ef6000ActiveZoneSetName_Type()
)
ef6000ActiveZoneSetName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ef6000ActiveZoneSetName.setStatus("mandatory")
_Ef6000ActiveZoneCount_Type = Integer32
_Ef6000ActiveZoneCount_Object = MibScalar
ef6000ActiveZoneCount = _Ef6000ActiveZoneCount_Object(
    (1, 3, 6, 1, 4, 1, 289, 2, 1, 1, 2, 5, 2),
    _Ef6000ActiveZoneCount_Type()
)
ef6000ActiveZoneCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ef6000ActiveZoneCount.setStatus("mandatory")


class _Ef6000DefaultZoneSetState_Type(Integer32):
    """Custom type ef6000DefaultZoneSetState based on Integer32"""
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


_Ef6000DefaultZoneSetState_Type.__name__ = "Integer32"
_Ef6000DefaultZoneSetState_Object = MibScalar
ef6000DefaultZoneSetState = _Ef6000DefaultZoneSetState_Object(
    (1, 3, 6, 1, 4, 1, 289, 2, 1, 1, 2, 5, 3),
    _Ef6000DefaultZoneSetState_Type()
)
ef6000DefaultZoneSetState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ef6000DefaultZoneSetState.setStatus("mandatory")


class _Ef6000ActiveZoneSetState_Type(Integer32):
    """Custom type ef6000ActiveZoneSetState based on Integer32"""
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


_Ef6000ActiveZoneSetState_Type.__name__ = "Integer32"
_Ef6000ActiveZoneSetState_Object = MibScalar
ef6000ActiveZoneSetState = _Ef6000ActiveZoneSetState_Object(
    (1, 3, 6, 1, 4, 1, 289, 2, 1, 1, 2, 5, 4),
    _Ef6000ActiveZoneSetState_Type()
)
ef6000ActiveZoneSetState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ef6000ActiveZoneSetState.setStatus("mandatory")


class _Ef6000HardwareEnforcedZoning_Type(Integer32):
    """Custom type ef6000HardwareEnforcedZoning based on Integer32"""
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


_Ef6000HardwareEnforcedZoning_Type.__name__ = "Integer32"
_Ef6000HardwareEnforcedZoning_Object = MibScalar
ef6000HardwareEnforcedZoning = _Ef6000HardwareEnforcedZoning_Object(
    (1, 3, 6, 1, 4, 1, 289, 2, 1, 1, 2, 5, 5),
    _Ef6000HardwareEnforcedZoning_Type()
)
ef6000HardwareEnforcedZoning.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ef6000HardwareEnforcedZoning.setStatus("mandatory")
_Ef6000ActiveZoneTable_Object = MibTable
ef6000ActiveZoneTable = _Ef6000ActiveZoneTable_Object(
    (1, 3, 6, 1, 4, 1, 289, 2, 1, 1, 2, 5, 6)
)
if mibBuilder.loadTexts:
    ef6000ActiveZoneTable.setStatus("mandatory")
_Ef6000ActiveZoneEntry_Object = MibTableRow
ef6000ActiveZoneEntry = _Ef6000ActiveZoneEntry_Object(
    (1, 3, 6, 1, 4, 1, 289, 2, 1, 1, 2, 5, 6, 1)
)
ef6000ActiveZoneEntry.setIndexNames(
    (0, "EF-6000-MIB", "ef6000ZoneIndex"),
)
if mibBuilder.loadTexts:
    ef6000ActiveZoneEntry.setStatus("mandatory")
_Ef6000ZoneIndex_Type = Integer32
_Ef6000ZoneIndex_Object = MibTableColumn
ef6000ZoneIndex = _Ef6000ZoneIndex_Object(
    (1, 3, 6, 1, 4, 1, 289, 2, 1, 1, 2, 5, 6, 1, 1),
    _Ef6000ZoneIndex_Type()
)
ef6000ZoneIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ef6000ZoneIndex.setStatus("mandatory")
_Ef6000ZoneName_Type = DisplayString
_Ef6000ZoneName_Object = MibTableColumn
ef6000ZoneName = _Ef6000ZoneName_Object(
    (1, 3, 6, 1, 4, 1, 289, 2, 1, 1, 2, 5, 6, 1, 2),
    _Ef6000ZoneName_Type()
)
ef6000ZoneName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ef6000ZoneName.setStatus("mandatory")
_Ef6000ZoneMemberCount_Type = Integer32
_Ef6000ZoneMemberCount_Object = MibTableColumn
ef6000ZoneMemberCount = _Ef6000ZoneMemberCount_Object(
    (1, 3, 6, 1, 4, 1, 289, 2, 1, 1, 2, 5, 6, 1, 3),
    _Ef6000ZoneMemberCount_Type()
)
ef6000ZoneMemberCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ef6000ZoneMemberCount.setStatus("mandatory")
_Ef6000ActiveMemberTable_Object = MibTable
ef6000ActiveMemberTable = _Ef6000ActiveMemberTable_Object(
    (1, 3, 6, 1, 4, 1, 289, 2, 1, 1, 2, 5, 7)
)
if mibBuilder.loadTexts:
    ef6000ActiveMemberTable.setStatus("mandatory")
_Ef6000ActiveMemberEntry_Object = MibTableRow
ef6000ActiveMemberEntry = _Ef6000ActiveMemberEntry_Object(
    (1, 3, 6, 1, 4, 1, 289, 2, 1, 1, 2, 5, 7, 1)
)
ef6000ActiveMemberEntry.setIndexNames(
    (0, "EF-6000-MIB", "ef6000MemberZoneIndex"),
    (0, "EF-6000-MIB", "ef6000MemberIndex"),
)
if mibBuilder.loadTexts:
    ef6000ActiveMemberEntry.setStatus("mandatory")
_Ef6000MemberZoneIndex_Type = Integer32
_Ef6000MemberZoneIndex_Object = MibTableColumn
ef6000MemberZoneIndex = _Ef6000MemberZoneIndex_Object(
    (1, 3, 6, 1, 4, 1, 289, 2, 1, 1, 2, 5, 7, 1, 1),
    _Ef6000MemberZoneIndex_Type()
)
ef6000MemberZoneIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ef6000MemberZoneIndex.setStatus("mandatory")
_Ef6000MemberIndex_Type = Integer32
_Ef6000MemberIndex_Object = MibTableColumn
ef6000MemberIndex = _Ef6000MemberIndex_Object(
    (1, 3, 6, 1, 4, 1, 289, 2, 1, 1, 2, 5, 7, 1, 2),
    _Ef6000MemberIndex_Type()
)
ef6000MemberIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ef6000MemberIndex.setStatus("mandatory")


class _Ef6000MemberType_Type(Integer32):
    """Custom type ef6000MemberType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("portnumber", 2),
          ("wwn", 1))
    )


_Ef6000MemberType_Type.__name__ = "Integer32"
_Ef6000MemberType_Object = MibTableColumn
ef6000MemberType = _Ef6000MemberType_Object(
    (1, 3, 6, 1, 4, 1, 289, 2, 1, 1, 2, 5, 7, 1, 3),
    _Ef6000MemberType_Type()
)
ef6000MemberType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ef6000MemberType.setStatus("mandatory")
_Ef6000MemberWWN_Type = Ef6000PortWWN
_Ef6000MemberWWN_Object = MibTableColumn
ef6000MemberWWN = _Ef6000MemberWWN_Object(
    (1, 3, 6, 1, 4, 1, 289, 2, 1, 1, 2, 5, 7, 1, 4),
    _Ef6000MemberWWN_Type()
)
ef6000MemberWWN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ef6000MemberWWN.setStatus("mandatory")
_Ef6000MemberDomainID_Type = Integer32
_Ef6000MemberDomainID_Object = MibTableColumn
ef6000MemberDomainID = _Ef6000MemberDomainID_Object(
    (1, 3, 6, 1, 4, 1, 289, 2, 1, 1, 2, 5, 7, 1, 5),
    _Ef6000MemberDomainID_Type()
)
ef6000MemberDomainID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ef6000MemberDomainID.setStatus("mandatory")
_Ef6000MemberPortNumber_Type = Integer32
_Ef6000MemberPortNumber_Object = MibTableColumn
ef6000MemberPortNumber = _Ef6000MemberPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 289, 2, 1, 1, 2, 5, 7, 1, 6),
    _Ef6000MemberPortNumber_Type()
)
ef6000MemberPortNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ef6000MemberPortNumber.setStatus("mandatory")
_Ef6000TA_ObjectIdentity = ObjectIdentity
ef6000TA = _Ef6000TA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 289, 2, 1, 1, 2, 6)
)
_Ef6000TATable_Object = MibTable
ef6000TATable = _Ef6000TATable_Object(
    (1, 3, 6, 1, 4, 1, 289, 2, 1, 1, 2, 6, 1)
)
if mibBuilder.loadTexts:
    ef6000TATable.setStatus("mandatory")
_Ef6000TAEntry_Object = MibTableRow
ef6000TAEntry = _Ef6000TAEntry_Object(
    (1, 3, 6, 1, 4, 1, 289, 2, 1, 1, 2, 6, 1, 1)
)
ef6000TAEntry.setIndexNames(
    (0, "EF-6000-MIB", "ef6000TAIndex"),
)
if mibBuilder.loadTexts:
    ef6000TAEntry.setStatus("mandatory")
_Ef6000TAIndex_Type = Integer32
_Ef6000TAIndex_Object = MibTableColumn
ef6000TAIndex = _Ef6000TAIndex_Object(
    (1, 3, 6, 1, 4, 1, 289, 2, 1, 1, 2, 6, 1, 1, 1),
    _Ef6000TAIndex_Type()
)
ef6000TAIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ef6000TAIndex.setStatus("mandatory")


class _Ef6000TAName_Type(DisplayString):
    """Custom type ef6000TAName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_Ef6000TAName_Type.__name__ = "DisplayString"
_Ef6000TAName_Object = MibTableColumn
ef6000TAName = _Ef6000TAName_Object(
    (1, 3, 6, 1, 4, 1, 289, 2, 1, 1, 2, 6, 1, 1, 2),
    _Ef6000TAName_Type()
)
ef6000TAName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ef6000TAName.setStatus("mandatory")


class _Ef6000TAState_Type(Integer32):
    """Custom type ef6000TAState based on Integer32"""
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


_Ef6000TAState_Type.__name__ = "Integer32"
_Ef6000TAState_Object = MibTableColumn
ef6000TAState = _Ef6000TAState_Object(
    (1, 3, 6, 1, 4, 1, 289, 2, 1, 1, 2, 6, 1, 1, 3),
    _Ef6000TAState_Type()
)
ef6000TAState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ef6000TAState.setStatus("mandatory")


class _Ef6000TAType_Type(Integer32):
    """Custom type ef6000TAType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("counter", 2),
          ("throughput", 1))
    )


_Ef6000TAType_Type.__name__ = "Integer32"
_Ef6000TAType_Object = MibTableColumn
ef6000TAType = _Ef6000TAType_Object(
    (1, 3, 6, 1, 4, 1, 289, 2, 1, 1, 2, 6, 1, 1, 4),
    _Ef6000TAType_Type()
)
ef6000TAType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ef6000TAType.setStatus("mandatory")


class _Ef6000TAPortType_Type(Integer32):
    """Custom type ef6000TAPortType based on Integer32"""
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
        *(("ePorts", 2),
          ("fPorts", 3),
          ("flPorts", 4),
          ("list", 1))
    )


_Ef6000TAPortType_Type.__name__ = "Integer32"
_Ef6000TAPortType_Object = MibTableColumn
ef6000TAPortType = _Ef6000TAPortType_Object(
    (1, 3, 6, 1, 4, 1, 289, 2, 1, 1, 2, 6, 1, 1, 5),
    _Ef6000TAPortType_Type()
)
ef6000TAPortType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ef6000TAPortType.setStatus("mandatory")
_Ef6000TAPortList_Type = Ef6000PortList
_Ef6000TAPortList_Object = MibTableColumn
ef6000TAPortList = _Ef6000TAPortList_Object(
    (1, 3, 6, 1, 4, 1, 289, 2, 1, 1, 2, 6, 1, 1, 6),
    _Ef6000TAPortList_Type()
)
ef6000TAPortList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ef6000TAPortList.setStatus("mandatory")
_Ef6000TAInterval_Type = Integer32
_Ef6000TAInterval_Object = MibTableColumn
ef6000TAInterval = _Ef6000TAInterval_Object(
    (1, 3, 6, 1, 4, 1, 289, 2, 1, 1, 2, 6, 1, 1, 7),
    _Ef6000TAInterval_Type()
)
ef6000TAInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ef6000TAInterval.setStatus("mandatory")
_Ef6000TATriggerValue_Type = Integer32
_Ef6000TATriggerValue_Object = MibTableColumn
ef6000TATriggerValue = _Ef6000TATriggerValue_Object(
    (1, 3, 6, 1, 4, 1, 289, 2, 1, 1, 2, 6, 1, 1, 8),
    _Ef6000TATriggerValue_Type()
)
ef6000TATriggerValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ef6000TATriggerValue.setStatus("mandatory")


class _Ef6000TTADirection_Type(Integer32):
    """Custom type ef6000TTADirection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("either", 3),
          ("receive", 2),
          ("transmit", 1))
    )


_Ef6000TTADirection_Type.__name__ = "Integer32"
_Ef6000TTADirection_Object = MibTableColumn
ef6000TTADirection = _Ef6000TTADirection_Object(
    (1, 3, 6, 1, 4, 1, 289, 2, 1, 1, 2, 6, 1, 1, 9),
    _Ef6000TTADirection_Type()
)
ef6000TTADirection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ef6000TTADirection.setStatus("mandatory")
_Ef6000TTATriggerDuration_Type = Integer32
_Ef6000TTATriggerDuration_Object = MibTableColumn
ef6000TTATriggerDuration = _Ef6000TTATriggerDuration_Object(
    (1, 3, 6, 1, 4, 1, 289, 2, 1, 1, 2, 6, 1, 1, 10),
    _Ef6000TTATriggerDuration_Type()
)
ef6000TTATriggerDuration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ef6000TTATriggerDuration.setStatus("mandatory")
_Ef6000CTACounter_Type = Integer32
_Ef6000CTACounter_Object = MibTableColumn
ef6000CTACounter = _Ef6000CTACounter_Object(
    (1, 3, 6, 1, 4, 1, 289, 2, 1, 1, 2, 6, 1, 1, 11),
    _Ef6000CTACounter_Type()
)
ef6000CTACounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ef6000CTACounter.setStatus("mandatory")

# Managed Objects groups


# Notification objects

ef6000PortScn = NotificationType(
    (1, 3, 6, 1, 4, 1, 289, 0, 1)
)
ef6000PortScn.setObjects(
    ("EF-6000-MIB", "ef6000PortOpStatus")
)
if mibBuilder.loadTexts:
    ef6000PortScn.setStatus(
        ""
    )

ef6000FruScn = NotificationType(
    (1, 3, 6, 1, 4, 1, 289, 0, 2)
)
ef6000FruScn.setObjects(
    ("EF-6000-MIB", "ef6000FruStatus")
)
if mibBuilder.loadTexts:
    ef6000FruScn.setStatus(
        ""
    )

ef6000PortBindingViolation = NotificationType(
    (1, 3, 6, 1, 4, 1, 289, 0, 3)
)
ef6000PortBindingViolation.setObjects(
    ("EF-6000-MIB", "ef6000PortAttachedWWN")
)
if mibBuilder.loadTexts:
    ef6000PortBindingViolation.setStatus(
        ""
    )

ef6000ThresholdAlert = NotificationType(
    (1, 3, 6, 1, 4, 1, 289, 0, 4)
)
ef6000ThresholdAlert.setObjects(
      *(("EF-6000-MIB", "ef6000PortIndex"),
        ("EF-6000-MIB", "ef6000TAIndex"))
)
if mibBuilder.loadTexts:
    ef6000ThresholdAlert.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "EF-6000-MIB",
    **{"DisplayString": DisplayString,
       "Ef6000SysOperStatus": Ef6000SysOperStatus,
       "Ef6000FruCode": Ef6000FruCode,
       "Ef6000FruPosition": Ef6000FruPosition,
       "Ef6000PortIndex": Ef6000PortIndex,
       "Ef6000PortPhyState": Ef6000PortPhyState,
       "Ef6000PortWWN": Ef6000PortWWN,
       "Ef6000PortList": Ef6000PortList,
       "mcData": mcData,
       "ef6000PortScn": ef6000PortScn,
       "ef6000FruScn": ef6000FruScn,
       "ef6000PortBindingViolation": ef6000PortBindingViolation,
       "ef6000ThresholdAlert": ef6000ThresholdAlert,
       "commDev": commDev,
       "fibreChannel": fibreChannel,
       "fcSwitch": fcSwitch,
       "ef-6000": ef_6000,
       "ef6000Sys": ef6000Sys,
       "ef6000SysCurrentDate": ef6000SysCurrentDate,
       "ef6000SysBootDate": ef6000SysBootDate,
       "ef6000SysFirmwareVersion": ef6000SysFirmwareVersion,
       "ef6000SysTypeNum": ef6000SysTypeNum,
       "ef6000SysModelNum": ef6000SysModelNum,
       "ef6000SysMfg": ef6000SysMfg,
       "ef6000SysPlantOfMfg": ef6000SysPlantOfMfg,
       "ef6000SysEcLevel": ef6000SysEcLevel,
       "ef6000SysSerialNum": ef6000SysSerialNum,
       "ef6000SysOperStatus": ef6000SysOperStatus,
       "ef6000SysState": ef6000SysState,
       "ef6000SysAdmStatus": ef6000SysAdmStatus,
       "ef6000SysConfigSpeed": ef6000SysConfigSpeed,
       "ef6000Fru": ef6000Fru,
       "ef6000FruTable": ef6000FruTable,
       "ef6000FruEntry": ef6000FruEntry,
       "ef6000FruCode": ef6000FruCode,
       "ef6000FruPosition": ef6000FruPosition,
       "ef6000FruStatus": ef6000FruStatus,
       "ef6000FruPartNumber": ef6000FruPartNumber,
       "ef6000FruSerialNumber": ef6000FruSerialNumber,
       "ef6000FruPowerOnHours": ef6000FruPowerOnHours,
       "ef6000FruTestDate": ef6000FruTestDate,
       "ef6000Port": ef6000Port,
       "ef6000PortTable": ef6000PortTable,
       "ef6000PortEntry": ef6000PortEntry,
       "ef6000PortIndex": ef6000PortIndex,
       "ef6000PortPhyState": ef6000PortPhyState,
       "ef6000PortOpStatus": ef6000PortOpStatus,
       "ef6000PortAdmStatus": ef6000PortAdmStatus,
       "ef6000PortConnector": ef6000PortConnector,
       "ef6000PortDistance": ef6000PortDistance,
       "ef6000PortType": ef6000PortType,
       "ef6000PortMedia": ef6000PortMedia,
       "ef6000PortSpeedCap": ef6000PortSpeedCap,
       "ef6000PortConfigSpeed": ef6000PortConfigSpeed,
       "ef6000PortSpeed": ef6000PortSpeed,
       "ef6000PortTxWords32": ef6000PortTxWords32,
       "ef6000PortRxWords32": ef6000PortRxWords32,
       "ef6000PortTxFrames32": ef6000PortTxFrames32,
       "ef6000PortRxFrames32": ef6000PortRxFrames32,
       "ef6000PortTxThroughput": ef6000PortTxThroughput,
       "ef6000PortRxThroughput": ef6000PortRxThroughput,
       "ef6000PortTxC2Words32": ef6000PortTxC2Words32,
       "ef6000PortRxC2Words32": ef6000PortRxC2Words32,
       "ef6000PortTxC2Frames32": ef6000PortTxC2Frames32,
       "ef6000PortRxC2Frames32": ef6000PortRxC2Frames32,
       "ef6000PortTxC2Octets32": ef6000PortTxC2Octets32,
       "ef6000PortRxC2Octets32": ef6000PortRxC2Octets32,
       "ef6000PortTxC3Words32": ef6000PortTxC3Words32,
       "ef6000PortRxC3Words32": ef6000PortRxC3Words32,
       "ef6000PortTxC3Frames32": ef6000PortTxC3Frames32,
       "ef6000PortRxC3Frames32": ef6000PortRxC3Frames32,
       "ef6000PortTxC3Octets32": ef6000PortTxC3Octets32,
       "ef6000PortRxC3Octets32": ef6000PortRxC3Octets32,
       "ef6000PortC3Discards32": ef6000PortC3Discards32,
       "ef6000PortDiscardFrames": ef6000PortDiscardFrames,
       "ef6000PortTxLinkResets": ef6000PortTxLinkResets,
       "ef6000PortRxLinkResets": ef6000PortRxLinkResets,
       "ef6000PortTxOLSs": ef6000PortTxOLSs,
       "ef6000PortRxOLSs": ef6000PortRxOLSs,
       "ef6000PortSyncLosses": ef6000PortSyncLosses,
       "ef6000PortSigLosses": ef6000PortSigLosses,
       "ef6000PortProtocolErrors": ef6000PortProtocolErrors,
       "ef6000PortInvalidTxWords": ef6000PortInvalidTxWords,
       "ef6000PortLinkFailures": ef6000PortLinkFailures,
       "ef6000PortCrcs": ef6000PortCrcs,
       "ef6000PortTruncs": ef6000PortTruncs,
       "ef6000PortTxWords64": ef6000PortTxWords64,
       "ef6000PortRxWords64": ef6000PortRxWords64,
       "ef6000PortTxFrames64": ef6000PortTxFrames64,
       "ef6000PortRxFrames64": ef6000PortRxFrames64,
       "ef6000PortTxC2Words64": ef6000PortTxC2Words64,
       "ef6000PortRxC2Words64": ef6000PortRxC2Words64,
       "ef6000PortTxC2Frames64": ef6000PortTxC2Frames64,
       "ef6000PortRxC2Frames64": ef6000PortRxC2Frames64,
       "ef6000PortTxC2Octets64": ef6000PortTxC2Octets64,
       "ef6000PortRxC2Octets64": ef6000PortRxC2Octets64,
       "ef6000PortTxC3Words64": ef6000PortTxC3Words64,
       "ef6000PortRxC3Words64": ef6000PortRxC3Words64,
       "ef6000PortTxC3Frames64": ef6000PortTxC3Frames64,
       "ef6000PortRxC3Frames64": ef6000PortRxC3Frames64,
       "ef6000PortTxC3Octets64": ef6000PortTxC3Octets64,
       "ef6000PortRxC3Octets64": ef6000PortRxC3Octets64,
       "ef6000PortC3Discards64": ef6000PortC3Discards64,
       "ef6000PortBinding": ef6000PortBinding,
       "ef6000PortBindingTable": ef6000PortBindingTable,
       "ef6000PortBindingEntry": ef6000PortBindingEntry,
       "ef6000PortBindingIndex": ef6000PortBindingIndex,
       "ef6000PortBindingFlag": ef6000PortBindingFlag,
       "ef6000PortConfiguredWWN": ef6000PortConfiguredWWN,
       "ef6000PortAttachedWWN": ef6000PortAttachedWWN,
       "ef6000Zoning": ef6000Zoning,
       "ef6000ActiveZoneSetName": ef6000ActiveZoneSetName,
       "ef6000ActiveZoneCount": ef6000ActiveZoneCount,
       "ef6000DefaultZoneSetState": ef6000DefaultZoneSetState,
       "ef6000ActiveZoneSetState": ef6000ActiveZoneSetState,
       "ef6000HardwareEnforcedZoning": ef6000HardwareEnforcedZoning,
       "ef6000ActiveZoneTable": ef6000ActiveZoneTable,
       "ef6000ActiveZoneEntry": ef6000ActiveZoneEntry,
       "ef6000ZoneIndex": ef6000ZoneIndex,
       "ef6000ZoneName": ef6000ZoneName,
       "ef6000ZoneMemberCount": ef6000ZoneMemberCount,
       "ef6000ActiveMemberTable": ef6000ActiveMemberTable,
       "ef6000ActiveMemberEntry": ef6000ActiveMemberEntry,
       "ef6000MemberZoneIndex": ef6000MemberZoneIndex,
       "ef6000MemberIndex": ef6000MemberIndex,
       "ef6000MemberType": ef6000MemberType,
       "ef6000MemberWWN": ef6000MemberWWN,
       "ef6000MemberDomainID": ef6000MemberDomainID,
       "ef6000MemberPortNumber": ef6000MemberPortNumber,
       "ef6000TA": ef6000TA,
       "ef6000TATable": ef6000TATable,
       "ef6000TAEntry": ef6000TAEntry,
       "ef6000TAIndex": ef6000TAIndex,
       "ef6000TAName": ef6000TAName,
       "ef6000TAState": ef6000TAState,
       "ef6000TAType": ef6000TAType,
       "ef6000TAPortType": ef6000TAPortType,
       "ef6000TAPortList": ef6000TAPortList,
       "ef6000TAInterval": ef6000TAInterval,
       "ef6000TATriggerValue": ef6000TATriggerValue,
       "ef6000TTADirection": ef6000TTADirection,
       "ef6000TTATriggerDuration": ef6000TTATriggerDuration,
       "ef6000CTACounter": ef6000CTACounter}
)
