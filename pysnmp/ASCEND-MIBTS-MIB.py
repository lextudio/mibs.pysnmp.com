# SNMP MIB module (ASCEND-MIBTS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ASCEND-MIBTS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:42:29 2024
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

(configuration,) = mibBuilder.importSymbols(
    "ASCEND-MIB",
    "configuration")

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



class DisplayString(OctetString):
    """Custom type DisplayString based on OctetString"""



# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_MibtermSrvProfile_ObjectIdentity = ObjectIdentity
mibtermSrvProfile = _MibtermSrvProfile_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 529, 23, 133)
)
_MibtermSrvProfileTable_Object = MibTable
mibtermSrvProfileTable = _MibtermSrvProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 133, 1)
)
if mibBuilder.loadTexts:
    mibtermSrvProfileTable.setStatus("mandatory")
_MibtermSrvProfileEntry_Object = MibTableRow
mibtermSrvProfileEntry = _MibtermSrvProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 133, 1, 1)
)
mibtermSrvProfileEntry.setIndexNames(
    (0, "ASCEND-MIBTS-MIB", "termSrvProfile-Index-o"),
)
if mibBuilder.loadTexts:
    mibtermSrvProfileEntry.setStatus("mandatory")
_TermSrvProfile_Index_o_Type = Integer32
_TermSrvProfile_Index_o_Object = MibScalar
termSrvProfile_Index_o = _TermSrvProfile_Index_o_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 133, 1, 1, 1),
    _TermSrvProfile_Index_o_Type()
)
termSrvProfile_Index_o.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    termSrvProfile_Index_o.setStatus("mandatory")


class _TermSrvProfile_Enabled_Type(Integer32):
    """Custom type termSrvProfile_Enabled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_TermSrvProfile_Enabled_Type.__name__ = "Integer32"
_TermSrvProfile_Enabled_Object = MibScalar
termSrvProfile_Enabled = _TermSrvProfile_Enabled_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 133, 1, 1, 2),
    _TermSrvProfile_Enabled_Type()
)
termSrvProfile_Enabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    termSrvProfile_Enabled.setStatus("mandatory")


class _TermSrvProfile_SecurityMode_Type(Integer32):
    """Custom type termSrvProfile_SecurityMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("full", 3),
          ("none", 1),
          ("partial", 2))
    )


_TermSrvProfile_SecurityMode_Type.__name__ = "Integer32"
_TermSrvProfile_SecurityMode_Object = MibScalar
termSrvProfile_SecurityMode = _TermSrvProfile_SecurityMode_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 133, 1, 1, 3),
    _TermSrvProfile_SecurityMode_Type()
)
termSrvProfile_SecurityMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    termSrvProfile_SecurityMode.setStatus("mandatory")


class _TermSrvProfile_ModemConfiguration_V42_mnp_Type(Integer32):
    """Custom type termSrvProfile_ModemConfiguration_V42_mnp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("mustV42", 3),
          ("willV42", 2),
          ("wontV42", 1))
    )


_TermSrvProfile_ModemConfiguration_V42_mnp_Type.__name__ = "Integer32"
_TermSrvProfile_ModemConfiguration_V42_mnp_Object = MibScalar
termSrvProfile_ModemConfiguration_V42_mnp = _TermSrvProfile_ModemConfiguration_V42_mnp_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 133, 1, 1, 4),
    _TermSrvProfile_ModemConfiguration_V42_mnp_Type()
)
termSrvProfile_ModemConfiguration_V42_mnp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    termSrvProfile_ModemConfiguration_V42_mnp.setStatus("mandatory")


class _TermSrvProfile_ModemConfiguration_MaxBaudRate_Type(Integer32):
    """Custom type termSrvProfile_ModemConfiguration_MaxBaudRate based on Integer32"""
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
        *(("n-12000MaxBaud", 10),
          ("n-14400MaxBaud", 9),
          ("n-16800MaxBaud", 8),
          ("n-19200MaxBaud", 7),
          ("n-21600MaxBaud", 6),
          ("n-24000MaxBaud", 5),
          ("n-2400MaxBaud", 14),
          ("n-26400MaxBaud", 4),
          ("n-28800MaxBaud", 3),
          ("n-31200MaxBaud", 2),
          ("n-33600MaxBaud", 1),
          ("n-4800MaxBaud", 13),
          ("n-7200MaxBaud", 12),
          ("n-9600MaxBaud", 11))
    )


_TermSrvProfile_ModemConfiguration_MaxBaudRate_Type.__name__ = "Integer32"
_TermSrvProfile_ModemConfiguration_MaxBaudRate_Object = MibScalar
termSrvProfile_ModemConfiguration_MaxBaudRate = _TermSrvProfile_ModemConfiguration_MaxBaudRate_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 133, 1, 1, 5),
    _TermSrvProfile_ModemConfiguration_MaxBaudRate_Type()
)
termSrvProfile_ModemConfiguration_MaxBaudRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    termSrvProfile_ModemConfiguration_MaxBaudRate.setStatus("mandatory")


class _TermSrvProfile_ModemConfiguration_ModemTransmitLevel_Type(Integer32):
    """Custom type termSrvProfile_ModemConfiguration_ModemTransmitLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(11,
              12,
              13,
              14,
              15,
              16)
        )
    )
    namedValues = NamedValues(
        *(("level-13DbMdmTrnLevel", 11),
          ("level-14DbMdmTrnLevel", 12),
          ("level-15DbMdmTrnLevel", 13),
          ("level-16DbMdmTrnLevel", 14),
          ("level-17DbMdmTrnLevel", 15),
          ("level-18DbMdmTrnLevel", 16))
    )


_TermSrvProfile_ModemConfiguration_ModemTransmitLevel_Type.__name__ = "Integer32"
_TermSrvProfile_ModemConfiguration_ModemTransmitLevel_Object = MibScalar
termSrvProfile_ModemConfiguration_ModemTransmitLevel = _TermSrvProfile_ModemConfiguration_ModemTransmitLevel_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 133, 1, 1, 6),
    _TermSrvProfile_ModemConfiguration_ModemTransmitLevel_Type()
)
termSrvProfile_ModemConfiguration_ModemTransmitLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    termSrvProfile_ModemConfiguration_ModemTransmitLevel.setStatus("mandatory")


class _TermSrvProfile_ModemConfiguration_CellModeFirst_Type(Integer32):
    """Custom type termSrvProfile_ModemConfiguration_CellModeFirst based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_TermSrvProfile_ModemConfiguration_CellModeFirst_Type.__name__ = "Integer32"
_TermSrvProfile_ModemConfiguration_CellModeFirst_Object = MibScalar
termSrvProfile_ModemConfiguration_CellModeFirst = _TermSrvProfile_ModemConfiguration_CellModeFirst_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 133, 1, 1, 7),
    _TermSrvProfile_ModemConfiguration_CellModeFirst_Type()
)
termSrvProfile_ModemConfiguration_CellModeFirst.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    termSrvProfile_ModemConfiguration_CellModeFirst.setStatus("mandatory")


class _TermSrvProfile_ModemConfiguration_CellLevel_Type(Integer32):
    """Custom type termSrvProfile_ModemConfiguration_CellLevel based on Integer32"""
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
              9)
        )
    )
    namedValues = NamedValues(
        *(("level-10DbCellLevel", 9),
          ("level-11DbCellLevel", 8),
          ("level-12DbCellLevel", 7),
          ("level-13DbCellLevel", 6),
          ("level-14DbCellLevel", 5),
          ("level-15DbCellLevel", 4),
          ("level-16DbCellLevel", 3),
          ("level-17DbCellLevel", 2),
          ("level-18DbCellLevel", 1))
    )


_TermSrvProfile_ModemConfiguration_CellLevel_Type.__name__ = "Integer32"
_TermSrvProfile_ModemConfiguration_CellLevel_Object = MibScalar
termSrvProfile_ModemConfiguration_CellLevel = _TermSrvProfile_ModemConfiguration_CellLevel_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 133, 1, 1, 8),
    _TermSrvProfile_ModemConfiguration_CellLevel_Type()
)
termSrvProfile_ModemConfiguration_CellLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    termSrvProfile_ModemConfiguration_CellLevel.setStatus("mandatory")


class _TermSrvProfile_ModemConfiguration_o7Even_Type(Integer32):
    """Custom type termSrvProfile_ModemConfiguration_o7Even based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_TermSrvProfile_ModemConfiguration_o7Even_Type.__name__ = "Integer32"
_TermSrvProfile_ModemConfiguration_o7Even_Object = MibScalar
termSrvProfile_ModemConfiguration_o7Even = _TermSrvProfile_ModemConfiguration_o7Even_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 133, 1, 1, 9),
    _TermSrvProfile_ModemConfiguration_o7Even_Type()
)
termSrvProfile_ModemConfiguration_o7Even.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    termSrvProfile_ModemConfiguration_o7Even.setStatus("mandatory")


class _TermSrvProfile_ModemConfiguration_ModemMod_Type(Integer32):
    """Custom type termSrvProfile_ModemConfiguration_ModemMod based on Integer32"""
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
        *(("k56Modulation", 1),
          ("v34Modulation", 2),
          ("v90Modulation", 3),
          ("v92Modulation", 4))
    )


_TermSrvProfile_ModemConfiguration_ModemMod_Type.__name__ = "Integer32"
_TermSrvProfile_ModemConfiguration_ModemMod_Object = MibScalar
termSrvProfile_ModemConfiguration_ModemMod = _TermSrvProfile_ModemConfiguration_ModemMod_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 133, 1, 1, 10),
    _TermSrvProfile_ModemConfiguration_ModemMod_Type()
)
termSrvProfile_ModemConfiguration_ModemMod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    termSrvProfile_ModemConfiguration_ModemMod.setStatus("mandatory")
_TermSrvProfile_ModemConfiguration_oATAnswerString_Type = DisplayString
_TermSrvProfile_ModemConfiguration_oATAnswerString_Object = MibScalar
termSrvProfile_ModemConfiguration_oATAnswerString = _TermSrvProfile_ModemConfiguration_oATAnswerString_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 133, 1, 1, 11),
    _TermSrvProfile_ModemConfiguration_oATAnswerString_Type()
)
termSrvProfile_ModemConfiguration_oATAnswerString.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    termSrvProfile_ModemConfiguration_oATAnswerString.setStatus("mandatory")


