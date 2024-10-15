# SNMP MIB module (DT1-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/DT1-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:33:45 2024
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
_Dt1_ObjectIdentity = ObjectIdentity
dt1 = _Dt1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 429, 1, 3)
)
_Dt1Id_ObjectIdentity = ObjectIdentity
dt1Id = _Dt1Id_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 429, 1, 3, 1)
)
_Dt1IdTable_Object = MibTable
dt1IdTable = _Dt1IdTable_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 3, 1, 1)
)
if mibBuilder.loadTexts:
    dt1IdTable.setStatus("mandatory")
_Dt1IdEntry_Object = MibTableRow
dt1IdEntry = _Dt1IdEntry_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 3, 1, 1, 1)
)
dt1IdEntry.setIndexNames(
    (0, "DT1-MIB", "dt1IdIndex"),
)
if mibBuilder.loadTexts:
    dt1IdEntry.setStatus("mandatory")
_Dt1IdIndex_Type = Integer32
_Dt1IdIndex_Object = MibTableColumn
dt1IdIndex = _Dt1IdIndex_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 3, 1, 1, 1, 1),
    _Dt1IdIndex_Type()
)
dt1IdIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dt1IdIndex.setStatus("mandatory")


class _Dt1IdHardwareSerNum_Type(DisplayString):
    """Custom type dt1IdHardwareSerNum based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 24),
    )


_Dt1IdHardwareSerNum_Type.__name__ = "DisplayString"
_Dt1IdHardwareSerNum_Object = MibTableColumn
dt1IdHardwareSerNum = _Dt1IdHardwareSerNum_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 3, 1, 1, 1, 2),
    _Dt1IdHardwareSerNum_Type()
)
dt1IdHardwareSerNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dt1IdHardwareSerNum.setStatus("mandatory")


class _Dt1IdHardwareRev_Type(DisplayString):
    """Custom type dt1IdHardwareRev based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 24),
    )


_Dt1IdHardwareRev_Type.__name__ = "DisplayString"
_Dt1IdHardwareRev_Object = MibTableColumn
dt1IdHardwareRev = _Dt1IdHardwareRev_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 3, 1, 1, 1, 3),
    _Dt1IdHardwareRev_Type()
)
dt1IdHardwareRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dt1IdHardwareRev.setStatus("mandatory")


