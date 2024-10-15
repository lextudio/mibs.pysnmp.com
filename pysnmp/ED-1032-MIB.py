# SNMP MIB module (ED-1032-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ED-1032-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:36:31 2024
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




class Ed1032SysOperStatus(Integer32):
    """Custom type Ed1032SysOperStatus based on Integer32"""
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





class Ed1032SysState(Integer32):
    """Custom type Ed1032SysState based on Integer32"""
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





class Ed1032FruCode(Integer32):
    """Custom type Ed1032FruCode based on Integer32"""
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
        *(("fru-bkplane", 1),
          ("fru-cmm", 4),
          ("fru-ctp", 2),
          ("fru-fan", 5),
          ("fru-gls", 9),
          ("fru-glx", 10),
          ("fru-gsm", 8),
          ("fru-gxx", 12),
          ("fru-lsm", 11),
          ("fru-mpc", 3),
          ("fru-panel", 7),
          ("fru-power", 6))
    )





class Ed1032FruPosition(Integer32):
    """Custom type Ed1032FruPosition based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )





class Ed1032FruStatus(Integer32):
    """Custom type Ed1032FruStatus based on Integer32"""
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





class Ed1032PortIndex(Integer32):
    """Custom type Ed1032PortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2048),
    )





class Ed1032PortPhyState(Integer32):
    """Custom type Ed1032PortPhyState based on Integer32"""
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
        *(("psAvailable", 2),
          ("psBlocked", 3),
          ("psExtLoop", 8),
          ("psIntDiags", 7),
          ("psLR", 11),
          ("psLinkFailLOL", 6),
          ("psLinkFailure", 5),
          ("psNotInstalled", 1),
          ("psPortFail", 9),
          ("psSR", 10),
          ("psUnavailable", 4))
    )





class Ed1032PortStatus(Integer32):
    """Custom type Ed1032PortStatus based on Integer32"""
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





class Ed1032PortAdmStatus(Integer32):
    """Custom type Ed1032PortAdmStatus based on Integer32"""
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
_Ed_1032_ObjectIdentity = ObjectIdentity
ed_1032 = _Ed_1032_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 289, 2, 1, 1, 1)
)
_Ed1032Sys_ObjectIdentity = ObjectIdentity
ed1032Sys = _Ed1032Sys_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 289, 2, 1, 1, 1, 1)
)


class _Ed1032SysCurrentDate_Type(DisplayString):
    """Custom type ed1032SysCurrentDate based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(64, 64),
    )


_Ed1032SysCurrentDate_Type.__name__ = "DisplayString"
_Ed1032SysCurrentDate_Object = MibScalar
ed1032SysCurrentDate = _Ed1032SysCurrentDate_Object(
    (1, 3, 6, 1, 4, 1, 289, 2, 1, 1, 1, 1, 1),
    _Ed1032SysCurrentDate_Type()
)
ed1032SysCurrentDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ed1032SysCurrentDate.setStatus("mandatory")


class _Ed1032SysBootDate_Type(DisplayString):
    """Custom type ed1032SysBootDate based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(64, 64),
    )


_Ed1032SysBootDate_Type.__name__ = "DisplayString"
_Ed1032SysBootDate_Object = MibScalar
ed1032SysBootDate = _Ed1032SysBootDate_Object(
    (1, 3, 6, 1, 4, 1, 289, 2, 1, 1, 1, 1, 2),
    _Ed1032SysBootDate_Type()
)
ed1032SysBootDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ed1032SysBootDate.setStatus("mandatory")


class _Ed1032SysFirmwareVersion_Type(DisplayString):
    """Custom type ed1032SysFirmwareVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(24, 24),
    )


_Ed1032SysFirmwareVersion_Type.__name__ = "DisplayString"
_Ed1032SysFirmwareVersion_Object = MibScalar
ed1032SysFirmwareVersion = _Ed1032SysFirmwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 289, 2, 1, 1, 1, 1, 3),
    _Ed1032SysFirmwareVersion_Type()
)
ed1032SysFirmwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ed1032SysFirmwareVersion.setStatus("mandatory")


class _Ed1032SysTypeNum_Type(DisplayString):
    """Custom type ed1032SysTypeNum based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(64, 64),
    )