class _TermSrvProfile_TerminalModeConfiguration_SilentMode_Type(Integer32):
    """Custom type termSrvProfile_TerminalModeConfiguration_SilentMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_TermSrvProfile_TerminalModeConfiguration_SilentMode_Type.__name__ = "Integer32"
_TermSrvProfile_TerminalModeConfiguration_SilentMode_Object = MibScalar
termSrvProfile_TerminalModeConfiguration_SilentMode = _TermSrvProfile_TerminalModeConfiguration_SilentMode_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 133, 1, 1, 12),
    _TermSrvProfile_TerminalModeConfiguration_SilentMode_Type()
)
termSrvProfile_TerminalModeConfiguration_SilentMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    termSrvProfile_TerminalModeConfiguration_SilentMode.setStatus("mandatory")


class _TermSrvProfile_TerminalModeConfiguration_ClearScreen_Type(Integer32):
    """Custom type termSrvProfile_TerminalModeConfiguration_ClearScreen based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_TermSrvProfile_TerminalModeConfiguration_ClearScreen_Type.__name__ = "Integer32"
_TermSrvProfile_TerminalModeConfiguration_ClearScreen_Object = MibScalar
termSrvProfile_TerminalModeConfiguration_ClearScreen = _TermSrvProfile_TerminalModeConfiguration_ClearScreen_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 133, 1, 1, 13),
    _TermSrvProfile_TerminalModeConfiguration_ClearScreen_Type()
)
termSrvProfile_TerminalModeConfiguration_ClearScreen.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    termSrvProfile_TerminalModeConfiguration_ClearScreen.setStatus("mandatory")
_TermSrvProfile_TerminalModeConfiguration_SystemPassword_Type = DisplayString
_TermSrvProfile_TerminalModeConfiguration_SystemPassword_Object = MibScalar
termSrvProfile_TerminalModeConfiguration_SystemPassword = _TermSrvProfile_TerminalModeConfiguration_SystemPassword_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 133, 1, 1, 14),
    _TermSrvProfile_TerminalModeConfiguration_SystemPassword_Type()
)
termSrvProfile_TerminalModeConfiguration_SystemPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    termSrvProfile_TerminalModeConfiguration_SystemPassword.setStatus("mandatory")
_TermSrvProfile_TerminalModeConfiguration_Banner_Type = DisplayString
_TermSrvProfile_TerminalModeConfiguration_Banner_Object = MibScalar
termSrvProfile_TerminalModeConfiguration_Banner = _TermSrvProfile_TerminalModeConfiguration_Banner_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 133, 1, 1, 15),
    _TermSrvProfile_TerminalModeConfiguration_Banner_Type()
)
termSrvProfile_TerminalModeConfiguration_Banner.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    termSrvProfile_TerminalModeConfiguration_Banner.setStatus("mandatory")
_TermSrvProfile_TerminalModeConfiguration_LoginPrompt_Type = DisplayString
_TermSrvProfile_TerminalModeConfiguration_LoginPrompt_Object = MibScalar
termSrvProfile_TerminalModeConfiguration_LoginPrompt = _TermSrvProfile_TerminalModeConfiguration_LoginPrompt_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 133, 1, 1, 16),
    _TermSrvProfile_TerminalModeConfiguration_LoginPrompt_Type()
)
termSrvProfile_TerminalModeConfiguration_LoginPrompt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    termSrvProfile_TerminalModeConfiguration_LoginPrompt.setStatus("mandatory")
_TermSrvProfile_TerminalModeConfiguration_PasswordPrompt_Type = DisplayString
_TermSrvProfile_TerminalModeConfiguration_PasswordPrompt_Object = MibScalar
termSrvProfile_TerminalModeConfiguration_PasswordPrompt = _TermSrvProfile_TerminalModeConfiguration_PasswordPrompt_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 133, 1, 1, 17),
    _TermSrvProfile_TerminalModeConfiguration_PasswordPrompt_Type()
)
termSrvProfile_TerminalModeConfiguration_PasswordPrompt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    termSrvProfile_TerminalModeConfiguration_PasswordPrompt.setStatus("mandatory")
_TermSrvProfile_TerminalModeConfiguration_ThirdLoginPrompt_Type = DisplayString
_TermSrvProfile_TerminalModeConfiguration_ThirdLoginPrompt_Object = MibScalar
termSrvProfile_TerminalModeConfiguration_ThirdLoginPrompt = _TermSrvProfile_TerminalModeConfiguration_ThirdLoginPrompt_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 133, 1, 1, 18),
    _TermSrvProfile_TerminalModeConfiguration_ThirdLoginPrompt_Type()
)
termSrvProfile_TerminalModeConfiguration_ThirdLoginPrompt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    termSrvProfile_TerminalModeConfiguration_ThirdLoginPrompt.setStatus("mandatory")


class _TermSrvProfile_TerminalModeConfiguration_ThirdPromptSequence_Type(Integer32):
    """Custom type termSrvProfile_TerminalModeConfiguration_ThirdPromptSequence based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("first", 2),
          ("last", 1))
    )


_TermSrvProfile_TerminalModeConfiguration_ThirdPromptSequence_Type.__name__ = "Integer32"
_TermSrvProfile_TerminalModeConfiguration_ThirdPromptSequence_Object = MibScalar
termSrvProfile_TerminalModeConfiguration_ThirdPromptSequence = _TermSrvProfile_TerminalModeConfiguration_ThirdPromptSequence_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 133, 1, 1, 19),
    _TermSrvProfile_TerminalModeConfiguration_ThirdPromptSequence_Type()
)
termSrvProfile_TerminalModeConfiguration_ThirdPromptSequence.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    termSrvProfile_TerminalModeConfiguration_ThirdPromptSequence.setStatus("mandatory")
_TermSrvProfile_TerminalModeConfiguration_Prompt_Type = DisplayString
_TermSrvProfile_TerminalModeConfiguration_Prompt_Object = MibScalar
termSrvProfile_TerminalModeConfiguration_Prompt = _TermSrvProfile_TerminalModeConfiguration_Prompt_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 133, 1, 1, 20),
    _TermSrvProfile_TerminalModeConfiguration_Prompt_Type()
)
termSrvProfile_TerminalModeConfiguration_Prompt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    termSrvProfile_TerminalModeConfiguration_Prompt.setStatus("mandatory")
_TermSrvProfile_TerminalModeConfiguration_TerminalType_Type = DisplayString
_TermSrvProfile_TerminalModeConfiguration_TerminalType_Object = MibScalar
termSrvProfile_TerminalModeConfiguration_TerminalType = _TermSrvProfile_TerminalModeConfiguration_TerminalType_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 133, 1, 1, 21),
    _TermSrvProfile_TerminalModeConfiguration_TerminalType_Type()
)
termSrvProfile_TerminalModeConfiguration_TerminalType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    termSrvProfile_TerminalModeConfiguration_TerminalType.setStatus("mandatory")


class _TermSrvProfile_TerminalModeConfiguration_ClearCall_Type(Integer32):
    """Custom type termSrvProfile_TerminalModeConfiguration_ClearCall based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_TermSrvProfile_TerminalModeConfiguration_ClearCall_Type.__name__ = "Integer32"
_TermSrvProfile_TerminalModeConfiguration_ClearCall_Object = MibScalar
termSrvProfile_TerminalModeConfiguration_ClearCall = _TermSrvProfile_TerminalModeConfiguration_ClearCall_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 133, 1, 1, 22),
    _TermSrvProfile_TerminalModeConfiguration_ClearCall_Type()
)
termSrvProfile_TerminalModeConfiguration_ClearCall.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    termSrvProfile_TerminalModeConfiguration_ClearCall.setStatus("mandatory")


class _TermSrvProfile_TerminalModeConfiguration_BufferChars_Type(Integer32):
    """Custom type termSrvProfile_TerminalModeConfiguration_BufferChars based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_TermSrvProfile_TerminalModeConfiguration_BufferChars_Type.__name__ = "Integer32"
_TermSrvProfile_TerminalModeConfiguration_BufferChars_Object = MibScalar
termSrvProfile_TerminalModeConfiguration_BufferChars = _TermSrvProfile_TerminalModeConfiguration_BufferChars_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 133, 1, 1, 23),
    _TermSrvProfile_TerminalModeConfiguration_BufferChars_Type()
)
termSrvProfile_TerminalModeConfiguration_BufferChars.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    termSrvProfile_TerminalModeConfiguration_BufferChars.setStatus("mandatory")


class _TermSrvProfile_TerminalModeConfiguration_Ping_Type(Integer32):
    """Custom type termSrvProfile_TerminalModeConfiguration_Ping based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_TermSrvProfile_TerminalModeConfiguration_Ping_Type.__name__ = "Integer32"
_TermSrvProfile_TerminalModeConfiguration_Ping_Object = MibScalar
termSrvProfile_TerminalModeConfiguration_Ping = _TermSrvProfile_TerminalModeConfiguration_Ping_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 133, 1, 1, 24),
    _TermSrvProfile_TerminalModeConfiguration_Ping_Type()
)
termSrvProfile_TerminalModeConfiguration_Ping.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    termSrvProfile_TerminalModeConfiguration_Ping.setStatus("mandatory")


