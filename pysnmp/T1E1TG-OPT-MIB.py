# SNMP MIB module (T1E1TG-OPT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/T1E1TG-OPT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:00:44 2024
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
_Cdx6500PCTT1E1TGPortTable_Object = MibTable
cdx6500PCTT1E1TGPortTable = _Cdx6500PCTT1E1TGPortTable_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 34)
)
if mibBuilder.loadTexts:
    cdx6500PCTT1E1TGPortTable.setStatus("mandatory")
_Cdx6500PCTT1E1TGPortEntry_Object = MibTableRow
cdx6500PCTT1E1TGPortEntry = _Cdx6500PCTT1E1TGPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 34, 1)
)
cdx6500PCTT1E1TGPortEntry.setIndexNames(
    (0, "T1E1TG-OPT-MIB", "cdx6500T1E1TGCfgPortNumber"),
)
if mibBuilder.loadTexts:
    cdx6500PCTT1E1TGPortEntry.setStatus("mandatory")
_Cdx6500T1E1TGCfgPortNumber_Type = Integer32
_Cdx6500T1E1TGCfgPortNumber_Object = MibTableColumn
cdx6500T1E1TGCfgPortNumber = _Cdx6500T1E1TGCfgPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 34, 1, 1),
    _Cdx6500T1E1TGCfgPortNumber_Type()
)
cdx6500T1E1TGCfgPortNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500T1E1TGCfgPortNumber.setStatus("mandatory")
_Cdx6500T1E1TGCfgInterfaceType_Type = DisplayString
_Cdx6500T1E1TGCfgInterfaceType_Object = MibTableColumn
cdx6500T1E1TGCfgInterfaceType = _Cdx6500T1E1TGCfgInterfaceType_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 34, 1, 2),
    _Cdx6500T1E1TGCfgInterfaceType_Type()
)
cdx6500T1E1TGCfgInterfaceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500T1E1TGCfgInterfaceType.setStatus("mandatory")


class _Cdx6500T1E1TGCfgFormat_Type(Integer32):
    """Custom type cdx6500T1E1TGCfgFormat based on Integer32"""
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
        *(("vg-format-ccs", 4),
          ("vg-format-channelize", 2),
          ("vg-format-frational", 1),
          ("vg-format-isdn", 3))
    )


_Cdx6500T1E1TGCfgFormat_Type.__name__ = "Integer32"
_Cdx6500T1E1TGCfgFormat_Object = MibTableColumn
cdx6500T1E1TGCfgFormat = _Cdx6500T1E1TGCfgFormat_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 34, 1, 3),
    _Cdx6500T1E1TGCfgFormat_Type()
)
cdx6500T1E1TGCfgFormat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500T1E1TGCfgFormat.setStatus("mandatory")


class _Cdx6500T1E1TGCfgSwitchType_Type(Integer32):
    """Custom type cdx6500T1E1TGCfgSwitchType based on Integer32"""
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
        *(("dms100", 4),
          ("ess5", 3),
          ("etsi", 7),
          ("ni2", 2),
          ("ntt", 5),
          ("qsig", 8),
          ("tso14", 6),
          ("unspecified", 1))
    )


_Cdx6500T1E1TGCfgSwitchType_Type.__name__ = "Integer32"
_Cdx6500T1E1TGCfgSwitchType_Object = MibTableColumn
cdx6500T1E1TGCfgSwitchType = _Cdx6500T1E1TGCfgSwitchType_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 34, 1, 4),
    _Cdx6500T1E1TGCfgSwitchType_Type()
)
cdx6500T1E1TGCfgSwitchType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500T1E1TGCfgSwitchType.setStatus("mandatory")


class _Cdx6500T1E1TGCfgUserNetworkSide_Type(Integer32):
    """Custom type cdx6500T1E1TGCfgUserNetworkSide based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("network", 2),
          ("user", 1))
    )


_Cdx6500T1E1TGCfgUserNetworkSide_Type.__name__ = "Integer32"
_Cdx6500T1E1TGCfgUserNetworkSide_Object = MibTableColumn
cdx6500T1E1TGCfgUserNetworkSide = _Cdx6500T1E1TGCfgUserNetworkSide_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 34, 1, 5),
    _Cdx6500T1E1TGCfgUserNetworkSide_Type()
)
cdx6500T1E1TGCfgUserNetworkSide.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500T1E1TGCfgUserNetworkSide.setStatus("mandatory")


class _Cdx6500T1E1TGCfgDirectBchannel_Type(Integer32):
    """Custom type cdx6500T1E1TGCfgDirectBchannel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("high-to-low", 1),
          ("low-to-high", 2))
    )


_Cdx6500T1E1TGCfgDirectBchannel_Type.__name__ = "Integer32"
_Cdx6500T1E1TGCfgDirectBchannel_Object = MibTableColumn
cdx6500T1E1TGCfgDirectBchannel = _Cdx6500T1E1TGCfgDirectBchannel_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 34, 1, 6),
    _Cdx6500T1E1TGCfgDirectBchannel_Type()
)
cdx6500T1E1TGCfgDirectBchannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500T1E1TGCfgDirectBchannel.setStatus("mandatory")


class _Cdx6500T1E1TGCfgBchNumScheme_Type(Integer32):
    """Custom type cdx6500T1E1TGCfgBchNumScheme based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("nb-1-30", 1),
          ("nb-1-31", 2))
    )


_Cdx6500T1E1TGCfgBchNumScheme_Type.__name__ = "Integer32"
_Cdx6500T1E1TGCfgBchNumScheme_Object = MibTableColumn
cdx6500T1E1TGCfgBchNumScheme = _Cdx6500T1E1TGCfgBchNumScheme_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 34, 1, 7),
    _Cdx6500T1E1TGCfgBchNumScheme_Type()
)
cdx6500T1E1TGCfgBchNumScheme.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500T1E1TGCfgBchNumScheme.setStatus("mandatory")
_Cdx6500T1E1TGCfgBchRange_Type = DisplayString
_Cdx6500T1E1TGCfgBchRange_Object = MibTableColumn
cdx6500T1E1TGCfgBchRange = _Cdx6500T1E1TGCfgBchRange_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 34, 1, 8),
    _Cdx6500T1E1TGCfgBchRange_Type()
)
cdx6500T1E1TGCfgBchRange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500T1E1TGCfgBchRange.setStatus("mandatory")
_Cdx6500T1E1TGCfgCallAddrReplace_Type = DisplayString
_Cdx6500T1E1TGCfgCallAddrReplace_Object = MibTableColumn
cdx6500T1E1TGCfgCallAddrReplace = _Cdx6500T1E1TGCfgCallAddrReplace_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 34, 1, 9),
    _Cdx6500T1E1TGCfgCallAddrReplace_Type()
)
cdx6500T1E1TGCfgCallAddrReplace.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500T1E1TGCfgCallAddrReplace.setStatus("mandatory")
_Cdx6500T1E1TGCfgIsdnQsigOpt_Type = DisplayString
_Cdx6500T1E1TGCfgIsdnQsigOpt_Object = MibTableColumn
cdx6500T1E1TGCfgIsdnQsigOpt = _Cdx6500T1E1TGCfgIsdnQsigOpt_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 34, 1, 10),
    _Cdx6500T1E1TGCfgIsdnQsigOpt_Type()
)
cdx6500T1E1TGCfgIsdnQsigOpt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500T1E1TGCfgIsdnQsigOpt.setStatus("mandatory")
_Cdx6500T1E1TGCfgFilteredIE_Type = DisplayString
_Cdx6500T1E1TGCfgFilteredIE_Object = MibTableColumn
cdx6500T1E1TGCfgFilteredIE = _Cdx6500T1E1TGCfgFilteredIE_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 34, 1, 11),
    _Cdx6500T1E1TGCfgFilteredIE_Type()
)
cdx6500T1E1TGCfgFilteredIE.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500T1E1TGCfgFilteredIE.setStatus("mandatory")
_Cdx6500T1E1TGCfgReplIsdnQsig_Type = DisplayString
_Cdx6500T1E1TGCfgReplIsdnQsig_Object = MibTableColumn
cdx6500T1E1TGCfgReplIsdnQsig = _Cdx6500T1E1TGCfgReplIsdnQsig_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 34, 1, 12),
    _Cdx6500T1E1TGCfgReplIsdnQsig_Type()
)
cdx6500T1E1TGCfgReplIsdnQsig.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500T1E1TGCfgReplIsdnQsig.setStatus("mandatory")


class _Cdx6500T1E1TGCfgCallPartyNumType_Type(Integer32):
    """Custom type cdx6500T1E1TGCfgCallPartyNumType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              5)
        )
    )
    namedValues = NamedValues(
        *(("international", 2),
          ("national", 3),
          ("subscriber", 5),
          ("unknown", 1))
    )


