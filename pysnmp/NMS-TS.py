# SNMP MIB module (NMS-TS) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/NMS-TS
# Produced by pysmi-1.5.4 at Mon Oct 14 22:28:06 2024
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

(nmslocal,) = mibBuilder.importSymbols(
    "NMS-SMI",
    "nmslocal")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Nmslts_ObjectIdentity = ObjectIdentity
nmslts = _Nmslts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11606, 10, 2, 9)
)
_NmstsLines_Type = Integer32
_NmstsLines_Object = MibScalar
nmstsLines = _NmstsLines_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 2, 9, 1),
    _NmstsLines_Type()
)
nmstsLines.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nmstsLines.setStatus("mandatory")
_NmsltsLineTable_Object = MibTable
nmsltsLineTable = _NmsltsLineTable_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 2, 9, 2)
)
if mibBuilder.loadTexts:
    nmsltsLineTable.setStatus("mandatory")
_NmsltsLineEntry_Object = MibTableRow
nmsltsLineEntry = _NmsltsLineEntry_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 2, 9, 2, 1)
)
nmsltsLineEntry.setIndexNames(
    (0, "NMS-TS", "tsLineNumber"),
)
if mibBuilder.loadTexts:
    nmsltsLineEntry.setStatus("mandatory")
_NmstsLineActive_Type = Integer32
_NmstsLineActive_Object = MibTableColumn
nmstsLineActive = _NmstsLineActive_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 2, 9, 2, 1, 1),
    _NmstsLineActive_Type()
)
nmstsLineActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nmstsLineActive.setStatus("mandatory")


class _NmstsLineType_Type(Integer32):
    """Custom type nmstsLineType based on Integer32"""
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
        *(("auxiliary", 6),
          ("console", 2),
          ("line-printer", 4),
          ("terminal", 3),
          ("unknown", 1),
          ("virtual-terminal", 5))
    )


_NmstsLineType_Type.__name__ = "Integer32"
_NmstsLineType_Object = MibTableColumn
nmstsLineType = _NmstsLineType_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 2, 9, 2, 1, 2),
    _NmstsLineType_Type()
)
nmstsLineType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nmstsLineType.setStatus("mandatory")
_NmstsLineAutobaud_Type = Integer32
_NmstsLineAutobaud_Object = MibTableColumn
nmstsLineAutobaud = _NmstsLineAutobaud_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 2, 9, 2, 1, 3),
    _NmstsLineAutobaud_Type()
)
nmstsLineAutobaud.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nmstsLineAutobaud.setStatus("mandatory")
_NmstsLineSpeedin_Type = Integer32
_NmstsLineSpeedin_Object = MibTableColumn
nmstsLineSpeedin = _NmstsLineSpeedin_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 2, 9, 2, 1, 4),
    _NmstsLineSpeedin_Type()
)
nmstsLineSpeedin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nmstsLineSpeedin.setStatus("mandatory")
_NmstsLineSpeedout_Type = Integer32
_NmstsLineSpeedout_Object = MibTableColumn
nmstsLineSpeedout = _NmstsLineSpeedout_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 2, 9, 2, 1, 5),
    _NmstsLineSpeedout_Type()
)
nmstsLineSpeedout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nmstsLineSpeedout.setStatus("mandatory")


class _NmstsLineFlow_Type(Integer32):
    """Custom type nmstsLineFlow based on Integer32"""
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
        *(("hardware-both", 8),
          ("hardware-input", 6),
          ("hardware-output", 7),
          ("none", 2),
          ("software-both", 5),
          ("software-input", 3),
          ("software-output", 4),
          ("unknown", 1))
    )


_NmstsLineFlow_Type.__name__ = "Integer32"
_NmstsLineFlow_Object = MibTableColumn
nmstsLineFlow = _NmstsLineFlow_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 2, 9, 2, 1, 6),
    _NmstsLineFlow_Type()
)
nmstsLineFlow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nmstsLineFlow.setStatus("mandatory")


class _NmstsLineModem_Type(Integer32):
    """Custom type nmstsLineModem based on Integer32"""
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
        *(("call-in", 3),
          ("call-out", 4),
          ("cts-required", 5),
          ("inout", 7),
          ("none", 2),
          ("ri-is-cd", 6),
          ("unknown", 1))
    )