class _TermSrvProfile_TerminalModeConfiguration_Traceroute_Type(Integer32):
    """Custom type termSrvProfile_TerminalModeConfiguration_Traceroute based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_TermSrvProfile_TerminalModeConfiguration_Traceroute_Type.__name__ = "Integer32"
_TermSrvProfile_TerminalModeConfiguration_Traceroute_Object = MibScalar
termSrvProfile_TerminalModeConfiguration_Traceroute = _TermSrvProfile_TerminalModeConfiguration_Traceroute_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 133, 1, 1, 25),
    _TermSrvProfile_TerminalModeConfiguration_Traceroute_Type()
)
termSrvProfile_TerminalModeConfiguration_Traceroute.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    termSrvProfile_TerminalModeConfiguration_Traceroute.setStatus("mandatory")


class _TermSrvProfile_TerminalModeConfiguration_Tcp_Type(Integer32):
    """Custom type termSrvProfile_TerminalModeConfiguration_Tcp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_TermSrvProfile_TerminalModeConfiguration_Tcp_Type.__name__ = "Integer32"
_TermSrvProfile_TerminalModeConfiguration_Tcp_Object = MibScalar
termSrvProfile_TerminalModeConfiguration_Tcp = _TermSrvProfile_TerminalModeConfiguration_Tcp_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 133, 1, 1, 26),
    _TermSrvProfile_TerminalModeConfiguration_Tcp_Type()
)
termSrvProfile_TerminalModeConfiguration_Tcp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    termSrvProfile_TerminalModeConfiguration_Tcp.setStatus("mandatory")


class _TermSrvProfile_TerminalModeConfiguration_TsAraEnabled_Type(Integer32):
    """Custom type termSrvProfile_TerminalModeConfiguration_TsAraEnabled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_TermSrvProfile_TerminalModeConfiguration_TsAraEnabled_Type.__name__ = "Integer32"
_TermSrvProfile_TerminalModeConfiguration_TsAraEnabled_Object = MibScalar
termSrvProfile_TerminalModeConfiguration_TsAraEnabled = _TermSrvProfile_TerminalModeConfiguration_TsAraEnabled_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 133, 1, 1, 27),
    _TermSrvProfile_TerminalModeConfiguration_TsAraEnabled_Type()
)
termSrvProfile_TerminalModeConfiguration_TsAraEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    termSrvProfile_TerminalModeConfiguration_TsAraEnabled.setStatus("mandatory")


class _TermSrvProfile_TerminalModeConfiguration_RloginOptions_Rlogin_Type(Integer32):
    """Custom type termSrvProfile_TerminalModeConfiguration_RloginOptions_Rlogin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_TermSrvProfile_TerminalModeConfiguration_RloginOptions_Rlogin_Type.__name__ = "Integer32"
_TermSrvProfile_TerminalModeConfiguration_RloginOptions_Rlogin_Object = MibScalar
termSrvProfile_TerminalModeConfiguration_RloginOptions_Rlogin = _TermSrvProfile_TerminalModeConfiguration_RloginOptions_Rlogin_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 133, 1, 1, 28),
    _TermSrvProfile_TerminalModeConfiguration_RloginOptions_Rlogin_Type()
)
termSrvProfile_TerminalModeConfiguration_RloginOptions_Rlogin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    termSrvProfile_TerminalModeConfiguration_RloginOptions_Rlogin.setStatus("mandatory")
_TermSrvProfile_TerminalModeConfiguration_RloginOptions_MaxSourcePort_Type = Integer32
_TermSrvProfile_TerminalModeConfiguration_RloginOptions_MaxSourcePort_Object = MibScalar
termSrvProfile_TerminalModeConfiguration_RloginOptions_MaxSourcePort = _TermSrvProfile_TerminalModeConfiguration_RloginOptions_MaxSourcePort_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 133, 1, 1, 29),
    _TermSrvProfile_TerminalModeConfiguration_RloginOptions_MaxSourcePort_Type()
)
termSrvProfile_TerminalModeConfiguration_RloginOptions_MaxSourcePort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    termSrvProfile_TerminalModeConfiguration_RloginOptions_MaxSourcePort.setStatus("mandatory")
_TermSrvProfile_TerminalModeConfiguration_RloginOptions_MinSourcePort_Type = Integer32
_TermSrvProfile_TerminalModeConfiguration_RloginOptions_MinSourcePort_Object = MibScalar
termSrvProfile_TerminalModeConfiguration_RloginOptions_MinSourcePort = _TermSrvProfile_TerminalModeConfiguration_RloginOptions_MinSourcePort_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 133, 1, 1, 30),
    _TermSrvProfile_TerminalModeConfiguration_RloginOptions_MinSourcePort_Type()
)
termSrvProfile_TerminalModeConfiguration_RloginOptions_MinSourcePort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    termSrvProfile_TerminalModeConfiguration_RloginOptions_MinSourcePort.setStatus("mandatory")


class _TermSrvProfile_TerminalModeConfiguration_TelnetOptions_Telnet_Type(Integer32):
    """Custom type termSrvProfile_TerminalModeConfiguration_TelnetOptions_Telnet based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_TermSrvProfile_TerminalModeConfiguration_TelnetOptions_Telnet_Type.__name__ = "Integer32"
_TermSrvProfile_TerminalModeConfiguration_TelnetOptions_Telnet_Object = MibScalar
termSrvProfile_TerminalModeConfiguration_TelnetOptions_Telnet = _TermSrvProfile_TerminalModeConfiguration_TelnetOptions_Telnet_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 133, 1, 1, 31),
    _TermSrvProfile_TerminalModeConfiguration_TelnetOptions_Telnet_Type()
)
termSrvProfile_TerminalModeConfiguration_TelnetOptions_Telnet.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    termSrvProfile_TerminalModeConfiguration_TelnetOptions_Telnet.setStatus("mandatory")


class _TermSrvProfile_TerminalModeConfiguration_TelnetOptions_TelnetMode_Type(Integer32):
    """Custom type termSrvProfile_TerminalModeConfiguration_TelnetOptions_TelnetMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("ascii", 1),
          ("binary", 2),
          ("transparent", 3))
    )


_TermSrvProfile_TerminalModeConfiguration_TelnetOptions_TelnetMode_Type.__name__ = "Integer32"
_TermSrvProfile_TerminalModeConfiguration_TelnetOptions_TelnetMode_Object = MibScalar
termSrvProfile_TerminalModeConfiguration_TelnetOptions_TelnetMode = _TermSrvProfile_TerminalModeConfiguration_TelnetOptions_TelnetMode_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 133, 1, 1, 32),
    _TermSrvProfile_TerminalModeConfiguration_TelnetOptions_TelnetMode_Type()
)
termSrvProfile_TerminalModeConfiguration_TelnetOptions_TelnetMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    termSrvProfile_TerminalModeConfiguration_TelnetOptions_TelnetMode.setStatus("mandatory")


class _TermSrvProfile_TerminalModeConfiguration_TelnetOptions_AutoTelnet_Type(Integer32):
    """Custom type termSrvProfile_TerminalModeConfiguration_TelnetOptions_AutoTelnet based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_TermSrvProfile_TerminalModeConfiguration_TelnetOptions_AutoTelnet_Type.__name__ = "Integer32"
_TermSrvProfile_TerminalModeConfiguration_TelnetOptions_AutoTelnet_Object = MibScalar
termSrvProfile_TerminalModeConfiguration_TelnetOptions_AutoTelnet = _TermSrvProfile_TerminalModeConfiguration_TelnetOptions_AutoTelnet_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 133, 1, 1, 33),
    _TermSrvProfile_TerminalModeConfiguration_TelnetOptions_AutoTelnet_Type()
)
termSrvProfile_TerminalModeConfiguration_TelnetOptions_AutoTelnet.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    termSrvProfile_TerminalModeConfiguration_TelnetOptions_AutoTelnet.setStatus("mandatory")


class _TermSrvProfile_TerminalModeConfiguration_TelnetOptions_LocalEcho_Type(Integer32):
    """Custom type termSrvProfile_TerminalModeConfiguration_TelnetOptions_LocalEcho based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_TermSrvProfile_TerminalModeConfiguration_TelnetOptions_LocalEcho_Type.__name__ = "Integer32"
_TermSrvProfile_TerminalModeConfiguration_TelnetOptions_LocalEcho_Object = MibScalar
termSrvProfile_TerminalModeConfiguration_TelnetOptions_LocalEcho = _TermSrvProfile_TerminalModeConfiguration_TelnetOptions_LocalEcho_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 133, 1, 1, 34),
    _TermSrvProfile_TerminalModeConfiguration_TelnetOptions_LocalEcho_Type()
)
termSrvProfile_TerminalModeConfiguration_TelnetOptions_LocalEcho.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    termSrvProfile_TerminalModeConfiguration_TelnetOptions_LocalEcho.setStatus("mandatory")


class _TermSrvProfile_TerminalModeConfiguration_TelnetOptions_Security_Type(Integer32):
    """Custom type termSrvProfile_TerminalModeConfiguration_TelnetOptions_Security based on Integer32"""
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
        *(("telnetSecurityAuthSetting", 4),
          ("telnetSecurityGlobal", 2),
          ("telnetSecurityNone", 1),
          ("telnetSecurityProfile", 3))
    )