class _Dt1IdSoftwareRev_Type(DisplayString):
    """Custom type dt1IdSoftwareRev based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 24),
    )


_Dt1IdSoftwareRev_Type.__name__ = "DisplayString"
_Dt1IdSoftwareRev_Object = MibTableColumn
dt1IdSoftwareRev = _Dt1IdSoftwareRev_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 3, 1, 1, 1, 4),
    _Dt1IdSoftwareRev_Type()
)
dt1IdSoftwareRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dt1IdSoftwareRev.setStatus("mandatory")
_Dt1Cfg_ObjectIdentity = ObjectIdentity
dt1Cfg = _Dt1Cfg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 429, 1, 3, 2)
)
_Dt1CfgTable_Object = MibTable
dt1CfgTable = _Dt1CfgTable_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 3, 2, 1)
)
if mibBuilder.loadTexts:
    dt1CfgTable.setStatus("mandatory")
_Dt1CfgEntry_Object = MibTableRow
dt1CfgEntry = _Dt1CfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 3, 2, 1, 1)
)
dt1CfgEntry.setIndexNames(
    (0, "DT1-MIB", "dt1CfgIndex"),
)
if mibBuilder.loadTexts:
    dt1CfgEntry.setStatus("mandatory")
_Dt1CfgIndex_Type = Integer32
_Dt1CfgIndex_Object = MibTableColumn
dt1CfgIndex = _Dt1CfgIndex_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 3, 2, 1, 1, 1),
    _Dt1CfgIndex_Type()
)
dt1CfgIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dt1CfgIndex.setStatus("mandatory")


class _Dt1CfgSpanATmgSrcPrio_Type(Integer32):
    """Custom type dt1CfgSpanATmgSrcPrio based on Integer32"""
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
        *(("high", 2),
          ("low", 5),
          ("medium", 4),
          ("mediumHigh", 3),
          ("notAllowed", 1))
    )


_Dt1CfgSpanATmgSrcPrio_Type.__name__ = "Integer32"
_Dt1CfgSpanATmgSrcPrio_Object = MibTableColumn
dt1CfgSpanATmgSrcPrio = _Dt1CfgSpanATmgSrcPrio_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 3, 2, 1, 1, 2),
    _Dt1CfgSpanATmgSrcPrio_Type()
)
dt1CfgSpanATmgSrcPrio.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dt1CfgSpanATmgSrcPrio.setStatus("mandatory")


class _Dt1CfgSpanBTmgSrcPrio_Type(Integer32):
    """Custom type dt1CfgSpanBTmgSrcPrio based on Integer32"""
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
        *(("high", 2),
          ("low", 5),
          ("medium", 4),
          ("mediumHigh", 3),
          ("notAllowed", 1))
    )


_Dt1CfgSpanBTmgSrcPrio_Type.__name__ = "Integer32"
_Dt1CfgSpanBTmgSrcPrio_Object = MibTableColumn
dt1CfgSpanBTmgSrcPrio = _Dt1CfgSpanBTmgSrcPrio_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 3, 2, 1, 1, 3),
    _Dt1CfgSpanBTmgSrcPrio_Type()
)
dt1CfgSpanBTmgSrcPrio.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dt1CfgSpanBTmgSrcPrio.setStatus("mandatory")


class _Dt1CfgInternTmgSrcPrio_Type(Integer32):
    """Custom type dt1CfgInternTmgSrcPrio based on Integer32"""
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
        *(("high", 2),
          ("low", 5),
          ("medium", 4),
          ("mediumHigh", 3),
          ("notAllowed", 1))
    )


_Dt1CfgInternTmgSrcPrio_Type.__name__ = "Integer32"
_Dt1CfgInternTmgSrcPrio_Object = MibTableColumn
dt1CfgInternTmgSrcPrio = _Dt1CfgInternTmgSrcPrio_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 3, 2, 1, 1, 4),
    _Dt1CfgInternTmgSrcPrio_Type()
)
dt1CfgInternTmgSrcPrio.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dt1CfgInternTmgSrcPrio.setStatus("mandatory")


class _Dt1CfgTdmBusTmgSrcPrio_Type(Integer32):
    """Custom type dt1CfgTdmBusTmgSrcPrio based on Integer32"""
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
        *(("high", 2),
          ("low", 5),
          ("medium", 4),
          ("mediumHigh", 3),
          ("notAllowed", 1))
    )


_Dt1CfgTdmBusTmgSrcPrio_Type.__name__ = "Integer32"
_Dt1CfgTdmBusTmgSrcPrio_Object = MibTableColumn
dt1CfgTdmBusTmgSrcPrio = _Dt1CfgTdmBusTmgSrcPrio_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 3, 2, 1, 1, 5),
    _Dt1CfgTdmBusTmgSrcPrio_Type()
)
dt1CfgTdmBusTmgSrcPrio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dt1CfgTdmBusTmgSrcPrio.setStatus("deprecated")


class _Dt1CfgIdleDiscPatt_Type(Integer32):
    """Custom type dt1CfgIdleDiscPatt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_Dt1CfgIdleDiscPatt_Type.__name__ = "Integer32"
_Dt1CfgIdleDiscPatt_Object = MibTableColumn
dt1CfgIdleDiscPatt = _Dt1CfgIdleDiscPatt_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 3, 2, 1, 1, 6),
    _Dt1CfgIdleDiscPatt_Type()
)
dt1CfgIdleDiscPatt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dt1CfgIdleDiscPatt.setStatus("mandatory")