_Cdx6500T1E1TGCfgCallPartyNumType_Type.__name__ = "Integer32"
_Cdx6500T1E1TGCfgCallPartyNumType_Object = MibTableColumn
cdx6500T1E1TGCfgCallPartyNumType = _Cdx6500T1E1TGCfgCallPartyNumType_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 34, 1, 13),
    _Cdx6500T1E1TGCfgCallPartyNumType_Type()
)
cdx6500T1E1TGCfgCallPartyNumType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500T1E1TGCfgCallPartyNumType.setStatus("mandatory")


class _Cdx6500T1E1TGCfgCallPartyNumPlan_Type(Integer32):
    """Custom type cdx6500T1E1TGCfgCallPartyNumPlan based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              10)
        )
    )
    namedValues = NamedValues(
        *(("isdn", 2),
          ("private", 10),
          ("telephony", 3),
          ("unknown", 1))
    )


_Cdx6500T1E1TGCfgCallPartyNumPlan_Type.__name__ = "Integer32"
_Cdx6500T1E1TGCfgCallPartyNumPlan_Object = MibTableColumn
cdx6500T1E1TGCfgCallPartyNumPlan = _Cdx6500T1E1TGCfgCallPartyNumPlan_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 34, 1, 14),
    _Cdx6500T1E1TGCfgCallPartyNumPlan_Type()
)
cdx6500T1E1TGCfgCallPartyNumPlan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500T1E1TGCfgCallPartyNumPlan.setStatus("mandatory")


class _Cdx6500T1E1TGCfgLineFramingType_Type(Integer32):
    """Custom type cdx6500T1E1TGCfgLineFramingType based on Integer32"""
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
        *(("e1", 3),
          ("e1crc", 4),
          ("e1crc-febe", 5),
          ("esf", 2),
          ("sf", 1))
    )


_Cdx6500T1E1TGCfgLineFramingType_Type.__name__ = "Integer32"
_Cdx6500T1E1TGCfgLineFramingType_Object = MibTableColumn
cdx6500T1E1TGCfgLineFramingType = _Cdx6500T1E1TGCfgLineFramingType_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 34, 1, 15),
    _Cdx6500T1E1TGCfgLineFramingType_Type()
)
cdx6500T1E1TGCfgLineFramingType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500T1E1TGCfgLineFramingType.setStatus("mandatory")


class _Cdx6500T1E1TGCfgLineCoding_Type(Integer32):
    """Custom type cdx6500T1E1TGCfgLineCoding based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("ami", 1),
          ("b8zs", 2),
          ("hdb3", 3))
    )


_Cdx6500T1E1TGCfgLineCoding_Type.__name__ = "Integer32"
_Cdx6500T1E1TGCfgLineCoding_Object = MibTableColumn
cdx6500T1E1TGCfgLineCoding = _Cdx6500T1E1TGCfgLineCoding_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 34, 1, 16),
    _Cdx6500T1E1TGCfgLineCoding_Type()
)
cdx6500T1E1TGCfgLineCoding.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500T1E1TGCfgLineCoding.setStatus("mandatory")


class _Cdx6500T1E1TGCfgClockPriority_Type(Integer32):
    """Custom type cdx6500T1E1TGCfgClockPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("high", 1),
          ("low", 3),
          ("medium", 2))
    )


_Cdx6500T1E1TGCfgClockPriority_Type.__name__ = "Integer32"
_Cdx6500T1E1TGCfgClockPriority_Object = MibTableColumn
cdx6500T1E1TGCfgClockPriority = _Cdx6500T1E1TGCfgClockPriority_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 34, 1, 17),
    _Cdx6500T1E1TGCfgClockPriority_Type()
)
cdx6500T1E1TGCfgClockPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500T1E1TGCfgClockPriority.setStatus("mandatory")


class _Cdx6500T1E1TGCfgLineImpedance_Type(Integer32):
    """Custom type cdx6500T1E1TGCfgLineImpedance based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ohms-120", 1),
          ("ohms-75", 2))
    )


_Cdx6500T1E1TGCfgLineImpedance_Type.__name__ = "Integer32"
_Cdx6500T1E1TGCfgLineImpedance_Object = MibTableColumn
cdx6500T1E1TGCfgLineImpedance = _Cdx6500T1E1TGCfgLineImpedance_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 34, 1, 18),
    _Cdx6500T1E1TGCfgLineImpedance_Type()
)
cdx6500T1E1TGCfgLineImpedance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500T1E1TGCfgLineImpedance.setStatus("mandatory")
_Cdx6500T1E1TGCfgLineBuildOut_Type = Integer32
_Cdx6500T1E1TGCfgLineBuildOut_Object = MibTableColumn
cdx6500T1E1TGCfgLineBuildOut = _Cdx6500T1E1TGCfgLineBuildOut_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 34, 1, 19),
    _Cdx6500T1E1TGCfgLineBuildOut_Type()
)
cdx6500T1E1TGCfgLineBuildOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500T1E1TGCfgLineBuildOut.setStatus("mandatory")


class _Cdx6500T1E1TGCfgRecvSense_Type(Integer32):
    """Custom type cdx6500T1E1TGCfgRecvSense based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("high", 2),
          ("low", 1))
    )


_Cdx6500T1E1TGCfgRecvSense_Type.__name__ = "Integer32"
_Cdx6500T1E1TGCfgRecvSense_Object = MibTableColumn
cdx6500T1E1TGCfgRecvSense = _Cdx6500T1E1TGCfgRecvSense_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 34, 1, 20),
    _Cdx6500T1E1TGCfgRecvSense_Type()
)
cdx6500T1E1TGCfgRecvSense.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500T1E1TGCfgRecvSense.setStatus("mandatory")


class _Cdx6500T1E1TGCfgFacilityDataLink_Type(Integer32):
    """Custom type cdx6500T1E1TGCfgFacilityDataLink based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("ansi", 3),
          ("att", 2),
          ("none", 1))
    )


_Cdx6500T1E1TGCfgFacilityDataLink_Type.__name__ = "Integer32"
_Cdx6500T1E1TGCfgFacilityDataLink_Object = MibTableColumn
cdx6500T1E1TGCfgFacilityDataLink = _Cdx6500T1E1TGCfgFacilityDataLink_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 34, 1, 21),
    _Cdx6500T1E1TGCfgFacilityDataLink_Type()
)
cdx6500T1E1TGCfgFacilityDataLink.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500T1E1TGCfgFacilityDataLink.setStatus("mandatory")