_TermSrvProfile_TerminalModeConfiguration_TelnetOptions_Security_Type.__name__ = "Integer32"
_TermSrvProfile_TerminalModeConfiguration_TelnetOptions_Security_Object = MibScalar
termSrvProfile_TerminalModeConfiguration_TelnetOptions_Security = _TermSrvProfile_TerminalModeConfiguration_TelnetOptions_Security_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 133, 1, 1, 35),
    _TermSrvProfile_TerminalModeConfiguration_TelnetOptions_Security_Type()
)
termSrvProfile_TerminalModeConfiguration_TelnetOptions_Security.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    termSrvProfile_TerminalModeConfiguration_TelnetOptions_Security.setStatus("mandatory")
_TermSrvProfile_TerminalModeConfiguration_IpAddMsg_Type = DisplayString
_TermSrvProfile_TerminalModeConfiguration_IpAddMsg_Object = MibScalar
termSrvProfile_TerminalModeConfiguration_IpAddMsg = _TermSrvProfile_TerminalModeConfiguration_IpAddMsg_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 133, 1, 1, 36),
    _TermSrvProfile_TerminalModeConfiguration_IpAddMsg_Type()
)
termSrvProfile_TerminalModeConfiguration_IpAddMsg.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    termSrvProfile_TerminalModeConfiguration_IpAddMsg.setStatus("mandatory")


class _TermSrvProfile_TerminalModeConfiguration_PromptFormat_Type(Integer32):
    """Custom type termSrvProfile_TerminalModeConfiguration_PromptFormat based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_TermSrvProfile_TerminalModeConfiguration_PromptFormat_Type.__name__ = "Integer32"
_TermSrvProfile_TerminalModeConfiguration_PromptFormat_Object = MibScalar
termSrvProfile_TerminalModeConfiguration_PromptFormat = _TermSrvProfile_TerminalModeConfiguration_PromptFormat_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 133, 1, 1, 37),
    _TermSrvProfile_TerminalModeConfiguration_PromptFormat_Type()
)
termSrvProfile_TerminalModeConfiguration_PromptFormat.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    termSrvProfile_TerminalModeConfiguration_PromptFormat.setStatus("mandatory")
_TermSrvProfile_TerminalModeConfiguration_IpNetmaskMsg_Type = DisplayString
_TermSrvProfile_TerminalModeConfiguration_IpNetmaskMsg_Object = MibScalar
termSrvProfile_TerminalModeConfiguration_IpNetmaskMsg = _TermSrvProfile_TerminalModeConfiguration_IpNetmaskMsg_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 133, 1, 1, 38),
    _TermSrvProfile_TerminalModeConfiguration_IpNetmaskMsg_Type()
)
termSrvProfile_TerminalModeConfiguration_IpNetmaskMsg.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    termSrvProfile_TerminalModeConfiguration_IpNetmaskMsg.setStatus("mandatory")
_TermSrvProfile_TerminalModeConfiguration_IpGwAddMsg_Type = DisplayString
_TermSrvProfile_TerminalModeConfiguration_IpGwAddMsg_Object = MibScalar
termSrvProfile_TerminalModeConfiguration_IpGwAddMsg = _TermSrvProfile_TerminalModeConfiguration_IpGwAddMsg_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 133, 1, 1, 39),
    _TermSrvProfile_TerminalModeConfiguration_IpGwAddMsg_Type()
)
termSrvProfile_TerminalModeConfiguration_IpGwAddMsg.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    termSrvProfile_TerminalModeConfiguration_IpGwAddMsg.setStatus("mandatory")
_TermSrvProfile_TerminalModeConfiguration_LoginTimeout_Type = Integer32
_TermSrvProfile_TerminalModeConfiguration_LoginTimeout_Object = MibScalar
termSrvProfile_TerminalModeConfiguration_LoginTimeout = _TermSrvProfile_TerminalModeConfiguration_LoginTimeout_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 133, 1, 1, 40),
    _TermSrvProfile_TerminalModeConfiguration_LoginTimeout_Type()
)
termSrvProfile_TerminalModeConfiguration_LoginTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    termSrvProfile_TerminalModeConfiguration_LoginTimeout.setStatus("mandatory")
_TermSrvProfile_TerminalModeConfiguration_PacketizeWaitTime_Type = Integer32
_TermSrvProfile_TerminalModeConfiguration_PacketizeWaitTime_Object = MibScalar
termSrvProfile_TerminalModeConfiguration_PacketizeWaitTime = _TermSrvProfile_TerminalModeConfiguration_PacketizeWaitTime_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 133, 1, 1, 41),
    _TermSrvProfile_TerminalModeConfiguration_PacketizeWaitTime_Type()
)
termSrvProfile_TerminalModeConfiguration_PacketizeWaitTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    termSrvProfile_TerminalModeConfiguration_PacketizeWaitTime.setStatus("mandatory")
_TermSrvProfile_TerminalModeConfiguration_PacketizeChars_Type = Integer32
_TermSrvProfile_TerminalModeConfiguration_PacketizeChars_Object = MibScalar
termSrvProfile_TerminalModeConfiguration_PacketizeChars = _TermSrvProfile_TerminalModeConfiguration_PacketizeChars_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 133, 1, 1, 42),
    _TermSrvProfile_TerminalModeConfiguration_PacketizeChars_Type()
)
termSrvProfile_TerminalModeConfiguration_PacketizeChars.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    termSrvProfile_TerminalModeConfiguration_PacketizeChars.setStatus("mandatory")


class _TermSrvProfile_ImmediateModeOptions_Service_Type(Integer32):
    """Custom type termSrvProfile_ImmediateModeOptions_Service based on Integer32"""
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
        *(("none", 1),
          ("rawTcp", 3),
          ("rlogin", 4),
          ("telnet", 2),
          ("x25Pad", 5),
          ("x25T3pos", 6))
    )


_TermSrvProfile_ImmediateModeOptions_Service_Type.__name__ = "Integer32"
_TermSrvProfile_ImmediateModeOptions_Service_Object = MibScalar
termSrvProfile_ImmediateModeOptions_Service = _TermSrvProfile_ImmediateModeOptions_Service_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 133, 1, 1, 43),
    _TermSrvProfile_ImmediateModeOptions_Service_Type()
)
termSrvProfile_ImmediateModeOptions_Service.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    termSrvProfile_ImmediateModeOptions_Service.setStatus("mandatory")


class _TermSrvProfile_ImmediateModeOptions_TelnetHostAuth_Type(Integer32):
    """Custom type termSrvProfile_ImmediateModeOptions_TelnetHostAuth based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_TermSrvProfile_ImmediateModeOptions_TelnetHostAuth_Type.__name__ = "Integer32"
_TermSrvProfile_ImmediateModeOptions_TelnetHostAuth_Object = MibScalar
termSrvProfile_ImmediateModeOptions_TelnetHostAuth = _TermSrvProfile_ImmediateModeOptions_TelnetHostAuth_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 133, 1, 1, 44),
    _TermSrvProfile_ImmediateModeOptions_TelnetHostAuth_Type()
)
termSrvProfile_ImmediateModeOptions_TelnetHostAuth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    termSrvProfile_ImmediateModeOptions_TelnetHostAuth.setStatus("mandatory")
_TermSrvProfile_ImmediateModeOptions_Host_Type = DisplayString
_TermSrvProfile_ImmediateModeOptions_Host_Object = MibScalar
termSrvProfile_ImmediateModeOptions_Host = _TermSrvProfile_ImmediateModeOptions_Host_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 133, 1, 1, 45),
    _TermSrvProfile_ImmediateModeOptions_Host_Type()
)
termSrvProfile_ImmediateModeOptions_Host.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    termSrvProfile_ImmediateModeOptions_Host.setStatus("mandatory")
_TermSrvProfile_ImmediateModeOptions_Port_Type = Integer32
_TermSrvProfile_ImmediateModeOptions_Port_Object = MibScalar
termSrvProfile_ImmediateModeOptions_Port = _TermSrvProfile_ImmediateModeOptions_Port_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 133, 1, 1, 46),
    _TermSrvProfile_ImmediateModeOptions_Port_Type()
)
termSrvProfile_ImmediateModeOptions_Port.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    termSrvProfile_ImmediateModeOptions_Port.setStatus("mandatory")


class _TermSrvProfile_MenuModeOptions_StartWithMenus_Type(Integer32):
    """Custom type termSrvProfile_MenuModeOptions_StartWithMenus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_TermSrvProfile_MenuModeOptions_StartWithMenus_Type.__name__ = "Integer32"
_TermSrvProfile_MenuModeOptions_StartWithMenus_Object = MibScalar
termSrvProfile_MenuModeOptions_StartWithMenus = _TermSrvProfile_MenuModeOptions_StartWithMenus_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 133, 1, 1, 47),
    _TermSrvProfile_MenuModeOptions_StartWithMenus_Type()
)
termSrvProfile_MenuModeOptions_StartWithMenus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    termSrvProfile_MenuModeOptions_StartWithMenus.setStatus("mandatory")


class _TermSrvProfile_MenuModeOptions_ToggleScreen_Type(Integer32):
    """Custom type termSrvProfile_MenuModeOptions_ToggleScreen based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_TermSrvProfile_MenuModeOptions_ToggleScreen_Type.__name__ = "Integer32"
_TermSrvProfile_MenuModeOptions_ToggleScreen_Object = MibScalar
termSrvProfile_MenuModeOptions_ToggleScreen = _TermSrvProfile_MenuModeOptions_ToggleScreen_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 133, 1, 1, 48),
    _TermSrvProfile_MenuModeOptions_ToggleScreen_Type()
)
termSrvProfile_MenuModeOptions_ToggleScreen.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    termSrvProfile_MenuModeOptions_ToggleScreen.setStatus("mandatory")