class _Dt1CfgNumT1TypeNacs_Type(Integer32):
    """Custom type dt1CfgNumT1TypeNacs based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("multiple", 3),
          ("notSupported", 1),
          ("single", 2))
    )


_Dt1CfgNumT1TypeNacs_Type.__name__ = "Integer32"
_Dt1CfgNumT1TypeNacs_Object = MibTableColumn
dt1CfgNumT1TypeNacs = _Dt1CfgNumT1TypeNacs_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 3, 2, 1, 1, 7),
    _Dt1CfgNumT1TypeNacs_Type()
)
dt1CfgNumT1TypeNacs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dt1CfgNumT1TypeNacs.setStatus("mandatory")


class _Dt1CfgCallEventFilter_Type(Integer32):
    """Custom type dt1CfgCallEventFilter based on Integer32"""
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
        *(("filterOutBoth", 3),
          ("filterOutFailure", 5),
          ("filterOutNone", 2),
          ("filterOutSuccess", 4),
          ("notSupported", 1))
    )


_Dt1CfgCallEventFilter_Type.__name__ = "Integer32"
_Dt1CfgCallEventFilter_Object = MibTableColumn
dt1CfgCallEventFilter = _Dt1CfgCallEventFilter_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 3, 2, 1, 1, 8),
    _Dt1CfgCallEventFilter_Type()
)
dt1CfgCallEventFilter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dt1CfgCallEventFilter.setStatus("mandatory")


class _Dt1CfgSetDs0OutofService_Type(Integer32):
    """Custom type dt1CfgSetDs0OutofService based on Integer32"""
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


_Dt1CfgSetDs0OutofService_Type.__name__ = "Integer32"
_Dt1CfgSetDs0OutofService_Object = MibTableColumn
dt1CfgSetDs0OutofService = _Dt1CfgSetDs0OutofService_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 3, 2, 1, 1, 9),
    _Dt1CfgSetDs0OutofService_Type()
)
dt1CfgSetDs0OutofService.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dt1CfgSetDs0OutofService.setStatus("mandatory")


class _Dt1CfgWirelessMode_Type(Integer32):
    """Custom type dt1CfgWirelessMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("normal", 1),
          ("wireless", 2))
    )


_Dt1CfgWirelessMode_Type.__name__ = "Integer32"
_Dt1CfgWirelessMode_Object = MibTableColumn
dt1CfgWirelessMode = _Dt1CfgWirelessMode_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 3, 2, 1, 1, 10),
    _Dt1CfgWirelessMode_Type()
)
dt1CfgWirelessMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dt1CfgWirelessMode.setStatus("mandatory")
_Dt1Stat_ObjectIdentity = ObjectIdentity
dt1Stat = _Dt1Stat_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 429, 1, 3, 3)
)
_Dt1StatTable_Object = MibTable
dt1StatTable = _Dt1StatTable_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 3, 3, 1)
)
if mibBuilder.loadTexts:
    dt1StatTable.setStatus("mandatory")
_Dt1StatEntry_Object = MibTableRow
dt1StatEntry = _Dt1StatEntry_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 3, 3, 1, 1)
)
dt1StatEntry.setIndexNames(
    (0, "DT1-MIB", "dt1StatIndex"),
)
if mibBuilder.loadTexts:
    dt1StatEntry.setStatus("mandatory")
_Dt1StatIndex_Type = Integer32
_Dt1StatIndex_Object = MibTableColumn
dt1StatIndex = _Dt1StatIndex_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 3, 3, 1, 1, 1),
    _Dt1StatIndex_Type()
)
dt1StatIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dt1StatIndex.setStatus("mandatory")


class _Dt1StatCurrentTmgSrc_Type(Integer32):
    """Custom type dt1StatCurrentTmgSrc based on Integer32"""
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
        *(("internalClock", 3),
          ("spanLineA", 1),
          ("spanLineB", 2),
          ("tdmBusClock", 4))
    )


