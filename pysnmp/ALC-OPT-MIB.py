# SNMP MIB module (ALC-OPT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ALC-OPT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:35:32 2024
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

_Codex_ObjectIdentity = ObjectIdentity
codex = _Codex_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 449)
)
_CdxProductSpecific_ObjectIdentity = ObjectIdentity
cdxProductSpecific = _CdxProductSpecific_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 449, 2)
)
_Cdx6500_ObjectIdentity = ObjectIdentity
cdx6500 = _Cdx6500_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 449, 2, 1)
)
_Cdx6500Configuration_ObjectIdentity = ObjectIdentity
cdx6500Configuration = _Cdx6500Configuration_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2)
)
_Cdx6500CfgProtocolGroup_ObjectIdentity = ObjectIdentity
cdx6500CfgProtocolGroup = _Cdx6500CfgProtocolGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1)
)
_Cdx6500PCTPortProtocolGroup_ObjectIdentity = ObjectIdentity
cdx6500PCTPortProtocolGroup = _Cdx6500PCTPortProtocolGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1)
)
_Cdx6500PPCTALCCfgTable_ObjectIdentity = ObjectIdentity
cdx6500PPCTALCCfgTable = _Cdx6500PPCTALCCfgTable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 27)
)
_Cdx6500PPCTALCPortTable_Object = MibTable
cdx6500PPCTALCPortTable = _Cdx6500PPCTALCPortTable_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 27, 1)
)
if mibBuilder.loadTexts:
    cdx6500PPCTALCPortTable.setStatus("mandatory")
_Cdx6500PPCTALCPortEntry_Object = MibTableRow
cdx6500PPCTALCPortEntry = _Cdx6500PPCTALCPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 27, 1, 1)
)
cdx6500PPCTALCPortEntry.setIndexNames(
    (0, "ALC-OPT-MIB", "alcPCfgPortNumber"),
)
if mibBuilder.loadTexts:
    cdx6500PPCTALCPortEntry.setStatus("mandatory")


class _AlcPCfgPortNumber_Type(Integer32):
    """Custom type alcPCfgPortNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 54),
    )


_AlcPCfgPortNumber_Type.__name__ = "Integer32"
_AlcPCfgPortNumber_Object = MibTableColumn
alcPCfgPortNumber = _AlcPCfgPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 27, 1, 1, 1),
    _AlcPCfgPortNumber_Type()
)
alcPCfgPortNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alcPCfgPortNumber.setStatus("mandatory")


class _AlcPCfgPortType_Type(Integer32):
    """Custom type alcPCfgPortType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            31
        )
    )
    namedValues = NamedValues(
        ("alc", 31)
    )


_AlcPCfgPortType_Type.__name__ = "Integer32"
_AlcPCfgPortType_Object = MibTableColumn
alcPCfgPortType = _AlcPCfgPortType_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 27, 1, 1, 2),
    _AlcPCfgPortType_Type()
)
alcPCfgPortType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alcPCfgPortType.setStatus("mandatory")


class _AlcPCfgSubtype_Type(Integer32):
    """Custom type alcPCfgSubtype based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("alcHpad", 1),
          ("alcTpad", 2))
    )


_AlcPCfgSubtype_Type.__name__ = "Integer32"
_AlcPCfgSubtype_Object = MibTableColumn
alcPCfgSubtype = _AlcPCfgSubtype_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 27, 1, 1, 3),
    _AlcPCfgSubtype_Type()
)
alcPCfgSubtype.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alcPCfgSubtype.setStatus("mandatory")


class _AlcPCfgPortControl_Type(Integer32):
    """Custom type alcPCfgPortControl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              4,
              5,
              13,
              15)
        )
    )
    namedValues = NamedValues(
        *(("alcDte", 15),
          ("dtr", 13),
          ("emdc", 5),
          ("emri", 4),
          ("simp", 1))
    )


_AlcPCfgPortControl_Type.__name__ = "Integer32"
_AlcPCfgPortControl_Object = MibTableColumn
alcPCfgPortControl = _AlcPCfgPortControl_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 27, 1, 1, 4),
    _AlcPCfgPortControl_Type()
)
alcPCfgPortControl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alcPCfgPortControl.setStatus("mandatory")


class _AlcPCfgClockSource_Type(Integer32):
    """Custom type alcPCfgClockSource based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ext", 2),
          ("int", 1))
    )


_AlcPCfgClockSource_Type.__name__ = "Integer32"
_AlcPCfgClockSource_Object = MibTableColumn
alcPCfgClockSource = _AlcPCfgClockSource_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 27, 1, 1, 5),
    _AlcPCfgClockSource_Type()
)
alcPCfgClockSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alcPCfgClockSource.setStatus("mandatory")


class _AlcPCfgClockSpeed_Type(Integer32):
    """Custom type alcPCfgClockSpeed based on Integer32"""
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
        *(("clkspd1200", 1),
          ("clkspd19200", 5),
          ("clkspd2400", 2),
          ("clkspd38400", 6),
          ("clkspd4800", 3),
          ("clkspd9600", 4))
    )


_AlcPCfgClockSpeed_Type.__name__ = "Integer32"
_AlcPCfgClockSpeed_Object = MibTableColumn
alcPCfgClockSpeed = _AlcPCfgClockSpeed_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 27, 1, 1, 6),
    _AlcPCfgClockSpeed_Type()
)
alcPCfgClockSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alcPCfgClockSpeed.setStatus("mandatory")


class _AlcPCfgPollDelayTimer_Type(Integer32):
    """Custom type alcPCfgPollDelayTimer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(50, 100000),
    )


_AlcPCfgPollDelayTimer_Type.__name__ = "Integer32"
_AlcPCfgPollDelayTimer_Object = MibTableColumn
alcPCfgPollDelayTimer = _AlcPCfgPollDelayTimer_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 27, 1, 1, 7),
    _AlcPCfgPollDelayTimer_Type()
)
alcPCfgPollDelayTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alcPCfgPollDelayTimer.setStatus("mandatory")


class _AlcPCfgHostTimeout_Type(Integer32):
    """Custom type alcPCfgHostTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(50, 10000),
    )


_AlcPCfgHostTimeout_Type.__name__ = "Integer32"
_AlcPCfgHostTimeout_Object = MibTableColumn
alcPCfgHostTimeout = _AlcPCfgHostTimeout_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 27, 1, 1, 8),
    _AlcPCfgHostTimeout_Type()
)
alcPCfgHostTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alcPCfgHostTimeout.setStatus("mandatory")


class _AlcPCfgMaxMesgSize_Type(Integer32):
    """Custom type alcPCfgMaxMesgSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 10000),
    )


_AlcPCfgMaxMesgSize_Type.__name__ = "Integer32"
_AlcPCfgMaxMesgSize_Object = MibTableColumn
alcPCfgMaxMesgSize = _AlcPCfgMaxMesgSize_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 27, 1, 1, 9),
    _AlcPCfgMaxMesgSize_Type()
)
alcPCfgMaxMesgSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alcPCfgMaxMesgSize.setStatus("mandatory")


class _AlcPCfgMinIntrvlBetweenPolls_Type(Integer32):
    """Custom type alcPCfgMinIntrvlBetweenPolls based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100000),
    )


_AlcPCfgMinIntrvlBetweenPolls_Type.__name__ = "Integer32"
_AlcPCfgMinIntrvlBetweenPolls_Object = MibTableColumn
alcPCfgMinIntrvlBetweenPolls = _AlcPCfgMinIntrvlBetweenPolls_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 27, 1, 1, 10),
    _AlcPCfgMinIntrvlBetweenPolls_Type()
)
alcPCfgMinIntrvlBetweenPolls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alcPCfgMinIntrvlBetweenPolls.setStatus("mandatory")


class _AlcPCfgRtsCtsTimeout_Type(Integer32):
    """Custom type alcPCfgRtsCtsTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(50, 10000),
    )


_AlcPCfgRtsCtsTimeout_Type.__name__ = "Integer32"
_AlcPCfgRtsCtsTimeout_Object = MibTableColumn
alcPCfgRtsCtsTimeout = _AlcPCfgRtsCtsTimeout_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 27, 1, 1, 11),
    _AlcPCfgRtsCtsTimeout_Type()
)
alcPCfgRtsCtsTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alcPCfgRtsCtsTimeout.setStatus("mandatory")
_AlcPCfgLeadPadChar_Type = OctetString
_AlcPCfgLeadPadChar_Object = MibTableColumn
alcPCfgLeadPadChar = _AlcPCfgLeadPadChar_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 27, 1, 1, 12),
    _AlcPCfgLeadPadChar_Type()
)
alcPCfgLeadPadChar.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alcPCfgLeadPadChar.setStatus("mandatory")


class _AlcPCfgNumLeadPadChars_Type(Integer32):
    """Custom type alcPCfgNumLeadPadChars based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_AlcPCfgNumLeadPadChars_Type.__name__ = "Integer32"
_AlcPCfgNumLeadPadChars_Object = MibTableColumn
alcPCfgNumLeadPadChars = _AlcPCfgNumLeadPadChars_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 27, 1, 1, 13),
    _AlcPCfgNumLeadPadChars_Type()
)
alcPCfgNumLeadPadChars.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alcPCfgNumLeadPadChars.setStatus("mandatory")
_AlcPCfgTrailPadChar_Type = OctetString
_AlcPCfgTrailPadChar_Object = MibTableColumn
alcPCfgTrailPadChar = _AlcPCfgTrailPadChar_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 27, 1, 1, 14),
    _AlcPCfgTrailPadChar_Type()
)
alcPCfgTrailPadChar.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alcPCfgTrailPadChar.setStatus("mandatory")


class _AlcPCfgNumTrailPadChars_Type(Integer32):
    """Custom type alcPCfgNumTrailPadChars based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_AlcPCfgNumTrailPadChars_Type.__name__ = "Integer32"
_AlcPCfgNumTrailPadChars_Object = MibTableColumn
alcPCfgNumTrailPadChars = _AlcPCfgNumTrailPadChars_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 27, 1, 1, 15),
    _AlcPCfgNumTrailPadChars_Type()
)
alcPCfgNumTrailPadChars.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alcPCfgNumTrailPadChars.setStatus("mandatory")


class _AlcPCfgALCLineOptions_Type(DisplayString):
    """Custom type alcPCfgALCLineOptions based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 71),
    )


_AlcPCfgALCLineOptions_Type.__name__ = "DisplayString"
_AlcPCfgALCLineOptions_Object = MibTableColumn
alcPCfgALCLineOptions = _AlcPCfgALCLineOptions_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 27, 1, 1, 16),
    _AlcPCfgALCLineOptions_Type()
)
alcPCfgALCLineOptions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alcPCfgALCLineOptions.setStatus("mandatory")


class _AlcPCfgConnType_Type(Integer32):
    """Custom type alcPCfgConnType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              100)
        )
    )
    namedValues = NamedValues(
        *(("nc", 100),
          ("none", 1),
          ("x25", 2))
    )


_AlcPCfgConnType_Type.__name__ = "Integer32"
_AlcPCfgConnType_Object = MibTableColumn
alcPCfgConnType = _AlcPCfgConnType_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 27, 1, 1, 17),
    _AlcPCfgConnType_Type()
)
alcPCfgConnType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alcPCfgConnType.setStatus("mandatory")


class _AlcPCfgAcallMnemonic_Type(DisplayString):
    """Custom type alcPCfgAcallMnemonic based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_AlcPCfgAcallMnemonic_Type.__name__ = "DisplayString"
_AlcPCfgAcallMnemonic_Object = MibTableColumn
alcPCfgAcallMnemonic = _AlcPCfgAcallMnemonic_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 27, 1, 1, 18),
    _AlcPCfgAcallMnemonic_Type()
)
alcPCfgAcallMnemonic.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alcPCfgAcallMnemonic.setStatus("mandatory")


class _AlcPCfgCallingAddress_Type(DisplayString):
    """Custom type alcPCfgCallingAddress based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_AlcPCfgCallingAddress_Type.__name__ = "DisplayString"
_AlcPCfgCallingAddress_Object = MibTableColumn
alcPCfgCallingAddress = _AlcPCfgCallingAddress_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 27, 1, 1, 19),
    _AlcPCfgCallingAddress_Type()
)
alcPCfgCallingAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alcPCfgCallingAddress.setStatus("mandatory")


class _AlcPCfgCUD_Type(DisplayString):
    """Custom type alcPCfgCUD based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 47),
    )


_AlcPCfgCUD_Type.__name__ = "DisplayString"
_AlcPCfgCUD_Object = MibTableColumn
alcPCfgCUD = _AlcPCfgCUD_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 27, 1, 1, 20),
    _AlcPCfgCUD_Type()
)
alcPCfgCUD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alcPCfgCUD.setStatus("mandatory")


class _AlcPCfgNumOfBuffers_Type(Integer32):
    """Custom type alcPCfgNumOfBuffers based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1000),
    )


_AlcPCfgNumOfBuffers_Type.__name__ = "Integer32"
_AlcPCfgNumOfBuffers_Object = MibTableColumn
alcPCfgNumOfBuffers = _AlcPCfgNumOfBuffers_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 27, 1, 1, 21),
    _AlcPCfgNumOfBuffers_Type()
)
alcPCfgNumOfBuffers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alcPCfgNumOfBuffers.setStatus("mandatory")


class _AlcPCfgInHeader_Type(DisplayString):
    """Custom type alcPCfgInHeader based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 53),
    )


_AlcPCfgInHeader_Type.__name__ = "DisplayString"
_AlcPCfgInHeader_Object = MibTableColumn
alcPCfgInHeader = _AlcPCfgInHeader_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 27, 1, 1, 22),
    _AlcPCfgInHeader_Type()
)
alcPCfgInHeader.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alcPCfgInHeader.setStatus("mandatory")


class _AlcPCfgOutHeader_Type(DisplayString):
    """Custom type alcPCfgOutHeader based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 53),
    )


_AlcPCfgOutHeader_Type.__name__ = "DisplayString"
_AlcPCfgOutHeader_Object = MibTableColumn
alcPCfgOutHeader = _AlcPCfgOutHeader_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 27, 1, 1, 23),
    _AlcPCfgOutHeader_Type()
)
alcPCfgOutHeader.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alcPCfgOutHeader.setStatus("mandatory")


class _AlcPCfgReconnectTimeout_Type(Integer32):
    """Custom type alcPCfgReconnectTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1000),
    )


_AlcPCfgReconnectTimeout_Type.__name__ = "Integer32"
_AlcPCfgReconnectTimeout_Object = MibTableColumn
alcPCfgReconnectTimeout = _AlcPCfgReconnectTimeout_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 27, 1, 1, 24),
    _AlcPCfgReconnectTimeout_Type()
)
alcPCfgReconnectTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alcPCfgReconnectTimeout.setStatus("mandatory")


class _AlcPCfgInactivityTimeout_Type(Integer32):
    """Custom type alcPCfgInactivityTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_AlcPCfgInactivityTimeout_Type.__name__ = "Integer32"