class _TermSrvProfile_MenuModeOptions_RemoteConfiguration_Type(Integer32):
    """Custom type termSrvProfile_MenuModeOptions_RemoteConfiguration based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_TermSrvProfile_MenuModeOptions_RemoteConfiguration_Type.__name__ = "Integer32"
_TermSrvProfile_MenuModeOptions_RemoteConfiguration_Object = MibScalar
termSrvProfile_MenuModeOptions_RemoteConfiguration = _TermSrvProfile_MenuModeOptions_RemoteConfiguration_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 133, 1, 1, 49),
    _TermSrvProfile_MenuModeOptions_RemoteConfiguration_Type()
)
termSrvProfile_MenuModeOptions_RemoteConfiguration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    termSrvProfile_MenuModeOptions_RemoteConfiguration.setStatus("mandatory")
_TermSrvProfile_MenuModeOptions_Text1_Type = DisplayString
_TermSrvProfile_MenuModeOptions_Text1_Object = MibScalar
termSrvProfile_MenuModeOptions_Text1 = _TermSrvProfile_MenuModeOptions_Text1_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 133, 1, 1, 50),
    _TermSrvProfile_MenuModeOptions_Text1_Type()
)
termSrvProfile_MenuModeOptions_Text1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    termSrvProfile_MenuModeOptions_Text1.setStatus("mandatory")
_TermSrvProfile_MenuModeOptions_Host1_Type = DisplayString
_TermSrvProfile_MenuModeOptions_Host1_Object = MibScalar
termSrvProfile_MenuModeOptions_Host1 = _TermSrvProfile_MenuModeOptions_Host1_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 133, 1, 1, 51),
    _TermSrvProfile_MenuModeOptions_Host1_Type()
)
termSrvProfile_MenuModeOptions_Host1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    termSrvProfile_MenuModeOptions_Host1.setStatus("mandatory")


class _TermSrvProfile_MenuModeOptions_Service1_Type(Integer32):
    """Custom type termSrvProfile_MenuModeOptions_Service1 based on Integer32"""
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
        *(("ppp", 3),
          ("rawtcp", 4),
          ("rlogin", 2),
          ("telnet", 1))
    )


_TermSrvProfile_MenuModeOptions_Service1_Type.__name__ = "Integer32"
_TermSrvProfile_MenuModeOptions_Service1_Object = MibScalar
termSrvProfile_MenuModeOptions_Service1 = _TermSrvProfile_MenuModeOptions_Service1_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 133, 1, 1, 52),
    _TermSrvProfile_MenuModeOptions_Service1_Type()
)
termSrvProfile_MenuModeOptions_Service1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    termSrvProfile_MenuModeOptions_Service1.setStatus("mandatory")
_TermSrvProfile_MenuModeOptions_Port1_Type = Integer32
_TermSrvProfile_MenuModeOptions_Port1_Object = MibScalar
termSrvProfile_MenuModeOptions_Port1 = _TermSrvProfile_MenuModeOptions_Port1_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 133, 1, 1, 53),
    _TermSrvProfile_MenuModeOptions_Port1_Type()
)
termSrvProfile_MenuModeOptions_Port1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    termSrvProfile_MenuModeOptions_Port1.setStatus("mandatory")
_TermSrvProfile_MenuModeOptions_User1_Type = DisplayString
_TermSrvProfile_MenuModeOptions_User1_Object = MibScalar
termSrvProfile_MenuModeOptions_User1 = _TermSrvProfile_MenuModeOptions_User1_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 133, 1, 1, 54),
    _TermSrvProfile_MenuModeOptions_User1_Type()
)
termSrvProfile_MenuModeOptions_User1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    termSrvProfile_MenuModeOptions_User1.setStatus("mandatory")
_TermSrvProfile_MenuModeOptions_Text2_Type = DisplayString
_TermSrvProfile_MenuModeOptions_Text2_Object = MibScalar
termSrvProfile_MenuModeOptions_Text2 = _TermSrvProfile_MenuModeOptions_Text2_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 133, 1, 1, 55),
    _TermSrvProfile_MenuModeOptions_Text2_Type()
)
termSrvProfile_MenuModeOptions_Text2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    termSrvProfile_MenuModeOptions_Text2.setStatus("mandatory")
_TermSrvProfile_MenuModeOptions_Host2_Type = DisplayString
_TermSrvProfile_MenuModeOptions_Host2_Object = MibScalar
termSrvProfile_MenuModeOptions_Host2 = _TermSrvProfile_MenuModeOptions_Host2_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 133, 1, 1, 56),
    _TermSrvProfile_MenuModeOptions_Host2_Type()
)
termSrvProfile_MenuModeOptions_Host2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    termSrvProfile_MenuModeOptions_Host2.setStatus("mandatory")


class _TermSrvProfile_MenuModeOptions_Service2_Type(Integer32):
    """Custom type termSrvProfile_MenuModeOptions_Service2 based on Integer32"""
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
        *(("ppp", 3),
          ("rawtcp", 4),
          ("rlogin", 2),
          ("telnet", 1))
    )


_TermSrvProfile_MenuModeOptions_Service2_Type.__name__ = "Integer32"
_TermSrvProfile_MenuModeOptions_Service2_Object = MibScalar
termSrvProfile_MenuModeOptions_Service2 = _TermSrvProfile_MenuModeOptions_Service2_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 133, 1, 1, 57),
    _TermSrvProfile_MenuModeOptions_Service2_Type()
)
termSrvProfile_MenuModeOptions_Service2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    termSrvProfile_MenuModeOptions_Service2.setStatus("mandatory")
_TermSrvProfile_MenuModeOptions_Port2_Type = Integer32
_TermSrvProfile_MenuModeOptions_Port2_Object = MibScalar
termSrvProfile_MenuModeOptions_Port2 = _TermSrvProfile_MenuModeOptions_Port2_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 133, 1, 1, 58),
    _TermSrvProfile_MenuModeOptions_Port2_Type()
)
termSrvProfile_MenuModeOptions_Port2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    termSrvProfile_MenuModeOptions_Port2.setStatus("mandatory")
_TermSrvProfile_MenuModeOptions_User2_Type = DisplayString
_TermSrvProfile_MenuModeOptions_User2_Object = MibScalar
termSrvProfile_MenuModeOptions_User2 = _TermSrvProfile_MenuModeOptions_User2_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 133, 1, 1, 59),
    _TermSrvProfile_MenuModeOptions_User2_Type()
)
termSrvProfile_MenuModeOptions_User2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    termSrvProfile_MenuModeOptions_User2.setStatus("mandatory")
_TermSrvProfile_MenuModeOptions_Text3_Type = DisplayString
_TermSrvProfile_MenuModeOptions_Text3_Object = MibScalar
termSrvProfile_MenuModeOptions_Text3 = _TermSrvProfile_MenuModeOptions_Text3_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 133, 1, 1, 60),
    _TermSrvProfile_MenuModeOptions_Text3_Type()
)
termSrvProfile_MenuModeOptions_Text3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    termSrvProfile_MenuModeOptions_Text3.setStatus("mandatory")
_TermSrvProfile_MenuModeOptions_Host3_Type = DisplayString
_TermSrvProfile_MenuModeOptions_Host3_Object = MibScalar
termSrvProfile_MenuModeOptions_Host3 = _TermSrvProfile_MenuModeOptions_Host3_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 133, 1, 1, 61),
    _TermSrvProfile_MenuModeOptions_Host3_Type()
)
termSrvProfile_MenuModeOptions_Host3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    termSrvProfile_MenuModeOptions_Host3.setStatus("mandatory")


class _TermSrvProfile_MenuModeOptions_Service3_Type(Integer32):
    """Custom type termSrvProfile_MenuModeOptions_Service3 based on Integer32"""
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
        *(("ppp", 3),
          ("rawtcp", 4),
          ("rlogin", 2),
          ("telnet", 1))
    )


_TermSrvProfile_MenuModeOptions_Service3_Type.__name__ = "Integer32"
_TermSrvProfile_MenuModeOptions_Service3_Object = MibScalar
termSrvProfile_MenuModeOptions_Service3 = _TermSrvProfile_MenuModeOptions_Service3_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 133, 1, 1, 62),
    _TermSrvProfile_MenuModeOptions_Service3_Type()
)
termSrvProfile_MenuModeOptions_Service3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    termSrvProfile_MenuModeOptions_Service3.setStatus("mandatory")
_TermSrvProfile_MenuModeOptions_Port3_Type = Integer32
_TermSrvProfile_MenuModeOptions_Port3_Object = MibScalar
termSrvProfile_MenuModeOptions_Port3 = _TermSrvProfile_MenuModeOptions_Port3_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 133, 1, 1, 63),
    _TermSrvProfile_MenuModeOptions_Port3_Type()
)
termSrvProfile_MenuModeOptions_Port3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    termSrvProfile_MenuModeOptions_Port3.setStatus("mandatory")
_TermSrvProfile_MenuModeOptions_User3_Type = DisplayString
_TermSrvProfile_MenuModeOptions_User3_Object = MibScalar
termSrvProfile_MenuModeOptions_User3 = _TermSrvProfile_MenuModeOptions_User3_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 133, 1, 1, 64),
    _TermSrvProfile_MenuModeOptions_User3_Type()
)
termSrvProfile_MenuModeOptions_User3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    termSrvProfile_MenuModeOptions_User3.setStatus("mandatory")
_TermSrvProfile_MenuModeOptions_Text4_Type = DisplayString
_TermSrvProfile_MenuModeOptions_Text4_Object = MibScalar
termSrvProfile_MenuModeOptions_Text4 = _TermSrvProfile_MenuModeOptions_Text4_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 133, 1, 1, 65),
    _TermSrvProfile_MenuModeOptions_Text4_Type()
)
termSrvProfile_MenuModeOptions_Text4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    termSrvProfile_MenuModeOptions_Text4.setStatus("mandatory")
_TermSrvProfile_MenuModeOptions_Host4_Type = DisplayString
_TermSrvProfile_MenuModeOptions_Host4_Object = MibScalar
termSrvProfile_MenuModeOptions_Host4 = _TermSrvProfile_MenuModeOptions_Host4_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 133, 1, 1, 66),
    _TermSrvProfile_MenuModeOptions_Host4_Type()
)
termSrvProfile_MenuModeOptions_Host4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    termSrvProfile_MenuModeOptions_Host4.setStatus("mandatory")


class _TermSrvProfile_MenuModeOptions_Service4_Type(Integer32):
    """Custom type termSrvProfile_MenuModeOptions_Service4 based on Integer32"""
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
        *(("ppp", 3),
          ("rawtcp", 4),
          ("rlogin", 2),
          ("telnet", 1))
    )


_TermSrvProfile_MenuModeOptions_Service4_Type.__name__ = "Integer32"
_TermSrvProfile_MenuModeOptions_Service4_Object = MibScalar
termSrvProfile_MenuModeOptions_Service4 = _TermSrvProfile_MenuModeOptions_Service4_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 133, 1, 1, 67),
    _TermSrvProfile_MenuModeOptions_Service4_Type()
)
termSrvProfile_MenuModeOptions_Service4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    termSrvProfile_MenuModeOptions_Service4.setStatus("mandatory")
_TermSrvProfile_MenuModeOptions_Port4_Type = Integer32
_TermSrvProfile_MenuModeOptions_Port4_Object = MibScalar
termSrvProfile_MenuModeOptions_Port4 = _TermSrvProfile_MenuModeOptions_Port4_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 133, 1, 1, 68),
    _TermSrvProfile_MenuModeOptions_Port4_Type()
)
termSrvProfile_MenuModeOptions_Port4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    termSrvProfile_MenuModeOptions_Port4.setStatus("mandatory")
_TermSrvProfile_MenuModeOptions_User4_Type = DisplayString
_TermSrvProfile_MenuModeOptions_User4_Object = MibScalar
termSrvProfile_MenuModeOptions_User4 = _TermSrvProfile_MenuModeOptions_User4_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 133, 1, 1, 69),
    _TermSrvProfile_MenuModeOptions_User4_Type()
)
termSrvProfile_MenuModeOptions_User4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    termSrvProfile_MenuModeOptions_User4.setStatus("mandatory")
_TermSrvProfile_MenuModeOptions_MenuSelectionString_Type = DisplayString
_TermSrvProfile_MenuModeOptions_MenuSelectionString_Object = MibScalar
termSrvProfile_MenuModeOptions_MenuSelectionString = _TermSrvProfile_MenuModeOptions_MenuSelectionString_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 133, 1, 1, 70),
    _TermSrvProfile_MenuModeOptions_MenuSelectionString_Type()
)
termSrvProfile_MenuModeOptions_MenuSelectionString.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    termSrvProfile_MenuModeOptions_MenuSelectionString.setStatus("mandatory")


class _TermSrvProfile_PppModeConfiguration_Ppp_Type(Integer32):
    """Custom type termSrvProfile_PppModeConfiguration_Ppp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_TermSrvProfile_PppModeConfiguration_Ppp_Type.__name__ = "Integer32"