_Dt1StatCurrentTmgSrc_Type.__name__ = "Integer32"
_Dt1StatCurrentTmgSrc_Object = MibTableColumn
dt1StatCurrentTmgSrc = _Dt1StatCurrentTmgSrc_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 3, 3, 1, 1, 2),
    _Dt1StatCurrentTmgSrc_Type()
)
dt1StatCurrentTmgSrc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dt1StatCurrentTmgSrc.setStatus("mandatory")
_Dt1StatSelfTest_Type = Integer32
_Dt1StatSelfTest_Object = MibTableColumn
dt1StatSelfTest = _Dt1StatSelfTest_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 3, 3, 1, 1, 3),
    _Dt1StatSelfTest_Type()
)
dt1StatSelfTest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dt1StatSelfTest.setStatus("mandatory")
_Dt1StatUpTime_Type = Integer32
_Dt1StatUpTime_Object = MibTableColumn
dt1StatUpTime = _Dt1StatUpTime_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 3, 3, 1, 1, 4),
    _Dt1StatUpTime_Type()
)
dt1StatUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dt1StatUpTime.setStatus("mandatory")


class _Dt1StatCallEventCode_Type(Integer32):
    """Custom type dt1StatCallEventCode based on Integer32"""
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
              32)
        )
    )
    namedValues = NamedValues(
        *(("analogBlocked", 21),
          ("bcReject", 14),
          ("blocked", 20),
          ("busy", 24),
          ("calledPartyReject", 19),
          ("callingPartyReject", 18),
          ("chidReject", 16),
          ("congestion", 25),
          ("digitalBlocked", 22),
          ("ieReject", 15),
          ("igwRejectCall", 11),
          ("igwSetupTimeout", 12),
          ("inCallArrival", 29),
          ("inCallConnect", 31),
          ("inOutCallCollision", 28),
          ("modemSetupTimeout", 9),
          ("modemsNotAllowed", 7),
          ("modemsRejectCall", 8),
          ("noFreeBchannel", 27),
          ("noFreeIGW", 10),
          ("noFreeModem", 6),
          ("noFreeTdmts", 13),
          ("notSupported", 1),
          ("outCallArrival", 30),
          ("outCallConnect", 32),
          ("outOfService", 23),
          ("progReject", 17),
          ("protocolError", 26),
          ("setup", 2),
          ("telcoDisconnect", 4),
          ("usrDisconnect", 5),
          ("usrSetup", 3))
    )


_Dt1StatCallEventCode_Type.__name__ = "Integer32"
_Dt1StatCallEventCode_Object = MibTableColumn
dt1StatCallEventCode = _Dt1StatCallEventCode_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 3, 3, 1, 1, 5),
    _Dt1StatCallEventCode_Type()
)
dt1StatCallEventCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dt1StatCallEventCode.setStatus("mandatory")
_Dt1StatCallEventQ931Value_Type = Integer32
_Dt1StatCallEventQ931Value_Object = MibTableColumn
dt1StatCallEventQ931Value = _Dt1StatCallEventQ931Value_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 3, 3, 1, 1, 6),
    _Dt1StatCallEventQ931Value_Type()
)
dt1StatCallEventQ931Value.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dt1StatCallEventQ931Value.setStatus("mandatory")
_Dt1Cmd_ObjectIdentity = ObjectIdentity
dt1Cmd = _Dt1Cmd_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 429, 1, 3, 4)
)
_Dt1CmdTable_Object = MibTable
dt1CmdTable = _Dt1CmdTable_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 3, 4, 1)
)
if mibBuilder.loadTexts:
    dt1CmdTable.setStatus("mandatory")
_Dt1CmdEntry_Object = MibTableRow
dt1CmdEntry = _Dt1CmdEntry_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 3, 4, 1, 1)
)
dt1CmdEntry.setIndexNames(
    (0, "DT1-MIB", "dt1CmdIndex"),
)
if mibBuilder.loadTexts:
    dt1CmdEntry.setStatus("mandatory")
_Dt1CmdIndex_Type = Integer32
_Dt1CmdIndex_Object = MibTableColumn
dt1CmdIndex = _Dt1CmdIndex_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 3, 4, 1, 1, 1),
    _Dt1CmdIndex_Type()
)
dt1CmdIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dt1CmdIndex.setStatus("mandatory")