_NmstsLineModem_Type.__name__ = "Integer32"
_NmstsLineModem_Object = MibTableColumn
nmstsLineModem = _NmstsLineModem_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 2, 9, 2, 1, 7),
    _NmstsLineModem_Type()
)
nmstsLineModem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nmstsLineModem.setStatus("mandatory")
_NmstsLineLoc_Type = DisplayString
_NmstsLineLoc_Object = MibTableColumn
nmstsLineLoc = _NmstsLineLoc_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 2, 9, 2, 1, 8),
    _NmstsLineLoc_Type()
)
nmstsLineLoc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nmstsLineLoc.setStatus("mandatory")
_NmstsLineTerm_Type = DisplayString
_NmstsLineTerm_Object = MibTableColumn
nmstsLineTerm = _NmstsLineTerm_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 2, 9, 2, 1, 9),
    _NmstsLineTerm_Type()
)
nmstsLineTerm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nmstsLineTerm.setStatus("mandatory")
_NmstsLineScrlen_Type = Integer32
_NmstsLineScrlen_Object = MibTableColumn
nmstsLineScrlen = _NmstsLineScrlen_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 2, 9, 2, 1, 10),
    _NmstsLineScrlen_Type()
)
nmstsLineScrlen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nmstsLineScrlen.setStatus("mandatory")
_NmstsLineScrwid_Type = Integer32
_NmstsLineScrwid_Object = MibTableColumn
nmstsLineScrwid = _NmstsLineScrwid_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 2, 9, 2, 1, 11),
    _NmstsLineScrwid_Type()
)
nmstsLineScrwid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nmstsLineScrwid.setStatus("mandatory")
_NmstsLineEsc_Type = DisplayString
_NmstsLineEsc_Object = MibTableColumn
nmstsLineEsc = _NmstsLineEsc_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 2, 9, 2, 1, 12),
    _NmstsLineEsc_Type()
)
nmstsLineEsc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nmstsLineEsc.setStatus("mandatory")
_NmstsLineTmo_Type = Integer32
_NmstsLineTmo_Object = MibTableColumn
nmstsLineTmo = _NmstsLineTmo_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 2, 9, 2, 1, 13),
    _NmstsLineTmo_Type()
)
nmstsLineTmo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nmstsLineTmo.setStatus("mandatory")
_NmstsLineSestmo_Type = Integer32
_NmstsLineSestmo_Object = MibTableColumn
nmstsLineSestmo = _NmstsLineSestmo_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 2, 9, 2, 1, 14),
    _NmstsLineSestmo_Type()
)
nmstsLineSestmo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nmstsLineSestmo.setStatus("mandatory")
_NmstsLineRotary_Type = Integer32
_NmstsLineRotary_Object = MibTableColumn
nmstsLineRotary = _NmstsLineRotary_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 2, 9, 2, 1, 15),
    _NmstsLineRotary_Type()
)
nmstsLineRotary.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nmstsLineRotary.setStatus("mandatory")
_NmstsLineUses_Type = Integer32
_NmstsLineUses_Object = MibTableColumn
nmstsLineUses = _NmstsLineUses_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 2, 9, 2, 1, 16),
    _NmstsLineUses_Type()
)
nmstsLineUses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nmstsLineUses.setStatus("mandatory")
_NmstsLineNses_Type = Integer32
_NmstsLineNses_Object = MibTableColumn
nmstsLineNses = _NmstsLineNses_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 2, 9, 2, 1, 17),
    _NmstsLineNses_Type()
)
nmstsLineNses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nmstsLineNses.setStatus("mandatory")
_NmstsLineUser_Type = DisplayString
_NmstsLineUser_Object = MibTableColumn
nmstsLineUser = _NmstsLineUser_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 2, 9, 2, 1, 18),
    _NmstsLineUser_Type()
)
nmstsLineUser.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nmstsLineUser.setStatus("mandatory")
_NmstsLineNoise_Type = Integer32
_NmstsLineNoise_Object = MibTableColumn
nmstsLineNoise = _NmstsLineNoise_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 2, 9, 2, 1, 19),
    _NmstsLineNoise_Type()
)
nmstsLineNoise.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nmstsLineNoise.setStatus("mandatory")
_NmstsLineNumber_Type = Integer32
_NmstsLineNumber_Object = MibTableColumn
nmstsLineNumber = _NmstsLineNumber_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 2, 9, 2, 1, 20),
    _NmstsLineNumber_Type()
)
nmstsLineNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nmstsLineNumber.setStatus("mandatory")
_NmstsLineTimeActive_Type = Integer32
_NmstsLineTimeActive_Object = MibTableColumn
nmstsLineTimeActive = _NmstsLineTimeActive_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 2, 9, 2, 1, 21),
    _NmstsLineTimeActive_Type()
)
nmstsLineTimeActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nmstsLineTimeActive.setStatus("mandatory")
_NmsltsLineSessionTable_Object = MibTable
nmsltsLineSessionTable = _NmsltsLineSessionTable_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 2, 9, 3)
)
if mibBuilder.loadTexts:
    nmsltsLineSessionTable.setStatus("mandatory")