_AlcPCfgInactivityTimeout_Object = MibTableColumn
alcPCfgInactivityTimeout = _AlcPCfgInactivityTimeout_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 27, 1, 1, 25),
    _AlcPCfgInactivityTimeout_Type()
)
alcPCfgInactivityTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alcPCfgInactivityTimeout.setStatus("mandatory")


class _AlcPCfgDebounceTimeout_Type(Integer32):
    """Custom type alcPCfgDebounceTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_AlcPCfgDebounceTimeout_Type.__name__ = "Integer32"
_AlcPCfgDebounceTimeout_Object = MibTableColumn
alcPCfgDebounceTimeout = _AlcPCfgDebounceTimeout_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 27, 1, 1, 26),
    _AlcPCfgDebounceTimeout_Type()
)
alcPCfgDebounceTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alcPCfgDebounceTimeout.setStatus("mandatory")


class _AlcPCfgParity_Type(Integer32):
    """Custom type alcPCfgParity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              100)
        )
    )
    namedValues = NamedValues(
        *(("nc", 100),
          ("none", 1),
          ("odd", 2))
    )


_AlcPCfgParity_Type.__name__ = "Integer32"
_AlcPCfgParity_Object = MibTableColumn
alcPCfgParity = _AlcPCfgParity_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 27, 1, 1, 27),
    _AlcPCfgParity_Type()
)
alcPCfgParity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alcPCfgParity.setStatus("mandatory")


class _AlcPCfgConnOptions_Type(DisplayString):
    """Custom type alcPCfgConnOptions based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(3, 32),
    )


_AlcPCfgConnOptions_Type.__name__ = "DisplayString"
_AlcPCfgConnOptions_Object = MibTableColumn
alcPCfgConnOptions = _AlcPCfgConnOptions_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 27, 1, 1, 28),
    _AlcPCfgConnOptions_Type()
)
alcPCfgConnOptions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alcPCfgConnOptions.setStatus("mandatory")


class _AlcPCfgAvailableMesg_Type(DisplayString):
    """Custom type alcPCfgAvailableMesg based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 62),
    )


_AlcPCfgAvailableMesg_Type.__name__ = "DisplayString"
_AlcPCfgAvailableMesg_Object = MibTableColumn
alcPCfgAvailableMesg = _AlcPCfgAvailableMesg_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 27, 1, 1, 29),
    _AlcPCfgAvailableMesg_Type()
)
alcPCfgAvailableMesg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alcPCfgAvailableMesg.setStatus("mandatory")


class _AlcPCfgUnavailableMesg_Type(DisplayString):
    """Custom type alcPCfgUnavailableMesg based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 62),
    )


_AlcPCfgUnavailableMesg_Type.__name__ = "DisplayString"
_AlcPCfgUnavailableMesg_Object = MibTableColumn
alcPCfgUnavailableMesg = _AlcPCfgUnavailableMesg_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 27, 1, 1, 30),
    _AlcPCfgUnavailableMesg_Type()
)
alcPCfgUnavailableMesg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alcPCfgUnavailableMesg.setStatus("mandatory")
_Cdx6500PPCTALCInterchangeTable_Object = MibTable
cdx6500PPCTALCInterchangeTable = _Cdx6500PPCTALCInterchangeTable_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 27, 2)
)
if mibBuilder.loadTexts:
    cdx6500PPCTALCInterchangeTable.setStatus("mandatory")
_Cdx6500PPCTALCInterchangeEntry_Object = MibTableRow
cdx6500PPCTALCInterchangeEntry = _Cdx6500PPCTALCInterchangeEntry_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 27, 2, 1)
)
cdx6500PPCTALCInterchangeEntry.setIndexNames(
    (0, "ALC-OPT-MIB", "alcICfgPortNumber"),
    (0, "ALC-OPT-MIB", "alcICfgInterchangeAddress"),
)
if mibBuilder.loadTexts:
    cdx6500PPCTALCInterchangeEntry.setStatus("mandatory")


class _AlcICfgPortNumber_Type(Integer32):
    """Custom type alcICfgPortNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 54),
    )


_AlcICfgPortNumber_Type.__name__ = "Integer32"
_AlcICfgPortNumber_Object = MibTableColumn
alcICfgPortNumber = _AlcICfgPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 27, 2, 1, 1),
    _AlcICfgPortNumber_Type()
)
alcICfgPortNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alcICfgPortNumber.setStatus("mandatory")


class _AlcICfgInterchangeAddress_Type(OctetString):
    """Custom type alcICfgInterchangeAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_AlcICfgInterchangeAddress_Type.__name__ = "OctetString"
_AlcICfgInterchangeAddress_Object = MibTableColumn
alcICfgInterchangeAddress = _AlcICfgInterchangeAddress_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 27, 2, 1, 2),
    _AlcICfgInterchangeAddress_Type()
)
alcICfgInterchangeAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alcICfgInterchangeAddress.setStatus("mandatory")


class _AlcICfgOptionOnInvalidCCC_Type(Integer32):
    """Custom type alcICfgOptionOnInvalidCCC based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("discard", 2),
          ("ignore", 5),
          ("reenter", 4),
          ("resend", 3))
    )


_AlcICfgOptionOnInvalidCCC_Type.__name__ = "Integer32"
_AlcICfgOptionOnInvalidCCC_Object = MibTableColumn
alcICfgOptionOnInvalidCCC = _AlcICfgOptionOnInvalidCCC_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 27, 2, 1, 3),
    _AlcICfgOptionOnInvalidCCC_Type()
)
alcICfgOptionOnInvalidCCC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alcICfgOptionOnInvalidCCC.setStatus("mandatory")
_AlcICfgGenTerminalAddress_Type = OctetString
_AlcICfgGenTerminalAddress_Object = MibTableColumn
alcICfgGenTerminalAddress = _AlcICfgGenTerminalAddress_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 27, 2, 1, 4),
    _AlcICfgGenTerminalAddress_Type()
)
alcICfgGenTerminalAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alcICfgGenTerminalAddress.setStatus("mandatory")


class _AlcICfgHostTimeout_Type(Integer32):
    """Custom type alcICfgHostTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(50, 100000),
    )


_AlcICfgHostTimeout_Type.__name__ = "Integer32"
_AlcICfgHostTimeout_Object = MibTableColumn
alcICfgHostTimeout = _AlcICfgHostTimeout_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 27, 2, 1, 5),
    _AlcICfgHostTimeout_Type()
)
alcICfgHostTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alcICfgHostTimeout.setStatus("mandatory")


class _AlcICfgMaxComponentsPerFrame_Type(Integer32):
    """Custom type alcICfgMaxComponentsPerFrame based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_AlcICfgMaxComponentsPerFrame_Type.__name__ = "Integer32"
_AlcICfgMaxComponentsPerFrame_Object = MibTableColumn
alcICfgMaxComponentsPerFrame = _AlcICfgMaxComponentsPerFrame_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 27, 2, 1, 6),
    _AlcICfgMaxComponentsPerFrame_Type()
)
alcICfgMaxComponentsPerFrame.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alcICfgMaxComponentsPerFrame.setStatus("mandatory")


class _AlcICfgFastPollCycleCount_Type(Integer32):
    """Custom type alcICfgFastPollCycleCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_AlcICfgFastPollCycleCount_Type.__name__ = "Integer32"
_AlcICfgFastPollCycleCount_Object = MibTableColumn
alcICfgFastPollCycleCount = _AlcICfgFastPollCycleCount_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 27, 2, 1, 7),
    _AlcICfgFastPollCycleCount_Type()
)
alcICfgFastPollCycleCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alcICfgFastPollCycleCount.setStatus("mandatory")


class _AlcICfgSlowPollCycleCount_Type(Integer32):
    """Custom type alcICfgSlowPollCycleCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_AlcICfgSlowPollCycleCount_Type.__name__ = "Integer32"
_AlcICfgSlowPollCycleCount_Object = MibTableColumn
alcICfgSlowPollCycleCount = _AlcICfgSlowPollCycleCount_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 27, 2, 1, 8),
    _AlcICfgSlowPollCycleCount_Type()
)
alcICfgSlowPollCycleCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alcICfgSlowPollCycleCount.setStatus("mandatory")


class _AlcICfgN1Counter_Type(Integer32):
    """Custom type alcICfgN1Counter based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_AlcICfgN1Counter_Type.__name__ = "Integer32"
_AlcICfgN1Counter_Object = MibTableColumn
alcICfgN1Counter = _AlcICfgN1Counter_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 27, 2, 1, 9),
    _AlcICfgN1Counter_Type()
)
alcICfgN1Counter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alcICfgN1Counter.setStatus("mandatory")


class _AlcICfgN2Counter_Type(Integer32):
    """Custom type alcICfgN2Counter based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_AlcICfgN2Counter_Type.__name__ = "Integer32"
_AlcICfgN2Counter_Object = MibTableColumn
alcICfgN2Counter = _AlcICfgN2Counter_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 27, 2, 1, 10),
    _AlcICfgN2Counter_Type()
)
alcICfgN2Counter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alcICfgN2Counter.setStatus("mandatory")


class _AlcICfgT1Timeout_Type(Integer32):
    """Custom type alcICfgT1Timeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(100, 100000),
    )


_AlcICfgT1Timeout_Type.__name__ = "Integer32"
_AlcICfgT1Timeout_Object = MibTableColumn
alcICfgT1Timeout = _AlcICfgT1Timeout_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 27, 2, 1, 11),
    _AlcICfgT1Timeout_Type()
)
alcICfgT1Timeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alcICfgT1Timeout.setStatus("mandatory")


class _AlcICfgT2Timeout_Type(Integer32):
    """Custom type alcICfgT2Timeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(100, 100000),
    )


_AlcICfgT2Timeout_Type.__name__ = "Integer32"
_AlcICfgT2Timeout_Object = MibTableColumn
alcICfgT2Timeout = _AlcICfgT2Timeout_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 27, 2, 1, 12),
    _AlcICfgT2Timeout_Type()
)
alcICfgT2Timeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alcICfgT2Timeout.setStatus("mandatory")


class _AlcICfgReenterMessage_Type(DisplayString):
    """Custom type alcICfgReenterMessage based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_AlcICfgReenterMessage_Type.__name__ = "DisplayString"
_AlcICfgReenterMessage_Object = MibTableColumn
alcICfgReenterMessage = _AlcICfgReenterMessage_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 27, 2, 1, 13),
    _AlcICfgReenterMessage_Type()
)
alcICfgReenterMessage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alcICfgReenterMessage.setStatus("mandatory")


class _AlcICfgStartMessage_Type(DisplayString):
    """Custom type alcICfgStartMessage based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_AlcICfgStartMessage_Type.__name__ = "DisplayString"
_AlcICfgStartMessage_Object = MibTableColumn
alcICfgStartMessage = _AlcICfgStartMessage_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 27, 2, 1, 14),
    _AlcICfgStartMessage_Type()
)
alcICfgStartMessage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alcICfgStartMessage.setStatus("mandatory")


class _AlcICfgStopMessage_Type(DisplayString):
    """Custom type alcICfgStopMessage based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_AlcICfgStopMessage_Type.__name__ = "DisplayString"
_AlcICfgStopMessage_Object = MibTableColumn
alcICfgStopMessage = _AlcICfgStopMessage_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 27, 2, 1, 15),
    _AlcICfgStopMessage_Type()
)
alcICfgStopMessage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alcICfgStopMessage.setStatus("mandatory")


class _AlcICfgOptions_Type(DisplayString):
    """Custom type alcICfgOptions based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(3, 21),
    )


_AlcICfgOptions_Type.__name__ = "DisplayString"
_AlcICfgOptions_Object = MibTableColumn
alcICfgOptions = _AlcICfgOptions_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 27, 2, 1, 16),
    _AlcICfgOptions_Type()
)
alcICfgOptions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alcICfgOptions.setStatus("mandatory")
_AlcICfgValidTAList_Type = DisplayString
_AlcICfgValidTAList_Object = MibTableColumn
alcICfgValidTAList = _AlcICfgValidTAList_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 27, 2, 1, 17),
    _AlcICfgValidTAList_Type()
)
alcICfgValidTAList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alcICfgValidTAList.setStatus("mandatory")


class _AlcICfgConnType_Type(Integer32):
    """Custom type alcICfgConnType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              100)
        )
    )
    namedValues = NamedValues(
        *(("nc", 100),
          ("none", 1),
          ("x25", 2))
    )


_AlcICfgConnType_Type.__name__ = "Integer32"
_AlcICfgConnType_Object = MibTableColumn
alcICfgConnType = _AlcICfgConnType_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 27, 2, 1, 18),
    _AlcICfgConnType_Type()
)
alcICfgConnType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alcICfgConnType.setStatus("mandatory")


class _AlcICfgAcallMnemonic_Type(DisplayString):
    """Custom type alcICfgAcallMnemonic based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_AlcICfgAcallMnemonic_Type.__name__ = "DisplayString"
_AlcICfgAcallMnemonic_Object = MibTableColumn
alcICfgAcallMnemonic = _AlcICfgAcallMnemonic_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 27, 2, 1, 19),
    _AlcICfgAcallMnemonic_Type()
)
alcICfgAcallMnemonic.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alcICfgAcallMnemonic.setStatus("mandatory")


class _AlcICfgCallingAddress_Type(DisplayString):
    """Custom type alcICfgCallingAddress based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_AlcICfgCallingAddress_Type.__name__ = "DisplayString"
_AlcICfgCallingAddress_Object = MibTableColumn
alcICfgCallingAddress = _AlcICfgCallingAddress_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 27, 2, 1, 20),
    _AlcICfgCallingAddress_Type()
)
alcICfgCallingAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alcICfgCallingAddress.setStatus("mandatory")


class _AlcICfgCUD_Type(DisplayString):
    """Custom type alcICfgCUD based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 47),
    )


_AlcICfgCUD_Type.__name__ = "DisplayString"
_AlcICfgCUD_Object = MibTableColumn
alcICfgCUD = _AlcICfgCUD_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 27, 2, 1, 21),
    _AlcICfgCUD_Type()
)
alcICfgCUD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alcICfgCUD.setStatus("mandatory")


class _AlcICfgNumOfBuffers_Type(Integer32):
    """Custom type alcICfgNumOfBuffers based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1000),
    )


_AlcICfgNumOfBuffers_Type.__name__ = "Integer32"
_AlcICfgNumOfBuffers_Object = MibTableColumn
alcICfgNumOfBuffers = _AlcICfgNumOfBuffers_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 27, 2, 1, 22),
    _AlcICfgNumOfBuffers_Type()
)
alcICfgNumOfBuffers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alcICfgNumOfBuffers.setStatus("mandatory")


class _AlcICfgInHeader_Type(DisplayString):
    """Custom type alcICfgInHeader based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 53),
    )


_AlcICfgInHeader_Type.__name__ = "DisplayString"
_AlcICfgInHeader_Object = MibTableColumn
alcICfgInHeader = _AlcICfgInHeader_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 27, 2, 1, 23),
    _AlcICfgInHeader_Type()
)
alcICfgInHeader.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alcICfgInHeader.setStatus("mandatory")


