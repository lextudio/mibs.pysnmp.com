# SNMP MIB module (MDM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/MDM-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:20:44 2024
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
 experimental,
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
    "experimental",
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

_Usr_ObjectIdentity = ObjectIdentity
usr = _Usr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 429)
)
_Nas_ObjectIdentity = ObjectIdentity
nas = _Nas_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 429, 1)
)
_Mdm_ObjectIdentity = ObjectIdentity
mdm = _Mdm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 429, 1, 6)
)
_MdmID_ObjectIdentity = ObjectIdentity
mdmID = _MdmID_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 429, 1, 6, 1)
)
_MdmIDTable_Object = MibTable
mdmIDTable = _MdmIDTable_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 6, 1, 1)
)
if mibBuilder.loadTexts:
    mdmIDTable.setStatus("mandatory")
_MdmIDEntry_Object = MibTableRow
mdmIDEntry = _MdmIDEntry_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 6, 1, 1, 1)
)
mdmIDEntry.setIndexNames(
    (0, "MDM-MIB", "mdmIDIndex"),
)
if mibBuilder.loadTexts:
    mdmIDEntry.setStatus("mandatory")
_MdmIDIndex_Type = Integer32
_MdmIDIndex_Object = MibTableColumn
mdmIDIndex = _MdmIDIndex_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 6, 1, 1, 1, 1),
    _MdmIDIndex_Type()
)
mdmIDIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mdmIDIndex.setStatus("mandatory")


class _MdmIDModel_Type(Integer32):
    """Custom type mdmIDModel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              11,
              12,
              13,
              14,
              15,
              16,
              30,
              31,
              32,
              33,
              39)
        )
    )
    namedValues = NamedValues(
        *(("cdma", 39),
          ("hdm24Channel", 32),
          ("hdm30Channel", 33),
          ("hst", 3),
          ("unknown", 1),
          ("v32bis", 4),
          ("v32bisDualStandard", 2),
          ("v32terbo", 12),
          ("v32terboDualStandard", 11),
          ("v32terboFax", 13),
          ("v34", 15),
          ("v34DualStandard", 14),
          ("v34Fax", 16),
          ("v34FaxISDN", 30),
          ("x2", 31))
    )


_MdmIDModel_Type.__name__ = "Integer32"
_MdmIDModel_Object = MibTableColumn
mdmIDModel = _MdmIDModel_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 6, 1, 1, 1, 2),
    _MdmIDModel_Type()
)
mdmIDModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mdmIDModel.setStatus("mandatory")


class _MdmIDCountry_Type(Integer32):
    """Custom type mdmIDCountry based on Integer32"""
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
              24)
        )
    )
    namedValues = NamedValues(
        *(("australia", 16),
          ("austria", 20),
          ("belgium", 14),
          ("ccitt", 19),
          ("czech", 13),
          ("denmark", 15),
          ("finland", 4),
          ("france", 17),
          ("germany", 18),
          ("ireland", 21),
          ("italy", 11),
          ("japan", 3),
          ("malaysia", 24),
          ("netherlands", 9),
          ("newZealand", 12),
          ("northamerica", 2),
          ("norway", 7),
          ("portugal", 23),
          ("southAfrica", 10),
          ("spain", 22),
          ("sweden", 5),
          ("switzerland", 8),
          ("uk", 6),
          ("unknown", 1))
    )


_MdmIDCountry_Type.__name__ = "Integer32"
_MdmIDCountry_Object = MibTableColumn
mdmIDCountry = _MdmIDCountry_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 6, 1, 1, 1, 3),
    _MdmIDCountry_Type()
)
mdmIDCountry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mdmIDCountry.setStatus("mandatory")


class _MdmIDHardwareSerNum_Type(DisplayString):
    """Custom type mdmIDHardwareSerNum based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_MdmIDHardwareSerNum_Type.__name__ = "DisplayString"
_MdmIDHardwareSerNum_Object = MibTableColumn
mdmIDHardwareSerNum = _MdmIDHardwareSerNum_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 6, 1, 1, 1, 4),
    _MdmIDHardwareSerNum_Type()
)
mdmIDHardwareSerNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mdmIDHardwareSerNum.setStatus("mandatory")


class _MdmIDHardwareRev_Type(DisplayString):
    """Custom type mdmIDHardwareRev based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 11),
    )


_MdmIDHardwareRev_Type.__name__ = "DisplayString"
_MdmIDHardwareRev_Object = MibTableColumn
mdmIDHardwareRev = _MdmIDHardwareRev_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 6, 1, 1, 1, 5),
    _MdmIDHardwareRev_Type()
)
mdmIDHardwareRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mdmIDHardwareRev.setStatus("mandatory")


class _MdmIDSupervisorSwRev_Type(DisplayString):
    """Custom type mdmIDSupervisorSwRev based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 11),
    )


_MdmIDSupervisorSwRev_Type.__name__ = "DisplayString"
_MdmIDSupervisorSwRev_Object = MibTableColumn
mdmIDSupervisorSwRev = _MdmIDSupervisorSwRev_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 6, 1, 1, 1, 6),
    _MdmIDSupervisorSwRev_Type()
)
mdmIDSupervisorSwRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mdmIDSupervisorSwRev.setStatus("mandatory")


class _MdmIDDataPumpSwRev_Type(DisplayString):
    """Custom type mdmIDDataPumpSwRev based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 11),
    )


_MdmIDDataPumpSwRev_Type.__name__ = "DisplayString"
_MdmIDDataPumpSwRev_Object = MibTableColumn
mdmIDDataPumpSwRev = _MdmIDDataPumpSwRev_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 6, 1, 1, 1, 7),
    _MdmIDDataPumpSwRev_Type()
)
mdmIDDataPumpSwRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mdmIDDataPumpSwRev.setStatus("mandatory")


class _MdmIDIoProcessorSwRev_Type(DisplayString):
    """Custom type mdmIDIoProcessorSwRev based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 11),
    )


_MdmIDIoProcessorSwRev_Type.__name__ = "DisplayString"
_MdmIDIoProcessorSwRev_Object = MibTableColumn
mdmIDIoProcessorSwRev = _MdmIDIoProcessorSwRev_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 6, 1, 1, 1, 8),
    _MdmIDIoProcessorSwRev_Type()
)
mdmIDIoProcessorSwRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mdmIDIoProcessorSwRev.setStatus("mandatory")


class _MdmIDSupervisorDate_Type(DisplayString):
    """Custom type mdmIDSupervisorDate based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_MdmIDSupervisorDate_Type.__name__ = "DisplayString"
_MdmIDSupervisorDate_Object = MibTableColumn
mdmIDSupervisorDate = _MdmIDSupervisorDate_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 6, 1, 1, 1, 9),
    _MdmIDSupervisorDate_Type()
)
mdmIDSupervisorDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mdmIDSupervisorDate.setStatus("mandatory")
_MdmLi_ObjectIdentity = ObjectIdentity
mdmLi = _MdmLi_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 429, 1, 6, 2)
)
_MdmLiTable_Object = MibTable
mdmLiTable = _MdmLiTable_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 6, 2, 1)
)
if mibBuilder.loadTexts:
    mdmLiTable.setStatus("mandatory")
_MdmLiEntry_Object = MibTableRow
mdmLiEntry = _MdmLiEntry_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 6, 2, 1, 1)
)
mdmLiEntry.setIndexNames(
    (0, "MDM-MIB", "mdmLiIndex"),
)
if mibBuilder.loadTexts:
    mdmLiEntry.setStatus("mandatory")
_MdmLiIndex_Type = Integer32
_MdmLiIndex_Object = MibTableColumn
mdmLiIndex = _MdmLiIndex_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 6, 2, 1, 1, 1),
    _MdmLiIndex_Type()
)
mdmLiIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mdmLiIndex.setStatus("mandatory")


class _MdmLiDialPause_Type(Integer32):
    """Custom type mdmLiDialPause based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_MdmLiDialPause_Type.__name__ = "Integer32"
_MdmLiDialPause_Object = MibTableColumn
mdmLiDialPause = _MdmLiDialPause_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 6, 2, 1, 1, 2),
    _MdmLiDialPause_Type()
)
mdmLiDialPause.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mdmLiDialPause.setStatus("mandatory")


class _MdmLiCarrierRecDelay_Type(Integer32):
    """Custom type mdmLiCarrierRecDelay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_MdmLiCarrierRecDelay_Type.__name__ = "Integer32"
_MdmLiCarrierRecDelay_Object = MibTableColumn
mdmLiCarrierRecDelay = _MdmLiCarrierRecDelay_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 6, 2, 1, 1, 3),
    _MdmLiCarrierRecDelay_Type()
)
mdmLiCarrierRecDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mdmLiCarrierRecDelay.setStatus("mandatory")


class _MdmLiCarrierLoss_Type(Integer32):
    """Custom type mdmLiCarrierLoss based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_MdmLiCarrierLoss_Type.__name__ = "Integer32"
_MdmLiCarrierLoss_Object = MibTableColumn
mdmLiCarrierLoss = _MdmLiCarrierLoss_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 6, 2, 1, 1, 4),
    _MdmLiCarrierLoss_Type()
)
mdmLiCarrierLoss.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mdmLiCarrierLoss.setStatus("mandatory")


class _MdmLiToneDialTiming_Type(Integer32):
    """Custom type mdmLiToneDialTiming based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_MdmLiToneDialTiming_Type.__name__ = "Integer32"
_MdmLiToneDialTiming_Object = MibTableColumn
mdmLiToneDialTiming = _MdmLiToneDialTiming_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 6, 2, 1, 1, 5),
    _MdmLiToneDialTiming_Type()
)
mdmLiToneDialTiming.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mdmLiToneDialTiming.setStatus("mandatory")


class _MdmLiDteRxDataDelay_Type(Integer32):
    """Custom type mdmLiDteRxDataDelay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_MdmLiDteRxDataDelay_Type.__name__ = "Integer32"
_MdmLiDteRxDataDelay_Object = MibTableColumn
mdmLiDteRxDataDelay = _MdmLiDteRxDataDelay_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 6, 2, 1, 1, 6),
    _MdmLiDteRxDataDelay_Type()
)
mdmLiDteRxDataDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mdmLiDteRxDataDelay.setStatus("mandatory")


class _MdmLiTransmiter_Type(Integer32):
    """Custom type mdmLiTransmiter based on Integer32"""
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


_MdmLiTransmiter_Type.__name__ = "Integer32"
_MdmLiTransmiter_Object = MibTableColumn
mdmLiTransmiter = _MdmLiTransmiter_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 6, 2, 1, 1, 7),
    _MdmLiTransmiter_Type()
)
mdmLiTransmiter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mdmLiTransmiter.setStatus("mandatory")


class _MdmLiDialMode_Type(Integer32):
    """Custom type mdmLiDialMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("pulse", 1),
          ("tone", 2))
    )


_MdmLiDialMode_Type.__name__ = "Integer32"
_MdmLiDialMode_Object = MibTableColumn
mdmLiDialMode = _MdmLiDialMode_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 6, 2, 1, 1, 8),
    _MdmLiDialMode_Type()
)
mdmLiDialMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mdmLiDialMode.setStatus("mandatory")


class _MdmLiGuardTone_Type(Integer32):
    """Custom type mdmLiGuardTone based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("european550", 2),
          ("none", 1),
          ("uk1800", 3))
    )


_MdmLiGuardTone_Type.__name__ = "Integer32"
_MdmLiGuardTone_Object = MibTableColumn
mdmLiGuardTone = _MdmLiGuardTone_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 6, 2, 1, 1, 9),
    _MdmLiGuardTone_Type()
)
mdmLiGuardTone.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mdmLiGuardTone.setStatus("mandatory")


class _MdmLiLeasedLine_Type(Integer32):
    """Custom type mdmLiLeasedLine based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("cellularHSTMode", 3),
          ("disable", 1),
          ("enable", 2))
    )


_MdmLiLeasedLine_Type.__name__ = "Integer32"
_MdmLiLeasedLine_Object = MibTableColumn
mdmLiLeasedLine = _MdmLiLeasedLine_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 6, 2, 1, 1, 10),
    _MdmLiLeasedLine_Type()
)
mdmLiLeasedLine.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mdmLiLeasedLine.setStatus("mandatory")


class _MdmLiLeasedLineRestDelay_Type(Integer32):
    """Custom type mdmLiLeasedLineRestDelay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_MdmLiLeasedLineRestDelay_Type.__name__ = "Integer32"
_MdmLiLeasedLineRestDelay_Object = MibTableColumn
mdmLiLeasedLineRestDelay = _MdmLiLeasedLineRestDelay_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 6, 2, 1, 1, 11),
    _MdmLiLeasedLineRestDelay_Type()
)
mdmLiLeasedLineRestDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mdmLiLeasedLineRestDelay.setStatus("mandatory")


class _MdmLiPulseMakeBreak_Type(Integer32):
    """Custom type mdmLiPulseMakeBreak based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("britishCommonwealth", 2),
          ("northAmerica", 1))
    )


_MdmLiPulseMakeBreak_Type.__name__ = "Integer32"
_MdmLiPulseMakeBreak_Object = MibTableColumn
mdmLiPulseMakeBreak = _MdmLiPulseMakeBreak_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 6, 2, 1, 1, 12),
    _MdmLiPulseMakeBreak_Type()
)
mdmLiPulseMakeBreak.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mdmLiPulseMakeBreak.setStatus("mandatory")


class _MdmLiAnswerTone_Type(Integer32):
    """Custom type mdmLiAnswerTone based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_MdmLiAnswerTone_Type.__name__ = "Integer32"
_MdmLiAnswerTone_Object = MibTableColumn
mdmLiAnswerTone = _MdmLiAnswerTone_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 6, 2, 1, 1, 13),
    _MdmLiAnswerTone_Type()
)
mdmLiAnswerTone.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mdmLiAnswerTone.setStatus("mandatory")


class _MdmLiRemoteEscGuardTime_Type(Integer32):
    """Custom type mdmLiRemoteEscGuardTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_MdmLiRemoteEscGuardTime_Type.__name__ = "Integer32"
_MdmLiRemoteEscGuardTime_Object = MibTableColumn
mdmLiRemoteEscGuardTime = _MdmLiRemoteEscGuardTime_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 6, 2, 1, 1, 14),
    _MdmLiRemoteEscGuardTime_Type()
)
mdmLiRemoteEscGuardTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mdmLiRemoteEscGuardTime.setStatus("mandatory")


class _MdmLiRemoteEscChar_Type(Integer32):
    """Custom type mdmLiRemoteEscChar based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_MdmLiRemoteEscChar_Type.__name__ = "Integer32"
_MdmLiRemoteEscChar_Object = MibTableColumn
mdmLiRemoteEscChar = _MdmLiRemoteEscChar_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 6, 2, 1, 1, 15),
    _MdmLiRemoteEscChar_Type()
)
mdmLiRemoteEscChar.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mdmLiRemoteEscChar.setStatus("mandatory")


class _MdmLiRemAccessLimit_Type(Integer32):
    """Custom type mdmLiRemAccessLimit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_MdmLiRemAccessLimit_Type.__name__ = "Integer32"
_MdmLiRemAccessLimit_Object = MibTableColumn
mdmLiRemAccessLimit = _MdmLiRemAccessLimit_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 6, 2, 1, 1, 16),
    _MdmLiRemAccessLimit_Type()
)
mdmLiRemAccessLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mdmLiRemAccessLimit.setStatus("mandatory")


class _MdmLiRemPassword0_Type(DisplayString):
    """Custom type mdmLiRemPassword0 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_MdmLiRemPassword0_Type.__name__ = "DisplayString"
_MdmLiRemPassword0_Object = MibTableColumn
mdmLiRemPassword0 = _MdmLiRemPassword0_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 6, 2, 1, 1, 17),
    _MdmLiRemPassword0_Type()
)
mdmLiRemPassword0.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mdmLiRemPassword0.setStatus("mandatory")


class _MdmLiRemPassword1_Type(DisplayString):
    """Custom type mdmLiRemPassword1 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_MdmLiRemPassword1_Type.__name__ = "DisplayString"
_MdmLiRemPassword1_Object = MibTableColumn
mdmLiRemPassword1 = _MdmLiRemPassword1_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 6, 2, 1, 1, 18),
    _MdmLiRemPassword1_Type()
)
mdmLiRemPassword1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mdmLiRemPassword1.setStatus("mandatory")


class _MdmLiTransmitLevel_Type(Integer32):
    """Custom type mdmLiTransmitLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 20),
    )


_MdmLiTransmitLevel_Type.__name__ = "Integer32"
_MdmLiTransmitLevel_Object = MibTableColumn
mdmLiTransmitLevel = _MdmLiTransmitLevel_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 6, 2, 1, 1, 19),
    _MdmLiTransmitLevel_Type()
)
mdmLiTransmitLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mdmLiTransmitLevel.setStatus("mandatory")


class _MdmLiSrc_Type(Integer32):
    """Custom type mdmLiSrc based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("nic", 1),
          ("priTdm", 3),
          ("t1Tdm", 2))
    )


_MdmLiSrc_Type.__name__ = "Integer32"
_MdmLiSrc_Object = MibTableColumn
mdmLiSrc = _MdmLiSrc_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 6, 2, 1, 1, 20),
    _MdmLiSrc_Type()
)
mdmLiSrc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mdmLiSrc.setStatus("optional")
_MdmDc_ObjectIdentity = ObjectIdentity
mdmDc = _MdmDc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 429, 1, 6, 3)
)
_MdmDcTable_Object = MibTable
mdmDcTable = _MdmDcTable_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 6, 3, 1)
)
if mibBuilder.loadTexts:
    mdmDcTable.setStatus("mandatory")
_MdmDcEntry_Object = MibTableRow
mdmDcEntry = _MdmDcEntry_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 6, 3, 1, 1)
)
mdmDcEntry.setIndexNames(
    (0, "MDM-MIB", "mdmDcIndex"),
)
if mibBuilder.loadTexts:
    mdmDcEntry.setStatus("mandatory")
_MdmDcIndex_Type = Integer32
_MdmDcIndex_Object = MibTableColumn
mdmDcIndex = _MdmDcIndex_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 6, 3, 1, 1, 1),
    _MdmDcIndex_Type()
)
mdmDcIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mdmDcIndex.setStatus("mandatory")


class _MdmDcDataCompression_Type(Integer32):
    """Custom type mdmDcDataCompression based on Integer32"""
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
        *(("autoEnable", 2),
          ("enable", 3),
          ("mnpWoCompression", 4),
          ("none", 1))
    )


_MdmDcDataCompression_Type.__name__ = "Integer32"
_MdmDcDataCompression_Object = MibTableColumn
mdmDcDataCompression = _MdmDcDataCompression_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 6, 3, 1, 1, 2),
    _MdmDcDataCompression_Type()
)
mdmDcDataCompression.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mdmDcDataCompression.setStatus("mandatory")
_MdmTf_ObjectIdentity = ObjectIdentity
mdmTf = _MdmTf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 429, 1, 6, 4)
)
_MdmTfTable_Object = MibTable
mdmTfTable = _MdmTfTable_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 6, 4, 1)
)
if mibBuilder.loadTexts:
    mdmTfTable.setStatus("mandatory")
_MdmTfEntry_Object = MibTableRow
mdmTfEntry = _MdmTfEntry_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 6, 4, 1, 1)
)
mdmTfEntry.setIndexNames(
    (0, "MDM-MIB", "mdmTfIndex"),
)
if mibBuilder.loadTexts:
    mdmTfEntry.setStatus("mandatory")
_MdmTfIndex_Type = Integer32
_MdmTfIndex_Object = MibTableColumn
mdmTfIndex = _MdmTfIndex_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 6, 4, 1, 1, 1),
    _MdmTfIndex_Type()
)
mdmTfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mdmTfIndex.setStatus("mandatory")


class _MdmTfTest_Type(Integer32):
    """Custom type mdmTfTest based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_MdmTfTest_Type.__name__ = "Integer32"
_MdmTfTest_Object = MibTableColumn
mdmTfTest = _MdmTfTest_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 6, 4, 1, 1, 2),
    _MdmTfTest_Type()
)
mdmTfTest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mdmTfTest.setStatus("mandatory")


class _MdmTfTestTime_Type(Integer32):
    """Custom type mdmTfTestTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_MdmTfTestTime_Type.__name__ = "Integer32"
_MdmTfTestTime_Object = MibTableColumn
mdmTfTestTime = _MdmTfTestTime_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 6, 4, 1, 1, 3),
    _MdmTfTestTime_Type()
)
mdmTfTestTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mdmTfTestTime.setStatus("mandatory")


class _MdmTfV54_Type(Integer32):
    """Custom type mdmTfV54 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_MdmTfV54_Type.__name__ = "Integer32"
_MdmTfV54_Object = MibTableColumn
mdmTfV54 = _MdmTfV54_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 6, 4, 1, 1, 4),
    _MdmTfV54_Type()
)
mdmTfV54.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mdmTfV54.setStatus("mandatory")
_MdmTfV54Errors_Type = Integer32
_MdmTfV54Errors_Object = MibTableColumn
mdmTfV54Errors = _MdmTfV54Errors_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 6, 4, 1, 1, 5),
    _MdmTfV54Errors_Type()
)
mdmTfV54Errors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mdmTfV54Errors.setStatus("mandatory")


class _MdmTfATG_Type(OctetString):
    """Custom type mdmTfATG based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_MdmTfATG_Type.__name__ = "OctetString"
_MdmTfATG_Object = MibTableColumn
mdmTfATG = _MdmTfATG_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 6, 4, 1, 1, 6),
    _MdmTfATG_Type()
)
mdmTfATG.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mdmTfATG.setStatus("mandatory")


class _MdmTfDialInToneTest_Type(Integer32):
    """Custom type mdmTfDialInToneTest based on Integer32"""
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


_MdmTfDialInToneTest_Type.__name__ = "Integer32"
_MdmTfDialInToneTest_Object = MibTableColumn
mdmTfDialInToneTest = _MdmTfDialInToneTest_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 6, 4, 1, 1, 7),
    _MdmTfDialInToneTest_Type()
)
mdmTfDialInToneTest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mdmTfDialInToneTest.setStatus("mandatory")


class _MdmTfToneTestCallRef_Type(OctetString):
    """Custom type mdmTfToneTestCallRef based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 53),
    )


_MdmTfToneTestCallRef_Type.__name__ = "OctetString"
_MdmTfToneTestCallRef_Object = MibTableColumn
mdmTfToneTestCallRef = _MdmTfToneTestCallRef_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 6, 4, 1, 1, 8),
    _MdmTfToneTestCallRef_Type()
)
mdmTfToneTestCallRef.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mdmTfToneTestCallRef.setStatus("mandatory")
_MdmTfToneTable_Object = MibTable
mdmTfToneTable = _MdmTfToneTable_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 6, 4, 2)
)
if mibBuilder.loadTexts:
    mdmTfToneTable.setStatus("optional")
_MdmTfToneEntry_Object = MibTableRow
mdmTfToneEntry = _MdmTfToneEntry_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 6, 4, 2, 1)
)
mdmTfToneEntry.setIndexNames(
    (0, "MDM-MIB", "mdmTfToneIndex"),
)
if mibBuilder.loadTexts:
    mdmTfToneEntry.setStatus("optional")
_MdmTfToneIndex_Type = Integer32
_MdmTfToneIndex_Object = MibTableColumn
mdmTfToneIndex = _MdmTfToneIndex_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 6, 4, 2, 1, 1),
    _MdmTfToneIndex_Type()
)
mdmTfToneIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mdmTfToneIndex.setStatus("optional")


class _MdmTfTxFreq_Type(Integer32):
    """Custom type mdmTfTxFreq based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(300, 4000),
    )


_MdmTfTxFreq_Type.__name__ = "Integer32"
_MdmTfTxFreq_Object = MibTableColumn
mdmTfTxFreq = _MdmTfTxFreq_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 6, 4, 2, 1, 2),
    _MdmTfTxFreq_Type()
)
mdmTfTxFreq.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mdmTfTxFreq.setStatus("optional")


class _MdmTfTxAmpl_Type(Integer32):
    """Custom type mdmTfTxAmpl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-40, 0),
    )


_MdmTfTxAmpl_Type.__name__ = "Integer32"
_MdmTfTxAmpl_Object = MibTableColumn
mdmTfTxAmpl = _MdmTfTxAmpl_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 6, 4, 2, 1, 3),
    _MdmTfTxAmpl_Type()
)
mdmTfTxAmpl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mdmTfTxAmpl.setStatus("optional")


class _MdmTfRxFreq_Type(Integer32):
    """Custom type mdmTfRxFreq based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5000),
    )


_MdmTfRxFreq_Type.__name__ = "Integer32"
_MdmTfRxFreq_Object = MibTableColumn
mdmTfRxFreq = _MdmTfRxFreq_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 6, 4, 2, 1, 4),
    _MdmTfRxFreq_Type()
)
mdmTfRxFreq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mdmTfRxFreq.setStatus("optional")
_MdmTfRxAmpl_Type = Integer32
_MdmTfRxAmpl_Object = MibTableColumn
mdmTfRxAmpl = _MdmTfRxAmpl_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 6, 4, 2, 1, 5),
    _MdmTfRxAmpl_Type()
)
mdmTfRxAmpl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mdmTfRxAmpl.setStatus("optional")
_MdmTfRspndrTable_Object = MibTable
mdmTfRspndrTable = _MdmTfRspndrTable_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 6, 4, 3)
)
if mibBuilder.loadTexts:
    mdmTfRspndrTable.setStatus("optional")
_MdmTfRspndrEntry_Object = MibTableRow
mdmTfRspndrEntry = _MdmTfRspndrEntry_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 6, 4, 3, 1)
)
mdmTfRspndrEntry.setIndexNames(
    (0, "MDM-MIB", "mdmTfRspndrIndex"),
)
if mibBuilder.loadTexts:
    mdmTfRspndrEntry.setStatus("optional")
_MdmTfRspndrIndex_Type = Integer32
_MdmTfRspndrIndex_Object = MibTableColumn
mdmTfRspndrIndex = _MdmTfRspndrIndex_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 6, 4, 3, 1, 1),
    _MdmTfRspndrIndex_Type()
)
mdmTfRspndrIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mdmTfRspndrIndex.setStatus("optional")
_MdmTf404FarNearLvl_Type = Integer32
_MdmTf404FarNearLvl_Object = MibTableColumn
mdmTf404FarNearLvl = _MdmTf404FarNearLvl_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 6, 4, 3, 1, 2),
    _MdmTf404FarNearLvl_Type()
)
mdmTf404FarNearLvl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mdmTf404FarNearLvl.setStatus("optional")
_MdmTf404NearFarLvl_Type = Integer32
_MdmTf404NearFarLvl_Object = MibTableColumn
mdmTf404NearFarLvl = _MdmTf404NearFarLvl_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 6, 4, 3, 1, 3),
    _MdmTf404NearFarLvl_Type()
)
mdmTf404NearFarLvl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mdmTf404NearFarLvl.setStatus("optional")
_MdmTf1004FarNearLvl_Type = Integer32
_MdmTf1004FarNearLvl_Object = MibTableColumn
mdmTf1004FarNearLvl = _MdmTf1004FarNearLvl_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 6, 4, 3, 1, 4),
    _MdmTf1004FarNearLvl_Type()
)
mdmTf1004FarNearLvl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mdmTf1004FarNearLvl.setStatus("optional")
_MdmTf1004NearFarLvl_Type = Integer32
_MdmTf1004NearFarLvl_Object = MibTableColumn
mdmTf1004NearFarLvl = _MdmTf1004NearFarLvl_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 6, 4, 3, 1, 5),
    _MdmTf1004NearFarLvl_Type()
)
mdmTf1004NearFarLvl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mdmTf1004NearFarLvl.setStatus("optional")
_MdmTf2804FarNearLvl_Type = Integer32
_MdmTf2804FarNearLvl_Object = MibTableColumn
mdmTf2804FarNearLvl = _MdmTf2804FarNearLvl_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 6, 4, 3, 1, 6),
    _MdmTf2804FarNearLvl_Type()
)
mdmTf2804FarNearLvl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mdmTf2804FarNearLvl.setStatus("optional")
_MdmTf2804NearFarLvl_Type = Integer32
_MdmTf2804NearFarLvl_Object = MibTableColumn
mdmTf2804NearFarLvl = _MdmTf2804NearFarLvl_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 6, 4, 3, 1, 7),
    _MdmTf2804NearFarLvl_Type()
)
mdmTf2804NearFarLvl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mdmTf2804NearFarLvl.setStatus("optional")
_MdmTfCmsgFarNearLvl_Type = Integer32
_MdmTfCmsgFarNearLvl_Object = MibTableColumn
mdmTfCmsgFarNearLvl = _MdmTfCmsgFarNearLvl_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 6, 4, 3, 1, 8),
    _MdmTfCmsgFarNearLvl_Type()
)
mdmTfCmsgFarNearLvl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mdmTfCmsgFarNearLvl.setStatus("optional")
_MdmTfCmsgNearFarLvl_Type = Integer32
_MdmTfCmsgNearFarLvl_Object = MibTableColumn
mdmTfCmsgNearFarLvl = _MdmTfCmsgNearFarLvl_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 6, 4, 3, 1, 9),
    _MdmTfCmsgNearFarLvl_Type()
)
mdmTfCmsgNearFarLvl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mdmTfCmsgNearFarLvl.setStatus("optional")
_MdmTfCnotchFarNearLvl_Type = Integer32
_MdmTfCnotchFarNearLvl_Object = MibTableColumn
mdmTfCnotchFarNearLvl = _MdmTfCnotchFarNearLvl_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 6, 4, 3, 1, 10),
    _MdmTfCnotchFarNearLvl_Type()
)
mdmTfCnotchFarNearLvl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mdmTfCnotchFarNearLvl.setStatus("optional")
_MdmTfCnotchNearFarLvl_Type = Integer32
_MdmTfCnotchNearFarLvl_Object = MibTableColumn
mdmTfCnotchNearFarLvl = _MdmTfCnotchNearFarLvl_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 6, 4, 3, 1, 11),
    _MdmTfCnotchNearFarLvl_Type()
)
mdmTfCnotchNearFarLvl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mdmTfCnotchNearFarLvl.setStatus("optional")
_MdmtTfSigNoiseFarNearLvl_Type = Integer32
_MdmtTfSigNoiseFarNearLvl_Object = MibTableColumn
mdmtTfSigNoiseFarNearLvl = _MdmtTfSigNoiseFarNearLvl_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 6, 4, 3, 1, 12),
    _MdmtTfSigNoiseFarNearLvl_Type()
)
mdmtTfSigNoiseFarNearLvl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mdmtTfSigNoiseFarNearLvl.setStatus("optional")
_MdmtTfSigNoiseNearFarLvl_Type = Integer32
_MdmtTfSigNoiseNearFarLvl_Object = MibTableColumn
mdmtTfSigNoiseNearFarLvl = _MdmtTfSigNoiseNearFarLvl_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 6, 4, 3, 1, 13),
    _MdmtTfSigNoiseNearFarLvl_Type()
)
mdmtTfSigNoiseNearFarLvl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mdmtTfSigNoiseNearFarLvl.setStatus("optional")


class _MdmTf404FarNearSts_Type(Integer32):
    """Custom type mdmTf404FarNearSts based on Integer32"""
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
        *(("noResponder", 3),
          ("noTest", 1),
          ("noToneDetected", 6),
          ("success", 2),
          ("timeOut", 5),
          ("unsupported", 4))
    )


_MdmTf404FarNearSts_Type.__name__ = "Integer32"
_MdmTf404FarNearSts_Object = MibTableColumn
mdmTf404FarNearSts = _MdmTf404FarNearSts_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 6, 4, 3, 1, 14),
    _MdmTf404FarNearSts_Type()
)
mdmTf404FarNearSts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mdmTf404FarNearSts.setStatus("optional")


class _MdmTf404NearFarSts_Type(Integer32):
    """Custom type mdmTf404NearFarSts based on Integer32"""
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
        *(("noResponder", 3),
          ("noTest", 1),
          ("noToneDetected", 6),
          ("success", 2),
          ("timeOut", 5),
          ("unsupported", 4))
    )


_MdmTf404NearFarSts_Type.__name__ = "Integer32"
_MdmTf404NearFarSts_Object = MibTableColumn
mdmTf404NearFarSts = _MdmTf404NearFarSts_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 6, 4, 3, 1, 15),
    _MdmTf404NearFarSts_Type()
)
mdmTf404NearFarSts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mdmTf404NearFarSts.setStatus("optional")


class _MdmTf1004FarNearSts_Type(Integer32):
    """Custom type mdmTf1004FarNearSts based on Integer32"""
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
        *(("noResponder", 3),
          ("noTest", 1),
          ("noToneDetected", 6),
          ("success", 2),
          ("timeOut", 5),
          ("unsupported", 4))
    )


_MdmTf1004FarNearSts_Type.__name__ = "Integer32"
_MdmTf1004FarNearSts_Object = MibTableColumn
mdmTf1004FarNearSts = _MdmTf1004FarNearSts_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 6, 4, 3, 1, 16),
    _MdmTf1004FarNearSts_Type()
)
mdmTf1004FarNearSts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mdmTf1004FarNearSts.setStatus("optional")


class _MdmTf1004NearFarSts_Type(Integer32):
    """Custom type mdmTf1004NearFarSts based on Integer32"""
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
        *(("noResponder", 3),
          ("noTest", 1),
          ("noToneDetected", 6),
          ("success", 2),
          ("timeOut", 5),
          ("unsupported", 4))
    )


_MdmTf1004NearFarSts_Type.__name__ = "Integer32"
_MdmTf1004NearFarSts_Object = MibTableColumn
mdmTf1004NearFarSts = _MdmTf1004NearFarSts_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 6, 4, 3, 1, 17),
    _MdmTf1004NearFarSts_Type()
)
mdmTf1004NearFarSts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mdmTf1004NearFarSts.setStatus("optional")


class _MdmTf2804FarNearSts_Type(Integer32):
    """Custom type mdmTf2804FarNearSts based on Integer32"""
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
        *(("noResponder", 3),
          ("noTest", 1),
          ("noToneDetected", 6),
          ("success", 2),
          ("timeOut", 5),
          ("unsupported", 4))
    )


_MdmTf2804FarNearSts_Type.__name__ = "Integer32"
_MdmTf2804FarNearSts_Object = MibTableColumn
mdmTf2804FarNearSts = _MdmTf2804FarNearSts_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 6, 4, 3, 1, 18),
    _MdmTf2804FarNearSts_Type()
)
mdmTf2804FarNearSts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mdmTf2804FarNearSts.setStatus("optional")


class _MdmTf2804NearFarSts_Type(Integer32):
    """Custom type mdmTf2804NearFarSts based on Integer32"""
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
        *(("noResponder", 3),
          ("noTest", 1),
          ("noToneDetected", 6),
          ("success", 2),
          ("timeOut", 5),
          ("unsupported", 4))
    )


_MdmTf2804NearFarSts_Type.__name__ = "Integer32"
_MdmTf2804NearFarSts_Object = MibTableColumn
mdmTf2804NearFarSts = _MdmTf2804NearFarSts_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 6, 4, 3, 1, 19),
    _MdmTf2804NearFarSts_Type()
)
mdmTf2804NearFarSts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mdmTf2804NearFarSts.setStatus("optional")


class _MdmTfCmsgFarNearSts_Type(Integer32):
    """Custom type mdmTfCmsgFarNearSts based on Integer32"""
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
        *(("noResponder", 3),
          ("noTest", 1),
          ("noToneDetected", 6),
          ("success", 2),
          ("timeOut", 5),
          ("unsupported", 4))
    )


_MdmTfCmsgFarNearSts_Type.__name__ = "Integer32"
_MdmTfCmsgFarNearSts_Object = MibTableColumn
mdmTfCmsgFarNearSts = _MdmTfCmsgFarNearSts_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 6, 4, 3, 1, 20),
    _MdmTfCmsgFarNearSts_Type()
)
mdmTfCmsgFarNearSts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mdmTfCmsgFarNearSts.setStatus("optional")


class _MdmTfCmsgNearFarSts_Type(Integer32):
    """Custom type mdmTfCmsgNearFarSts based on Integer32"""
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
        *(("noResponder", 3),
          ("noTest", 1),
          ("noToneDetected", 6),
          ("success", 2),
          ("timeOut", 5),
          ("unsupported", 4))
    )


_MdmTfCmsgNearFarSts_Type.__name__ = "Integer32"
_MdmTfCmsgNearFarSts_Object = MibTableColumn
mdmTfCmsgNearFarSts = _MdmTfCmsgNearFarSts_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 6, 4, 3, 1, 21),
    _MdmTfCmsgNearFarSts_Type()
)
mdmTfCmsgNearFarSts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mdmTfCmsgNearFarSts.setStatus("optional")


class _MdmTfCnotchFarNearSts_Type(Integer32):
    """Custom type mdmTfCnotchFarNearSts based on Integer32"""
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
        *(("noResponder", 3),
          ("noTest", 1),
          ("noToneDetected", 6),
          ("success", 2),
          ("timeOut", 5),
          ("unsupported", 4))
    )


_MdmTfCnotchFarNearSts_Type.__name__ = "Integer32"
_MdmTfCnotchFarNearSts_Object = MibTableColumn
mdmTfCnotchFarNearSts = _MdmTfCnotchFarNearSts_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 6, 4, 3, 1, 22),
    _MdmTfCnotchFarNearSts_Type()
)
mdmTfCnotchFarNearSts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mdmTfCnotchFarNearSts.setStatus("optional")


class _MdmTfCnotchNearFarSts_Type(Integer32):
    """Custom type mdmTfCnotchNearFarSts based on Integer32"""
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
        *(("noResponder", 3),
          ("noTest", 1),
          ("noToneDetected", 6),
          ("success", 2),
          ("timeOut", 5),
          ("unsupported", 4))
    )


_MdmTfCnotchNearFarSts_Type.__name__ = "Integer32"
_MdmTfCnotchNearFarSts_Object = MibTableColumn
mdmTfCnotchNearFarSts = _MdmTfCnotchNearFarSts_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 6, 4, 3, 1, 23),
    _MdmTfCnotchNearFarSts_Type()
)
mdmTfCnotchNearFarSts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mdmTfCnotchNearFarSts.setStatus("optional")


class _MdmTfSigNoiseFarNearSts_Type(Integer32):
    """Custom type mdmTfSigNoiseFarNearSts based on Integer32"""
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
        *(("noResponder", 3),
          ("noTest", 1),
          ("noToneDetected", 6),
          ("success", 2),
          ("timeOut", 5),
          ("unsupported", 4))
    )


_MdmTfSigNoiseFarNearSts_Type.__name__ = "Integer32"
_MdmTfSigNoiseFarNearSts_Object = MibTableColumn
mdmTfSigNoiseFarNearSts = _MdmTfSigNoiseFarNearSts_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 6, 4, 3, 1, 24),
    _MdmTfSigNoiseFarNearSts_Type()
)
mdmTfSigNoiseFarNearSts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mdmTfSigNoiseFarNearSts.setStatus("optional")


class _MdmTfSigNoiseNearFarSts_Type(Integer32):
    """Custom type mdmTfSigNoiseNearFarSts based on Integer32"""
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
        *(("noResponder", 3),
          ("noTest", 1),
          ("noToneDetected", 6),
          ("success", 2),
          ("timeOut", 5),
          ("unsupported", 4))
    )


_MdmTfSigNoiseNearFarSts_Type.__name__ = "Integer32"
_MdmTfSigNoiseNearFarSts_Object = MibTableColumn
mdmTfSigNoiseNearFarSts = _MdmTfSigNoiseNearFarSts_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 6, 4, 3, 1, 25),
    _MdmTfSigNoiseNearFarSts_Type()
)
mdmTfSigNoiseNearFarSts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mdmTfSigNoiseNearFarSts.setStatus("optional")
_MdmTf0dB1004FarNearLvl_Type = Integer32
_MdmTf0dB1004FarNearLvl_Object = MibTableColumn
mdmTf0dB1004FarNearLvl = _MdmTf0dB1004FarNearLvl_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 6, 4, 3, 1, 26),
    _MdmTf0dB1004FarNearLvl_Type()
)
mdmTf0dB1004FarNearLvl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mdmTf0dB1004FarNearLvl.setStatus("optional")
_MdmTf0dB1004NearFarLvl_Type = Integer32
_MdmTf0dB1004NearFarLvl_Object = MibTableColumn
mdmTf0dB1004NearFarLvl = _MdmTf0dB1004NearFarLvl_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 6, 4, 3, 1, 27),
    _MdmTf0dB1004NearFarLvl_Type()
)
mdmTf0dB1004NearFarLvl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mdmTf0dB1004NearFarLvl.setStatus("optional")


class _MdmTf0dB1004FarNearSts_Type(Integer32):
    """Custom type mdmTf0dB1004FarNearSts based on Integer32"""
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
        *(("noResponder", 3),
          ("noTest", 1),
          ("noToneDetected", 6),
          ("success", 2),
          ("timeOut", 5),
          ("unsupported", 4))
    )


_MdmTf0dB1004FarNearSts_Type.__name__ = "Integer32"
_MdmTf0dB1004FarNearSts_Object = MibTableColumn
mdmTf0dB1004FarNearSts = _MdmTf0dB1004FarNearSts_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 6, 4, 3, 1, 28),
    _MdmTf0dB1004FarNearSts_Type()
)
mdmTf0dB1004FarNearSts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mdmTf0dB1004FarNearSts.setStatus("optional")


class _MdmTf0dB1004NearFarSts_Type(Integer32):
    """Custom type mdmTf0dB1004NearFarSts based on Integer32"""
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
        *(("noResponder", 3),
          ("noTest", 1),
          ("noToneDetected", 6),
          ("success", 2),
          ("timeOut", 5),
          ("unsupported", 4))
    )


_MdmTf0dB1004NearFarSts_Type.__name__ = "Integer32"
_MdmTf0dB1004NearFarSts_Object = MibTableColumn
mdmTf0dB1004NearFarSts = _MdmTf0dB1004NearFarSts_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 6, 4, 3, 1, 29),
    _MdmTf0dB1004NearFarSts_Type()
)
mdmTf0dB1004NearFarSts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mdmTf0dB1004NearFarSts.setStatus("optional")
_MdmDi_ObjectIdentity = ObjectIdentity
mdmDi = _MdmDi_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 429, 1, 6, 5)
)
_MdmDiTable_Object = MibTable
mdmDiTable = _MdmDiTable_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 6, 5, 1)
)
if mibBuilder.loadTexts:
    mdmDiTable.setStatus("mandatory")
_MdmDiEntry_Object = MibTableRow
mdmDiEntry = _MdmDiEntry_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 6, 5, 1, 1)
)
mdmDiEntry.setIndexNames(
    (0, "MDM-MIB", "mdmDiIndex"),
)
if mibBuilder.loadTexts:
    mdmDiEntry.setStatus("mandatory")
_MdmDiIndex_Type = Integer32
_MdmDiIndex_Object = MibTableColumn
mdmDiIndex = _MdmDiIndex_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 6, 5, 1, 1, 1),
    _MdmDiIndex_Type()
)
mdmDiIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mdmDiIndex.setStatus("mandatory")


class _MdmDiEscCodeGuardTime_Type(Integer32):
    """Custom type mdmDiEscCodeGuardTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_MdmDiEscCodeGuardTime_Type.__name__ = "Integer32"
_MdmDiEscCodeGuardTime_Object = MibTableColumn
mdmDiEscCodeGuardTime = _MdmDiEscCodeGuardTime_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 6, 5, 1, 1, 2),
    _MdmDiEscCodeGuardTime_Type()
)
mdmDiEscCodeGuardTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mdmDiEscCodeGuardTime.setStatus("mandatory")


class _MdmDiLocalEscChar_Type(Integer32):
    """Custom type mdmDiLocalEscChar based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_MdmDiLocalEscChar_Type.__name__ = "Integer32"
_MdmDiLocalEscChar_Object = MibTableColumn
mdmDiLocalEscChar = _MdmDiLocalEscChar_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 6, 5, 1, 1, 3),
    _MdmDiLocalEscChar_Type()
)
mdmDiLocalEscChar.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mdmDiLocalEscChar.setStatus("mandatory")


class _MdmDiCarriageRetChar_Type(Integer32):
    """Custom type mdmDiCarriageRetChar based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_MdmDiCarriageRetChar_Type.__name__ = "Integer32"
_MdmDiCarriageRetChar_Object = MibTableColumn
mdmDiCarriageRetChar = _MdmDiCarriageRetChar_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 6, 5, 1, 1, 4),
    _MdmDiCarriageRetChar_Type()
)
mdmDiCarriageRetChar.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mdmDiCarriageRetChar.setStatus("mandatory")


class _MdmDiLineFeedChar_Type(Integer32):
    """Custom type mdmDiLineFeedChar based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_MdmDiLineFeedChar_Type.__name__ = "Integer32"
_MdmDiLineFeedChar_Object = MibTableColumn
mdmDiLineFeedChar = _MdmDiLineFeedChar_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 6, 5, 1, 1, 5),
    _MdmDiLineFeedChar_Type()
)
mdmDiLineFeedChar.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mdmDiLineFeedChar.setStatus("mandatory")


class _MdmDiBackspaceChar_Type(Integer32):
    """Custom type mdmDiBackspaceChar based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_MdmDiBackspaceChar_Type.__name__ = "Integer32"
_MdmDiBackspaceChar_Object = MibTableColumn
mdmDiBackspaceChar = _MdmDiBackspaceChar_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 6, 5, 1, 1, 6),
    _MdmDiBackspaceChar_Type()
)
mdmDiBackspaceChar.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mdmDiBackspaceChar.setStatus("mandatory")


class _MdmDiDelAsBackspace_Type(Integer32):
    """Custom type mdmDiDelAsBackspace based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("backspace", 2),
          ("delete", 1))
    )


_MdmDiDelAsBackspace_Type.__name__ = "Integer32"
_MdmDiDelAsBackspace_Object = MibTableColumn
mdmDiDelAsBackspace = _MdmDiDelAsBackspace_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 6, 5, 1, 1, 7),
    _MdmDiDelAsBackspace_Type()
)
mdmDiDelAsBackspace.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mdmDiDelAsBackspace.setStatus("mandatory")


class _MdmDiResetOnDtrEna_Type(Integer32):
    """Custom type mdmDiResetOnDtrEna based on Integer32"""
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


_MdmDiResetOnDtrEna_Type.__name__ = "Integer32"
_MdmDiResetOnDtrEna_Object = MibTableColumn
mdmDiResetOnDtrEna = _MdmDiResetOnDtrEna_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 6, 5, 1, 1, 8),
    _MdmDiResetOnDtrEna_Type()
)
mdmDiResetOnDtrEna.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mdmDiResetOnDtrEna.setStatus("mandatory")


class _MdmDiResultCodePauseDis_Type(Integer32):
    """Custom type mdmDiResultCodePauseDis based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_MdmDiResultCodePauseDis_Type.__name__ = "Integer32"
_MdmDiResultCodePauseDis_Object = MibTableColumn
mdmDiResultCodePauseDis = _MdmDiResultCodePauseDis_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 6, 5, 1, 1, 9),
    _MdmDiResultCodePauseDis_Type()
)
mdmDiResultCodePauseDis.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mdmDiResultCodePauseDis.setStatus("mandatory")


class _MdmDiInterbridgeEna_Type(Integer32):
    """Custom type mdmDiInterbridgeEna based on Integer32"""
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


_MdmDiInterbridgeEna_Type.__name__ = "Integer32"
_MdmDiInterbridgeEna_Object = MibTableColumn
mdmDiInterbridgeEna = _MdmDiInterbridgeEna_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 6, 5, 1, 1, 10),
    _MdmDiInterbridgeEna_Type()
)
mdmDiInterbridgeEna.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mdmDiInterbridgeEna.setStatus("mandatory")


class _MdmDiBreakLen_Type(Integer32):
    """Custom type mdmDiBreakLen based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_MdmDiBreakLen_Type.__name__ = "Integer32"
_MdmDiBreakLen_Object = MibTableColumn
mdmDiBreakLen = _MdmDiBreakLen_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 6, 5, 1, 1, 11),
    _MdmDiBreakLen_Type()
)
mdmDiBreakLen.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mdmDiBreakLen.setStatus("mandatory")


class _MdmDiXonChar_Type(Integer32):
    """Custom type mdmDiXonChar based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_MdmDiXonChar_Type.__name__ = "Integer32"
_MdmDiXonChar_Object = MibTableColumn
mdmDiXonChar = _MdmDiXonChar_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 6, 5, 1, 1, 12),
    _MdmDiXonChar_Type()
)
mdmDiXonChar.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mdmDiXonChar.setStatus("mandatory")


class _MdmDiXoffChar_Type(Integer32):
    """Custom type mdmDiXoffChar based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_MdmDiXoffChar_Type.__name__ = "Integer32"
_MdmDiXoffChar_Object = MibTableColumn
mdmDiXoffChar = _MdmDiXoffChar_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 6, 5, 1, 1, 13),
    _MdmDiXoffChar_Type()
)
mdmDiXoffChar.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mdmDiXoffChar.setStatus("mandatory")


class _MdmDiDsrPulseTime_Type(Integer32):
    """Custom type mdmDiDsrPulseTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 150),
    )


_MdmDiDsrPulseTime_Type.__name__ = "Integer32"
_MdmDiDsrPulseTime_Object = MibTableColumn
mdmDiDsrPulseTime = _MdmDiDsrPulseTime_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 6, 5, 1, 1, 14),
    _MdmDiDsrPulseTime_Type()
)
mdmDiDsrPulseTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mdmDiDsrPulseTime.setStatus("mandatory")


class _MdmDiRtsCtsDelay_Type(Integer32):
    """Custom type mdmDiRtsCtsDelay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_MdmDiRtsCtsDelay_Type.__name__ = "Integer32"
_MdmDiRtsCtsDelay_Object = MibTableColumn
mdmDiRtsCtsDelay = _MdmDiRtsCtsDelay_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 6, 5, 1, 1, 15),
    _MdmDiRtsCtsDelay_Type()
)
mdmDiRtsCtsDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mdmDiRtsCtsDelay.setStatus("mandatory")


class _MdmDiHiSpeedResCodeEna_Type(Integer32):
    """Custom type mdmDiHiSpeedResCodeEna based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_MdmDiHiSpeedResCodeEna_Type.__name__ = "Integer32"
_MdmDiHiSpeedResCodeEna_Object = MibTableColumn
mdmDiHiSpeedResCodeEna = _MdmDiHiSpeedResCodeEna_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 6, 5, 1, 1, 16),
    _MdmDiHiSpeedResCodeEna_Type()
)
mdmDiHiSpeedResCodeEna.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mdmDiHiSpeedResCodeEna.setStatus("mandatory")


class _MdmDiCmdLocalEchoEna_Type(Integer32):
    """Custom type mdmDiCmdLocalEchoEna based on Integer32"""
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


_MdmDiCmdLocalEchoEna_Type.__name__ = "Integer32"
_MdmDiCmdLocalEchoEna_Object = MibTableColumn
mdmDiCmdLocalEchoEna = _MdmDiCmdLocalEchoEna_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 6, 5, 1, 1, 17),
    _MdmDiCmdLocalEchoEna_Type()
)
mdmDiCmdLocalEchoEna.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mdmDiCmdLocalEchoEna.setStatus("mandatory")


class _MdmDiDataModeEchoEna_Type(Integer32):
    """Custom type mdmDiDataModeEchoEna based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_MdmDiDataModeEchoEna_Type.__name__ = "Integer32"
_MdmDiDataModeEchoEna_Object = MibTableColumn
mdmDiDataModeEchoEna = _MdmDiDataModeEchoEna_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 6, 5, 1, 1, 18),
    _MdmDiDataModeEchoEna_Type()
)
mdmDiDataModeEchoEna.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mdmDiDataModeEchoEna.setStatus("mandatory")


class _MdmDiDteDataRateMode_Type(Integer32):
    """Custom type mdmDiDteDataRateMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("arqFixedNonArqFollows", 3),
          ("fixed", 2),
          ("followsLinkRate", 1))
    )


_MdmDiDteDataRateMode_Type.__name__ = "Integer32"
_MdmDiDteDataRateMode_Object = MibTableColumn
mdmDiDteDataRateMode = _MdmDiDteDataRateMode_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 6, 5, 1, 1, 19),
    _MdmDiDteDataRateMode_Type()
)
mdmDiDteDataRateMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mdmDiDteDataRateMode.setStatus("mandatory")


class _MdmDiCdOverride_Type(Integer32):
    """Custom type mdmDiCdOverride based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_MdmDiCdOverride_Type.__name__ = "Integer32"
_MdmDiCdOverride_Object = MibTableColumn
mdmDiCdOverride = _MdmDiCdOverride_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 6, 5, 1, 1, 20),
    _MdmDiCdOverride_Type()
)
mdmDiCdOverride.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mdmDiCdOverride.setStatus("mandatory")


class _MdmDiDtrOverride_Type(Integer32):
    """Custom type mdmDiDtrOverride based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_MdmDiDtrOverride_Type.__name__ = "Integer32"
_MdmDiDtrOverride_Object = MibTableColumn
mdmDiDtrOverride = _MdmDiDtrOverride_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 6, 5, 1, 1, 21),
    _MdmDiDtrOverride_Type()
)
mdmDiDtrOverride.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mdmDiDtrOverride.setStatus("mandatory")


class _MdmDiDsrOverride_Type(Integer32):
    """Custom type mdmDiDsrOverride based on Integer32"""
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
        *(("dsrEqualsCd", 5),
          ("dsrOveridden", 1),
          ("modemControled", 2),
          ("normalCtsFollowsCd", 6),
          ("pulsed", 4),
          ("pulsedCtsFollowsCd", 3))
    )


_MdmDiDsrOverride_Type.__name__ = "Integer32"
_MdmDiDsrOverride_Object = MibTableColumn
mdmDiDsrOverride = _MdmDiDsrOverride_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 6, 5, 1, 1, 22),
    _MdmDiDsrOverride_Type()
)
mdmDiDsrOverride.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mdmDiDsrOverride.setStatus("mandatory")


class _MdmDiEiaLineStatus_Type(Integer32):
    """Custom type mdmDiEiaLineStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_MdmDiEiaLineStatus_Type.__name__ = "Integer32"
_MdmDiEiaLineStatus_Object = MibTableColumn
mdmDiEiaLineStatus = _MdmDiEiaLineStatus_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 6, 5, 1, 1, 23),
    _MdmDiEiaLineStatus_Type()
)
mdmDiEiaLineStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mdmDiEiaLineStatus.setStatus("mandatory")


class _MdmDiTransmitFlowCntl_Type(Integer32):
    """Custom type mdmDiTransmitFlowCntl based on Integer32"""
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
        *(("hardware", 2),
          ("hardwareAndSoftware", 4),
          ("none", 1),
          ("software", 3))
    )


_MdmDiTransmitFlowCntl_Type.__name__ = "Integer32"
_MdmDiTransmitFlowCntl_Object = MibTableColumn
mdmDiTransmitFlowCntl = _MdmDiTransmitFlowCntl_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 6, 5, 1, 1, 24),
    _MdmDiTransmitFlowCntl_Type()
)
mdmDiTransmitFlowCntl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mdmDiTransmitFlowCntl.setStatus("mandatory")


class _MdmDiSoftwareRxFlowCntl_Type(Integer32):
    """Custom type mdmDiSoftwareRxFlowCntl based on Integer32"""
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
        *(("hpHostMode", 4),
          ("hpTerminalMode", 5),
          ("localIncommingXonXoff", 6),
          ("none", 1),
          ("xonXoffLocal", 3),
          ("xonXoffLocalRemote", 2))
    )


_MdmDiSoftwareRxFlowCntl_Type.__name__ = "Integer32"
_MdmDiSoftwareRxFlowCntl_Object = MibTableColumn
mdmDiSoftwareRxFlowCntl = _MdmDiSoftwareRxFlowCntl_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 6, 5, 1, 1, 25),
    _MdmDiSoftwareRxFlowCntl_Type()
)
mdmDiSoftwareRxFlowCntl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mdmDiSoftwareRxFlowCntl.setStatus("mandatory")


class _MdmDiHardwareRxFlowCntl_Type(Integer32):
    """Custom type mdmDiHardwareRxFlowCntl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("dataOnRtsHigh", 3),
          ("rtsCtsDelayed", 1),
          ("rtsIgnored", 2))
    )


_MdmDiHardwareRxFlowCntl_Type.__name__ = "Integer32"
_MdmDiHardwareRxFlowCntl_Object = MibTableColumn
mdmDiHardwareRxFlowCntl = _MdmDiHardwareRxFlowCntl_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 6, 5, 1, 1, 26),
    _MdmDiHardwareRxFlowCntl_Type()
)
mdmDiHardwareRxFlowCntl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mdmDiHardwareRxFlowCntl.setStatus("mandatory")


class _MdmDiBreakHandling_Type(Integer32):
    """Custom type mdmDiBreakHandling based on Integer32"""
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
        *(("destructiveExpedited", 2),
          ("destructiveNotSent", 1),
          ("nondestructiveExpedited", 3),
          ("nondestructiveNotSent", 4))
    )


_MdmDiBreakHandling_Type.__name__ = "Integer32"
_MdmDiBreakHandling_Object = MibTableColumn
mdmDiBreakHandling = _MdmDiBreakHandling_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 6, 5, 1, 1, 27),
    _MdmDiBreakHandling_Type()
)
mdmDiBreakHandling.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mdmDiBreakHandling.setStatus("mandatory")


class _MdmDiDteNvramLock_Type(Integer32):
    """Custom type mdmDiDteNvramLock based on Integer32"""
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


_MdmDiDteNvramLock_Type.__name__ = "Integer32"
_MdmDiDteNvramLock_Object = MibTableColumn
mdmDiDteNvramLock = _MdmDiDteNvramLock_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 6, 5, 1, 1, 28),
    _MdmDiDteNvramLock_Type()
)
mdmDiDteNvramLock.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mdmDiDteNvramLock.setStatus("mandatory")


class _MdmDiSerialFormat_Type(Integer32):
    """Custom type mdmDiSerialFormat based on Integer32"""
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
        *(("bit7EvenParity", 2),
          ("bit7MarkParity", 4),
          ("bit7OddParity", 3),
          ("bit8NoParity", 1))
    )


_MdmDiSerialFormat_Type.__name__ = "Integer32"
_MdmDiSerialFormat_Object = MibTableColumn
mdmDiSerialFormat = _MdmDiSerialFormat_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 6, 5, 1, 1, 29),
    _MdmDiSerialFormat_Type()
)
mdmDiSerialFormat.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mdmDiSerialFormat.setStatus("mandatory")


class _MdmDiDefaultDteDataRate_Type(Integer32):
    """Custom type mdmDiDefaultDteDataRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              8,
              12,
              13,
              16,
              17,
              22)
        )
    )
    namedValues = NamedValues(
        *(("bps110", 1),
          ("bps115K", 22),
          ("bps1200", 4),
          ("bps19K", 12),
          ("bps2400", 5),
          ("bps300", 2),
          ("bps38K", 13),
          ("bps4800", 6),
          ("bps57K", 17),
          ("bps600", 3),
          ("bps9600", 8),
          ("unknown", 16))
    )


_MdmDiDefaultDteDataRate_Type.__name__ = "Integer32"
_MdmDiDefaultDteDataRate_Object = MibTableColumn
mdmDiDefaultDteDataRate = _MdmDiDefaultDteDataRate_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 6, 5, 1, 1, 30),
    _MdmDiDefaultDteDataRate_Type()
)
mdmDiDefaultDteDataRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mdmDiDefaultDteDataRate.setStatus("mandatory")


class _MdmDiRemAccessMsg_Type(Integer32):
    """Custom type mdmDiRemAccessMsg based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_MdmDiRemAccessMsg_Type.__name__ = "Integer32"
_MdmDiRemAccessMsg_Object = MibTableColumn
mdmDiRemAccessMsg = _MdmDiRemAccessMsg_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 6, 5, 1, 1, 31),
    _MdmDiRemAccessMsg_Type()
)
mdmDiRemAccessMsg.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mdmDiRemAccessMsg.setStatus("mandatory")


class _MdmDiV25DteDataRate_Type(Integer32):
    """Custom type mdmDiV25DteDataRate based on Integer32"""
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
        *(("bps1200", 1),
          ("bps12K", 6),
          ("bps14K", 7),
          ("bps16K", 8),
          ("bps19K", 9),
          ("bps21K", 10),
          ("bps2400", 2),
          ("bps24K", 11),
          ("bps26K", 12),
          ("bps28K", 13),
          ("bps4800", 3),
          ("bps7200", 4),
          ("bps9600", 5))
    )


_MdmDiV25DteDataRate_Type.__name__ = "Integer32"
_MdmDiV25DteDataRate_Object = MibTableColumn
mdmDiV25DteDataRate = _MdmDiV25DteDataRate_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 6, 5, 1, 1, 32),
    _MdmDiV25DteDataRate_Type()
)
mdmDiV25DteDataRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mdmDiV25DteDataRate.setStatus("optional")


class _MdmDiSrc_Type(Integer32):
    """Custom type mdmDiSrc based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("nic", 1),
          ("packetBus", 2))
    )


_MdmDiSrc_Type.__name__ = "Integer32"
_MdmDiSrc_Object = MibTableColumn
mdmDiSrc = _MdmDiSrc_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 6, 5, 1, 1, 33),
    _MdmDiSrc_Type()
)
mdmDiSrc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mdmDiSrc.setStatus("optional")


class _MdmDiSlot_Type(Integer32):
    """Custom type mdmDiSlot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_MdmDiSlot_Type.__name__ = "Integer32"
_MdmDiSlot_Object = MibTableColumn
mdmDiSlot = _MdmDiSlot_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 6, 5, 1, 1, 34),
    _MdmDiSlot_Type()
)
mdmDiSlot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mdmDiSlot.setStatus("optional")


class _MdmDiBusyClock_Type(Integer32):
    """Custom type mdmDiBusyClock based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("busyOut", 2),
          ("extClock1", 1))
    )


_MdmDiBusyClock_Type.__name__ = "Integer32"
_MdmDiBusyClock_Object = MibTableColumn
mdmDiBusyClock = _MdmDiBusyClock_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 6, 5, 1, 1, 35),
    _MdmDiBusyClock_Type()
)
mdmDiBusyClock.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mdmDiBusyClock.setStatus("optional")


class _MdmDiAtString_Type(DisplayString):
    """Custom type mdmDiAtString based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 41),
    )


_MdmDiAtString_Type.__name__ = "DisplayString"
_MdmDiAtString_Object = MibTableColumn
mdmDiAtString = _MdmDiAtString_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 6, 5, 1, 1, 36),
    _MdmDiAtString_Type()
)
mdmDiAtString.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mdmDiAtString.setStatus("mandatory")


class _MdmDiDtrRecognitionTime_Type(Integer32):
    """Custom type mdmDiDtrRecognitionTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_MdmDiDtrRecognitionTime_Type.__name__ = "Integer32"
_MdmDiDtrRecognitionTime_Object = MibTableColumn
mdmDiDtrRecognitionTime = _MdmDiDtrRecognitionTime_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 6, 5, 1, 1, 37),
    _MdmDiDtrRecognitionTime_Type()
)
mdmDiDtrRecognitionTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mdmDiDtrRecognitionTime.setStatus("mandatory")
_MdmSc_ObjectIdentity = ObjectIdentity
mdmSc = _MdmSc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 429, 1, 6, 6)
)
_MdmScTable_Object = MibTable
mdmScTable = _MdmScTable_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 6, 6, 1)
)
if mibBuilder.loadTexts:
    mdmScTable.setStatus("mandatory")
_MdmScEntry_Object = MibTableRow
mdmScEntry = _MdmScEntry_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 6, 6, 1, 1)
)
mdmScEntry.setIndexNames(
    (0, "MDM-MIB", "mdmScIndex"),
)
if mibBuilder.loadTexts:
    mdmScEntry.setStatus("mandatory")
_MdmScIndex_Type = Integer32
_MdmScIndex_Object = MibTableColumn
mdmScIndex = _MdmScIndex_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 6, 6, 1, 1, 1),
    _MdmScIndex_Type()
)
mdmScIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mdmScIndex.setStatus("mandatory")


class _MdmScLinkRateSelect_Type(Integer32):
    """Custom type mdmScLinkRateSelect based on Integer32"""
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
              25,
              26,
              27,
              28,
              29,
              30,
              31,
              32,
              33,
              34,
              35,
              36,
              37,
              38,
              39,
              40,
              41,
              42,
              43,
              44,
              45)
        )
    )
    namedValues = NamedValues(
        *(("bps1200", 3),
          ("bps12000", 8),
          ("bps14400", 9),
          ("bps16800", 10),
          ("bps19200", 11),
          ("bps21600", 12),
          ("bps2400", 4),
          ("bps24000", 13),
          ("bps26400", 14),
          ("bps28000", 34),
          ("bps28800", 15),
          ("bps29333", 35),
          ("bps300", 2),
          ("bps30666", 36),
          ("bps31200", 16),
          ("bps32000", 37),
          ("bps33333", 18),
          ("bps33600", 17),
          ("bps34666", 38),
          ("bps36000", 39),
          ("bps37333", 19),
          ("bps38666", 40),
          ("bps40000", 41),
          ("bps41333", 20),
          ("bps42666", 21),
          ("bps44000", 22),
          ("bps45333", 23),
          ("bps46666", 24),
          ("bps4800", 5),
          ("bps48000", 25),
          ("bps49333", 26),
          ("bps50666", 27),
          ("bps52000", 28),
          ("bps53333", 29),
          ("bps54666", 30),
          ("bps56000", 31),
          ("bps57333", 32),
          ("bps58666", 42),
          ("bps60000", 43),
          ("bps61333", 44),
          ("bps62666", 45),
          ("bps64000", 33),
          ("bps7200", 6),
          ("bps9600", 7),
          ("variable", 1))
    )


_MdmScLinkRateSelect_Type.__name__ = "Integer32"
_MdmScLinkRateSelect_Object = MibTableColumn
mdmScLinkRateSelect = _MdmScLinkRateSelect_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 6, 6, 1, 1, 2),
    _MdmScLinkRateSelect_Type()
)
mdmScLinkRateSelect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mdmScLinkRateSelect.setStatus("mandatory")


class _MdmScNonArqBufSize_Type(Integer32):
    """Custom type mdmScNonArqBufSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("bytes128", 2),
          ("bytes1500", 1))
    )


_MdmScNonArqBufSize_Type.__name__ = "Integer32"
_MdmScNonArqBufSize_Object = MibTableColumn
mdmScNonArqBufSize = _MdmScNonArqBufSize_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 6, 6, 1, 1, 3),
    _MdmScNonArqBufSize_Type()
)
mdmScNonArqBufSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mdmScNonArqBufSize.setStatus("mandatory")


class _MdmScNonMnpDataCapture_Type(Integer32):
    """Custom type mdmScNonMnpDataCapture based on Integer32"""
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


_MdmScNonMnpDataCapture_Type.__name__ = "Integer32"
_MdmScNonMnpDataCapture_Object = MibTableColumn
mdmScNonMnpDataCapture = _MdmScNonMnpDataCapture_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 6, 6, 1, 1, 4),
    _MdmScNonMnpDataCapture_Type()
)
mdmScNonMnpDataCapture.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mdmScNonMnpDataCapture.setStatus("mandatory")


class _MdmScSyncTimingSource_Type(Integer32):
    """Custom type mdmScSyncTimingSource based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("external", 2),
          ("internal", 1),
          ("rxLinkClock", 3))
    )


_MdmScSyncTimingSource_Type.__name__ = "Integer32"
_MdmScSyncTimingSource_Object = MibTableColumn
mdmScSyncTimingSource = _MdmScSyncTimingSource_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 6, 6, 1, 1, 5),
    _MdmScSyncTimingSource_Type()
)
mdmScSyncTimingSource.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mdmScSyncTimingSource.setStatus("mandatory")


class _MdmScHstMod_Type(Integer32):
    """Custom type mdmScHstMod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_MdmScHstMod_Type.__name__ = "Integer32"
_MdmScHstMod_Object = MibTableColumn
mdmScHstMod = _MdmScHstMod_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 6, 6, 1, 1, 6),
    _MdmScHstMod_Type()
)
mdmScHstMod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mdmScHstMod.setStatus("mandatory")


class _MdmScHiFreqEq_Type(Integer32):
    """Custom type mdmScHiFreqEq based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_MdmScHiFreqEq_Type.__name__ = "Integer32"
_MdmScHiFreqEq_Object = MibTableColumn
mdmScHiFreqEq = _MdmScHiFreqEq_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 6, 6, 1, 1, 7),
    _MdmScHiFreqEq_Type()
)
mdmScHiFreqEq.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mdmScHiFreqEq.setStatus("mandatory")


class _MdmScBackChanRate_Type(Integer32):
    """Custom type mdmScBackChanRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("bps300", 2),
          ("bps450", 1))
    )


_MdmScBackChanRate_Type.__name__ = "Integer32"
_MdmScBackChanRate_Object = MibTableColumn
mdmScBackChanRate = _MdmScBackChanRate_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 6, 6, 1, 1, 8),
    _MdmScBackChanRate_Type()
)
mdmScBackChanRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mdmScBackChanRate.setStatus("mandatory")


class _MdmScV21Mod_Type(Integer32):
    """Custom type mdmScV21Mod based on Integer32"""
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


_MdmScV21Mod_Type.__name__ = "Integer32"
_MdmScV21Mod_Object = MibTableColumn
mdmScV21Mod = _MdmScV21Mod_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 6, 6, 1, 1, 9),
    _MdmScV21Mod_Type()
)
mdmScV21Mod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mdmScV21Mod.setStatus("mandatory")


class _MdmScV32UnencodedMod_Type(Integer32):
    """Custom type mdmScV32UnencodedMod based on Integer32"""
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


_MdmScV32UnencodedMod_Type.__name__ = "Integer32"
_MdmScV32UnencodedMod_Object = MibTableColumn
mdmScV32UnencodedMod = _MdmScV32UnencodedMod_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 6, 6, 1, 1, 10),
    _MdmScV32UnencodedMod_Type()
)
mdmScV32UnencodedMod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mdmScV32UnencodedMod.setStatus("mandatory")


class _MdmScV32Mod_Type(Integer32):
    """Custom type mdmScV32Mod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_MdmScV32Mod_Type.__name__ = "Integer32"
_MdmScV32Mod_Object = MibTableColumn
mdmScV32Mod = _MdmScV32Mod_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 6, 6, 1, 1, 11),
    _MdmScV32Mod_Type()
)
mdmScV32Mod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mdmScV32Mod.setStatus("mandatory")


class _MdmScBell208_Type(Integer32):
    """Custom type mdmScBell208 based on Integer32"""
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


_MdmScBell208_Type.__name__ = "Integer32"
_MdmScBell208_Object = MibTableColumn
mdmScBell208 = _MdmScBell208_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 6, 6, 1, 1, 12),
    _MdmScBell208_Type()
)
mdmScBell208.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mdmScBell208.setStatus("mandatory")


class _MdmScV32Bis_Type(Integer32):
    """Custom type mdmScV32Bis based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_MdmScV32Bis_Type.__name__ = "Integer32"
_MdmScV32Bis_Object = MibTableColumn
mdmScV32Bis = _MdmScV32Bis_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 6, 6, 1, 1, 13),
    _MdmScV32Bis_Type()
)
mdmScV32Bis.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mdmScV32Bis.setStatus("mandatory")


class _MdmScV32BisEnhance_Type(Integer32):
    """Custom type mdmScV32BisEnhance based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_MdmScV32BisEnhance_Type.__name__ = "Integer32"
_MdmScV32BisEnhance_Object = MibTableColumn
mdmScV32BisEnhance = _MdmScV32BisEnhance_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 6, 6, 1, 1, 14),
    _MdmScV32BisEnhance_Type()
)
mdmScV32BisEnhance.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mdmScV32BisEnhance.setStatus("mandatory")


class _MdmScV32QuickRetrain_Type(Integer32):
    """Custom type mdmScV32QuickRetrain based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_MdmScV32QuickRetrain_Type.__name__ = "Integer32"
_MdmScV32QuickRetrain_Object = MibTableColumn
mdmScV32QuickRetrain = _MdmScV32QuickRetrain_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 6, 6, 1, 1, 15),
    _MdmScV32QuickRetrain_Type()
)
mdmScV32QuickRetrain.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mdmScV32QuickRetrain.setStatus("mandatory")


class _MdmScV23_Type(Integer32):
    """Custom type mdmScV23 based on Integer32"""
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


_MdmScV23_Type.__name__ = "Integer32"
_MdmScV23_Object = MibTableColumn
mdmScV23 = _MdmScV23_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 6, 6, 1, 1, 16),
    _MdmScV23_Type()
)
mdmScV23.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mdmScV23.setStatus("mandatory")


class _MdmScHiSpeedModulation_Type(Integer32):
    """Custom type mdmScHiSpeedModulation based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("bell208", 3),
          ("hst", 2),
          ("v32", 1))
    )


_MdmScHiSpeedModulation_Type.__name__ = "Integer32"
_MdmScHiSpeedModulation_Object = MibTableColumn
mdmScHiSpeedModulation = _MdmScHiSpeedModulation_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 6, 6, 1, 1, 17),
    _MdmScHiSpeedModulation_Type()
)
mdmScHiSpeedModulation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mdmScHiSpeedModulation.setStatus("mandatory")


class _MdmScFallback_Type(Integer32):
    """Custom type mdmScFallback based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_MdmScFallback_Type.__name__ = "Integer32"
_MdmScFallback_Object = MibTableColumn
mdmScFallback = _MdmScFallback_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 6, 6, 1, 1, 18),
    _MdmScFallback_Type()
)
mdmScFallback.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mdmScFallback.setStatus("mandatory")


class _MdmScV32TerboModeEnable_Type(Integer32):
    """Custom type mdmScV32TerboModeEnable based on Integer32"""
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


_MdmScV32TerboModeEnable_Type.__name__ = "Integer32"
_MdmScV32TerboModeEnable_Object = MibTableColumn
mdmScV32TerboModeEnable = _MdmScV32TerboModeEnable_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 6, 6, 1, 1, 19),
    _MdmScV32TerboModeEnable_Type()
)
mdmScV32TerboModeEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mdmScV32TerboModeEnable.setStatus("mandatory")


class _MdmScV34ModeEnable_Type(Integer32):
    """Custom type mdmScV34ModeEnable based on Integer32"""
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


_MdmScV34ModeEnable_Type.__name__ = "Integer32"
_MdmScV34ModeEnable_Object = MibTableColumn
mdmScV34ModeEnable = _MdmScV34ModeEnable_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 6, 6, 1, 1, 20),
    _MdmScV34ModeEnable_Type()
)
mdmScV34ModeEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mdmScV34ModeEnable.setStatus("mandatory")


class _MdmScVFCSymRate2400_Type(Integer32):
    """Custom type mdmScVFCSymRate2400 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_MdmScVFCSymRate2400_Type.__name__ = "Integer32"
_MdmScVFCSymRate2400_Object = MibTableColumn
mdmScVFCSymRate2400 = _MdmScVFCSymRate2400_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 6, 6, 1, 1, 21),
    _MdmScVFCSymRate2400_Type()
)
mdmScVFCSymRate2400.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mdmScVFCSymRate2400.setStatus("mandatory")


class _MdmScVFCSymRate2743_Type(Integer32):
    """Custom type mdmScVFCSymRate2743 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_MdmScVFCSymRate2743_Type.__name__ = "Integer32"
_MdmScVFCSymRate2743_Object = MibTableColumn
mdmScVFCSymRate2743 = _MdmScVFCSymRate2743_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 6, 6, 1, 1, 22),
    _MdmScVFCSymRate2743_Type()
)
mdmScVFCSymRate2743.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mdmScVFCSymRate2743.setStatus("mandatory")


class _MdmScVFCSymRate2800_Type(Integer32):
    """Custom type mdmScVFCSymRate2800 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_MdmScVFCSymRate2800_Type.__name__ = "Integer32"
_MdmScVFCSymRate2800_Object = MibTableColumn
mdmScVFCSymRate2800 = _MdmScVFCSymRate2800_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 6, 6, 1, 1, 23),
    _MdmScVFCSymRate2800_Type()
)
mdmScVFCSymRate2800.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mdmScVFCSymRate2800.setStatus("mandatory")


class _MdmScVFCSymRate3000_Type(Integer32):
    """Custom type mdmScVFCSymRate3000 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_MdmScVFCSymRate3000_Type.__name__ = "Integer32"
_MdmScVFCSymRate3000_Object = MibTableColumn
mdmScVFCSymRate3000 = _MdmScVFCSymRate3000_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 6, 6, 1, 1, 24),
    _MdmScVFCSymRate3000_Type()
)
mdmScVFCSymRate3000.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mdmScVFCSymRate3000.setStatus("mandatory")


class _MdmScVFCSymRate3200_Type(Integer32):
    """Custom type mdmScVFCSymRate3200 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_MdmScVFCSymRate3200_Type.__name__ = "Integer32"
_MdmScVFCSymRate3200_Object = MibTableColumn
mdmScVFCSymRate3200 = _MdmScVFCSymRate3200_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 6, 6, 1, 1, 25),
    _MdmScVFCSymRate3200_Type()
)
mdmScVFCSymRate3200.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mdmScVFCSymRate3200.setStatus("mandatory")


class _MdmScVFCSymRate3429_Type(Integer32):
    """Custom type mdmScVFCSymRate3429 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_MdmScVFCSymRate3429_Type.__name__ = "Integer32"
_MdmScVFCSymRate3429_Object = MibTableColumn
mdmScVFCSymRate3429 = _MdmScVFCSymRate3429_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 6, 6, 1, 1, 26),
    _MdmScVFCSymRate3429_Type()
)
mdmScVFCSymRate3429.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mdmScVFCSymRate3429.setStatus("mandatory")


class _MdmScVFC8S2DMapping_Type(Integer32):
    """Custom type mdmScVFC8S2DMapping based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_MdmScVFC8S2DMapping_Type.__name__ = "Integer32"
_MdmScVFC8S2DMapping_Object = MibTableColumn
mdmScVFC8S2DMapping = _MdmScVFC8S2DMapping_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 6, 6, 1, 1, 27),
    _MdmScVFC8S2DMapping_Type()
)
mdmScVFC8S2DMapping.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mdmScVFC8S2DMapping.setStatus("mandatory")


class _MdmScVFC16S4DMapping_Type(Integer32):
    """Custom type mdmScVFC16S4DMapping based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_MdmScVFC16S4DMapping_Type.__name__ = "Integer32"
_MdmScVFC16S4DMapping_Object = MibTableColumn
mdmScVFC16S4DMapping = _MdmScVFC16S4DMapping_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 6, 6, 1, 1, 28),
    _MdmScVFC16S4DMapping_Type()
)
mdmScVFC16S4DMapping.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mdmScVFC16S4DMapping.setStatus("mandatory")


class _MdmScVFC32S2DMapping_Type(Integer32):
    """Custom type mdmScVFC32S2DMapping based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_MdmScVFC32S2DMapping_Type.__name__ = "Integer32"
_MdmScVFC32S2DMapping_Object = MibTableColumn
mdmScVFC32S2DMapping = _MdmScVFC32S2DMapping_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 6, 6, 1, 1, 29),
    _MdmScVFC32S2DMapping_Type()
)
mdmScVFC32S2DMapping.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mdmScVFC32S2DMapping.setStatus("mandatory")


class _MdmScVFC64S4DMapping_Type(Integer32):
    """Custom type mdmScVFC64S4DMapping based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_MdmScVFC64S4DMapping_Type.__name__ = "Integer32"
_MdmScVFC64S4DMapping_Object = MibTableColumn
mdmScVFC64S4DMapping = _MdmScVFC64S4DMapping_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 6, 6, 1, 1, 30),
    _MdmScVFC64S4DMapping_Type()
)
mdmScVFC64S4DMapping.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mdmScVFC64S4DMapping.setStatus("mandatory")


class _MdmScVFCNonLinearCoding_Type(Integer32):
    """Custom type mdmScVFCNonLinearCoding based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_MdmScVFCNonLinearCoding_Type.__name__ = "Integer32"
_MdmScVFCNonLinearCoding_Object = MibTableColumn
mdmScVFCNonLinearCoding = _MdmScVFCNonLinearCoding_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 6, 6, 1, 1, 31),
    _MdmScVFCNonLinearCoding_Type()
)
mdmScVFCNonLinearCoding.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mdmScVFCNonLinearCoding.setStatus("mandatory")


class _MdmScVFCTxLevelDeviation_Type(Integer32):
    """Custom type mdmScVFCTxLevelDeviation based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_MdmScVFCTxLevelDeviation_Type.__name__ = "Integer32"
_MdmScVFCTxLevelDeviation_Object = MibTableColumn
mdmScVFCTxLevelDeviation = _MdmScVFCTxLevelDeviation_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 6, 6, 1, 1, 32),
    _MdmScVFCTxLevelDeviation_Type()
)
mdmScVFCTxLevelDeviation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mdmScVFCTxLevelDeviation.setStatus("mandatory")


class _MdmScVFCPreEmphasis_Type(Integer32):
    """Custom type mdmScVFCPreEmphasis based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_MdmScVFCPreEmphasis_Type.__name__ = "Integer32"
_MdmScVFCPreEmphasis_Object = MibTableColumn
mdmScVFCPreEmphasis = _MdmScVFCPreEmphasis_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 6, 6, 1, 1, 33),
    _MdmScVFCPreEmphasis_Type()
)
mdmScVFCPreEmphasis.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mdmScVFCPreEmphasis.setStatus("mandatory")


class _MdmScVFCPreCoding_Type(Integer32):
    """Custom type mdmScVFCPreCoding based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_MdmScVFCPreCoding_Type.__name__ = "Integer32"
_MdmScVFCPreCoding_Object = MibTableColumn
mdmScVFCPreCoding = _MdmScVFCPreCoding_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 6, 6, 1, 1, 34),
    _MdmScVFCPreCoding_Type()
)
mdmScVFCPreCoding.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mdmScVFCPreCoding.setStatus("mandatory")


class _MdmScVFCShaping_Type(Integer32):
    """Custom type mdmScVFCShaping based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_MdmScVFCShaping_Type.__name__ = "Integer32"
_MdmScVFCShaping_Object = MibTableColumn
mdmScVFCShaping = _MdmScVFCShaping_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 6, 6, 1, 1, 35),
    _MdmScVFCShaping_Type()
)
mdmScVFCShaping.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mdmScVFCShaping.setStatus("mandatory")


class _MdmScVFCModeEnable_Type(Integer32):
    """Custom type mdmScVFCModeEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_MdmScVFCModeEnable_Type.__name__ = "Integer32"
_MdmScVFCModeEnable_Object = MibTableColumn
mdmScVFCModeEnable = _MdmScVFCModeEnable_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 6, 6, 1, 1, 36),
    _MdmScVFCModeEnable_Type()
)
mdmScVFCModeEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mdmScVFCModeEnable.setStatus("mandatory")


class _MdmScV8_Type(Integer32):
    """Custom type mdmScV8 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_MdmScV8_Type.__name__ = "Integer32"
_MdmScV8_Object = MibTableColumn
mdmScV8 = _MdmScV8_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 6, 6, 1, 1, 37),
    _MdmScV8_Type()
)
mdmScV8.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mdmScV8.setStatus("mandatory")


class _MdmSCV8CallIndicator_Type(Integer32):
    """Custom type mdmSCV8CallIndicator based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_MdmSCV8CallIndicator_Type.__name__ = "Integer32"
_MdmSCV8CallIndicator_Object = MibTableColumn
mdmSCV8CallIndicator = _MdmSCV8CallIndicator_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 6, 6, 1, 1, 38),
    _MdmSCV8CallIndicator_Type()
)
mdmSCV8CallIndicator.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mdmSCV8CallIndicator.setStatus("mandatory")


class _MdmScV34pModeEnable_Type(Integer32):
    """Custom type mdmScV34pModeEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_MdmScV34pModeEnable_Type.__name__ = "Integer32"
_MdmScV34pModeEnable_Object = MibTableColumn
mdmScV34pModeEnable = _MdmScV34pModeEnable_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 6, 6, 1, 1, 39),
    _MdmScV34pModeEnable_Type()
)
mdmScV34pModeEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mdmScV34pModeEnable.setStatus("mandatory")


class _MdmSc300_Type(Integer32):
    """Custom type mdmSc300 based on Integer32"""
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


_MdmSc300_Type.__name__ = "Integer32"
_MdmSc300_Object = MibTableColumn
mdmSc300 = _MdmSc300_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 6, 6, 1, 1, 40),
    _MdmSc300_Type()
)
mdmSc300.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mdmSc300.setStatus("mandatory")


class _MdmSc1200_Type(Integer32):
    """Custom type mdmSc1200 based on Integer32"""
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


_MdmSc1200_Type.__name__ = "Integer32"
_MdmSc1200_Object = MibTableColumn
mdmSc1200 = _MdmSc1200_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 6, 6, 1, 1, 41),
    _MdmSc1200_Type()
)
mdmSc1200.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mdmSc1200.setStatus("mandatory")


class _MdmSc2400_Type(Integer32):
    """Custom type mdmSc2400 based on Integer32"""
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


_MdmSc2400_Type.__name__ = "Integer32"
_MdmSc2400_Object = MibTableColumn
mdmSc2400 = _MdmSc2400_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 6, 6, 1, 1, 42),
    _MdmSc2400_Type()
)
mdmSc2400.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mdmSc2400.setStatus("mandatory")


class _MdmScHighSpeed_Type(Integer32):
    """Custom type mdmScHighSpeed based on Integer32"""
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


_MdmScHighSpeed_Type.__name__ = "Integer32"
_MdmScHighSpeed_Object = MibTableColumn
mdmScHighSpeed = _MdmScHighSpeed_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 6, 6, 1, 1, 43),
    _MdmScHighSpeed_Type()
)
mdmScHighSpeed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mdmScHighSpeed.setStatus("mandatory")


class _MdmScSelectiveReject_Type(Integer32):
    """Custom type mdmScSelectiveReject based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_MdmScSelectiveReject_Type.__name__ = "Integer32"
_MdmScSelectiveReject_Object = MibTableColumn
mdmScSelectiveReject = _MdmScSelectiveReject_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 6, 6, 1, 1, 44),
    _MdmScSelectiveReject_Type()
)
mdmScSelectiveReject.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mdmScSelectiveReject.setStatus("mandatory")


class _MdmScPhExclusionDel_Type(Integer32):
    """Custom type mdmScPhExclusionDel based on Integer32"""
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


_MdmScPhExclusionDel_Type.__name__ = "Integer32"
_MdmScPhExclusionDel_Object = MibTableColumn
mdmScPhExclusionDel = _MdmScPhExclusionDel_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 6, 6, 1, 1, 45),
    _MdmScPhExclusionDel_Type()
)
mdmScPhExclusionDel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mdmScPhExclusionDel.setStatus("mandatory")


class _MdmScLinkRateAmpU_Type(Integer32):
    """Custom type mdmScLinkRateAmpU based on Integer32"""
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
              25,
              26,
              27,
              28,
              29,
              30,
              31,
              32,
              33,
              34,
              35,
              36,
              37,
              38,
              39,
              40,
              41,
              42,
              43,
              44,
              45)
        )
    )
    namedValues = NamedValues(
        *(("bps1200", 3),
          ("bps12000", 8),
          ("bps14400", 9),
          ("bps16800", 10),
          ("bps19200", 11),
          ("bps21600", 12),
          ("bps2400", 4),
          ("bps24000", 13),
          ("bps26400", 14),
          ("bps28000", 34),
          ("bps28800", 15),
          ("bps29333", 35),
          ("bps300", 2),
          ("bps30666", 36),
          ("bps31200", 16),
          ("bps32000", 37),
          ("bps33333", 18),
          ("bps33600", 17),
          ("bps34666", 38),
          ("bps36000", 39),
          ("bps37333", 19),
          ("bps38666", 40),
          ("bps40000", 41),
          ("bps41333", 20),
          ("bps42666", 21),
          ("bps44000", 22),
          ("bps45333", 23),
          ("bps46666", 24),
          ("bps4800", 5),
          ("bps48000", 25),
          ("bps49333", 26),
          ("bps50666", 27),
          ("bps52000", 28),
          ("bps53333", 29),
          ("bps54666", 30),
          ("bps56000", 31),
          ("bps57333", 32),
          ("bps58666", 42),
          ("bps60000", 43),
          ("bps61333", 44),
          ("bps62666", 45),
          ("bps64000", 33),
          ("bps7200", 6),
          ("bps9600", 7),
          ("variable", 1))
    )


_MdmScLinkRateAmpU_Type.__name__ = "Integer32"
_MdmScLinkRateAmpU_Object = MibTableColumn
mdmScLinkRateAmpU = _MdmScLinkRateAmpU_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 6, 6, 1, 1, 46),
    _MdmScLinkRateAmpU_Type()
)
mdmScLinkRateAmpU.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mdmScLinkRateAmpU.setStatus("mandatory")


class _MdmScLowerSpeedMin_Type(Integer32):
    """Custom type mdmScLowerSpeedMin based on Integer32"""
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
              25,
              26,
              27,
              28,
              29,
              30,
              31,
              32,
              33,
              34,
              35,
              36,
              37,
              38,
              39,
              40,
              41,
              42,
              43,
              44,
              45)
        )
    )
    namedValues = NamedValues(
        *(("bps1200", 3),
          ("bps12000", 8),
          ("bps14400", 9),
          ("bps16800", 10),
          ("bps19200", 11),
          ("bps21600", 12),
          ("bps2400", 4),
          ("bps24000", 13),
          ("bps26400", 14),
          ("bps28000", 34),
          ("bps28800", 15),
          ("bps29333", 35),
          ("bps300", 2),
          ("bps30666", 36),
          ("bps31200", 16),
          ("bps32000", 37),
          ("bps33333", 18),
          ("bps33600", 17),
          ("bps34666", 38),
          ("bps36000", 39),
          ("bps37333", 19),
          ("bps38666", 40),
          ("bps40000", 41),
          ("bps41333", 20),
          ("bps42666", 21),
          ("bps44000", 22),
          ("bps45333", 23),
          ("bps46666", 24),
          ("bps4800", 5),
          ("bps48000", 25),
          ("bps49333", 26),
          ("bps50666", 27),
          ("bps52000", 28),
          ("bps53333", 29),
          ("bps54666", 30),
          ("bps56000", 31),
          ("bps57333", 32),
          ("bps58666", 42),
          ("bps60000", 43),
          ("bps61333", 44),
          ("bps62666", 45),
          ("bps64000", 33),
          ("bps7200", 6),
          ("bps9600", 7),
          ("variable", 1))
    )


_MdmScLowerSpeedMin_Type.__name__ = "Integer32"
_MdmScLowerSpeedMin_Object = MibTableColumn
mdmScLowerSpeedMin = _MdmScLowerSpeedMin_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 6, 6, 1, 1, 47),
    _MdmScLowerSpeedMin_Type()
)
mdmScLowerSpeedMin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mdmScLowerSpeedMin.setStatus("mandatory")


class _MdmScLowerSpeedMax_Type(Integer32):
    """Custom type mdmScLowerSpeedMax based on Integer32"""
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
              25,
              26,
              27,
              28,
              29,
              30,
              31,
              32,
              33,
              34,
              35,
              36,
              37,
              38,
              39,
              40,
              41,
              42,
              43,
              44,
              45)
        )
    )
    namedValues = NamedValues(
        *(("bps1200", 3),
          ("bps12000", 8),
          ("bps14400", 9),
          ("bps16800", 10),
          ("bps19200", 11),
          ("bps21600", 12),
          ("bps2400", 4),
          ("bps24000", 13),
          ("bps26400", 14),
          ("bps28000", 34),
          ("bps28800", 15),
          ("bps29333", 35),
          ("bps300", 2),
          ("bps30666", 36),
          ("bps31200", 16),
          ("bps32000", 37),
          ("bps33333", 18),
          ("bps33600", 17),
          ("bps34666", 38),
          ("bps36000", 39),
          ("bps37333", 19),
          ("bps38666", 40),
          ("bps40000", 41),
          ("bps41333", 20),
          ("bps42666", 21),
          ("bps44000", 22),
          ("bps45333", 23),
          ("bps46666", 24),
          ("bps4800", 5),
          ("bps48000", 25),
          ("bps49333", 26),
          ("bps50666", 27),
          ("bps52000", 28),
          ("bps53333", 29),
          ("bps54666", 30),
          ("bps56000", 31),
          ("bps57333", 32),
          ("bps58666", 42),
          ("bps60000", 43),
          ("bps61333", 44),
          ("bps62666", 45),
          ("bps64000", 33),
          ("bps7200", 6),
          ("bps9600", 7),
          ("variable", 1))
    )


_MdmScLowerSpeedMax_Type.__name__ = "Integer32"
_MdmScLowerSpeedMax_Object = MibTableColumn
mdmScLowerSpeedMax = _MdmScLowerSpeedMax_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 6, 6, 1, 1, 48),
    _MdmScLowerSpeedMax_Type()
)
mdmScLowerSpeedMax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mdmScLowerSpeedMax.setStatus("mandatory")


class _MdmScX2Client_Type(Integer32):
    """Custom type mdmScX2Client based on Integer32"""
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


_MdmScX2Client_Type.__name__ = "Integer32"
_MdmScX2Client_Object = MibTableColumn
mdmScX2Client = _MdmScX2Client_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 6, 6, 1, 1, 49),
    _MdmScX2Client_Type()
)
mdmScX2Client.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mdmScX2Client.setStatus("mandatory")


class _MdmScX2Server_Type(Integer32):
    """Custom type mdmScX2Server based on Integer32"""
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


_MdmScX2Server_Type.__name__ = "Integer32"
_MdmScX2Server_Object = MibTableColumn
mdmScX2Server = _MdmScX2Server_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 6, 6, 1, 1, 50),
    _MdmScX2Server_Type()
)
mdmScX2Server.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mdmScX2Server.setStatus("mandatory")


class _MdmScX2Symmetric_Type(Integer32):
    """Custom type mdmScX2Symmetric based on Integer32"""
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


_MdmScX2Symmetric_Type.__name__ = "Integer32"
_MdmScX2Symmetric_Object = MibTableColumn
mdmScX2Symmetric = _MdmScX2Symmetric_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 6, 6, 1, 1, 51),
    _MdmScX2Symmetric_Type()
)
mdmScX2Symmetric.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mdmScX2Symmetric.setStatus("mandatory")


class _MdmScX2HighPowerConst_Type(Integer32):
    """Custom type mdmScX2HighPowerConst based on Integer32"""
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


_MdmScX2HighPowerConst_Type.__name__ = "Integer32"
_MdmScX2HighPowerConst_Object = MibTableColumn
mdmScX2HighPowerConst = _MdmScX2HighPowerConst_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 6, 6, 1, 1, 52),
    _MdmScX2HighPowerConst_Type()
)
mdmScX2HighPowerConst.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mdmScX2HighPowerConst.setStatus("mandatory")


class _MdmScPiafs_Type(Integer32):
    """Custom type mdmScPiafs based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_MdmScPiafs_Type.__name__ = "Integer32"
_MdmScPiafs_Object = MibTableColumn
mdmScPiafs = _MdmScPiafs_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 6, 6, 1, 1, 53),
    _MdmScPiafs_Type()
)
mdmScPiafs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mdmScPiafs.setStatus("mandatory")


class _MdmScPiafsV42bis_Type(Integer32):
    """Custom type mdmScPiafsV42bis based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_MdmScPiafsV42bis_Type.__name__ = "Integer32"
_MdmScPiafsV42bis_Object = MibTableColumn
mdmScPiafsV42bis = _MdmScPiafsV42bis_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 6, 6, 1, 1, 54),
    _MdmScPiafsV42bis_Type()
)
mdmScPiafsV42bis.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mdmScPiafsV42bis.setStatus("mandatory")


class _MdmScTxPwrLvl_Type(Integer32):
    """Custom type mdmScTxPwrLvl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 31),
    )


_MdmScTxPwrLvl_Type.__name__ = "Integer32"
_MdmScTxPwrLvl_Object = MibTableColumn
mdmScTxPwrLvl = _MdmScTxPwrLvl_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 6, 6, 1, 1, 55),
    _MdmScTxPwrLvl_Type()
)
mdmScTxPwrLvl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mdmScTxPwrLvl.setStatus("mandatory")


class _MdmScTxPwrLvlApplied_Type(Integer32):
    """Custom type mdmScTxPwrLvlApplied based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("inputToFarEndOfCodec", 1),
          ("outputOfTheServerModem", 2))
    )


_MdmScTxPwrLvlApplied_Type.__name__ = "Integer32"
_MdmScTxPwrLvlApplied_Object = MibTableColumn
mdmScTxPwrLvlApplied = _MdmScTxPwrLvlApplied_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 6, 6, 1, 1, 56),
    _MdmScTxPwrLvlApplied_Type()
)
mdmScTxPwrLvlApplied.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mdmScTxPwrLvlApplied.setStatus("mandatory")


class _MdmScX2Version2_Type(Integer32):
    """Custom type mdmScX2Version2 based on Integer32"""
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


_MdmScX2Version2_Type.__name__ = "Integer32"
_MdmScX2Version2_Object = MibTableColumn
mdmScX2Version2 = _MdmScX2Version2_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 6, 6, 1, 1, 57),
    _MdmScX2Version2_Type()
)
mdmScX2Version2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mdmScX2Version2.setStatus("mandatory")


class _MdmScV34Fallback_Type(Integer32):
    """Custom type mdmScV34Fallback based on Integer32"""
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


_MdmScV34Fallback_Type.__name__ = "Integer32"
_MdmScV34Fallback_Object = MibTableColumn
mdmScV34Fallback = _MdmScV34Fallback_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 6, 6, 1, 1, 58),
    _MdmScV34Fallback_Type()
)
mdmScV34Fallback.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mdmScV34Fallback.setStatus("mandatory")


class _MdmScV90Analogue_Type(Integer32):
    """Custom type mdmScV90Analogue based on Integer32"""
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


_MdmScV90Analogue_Type.__name__ = "Integer32"
_MdmScV90Analogue_Object = MibTableColumn
mdmScV90Analogue = _MdmScV90Analogue_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 6, 6, 1, 1, 59),
    _MdmScV90Analogue_Type()
)
mdmScV90Analogue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mdmScV90Analogue.setStatus("mandatory")


class _MdmScV90Digital_Type(Integer32):
    """Custom type mdmScV90Digital based on Integer32"""
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


_MdmScV90Digital_Type.__name__ = "Integer32"
_MdmScV90Digital_Object = MibTableColumn
mdmScV90Digital = _MdmScV90Digital_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 6, 6, 1, 1, 60),
    _MdmScV90Digital_Type()
)
mdmScV90Digital.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mdmScV90Digital.setStatus("mandatory")


class _MdmScV90AllDigital_Type(Integer32):
    """Custom type mdmScV90AllDigital based on Integer32"""
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


_MdmScV90AllDigital_Type.__name__ = "Integer32"
_MdmScV90AllDigital_Object = MibTableColumn
mdmScV90AllDigital = _MdmScV90AllDigital_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 6, 6, 1, 1, 61),
    _MdmScV90AllDigital_Type()
)
mdmScV90AllDigital.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mdmScV90AllDigital.setStatus("mandatory")
_MdmCc_ObjectIdentity = ObjectIdentity
mdmCc = _MdmCc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 429, 1, 6, 7)
)
_MdmCcTable_Object = MibTable
mdmCcTable = _MdmCcTable_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 6, 7, 1)
)
if mibBuilder.loadTexts:
    mdmCcTable.setStatus("mandatory")
_MdmCcEntry_Object = MibTableRow
mdmCcEntry = _MdmCcEntry_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 6, 7, 1, 1)
)
mdmCcEntry.setIndexNames(
    (0, "MDM-MIB", "mdmCcIndex"),
)
if mibBuilder.loadTexts:
    mdmCcEntry.setStatus("mandatory")
_MdmCcIndex_Type = Integer32
_MdmCcIndex_Object = MibTableColumn
mdmCcIndex = _MdmCcIndex_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 6, 7, 1, 1, 1),
    _MdmCcIndex_Type()
)
mdmCcIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mdmCcIndex.setStatus("mandatory")


class _MdmCcDialDelay_Type(Integer32):
    """Custom type mdmCcDialDelay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_MdmCcDialDelay_Type.__name__ = "Integer32"
_MdmCcDialDelay_Object = MibTableColumn
mdmCcDialDelay = _MdmCcDialDelay_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 6, 7, 1, 1, 2),
    _MdmCcDialDelay_Type()
)
mdmCcDialDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mdmCcDialDelay.setStatus("mandatory")


class _MdmCcWaitForCarrier_Type(Integer32):
    """Custom type mdmCcWaitForCarrier based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_MdmCcWaitForCarrier_Type.__name__ = "Integer32"
_MdmCcWaitForCarrier_Object = MibTableColumn
mdmCcWaitForCarrier = _MdmCcWaitForCarrier_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 6, 7, 1, 1, 3),
    _MdmCcWaitForCarrier_Type()
)
mdmCcWaitForCarrier.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mdmCcWaitForCarrier.setStatus("mandatory")


class _MdmCcInactivityTimer_Type(Integer32):
    """Custom type mdmCcInactivityTimer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_MdmCcInactivityTimer_Type.__name__ = "Integer32"
_MdmCcInactivityTimer_Object = MibTableColumn
mdmCcInactivityTimer = _MdmCcInactivityTimer_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 6, 7, 1, 1, 4),
    _MdmCcInactivityTimer_Type()
)
mdmCcInactivityTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mdmCcInactivityTimer.setStatus("mandatory")


class _MdmCcAutoDialOnDtrEna_Type(Integer32):
    """Custom type mdmCcAutoDialOnDtrEna based on Integer32"""
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


_MdmCcAutoDialOnDtrEna_Type.__name__ = "Integer32"
_MdmCcAutoDialOnDtrEna_Object = MibTableColumn
mdmCcAutoDialOnDtrEna = _MdmCcAutoDialOnDtrEna_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 6, 7, 1, 1, 5),
    _MdmCcAutoDialOnDtrEna_Type()
)
mdmCcAutoDialOnDtrEna.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mdmCcAutoDialOnDtrEna.setStatus("mandatory")


class _MdmCcAutoDialOnPwrUpEna_Type(Integer32):
    """Custom type mdmCcAutoDialOnPwrUpEna based on Integer32"""
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


_MdmCcAutoDialOnPwrUpEna_Type.__name__ = "Integer32"
_MdmCcAutoDialOnPwrUpEna_Object = MibTableColumn
mdmCcAutoDialOnPwrUpEna = _MdmCcAutoDialOnPwrUpEna_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 6, 7, 1, 1, 6),
    _MdmCcAutoDialOnPwrUpEna_Type()
)
mdmCcAutoDialOnPwrUpEna.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mdmCcAutoDialOnPwrUpEna.setStatus("mandatory")


class _MdmCcGhostPortLockEna_Type(Integer32):
    """Custom type mdmCcGhostPortLockEna based on Integer32"""
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


_MdmCcGhostPortLockEna_Type.__name__ = "Integer32"
_MdmCcGhostPortLockEna_Object = MibTableColumn
mdmCcGhostPortLockEna = _MdmCcGhostPortLockEna_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 6, 7, 1, 1, 7),
    _MdmCcGhostPortLockEna_Type()
)
mdmCcGhostPortLockEna.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mdmCcGhostPortLockEna.setStatus("mandatory")


class _MdmCcQuietResultCodes_Type(Integer32):
    """Custom type mdmCcQuietResultCodes based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("displayResult", 1),
          ("noResult", 2),
          ("originateOnly", 3))
    )


_MdmCcQuietResultCodes_Type.__name__ = "Integer32"
_MdmCcQuietResultCodes_Object = MibTableColumn
mdmCcQuietResultCodes = _MdmCcQuietResultCodes_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 6, 7, 1, 1, 8),
    _MdmCcQuietResultCodes_Type()
)
mdmCcQuietResultCodes.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mdmCcQuietResultCodes.setStatus("mandatory")


class _MdmCcResponseMode_Type(Integer32):
    """Custom type mdmCcResponseMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("numeric", 1),
          ("verbal", 2))
    )


_MdmCcResponseMode_Type.__name__ = "Integer32"
_MdmCcResponseMode_Object = MibTableColumn
mdmCcResponseMode = _MdmCcResponseMode_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 6, 7, 1, 1, 9),
    _MdmCcResponseMode_Type()
)
mdmCcResponseMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mdmCcResponseMode.setStatus("mandatory")


class _MdmCcResultCodeOptions_Type(Integer32):
    """Custom type mdmCcResultCodeOptions based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_MdmCcResultCodeOptions_Type.__name__ = "Integer32"
_MdmCcResultCodeOptions_Object = MibTableColumn
mdmCcResultCodeOptions = _MdmCcResultCodeOptions_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 6, 7, 1, 1, 10),
    _MdmCcResultCodeOptions_Type()
)
mdmCcResultCodeOptions.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mdmCcResultCodeOptions.setStatus("mandatory")


class _MdmCcArqResultCodeMode_Type(Integer32):
    """Custom type mdmCcArqResultCodeMode based on Integer32"""
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
        *(("arqResultsDisabled", 1),
          ("arqResultsEnabled", 2),
          ("includeHstV32", 3),
          ("includeProtocol", 4))
    )


_MdmCcArqResultCodeMode_Type.__name__ = "Integer32"
_MdmCcArqResultCodeMode_Object = MibTableColumn
mdmCcArqResultCodeMode = _MdmCcArqResultCodeMode_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 6, 7, 1, 1, 11),
    _MdmCcArqResultCodeMode_Type()
)
mdmCcArqResultCodeMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mdmCcArqResultCodeMode.setStatus("mandatory")


class _MdmCcEscCodeRsp_Type(Integer32):
    """Custom type mdmCcEscCodeRsp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("enterCommandMode", 2),
          ("goOnHook", 1),
          ("ignoreEscCode", 3))
    )


_MdmCcEscCodeRsp_Type.__name__ = "Integer32"
_MdmCcEscCodeRsp_Object = MibTableColumn
mdmCcEscCodeRsp = _MdmCcEscCodeRsp_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 6, 7, 1, 1, 12),
    _MdmCcEscCodeRsp_Type()
)
mdmCcEscCodeRsp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mdmCcEscCodeRsp.setStatus("mandatory")


class _MdmCcAtRecognition_Type(Integer32):
    """Custom type mdmCcAtRecognition based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("enableAll", 3),
          ("ignore", 1),
          ("queryOnly", 2))
    )


_MdmCcAtRecognition_Type.__name__ = "Integer32"
_MdmCcAtRecognition_Object = MibTableColumn
mdmCcAtRecognition = _MdmCcAtRecognition_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 6, 7, 1, 1, 13),
    _MdmCcAtRecognition_Type()
)
mdmCcAtRecognition.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mdmCcAtRecognition.setStatus("mandatory")


class _MdmCcMgmtSysMsgDis_Type(Integer32):
    """Custom type mdmCcMgmtSysMsgDis based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_MdmCcMgmtSysMsgDis_Type.__name__ = "Integer32"
_MdmCcMgmtSysMsgDis_Object = MibTableColumn
mdmCcMgmtSysMsgDis = _MdmCcMgmtSysMsgDis_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 6, 7, 1, 1, 14),
    _MdmCcMgmtSysMsgDis_Type()
)
mdmCcMgmtSysMsgDis.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mdmCcMgmtSysMsgDis.setStatus("mandatory")


class _MdmCcV32ToneDuration_Type(Integer32):
    """Custom type mdmCcV32ToneDuration based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_MdmCcV32ToneDuration_Type.__name__ = "Integer32"
_MdmCcV32ToneDuration_Object = MibTableColumn
mdmCcV32ToneDuration = _MdmCcV32ToneDuration_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 6, 7, 1, 1, 15),
    _MdmCcV32ToneDuration_Type()
)
mdmCcV32ToneDuration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mdmCcV32ToneDuration.setStatus("mandatory")


class _MdmCcAutoAnswer_Type(Integer32):
    """Custom type mdmCcAutoAnswer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_MdmCcAutoAnswer_Type.__name__ = "Integer32"
_MdmCcAutoAnswer_Object = MibTableColumn
mdmCcAutoAnswer = _MdmCcAutoAnswer_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 6, 7, 1, 1, 17),
    _MdmCcAutoAnswer_Type()
)
mdmCcAutoAnswer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mdmCcAutoAnswer.setStatus("mandatory")


class _MdmCcAnswerInOrigMode_Type(Integer32):
    """Custom type mdmCcAnswerInOrigMode based on Integer32"""
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


_MdmCcAnswerInOrigMode_Type.__name__ = "Integer32"
_MdmCcAnswerInOrigMode_Object = MibTableColumn
mdmCcAnswerInOrigMode = _MdmCcAnswerInOrigMode_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 6, 7, 1, 1, 18),
    _MdmCcAnswerInOrigMode_Type()
)
mdmCcAnswerInOrigMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mdmCcAnswerInOrigMode.setStatus("mandatory")


class _MdmCcArqBufWait_Type(Integer32):
    """Custom type mdmCcArqBufWait based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_MdmCcArqBufWait_Type.__name__ = "Integer32"
_MdmCcArqBufWait_Object = MibTableColumn
mdmCcArqBufWait = _MdmCcArqBufWait_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 6, 7, 1, 1, 19),
    _MdmCcArqBufWait_Type()
)
mdmCcArqBufWait.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mdmCcArqBufWait.setStatus("mandatory")


class _MdmCcPhoneString0_Type(DisplayString):
    """Custom type mdmCcPhoneString0 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 36),
    )


_MdmCcPhoneString0_Type.__name__ = "DisplayString"
_MdmCcPhoneString0_Object = MibTableColumn
mdmCcPhoneString0 = _MdmCcPhoneString0_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 6, 7, 1, 1, 20),
    _MdmCcPhoneString0_Type()
)
mdmCcPhoneString0.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mdmCcPhoneString0.setStatus("mandatory")


class _MdmCcPhoneString1_Type(DisplayString):
    """Custom type mdmCcPhoneString1 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 36),
    )


_MdmCcPhoneString1_Type.__name__ = "DisplayString"
_MdmCcPhoneString1_Object = MibTableColumn
mdmCcPhoneString1 = _MdmCcPhoneString1_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 6, 7, 1, 1, 21),
    _MdmCcPhoneString1_Type()
)
mdmCcPhoneString1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mdmCcPhoneString1.setStatus("mandatory")


class _MdmCcPhoneString2_Type(DisplayString):
    """Custom type mdmCcPhoneString2 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 36),
    )


_MdmCcPhoneString2_Type.__name__ = "DisplayString"
_MdmCcPhoneString2_Object = MibTableColumn
mdmCcPhoneString2 = _MdmCcPhoneString2_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 6, 7, 1, 1, 22),
    _MdmCcPhoneString2_Type()
)
mdmCcPhoneString2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mdmCcPhoneString2.setStatus("mandatory")


class _MdmCcPhoneString3_Type(DisplayString):
    """Custom type mdmCcPhoneString3 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 36),
    )


_MdmCcPhoneString3_Type.__name__ = "DisplayString"
_MdmCcPhoneString3_Object = MibTableColumn
mdmCcPhoneString3 = _MdmCcPhoneString3_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 6, 7, 1, 1, 23),
    _MdmCcPhoneString3_Type()
)
mdmCcPhoneString3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mdmCcPhoneString3.setStatus("mandatory")


class _MdmCcErrorCntlMode_Type(Integer32):
    """Custom type mdmCcErrorCntlMode based on Integer32"""
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
        *(("arqOnly", 4),
          ("none", 1),
          ("normalArq", 3),
          ("syncMode", 2),
          ("v25bisBit", 6),
          ("v25bisChar", 5))
    )


_MdmCcErrorCntlMode_Type.__name__ = "Integer32"
_MdmCcErrorCntlMode_Object = MibTableColumn
mdmCcErrorCntlMode = _MdmCcErrorCntlMode_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 6, 7, 1, 1, 24),
    _MdmCcErrorCntlMode_Type()
)
mdmCcErrorCntlMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mdmCcErrorCntlMode.setStatus("mandatory")


class _MdmCcMiMic_Type(Integer32):
    """Custom type mdmCcMiMic based on Integer32"""
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


_MdmCcMiMic_Type.__name__ = "Integer32"
_MdmCcMiMic_Object = MibTableColumn
mdmCcMiMic = _MdmCcMiMic_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 6, 7, 1, 1, 25),
    _MdmCcMiMic_Type()
)
mdmCcMiMic.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mdmCcMiMic.setStatus("mandatory")


class _MdmCcMnpWith1200_Type(Integer32):
    """Custom type mdmCcMnpWith1200 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_MdmCcMnpWith1200_Type.__name__ = "Integer32"
_MdmCcMnpWith1200_Object = MibTableColumn
mdmCcMnpWith1200 = _MdmCcMnpWith1200_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 6, 7, 1, 1, 26),
    _MdmCcMnpWith1200_Type()
)
mdmCcMnpWith1200.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mdmCcMnpWith1200.setStatus("mandatory")


class _MdmCcMnpWith2400_Type(Integer32):
    """Custom type mdmCcMnpWith2400 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_MdmCcMnpWith2400_Type.__name__ = "Integer32"
_MdmCcMnpWith2400_Object = MibTableColumn
mdmCcMnpWith2400 = _MdmCcMnpWith2400_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 6, 7, 1, 1, 27),
    _MdmCcMnpWith2400_Type()
)
mdmCcMnpWith2400.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mdmCcMnpWith2400.setStatus("mandatory")


class _MdmCcMnpWithV32_Type(Integer32):
    """Custom type mdmCcMnpWithV32 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_MdmCcMnpWithV32_Type.__name__ = "Integer32"
_MdmCcMnpWithV32_Object = MibTableColumn
mdmCcMnpWithV32 = _MdmCcMnpWithV32_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 6, 7, 1, 1, 28),
    _MdmCcMnpWithV32_Type()
)
mdmCcMnpWithV32.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mdmCcMnpWithV32.setStatus("mandatory")


class _MdmCcMnpTimeout_Type(Integer32):
    """Custom type mdmCcMnpTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 14),
    )


_MdmCcMnpTimeout_Type.__name__ = "Integer32"
_MdmCcMnpTimeout_Object = MibTableColumn
mdmCcMnpTimeout = _MdmCcMnpTimeout_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 6, 7, 1, 1, 29),
    _MdmCcMnpTimeout_Type()
)
mdmCcMnpTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mdmCcMnpTimeout.setStatus("mandatory")


class _MdmCcV21V23FallBackTimer_Type(Integer32):
    """Custom type mdmCcV21V23FallBackTimer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_MdmCcV21V23FallBackTimer_Type.__name__ = "Integer32"
_MdmCcV21V23FallBackTimer_Object = MibTableColumn
mdmCcV21V23FallBackTimer = _MdmCcV21V23FallBackTimer_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 6, 7, 1, 1, 30),
    _MdmCcV21V23FallBackTimer_Type()
)
mdmCcV21V23FallBackTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mdmCcV21V23FallBackTimer.setStatus("mandatory")


class _MdmCcAddnlAnswToneDur_Type(Integer32):
    """Custom type mdmCcAddnlAnswToneDur based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_MdmCcAddnlAnswToneDur_Type.__name__ = "Integer32"
_MdmCcAddnlAnswToneDur_Object = MibTableColumn
mdmCcAddnlAnswToneDur = _MdmCcAddnlAnswToneDur_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 6, 7, 1, 1, 31),
    _MdmCcAddnlAnswToneDur_Type()
)
mdmCcAddnlAnswToneDur.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mdmCcAddnlAnswToneDur.setStatus("optional")


class _MdmCcBillingDelayPeriod_Type(Integer32):
    """Custom type mdmCcBillingDelayPeriod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_MdmCcBillingDelayPeriod_Type.__name__ = "Integer32"
_MdmCcBillingDelayPeriod_Object = MibTableColumn
mdmCcBillingDelayPeriod = _MdmCcBillingDelayPeriod_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 6, 7, 1, 1, 32),
    _MdmCcBillingDelayPeriod_Type()
)
mdmCcBillingDelayPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mdmCcBillingDelayPeriod.setStatus("optional")


class _MdmCcCarrierAccessCode1_Type(DisplayString):
    """Custom type mdmCcCarrierAccessCode1 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_MdmCcCarrierAccessCode1_Type.__name__ = "DisplayString"
_MdmCcCarrierAccessCode1_Object = MibTableColumn
mdmCcCarrierAccessCode1 = _MdmCcCarrierAccessCode1_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 6, 7, 1, 1, 33),
    _MdmCcCarrierAccessCode1_Type()
)
mdmCcCarrierAccessCode1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mdmCcCarrierAccessCode1.setStatus("optional")


class _MdmCcCarrierAccessCode2_Type(DisplayString):
    """Custom type mdmCcCarrierAccessCode2 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_MdmCcCarrierAccessCode2_Type.__name__ = "DisplayString"
_MdmCcCarrierAccessCode2_Object = MibTableColumn
mdmCcCarrierAccessCode2 = _MdmCcCarrierAccessCode2_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 6, 7, 1, 1, 34),
    _MdmCcCarrierAccessCode2_Type()
)
mdmCcCarrierAccessCode2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mdmCcCarrierAccessCode2.setStatus("optional")


class _MdmCcCarrierAccessCode3_Type(DisplayString):
    """Custom type mdmCcCarrierAccessCode3 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_MdmCcCarrierAccessCode3_Type.__name__ = "DisplayString"
_MdmCcCarrierAccessCode3_Object = MibTableColumn
mdmCcCarrierAccessCode3 = _MdmCcCarrierAccessCode3_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 6, 7, 1, 1, 35),
    _MdmCcCarrierAccessCode3_Type()
)
mdmCcCarrierAccessCode3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mdmCcCarrierAccessCode3.setStatus("optional")


class _MdmCcCallingInitStr1_Type(DisplayString):
    """Custom type mdmCcCallingInitStr1 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_MdmCcCallingInitStr1_Type.__name__ = "DisplayString"
_MdmCcCallingInitStr1_Object = MibTableColumn
mdmCcCallingInitStr1 = _MdmCcCallingInitStr1_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 6, 7, 1, 1, 36),
    _MdmCcCallingInitStr1_Type()
)
mdmCcCallingInitStr1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mdmCcCallingInitStr1.setStatus("optional")


class _MdmCcCallingInitStr2_Type(DisplayString):
    """Custom type mdmCcCallingInitStr2 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_MdmCcCallingInitStr2_Type.__name__ = "DisplayString"
_MdmCcCallingInitStr2_Object = MibTableColumn
mdmCcCallingInitStr2 = _MdmCcCallingInitStr2_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 6, 7, 1, 1, 37),
    _MdmCcCallingInitStr2_Type()
)
mdmCcCallingInitStr2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mdmCcCallingInitStr2.setStatus("optional")


class _MdmCcCallingInitStr3_Type(DisplayString):
    """Custom type mdmCcCallingInitStr3 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_MdmCcCallingInitStr3_Type.__name__ = "DisplayString"
_MdmCcCallingInitStr3_Object = MibTableColumn
mdmCcCallingInitStr3 = _MdmCcCallingInitStr3_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 6, 7, 1, 1, 38),
    _MdmCcCallingInitStr3_Type()
)
mdmCcCallingInitStr3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mdmCcCallingInitStr3.setStatus("optional")


class _MdmCcCallingInitStr4_Type(DisplayString):
    """Custom type mdmCcCallingInitStr4 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_MdmCcCallingInitStr4_Type.__name__ = "DisplayString"
_MdmCcCallingInitStr4_Object = MibTableColumn
mdmCcCallingInitStr4 = _MdmCcCallingInitStr4_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 6, 7, 1, 1, 39),
    _MdmCcCallingInitStr4_Type()
)
mdmCcCallingInitStr4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mdmCcCallingInitStr4.setStatus("optional")


class _MdmCcDataFaxMode_Type(Integer32):
    """Custom type mdmCcDataFaxMode based on Integer32"""
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
        *(("dataFaxClass1Mode", 3),
          ("dataFaxClass2Mode", 5),
          ("dataMode", 1),
          ("faxClass1Mode", 2),
          ("faxClass2Mode", 4))
    )


_MdmCcDataFaxMode_Type.__name__ = "Integer32"
_MdmCcDataFaxMode_Object = MibTableColumn
mdmCcDataFaxMode = _MdmCcDataFaxMode_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 6, 7, 1, 1, 40),
    _MdmCcDataFaxMode_Type()
)
mdmCcDataFaxMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mdmCcDataFaxMode.setStatus("mandatory")


class _MdmCcT1CallSetupProc_Type(Integer32):
    """Custom type mdmCcT1CallSetupProc based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noSetup", 2),
          ("normalSetup", 1))
    )


_MdmCcT1CallSetupProc_Type.__name__ = "Integer32"
_MdmCcT1CallSetupProc_Object = MibTableColumn
mdmCcT1CallSetupProc = _MdmCcT1CallSetupProc_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 6, 7, 1, 1, 41),
    _MdmCcT1CallSetupProc_Type()
)
mdmCcT1CallSetupProc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mdmCcT1CallSetupProc.setStatus("optional")


class _MdmCcT1DialToneType_Type(Integer32):
    """Custom type mdmCcT1DialToneType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dtmfTones", 2),
          ("mfTones", 1))
    )


_MdmCcT1DialToneType_Type.__name__ = "Integer32"
_MdmCcT1DialToneType_Object = MibTableColumn
mdmCcT1DialToneType = _MdmCcT1DialToneType_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 6, 7, 1, 1, 42),
    _MdmCcT1DialToneType_Type()
)
mdmCcT1DialToneType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mdmCcT1DialToneType.setStatus("optional")


class _MdmCcT1KpStMfTones_Type(Integer32):
    """Custom type mdmCcT1KpStMfTones based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_MdmCcT1KpStMfTones_Type.__name__ = "Integer32"
_MdmCcT1KpStMfTones_Object = MibTableColumn
mdmCcT1KpStMfTones = _MdmCcT1KpStMfTones_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 6, 7, 1, 1, 43),
    _MdmCcT1KpStMfTones_Type()
)
mdmCcT1KpStMfTones.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mdmCcT1KpStMfTones.setStatus("optional")


class _MdmCcT1CallInitStrUse_Type(Integer32):
    """Custom type mdmCcT1CallInitStrUse based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_MdmCcT1CallInitStrUse_Type.__name__ = "Integer32"
_MdmCcT1CallInitStrUse_Object = MibTableColumn
mdmCcT1CallInitStrUse = _MdmCcT1CallInitStrUse_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 6, 7, 1, 1, 44),
    _MdmCcT1CallInitStrUse_Type()
)
mdmCcT1CallInitStrUse.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mdmCcT1CallInitStrUse.setStatus("optional")


class _MdmCcT1CallInitStrBase_Type(Integer32):
    """Custom type mdmCcT1CallInitStrBase based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("aniBase", 2),
          ("dnisBase", 1))
    )


_MdmCcT1CallInitStrBase_Type.__name__ = "Integer32"
_MdmCcT1CallInitStrBase_Object = MibTableColumn
mdmCcT1CallInitStrBase = _MdmCcT1CallInitStrBase_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 6, 7, 1, 1, 45),
    _MdmCcT1CallInitStrBase_Type()
)
mdmCcT1CallInitStrBase.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mdmCcT1CallInitStrBase.setStatus("optional")


class _MdmCcIntBlackListDis_Type(Integer32):
    """Custom type mdmCcIntBlackListDis based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_MdmCcIntBlackListDis_Type.__name__ = "Integer32"
_MdmCcIntBlackListDis_Object = MibTableColumn
mdmCcIntBlackListDis = _MdmCcIntBlackListDis_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 6, 7, 1, 1, 46),
    _MdmCcIntBlackListDis_Type()
)
mdmCcIntBlackListDis.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mdmCcIntBlackListDis.setStatus("mandatory")


class _MdmCcOffHookRestrict_Type(Integer32):
    """Custom type mdmCcOffHookRestrict based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_MdmCcOffHookRestrict_Type.__name__ = "Integer32"
_MdmCcOffHookRestrict_Object = MibTableColumn
mdmCcOffHookRestrict = _MdmCcOffHookRestrict_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 6, 7, 1, 1, 47),
    _MdmCcOffHookRestrict_Type()
)
mdmCcOffHookRestrict.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mdmCcOffHookRestrict.setStatus("mandatory")


class _MdmCcT1DialInAniDig_Type(Integer32):
    """Custom type mdmCcT1DialInAniDig based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 12),
    )


_MdmCcT1DialInAniDig_Type.__name__ = "Integer32"
_MdmCcT1DialInAniDig_Object = MibTableColumn
mdmCcT1DialInAniDig = _MdmCcT1DialInAniDig_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 6, 7, 1, 1, 48),
    _MdmCcT1DialInAniDig_Type()
)
mdmCcT1DialInAniDig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mdmCcT1DialInAniDig.setStatus("optional")


class _MdmCcT1DialInDnisDig_Type(Integer32):
    """Custom type mdmCcT1DialInDnisDig based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 12),
    )


_MdmCcT1DialInDnisDig_Type.__name__ = "Integer32"
_MdmCcT1DialInDnisDig_Object = MibTableColumn
mdmCcT1DialInDnisDig = _MdmCcT1DialInDnisDig_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 6, 7, 1, 1, 49),
    _MdmCcT1DialInDnisDig_Type()
)
mdmCcT1DialInDnisDig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mdmCcT1DialInDnisDig.setStatus("optional")


class _MdmCcNoPbNoConnEna_Type(Integer32):
    """Custom type mdmCcNoPbNoConnEna based on Integer32"""
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


_MdmCcNoPbNoConnEna_Type.__name__ = "Integer32"
_MdmCcNoPbNoConnEna_Object = MibTableColumn
mdmCcNoPbNoConnEna = _MdmCcNoPbNoConnEna_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 6, 7, 1, 1, 50),
    _MdmCcNoPbNoConnEna_Type()
)
mdmCcNoPbNoConnEna.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mdmCcNoPbNoConnEna.setStatus("optional")


class _MdmCcIdleDiscPatt_Type(Integer32):
    """Custom type mdmCcIdleDiscPatt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_MdmCcIdleDiscPatt_Type.__name__ = "Integer32"
_MdmCcIdleDiscPatt_Object = MibTableColumn
mdmCcIdleDiscPatt = _MdmCcIdleDiscPatt_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 6, 7, 1, 1, 51),
    _MdmCcIdleDiscPatt_Type()
)
mdmCcIdleDiscPatt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mdmCcIdleDiscPatt.setStatus("optional")


class _MdmCcMnp10_Type(Integer32):
    """Custom type mdmCcMnp10 based on Integer32"""
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


_MdmCcMnp10_Type.__name__ = "Integer32"
_MdmCcMnp10_Object = MibTableColumn
mdmCcMnp10 = _MdmCcMnp10_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 6, 7, 1, 1, 52),
    _MdmCcMnp10_Type()
)
mdmCcMnp10.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mdmCcMnp10.setStatus("optional")


class _MdmCcMnp10Ec_Type(Integer32):
    """Custom type mdmCcMnp10Ec based on Integer32"""
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


_MdmCcMnp10Ec_Type.__name__ = "Integer32"
_MdmCcMnp10Ec_Object = MibTableColumn
mdmCcMnp10Ec = _MdmCcMnp10Ec_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 6, 7, 1, 1, 53),
    _MdmCcMnp10Ec_Type()
)
mdmCcMnp10Ec.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mdmCcMnp10Ec.setStatus("optional")


class _MdmCcAtzPbHandling_Type(Integer32):
    """Custom type mdmCcAtzPbHandling based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("atzPbIgnored", 2),
          ("atzPbNvram", 3),
          ("normalAtz", 1))
    )


_MdmCcAtzPbHandling_Type.__name__ = "Integer32"
_MdmCcAtzPbHandling_Object = MibTableColumn
mdmCcAtzPbHandling = _MdmCcAtzPbHandling_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 6, 7, 1, 1, 54),
    _MdmCcAtzPbHandling_Type()
)
mdmCcAtzPbHandling.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mdmCcAtzPbHandling.setStatus("optional")


class _MdmCcDefltPRISlot_Type(Integer32):
    """Custom type mdmCcDefltPRISlot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5),
    )


_MdmCcDefltPRISlot_Type.__name__ = "Integer32"
_MdmCcDefltPRISlot_Object = MibTableColumn
mdmCcDefltPRISlot = _MdmCcDefltPRISlot_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 6, 7, 1, 1, 55),
    _MdmCcDefltPRISlot_Type()
)
mdmCcDefltPRISlot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mdmCcDefltPRISlot.setStatus("mandatory")


class _MdmCcExtDTMFToneSupport_Type(Integer32):
    """Custom type mdmCcExtDTMFToneSupport based on Integer32"""
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


_MdmCcExtDTMFToneSupport_Type.__name__ = "Integer32"
_MdmCcExtDTMFToneSupport_Object = MibTableColumn
mdmCcExtDTMFToneSupport = _MdmCcExtDTMFToneSupport_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 6, 7, 1, 1, 56),
    _MdmCcExtDTMFToneSupport_Type()
)
mdmCcExtDTMFToneSupport.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mdmCcExtDTMFToneSupport.setStatus("mandatory")


class _MdmCcDataOverVoice_Type(Integer32):
    """Custom type mdmCcDataOverVoice based on Integer32"""
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


_MdmCcDataOverVoice_Type.__name__ = "Integer32"
_MdmCcDataOverVoice_Object = MibTableColumn
mdmCcDataOverVoice = _MdmCcDataOverVoice_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 6, 7, 1, 1, 57),
    _MdmCcDataOverVoice_Type()
)
mdmCcDataOverVoice.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mdmCcDataOverVoice.setStatus("mandatory")


class _MdmCc2100AnswerTone_Type(Integer32):
    """Custom type mdmCc2100AnswerTone based on Integer32"""
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


_MdmCc2100AnswerTone_Type.__name__ = "Integer32"
_MdmCc2100AnswerTone_Object = MibTableColumn
mdmCc2100AnswerTone = _MdmCc2100AnswerTone_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 6, 7, 1, 1, 58),
    _MdmCc2100AnswerTone_Type()
)
mdmCc2100AnswerTone.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mdmCc2100AnswerTone.setStatus("mandatory")


class _MdmCcEnableV120v42Bis_Type(Integer32):
    """Custom type mdmCcEnableV120v42Bis based on Integer32"""
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


_MdmCcEnableV120v42Bis_Type.__name__ = "Integer32"
_MdmCcEnableV120v42Bis_Object = MibTableColumn
mdmCcEnableV120v42Bis = _MdmCcEnableV120v42Bis_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 6, 7, 1, 1, 59),
    _MdmCcEnableV120v42Bis_Type()
)
mdmCcEnableV120v42Bis.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mdmCcEnableV120v42Bis.setStatus("mandatory")


class _MdmCcHdlcLicIe_Type(Integer32):
    """Custom type mdmCcHdlcLicIe based on Integer32"""
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


_MdmCcHdlcLicIe_Type.__name__ = "Integer32"
_MdmCcHdlcLicIe_Object = MibTableColumn
mdmCcHdlcLicIe = _MdmCcHdlcLicIe_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 6, 7, 1, 1, 60),
    _MdmCcHdlcLicIe_Type()
)
mdmCcHdlcLicIe.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mdmCcHdlcLicIe.setStatus("mandatory")


class _MdmCcDtmfTerminationTone_Type(Integer32):
    """Custom type mdmCcDtmfTerminationTone based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16),
    )


_MdmCcDtmfTerminationTone_Type.__name__ = "Integer32"
_MdmCcDtmfTerminationTone_Object = MibTableColumn
mdmCcDtmfTerminationTone = _MdmCcDtmfTerminationTone_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 6, 7, 1, 1, 61),
    _MdmCcDtmfTerminationTone_Type()
)
mdmCcDtmfTerminationTone.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mdmCcDtmfTerminationTone.setStatus("mandatory")


class _MdmCcAfaxMaxRateSrvOpt20_Type(Integer32):
    """Custom type mdmCcAfaxMaxRateSrvOpt20 based on Integer32"""
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
        *(("bps12000", 5),
          ("bps14400", 6),
          ("bps2400", 1),
          ("bps4800", 2),
          ("bps7200", 3),
          ("bps9600", 4))
    )


_MdmCcAfaxMaxRateSrvOpt20_Type.__name__ = "Integer32"
_MdmCcAfaxMaxRateSrvOpt20_Object = MibTableColumn
mdmCcAfaxMaxRateSrvOpt20 = _MdmCcAfaxMaxRateSrvOpt20_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 6, 7, 1, 1, 62),
    _MdmCcAfaxMaxRateSrvOpt20_Type()
)
mdmCcAfaxMaxRateSrvOpt20.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mdmCcAfaxMaxRateSrvOpt20.setStatus("mandatory")


class _MdmCcAfaxMaxRateSrvOpt21_Type(Integer32):
    """Custom type mdmCcAfaxMaxRateSrvOpt21 based on Integer32"""
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
        *(("bps12000", 5),
          ("bps14400", 6),
          ("bps2400", 1),
          ("bps4800", 2),
          ("bps7200", 3),
          ("bps9600", 4))
    )


_MdmCcAfaxMaxRateSrvOpt21_Type.__name__ = "Integer32"
_MdmCcAfaxMaxRateSrvOpt21_Object = MibTableColumn
mdmCcAfaxMaxRateSrvOpt21 = _MdmCcAfaxMaxRateSrvOpt21_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 6, 7, 1, 1, 63),
    _MdmCcAfaxMaxRateSrvOpt21_Type()
)
mdmCcAfaxMaxRateSrvOpt21.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mdmCcAfaxMaxRateSrvOpt21.setStatus("mandatory")
_MdmEc_ObjectIdentity = ObjectIdentity
mdmEc = _MdmEc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 429, 1, 6, 8)
)
_MdmEcTable_Object = MibTable
mdmEcTable = _MdmEcTable_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 6, 8, 1)
)
if mibBuilder.loadTexts:
    mdmEcTable.setStatus("mandatory")
_MdmEcEntry_Object = MibTableRow
mdmEcEntry = _MdmEcEntry_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 6, 8, 1, 1)
)
mdmEcEntry.setIndexNames(
    (0, "MDM-MIB", "mdmEcIndex"),
)
if mibBuilder.loadTexts:
    mdmEcEntry.setStatus("mandatory")
_MdmEcIndex_Type = Integer32
_MdmEcIndex_Object = MibTableColumn
mdmEcIndex = _MdmEcIndex_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 6, 8, 1, 1, 1),
    _MdmEcIndex_Type()
)
mdmEcIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mdmEcIndex.setStatus("mandatory")


class _MdmEcMnp3Dis_Type(Integer32):
    """Custom type mdmEcMnp3Dis based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_MdmEcMnp3Dis_Type.__name__ = "Integer32"
_MdmEcMnp3Dis_Object = MibTableColumn
mdmEcMnp3Dis = _MdmEcMnp3Dis_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 6, 8, 1, 1, 2),
    _MdmEcMnp3Dis_Type()
)
mdmEcMnp3Dis.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mdmEcMnp3Dis.setStatus("mandatory")


class _MdmEcMnp4Dis_Type(Integer32):
    """Custom type mdmEcMnp4Dis based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_MdmEcMnp4Dis_Type.__name__ = "Integer32"
_MdmEcMnp4Dis_Object = MibTableColumn
mdmEcMnp4Dis = _MdmEcMnp4Dis_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 6, 8, 1, 1, 3),
    _MdmEcMnp4Dis_Type()
)
mdmEcMnp4Dis.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mdmEcMnp4Dis.setStatus("mandatory")


class _MdmEcMnpUnusual_Type(Integer32):
    """Custom type mdmEcMnpUnusual based on Integer32"""
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


_MdmEcMnpUnusual_Type.__name__ = "Integer32"
_MdmEcMnpUnusual_Object = MibTableColumn
mdmEcMnpUnusual = _MdmEcMnpUnusual_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 6, 8, 1, 1, 4),
    _MdmEcMnpUnusual_Type()
)
mdmEcMnpUnusual.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mdmEcMnpUnusual.setStatus("mandatory")


class _MdmEcV42MnpHandshake_Type(Integer32):
    """Custom type mdmEcV42MnpHandshake based on Integer32"""
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
        *(("disableDetectionPhase", 4),
          ("disablev42enablemnp", 3),
          ("enableAll", 1),
          ("enableV42disableMnp", 2))
    )


_MdmEcV42MnpHandshake_Type.__name__ = "Integer32"
_MdmEcV42MnpHandshake_Object = MibTableColumn
mdmEcV42MnpHandshake = _MdmEcV42MnpHandshake_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 6, 8, 1, 1, 5),
    _MdmEcV42MnpHandshake_Type()
)
mdmEcV42MnpHandshake.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mdmEcV42MnpHandshake.setStatus("mandatory")
_MdmCs_ObjectIdentity = ObjectIdentity
mdmCs = _MdmCs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 429, 1, 6, 9)
)
_MdmCsTable_Object = MibTable
mdmCsTable = _MdmCsTable_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 6, 9, 1)
)
if mibBuilder.loadTexts:
    mdmCsTable.setStatus("mandatory")
_MdmCsEntry_Object = MibTableRow
mdmCsEntry = _MdmCsEntry_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 6, 9, 1, 1)
)
mdmCsEntry.setIndexNames(
    (0, "MDM-MIB", "mdmCsIndex"),
)
if mibBuilder.loadTexts:
    mdmCsEntry.setStatus("mandatory")
_MdmCsIndex_Type = Integer32
_MdmCsIndex_Object = MibTableColumn
mdmCsIndex = _MdmCsIndex_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 6, 9, 1, 1, 1),
    _MdmCsIndex_Type()
)
mdmCsIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mdmCsIndex.setStatus("mandatory")


class _MdmCsStatus_Type(Integer32):
    """Custom type mdmCsStatus based on Integer32"""
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
              33,
              49,
              50,
              51,
              52,
              53,
              54,
              55,
              56,
              57,
              58,
              59,
              60,
              61,
              62)
        )
    )
    namedValues = NamedValues(
        *(("analogLoopback", 52),
          ("dialing", 3),
          ("failed", 33),
          ("idle", 1),
          ("lineBusiedOut", 11),
          ("linkNegotiation", 6),
          ("localCommandMode", 9),
          ("localDigitalLoopback", 53),
          ("miuFailed", 62),
          ("modemDisabled", 59),
          ("nonManagableDevice", 61),
          ("nonManagedDevice", 57),
          ("notResponding", 60),
          ("offHook", 2),
          ("onlineAnswer", 8),
          ("onlineOriginate", 7),
          ("phoneTest", 56),
          ("remoteCommandMode", 10),
          ("remoteDigitalLoopback", 54),
          ("responderTest102", 14),
          ("responderTest105", 13),
          ("ringRcvd", 5),
          ("ringing", 4),
          ("selfTest", 55),
          ("slotEmpty", 58),
          ("testingNvram", 51),
          ("testingRam", 50),
          ("testingRom", 49),
          ("toneTest", 12))
    )


_MdmCsStatus_Type.__name__ = "Integer32"
_MdmCsStatus_Object = MibTableColumn
mdmCsStatus = _MdmCsStatus_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 6, 9, 1, 1, 2),
    _MdmCsStatus_Type()
)
mdmCsStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mdmCsStatus.setStatus("mandatory")


class _MdmCsLastNumberDialedOut_Type(DisplayString):
    """Custom type mdmCsLastNumberDialedOut based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_MdmCsLastNumberDialedOut_Type.__name__ = "DisplayString"
_MdmCsLastNumberDialedOut_Object = MibTableColumn
mdmCsLastNumberDialedOut = _MdmCsLastNumberDialedOut_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 6, 9, 1, 1, 3),
    _MdmCsLastNumberDialedOut_Type()
)
mdmCsLastNumberDialedOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mdmCsLastNumberDialedOut.setStatus("mandatory")


class _MdmCsLastNumberDialedIn_Type(DisplayString):
    """Custom type mdmCsLastNumberDialedIn based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_MdmCsLastNumberDialedIn_Type.__name__ = "DisplayString"
_MdmCsLastNumberDialedIn_Object = MibTableColumn
mdmCsLastNumberDialedIn = _MdmCsLastNumberDialedIn_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 6, 9, 1, 1, 4),
    _MdmCsLastNumberDialedIn_Type()
)
mdmCsLastNumberDialedIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mdmCsLastNumberDialedIn.setStatus("mandatory")


class _MdmCsLastCallingPartyNum_Type(DisplayString):
    """Custom type mdmCsLastCallingPartyNum based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_MdmCsLastCallingPartyNum_Type.__name__ = "DisplayString"
_MdmCsLastCallingPartyNum_Object = MibTableColumn
mdmCsLastCallingPartyNum = _MdmCsLastCallingPartyNum_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 6, 9, 1, 1, 5),
    _MdmCsLastCallingPartyNum_Type()
)
mdmCsLastCallingPartyNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mdmCsLastCallingPartyNum.setStatus("mandatory")


class _MdmCsOriginateAnswer_Type(Integer32):
    """Custom type mdmCsOriginateAnswer based on Integer32"""
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
        *(("answerInAnswer", 4),
          ("answerInOriginate", 3),
          ("originateInAnswer", 2),
          ("originateInOriginate", 1))
    )


_MdmCsOriginateAnswer_Type.__name__ = "Integer32"
_MdmCsOriginateAnswer_Object = MibTableColumn
mdmCsOriginateAnswer = _MdmCsOriginateAnswer_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 6, 9, 1, 1, 6),
    _MdmCsOriginateAnswer_Type()
)
mdmCsOriginateAnswer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mdmCsOriginateAnswer.setStatus("mandatory")
_MdmCsRings_Type = Integer32
_MdmCsRings_Object = MibTableColumn
mdmCsRings = _MdmCsRings_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 6, 9, 1, 1, 7),
    _MdmCsRings_Type()
)
mdmCsRings.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mdmCsRings.setStatus("mandatory")


class _MdmCsDisconnectReason_Type(Integer32):
    """Custom type mdmCsDisconnectReason based on Integer32"""
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
              25,
              26,
              27,
              28,
              29,
              30,
              31,
              32,
              33,
              34,
              35,
              36,
              37,
              38,
              39,
              40,
              41,
              42,
              43,
              44,
              45,
              46,
              47,
              48,
              49,
              50,
              51,
              52,
              53,
              54,
              55,
              56,
              57,
              58,
              59,
              60,
              61,
              62,
              63,
              64,
              65,
              66,
              67,
              68,
              69,
              70,
              71,
              72,
              73,
              74,
              75,
              76,
              77,
              78,
              79,
              80,
              81,
              82,
              83,
              84,
              85,
              86,
              87,
              88,
              89,
              90,
              91,
              92,
              93,
              94,
              95,
              96,
              97,
              98,
              99,
              100,
              101,
              102,
              103,
              104,
              105,
              106,
              107,
              108,
              109,
              110,
              111)
        )
    )
    namedValues = NamedValues(
        *(("abnormalDisconnect", 77),
          ("abortAnlgDstOvrIsdn", 72),
          ("athCommand", 3),
          ("autopassFailed", 45),
          ("bearerIncompatibility", 75),
          ("callBlacklisted", 111),
          ("carrierLoss", 4),
          ("chasAwarenessNotAvailable", 102),
          ("class2FaxHangupCmd", 66),
          ("dataProcessingGenericErr", 99),
          ("dialBackLink", 43),
          ("dialSecurity", 34),
          ("ds0Teardown", 37),
          ("dspHeadPtrInvalid", 98),
          ("dspInterruptTimeout", 64),
          ("dspReboot", 94),
          ("dspTailPtrInvalid", 97),
          ("dtrDrop", 1),
          ("escapeSequence", 2),
          ("gmtTimeNotSet", 101),
          ("hstSpeedSwitchTimeout", 67),
          ("inactivityTimout", 5),
          ("incomingCallBlock", 88),
          ("incomingInvalidBearerCap", 83),
          ("incomingInvalidCalledPty", 87),
          ("incomingInvalidCallingPty", 86),
          ("incomingInvalidChannelID", 84),
          ("incomingInvalidProgInd", 85),
          ("incomingLoopStNoRingOff", 89),
          ("incomingModemNotAvailable", 82),
          ("invalidCauseValue", 78),
          ("invalidSpeed", 13),
          ("keyAbort", 17),
          ("lineBusy", 18),
          ("linkAbort", 44),
          ("linkDisconnectMsgReceived", 11),
          ("linkPassword", 9),
          ("loopLoss", 36),
          ("managementCommand", 15),
          ("mnpIncompatible", 6),
          ("mnpProtocolViolation", 65),
          ("modeIncompatible", 41),
          ("noAnswer", 19),
          ("noAnswerTone", 21),
          ("noCarrier", 22),
          ("noDSPRespToDisc", 96),
          ("noDSPRespToKA", 95),
          ("noDialTone", 16),
          ("noLoopCurrent", 12),
          ("noPromptInNonARQ", 42),
          ("noPromptingInSync", 39),
          ("nonArqMode", 40),
          ("none", 32),
          ("normalUnspecified", 74),
          ("normalUserCallClear", 73),
          ("outgoingEMWinkTimeout", 91),
          ("outgoingEMWinkTooShort", 92),
          ("outgoingNoChannelAvail", 93),
          ("outgoingTelcoDisconnect", 90),
          ("pbAckWaitTimeout", 58),
          ("pbBadFrame", 57),
          ("pbClockMissing", 54),
          ("pbGenericError", 46),
          ("pbLinkErrRxTAL", 52),
          ("pbLinkErrTxPreAck", 47),
          ("pbLinkErrTxTAL", 51),
          ("pbLinkErrTxTardyACK", 48),
          ("pbOutOfSequenceFrame", 56),
          ("pbReceiveBusTimeout", 50),
          ("pbReceiveMsgBufOvrflw", 61),
          ("pbReceiveOvrflwRNRFailed", 60),
          ("pbReceivedAckSequenceErr", 59),
          ("pbReceivedLsWhileLinkUp", 55),
          ("pbTransmitBusTimeout", 49),
          ("pbTransmitMasterTimeout", 53),
          ("priDialoutRqTimeout", 71),
          ("promptNotEnabled", 38),
          ("protocolErrorEvent", 76),
          ("r2ChannelBlockedByNetwork", 104),
          ("r2DNISNotFound", 107),
          ("r2DSPFatalError", 110),
          ("r2Glare", 105),
          ("r2InvalidChannelDirection", 103),
          ("r2OutgoingCallBlocked", 106),
          ("r2SigCauseCongestion", 108),
          ("r2SigCauseUnallocNumber", 109),
          ("rcvdGatewayDiscCmd", 62),
          ("remotHungUpDuringTraining", 80),
          ("remoteAccessDenied", 35),
          ("remotePassword", 8),
          ("resourceUnavailable", 79),
          ("retransmitLimit", 10),
          ("t1Glare", 70),
          ("timerExpired", 69),
          ("timeslotUnavailable", 100),
          ("tokenPassingTimeout", 63),
          ("tooManyUnacked", 68),
          ("trainingTimeout", 81),
          ("unableToRetrain", 14),
          ("undefined", 7),
          ("undetermined", 23),
          ("v32Cleardown", 33),
          ("v42BadSetup", 28),
          ("v42BreakTimeout", 25),
          ("v42DisconnectCmd", 26),
          ("v42IdExchangeFail", 27),
          ("v42InvalidCodeWord", 29),
          ("v42InvalidCommand", 31),
          ("v42SabmeTimeout", 24),
          ("v42StringToLong", 30),
          ("voice", 20))
    )


_MdmCsDisconnectReason_Type.__name__ = "Integer32"
_MdmCsDisconnectReason_Object = MibTableColumn
mdmCsDisconnectReason = _MdmCsDisconnectReason_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 6, 9, 1, 1, 8),
    _MdmCsDisconnectReason_Type()
)
mdmCsDisconnectReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mdmCsDisconnectReason.setStatus("mandatory")


class _MdmCsConnectFailReason_Type(Integer32):
    """Custom type mdmCsConnectFailReason based on Integer32"""
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
              25,
              26,
              27,
              28,
              29,
              30,
              31,
              32,
              33,
              34,
              35,
              36,
              37,
              38,
              39,
              40,
              41,
              42,
              43,
              44,
              45,
              46,
              47,
              48,
              49,
              50,
              51,
              52,
              53,
              54,
              55,
              56,
              57,
              58,
              59,
              60,
              61,
              62,
              63,
              64,
              65,
              66,
              67,
              68,
              69,
              70,
              71,
              72,
              73,
              74,
              75,
              76,
              77,
              78,
              79,
              80,
              81,
              82,
              83,
              84,
              85,
              86,
              87,
              88,
              89,
              90,
              91,
              92,
              93,
              94,
              95,
              96,
              97,
              98,
              99,
              100,
              101,
              102,
              103,
              104,
              105,
              106,
              107,
              108,
              109,
              110,
              111)
        )
    )
    namedValues = NamedValues(
        *(("abnormalDisconnect", 77),
          ("abortAnlgDstOvrIsdn", 72),
          ("athCommand", 3),
          ("autopassFailed", 45),
          ("bearerIncompatibility", 75),
          ("callBlacklisted", 111),
          ("carrierLoss", 4),
          ("chasAwarenessNotAvailable", 102),
          ("class2FaxHangupCmd", 66),
          ("dataProcessingGenericErr", 99),
          ("dialBackLink", 43),
          ("dialSecurity", 34),
          ("ds0Teardown", 37),
          ("dspHeadPtrInvalid", 98),
          ("dspInterruptTimeout", 64),
          ("dspReboot", 94),
          ("dspTailPtrInvalid", 97),
          ("dtrDrop", 1),
          ("escapeSequence", 2),
          ("gmtTimeNotSet", 101),
          ("hstSpeedSwitchTimeout", 67),
          ("inactivityTimout", 5),
          ("incomingCallBlock", 88),
          ("incomingInvalidBearerCap", 83),
          ("incomingInvalidCalledPty", 87),
          ("incomingInvalidCallingPty", 86),
          ("incomingInvalidChannelID", 84),
          ("incomingInvalidProgInd", 85),
          ("incomingLoopStNoRingOff", 89),
          ("incomingModemNotAvailable", 82),
          ("invalidCauseValue", 78),
          ("invalidSpeed", 13),
          ("keyAbort", 17),
          ("lineBusy", 18),
          ("linkAbort", 44),
          ("linkDisconnectMsgReceived", 11),
          ("linkPassword", 9),
          ("loopLoss", 36),
          ("managementCommand", 15),
          ("mnpIncompatible", 6),
          ("mnpProtocolViolation", 65),
          ("modeIncompatible", 41),
          ("noAnswer", 19),
          ("noAnswerTone", 21),
          ("noCarrier", 22),
          ("noDSPRespToDisc", 96),
          ("noDSPRespToKA", 95),
          ("noDialTone", 16),
          ("noLoopCurrent", 12),
          ("noPromptInNonARQ", 42),
          ("noPromptingInSync", 39),
          ("nonArqMode", 40),
          ("none", 32),
          ("normalUnspecified", 74),
          ("normalUserCallClear", 73),
          ("outgoingEMWinkTimeout", 91),
          ("outgoingEMWinkTooShort", 92),
          ("outgoingNoChannelAvail", 93),
          ("outgoingTelcoDisconnect", 90),
          ("pbAckWaitTimeout", 58),
          ("pbBadFrame", 57),
          ("pbClockMissing", 54),
          ("pbGenericError", 46),
          ("pbLinkErrRxTAL", 52),
          ("pbLinkErrTxPreAck", 47),
          ("pbLinkErrTxTAL", 51),
          ("pbLinkErrTxTardyACK", 48),
          ("pbOutOfSequenceFrame", 56),
          ("pbReceiveBusTimeout", 50),
          ("pbReceiveMsgBufOvrflw", 61),
          ("pbReceiveOvrflwRNRFailed", 60),
          ("pbReceivedAckSequenceErr", 59),
          ("pbReceivedLsWhileLinkUp", 55),
          ("pbTransmitBusTimeout", 49),
          ("pbTransmitMasterTimeout", 53),
          ("priDialoutRqTimeout", 71),
          ("promptNotEnabled", 38),
          ("protocolErrorEvent", 76),
          ("r2ChannelBlockedByNetwork", 104),
          ("r2DNISNotFound", 107),
          ("r2DSPFatalError", 110),
          ("r2Glare", 105),
          ("r2InvalidChannelDirection", 103),
          ("r2OutgoingCallBlocked", 106),
          ("r2SigCauseCongestion", 108),
          ("r2SigCauseUnallocNumber", 109),
          ("rcvdGatewayDiscCmd", 62),
          ("remotHungUpDuringTraining", 80),
          ("remoteAccessDenied", 35),
          ("remotePassword", 8),
          ("resourceUnavailable", 79),
          ("retransmitLimit", 10),
          ("t1Glare", 70),
          ("timerExpired", 69),
          ("timeslotUnavailable", 100),
          ("tokenPassingTimeout", 63),
          ("tooManyUnacked", 68),
          ("trainingTimeout", 81),
          ("unableToRetrain", 14),
          ("undefined", 7),
          ("undetermined", 23),
          ("v32Cleardown", 33),
          ("v42BadSetup", 28),
          ("v42BreakTimeout", 25),
          ("v42DisconnectCmd", 26),
          ("v42IdExchangeFail", 27),
          ("v42InvalidCodeWord", 29),
          ("v42InvalidCommand", 31),
          ("v42SabmeTimeout", 24),
          ("v42StringToLong", 30),
          ("voice", 20))
    )


_MdmCsConnectFailReason_Type.__name__ = "Integer32"
_MdmCsConnectFailReason_Object = MibTableColumn
mdmCsConnectFailReason = _MdmCsConnectFailReason_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 6, 9, 1, 1, 9),
    _MdmCsConnectFailReason_Type()
)
mdmCsConnectFailReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mdmCsConnectFailReason.setStatus("mandatory")


class _MdmCsInitialTxLinkRate_Type(Integer32):
    """Custom type mdmCsInitialTxLinkRate based on Integer32"""
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
              23,
              24,
              25,
              26,
              27,
              28,
              29,
              30,
              31,
              32,
              33,
              34,
              35,
              36,
              37,
              38,
              39,
              40,
              41,
              42,
              43,
              44,
              45,
              46,
              47,
              48,
              49,
              50,
              51,
              52,
              53,
              54)
        )
    )
    namedValues = NamedValues(
        *(("bps110", 1),
          ("bps1200", 4),
          ("bps12K", 9),
          ("bps14K", 10),
          ("bps16K", 11),
          ("bps19K", 12),
          ("bps21K", 18),
          ("bps2400", 5),
          ("bps24K", 19),
          ("bps25333", 25),
          ("bps26666", 26),
          ("bps26K", 20),
          ("bps28000", 27),
          ("bps28K", 21),
          ("bps29333", 28),
          ("bps300", 2),
          ("bps30666", 29),
          ("bps31K", 23),
          ("bps32000", 30),
          ("bps33333", 31),
          ("bps33K", 24),
          ("bps34666", 32),
          ("bps36000", 33),
          ("bps37333", 34),
          ("bps38666", 35),
          ("bps38K", 13),
          ("bps40000", 36),
          ("bps41333", 37),
          ("bps42666", 38),
          ("bps44000", 39),
          ("bps450", 15),
          ("bps45333", 40),
          ("bps46666", 41),
          ("bps4800", 6),
          ("bps48000", 42),
          ("bps49333", 43),
          ("bps50666", 44),
          ("bps52000", 45),
          ("bps53333", 46),
          ("bps54666", 47),
          ("bps56000", 48),
          ("bps57333", 49),
          ("bps57K", 17),
          ("bps58666", 50),
          ("bps600", 3),
          ("bps60000", 51),
          ("bps61333", 52),
          ("bps62666", 53),
          ("bps64000", 54),
          ("bps7200", 7),
          ("bps75", 14),
          ("bps9600", 8),
          ("unknown", 16))
    )


_MdmCsInitialTxLinkRate_Type.__name__ = "Integer32"
_MdmCsInitialTxLinkRate_Object = MibTableColumn
mdmCsInitialTxLinkRate = _MdmCsInitialTxLinkRate_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 6, 9, 1, 1, 10),
    _MdmCsInitialTxLinkRate_Type()
)
mdmCsInitialTxLinkRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mdmCsInitialTxLinkRate.setStatus("mandatory")


class _MdmCsInitialRxLinkRate_Type(Integer32):
    """Custom type mdmCsInitialRxLinkRate based on Integer32"""
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
              23,
              24,
              25,
              26,
              27,
              28,
              29,
              30,
              31,
              32,
              33,
              34,
              35,
              36,
              37,
              38,
              39,
              40,
              41,
              42,
              43,
              44,
              45,
              46,
              47,
              48,
              49,
              50,
              51,
              52,
              53,
              54)
        )
    )
    namedValues = NamedValues(
        *(("bps110", 1),
          ("bps1200", 4),
          ("bps12K", 9),
          ("bps14K", 10),
          ("bps16K", 11),
          ("bps19K", 12),
          ("bps21K", 18),
          ("bps2400", 5),
          ("bps24K", 19),
          ("bps25333", 25),
          ("bps26666", 26),
          ("bps26K", 20),
          ("bps28000", 27),
          ("bps28K", 21),
          ("bps29333", 28),
          ("bps300", 2),
          ("bps30666", 29),
          ("bps31K", 23),
          ("bps32000", 30),
          ("bps33333", 31),
          ("bps33K", 24),
          ("bps34666", 32),
          ("bps36000", 33),
          ("bps37333", 34),
          ("bps38666", 35),
          ("bps38K", 13),
          ("bps40000", 36),
          ("bps41333", 37),
          ("bps42666", 38),
          ("bps44000", 39),
          ("bps450", 15),
          ("bps45333", 40),
          ("bps46666", 41),
          ("bps4800", 6),
          ("bps48000", 42),
          ("bps49333", 43),
          ("bps50666", 44),
          ("bps52000", 45),
          ("bps53333", 46),
          ("bps54666", 47),
          ("bps56000", 48),
          ("bps57333", 49),
          ("bps57K", 17),
          ("bps58666", 50),
          ("bps600", 3),
          ("bps60000", 51),
          ("bps61333", 52),
          ("bps62666", 53),
          ("bps64000", 54),
          ("bps7200", 7),
          ("bps75", 14),
          ("bps9600", 8),
          ("unknown", 16))
    )


_MdmCsInitialRxLinkRate_Type.__name__ = "Integer32"
_MdmCsInitialRxLinkRate_Object = MibTableColumn
mdmCsInitialRxLinkRate = _MdmCsInitialRxLinkRate_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 6, 9, 1, 1, 11),
    _MdmCsInitialRxLinkRate_Type()
)
mdmCsInitialRxLinkRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mdmCsInitialRxLinkRate.setStatus("mandatory")


class _MdmCsFinalTxLinkRate_Type(Integer32):
    """Custom type mdmCsFinalTxLinkRate based on Integer32"""
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
              23,
              24,
              25,
              26,
              27,
              28,
              29,
              30,
              31,
              32,
              33,
              34,
              35,
              36,
              37,
              38,
              39,
              40,
              41,
              42,
              43,
              44,
              45,
              46,
              47,
              48,
              49,
              50,
              51,
              52,
              53,
              54)
        )
    )
    namedValues = NamedValues(
        *(("bps110", 1),
          ("bps1200", 4),
          ("bps12K", 9),
          ("bps14K", 10),
          ("bps16K", 11),
          ("bps19K", 12),
          ("bps21K", 18),
          ("bps2400", 5),
          ("bps24K", 19),
          ("bps25333", 25),
          ("bps26666", 26),
          ("bps26K", 20),
          ("bps28000", 27),
          ("bps28K", 21),
          ("bps29333", 28),
          ("bps300", 2),
          ("bps30666", 29),
          ("bps31K", 23),
          ("bps32000", 30),
          ("bps33333", 31),
          ("bps33K", 24),
          ("bps34666", 32),
          ("bps36000", 33),
          ("bps37333", 34),
          ("bps38666", 35),
          ("bps38K", 13),
          ("bps40000", 36),
          ("bps41333", 37),
          ("bps42666", 38),
          ("bps44000", 39),
          ("bps450", 15),
          ("bps45333", 40),
          ("bps46666", 41),
          ("bps4800", 6),
          ("bps48000", 42),
          ("bps49333", 43),
          ("bps50666", 44),
          ("bps52000", 45),
          ("bps53333", 46),
          ("bps54666", 47),
          ("bps56000", 48),
          ("bps57333", 49),
          ("bps57K", 17),
          ("bps58666", 50),
          ("bps600", 3),
          ("bps60000", 51),
          ("bps61333", 52),
          ("bps62666", 53),
          ("bps64000", 54),
          ("bps7200", 7),
          ("bps75", 14),
          ("bps9600", 8),
          ("unknown", 16))
    )


_MdmCsFinalTxLinkRate_Type.__name__ = "Integer32"
_MdmCsFinalTxLinkRate_Object = MibTableColumn
mdmCsFinalTxLinkRate = _MdmCsFinalTxLinkRate_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 6, 9, 1, 1, 12),
    _MdmCsFinalTxLinkRate_Type()
)
mdmCsFinalTxLinkRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mdmCsFinalTxLinkRate.setStatus("mandatory")


class _MdmCsFinalRxLinkRate_Type(Integer32):
    """Custom type mdmCsFinalRxLinkRate based on Integer32"""
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
              23,
              24,
              25,
              26,
              27,
              28,
              29,
              30,
              31,
              32,
              33,
              34,
              35,
              36,
              37,
              38,
              39,
              40,
              41,
              42,
              43,
              44,
              45,
              46,
              47,
              48,
              49,
              50,
              51,
              52,
              53,
              54)
        )
    )
    namedValues = NamedValues(
        *(("bps110", 1),
          ("bps1200", 4),
          ("bps12K", 9),
          ("bps14K", 10),
          ("bps16K", 11),
          ("bps19K", 12),
          ("bps21K", 18),
          ("bps2400", 5),
          ("bps24K", 19),
          ("bps25333", 25),
          ("bps26666", 26),
          ("bps26K", 20),
          ("bps28000", 27),
          ("bps28K", 21),
          ("bps29333", 28),
          ("bps300", 2),
          ("bps30666", 29),
          ("bps31K", 23),
          ("bps32000", 30),
          ("bps33333", 31),
          ("bps33K", 24),
          ("bps34666", 32),
          ("bps36000", 33),
          ("bps37333", 34),
          ("bps38666", 35),
          ("bps38K", 13),
          ("bps40000", 36),
          ("bps41333", 37),
          ("bps42666", 38),
          ("bps44000", 39),
          ("bps450", 15),
          ("bps45333", 40),
          ("bps46666", 41),
          ("bps4800", 6),
          ("bps48000", 42),
          ("bps49333", 43),
          ("bps50666", 44),
          ("bps52000", 45),
          ("bps53333", 46),
          ("bps54666", 47),
          ("bps56000", 48),
          ("bps57333", 49),
          ("bps57K", 17),
          ("bps58666", 50),
          ("bps600", 3),
          ("bps60000", 51),
          ("bps61333", 52),
          ("bps62666", 53),
          ("bps64000", 54),
          ("bps7200", 7),
          ("bps75", 14),
          ("bps9600", 8),
          ("unknown", 16))
    )


_MdmCsFinalRxLinkRate_Type.__name__ = "Integer32"
_MdmCsFinalRxLinkRate_Object = MibTableColumn
mdmCsFinalRxLinkRate = _MdmCsFinalRxLinkRate_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 6, 9, 1, 1, 13),
    _MdmCsFinalRxLinkRate_Type()
)
mdmCsFinalRxLinkRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mdmCsFinalRxLinkRate.setStatus("mandatory")


class _MdmCsModulationType_Type(Integer32):
    """Custom type mdmCsModulationType based on Integer32"""
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
              25,
              26,
              27,
              28,
              29,
              30,
              31,
              32,
              33,
              34,
              35)
        )
    )
    namedValues = NamedValues(
        *(("asyncSyncPPP", 27),
          ("bell103", 4),
          ("bell208b", 10),
          ("bell212", 6),
          ("ccittV21", 5),
          ("ccittV22bis", 3),
          ("ccittV23", 8),
          ("ccittV32", 2),
          ("ccittV32bis", 7),
          ("clearChannel", 28),
          ("noConnection", 9),
          ("piafs", 31),
          ("usRoboticsHST", 1),
          ("v110", 24),
          ("v120", 25),
          ("v17FaxClass1", 14),
          ("v17FaxClass2", 18),
          ("v21FaxClass1", 11),
          ("v21FaxClass2", 15),
          ("v27FaxClass1", 12),
          ("v27FaxClass2", 16),
          ("v29FaxClass1", 13),
          ("v29FaxClass2", 17),
          ("v32Terbo", 19),
          ("v34", 20),
          ("v34plus", 22),
          ("v90AllDigital", 35),
          ("v90Analogue", 33),
          ("v90Digital", 34),
          ("vFC", 21),
          ("x2client", 29),
          ("x2server", 23),
          ("x2symmetric", 30),
          ("x2version2", 32),
          ("x75", 26))
    )


_MdmCsModulationType_Type.__name__ = "Integer32"
_MdmCsModulationType_Object = MibTableColumn
mdmCsModulationType = _MdmCsModulationType_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 6, 9, 1, 1, 14),
    _MdmCsModulationType_Type()
)
mdmCsModulationType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mdmCsModulationType.setStatus("mandatory")


class _MdmCsSyncAsyncModeUsed_Type(Integer32):
    """Custom type mdmCsSyncAsyncModeUsed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("asynchronous", 1),
          ("synchronous", 2))
    )


_MdmCsSyncAsyncModeUsed_Type.__name__ = "Integer32"
_MdmCsSyncAsyncModeUsed_Object = MibTableColumn
mdmCsSyncAsyncModeUsed = _MdmCsSyncAsyncModeUsed_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 6, 9, 1, 1, 15),
    _MdmCsSyncAsyncModeUsed_Type()
)
mdmCsSyncAsyncModeUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mdmCsSyncAsyncModeUsed.setStatus("mandatory")


class _MdmCsErrorControlType_Type(Integer32):
    """Custom type mdmCsErrorControlType based on Integer32"""
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
        *(("ccittV42", 4),
          ("ccittV42SREJ", 13),
          ("lapmEc", 11),
          ("mnp10", 8),
          ("mnp10Ec", 10),
          ("mnpLevel2", 7),
          ("mnpLevel3", 2),
          ("mnpLevel4", 3),
          ("none", 1),
          ("piafs", 14),
          ("synchronousNone", 6),
          ("usRoboticsHST", 5),
          ("v120", 15),
          ("v42Etc", 9),
          ("v42Etc2", 12),
          ("x75", 16))
    )


_MdmCsErrorControlType_Type.__name__ = "Integer32"
_MdmCsErrorControlType_Object = MibTableColumn
mdmCsErrorControlType = _MdmCsErrorControlType_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 6, 9, 1, 1, 16),
    _MdmCsErrorControlType_Type()
)
mdmCsErrorControlType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mdmCsErrorControlType.setStatus("mandatory")


class _MdmCsCompressionType_Type(Integer32):
    """Custom type mdmCsCompressionType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("ccittV42bis", 2),
          ("mnpLevel5", 3),
          ("none", 1))
    )


_MdmCsCompressionType_Type.__name__ = "Integer32"
_MdmCsCompressionType_Object = MibTableColumn
mdmCsCompressionType = _MdmCsCompressionType_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 6, 9, 1, 1, 17),
    _MdmCsCompressionType_Type()
)
mdmCsCompressionType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mdmCsCompressionType.setStatus("mandatory")


class _MdmCsEqualizationType_Type(Integer32):
    """Custom type mdmCsEqualizationType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("long", 1),
          ("short", 2))
    )


_MdmCsEqualizationType_Type.__name__ = "Integer32"
_MdmCsEqualizationType_Object = MibTableColumn
mdmCsEqualizationType = _MdmCsEqualizationType_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 6, 9, 1, 1, 18),
    _MdmCsEqualizationType_Type()
)
mdmCsEqualizationType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mdmCsEqualizationType.setStatus("mandatory")


class _MdmCsFallbackEnabled_Type(Integer32):
    """Custom type mdmCsFallbackEnabled based on Integer32"""
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


_MdmCsFallbackEnabled_Type.__name__ = "Integer32"
_MdmCsFallbackEnabled_Object = MibTableColumn
mdmCsFallbackEnabled = _MdmCsFallbackEnabled_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 6, 9, 1, 1, 19),
    _MdmCsFallbackEnabled_Type()
)
mdmCsFallbackEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mdmCsFallbackEnabled.setStatus("mandatory")
_MdmCsCharsSent_Type = Integer32
_MdmCsCharsSent_Object = MibTableColumn
mdmCsCharsSent = _MdmCsCharsSent_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 6, 9, 1, 1, 20),
    _MdmCsCharsSent_Type()
)
mdmCsCharsSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mdmCsCharsSent.setStatus("mandatory")
_MdmCsCharsReceived_Type = Integer32
_MdmCsCharsReceived_Object = MibTableColumn
mdmCsCharsReceived = _MdmCsCharsReceived_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 6, 9, 1, 1, 21),
    _MdmCsCharsReceived_Type()
)
mdmCsCharsReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mdmCsCharsReceived.setStatus("mandatory")
_MdmCsOctetsSent_Type = Integer32
_MdmCsOctetsSent_Object = MibTableColumn
mdmCsOctetsSent = _MdmCsOctetsSent_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 6, 9, 1, 1, 22),
    _MdmCsOctetsSent_Type()
)
mdmCsOctetsSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mdmCsOctetsSent.setStatus("mandatory")
_MdmCsOctetsReceived_Type = Integer32
_MdmCsOctetsReceived_Object = MibTableColumn
mdmCsOctetsReceived = _MdmCsOctetsReceived_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 6, 9, 1, 1, 23),
    _MdmCsOctetsReceived_Type()
)
mdmCsOctetsReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mdmCsOctetsReceived.setStatus("mandatory")
_MdmCsBlocksSent_Type = Integer32
_MdmCsBlocksSent_Object = MibTableColumn
mdmCsBlocksSent = _MdmCsBlocksSent_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 6, 9, 1, 1, 24),
    _MdmCsBlocksSent_Type()
)
mdmCsBlocksSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mdmCsBlocksSent.setStatus("mandatory")
_MdmCsBlocksReceived_Type = Integer32
_MdmCsBlocksReceived_Object = MibTableColumn
mdmCsBlocksReceived = _MdmCsBlocksReceived_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 6, 9, 1, 1, 25),
    _MdmCsBlocksReceived_Type()
)
mdmCsBlocksReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mdmCsBlocksReceived.setStatus("mandatory")
_MdmCsBlocksResent_Type = Integer32
_MdmCsBlocksResent_Object = MibTableColumn
mdmCsBlocksResent = _MdmCsBlocksResent_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 6, 9, 1, 1, 26),
    _MdmCsBlocksResent_Type()
)
mdmCsBlocksResent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mdmCsBlocksResent.setStatus("mandatory")
_MdmCsRetrainsRequested_Type = Integer32
_MdmCsRetrainsRequested_Object = MibTableColumn
mdmCsRetrainsRequested = _MdmCsRetrainsRequested_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 6, 9, 1, 1, 27),
    _MdmCsRetrainsRequested_Type()
)
mdmCsRetrainsRequested.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mdmCsRetrainsRequested.setStatus("mandatory")
_MdmCsRetrainsGranted_Type = Integer32
_MdmCsRetrainsGranted_Object = MibTableColumn
mdmCsRetrainsGranted = _MdmCsRetrainsGranted_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 6, 9, 1, 1, 28),
    _MdmCsRetrainsGranted_Type()
)
mdmCsRetrainsGranted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mdmCsRetrainsGranted.setStatus("mandatory")
_MdmCsLineReversalQty_Type = Integer32
_MdmCsLineReversalQty_Object = MibTableColumn
mdmCsLineReversalQty = _MdmCsLineReversalQty_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 6, 9, 1, 1, 29),
    _MdmCsLineReversalQty_Type()
)
mdmCsLineReversalQty.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mdmCsLineReversalQty.setStatus("mandatory")
_MdmCsCharsLost_Type = Integer32
_MdmCsCharsLost_Object = MibTableColumn
mdmCsCharsLost = _MdmCsCharsLost_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 6, 9, 1, 1, 30),
    _MdmCsCharsLost_Type()
)
mdmCsCharsLost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mdmCsCharsLost.setStatus("mandatory")


class _MdmCsBackChannelRate_Type(Integer32):
    """Custom type mdmCsBackChannelRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("bps300", 2),
          ("bps450", 1),
          ("none", 3))
    )


_MdmCsBackChannelRate_Type.__name__ = "Integer32"
_MdmCsBackChannelRate_Object = MibTableColumn
mdmCsBackChannelRate = _MdmCsBackChannelRate_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 6, 9, 1, 1, 31),
    _MdmCsBackChannelRate_Type()
)
mdmCsBackChannelRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mdmCsBackChannelRate.setStatus("mandatory")
_MdmCsBlerQty_Type = Integer32
_MdmCsBlerQty_Object = MibTableColumn
mdmCsBlerQty = _MdmCsBlerQty_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 6, 9, 1, 1, 32),
    _MdmCsBlerQty_Type()
)
mdmCsBlerQty.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mdmCsBlerQty.setStatus("mandatory")
_MdmCsLinkTimeoutQty_Type = Integer32
_MdmCsLinkTimeoutQty_Object = MibTableColumn
mdmCsLinkTimeoutQty = _MdmCsLinkTimeoutQty_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 6, 9, 1, 1, 33),
    _MdmCsLinkTimeoutQty_Type()
)
mdmCsLinkTimeoutQty.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mdmCsLinkTimeoutQty.setStatus("mandatory")
_MdmCsFallbackQty_Type = Integer32
_MdmCsFallbackQty_Object = MibTableColumn
mdmCsFallbackQty = _MdmCsFallbackQty_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 6, 9, 1, 1, 34),
    _MdmCsFallbackQty_Type()
)
mdmCsFallbackQty.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mdmCsFallbackQty.setStatus("mandatory")
_MdmCsUpshiftQty_Type = Integer32
_MdmCsUpshiftQty_Object = MibTableColumn
mdmCsUpshiftQty = _MdmCsUpshiftQty_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 6, 9, 1, 1, 35),
    _MdmCsUpshiftQty_Type()
)
mdmCsUpshiftQty.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mdmCsUpshiftQty.setStatus("mandatory")
_MdmCsLinkNakQty_Type = Integer32
_MdmCsLinkNakQty_Object = MibTableColumn
mdmCsLinkNakQty = _MdmCsLinkNakQty_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 6, 9, 1, 1, 36),
    _MdmCsLinkNakQty_Type()
)
mdmCsLinkNakQty.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mdmCsLinkNakQty.setStatus("mandatory")
_MdmCsGainHitCount_Type = Integer32
_MdmCsGainHitCount_Object = MibTableColumn
mdmCsGainHitCount = _MdmCsGainHitCount_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 6, 9, 1, 1, 37),
    _MdmCsGainHitCount_Type()
)
mdmCsGainHitCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mdmCsGainHitCount.setStatus("mandatory")


class _MdmCsSecurityUserName_Type(DisplayString):
    """Custom type mdmCsSecurityUserName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_MdmCsSecurityUserName_Type.__name__ = "DisplayString"
_MdmCsSecurityUserName_Object = MibTableColumn
mdmCsSecurityUserName = _MdmCsSecurityUserName_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 6, 9, 1, 1, 38),
    _MdmCsSecurityUserName_Type()
)
mdmCsSecurityUserName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mdmCsSecurityUserName.setStatus("mandatory")


class _MdmCsCallDuration_Type(DisplayString):
    """Custom type mdmCsCallDuration based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_MdmCsCallDuration_Type.__name__ = "DisplayString"
_MdmCsCallDuration_Object = MibTableColumn
mdmCsCallDuration = _MdmCsCallDuration_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 6, 9, 1, 1, 39),
    _MdmCsCallDuration_Type()
)
mdmCsCallDuration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mdmCsCallDuration.setStatus("mandatory")
_MdmCsCallRefNum_Type = Integer32
_MdmCsCallRefNum_Object = MibTableColumn
mdmCsCallRefNum = _MdmCsCallRefNum_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 6, 9, 1, 1, 40),
    _MdmCsCallRefNum_Type()
)
mdmCsCallRefNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mdmCsCallRefNum.setStatus("mandatory")
_MdmCsPriCardSlot_Type = Integer32
_MdmCsPriCardSlot_Object = MibTableColumn
mdmCsPriCardSlot = _MdmCsPriCardSlot_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 6, 9, 1, 1, 41),
    _MdmCsPriCardSlot_Type()
)
mdmCsPriCardSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mdmCsPriCardSlot.setStatus("mandatory")
_MdmCsTDMTimeSlot_Type = Integer32
_MdmCsTDMTimeSlot_Object = MibTableColumn
mdmCsTDMTimeSlot = _MdmCsTDMTimeSlot_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 6, 9, 1, 1, 42),
    _MdmCsTDMTimeSlot_Type()
)
mdmCsTDMTimeSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mdmCsTDMTimeSlot.setStatus("mandatory")
_MdmCsPriCardSpanLine_Type = Integer32
_MdmCsPriCardSpanLine_Object = MibTableColumn
mdmCsPriCardSpanLine = _MdmCsPriCardSpanLine_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 6, 9, 1, 1, 43),
    _MdmCsPriCardSpanLine_Type()
)
mdmCsPriCardSpanLine.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mdmCsPriCardSpanLine.setStatus("mandatory")
_MdmCsBChannelUsed_Type = Integer32
_MdmCsBChannelUsed_Object = MibTableColumn
mdmCsBChannelUsed = _MdmCsBChannelUsed_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 6, 9, 1, 1, 44),
    _MdmCsBChannelUsed_Type()
)
mdmCsBChannelUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mdmCsBChannelUsed.setStatus("mandatory")


class _MdmCsQCarrFreqTx_Type(Integer32):
    """Custom type mdmCsQCarrFreqTx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_MdmCsQCarrFreqTx_Type.__name__ = "Integer32"
_MdmCsQCarrFreqTx_Object = MibTableColumn
mdmCsQCarrFreqTx = _MdmCsQCarrFreqTx_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 6, 9, 1, 1, 45),
    _MdmCsQCarrFreqTx_Type()
)
mdmCsQCarrFreqTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mdmCsQCarrFreqTx.setStatus("mandatory")


class _MdmCsQCarrFreqRx_Type(Integer32):
    """Custom type mdmCsQCarrFreqRx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_MdmCsQCarrFreqRx_Type.__name__ = "Integer32"
_MdmCsQCarrFreqRx_Object = MibTableColumn
mdmCsQCarrFreqRx = _MdmCsQCarrFreqRx_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 6, 9, 1, 1, 46),
    _MdmCsQCarrFreqRx_Type()
)
mdmCsQCarrFreqRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mdmCsQCarrFreqRx.setStatus("mandatory")


class _MdmCsQSymRateTx_Type(Integer32):
    """Custom type mdmCsQSymRateTx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_MdmCsQSymRateTx_Type.__name__ = "Integer32"
_MdmCsQSymRateTx_Object = MibTableColumn
mdmCsQSymRateTx = _MdmCsQSymRateTx_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 6, 9, 1, 1, 47),
    _MdmCsQSymRateTx_Type()
)
mdmCsQSymRateTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mdmCsQSymRateTx.setStatus("mandatory")


class _MdmCsQSymRateRx_Type(Integer32):
    """Custom type mdmCsQSymRateRx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_MdmCsQSymRateRx_Type.__name__ = "Integer32"
_MdmCsQSymRateRx_Object = MibTableColumn
mdmCsQSymRateRx = _MdmCsQSymRateRx_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 6, 9, 1, 1, 48),
    _MdmCsQSymRateRx_Type()
)
mdmCsQSymRateRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mdmCsQSymRateRx.setStatus("mandatory")


class _MdmCsQTrellisTx_Type(Integer32):
    """Custom type mdmCsQTrellisTx based on Integer32"""
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
        *(("trellis16S-4D", 2),
          ("trellis32S-2D", 3),
          ("trellis64S-4D", 4),
          ("trellis8S-2D", 1))
    )


_MdmCsQTrellisTx_Type.__name__ = "Integer32"
_MdmCsQTrellisTx_Object = MibTableColumn
mdmCsQTrellisTx = _MdmCsQTrellisTx_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 6, 9, 1, 1, 49),
    _MdmCsQTrellisTx_Type()
)
mdmCsQTrellisTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mdmCsQTrellisTx.setStatus("mandatory")


class _MdmCsQTrellisRx_Type(Integer32):
    """Custom type mdmCsQTrellisRx based on Integer32"""
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
        *(("trellis16S-4D", 2),
          ("trellis32S-2D", 3),
          ("trellis64S-4D", 4),
          ("trellis8S-2D", 1))
    )


_MdmCsQTrellisRx_Type.__name__ = "Integer32"
_MdmCsQTrellisRx_Object = MibTableColumn
mdmCsQTrellisRx = _MdmCsQTrellisRx_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 6, 9, 1, 1, 50),
    _MdmCsQTrellisRx_Type()
)
mdmCsQTrellisRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mdmCsQTrellisRx.setStatus("mandatory")


class _MdmCsQNonLinCdTx_Type(Integer32):
    """Custom type mdmCsQNonLinCdTx based on Integer32"""
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


_MdmCsQNonLinCdTx_Type.__name__ = "Integer32"
_MdmCsQNonLinCdTx_Object = MibTableColumn
mdmCsQNonLinCdTx = _MdmCsQNonLinCdTx_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 6, 9, 1, 1, 51),
    _MdmCsQNonLinCdTx_Type()
)
mdmCsQNonLinCdTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mdmCsQNonLinCdTx.setStatus("mandatory")


class _MdmCsQNonLinCdRx_Type(Integer32):
    """Custom type mdmCsQNonLinCdRx based on Integer32"""
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


_MdmCsQNonLinCdRx_Type.__name__ = "Integer32"
_MdmCsQNonLinCdRx_Object = MibTableColumn
mdmCsQNonLinCdRx = _MdmCsQNonLinCdRx_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 6, 9, 1, 1, 52),
    _MdmCsQNonLinCdRx_Type()
)
mdmCsQNonLinCdRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mdmCsQNonLinCdRx.setStatus("mandatory")


class _MdmCsQPrecodingTx_Type(Integer32):
    """Custom type mdmCsQPrecodingTx based on Integer32"""
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


_MdmCsQPrecodingTx_Type.__name__ = "Integer32"
_MdmCsQPrecodingTx_Object = MibTableColumn
mdmCsQPrecodingTx = _MdmCsQPrecodingTx_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 6, 9, 1, 1, 53),
    _MdmCsQPrecodingTx_Type()
)
mdmCsQPrecodingTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mdmCsQPrecodingTx.setStatus("mandatory")


class _MdmCsQPrecodingRx_Type(Integer32):
    """Custom type mdmCsQPrecodingRx based on Integer32"""
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


_MdmCsQPrecodingRx_Type.__name__ = "Integer32"
_MdmCsQPrecodingRx_Object = MibTableColumn
mdmCsQPrecodingRx = _MdmCsQPrecodingRx_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 6, 9, 1, 1, 54),
    _MdmCsQPrecodingRx_Type()
)
mdmCsQPrecodingRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mdmCsQPrecodingRx.setStatus("mandatory")


class _MdmCsQShapingTx_Type(Integer32):
    """Custom type mdmCsQShapingTx based on Integer32"""
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


_MdmCsQShapingTx_Type.__name__ = "Integer32"
_MdmCsQShapingTx_Object = MibTableColumn
mdmCsQShapingTx = _MdmCsQShapingTx_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 6, 9, 1, 1, 55),
    _MdmCsQShapingTx_Type()
)
mdmCsQShapingTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mdmCsQShapingTx.setStatus("mandatory")


class _MdmCsQShapingRx_Type(Integer32):
    """Custom type mdmCsQShapingRx based on Integer32"""
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


_MdmCsQShapingRx_Type.__name__ = "Integer32"
_MdmCsQShapingRx_Object = MibTableColumn
mdmCsQShapingRx = _MdmCsQShapingRx_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 6, 9, 1, 1, 56),
    _MdmCsQShapingRx_Type()
)
mdmCsQShapingRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mdmCsQShapingRx.setStatus("mandatory")


class _MdmCsQPreemphTx_Type(Integer32):
    """Custom type mdmCsQPreemphTx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_MdmCsQPreemphTx_Type.__name__ = "Integer32"
_MdmCsQPreemphTx_Object = MibTableColumn
mdmCsQPreemphTx = _MdmCsQPreemphTx_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 6, 9, 1, 1, 57),
    _MdmCsQPreemphTx_Type()
)
mdmCsQPreemphTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mdmCsQPreemphTx.setStatus("mandatory")


class _MdmCsQPreemphRx_Type(Integer32):
    """Custom type mdmCsQPreemphRx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_MdmCsQPreemphRx_Type.__name__ = "Integer32"
_MdmCsQPreemphRx_Object = MibTableColumn
mdmCsQPreemphRx = _MdmCsQPreemphRx_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 6, 9, 1, 1, 58),
    _MdmCsQPreemphRx_Type()
)
mdmCsQPreemphRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mdmCsQPreemphRx.setStatus("mandatory")
_MdmCsQRxLevel_Type = Integer32
_MdmCsQRxLevel_Object = MibTableColumn
mdmCsQRxLevel = _MdmCsQRxLevel_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 6, 9, 1, 1, 59),
    _MdmCsQRxLevel_Type()
)
mdmCsQRxLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mdmCsQRxLevel.setStatus("mandatory")
_MdmCsQTxLevel_Type = Integer32
_MdmCsQTxLevel_Object = MibTableColumn
mdmCsQTxLevel = _MdmCsQTxLevel_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 6, 9, 1, 1, 60),
    _MdmCsQTxLevel_Type()
)
mdmCsQTxLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mdmCsQTxLevel.setStatus("mandatory")
_MdmCsQSNR_Type = Integer32
_MdmCsQSNR_Object = MibTableColumn
mdmCsQSNR = _MdmCsQSNR_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 6, 9, 1, 1, 61),
    _MdmCsQSNR_Type()
)
mdmCsQSNR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mdmCsQSNR.setStatus("mandatory")
_MdmCsQNearEcho_Type = Integer32
_MdmCsQNearEcho_Object = MibTableColumn
mdmCsQNearEcho = _MdmCsQNearEcho_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 6, 9, 1, 1, 62),
    _MdmCsQNearEcho_Type()
)
mdmCsQNearEcho.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mdmCsQNearEcho.setStatus("mandatory")
_MdmCsQFarEcho_Type = Integer32
_MdmCsQFarEcho_Object = MibTableColumn
mdmCsQFarEcho = _MdmCsQFarEcho_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 6, 9, 1, 1, 63),
    _MdmCsQFarEcho_Type()
)
mdmCsQFarEcho.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mdmCsQFarEcho.setStatus("mandatory")


class _MdmCsQRndTripDly_Type(Integer32):
    """Custom type mdmCsQRndTripDly based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_MdmCsQRndTripDly_Type.__name__ = "Integer32"
_MdmCsQRndTripDly_Object = MibTableColumn
mdmCsQRndTripDly = _MdmCsQRndTripDly_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 6, 9, 1, 1, 64),
    _MdmCsQRndTripDly_Type()
)
mdmCsQRndTripDly.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mdmCsQRndTripDly.setStatus("mandatory")


class _MdmCsQPacketSizeCurr_Type(Integer32):
    """Custom type mdmCsQPacketSizeCurr based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_MdmCsQPacketSizeCurr_Type.__name__ = "Integer32"
_MdmCsQPacketSizeCurr_Object = MibTableColumn
mdmCsQPacketSizeCurr = _MdmCsQPacketSizeCurr_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 6, 9, 1, 1, 65),
    _MdmCsQPacketSizeCurr_Type()
)
mdmCsQPacketSizeCurr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mdmCsQPacketSizeCurr.setStatus("mandatory")


class _MdmCsQPacketSizeLow_Type(Integer32):
    """Custom type mdmCsQPacketSizeLow based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_MdmCsQPacketSizeLow_Type.__name__ = "Integer32"
_MdmCsQPacketSizeLow_Object = MibTableColumn
mdmCsQPacketSizeLow = _MdmCsQPacketSizeLow_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 6, 9, 1, 1, 66),
    _MdmCsQPacketSizeLow_Type()
)
mdmCsQPacketSizeLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mdmCsQPacketSizeLow.setStatus("mandatory")


class _MdmCsQPacketSizeHigh_Type(Integer32):
    """Custom type mdmCsQPacketSizeHigh based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_MdmCsQPacketSizeHigh_Type.__name__ = "Integer32"
_MdmCsQPacketSizeHigh_Object = MibTableColumn
mdmCsQPacketSizeHigh = _MdmCsQPacketSizeHigh_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 6, 9, 1, 1, 67),
    _MdmCsQPacketSizeHigh_Type()
)
mdmCsQPacketSizeHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mdmCsQPacketSizeHigh.setStatus("mandatory")
_MdmCsQCellTxLevelCurr_Type = Integer32
_MdmCsQCellTxLevelCurr_Object = MibTableColumn
mdmCsQCellTxLevelCurr = _MdmCsQCellTxLevelCurr_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 6, 9, 1, 1, 68),
    _MdmCsQCellTxLevelCurr_Type()
)
mdmCsQCellTxLevelCurr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mdmCsQCellTxLevelCurr.setStatus("mandatory")
_MdmCsQCellTxLevelLow_Type = Integer32
_MdmCsQCellTxLevelLow_Object = MibTableColumn
mdmCsQCellTxLevelLow = _MdmCsQCellTxLevelLow_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 6, 9, 1, 1, 69),
    _MdmCsQCellTxLevelLow_Type()
)
mdmCsQCellTxLevelLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mdmCsQCellTxLevelLow.setStatus("mandatory")
_MdmCsQCellTxLevelHigh_Type = Integer32
_MdmCsQCellTxLevelHigh_Object = MibTableColumn
mdmCsQCellTxLevelHigh = _MdmCsQCellTxLevelHigh_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 6, 9, 1, 1, 70),
    _MdmCsQCellTxLevelHigh_Type()
)
mdmCsQCellTxLevelHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mdmCsQCellTxLevelHigh.setStatus("mandatory")
_MdmCsQSNRLevelCurr_Type = Integer32
_MdmCsQSNRLevelCurr_Object = MibTableColumn
mdmCsQSNRLevelCurr = _MdmCsQSNRLevelCurr_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 6, 9, 1, 1, 71),
    _MdmCsQSNRLevelCurr_Type()
)
mdmCsQSNRLevelCurr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mdmCsQSNRLevelCurr.setStatus("mandatory")
_MdmCsQSNRLevelLow_Type = Integer32
_MdmCsQSNRLevelLow_Object = MibTableColumn
mdmCsQSNRLevelLow = _MdmCsQSNRLevelLow_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 6, 9, 1, 1, 72),
    _MdmCsQSNRLevelLow_Type()
)
mdmCsQSNRLevelLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mdmCsQSNRLevelLow.setStatus("mandatory")
_MdmCsQSNRLevelHigh_Type = Integer32
_MdmCsQSNRLevelHigh_Object = MibTableColumn
mdmCsQSNRLevelHigh = _MdmCsQSNRLevelHigh_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 6, 9, 1, 1, 73),
    _MdmCsQSNRLevelHigh_Type()
)
mdmCsQSNRLevelHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mdmCsQSNRLevelHigh.setStatus("mandatory")


class _MdmCsQCellularProt_Type(Integer32):
    """Custom type mdmCsQCellularProt based on Integer32"""
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
        *(("mnp10", 2),
          ("mnp10ec", 3),
          ("none", 1),
          ("v42etc", 4))
    )


_MdmCsQCellularProt_Type.__name__ = "Integer32"
_MdmCsQCellularProt_Object = MibTableColumn
mdmCsQCellularProt = _MdmCsQCellularProt_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 6, 9, 1, 1, 74),
    _MdmCsQCellularProt_Type()
)
mdmCsQCellularProt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mdmCsQCellularProt.setStatus("mandatory")


class _MdmCsFreqProbeData_Type(OctetString):
    """Custom type mdmCsFreqProbeData based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 60),
    )


_MdmCsFreqProbeData_Type.__name__ = "OctetString"
_MdmCsFreqProbeData_Object = MibTableColumn
mdmCsFreqProbeData = _MdmCsFreqProbeData_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 6, 9, 1, 1, 75),
    _MdmCsFreqProbeData_Type()
)
mdmCsFreqProbeData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mdmCsFreqProbeData.setStatus("mandatory")


class _MdmCsLevelProbeData_Type(OctetString):
    """Custom type mdmCsLevelProbeData based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 30),
    )


_MdmCsLevelProbeData_Type.__name__ = "OctetString"
_MdmCsLevelProbeData_Object = MibTableColumn
mdmCsLevelProbeData = _MdmCsLevelProbeData_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 6, 9, 1, 1, 76),
    _MdmCsLevelProbeData_Type()
)
mdmCsLevelProbeData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mdmCsLevelProbeData.setStatus("mandatory")


class _MdmCsQTimingOffset_Type(Integer32):
    """Custom type mdmCsQTimingOffset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_MdmCsQTimingOffset_Type.__name__ = "Integer32"
_MdmCsQTimingOffset_Object = MibTableColumn
mdmCsQTimingOffset = _MdmCsQTimingOffset_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 6, 9, 1, 1, 77),
    _MdmCsQTimingOffset_Type()
)
mdmCsQTimingOffset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mdmCsQTimingOffset.setStatus("mandatory")


class _MdmCsQCarrierOffset_Type(Integer32):
    """Custom type mdmCsQCarrierOffset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_MdmCsQCarrierOffset_Type.__name__ = "Integer32"
_MdmCsQCarrierOffset_Object = MibTableColumn
mdmCsQCarrierOffset = _MdmCsQCarrierOffset_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 6, 9, 1, 1, 78),
    _MdmCsQCarrierOffset_Type()
)
mdmCsQCarrierOffset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mdmCsQCarrierOffset.setStatus("mandatory")


class _MdmCsQCoding_Type(Integer32):
    """Custom type mdmCsQCoding based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("alaw", 2),
          ("mulaw", 1))
    )


_MdmCsQCoding_Type.__name__ = "Integer32"
_MdmCsQCoding_Object = MibTableColumn
mdmCsQCoding = _MdmCsQCoding_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 6, 9, 1, 1, 80),
    _MdmCsQCoding_Type()
)
mdmCsQCoding.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mdmCsQCoding.setStatus("mandatory")


class _MdmCsTrainingInfo_Type(OctetString):
    """Custom type mdmCsTrainingInfo based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_MdmCsTrainingInfo_Type.__name__ = "OctetString"
_MdmCsTrainingInfo_Object = MibTableColumn
mdmCsTrainingInfo = _MdmCsTrainingInfo_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 6, 9, 1, 1, 81),
    _MdmCsTrainingInfo_Type()
)
mdmCsTrainingInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mdmCsTrainingInfo.setStatus("mandatory")


class _MdmCsX2signature_Type(OctetString):
    """Custom type mdmCsX2signature based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_MdmCsX2signature_Type.__name__ = "OctetString"
_MdmCsX2signature_Object = MibTableColumn
mdmCsX2signature = _MdmCsX2signature_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 6, 9, 1, 1, 82),
    _MdmCsX2signature_Type()
)
mdmCsX2signature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mdmCsX2signature.setStatus("mandatory")


class _MdmCsX2Status_Type(Integer32):
    """Custom type mdmCsX2Status based on Integer32"""
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
              24)
        )
    )
    namedValues = NamedValues(
        *(("baud3200DisabledLocal", 5),
          ("baud3200DisabledRemote", 11),
          ("channelNoSymbolRate", 13),
          ("excessiveHFAttenuation", 12),
          ("exitBeforeX2Connect", 14),
          ("incompatibleV90Modes", 23),
          ("incompatibleV90Versions", 22),
          ("incompatibleX2Modes", 10),
          ("incompatibleX2Versions", 9),
          ("speedLimitedLocal", 6),
          ("v8DisabledLocal", 3),
          ("v8notDetectedFromRemote", 7),
          ("v90DisabledLocal", 17),
          ("v90IncompactibleSymRate", 24),
          ("v90NotDetectedFrmRemote", 20),
          ("v90Operational", 15),
          ("v90SymRatesDisabledLcl", 19),
          ("x2DisabledLocal", 4),
          ("x2Operational", 2),
          ("x2notDetectedFromRemote", 8),
          ("x2v90DisabledLocal", 18),
          ("x2v90NotDetectedFrmRmt", 21),
          ("x2v90NotOperational", 1),
          ("x2v90Operational", 16))
    )


_MdmCsX2Status_Type.__name__ = "Integer32"
_MdmCsX2Status_Object = MibTableColumn
mdmCsX2Status = _MdmCsX2Status_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 6, 9, 1, 1, 83),
    _MdmCsX2Status_Type()
)
mdmCsX2Status.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mdmCsX2Status.setStatus("mandatory")


class _MdmCsCallType_Type(Integer32):
    """Custom type mdmCsCallType based on Integer32"""
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
        *(("analogCall", 1),
          ("chT1GroundStart", 5),
          ("chT1ImmediateStart", 3),
          ("chT1LoopStart", 4),
          ("chT1PRICall", 6),
          ("chT1WinkStart", 2))
    )


_MdmCsCallType_Type.__name__ = "Integer32"
_MdmCsCallType_Object = MibTableColumn
mdmCsCallType = _MdmCsCallType_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 6, 9, 1, 1, 84),
    _MdmCsCallType_Type()
)
mdmCsCallType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mdmCsCallType.setStatus("mandatory")
_MdmCsCallStartTime_Type = Integer32
_MdmCsCallStartTime_Object = MibTableColumn
mdmCsCallStartTime = _MdmCsCallStartTime_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 6, 9, 1, 1, 85),
    _MdmCsCallStartTime_Type()
)
mdmCsCallStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mdmCsCallStartTime.setStatus("mandatory")
_MdmCsCallEndTime_Type = Integer32
_MdmCsCallEndTime_Object = MibTableColumn
mdmCsCallEndTime = _MdmCsCallEndTime_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 6, 9, 1, 1, 86),
    _MdmCsCallEndTime_Type()
)
mdmCsCallEndTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mdmCsCallEndTime.setStatus("mandatory")


class _MdmCsDigitalPadAttenuated_Type(Integer32):
    """Custom type mdmCsDigitalPadAttenuated based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_MdmCsDigitalPadAttenuated_Type.__name__ = "Integer32"
_MdmCsDigitalPadAttenuated_Object = MibTableColumn
mdmCsDigitalPadAttenuated = _MdmCsDigitalPadAttenuated_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 6, 9, 1, 1, 87),
    _MdmCsDigitalPadAttenuated_Type()
)
mdmCsDigitalPadAttenuated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mdmCsDigitalPadAttenuated.setStatus("mandatory")


class _MdmCsInitModulationType_Type(Integer32):
    """Custom type mdmCsInitModulationType based on Integer32"""
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
              25,
              26,
              27,
              28,
              29,
              30,
              31,
              32,
              33,
              34,
              35)
        )
    )
    namedValues = NamedValues(
        *(("asyncSyncPPP", 27),
          ("bell103", 4),
          ("bell208b", 10),
          ("bell212", 6),
          ("ccittV21", 5),
          ("ccittV22bis", 3),
          ("ccittV23", 8),
          ("ccittV32", 2),
          ("ccittV32bis", 7),
          ("clearChannel", 28),
          ("noConnection", 9),
          ("piafs", 31),
          ("usRoboticsHST", 1),
          ("v110", 24),
          ("v120", 25),
          ("v17FaxClass1", 14),
          ("v17FaxClass2", 18),
          ("v21FaxClass1", 11),
          ("v21FaxClass2", 15),
          ("v27FaxClass1", 12),
          ("v27FaxClass2", 16),
          ("v29FaxClass1", 13),
          ("v29FaxClass2", 17),
          ("v32Terbo", 19),
          ("v34", 20),
          ("v34plus", 22),
          ("v90AllDigital", 35),
          ("v90Analogue", 33),
          ("v90Digital", 34),
          ("vFC", 21),
          ("x2client", 29),
          ("x2server", 23),
          ("x2symmetric", 30),
          ("x2version2", 32),
          ("x75", 26))
    )


_MdmCsInitModulationType_Type.__name__ = "Integer32"
_MdmCsInitModulationType_Object = MibTableColumn
mdmCsInitModulationType = _MdmCsInitModulationType_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 6, 9, 1, 1, 88),
    _MdmCsInitModulationType_Type()
)
mdmCsInitModulationType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mdmCsInitModulationType.setStatus("mandatory")


class _MdmCsRxMinSpeed_Type(Integer32):
    """Custom type mdmCsRxMinSpeed based on Integer32"""
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
              23,
              24,
              25,
              26,
              27,
              28,
              29,
              30,
              31,
              32,
              33,
              34,
              35,
              36,
              37,
              38,
              39,
              40,
              41,
              42,
              43,
              44,
              45,
              46,
              47,
              48,
              49,
              50,
              51,
              52,
              53,
              54)
        )
    )
    namedValues = NamedValues(
        *(("bps110", 1),
          ("bps1200", 4),
          ("bps12K", 9),
          ("bps14K", 10),
          ("bps16K", 11),
          ("bps19K", 12),
          ("bps21K", 18),
          ("bps2400", 5),
          ("bps24K", 19),
          ("bps25333", 25),
          ("bps26666", 26),
          ("bps26K", 20),
          ("bps28000", 27),
          ("bps28K", 21),
          ("bps29333", 28),
          ("bps300", 2),
          ("bps30666", 29),
          ("bps31K", 23),
          ("bps32000", 30),
          ("bps33333", 31),
          ("bps33K", 24),
          ("bps34666", 32),
          ("bps36000", 33),
          ("bps37333", 34),
          ("bps38666", 35),
          ("bps38K", 13),
          ("bps40000", 36),
          ("bps41333", 37),
          ("bps42666", 38),
          ("bps44000", 39),
          ("bps450", 15),
          ("bps45333", 40),
          ("bps46666", 41),
          ("bps4800", 6),
          ("bps48000", 42),
          ("bps49333", 43),
          ("bps50666", 44),
          ("bps52000", 45),
          ("bps53333", 46),
          ("bps54666", 47),
          ("bps56000", 48),
          ("bps57333", 49),
          ("bps57K", 17),
          ("bps58666", 50),
          ("bps600", 3),
          ("bps60000", 51),
          ("bps61333", 52),
          ("bps62666", 53),
          ("bps64000", 54),
          ("bps7200", 7),
          ("bps75", 14),
          ("bps9600", 8),
          ("unknown", 16))
    )


_MdmCsRxMinSpeed_Type.__name__ = "Integer32"
_MdmCsRxMinSpeed_Object = MibTableColumn
mdmCsRxMinSpeed = _MdmCsRxMinSpeed_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 6, 9, 1, 1, 89),
    _MdmCsRxMinSpeed_Type()
)
mdmCsRxMinSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mdmCsRxMinSpeed.setStatus("mandatory")


class _MdmCsRxMaxSpeed_Type(Integer32):
    """Custom type mdmCsRxMaxSpeed based on Integer32"""
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
              23,
              24,
              25,
              26,
              27,
              28,
              29,
              30,
              31,
              32,
              33,
              34,
              35,
              36,
              37,
              38,
              39,
              40,
              41,
              42,
              43,
              44,
              45,
              46,
              47,
              48,
              49,
              50,
              51,
              52,
              53,
              54)
        )
    )
    namedValues = NamedValues(
        *(("bps110", 1),
          ("bps1200", 4),
          ("bps12K", 9),
          ("bps14K", 10),
          ("bps16K", 11),
          ("bps19K", 12),
          ("bps21K", 18),
          ("bps2400", 5),
          ("bps24K", 19),
          ("bps25333", 25),
          ("bps26666", 26),
          ("bps26K", 20),
          ("bps28000", 27),
          ("bps28K", 21),
          ("bps29333", 28),
          ("bps300", 2),
          ("bps30666", 29),
          ("bps31K", 23),
          ("bps32000", 30),
          ("bps33333", 31),
          ("bps33K", 24),
          ("bps34666", 32),
          ("bps36000", 33),
          ("bps37333", 34),
          ("bps38666", 35),
          ("bps38K", 13),
          ("bps40000", 36),
          ("bps41333", 37),
          ("bps42666", 38),
          ("bps44000", 39),
          ("bps450", 15),
          ("bps45333", 40),
          ("bps46666", 41),
          ("bps4800", 6),
          ("bps48000", 42),
          ("bps49333", 43),
          ("bps50666", 44),
          ("bps52000", 45),
          ("bps53333", 46),
          ("bps54666", 47),
          ("bps56000", 48),
          ("bps57333", 49),
          ("bps57K", 17),
          ("bps58666", 50),
          ("bps600", 3),
          ("bps60000", 51),
          ("bps61333", 52),
          ("bps62666", 53),
          ("bps64000", 54),
          ("bps7200", 7),
          ("bps75", 14),
          ("bps9600", 8),
          ("unknown", 16))
    )


_MdmCsRxMaxSpeed_Type.__name__ = "Integer32"
_MdmCsRxMaxSpeed_Object = MibTableColumn
mdmCsRxMaxSpeed = _MdmCsRxMaxSpeed_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 6, 9, 1, 1, 90),
    _MdmCsRxMaxSpeed_Type()
)
mdmCsRxMaxSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mdmCsRxMaxSpeed.setStatus("mandatory")


class _MdmCsTxMinSpeed_Type(Integer32):
    """Custom type mdmCsTxMinSpeed based on Integer32"""
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
              23,
              24,
              25,
              26,
              27,
              28,
              29,
              30,
              31,
              32,
              33,
              34,
              35,
              36,
              37,
              38,
              39,
              40,
              41,
              42,
              43,
              44,
              45,
              46,
              47,
              48,
              49,
              50,
              51,
              52,
              53,
              54)
        )
    )
    namedValues = NamedValues(
        *(("bps110", 1),
          ("bps1200", 4),
          ("bps12K", 9),
          ("bps14K", 10),
          ("bps16K", 11),
          ("bps19K", 12),
          ("bps21K", 18),
          ("bps2400", 5),
          ("bps24K", 19),
          ("bps25333", 25),
          ("bps26666", 26),
          ("bps26K", 20),
          ("bps28000", 27),
          ("bps28K", 21),
          ("bps29333", 28),
          ("bps300", 2),
          ("bps30666", 29),
          ("bps31K", 23),
          ("bps32000", 30),
          ("bps33333", 31),
          ("bps33K", 24),
          ("bps34666", 32),
          ("bps36000", 33),
          ("bps37333", 34),
          ("bps38666", 35),
          ("bps38K", 13),
          ("bps40000", 36),
          ("bps41333", 37),
          ("bps42666", 38),
          ("bps44000", 39),
          ("bps450", 15),
          ("bps45333", 40),
          ("bps46666", 41),
          ("bps4800", 6),
          ("bps48000", 42),
          ("bps49333", 43),
          ("bps50666", 44),
          ("bps52000", 45),
          ("bps53333", 46),
          ("bps54666", 47),
          ("bps56000", 48),
          ("bps57333", 49),
          ("bps57K", 17),
          ("bps58666", 50),
          ("bps600", 3),
          ("bps60000", 51),
          ("bps61333", 52),
          ("bps62666", 53),
          ("bps64000", 54),
          ("bps7200", 7),
          ("bps75", 14),
          ("bps9600", 8),
          ("unknown", 16))
    )


_MdmCsTxMinSpeed_Type.__name__ = "Integer32"
_MdmCsTxMinSpeed_Object = MibTableColumn
mdmCsTxMinSpeed = _MdmCsTxMinSpeed_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 6, 9, 1, 1, 91),
    _MdmCsTxMinSpeed_Type()
)
mdmCsTxMinSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mdmCsTxMinSpeed.setStatus("mandatory")


class _MdmCsTxMaxSpeed_Type(Integer32):
    """Custom type mdmCsTxMaxSpeed based on Integer32"""
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
              23,
              24,
              25,
              26,
              27,
              28,
              29,
              30,
              31,
              32,
              33,
              34,
              35,
              36,
              37,
              38,
              39,
              40,
              41,
              42,
              43,
              44,
              45,
              46,
              47,
              48,
              49,
              50,
              51,
              52,
              53,
              54)
        )
    )
    namedValues = NamedValues(
        *(("bps110", 1),
          ("bps1200", 4),
          ("bps12K", 9),
          ("bps14K", 10),
          ("bps16K", 11),
          ("bps19K", 12),
          ("bps21K", 18),
          ("bps2400", 5),
          ("bps24K", 19),
          ("bps25333", 25),
          ("bps26666", 26),
          ("bps26K", 20),
          ("bps28000", 27),
          ("bps28K", 21),
          ("bps29333", 28),
          ("bps300", 2),
          ("bps30666", 29),
          ("bps31K", 23),
          ("bps32000", 30),
          ("bps33333", 31),
          ("bps33K", 24),
          ("bps34666", 32),
          ("bps36000", 33),
          ("bps37333", 34),
          ("bps38666", 35),
          ("bps38K", 13),
          ("bps40000", 36),
          ("bps41333", 37),
          ("bps42666", 38),
          ("bps44000", 39),
          ("bps450", 15),
          ("bps45333", 40),
          ("bps46666", 41),
          ("bps4800", 6),
          ("bps48000", 42),
          ("bps49333", 43),
          ("bps50666", 44),
          ("bps52000", 45),
          ("bps53333", 46),
          ("bps54666", 47),
          ("bps56000", 48),
          ("bps57333", 49),
          ("bps57K", 17),
          ("bps58666", 50),
          ("bps600", 3),
          ("bps60000", 51),
          ("bps61333", 52),
          ("bps62666", 53),
          ("bps64000", 54),
          ("bps7200", 7),
          ("bps75", 14),
          ("bps9600", 8),
          ("unknown", 16))
    )


_MdmCsTxMaxSpeed_Type.__name__ = "Integer32"
_MdmCsTxMaxSpeed_Object = MibTableColumn
mdmCsTxMaxSpeed = _MdmCsTxMaxSpeed_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 6, 9, 1, 1, 92),
    _MdmCsTxMaxSpeed_Type()
)
mdmCsTxMaxSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mdmCsTxMaxSpeed.setStatus("mandatory")


class _MdmCsCollectedDTMFDigits_Type(OctetString):
    """Custom type mdmCsCollectedDTMFDigits based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_MdmCsCollectedDTMFDigits_Type.__name__ = "OctetString"
_MdmCsCollectedDTMFDigits_Object = MibTableColumn
mdmCsCollectedDTMFDigits = _MdmCsCollectedDTMFDigits_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 6, 9, 1, 1, 93),
    _MdmCsCollectedDTMFDigits_Type()
)
mdmCsCollectedDTMFDigits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mdmCsCollectedDTMFDigits.setStatus("mandatory")
_MdmEv_ObjectIdentity = ObjectIdentity
mdmEv = _MdmEv_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 429, 1, 6, 10)
)
_MdmEvTable_Object = MibTable
mdmEvTable = _MdmEvTable_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 6, 10, 1)
)
if mibBuilder.loadTexts:
    mdmEvTable.setStatus("mandatory")
_MdmEvEntry_Object = MibTableRow
mdmEvEntry = _MdmEvEntry_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 6, 10, 1, 1)
)
mdmEvEntry.setIndexNames(
    (0, "MDM-MIB", "mdmEvIndex"),
)
if mibBuilder.loadTexts:
    mdmEvEntry.setStatus("mandatory")
_MdmEvIndex_Type = Integer32
_MdmEvIndex_Object = MibTableColumn
mdmEvIndex = _MdmEvIndex_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 6, 10, 1, 1, 1),
    _MdmEvIndex_Type()
)
mdmEvIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mdmEvIndex.setStatus("mandatory")
_MdmEvWatchdogTimouts_Type = Counter32
_MdmEvWatchdogTimouts_Object = MibTableColumn
mdmEvWatchdogTimouts = _MdmEvWatchdogTimouts_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 6, 10, 1, 1, 2),
    _MdmEvWatchdogTimouts_Type()
)
mdmEvWatchdogTimouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mdmEvWatchdogTimouts.setStatus("mandatory")
_MdmEvDteIdleTimouts_Type = Counter32
_MdmEvDteIdleTimouts_Object = MibTableColumn
mdmEvDteIdleTimouts = _MdmEvDteIdleTimouts_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 6, 10, 1, 1, 3),
    _MdmEvDteIdleTimouts_Type()
)
mdmEvDteIdleTimouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mdmEvDteIdleTimouts.setStatus("mandatory")
_MdmEvInConnectEstabs_Type = Counter32
_MdmEvInConnectEstabs_Object = MibTableColumn
mdmEvInConnectEstabs = _MdmEvInConnectEstabs_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 6, 10, 1, 1, 4),
    _MdmEvInConnectEstabs_Type()
)
mdmEvInConnectEstabs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mdmEvInConnectEstabs.setStatus("mandatory")
_MdmEvOutConnectEstabs_Type = Counter32
_MdmEvOutConnectEstabs_Object = MibTableColumn
mdmEvOutConnectEstabs = _MdmEvOutConnectEstabs_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 6, 10, 1, 1, 5),
    _MdmEvOutConnectEstabs_Type()
)
mdmEvOutConnectEstabs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mdmEvOutConnectEstabs.setStatus("mandatory")
_MdmEvInConnectTerms_Type = Counter32
_MdmEvInConnectTerms_Object = MibTableColumn
mdmEvInConnectTerms = _MdmEvInConnectTerms_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 6, 10, 1, 1, 6),
    _MdmEvInConnectTerms_Type()
)
mdmEvInConnectTerms.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mdmEvInConnectTerms.setStatus("mandatory")
_MdmEvOutConnectTerms_Type = Counter32
_MdmEvOutConnectTerms_Object = MibTableColumn
mdmEvOutConnectTerms = _MdmEvOutConnectTerms_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 6, 10, 1, 1, 7),
    _MdmEvOutConnectTerms_Type()
)
mdmEvOutConnectTerms.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mdmEvOutConnectTerms.setStatus("mandatory")
_MdmEvConnectAttemptFails_Type = Counter32
_MdmEvConnectAttemptFails_Object = MibTableColumn
mdmEvConnectAttemptFails = _MdmEvConnectAttemptFails_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 6, 10, 1, 1, 8),
    _MdmEvConnectAttemptFails_Type()
)
mdmEvConnectAttemptFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mdmEvConnectAttemptFails.setStatus("mandatory")
_MdmEvConnectTimouts_Type = Counter32
_MdmEvConnectTimouts_Object = MibTableColumn
mdmEvConnectTimouts = _MdmEvConnectTimouts_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 6, 10, 1, 1, 9),
    _MdmEvConnectTimouts_Type()
)
mdmEvConnectTimouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mdmEvConnectTimouts.setStatus("mandatory")
_MdmEvMgmtBusFailures_Type = Counter32
_MdmEvMgmtBusFailures_Object = MibTableColumn
mdmEvMgmtBusFailures = _MdmEvMgmtBusFailures_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 6, 10, 1, 1, 10),
    _MdmEvMgmtBusFailures_Type()
)
mdmEvMgmtBusFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mdmEvMgmtBusFailures.setStatus("mandatory")
_MdmEvResetByDtes_Type = Counter32
_MdmEvResetByDtes_Object = MibTableColumn
mdmEvResetByDtes = _MdmEvResetByDtes_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 6, 10, 1, 1, 11),
    _MdmEvResetByDtes_Type()
)
mdmEvResetByDtes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mdmEvResetByDtes.setStatus("mandatory")
_MdmEvDtrFalses_Type = Counter32
_MdmEvDtrFalses_Object = MibTableColumn
mdmEvDtrFalses = _MdmEvDtrFalses_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 6, 10, 1, 1, 12),
    _MdmEvDtrFalses_Type()
)
mdmEvDtrFalses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mdmEvDtrFalses.setStatus("mandatory")
_MdmEvDtrTrues_Type = Counter32
_MdmEvDtrTrues_Object = MibTableColumn
mdmEvDtrTrues = _MdmEvDtrTrues_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 6, 10, 1, 1, 13),
    _MdmEvDtrTrues_Type()
)
mdmEvDtrTrues.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mdmEvDtrTrues.setStatus("mandatory")
_MdmEvNoTones_Type = Counter32
_MdmEvNoTones_Object = MibTableColumn
mdmEvNoTones = _MdmEvNoTones_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 6, 10, 1, 1, 14),
    _MdmEvNoTones_Type()
)
mdmEvNoTones.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mdmEvNoTones.setStatus("mandatory")
_MdmEvNoLoops_Type = Counter32
_MdmEvNoLoops_Object = MibTableColumn
mdmEvNoLoops = _MdmEvNoLoops_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 6, 10, 1, 1, 15),
    _MdmEvNoLoops_Type()
)
mdmEvNoLoops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mdmEvNoLoops.setStatus("mandatory")
_MdmEvBlers_Type = Counter32
_MdmEvBlers_Object = MibTableColumn
mdmEvBlers = _MdmEvBlers_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 6, 10, 1, 1, 16),
    _MdmEvBlers_Type()
)
mdmEvBlers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mdmEvBlers.setStatus("mandatory")
_MdmEvFallBacks_Type = Counter32
_MdmEvFallBacks_Object = MibTableColumn
mdmEvFallBacks = _MdmEvFallBacks_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 6, 10, 1, 1, 17),
    _MdmEvFallBacks_Type()
)
mdmEvFallBacks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mdmEvFallBacks.setStatus("mandatory")
_MdmEvInConnectTime_Type = Counter32
_MdmEvInConnectTime_Object = MibTableColumn
mdmEvInConnectTime = _MdmEvInConnectTime_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 6, 10, 1, 1, 18),
    _MdmEvInConnectTime_Type()
)
mdmEvInConnectTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mdmEvInConnectTime.setStatus("mandatory")
_MdmEvInTotalBytesRx_Type = Counter32
_MdmEvInTotalBytesRx_Object = MibTableColumn
mdmEvInTotalBytesRx = _MdmEvInTotalBytesRx_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 6, 10, 1, 1, 19),
    _MdmEvInTotalBytesRx_Type()
)
mdmEvInTotalBytesRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mdmEvInTotalBytesRx.setStatus("mandatory")
_MdmEvInTotalBytesTx_Type = Counter32
_MdmEvInTotalBytesTx_Object = MibTableColumn
mdmEvInTotalBytesTx = _MdmEvInTotalBytesTx_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 6, 10, 1, 1, 20),
    _MdmEvInTotalBytesTx_Type()
)
mdmEvInTotalBytesTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mdmEvInTotalBytesTx.setStatus("mandatory")
_MdmEvOutConnectTime_Type = Counter32
_MdmEvOutConnectTime_Object = MibTableColumn
mdmEvOutConnectTime = _MdmEvOutConnectTime_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 6, 10, 1, 1, 21),
    _MdmEvOutConnectTime_Type()
)
mdmEvOutConnectTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mdmEvOutConnectTime.setStatus("mandatory")
_MdmEvOutTotalBytesRx_Type = Counter32
_MdmEvOutTotalBytesRx_Object = MibTableColumn
mdmEvOutTotalBytesRx = _MdmEvOutTotalBytesRx_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 6, 10, 1, 1, 22),
    _MdmEvOutTotalBytesRx_Type()
)
mdmEvOutTotalBytesRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mdmEvOutTotalBytesRx.setStatus("mandatory")
_MdmEvOutTotalBytesTx_Type = Counter32
_MdmEvOutTotalBytesTx_Object = MibTableColumn
mdmEvOutTotalBytesTx = _MdmEvOutTotalBytesTx_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 6, 10, 1, 1, 23),
    _MdmEvOutTotalBytesTx_Type()
)
mdmEvOutTotalBytesTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mdmEvOutTotalBytesTx.setStatus("mandatory")
_MdmEvInConnAttemptFails_Type = Counter32
_MdmEvInConnAttemptFails_Object = MibTableColumn
mdmEvInConnAttemptFails = _MdmEvInConnAttemptFails_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 6, 10, 1, 1, 24),
    _MdmEvInConnAttemptFails_Type()
)
mdmEvInConnAttemptFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mdmEvInConnAttemptFails.setStatus("mandatory")
_MdmEvOutConnAttemptFails_Type = Counter32
_MdmEvOutConnAttemptFails_Object = MibTableColumn
mdmEvOutConnAttemptFails = _MdmEvOutConnAttemptFails_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 6, 10, 1, 1, 25),
    _MdmEvOutConnAttemptFails_Type()
)
mdmEvOutConnAttemptFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mdmEvOutConnAttemptFails.setStatus("mandatory")
_MdmEt_ObjectIdentity = ObjectIdentity
mdmEt = _MdmEt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 429, 1, 6, 11)
)
_MdmEtTable_Object = MibTable
mdmEtTable = _MdmEtTable_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 6, 11, 1)
)
if mibBuilder.loadTexts:
    mdmEtTable.setStatus("mandatory")
_MdmEtEntry_Object = MibTableRow
mdmEtEntry = _MdmEtEntry_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 6, 11, 1, 1)
)
mdmEtEntry.setIndexNames(
    (0, "MDM-MIB", "mdmEtIndex"),
)
if mibBuilder.loadTexts:
    mdmEtEntry.setStatus("mandatory")
_MdmEtIndex_Type = Integer32
_MdmEtIndex_Object = MibTableColumn
mdmEtIndex = _MdmEtIndex_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 6, 11, 1, 1, 1),
    _MdmEtIndex_Type()
)
mdmEtIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mdmEtIndex.setStatus("mandatory")


class _MdmEtDteIdleThresh_Type(Integer32):
    """Custom type mdmEtDteIdleThresh based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_MdmEtDteIdleThresh_Type.__name__ = "Integer32"
_MdmEtDteIdleThresh_Object = MibTableColumn
mdmEtDteIdleThresh = _MdmEtDteIdleThresh_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 6, 11, 1, 1, 2),
    _MdmEtDteIdleThresh_Type()
)
mdmEtDteIdleThresh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mdmEtDteIdleThresh.setStatus("mandatory")


class _MdmEtDtrFalseThresh_Type(Integer32):
    """Custom type mdmEtDtrFalseThresh based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_MdmEtDtrFalseThresh_Type.__name__ = "Integer32"
_MdmEtDtrFalseThresh_Object = MibTableColumn
mdmEtDtrFalseThresh = _MdmEtDtrFalseThresh_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 6, 11, 1, 1, 3),
    _MdmEtDtrFalseThresh_Type()
)
mdmEtDtrFalseThresh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mdmEtDtrFalseThresh.setStatus("mandatory")


class _MdmEtDtrTrueThresh_Type(Integer32):
    """Custom type mdmEtDtrTrueThresh based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_MdmEtDtrTrueThresh_Type.__name__ = "Integer32"
_MdmEtDtrTrueThresh_Object = MibTableColumn
mdmEtDtrTrueThresh = _MdmEtDtrTrueThresh_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 6, 11, 1, 1, 4),
    _MdmEtDtrTrueThresh_Type()
)
mdmEtDtrTrueThresh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mdmEtDtrTrueThresh.setStatus("mandatory")


class _MdmEtConnTimeLimit_Type(Integer32):
    """Custom type mdmEtConnTimeLimit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_MdmEtConnTimeLimit_Type.__name__ = "Integer32"
_MdmEtConnTimeLimit_Object = MibTableColumn
mdmEtConnTimeLimit = _MdmEtConnTimeLimit_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 6, 11, 1, 1, 5),
    _MdmEtConnTimeLimit_Type()
)
mdmEtConnTimeLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mdmEtConnTimeLimit.setStatus("mandatory")


class _MdmEtBlerThresh_Type(Integer32):
    """Custom type mdmEtBlerThresh based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_MdmEtBlerThresh_Type.__name__ = "Integer32"
_MdmEtBlerThresh_Object = MibTableColumn
mdmEtBlerThresh = _MdmEtBlerThresh_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 6, 11, 1, 1, 6),
    _MdmEtBlerThresh_Type()
)
mdmEtBlerThresh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mdmEtBlerThresh.setStatus("mandatory")


class _MdmEtFallbackThresh_Type(Integer32):
    """Custom type mdmEtFallbackThresh based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_MdmEtFallbackThresh_Type.__name__ = "Integer32"
_MdmEtFallbackThresh_Object = MibTableColumn
mdmEtFallbackThresh = _MdmEtFallbackThresh_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 6, 11, 1, 1, 7),
    _MdmEtFallbackThresh_Type()
)
mdmEtFallbackThresh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mdmEtFallbackThresh.setStatus("mandatory")
_MdmCd_ObjectIdentity = ObjectIdentity
mdmCd = _MdmCd_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 429, 1, 6, 12)
)
_MdmCdTable_Object = MibTable
mdmCdTable = _MdmCdTable_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 6, 12, 1)
)
if mibBuilder.loadTexts:
    mdmCdTable.setStatus("mandatory")
_MdmCdEntry_Object = MibTableRow
mdmCdEntry = _MdmCdEntry_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 6, 12, 1, 1)
)
mdmCdEntry.setIndexNames(
    (0, "MDM-MIB", "mdmCdIndex"),
)
if mibBuilder.loadTexts:
    mdmCdEntry.setStatus("mandatory")
_MdmCdIndex_Type = Integer32
_MdmCdIndex_Object = MibTableColumn
mdmCdIndex = _MdmCdIndex_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 6, 12, 1, 1, 1),
    _MdmCdIndex_Type()
)
mdmCdIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mdmCdIndex.setStatus("mandatory")


class _MdmCdMgtStationId_Type(OctetString):
    """Custom type mdmCdMgtStationId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_MdmCdMgtStationId_Type.__name__ = "OctetString"
_MdmCdMgtStationId_Object = MibTableColumn
mdmCdMgtStationId = _MdmCdMgtStationId_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 6, 12, 1, 1, 2),
    _MdmCdMgtStationId_Type()
)
mdmCdMgtStationId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mdmCdMgtStationId.setStatus("mandatory")
_MdmCdReqId_Type = Integer32
_MdmCdReqId_Object = MibTableColumn
mdmCdReqId = _MdmCdReqId_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 6, 12, 1, 1, 3),
    _MdmCdReqId_Type()
)
mdmCdReqId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mdmCdReqId.setStatus("mandatory")


class _MdmCdFunction_Type(Integer32):
    """Custom type mdmCdFunction based on Integer32"""
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
              25,
              26,
              27,
              33,
              34,
              35)
        )
    )
    namedValues = NamedValues(
        *(("endTest", 10),
          ("hardBusyAtDisable", 33),
          ("idlePhoneLine", 22),
          ("lclAnlgLpbk", 13),
          ("lclDgtlLpbk", 14),
          ("loadHwFlowDflt", 23),
          ("loadMnp10CllulrDflt", 25),
          ("loadSwFlowDflt", 24),
          ("loadV42CllulrFxdDflt", 27),
          ("loadV42CllulrMblDflt", 26),
          ("noCommand", 1),
          ("offHook", 6),
          ("onHook", 7),
          ("rcvTone", 9),
          ("restoreFromDflt", 4),
          ("restoreFromNvram", 5),
          ("restoreLineAt", 35),
          ("rmtDgtlLpbk", 15),
          ("rspndrTest102", 12),
          ("rspndrTest105", 11),
          ("selfTest", 16),
          ("sndTone", 8),
          ("softBusyAtDisable", 34),
          ("softwareReset", 2),
          ("storeToNvram", 3),
          ("testNVRAM", 19),
          ("testRam", 17),
          ("testRom", 18),
          ("v54LclAnlgLpbk", 20),
          ("v54RmtDgtlLpbk", 21))
    )


_MdmCdFunction_Type.__name__ = "Integer32"
_MdmCdFunction_Object = MibTableColumn
mdmCdFunction = _MdmCdFunction_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 6, 12, 1, 1, 4),
    _MdmCdFunction_Type()
)
mdmCdFunction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mdmCdFunction.setStatus("mandatory")


class _MdmCdForce_Type(Integer32):
    """Custom type mdmCdForce based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("force", 1),
          ("noForce", 2))
    )


_MdmCdForce_Type.__name__ = "Integer32"
_MdmCdForce_Object = MibTableColumn
mdmCdForce = _MdmCdForce_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 6, 12, 1, 1, 5),
    _MdmCdForce_Type()
)
mdmCdForce.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mdmCdForce.setStatus("mandatory")


class _MdmCdParam_Type(OctetString):
    """Custom type mdmCdParam based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 24),
    )


_MdmCdParam_Type.__name__ = "OctetString"
_MdmCdParam_Object = MibTableColumn
mdmCdParam = _MdmCdParam_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 6, 12, 1, 1, 6),
    _MdmCdParam_Type()
)
mdmCdParam.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mdmCdParam.setStatus("mandatory")


class _MdmCdResult_Type(Integer32):
    """Custom type mdmCdResult based on Integer32"""
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
        *(("aborted", 6),
          ("failed", 7),
          ("inProgress", 3),
          ("none", 1),
          ("notSupported", 4),
          ("success", 2),
          ("unAbleToRun", 5))
    )


_MdmCdResult_Type.__name__ = "Integer32"
_MdmCdResult_Object = MibTableColumn
mdmCdResult = _MdmCdResult_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 6, 12, 1, 1, 7),
    _MdmCdResult_Type()
)
mdmCdResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mdmCdResult.setStatus("mandatory")


class _MdmCdCode_Type(Integer32):
    """Custom type mdmCdCode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              6,
              8,
              12,
              13,
              14,
              17,
              20,
              22,
              24,
              25,
              31,
              51,
              52,
              53,
              54,
              73,
              89,
              90,
              91,
              92)
        )
    )
    namedValues = NamedValues(
        *(("connected", 14),
          ("deviceDisabled", 22),
          ("deviceInSecurityMode", 31),
          ("deviceInTestMode", 24),
          ("invalidFrequency", 89),
          ("noDTR", 52),
          ("noDialTone", 91),
          ("noError", 1),
          ("noLineDetected", 92),
          ("noLoopCurrent", 90),
          ("noLoopbackInARQ", 54),
          ("noRTS", 51),
          ("noResponse", 12),
          ("notConnected", 13),
          ("onLine", 17),
          ("pendingSoftwareDownload", 73),
          ("slotEmpty", 8),
          ("testFailed", 25),
          ("unable", 2),
          ("unrecognizedCommand", 6),
          ("unsupportedCommand", 20),
          ("wrongLoopbackSpeed", 53))
    )


_MdmCdCode_Type.__name__ = "Integer32"
_MdmCdCode_Object = MibTableColumn
mdmCdCode = _MdmCdCode_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 6, 12, 1, 1, 8),
    _MdmCdCode_Type()
)
mdmCdCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mdmCdCode.setStatus("mandatory")
_MdmTe_ObjectIdentity = ObjectIdentity
mdmTe = _MdmTe_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 429, 1, 6, 13)
)
_MdmTeTable_Object = MibTable
mdmTeTable = _MdmTeTable_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 6, 13, 1)
)
if mibBuilder.loadTexts:
    mdmTeTable.setStatus("mandatory")
_MdmTeEntry_Object = MibTableRow
mdmTeEntry = _MdmTeEntry_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 6, 13, 1, 1)
)
mdmTeEntry.setIndexNames(
    (0, "MDM-MIB", "mdmTeIndex"),
)
if mibBuilder.loadTexts:
    mdmTeEntry.setStatus("mandatory")
_MdmTeIndex_Type = Integer32
_MdmTeIndex_Object = MibTableColumn
mdmTeIndex = _MdmTeIndex_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 6, 13, 1, 1, 1),
    _MdmTeIndex_Type()
)
mdmTeIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mdmTeIndex.setStatus("mandatory")


class _MdmTeInConnEstablished_Type(Integer32):
    """Custom type mdmTeInConnEstablished based on Integer32"""
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
        *(("disableAll", 2),
          ("enableAll", 4),
          ("enableLog", 3),
          ("enableTrap", 1))
    )


_MdmTeInConnEstablished_Type.__name__ = "Integer32"
_MdmTeInConnEstablished_Object = MibTableColumn
mdmTeInConnEstablished = _MdmTeInConnEstablished_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 6, 13, 1, 1, 2),
    _MdmTeInConnEstablished_Type()
)
mdmTeInConnEstablished.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mdmTeInConnEstablished.setStatus("mandatory")


class _MdmTeOutConnEstablished_Type(Integer32):
    """Custom type mdmTeOutConnEstablished based on Integer32"""
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
        *(("disableAll", 2),
          ("enableAll", 4),
          ("enableLog", 3),
          ("enableTrap", 1))
    )


_MdmTeOutConnEstablished_Type.__name__ = "Integer32"
_MdmTeOutConnEstablished_Object = MibTableColumn
mdmTeOutConnEstablished = _MdmTeOutConnEstablished_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 6, 13, 1, 1, 3),
    _MdmTeOutConnEstablished_Type()
)
mdmTeOutConnEstablished.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mdmTeOutConnEstablished.setStatus("mandatory")


class _MdmTeInConnTerminated_Type(Integer32):
    """Custom type mdmTeInConnTerminated based on Integer32"""
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
        *(("disableAll", 2),
          ("enableAll", 4),
          ("enableLog", 3),
          ("enableTrap", 1))
    )


_MdmTeInConnTerminated_Type.__name__ = "Integer32"
_MdmTeInConnTerminated_Object = MibTableColumn
mdmTeInConnTerminated = _MdmTeInConnTerminated_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 6, 13, 1, 1, 4),
    _MdmTeInConnTerminated_Type()
)
mdmTeInConnTerminated.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mdmTeInConnTerminated.setStatus("mandatory")


class _MdmTeOutConnTerminated_Type(Integer32):
    """Custom type mdmTeOutConnTerminated based on Integer32"""
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
        *(("disableAll", 2),
          ("enableAll", 4),
          ("enableLog", 3),
          ("enableTrap", 1))
    )


_MdmTeOutConnTerminated_Type.__name__ = "Integer32"
_MdmTeOutConnTerminated_Object = MibTableColumn
mdmTeOutConnTerminated = _MdmTeOutConnTerminated_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 6, 13, 1, 1, 5),
    _MdmTeOutConnTerminated_Type()
)
mdmTeOutConnTerminated.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mdmTeOutConnTerminated.setStatus("mandatory")


class _MdmTeConnAttemptFailure_Type(Integer32):
    """Custom type mdmTeConnAttemptFailure based on Integer32"""
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
        *(("disableAll", 2),
          ("enableAll", 4),
          ("enableLog", 3),
          ("enableTrap", 1))
    )


_MdmTeConnAttemptFailure_Type.__name__ = "Integer32"
_MdmTeConnAttemptFailure_Object = MibTableColumn
mdmTeConnAttemptFailure = _MdmTeConnAttemptFailure_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 6, 13, 1, 1, 6),
    _MdmTeConnAttemptFailure_Type()
)
mdmTeConnAttemptFailure.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mdmTeConnAttemptFailure.setStatus("mandatory")


class _MdmTeConnLimitExpired_Type(Integer32):
    """Custom type mdmTeConnLimitExpired based on Integer32"""
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
        *(("disableAll", 2),
          ("enableAll", 4),
          ("enableLog", 3),
          ("enableTrap", 1))
    )


_MdmTeConnLimitExpired_Type.__name__ = "Integer32"
_MdmTeConnLimitExpired_Object = MibTableColumn
mdmTeConnLimitExpired = _MdmTeConnLimitExpired_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 6, 13, 1, 1, 7),
    _MdmTeConnLimitExpired_Type()
)
mdmTeConnLimitExpired.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mdmTeConnLimitExpired.setStatus("mandatory")


class _MdmTeDteXmitDataIdle_Type(Integer32):
    """Custom type mdmTeDteXmitDataIdle based on Integer32"""
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
        *(("disableAll", 2),
          ("enableAll", 4),
          ("enableLog", 3),
          ("enableTrap", 1))
    )


_MdmTeDteXmitDataIdle_Type.__name__ = "Integer32"
_MdmTeDteXmitDataIdle_Object = MibTableColumn
mdmTeDteXmitDataIdle = _MdmTeDteXmitDataIdle_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 6, 13, 1, 1, 8),
    _MdmTeDteXmitDataIdle_Type()
)
mdmTeDteXmitDataIdle.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mdmTeDteXmitDataIdle.setStatus("mandatory")


class _MdmTeDtrTrue_Type(Integer32):
    """Custom type mdmTeDtrTrue based on Integer32"""
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
        *(("disableAll", 2),
          ("enableAll", 4),
          ("enableLog", 3),
          ("enableTrap", 1))
    )


_MdmTeDtrTrue_Type.__name__ = "Integer32"
_MdmTeDtrTrue_Object = MibTableColumn
mdmTeDtrTrue = _MdmTeDtrTrue_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 6, 13, 1, 1, 9),
    _MdmTeDtrTrue_Type()
)
mdmTeDtrTrue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mdmTeDtrTrue.setStatus("mandatory")


class _MdmTeDtrFalse_Type(Integer32):
    """Custom type mdmTeDtrFalse based on Integer32"""
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
        *(("disableAll", 2),
          ("enableAll", 4),
          ("enableLog", 3),
          ("enableTrap", 1))
    )


_MdmTeDtrFalse_Type.__name__ = "Integer32"
_MdmTeDtrFalse_Object = MibTableColumn
mdmTeDtrFalse = _MdmTeDtrFalse_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 6, 13, 1, 1, 10),
    _MdmTeDtrFalse_Type()
)
mdmTeDtrFalse.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mdmTeDtrFalse.setStatus("mandatory")


class _MdmTeBlerCountAtThresh_Type(Integer32):
    """Custom type mdmTeBlerCountAtThresh based on Integer32"""
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
        *(("disableAll", 2),
          ("enableAll", 4),
          ("enableLog", 3),
          ("enableTrap", 1))
    )


_MdmTeBlerCountAtThresh_Type.__name__ = "Integer32"
_MdmTeBlerCountAtThresh_Object = MibTableColumn
mdmTeBlerCountAtThresh = _MdmTeBlerCountAtThresh_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 6, 13, 1, 1, 11),
    _MdmTeBlerCountAtThresh_Type()
)
mdmTeBlerCountAtThresh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mdmTeBlerCountAtThresh.setStatus("mandatory")


class _MdmTeFallbkCountAtThresh_Type(Integer32):
    """Custom type mdmTeFallbkCountAtThresh based on Integer32"""
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
        *(("disableAll", 2),
          ("enableAll", 4),
          ("enableLog", 3),
          ("enableTrap", 1))
    )


_MdmTeFallbkCountAtThresh_Type.__name__ = "Integer32"
_MdmTeFallbkCountAtThresh_Object = MibTableColumn
mdmTeFallbkCountAtThresh = _MdmTeFallbkCountAtThresh_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 6, 13, 1, 1, 12),
    _MdmTeFallbkCountAtThresh_Type()
)
mdmTeFallbkCountAtThresh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mdmTeFallbkCountAtThresh.setStatus("mandatory")


class _MdmTeNoDialTone_Type(Integer32):
    """Custom type mdmTeNoDialTone based on Integer32"""
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
        *(("disableAll", 2),
          ("enableAll", 4),
          ("enableLog", 3),
          ("enableTrap", 1))
    )


_MdmTeNoDialTone_Type.__name__ = "Integer32"
_MdmTeNoDialTone_Object = MibTableColumn
mdmTeNoDialTone = _MdmTeNoDialTone_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 6, 13, 1, 1, 13),
    _MdmTeNoDialTone_Type()
)
mdmTeNoDialTone.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mdmTeNoDialTone.setStatus("mandatory")


class _MdmTeNoLoopCurrent_Type(Integer32):
    """Custom type mdmTeNoLoopCurrent based on Integer32"""
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
        *(("disableAll", 2),
          ("enableAll", 4),
          ("enableLog", 3),
          ("enableTrap", 1))
    )


_MdmTeNoLoopCurrent_Type.__name__ = "Integer32"
_MdmTeNoLoopCurrent_Object = MibTableColumn
mdmTeNoLoopCurrent = _MdmTeNoLoopCurrent_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 6, 13, 1, 1, 14),
    _MdmTeNoLoopCurrent_Type()
)
mdmTeNoLoopCurrent.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mdmTeNoLoopCurrent.setStatus("mandatory")


class _MdmTeResetByDTE_Type(Integer32):
    """Custom type mdmTeResetByDTE based on Integer32"""
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
        *(("disableAll", 2),
          ("enableAll", 4),
          ("enableLog", 3),
          ("enableTrap", 1))
    )


_MdmTeResetByDTE_Type.__name__ = "Integer32"
_MdmTeResetByDTE_Object = MibTableColumn
mdmTeResetByDTE = _MdmTeResetByDTE_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 6, 13, 1, 1, 15),
    _MdmTeResetByDTE_Type()
)
mdmTeResetByDTE.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mdmTeResetByDTE.setStatus("mandatory")


class _MdmTeDialOutCallDur_Type(Integer32):
    """Custom type mdmTeDialOutCallDur based on Integer32"""
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
        *(("disableAll", 2),
          ("enableAll", 4),
          ("enableLog", 3),
          ("enableTrap", 1))
    )


_MdmTeDialOutCallDur_Type.__name__ = "Integer32"
_MdmTeDialOutCallDur_Object = MibTableColumn
mdmTeDialOutCallDur = _MdmTeDialOutCallDur_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 6, 13, 1, 1, 16),
    _MdmTeDialOutCallDur_Type()
)
mdmTeDialOutCallDur.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mdmTeDialOutCallDur.setStatus("mandatory")


class _MdmTeDialInCallDur_Type(Integer32):
    """Custom type mdmTeDialInCallDur based on Integer32"""
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
        *(("disableAll", 2),
          ("enableAll", 4),
          ("enableLog", 3),
          ("enableTrap", 1))
    )


_MdmTeDialInCallDur_Type.__name__ = "Integer32"
_MdmTeDialInCallDur_Object = MibTableColumn
mdmTeDialInCallDur = _MdmTeDialInCallDur_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 6, 13, 1, 1, 17),
    _MdmTeDialInCallDur_Type()
)
mdmTeDialInCallDur.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mdmTeDialInCallDur.setStatus("mandatory")


class _MdmTePbActive_Type(Integer32):
    """Custom type mdmTePbActive based on Integer32"""
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
        *(("disableAll", 2),
          ("enableAll", 4),
          ("enableLog", 3),
          ("enableTrap", 1))
    )


_MdmTePbActive_Type.__name__ = "Integer32"
_MdmTePbActive_Object = MibTableColumn
mdmTePbActive = _MdmTePbActive_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 6, 13, 1, 1, 18),
    _MdmTePbActive_Type()
)
mdmTePbActive.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mdmTePbActive.setStatus("optional")


class _MdmTePbLost_Type(Integer32):
    """Custom type mdmTePbLost based on Integer32"""
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
        *(("disableAll", 2),
          ("enableAll", 4),
          ("enableLog", 3),
          ("enableTrap", 1))
    )


_MdmTePbLost_Type.__name__ = "Integer32"
_MdmTePbLost_Object = MibTableColumn
mdmTePbLost = _MdmTePbLost_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 6, 13, 1, 1, 19),
    _MdmTePbLost_Type()
)
mdmTePbLost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mdmTePbLost.setStatus("optional")


class _MdmTeDteRingNoAns_Type(Integer32):
    """Custom type mdmTeDteRingNoAns based on Integer32"""
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
        *(("disableAll", 2),
          ("enableAll", 4),
          ("enableLog", 3),
          ("enableTrap", 1))
    )


_MdmTeDteRingNoAns_Type.__name__ = "Integer32"
_MdmTeDteRingNoAns_Object = MibTableColumn
mdmTeDteRingNoAns = _MdmTeDteRingNoAns_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 6, 13, 1, 1, 20),
    _MdmTeDteRingNoAns_Type()
)
mdmTeDteRingNoAns.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mdmTeDteRingNoAns.setStatus("optional")


class _MdmTePbClockLossEvent_Type(Integer32):
    """Custom type mdmTePbClockLossEvent based on Integer32"""
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
        *(("disableAll", 2),
          ("enableAll", 4),
          ("enableLog", 3),
          ("enableTrap", 1))
    )


_MdmTePbClockLossEvent_Type.__name__ = "Integer32"
_MdmTePbClockLossEvent_Object = MibTableColumn
mdmTePbClockLossEvent = _MdmTePbClockLossEvent_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 6, 13, 1, 1, 21),
    _MdmTePbClockLossEvent_Type()
)
mdmTePbClockLossEvent.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mdmTePbClockLossEvent.setStatus("mandatory")


class _MdmTePbClockRestoreEvent_Type(Integer32):
    """Custom type mdmTePbClockRestoreEvent based on Integer32"""
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
        *(("disableAll", 2),
          ("enableAll", 4),
          ("enableLog", 3),
          ("enableTrap", 1))
    )


_MdmTePbClockRestoreEvent_Type.__name__ = "Integer32"
_MdmTePbClockRestoreEvent_Object = MibTableColumn
mdmTePbClockRestoreEvent = _MdmTePbClockRestoreEvent_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 6, 13, 1, 1, 22),
    _MdmTePbClockRestoreEvent_Type()
)
mdmTePbClockRestoreEvent.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mdmTePbClockRestoreEvent.setStatus("mandatory")


class _MdmTeInConnAttemptFail_Type(Integer32):
    """Custom type mdmTeInConnAttemptFail based on Integer32"""
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
        *(("disableAll", 2),
          ("enableAll", 4),
          ("enableLog", 3),
          ("enableTrap", 1))
    )


_MdmTeInConnAttemptFail_Type.__name__ = "Integer32"
_MdmTeInConnAttemptFail_Object = MibTableColumn
mdmTeInConnAttemptFail = _MdmTeInConnAttemptFail_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 6, 13, 1, 1, 23),
    _MdmTeInConnAttemptFail_Type()
)
mdmTeInConnAttemptFail.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mdmTeInConnAttemptFail.setStatus("mandatory")


class _MdmTeOutConnAttemptFail_Type(Integer32):
    """Custom type mdmTeOutConnAttemptFail based on Integer32"""
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
        *(("disableAll", 2),
          ("enableAll", 4),
          ("enableLog", 3),
          ("enableTrap", 1))
    )


_MdmTeOutConnAttemptFail_Type.__name__ = "Integer32"
_MdmTeOutConnAttemptFail_Object = MibTableColumn
mdmTeOutConnAttemptFail = _MdmTeOutConnAttemptFail_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 6, 13, 1, 1, 24),
    _MdmTeOutConnAttemptFail_Type()
)
mdmTeOutConnAttemptFail.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mdmTeOutConnAttemptFail.setStatus("mandatory")


class _MdmTe105ResponderTest_Type(Integer32):
    """Custom type mdmTe105ResponderTest based on Integer32"""
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
        *(("disableAll", 2),
          ("enableAll", 4),
          ("enableLog", 3),
          ("enableTrap", 1))
    )


_MdmTe105ResponderTest_Type.__name__ = "Integer32"
_MdmTe105ResponderTest_Object = MibTableColumn
mdmTe105ResponderTest = _MdmTe105ResponderTest_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 6, 13, 1, 1, 25),
    _MdmTe105ResponderTest_Type()
)
mdmTe105ResponderTest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mdmTe105ResponderTest.setStatus("mandatory")
_MdmLs_ObjectIdentity = ObjectIdentity
mdmLs = _MdmLs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 429, 1, 6, 14)
)
_MdmLsTable_Object = MibTable
mdmLsTable = _MdmLsTable_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 6, 14, 1)
)
if mibBuilder.loadTexts:
    mdmLsTable.setStatus("mandatory")
_MdmLsTableEntry_Object = MibTableRow
mdmLsTableEntry = _MdmLsTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 6, 14, 1, 1)
)
mdmLsTableEntry.setIndexNames(
    (0, "MDM-MIB", "mdmLsIndex"),
)
if mibBuilder.loadTexts:
    mdmLsTableEntry.setStatus("mandatory")
_MdmLsIndex_Type = Integer32
_MdmLsIndex_Object = MibTableColumn
mdmLsIndex = _MdmLsIndex_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 6, 14, 1, 1, 1),
    _MdmLsIndex_Type()
)
mdmLsIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mdmLsIndex.setStatus("mandatory")


class _MdmLsSecurityEnable_Type(Integer32):
    """Custom type mdmLsSecurityEnable based on Integer32"""
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


_MdmLsSecurityEnable_Type.__name__ = "Integer32"
_MdmLsSecurityEnable_Object = MibTableColumn
mdmLsSecurityEnable = _MdmLsSecurityEnable_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 6, 14, 1, 1, 2),
    _MdmLsSecurityEnable_Type()
)
mdmLsSecurityEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mdmLsSecurityEnable.setStatus("mandatory")


class _MdmLsFallbackPromptEnable_Type(Integer32):
    """Custom type mdmLsFallbackPromptEnable based on Integer32"""
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


_MdmLsFallbackPromptEnable_Type.__name__ = "Integer32"
_MdmLsFallbackPromptEnable_Object = MibTableColumn
mdmLsFallbackPromptEnable = _MdmLsFallbackPromptEnable_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 6, 14, 1, 1, 3),
    _MdmLsFallbackPromptEnable_Type()
)
mdmLsFallbackPromptEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mdmLsFallbackPromptEnable.setStatus("mandatory")


class _MdmLsForcePromptEnable_Type(Integer32):
    """Custom type mdmLsForcePromptEnable based on Integer32"""
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


_MdmLsForcePromptEnable_Type.__name__ = "Integer32"
_MdmLsForcePromptEnable_Object = MibTableColumn
mdmLsForcePromptEnable = _MdmLsForcePromptEnable_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 6, 14, 1, 1, 4),
    _MdmLsForcePromptEnable_Type()
)
mdmLsForcePromptEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mdmLsForcePromptEnable.setStatus("mandatory")


class _MdmLsLocAccPasswdEnable_Type(Integer32):
    """Custom type mdmLsLocAccPasswdEnable based on Integer32"""
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


_MdmLsLocAccPasswdEnable_Type.__name__ = "Integer32"
_MdmLsLocAccPasswdEnable_Object = MibTableColumn
mdmLsLocAccPasswdEnable = _MdmLsLocAccPasswdEnable_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 6, 14, 1, 1, 5),
    _MdmLsLocAccPasswdEnable_Type()
)
mdmLsLocAccPasswdEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mdmLsLocAccPasswdEnable.setStatus("mandatory")


class _MdmLsDialBackEnable_Type(Integer32):
    """Custom type mdmLsDialBackEnable based on Integer32"""
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


_MdmLsDialBackEnable_Type.__name__ = "Integer32"
_MdmLsDialBackEnable_Object = MibTableColumn
mdmLsDialBackEnable = _MdmLsDialBackEnable_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 6, 14, 1, 1, 6),
    _MdmLsDialBackEnable_Type()
)
mdmLsDialBackEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mdmLsDialBackEnable.setStatus("mandatory")


class _MdmLsAutoPassPasswd_Type(DisplayString):
    """Custom type mdmLsAutoPassPasswd based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_MdmLsAutoPassPasswd_Type.__name__ = "DisplayString"
_MdmLsAutoPassPasswd_Object = MibTableColumn
mdmLsAutoPassPasswd = _MdmLsAutoPassPasswd_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 6, 14, 1, 1, 7),
    _MdmLsAutoPassPasswd_Type()
)
mdmLsAutoPassPasswd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mdmLsAutoPassPasswd.setStatus("mandatory")


class _MdmLsLocalAccessPasswd_Type(DisplayString):
    """Custom type mdmLsLocalAccessPasswd based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_MdmLsLocalAccessPasswd_Type.__name__ = "DisplayString"
_MdmLsLocalAccessPasswd_Object = MibTableColumn
mdmLsLocalAccessPasswd = _MdmLsLocalAccessPasswd_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 6, 14, 1, 1, 8),
    _MdmLsLocalAccessPasswd_Type()
)
mdmLsLocalAccessPasswd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mdmLsLocalAccessPasswd.setStatus("mandatory")


class _MdmLsAccountPasswd_Type(DisplayString):
    """Custom type mdmLsAccountPasswd based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_MdmLsAccountPasswd_Type.__name__ = "DisplayString"
_MdmLsAccountPasswd_Object = MibTableColumn
mdmLsAccountPasswd = _MdmLsAccountPasswd_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 6, 14, 1, 1, 9),
    _MdmLsAccountPasswd_Type()
)
mdmLsAccountPasswd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mdmLsAccountPasswd.setStatus("mandatory")
_MdmHs_ObjectIdentity = ObjectIdentity
mdmHs = _MdmHs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 429, 1, 6, 15)
)
_MdmHsTable_Object = MibTable
mdmHsTable = _MdmHsTable_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 6, 15, 1)
)
if mibBuilder.loadTexts:
    mdmHsTable.setStatus("optional")
_MdmHsEntry_Object = MibTableRow
mdmHsEntry = _MdmHsEntry_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 6, 15, 1, 1)
)
mdmHsEntry.setIndexNames(
    (0, "MDM-MIB", "mdmHsIndex"),
)
if mibBuilder.loadTexts:
    mdmHsEntry.setStatus("optional")
_MdmHsIndex_Type = Integer32
_MdmHsIndex_Object = MibTableColumn
mdmHsIndex = _MdmHsIndex_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 6, 15, 1, 1, 1),
    _MdmHsIndex_Type()
)
mdmHsIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mdmHsIndex.setStatus("optional")


class _MdmHsDialInEnable_Type(Integer32):
    """Custom type mdmHsDialInEnable based on Integer32"""
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
        *(("allowNoNMC", 2),
          ("busyOutNoNMC", 4),
          ("disable", 1),
          ("refuseNoNMC", 3))
    )


_MdmHsDialInEnable_Type.__name__ = "Integer32"
_MdmHsDialInEnable_Object = MibTableColumn
mdmHsDialInEnable = _MdmHsDialInEnable_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 6, 15, 1, 1, 2),
    _MdmHsDialInEnable_Type()
)
mdmHsDialInEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mdmHsDialInEnable.setStatus("optional")


class _MdmHsDialOutEnable_Type(Integer32):
    """Custom type mdmHsDialOutEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("allowNoNMC", 3),
          ("disable", 1),
          ("refuseNoNMC", 2))
    )


_MdmHsDialOutEnable_Type.__name__ = "Integer32"
_MdmHsDialOutEnable_Object = MibTableColumn
mdmHsDialOutEnable = _MdmHsDialOutEnable_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 6, 15, 1, 1, 3),
    _MdmHsDialOutEnable_Type()
)
mdmHsDialOutEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mdmHsDialOutEnable.setStatus("optional")


class _MdmHsDtrDcdDelay_Type(Integer32):
    """Custom type mdmHsDtrDcdDelay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_MdmHsDtrDcdDelay_Type.__name__ = "Integer32"
_MdmHsDtrDcdDelay_Object = MibTableColumn
mdmHsDtrDcdDelay = _MdmHsDtrDcdDelay_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 6, 15, 1, 1, 4),
    _MdmHsDtrDcdDelay_Type()
)
mdmHsDtrDcdDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mdmHsDtrDcdDelay.setStatus("optional")


class _MdmHsDtrDsrDelay_Type(Integer32):
    """Custom type mdmHsDtrDsrDelay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_MdmHsDtrDsrDelay_Type.__name__ = "Integer32"
_MdmHsDtrDsrDelay_Object = MibTableColumn
mdmHsDtrDsrDelay = _MdmHsDtrDsrDelay_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 6, 15, 1, 1, 5),
    _MdmHsDtrDsrDelay_Type()
)
mdmHsDtrDsrDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mdmHsDtrDsrDelay.setStatus("optional")
_MdmAutoResponse_ObjectIdentity = ObjectIdentity
mdmAutoResponse = _MdmAutoResponse_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 429, 1, 6, 16)
)
_MdmArTable_Object = MibTable
mdmArTable = _MdmArTable_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 6, 16, 1)
)
if mibBuilder.loadTexts:
    mdmArTable.setStatus("optional")
_MdmArEntry_Object = MibTableRow
mdmArEntry = _MdmArEntry_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 6, 16, 1, 1)
)
mdmArEntry.setIndexNames(
    (0, "MDM-MIB", "mdmArIndex"),
)
if mibBuilder.loadTexts:
    mdmArEntry.setStatus("optional")
_MdmArIndex_Type = Integer32
_MdmArIndex_Object = MibTableColumn
mdmArIndex = _MdmArIndex_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 6, 16, 1, 1, 1),
    _MdmArIndex_Type()
)
mdmArIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mdmArIndex.setStatus("optional")


class _MdmArIncomConnectEstab_Type(OctetString):
    """Custom type mdmArIncomConnectEstab based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_MdmArIncomConnectEstab_Type.__name__ = "OctetString"
_MdmArIncomConnectEstab_Object = MibTableColumn
mdmArIncomConnectEstab = _MdmArIncomConnectEstab_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 6, 16, 1, 1, 2),
    _MdmArIncomConnectEstab_Type()
)
mdmArIncomConnectEstab.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mdmArIncomConnectEstab.setStatus("optional")


class _MdmArOutgoConnectEstab_Type(OctetString):
    """Custom type mdmArOutgoConnectEstab based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_MdmArOutgoConnectEstab_Type.__name__ = "OctetString"
_MdmArOutgoConnectEstab_Object = MibTableColumn
mdmArOutgoConnectEstab = _MdmArOutgoConnectEstab_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 6, 16, 1, 1, 3),
    _MdmArOutgoConnectEstab_Type()
)
mdmArOutgoConnectEstab.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mdmArOutgoConnectEstab.setStatus("optional")


class _MdmArIncomConnectTerm_Type(OctetString):
    """Custom type mdmArIncomConnectTerm based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_MdmArIncomConnectTerm_Type.__name__ = "OctetString"
_MdmArIncomConnectTerm_Object = MibTableColumn
mdmArIncomConnectTerm = _MdmArIncomConnectTerm_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 6, 16, 1, 1, 4),
    _MdmArIncomConnectTerm_Type()
)
mdmArIncomConnectTerm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mdmArIncomConnectTerm.setStatus("optional")


class _MdmArOutgoConnectTerm_Type(OctetString):
    """Custom type mdmArOutgoConnectTerm based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_MdmArOutgoConnectTerm_Type.__name__ = "OctetString"
_MdmArOutgoConnectTerm_Object = MibTableColumn
mdmArOutgoConnectTerm = _MdmArOutgoConnectTerm_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 6, 16, 1, 1, 5),
    _MdmArOutgoConnectTerm_Type()
)
mdmArOutgoConnectTerm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mdmArOutgoConnectTerm.setStatus("optional")


class _MdmArConnectAttemptFail_Type(OctetString):
    """Custom type mdmArConnectAttemptFail based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_MdmArConnectAttemptFail_Type.__name__ = "OctetString"
_MdmArConnectAttemptFail_Object = MibTableColumn
mdmArConnectAttemptFail = _MdmArConnectAttemptFail_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 6, 16, 1, 1, 6),
    _MdmArConnectAttemptFail_Type()
)
mdmArConnectAttemptFail.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mdmArConnectAttemptFail.setStatus("optional")


class _MdmArConnectTimeExpire_Type(OctetString):
    """Custom type mdmArConnectTimeExpire based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_MdmArConnectTimeExpire_Type.__name__ = "OctetString"
_MdmArConnectTimeExpire_Object = MibTableColumn
mdmArConnectTimeExpire = _MdmArConnectTimeExpire_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 6, 16, 1, 1, 7),
    _MdmArConnectTimeExpire_Type()
)
mdmArConnectTimeExpire.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mdmArConnectTimeExpire.setStatus("optional")


class _MdmArResetByDte_Type(OctetString):
    """Custom type mdmArResetByDte based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_MdmArResetByDte_Type.__name__ = "OctetString"
_MdmArResetByDte_Object = MibTableColumn
mdmArResetByDte = _MdmArResetByDte_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 6, 16, 1, 1, 8),
    _MdmArResetByDte_Type()
)
mdmArResetByDte.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mdmArResetByDte.setStatus("optional")


class _MdmArDteXmitIdle_Type(OctetString):
    """Custom type mdmArDteXmitIdle based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_MdmArDteXmitIdle_Type.__name__ = "OctetString"
_MdmArDteXmitIdle_Object = MibTableColumn
mdmArDteXmitIdle = _MdmArDteXmitIdle_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 6, 16, 1, 1, 9),
    _MdmArDteXmitIdle_Type()
)
mdmArDteXmitIdle.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mdmArDteXmitIdle.setStatus("optional")


class _MdmArBlersAtThresh_Type(OctetString):
    """Custom type mdmArBlersAtThresh based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_MdmArBlersAtThresh_Type.__name__ = "OctetString"
_MdmArBlersAtThresh_Object = MibTableColumn
mdmArBlersAtThresh = _MdmArBlersAtThresh_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 6, 16, 1, 1, 10),
    _MdmArBlersAtThresh_Type()
)
mdmArBlersAtThresh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mdmArBlersAtThresh.setStatus("optional")


class _MdmArFbacksAtThresh_Type(OctetString):
    """Custom type mdmArFbacksAtThresh based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_MdmArFbacksAtThresh_Type.__name__ = "OctetString"
_MdmArFbacksAtThresh_Object = MibTableColumn
mdmArFbacksAtThresh = _MdmArFbacksAtThresh_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 6, 16, 1, 1, 11),
    _MdmArFbacksAtThresh_Type()
)
mdmArFbacksAtThresh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mdmArFbacksAtThresh.setStatus("optional")


class _MdmArDialOutLoginFail_Type(OctetString):
    """Custom type mdmArDialOutLoginFail based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_MdmArDialOutLoginFail_Type.__name__ = "OctetString"
_MdmArDialOutLoginFail_Object = MibTableColumn
mdmArDialOutLoginFail = _MdmArDialOutLoginFail_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 6, 16, 1, 1, 12),
    _MdmArDialOutLoginFail_Type()
)
mdmArDialOutLoginFail.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mdmArDialOutLoginFail.setStatus("optional")


class _MdmArDialOutRestrNum_Type(OctetString):
    """Custom type mdmArDialOutRestrNum based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_MdmArDialOutRestrNum_Type.__name__ = "OctetString"
_MdmArDialOutRestrNum_Object = MibTableColumn
mdmArDialOutRestrNum = _MdmArDialOutRestrNum_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 6, 16, 1, 1, 13),
    _MdmArDialOutRestrNum_Type()
)
mdmArDialOutRestrNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mdmArDialOutRestrNum.setStatus("optional")


class _MdmArDialInLoginFail_Type(OctetString):
    """Custom type mdmArDialInLoginFail based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_MdmArDialInLoginFail_Type.__name__ = "OctetString"
_MdmArDialInLoginFail_Object = MibTableColumn
mdmArDialInLoginFail = _MdmArDialInLoginFail_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 6, 16, 1, 1, 14),
    _MdmArDialInLoginFail_Type()
)
mdmArDialInLoginFail.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mdmArDialInLoginFail.setStatus("optional")


class _MdmArDialBackRestrNum_Type(OctetString):
    """Custom type mdmArDialBackRestrNum based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_MdmArDialBackRestrNum_Type.__name__ = "OctetString"
_MdmArDialBackRestrNum_Object = MibTableColumn
mdmArDialBackRestrNum = _MdmArDialBackRestrNum_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 6, 16, 1, 1, 15),
    _MdmArDialBackRestrNum_Type()
)
mdmArDialBackRestrNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mdmArDialBackRestrNum.setStatus("optional")


class _MdmArDialBackRestModem_Type(OctetString):
    """Custom type mdmArDialBackRestModem based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_MdmArDialBackRestModem_Type.__name__ = "OctetString"
_MdmArDialBackRestModem_Object = MibTableColumn
mdmArDialBackRestModem = _MdmArDialBackRestModem_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 6, 16, 1, 1, 16),
    _MdmArDialBackRestModem_Type()
)
mdmArDialBackRestModem.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mdmArDialBackRestModem.setStatus("optional")


class _MdmArLoginAttemptsExceed_Type(OctetString):
    """Custom type mdmArLoginAttemptsExceed based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_MdmArLoginAttemptsExceed_Type.__name__ = "OctetString"
_MdmArLoginAttemptsExceed_Object = MibTableColumn
mdmArLoginAttemptsExceed = _MdmArLoginAttemptsExceed_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 6, 16, 1, 1, 17),
    _MdmArLoginAttemptsExceed_Type()
)
mdmArLoginAttemptsExceed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mdmArLoginAttemptsExceed.setStatus("optional")


class _MdmArUserBlacklisted_Type(OctetString):
    """Custom type mdmArUserBlacklisted based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_MdmArUserBlacklisted_Type.__name__ = "OctetString"
_MdmArUserBlacklisted_Object = MibTableColumn
mdmArUserBlacklisted = _MdmArUserBlacklisted_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 6, 16, 1, 1, 18),
    _MdmArUserBlacklisted_Type()
)
mdmArUserBlacklisted.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mdmArUserBlacklisted.setStatus("optional")


class _MdmArAttmpLoginByBlistUsr_Type(OctetString):
    """Custom type mdmArAttmpLoginByBlistUsr based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_MdmArAttmpLoginByBlistUsr_Type.__name__ = "OctetString"
_MdmArAttmpLoginByBlistUsr_Object = MibTableColumn
mdmArAttmpLoginByBlistUsr = _MdmArAttmpLoginByBlistUsr_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 6, 16, 1, 1, 19),
    _MdmArAttmpLoginByBlistUsr_Type()
)
mdmArAttmpLoginByBlistUsr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mdmArAttmpLoginByBlistUsr.setStatus("optional")


class _MdmArRspAttemptLimExceed_Type(OctetString):
    """Custom type mdmArRspAttemptLimExceed based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_MdmArRspAttemptLimExceed_Type.__name__ = "OctetString"
_MdmArRspAttemptLimExceed_Object = MibTableColumn
mdmArRspAttemptLimExceed = _MdmArRspAttemptLimExceed_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 6, 16, 1, 1, 20),
    _MdmArRspAttemptLimExceed_Type()
)
mdmArRspAttemptLimExceed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mdmArRspAttemptLimExceed.setStatus("optional")


class _MdmArWatchdog_Type(OctetString):
    """Custom type mdmArWatchdog based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_MdmArWatchdog_Type.__name__ = "OctetString"
_MdmArWatchdog_Object = MibTableColumn
mdmArWatchdog = _MdmArWatchdog_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 6, 16, 1, 1, 21),
    _MdmArWatchdog_Type()
)
mdmArWatchdog.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mdmArWatchdog.setStatus("optional")


class _MdmArMgtBusFailure_Type(OctetString):
    """Custom type mdmArMgtBusFailure based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_MdmArMgtBusFailure_Type.__name__ = "OctetString"
_MdmArMgtBusFailure_Object = MibTableColumn
mdmArMgtBusFailure = _MdmArMgtBusFailure_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 6, 16, 1, 1, 22),
    _MdmArMgtBusFailure_Type()
)
mdmArMgtBusFailure.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mdmArMgtBusFailure.setStatus("optional")


class _MdmArDtrTrue_Type(OctetString):
    """Custom type mdmArDtrTrue based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_MdmArDtrTrue_Type.__name__ = "OctetString"
_MdmArDtrTrue_Object = MibTableColumn
mdmArDtrTrue = _MdmArDtrTrue_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 6, 16, 1, 1, 23),
    _MdmArDtrTrue_Type()
)
mdmArDtrTrue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mdmArDtrTrue.setStatus("optional")


class _MdmArDtrFalse_Type(OctetString):
    """Custom type mdmArDtrFalse based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_MdmArDtrFalse_Type.__name__ = "OctetString"
_MdmArDtrFalse_Object = MibTableColumn
mdmArDtrFalse = _MdmArDtrFalse_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 6, 16, 1, 1, 24),
    _MdmArDtrFalse_Type()
)
mdmArDtrFalse.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mdmArDtrFalse.setStatus("optional")


class _MdmArMdmRingNoAnswer_Type(OctetString):
    """Custom type mdmArMdmRingNoAnswer based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_MdmArMdmRingNoAnswer_Type.__name__ = "OctetString"
_MdmArMdmRingNoAnswer_Object = MibTableColumn
mdmArMdmRingNoAnswer = _MdmArMdmRingNoAnswer_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 6, 16, 1, 1, 25),
    _MdmArMdmRingNoAnswer_Type()
)
mdmArMdmRingNoAnswer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mdmArMdmRingNoAnswer.setStatus("optional")


class _MdmArDteRingNoAnswer_Type(OctetString):
    """Custom type mdmArDteRingNoAnswer based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_MdmArDteRingNoAnswer_Type.__name__ = "OctetString"
_MdmArDteRingNoAnswer_Object = MibTableColumn
mdmArDteRingNoAnswer = _MdmArDteRingNoAnswer_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 6, 16, 1, 1, 26),
    _MdmArDteRingNoAnswer_Type()
)
mdmArDteRingNoAnswer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mdmArDteRingNoAnswer.setStatus("optional")


class _MdmArNoDialTone_Type(OctetString):
    """Custom type mdmArNoDialTone based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_MdmArNoDialTone_Type.__name__ = "OctetString"
_MdmArNoDialTone_Object = MibTableColumn
mdmArNoDialTone = _MdmArNoDialTone_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 6, 16, 1, 1, 27),
    _MdmArNoDialTone_Type()
)
mdmArNoDialTone.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mdmArNoDialTone.setStatus("optional")


class _MdmArNoLoopCurrent_Type(OctetString):
    """Custom type mdmArNoLoopCurrent based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_MdmArNoLoopCurrent_Type.__name__ = "OctetString"
_MdmArNoLoopCurrent_Object = MibTableColumn
mdmArNoLoopCurrent = _MdmArNoLoopCurrent_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 6, 16, 1, 1, 28),
    _MdmArNoLoopCurrent_Type()
)
mdmArNoLoopCurrent.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mdmArNoLoopCurrent.setStatus("optional")


class _MdmArTimer1_Type(OctetString):
    """Custom type mdmArTimer1 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_MdmArTimer1_Type.__name__ = "OctetString"
_MdmArTimer1_Object = MibTableColumn
mdmArTimer1 = _MdmArTimer1_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 6, 16, 1, 1, 29),
    _MdmArTimer1_Type()
)
mdmArTimer1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mdmArTimer1.setStatus("optional")


class _MdmArTimer2_Type(OctetString):
    """Custom type mdmArTimer2 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_MdmArTimer2_Type.__name__ = "OctetString"
_MdmArTimer2_Object = MibTableColumn
mdmArTimer2 = _MdmArTimer2_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 6, 16, 1, 1, 30),
    _MdmArTimer2_Type()
)
mdmArTimer2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mdmArTimer2.setStatus("optional")


class _MdmArTimer3_Type(OctetString):
    """Custom type mdmArTimer3 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_MdmArTimer3_Type.__name__ = "OctetString"
_MdmArTimer3_Object = MibTableColumn
mdmArTimer3 = _MdmArTimer3_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 6, 16, 1, 1, 31),
    _MdmArTimer3_Type()
)
mdmArTimer3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mdmArTimer3.setStatus("optional")


class _MdmArTimer4_Type(OctetString):
    """Custom type mdmArTimer4 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_MdmArTimer4_Type.__name__ = "OctetString"
_MdmArTimer4_Object = MibTableColumn
mdmArTimer4 = _MdmArTimer4_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 6, 16, 1, 1, 32),
    _MdmArTimer4_Type()
)
mdmArTimer4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mdmArTimer4.setStatus("optional")


class _MdmArPacketBusActive_Type(OctetString):
    """Custom type mdmArPacketBusActive based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_MdmArPacketBusActive_Type.__name__ = "OctetString"
_MdmArPacketBusActive_Object = MibTableColumn
mdmArPacketBusActive = _MdmArPacketBusActive_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 6, 16, 1, 1, 33),
    _MdmArPacketBusActive_Type()
)
mdmArPacketBusActive.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mdmArPacketBusActive.setStatus("optional")


class _MdmArPacketBusLost_Type(OctetString):
    """Custom type mdmArPacketBusLost based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_MdmArPacketBusLost_Type.__name__ = "OctetString"
_MdmArPacketBusLost_Object = MibTableColumn
mdmArPacketBusLost = _MdmArPacketBusLost_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 6, 16, 1, 1, 34),
    _MdmArPacketBusLost_Type()
)
mdmArPacketBusLost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mdmArPacketBusLost.setStatus("optional")
_MdmCe_ObjectIdentity = ObjectIdentity
mdmCe = _MdmCe_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 429, 1, 6, 17)
)
_MdmCeTable_Object = MibTable
mdmCeTable = _MdmCeTable_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 6, 17, 1)
)
if mibBuilder.loadTexts:
    mdmCeTable.setStatus("mandatory")
_MdmCeEntry_Object = MibTableRow
mdmCeEntry = _MdmCeEntry_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 6, 17, 1, 1)
)
mdmCeEntry.setIndexNames(
    (0, "MDM-MIB", "mdmCeIndex"),
)
if mibBuilder.loadTexts:
    mdmCeEntry.setStatus("mandatory")
_MdmCeIndex_Type = Integer32
_MdmCeIndex_Object = MibTableColumn
mdmCeIndex = _MdmCeIndex_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 6, 17, 1, 1, 1),
    _MdmCeIndex_Type()
)
mdmCeIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mdmCeIndex.setStatus("mandatory")


class _MdmCeMnp10Dis_Type(Integer32):
    """Custom type mdmCeMnp10Dis based on Integer32"""
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


_MdmCeMnp10Dis_Type.__name__ = "Integer32"
_MdmCeMnp10Dis_Object = MibTableColumn
mdmCeMnp10Dis = _MdmCeMnp10Dis_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 6, 17, 1, 1, 2),
    _MdmCeMnp10Dis_Type()
)
mdmCeMnp10Dis.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mdmCeMnp10Dis.setStatus("mandatory")


class _MdmCeMnpxDis_Type(Integer32):
    """Custom type mdmCeMnpxDis based on Integer32"""
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


_MdmCeMnpxDis_Type.__name__ = "Integer32"
_MdmCeMnpxDis_Object = MibTableColumn
mdmCeMnpxDis = _MdmCeMnpxDis_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 6, 17, 1, 1, 3),
    _MdmCeMnpxDis_Type()
)
mdmCeMnpxDis.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mdmCeMnpxDis.setStatus("mandatory")


class _MdmCeComp_Type(Integer32):
    """Custom type mdmCeComp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("mnp5", 1),
          ("v42bis", 2))
    )


_MdmCeComp_Type.__name__ = "Integer32"
_MdmCeComp_Object = MibTableColumn
mdmCeComp = _MdmCeComp_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 6, 17, 1, 1, 4),
    _MdmCeComp_Type()
)
mdmCeComp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mdmCeComp.setStatus("mandatory")


class _MdmCeOperDis_Type(Integer32):
    """Custom type mdmCeOperDis based on Integer32"""
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


_MdmCeOperDis_Type.__name__ = "Integer32"
_MdmCeOperDis_Object = MibTableColumn
mdmCeOperDis = _MdmCeOperDis_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 6, 17, 1, 1, 5),
    _MdmCeOperDis_Type()
)
mdmCeOperDis.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mdmCeOperDis.setStatus("mandatory")


class _MdmCeLinkSpeed_Type(Integer32):
    """Custom type mdmCeLinkSpeed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("linkAt1200BpsV22", 2),
          ("linkAtHighSpeed", 1))
    )


_MdmCeLinkSpeed_Type.__name__ = "Integer32"
_MdmCeLinkSpeed_Object = MibTableColumn
mdmCeLinkSpeed = _MdmCeLinkSpeed_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 6, 17, 1, 1, 6),
    _MdmCeLinkSpeed_Type()
)
mdmCeLinkSpeed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mdmCeLinkSpeed.setStatus("mandatory")


class _MdmCeShortFormRules_Type(Integer32):
    """Custom type mdmCeShortFormRules based on Integer32"""
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
        *(("disable", 1),
          ("form1CodeWords512", 2),
          ("form2CodeWords1024", 3),
          ("form3CodeWords2048", 4))
    )


_MdmCeShortFormRules_Type.__name__ = "Integer32"
_MdmCeShortFormRules_Object = MibTableColumn
mdmCeShortFormRules = _MdmCeShortFormRules_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 6, 17, 1, 1, 7),
    _MdmCeShortFormRules_Type()
)
mdmCeShortFormRules.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mdmCeShortFormRules.setStatus("mandatory")


class _MdmCeDceBitraLim_Type(Integer32):
    """Custom type mdmCeDceBitraLim based on Integer32"""
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
        *(("bps12000", 5),
          ("bps14400", 6),
          ("bps4800", 2),
          ("bps7200", 3),
          ("bps9600", 4),
          ("maxDceRate", 1))
    )


_MdmCeDceBitraLim_Type.__name__ = "Integer32"
_MdmCeDceBitraLim_Object = MibTableColumn
mdmCeDceBitraLim = _MdmCeDceBitraLim_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 6, 17, 1, 1, 8),
    _MdmCeDceBitraLim_Type()
)
mdmCeDceBitraLim.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mdmCeDceBitraLim.setStatus("mandatory")


class _MdmCeDceTxLev_Type(Integer32):
    """Custom type mdmCeDceTxLev based on Integer32"""
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
              17)
        )
    )
    namedValues = NamedValues(
        *(("dBm10", 2),
          ("dBm11", 3),
          ("dBm12", 4),
          ("dBm13", 5),
          ("dBm14", 6),
          ("dBm15", 7),
          ("dBm16", 8),
          ("dBm17", 9),
          ("dBm18", 10),
          ("dBm19", 11),
          ("dBm20", 12),
          ("dBm21", 13),
          ("dBm22", 14),
          ("dBm23", 15),
          ("dBm24", 16),
          ("dBm25", 17),
          ("modemContrlTxLev", 1))
    )


_MdmCeDceTxLev_Type.__name__ = "Integer32"
_MdmCeDceTxLev_Object = MibTableColumn
mdmCeDceTxLev = _MdmCeDceTxLev_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 6, 17, 1, 1, 9),
    _MdmCeDceTxLev_Type()
)
mdmCeDceTxLev.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mdmCeDceTxLev.setStatus("mandatory")


class _MdmCeV42EtcDis_Type(Integer32):
    """Custom type mdmCeV42EtcDis based on Integer32"""
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


_MdmCeV42EtcDis_Type.__name__ = "Integer32"
_MdmCeV42EtcDis_Object = MibTableColumn
mdmCeV42EtcDis = _MdmCeV42EtcDis_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 6, 17, 1, 1, 10),
    _MdmCeV42EtcDis_Type()
)
mdmCeV42EtcDis.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mdmCeV42EtcDis.setStatus("mandatory")


class _MdmCeV42CellSite_Type(Integer32):
    """Custom type mdmCeV42CellSite based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("fixedSite", 1),
          ("mobileSite", 2))
    )


_MdmCeV42CellSite_Type.__name__ = "Integer32"
_MdmCeV42CellSite_Object = MibTableColumn
mdmCeV42CellSite = _MdmCeV42CellSite_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 6, 17, 1, 1, 11),
    _MdmCeV42CellSite_Type()
)
mdmCeV42CellSite.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mdmCeV42CellSite.setStatus("mandatory")


class _MdmCeV42EtcCallToneDis_Type(Integer32):
    """Custom type mdmCeV42EtcCallToneDis based on Integer32"""
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


_MdmCeV42EtcCallToneDis_Type.__name__ = "Integer32"
_MdmCeV42EtcCallToneDis_Object = MibTableColumn
mdmCeV42EtcCallToneDis = _MdmCeV42EtcCallToneDis_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 6, 17, 1, 1, 12),
    _MdmCeV42EtcCallToneDis_Type()
)
mdmCeV42EtcCallToneDis.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mdmCeV42EtcCallToneDis.setStatus("mandatory")


class _MdmCeV42EtcTxLevConDis_Type(Integer32):
    """Custom type mdmCeV42EtcTxLevConDis based on Integer32"""
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


_MdmCeV42EtcTxLevConDis_Type.__name__ = "Integer32"
_MdmCeV42EtcTxLevConDis_Object = MibTableColumn
mdmCeV42EtcTxLevConDis = _MdmCeV42EtcTxLevConDis_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 6, 17, 1, 1, 13),
    _MdmCeV42EtcTxLevConDis_Type()
)
mdmCeV42EtcTxLevConDis.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mdmCeV42EtcTxLevConDis.setStatus("mandatory")


class _MdmCeDceStartRate_Type(Integer32):
    """Custom type mdmCeDceStartRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("auto", 1),
          ("bps4800", 2),
          ("bps9600", 3))
    )


_MdmCeDceStartRate_Type.__name__ = "Integer32"
_MdmCeDceStartRate_Object = MibTableColumn
mdmCeDceStartRate = _MdmCeDceStartRate_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 6, 17, 1, 1, 14),
    _MdmCeDceStartRate_Type()
)
mdmCeDceStartRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mdmCeDceStartRate.setStatus("mandatory")


class _MdmCeV42DceTxDemDis_Type(Integer32):
    """Custom type mdmCeV42DceTxDemDis based on Integer32"""
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


_MdmCeV42DceTxDemDis_Type.__name__ = "Integer32"
_MdmCeV42DceTxDemDis_Object = MibTableColumn
mdmCeV42DceTxDemDis = _MdmCeV42DceTxDemDis_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 6, 17, 1, 1, 15),
    _MdmCeV42DceTxDemDis_Type()
)
mdmCeV42DceTxDemDis.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mdmCeV42DceTxDemDis.setStatus("mandatory")


class _MdmCeMnp10FallbackDis_Type(Integer32):
    """Custom type mdmCeMnp10FallbackDis based on Integer32"""
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


_MdmCeMnp10FallbackDis_Type.__name__ = "Integer32"
_MdmCeMnp10FallbackDis_Object = MibTableColumn
mdmCeMnp10FallbackDis = _MdmCeMnp10FallbackDis_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 6, 17, 1, 1, 16),
    _MdmCeMnp10FallbackDis_Type()
)
mdmCeMnp10FallbackDis.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mdmCeMnp10FallbackDis.setStatus("mandatory")


class _MdmCeMnp10FallforDis_Type(Integer32):
    """Custom type mdmCeMnp10FallforDis based on Integer32"""
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


_MdmCeMnp10FallforDis_Type.__name__ = "Integer32"
_MdmCeMnp10FallforDis_Object = MibTableColumn
mdmCeMnp10FallforDis = _MdmCeMnp10FallforDis_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 6, 17, 1, 1, 17),
    _MdmCeMnp10FallforDis_Type()
)
mdmCeMnp10FallforDis.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mdmCeMnp10FallforDis.setStatus("mandatory")


class _MdmCeDbNoEtcDis_Type(Integer32):
    """Custom type mdmCeDbNoEtcDis based on Integer32"""
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


_MdmCeDbNoEtcDis_Type.__name__ = "Integer32"
_MdmCeDbNoEtcDis_Object = MibTableColumn
mdmCeDbNoEtcDis = _MdmCeDbNoEtcDis_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 6, 17, 1, 1, 18),
    _MdmCeDbNoEtcDis_Type()
)
mdmCeDbNoEtcDis.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mdmCeDbNoEtcDis.setStatus("mandatory")


class _MdmCeMnpxDetPhEna_Type(Integer32):
    """Custom type mdmCeMnpxDetPhEna based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_MdmCeMnpxDetPhEna_Type.__name__ = "Integer32"
_MdmCeMnpxDetPhEna_Object = MibTableColumn
mdmCeMnpxDetPhEna = _MdmCeMnpxDetPhEna_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 6, 17, 1, 1, 19),
    _MdmCeMnpxDetPhEna_Type()
)
mdmCeMnpxDetPhEna.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mdmCeMnpxDetPhEna.setStatus("mandatory")
_MdmSts_ObjectIdentity = ObjectIdentity
mdmSts = _MdmSts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 429, 1, 6, 18)
)
_MdmStsTable_Object = MibTable
mdmStsTable = _MdmStsTable_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 6, 18, 1)
)
if mibBuilder.loadTexts:
    mdmStsTable.setStatus("mandatory")
_MdmStsEntry_Object = MibTableRow
mdmStsEntry = _MdmStsEntry_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 6, 18, 1, 1)
)
mdmStsEntry.setIndexNames(
    (0, "MDM-MIB", "mdmStsIndex"),
)
if mibBuilder.loadTexts:
    mdmStsEntry.setStatus("mandatory")
_MdmStsIndex_Type = Integer32
_MdmStsIndex_Object = MibTableColumn
mdmStsIndex = _MdmStsIndex_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 6, 18, 1, 1, 1),
    _MdmStsIndex_Type()
)
mdmStsIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mdmStsIndex.setStatus("mandatory")


class _MdmStsPbClock_Type(Integer32):
    """Custom type mdmStsPbClock based on Integer32"""
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
        *(("clockMaster", 2),
          ("clockSlave", 3),
          ("noClockPresent", 4),
          ("notSupported", 1))
    )


_MdmStsPbClock_Type.__name__ = "Integer32"
_MdmStsPbClock_Object = MibTableColumn
mdmStsPbClock = _MdmStsPbClock_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 6, 18, 1, 1, 2),
    _MdmStsPbClock_Type()
)
mdmStsPbClock.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mdmStsPbClock.setStatus("mandatory")
_MdmMa_ObjectIdentity = ObjectIdentity
mdmMa = _MdmMa_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 429, 1, 6, 19)
)
_MdmMaTable_Object = MibTable
mdmMaTable = _MdmMaTable_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 6, 19, 1)
)
if mibBuilder.loadTexts:
    mdmMaTable.setStatus("mandatory")
_MdmMaEntry_Object = MibTableRow
mdmMaEntry = _MdmMaEntry_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 6, 19, 1, 1)
)
mdmMaEntry.setIndexNames(
    (0, "MDM-MIB", "mdmMaIndex"),
)
if mibBuilder.loadTexts:
    mdmMaEntry.setStatus("mandatory")
_MdmMaIndex_Type = Integer32
_MdmMaIndex_Object = MibTableColumn
mdmMaIndex = _MdmMaIndex_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 6, 19, 1, 1, 1),
    _MdmMaIndex_Type()
)
mdmMaIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mdmMaIndex.setStatus("mandatory")


class _MdmMaChangeIndicator_Type(Integer32):
    """Custom type mdmMaChangeIndicator based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("cfgChanged", 2),
          ("cfgUnchanged", 3),
          ("notSupported", 1))
    )


_MdmMaChangeIndicator_Type.__name__ = "Integer32"
_MdmMaChangeIndicator_Object = MibTableColumn
mdmMaChangeIndicator = _MdmMaChangeIndicator_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 6, 19, 1, 1, 2),
    _MdmMaChangeIndicator_Type()
)
mdmMaChangeIndicator.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mdmMaChangeIndicator.setStatus("mandatory")


class _MdmMaChannelConfig_Type(Integer32):
    """Custom type mdmMaChannelConfig based on Integer32"""
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
        *(("group1", 1),
          ("group2", 2),
          ("group3", 3),
          ("group4", 4))
    )


_MdmMaChannelConfig_Type.__name__ = "Integer32"
_MdmMaChannelConfig_Object = MibTableColumn
mdmMaChannelConfig = _MdmMaChannelConfig_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 6, 19, 1, 1, 3),
    _MdmMaChannelConfig_Type()
)
mdmMaChannelConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mdmMaChannelConfig.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "MDM-MIB",
    **{"usr": usr,
       "nas": nas,
       "mdm": mdm,
       "mdmID": mdmID,
       "mdmIDTable": mdmIDTable,
       "mdmIDEntry": mdmIDEntry,
       "mdmIDIndex": mdmIDIndex,
       "mdmIDModel": mdmIDModel,
       "mdmIDCountry": mdmIDCountry,
       "mdmIDHardwareSerNum": mdmIDHardwareSerNum,
       "mdmIDHardwareRev": mdmIDHardwareRev,
       "mdmIDSupervisorSwRev": mdmIDSupervisorSwRev,
       "mdmIDDataPumpSwRev": mdmIDDataPumpSwRev,
       "mdmIDIoProcessorSwRev": mdmIDIoProcessorSwRev,
       "mdmIDSupervisorDate": mdmIDSupervisorDate,
       "mdmLi": mdmLi,
       "mdmLiTable": mdmLiTable,
       "mdmLiEntry": mdmLiEntry,
       "mdmLiIndex": mdmLiIndex,
       "mdmLiDialPause": mdmLiDialPause,
       "mdmLiCarrierRecDelay": mdmLiCarrierRecDelay,
       "mdmLiCarrierLoss": mdmLiCarrierLoss,
       "mdmLiToneDialTiming": mdmLiToneDialTiming,
       "mdmLiDteRxDataDelay": mdmLiDteRxDataDelay,
       "mdmLiTransmiter": mdmLiTransmiter,
       "mdmLiDialMode": mdmLiDialMode,
       "mdmLiGuardTone": mdmLiGuardTone,
       "mdmLiLeasedLine": mdmLiLeasedLine,
       "mdmLiLeasedLineRestDelay": mdmLiLeasedLineRestDelay,
       "mdmLiPulseMakeBreak": mdmLiPulseMakeBreak,
       "mdmLiAnswerTone": mdmLiAnswerTone,
       "mdmLiRemoteEscGuardTime": mdmLiRemoteEscGuardTime,
       "mdmLiRemoteEscChar": mdmLiRemoteEscChar,
       "mdmLiRemAccessLimit": mdmLiRemAccessLimit,
       "mdmLiRemPassword0": mdmLiRemPassword0,
       "mdmLiRemPassword1": mdmLiRemPassword1,
       "mdmLiTransmitLevel": mdmLiTransmitLevel,
       "mdmLiSrc": mdmLiSrc,
       "mdmDc": mdmDc,
       "mdmDcTable": mdmDcTable,
       "mdmDcEntry": mdmDcEntry,
       "mdmDcIndex": mdmDcIndex,
       "mdmDcDataCompression": mdmDcDataCompression,
       "mdmTf": mdmTf,
       "mdmTfTable": mdmTfTable,
       "mdmTfEntry": mdmTfEntry,
       "mdmTfIndex": mdmTfIndex,
       "mdmTfTest": mdmTfTest,
       "mdmTfTestTime": mdmTfTestTime,
       "mdmTfV54": mdmTfV54,
       "mdmTfV54Errors": mdmTfV54Errors,
       "mdmTfATG": mdmTfATG,
       "mdmTfDialInToneTest": mdmTfDialInToneTest,
       "mdmTfToneTestCallRef": mdmTfToneTestCallRef,
       "mdmTfToneTable": mdmTfToneTable,
       "mdmTfToneEntry": mdmTfToneEntry,
       "mdmTfToneIndex": mdmTfToneIndex,
       "mdmTfTxFreq": mdmTfTxFreq,
       "mdmTfTxAmpl": mdmTfTxAmpl,
       "mdmTfRxFreq": mdmTfRxFreq,
       "mdmTfRxAmpl": mdmTfRxAmpl,
       "mdmTfRspndrTable": mdmTfRspndrTable,
       "mdmTfRspndrEntry": mdmTfRspndrEntry,
       "mdmTfRspndrIndex": mdmTfRspndrIndex,
       "mdmTf404FarNearLvl": mdmTf404FarNearLvl,
       "mdmTf404NearFarLvl": mdmTf404NearFarLvl,
       "mdmTf1004FarNearLvl": mdmTf1004FarNearLvl,
       "mdmTf1004NearFarLvl": mdmTf1004NearFarLvl,
       "mdmTf2804FarNearLvl": mdmTf2804FarNearLvl,
       "mdmTf2804NearFarLvl": mdmTf2804NearFarLvl,
       "mdmTfCmsgFarNearLvl": mdmTfCmsgFarNearLvl,
       "mdmTfCmsgNearFarLvl": mdmTfCmsgNearFarLvl,
       "mdmTfCnotchFarNearLvl": mdmTfCnotchFarNearLvl,
       "mdmTfCnotchNearFarLvl": mdmTfCnotchNearFarLvl,
       "mdmtTfSigNoiseFarNearLvl": mdmtTfSigNoiseFarNearLvl,
       "mdmtTfSigNoiseNearFarLvl": mdmtTfSigNoiseNearFarLvl,
       "mdmTf404FarNearSts": mdmTf404FarNearSts,
       "mdmTf404NearFarSts": mdmTf404NearFarSts,
       "mdmTf1004FarNearSts": mdmTf1004FarNearSts,
       "mdmTf1004NearFarSts": mdmTf1004NearFarSts,
       "mdmTf2804FarNearSts": mdmTf2804FarNearSts,
       "mdmTf2804NearFarSts": mdmTf2804NearFarSts,
       "mdmTfCmsgFarNearSts": mdmTfCmsgFarNearSts,
       "mdmTfCmsgNearFarSts": mdmTfCmsgNearFarSts,
       "mdmTfCnotchFarNearSts": mdmTfCnotchFarNearSts,
       "mdmTfCnotchNearFarSts": mdmTfCnotchNearFarSts,
       "mdmTfSigNoiseFarNearSts": mdmTfSigNoiseFarNearSts,
       "mdmTfSigNoiseNearFarSts": mdmTfSigNoiseNearFarSts,
       "mdmTf0dB1004FarNearLvl": mdmTf0dB1004FarNearLvl,
       "mdmTf0dB1004NearFarLvl": mdmTf0dB1004NearFarLvl,
       "mdmTf0dB1004FarNearSts": mdmTf0dB1004FarNearSts,
       "mdmTf0dB1004NearFarSts": mdmTf0dB1004NearFarSts,
       "mdmDi": mdmDi,
       "mdmDiTable": mdmDiTable,
       "mdmDiEntry": mdmDiEntry,
       "mdmDiIndex": mdmDiIndex,
       "mdmDiEscCodeGuardTime": mdmDiEscCodeGuardTime,
       "mdmDiLocalEscChar": mdmDiLocalEscChar,
       "mdmDiCarriageRetChar": mdmDiCarriageRetChar,
       "mdmDiLineFeedChar": mdmDiLineFeedChar,
       "mdmDiBackspaceChar": mdmDiBackspaceChar,
       "mdmDiDelAsBackspace": mdmDiDelAsBackspace,
       "mdmDiResetOnDtrEna": mdmDiResetOnDtrEna,
       "mdmDiResultCodePauseDis": mdmDiResultCodePauseDis,
       "mdmDiInterbridgeEna": mdmDiInterbridgeEna,
       "mdmDiBreakLen": mdmDiBreakLen,
       "mdmDiXonChar": mdmDiXonChar,
       "mdmDiXoffChar": mdmDiXoffChar,
       "mdmDiDsrPulseTime": mdmDiDsrPulseTime,
       "mdmDiRtsCtsDelay": mdmDiRtsCtsDelay,
       "mdmDiHiSpeedResCodeEna": mdmDiHiSpeedResCodeEna,
       "mdmDiCmdLocalEchoEna": mdmDiCmdLocalEchoEna,
       "mdmDiDataModeEchoEna": mdmDiDataModeEchoEna,
       "mdmDiDteDataRateMode": mdmDiDteDataRateMode,
       "mdmDiCdOverride": mdmDiCdOverride,
       "mdmDiDtrOverride": mdmDiDtrOverride,
       "mdmDiDsrOverride": mdmDiDsrOverride,
       "mdmDiEiaLineStatus": mdmDiEiaLineStatus,
       "mdmDiTransmitFlowCntl": mdmDiTransmitFlowCntl,
       "mdmDiSoftwareRxFlowCntl": mdmDiSoftwareRxFlowCntl,
       "mdmDiHardwareRxFlowCntl": mdmDiHardwareRxFlowCntl,
       "mdmDiBreakHandling": mdmDiBreakHandling,
       "mdmDiDteNvramLock": mdmDiDteNvramLock,
       "mdmDiSerialFormat": mdmDiSerialFormat,
       "mdmDiDefaultDteDataRate": mdmDiDefaultDteDataRate,
       "mdmDiRemAccessMsg": mdmDiRemAccessMsg,
       "mdmDiV25DteDataRate": mdmDiV25DteDataRate,
       "mdmDiSrc": mdmDiSrc,
       "mdmDiSlot": mdmDiSlot,
       "mdmDiBusyClock": mdmDiBusyClock,
       "mdmDiAtString": mdmDiAtString,
       "mdmDiDtrRecognitionTime": mdmDiDtrRecognitionTime,
       "mdmSc": mdmSc,
       "mdmScTable": mdmScTable,
       "mdmScEntry": mdmScEntry,
       "mdmScIndex": mdmScIndex,
       "mdmScLinkRateSelect": mdmScLinkRateSelect,
       "mdmScNonArqBufSize": mdmScNonArqBufSize,
       "mdmScNonMnpDataCapture": mdmScNonMnpDataCapture,
       "mdmScSyncTimingSource": mdmScSyncTimingSource,
       "mdmScHstMod": mdmScHstMod,
       "mdmScHiFreqEq": mdmScHiFreqEq,
       "mdmScBackChanRate": mdmScBackChanRate,
       "mdmScV21Mod": mdmScV21Mod,
       "mdmScV32UnencodedMod": mdmScV32UnencodedMod,
       "mdmScV32Mod": mdmScV32Mod,
       "mdmScBell208": mdmScBell208,
       "mdmScV32Bis": mdmScV32Bis,
       "mdmScV32BisEnhance": mdmScV32BisEnhance,
       "mdmScV32QuickRetrain": mdmScV32QuickRetrain,
       "mdmScV23": mdmScV23,
       "mdmScHiSpeedModulation": mdmScHiSpeedModulation,
       "mdmScFallback": mdmScFallback,
       "mdmScV32TerboModeEnable": mdmScV32TerboModeEnable,
       "mdmScV34ModeEnable": mdmScV34ModeEnable,
       "mdmScVFCSymRate2400": mdmScVFCSymRate2400,
       "mdmScVFCSymRate2743": mdmScVFCSymRate2743,
       "mdmScVFCSymRate2800": mdmScVFCSymRate2800,
       "mdmScVFCSymRate3000": mdmScVFCSymRate3000,
       "mdmScVFCSymRate3200": mdmScVFCSymRate3200,
       "mdmScVFCSymRate3429": mdmScVFCSymRate3429,
       "mdmScVFC8S2DMapping": mdmScVFC8S2DMapping,
       "mdmScVFC16S4DMapping": mdmScVFC16S4DMapping,
       "mdmScVFC32S2DMapping": mdmScVFC32S2DMapping,
       "mdmScVFC64S4DMapping": mdmScVFC64S4DMapping,
       "mdmScVFCNonLinearCoding": mdmScVFCNonLinearCoding,
       "mdmScVFCTxLevelDeviation": mdmScVFCTxLevelDeviation,
       "mdmScVFCPreEmphasis": mdmScVFCPreEmphasis,
       "mdmScVFCPreCoding": mdmScVFCPreCoding,
       "mdmScVFCShaping": mdmScVFCShaping,
       "mdmScVFCModeEnable": mdmScVFCModeEnable,
       "mdmScV8": mdmScV8,
       "mdmSCV8CallIndicator": mdmSCV8CallIndicator,
       "mdmScV34pModeEnable": mdmScV34pModeEnable,
       "mdmSc300": mdmSc300,
       "mdmSc1200": mdmSc1200,
       "mdmSc2400": mdmSc2400,
       "mdmScHighSpeed": mdmScHighSpeed,
       "mdmScSelectiveReject": mdmScSelectiveReject,
       "mdmScPhExclusionDel": mdmScPhExclusionDel,
       "mdmScLinkRateAmpU": mdmScLinkRateAmpU,
       "mdmScLowerSpeedMin": mdmScLowerSpeedMin,
       "mdmScLowerSpeedMax": mdmScLowerSpeedMax,
       "mdmScX2Client": mdmScX2Client,
       "mdmScX2Server": mdmScX2Server,
       "mdmScX2Symmetric": mdmScX2Symmetric,
       "mdmScX2HighPowerConst": mdmScX2HighPowerConst,
       "mdmScPiafs": mdmScPiafs,
       "mdmScPiafsV42bis": mdmScPiafsV42bis,
       "mdmScTxPwrLvl": mdmScTxPwrLvl,
       "mdmScTxPwrLvlApplied": mdmScTxPwrLvlApplied,
       "mdmScX2Version2": mdmScX2Version2,
       "mdmScV34Fallback": mdmScV34Fallback,
       "mdmScV90Analogue": mdmScV90Analogue,
       "mdmScV90Digital": mdmScV90Digital,
       "mdmScV90AllDigital": mdmScV90AllDigital,
       "mdmCc": mdmCc,
       "mdmCcTable": mdmCcTable,
       "mdmCcEntry": mdmCcEntry,
       "mdmCcIndex": mdmCcIndex,
       "mdmCcDialDelay": mdmCcDialDelay,
       "mdmCcWaitForCarrier": mdmCcWaitForCarrier,
       "mdmCcInactivityTimer": mdmCcInactivityTimer,
       "mdmCcAutoDialOnDtrEna": mdmCcAutoDialOnDtrEna,
       "mdmCcAutoDialOnPwrUpEna": mdmCcAutoDialOnPwrUpEna,
       "mdmCcGhostPortLockEna": mdmCcGhostPortLockEna,
       "mdmCcQuietResultCodes": mdmCcQuietResultCodes,
       "mdmCcResponseMode": mdmCcResponseMode,
       "mdmCcResultCodeOptions": mdmCcResultCodeOptions,
       "mdmCcArqResultCodeMode": mdmCcArqResultCodeMode,
       "mdmCcEscCodeRsp": mdmCcEscCodeRsp,
       "mdmCcAtRecognition": mdmCcAtRecognition,
       "mdmCcMgmtSysMsgDis": mdmCcMgmtSysMsgDis,
       "mdmCcV32ToneDuration": mdmCcV32ToneDuration,
       "mdmCcAutoAnswer": mdmCcAutoAnswer,
       "mdmCcAnswerInOrigMode": mdmCcAnswerInOrigMode,
       "mdmCcArqBufWait": mdmCcArqBufWait,
       "mdmCcPhoneString0": mdmCcPhoneString0,
       "mdmCcPhoneString1": mdmCcPhoneString1,
       "mdmCcPhoneString2": mdmCcPhoneString2,
       "mdmCcPhoneString3": mdmCcPhoneString3,
       "mdmCcErrorCntlMode": mdmCcErrorCntlMode,
       "mdmCcMiMic": mdmCcMiMic,
       "mdmCcMnpWith1200": mdmCcMnpWith1200,
       "mdmCcMnpWith2400": mdmCcMnpWith2400,
       "mdmCcMnpWithV32": mdmCcMnpWithV32,
       "mdmCcMnpTimeout": mdmCcMnpTimeout,
       "mdmCcV21V23FallBackTimer": mdmCcV21V23FallBackTimer,
       "mdmCcAddnlAnswToneDur": mdmCcAddnlAnswToneDur,
       "mdmCcBillingDelayPeriod": mdmCcBillingDelayPeriod,
       "mdmCcCarrierAccessCode1": mdmCcCarrierAccessCode1,
       "mdmCcCarrierAccessCode2": mdmCcCarrierAccessCode2,
       "mdmCcCarrierAccessCode3": mdmCcCarrierAccessCode3,
       "mdmCcCallingInitStr1": mdmCcCallingInitStr1,
       "mdmCcCallingInitStr2": mdmCcCallingInitStr2,
       "mdmCcCallingInitStr3": mdmCcCallingInitStr3,
       "mdmCcCallingInitStr4": mdmCcCallingInitStr4,
       "mdmCcDataFaxMode": mdmCcDataFaxMode,
       "mdmCcT1CallSetupProc": mdmCcT1CallSetupProc,
       "mdmCcT1DialToneType": mdmCcT1DialToneType,
       "mdmCcT1KpStMfTones": mdmCcT1KpStMfTones,
       "mdmCcT1CallInitStrUse": mdmCcT1CallInitStrUse,
       "mdmCcT1CallInitStrBase": mdmCcT1CallInitStrBase,
       "mdmCcIntBlackListDis": mdmCcIntBlackListDis,
       "mdmCcOffHookRestrict": mdmCcOffHookRestrict,
       "mdmCcT1DialInAniDig": mdmCcT1DialInAniDig,
       "mdmCcT1DialInDnisDig": mdmCcT1DialInDnisDig,
       "mdmCcNoPbNoConnEna": mdmCcNoPbNoConnEna,
       "mdmCcIdleDiscPatt": mdmCcIdleDiscPatt,
       "mdmCcMnp10": mdmCcMnp10,
       "mdmCcMnp10Ec": mdmCcMnp10Ec,
       "mdmCcAtzPbHandling": mdmCcAtzPbHandling,
       "mdmCcDefltPRISlot": mdmCcDefltPRISlot,
       "mdmCcExtDTMFToneSupport": mdmCcExtDTMFToneSupport,
       "mdmCcDataOverVoice": mdmCcDataOverVoice,
       "mdmCc2100AnswerTone": mdmCc2100AnswerTone,
       "mdmCcEnableV120v42Bis": mdmCcEnableV120v42Bis,
       "mdmCcHdlcLicIe": mdmCcHdlcLicIe,
       "mdmCcDtmfTerminationTone": mdmCcDtmfTerminationTone,
       "mdmCcAfaxMaxRateSrvOpt20": mdmCcAfaxMaxRateSrvOpt20,
       "mdmCcAfaxMaxRateSrvOpt21": mdmCcAfaxMaxRateSrvOpt21,
       "mdmEc": mdmEc,
       "mdmEcTable": mdmEcTable,
       "mdmEcEntry": mdmEcEntry,
       "mdmEcIndex": mdmEcIndex,
       "mdmEcMnp3Dis": mdmEcMnp3Dis,
       "mdmEcMnp4Dis": mdmEcMnp4Dis,
       "mdmEcMnpUnusual": mdmEcMnpUnusual,
       "mdmEcV42MnpHandshake": mdmEcV42MnpHandshake,
       "mdmCs": mdmCs,
       "mdmCsTable": mdmCsTable,
       "mdmCsEntry": mdmCsEntry,
       "mdmCsIndex": mdmCsIndex,
       "mdmCsStatus": mdmCsStatus,
       "mdmCsLastNumberDialedOut": mdmCsLastNumberDialedOut,
       "mdmCsLastNumberDialedIn": mdmCsLastNumberDialedIn,
       "mdmCsLastCallingPartyNum": mdmCsLastCallingPartyNum,
       "mdmCsOriginateAnswer": mdmCsOriginateAnswer,
       "mdmCsRings": mdmCsRings,
       "mdmCsDisconnectReason": mdmCsDisconnectReason,
       "mdmCsConnectFailReason": mdmCsConnectFailReason,
       "mdmCsInitialTxLinkRate": mdmCsInitialTxLinkRate,
       "mdmCsInitialRxLinkRate": mdmCsInitialRxLinkRate,
       "mdmCsFinalTxLinkRate": mdmCsFinalTxLinkRate,
       "mdmCsFinalRxLinkRate": mdmCsFinalRxLinkRate,
       "mdmCsModulationType": mdmCsModulationType,
       "mdmCsSyncAsyncModeUsed": mdmCsSyncAsyncModeUsed,
       "mdmCsErrorControlType": mdmCsErrorControlType,
       "mdmCsCompressionType": mdmCsCompressionType,
       "mdmCsEqualizationType": mdmCsEqualizationType,
       "mdmCsFallbackEnabled": mdmCsFallbackEnabled,
       "mdmCsCharsSent": mdmCsCharsSent,
       "mdmCsCharsReceived": mdmCsCharsReceived,
       "mdmCsOctetsSent": mdmCsOctetsSent,
       "mdmCsOctetsReceived": mdmCsOctetsReceived,
       "mdmCsBlocksSent": mdmCsBlocksSent,
       "mdmCsBlocksReceived": mdmCsBlocksReceived,
       "mdmCsBlocksResent": mdmCsBlocksResent,
       "mdmCsRetrainsRequested": mdmCsRetrainsRequested,
       "mdmCsRetrainsGranted": mdmCsRetrainsGranted,
       "mdmCsLineReversalQty": mdmCsLineReversalQty,
       "mdmCsCharsLost": mdmCsCharsLost,
       "mdmCsBackChannelRate": mdmCsBackChannelRate,
       "mdmCsBlerQty": mdmCsBlerQty,
       "mdmCsLinkTimeoutQty": mdmCsLinkTimeoutQty,
       "mdmCsFallbackQty": mdmCsFallbackQty,
       "mdmCsUpshiftQty": mdmCsUpshiftQty,
       "mdmCsLinkNakQty": mdmCsLinkNakQty,
       "mdmCsGainHitCount": mdmCsGainHitCount,
       "mdmCsSecurityUserName": mdmCsSecurityUserName,
       "mdmCsCallDuration": mdmCsCallDuration,
       "mdmCsCallRefNum": mdmCsCallRefNum,
       "mdmCsPriCardSlot": mdmCsPriCardSlot,
       "mdmCsTDMTimeSlot": mdmCsTDMTimeSlot,
       "mdmCsPriCardSpanLine": mdmCsPriCardSpanLine,
       "mdmCsBChannelUsed": mdmCsBChannelUsed,
       "mdmCsQCarrFreqTx": mdmCsQCarrFreqTx,
       "mdmCsQCarrFreqRx": mdmCsQCarrFreqRx,
       "mdmCsQSymRateTx": mdmCsQSymRateTx,
       "mdmCsQSymRateRx": mdmCsQSymRateRx,
       "mdmCsQTrellisTx": mdmCsQTrellisTx,
       "mdmCsQTrellisRx": mdmCsQTrellisRx,
       "mdmCsQNonLinCdTx": mdmCsQNonLinCdTx,
       "mdmCsQNonLinCdRx": mdmCsQNonLinCdRx,
       "mdmCsQPrecodingTx": mdmCsQPrecodingTx,
       "mdmCsQPrecodingRx": mdmCsQPrecodingRx,
       "mdmCsQShapingTx": mdmCsQShapingTx,
       "mdmCsQShapingRx": mdmCsQShapingRx,
       "mdmCsQPreemphTx": mdmCsQPreemphTx,
       "mdmCsQPreemphRx": mdmCsQPreemphRx,
       "mdmCsQRxLevel": mdmCsQRxLevel,
       "mdmCsQTxLevel": mdmCsQTxLevel,
       "mdmCsQSNR": mdmCsQSNR,
       "mdmCsQNearEcho": mdmCsQNearEcho,
       "mdmCsQFarEcho": mdmCsQFarEcho,
       "mdmCsQRndTripDly": mdmCsQRndTripDly,
       "mdmCsQPacketSizeCurr": mdmCsQPacketSizeCurr,
       "mdmCsQPacketSizeLow": mdmCsQPacketSizeLow,
       "mdmCsQPacketSizeHigh": mdmCsQPacketSizeHigh,
       "mdmCsQCellTxLevelCurr": mdmCsQCellTxLevelCurr,
       "mdmCsQCellTxLevelLow": mdmCsQCellTxLevelLow,
       "mdmCsQCellTxLevelHigh": mdmCsQCellTxLevelHigh,
       "mdmCsQSNRLevelCurr": mdmCsQSNRLevelCurr,
       "mdmCsQSNRLevelLow": mdmCsQSNRLevelLow,
       "mdmCsQSNRLevelHigh": mdmCsQSNRLevelHigh,
       "mdmCsQCellularProt": mdmCsQCellularProt,
       "mdmCsFreqProbeData": mdmCsFreqProbeData,
       "mdmCsLevelProbeData": mdmCsLevelProbeData,
       "mdmCsQTimingOffset": mdmCsQTimingOffset,
       "mdmCsQCarrierOffset": mdmCsQCarrierOffset,
       "mdmCsQCoding": mdmCsQCoding,
       "mdmCsTrainingInfo": mdmCsTrainingInfo,
       "mdmCsX2signature": mdmCsX2signature,
       "mdmCsX2Status": mdmCsX2Status,
       "mdmCsCallType": mdmCsCallType,
       "mdmCsCallStartTime": mdmCsCallStartTime,
       "mdmCsCallEndTime": mdmCsCallEndTime,
       "mdmCsDigitalPadAttenuated": mdmCsDigitalPadAttenuated,
       "mdmCsInitModulationType": mdmCsInitModulationType,
       "mdmCsRxMinSpeed": mdmCsRxMinSpeed,
       "mdmCsRxMaxSpeed": mdmCsRxMaxSpeed,
       "mdmCsTxMinSpeed": mdmCsTxMinSpeed,
       "mdmCsTxMaxSpeed": mdmCsTxMaxSpeed,
       "mdmCsCollectedDTMFDigits": mdmCsCollectedDTMFDigits,
       "mdmEv": mdmEv,
       "mdmEvTable": mdmEvTable,
       "mdmEvEntry": mdmEvEntry,
       "mdmEvIndex": mdmEvIndex,
       "mdmEvWatchdogTimouts": mdmEvWatchdogTimouts,
       "mdmEvDteIdleTimouts": mdmEvDteIdleTimouts,
       "mdmEvInConnectEstabs": mdmEvInConnectEstabs,
       "mdmEvOutConnectEstabs": mdmEvOutConnectEstabs,
       "mdmEvInConnectTerms": mdmEvInConnectTerms,
       "mdmEvOutConnectTerms": mdmEvOutConnectTerms,
       "mdmEvConnectAttemptFails": mdmEvConnectAttemptFails,
       "mdmEvConnectTimouts": mdmEvConnectTimouts,
       "mdmEvMgmtBusFailures": mdmEvMgmtBusFailures,
       "mdmEvResetByDtes": mdmEvResetByDtes,
       "mdmEvDtrFalses": mdmEvDtrFalses,
       "mdmEvDtrTrues": mdmEvDtrTrues,
       "mdmEvNoTones": mdmEvNoTones,
       "mdmEvNoLoops": mdmEvNoLoops,
       "mdmEvBlers": mdmEvBlers,
       "mdmEvFallBacks": mdmEvFallBacks,
       "mdmEvInConnectTime": mdmEvInConnectTime,
       "mdmEvInTotalBytesRx": mdmEvInTotalBytesRx,
       "mdmEvInTotalBytesTx": mdmEvInTotalBytesTx,
       "mdmEvOutConnectTime": mdmEvOutConnectTime,
       "mdmEvOutTotalBytesRx": mdmEvOutTotalBytesRx,
       "mdmEvOutTotalBytesTx": mdmEvOutTotalBytesTx,
       "mdmEvInConnAttemptFails": mdmEvInConnAttemptFails,
       "mdmEvOutConnAttemptFails": mdmEvOutConnAttemptFails,
       "mdmEt": mdmEt,
       "mdmEtTable": mdmEtTable,
       "mdmEtEntry": mdmEtEntry,
       "mdmEtIndex": mdmEtIndex,
       "mdmEtDteIdleThresh": mdmEtDteIdleThresh,
       "mdmEtDtrFalseThresh": mdmEtDtrFalseThresh,
       "mdmEtDtrTrueThresh": mdmEtDtrTrueThresh,
       "mdmEtConnTimeLimit": mdmEtConnTimeLimit,
       "mdmEtBlerThresh": mdmEtBlerThresh,
       "mdmEtFallbackThresh": mdmEtFallbackThresh,
       "mdmCd": mdmCd,
       "mdmCdTable": mdmCdTable,
       "mdmCdEntry": mdmCdEntry,
       "mdmCdIndex": mdmCdIndex,
       "mdmCdMgtStationId": mdmCdMgtStationId,
       "mdmCdReqId": mdmCdReqId,
       "mdmCdFunction": mdmCdFunction,
       "mdmCdForce": mdmCdForce,
       "mdmCdParam": mdmCdParam,
       "mdmCdResult": mdmCdResult,
       "mdmCdCode": mdmCdCode,
       "mdmTe": mdmTe,
       "mdmTeTable": mdmTeTable,
       "mdmTeEntry": mdmTeEntry,
       "mdmTeIndex": mdmTeIndex,
       "mdmTeInConnEstablished": mdmTeInConnEstablished,
       "mdmTeOutConnEstablished": mdmTeOutConnEstablished,
       "mdmTeInConnTerminated": mdmTeInConnTerminated,
       "mdmTeOutConnTerminated": mdmTeOutConnTerminated,
       "mdmTeConnAttemptFailure": mdmTeConnAttemptFailure,
       "mdmTeConnLimitExpired": mdmTeConnLimitExpired,
       "mdmTeDteXmitDataIdle": mdmTeDteXmitDataIdle,
       "mdmTeDtrTrue": mdmTeDtrTrue,
       "mdmTeDtrFalse": mdmTeDtrFalse,
       "mdmTeBlerCountAtThresh": mdmTeBlerCountAtThresh,
       "mdmTeFallbkCountAtThresh": mdmTeFallbkCountAtThresh,
       "mdmTeNoDialTone": mdmTeNoDialTone,
       "mdmTeNoLoopCurrent": mdmTeNoLoopCurrent,
       "mdmTeResetByDTE": mdmTeResetByDTE,
       "mdmTeDialOutCallDur": mdmTeDialOutCallDur,
       "mdmTeDialInCallDur": mdmTeDialInCallDur,
       "mdmTePbActive": mdmTePbActive,
       "mdmTePbLost": mdmTePbLost,
       "mdmTeDteRingNoAns": mdmTeDteRingNoAns,
       "mdmTePbClockLossEvent": mdmTePbClockLossEvent,
       "mdmTePbClockRestoreEvent": mdmTePbClockRestoreEvent,
       "mdmTeInConnAttemptFail": mdmTeInConnAttemptFail,
       "mdmTeOutConnAttemptFail": mdmTeOutConnAttemptFail,
       "mdmTe105ResponderTest": mdmTe105ResponderTest,
       "mdmLs": mdmLs,
       "mdmLsTable": mdmLsTable,
       "mdmLsTableEntry": mdmLsTableEntry,
       "mdmLsIndex": mdmLsIndex,
       "mdmLsSecurityEnable": mdmLsSecurityEnable,
       "mdmLsFallbackPromptEnable": mdmLsFallbackPromptEnable,
       "mdmLsForcePromptEnable": mdmLsForcePromptEnable,
       "mdmLsLocAccPasswdEnable": mdmLsLocAccPasswdEnable,
       "mdmLsDialBackEnable": mdmLsDialBackEnable,
       "mdmLsAutoPassPasswd": mdmLsAutoPassPasswd,
       "mdmLsLocalAccessPasswd": mdmLsLocalAccessPasswd,
       "mdmLsAccountPasswd": mdmLsAccountPasswd,
       "mdmHs": mdmHs,
       "mdmHsTable": mdmHsTable,
       "mdmHsEntry": mdmHsEntry,
       "mdmHsIndex": mdmHsIndex,
       "mdmHsDialInEnable": mdmHsDialInEnable,
       "mdmHsDialOutEnable": mdmHsDialOutEnable,
       "mdmHsDtrDcdDelay": mdmHsDtrDcdDelay,
       "mdmHsDtrDsrDelay": mdmHsDtrDsrDelay,
       "mdmAutoResponse": mdmAutoResponse,
       "mdmArTable": mdmArTable,
       "mdmArEntry": mdmArEntry,
       "mdmArIndex": mdmArIndex,
       "mdmArIncomConnectEstab": mdmArIncomConnectEstab,
       "mdmArOutgoConnectEstab": mdmArOutgoConnectEstab,
       "mdmArIncomConnectTerm": mdmArIncomConnectTerm,
       "mdmArOutgoConnectTerm": mdmArOutgoConnectTerm,
       "mdmArConnectAttemptFail": mdmArConnectAttemptFail,
       "mdmArConnectTimeExpire": mdmArConnectTimeExpire,
       "mdmArResetByDte": mdmArResetByDte,
       "mdmArDteXmitIdle": mdmArDteXmitIdle,
       "mdmArBlersAtThresh": mdmArBlersAtThresh,
       "mdmArFbacksAtThresh": mdmArFbacksAtThresh,
       "mdmArDialOutLoginFail": mdmArDialOutLoginFail,
       "mdmArDialOutRestrNum": mdmArDialOutRestrNum,
       "mdmArDialInLoginFail": mdmArDialInLoginFail,
       "mdmArDialBackRestrNum": mdmArDialBackRestrNum,
       "mdmArDialBackRestModem": mdmArDialBackRestModem,
       "mdmArLoginAttemptsExceed": mdmArLoginAttemptsExceed,
       "mdmArUserBlacklisted": mdmArUserBlacklisted,
       "mdmArAttmpLoginByBlistUsr": mdmArAttmpLoginByBlistUsr,
       "mdmArRspAttemptLimExceed": mdmArRspAttemptLimExceed,
       "mdmArWatchdog": mdmArWatchdog,
       "mdmArMgtBusFailure": mdmArMgtBusFailure,
       "mdmArDtrTrue": mdmArDtrTrue,
       "mdmArDtrFalse": mdmArDtrFalse,
       "mdmArMdmRingNoAnswer": mdmArMdmRingNoAnswer,
       "mdmArDteRingNoAnswer": mdmArDteRingNoAnswer,
       "mdmArNoDialTone": mdmArNoDialTone,
       "mdmArNoLoopCurrent": mdmArNoLoopCurrent,
       "mdmArTimer1": mdmArTimer1,
       "mdmArTimer2": mdmArTimer2,
       "mdmArTimer3": mdmArTimer3,
       "mdmArTimer4": mdmArTimer4,
       "mdmArPacketBusActive": mdmArPacketBusActive,
       "mdmArPacketBusLost": mdmArPacketBusLost,
       "mdmCe": mdmCe,
       "mdmCeTable": mdmCeTable,
       "mdmCeEntry": mdmCeEntry,
       "mdmCeIndex": mdmCeIndex,
       "mdmCeMnp10Dis": mdmCeMnp10Dis,
       "mdmCeMnpxDis": mdmCeMnpxDis,
       "mdmCeComp": mdmCeComp,
       "mdmCeOperDis": mdmCeOperDis,
       "mdmCeLinkSpeed": mdmCeLinkSpeed,
       "mdmCeShortFormRules": mdmCeShortFormRules,
       "mdmCeDceBitraLim": mdmCeDceBitraLim,
       "mdmCeDceTxLev": mdmCeDceTxLev,
       "mdmCeV42EtcDis": mdmCeV42EtcDis,
       "mdmCeV42CellSite": mdmCeV42CellSite,
       "mdmCeV42EtcCallToneDis": mdmCeV42EtcCallToneDis,
       "mdmCeV42EtcTxLevConDis": mdmCeV42EtcTxLevConDis,
       "mdmCeDceStartRate": mdmCeDceStartRate,
       "mdmCeV42DceTxDemDis": mdmCeV42DceTxDemDis,
       "mdmCeMnp10FallbackDis": mdmCeMnp10FallbackDis,
       "mdmCeMnp10FallforDis": mdmCeMnp10FallforDis,
       "mdmCeDbNoEtcDis": mdmCeDbNoEtcDis,
       "mdmCeMnpxDetPhEna": mdmCeMnpxDetPhEna,
       "mdmSts": mdmSts,
       "mdmStsTable": mdmStsTable,
       "mdmStsEntry": mdmStsEntry,
       "mdmStsIndex": mdmStsIndex,
       "mdmStsPbClock": mdmStsPbClock,
       "mdmMa": mdmMa,
       "mdmMaTable": mdmMaTable,
       "mdmMaEntry": mdmMaEntry,
       "mdmMaIndex": mdmMaIndex,
       "mdmMaChangeIndicator": mdmMaChangeIndicator,
       "mdmMaChannelConfig": mdmMaChannelConfig}
)