_NmsltsLineSessionEntry_Object = MibTableRow
nmsltsLineSessionEntry = _NmsltsLineSessionEntry_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 2, 9, 3, 1)
)
nmsltsLineSessionEntry.setIndexNames(
    (0, "NMS-TS", "nmstslineSesLine"),
    (0, "NMS-TS", "nmstslineSesSession"),
)
if mibBuilder.loadTexts:
    nmsltsLineSessionEntry.setStatus("mandatory")


class _NmstslineSesType_Type(Integer32):
    """Custom type nmstslineSesType based on Integer32"""
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
        *(("lat", 7),
          ("mop", 8),
          ("pad", 2),
          ("rlogin", 4),
          ("rshell", 11),
          ("slip", 9),
          ("stream", 3),
          ("tcp", 6),
          ("telnet", 5),
          ("unknown", 1),
          ("xremote", 10))
    )


_NmstslineSesType_Type.__name__ = "Integer32"
_NmstslineSesType_Object = MibTableColumn
nmstslineSesType = _NmstslineSesType_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 2, 9, 3, 1, 1),
    _NmstslineSesType_Type()
)
nmstslineSesType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nmstslineSesType.setStatus("mandatory")


class _NmstslineSesDir_Type(Integer32):
    """Custom type nmstslineSesDir based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("incoming", 2),
          ("outgoing", 3),
          ("unknown", 1))
    )


_NmstslineSesDir_Type.__name__ = "Integer32"
_NmstslineSesDir_Object = MibTableColumn
nmstslineSesDir = _NmstslineSesDir_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 2, 9, 3, 1, 2),
    _NmstslineSesDir_Type()
)
nmstslineSesDir.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nmstslineSesDir.setStatus("mandatory")
_NmstslineSesAddr_Type = IpAddress
_NmstslineSesAddr_Object = MibTableColumn
nmstslineSesAddr = _NmstslineSesAddr_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 2, 9, 3, 1, 3),
    _NmstslineSesAddr_Type()
)
nmstslineSesAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nmstslineSesAddr.setStatus("mandatory")
_NmstslineSesName_Type = DisplayString
_NmstslineSesName_Object = MibTableColumn
nmstslineSesName = _NmstslineSesName_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 2, 9, 3, 1, 4),
    _NmstslineSesName_Type()
)
nmstslineSesName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nmstslineSesName.setStatus("mandatory")
_NmstslineSesCur_Type = Integer32
_NmstslineSesCur_Object = MibTableColumn
nmstslineSesCur = _NmstslineSesCur_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 2, 9, 3, 1, 5),
    _NmstslineSesCur_Type()
)
nmstslineSesCur.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nmstslineSesCur.setStatus("mandatory")
_NmstslineSesIdle_Type = Integer32
_NmstslineSesIdle_Object = MibTableColumn
nmstslineSesIdle = _NmstslineSesIdle_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 2, 9, 3, 1, 6),
    _NmstslineSesIdle_Type()
)
nmstslineSesIdle.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nmstslineSesIdle.setStatus("mandatory")
_NmstslineSesLine_Type = Integer32
_NmstslineSesLine_Object = MibTableColumn
nmstslineSesLine = _NmstslineSesLine_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 2, 9, 3, 1, 7),
    _NmstslineSesLine_Type()
)
nmstslineSesLine.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nmstslineSesLine.setStatus("mandatory")
_NmstslineSesSession_Type = Integer32
_NmstslineSesSession_Object = MibTableColumn
nmstslineSesSession = _NmstslineSesSession_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 2, 9, 3, 1, 8),
    _NmstslineSesSession_Type()
)
nmstslineSesSession.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nmstslineSesSession.setStatus("mandatory")
_NmstsMsgTtyLine_Type = Integer32
_NmstsMsgTtyLine_Object = MibScalar
nmstsMsgTtyLine = _NmstsMsgTtyLine_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 2, 9, 4),
    _NmstsMsgTtyLine_Type()
)
nmstsMsgTtyLine.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nmstsMsgTtyLine.setStatus("mandatory")
_NmstsMsgIntervaltim_Type = Integer32
_NmstsMsgIntervaltim_Object = MibScalar
nmstsMsgIntervaltim = _NmstsMsgIntervaltim_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 2, 9, 5),
    _NmstsMsgIntervaltim_Type()
)
nmstsMsgIntervaltim.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nmstsMsgIntervaltim.setStatus("mandatory")
_NmstsMsgDuration_Type = Integer32
_NmstsMsgDuration_Object = MibScalar
nmstsMsgDuration = _NmstsMsgDuration_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 2, 9, 6),
    _NmstsMsgDuration_Type()
)
nmstsMsgDuration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nmstsMsgDuration.setStatus("mandatory")
_NmstsMsgText_Type = DisplayString
_NmstsMsgText_Object = MibScalar
nmstsMsgText = _NmstsMsgText_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 2, 9, 7),
    _NmstsMsgText_Type()
)
nmstsMsgText.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nmstsMsgText.setStatus("mandatory")


class _NmstsMsgTmpBanner_Type(Integer32):
    """Custom type nmstsMsgTmpBanner based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("additive", 2),
          ("no", 1))
    )