class _Dt1CmdMgtStationId_Type(OctetString):
    """Custom type dt1CmdMgtStationId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_Dt1CmdMgtStationId_Type.__name__ = "OctetString"
_Dt1CmdMgtStationId_Object = MibTableColumn
dt1CmdMgtStationId = _Dt1CmdMgtStationId_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 3, 4, 1, 1, 2),
    _Dt1CmdMgtStationId_Type()
)
dt1CmdMgtStationId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dt1CmdMgtStationId.setStatus("mandatory")
_Dt1CmdReqId_Type = Integer32
_Dt1CmdReqId_Object = MibTableColumn
dt1CmdReqId = _Dt1CmdReqId_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 3, 4, 1, 1, 3),
    _Dt1CmdReqId_Type()
)
dt1CmdReqId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dt1CmdReqId.setStatus("mandatory")


class _Dt1CmdFunction_Type(Integer32):
    """Custom type dt1CmdFunction based on Integer32"""
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
        *(("disruptSelfTest", 6),
          ("enterSpanToSpanLoopback", 10),
          ("exitSpanToSpanLoopback", 11),
          ("forceTdmBusMastership", 9),
          ("noCommand", 1),
          ("nonDisruptSelfTest", 5),
          ("resetToHiPrioTimingSrc", 8),
          ("restoreDefaultUIPassword", 12),
          ("restoreFromDefault", 4),
          ("restoreFromNVRAM", 3),
          ("saveToNVRAM", 2),
          ("softwareReset", 7))
    )


_Dt1CmdFunction_Type.__name__ = "Integer32"
_Dt1CmdFunction_Object = MibTableColumn
dt1CmdFunction = _Dt1CmdFunction_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 3, 4, 1, 1, 4),
    _Dt1CmdFunction_Type()
)
dt1CmdFunction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dt1CmdFunction.setStatus("mandatory")


class _Dt1CmdForce_Type(Integer32):
    """Custom type dt1CmdForce based on Integer32"""
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


_Dt1CmdForce_Type.__name__ = "Integer32"
_Dt1CmdForce_Object = MibTableColumn
dt1CmdForce = _Dt1CmdForce_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 3, 4, 1, 1, 5),
    _Dt1CmdForce_Type()
)
dt1CmdForce.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dt1CmdForce.setStatus("mandatory")


class _Dt1CmdParam_Type(OctetString):
    """Custom type dt1CmdParam based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 24),
    )


_Dt1CmdParam_Type.__name__ = "OctetString"
_Dt1CmdParam_Object = MibTableColumn
dt1CmdParam = _Dt1CmdParam_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 3, 4, 1, 1, 6),
    _Dt1CmdParam_Type()
)
dt1CmdParam.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dt1CmdParam.setStatus("mandatory")


class _Dt1CmdResult_Type(Integer32):
    """Custom type dt1CmdResult based on Integer32"""
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


_Dt1CmdResult_Type.__name__ = "Integer32"
_Dt1CmdResult_Object = MibTableColumn
dt1CmdResult = _Dt1CmdResult_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 3, 4, 1, 1, 7),
    _Dt1CmdResult_Type()
)
dt1CmdResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dt1CmdResult.setStatus("mandatory")


