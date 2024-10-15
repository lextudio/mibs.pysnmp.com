# SNMP MIB module (ED-5000-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ED-5000-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:36:32 2024
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




class Ed5000SysOperStatus(Integer32):
    """Custom type Ed5000SysOperStatus based on Integer32"""
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





class Ed5000SysState(Integer32):
    """Custom type Ed5000SysState based on Integer32"""
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





class Ed5000FruCode(Integer32):
    """Custom type Ed5000FruCode based on Integer32"""
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





class Ed5000FruPosition(Integer32):
    """Custom type Ed5000FruPosition based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )





class Ed5000FruStatus(Integer32):
    """Custom type Ed5000FruStatus based on Integer32"""
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





class Ed5000PortIndex(Integer32):
    """Custom type Ed5000PortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2048),
    )





class Ed5000PortPhyState(Integer32):
    """Custom type Ed5000PortPhyState based on Integer32"""
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





class Ed5000PortStatus(Integer32):
    """Custom type Ed5000PortStatus based on Integer32"""
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





class Ed5000PortAdmStatus(Integer32):
    """Custom type Ed5000PortAdmStatus based on Integer32"""
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
_Ed_5000_ObjectIdentity = ObjectIdentity
ed_5000 = _Ed_5000_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 289, 2, 1, 1, 1)
)
_Ed5000Sys_ObjectIdentity = ObjectIdentity
ed5000Sys = _Ed5000Sys_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 289, 2, 1, 1, 1, 1)
)


class _Ed5000SysCurrentDate_Type(DisplayString):
    """Custom type ed5000SysCurrentDate based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(64, 64),
    )


_Ed5000SysCurrentDate_Type.__name__ = "DisplayString"
_Ed5000SysCurrentDate_Object = MibScalar
ed5000SysCurrentDate = _Ed5000SysCurrentDate_Object(
    (1, 3, 6, 1, 4, 1, 289, 2, 1, 1, 1, 1, 1),
    _Ed5000SysCurrentDate_Type()
)
ed5000SysCurrentDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ed5000SysCurrentDate.setStatus("mandatory")


class _Ed5000SysBootDate_Type(DisplayString):
    """Custom type ed5000SysBootDate based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(64, 64),
    )


_Ed5000SysBootDate_Type.__name__ = "DisplayString"
_Ed5000SysBootDate_Object = MibScalar
ed5000SysBootDate = _Ed5000SysBootDate_Object(
    (1, 3, 6, 1, 4, 1, 289, 2, 1, 1, 1, 1, 2),
    _Ed5000SysBootDate_Type()
)
ed5000SysBootDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ed5000SysBootDate.setStatus("mandatory")


class _Ed5000SysFirmwareVersion_Type(DisplayString):
    """Custom type ed5000SysFirmwareVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(24, 24),
    )


_Ed5000SysFirmwareVersion_Type.__name__ = "DisplayString"
_Ed5000SysFirmwareVersion_Object = MibScalar
ed5000SysFirmwareVersion = _Ed5000SysFirmwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 289, 2, 1, 1, 1, 1, 3),
    _Ed5000SysFirmwareVersion_Type()
)
ed5000SysFirmwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ed5000SysFirmwareVersion.setStatus("mandatory")


class _Ed5000SysTypeNum_Type(DisplayString):
    """Custom type ed5000SysTypeNum based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(64, 64),
    )


_Ed5000SysTypeNum_Type.__name__ = "DisplayString"
_Ed5000SysTypeNum_Object = MibScalar
ed5000SysTypeNum = _Ed5000SysTypeNum_Object(
    (1, 3, 6, 1, 4, 1, 289, 2, 1, 1, 1, 1, 4),
    _Ed5000SysTypeNum_Type()
)
ed5000SysTypeNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ed5000SysTypeNum.setStatus("mandatory")