_NmstsMsgTmpBanner_Type.__name__ = "Integer32"
_NmstsMsgTmpBanner_Object = MibScalar
nmstsMsgTmpBanner = _NmstsMsgTmpBanner_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 2, 9, 8),
    _NmstsMsgTmpBanner_Type()
)
nmstsMsgTmpBanner.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nmstsMsgTmpBanner.setStatus("mandatory")


class _NmstsMsgSend_Type(Integer32):
    """Custom type nmstsMsgSend based on Integer32"""
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
        *(("abort", 4),
          ("messagedone", 3),
          ("nothing", 1),
          ("reload", 2))
    )


_NmstsMsgSend_Type.__name__ = "Integer32"
_NmstsMsgSend_Object = MibScalar
nmstsMsgSend = _NmstsMsgSend_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 2, 9, 9),
    _NmstsMsgSend_Type()
)
nmstsMsgSend.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nmstsMsgSend.setStatus("mandatory")
_NmstsClrTtyLine_Type = Integer32
_NmstsClrTtyLine_Object = MibScalar
nmstsClrTtyLine = _NmstsClrTtyLine_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 2, 9, 10),
    _NmstsClrTtyLine_Type()
)
nmstsClrTtyLine.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nmstsClrTtyLine.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "NMS-TS",
    **{"nmslts": nmslts,
       "nmstsLines": nmstsLines,
       "nmsltsLineTable": nmsltsLineTable,
       "nmsltsLineEntry": nmsltsLineEntry,
       "nmstsLineActive": nmstsLineActive,
       "nmstsLineType": nmstsLineType,
       "nmstsLineAutobaud": nmstsLineAutobaud,
       "nmstsLineSpeedin": nmstsLineSpeedin,
       "nmstsLineSpeedout": nmstsLineSpeedout,
       "nmstsLineFlow": nmstsLineFlow,
       "nmstsLineModem": nmstsLineModem,
       "nmstsLineLoc": nmstsLineLoc,
       "nmstsLineTerm": nmstsLineTerm,
       "nmstsLineScrlen": nmstsLineScrlen,
       "nmstsLineScrwid": nmstsLineScrwid,
       "nmstsLineEsc": nmstsLineEsc,
       "nmstsLineTmo": nmstsLineTmo,
       "nmstsLineSestmo": nmstsLineSestmo,
       "nmstsLineRotary": nmstsLineRotary,
       "nmstsLineUses": nmstsLineUses,
       "nmstsLineNses": nmstsLineNses,
       "nmstsLineUser": nmstsLineUser,
       "nmstsLineNoise": nmstsLineNoise,
       "nmstsLineNumber": nmstsLineNumber,
       "nmstsLineTimeActive": nmstsLineTimeActive,
       "nmsltsLineSessionTable": nmsltsLineSessionTable,
       "nmsltsLineSessionEntry": nmsltsLineSessionEntry,
       "nmstslineSesType": nmstslineSesType,
       "nmstslineSesDir": nmstslineSesDir,
       "nmstslineSesAddr": nmstslineSesAddr,
       "nmstslineSesName": nmstslineSesName,
       "nmstslineSesCur": nmstslineSesCur,
       "nmstslineSesIdle": nmstslineSesIdle,
       "nmstslineSesLine": nmstslineSesLine,
       "nmstslineSesSession": nmstslineSesSession,
       "nmstsMsgTtyLine": nmstsMsgTtyLine,
       "nmstsMsgIntervaltim": nmstsMsgIntervaltim,
       "nmstsMsgDuration": nmstsMsgDuration,
       "nmstsMsgText": nmstsMsgText,
       "nmstsMsgTmpBanner": nmstsMsgTmpBanner,
       "nmstsMsgSend": nmstsMsgSend,
       "nmstsClrTtyLine": nmstsClrTtyLine}
)