_Ed1032SysTypeNum_Type.__name__ = "DisplayString"
_Ed1032SysTypeNum_Object = MibScalar
ed1032SysTypeNum = _Ed1032SysTypeNum_Object(
    (1, 3, 6, 1, 4, 1, 289, 2, 1, 1, 1, 1, 4),
    _Ed1032SysTypeNum_Type()
)
ed1032SysTypeNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ed1032SysTypeNum.setStatus("mandatory")


class _Ed1032SysModelNum_Type(DisplayString):
    """Custom type ed1032SysModelNum based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(64, 64),
    )


_Ed1032SysModelNum_Type.__name__ = "DisplayString"
_Ed1032SysModelNum_Object = MibScalar
ed1032SysModelNum = _Ed1032SysModelNum_Object(
    (1, 3, 6, 1, 4, 1, 289, 2, 1, 1, 1, 1, 5),
    _Ed1032SysModelNum_Type()
)
ed1032SysModelNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ed1032SysModelNum.setStatus("mandatory")


class _Ed1032SysMfg_Type(DisplayString):
    """Custom type ed1032SysMfg based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(64, 64),
    )


_Ed1032SysMfg_Type.__name__ = "DisplayString"
_Ed1032SysMfg_Object = MibScalar
ed1032SysMfg = _Ed1032SysMfg_Object(
    (1, 3, 6, 1, 4, 1, 289, 2, 1, 1, 1, 1, 6),
    _Ed1032SysMfg_Type()
)
ed1032SysMfg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ed1032SysMfg.setStatus("mandatory")


class _Ed1032SysPlantOfMfg_Type(DisplayString):
    """Custom type ed1032SysPlantOfMfg based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(64, 64),
    )


_Ed1032SysPlantOfMfg_Type.__name__ = "DisplayString"
_Ed1032SysPlantOfMfg_Object = MibScalar
ed1032SysPlantOfMfg = _Ed1032SysPlantOfMfg_Object(
    (1, 3, 6, 1, 4, 1, 289, 2, 1, 1, 1, 1, 7),
    _Ed1032SysPlantOfMfg_Type()
)
ed1032SysPlantOfMfg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ed1032SysPlantOfMfg.setStatus("mandatory")


class _Ed1032SysSeqNum_Type(DisplayString):
    """Custom type ed1032SysSeqNum based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(64, 64),
    )


_Ed1032SysSeqNum_Type.__name__ = "DisplayString"
_Ed1032SysSeqNum_Object = MibScalar
ed1032SysSeqNum = _Ed1032SysSeqNum_Object(
    (1, 3, 6, 1, 4, 1, 289, 2, 1, 1, 1, 1, 8),
    _Ed1032SysSeqNum_Type()
)
ed1032SysSeqNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ed1032SysSeqNum.setStatus("mandatory")


class _Ed1032SysEcLevel_Type(DisplayString):
    """Custom type ed1032SysEcLevel based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(64, 64),
    )


_Ed1032SysEcLevel_Type.__name__ = "DisplayString"
_Ed1032SysEcLevel_Object = MibScalar
ed1032SysEcLevel = _Ed1032SysEcLevel_Object(
    (1, 3, 6, 1, 4, 1, 289, 2, 1, 1, 1, 1, 9),
    _Ed1032SysEcLevel_Type()
)
ed1032SysEcLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ed1032SysEcLevel.setStatus("mandatory")


class _Ed1032SysOemSerialNum_Type(DisplayString):
    """Custom type ed1032SysOemSerialNum based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(64, 64),
    )