class _AlcICfgOutHeader_Type(DisplayString):
    """Custom type alcICfgOutHeader based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 53),
    )


_AlcICfgOutHeader_Type.__name__ = "DisplayString"
_AlcICfgOutHeader_Object = MibTableColumn
alcICfgOutHeader = _AlcICfgOutHeader_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 27, 2, 1, 24),
    _AlcICfgOutHeader_Type()
)
alcICfgOutHeader.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alcICfgOutHeader.setStatus("mandatory")


class _AlcICfgReconnectTimeout_Type(Integer32):
    """Custom type alcICfgReconnectTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1000),
    )


_AlcICfgReconnectTimeout_Type.__name__ = "Integer32"
_AlcICfgReconnectTimeout_Object = MibTableColumn
alcICfgReconnectTimeout = _AlcICfgReconnectTimeout_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 27, 2, 1, 25),
    _AlcICfgReconnectTimeout_Type()
)
alcICfgReconnectTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alcICfgReconnectTimeout.setStatus("mandatory")


class _AlcICfgInactivityTimeout_Type(Integer32):
    """Custom type alcICfgInactivityTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_AlcICfgInactivityTimeout_Type.__name__ = "Integer32"
_AlcICfgInactivityTimeout_Object = MibTableColumn
alcICfgInactivityTimeout = _AlcICfgInactivityTimeout_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 27, 2, 1, 26),
    _AlcICfgInactivityTimeout_Type()
)
alcICfgInactivityTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alcICfgInactivityTimeout.setStatus("mandatory")


class _AlcICfgDebounceTimeout_Type(Integer32):
    """Custom type alcICfgDebounceTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_AlcICfgDebounceTimeout_Type.__name__ = "Integer32"
_AlcICfgDebounceTimeout_Object = MibTableColumn
alcICfgDebounceTimeout = _AlcICfgDebounceTimeout_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 27, 2, 1, 27),
    _AlcICfgDebounceTimeout_Type()
)
alcICfgDebounceTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alcICfgDebounceTimeout.setStatus("mandatory")


class _AlcICfgParity_Type(Integer32):
    """Custom type alcICfgParity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              100)
        )
    )
    namedValues = NamedValues(
        *(("nc", 100),
          ("none", 1),
          ("odd", 2))
    )


_AlcICfgParity_Type.__name__ = "Integer32"
_AlcICfgParity_Object = MibTableColumn
alcICfgParity = _AlcICfgParity_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 27, 2, 1, 28),
    _AlcICfgParity_Type()
)
alcICfgParity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alcICfgParity.setStatus("mandatory")


class _AlcICfgConnOptions_Type(DisplayString):
    """Custom type alcICfgConnOptions based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(3, 32),
    )


_AlcICfgConnOptions_Type.__name__ = "DisplayString"
_AlcICfgConnOptions_Object = MibTableColumn
alcICfgConnOptions = _AlcICfgConnOptions_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 27, 2, 1, 29),
    _AlcICfgConnOptions_Type()
)
alcICfgConnOptions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alcICfgConnOptions.setStatus("mandatory")


class _AlcICfgAvailableMesg_Type(DisplayString):
    """Custom type alcICfgAvailableMesg based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 62),
    )


_AlcICfgAvailableMesg_Type.__name__ = "DisplayString"
_AlcICfgAvailableMesg_Object = MibTableColumn
alcICfgAvailableMesg = _AlcICfgAvailableMesg_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 27, 2, 1, 30),
    _AlcICfgAvailableMesg_Type()
)
alcICfgAvailableMesg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alcICfgAvailableMesg.setStatus("mandatory")


class _AlcICfgUnavailableMesg_Type(DisplayString):
    """Custom type alcICfgUnavailableMesg based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 62),
    )


_AlcICfgUnavailableMesg_Type.__name__ = "DisplayString"
_AlcICfgUnavailableMesg_Object = MibTableColumn
alcICfgUnavailableMesg = _AlcICfgUnavailableMesg_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 27, 2, 1, 31),
    _AlcICfgUnavailableMesg_Type()
)
alcICfgUnavailableMesg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alcICfgUnavailableMesg.setStatus("mandatory")
_Cdx6500PPCTALCTerminalTable_Object = MibTable
cdx6500PPCTALCTerminalTable = _Cdx6500PPCTALCTerminalTable_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 27, 3)
)
if mibBuilder.loadTexts:
    cdx6500PPCTALCTerminalTable.setStatus("mandatory")
_Cdx6500PPCTALCTerminalEntry_Object = MibTableRow
cdx6500PPCTALCTerminalEntry = _Cdx6500PPCTALCTerminalEntry_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 27, 3, 1)
)
cdx6500PPCTALCTerminalEntry.setIndexNames(
    (0, "ALC-OPT-MIB", "alcTCfgPortNumber"),
    (0, "ALC-OPT-MIB", "alcTCfgInterchangeAddress"),
    (0, "ALC-OPT-MIB", "alcTCfgTerminalAddress"),
)
if mibBuilder.loadTexts:
    cdx6500PPCTALCTerminalEntry.setStatus("mandatory")


class _AlcTCfgPortNumber_Type(Integer32):
    """Custom type alcTCfgPortNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 54),
    )


_AlcTCfgPortNumber_Type.__name__ = "Integer32"
_AlcTCfgPortNumber_Object = MibTableColumn
alcTCfgPortNumber = _AlcTCfgPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 27, 3, 1, 1),
    _AlcTCfgPortNumber_Type()
)
alcTCfgPortNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alcTCfgPortNumber.setStatus("mandatory")


class _AlcTCfgInterchangeAddress_Type(OctetString):
    """Custom type alcTCfgInterchangeAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_AlcTCfgInterchangeAddress_Type.__name__ = "OctetString"
_AlcTCfgInterchangeAddress_Object = MibTableColumn
alcTCfgInterchangeAddress = _AlcTCfgInterchangeAddress_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 27, 3, 1, 2),
    _AlcTCfgInterchangeAddress_Type()
)
alcTCfgInterchangeAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alcTCfgInterchangeAddress.setStatus("mandatory")


class _AlcTCfgTerminalAddress_Type(OctetString):
    """Custom type alcTCfgTerminalAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_AlcTCfgTerminalAddress_Type.__name__ = "OctetString"
_AlcTCfgTerminalAddress_Object = MibTableColumn
alcTCfgTerminalAddress = _AlcTCfgTerminalAddress_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 27, 3, 1, 3),
    _AlcTCfgTerminalAddress_Type()
)
alcTCfgTerminalAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alcTCfgTerminalAddress.setStatus("mandatory")


class _AlcTCfgConnType_Type(Integer32):
    """Custom type alcTCfgConnType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              100)
        )
    )
    namedValues = NamedValues(
        *(("nc", 100),
          ("none", 1),
          ("x25", 2))
    )


_AlcTCfgConnType_Type.__name__ = "Integer32"
_AlcTCfgConnType_Object = MibTableColumn
alcTCfgConnType = _AlcTCfgConnType_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 27, 3, 1, 4),
    _AlcTCfgConnType_Type()
)
alcTCfgConnType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alcTCfgConnType.setStatus("mandatory")


class _AlcTCfgAcallMnemonic_Type(DisplayString):
    """Custom type alcTCfgAcallMnemonic based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_AlcTCfgAcallMnemonic_Type.__name__ = "DisplayString"
_AlcTCfgAcallMnemonic_Object = MibTableColumn
alcTCfgAcallMnemonic = _AlcTCfgAcallMnemonic_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 27, 3, 1, 5),
    _AlcTCfgAcallMnemonic_Type()
)
alcTCfgAcallMnemonic.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alcTCfgAcallMnemonic.setStatus("mandatory")


class _AlcTCfgCallingAddress_Type(DisplayString):
    """Custom type alcTCfgCallingAddress based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_AlcTCfgCallingAddress_Type.__name__ = "DisplayString"
_AlcTCfgCallingAddress_Object = MibTableColumn
alcTCfgCallingAddress = _AlcTCfgCallingAddress_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 27, 3, 1, 6),
    _AlcTCfgCallingAddress_Type()
)
alcTCfgCallingAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alcTCfgCallingAddress.setStatus("mandatory")


class _AlcTCfgCUD_Type(DisplayString):
    """Custom type alcTCfgCUD based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 47),
    )


_AlcTCfgCUD_Type.__name__ = "DisplayString"
_AlcTCfgCUD_Object = MibTableColumn
alcTCfgCUD = _AlcTCfgCUD_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 27, 3, 1, 7),
    _AlcTCfgCUD_Type()
)
alcTCfgCUD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alcTCfgCUD.setStatus("mandatory")


class _AlcTCfgNumOfBuffers_Type(Integer32):
    """Custom type alcTCfgNumOfBuffers based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1000),
    )


_AlcTCfgNumOfBuffers_Type.__name__ = "Integer32"
_AlcTCfgNumOfBuffers_Object = MibTableColumn
alcTCfgNumOfBuffers = _AlcTCfgNumOfBuffers_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 27, 3, 1, 8),
    _AlcTCfgNumOfBuffers_Type()
)
alcTCfgNumOfBuffers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alcTCfgNumOfBuffers.setStatus("mandatory")


class _AlcTCfgInHeader_Type(DisplayString):
    """Custom type alcTCfgInHeader based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 53),
    )


_AlcTCfgInHeader_Type.__name__ = "DisplayString"
_AlcTCfgInHeader_Object = MibTableColumn
alcTCfgInHeader = _AlcTCfgInHeader_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 27, 3, 1, 9),
    _AlcTCfgInHeader_Type()
)
alcTCfgInHeader.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alcTCfgInHeader.setStatus("mandatory")


class _AlcTCfgOutHeader_Type(DisplayString):
    """Custom type alcTCfgOutHeader based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 53),
    )


_AlcTCfgOutHeader_Type.__name__ = "DisplayString"
_AlcTCfgOutHeader_Object = MibTableColumn
alcTCfgOutHeader = _AlcTCfgOutHeader_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 27, 3, 1, 10),
    _AlcTCfgOutHeader_Type()
)
alcTCfgOutHeader.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alcTCfgOutHeader.setStatus("mandatory")


class _AlcTCfgReconnectTimeout_Type(Integer32):
    """Custom type alcTCfgReconnectTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1000),
    )


_AlcTCfgReconnectTimeout_Type.__name__ = "Integer32"
_AlcTCfgReconnectTimeout_Object = MibTableColumn
alcTCfgReconnectTimeout = _AlcTCfgReconnectTimeout_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 27, 3, 1, 11),
    _AlcTCfgReconnectTimeout_Type()
)
alcTCfgReconnectTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alcTCfgReconnectTimeout.setStatus("mandatory")


class _AlcTCfgInactivityTimeout_Type(Integer32):
    """Custom type alcTCfgInactivityTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_AlcTCfgInactivityTimeout_Type.__name__ = "Integer32"
_AlcTCfgInactivityTimeout_Object = MibTableColumn
alcTCfgInactivityTimeout = _AlcTCfgInactivityTimeout_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 27, 3, 1, 12),
    _AlcTCfgInactivityTimeout_Type()
)
alcTCfgInactivityTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alcTCfgInactivityTimeout.setStatus("mandatory")


class _AlcTCfgDebounceTimeout_Type(Integer32):
    """Custom type alcTCfgDebounceTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_AlcTCfgDebounceTimeout_Type.__name__ = "Integer32"
_AlcTCfgDebounceTimeout_Object = MibTableColumn
alcTCfgDebounceTimeout = _AlcTCfgDebounceTimeout_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 27, 3, 1, 13),
    _AlcTCfgDebounceTimeout_Type()
)
alcTCfgDebounceTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alcTCfgDebounceTimeout.setStatus("mandatory")


class _AlcTCfgParity_Type(Integer32):
    """Custom type alcTCfgParity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              100)
        )
    )
    namedValues = NamedValues(
        *(("nc", 100),
          ("none", 1),
          ("odd", 2))
    )


_AlcTCfgParity_Type.__name__ = "Integer32"
_AlcTCfgParity_Object = MibTableColumn
alcTCfgParity = _AlcTCfgParity_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 27, 3, 1, 14),
    _AlcTCfgParity_Type()
)
alcTCfgParity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alcTCfgParity.setStatus("mandatory")


class _AlcTCfgConnOptions_Type(DisplayString):
    """Custom type alcTCfgConnOptions based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(3, 32),
    )


_AlcTCfgConnOptions_Type.__name__ = "DisplayString"
_AlcTCfgConnOptions_Object = MibTableColumn
alcTCfgConnOptions = _AlcTCfgConnOptions_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 27, 3, 1, 15),
    _AlcTCfgConnOptions_Type()
)
alcTCfgConnOptions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alcTCfgConnOptions.setStatus("mandatory")


class _AlcTCfgAvailableMesg_Type(DisplayString):
    """Custom type alcTCfgAvailableMesg based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 62),
    )


_AlcTCfgAvailableMesg_Type.__name__ = "DisplayString"
_AlcTCfgAvailableMesg_Object = MibTableColumn
alcTCfgAvailableMesg = _AlcTCfgAvailableMesg_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 27, 3, 1, 16),
    _AlcTCfgAvailableMesg_Type()
)
alcTCfgAvailableMesg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alcTCfgAvailableMesg.setStatus("mandatory")


class _AlcTCfgUnavailableMesg_Type(DisplayString):
    """Custom type alcTCfgUnavailableMesg based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 62),
    )


_AlcTCfgUnavailableMesg_Type.__name__ = "DisplayString"
_AlcTCfgUnavailableMesg_Object = MibTableColumn
alcTCfgUnavailableMesg = _AlcTCfgUnavailableMesg_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 27, 3, 1, 17),
    _AlcTCfgUnavailableMesg_Type()
)
alcTCfgUnavailableMesg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alcTCfgUnavailableMesg.setStatus("mandatory")
_Cdx6500Statistics_ObjectIdentity = ObjectIdentity
cdx6500Statistics = _Cdx6500Statistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3)
)
_Cdx6500StatProtocolGroup_ObjectIdentity = ObjectIdentity
cdx6500StatProtocolGroup = _Cdx6500StatProtocolGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1)
)
_Cdx6500PSTPortProtocolGroup_ObjectIdentity = ObjectIdentity
cdx6500PSTPortProtocolGroup = _Cdx6500PSTPortProtocolGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1)
)
_Cdx6500PPSTALCStatsTable_ObjectIdentity = ObjectIdentity
cdx6500PPSTALCStatsTable = _Cdx6500PPSTALCStatsTable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 28)
)
_Cdx6500PPSTALCPortTable_Object = MibTable
cdx6500PPSTALCPortTable = _Cdx6500PPSTALCPortTable_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 28, 1)
)
if mibBuilder.loadTexts:
    cdx6500PPSTALCPortTable.setStatus("mandatory")
_Cdx6500PPSTALCPortEntry_Object = MibTableRow
cdx6500PPSTALCPortEntry = _Cdx6500PPSTALCPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 28, 1, 1)
)
cdx6500PPSTALCPortEntry.setIndexNames(
    (0, "ALC-OPT-MIB", "alcPStatsPortNumber"),
)
if mibBuilder.loadTexts:
    cdx6500PPSTALCPortEntry.setStatus("mandatory")


class _AlcPStatsPortNumber_Type(Integer32):
    """Custom type alcPStatsPortNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 54),
    )