class _Ed5000SysModelNum_Type(DisplayString):
    """Custom type ed5000SysModelNum based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(64, 64),
    )


_Ed5000SysModelNum_Type.__name__ = "DisplayString"
_Ed5000SysModelNum_Object = MibScalar
ed5000SysModelNum = _Ed5000SysModelNum_Object(
    (1, 3, 6, 1, 4, 1, 289, 2, 1, 1, 1, 1, 5),
    _Ed5000SysModelNum_Type()
)
ed5000SysModelNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ed5000SysModelNum.setStatus("mandatory")


class _Ed5000SysMfg_Type(DisplayString):
    """Custom type ed5000SysMfg based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(64, 64),
    )


_Ed5000SysMfg_Type.__name__ = "DisplayString"
_Ed5000SysMfg_Object = MibScalar
ed5000SysMfg = _Ed5000SysMfg_Object(
    (1, 3, 6, 1, 4, 1, 289, 2, 1, 1, 1, 1, 6),
    _Ed5000SysMfg_Type()
)
ed5000SysMfg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ed5000SysMfg.setStatus("mandatory")


class _Ed5000SysPlantOfMfg_Type(DisplayString):
    """Custom type ed5000SysPlantOfMfg based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(64, 64),
    )


_Ed5000SysPlantOfMfg_Type.__name__ = "DisplayString"
_Ed5000SysPlantOfMfg_Object = MibScalar
ed5000SysPlantOfMfg = _Ed5000SysPlantOfMfg_Object(
    (1, 3, 6, 1, 4, 1, 289, 2, 1, 1, 1, 1, 7),
    _Ed5000SysPlantOfMfg_Type()
)
ed5000SysPlantOfMfg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ed5000SysPlantOfMfg.setStatus("mandatory")


class _Ed5000SysSeqNum_Type(DisplayString):
    """Custom type ed5000SysSeqNum based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(64, 64),
    )


_Ed5000SysSeqNum_Type.__name__ = "DisplayString"
_Ed5000SysSeqNum_Object = MibScalar
ed5000SysSeqNum = _Ed5000SysSeqNum_Object(
    (1, 3, 6, 1, 4, 1, 289, 2, 1, 1, 1, 1, 8),
    _Ed5000SysSeqNum_Type()
)
ed5000SysSeqNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ed5000SysSeqNum.setStatus("mandatory")


class _Ed5000SysEcLevel_Type(DisplayString):
    """Custom type ed5000SysEcLevel based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(64, 64),
    )


_Ed5000SysEcLevel_Type.__name__ = "DisplayString"
_Ed5000SysEcLevel_Object = MibScalar
ed5000SysEcLevel = _Ed5000SysEcLevel_Object(
    (1, 3, 6, 1, 4, 1, 289, 2, 1, 1, 1, 1, 9),
    _Ed5000SysEcLevel_Type()
)
ed5000SysEcLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ed5000SysEcLevel.setStatus("mandatory")


class _Ed5000SysOemSerialNum_Type(DisplayString):
    """Custom type ed5000SysOemSerialNum based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(64, 64),
    )


_Ed5000SysOemSerialNum_Type.__name__ = "DisplayString"
_Ed5000SysOemSerialNum_Object = MibScalar
ed5000SysOemSerialNum = _Ed5000SysOemSerialNum_Object(
    (1, 3, 6, 1, 4, 1, 289, 2, 1, 1, 1, 1, 10),
    _Ed5000SysOemSerialNum_Type()
)
ed5000SysOemSerialNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ed5000SysOemSerialNum.setStatus("mandatory")
_Ed5000SysOperStatus_Type = Ed5000SysOperStatus
_Ed5000SysOperStatus_Object = MibScalar
ed5000SysOperStatus = _Ed5000SysOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 289, 2, 1, 1, 1, 1, 11),
    _Ed5000SysOperStatus_Type()
)
ed5000SysOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ed5000SysOperStatus.setStatus("mandatory")
_Ed5000SysState_Type = Ed5000SysState
_Ed5000SysState_Object = MibScalar
ed5000SysState = _Ed5000SysState_Object(
    (1, 3, 6, 1, 4, 1, 289, 2, 1, 1, 1, 1, 12),
    _Ed5000SysState_Type()
)
ed5000SysState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ed5000SysState.setStatus("mandatory")