_Ed1032SysOemSerialNum_Type.__name__ = "DisplayString"
_Ed1032SysOemSerialNum_Object = MibScalar
ed1032SysOemSerialNum = _Ed1032SysOemSerialNum_Object(
    (1, 3, 6, 1, 4, 1, 289, 2, 1, 1, 1, 1, 10),
    _Ed1032SysOemSerialNum_Type()
)
ed1032SysOemSerialNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ed1032SysOemSerialNum.setStatus("mandatory")
_Ed1032SysOperStatus_Type = Ed1032SysOperStatus
_Ed1032SysOperStatus_Object = MibScalar
ed1032SysOperStatus = _Ed1032SysOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 289, 2, 1, 1, 1, 1, 11),
    _Ed1032SysOperStatus_Type()
)
ed1032SysOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ed1032SysOperStatus.setStatus("mandatory")
_Ed1032SysState_Type = Ed1032SysState
_Ed1032SysState_Object = MibScalar
ed1032SysState = _Ed1032SysState_Object(
    (1, 3, 6, 1, 4, 1, 289, 2, 1, 1, 1, 1, 12),
    _Ed1032SysState_Type()
)
ed1032SysState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ed1032SysState.setStatus("mandatory")


class _Ed1032SysAdmStatus_Type(Integer32):
    """Custom type ed1032SysAdmStatus based on Integer32"""
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


_Ed1032SysAdmStatus_Type.__name__ = "Integer32"
_Ed1032SysAdmStatus_Object = MibScalar
ed1032SysAdmStatus = _Ed1032SysAdmStatus_Object(
    (1, 3, 6, 1, 4, 1, 289, 2, 1, 1, 1, 1, 13),
    _Ed1032SysAdmStatus_Type()
)
ed1032SysAdmStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ed1032SysAdmStatus.setStatus("mandatory")
_Ed1032Fru_ObjectIdentity = ObjectIdentity
ed1032Fru = _Ed1032Fru_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 289, 2, 1, 1, 1, 2)
)
_Ed1032FruTable_Object = MibTable
ed1032FruTable = _Ed1032FruTable_Object(
    (1, 3, 6, 1, 4, 1, 289, 2, 1, 1, 1, 2, 1)
)
if mibBuilder.loadTexts:
    ed1032FruTable.setStatus("mandatory")
_Ed1032FruEntry_Object = MibTableRow
ed1032FruEntry = _Ed1032FruEntry_Object(
    (1, 3, 6, 1, 4, 1, 289, 2, 1, 1, 1, 2, 1, 1)
)
ed1032FruEntry.setIndexNames(
    (0, "ED-1032-MIB", "ed1032FruCode"),
    (0, "ED-1032-MIB", "ed1032FruPosition"),
)
if mibBuilder.loadTexts:
    ed1032FruEntry.setStatus("mandatory")
_Ed1032FruCode_Type = Ed1032FruCode
_Ed1032FruCode_Object = MibTableColumn
ed1032FruCode = _Ed1032FruCode_Object(
    (1, 3, 6, 1, 4, 1, 289, 2, 1, 1, 1, 2, 1, 1, 1),
    _Ed1032FruCode_Type()
)
ed1032FruCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ed1032FruCode.setStatus("mandatory")
_Ed1032FruPosition_Type = Ed1032FruPosition
_Ed1032FruPosition_Object = MibTableColumn
ed1032FruPosition = _Ed1032FruPosition_Object(
    (1, 3, 6, 1, 4, 1, 289, 2, 1, 1, 1, 2, 1, 1, 2),
    _Ed1032FruPosition_Type()
)
ed1032FruPosition.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ed1032FruPosition.setStatus("mandatory")
_Ed1032FruStatus_Type = Ed1032FruStatus
_Ed1032FruStatus_Object = MibTableColumn
ed1032FruStatus = _Ed1032FruStatus_Object(
    (1, 3, 6, 1, 4, 1, 289, 2, 1, 1, 1, 2, 1, 1, 3),
    _Ed1032FruStatus_Type()
)
ed1032FruStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ed1032FruStatus.setStatus("mandatory")