_AlcPStatsPortNumber_Type.__name__ = "Integer32"
_AlcPStatsPortNumber_Object = MibTableColumn
alcPStatsPortNumber = _AlcPStatsPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 28, 1, 1, 1),
    _AlcPStatsPortNumber_Type()
)
alcPStatsPortNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alcPStatsPortNumber.setStatus("mandatory")


class _AlcPStatsPortType_Type(Integer32):
    """Custom type alcPStatsPortType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            31
        )
    )
    namedValues = NamedValues(
        ("alc", 31)
    )


_AlcPStatsPortType_Type.__name__ = "Integer32"
_AlcPStatsPortType_Object = MibTableColumn
alcPStatsPortType = _AlcPStatsPortType_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 28, 1, 1, 2),
    _AlcPStatsPortType_Type()
)
alcPStatsPortType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alcPStatsPortType.setStatus("mandatory")


class _AlcPStatsPortState_Type(Integer32):
    """Custom type alcPStatsPortState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              7,
              8,
              9,
              11,
              100)
        )
    )
    namedValues = NamedValues(
        *(("connecting", 9),
          ("flowCtrl", 11),
          ("na", 100),
          ("offline", 1),
          ("online", 2),
          ("pending", 8),
          ("timedOut", 7))
    )


_AlcPStatsPortState_Type.__name__ = "Integer32"
_AlcPStatsPortState_Object = MibTableColumn
alcPStatsPortState = _AlcPStatsPortState_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 28, 1, 1, 3),
    _AlcPStatsPortState_Type()
)
alcPStatsPortState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alcPStatsPortState.setStatus("mandatory")
_AlcPStatsFramesIn_Type = Counter32
_AlcPStatsFramesIn_Object = MibTableColumn
alcPStatsFramesIn = _AlcPStatsFramesIn_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 28, 1, 1, 4),
    _AlcPStatsFramesIn_Type()
)
alcPStatsFramesIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alcPStatsFramesIn.setStatus("mandatory")
_AlcPStatsFramesOut_Type = Counter32
_AlcPStatsFramesOut_Object = MibTableColumn
alcPStatsFramesOut = _AlcPStatsFramesOut_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 28, 1, 1, 5),
    _AlcPStatsFramesOut_Type()
)
alcPStatsFramesOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alcPStatsFramesOut.setStatus("mandatory")
_AlcPStatsDataMesgsIn_Type = Counter32
_AlcPStatsDataMesgsIn_Object = MibTableColumn
alcPStatsDataMesgsIn = _AlcPStatsDataMesgsIn_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 28, 1, 1, 6),
    _AlcPStatsDataMesgsIn_Type()
)
alcPStatsDataMesgsIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alcPStatsDataMesgsIn.setStatus("mandatory")
_AlcPStatsDataMesgsOut_Type = Counter32
_AlcPStatsDataMesgsOut_Object = MibTableColumn
alcPStatsDataMesgsOut = _AlcPStatsDataMesgsOut_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 28, 1, 1, 7),
    _AlcPStatsDataMesgsOut_Type()
)
alcPStatsDataMesgsOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alcPStatsDataMesgsOut.setStatus("mandatory")
_AlcPStatsCharsIn_Type = Counter32
_AlcPStatsCharsIn_Object = MibTableColumn
alcPStatsCharsIn = _AlcPStatsCharsIn_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 28, 1, 1, 8),
    _AlcPStatsCharsIn_Type()
)
alcPStatsCharsIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alcPStatsCharsIn.setStatus("mandatory")
_AlcPStatsCharsOut_Type = Counter32
_AlcPStatsCharsOut_Object = MibTableColumn
alcPStatsCharsOut = _AlcPStatsCharsOut_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 28, 1, 1, 9),
    _AlcPStatsCharsOut_Type()
)
alcPStatsCharsOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alcPStatsCharsOut.setStatus("mandatory")
_AlcPStatsPolls_Type = Counter32
_AlcPStatsPolls_Object = MibTableColumn
alcPStatsPolls = _AlcPStatsPolls_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 28, 1, 1, 10),
    _AlcPStatsPolls_Type()
)
alcPStatsPolls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alcPStatsPolls.setStatus("mandatory")
_AlcPStatsGAs_Type = Counter32
_AlcPStatsGAs_Object = MibTableColumn
alcPStatsGAs = _AlcPStatsGAs_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 28, 1, 1, 11),
    _AlcPStatsGAs_Type()
)
alcPStatsGAs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alcPStatsGAs.setStatus("mandatory")
_AlcPStatsResets_Type = Counter32
_AlcPStatsResets_Object = MibTableColumn
alcPStatsResets = _AlcPStatsResets_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 28, 1, 1, 12),
    _AlcPStatsResets_Type()
)
alcPStatsResets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alcPStatsResets.setStatus("mandatory")
_AlcPStatsDiscardBadIAIn_Type = Counter32
_AlcPStatsDiscardBadIAIn_Object = MibTableColumn
alcPStatsDiscardBadIAIn = _AlcPStatsDiscardBadIAIn_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 28, 1, 1, 13),
    _AlcPStatsDiscardBadIAIn_Type()
)
alcPStatsDiscardBadIAIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alcPStatsDiscardBadIAIn.setStatus("mandatory")
_AlcPStatsDiscardBadIAOut_Type = Counter32
_AlcPStatsDiscardBadIAOut_Object = MibTableColumn
alcPStatsDiscardBadIAOut = _AlcPStatsDiscardBadIAOut_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 28, 1, 1, 14),
    _AlcPStatsDiscardBadIAOut_Type()
)
alcPStatsDiscardBadIAOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alcPStatsDiscardBadIAOut.setStatus("mandatory")
_AlcPStatsMaxQSizeOut_Type = Integer32
_AlcPStatsMaxQSizeOut_Object = MibTableColumn
alcPStatsMaxQSizeOut = _AlcPStatsMaxQSizeOut_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 28, 1, 1, 15),
    _AlcPStatsMaxQSizeOut_Type()
)
alcPStatsMaxQSizeOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alcPStatsMaxQSizeOut.setStatus("mandatory")
_AlcPStatsCCCErrors_Type = Counter32
_AlcPStatsCCCErrors_Object = MibTableColumn
alcPStatsCCCErrors = _AlcPStatsCCCErrors_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 28, 1, 1, 16),
    _AlcPStatsCCCErrors_Type()
)
alcPStatsCCCErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alcPStatsCCCErrors.setStatus("mandatory")
_AlcPStatsSignalLosses_Type = Counter32
_AlcPStatsSignalLosses_Object = MibTableColumn
alcPStatsSignalLosses = _AlcPStatsSignalLosses_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 28, 1, 1, 17),
    _AlcPStatsSignalLosses_Type()
)
alcPStatsSignalLosses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alcPStatsSignalLosses.setStatus("mandatory")
_AlcPStatsOverlengthFrames_Type = Counter32
_AlcPStatsOverlengthFrames_Object = MibTableColumn
alcPStatsOverlengthFrames = _AlcPStatsOverlengthFrames_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 28, 1, 1, 18),
    _AlcPStatsOverlengthFrames_Type()
)
alcPStatsOverlengthFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alcPStatsOverlengthFrames.setStatus("mandatory")


class _AlcPStatsPortStatus_Type(Integer32):
    """Custom type alcPStatsPortStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              100)
        )
    )
    namedValues = NamedValues(
        *(("busyOut", 3),
          ("disabled", 1),
          ("down", 5),
          ("enabled", 2),
          ("na", 100),
          ("up", 4))
    )


_AlcPStatsPortStatus_Type.__name__ = "Integer32"
_AlcPStatsPortStatus_Object = MibTableColumn
alcPStatsPortStatus = _AlcPStatsPortStatus_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 28, 1, 1, 19),
    _AlcPStatsPortStatus_Type()
)
alcPStatsPortStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alcPStatsPortStatus.setStatus("mandatory")


class _AlcPStatsConnState_Type(Integer32):
    """Custom type alcPStatsConnState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              100)
        )
    )
    namedValues = NamedValues(
        *(("connecting", 3),
          ("inactive", 4),
          ("na", 100),
          ("offline", 2),
          ("online", 1),
          ("pending", 5))
    )


_AlcPStatsConnState_Type.__name__ = "Integer32"
_AlcPStatsConnState_Object = MibTableColumn
alcPStatsConnState = _AlcPStatsConnState_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 28, 1, 1, 20),
    _AlcPStatsConnState_Type()
)
alcPStatsConnState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alcPStatsConnState.setStatus("mandatory")
_AlcPStatsALCMesgsIn_Type = Counter32
_AlcPStatsALCMesgsIn_Object = MibTableColumn
alcPStatsALCMesgsIn = _AlcPStatsALCMesgsIn_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 28, 1, 1, 21),
    _AlcPStatsALCMesgsIn_Type()
)
alcPStatsALCMesgsIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alcPStatsALCMesgsIn.setStatus("mandatory")
_AlcPStatsALCMesgsOut_Type = Counter32
_AlcPStatsALCMesgsOut_Object = MibTableColumn
alcPStatsALCMesgsOut = _AlcPStatsALCMesgsOut_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 28, 1, 1, 22),
    _AlcPStatsALCMesgsOut_Type()
)
alcPStatsALCMesgsOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alcPStatsALCMesgsOut.setStatus("mandatory")
_AlcPStatsX25MesgsIn_Type = Counter32
_AlcPStatsX25MesgsIn_Object = MibTableColumn
alcPStatsX25MesgsIn = _AlcPStatsX25MesgsIn_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 28, 1, 1, 23),
    _AlcPStatsX25MesgsIn_Type()
)
alcPStatsX25MesgsIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alcPStatsX25MesgsIn.setStatus("mandatory")
_AlcPStatsX25MesgsOut_Type = Counter32
_AlcPStatsX25MesgsOut_Object = MibTableColumn
alcPStatsX25MesgsOut = _AlcPStatsX25MesgsOut_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 28, 1, 1, 24),
    _AlcPStatsX25MesgsOut_Type()
)
alcPStatsX25MesgsOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alcPStatsX25MesgsOut.setStatus("mandatory")
_AlcPStatsALCCharsIn_Type = Counter32
_AlcPStatsALCCharsIn_Object = MibTableColumn
alcPStatsALCCharsIn = _AlcPStatsALCCharsIn_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 28, 1, 1, 25),
    _AlcPStatsALCCharsIn_Type()
)
alcPStatsALCCharsIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alcPStatsALCCharsIn.setStatus("mandatory")
_AlcPStatsALCCharsOut_Type = Counter32
_AlcPStatsALCCharsOut_Object = MibTableColumn
alcPStatsALCCharsOut = _AlcPStatsALCCharsOut_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 28, 1, 1, 26),
    _AlcPStatsALCCharsOut_Type()
)
alcPStatsALCCharsOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alcPStatsALCCharsOut.setStatus("mandatory")
_AlcPStatsX25CharsIn_Type = Counter32
_AlcPStatsX25CharsIn_Object = MibTableColumn
alcPStatsX25CharsIn = _AlcPStatsX25CharsIn_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 28, 1, 1, 27),
    _AlcPStatsX25CharsIn_Type()
)
alcPStatsX25CharsIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alcPStatsX25CharsIn.setStatus("mandatory")
_AlcPStatsX25CharsOut_Type = Counter32
_AlcPStatsX25CharsOut_Object = MibTableColumn
alcPStatsX25CharsOut = _AlcPStatsX25CharsOut_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 28, 1, 1, 28),
    _AlcPStatsX25CharsOut_Type()
)
alcPStatsX25CharsOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alcPStatsX25CharsOut.setStatus("mandatory")
_AlcPStatsALCDiscardedMesgsEntityDown_Type = Counter32
_AlcPStatsALCDiscardedMesgsEntityDown_Object = MibTableColumn
alcPStatsALCDiscardedMesgsEntityDown = _AlcPStatsALCDiscardedMesgsEntityDown_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 28, 1, 1, 29),
    _AlcPStatsALCDiscardedMesgsEntityDown_Type()
)
alcPStatsALCDiscardedMesgsEntityDown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alcPStatsALCDiscardedMesgsEntityDown.setStatus("mandatory")
_AlcPStatsX25DiscardedMesgsEntityDown_Type = Counter32
_AlcPStatsX25DiscardedMesgsEntityDown_Object = MibTableColumn
alcPStatsX25DiscardedMesgsEntityDown = _AlcPStatsX25DiscardedMesgsEntityDown_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 28, 1, 1, 30),
    _AlcPStatsX25DiscardedMesgsEntityDown_Type()
)
alcPStatsX25DiscardedMesgsEntityDown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alcPStatsX25DiscardedMesgsEntityDown.setStatus("mandatory")
_AlcPStatsX25DiscardedMesgsBadALCAddr_Type = Counter32
_AlcPStatsX25DiscardedMesgsBadALCAddr_Object = MibTableColumn
alcPStatsX25DiscardedMesgsBadALCAddr = _AlcPStatsX25DiscardedMesgsBadALCAddr_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 28, 1, 1, 31),
    _AlcPStatsX25DiscardedMesgsBadALCAddr_Type()
)
alcPStatsX25DiscardedMesgsBadALCAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alcPStatsX25DiscardedMesgsBadALCAddr.setStatus("mandatory")
_AlcPStatsX25DiscardedMesgsBadHeader_Type = Counter32
_AlcPStatsX25DiscardedMesgsBadHeader_Object = MibTableColumn
alcPStatsX25DiscardedMesgsBadHeader = _AlcPStatsX25DiscardedMesgsBadHeader_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 28, 1, 1, 32),
    _AlcPStatsX25DiscardedMesgsBadHeader_Type()
)
alcPStatsX25DiscardedMesgsBadHeader.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alcPStatsX25DiscardedMesgsBadHeader.setStatus("mandatory")
_AlcPStatsX25DiscardedMesgsTooLong_Type = Counter32
_AlcPStatsX25DiscardedMesgsTooLong_Object = MibTableColumn
alcPStatsX25DiscardedMesgsTooLong = _AlcPStatsX25DiscardedMesgsTooLong_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 28, 1, 1, 33),
    _AlcPStatsX25DiscardedMesgsTooLong_Type()
)
alcPStatsX25DiscardedMesgsTooLong.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alcPStatsX25DiscardedMesgsTooLong.setStatus("mandatory")
_AlcPStatsALCDiscardedMesgsQFull_Type = Counter32
_AlcPStatsALCDiscardedMesgsQFull_Object = MibTableColumn
alcPStatsALCDiscardedMesgsQFull = _AlcPStatsALCDiscardedMesgsQFull_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 28, 1, 1, 34),
    _AlcPStatsALCDiscardedMesgsQFull_Type()
)
alcPStatsALCDiscardedMesgsQFull.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alcPStatsALCDiscardedMesgsQFull.setStatus("mandatory")
_AlcPStatsX25DiscardedMesgsQFull_Type = Counter32
_AlcPStatsX25DiscardedMesgsQFull_Object = MibTableColumn
alcPStatsX25DiscardedMesgsQFull = _AlcPStatsX25DiscardedMesgsQFull_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 28, 1, 1, 35),
    _AlcPStatsX25DiscardedMesgsQFull_Type()
)
alcPStatsX25DiscardedMesgsQFull.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alcPStatsX25DiscardedMesgsQFull.setStatus("mandatory")
_AlcPStatsCurrTxALCQSize_Type = Integer32
_AlcPStatsCurrTxALCQSize_Object = MibTableColumn
alcPStatsCurrTxALCQSize = _AlcPStatsCurrTxALCQSize_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 28, 1, 1, 36),
    _AlcPStatsCurrTxALCQSize_Type()
)
alcPStatsCurrTxALCQSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alcPStatsCurrTxALCQSize.setStatus("mandatory")
_AlcPStatsCurrTxX25QSize_Type = Integer32
_AlcPStatsCurrTxX25QSize_Object = MibTableColumn
alcPStatsCurrTxX25QSize = _AlcPStatsCurrTxX25QSize_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 28, 1, 1, 37),
    _AlcPStatsCurrTxX25QSize_Type()
)
alcPStatsCurrTxX25QSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alcPStatsCurrTxX25QSize.setStatus("mandatory")
_AlcPStatsMaxTxALCQSize_Type = Integer32
_AlcPStatsMaxTxALCQSize_Object = MibTableColumn
alcPStatsMaxTxALCQSize = _AlcPStatsMaxTxALCQSize_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 28, 1, 1, 38),
    _AlcPStatsMaxTxALCQSize_Type()
)
alcPStatsMaxTxALCQSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alcPStatsMaxTxALCQSize.setStatus("mandatory")
_AlcPStatsMaxTxX25QSize_Type = Integer32
_AlcPStatsMaxTxX25QSize_Object = MibTableColumn
alcPStatsMaxTxX25QSize = _AlcPStatsMaxTxX25QSize_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 28, 1, 1, 39),
    _AlcPStatsMaxTxX25QSize_Type()
)
alcPStatsMaxTxX25QSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alcPStatsMaxTxX25QSize.setStatus("mandatory")
_Cdx6500PPSTALCInterchangeTable_Object = MibTable
cdx6500PPSTALCInterchangeTable = _Cdx6500PPSTALCInterchangeTable_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 28, 2)
)
if mibBuilder.loadTexts:
    cdx6500PPSTALCInterchangeTable.setStatus("mandatory")