_TermSrvProfile_PppModeConfiguration_Ppp_Object = MibScalar
termSrvProfile_PppModeConfiguration_Ppp = _TermSrvProfile_PppModeConfiguration_Ppp_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 133, 1, 1, 71),
    _TermSrvProfile_PppModeConfiguration_Ppp_Type()
)
termSrvProfile_PppModeConfiguration_Ppp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    termSrvProfile_PppModeConfiguration_Ppp.setStatus("mandatory")
_TermSrvProfile_PppModeConfiguration_Delay_Type = Integer32
_TermSrvProfile_PppModeConfiguration_Delay_Object = MibScalar
termSrvProfile_PppModeConfiguration_Delay = _TermSrvProfile_PppModeConfiguration_Delay_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 133, 1, 1, 72),
    _TermSrvProfile_PppModeConfiguration_Delay_Type()
)
termSrvProfile_PppModeConfiguration_Delay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    termSrvProfile_PppModeConfiguration_Delay.setStatus("mandatory")


class _TermSrvProfile_PppModeConfiguration_Direct_Type(Integer32):
    """Custom type termSrvProfile_PppModeConfiguration_Direct based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_TermSrvProfile_PppModeConfiguration_Direct_Type.__name__ = "Integer32"
_TermSrvProfile_PppModeConfiguration_Direct_Object = MibScalar
termSrvProfile_PppModeConfiguration_Direct = _TermSrvProfile_PppModeConfiguration_Direct_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 133, 1, 1, 73),
    _TermSrvProfile_PppModeConfiguration_Direct_Type()
)
termSrvProfile_PppModeConfiguration_Direct.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    termSrvProfile_PppModeConfiguration_Direct.setStatus("mandatory")


class _TermSrvProfile_PppModeConfiguration_Info_Type(Integer32):
    """Custom type termSrvProfile_PppModeConfiguration_Info based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("modePpp", 2),
          ("none", 1),
          ("sessionPpp", 3))
    )


_TermSrvProfile_PppModeConfiguration_Info_Type.__name__ = "Integer32"
_TermSrvProfile_PppModeConfiguration_Info_Object = MibScalar
termSrvProfile_PppModeConfiguration_Info = _TermSrvProfile_PppModeConfiguration_Info_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 133, 1, 1, 74),
    _TermSrvProfile_PppModeConfiguration_Info_Type()
)
termSrvProfile_PppModeConfiguration_Info.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    termSrvProfile_PppModeConfiguration_Info.setStatus("mandatory")


class _TermSrvProfile_SlipModeConfiguration_Slip_Type(Integer32):
    """Custom type termSrvProfile_SlipModeConfiguration_Slip based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_TermSrvProfile_SlipModeConfiguration_Slip_Type.__name__ = "Integer32"
_TermSrvProfile_SlipModeConfiguration_Slip_Object = MibScalar
termSrvProfile_SlipModeConfiguration_Slip = _TermSrvProfile_SlipModeConfiguration_Slip_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 133, 1, 1, 75),
    _TermSrvProfile_SlipModeConfiguration_Slip_Type()
)
termSrvProfile_SlipModeConfiguration_Slip.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    termSrvProfile_SlipModeConfiguration_Slip.setStatus("mandatory")


class _TermSrvProfile_SlipModeConfiguration_SlipBootp_Type(Integer32):
    """Custom type termSrvProfile_SlipModeConfiguration_SlipBootp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_TermSrvProfile_SlipModeConfiguration_SlipBootp_Type.__name__ = "Integer32"
_TermSrvProfile_SlipModeConfiguration_SlipBootp_Object = MibScalar
termSrvProfile_SlipModeConfiguration_SlipBootp = _TermSrvProfile_SlipModeConfiguration_SlipBootp_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 133, 1, 1, 76),
    _TermSrvProfile_SlipModeConfiguration_SlipBootp_Type()
)
termSrvProfile_SlipModeConfiguration_SlipBootp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    termSrvProfile_SlipModeConfiguration_SlipBootp.setStatus("mandatory")


class _TermSrvProfile_SlipModeConfiguration_Info_Type(Integer32):
    """Custom type termSrvProfile_SlipModeConfiguration_Info based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("advancedSlip", 2),
          ("basicSlip", 1))
    )


_TermSrvProfile_SlipModeConfiguration_Info_Type.__name__ = "Integer32"
_TermSrvProfile_SlipModeConfiguration_Info_Object = MibScalar
termSrvProfile_SlipModeConfiguration_Info = _TermSrvProfile_SlipModeConfiguration_Info_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 133, 1, 1, 77),
    _TermSrvProfile_SlipModeConfiguration_Info_Type()
)
termSrvProfile_SlipModeConfiguration_Info.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    termSrvProfile_SlipModeConfiguration_Info.setStatus("mandatory")


class _TermSrvProfile_SlipModeConfiguration_CslipAutoDetect_Type(Integer32):
    """Custom type termSrvProfile_SlipModeConfiguration_CslipAutoDetect based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_TermSrvProfile_SlipModeConfiguration_CslipAutoDetect_Type.__name__ = "Integer32"
_TermSrvProfile_SlipModeConfiguration_CslipAutoDetect_Object = MibScalar
termSrvProfile_SlipModeConfiguration_CslipAutoDetect = _TermSrvProfile_SlipModeConfiguration_CslipAutoDetect_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 133, 1, 1, 78),
    _TermSrvProfile_SlipModeConfiguration_CslipAutoDetect_Type()
)
termSrvProfile_SlipModeConfiguration_CslipAutoDetect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    termSrvProfile_SlipModeConfiguration_CslipAutoDetect.setStatus("mandatory")


class _TermSrvProfile_DialoutConfiguration_Enabled_Type(Integer32):
    """Custom type termSrvProfile_DialoutConfiguration_Enabled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_TermSrvProfile_DialoutConfiguration_Enabled_Type.__name__ = "Integer32"
_TermSrvProfile_DialoutConfiguration_Enabled_Object = MibScalar
termSrvProfile_DialoutConfiguration_Enabled = _TermSrvProfile_DialoutConfiguration_Enabled_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 133, 1, 1, 79),
    _TermSrvProfile_DialoutConfiguration_Enabled_Type()
)
termSrvProfile_DialoutConfiguration_Enabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    termSrvProfile_DialoutConfiguration_Enabled.setStatus("mandatory")


class _TermSrvProfile_DialoutConfiguration_DirectAccess_Type(Integer32):
    """Custom type termSrvProfile_DialoutConfiguration_DirectAccess based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_TermSrvProfile_DialoutConfiguration_DirectAccess_Type.__name__ = "Integer32"