class _Cdx6500T1E1TGCfgV54RecvRLBK_Type(Integer32):
    """Custom type cdx6500T1E1TGCfgV54RecvRLBK based on Integer32"""
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


_Cdx6500T1E1TGCfgV54RecvRLBK_Type.__name__ = "Integer32"
_Cdx6500T1E1TGCfgV54RecvRLBK_Object = MibTableColumn
cdx6500T1E1TGCfgV54RecvRLBK = _Cdx6500T1E1TGCfgV54RecvRLBK_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 34, 1, 22),
    _Cdx6500T1E1TGCfgV54RecvRLBK_Type()
)
cdx6500T1E1TGCfgV54RecvRLBK.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500T1E1TGCfgV54RecvRLBK.setStatus("mandatory")


class _Cdx6500T1E1TGCfgThresholdValueLES_Type(Integer32):
    """Custom type cdx6500T1E1TGCfgThresholdValueLES based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_Cdx6500T1E1TGCfgThresholdValueLES_Type.__name__ = "Integer32"
_Cdx6500T1E1TGCfgThresholdValueLES_Object = MibTableColumn
cdx6500T1E1TGCfgThresholdValueLES = _Cdx6500T1E1TGCfgThresholdValueLES_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 34, 1, 23),
    _Cdx6500T1E1TGCfgThresholdValueLES_Type()
)
cdx6500T1E1TGCfgThresholdValueLES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500T1E1TGCfgThresholdValueLES.setStatus("mandatory")


class _Cdx6500T1E1TGCfgThresholdValueLCV_Type(Integer32):
    """Custom type cdx6500T1E1TGCfgThresholdValueLCV based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_Cdx6500T1E1TGCfgThresholdValueLCV_Type.__name__ = "Integer32"
_Cdx6500T1E1TGCfgThresholdValueLCV_Object = MibTableColumn
cdx6500T1E1TGCfgThresholdValueLCV = _Cdx6500T1E1TGCfgThresholdValueLCV_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 34, 1, 24),
    _Cdx6500T1E1TGCfgThresholdValueLCV_Type()
)
cdx6500T1E1TGCfgThresholdValueLCV.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500T1E1TGCfgThresholdValueLCV.setStatus("mandatory")


class _Cdx6500T1E1TGCfgThresholdValuePCV_Type(Integer32):
    """Custom type cdx6500T1E1TGCfgThresholdValuePCV based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_Cdx6500T1E1TGCfgThresholdValuePCV_Type.__name__ = "Integer32"
_Cdx6500T1E1TGCfgThresholdValuePCV_Object = MibTableColumn
cdx6500T1E1TGCfgThresholdValuePCV = _Cdx6500T1E1TGCfgThresholdValuePCV_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 34, 1, 25),
    _Cdx6500T1E1TGCfgThresholdValuePCV_Type()
)
cdx6500T1E1TGCfgThresholdValuePCV.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500T1E1TGCfgThresholdValuePCV.setStatus("mandatory")


class _Cdx6500T1E1TGCfgThresholdValueCSS_Type(Integer32):
    """Custom type cdx6500T1E1TGCfgThresholdValueCSS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_Cdx6500T1E1TGCfgThresholdValueCSS_Type.__name__ = "Integer32"
_Cdx6500T1E1TGCfgThresholdValueCSS_Object = MibTableColumn
cdx6500T1E1TGCfgThresholdValueCSS = _Cdx6500T1E1TGCfgThresholdValueCSS_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 34, 1, 26),
    _Cdx6500T1E1TGCfgThresholdValueCSS_Type()
)
cdx6500T1E1TGCfgThresholdValueCSS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500T1E1TGCfgThresholdValueCSS.setStatus("mandatory")


class _Cdx6500T1E1TGCfgThresholdValueES_Type(Integer32):
    """Custom type cdx6500T1E1TGCfgThresholdValueES based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_Cdx6500T1E1TGCfgThresholdValueES_Type.__name__ = "Integer32"
_Cdx6500T1E1TGCfgThresholdValueES_Object = MibTableColumn
cdx6500T1E1TGCfgThresholdValueES = _Cdx6500T1E1TGCfgThresholdValueES_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 34, 1, 27),
    _Cdx6500T1E1TGCfgThresholdValueES_Type()
)
cdx6500T1E1TGCfgThresholdValueES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500T1E1TGCfgThresholdValueES.setStatus("mandatory")


class _Cdx6500T1E1TGCfgThresholdValueBES_Type(Integer32):
    """Custom type cdx6500T1E1TGCfgThresholdValueBES based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_Cdx6500T1E1TGCfgThresholdValueBES_Type.__name__ = "Integer32"
_Cdx6500T1E1TGCfgThresholdValueBES_Object = MibTableColumn
cdx6500T1E1TGCfgThresholdValueBES = _Cdx6500T1E1TGCfgThresholdValueBES_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 34, 1, 28),
    _Cdx6500T1E1TGCfgThresholdValueBES_Type()
)
cdx6500T1E1TGCfgThresholdValueBES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500T1E1TGCfgThresholdValueBES.setStatus("mandatory")


class _Cdx6500T1E1TGCfgThresholdValueSES_Type(Integer32):
    """Custom type cdx6500T1E1TGCfgThresholdValueSES based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_Cdx6500T1E1TGCfgThresholdValueSES_Type.__name__ = "Integer32"
_Cdx6500T1E1TGCfgThresholdValueSES_Object = MibTableColumn
cdx6500T1E1TGCfgThresholdValueSES = _Cdx6500T1E1TGCfgThresholdValueSES_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 34, 1, 29),
    _Cdx6500T1E1TGCfgThresholdValueSES_Type()
)
cdx6500T1E1TGCfgThresholdValueSES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500T1E1TGCfgThresholdValueSES.setStatus("mandatory")


class _Cdx6500T1E1TGCfgThresholdValueSEFS_Type(Integer32):
    """Custom type cdx6500T1E1TGCfgThresholdValueSEFS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_Cdx6500T1E1TGCfgThresholdValueSEFS_Type.__name__ = "Integer32"
_Cdx6500T1E1TGCfgThresholdValueSEFS_Object = MibTableColumn
cdx6500T1E1TGCfgThresholdValueSEFS = _Cdx6500T1E1TGCfgThresholdValueSEFS_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 34, 1, 30),
    _Cdx6500T1E1TGCfgThresholdValueSEFS_Type()
)
cdx6500T1E1TGCfgThresholdValueSEFS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500T1E1TGCfgThresholdValueSEFS.setStatus("mandatory")