class _Dt1CmdCode_Type(Integer32):
    """Custom type dt1CmdCode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              6,
              8,
              12,
              20,
              22,
              25,
              58,
              73)
        )
    )
    namedValues = NamedValues(
        *(("deviceDisabled", 22),
          ("noError", 1),
          ("noResponse", 12),
          ("pendingSoftwareDownload", 73),
          ("slotEmpty", 8),
          ("testFailed", 25),
          ("unable", 2),
          ("unrecognizedCommand", 6),
          ("unsupportedCommand", 20),
          ("userInterfaceActive", 58))
    )


_Dt1CmdCode_Type.__name__ = "Integer32"
_Dt1CmdCode_Object = MibTableColumn
dt1CmdCode = _Dt1CmdCode_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 3, 4, 1, 1, 8),
    _Dt1CmdCode_Type()
)
dt1CmdCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dt1CmdCode.setStatus("mandatory")
_Dt1TrapEnaTable_Object = MibTable
dt1TrapEnaTable = _Dt1TrapEnaTable_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 3, 5)
)
if mibBuilder.loadTexts:
    dt1TrapEnaTable.setStatus("mandatory")
_Dt1TrapEnaEntry_Object = MibTableRow
dt1TrapEnaEntry = _Dt1TrapEnaEntry_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 3, 5, 1)
)
dt1TrapEnaEntry.setIndexNames(
    (0, "DT1-MIB", "dt1TrapEnaIndex"),
)
if mibBuilder.loadTexts:
    dt1TrapEnaEntry.setStatus("mandatory")
_Dt1TrapEnaIndex_Type = Integer32
_Dt1TrapEnaIndex_Object = MibTableColumn
dt1TrapEnaIndex = _Dt1TrapEnaIndex_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 3, 5, 1, 1),
    _Dt1TrapEnaIndex_Type()
)
dt1TrapEnaIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dt1TrapEnaIndex.setStatus("mandatory")


class _Dt1TrapEnaTxTmgSrcSwitch_Type(Integer32):
    """Custom type dt1TrapEnaTxTmgSrcSwitch based on Integer32"""
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


_Dt1TrapEnaTxTmgSrcSwitch_Type.__name__ = "Integer32"
_Dt1TrapEnaTxTmgSrcSwitch_Object = MibTableColumn
dt1TrapEnaTxTmgSrcSwitch = _Dt1TrapEnaTxTmgSrcSwitch_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 3, 5, 1, 2),
    _Dt1TrapEnaTxTmgSrcSwitch_Type()
)
dt1TrapEnaTxTmgSrcSwitch.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dt1TrapEnaTxTmgSrcSwitch.setStatus("mandatory")


class _Dt1TrapEnaCallEvent_Type(Integer32):
    """Custom type dt1TrapEnaCallEvent based on Integer32"""
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


_Dt1TrapEnaCallEvent_Type.__name__ = "Integer32"
_Dt1TrapEnaCallEvent_Object = MibTableColumn
dt1TrapEnaCallEvent = _Dt1TrapEnaCallEvent_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 3, 5, 1, 3),
    _Dt1TrapEnaCallEvent_Type()
)
dt1TrapEnaCallEvent.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dt1TrapEnaCallEvent.setStatus("mandatory")


class _Dt1TrapEnaCallArriveEvent_Type(Integer32):
    """Custom type dt1TrapEnaCallArriveEvent based on Integer32"""
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


_Dt1TrapEnaCallArriveEvent_Type.__name__ = "Integer32"
_Dt1TrapEnaCallArriveEvent_Object = MibTableColumn
dt1TrapEnaCallArriveEvent = _Dt1TrapEnaCallArriveEvent_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 3, 5, 1, 4),
    _Dt1TrapEnaCallArriveEvent_Type()
)
dt1TrapEnaCallArriveEvent.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dt1TrapEnaCallArriveEvent.setStatus("mandatory")


class _Dt1TrapEnaCallConnEvent_Type(Integer32):
    """Custom type dt1TrapEnaCallConnEvent based on Integer32"""
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


_Dt1TrapEnaCallConnEvent_Type.__name__ = "Integer32"
_Dt1TrapEnaCallConnEvent_Object = MibTableColumn
dt1TrapEnaCallConnEvent = _Dt1TrapEnaCallConnEvent_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 3, 5, 1, 5),
    _Dt1TrapEnaCallConnEvent_Type()
)
dt1TrapEnaCallConnEvent.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dt1TrapEnaCallConnEvent.setStatus("mandatory")


class _Dt1TrapEnaCallTermEvent_Type(Integer32):
    """Custom type dt1TrapEnaCallTermEvent based on Integer32"""
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


_Dt1TrapEnaCallTermEvent_Type.__name__ = "Integer32"
_Dt1TrapEnaCallTermEvent_Object = MibTableColumn
dt1TrapEnaCallTermEvent = _Dt1TrapEnaCallTermEvent_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 3, 5, 1, 6),
    _Dt1TrapEnaCallTermEvent_Type()
)
dt1TrapEnaCallTermEvent.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dt1TrapEnaCallTermEvent.setStatus("mandatory")


class _Dt1TrapEnaCallFailEvent_Type(Integer32):
    """Custom type dt1TrapEnaCallFailEvent based on Integer32"""
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


_Dt1TrapEnaCallFailEvent_Type.__name__ = "Integer32"
_Dt1TrapEnaCallFailEvent_Object = MibTableColumn
dt1TrapEnaCallFailEvent = _Dt1TrapEnaCallFailEvent_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 3, 5, 1, 7),
    _Dt1TrapEnaCallFailEvent_Type()
)
dt1TrapEnaCallFailEvent.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dt1TrapEnaCallFailEvent.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "DT1-MIB",
    **{"usr": usr,
       "nas": nas,
       "dt1": dt1,
       "dt1Id": dt1Id,
       "dt1IdTable": dt1IdTable,
       "dt1IdEntry": dt1IdEntry,
       "dt1IdIndex": dt1IdIndex,
       "dt1IdHardwareSerNum": dt1IdHardwareSerNum,
       "dt1IdHardwareRev": dt1IdHardwareRev,
       "dt1IdSoftwareRev": dt1IdSoftwareRev,
       "dt1Cfg": dt1Cfg,
       "dt1CfgTable": dt1CfgTable,
       "dt1CfgEntry": dt1CfgEntry,
       "dt1CfgIndex": dt1CfgIndex,
       "dt1CfgSpanATmgSrcPrio": dt1CfgSpanATmgSrcPrio,
       "dt1CfgSpanBTmgSrcPrio": dt1CfgSpanBTmgSrcPrio,
       "dt1CfgInternTmgSrcPrio": dt1CfgInternTmgSrcPrio,
       "dt1CfgTdmBusTmgSrcPrio": dt1CfgTdmBusTmgSrcPrio,
       "dt1CfgIdleDiscPatt": dt1CfgIdleDiscPatt,
       "dt1CfgNumT1TypeNacs": dt1CfgNumT1TypeNacs,
       "dt1CfgCallEventFilter": dt1CfgCallEventFilter,
       "dt1CfgSetDs0OutofService": dt1CfgSetDs0OutofService,
       "dt1CfgWirelessMode": dt1CfgWirelessMode,
       "dt1Stat": dt1Stat,
       "dt1StatTable": dt1StatTable,
       "dt1StatEntry": dt1StatEntry,
       "dt1StatIndex": dt1StatIndex,
       "dt1StatCurrentTmgSrc": dt1StatCurrentTmgSrc,
       "dt1StatSelfTest": dt1StatSelfTest,
       "dt1StatUpTime": dt1StatUpTime,
       "dt1StatCallEventCode": dt1StatCallEventCode,
       "dt1StatCallEventQ931Value": dt1StatCallEventQ931Value,
       "dt1Cmd": dt1Cmd,
       "dt1CmdTable": dt1CmdTable,
       "dt1CmdEntry": dt1CmdEntry,
       "dt1CmdIndex": dt1CmdIndex,
       "dt1CmdMgtStationId": dt1CmdMgtStationId,
       "dt1CmdReqId": dt1CmdReqId,
       "dt1CmdFunction": dt1CmdFunction,
       "dt1CmdForce": dt1CmdForce,
       "dt1CmdParam": dt1CmdParam,
       "dt1CmdResult": dt1CmdResult,
       "dt1CmdCode": dt1CmdCode,
       "dt1TrapEnaTable": dt1TrapEnaTable,
       "dt1TrapEnaEntry": dt1TrapEnaEntry,
       "dt1TrapEnaIndex": dt1TrapEnaIndex,
       "dt1TrapEnaTxTmgSrcSwitch": dt1TrapEnaTxTmgSrcSwitch,
       "dt1TrapEnaCallEvent": dt1TrapEnaCallEvent,
       "dt1TrapEnaCallArriveEvent": dt1TrapEnaCallArriveEvent,
       "dt1TrapEnaCallConnEvent": dt1TrapEnaCallConnEvent,
       "dt1TrapEnaCallTermEvent": dt1TrapEnaCallTermEvent,
       "dt1TrapEnaCallFailEvent": dt1TrapEnaCallFailEvent}
)