class _Ed1032FruPartNumber_Type(DisplayString):
    """Custom type ed1032FruPartNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(64, 64),
    )


_Ed1032FruPartNumber_Type.__name__ = "DisplayString"
_Ed1032FruPartNumber_Object = MibTableColumn
ed1032FruPartNumber = _Ed1032FruPartNumber_Object(
    (1, 3, 6, 1, 4, 1, 289, 2, 1, 1, 1, 2, 1, 1, 4),
    _Ed1032FruPartNumber_Type()
)
ed1032FruPartNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ed1032FruPartNumber.setStatus("mandatory")


class _Ed1032FruSerialNumber_Type(DisplayString):
    """Custom type ed1032FruSerialNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(64, 64),
    )


_Ed1032FruSerialNumber_Type.__name__ = "DisplayString"
_Ed1032FruSerialNumber_Object = MibTableColumn
ed1032FruSerialNumber = _Ed1032FruSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 289, 2, 1, 1, 1, 2, 1, 1, 5),
    _Ed1032FruSerialNumber_Type()
)
ed1032FruSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ed1032FruSerialNumber.setStatus("mandatory")
_Ed1032FruPowerOnHours_Type = Counter32
_Ed1032FruPowerOnHours_Object = MibTableColumn
ed1032FruPowerOnHours = _Ed1032FruPowerOnHours_Object(
    (1, 3, 6, 1, 4, 1, 289, 2, 1, 1, 1, 2, 1, 1, 6),
    _Ed1032FruPowerOnHours_Type()
)
ed1032FruPowerOnHours.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ed1032FruPowerOnHours.setStatus("mandatory")