class _Cdx6500T1E1TGCfgThresholdValueUAS_Type(Integer32):
    """Custom type cdx6500T1E1TGCfgThresholdValueUAS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_Cdx6500T1E1TGCfgThresholdValueUAS_Type.__name__ = "Integer32"
_Cdx6500T1E1TGCfgThresholdValueUAS_Object = MibTableColumn
cdx6500T1E1TGCfgThresholdValueUAS = _Cdx6500T1E1TGCfgThresholdValueUAS_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 34, 1, 31),
    _Cdx6500T1E1TGCfgThresholdValueUAS_Type()
)
cdx6500T1E1TGCfgThresholdValueUAS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500T1E1TGCfgThresholdValueUAS.setStatus("mandatory")
_Cdx6500CfgGeneralGroup_ObjectIdentity = ObjectIdentity
cdx6500CfgGeneralGroup = _Cdx6500CfgGeneralGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 2)
)
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
_Cdx6500PSTT1E1TGPortTable_ObjectIdentity = ObjectIdentity
cdx6500PSTT1E1TGPortTable = _Cdx6500PSTT1E1TGPortTable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 35)
)
_Cdx6500PSTT1E1TGTable_Object = MibTable
cdx6500PSTT1E1TGTable = _Cdx6500PSTT1E1TGTable_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 35, 1)
)
if mibBuilder.loadTexts:
    cdx6500PSTT1E1TGTable.setStatus("mandatory")
_Cdx6500PSTT1E1TGEntry_Object = MibTableRow
cdx6500PSTT1E1TGEntry = _Cdx6500PSTT1E1TGEntry_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 35, 1, 1)
)
cdx6500PSTT1E1TGEntry.setIndexNames(
    (0, "T1E1TG-OPT-MIB", "cdx6500T1E1TGStatPortNumber"),
)
if mibBuilder.loadTexts:
    cdx6500PSTT1E1TGEntry.setStatus("mandatory")
_Cdx6500T1E1TGStatPortNumber_Type = Integer32
_Cdx6500T1E1TGStatPortNumber_Object = MibTableColumn
cdx6500T1E1TGStatPortNumber = _Cdx6500T1E1TGStatPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 35, 1, 1, 1),
    _Cdx6500T1E1TGStatPortNumber_Type()
)
cdx6500T1E1TGStatPortNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500T1E1TGStatPortNumber.setStatus("mandatory")
_Cdx6500T1E1TGStatInterfaceType_Type = DisplayString
_Cdx6500T1E1TGStatInterfaceType_Object = MibTableColumn
cdx6500T1E1TGStatInterfaceType = _Cdx6500T1E1TGStatInterfaceType_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 35, 1, 1, 2),
    _Cdx6500T1E1TGStatInterfaceType_Type()
)
cdx6500T1E1TGStatInterfaceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500T1E1TGStatInterfaceType.setStatus("mandatory")
_Cdx6500T1E1TGStatTimeSinceLastReset_Type = DisplayString
_Cdx6500T1E1TGStatTimeSinceLastReset_Object = MibTableColumn
cdx6500T1E1TGStatTimeSinceLastReset = _Cdx6500T1E1TGStatTimeSinceLastReset_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 35, 1, 1, 3),
    _Cdx6500T1E1TGStatTimeSinceLastReset_Type()
)
cdx6500T1E1TGStatTimeSinceLastReset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500T1E1TGStatTimeSinceLastReset.setStatus("mandatory")
_Cdx6500T1E1TGStatAlarmState_Type = DisplayString
_Cdx6500T1E1TGStatAlarmState_Object = MibTableColumn
cdx6500T1E1TGStatAlarmState = _Cdx6500T1E1TGStatAlarmState_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 35, 1, 1, 4),
    _Cdx6500T1E1TGStatAlarmState_Type()
)
cdx6500T1E1TGStatAlarmState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500T1E1TGStatAlarmState.setStatus("mandatory")
_Cdx6500PSTT1E1TGStatTotal24HoursReportTable_Object = MibTable
cdx6500PSTT1E1TGStatTotal24HoursReportTable = _Cdx6500PSTT1E1TGStatTotal24HoursReportTable_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 35, 2)
)
if mibBuilder.loadTexts:
    cdx6500PSTT1E1TGStatTotal24HoursReportTable.setStatus("mandatory")
_Cdx6500PSTT1E1TGStatTotal24HoursReportEntry_Object = MibTableRow
cdx6500PSTT1E1TGStatTotal24HoursReportEntry = _Cdx6500PSTT1E1TGStatTotal24HoursReportEntry_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 35, 2, 1)
)
cdx6500PSTT1E1TGStatTotal24HoursReportEntry.setIndexNames(
    (0, "T1E1TG-OPT-MIB", "cdx6500PSTT1E1TGStatTotal24HoursReportPortNumber"),
)
if mibBuilder.loadTexts:
    cdx6500PSTT1E1TGStatTotal24HoursReportEntry.setStatus("mandatory")
_Cdx6500T1E1TGStatTotal24HoursReportPortNumber_Type = Integer32
_Cdx6500T1E1TGStatTotal24HoursReportPortNumber_Object = MibTableColumn
cdx6500T1E1TGStatTotal24HoursReportPortNumber = _Cdx6500T1E1TGStatTotal24HoursReportPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 35, 2, 1, 1),
    _Cdx6500T1E1TGStatTotal24HoursReportPortNumber_Type()
)
cdx6500T1E1TGStatTotal24HoursReportPortNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500T1E1TGStatTotal24HoursReportPortNumber.setStatus("mandatory")
_Cdx6500T1E1TGStatTotal24HoursReportLES_Type = Gauge32
_Cdx6500T1E1TGStatTotal24HoursReportLES_Object = MibTableColumn
cdx6500T1E1TGStatTotal24HoursReportLES = _Cdx6500T1E1TGStatTotal24HoursReportLES_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 35, 2, 1, 2),
    _Cdx6500T1E1TGStatTotal24HoursReportLES_Type()
)
cdx6500T1E1TGStatTotal24HoursReportLES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500T1E1TGStatTotal24HoursReportLES.setStatus("mandatory")
_Cdx6500T1E1TGStatTotal24HoursReportLCV_Type = Gauge32
_Cdx6500T1E1TGStatTotal24HoursReportLCV_Object = MibTableColumn
cdx6500T1E1TGStatTotal24HoursReportLCV = _Cdx6500T1E1TGStatTotal24HoursReportLCV_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 35, 2, 1, 3),
    _Cdx6500T1E1TGStatTotal24HoursReportLCV_Type()
)
cdx6500T1E1TGStatTotal24HoursReportLCV.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500T1E1TGStatTotal24HoursReportLCV.setStatus("mandatory")
_Cdx6500T1E1TGStatTotal24HoursReportPCV_Type = Gauge32
_Cdx6500T1E1TGStatTotal24HoursReportPCV_Object = MibTableColumn
cdx6500T1E1TGStatTotal24HoursReportPCV = _Cdx6500T1E1TGStatTotal24HoursReportPCV_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 35, 2, 1, 4),
    _Cdx6500T1E1TGStatTotal24HoursReportPCV_Type()
)
cdx6500T1E1TGStatTotal24HoursReportPCV.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500T1E1TGStatTotal24HoursReportPCV.setStatus("mandatory")
_Cdx6500T1E1TGStatTotal24HoursReportCSS_Type = Gauge32
_Cdx6500T1E1TGStatTotal24HoursReportCSS_Object = MibTableColumn
cdx6500T1E1TGStatTotal24HoursReportCSS = _Cdx6500T1E1TGStatTotal24HoursReportCSS_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 35, 2, 1, 5),
    _Cdx6500T1E1TGStatTotal24HoursReportCSS_Type()
)
cdx6500T1E1TGStatTotal24HoursReportCSS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500T1E1TGStatTotal24HoursReportCSS.setStatus("mandatory")
_Cdx6500T1E1TGStatTotal24HoursReportES_Type = Gauge32
_Cdx6500T1E1TGStatTotal24HoursReportES_Object = MibTableColumn
cdx6500T1E1TGStatTotal24HoursReportES = _Cdx6500T1E1TGStatTotal24HoursReportES_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 35, 2, 1, 6),
    _Cdx6500T1E1TGStatTotal24HoursReportES_Type()
)
cdx6500T1E1TGStatTotal24HoursReportES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500T1E1TGStatTotal24HoursReportES.setStatus("mandatory")
_Cdx6500T1E1TGStatTotal24HoursReportBES_Type = Gauge32
_Cdx6500T1E1TGStatTotal24HoursReportBES_Object = MibTableColumn
cdx6500T1E1TGStatTotal24HoursReportBES = _Cdx6500T1E1TGStatTotal24HoursReportBES_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 35, 2, 1, 7),
    _Cdx6500T1E1TGStatTotal24HoursReportBES_Type()
)
cdx6500T1E1TGStatTotal24HoursReportBES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500T1E1TGStatTotal24HoursReportBES.setStatus("mandatory")
_Cdx6500T1E1TGStatTotal24HoursReportSES_Type = Gauge32
_Cdx6500T1E1TGStatTotal24HoursReportSES_Object = MibTableColumn
cdx6500T1E1TGStatTotal24HoursReportSES = _Cdx6500T1E1TGStatTotal24HoursReportSES_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 35, 2, 1, 8),
    _Cdx6500T1E1TGStatTotal24HoursReportSES_Type()
)
cdx6500T1E1TGStatTotal24HoursReportSES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500T1E1TGStatTotal24HoursReportSES.setStatus("mandatory")
_Cdx6500T1E1TGStatTotal24HoursReportSEFS_Type = Gauge32
_Cdx6500T1E1TGStatTotal24HoursReportSEFS_Object = MibTableColumn
cdx6500T1E1TGStatTotal24HoursReportSEFS = _Cdx6500T1E1TGStatTotal24HoursReportSEFS_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 35, 2, 1, 9),
    _Cdx6500T1E1TGStatTotal24HoursReportSEFS_Type()
)
cdx6500T1E1TGStatTotal24HoursReportSEFS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500T1E1TGStatTotal24HoursReportSEFS.setStatus("mandatory")
_Cdx6500T1E1TGStatTotal24HoursReportUAS_Type = Gauge32
_Cdx6500T1E1TGStatTotal24HoursReportUAS_Object = MibTableColumn
cdx6500T1E1TGStatTotal24HoursReportUAS = _Cdx6500T1E1TGStatTotal24HoursReportUAS_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 35, 2, 1, 10),
    _Cdx6500T1E1TGStatTotal24HoursReportUAS_Type()
)
cdx6500T1E1TGStatTotal24HoursReportUAS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500T1E1TGStatTotal24HoursReportUAS.setStatus("mandatory")
_Cdx6500PSTT1E1TGStatCurrent15MinutesReportTable_Object = MibTable
cdx6500PSTT1E1TGStatCurrent15MinutesReportTable = _Cdx6500PSTT1E1TGStatCurrent15MinutesReportTable_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 35, 3)
)
if mibBuilder.loadTexts:
    cdx6500PSTT1E1TGStatCurrent15MinutesReportTable.setStatus("mandatory")
_Cdx6500PSTT1E1TGStatCurrent15MinutesReportEntry_Object = MibTableRow
cdx6500PSTT1E1TGStatCurrent15MinutesReportEntry = _Cdx6500PSTT1E1TGStatCurrent15MinutesReportEntry_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 35, 3, 1)
)
cdx6500PSTT1E1TGStatCurrent15MinutesReportEntry.setIndexNames(
    (0, "T1E1TG-OPT-MIB", "cdx6500T1E1TGStatCurrent15MinutesReportPortNumber"),
)
if mibBuilder.loadTexts:
    cdx6500PSTT1E1TGStatCurrent15MinutesReportEntry.setStatus("mandatory")
_Cdx6500T1E1TGStatCurrent15MinutesReportPortNumber_Type = Integer32
_Cdx6500T1E1TGStatCurrent15MinutesReportPortNumber_Object = MibTableColumn
cdx6500T1E1TGStatCurrent15MinutesReportPortNumber = _Cdx6500T1E1TGStatCurrent15MinutesReportPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 35, 3, 1, 1),
    _Cdx6500T1E1TGStatCurrent15MinutesReportPortNumber_Type()
)
cdx6500T1E1TGStatCurrent15MinutesReportPortNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500T1E1TGStatCurrent15MinutesReportPortNumber.setStatus("mandatory")
_Cdx6500T1E1TGStatCurrent15MinutesReportTimeElapsed_Type = Integer32
_Cdx6500T1E1TGStatCurrent15MinutesReportTimeElapsed_Object = MibTableColumn
cdx6500T1E1TGStatCurrent15MinutesReportTimeElapsed = _Cdx6500T1E1TGStatCurrent15MinutesReportTimeElapsed_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 35, 3, 1, 2),
    _Cdx6500T1E1TGStatCurrent15MinutesReportTimeElapsed_Type()
)
cdx6500T1E1TGStatCurrent15MinutesReportTimeElapsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500T1E1TGStatCurrent15MinutesReportTimeElapsed.setStatus("mandatory")
_Cdx6500T1E1TGStatCurrent15MinutesReportLES_Type = Gauge32
_Cdx6500T1E1TGStatCurrent15MinutesReportLES_Object = MibTableColumn
cdx6500T1E1TGStatCurrent15MinutesReportLES = _Cdx6500T1E1TGStatCurrent15MinutesReportLES_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 35, 3, 1, 3),
    _Cdx6500T1E1TGStatCurrent15MinutesReportLES_Type()
)
cdx6500T1E1TGStatCurrent15MinutesReportLES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500T1E1TGStatCurrent15MinutesReportLES.setStatus("mandatory")
_Cdx6500T1E1TGStatCurrent15MinutesReportLCV_Type = Gauge32
_Cdx6500T1E1TGStatCurrent15MinutesReportLCV_Object = MibTableColumn
cdx6500T1E1TGStatCurrent15MinutesReportLCV = _Cdx6500T1E1TGStatCurrent15MinutesReportLCV_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 35, 3, 1, 4),
    _Cdx6500T1E1TGStatCurrent15MinutesReportLCV_Type()
)
cdx6500T1E1TGStatCurrent15MinutesReportLCV.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500T1E1TGStatCurrent15MinutesReportLCV.setStatus("mandatory")
_Cdx6500T1E1TGStatCurrent15MinutesReportPCV_Type = Gauge32
_Cdx6500T1E1TGStatCurrent15MinutesReportPCV_Object = MibTableColumn
cdx6500T1E1TGStatCurrent15MinutesReportPCV = _Cdx6500T1E1TGStatCurrent15MinutesReportPCV_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 35, 3, 1, 5),
    _Cdx6500T1E1TGStatCurrent15MinutesReportPCV_Type()
)
cdx6500T1E1TGStatCurrent15MinutesReportPCV.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500T1E1TGStatCurrent15MinutesReportPCV.setStatus("mandatory")
_Cdx6500T1E1TGStatCurrent15MinutesReportCSS_Type = Gauge32
_Cdx6500T1E1TGStatCurrent15MinutesReportCSS_Object = MibTableColumn
cdx6500T1E1TGStatCurrent15MinutesReportCSS = _Cdx6500T1E1TGStatCurrent15MinutesReportCSS_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 35, 3, 1, 6),
    _Cdx6500T1E1TGStatCurrent15MinutesReportCSS_Type()
)
cdx6500T1E1TGStatCurrent15MinutesReportCSS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500T1E1TGStatCurrent15MinutesReportCSS.setStatus("mandatory")
_Cdx6500T1E1TGStatCurrent15MinutesReportES_Type = Gauge32
_Cdx6500T1E1TGStatCurrent15MinutesReportES_Object = MibTableColumn
cdx6500T1E1TGStatCurrent15MinutesReportES = _Cdx6500T1E1TGStatCurrent15MinutesReportES_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 35, 3, 1, 7),
    _Cdx6500T1E1TGStatCurrent15MinutesReportES_Type()
)
cdx6500T1E1TGStatCurrent15MinutesReportES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500T1E1TGStatCurrent15MinutesReportES.setStatus("mandatory")
_Cdx6500T1E1TGStatCurrent15MinutesReportBES_Type = Gauge32
_Cdx6500T1E1TGStatCurrent15MinutesReportBES_Object = MibTableColumn
cdx6500T1E1TGStatCurrent15MinutesReportBES = _Cdx6500T1E1TGStatCurrent15MinutesReportBES_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 35, 3, 1, 8),
    _Cdx6500T1E1TGStatCurrent15MinutesReportBES_Type()
)
cdx6500T1E1TGStatCurrent15MinutesReportBES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500T1E1TGStatCurrent15MinutesReportBES.setStatus("mandatory")
_Cdx6500T1E1TGStatCurrent15MinutesReportSES_Type = Gauge32
_Cdx6500T1E1TGStatCurrent15MinutesReportSES_Object = MibTableColumn
cdx6500T1E1TGStatCurrent15MinutesReportSES = _Cdx6500T1E1TGStatCurrent15MinutesReportSES_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 35, 3, 1, 9),
    _Cdx6500T1E1TGStatCurrent15MinutesReportSES_Type()
)
cdx6500T1E1TGStatCurrent15MinutesReportSES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500T1E1TGStatCurrent15MinutesReportSES.setStatus("mandatory")
_Cdx6500T1E1TGStatCurrent15MinutesReportSEFS_Type = Gauge32
_Cdx6500T1E1TGStatCurrent15MinutesReportSEFS_Object = MibTableColumn
cdx6500T1E1TGStatCurrent15MinutesReportSEFS = _Cdx6500T1E1TGStatCurrent15MinutesReportSEFS_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 35, 3, 1, 10),
    _Cdx6500T1E1TGStatCurrent15MinutesReportSEFS_Type()
)
cdx6500T1E1TGStatCurrent15MinutesReportSEFS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500T1E1TGStatCurrent15MinutesReportSEFS.setStatus("mandatory")
_Cdx6500T1E1TGStatCurrent15MinutesReportUAS_Type = Gauge32
_Cdx6500T1E1TGStatCurrent15MinutesReportUAS_Object = MibScalar
cdx6500T1E1TGStatCurrent15MinutesReportUAS = _Cdx6500T1E1TGStatCurrent15MinutesReportUAS_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 35, 3, 1, 11),
    _Cdx6500T1E1TGStatCurrent15MinutesReportUAS_Type()
)
cdx6500T1E1TGStatCurrent15MinutesReportUAS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500T1E1TGStatCurrent15MinutesReportUAS.setStatus("mandatory")
_Cdx6500PSTT1E1TGStatIntervalReportTable_Object = MibTable
cdx6500PSTT1E1TGStatIntervalReportTable = _Cdx6500PSTT1E1TGStatIntervalReportTable_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 35, 4)
)
if mibBuilder.loadTexts:
    cdx6500PSTT1E1TGStatIntervalReportTable.setStatus("mandatory")
_Cdx6500PSTT1E1TGStatIntervalReportEntry_Object = MibTableRow
cdx6500PSTT1E1TGStatIntervalReportEntry = _Cdx6500PSTT1E1TGStatIntervalReportEntry_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 35, 4, 1)
)
cdx6500PSTT1E1TGStatIntervalReportEntry.setIndexNames(
    (0, "T1E1TG-OPT-MIB", "cdx6500T1E1TGStatIntervalReportPortNumber"),
    (0, "T1E1TG-OPT-MIB", "cdx6500T1E1TGStatIntervalNumber"),
)
if mibBuilder.loadTexts:
    cdx6500PSTT1E1TGStatIntervalReportEntry.setStatus("mandatory")
_Cdx6500T1E1TGStatIntervalReportPortNumber_Type = Integer32
_Cdx6500T1E1TGStatIntervalReportPortNumber_Object = MibTableColumn
cdx6500T1E1TGStatIntervalReportPortNumber = _Cdx6500T1E1TGStatIntervalReportPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 35, 4, 1, 1),
    _Cdx6500T1E1TGStatIntervalReportPortNumber_Type()
)
cdx6500T1E1TGStatIntervalReportPortNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500T1E1TGStatIntervalReportPortNumber.setStatus("mandatory")


class _Cdx6500T1E1TGStatIntervalNumber_Type(Integer32):
    """Custom type cdx6500T1E1TGStatIntervalNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 96),
    )