_Cdx6500PPSTALCInterchangeEntry_Object = MibTableRow
cdx6500PPSTALCInterchangeEntry = _Cdx6500PPSTALCInterchangeEntry_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 28, 2, 1)
)
cdx6500PPSTALCInterchangeEntry.setIndexNames(
    (0, "ALC-OPT-MIB", "alcIStatsPortNumber"),
    (0, "ALC-OPT-MIB", "alcIStatsInterchangeAddress"),
)
if mibBuilder.loadTexts:
    cdx6500PPSTALCInterchangeEntry.setStatus("mandatory")


class _AlcIStatsPortNumber_Type(Integer32):
    """Custom type alcIStatsPortNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 54),
    )


_AlcIStatsPortNumber_Type.__name__ = "Integer32"
_AlcIStatsPortNumber_Object = MibTableColumn
alcIStatsPortNumber = _AlcIStatsPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 28, 2, 1, 1),
    _AlcIStatsPortNumber_Type()
)
alcIStatsPortNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alcIStatsPortNumber.setStatus("mandatory")


class _AlcIStatsInterchangeAddress_Type(OctetString):
    """Custom type alcIStatsInterchangeAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_AlcIStatsInterchangeAddress_Type.__name__ = "OctetString"
_AlcIStatsInterchangeAddress_Object = MibTableColumn
alcIStatsInterchangeAddress = _AlcIStatsInterchangeAddress_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 28, 2, 1, 2),
    _AlcIStatsInterchangeAddress_Type()
)
alcIStatsInterchangeAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alcIStatsInterchangeAddress.setStatus("mandatory")


class _AlcIStatsInterchangeState_Type(Integer32):
    """Custom type alcIStatsInterchangeState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              6,
              7,
              8,
              10,
              11,
              100)
        )
    )
    namedValues = NamedValues(
        *(("failed", 10),
          ("fastPoll", 3),
          ("flowCtrl", 11),
          ("na", 100),
          ("offline", 1),
          ("online", 2),
          ("pending", 8),
          ("slowPoll", 4),
          ("stopped", 6),
          ("timedOut", 7))
    )


_AlcIStatsInterchangeState_Type.__name__ = "Integer32"
_AlcIStatsInterchangeState_Object = MibTableColumn
alcIStatsInterchangeState = _AlcIStatsInterchangeState_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 28, 2, 1, 3),
    _AlcIStatsInterchangeState_Type()
)
alcIStatsInterchangeState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alcIStatsInterchangeState.setStatus("mandatory")
_AlcIStatsFramesIn_Type = Counter32
_AlcIStatsFramesIn_Object = MibTableColumn
alcIStatsFramesIn = _AlcIStatsFramesIn_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 28, 2, 1, 4),
    _AlcIStatsFramesIn_Type()
)
alcIStatsFramesIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alcIStatsFramesIn.setStatus("mandatory")
_AlcIStatsFramesOut_Type = Counter32
_AlcIStatsFramesOut_Object = MibTableColumn
alcIStatsFramesOut = _AlcIStatsFramesOut_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 28, 2, 1, 5),
    _AlcIStatsFramesOut_Type()
)
alcIStatsFramesOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alcIStatsFramesOut.setStatus("mandatory")
_AlcIStatsDataMesgsIn_Type = Counter32
_AlcIStatsDataMesgsIn_Object = MibTableColumn
alcIStatsDataMesgsIn = _AlcIStatsDataMesgsIn_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 28, 2, 1, 6),
    _AlcIStatsDataMesgsIn_Type()
)
alcIStatsDataMesgsIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alcIStatsDataMesgsIn.setStatus("mandatory")
_AlcIStatsDataMesgsOut_Type = Counter32
_AlcIStatsDataMesgsOut_Object = MibTableColumn
alcIStatsDataMesgsOut = _AlcIStatsDataMesgsOut_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 28, 2, 1, 7),
    _AlcIStatsDataMesgsOut_Type()
)
alcIStatsDataMesgsOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alcIStatsDataMesgsOut.setStatus("mandatory")
_AlcIStatsCharsIn_Type = Counter32
_AlcIStatsCharsIn_Object = MibTableColumn
alcIStatsCharsIn = _AlcIStatsCharsIn_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 28, 2, 1, 8),
    _AlcIStatsCharsIn_Type()
)
alcIStatsCharsIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alcIStatsCharsIn.setStatus("mandatory")
_AlcIStatsCharsOut_Type = Counter32
_AlcIStatsCharsOut_Object = MibTableColumn
alcIStatsCharsOut = _AlcIStatsCharsOut_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 28, 2, 1, 9),
    _AlcIStatsCharsOut_Type()
)
alcIStatsCharsOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alcIStatsCharsOut.setStatus("mandatory")
_AlcIStatsPolls_Type = Counter32
_AlcIStatsPolls_Object = MibTableColumn
alcIStatsPolls = _AlcIStatsPolls_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 28, 2, 1, 10),
    _AlcIStatsPolls_Type()
)
alcIStatsPolls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alcIStatsPolls.setStatus("mandatory")
_AlcIStatsGAs_Type = Counter32
_AlcIStatsGAs_Object = MibTableColumn
alcIStatsGAs = _AlcIStatsGAs_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 28, 2, 1, 11),
    _AlcIStatsGAs_Type()
)
alcIStatsGAs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alcIStatsGAs.setStatus("mandatory")
_AlcIStatsResets_Type = Counter32
_AlcIStatsResets_Object = MibTableColumn
alcIStatsResets = _AlcIStatsResets_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 28, 2, 1, 12),
    _AlcIStatsResets_Type()
)
alcIStatsResets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alcIStatsResets.setStatus("mandatory")
_AlcIStatsDiscardBadTAIn_Type = Counter32
_AlcIStatsDiscardBadTAIn_Object = MibTableColumn
alcIStatsDiscardBadTAIn = _AlcIStatsDiscardBadTAIn_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 28, 2, 1, 13),
    _AlcIStatsDiscardBadTAIn_Type()
)
alcIStatsDiscardBadTAIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alcIStatsDiscardBadTAIn.setStatus("mandatory")
_AlcIStatsDiscardBadTAOut_Type = Counter32
_AlcIStatsDiscardBadTAOut_Object = MibTableColumn
alcIStatsDiscardBadTAOut = _AlcIStatsDiscardBadTAOut_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 28, 2, 1, 14),
    _AlcIStatsDiscardBadTAOut_Type()
)
alcIStatsDiscardBadTAOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alcIStatsDiscardBadTAOut.setStatus("mandatory")
_AlcIStatsDisabledIAIn_Type = Counter32
_AlcIStatsDisabledIAIn_Object = MibTableColumn
alcIStatsDisabledIAIn = _AlcIStatsDisabledIAIn_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 28, 2, 1, 15),
    _AlcIStatsDisabledIAIn_Type()
)
alcIStatsDisabledIAIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alcIStatsDisabledIAIn.setStatus("mandatory")
_AlcIStatsDisabledIAOut_Type = Counter32
_AlcIStatsDisabledIAOut_Object = MibTableColumn
alcIStatsDisabledIAOut = _AlcIStatsDisabledIAOut_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 28, 2, 1, 16),
    _AlcIStatsDisabledIAOut_Type()
)
alcIStatsDisabledIAOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alcIStatsDisabledIAOut.setStatus("mandatory")
_AlcIStatsMaxQSizeOut_Type = Integer32
_AlcIStatsMaxQSizeOut_Object = MibTableColumn
alcIStatsMaxQSizeOut = _AlcIStatsMaxQSizeOut_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 28, 2, 1, 17),
    _AlcIStatsMaxQSizeOut_Type()
)
alcIStatsMaxQSizeOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alcIStatsMaxQSizeOut.setStatus("mandatory")
_AlcIStatsCCCErrors_Type = Counter32
_AlcIStatsCCCErrors_Object = MibTableColumn
alcIStatsCCCErrors = _AlcIStatsCCCErrors_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 28, 2, 1, 18),
    _AlcIStatsCCCErrors_Type()
)
alcIStatsCCCErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alcIStatsCCCErrors.setStatus("mandatory")
_AlcIStatsT1Timeouts_Type = Counter32
_AlcIStatsT1Timeouts_Object = MibTableColumn
alcIStatsT1Timeouts = _AlcIStatsT1Timeouts_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 28, 2, 1, 19),
    _AlcIStatsT1Timeouts_Type()
)
alcIStatsT1Timeouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alcIStatsT1Timeouts.setStatus("mandatory")
_AlcIStatsT2Timeouts_Type = Counter32
_AlcIStatsT2Timeouts_Object = MibTableColumn
alcIStatsT2Timeouts = _AlcIStatsT2Timeouts_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 28, 2, 1, 20),
    _AlcIStatsT2Timeouts_Type()
)
alcIStatsT2Timeouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alcIStatsT2Timeouts.setStatus("mandatory")


class _AlcIStatsConnState_Type(Integer32):
    """Custom type alcIStatsConnState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              100)
        )
    )
    namedValues = NamedValues(
        *(("connecting", 3),
          ("inactive", 4),
          ("na", 100),
          ("offline", 2),
          ("online", 1),
          ("pending", 5))
    )


