# SNMP MIB module (BDCOM-TS) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/BDCOM-TS
# Produced by pysmi-1.5.4 at Mon Oct 14 20:46:39 2024
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

(bdlocal,) = mibBuilder.importSymbols(
    "BDCOM-SMI",
    "bdlocal")

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

_Bdlts_ObjectIdentity = ObjectIdentity
bdlts = _Bdlts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3320, 2, 9)
)
_BdtsLines_Type = Integer32
_BdtsLines_Object = MibScalar
bdtsLines = _BdtsLines_Object(
    (1, 3, 6, 1, 4, 1, 3320, 2, 9, 1),
    _BdtsLines_Type()
)
bdtsLines.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bdtsLines.setStatus("mandatory")
_BdltsLineTable_Object = MibTable
bdltsLineTable = _BdltsLineTable_Object(
    (1, 3, 6, 1, 4, 1, 3320, 2, 9, 2)
)
if mibBuilder.loadTexts:
    bdltsLineTable.setStatus("mandatory")
_BdltsLineEntry_Object = MibTableRow
bdltsLineEntry = _BdltsLineEntry_Object(
    (1, 3, 6, 1, 4, 1, 3320, 2, 9, 2, 1)
)
bdltsLineEntry.setIndexNames(
    (0, "BDCOM-TS", "tsLineNumber"),
)
if mibBuilder.loadTexts:
    bdltsLineEntry.setStatus("mandatory")
_BdtsLineActive_Type = Integer32
_BdtsLineActive_Object = MibTableColumn
bdtsLineActive = _BdtsLineActive_Object(
    (1, 3, 6, 1, 4, 1, 3320, 2, 9, 2, 1, 1),
    _BdtsLineActive_Type()
)
bdtsLineActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bdtsLineActive.setStatus("mandatory")


class _BdtsLineType_Type(Integer32):
    """Custom type bdtsLineType based on Integer32"""
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


_BdtsLineType_Type.__name__ = "Integer32"
_BdtsLineType_Object = MibTableColumn
bdtsLineType = _BdtsLineType_Object(
    (1, 3, 6, 1, 4, 1, 3320, 2, 9, 2, 1, 2),
    _BdtsLineType_Type()
)
bdtsLineType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bdtsLineType.setStatus("mandatory")
_BdtsLineAutobaud_Type = Integer32
_BdtsLineAutobaud_Object = MibTableColumn
bdtsLineAutobaud = _BdtsLineAutobaud_Object(
    (1, 3, 6, 1, 4, 1, 3320, 2, 9, 2, 1, 3),
    _BdtsLineAutobaud_Type()
)
bdtsLineAutobaud.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bdtsLineAutobaud.setStatus("mandatory")
_BdtsLineSpeedin_Type = Integer32
_BdtsLineSpeedin_Object = MibTableColumn
bdtsLineSpeedin = _BdtsLineSpeedin_Object(
    (1, 3, 6, 1, 4, 1, 3320, 2, 9, 2, 1, 4),
    _BdtsLineSpeedin_Type()
)
bdtsLineSpeedin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bdtsLineSpeedin.setStatus("mandatory")
_BdtsLineSpeedout_Type = Integer32
_BdtsLineSpeedout_Object = MibTableColumn
bdtsLineSpeedout = _BdtsLineSpeedout_Object(
    (1, 3, 6, 1, 4, 1, 3320, 2, 9, 2, 1, 5),
    _BdtsLineSpeedout_Type()
)
bdtsLineSpeedout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bdtsLineSpeedout.setStatus("mandatory")


class _BdtsLineFlow_Type(Integer32):
    """Custom type bdtsLineFlow based on Integer32"""
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


_BdtsLineFlow_Type.__name__ = "Integer32"
_BdtsLineFlow_Object = MibTableColumn
bdtsLineFlow = _BdtsLineFlow_Object(
    (1, 3, 6, 1, 4, 1, 3320, 2, 9, 2, 1, 6),
    _BdtsLineFlow_Type()
)
bdtsLineFlow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bdtsLineFlow.setStatus("mandatory")