_TermSrvProfile_DialoutConfiguration_DirectAccess_Object = MibScalar
termSrvProfile_DialoutConfiguration_DirectAccess = _TermSrvProfile_DialoutConfiguration_DirectAccess_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 133, 1, 1, 80),
    _TermSrvProfile_DialoutConfiguration_DirectAccess_Type()
)
termSrvProfile_DialoutConfiguration_DirectAccess.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    termSrvProfile_DialoutConfiguration_DirectAccess.setStatus("mandatory")
_TermSrvProfile_DialoutConfiguration_PortForDirectAccess_Type = Integer32
_TermSrvProfile_DialoutConfiguration_PortForDirectAccess_Object = MibScalar
termSrvProfile_DialoutConfiguration_PortForDirectAccess = _TermSrvProfile_DialoutConfiguration_PortForDirectAccess_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 133, 1, 1, 81),
    _TermSrvProfile_DialoutConfiguration_PortForDirectAccess_Type()
)
termSrvProfile_DialoutConfiguration_PortForDirectAccess.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    termSrvProfile_DialoutConfiguration_PortForDirectAccess.setStatus("mandatory")
_TermSrvProfile_DialoutConfiguration_PasswordForDirectAccess_Type = DisplayString
_TermSrvProfile_DialoutConfiguration_PasswordForDirectAccess_Object = MibScalar
termSrvProfile_DialoutConfiguration_PasswordForDirectAccess = _TermSrvProfile_DialoutConfiguration_PasswordForDirectAccess_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 133, 1, 1, 82),
    _TermSrvProfile_DialoutConfiguration_PasswordForDirectAccess_Type()
)
termSrvProfile_DialoutConfiguration_PasswordForDirectAccess.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    termSrvProfile_DialoutConfiguration_PasswordForDirectAccess.setStatus("mandatory")


class _TermSrvProfile_DialoutConfiguration_SecurityForDirectAccess_Type(Integer32):
    """Custom type termSrvProfile_DialoutConfiguration_SecurityForDirectAccess based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("global", 2),
          ("none", 1),
          ("user", 3))
    )


_TermSrvProfile_DialoutConfiguration_SecurityForDirectAccess_Type.__name__ = "Integer32"
_TermSrvProfile_DialoutConfiguration_SecurityForDirectAccess_Object = MibScalar
termSrvProfile_DialoutConfiguration_SecurityForDirectAccess = _TermSrvProfile_DialoutConfiguration_SecurityForDirectAccess_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 133, 1, 1, 83),
    _TermSrvProfile_DialoutConfiguration_SecurityForDirectAccess_Type()
)
termSrvProfile_DialoutConfiguration_SecurityForDirectAccess.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    termSrvProfile_DialoutConfiguration_SecurityForDirectAccess.setStatus("mandatory")


class _TermSrvProfile_Action_o_Type(Integer32):
    """Custom type termSrvProfile_Action_o based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("createProfile", 2),
          ("deleteProfile", 3),
          ("noAction", 1))
    )


_TermSrvProfile_Action_o_Type.__name__ = "Integer32"
_TermSrvProfile_Action_o_Object = MibScalar
termSrvProfile_Action_o = _TermSrvProfile_Action_o_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 133, 1, 1, 84),
    _TermSrvProfile_Action_o_Type()
)
termSrvProfile_Action_o.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    termSrvProfile_Action_o.setStatus("mandatory")


class _TermSrvProfile_ModemConfiguration_ModemOnHoldTimeout_Type(Integer32):
    """Custom type termSrvProfile_ModemConfiguration_ModemOnHoldTimeout based on Integer32"""
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
              15)
        )
    )
    namedValues = NamedValues(
        *(("connProfileUseGlobal", 15),
          ("mohDisabled", 1),
          ("n-10SecMohTimeout", 2),
          ("n-12MinMohTimeout", 12),
          ("n-16MinMohTimeout", 13),
          ("n-1MinMohTimeout", 6),
          ("n-20SecMohTimeout", 3),
          ("n-2MinMohTimeout", 7),
          ("n-30SecMohTimeout", 4),
          ("n-3MinMohTimeout", 8),
          ("n-40SecMohTimeout", 5),
          ("n-4MinMohTimeout", 9),
          ("n-6MinMohTimeout", 10),
          ("n-8MinMohTimeout", 11),
          ("noLimitMohTimeout", 14))
    )


_TermSrvProfile_ModemConfiguration_ModemOnHoldTimeout_Type.__name__ = "Integer32"
_TermSrvProfile_ModemConfiguration_ModemOnHoldTimeout_Object = MibScalar
termSrvProfile_ModemConfiguration_ModemOnHoldTimeout = _TermSrvProfile_ModemConfiguration_ModemOnHoldTimeout_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 133, 1, 1, 85),
    _TermSrvProfile_ModemConfiguration_ModemOnHoldTimeout_Type()
)
termSrvProfile_ModemConfiguration_ModemOnHoldTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    termSrvProfile_ModemConfiguration_ModemOnHoldTimeout.setStatus("mandatory")


class _TermSrvProfile_ModemConfiguration_QuickConnectEnabled_Type(Integer32):
    """Custom type termSrvProfile_ModemConfiguration_QuickConnectEnabled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_TermSrvProfile_ModemConfiguration_QuickConnectEnabled_Type.__name__ = "Integer32"
_TermSrvProfile_ModemConfiguration_QuickConnectEnabled_Object = MibScalar
termSrvProfile_ModemConfiguration_QuickConnectEnabled = _TermSrvProfile_ModemConfiguration_QuickConnectEnabled_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 133, 1, 1, 86),
    _TermSrvProfile_ModemConfiguration_QuickConnectEnabled_Type()
)
termSrvProfile_ModemConfiguration_QuickConnectEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    termSrvProfile_ModemConfiguration_QuickConnectEnabled.setStatus("mandatory")


class _TermSrvProfile_ModemConfiguration_MaxV92ReceiveBaudRate_Type(Integer32):
    """Custom type termSrvProfile_ModemConfiguration_MaxV92ReceiveBaudRate based on Integer32"""
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
              19)
        )
    )
    namedValues = NamedValues(
        *(("n-24000MaxV92Baud", 19),
          ("n-25333MaxV92Baud", 18),
          ("n-26667MaxV92Baud", 17),
          ("n-28000MaxV92Baud", 16),
          ("n-29333MaxV92Baud", 15),
          ("n-30667MaxV92Baud", 14),
          ("n-32000MaxV92Baud", 13),
          ("n-33333MaxV92Baud", 12),
          ("n-34667MaxV92Baud", 11),
          ("n-36000MaxV92Baud", 10),
          ("n-37333MaxV92Baud", 9),
          ("n-38667MaxV92Baud", 8),
          ("n-40000MaxV92Baud", 7),
          ("n-41333MaxV92Baud", 6),
          ("n-42667MaxV92Baud", 5),
          ("n-44000MaxV92Baud", 4),
          ("n-45333MaxV92Baud", 3),
          ("n-46667MaxV92Baud", 2),
          ("n-48000MaxV92Baud", 1))
    )


_TermSrvProfile_ModemConfiguration_MaxV92ReceiveBaudRate_Type.__name__ = "Integer32"
_TermSrvProfile_ModemConfiguration_MaxV92ReceiveBaudRate_Object = MibScalar
termSrvProfile_ModemConfiguration_MaxV92ReceiveBaudRate = _TermSrvProfile_ModemConfiguration_MaxV92ReceiveBaudRate_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 133, 1, 1, 87),
    _TermSrvProfile_ModemConfiguration_MaxV92ReceiveBaudRate_Type()
)
termSrvProfile_ModemConfiguration_MaxV92ReceiveBaudRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    termSrvProfile_ModemConfiguration_MaxV92ReceiveBaudRate.setStatus("mandatory")


class _TermSrvProfile_ModemConfiguration_V44Enabled_Type(Integer32):
    """Custom type termSrvProfile_ModemConfiguration_V44Enabled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_TermSrvProfile_ModemConfiguration_V44Enabled_Type.__name__ = "Integer32"