_Cdx6500T1E1TGStatIntervalNumber_Type.__name__ = "Integer32"
_Cdx6500T1E1TGStatIntervalNumber_Object = MibTableColumn
cdx6500T1E1TGStatIntervalNumber = _Cdx6500T1E1TGStatIntervalNumber_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 35, 4, 1, 2),
    _Cdx6500T1E1TGStatIntervalNumber_Type()
)
cdx6500T1E1TGStatIntervalNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500T1E1TGStatIntervalNumber.setStatus("mandatory")
_Cdx6500T1E1TGStatIntervalReportLES_Type = Gauge32
_Cdx6500T1E1TGStatIntervalReportLES_Object = MibTableColumn
cdx6500T1E1TGStatIntervalReportLES = _Cdx6500T1E1TGStatIntervalReportLES_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 35, 4, 1, 3),
    _Cdx6500T1E1TGStatIntervalReportLES_Type()
)
cdx6500T1E1TGStatIntervalReportLES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500T1E1TGStatIntervalReportLES.setStatus("mandatory")
_Cdx6500T1E1TGStatIntervalReportLCV_Type = Gauge32
_Cdx6500T1E1TGStatIntervalReportLCV_Object = MibTableColumn
cdx6500T1E1TGStatIntervalReportLCV = _Cdx6500T1E1TGStatIntervalReportLCV_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 35, 4, 1, 4),
    _Cdx6500T1E1TGStatIntervalReportLCV_Type()
)
cdx6500T1E1TGStatIntervalReportLCV.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500T1E1TGStatIntervalReportLCV.setStatus("mandatory")
_Cdx6500T1E1TGStatIntervalReportPCV_Type = Gauge32
_Cdx6500T1E1TGStatIntervalReportPCV_Object = MibTableColumn
cdx6500T1E1TGStatIntervalReportPCV = _Cdx6500T1E1TGStatIntervalReportPCV_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 35, 4, 1, 5),
    _Cdx6500T1E1TGStatIntervalReportPCV_Type()
)
cdx6500T1E1TGStatIntervalReportPCV.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500T1E1TGStatIntervalReportPCV.setStatus("mandatory")
_Cdx6500T1E1TGStatIntervalReportCSS_Type = Gauge32
_Cdx6500T1E1TGStatIntervalReportCSS_Object = MibTableColumn
cdx6500T1E1TGStatIntervalReportCSS = _Cdx6500T1E1TGStatIntervalReportCSS_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 35, 4, 1, 6),
    _Cdx6500T1E1TGStatIntervalReportCSS_Type()
)
cdx6500T1E1TGStatIntervalReportCSS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500T1E1TGStatIntervalReportCSS.setStatus("mandatory")
_Cdx6500T1E1TGStatIntervalReportES_Type = Gauge32
_Cdx6500T1E1TGStatIntervalReportES_Object = MibTableColumn
cdx6500T1E1TGStatIntervalReportES = _Cdx6500T1E1TGStatIntervalReportES_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 35, 4, 1, 7),
    _Cdx6500T1E1TGStatIntervalReportES_Type()
)
cdx6500T1E1TGStatIntervalReportES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500T1E1TGStatIntervalReportES.setStatus("mandatory")
_Cdx6500T1E1TGStatIntervalReportBES_Type = Gauge32
_Cdx6500T1E1TGStatIntervalReportBES_Object = MibTableColumn
cdx6500T1E1TGStatIntervalReportBES = _Cdx6500T1E1TGStatIntervalReportBES_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 35, 4, 1, 8),
    _Cdx6500T1E1TGStatIntervalReportBES_Type()
)
cdx6500T1E1TGStatIntervalReportBES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500T1E1TGStatIntervalReportBES.setStatus("mandatory")
_Cdx6500T1E1TGStatIntervalReportSES_Type = Gauge32
_Cdx6500T1E1TGStatIntervalReportSES_Object = MibTableColumn
cdx6500T1E1TGStatIntervalReportSES = _Cdx6500T1E1TGStatIntervalReportSES_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 35, 4, 1, 9),
    _Cdx6500T1E1TGStatIntervalReportSES_Type()
)
cdx6500T1E1TGStatIntervalReportSES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500T1E1TGStatIntervalReportSES.setStatus("mandatory")
_Cdx6500T1E1TGStatIntervalReportSEFS_Type = Gauge32
_Cdx6500T1E1TGStatIntervalReportSEFS_Object = MibTableColumn
cdx6500T1E1TGStatIntervalReportSEFS = _Cdx6500T1E1TGStatIntervalReportSEFS_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 35, 4, 1, 10),
    _Cdx6500T1E1TGStatIntervalReportSEFS_Type()
)
cdx6500T1E1TGStatIntervalReportSEFS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500T1E1TGStatIntervalReportSEFS.setStatus("mandatory")
_Cdx6500T1E1TGStatIntervalReportUAS_Type = Gauge32
_Cdx6500T1E1TGStatIntervalReportUAS_Object = MibScalar
cdx6500T1E1TGStatIntervalReportUAS = _Cdx6500T1E1TGStatIntervalReportUAS_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 35, 4, 1, 11),
    _Cdx6500T1E1TGStatIntervalReportUAS_Type()
)
cdx6500T1E1TGStatIntervalReportUAS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500T1E1TGStatIntervalReportUAS.setStatus("mandatory")
_Cdx6500Controls_ObjectIdentity = ObjectIdentity
cdx6500Controls = _Cdx6500Controls_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 4)
)
_Cdx6500ContT1E1TGTable_ObjectIdentity = ObjectIdentity
cdx6500ContT1E1TGTable = _Cdx6500ContT1E1TGTable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 4, 22)
)
_Cdx6500T1E1TGContEntry_Object = MibTableRow
cdx6500T1E1TGContEntry = _Cdx6500T1E1TGContEntry_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 4, 22, 1)
)
cdx6500T1E1TGContEntry.setIndexNames(
    (0, "T1E1TG-OPT-MIB", "t1e1tgContPortNumber"),
)
if mibBuilder.loadTexts:
    cdx6500T1E1TGContEntry.setStatus("mandatory")