class _BdtsLineModem_Type(Integer32):
    """Custom type bdtsLineModem based on Integer32"""
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


_BdtsLineModem_Type.__name__ = "Integer32"
_BdtsLineModem_Object = MibTableColumn
bdtsLineModem = _BdtsLineModem_Object(
    (1, 3, 6, 1, 4, 1, 3320, 2, 9, 2, 1, 7),
    _BdtsLineModem_Type()
)
bdtsLineModem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bdtsLineModem.setStatus("mandatory")
_BdtsLineLoc_Type = DisplayString
_BdtsLineLoc_Object = MibTableColumn
bdtsLineLoc = _BdtsLineLoc_Object(
    (1, 3, 6, 1, 4, 1, 3320, 2, 9, 2, 1, 8),
    _BdtsLineLoc_Type()
)
bdtsLineLoc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bdtsLineLoc.setStatus("mandatory")
_BdtsLineTerm_Type = DisplayString
_BdtsLineTerm_Object = MibTableColumn
bdtsLineTerm = _BdtsLineTerm_Object(
    (1, 3, 6, 1, 4, 1, 3320, 2, 9, 2, 1, 9),
    _BdtsLineTerm_Type()
)
bdtsLineTerm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bdtsLineTerm.setStatus("mandatory")
_BdtsLineScrlen_Type = Integer32
_BdtsLineScrlen_Object = MibTableColumn
bdtsLineScrlen = _BdtsLineScrlen_Object(
    (1, 3, 6, 1, 4, 1, 3320, 2, 9, 2, 1, 10),
    _BdtsLineScrlen_Type()
)
bdtsLineScrlen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bdtsLineScrlen.setStatus("mandatory")
_BdtsLineScrwid_Type = Integer32
_BdtsLineScrwid_Object = MibTableColumn
bdtsLineScrwid = _BdtsLineScrwid_Object(
    (1, 3, 6, 1, 4, 1, 3320, 2, 9, 2, 1, 11),
    _BdtsLineScrwid_Type()
)
bdtsLineScrwid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bdtsLineScrwid.setStatus("mandatory")
_BdtsLineEsc_Type = DisplayString
_BdtsLineEsc_Object = MibTableColumn
bdtsLineEsc = _BdtsLineEsc_Object(
    (1, 3, 6, 1, 4, 1, 3320, 2, 9, 2, 1, 12),
    _BdtsLineEsc_Type()
)
bdtsLineEsc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bdtsLineEsc.setStatus("mandatory")
_BdtsLineTmo_Type = Integer32
_BdtsLineTmo_Object = MibTableColumn
bdtsLineTmo = _BdtsLineTmo_Object(
    (1, 3, 6, 1, 4, 1, 3320, 2, 9, 2, 1, 13),
    _BdtsLineTmo_Type()
)
bdtsLineTmo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bdtsLineTmo.setStatus("mandatory")
_BdtsLineSestmo_Type = Integer32
_BdtsLineSestmo_Object = MibTableColumn
bdtsLineSestmo = _BdtsLineSestmo_Object(
    (1, 3, 6, 1, 4, 1, 3320, 2, 9, 2, 1, 14),
    _BdtsLineSestmo_Type()
)
bdtsLineSestmo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bdtsLineSestmo.setStatus("mandatory")
_BdtsLineRotary_Type = Integer32
_BdtsLineRotary_Object = MibTableColumn
bdtsLineRotary = _BdtsLineRotary_Object(
    (1, 3, 6, 1, 4, 1, 3320, 2, 9, 2, 1, 15),
    _BdtsLineRotary_Type()
)
bdtsLineRotary.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bdtsLineRotary.setStatus("mandatory")
_BdtsLineUses_Type = Integer32
_BdtsLineUses_Object = MibTableColumn
bdtsLineUses = _BdtsLineUses_Object(
    (1, 3, 6, 1, 4, 1, 3320, 2, 9, 2, 1, 16),
    _BdtsLineUses_Type()
)
bdtsLineUses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bdtsLineUses.setStatus("mandatory")
_BdtsLineNses_Type = Integer32
_BdtsLineNses_Object = MibTableColumn
bdtsLineNses = _BdtsLineNses_Object(
    (1, 3, 6, 1, 4, 1, 3320, 2, 9, 2, 1, 17),
    _BdtsLineNses_Type()
)
bdtsLineNses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bdtsLineNses.setStatus("mandatory")
_BdtsLineUser_Type = DisplayString
_BdtsLineUser_Object = MibTableColumn
bdtsLineUser = _BdtsLineUser_Object(
    (1, 3, 6, 1, 4, 1, 3320, 2, 9, 2, 1, 18),
    _BdtsLineUser_Type()
)
bdtsLineUser.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bdtsLineUser.setStatus("mandatory")
_BdtsLineNoise_Type = Integer32
_BdtsLineNoise_Object = MibTableColumn
bdtsLineNoise = _BdtsLineNoise_Object(
    (1, 3, 6, 1, 4, 1, 3320, 2, 9, 2, 1, 19),
    _BdtsLineNoise_Type()
)
bdtsLineNoise.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bdtsLineNoise.setStatus("mandatory")
_BdtsLineNumber_Type = Integer32
_BdtsLineNumber_Object = MibTableColumn
bdtsLineNumber = _BdtsLineNumber_Object(
    (1, 3, 6, 1, 4, 1, 3320, 2, 9, 2, 1, 20),
    _BdtsLineNumber_Type()
)
bdtsLineNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bdtsLineNumber.setStatus("mandatory")
_BdtsLineTimeActive_Type = Integer32
_BdtsLineTimeActive_Object = MibTableColumn
bdtsLineTimeActive = _BdtsLineTimeActive_Object(
    (1, 3, 6, 1, 4, 1, 3320, 2, 9, 2, 1, 21),
    _BdtsLineTimeActive_Type()
)
bdtsLineTimeActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bdtsLineTimeActive.setStatus("mandatory")
_BdltsLineSessionTable_Object = MibTable
bdltsLineSessionTable = _BdltsLineSessionTable_Object(
    (1, 3, 6, 1, 4, 1, 3320, 2, 9, 3)
)
if mibBuilder.loadTexts:
    bdltsLineSessionTable.setStatus("mandatory")