_AlcIStatsConnState_Type.__name__ = "Integer32"
_AlcIStatsConnState_Object = MibTableColumn
alcIStatsConnState = _AlcIStatsConnState_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 28, 2, 1, 21),
    _AlcIStatsConnState_Type()
)
alcIStatsConnState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alcIStatsConnState.setStatus("mandatory")
_AlcIStatsALCMesgsIn_Type = Counter32
_AlcIStatsALCMesgsIn_Object = MibTableColumn
alcIStatsALCMesgsIn = _AlcIStatsALCMesgsIn_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 28, 2, 1, 22),
    _AlcIStatsALCMesgsIn_Type()
)
alcIStatsALCMesgsIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alcIStatsALCMesgsIn.setStatus("mandatory")
_AlcIStatsALCMesgsOut_Type = Counter32
_AlcIStatsALCMesgsOut_Object = MibTableColumn
alcIStatsALCMesgsOut = _AlcIStatsALCMesgsOut_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 28, 2, 1, 23),
    _AlcIStatsALCMesgsOut_Type()
)
alcIStatsALCMesgsOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alcIStatsALCMesgsOut.setStatus("mandatory")
_AlcIStatsX25MesgsIn_Type = Counter32
_AlcIStatsX25MesgsIn_Object = MibTableColumn
alcIStatsX25MesgsIn = _AlcIStatsX25MesgsIn_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 28, 2, 1, 24),
    _AlcIStatsX25MesgsIn_Type()
)
alcIStatsX25MesgsIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alcIStatsX25MesgsIn.setStatus("mandatory")
_AlcIStatsX25MesgsOut_Type = Counter32
_AlcIStatsX25MesgsOut_Object = MibTableColumn
alcIStatsX25MesgsOut = _AlcIStatsX25MesgsOut_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 28, 2, 1, 25),
    _AlcIStatsX25MesgsOut_Type()
)
alcIStatsX25MesgsOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alcIStatsX25MesgsOut.setStatus("mandatory")
_AlcIStatsALCCharsIn_Type = Counter32
_AlcIStatsALCCharsIn_Object = MibTableColumn
alcIStatsALCCharsIn = _AlcIStatsALCCharsIn_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 28, 2, 1, 26),
    _AlcIStatsALCCharsIn_Type()
)
alcIStatsALCCharsIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alcIStatsALCCharsIn.setStatus("mandatory")
_AlcIStatsALCCharsOut_Type = Counter32
_AlcIStatsALCCharsOut_Object = MibTableColumn
alcIStatsALCCharsOut = _AlcIStatsALCCharsOut_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 28, 2, 1, 27),
    _AlcIStatsALCCharsOut_Type()
)
alcIStatsALCCharsOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alcIStatsALCCharsOut.setStatus("mandatory")
_AlcIStatsX25CharsIn_Type = Counter32
_AlcIStatsX25CharsIn_Object = MibTableColumn
alcIStatsX25CharsIn = _AlcIStatsX25CharsIn_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 28, 2, 1, 28),
    _AlcIStatsX25CharsIn_Type()
)
alcIStatsX25CharsIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alcIStatsX25CharsIn.setStatus("mandatory")
_AlcIStatsX25CharsOut_Type = Counter32
_AlcIStatsX25CharsOut_Object = MibTableColumn
alcIStatsX25CharsOut = _AlcIStatsX25CharsOut_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 28, 2, 1, 29),
    _AlcIStatsX25CharsOut_Type()
)
alcIStatsX25CharsOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alcIStatsX25CharsOut.setStatus("mandatory")
_AlcIStatsALCDiscardedMesgsEntityDown_Type = Counter32
_AlcIStatsALCDiscardedMesgsEntityDown_Object = MibTableColumn
alcIStatsALCDiscardedMesgsEntityDown = _AlcIStatsALCDiscardedMesgsEntityDown_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 28, 2, 1, 30),
    _AlcIStatsALCDiscardedMesgsEntityDown_Type()
)
alcIStatsALCDiscardedMesgsEntityDown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alcIStatsALCDiscardedMesgsEntityDown.setStatus("mandatory")
_AlcIStatsX25DiscardedMesgsEntityDown_Type = Counter32
_AlcIStatsX25DiscardedMesgsEntityDown_Object = MibTableColumn
alcIStatsX25DiscardedMesgsEntityDown = _AlcIStatsX25DiscardedMesgsEntityDown_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 28, 2, 1, 31),
    _AlcIStatsX25DiscardedMesgsEntityDown_Type()
)
alcIStatsX25DiscardedMesgsEntityDown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alcIStatsX25DiscardedMesgsEntityDown.setStatus("mandatory")
_AlcIStatsX25DiscardedMesgsBadALCAddr_Type = Counter32
_AlcIStatsX25DiscardedMesgsBadALCAddr_Object = MibTableColumn
alcIStatsX25DiscardedMesgsBadALCAddr = _AlcIStatsX25DiscardedMesgsBadALCAddr_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 28, 2, 1, 32),
    _AlcIStatsX25DiscardedMesgsBadALCAddr_Type()
)
alcIStatsX25DiscardedMesgsBadALCAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alcIStatsX25DiscardedMesgsBadALCAddr.setStatus("mandatory")
_AlcIStatsX25DiscardedMesgsBadHeader_Type = Counter32
_AlcIStatsX25DiscardedMesgsBadHeader_Object = MibTableColumn
alcIStatsX25DiscardedMesgsBadHeader = _AlcIStatsX25DiscardedMesgsBadHeader_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 28, 2, 1, 33),
    _AlcIStatsX25DiscardedMesgsBadHeader_Type()
)
alcIStatsX25DiscardedMesgsBadHeader.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alcIStatsX25DiscardedMesgsBadHeader.setStatus("mandatory")
_AlcIStatsX25DiscardedMesgsTooLong_Type = Counter32
_AlcIStatsX25DiscardedMesgsTooLong_Object = MibTableColumn
alcIStatsX25DiscardedMesgsTooLong = _AlcIStatsX25DiscardedMesgsTooLong_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 28, 2, 1, 34),
    _AlcIStatsX25DiscardedMesgsTooLong_Type()
)
alcIStatsX25DiscardedMesgsTooLong.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alcIStatsX25DiscardedMesgsTooLong.setStatus("mandatory")
_AlcIStatsALCDiscardedMesgsQFull_Type = Counter32
_AlcIStatsALCDiscardedMesgsQFull_Object = MibTableColumn
alcIStatsALCDiscardedMesgsQFull = _AlcIStatsALCDiscardedMesgsQFull_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 28, 2, 1, 35),
    _AlcIStatsALCDiscardedMesgsQFull_Type()
)
alcIStatsALCDiscardedMesgsQFull.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alcIStatsALCDiscardedMesgsQFull.setStatus("mandatory")
_AlcIStatsX25DiscardedMesgsQFull_Type = Counter32
_AlcIStatsX25DiscardedMesgsQFull_Object = MibTableColumn
alcIStatsX25DiscardedMesgsQFull = _AlcIStatsX25DiscardedMesgsQFull_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 28, 2, 1, 36),
    _AlcIStatsX25DiscardedMesgsQFull_Type()
)
alcIStatsX25DiscardedMesgsQFull.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alcIStatsX25DiscardedMesgsQFull.setStatus("mandatory")
_AlcIStatsCurrTxALCQSize_Type = Integer32
_AlcIStatsCurrTxALCQSize_Object = MibTableColumn
alcIStatsCurrTxALCQSize = _AlcIStatsCurrTxALCQSize_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 28, 2, 1, 37),
    _AlcIStatsCurrTxALCQSize_Type()
)
alcIStatsCurrTxALCQSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alcIStatsCurrTxALCQSize.setStatus("mandatory")
_AlcIStatsCurrTxX25QSize_Type = Integer32
_AlcIStatsCurrTxX25QSize_Object = MibTableColumn
alcIStatsCurrTxX25QSize = _AlcIStatsCurrTxX25QSize_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 28, 2, 1, 38),
    _AlcIStatsCurrTxX25QSize_Type()
)
alcIStatsCurrTxX25QSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alcIStatsCurrTxX25QSize.setStatus("mandatory")
_AlcIStatsMaxTxALCQSize_Type = Integer32
_AlcIStatsMaxTxALCQSize_Object = MibTableColumn
alcIStatsMaxTxALCQSize = _AlcIStatsMaxTxALCQSize_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 28, 2, 1, 39),
    _AlcIStatsMaxTxALCQSize_Type()
)
alcIStatsMaxTxALCQSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alcIStatsMaxTxALCQSize.setStatus("mandatory")
_AlcIStatsMaxTxX25QSize_Type = Integer32
_AlcIStatsMaxTxX25QSize_Object = MibTableColumn
alcIStatsMaxTxX25QSize = _AlcIStatsMaxTxX25QSize_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 28, 2, 1, 40),
    _AlcIStatsMaxTxX25QSize_Type()
)
alcIStatsMaxTxX25QSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alcIStatsMaxTxX25QSize.setStatus("mandatory")
_Cdx6500PPSTALCTerminalTable_Object = MibTable
cdx6500PPSTALCTerminalTable = _Cdx6500PPSTALCTerminalTable_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 28, 3)
)
if mibBuilder.loadTexts:
    cdx6500PPSTALCTerminalTable.setStatus("mandatory")
_Cdx6500PPSTALCTerminalEntry_Object = MibTableRow
cdx6500PPSTALCTerminalEntry = _Cdx6500PPSTALCTerminalEntry_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 28, 3, 1)
)
cdx6500PPSTALCTerminalEntry.setIndexNames(
    (0, "ALC-OPT-MIB", "alcTStatsPortNumber"),
    (0, "ALC-OPT-MIB", "alcTStatsInterchangeAddress"),
    (0, "ALC-OPT-MIB", "alcTStatsTerminalAddress"),
)
if mibBuilder.loadTexts:
    cdx6500PPSTALCTerminalEntry.setStatus("mandatory")


class _AlcTStatsPortNumber_Type(Integer32):
    """Custom type alcTStatsPortNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 54),
    )


_AlcTStatsPortNumber_Type.__name__ = "Integer32"
_AlcTStatsPortNumber_Object = MibTableColumn
alcTStatsPortNumber = _AlcTStatsPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 28, 3, 1, 1),
    _AlcTStatsPortNumber_Type()
)
alcTStatsPortNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alcTStatsPortNumber.setStatus("mandatory")


class _AlcTStatsInterchangeAddress_Type(OctetString):
    """Custom type alcTStatsInterchangeAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_AlcTStatsInterchangeAddress_Type.__name__ = "OctetString"
_AlcTStatsInterchangeAddress_Object = MibTableColumn
alcTStatsInterchangeAddress = _AlcTStatsInterchangeAddress_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 28, 3, 1, 2),
    _AlcTStatsInterchangeAddress_Type()
)
alcTStatsInterchangeAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alcTStatsInterchangeAddress.setStatus("mandatory")


class _AlcTStatsTerminalAddress_Type(OctetString):
    """Custom type alcTStatsTerminalAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_AlcTStatsTerminalAddress_Type.__name__ = "OctetString"
_AlcTStatsTerminalAddress_Object = MibTableColumn
alcTStatsTerminalAddress = _AlcTStatsTerminalAddress_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 28, 3, 1, 3),
    _AlcTStatsTerminalAddress_Type()
)
alcTStatsTerminalAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alcTStatsTerminalAddress.setStatus("mandatory")


class _AlcTStatsConnState_Type(Integer32):
    """Custom type alcTStatsConnState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              100)
        )
    )
    namedValues = NamedValues(
        *(("connecting", 3),
          ("inactive", 4),
          ("na", 100),
          ("offline", 2),
          ("online", 1),
          ("pending", 5))
    )


_AlcTStatsConnState_Type.__name__ = "Integer32"
_AlcTStatsConnState_Object = MibTableColumn
alcTStatsConnState = _AlcTStatsConnState_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 28, 3, 1, 4),
    _AlcTStatsConnState_Type()
)
alcTStatsConnState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alcTStatsConnState.setStatus("mandatory")
_AlcTStatsALCMesgsIn_Type = Counter32
_AlcTStatsALCMesgsIn_Object = MibTableColumn
alcTStatsALCMesgsIn = _AlcTStatsALCMesgsIn_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 28, 3, 1, 5),
    _AlcTStatsALCMesgsIn_Type()
)
alcTStatsALCMesgsIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alcTStatsALCMesgsIn.setStatus("mandatory")
_AlcTStatsALCMesgsOut_Type = Counter32
_AlcTStatsALCMesgsOut_Object = MibTableColumn
alcTStatsALCMesgsOut = _AlcTStatsALCMesgsOut_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 28, 3, 1, 6),
    _AlcTStatsALCMesgsOut_Type()
)
alcTStatsALCMesgsOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alcTStatsALCMesgsOut.setStatus("mandatory")
_AlcTStatsX25MesgsIn_Type = Counter32
_AlcTStatsX25MesgsIn_Object = MibTableColumn
alcTStatsX25MesgsIn = _AlcTStatsX25MesgsIn_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 28, 3, 1, 7),
    _AlcTStatsX25MesgsIn_Type()
)
alcTStatsX25MesgsIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alcTStatsX25MesgsIn.setStatus("mandatory")
_AlcTStatsX25MesgsOut_Type = Counter32
_AlcTStatsX25MesgsOut_Object = MibTableColumn
alcTStatsX25MesgsOut = _AlcTStatsX25MesgsOut_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 28, 3, 1, 8),
    _AlcTStatsX25MesgsOut_Type()
)
alcTStatsX25MesgsOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alcTStatsX25MesgsOut.setStatus("mandatory")
_AlcTStatsALCCharsIn_Type = Counter32
_AlcTStatsALCCharsIn_Object = MibTableColumn
alcTStatsALCCharsIn = _AlcTStatsALCCharsIn_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 28, 3, 1, 9),
    _AlcTStatsALCCharsIn_Type()
)
alcTStatsALCCharsIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alcTStatsALCCharsIn.setStatus("mandatory")
_AlcTStatsALCCharsOut_Type = Counter32
_AlcTStatsALCCharsOut_Object = MibTableColumn
alcTStatsALCCharsOut = _AlcTStatsALCCharsOut_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 28, 3, 1, 10),
    _AlcTStatsALCCharsOut_Type()
)
alcTStatsALCCharsOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alcTStatsALCCharsOut.setStatus("mandatory")
_AlcTStatsX25CharsIn_Type = Counter32
_AlcTStatsX25CharsIn_Object = MibTableColumn
alcTStatsX25CharsIn = _AlcTStatsX25CharsIn_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 28, 3, 1, 11),
    _AlcTStatsX25CharsIn_Type()
)
alcTStatsX25CharsIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alcTStatsX25CharsIn.setStatus("mandatory")
_AlcTStatsX25CharsOut_Type = Counter32
_AlcTStatsX25CharsOut_Object = MibTableColumn
alcTStatsX25CharsOut = _AlcTStatsX25CharsOut_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 28, 3, 1, 12),
    _AlcTStatsX25CharsOut_Type()
)
alcTStatsX25CharsOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alcTStatsX25CharsOut.setStatus("mandatory")
_AlcTStatsALCDiscardedMesgsEntityDown_Type = Counter32
_AlcTStatsALCDiscardedMesgsEntityDown_Object = MibTableColumn
alcTStatsALCDiscardedMesgsEntityDown = _AlcTStatsALCDiscardedMesgsEntityDown_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 28, 3, 1, 13),
    _AlcTStatsALCDiscardedMesgsEntityDown_Type()
)
alcTStatsALCDiscardedMesgsEntityDown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alcTStatsALCDiscardedMesgsEntityDown.setStatus("mandatory")
_AlcTStatsX25DiscardedMesgsEntityDown_Type = Counter32
_AlcTStatsX25DiscardedMesgsEntityDown_Object = MibTableColumn
alcTStatsX25DiscardedMesgsEntityDown = _AlcTStatsX25DiscardedMesgsEntityDown_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 28, 3, 1, 14),
    _AlcTStatsX25DiscardedMesgsEntityDown_Type()
)
alcTStatsX25DiscardedMesgsEntityDown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alcTStatsX25DiscardedMesgsEntityDown.setStatus("mandatory")
_AlcTStatsX25DiscardedMesgsBadALCAddr_Type = Counter32
_AlcTStatsX25DiscardedMesgsBadALCAddr_Object = MibTableColumn
alcTStatsX25DiscardedMesgsBadALCAddr = _AlcTStatsX25DiscardedMesgsBadALCAddr_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 28, 3, 1, 15),
    _AlcTStatsX25DiscardedMesgsBadALCAddr_Type()
)
alcTStatsX25DiscardedMesgsBadALCAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alcTStatsX25DiscardedMesgsBadALCAddr.setStatus("mandatory")
_AlcTStatsX25DiscardedMesgsBadHeader_Type = Counter32
_AlcTStatsX25DiscardedMesgsBadHeader_Object = MibTableColumn
alcTStatsX25DiscardedMesgsBadHeader = _AlcTStatsX25DiscardedMesgsBadHeader_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 28, 3, 1, 16),
    _AlcTStatsX25DiscardedMesgsBadHeader_Type()
)
alcTStatsX25DiscardedMesgsBadHeader.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alcTStatsX25DiscardedMesgsBadHeader.setStatus("mandatory")
_AlcTStatsX25DiscardedMesgsTooLong_Type = Counter32
_AlcTStatsX25DiscardedMesgsTooLong_Object = MibTableColumn
alcTStatsX25DiscardedMesgsTooLong = _AlcTStatsX25DiscardedMesgsTooLong_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 28, 3, 1, 17),
    _AlcTStatsX25DiscardedMesgsTooLong_Type()
)
alcTStatsX25DiscardedMesgsTooLong.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alcTStatsX25DiscardedMesgsTooLong.setStatus("mandatory")
_AlcTStatsALCDiscardedMesgsQFull_Type = Counter32
_AlcTStatsALCDiscardedMesgsQFull_Object = MibTableColumn
alcTStatsALCDiscardedMesgsQFull = _AlcTStatsALCDiscardedMesgsQFull_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 28, 3, 1, 18),
    _AlcTStatsALCDiscardedMesgsQFull_Type()
)
alcTStatsALCDiscardedMesgsQFull.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alcTStatsALCDiscardedMesgsQFull.setStatus("mandatory")
_AlcTStatsX25DiscardedMesgsQFull_Type = Counter32
_AlcTStatsX25DiscardedMesgsQFull_Object = MibTableColumn
alcTStatsX25DiscardedMesgsQFull = _AlcTStatsX25DiscardedMesgsQFull_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 28, 3, 1, 19),
    _AlcTStatsX25DiscardedMesgsQFull_Type()
)
alcTStatsX25DiscardedMesgsQFull.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alcTStatsX25DiscardedMesgsQFull.setStatus("mandatory")
_AlcTStatsCurrTxALCQSize_Type = Integer32
_AlcTStatsCurrTxALCQSize_Object = MibTableColumn
alcTStatsCurrTxALCQSize = _AlcTStatsCurrTxALCQSize_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 28, 3, 1, 20),
    _AlcTStatsCurrTxALCQSize_Type()
)
alcTStatsCurrTxALCQSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alcTStatsCurrTxALCQSize.setStatus("mandatory")
_AlcTStatsCurrTxX25QSize_Type = Integer32
_AlcTStatsCurrTxX25QSize_Object = MibTableColumn
alcTStatsCurrTxX25QSize = _AlcTStatsCurrTxX25QSize_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 28, 3, 1, 21),
    _AlcTStatsCurrTxX25QSize_Type()
)
alcTStatsCurrTxX25QSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alcTStatsCurrTxX25QSize.setStatus("mandatory")
_AlcTStatsMaxTxALCQSize_Type = Integer32
_AlcTStatsMaxTxALCQSize_Object = MibTableColumn
alcTStatsMaxTxALCQSize = _AlcTStatsMaxTxALCQSize_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 28, 3, 1, 22),
    _AlcTStatsMaxTxALCQSize_Type()
)
alcTStatsMaxTxALCQSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alcTStatsMaxTxALCQSize.setStatus("mandatory")
_AlcTStatsMaxTxX25QSize_Type = Integer32
_AlcTStatsMaxTxX25QSize_Object = MibTableColumn
alcTStatsMaxTxX25QSize = _AlcTStatsMaxTxX25QSize_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 28, 3, 1, 23),
    _AlcTStatsMaxTxX25QSize_Type()
)
alcTStatsMaxTxX25QSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alcTStatsMaxTxX25QSize.setStatus("mandatory")
_Cdx6500Controls_ObjectIdentity = ObjectIdentity
cdx6500Controls = _Cdx6500Controls_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 4)
)
_Cdx6500ContALC_ObjectIdentity = ObjectIdentity
cdx6500ContALC = _Cdx6500ContALC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 4, 10)
)
_Cdx6500ContALCPortTable_Object = MibTable
cdx6500ContALCPortTable = _Cdx6500ContALCPortTable_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 4, 10, 1)
)
if mibBuilder.loadTexts:
    cdx6500ContALCPortTable.setStatus("mandatory")