_T1e1tgContPortNumber_Type = Integer32
_T1e1tgContPortNumber_Object = MibTableColumn
t1e1tgContPortNumber = _T1e1tgContPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 4, 22, 1, 1),
    _T1e1tgContPortNumber_Type()
)
t1e1tgContPortNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    t1e1tgContPortNumber.setStatus("mandatory")


class _T1e1tgContPortBoot_Type(Integer32):
    """Custom type t1e1tgContPortBoot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("boot", 1),
          ("noboot", 2))
    )


_T1e1tgContPortBoot_Type.__name__ = "Integer32"
_T1e1tgContPortBoot_Object = MibTableColumn
t1e1tgContPortBoot = _T1e1tgContPortBoot_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 4, 22, 1, 2),
    _T1e1tgContPortBoot_Type()
)
t1e1tgContPortBoot.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    t1e1tgContPortBoot.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "T1E1TG-OPT-MIB",
    **{"DisplayString": DisplayString,
       "codex": codex,
       "cdxProductSpecific": cdxProductSpecific,
       "cdx6500": cdx6500,
       "cdx6500Configuration": cdx6500Configuration,
       "cdx6500CfgProtocolGroup": cdx6500CfgProtocolGroup,
       "cdx6500PCTPortProtocolGroup": cdx6500PCTPortProtocolGroup,
       "cdx6500PCTT1E1TGPortTable": cdx6500PCTT1E1TGPortTable,
       "cdx6500PCTT1E1TGPortEntry": cdx6500PCTT1E1TGPortEntry,
       "cdx6500T1E1TGCfgPortNumber": cdx6500T1E1TGCfgPortNumber,
       "cdx6500T1E1TGCfgInterfaceType": cdx6500T1E1TGCfgInterfaceType,
       "cdx6500T1E1TGCfgFormat": cdx6500T1E1TGCfgFormat,
       "cdx6500T1E1TGCfgSwitchType": cdx6500T1E1TGCfgSwitchType,
       "cdx6500T1E1TGCfgUserNetworkSide": cdx6500T1E1TGCfgUserNetworkSide,
       "cdx6500T1E1TGCfgDirectBchannel": cdx6500T1E1TGCfgDirectBchannel,
       "cdx6500T1E1TGCfgBchNumScheme": cdx6500T1E1TGCfgBchNumScheme,
       "cdx6500T1E1TGCfgBchRange": cdx6500T1E1TGCfgBchRange,
       "cdx6500T1E1TGCfgCallAddrReplace": cdx6500T1E1TGCfgCallAddrReplace,
       "cdx6500T1E1TGCfgIsdnQsigOpt": cdx6500T1E1TGCfgIsdnQsigOpt,
       "cdx6500T1E1TGCfgFilteredIE": cdx6500T1E1TGCfgFilteredIE,
       "cdx6500T1E1TGCfgReplIsdnQsig": cdx6500T1E1TGCfgReplIsdnQsig,
       "cdx6500T1E1TGCfgCallPartyNumType": cdx6500T1E1TGCfgCallPartyNumType,
       "cdx6500T1E1TGCfgCallPartyNumPlan": cdx6500T1E1TGCfgCallPartyNumPlan,
       "cdx6500T1E1TGCfgLineFramingType": cdx6500T1E1TGCfgLineFramingType,
       "cdx6500T1E1TGCfgLineCoding": cdx6500T1E1TGCfgLineCoding,
       "cdx6500T1E1TGCfgClockPriority": cdx6500T1E1TGCfgClockPriority,
       "cdx6500T1E1TGCfgLineImpedance": cdx6500T1E1TGCfgLineImpedance,
       "cdx6500T1E1TGCfgLineBuildOut": cdx6500T1E1TGCfgLineBuildOut,
       "cdx6500T1E1TGCfgRecvSense": cdx6500T1E1TGCfgRecvSense,
       "cdx6500T1E1TGCfgFacilityDataLink": cdx6500T1E1TGCfgFacilityDataLink,
       "cdx6500T1E1TGCfgV54RecvRLBK": cdx6500T1E1TGCfgV54RecvRLBK,
       "cdx6500T1E1TGCfgThresholdValueLES": cdx6500T1E1TGCfgThresholdValueLES,
       "cdx6500T1E1TGCfgThresholdValueLCV": cdx6500T1E1TGCfgThresholdValueLCV,
       "cdx6500T1E1TGCfgThresholdValuePCV": cdx6500T1E1TGCfgThresholdValuePCV,
       "cdx6500T1E1TGCfgThresholdValueCSS": cdx6500T1E1TGCfgThresholdValueCSS,
       "cdx6500T1E1TGCfgThresholdValueES": cdx6500T1E1TGCfgThresholdValueES,
       "cdx6500T1E1TGCfgThresholdValueBES": cdx6500T1E1TGCfgThresholdValueBES,
       "cdx6500T1E1TGCfgThresholdValueSES": cdx6500T1E1TGCfgThresholdValueSES,
       "cdx6500T1E1TGCfgThresholdValueSEFS": cdx6500T1E1TGCfgThresholdValueSEFS,
       "cdx6500T1E1TGCfgThresholdValueUAS": cdx6500T1E1TGCfgThresholdValueUAS,
       "cdx6500CfgGeneralGroup": cdx6500CfgGeneralGroup,
       "cdx6500Statistics": cdx6500Statistics,
       "cdx6500StatProtocolGroup": cdx6500StatProtocolGroup,
       "cdx6500PSTPortProtocolGroup": cdx6500PSTPortProtocolGroup,
       "cdx6500PSTT1E1TGPortTable": cdx6500PSTT1E1TGPortTable,
       "cdx6500PSTT1E1TGTable": cdx6500PSTT1E1TGTable,
       "cdx6500PSTT1E1TGEntry": cdx6500PSTT1E1TGEntry,
       "cdx6500T1E1TGStatPortNumber": cdx6500T1E1TGStatPortNumber,
       "cdx6500T1E1TGStatInterfaceType": cdx6500T1E1TGStatInterfaceType,
       "cdx6500T1E1TGStatTimeSinceLastReset": cdx6500T1E1TGStatTimeSinceLastReset,
       "cdx6500T1E1TGStatAlarmState": cdx6500T1E1TGStatAlarmState,
       "cdx6500PSTT1E1TGStatTotal24HoursReportTable": cdx6500PSTT1E1TGStatTotal24HoursReportTable,
       "cdx6500PSTT1E1TGStatTotal24HoursReportEntry": cdx6500PSTT1E1TGStatTotal24HoursReportEntry,
       "cdx6500T1E1TGStatTotal24HoursReportPortNumber": cdx6500T1E1TGStatTotal24HoursReportPortNumber,
       "cdx6500T1E1TGStatTotal24HoursReportLES": cdx6500T1E1TGStatTotal24HoursReportLES,
       "cdx6500T1E1TGStatTotal24HoursReportLCV": cdx6500T1E1TGStatTotal24HoursReportLCV,
       "cdx6500T1E1TGStatTotal24HoursReportPCV": cdx6500T1E1TGStatTotal24HoursReportPCV,
       "cdx6500T1E1TGStatTotal24HoursReportCSS": cdx6500T1E1TGStatTotal24HoursReportCSS,
       "cdx6500T1E1TGStatTotal24HoursReportES": cdx6500T1E1TGStatTotal24HoursReportES,
       "cdx6500T1E1TGStatTotal24HoursReportBES": cdx6500T1E1TGStatTotal24HoursReportBES,
       "cdx6500T1E1TGStatTotal24HoursReportSES": cdx6500T1E1TGStatTotal24HoursReportSES,
       "cdx6500T1E1TGStatTotal24HoursReportSEFS": cdx6500T1E1TGStatTotal24HoursReportSEFS,
       "cdx6500T1E1TGStatTotal24HoursReportUAS": cdx6500T1E1TGStatTotal24HoursReportUAS,
       "cdx6500PSTT1E1TGStatCurrent15MinutesReportTable": cdx6500PSTT1E1TGStatCurrent15MinutesReportTable,
       "cdx6500PSTT1E1TGStatCurrent15MinutesReportEntry": cdx6500PSTT1E1TGStatCurrent15MinutesReportEntry,
       "cdx6500T1E1TGStatCurrent15MinutesReportPortNumber": cdx6500T1E1TGStatCurrent15MinutesReportPortNumber,
       "cdx6500T1E1TGStatCurrent15MinutesReportTimeElapsed": cdx6500T1E1TGStatCurrent15MinutesReportTimeElapsed,
       "cdx6500T1E1TGStatCurrent15MinutesReportLES": cdx6500T1E1TGStatCurrent15MinutesReportLES,
       "cdx6500T1E1TGStatCurrent15MinutesReportLCV": cdx6500T1E1TGStatCurrent15MinutesReportLCV,
       "cdx6500T1E1TGStatCurrent15MinutesReportPCV": cdx6500T1E1TGStatCurrent15MinutesReportPCV,
       "cdx6500T1E1TGStatCurrent15MinutesReportCSS": cdx6500T1E1TGStatCurrent15MinutesReportCSS,
       "cdx6500T1E1TGStatCurrent15MinutesReportES": cdx6500T1E1TGStatCurrent15MinutesReportES,
       "cdx6500T1E1TGStatCurrent15MinutesReportBES": cdx6500T1E1TGStatCurrent15MinutesReportBES,
       "cdx6500T1E1TGStatCurrent15MinutesReportSES": cdx6500T1E1TGStatCurrent15MinutesReportSES,
       "cdx6500T1E1TGStatCurrent15MinutesReportSEFS": cdx6500T1E1TGStatCurrent15MinutesReportSEFS,
       "cdx6500T1E1TGStatCurrent15MinutesReportUAS": cdx6500T1E1TGStatCurrent15MinutesReportUAS,
       "cdx6500PSTT1E1TGStatIntervalReportTable": cdx6500PSTT1E1TGStatIntervalReportTable,
       "cdx6500PSTT1E1TGStatIntervalReportEntry": cdx6500PSTT1E1TGStatIntervalReportEntry,
       "cdx6500T1E1TGStatIntervalReportPortNumber": cdx6500T1E1TGStatIntervalReportPortNumber,
       "cdx6500T1E1TGStatIntervalNumber": cdx6500T1E1TGStatIntervalNumber,
       "cdx6500T1E1TGStatIntervalReportLES": cdx6500T1E1TGStatIntervalReportLES,
       "cdx6500T1E1TGStatIntervalReportLCV": cdx6500T1E1TGStatIntervalReportLCV,
       "cdx6500T1E1TGStatIntervalReportPCV": cdx6500T1E1TGStatIntervalReportPCV,
       "cdx6500T1E1TGStatIntervalReportCSS": cdx6500T1E1TGStatIntervalReportCSS,
       "cdx6500T1E1TGStatIntervalReportES": cdx6500T1E1TGStatIntervalReportES,
       "cdx6500T1E1TGStatIntervalReportBES": cdx6500T1E1TGStatIntervalReportBES,
       "cdx6500T1E1TGStatIntervalReportSES": cdx6500T1E1TGStatIntervalReportSES,
       "cdx6500T1E1TGStatIntervalReportSEFS": cdx6500T1E1TGStatIntervalReportSEFS,
       "cdx6500T1E1TGStatIntervalReportUAS": cdx6500T1E1TGStatIntervalReportUAS,
       "cdx6500Controls": cdx6500Controls,
       "cdx6500ContT1E1TGTable": cdx6500ContT1E1TGTable,
       "cdx6500T1E1TGContEntry": cdx6500T1E1TGContEntry,
       "t1e1tgContPortNumber": t1e1tgContPortNumber,
       "t1e1tgContPortBoot": t1e1tgContPortBoot}
)