class _Ed5000SysAdmStatus_Type(Integer32):
    """Custom type ed5000SysAdmStatus based on Integer32"""
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


_Ed5000SysAdmStatus_Type.__name__ = "Integer32"
_Ed5000SysAdmStatus_Object = MibScalar
ed5000SysAdmStatus = _Ed5000SysAdmStatus_Object(
    (1, 3, 6, 1, 4, 1, 289, 2, 1, 1, 1, 1, 13),
    _Ed5000SysAdmStatus_Type()
)
ed5000SysAdmStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ed5000SysAdmStatus.setStatus("mandatory")
_Ed5000Fru_ObjectIdentity = ObjectIdentity
ed5000Fru = _Ed5000Fru_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 289, 2, 1, 1, 1, 2)
)
_Ed5000FruTable_Object = MibTable
ed5000FruTable = _Ed5000FruTable_Object(
    (1, 3, 6, 1, 4, 1, 289, 2, 1, 1, 1, 2, 1)
)
if mibBuilder.loadTexts:
    ed5000FruTable.setStatus("mandatory")
_Ed5000FruEntry_Object = MibTableRow
ed5000FruEntry = _Ed5000FruEntry_Object(
    (1, 3, 6, 1, 4, 1, 289, 2, 1, 1, 1, 2, 1, 1)
)
ed5000FruEntry.setIndexNames(
    (0, "ED-5000-MIB", "ed5000FruCode"),
    (0, "ED-5000-MIB", "ed5000FruPosition"),
)
if mibBuilder.loadTexts:
    ed5000FruEntry.setStatus("mandatory")
_Ed5000FruCode_Type = Ed5000FruCode
_Ed5000FruCode_Object = MibTableColumn
ed5000FruCode = _Ed5000FruCode_Object(
    (1, 3, 6, 1, 4, 1, 289, 2, 1, 1, 1, 2, 1, 1, 1),
    _Ed5000FruCode_Type()
)
ed5000FruCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ed5000FruCode.setStatus("mandatory")
_Ed5000FruPosition_Type = Ed5000FruPosition
_Ed5000FruPosition_Object = MibTableColumn
ed5000FruPosition = _Ed5000FruPosition_Object(
    (1, 3, 6, 1, 4, 1, 289, 2, 1, 1, 1, 2, 1, 1, 2),
    _Ed5000FruPosition_Type()
)
ed5000FruPosition.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ed5000FruPosition.setStatus("mandatory")
_Ed5000FruStatus_Type = Ed5000FruStatus
_Ed5000FruStatus_Object = MibTableColumn
ed5000FruStatus = _Ed5000FruStatus_Object(
    (1, 3, 6, 1, 4, 1, 289, 2, 1, 1, 1, 2, 1, 1, 3),
    _Ed5000FruStatus_Type()
)
ed5000FruStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ed5000FruStatus.setStatus("mandatory")


class _Ed5000FruPartNumber_Type(DisplayString):
    """Custom type ed5000FruPartNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(64, 64),
    )


_Ed5000FruPartNumber_Type.__name__ = "DisplayString"
_Ed5000FruPartNumber_Object = MibTableColumn
ed5000FruPartNumber = _Ed5000FruPartNumber_Object(
    (1, 3, 6, 1, 4, 1, 289, 2, 1, 1, 1, 2, 1, 1, 4),
    _Ed5000FruPartNumber_Type()
)
ed5000FruPartNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ed5000FruPartNumber.setStatus("mandatory")


class _Ed5000FruSerialNumber_Type(DisplayString):
    """Custom type ed5000FruSerialNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(64, 64),
    )