_Cdx6500ContALCPortEntry_Object = MibTableRow
cdx6500ContALCPortEntry = _Cdx6500ContALCPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 4, 10, 1, 1)
)
cdx6500ContALCPortEntry.setIndexNames(
    (0, "ALC-OPT-MIB", "alcPContPortNumber"),
)
if mibBuilder.loadTexts:
    cdx6500ContALCPortEntry.setStatus("mandatory")


class _AlcPContPortNumber_Type(Integer32):
    """Custom type alcPContPortNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 54),
    )


_AlcPContPortNumber_Type.__name__ = "Integer32"
_AlcPContPortNumber_Object = MibTableColumn
alcPContPortNumber = _AlcPContPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 4, 10, 1, 1, 1),
    _AlcPContPortNumber_Type()
)
alcPContPortNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alcPContPortNumber.setStatus("mandatory")


class _AlcPContPortBoot_Type(Integer32):
    """Custom type alcPContPortBoot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("boot", 1),
          ("noBoot", 2))
    )


_AlcPContPortBoot_Type.__name__ = "Integer32"
_AlcPContPortBoot_Object = MibTableColumn
alcPContPortBoot = _AlcPContPortBoot_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 4, 10, 1, 1, 2),
    _AlcPContPortBoot_Type()
)
alcPContPortBoot.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    alcPContPortBoot.setStatus("mandatory")


class _AlcPContPortEnable_Type(Integer32):
    """Custom type alcPContPortEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("noEnable", 2))
    )


_AlcPContPortEnable_Type.__name__ = "Integer32"
_AlcPContPortEnable_Object = MibTableColumn
alcPContPortEnable = _AlcPContPortEnable_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 4, 10, 1, 1, 3),
    _AlcPContPortEnable_Type()
)
alcPContPortEnable.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    alcPContPortEnable.setStatus("mandatory")


class _AlcPContPortDisable_Type(Integer32):
    """Custom type alcPContPortDisable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("noDisable", 2))
    )


_AlcPContPortDisable_Type.__name__ = "Integer32"
_AlcPContPortDisable_Object = MibTableColumn
alcPContPortDisable = _AlcPContPortDisable_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 4, 10, 1, 1, 4),
    _AlcPContPortDisable_Type()
)
alcPContPortDisable.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    alcPContPortDisable.setStatus("mandatory")
_Cdx6500ContALCInterchangeTable_Object = MibTable
cdx6500ContALCInterchangeTable = _Cdx6500ContALCInterchangeTable_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 4, 10, 2)
)
if mibBuilder.loadTexts:
    cdx6500ContALCInterchangeTable.setStatus("mandatory")
_Cdx6500ContALCInterchangeEntry_Object = MibTableRow
cdx6500ContALCInterchangeEntry = _Cdx6500ContALCInterchangeEntry_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 4, 10, 2, 1)
)
cdx6500ContALCInterchangeEntry.setIndexNames(
    (0, "ALC-OPT-MIB", "alcIContPortNumber"),
    (0, "ALC-OPT-MIB", "alcIContInterchangeAddress"),
)
if mibBuilder.loadTexts:
    cdx6500ContALCInterchangeEntry.setStatus("mandatory")


class _AlcIContPortNumber_Type(Integer32):
    """Custom type alcIContPortNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 54),
    )


_AlcIContPortNumber_Type.__name__ = "Integer32"
_AlcIContPortNumber_Object = MibTableColumn
alcIContPortNumber = _AlcIContPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 4, 10, 2, 1, 1),
    _AlcIContPortNumber_Type()
)
alcIContPortNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alcIContPortNumber.setStatus("mandatory")


class _AlcIContInterchangeAddress_Type(OctetString):
    """Custom type alcIContInterchangeAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_AlcIContInterchangeAddress_Type.__name__ = "OctetString"
_AlcIContInterchangeAddress_Object = MibTableColumn
alcIContInterchangeAddress = _AlcIContInterchangeAddress_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 4, 10, 2, 1, 2),
    _AlcIContInterchangeAddress_Type()
)
alcIContInterchangeAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alcIContInterchangeAddress.setStatus("mandatory")


class _AlcIContInterchangeBoot_Type(Integer32):
    """Custom type alcIContInterchangeBoot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("boot", 1),
          ("noBoot", 2))
    )


_AlcIContInterchangeBoot_Type.__name__ = "Integer32"
_AlcIContInterchangeBoot_Object = MibTableColumn
alcIContInterchangeBoot = _AlcIContInterchangeBoot_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 4, 10, 2, 1, 3),
    _AlcIContInterchangeBoot_Type()
)
alcIContInterchangeBoot.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    alcIContInterchangeBoot.setStatus("mandatory")


class _AlcIContInterchangeEnable_Type(Integer32):
    """Custom type alcIContInterchangeEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("noEnable", 2))
    )


_AlcIContInterchangeEnable_Type.__name__ = "Integer32"
_AlcIContInterchangeEnable_Object = MibTableColumn
alcIContInterchangeEnable = _AlcIContInterchangeEnable_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 4, 10, 2, 1, 4),
    _AlcIContInterchangeEnable_Type()
)
alcIContInterchangeEnable.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    alcIContInterchangeEnable.setStatus("mandatory")


class _AlcIContInterchangeDisable_Type(Integer32):
    """Custom type alcIContInterchangeDisable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("noDisable", 2))
    )


_AlcIContInterchangeDisable_Type.__name__ = "Integer32"
_AlcIContInterchangeDisable_Object = MibTableColumn
alcIContInterchangeDisable = _AlcIContInterchangeDisable_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 4, 10, 2, 1, 5),
    _AlcIContInterchangeDisable_Type()
)
alcIContInterchangeDisable.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    alcIContInterchangeDisable.setStatus("mandatory")
_Cdx6500ContALCTerminalTable_Object = MibTable
cdx6500ContALCTerminalTable = _Cdx6500ContALCTerminalTable_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 4, 10, 3)
)
if mibBuilder.loadTexts:
    cdx6500ContALCTerminalTable.setStatus("mandatory")
_Cdx6500ContALCTerminalEntry_Object = MibTableRow
cdx6500ContALCTerminalEntry = _Cdx6500ContALCTerminalEntry_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 4, 10, 3, 1)
)
cdx6500ContALCTerminalEntry.setIndexNames(
    (0, "ALC-OPT-MIB", "alcTContPortNumber"),
    (0, "ALC-OPT-MIB", "alcTContInterchangeAddress"),
    (0, "ALC-OPT-MIB", "alcTContTerminalAddress"),
)
if mibBuilder.loadTexts:
    cdx6500ContALCTerminalEntry.setStatus("mandatory")


class _AlcTContPortNumber_Type(Integer32):
    """Custom type alcTContPortNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 54),
    )


_AlcTContPortNumber_Type.__name__ = "Integer32"
_AlcTContPortNumber_Object = MibTableColumn
alcTContPortNumber = _AlcTContPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 4, 10, 3, 1, 1),
    _AlcTContPortNumber_Type()
)
alcTContPortNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alcTContPortNumber.setStatus("mandatory")


class _AlcTContInterchangeAddress_Type(OctetString):
    """Custom type alcTContInterchangeAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_AlcTContInterchangeAddress_Type.__name__ = "OctetString"
_AlcTContInterchangeAddress_Object = MibTableColumn
alcTContInterchangeAddress = _AlcTContInterchangeAddress_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 4, 10, 3, 1, 2),
    _AlcTContInterchangeAddress_Type()
)
alcTContInterchangeAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alcTContInterchangeAddress.setStatus("mandatory")


class _AlcTContTerminalAddress_Type(OctetString):
    """Custom type alcTContTerminalAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_AlcTContTerminalAddress_Type.__name__ = "OctetString"
_AlcTContTerminalAddress_Object = MibTableColumn
alcTContTerminalAddress = _AlcTContTerminalAddress_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 4, 10, 3, 1, 3),
    _AlcTContTerminalAddress_Type()
)
alcTContTerminalAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alcTContTerminalAddress.setStatus("mandatory")


class _AlcTContTerminalBoot_Type(Integer32):
    """Custom type alcTContTerminalBoot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("boot", 1),
          ("noBoot", 2))
    )


_AlcTContTerminalBoot_Type.__name__ = "Integer32"
_AlcTContTerminalBoot_Object = MibTableColumn
alcTContTerminalBoot = _AlcTContTerminalBoot_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 4, 10, 3, 1, 4),
    _AlcTContTerminalBoot_Type()
)
alcTContTerminalBoot.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    alcTContTerminalBoot.setStatus("mandatory")


class _AlcTContTerminalEnable_Type(Integer32):
    """Custom type alcTContTerminalEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("noEnable", 2))
    )


_AlcTContTerminalEnable_Type.__name__ = "Integer32"
_AlcTContTerminalEnable_Object = MibTableColumn
alcTContTerminalEnable = _AlcTContTerminalEnable_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 4, 10, 3, 1, 5),
    _AlcTContTerminalEnable_Type()
)
alcTContTerminalEnable.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    alcTContTerminalEnable.setStatus("mandatory")