class _Ed1032FruTestDate_Type(DisplayString):
    """Custom type ed1032FruTestDate based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(64, 64),
    )


_Ed1032FruTestDate_Type.__name__ = "DisplayString"
_Ed1032FruTestDate_Object = MibTableColumn
ed1032FruTestDate = _Ed1032FruTestDate_Object(
    (1, 3, 6, 1, 4, 1, 289, 2, 1, 1, 1, 2, 1, 1, 7),
    _Ed1032FruTestDate_Type()
)
ed1032FruTestDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ed1032FruTestDate.setStatus("mandatory")
_Ed1032Port_ObjectIdentity = ObjectIdentity
ed1032Port = _Ed1032Port_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 289, 2, 1, 1, 1, 3)
)
_Ed1032PortTable_Object = MibTable
ed1032PortTable = _Ed1032PortTable_Object(
    (1, 3, 6, 1, 4, 1, 289, 2, 1, 1, 1, 3, 1)
)
if mibBuilder.loadTexts:
    ed1032PortTable.setStatus("mandatory")
_Ed1032PortEntry_Object = MibTableRow
ed1032PortEntry = _Ed1032PortEntry_Object(
    (1, 3, 6, 1, 4, 1, 289, 2, 1, 1, 1, 3, 1, 1)
)
ed1032PortEntry.setIndexNames(
    (0, "ED-1032-MIB", "ed1032PortIndex"),
)
if mibBuilder.loadTexts:
    ed1032PortEntry.setStatus("mandatory")
_Ed1032PortIndex_Type = Ed1032PortIndex
_Ed1032PortIndex_Object = MibTableColumn
ed1032PortIndex = _Ed1032PortIndex_Object(
    (1, 3, 6, 1, 4, 1, 289, 2, 1, 1, 1, 3, 1, 1, 1),
    _Ed1032PortIndex_Type()
)
ed1032PortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ed1032PortIndex.setStatus("mandatory")
_Ed1032PortPhyState_Type = Ed1032PortPhyState
_Ed1032PortPhyState_Object = MibTableColumn
ed1032PortPhyState = _Ed1032PortPhyState_Object(
    (1, 3, 6, 1, 4, 1, 289, 2, 1, 1, 1, 3, 1, 1, 2),
    _Ed1032PortPhyState_Type()
)
ed1032PortPhyState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ed1032PortPhyState.setStatus("mandatory")
_Ed1032PortOpStatus_Type = Ed1032PortStatus
_Ed1032PortOpStatus_Object = MibTableColumn
ed1032PortOpStatus = _Ed1032PortOpStatus_Object(
    (1, 3, 6, 1, 4, 1, 289, 2, 1, 1, 1, 3, 1, 1, 3),
    _Ed1032PortOpStatus_Type()
)
ed1032PortOpStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ed1032PortOpStatus.setStatus("mandatory")
_Ed1032PortAdmStatus_Type = Ed1032PortAdmStatus
_Ed1032PortAdmStatus_Object = MibTableColumn
ed1032PortAdmStatus = _Ed1032PortAdmStatus_Object(
    (1, 3, 6, 1, 4, 1, 289, 2, 1, 1, 1, 3, 1, 1, 4),
    _Ed1032PortAdmStatus_Type()
)
ed1032PortAdmStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ed1032PortAdmStatus.setStatus("mandatory")
_Ed1032PortTxWords_Type = Counter32
_Ed1032PortTxWords_Object = MibTableColumn
ed1032PortTxWords = _Ed1032PortTxWords_Object(
    (1, 3, 6, 1, 4, 1, 289, 2, 1, 1, 1, 3, 1, 1, 11),
    _Ed1032PortTxWords_Type()
)
ed1032PortTxWords.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ed1032PortTxWords.setStatus("mandatory")
_Ed1032PortRxWords_Type = Counter32
_Ed1032PortRxWords_Object = MibTableColumn
ed1032PortRxWords = _Ed1032PortRxWords_Object(
    (1, 3, 6, 1, 4, 1, 289, 2, 1, 1, 1, 3, 1, 1, 12),
    _Ed1032PortRxWords_Type()
)
ed1032PortRxWords.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ed1032PortRxWords.setStatus("mandatory")
_Ed1032PortTxFrames_Type = Counter32
_Ed1032PortTxFrames_Object = MibTableColumn
ed1032PortTxFrames = _Ed1032PortTxFrames_Object(
    (1, 3, 6, 1, 4, 1, 289, 2, 1, 1, 1, 3, 1, 1, 13),
    _Ed1032PortTxFrames_Type()
)
ed1032PortTxFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ed1032PortTxFrames.setStatus("mandatory")
_Ed1032PortRxFrames_Type = Counter32
_Ed1032PortRxFrames_Object = MibTableColumn
ed1032PortRxFrames = _Ed1032PortRxFrames_Object(
    (1, 3, 6, 1, 4, 1, 289, 2, 1, 1, 1, 3, 1, 1, 14),
    _Ed1032PortRxFrames_Type()
)
ed1032PortRxFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ed1032PortRxFrames.setStatus("mandatory")
_Ed1032PortRxC2Frames_Type = Counter32
_Ed1032PortRxC2Frames_Object = MibTableColumn
ed1032PortRxC2Frames = _Ed1032PortRxC2Frames_Object(
    (1, 3, 6, 1, 4, 1, 289, 2, 1, 1, 1, 3, 1, 1, 15),
    _Ed1032PortRxC2Frames_Type()
)
ed1032PortRxC2Frames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ed1032PortRxC2Frames.setStatus("mandatory")
_Ed1032PortRxC3Frames_Type = Counter32
_Ed1032PortRxC3Frames_Object = MibTableColumn
ed1032PortRxC3Frames = _Ed1032PortRxC3Frames_Object(
    (1, 3, 6, 1, 4, 1, 289, 2, 1, 1, 1, 3, 1, 1, 16),
    _Ed1032PortRxC3Frames_Type()
)
ed1032PortRxC3Frames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ed1032PortRxC3Frames.setStatus("mandatory")
_Ed1032PortRxLCs_Type = Counter32
_Ed1032PortRxLCs_Object = MibTableColumn
ed1032PortRxLCs = _Ed1032PortRxLCs_Object(
    (1, 3, 6, 1, 4, 1, 289, 2, 1, 1, 1, 3, 1, 1, 17),
    _Ed1032PortRxLCs_Type()
)
ed1032PortRxLCs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ed1032PortRxLCs.setStatus("mandatory")
_Ed1032PortRxMcasts_Type = Counter32
_Ed1032PortRxMcasts_Object = MibTableColumn
ed1032PortRxMcasts = _Ed1032PortRxMcasts_Object(
    (1, 3, 6, 1, 4, 1, 289, 2, 1, 1, 1, 3, 1, 1, 18),
    _Ed1032PortRxMcasts_Type()
)
ed1032PortRxMcasts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ed1032PortRxMcasts.setStatus("mandatory")
_Ed1032PortTooManyRdys_Type = Counter32
_Ed1032PortTooManyRdys_Object = MibTableColumn
ed1032PortTooManyRdys = _Ed1032PortTooManyRdys_Object(
    (1, 3, 6, 1, 4, 1, 289, 2, 1, 1, 1, 3, 1, 1, 19),
    _Ed1032PortTooManyRdys_Type()
)
ed1032PortTooManyRdys.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ed1032PortTooManyRdys.setStatus("mandatory")
_Ed1032PortNoTxCredits_Type = Counter32
_Ed1032PortNoTxCredits_Object = MibTableColumn
ed1032PortNoTxCredits = _Ed1032PortNoTxCredits_Object(
    (1, 3, 6, 1, 4, 1, 289, 2, 1, 1, 1, 3, 1, 1, 20),
    _Ed1032PortNoTxCredits_Type()
)
ed1032PortNoTxCredits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ed1032PortNoTxCredits.setStatus("mandatory")
_Ed1032PortRxEncFrs_Type = Counter32
_Ed1032PortRxEncFrs_Object = MibTableColumn
ed1032PortRxEncFrs = _Ed1032PortRxEncFrs_Object(
    (1, 3, 6, 1, 4, 1, 289, 2, 1, 1, 1, 3, 1, 1, 21),
    _Ed1032PortRxEncFrs_Type()
)
ed1032PortRxEncFrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ed1032PortRxEncFrs.setStatus("mandatory")
_Ed1032PortRxCrcs_Type = Counter32
_Ed1032PortRxCrcs_Object = MibTableColumn
ed1032PortRxCrcs = _Ed1032PortRxCrcs_Object(
    (1, 3, 6, 1, 4, 1, 289, 2, 1, 1, 1, 3, 1, 1, 22),
    _Ed1032PortRxCrcs_Type()
)
ed1032PortRxCrcs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ed1032PortRxCrcs.setStatus("mandatory")
_Ed1032PortRxTruncs_Type = Counter32
_Ed1032PortRxTruncs_Object = MibTableColumn
ed1032PortRxTruncs = _Ed1032PortRxTruncs_Object(
    (1, 3, 6, 1, 4, 1, 289, 2, 1, 1, 1, 3, 1, 1, 23),
    _Ed1032PortRxTruncs_Type()
)
ed1032PortRxTruncs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ed1032PortRxTruncs.setStatus("mandatory")
_Ed1032PortRxTooLongs_Type = Counter32
_Ed1032PortRxTooLongs_Object = MibTableColumn
ed1032PortRxTooLongs = _Ed1032PortRxTooLongs_Object(
    (1, 3, 6, 1, 4, 1, 289, 2, 1, 1, 1, 3, 1, 1, 24),
    _Ed1032PortRxTooLongs_Type()
)
ed1032PortRxTooLongs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ed1032PortRxTooLongs.setStatus("mandatory")
_Ed1032PortRxBadEofs_Type = Counter32
_Ed1032PortRxBadEofs_Object = MibTableColumn
ed1032PortRxBadEofs = _Ed1032PortRxBadEofs_Object(
    (1, 3, 6, 1, 4, 1, 289, 2, 1, 1, 1, 3, 1, 1, 25),
    _Ed1032PortRxBadEofs_Type()
)
ed1032PortRxBadEofs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ed1032PortRxBadEofs.setStatus("mandatory")
_Ed1032PortRxBadOs_Type = Counter32
_Ed1032PortRxBadOs_Object = MibTableColumn
ed1032PortRxBadOs = _Ed1032PortRxBadOs_Object(
    (1, 3, 6, 1, 4, 1, 289, 2, 1, 1, 1, 3, 1, 1, 26),
    _Ed1032PortRxBadOs_Type()
)
ed1032PortRxBadOs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ed1032PortRxBadOs.setStatus("mandatory")
_Ed1032PortC3Discards_Type = Counter32
_Ed1032PortC3Discards_Object = MibTableColumn
ed1032PortC3Discards = _Ed1032PortC3Discards_Object(
    (1, 3, 6, 1, 4, 1, 289, 2, 1, 1, 1, 3, 1, 1, 27),
    _Ed1032PortC3Discards_Type()
)
ed1032PortC3Discards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ed1032PortC3Discards.setStatus("mandatory")
_Ed1032PortMcastTimedOuts_Type = Counter32
_Ed1032PortMcastTimedOuts_Object = MibTableColumn
ed1032PortMcastTimedOuts = _Ed1032PortMcastTimedOuts_Object(
    (1, 3, 6, 1, 4, 1, 289, 2, 1, 1, 1, 3, 1, 1, 28),
    _Ed1032PortMcastTimedOuts_Type()
)
ed1032PortMcastTimedOuts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ed1032PortMcastTimedOuts.setStatus("mandatory")
_Ed1032PortTxMcasts_Type = Counter32
_Ed1032PortTxMcasts_Object = MibTableColumn
ed1032PortTxMcasts = _Ed1032PortTxMcasts_Object(
    (1, 3, 6, 1, 4, 1, 289, 2, 1, 1, 1, 3, 1, 1, 29),
    _Ed1032PortTxMcasts_Type()
)
ed1032PortTxMcasts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ed1032PortTxMcasts.setStatus("mandatory")
_Ed1032PortTxThroughput_Type = Counter32
_Ed1032PortTxThroughput_Object = MibTableColumn
ed1032PortTxThroughput = _Ed1032PortTxThroughput_Object(
    (1, 3, 6, 1, 4, 1, 289, 2, 1, 1, 1, 3, 1, 1, 30),
    _Ed1032PortTxThroughput_Type()
)
ed1032PortTxThroughput.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ed1032PortTxThroughput.setStatus("mandatory")
_Ed1032PortRxThroughput_Type = Counter32
_Ed1032PortRxThroughput_Object = MibTableColumn
ed1032PortRxThroughput = _Ed1032PortRxThroughput_Object(
    (1, 3, 6, 1, 4, 1, 289, 2, 1, 1, 1, 3, 1, 1, 31),
    _Ed1032PortRxThroughput_Type()
)
ed1032PortRxThroughput.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ed1032PortRxThroughput.setStatus("mandatory")

# Managed Objects groups


# Notification objects

ed1032PortScn = NotificationType(
    (1, 3, 6, 1, 4, 1, 289, 0, 1)
)
ed1032PortScn.setObjects(
    ("ED-1032-MIB", "ed1032PortOpStatus")
)
if mibBuilder.loadTexts:
    ed1032PortScn.setStatus(
        ""
    )

ed1032FruScn = NotificationType(
    (1, 3, 6, 1, 4, 1, 289, 0, 2)
)
ed1032FruScn.setObjects(
    ("ED-1032-MIB", "ed1032FruStatus")
)
if mibBuilder.loadTexts:
    ed1032FruScn.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ED-1032-MIB",
    **{"DisplayString": DisplayString,
       "Ed1032SysOperStatus": Ed1032SysOperStatus,
       "Ed1032SysState": Ed1032SysState,
       "Ed1032FruCode": Ed1032FruCode,
       "Ed1032FruPosition": Ed1032FruPosition,
       "Ed1032FruStatus": Ed1032FruStatus,
       "Ed1032PortIndex": Ed1032PortIndex,
       "Ed1032PortPhyState": Ed1032PortPhyState,
       "Ed1032PortStatus": Ed1032PortStatus,
       "Ed1032PortAdmStatus": Ed1032PortAdmStatus,
       "mcData": mcData,
       "ed1032PortScn": ed1032PortScn,
       "ed1032FruScn": ed1032FruScn,
       "commDev": commDev,
       "fibreChannel": fibreChannel,
       "fcSwitch": fcSwitch,
       "ed-1032": ed_1032,
       "ed1032Sys": ed1032Sys,
       "ed1032SysCurrentDate": ed1032SysCurrentDate,
       "ed1032SysBootDate": ed1032SysBootDate,
       "ed1032SysFirmwareVersion": ed1032SysFirmwareVersion,
       "ed1032SysTypeNum": ed1032SysTypeNum,
       "ed1032SysModelNum": ed1032SysModelNum,
       "ed1032SysMfg": ed1032SysMfg,
       "ed1032SysPlantOfMfg": ed1032SysPlantOfMfg,
       "ed1032SysSeqNum": ed1032SysSeqNum,
       "ed1032SysEcLevel": ed1032SysEcLevel,
       "ed1032SysOemSerialNum": ed1032SysOemSerialNum,
       "ed1032SysOperStatus": ed1032SysOperStatus,
       "ed1032SysState": ed1032SysState,
       "ed1032SysAdmStatus": ed1032SysAdmStatus,
       "ed1032Fru": ed1032Fru,
       "ed1032FruTable": ed1032FruTable,
       "ed1032FruEntry": ed1032FruEntry,
       "ed1032FruCode": ed1032FruCode,
       "ed1032FruPosition": ed1032FruPosition,
       "ed1032FruStatus": ed1032FruStatus,
       "ed1032FruPartNumber": ed1032FruPartNumber,
       "ed1032FruSerialNumber": ed1032FruSerialNumber,
       "ed1032FruPowerOnHours": ed1032FruPowerOnHours,
       "ed1032FruTestDate": ed1032FruTestDate,
       "ed1032Port": ed1032Port,
       "ed1032PortTable": ed1032PortTable,
       "ed1032PortEntry": ed1032PortEntry,
       "ed1032PortIndex": ed1032PortIndex,
       "ed1032PortPhyState": ed1032PortPhyState,
       "ed1032PortOpStatus": ed1032PortOpStatus,
       "ed1032PortAdmStatus": ed1032PortAdmStatus,
       "ed1032PortTxWords": ed1032PortTxWords,
       "ed1032PortRxWords": ed1032PortRxWords,
       "ed1032PortTxFrames": ed1032PortTxFrames,
       "ed1032PortRxFrames": ed1032PortRxFrames,
       "ed1032PortRxC2Frames": ed1032PortRxC2Frames,
       "ed1032PortRxC3Frames": ed1032PortRxC3Frames,
       "ed1032PortRxLCs": ed1032PortRxLCs,
       "ed1032PortRxMcasts": ed1032PortRxMcasts,
       "ed1032PortTooManyRdys": ed1032PortTooManyRdys,
       "ed1032PortNoTxCredits": ed1032PortNoTxCredits,
       "ed1032PortRxEncFrs": ed1032PortRxEncFrs,
       "ed1032PortRxCrcs": ed1032PortRxCrcs,
       "ed1032PortRxTruncs": ed1032PortRxTruncs,
       "ed1032PortRxTooLongs": ed1032PortRxTooLongs,
       "ed1032PortRxBadEofs": ed1032PortRxBadEofs,
       "ed1032PortRxBadOs": ed1032PortRxBadOs,
       "ed1032PortC3Discards": ed1032PortC3Discards,
       "ed1032PortMcastTimedOuts": ed1032PortMcastTimedOuts,
       "ed1032PortTxMcasts": ed1032PortTxMcasts,
       "ed1032PortTxThroughput": ed1032PortTxThroughput,
       "ed1032PortRxThroughput": ed1032PortRxThroughput}
)