_BdltsLineSessionEntry_Object = MibTableRow
bdltsLineSessionEntry = _BdltsLineSessionEntry_Object(
    (1, 3, 6, 1, 4, 1, 3320, 2, 9, 3, 1)
)
bdltsLineSessionEntry.setIndexNames(
    (0, "BDCOM-TS", "bdtslineSesLine"),
    (0, "BDCOM-TS", "bdtslineSesSession"),
)
if mibBuilder.loadTexts:
    bdltsLineSessionEntry.setStatus("mandatory")


class _BdtslineSesType_Type(Integer32):
    """Custom type bdtslineSesType based on Integer32"""
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


_BdtslineSesType_Type.__name__ = "Integer32"
_BdtslineSesType_Object = MibTableColumn
bdtslineSesType = _BdtslineSesType_Object(
    (1, 3, 6, 1, 4, 1, 3320, 2, 9, 3, 1, 1),
    _BdtslineSesType_Type()
)
bdtslineSesType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bdtslineSesType.setStatus("mandatory")


class _BdtslineSesDir_Type(Integer32):
    """Custom type bdtslineSesDir based on Integer32"""
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


_BdtslineSesDir_Type.__name__ = "Integer32"
_BdtslineSesDir_Object = MibTableColumn
bdtslineSesDir = _BdtslineSesDir_Object(
    (1, 3, 6, 1, 4, 1, 3320, 2, 9, 3, 1, 2),
    _BdtslineSesDir_Type()
)
bdtslineSesDir.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bdtslineSesDir.setStatus("mandatory")
_BdtslineSesAddr_Type = IpAddress
_BdtslineSesAddr_Object = MibTableColumn
bdtslineSesAddr = _BdtslineSesAddr_Object(
    (1, 3, 6, 1, 4, 1, 3320, 2, 9, 3, 1, 3),
    _BdtslineSesAddr_Type()
)
bdtslineSesAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bdtslineSesAddr.setStatus("mandatory")
_BdtslineSesName_Type = DisplayString
_BdtslineSesName_Object = MibTableColumn
bdtslineSesName = _BdtslineSesName_Object(
    (1, 3, 6, 1, 4, 1, 3320, 2, 9, 3, 1, 4),
    _BdtslineSesName_Type()
)
bdtslineSesName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bdtslineSesName.setStatus("mandatory")
_BdtslineSesCur_Type = Integer32
_BdtslineSesCur_Object = MibTableColumn
bdtslineSesCur = _BdtslineSesCur_Object(
    (1, 3, 6, 1, 4, 1, 3320, 2, 9, 3, 1, 5),
    _BdtslineSesCur_Type()
)
bdtslineSesCur.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bdtslineSesCur.setStatus("mandatory")
_BdtslineSesIdle_Type = Integer32
_BdtslineSesIdle_Object = MibTableColumn
bdtslineSesIdle = _BdtslineSesIdle_Object(
    (1, 3, 6, 1, 4, 1, 3320, 2, 9, 3, 1, 6),
    _BdtslineSesIdle_Type()
)
bdtslineSesIdle.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bdtslineSesIdle.setStatus("mandatory")
_BdtslineSesLine_Type = Integer32
_BdtslineSesLine_Object = MibTableColumn
bdtslineSesLine = _BdtslineSesLine_Object(
    (1, 3, 6, 1, 4, 1, 3320, 2, 9, 3, 1, 7),
    _BdtslineSesLine_Type()
)
bdtslineSesLine.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bdtslineSesLine.setStatus("mandatory")
_BdtslineSesSession_Type = Integer32
_BdtslineSesSession_Object = MibTableColumn
bdtslineSesSession = _BdtslineSesSession_Object(
    (1, 3, 6, 1, 4, 1, 3320, 2, 9, 3, 1, 8),
    _BdtslineSesSession_Type()
)
bdtslineSesSession.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bdtslineSesSession.setStatus("mandatory")
_BdtsMsgTtyLine_Type = Integer32
_BdtsMsgTtyLine_Object = MibScalar
bdtsMsgTtyLine = _BdtsMsgTtyLine_Object(
    (1, 3, 6, 1, 4, 1, 3320, 2, 9, 4),
    _BdtsMsgTtyLine_Type()
)
bdtsMsgTtyLine.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bdtsMsgTtyLine.setStatus("mandatory")
_BdtsMsgIntervaltim_Type = Integer32
_BdtsMsgIntervaltim_Object = MibScalar
bdtsMsgIntervaltim = _BdtsMsgIntervaltim_Object(
    (1, 3, 6, 1, 4, 1, 3320, 2, 9, 5),
    _BdtsMsgIntervaltim_Type()
)
bdtsMsgIntervaltim.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bdtsMsgIntervaltim.setStatus("mandatory")
_BdtsMsgDuration_Type = Integer32
_BdtsMsgDuration_Object = MibScalar
bdtsMsgDuration = _BdtsMsgDuration_Object(
    (1, 3, 6, 1, 4, 1, 3320, 2, 9, 6),
    _BdtsMsgDuration_Type()
)
bdtsMsgDuration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bdtsMsgDuration.setStatus("mandatory")
_BdtsMsgText_Type = DisplayString
_BdtsMsgText_Object = MibScalar
bdtsMsgText = _BdtsMsgText_Object(
    (1, 3, 6, 1, 4, 1, 3320, 2, 9, 7),
    _BdtsMsgText_Type()
)
bdtsMsgText.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bdtsMsgText.setStatus("mandatory")