_TermSrvProfile_ModemConfiguration_V44Enabled_Object = MibScalar
termSrvProfile_ModemConfiguration_V44Enabled = _TermSrvProfile_ModemConfiguration_V44Enabled_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 133, 1, 1, 88),
    _TermSrvProfile_ModemConfiguration_V44Enabled_Type()
)
termSrvProfile_ModemConfiguration_V44Enabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    termSrvProfile_ModemConfiguration_V44Enabled.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ASCEND-MIBTS-MIB",
    **{"DisplayString": DisplayString,
       "mibtermSrvProfile": mibtermSrvProfile,
       "mibtermSrvProfileTable": mibtermSrvProfileTable,
       "mibtermSrvProfileEntry": mibtermSrvProfileEntry,
       "termSrvProfile-Index-o": termSrvProfile_Index_o,
       "termSrvProfile-Enabled": termSrvProfile_Enabled,
       "termSrvProfile-SecurityMode": termSrvProfile_SecurityMode,
       "termSrvProfile-ModemConfiguration-V42-mnp": termSrvProfile_ModemConfiguration_V42_mnp,
       "termSrvProfile-ModemConfiguration-MaxBaudRate": termSrvProfile_ModemConfiguration_MaxBaudRate,
       "termSrvProfile-ModemConfiguration-ModemTransmitLevel": termSrvProfile_ModemConfiguration_ModemTransmitLevel,
       "termSrvProfile-ModemConfiguration-CellModeFirst": termSrvProfile_ModemConfiguration_CellModeFirst,
       "termSrvProfile-ModemConfiguration-CellLevel": termSrvProfile_ModemConfiguration_CellLevel,
       "termSrvProfile-ModemConfiguration-o7Even": termSrvProfile_ModemConfiguration_o7Even,
       "termSrvProfile-ModemConfiguration-ModemMod": termSrvProfile_ModemConfiguration_ModemMod,
       "termSrvProfile-ModemConfiguration-oATAnswerString": termSrvProfile_ModemConfiguration_oATAnswerString,
       "termSrvProfile-TerminalModeConfiguration-SilentMode": termSrvProfile_TerminalModeConfiguration_SilentMode,
       "termSrvProfile-TerminalModeConfiguration-ClearScreen": termSrvProfile_TerminalModeConfiguration_ClearScreen,
       "termSrvProfile-TerminalModeConfiguration-SystemPassword": termSrvProfile_TerminalModeConfiguration_SystemPassword,
       "termSrvProfile-TerminalModeConfiguration-Banner": termSrvProfile_TerminalModeConfiguration_Banner,
       "termSrvProfile-TerminalModeConfiguration-LoginPrompt": termSrvProfile_TerminalModeConfiguration_LoginPrompt,
       "termSrvProfile-TerminalModeConfiguration-PasswordPrompt": termSrvProfile_TerminalModeConfiguration_PasswordPrompt,
       "termSrvProfile-TerminalModeConfiguration-ThirdLoginPrompt": termSrvProfile_TerminalModeConfiguration_ThirdLoginPrompt,
       "termSrvProfile-TerminalModeConfiguration-ThirdPromptSequence": termSrvProfile_TerminalModeConfiguration_ThirdPromptSequence,
       "termSrvProfile-TerminalModeConfiguration-Prompt": termSrvProfile_TerminalModeConfiguration_Prompt,
       "termSrvProfile-TerminalModeConfiguration-TerminalType": termSrvProfile_TerminalModeConfiguration_TerminalType,
       "termSrvProfile-TerminalModeConfiguration-ClearCall": termSrvProfile_TerminalModeConfiguration_ClearCall,
       "termSrvProfile-TerminalModeConfiguration-BufferChars": termSrvProfile_TerminalModeConfiguration_BufferChars,
       "termSrvProfile-TerminalModeConfiguration-Ping": termSrvProfile_TerminalModeConfiguration_Ping,
       "termSrvProfile-TerminalModeConfiguration-Traceroute": termSrvProfile_TerminalModeConfiguration_Traceroute,
       "termSrvProfile-TerminalModeConfiguration-Tcp": termSrvProfile_TerminalModeConfiguration_Tcp,
       "termSrvProfile-TerminalModeConfiguration-TsAraEnabled": termSrvProfile_TerminalModeConfiguration_TsAraEnabled,
       "termSrvProfile-TerminalModeConfiguration-RloginOptions-Rlogin": termSrvProfile_TerminalModeConfiguration_RloginOptions_Rlogin,
       "termSrvProfile-TerminalModeConfiguration-RloginOptions-MaxSourcePort": termSrvProfile_TerminalModeConfiguration_RloginOptions_MaxSourcePort,
       "termSrvProfile-TerminalModeConfiguration-RloginOptions-MinSourcePort": termSrvProfile_TerminalModeConfiguration_RloginOptions_MinSourcePort,
       "termSrvProfile-TerminalModeConfiguration-TelnetOptions-Telnet": termSrvProfile_TerminalModeConfiguration_TelnetOptions_Telnet,
       "termSrvProfile-TerminalModeConfiguration-TelnetOptions-TelnetMode": termSrvProfile_TerminalModeConfiguration_TelnetOptions_TelnetMode,
       "termSrvProfile-TerminalModeConfiguration-TelnetOptions-AutoTelnet": termSrvProfile_TerminalModeConfiguration_TelnetOptions_AutoTelnet,
       "termSrvProfile-TerminalModeConfiguration-TelnetOptions-LocalEcho": termSrvProfile_TerminalModeConfiguration_TelnetOptions_LocalEcho,
       "termSrvProfile-TerminalModeConfiguration-TelnetOptions-Security": termSrvProfile_TerminalModeConfiguration_TelnetOptions_Security,
       "termSrvProfile-TerminalModeConfiguration-IpAddMsg": termSrvProfile_TerminalModeConfiguration_IpAddMsg,
       "termSrvProfile-TerminalModeConfiguration-PromptFormat": termSrvProfile_TerminalModeConfiguration_PromptFormat,
       "termSrvProfile-TerminalModeConfiguration-IpNetmaskMsg": termSrvProfile_TerminalModeConfiguration_IpNetmaskMsg,
       "termSrvProfile-TerminalModeConfiguration-IpGwAddMsg": termSrvProfile_TerminalModeConfiguration_IpGwAddMsg,
       "termSrvProfile-TerminalModeConfiguration-LoginTimeout": termSrvProfile_TerminalModeConfiguration_LoginTimeout,
       "termSrvProfile-TerminalModeConfiguration-PacketizeWaitTime": termSrvProfile_TerminalModeConfiguration_PacketizeWaitTime,
       "termSrvProfile-TerminalModeConfiguration-PacketizeChars": termSrvProfile_TerminalModeConfiguration_PacketizeChars,
       "termSrvProfile-ImmediateModeOptions-Service": termSrvProfile_ImmediateModeOptions_Service,
       "termSrvProfile-ImmediateModeOptions-TelnetHostAuth": termSrvProfile_ImmediateModeOptions_TelnetHostAuth,
       "termSrvProfile-ImmediateModeOptions-Host": termSrvProfile_ImmediateModeOptions_Host,
       "termSrvProfile-ImmediateModeOptions-Port": termSrvProfile_ImmediateModeOptions_Port,
       "termSrvProfile-MenuModeOptions-StartWithMenus": termSrvProfile_MenuModeOptions_StartWithMenus,
       "termSrvProfile-MenuModeOptions-ToggleScreen": termSrvProfile_MenuModeOptions_ToggleScreen,
       "termSrvProfile-MenuModeOptions-RemoteConfiguration": termSrvProfile_MenuModeOptions_RemoteConfiguration,
       "termSrvProfile-MenuModeOptions-Text1": termSrvProfile_MenuModeOptions_Text1,
       "termSrvProfile-MenuModeOptions-Host1": termSrvProfile_MenuModeOptions_Host1,
       "termSrvProfile-MenuModeOptions-Service1": termSrvProfile_MenuModeOptions_Service1,
       "termSrvProfile-MenuModeOptions-Port1": termSrvProfile_MenuModeOptions_Port1,
       "termSrvProfile-MenuModeOptions-User1": termSrvProfile_MenuModeOptions_User1,
       "termSrvProfile-MenuModeOptions-Text2": termSrvProfile_MenuModeOptions_Text2,
       "termSrvProfile-MenuModeOptions-Host2": termSrvProfile_MenuModeOptions_Host2,
       "termSrvProfile-MenuModeOptions-Service2": termSrvProfile_MenuModeOptions_Service2,
       "termSrvProfile-MenuModeOptions-Port2": termSrvProfile_MenuModeOptions_Port2,
       "termSrvProfile-MenuModeOptions-User2": termSrvProfile_MenuModeOptions_User2,
       "termSrvProfile-MenuModeOptions-Text3": termSrvProfile_MenuModeOptions_Text3,
       "termSrvProfile-MenuModeOptions-Host3": termSrvProfile_MenuModeOptions_Host3,
       "termSrvProfile-MenuModeOptions-Service3": termSrvProfile_MenuModeOptions_Service3,
       "termSrvProfile-MenuModeOptions-Port3": termSrvProfile_MenuModeOptions_Port3,
       "termSrvProfile-MenuModeOptions-User3": termSrvProfile_MenuModeOptions_User3,
       "termSrvProfile-MenuModeOptions-Text4": termSrvProfile_MenuModeOptions_Text4,
       "termSrvProfile-MenuModeOptions-Host4": termSrvProfile_MenuModeOptions_Host4,
       "termSrvProfile-MenuModeOptions-Service4": termSrvProfile_MenuModeOptions_Service4,
       "termSrvProfile-MenuModeOptions-Port4": termSrvProfile_MenuModeOptions_Port4,
       "termSrvProfile-MenuModeOptions-User4": termSrvProfile_MenuModeOptions_User4,
       "termSrvProfile-MenuModeOptions-MenuSelectionString": termSrvProfile_MenuModeOptions_MenuSelectionString,
       "termSrvProfile-PppModeConfiguration-Ppp": termSrvProfile_PppModeConfiguration_Ppp,
       "termSrvProfile-PppModeConfiguration-Delay": termSrvProfile_PppModeConfiguration_Delay,
       "termSrvProfile-PppModeConfiguration-Direct": termSrvProfile_PppModeConfiguration_Direct,
       "termSrvProfile-PppModeConfiguration-Info": termSrvProfile_PppModeConfiguration_Info,
       "termSrvProfile-SlipModeConfiguration-Slip": termSrvProfile_SlipModeConfiguration_Slip,
       "termSrvProfile-SlipModeConfiguration-SlipBootp": termSrvProfile_SlipModeConfiguration_SlipBootp,
       "termSrvProfile-SlipModeConfiguration-Info": termSrvProfile_SlipModeConfiguration_Info,
       "termSrvProfile-SlipModeConfiguration-CslipAutoDetect": termSrvProfile_SlipModeConfiguration_CslipAutoDetect,
       "termSrvProfile-DialoutConfiguration-Enabled": termSrvProfile_DialoutConfiguration_Enabled,
       "termSrvProfile-DialoutConfiguration-DirectAccess": termSrvProfile_DialoutConfiguration_DirectAccess,
       "termSrvProfile-DialoutConfiguration-PortForDirectAccess": termSrvProfile_DialoutConfiguration_PortForDirectAccess,
       "termSrvProfile-DialoutConfiguration-PasswordForDirectAccess": termSrvProfile_DialoutConfiguration_PasswordForDirectAccess,
       "termSrvProfile-DialoutConfiguration-SecurityForDirectAccess": termSrvProfile_DialoutConfiguration_SecurityForDirectAccess,
       "termSrvProfile-Action-o": termSrvProfile_Action_o,
       "termSrvProfile-ModemConfiguration-ModemOnHoldTimeout": termSrvProfile_ModemConfiguration_ModemOnHoldTimeout,
       "termSrvProfile-ModemConfiguration-QuickConnectEnabled": termSrvProfile_ModemConfiguration_QuickConnectEnabled,
       "termSrvProfile-ModemConfiguration-MaxV92ReceiveBaudRate": termSrvProfile_ModemConfiguration_MaxV92ReceiveBaudRate,
       "termSrvProfile-ModemConfiguration-V44Enabled": termSrvProfile_ModemConfiguration_V44Enabled}
)