class _AlcTContTerminalDisable_Type(Integer32):
    """Custom type alcTContTerminalDisable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("noDisable", 2))
    )


_AlcTContTerminalDisable_Type.__name__ = "Integer32"
_AlcTContTerminalDisable_Object = MibTableColumn
alcTContTerminalDisable = _AlcTContTerminalDisable_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 4, 10, 3, 1, 6),
    _AlcTContTerminalDisable_Type()
)
alcTContTerminalDisable.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    alcTContTerminalDisable.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ALC-OPT-MIB",
    **{"DisplayString": DisplayString,
       "codex": codex,
       "cdxProductSpecific": cdxProductSpecific,
       "cdx6500": cdx6500,
       "cdx6500Configuration": cdx6500Configuration,
       "cdx6500CfgProtocolGroup": cdx6500CfgProtocolGroup,
       "cdx6500PCTPortProtocolGroup": cdx6500PCTPortProtocolGroup,
       "cdx6500PPCTALCCfgTable": cdx6500PPCTALCCfgTable,
       "cdx6500PPCTALCPortTable": cdx6500PPCTALCPortTable,
       "cdx6500PPCTALCPortEntry": cdx6500PPCTALCPortEntry,
       "alcPCfgPortNumber": alcPCfgPortNumber,
       "alcPCfgPortType": alcPCfgPortType,
       "alcPCfgSubtype": alcPCfgSubtype,
       "alcPCfgPortControl": alcPCfgPortControl,
       "alcPCfgClockSource": alcPCfgClockSource,
       "alcPCfgClockSpeed": alcPCfgClockSpeed,
       "alcPCfgPollDelayTimer": alcPCfgPollDelayTimer,
       "alcPCfgHostTimeout": alcPCfgHostTimeout,
       "alcPCfgMaxMesgSize": alcPCfgMaxMesgSize,
       "alcPCfgMinIntrvlBetweenPolls": alcPCfgMinIntrvlBetweenPolls,
       "alcPCfgRtsCtsTimeout": alcPCfgRtsCtsTimeout,
       "alcPCfgLeadPadChar": alcPCfgLeadPadChar,
       "alcPCfgNumLeadPadChars": alcPCfgNumLeadPadChars,
       "alcPCfgTrailPadChar": alcPCfgTrailPadChar,
       "alcPCfgNumTrailPadChars": alcPCfgNumTrailPadChars,
       "alcPCfgALCLineOptions": alcPCfgALCLineOptions,
       "alcPCfgConnType": alcPCfgConnType,
       "alcPCfgAcallMnemonic": alcPCfgAcallMnemonic,
       "alcPCfgCallingAddress": alcPCfgCallingAddress,
       "alcPCfgCUD": alcPCfgCUD,
       "alcPCfgNumOfBuffers": alcPCfgNumOfBuffers,
       "alcPCfgInHeader": alcPCfgInHeader,
       "alcPCfgOutHeader": alcPCfgOutHeader,
       "alcPCfgReconnectTimeout": alcPCfgReconnectTimeout,
       "alcPCfgInactivityTimeout": alcPCfgInactivityTimeout,
       "alcPCfgDebounceTimeout": alcPCfgDebounceTimeout,
       "alcPCfgParity": alcPCfgParity,
       "alcPCfgConnOptions": alcPCfgConnOptions,
       "alcPCfgAvailableMesg": alcPCfgAvailableMesg,
       "alcPCfgUnavailableMesg": alcPCfgUnavailableMesg,
       "cdx6500PPCTALCInterchangeTable": cdx6500PPCTALCInterchangeTable,
       "cdx6500PPCTALCInterchangeEntry": cdx6500PPCTALCInterchangeEntry,
       "alcICfgPortNumber": alcICfgPortNumber,
       "alcICfgInterchangeAddress": alcICfgInterchangeAddress,
       "alcICfgOptionOnInvalidCCC": alcICfgOptionOnInvalidCCC,
       "alcICfgGenTerminalAddress": alcICfgGenTerminalAddress,
       "alcICfgHostTimeout": alcICfgHostTimeout,
       "alcICfgMaxComponentsPerFrame": alcICfgMaxComponentsPerFrame,
       "alcICfgFastPollCycleCount": alcICfgFastPollCycleCount,
       "alcICfgSlowPollCycleCount": alcICfgSlowPollCycleCount,
       "alcICfgN1Counter": alcICfgN1Counter,
       "alcICfgN2Counter": alcICfgN2Counter,
       "alcICfgT1Timeout": alcICfgT1Timeout,
       "alcICfgT2Timeout": alcICfgT2Timeout,
       "alcICfgReenterMessage": alcICfgReenterMessage,
       "alcICfgStartMessage": alcICfgStartMessage,
       "alcICfgStopMessage": alcICfgStopMessage,
       "alcICfgOptions": alcICfgOptions,
       "alcICfgValidTAList": alcICfgValidTAList,
       "alcICfgConnType": alcICfgConnType,
       "alcICfgAcallMnemonic": alcICfgAcallMnemonic,
       "alcICfgCallingAddress": alcICfgCallingAddress,
       "alcICfgCUD": alcICfgCUD,
       "alcICfgNumOfBuffers": alcICfgNumOfBuffers,
       "alcICfgInHeader": alcICfgInHeader,
       "alcICfgOutHeader": alcICfgOutHeader,
       "alcICfgReconnectTimeout": alcICfgReconnectTimeout,
       "alcICfgInactivityTimeout": alcICfgInactivityTimeout,
       "alcICfgDebounceTimeout": alcICfgDebounceTimeout,
       "alcICfgParity": alcICfgParity,
       "alcICfgConnOptions": alcICfgConnOptions,
       "alcICfgAvailableMesg": alcICfgAvailableMesg,
       "alcICfgUnavailableMesg": alcICfgUnavailableMesg,
       "cdx6500PPCTALCTerminalTable": cdx6500PPCTALCTerminalTable,
       "cdx6500PPCTALCTerminalEntry": cdx6500PPCTALCTerminalEntry,
       "alcTCfgPortNumber": alcTCfgPortNumber,
       "alcTCfgInterchangeAddress": alcTCfgInterchangeAddress,
       "alcTCfgTerminalAddress": alcTCfgTerminalAddress,
       "alcTCfgConnType": alcTCfgConnType,
       "alcTCfgAcallMnemonic": alcTCfgAcallMnemonic,
       "alcTCfgCallingAddress": alcTCfgCallingAddress,
       "alcTCfgCUD": alcTCfgCUD,
       "alcTCfgNumOfBuffers": alcTCfgNumOfBuffers,
       "alcTCfgInHeader": alcTCfgInHeader,
       "alcTCfgOutHeader": alcTCfgOutHeader,
       "alcTCfgReconnectTimeout": alcTCfgReconnectTimeout,
       "alcTCfgInactivityTimeout": alcTCfgInactivityTimeout,
       "alcTCfgDebounceTimeout": alcTCfgDebounceTimeout,
       "alcTCfgParity": alcTCfgParity,
       "alcTCfgConnOptions": alcTCfgConnOptions,
       "alcTCfgAvailableMesg": alcTCfgAvailableMesg,
       "alcTCfgUnavailableMesg": alcTCfgUnavailableMesg,
       "cdx6500Statistics": cdx6500Statistics,
       "cdx6500StatProtocolGroup": cdx6500StatProtocolGroup,
       "cdx6500PSTPortProtocolGroup": cdx6500PSTPortProtocolGroup,
       "cdx6500PPSTALCStatsTable": cdx6500PPSTALCStatsTable,
       "cdx6500PPSTALCPortTable": cdx6500PPSTALCPortTable,
       "cdx6500PPSTALCPortEntry": cdx6500PPSTALCPortEntry,
       "alcPStatsPortNumber": alcPStatsPortNumber,
       "alcPStatsPortType": alcPStatsPortType,
       "alcPStatsPortState": alcPStatsPortState,
       "alcPStatsFramesIn": alcPStatsFramesIn,
       "alcPStatsFramesOut": alcPStatsFramesOut,
       "alcPStatsDataMesgsIn": alcPStatsDataMesgsIn,
       "alcPStatsDataMesgsOut": alcPStatsDataMesgsOut,
       "alcPStatsCharsIn": alcPStatsCharsIn,
       "alcPStatsCharsOut": alcPStatsCharsOut,
       "alcPStatsPolls": alcPStatsPolls,
       "alcPStatsGAs": alcPStatsGAs,
       "alcPStatsResets": alcPStatsResets,
       "alcPStatsDiscardBadIAIn": alcPStatsDiscardBadIAIn,
       "alcPStatsDiscardBadIAOut": alcPStatsDiscardBadIAOut,
       "alcPStatsMaxQSizeOut": alcPStatsMaxQSizeOut,
       "alcPStatsCCCErrors": alcPStatsCCCErrors,
       "alcPStatsSignalLosses": alcPStatsSignalLosses,
       "alcPStatsOverlengthFrames": alcPStatsOverlengthFrames,
       "alcPStatsPortStatus": alcPStatsPortStatus,
       "alcPStatsConnState": alcPStatsConnState,
       "alcPStatsALCMesgsIn": alcPStatsALCMesgsIn,
       "alcPStatsALCMesgsOut": alcPStatsALCMesgsOut,
       "alcPStatsX25MesgsIn": alcPStatsX25MesgsIn,
       "alcPStatsX25MesgsOut": alcPStatsX25MesgsOut,
       "alcPStatsALCCharsIn": alcPStatsALCCharsIn,
       "alcPStatsALCCharsOut": alcPStatsALCCharsOut,
       "alcPStatsX25CharsIn": alcPStatsX25CharsIn,
       "alcPStatsX25CharsOut": alcPStatsX25CharsOut,
       "alcPStatsALCDiscardedMesgsEntityDown": alcPStatsALCDiscardedMesgsEntityDown,
       "alcPStatsX25DiscardedMesgsEntityDown": alcPStatsX25DiscardedMesgsEntityDown,
       "alcPStatsX25DiscardedMesgsBadALCAddr": alcPStatsX25DiscardedMesgsBadALCAddr,
       "alcPStatsX25DiscardedMesgsBadHeader": alcPStatsX25DiscardedMesgsBadHeader,
       "alcPStatsX25DiscardedMesgsTooLong": alcPStatsX25DiscardedMesgsTooLong,
       "alcPStatsALCDiscardedMesgsQFull": alcPStatsALCDiscardedMesgsQFull,
       "alcPStatsX25DiscardedMesgsQFull": alcPStatsX25DiscardedMesgsQFull,
       "alcPStatsCurrTxALCQSize": alcPStatsCurrTxALCQSize,
       "alcPStatsCurrTxX25QSize": alcPStatsCurrTxX25QSize,
       "alcPStatsMaxTxALCQSize": alcPStatsMaxTxALCQSize,
       "alcPStatsMaxTxX25QSize": alcPStatsMaxTxX25QSize,
       "cdx6500PPSTALCInterchangeTable": cdx6500PPSTALCInterchangeTable,
       "cdx6500PPSTALCInterchangeEntry": cdx6500PPSTALCInterchangeEntry,
       "alcIStatsPortNumber": alcIStatsPortNumber,
       "alcIStatsInterchangeAddress": alcIStatsInterchangeAddress,
       "alcIStatsInterchangeState": alcIStatsInterchangeState,
       "alcIStatsFramesIn": alcIStatsFramesIn,
       "alcIStatsFramesOut": alcIStatsFramesOut,
       "alcIStatsDataMesgsIn": alcIStatsDataMesgsIn,
       "alcIStatsDataMesgsOut": alcIStatsDataMesgsOut,
       "alcIStatsCharsIn": alcIStatsCharsIn,
       "alcIStatsCharsOut": alcIStatsCharsOut,
       "alcIStatsPolls": alcIStatsPolls,
       "alcIStatsGAs": alcIStatsGAs,
       "alcIStatsResets": alcIStatsResets,
       "alcIStatsDiscardBadTAIn": alcIStatsDiscardBadTAIn,
       "alcIStatsDiscardBadTAOut": alcIStatsDiscardBadTAOut,
       "alcIStatsDisabledIAIn": alcIStatsDisabledIAIn,
       "alcIStatsDisabledIAOut": alcIStatsDisabledIAOut,
       "alcIStatsMaxQSizeOut": alcIStatsMaxQSizeOut,
       "alcIStatsCCCErrors": alcIStatsCCCErrors,
       "alcIStatsT1Timeouts": alcIStatsT1Timeouts,
       "alcIStatsT2Timeouts": alcIStatsT2Timeouts,
       "alcIStatsConnState": alcIStatsConnState,
       "alcIStatsALCMesgsIn": alcIStatsALCMesgsIn,
       "alcIStatsALCMesgsOut": alcIStatsALCMesgsOut,
       "alcIStatsX25MesgsIn": alcIStatsX25MesgsIn,
       "alcIStatsX25MesgsOut": alcIStatsX25MesgsOut,
       "alcIStatsALCCharsIn": alcIStatsALCCharsIn,
       "alcIStatsALCCharsOut": alcIStatsALCCharsOut,
       "alcIStatsX25CharsIn": alcIStatsX25CharsIn,
       "alcIStatsX25CharsOut": alcIStatsX25CharsOut,
       "alcIStatsALCDiscardedMesgsEntityDown": alcIStatsALCDiscardedMesgsEntityDown,
       "alcIStatsX25DiscardedMesgsEntityDown": alcIStatsX25DiscardedMesgsEntityDown,
       "alcIStatsX25DiscardedMesgsBadALCAddr": alcIStatsX25DiscardedMesgsBadALCAddr,
       "alcIStatsX25DiscardedMesgsBadHeader": alcIStatsX25DiscardedMesgsBadHeader,
       "alcIStatsX25DiscardedMesgsTooLong": alcIStatsX25DiscardedMesgsTooLong,
       "alcIStatsALCDiscardedMesgsQFull": alcIStatsALCDiscardedMesgsQFull,
       "alcIStatsX25DiscardedMesgsQFull": alcIStatsX25DiscardedMesgsQFull,
       "alcIStatsCurrTxALCQSize": alcIStatsCurrTxALCQSize,
       "alcIStatsCurrTxX25QSize": alcIStatsCurrTxX25QSize,
       "alcIStatsMaxTxALCQSize": alcIStatsMaxTxALCQSize,
       "alcIStatsMaxTxX25QSize": alcIStatsMaxTxX25QSize,
       "cdx6500PPSTALCTerminalTable": cdx6500PPSTALCTerminalTable,
       "cdx6500PPSTALCTerminalEntry": cdx6500PPSTALCTerminalEntry,
       "alcTStatsPortNumber": alcTStatsPortNumber,
       "alcTStatsInterchangeAddress": alcTStatsInterchangeAddress,
       "alcTStatsTerminalAddress": alcTStatsTerminalAddress,
       "alcTStatsConnState": alcTStatsConnState,
       "alcTStatsALCMesgsIn": alcTStatsALCMesgsIn,
       "alcTStatsALCMesgsOut": alcTStatsALCMesgsOut,
       "alcTStatsX25MesgsIn": alcTStatsX25MesgsIn,
       "alcTStatsX25MesgsOut": alcTStatsX25MesgsOut,
       "alcTStatsALCCharsIn": alcTStatsALCCharsIn,
       "alcTStatsALCCharsOut": alcTStatsALCCharsOut,
       "alcTStatsX25CharsIn": alcTStatsX25CharsIn,
       "alcTStatsX25CharsOut": alcTStatsX25CharsOut,
       "alcTStatsALCDiscardedMesgsEntityDown": alcTStatsALCDiscardedMesgsEntityDown,
       "alcTStatsX25DiscardedMesgsEntityDown": alcTStatsX25DiscardedMesgsEntityDown,
       "alcTStatsX25DiscardedMesgsBadALCAddr": alcTStatsX25DiscardedMesgsBadALCAddr,
       "alcTStatsX25DiscardedMesgsBadHeader": alcTStatsX25DiscardedMesgsBadHeader,
       "alcTStatsX25DiscardedMesgsTooLong": alcTStatsX25DiscardedMesgsTooLong,
       "alcTStatsALCDiscardedMesgsQFull": alcTStatsALCDiscardedMesgsQFull,
       "alcTStatsX25DiscardedMesgsQFull": alcTStatsX25DiscardedMesgsQFull,
       "alcTStatsCurrTxALCQSize": alcTStatsCurrTxALCQSize,
       "alcTStatsCurrTxX25QSize": alcTStatsCurrTxX25QSize,
       "alcTStatsMaxTxALCQSize": alcTStatsMaxTxALCQSize,
       "alcTStatsMaxTxX25QSize": alcTStatsMaxTxX25QSize,
       "cdx6500Controls": cdx6500Controls,
       "cdx6500ContALC": cdx6500ContALC,
       "cdx6500ContALCPortTable": cdx6500ContALCPortTable,
       "cdx6500ContALCPortEntry": cdx6500ContALCPortEntry,
       "alcPContPortNumber": alcPContPortNumber,
       "alcPContPortBoot": alcPContPortBoot,
       "alcPContPortEnable": alcPContPortEnable,
       "alcPContPortDisable": alcPContPortDisable,
       "cdx6500ContALCInterchangeTable": cdx6500ContALCInterchangeTable,
       "cdx6500ContALCInterchangeEntry": cdx6500ContALCInterchangeEntry,
       "alcIContPortNumber": alcIContPortNumber,
       "alcIContInterchangeAddress": alcIContInterchangeAddress,
       "alcIContInterchangeBoot": alcIContInterchangeBoot,
       "alcIContInterchangeEnable": alcIContInterchangeEnable,
       "alcIContInterchangeDisable": alcIContInterchangeDisable,
       "cdx6500ContALCTerminalTable": cdx6500ContALCTerminalTable,
       "cdx6500ContALCTerminalEntry": cdx6500ContALCTerminalEntry,
       "alcTContPortNumber": alcTContPortNumber,
       "alcTContInterchangeAddress": alcTContInterchangeAddress,
       "alcTContTerminalAddress": alcTContTerminalAddress,
       "alcTContTerminalBoot": alcTContTerminalBoot,
       "alcTContTerminalEnable": alcTContTerminalEnable,
       "alcTContTerminalDisable": alcTContTerminalDisable}
)