_Ed5000FruSerialNumber_Type.__name__ = "DisplayString"
_Ed5000FruSerialNumber_Object = MibTableColumn
ed5000FruSerialNumber = _Ed5000FruSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 289, 2, 1, 1, 1, 2, 1, 1, 5),
    _Ed5000FruSerialNumber_Type()
)
ed5000FruSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ed5000FruSerialNumber.setStatus("mandatory")
_Ed5000FruPowerOnHours_Type = Counter32
_Ed5000FruPowerOnHours_Object = MibTableColumn
ed5000FruPowerOnHours = _Ed5000FruPowerOnHours_Object(
    (1, 3, 6, 1, 4, 1, 289, 2, 1, 1, 1, 2, 1, 1, 6),
    _Ed5000FruPowerOnHours_Type()
)
ed5000FruPowerOnHours.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ed5000FruPowerOnHours.setStatus("mandatory")


class _Ed5000FruTestDate_Type(DisplayString):
    """Custom type ed5000FruTestDate based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(64, 64),
    )


_Ed5000FruTestDate_Type.__name__ = "DisplayString"
_Ed5000FruTestDate_Object = MibTableColumn
ed5000FruTestDate = _Ed5000FruTestDate_Object(
    (1, 3, 6, 1, 4, 1, 289, 2, 1, 1, 1, 2, 1, 1, 7),
    _Ed5000FruTestDate_Type()
)
ed5000FruTestDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ed5000FruTestDate.setStatus("mandatory")
_Ed5000Port_ObjectIdentity = ObjectIdentity
ed5000Port = _Ed5000Port_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 289, 2, 1, 1, 1, 3)
)
_Ed5000PortTable_Object = MibTable
ed5000PortTable = _Ed5000PortTable_Object(
    (1, 3, 6, 1, 4, 1, 289, 2, 1, 1, 1, 3, 1)
)
if mibBuilder.loadTexts:
    ed5000PortTable.setStatus("mandatory")
_Ed5000PortEntry_Object = MibTableRow
ed5000PortEntry = _Ed5000PortEntry_Object(
    (1, 3, 6, 1, 4, 1, 289, 2, 1, 1, 1, 3, 1, 1)
)
ed5000PortEntry.setIndexNames(
    (0, "ED-5000-MIB", "ed5000PortIndex"),
)
if mibBuilder.loadTexts:
    ed5000PortEntry.setStatus("mandatory")
_Ed5000PortIndex_Type = Ed5000PortIndex
_Ed5000PortIndex_Object = MibTableColumn
ed5000PortIndex = _Ed5000PortIndex_Object(
    (1, 3, 6, 1, 4, 1, 289, 2, 1, 1, 1, 3, 1, 1, 1),
    _Ed5000PortIndex_Type()
)
ed5000PortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ed5000PortIndex.setStatus("mandatory")
_Ed5000PortPhyState_Type = Ed5000PortPhyState
_Ed5000PortPhyState_Object = MibTableColumn
ed5000PortPhyState = _Ed5000PortPhyState_Object(
    (1, 3, 6, 1, 4, 1, 289, 2, 1, 1, 1, 3, 1, 1, 2),
    _Ed5000PortPhyState_Type()
)
ed5000PortPhyState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ed5000PortPhyState.setStatus("mandatory")
_Ed5000PortOpStatus_Type = Ed5000PortStatus
_Ed5000PortOpStatus_Object = MibTableColumn
ed5000PortOpStatus = _Ed5000PortOpStatus_Object(
    (1, 3, 6, 1, 4, 1, 289, 2, 1, 1, 1, 3, 1, 1, 3),
    _Ed5000PortOpStatus_Type()
)
ed5000PortOpStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ed5000PortOpStatus.setStatus("mandatory")
_Ed5000PortAdmStatus_Type = Ed5000PortAdmStatus
_Ed5000PortAdmStatus_Object = MibTableColumn
ed5000PortAdmStatus = _Ed5000PortAdmStatus_Object(
    (1, 3, 6, 1, 4, 1, 289, 2, 1, 1, 1, 3, 1, 1, 4),
    _Ed5000PortAdmStatus_Type()
)
ed5000PortAdmStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ed5000PortAdmStatus.setStatus("mandatory")
_Ed5000PortTxWords_Type = Counter32
_Ed5000PortTxWords_Object = MibTableColumn
ed5000PortTxWords = _Ed5000PortTxWords_Object(
    (1, 3, 6, 1, 4, 1, 289, 2, 1, 1, 1, 3, 1, 1, 11),
    _Ed5000PortTxWords_Type()
)
ed5000PortTxWords.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ed5000PortTxWords.setStatus("mandatory")
_Ed5000PortRxWords_Type = Counter32
_Ed5000PortRxWords_Object = MibTableColumn
ed5000PortRxWords = _Ed5000PortRxWords_Object(
    (1, 3, 6, 1, 4, 1, 289, 2, 1, 1, 1, 3, 1, 1, 12),
    _Ed5000PortRxWords_Type()
)
ed5000PortRxWords.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ed5000PortRxWords.setStatus("mandatory")
_Ed5000PortTxFrames_Type = Counter32
_Ed5000PortTxFrames_Object = MibTableColumn
ed5000PortTxFrames = _Ed5000PortTxFrames_Object(
    (1, 3, 6, 1, 4, 1, 289, 2, 1, 1, 1, 3, 1, 1, 13),
    _Ed5000PortTxFrames_Type()
)
ed5000PortTxFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ed5000PortTxFrames.setStatus("mandatory")
_Ed5000PortRxFrames_Type = Counter32
_Ed5000PortRxFrames_Object = MibTableColumn
ed5000PortRxFrames = _Ed5000PortRxFrames_Object(
    (1, 3, 6, 1, 4, 1, 289, 2, 1, 1, 1, 3, 1, 1, 14),
    _Ed5000PortRxFrames_Type()
)
ed5000PortRxFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ed5000PortRxFrames.setStatus("mandatory")
_Ed5000PortRxC2Frames_Type = Counter32
_Ed5000PortRxC2Frames_Object = MibTableColumn
ed5000PortRxC2Frames = _Ed5000PortRxC2Frames_Object(
    (1, 3, 6, 1, 4, 1, 289, 2, 1, 1, 1, 3, 1, 1, 15),
    _Ed5000PortRxC2Frames_Type()
)
ed5000PortRxC2Frames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ed5000PortRxC2Frames.setStatus("mandatory")
_Ed5000PortRxC3Frames_Type = Counter32
_Ed5000PortRxC3Frames_Object = MibTableColumn
ed5000PortRxC3Frames = _Ed5000PortRxC3Frames_Object(
    (1, 3, 6, 1, 4, 1, 289, 2, 1, 1, 1, 3, 1, 1, 16),
    _Ed5000PortRxC3Frames_Type()
)
ed5000PortRxC3Frames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ed5000PortRxC3Frames.setStatus("mandatory")
_Ed5000PortRxLCs_Type = Counter32
_Ed5000PortRxLCs_Object = MibTableColumn
ed5000PortRxLCs = _Ed5000PortRxLCs_Object(
    (1, 3, 6, 1, 4, 1, 289, 2, 1, 1, 1, 3, 1, 1, 17),
    _Ed5000PortRxLCs_Type()
)
ed5000PortRxLCs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ed5000PortRxLCs.setStatus("mandatory")
_Ed5000PortRxMcasts_Type = Counter32
_Ed5000PortRxMcasts_Object = MibTableColumn
ed5000PortRxMcasts = _Ed5000PortRxMcasts_Object(
    (1, 3, 6, 1, 4, 1, 289, 2, 1, 1, 1, 3, 1, 1, 18),
    _Ed5000PortRxMcasts_Type()
)
ed5000PortRxMcasts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ed5000PortRxMcasts.setStatus("mandatory")
_Ed5000PortTooManyRdys_Type = Counter32
_Ed5000PortTooManyRdys_Object = MibTableColumn
ed5000PortTooManyRdys = _Ed5000PortTooManyRdys_Object(
    (1, 3, 6, 1, 4, 1, 289, 2, 1, 1, 1, 3, 1, 1, 19),
    _Ed5000PortTooManyRdys_Type()
)
ed5000PortTooManyRdys.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ed5000PortTooManyRdys.setStatus("mandatory")
_Ed5000PortNoTxCredits_Type = Counter32
_Ed5000PortNoTxCredits_Object = MibTableColumn
ed5000PortNoTxCredits = _Ed5000PortNoTxCredits_Object(
    (1, 3, 6, 1, 4, 1, 289, 2, 1, 1, 1, 3, 1, 1, 20),
    _Ed5000PortNoTxCredits_Type()
)
ed5000PortNoTxCredits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ed5000PortNoTxCredits.setStatus("mandatory")
_Ed5000PortRxEncFrs_Type = Counter32
_Ed5000PortRxEncFrs_Object = MibTableColumn
ed5000PortRxEncFrs = _Ed5000PortRxEncFrs_Object(
    (1, 3, 6, 1, 4, 1, 289, 2, 1, 1, 1, 3, 1, 1, 21),
    _Ed5000PortRxEncFrs_Type()
)
ed5000PortRxEncFrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ed5000PortRxEncFrs.setStatus("mandatory")
_Ed5000PortRxCrcs_Type = Counter32
_Ed5000PortRxCrcs_Object = MibTableColumn
ed5000PortRxCrcs = _Ed5000PortRxCrcs_Object(
    (1, 3, 6, 1, 4, 1, 289, 2, 1, 1, 1, 3, 1, 1, 22),
    _Ed5000PortRxCrcs_Type()
)
ed5000PortRxCrcs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ed5000PortRxCrcs.setStatus("mandatory")
_Ed5000PortRxTruncs_Type = Counter32
_Ed5000PortRxTruncs_Object = MibTableColumn
ed5000PortRxTruncs = _Ed5000PortRxTruncs_Object(
    (1, 3, 6, 1, 4, 1, 289, 2, 1, 1, 1, 3, 1, 1, 23),
    _Ed5000PortRxTruncs_Type()
)
ed5000PortRxTruncs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ed5000PortRxTruncs.setStatus("mandatory")
_Ed5000PortRxTooLongs_Type = Counter32
_Ed5000PortRxTooLongs_Object = MibTableColumn
ed5000PortRxTooLongs = _Ed5000PortRxTooLongs_Object(
    (1, 3, 6, 1, 4, 1, 289, 2, 1, 1, 1, 3, 1, 1, 24),
    _Ed5000PortRxTooLongs_Type()
)
ed5000PortRxTooLongs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ed5000PortRxTooLongs.setStatus("mandatory")
_Ed5000PortRxBadEofs_Type = Counter32
_Ed5000PortRxBadEofs_Object = MibTableColumn
ed5000PortRxBadEofs = _Ed5000PortRxBadEofs_Object(
    (1, 3, 6, 1, 4, 1, 289, 2, 1, 1, 1, 3, 1, 1, 25),
    _Ed5000PortRxBadEofs_Type()
)
ed5000PortRxBadEofs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ed5000PortRxBadEofs.setStatus("mandatory")
_Ed5000PortRxBadOs_Type = Counter32
_Ed5000PortRxBadOs_Object = MibTableColumn
ed5000PortRxBadOs = _Ed5000PortRxBadOs_Object(
    (1, 3, 6, 1, 4, 1, 289, 2, 1, 1, 1, 3, 1, 1, 26),
    _Ed5000PortRxBadOs_Type()
)
ed5000PortRxBadOs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ed5000PortRxBadOs.setStatus("mandatory")
_Ed5000PortC3Discards_Type = Counter32
_Ed5000PortC3Discards_Object = MibTableColumn
ed5000PortC3Discards = _Ed5000PortC3Discards_Object(
    (1, 3, 6, 1, 4, 1, 289, 2, 1, 1, 1, 3, 1, 1, 27),
    _Ed5000PortC3Discards_Type()
)
ed5000PortC3Discards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ed5000PortC3Discards.setStatus("mandatory")
_Ed5000PortMcastTimedOuts_Type = Counter32
_Ed5000PortMcastTimedOuts_Object = MibTableColumn
ed5000PortMcastTimedOuts = _Ed5000PortMcastTimedOuts_Object(
    (1, 3, 6, 1, 4, 1, 289, 2, 1, 1, 1, 3, 1, 1, 28),
    _Ed5000PortMcastTimedOuts_Type()
)
ed5000PortMcastTimedOuts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ed5000PortMcastTimedOuts.setStatus("mandatory")
_Ed5000PortTxMcasts_Type = Counter32
_Ed5000PortTxMcasts_Object = MibTableColumn
ed5000PortTxMcasts = _Ed5000PortTxMcasts_Object(
    (1, 3, 6, 1, 4, 1, 289, 2, 1, 1, 1, 3, 1, 1, 29),
    _Ed5000PortTxMcasts_Type()
)
ed5000PortTxMcasts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ed5000PortTxMcasts.setStatus("mandatory")
_Ed5000PortTxThroughput_Type = Counter32
_Ed5000PortTxThroughput_Object = MibTableColumn
ed5000PortTxThroughput = _Ed5000PortTxThroughput_Object(
    (1, 3, 6, 1, 4, 1, 289, 2, 1, 1, 1, 3, 1, 1, 30),
    _Ed5000PortTxThroughput_Type()
)
ed5000PortTxThroughput.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ed5000PortTxThroughput.setStatus("mandatory")
_Ed5000PortRxThroughput_Type = Counter32
_Ed5000PortRxThroughput_Object = MibTableColumn
ed5000PortRxThroughput = _Ed5000PortRxThroughput_Object(
    (1, 3, 6, 1, 4, 1, 289, 2, 1, 1, 1, 3, 1, 1, 31),
    _Ed5000PortRxThroughput_Type()
)
ed5000PortRxThroughput.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ed5000PortRxThroughput.setStatus("mandatory")

# Managed Objects groups


# Notification objects

ed5000PortScn = NotificationType(
    (1, 3, 6, 1, 4, 1, 289, 0, 1)
)
ed5000PortScn.setObjects(
    ("ED-5000-MIB", "ed5000PortOpStatus")
)
if mibBuilder.loadTexts:
    ed5000PortScn.setStatus(
        ""
    )

ed5000FruScn = NotificationType(
    (1, 3, 6, 1, 4, 1, 289, 0, 2)
)
ed5000FruScn.setObjects(
    ("ED-5000-MIB", "ed5000FruStatus")
)
if mibBuilder.loadTexts:
    ed5000FruScn.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ED-5000-MIB",
    **{"DisplayString": DisplayString,
       "Ed5000SysOperStatus": Ed5000SysOperStatus,
       "Ed5000SysState": Ed5000SysState,
       "Ed5000FruCode": Ed5000FruCode,
       "Ed5000FruPosition": Ed5000FruPosition,
       "Ed5000FruStatus": Ed5000FruStatus,
       "Ed5000PortIndex": Ed5000PortIndex,
       "Ed5000PortPhyState": Ed5000PortPhyState,
       "Ed5000PortStatus": Ed5000PortStatus,
       "Ed5000PortAdmStatus": Ed5000PortAdmStatus,
       "mcData": mcData,
       "ed5000PortScn": ed5000PortScn,
       "ed5000FruScn": ed5000FruScn,
       "commDev": commDev,
       "fibreChannel": fibreChannel,
       "fcSwitch": fcSwitch,
       "ed-5000": ed_5000,
       "ed5000Sys": ed5000Sys,
       "ed5000SysCurrentDate": ed5000SysCurrentDate,
       "ed5000SysBootDate": ed5000SysBootDate,
       "ed5000SysFirmwareVersion": ed5000SysFirmwareVersion,
       "ed5000SysTypeNum": ed5000SysTypeNum,
       "ed5000SysModelNum": ed5000SysModelNum,
       "ed5000SysMfg": ed5000SysMfg,
       "ed5000SysPlantOfMfg": ed5000SysPlantOfMfg,
       "ed5000SysSeqNum": ed5000SysSeqNum,
       "ed5000SysEcLevel": ed5000SysEcLevel,
       "ed5000SysOemSerialNum": ed5000SysOemSerialNum,
       "ed5000SysOperStatus": ed5000SysOperStatus,
       "ed5000SysState": ed5000SysState,
       "ed5000SysAdmStatus": ed5000SysAdmStatus,
       "ed5000Fru": ed5000Fru,
       "ed5000FruTable": ed5000FruTable,
       "ed5000FruEntry": ed5000FruEntry,
       "ed5000FruCode": ed5000FruCode,
       "ed5000FruPosition": ed5000FruPosition,
       "ed5000FruStatus": ed5000FruStatus,
       "ed5000FruPartNumber": ed5000FruPartNumber,
       "ed5000FruSerialNumber": ed5000FruSerialNumber,
       "ed5000FruPowerOnHours": ed5000FruPowerOnHours,
       "ed5000FruTestDate": ed5000FruTestDate,
       "ed5000Port": ed5000Port,
       "ed5000PortTable": ed5000PortTable,
       "ed5000PortEntry": ed5000PortEntry,
       "ed5000PortIndex": ed5000PortIndex,
       "ed5000PortPhyState": ed5000PortPhyState,
       "ed5000PortOpStatus": ed5000PortOpStatus,
       "ed5000PortAdmStatus": ed5000PortAdmStatus,
       "ed5000PortTxWords": ed5000PortTxWords,
       "ed5000PortRxWords": ed5000PortRxWords,
       "ed5000PortTxFrames": ed5000PortTxFrames,
       "ed5000PortRxFrames": ed5000PortRxFrames,
       "ed5000PortRxC2Frames": ed5000PortRxC2Frames,
       "ed5000PortRxC3Frames": ed5000PortRxC3Frames,
       "ed5000PortRxLCs": ed5000PortRxLCs,
       "ed5000PortRxMcasts": ed5000PortRxMcasts,
       "ed5000PortTooManyRdys": ed5000PortTooManyRdys,
       "ed5000PortNoTxCredits": ed5000PortNoTxCredits,
       "ed5000PortRxEncFrs": ed5000PortRxEncFrs,
       "ed5000PortRxCrcs": ed5000PortRxCrcs,
       "ed5000PortRxTruncs": ed5000PortRxTruncs,
       "ed5000PortRxTooLongs": ed5000PortRxTooLongs,
       "ed5000PortRxBadEofs": ed5000PortRxBadEofs,
       "ed5000PortRxBadOs": ed5000PortRxBadOs,
       "ed5000PortC3Discards": ed5000PortC3Discards,
       "ed5000PortMcastTimedOuts": ed5000PortMcastTimedOuts,
       "ed5000PortTxMcasts": ed5000PortTxMcasts,
       "ed5000PortTxThroughput": ed5000PortTxThroughput,
       "ed5000PortRxThroughput": ed5000PortRxThroughput}
)