class _BdtsMsgTmpBanner_Type(Integer32):
    """Custom type bdtsMsgTmpBanner based on Integer32"""
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


_BdtsMsgTmpBanner_Type.__name__ = "Integer32"
_BdtsMsgTmpBanner_Object = MibScalar
bdtsMsgTmpBanner = _BdtsMsgTmpBanner_Object(
    (1, 3, 6, 1, 4, 1, 3320, 2, 9, 8),
    _BdtsMsgTmpBanner_Type()
)
bdtsMsgTmpBanner.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bdtsMsgTmpBanner.setStatus("mandatory")


class _BdtsMsgSend_Type(Integer32):
    """Custom type bdtsMsgSend based on Integer32"""
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


_BdtsMsgSend_Type.__name__ = "Integer32"
_BdtsMsgSend_Object = MibScalar
bdtsMsgSend = _BdtsMsgSend_Object(
    (1, 3, 6, 1, 4, 1, 3320, 2, 9, 9),
    _BdtsMsgSend_Type()
)
bdtsMsgSend.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bdtsMsgSend.setStatus("mandatory")
_BdtsClrTtyLine_Type = Integer32
_BdtsClrTtyLine_Object = MibScalar
bdtsClrTtyLine = _BdtsClrTtyLine_Object(
    (1, 3, 6, 1, 4, 1, 3320, 2, 9, 10),
    _BdtsClrTtyLine_Type()
)
bdtsClrTtyLine.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bdtsClrTtyLine.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "BDCOM-TS",
    **{"bdlts": bdlts,
       "bdtsLines": bdtsLines,
       "bdltsLineTable": bdltsLineTable,
       "bdltsLineEntry": bdltsLineEntry,
       "bdtsLineActive": bdtsLineActive,
       "bdtsLineType": bdtsLineType,
       "bdtsLineAutobaud": bdtsLineAutobaud,
       "bdtsLineSpeedin": bdtsLineSpeedin,
       "bdtsLineSpeedout": bdtsLineSpeedout,
       "bdtsLineFlow": bdtsLineFlow,
       "bdtsLineModem": bdtsLineModem,
       "bdtsLineLoc": bdtsLineLoc,
       "bdtsLineTerm": bdtsLineTerm,
       "bdtsLineScrlen": bdtsLineScrlen,
       "bdtsLineScrwid": bdtsLineScrwid,
       "bdtsLineEsc": bdtsLineEsc,
       "bdtsLineTmo": bdtsLineTmo,
       "bdtsLineSestmo": bdtsLineSestmo,
       "bdtsLineRotary": bdtsLineRotary,
       "bdtsLineUses": bdtsLineUses,
       "bdtsLineNses": bdtsLineNses,
       "bdtsLineUser": bdtsLineUser,
       "bdtsLineNoise": bdtsLineNoise,
       "bdtsLineNumber": bdtsLineNumber,
       "bdtsLineTimeActive": bdtsLineTimeActive,
       "bdltsLineSessionTable": bdltsLineSessionTable,
       "bdltsLineSessionEntry": bdltsLineSessionEntry,
       "bdtslineSesType": bdtslineSesType,
       "bdtslineSesDir": bdtslineSesDir,
       "bdtslineSesAddr": bdtslineSesAddr,
       "bdtslineSesName": bdtslineSesName,
       "bdtslineSesCur": bdtslineSesCur,
       "bdtslineSesIdle": bdtslineSesIdle,
       "bdtslineSesLine": bdtslineSesLine,
       "bdtslineSesSession": bdtslineSesSession,
       "bdtsMsgTtyLine": bdtsMsgTtyLine,
       "bdtsMsgIntervaltim": bdtsMsgIntervaltim,
       "bdtsMsgDuration": bdtsMsgDuration,
       "bdtsMsgText": bdtsMsgText,
       "bdtsMsgTmpBanner": bdtsMsgTmpBanner,
       "bdtsMsgSend": bdtsMsgSend,
       "bdtsClrTtyLine": bdtsClrTtyLine}
)
