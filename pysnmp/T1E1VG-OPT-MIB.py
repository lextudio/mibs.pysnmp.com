# SNMP MIB module (T1E1VG-OPT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/T1E1VG-OPT-MIB
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
_Cdx6500CfgGeneralGroup_ObjectIdentity = ObjectIdentity
cdx6500CfgGeneralGroup = _Cdx6500CfgGeneralGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 2)
)
_Cdx6500T1E1VGTable_Object = MibTable
cdx6500T1E1VGTable = _Cdx6500T1E1VGTable_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 2, 25)
)
if mibBuilder.loadTexts:
    cdx6500T1E1VGTable.setStatus("mandatory")
_Cdx6500T1E1VGEntry_Object = MibTableRow
cdx6500T1E1VGEntry = _Cdx6500T1E1VGEntry_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 2, 25, 1)
)
cdx6500T1E1VGEntry.setIndexNames(
    (0, "T1E1VG-OPT-MIB", "cdx6500T1E1VGCfgEntryNumber"),
)
if mibBuilder.loadTexts:
    cdx6500T1E1VGEntry.setStatus("mandatory")
_Cdx6500T1E1VGCfgEntryNumber_Type = Integer32
_Cdx6500T1E1VGCfgEntryNumber_Object = MibTableColumn
cdx6500T1E1VGCfgEntryNumber = _Cdx6500T1E1VGCfgEntryNumber_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 2, 25, 1, 1),
    _Cdx6500T1E1VGCfgEntryNumber_Type()
)
cdx6500T1E1VGCfgEntryNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500T1E1VGCfgEntryNumber.setStatus("mandatory")
_Cdx6500T1E1VGCfgInterfaceType_Type = DisplayString
_Cdx6500T1E1VGCfgInterfaceType_Object = MibTableColumn
cdx6500T1E1VGCfgInterfaceType = _Cdx6500T1E1VGCfgInterfaceType_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 2, 25, 1, 2),
    _Cdx6500T1E1VGCfgInterfaceType_Type()
)
cdx6500T1E1VGCfgInterfaceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500T1E1VGCfgInterfaceType.setStatus("mandatory")


class _Cdx6500T1E1VGCfgFormat_Type(Integer32):
    """Custom type cdx6500T1E1VGCfgFormat based on Integer32"""
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


_Cdx6500T1E1VGCfgFormat_Type.__name__ = "Integer32"
_Cdx6500T1E1VGCfgFormat_Object = MibTableColumn
cdx6500T1E1VGCfgFormat = _Cdx6500T1E1VGCfgFormat_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 2, 25, 1, 3),
    _Cdx6500T1E1VGCfgFormat_Type()
)
cdx6500T1E1VGCfgFormat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500T1E1VGCfgFormat.setStatus("mandatory")


class _Cdx6500T1E1VGCfgSwitchType_Type(Integer32):
    """Custom type cdx6500T1E1VGCfgSwitchType based on Integer32"""
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


_Cdx6500T1E1VGCfgSwitchType_Type.__name__ = "Integer32"
_Cdx6500T1E1VGCfgSwitchType_Object = MibTableColumn
cdx6500T1E1VGCfgSwitchType = _Cdx6500T1E1VGCfgSwitchType_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 2, 25, 1, 4),
    _Cdx6500T1E1VGCfgSwitchType_Type()
)
cdx6500T1E1VGCfgSwitchType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500T1E1VGCfgSwitchType.setStatus("mandatory")


class _Cdx6500T1E1VGCfgUserNetworkSide_Type(Integer32):
    """Custom type cdx6500T1E1VGCfgUserNetworkSide based on Integer32"""
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


_Cdx6500T1E1VGCfgUserNetworkSide_Type.__name__ = "Integer32"
_Cdx6500T1E1VGCfgUserNetworkSide_Object = MibTableColumn
cdx6500T1E1VGCfgUserNetworkSide = _Cdx6500T1E1VGCfgUserNetworkSide_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 2, 25, 1, 5),
    _Cdx6500T1E1VGCfgUserNetworkSide_Type()
)
cdx6500T1E1VGCfgUserNetworkSide.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500T1E1VGCfgUserNetworkSide.setStatus("mandatory")


class _Cdx6500T1E1VGCfgDirectBchannel_Type(Integer32):
    """Custom type cdx6500T1E1VGCfgDirectBchannel based on Integer32"""
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


_Cdx6500T1E1VGCfgDirectBchannel_Type.__name__ = "Integer32"
_Cdx6500T1E1VGCfgDirectBchannel_Object = MibTableColumn
cdx6500T1E1VGCfgDirectBchannel = _Cdx6500T1E1VGCfgDirectBchannel_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 2, 25, 1, 6),
    _Cdx6500T1E1VGCfgDirectBchannel_Type()
)
cdx6500T1E1VGCfgDirectBchannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500T1E1VGCfgDirectBchannel.setStatus("mandatory")
_Cdx6500T1E1VGCfgBchRange_Type = DisplayString
_Cdx6500T1E1VGCfgBchRange_Object = MibTableColumn
cdx6500T1E1VGCfgBchRange = _Cdx6500T1E1VGCfgBchRange_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 2, 25, 1, 7),
    _Cdx6500T1E1VGCfgBchRange_Type()
)
cdx6500T1E1VGCfgBchRange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500T1E1VGCfgBchRange.setStatus("mandatory")


class _Cdx6500T1E1VGCfgCallAddrReplace_Type(Integer32):
    """Custom type cdx6500T1E1VGCfgCallAddrReplace based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("none", 1)
    )


_Cdx6500T1E1VGCfgCallAddrReplace_Type.__name__ = "Integer32"
_Cdx6500T1E1VGCfgCallAddrReplace_Object = MibTableColumn
cdx6500T1E1VGCfgCallAddrReplace = _Cdx6500T1E1VGCfgCallAddrReplace_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 2, 25, 1, 8),
    _Cdx6500T1E1VGCfgCallAddrReplace_Type()
)
cdx6500T1E1VGCfgCallAddrReplace.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500T1E1VGCfgCallAddrReplace.setStatus("mandatory")
_Cdx6500T1E1VGCfgIsdnQsigOpt_Type = DisplayString
_Cdx6500T1E1VGCfgIsdnQsigOpt_Object = MibTableColumn
cdx6500T1E1VGCfgIsdnQsigOpt = _Cdx6500T1E1VGCfgIsdnQsigOpt_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 2, 25, 1, 9),
    _Cdx6500T1E1VGCfgIsdnQsigOpt_Type()
)
cdx6500T1E1VGCfgIsdnQsigOpt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500T1E1VGCfgIsdnQsigOpt.setStatus("mandatory")
_Cdx6500T1E1VGCfgFilteredIE_Type = DisplayString
_Cdx6500T1E1VGCfgFilteredIE_Object = MibTableColumn
cdx6500T1E1VGCfgFilteredIE = _Cdx6500T1E1VGCfgFilteredIE_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 2, 25, 1, 10),
    _Cdx6500T1E1VGCfgFilteredIE_Type()
)
cdx6500T1E1VGCfgFilteredIE.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500T1E1VGCfgFilteredIE.setStatus("mandatory")
_Cdx6500T1E1VGCfgReplIsdnQsig_Type = DisplayString
_Cdx6500T1E1VGCfgReplIsdnQsig_Object = MibTableColumn
cdx6500T1E1VGCfgReplIsdnQsig = _Cdx6500T1E1VGCfgReplIsdnQsig_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 2, 25, 1, 11),
    _Cdx6500T1E1VGCfgReplIsdnQsig_Type()
)
cdx6500T1E1VGCfgReplIsdnQsig.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500T1E1VGCfgReplIsdnQsig.setStatus("mandatory")


class _Cdx6500T1E1VGCfgCallPartyNumType_Type(Integer32):
    """Custom type cdx6500T1E1VGCfgCallPartyNumType based on Integer32"""
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


_Cdx6500T1E1VGCfgCallPartyNumType_Type.__name__ = "Integer32"
_Cdx6500T1E1VGCfgCallPartyNumType_Object = MibTableColumn
cdx6500T1E1VGCfgCallPartyNumType = _Cdx6500T1E1VGCfgCallPartyNumType_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 2, 25, 1, 12),
    _Cdx6500T1E1VGCfgCallPartyNumType_Type()
)
cdx6500T1E1VGCfgCallPartyNumType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500T1E1VGCfgCallPartyNumType.setStatus("mandatory")


class _Cdx6500T1E1VGCfgCallPartyNumPlan_Type(Integer32):
    """Custom type cdx6500T1E1VGCfgCallPartyNumPlan based on Integer32"""
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


_Cdx6500T1E1VGCfgCallPartyNumPlan_Type.__name__ = "Integer32"
_Cdx6500T1E1VGCfgCallPartyNumPlan_Object = MibTableColumn
cdx6500T1E1VGCfgCallPartyNumPlan = _Cdx6500T1E1VGCfgCallPartyNumPlan_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 2, 25, 1, 13),
    _Cdx6500T1E1VGCfgCallPartyNumPlan_Type()
)
cdx6500T1E1VGCfgCallPartyNumPlan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500T1E1VGCfgCallPartyNumPlan.setStatus("mandatory")
_Cdx6500T1E1VGCfg1stChanPort_Type = Integer32
_Cdx6500T1E1VGCfg1stChanPort_Object = MibTableColumn
cdx6500T1E1VGCfg1stChanPort = _Cdx6500T1E1VGCfg1stChanPort_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 2, 25, 1, 14),
    _Cdx6500T1E1VGCfg1stChanPort_Type()
)
cdx6500T1E1VGCfg1stChanPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500T1E1VGCfg1stChanPort.setStatus("mandatory")
_Cdx6500T1E1VGCfg1stChanSlot_Type = DisplayString
_Cdx6500T1E1VGCfg1stChanSlot_Object = MibTableColumn
cdx6500T1E1VGCfg1stChanSlot = _Cdx6500T1E1VGCfg1stChanSlot_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 2, 25, 1, 15),
    _Cdx6500T1E1VGCfg1stChanSlot_Type()
)
cdx6500T1E1VGCfg1stChanSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500T1E1VGCfg1stChanSlot.setStatus("mandatory")


class _Cdx6500T1E1VGCfg1stChanDS0Rate_Type(Integer32):
    """Custom type cdx6500T1E1VGCfg1stChanDS0Rate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("rate-56k", 1),
          ("rate-64k", 2))
    )


_Cdx6500T1E1VGCfg1stChanDS0Rate_Type.__name__ = "Integer32"
_Cdx6500T1E1VGCfg1stChanDS0Rate_Object = MibTableColumn
cdx6500T1E1VGCfg1stChanDS0Rate = _Cdx6500T1E1VGCfg1stChanDS0Rate_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 2, 25, 1, 16),
    _Cdx6500T1E1VGCfg1stChanDS0Rate_Type()
)
cdx6500T1E1VGCfg1stChanDS0Rate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500T1E1VGCfg1stChanDS0Rate.setStatus("mandatory")
_Cdx6500T1E1VGCfg2ndChanPort_Type = Integer32
_Cdx6500T1E1VGCfg2ndChanPort_Object = MibTableColumn
cdx6500T1E1VGCfg2ndChanPort = _Cdx6500T1E1VGCfg2ndChanPort_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 2, 25, 1, 17),
    _Cdx6500T1E1VGCfg2ndChanPort_Type()
)
cdx6500T1E1VGCfg2ndChanPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500T1E1VGCfg2ndChanPort.setStatus("mandatory")
_Cdx6500T1E1VGCfg2ndChanSlot_Type = DisplayString
_Cdx6500T1E1VGCfg2ndChanSlot_Object = MibTableColumn
cdx6500T1E1VGCfg2ndChanSlot = _Cdx6500T1E1VGCfg2ndChanSlot_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 2, 25, 1, 18),
    _Cdx6500T1E1VGCfg2ndChanSlot_Type()
)
cdx6500T1E1VGCfg2ndChanSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500T1E1VGCfg2ndChanSlot.setStatus("mandatory")


class _Cdx6500T1E1VGCfg2ndChanDS0Rate_Type(Integer32):
    """Custom type cdx6500T1E1VGCfg2ndChanDS0Rate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("rate-56k", 1),
          ("rate-64k", 2))
    )


_Cdx6500T1E1VGCfg2ndChanDS0Rate_Type.__name__ = "Integer32"
_Cdx6500T1E1VGCfg2ndChanDS0Rate_Object = MibTableColumn
cdx6500T1E1VGCfg2ndChanDS0Rate = _Cdx6500T1E1VGCfg2ndChanDS0Rate_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 2, 25, 1, 19),
    _Cdx6500T1E1VGCfg2ndChanDS0Rate_Type()
)
cdx6500T1E1VGCfg2ndChanDS0Rate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500T1E1VGCfg2ndChanDS0Rate.setStatus("mandatory")
_Cdx6500T1E1VGCfg3rdChanPort_Type = Integer32
_Cdx6500T1E1VGCfg3rdChanPort_Object = MibTableColumn
cdx6500T1E1VGCfg3rdChanPort = _Cdx6500T1E1VGCfg3rdChanPort_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 2, 25, 1, 20),
    _Cdx6500T1E1VGCfg3rdChanPort_Type()
)
cdx6500T1E1VGCfg3rdChanPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500T1E1VGCfg3rdChanPort.setStatus("mandatory")
_Cdx6500T1E1VGCfg3rdChanSlot_Type = DisplayString
_Cdx6500T1E1VGCfg3rdChanSlot_Object = MibTableColumn
cdx6500T1E1VGCfg3rdChanSlot = _Cdx6500T1E1VGCfg3rdChanSlot_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 2, 25, 1, 21),
    _Cdx6500T1E1VGCfg3rdChanSlot_Type()
)
cdx6500T1E1VGCfg3rdChanSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500T1E1VGCfg3rdChanSlot.setStatus("mandatory")


class _Cdx6500T1E1VGCfg3rdChanDS0Rate_Type(Integer32):
    """Custom type cdx6500T1E1VGCfg3rdChanDS0Rate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("rate-56k", 1),
          ("rate-64k", 2))
    )


_Cdx6500T1E1VGCfg3rdChanDS0Rate_Type.__name__ = "Integer32"
_Cdx6500T1E1VGCfg3rdChanDS0Rate_Object = MibTableColumn
cdx6500T1E1VGCfg3rdChanDS0Rate = _Cdx6500T1E1VGCfg3rdChanDS0Rate_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 2, 25, 1, 22),
    _Cdx6500T1E1VGCfg3rdChanDS0Rate_Type()
)
cdx6500T1E1VGCfg3rdChanDS0Rate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500T1E1VGCfg3rdChanDS0Rate.setStatus("mandatory")


class _Cdx6500T1E1VGCfgLineFramingType_Type(Integer32):
    """Custom type cdx6500T1E1VGCfgLineFramingType based on Integer32"""
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


_Cdx6500T1E1VGCfgLineFramingType_Type.__name__ = "Integer32"
_Cdx6500T1E1VGCfgLineFramingType_Object = MibTableColumn
cdx6500T1E1VGCfgLineFramingType = _Cdx6500T1E1VGCfgLineFramingType_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 2, 25, 1, 23),
    _Cdx6500T1E1VGCfgLineFramingType_Type()
)
cdx6500T1E1VGCfgLineFramingType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500T1E1VGCfgLineFramingType.setStatus("mandatory")


class _Cdx6500T1E1VGCfgLineCoding_Type(Integer32):
    """Custom type cdx6500T1E1VGCfgLineCoding based on Integer32"""
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


_Cdx6500T1E1VGCfgLineCoding_Type.__name__ = "Integer32"
_Cdx6500T1E1VGCfgLineCoding_Object = MibTableColumn
cdx6500T1E1VGCfgLineCoding = _Cdx6500T1E1VGCfgLineCoding_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 2, 25, 1, 24),
    _Cdx6500T1E1VGCfgLineCoding_Type()
)
cdx6500T1E1VGCfgLineCoding.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500T1E1VGCfgLineCoding.setStatus("mandatory")


class _Cdx6500T1E1VGCfgTransmitClock_Type(Integer32):
    """Custom type cdx6500T1E1VGCfgTransmitClock based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("int", 2),
          ("rec", 1))
    )


_Cdx6500T1E1VGCfgTransmitClock_Type.__name__ = "Integer32"
_Cdx6500T1E1VGCfgTransmitClock_Object = MibTableColumn
cdx6500T1E1VGCfgTransmitClock = _Cdx6500T1E1VGCfgTransmitClock_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 2, 25, 1, 25),
    _Cdx6500T1E1VGCfgTransmitClock_Type()
)
cdx6500T1E1VGCfgTransmitClock.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500T1E1VGCfgTransmitClock.setStatus("mandatory")


class _Cdx6500T1E1VGCfgLineImpedance_Type(Integer32):
    """Custom type cdx6500T1E1VGCfgLineImpedance based on Integer32"""
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


_Cdx6500T1E1VGCfgLineImpedance_Type.__name__ = "Integer32"
_Cdx6500T1E1VGCfgLineImpedance_Object = MibTableColumn
cdx6500T1E1VGCfgLineImpedance = _Cdx6500T1E1VGCfgLineImpedance_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 2, 25, 1, 26),
    _Cdx6500T1E1VGCfgLineImpedance_Type()
)
cdx6500T1E1VGCfgLineImpedance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500T1E1VGCfgLineImpedance.setStatus("mandatory")
_Cdx6500T1E1VGCfgLineBuildOut_Type = Integer32
_Cdx6500T1E1VGCfgLineBuildOut_Object = MibTableColumn
cdx6500T1E1VGCfgLineBuildOut = _Cdx6500T1E1VGCfgLineBuildOut_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 2, 25, 1, 27),
    _Cdx6500T1E1VGCfgLineBuildOut_Type()
)
cdx6500T1E1VGCfgLineBuildOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500T1E1VGCfgLineBuildOut.setStatus("mandatory")


class _Cdx6500T1E1VGCfgRecvSense_Type(Integer32):
    """Custom type cdx6500T1E1VGCfgRecvSense based on Integer32"""
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


_Cdx6500T1E1VGCfgRecvSense_Type.__name__ = "Integer32"
_Cdx6500T1E1VGCfgRecvSense_Object = MibTableColumn
cdx6500T1E1VGCfgRecvSense = _Cdx6500T1E1VGCfgRecvSense_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 2, 25, 1, 28),
    _Cdx6500T1E1VGCfgRecvSense_Type()
)
cdx6500T1E1VGCfgRecvSense.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500T1E1VGCfgRecvSense.setStatus("mandatory")


class _Cdx6500T1E1VGCfgFacilityDataLink_Type(Integer32):
    """Custom type cdx6500T1E1VGCfgFacilityDataLink based on Integer32"""
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


_Cdx6500T1E1VGCfgFacilityDataLink_Type.__name__ = "Integer32"
_Cdx6500T1E1VGCfgFacilityDataLink_Object = MibTableColumn
cdx6500T1E1VGCfgFacilityDataLink = _Cdx6500T1E1VGCfgFacilityDataLink_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 2, 25, 1, 29),
    _Cdx6500T1E1VGCfgFacilityDataLink_Type()
)
cdx6500T1E1VGCfgFacilityDataLink.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500T1E1VGCfgFacilityDataLink.setStatus("mandatory")


class _Cdx6500T1E1VGCfgV54RecvRLBK_Type(Integer32):
    """Custom type cdx6500T1E1VGCfgV54RecvRLBK based on Integer32"""
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


_Cdx6500T1E1VGCfgV54RecvRLBK_Type.__name__ = "Integer32"
_Cdx6500T1E1VGCfgV54RecvRLBK_Object = MibTableColumn
cdx6500T1E1VGCfgV54RecvRLBK = _Cdx6500T1E1VGCfgV54RecvRLBK_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 2, 25, 1, 30),
    _Cdx6500T1E1VGCfgV54RecvRLBK_Type()
)
cdx6500T1E1VGCfgV54RecvRLBK.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500T1E1VGCfgV54RecvRLBK.setStatus("mandatory")


class _Cdx6500T1E1VGCfgThresholdValueLES_Type(Integer32):
    """Custom type cdx6500T1E1VGCfgThresholdValueLES based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_Cdx6500T1E1VGCfgThresholdValueLES_Type.__name__ = "Integer32"
_Cdx6500T1E1VGCfgThresholdValueLES_Object = MibTableColumn
cdx6500T1E1VGCfgThresholdValueLES = _Cdx6500T1E1VGCfgThresholdValueLES_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 2, 25, 1, 31),
    _Cdx6500T1E1VGCfgThresholdValueLES_Type()
)
cdx6500T1E1VGCfgThresholdValueLES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500T1E1VGCfgThresholdValueLES.setStatus("mandatory")


class _Cdx6500T1E1VGCfgThresholdValueLCV_Type(Integer32):
    """Custom type cdx6500T1E1VGCfgThresholdValueLCV based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_Cdx6500T1E1VGCfgThresholdValueLCV_Type.__name__ = "Integer32"
_Cdx6500T1E1VGCfgThresholdValueLCV_Object = MibTableColumn
cdx6500T1E1VGCfgThresholdValueLCV = _Cdx6500T1E1VGCfgThresholdValueLCV_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 2, 25, 1, 32),
    _Cdx6500T1E1VGCfgThresholdValueLCV_Type()
)
cdx6500T1E1VGCfgThresholdValueLCV.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500T1E1VGCfgThresholdValueLCV.setStatus("mandatory")


class _Cdx6500T1E1VGCfgThresholdValuePCV_Type(Integer32):
    """Custom type cdx6500T1E1VGCfgThresholdValuePCV based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_Cdx6500T1E1VGCfgThresholdValuePCV_Type.__name__ = "Integer32"
_Cdx6500T1E1VGCfgThresholdValuePCV_Object = MibTableColumn
cdx6500T1E1VGCfgThresholdValuePCV = _Cdx6500T1E1VGCfgThresholdValuePCV_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 2, 25, 1, 33),
    _Cdx6500T1E1VGCfgThresholdValuePCV_Type()
)
cdx6500T1E1VGCfgThresholdValuePCV.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500T1E1VGCfgThresholdValuePCV.setStatus("mandatory")


class _Cdx6500T1E1VGCfgThresholdValueCSS_Type(Integer32):
    """Custom type cdx6500T1E1VGCfgThresholdValueCSS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_Cdx6500T1E1VGCfgThresholdValueCSS_Type.__name__ = "Integer32"
_Cdx6500T1E1VGCfgThresholdValueCSS_Object = MibTableColumn
cdx6500T1E1VGCfgThresholdValueCSS = _Cdx6500T1E1VGCfgThresholdValueCSS_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 2, 25, 1, 34),
    _Cdx6500T1E1VGCfgThresholdValueCSS_Type()
)
cdx6500T1E1VGCfgThresholdValueCSS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500T1E1VGCfgThresholdValueCSS.setStatus("mandatory")


class _Cdx6500T1E1VGCfgThresholdValueES_Type(Integer32):
    """Custom type cdx6500T1E1VGCfgThresholdValueES based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_Cdx6500T1E1VGCfgThresholdValueES_Type.__name__ = "Integer32"
_Cdx6500T1E1VGCfgThresholdValueES_Object = MibTableColumn
cdx6500T1E1VGCfgThresholdValueES = _Cdx6500T1E1VGCfgThresholdValueES_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 2, 25, 1, 35),
    _Cdx6500T1E1VGCfgThresholdValueES_Type()
)
cdx6500T1E1VGCfgThresholdValueES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500T1E1VGCfgThresholdValueES.setStatus("mandatory")


class _Cdx6500T1E1VGCfgThresholdValueBES_Type(Integer32):
    """Custom type cdx6500T1E1VGCfgThresholdValueBES based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_Cdx6500T1E1VGCfgThresholdValueBES_Type.__name__ = "Integer32"
_Cdx6500T1E1VGCfgThresholdValueBES_Object = MibTableColumn
cdx6500T1E1VGCfgThresholdValueBES = _Cdx6500T1E1VGCfgThresholdValueBES_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 2, 25, 1, 36),
    _Cdx6500T1E1VGCfgThresholdValueBES_Type()
)
cdx6500T1E1VGCfgThresholdValueBES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500T1E1VGCfgThresholdValueBES.setStatus("mandatory")


class _Cdx6500T1E1VGCfgThresholdValueSES_Type(Integer32):
    """Custom type cdx6500T1E1VGCfgThresholdValueSES based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_Cdx6500T1E1VGCfgThresholdValueSES_Type.__name__ = "Integer32"
_Cdx6500T1E1VGCfgThresholdValueSES_Object = MibTableColumn
cdx6500T1E1VGCfgThresholdValueSES = _Cdx6500T1E1VGCfgThresholdValueSES_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 2, 25, 1, 37),
    _Cdx6500T1E1VGCfgThresholdValueSES_Type()
)
cdx6500T1E1VGCfgThresholdValueSES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500T1E1VGCfgThresholdValueSES.setStatus("mandatory")


class _Cdx6500T1E1VGCfgThresholdValueSEFS_Type(Integer32):
    """Custom type cdx6500T1E1VGCfgThresholdValueSEFS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_Cdx6500T1E1VGCfgThresholdValueSEFS_Type.__name__ = "Integer32"
_Cdx6500T1E1VGCfgThresholdValueSEFS_Object = MibTableColumn
cdx6500T1E1VGCfgThresholdValueSEFS = _Cdx6500T1E1VGCfgThresholdValueSEFS_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 2, 25, 1, 38),
    _Cdx6500T1E1VGCfgThresholdValueSEFS_Type()
)
cdx6500T1E1VGCfgThresholdValueSEFS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500T1E1VGCfgThresholdValueSEFS.setStatus("mandatory")


class _Cdx6500T1E1VGCfgThresholdValueUAS_Type(Integer32):
    """Custom type cdx6500T1E1VGCfgThresholdValueUAS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_Cdx6500T1E1VGCfgThresholdValueUAS_Type.__name__ = "Integer32"
_Cdx6500T1E1VGCfgThresholdValueUAS_Object = MibTableColumn
cdx6500T1E1VGCfgThresholdValueUAS = _Cdx6500T1E1VGCfgThresholdValueUAS_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 2, 25, 1, 39),
    _Cdx6500T1E1VGCfgThresholdValueUAS_Type()
)
cdx6500T1E1VGCfgThresholdValueUAS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500T1E1VGCfgThresholdValueUAS.setStatus("mandatory")


class _Cdx6500T1E1VGCfgBchNumScheme_Type(Integer32):
    """Custom type cdx6500T1E1VGCfgBchNumScheme based on Integer32"""
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


_Cdx6500T1E1VGCfgBchNumScheme_Type.__name__ = "Integer32"
_Cdx6500T1E1VGCfgBchNumScheme_Object = MibTableColumn
cdx6500T1E1VGCfgBchNumScheme = _Cdx6500T1E1VGCfgBchNumScheme_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 2, 25, 1, 40),
    _Cdx6500T1E1VGCfgBchNumScheme_Type()
)
cdx6500T1E1VGCfgBchNumScheme.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500T1E1VGCfgBchNumScheme.setStatus("mandatory")
_Cdx6500Statistics_ObjectIdentity = ObjectIdentity
cdx6500Statistics = _Cdx6500Statistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3)
)
_Cdx6500StatOtherStatsGroup_ObjectIdentity = ObjectIdentity
cdx6500StatOtherStatsGroup = _Cdx6500StatOtherStatsGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 2)
)
_Cdx6500STT1E1VGGroup_ObjectIdentity = ObjectIdentity
cdx6500STT1E1VGGroup = _Cdx6500STT1E1VGGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 2, 15)
)
_Cdx6500STT1E1VGTable_Object = MibTable
cdx6500STT1E1VGTable = _Cdx6500STT1E1VGTable_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 2, 15, 1)
)
if mibBuilder.loadTexts:
    cdx6500STT1E1VGTable.setStatus("mandatory")
_Cdx6500STT1E1VGEntry_Object = MibTableRow
cdx6500STT1E1VGEntry = _Cdx6500STT1E1VGEntry_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 2, 15, 1, 1)
)
cdx6500STT1E1VGEntry.setIndexNames(
    (0, "T1E1VG-OPT-MIB", "cdx6500T1E1VGStatIfNumber"),
)
if mibBuilder.loadTexts:
    cdx6500STT1E1VGEntry.setStatus("mandatory")
_Cdx6500T1E1VGStatIfNumber_Type = Integer32
_Cdx6500T1E1VGStatIfNumber_Object = MibTableColumn
cdx6500T1E1VGStatIfNumber = _Cdx6500T1E1VGStatIfNumber_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 2, 15, 1, 1, 1),
    _Cdx6500T1E1VGStatIfNumber_Type()
)
cdx6500T1E1VGStatIfNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500T1E1VGStatIfNumber.setStatus("mandatory")
_Cdx6500T1E1VGStatInterfaceType_Type = DisplayString
_Cdx6500T1E1VGStatInterfaceType_Object = MibTableColumn
cdx6500T1E1VGStatInterfaceType = _Cdx6500T1E1VGStatInterfaceType_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 2, 15, 1, 1, 2),
    _Cdx6500T1E1VGStatInterfaceType_Type()
)
cdx6500T1E1VGStatInterfaceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500T1E1VGStatInterfaceType.setStatus("mandatory")
_Cdx6500T1E1VGStatTimeSinceLastReset_Type = DisplayString
_Cdx6500T1E1VGStatTimeSinceLastReset_Object = MibTableColumn
cdx6500T1E1VGStatTimeSinceLastReset = _Cdx6500T1E1VGStatTimeSinceLastReset_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 2, 15, 1, 1, 3),
    _Cdx6500T1E1VGStatTimeSinceLastReset_Type()
)
cdx6500T1E1VGStatTimeSinceLastReset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500T1E1VGStatTimeSinceLastReset.setStatus("mandatory")
_Cdx6500T1E1VGStatAlarmState_Type = DisplayString
_Cdx6500T1E1VGStatAlarmState_Object = MibTableColumn
cdx6500T1E1VGStatAlarmState = _Cdx6500T1E1VGStatAlarmState_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 2, 15, 1, 1, 4),
    _Cdx6500T1E1VGStatAlarmState_Type()
)
cdx6500T1E1VGStatAlarmState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500T1E1VGStatAlarmState.setStatus("mandatory")
_Cdx6500T1E1VGStatChannelState_Type = DisplayString
_Cdx6500T1E1VGStatChannelState_Object = MibTableColumn
cdx6500T1E1VGStatChannelState = _Cdx6500T1E1VGStatChannelState_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 2, 15, 1, 1, 5),
    _Cdx6500T1E1VGStatChannelState_Type()
)
cdx6500T1E1VGStatChannelState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500T1E1VGStatChannelState.setStatus("mandatory")
_Cdx6500T1E1VGStatTotal24HoursReportTable_Object = MibTable
cdx6500T1E1VGStatTotal24HoursReportTable = _Cdx6500T1E1VGStatTotal24HoursReportTable_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 2, 15, 2)
)
if mibBuilder.loadTexts:
    cdx6500T1E1VGStatTotal24HoursReportTable.setStatus("mandatory")
_Cdx6500T1E1VGStatTotal24HoursReportEntry_Object = MibTableRow
cdx6500T1E1VGStatTotal24HoursReportEntry = _Cdx6500T1E1VGStatTotal24HoursReportEntry_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 2, 15, 2, 1)
)
cdx6500T1E1VGStatTotal24HoursReportEntry.setIndexNames(
    (0, "T1E1VG-OPT-MIB", "cdx6500T1E1VGStatTotal24HoursReportIfNumber"),
)
if mibBuilder.loadTexts:
    cdx6500T1E1VGStatTotal24HoursReportEntry.setStatus("mandatory")
_Cdx6500T1E1VGStatTotal24HoursReportIfNumber_Type = Integer32
_Cdx6500T1E1VGStatTotal24HoursReportIfNumber_Object = MibTableColumn
cdx6500T1E1VGStatTotal24HoursReportIfNumber = _Cdx6500T1E1VGStatTotal24HoursReportIfNumber_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 2, 15, 2, 1, 1),
    _Cdx6500T1E1VGStatTotal24HoursReportIfNumber_Type()
)
cdx6500T1E1VGStatTotal24HoursReportIfNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500T1E1VGStatTotal24HoursReportIfNumber.setStatus("mandatory")
_Cdx6500T1E1VGStatTotal24HoursReportLES_Type = Gauge32
_Cdx6500T1E1VGStatTotal24HoursReportLES_Object = MibTableColumn
cdx6500T1E1VGStatTotal24HoursReportLES = _Cdx6500T1E1VGStatTotal24HoursReportLES_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 2, 15, 2, 1, 2),
    _Cdx6500T1E1VGStatTotal24HoursReportLES_Type()
)
cdx6500T1E1VGStatTotal24HoursReportLES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500T1E1VGStatTotal24HoursReportLES.setStatus("mandatory")
_Cdx6500T1E1VGStatTotal24HoursReportLCV_Type = Gauge32
_Cdx6500T1E1VGStatTotal24HoursReportLCV_Object = MibTableColumn
cdx6500T1E1VGStatTotal24HoursReportLCV = _Cdx6500T1E1VGStatTotal24HoursReportLCV_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 2, 15, 2, 1, 3),
    _Cdx6500T1E1VGStatTotal24HoursReportLCV_Type()
)
cdx6500T1E1VGStatTotal24HoursReportLCV.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500T1E1VGStatTotal24HoursReportLCV.setStatus("mandatory")
_Cdx6500T1E1VGStatTotal24HoursReportPCV_Type = Gauge32
_Cdx6500T1E1VGStatTotal24HoursReportPCV_Object = MibTableColumn
cdx6500T1E1VGStatTotal24HoursReportPCV = _Cdx6500T1E1VGStatTotal24HoursReportPCV_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 2, 15, 2, 1, 4),
    _Cdx6500T1E1VGStatTotal24HoursReportPCV_Type()
)
cdx6500T1E1VGStatTotal24HoursReportPCV.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500T1E1VGStatTotal24HoursReportPCV.setStatus("mandatory")
_Cdx6500T1E1VGStatTotal24HoursReportCSS_Type = Gauge32
_Cdx6500T1E1VGStatTotal24HoursReportCSS_Object = MibTableColumn
cdx6500T1E1VGStatTotal24HoursReportCSS = _Cdx6500T1E1VGStatTotal24HoursReportCSS_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 2, 15, 2, 1, 5),
    _Cdx6500T1E1VGStatTotal24HoursReportCSS_Type()
)
cdx6500T1E1VGStatTotal24HoursReportCSS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500T1E1VGStatTotal24HoursReportCSS.setStatus("mandatory")
_Cdx6500T1E1VGStatTotal24HoursReportES_Type = Gauge32
_Cdx6500T1E1VGStatTotal24HoursReportES_Object = MibTableColumn
cdx6500T1E1VGStatTotal24HoursReportES = _Cdx6500T1E1VGStatTotal24HoursReportES_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 2, 15, 2, 1, 6),
    _Cdx6500T1E1VGStatTotal24HoursReportES_Type()
)
cdx6500T1E1VGStatTotal24HoursReportES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500T1E1VGStatTotal24HoursReportES.setStatus("mandatory")
_Cdx6500T1E1VGStatTotal24HoursReportBES_Type = Gauge32
_Cdx6500T1E1VGStatTotal24HoursReportBES_Object = MibTableColumn
cdx6500T1E1VGStatTotal24HoursReportBES = _Cdx6500T1E1VGStatTotal24HoursReportBES_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 2, 15, 2, 1, 7),
    _Cdx6500T1E1VGStatTotal24HoursReportBES_Type()
)
cdx6500T1E1VGStatTotal24HoursReportBES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500T1E1VGStatTotal24HoursReportBES.setStatus("mandatory")
_Cdx6500T1E1VGStatTotal24HoursReportSES_Type = Gauge32
_Cdx6500T1E1VGStatTotal24HoursReportSES_Object = MibTableColumn
cdx6500T1E1VGStatTotal24HoursReportSES = _Cdx6500T1E1VGStatTotal24HoursReportSES_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 2, 15, 2, 1, 8),
    _Cdx6500T1E1VGStatTotal24HoursReportSES_Type()
)
cdx6500T1E1VGStatTotal24HoursReportSES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500T1E1VGStatTotal24HoursReportSES.setStatus("mandatory")
_Cdx6500T1E1VGStatTotal24HoursReportSEFS_Type = Gauge32
_Cdx6500T1E1VGStatTotal24HoursReportSEFS_Object = MibTableColumn
cdx6500T1E1VGStatTotal24HoursReportSEFS = _Cdx6500T1E1VGStatTotal24HoursReportSEFS_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 2, 15, 2, 1, 9),
    _Cdx6500T1E1VGStatTotal24HoursReportSEFS_Type()
)
cdx6500T1E1VGStatTotal24HoursReportSEFS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500T1E1VGStatTotal24HoursReportSEFS.setStatus("mandatory")
_Cdx6500T1E1VGStatTotal24HoursReportUAS_Type = Gauge32
_Cdx6500T1E1VGStatTotal24HoursReportUAS_Object = MibTableColumn
cdx6500T1E1VGStatTotal24HoursReportUAS = _Cdx6500T1E1VGStatTotal24HoursReportUAS_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 2, 15, 2, 1, 10),
    _Cdx6500T1E1VGStatTotal24HoursReportUAS_Type()
)
cdx6500T1E1VGStatTotal24HoursReportUAS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500T1E1VGStatTotal24HoursReportUAS.setStatus("mandatory")
_Cdx6500T1E1VGStatCurrent15MinutesReportTable_Object = MibTable
cdx6500T1E1VGStatCurrent15MinutesReportTable = _Cdx6500T1E1VGStatCurrent15MinutesReportTable_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 2, 15, 3)
)
if mibBuilder.loadTexts:
    cdx6500T1E1VGStatCurrent15MinutesReportTable.setStatus("mandatory")
_Cdx6500T1E1VGStatCurrent15MinutesReportEntry_Object = MibTableRow
cdx6500T1E1VGStatCurrent15MinutesReportEntry = _Cdx6500T1E1VGStatCurrent15MinutesReportEntry_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 2, 15, 3, 1)
)
cdx6500T1E1VGStatCurrent15MinutesReportEntry.setIndexNames(
    (0, "T1E1VG-OPT-MIB", "cdx6500T1E1VGStatCurrent15MinutesReportIfNumber"),
)
if mibBuilder.loadTexts:
    cdx6500T1E1VGStatCurrent15MinutesReportEntry.setStatus("mandatory")
_Cdx6500T1E1VGStatCurrent15MinutesReportIfNumber_Type = Integer32
_Cdx6500T1E1VGStatCurrent15MinutesReportIfNumber_Object = MibTableColumn
cdx6500T1E1VGStatCurrent15MinutesReportIfNumber = _Cdx6500T1E1VGStatCurrent15MinutesReportIfNumber_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 2, 15, 3, 1, 1),
    _Cdx6500T1E1VGStatCurrent15MinutesReportIfNumber_Type()
)
cdx6500T1E1VGStatCurrent15MinutesReportIfNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500T1E1VGStatCurrent15MinutesReportIfNumber.setStatus("mandatory")
_Cdx6500T1E1VGStatCurrent15MinutesReportTimeElapsed_Type = Integer32
_Cdx6500T1E1VGStatCurrent15MinutesReportTimeElapsed_Object = MibTableColumn
cdx6500T1E1VGStatCurrent15MinutesReportTimeElapsed = _Cdx6500T1E1VGStatCurrent15MinutesReportTimeElapsed_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 2, 15, 3, 1, 2),
    _Cdx6500T1E1VGStatCurrent15MinutesReportTimeElapsed_Type()
)
cdx6500T1E1VGStatCurrent15MinutesReportTimeElapsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500T1E1VGStatCurrent15MinutesReportTimeElapsed.setStatus("mandatory")
_Cdx6500T1E1VGStatCurrent15MinutesReportLES_Type = Gauge32
_Cdx6500T1E1VGStatCurrent15MinutesReportLES_Object = MibTableColumn
cdx6500T1E1VGStatCurrent15MinutesReportLES = _Cdx6500T1E1VGStatCurrent15MinutesReportLES_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 2, 15, 3, 1, 3),
    _Cdx6500T1E1VGStatCurrent15MinutesReportLES_Type()
)
cdx6500T1E1VGStatCurrent15MinutesReportLES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500T1E1VGStatCurrent15MinutesReportLES.setStatus("mandatory")
_Cdx6500T1E1VGStatCurrent15MinutesReportLCV_Type = Gauge32
_Cdx6500T1E1VGStatCurrent15MinutesReportLCV_Object = MibTableColumn
cdx6500T1E1VGStatCurrent15MinutesReportLCV = _Cdx6500T1E1VGStatCurrent15MinutesReportLCV_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 2, 15, 3, 1, 4),
    _Cdx6500T1E1VGStatCurrent15MinutesReportLCV_Type()
)
cdx6500T1E1VGStatCurrent15MinutesReportLCV.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500T1E1VGStatCurrent15MinutesReportLCV.setStatus("mandatory")
_Cdx6500T1E1VGStatCurrent15MinutesReportPCV_Type = Gauge32
_Cdx6500T1E1VGStatCurrent15MinutesReportPCV_Object = MibTableColumn
cdx6500T1E1VGStatCurrent15MinutesReportPCV = _Cdx6500T1E1VGStatCurrent15MinutesReportPCV_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 2, 15, 3, 1, 5),
    _Cdx6500T1E1VGStatCurrent15MinutesReportPCV_Type()
)
cdx6500T1E1VGStatCurrent15MinutesReportPCV.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500T1E1VGStatCurrent15MinutesReportPCV.setStatus("mandatory")
_Cdx6500T1E1VGStatCurrent15MinutesReportCSS_Type = Gauge32
_Cdx6500T1E1VGStatCurrent15MinutesReportCSS_Object = MibTableColumn
cdx6500T1E1VGStatCurrent15MinutesReportCSS = _Cdx6500T1E1VGStatCurrent15MinutesReportCSS_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 2, 15, 3, 1, 6),
    _Cdx6500T1E1VGStatCurrent15MinutesReportCSS_Type()
)
cdx6500T1E1VGStatCurrent15MinutesReportCSS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500T1E1VGStatCurrent15MinutesReportCSS.setStatus("mandatory")
_Cdx6500T1E1VGStatCurrent15MinutesReportES_Type = Gauge32
_Cdx6500T1E1VGStatCurrent15MinutesReportES_Object = MibTableColumn
cdx6500T1E1VGStatCurrent15MinutesReportES = _Cdx6500T1E1VGStatCurrent15MinutesReportES_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 2, 15, 3, 1, 7),
    _Cdx6500T1E1VGStatCurrent15MinutesReportES_Type()
)
cdx6500T1E1VGStatCurrent15MinutesReportES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500T1E1VGStatCurrent15MinutesReportES.setStatus("mandatory")
_Cdx6500T1E1VGStatCurrent15MinutesReportBES_Type = Gauge32
_Cdx6500T1E1VGStatCurrent15MinutesReportBES_Object = MibTableColumn
cdx6500T1E1VGStatCurrent15MinutesReportBES = _Cdx6500T1E1VGStatCurrent15MinutesReportBES_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 2, 15, 3, 1, 8),
    _Cdx6500T1E1VGStatCurrent15MinutesReportBES_Type()
)
cdx6500T1E1VGStatCurrent15MinutesReportBES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500T1E1VGStatCurrent15MinutesReportBES.setStatus("mandatory")
_Cdx6500T1E1VGStatCurrent15MinutesReportSES_Type = Gauge32
_Cdx6500T1E1VGStatCurrent15MinutesReportSES_Object = MibTableColumn
cdx6500T1E1VGStatCurrent15MinutesReportSES = _Cdx6500T1E1VGStatCurrent15MinutesReportSES_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 2, 15, 3, 1, 9),
    _Cdx6500T1E1VGStatCurrent15MinutesReportSES_Type()
)
cdx6500T1E1VGStatCurrent15MinutesReportSES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500T1E1VGStatCurrent15MinutesReportSES.setStatus("mandatory")
_Cdx6500T1E1VGStatCurrent15MinutesReportSEFS_Type = Gauge32
_Cdx6500T1E1VGStatCurrent15MinutesReportSEFS_Object = MibTableColumn
cdx6500T1E1VGStatCurrent15MinutesReportSEFS = _Cdx6500T1E1VGStatCurrent15MinutesReportSEFS_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 2, 15, 3, 1, 10),
    _Cdx6500T1E1VGStatCurrent15MinutesReportSEFS_Type()
)
cdx6500T1E1VGStatCurrent15MinutesReportSEFS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500T1E1VGStatCurrent15MinutesReportSEFS.setStatus("mandatory")
_Cdx6500T1E1VGStatCurrent15MinutesReportUAS_Type = Gauge32
_Cdx6500T1E1VGStatCurrent15MinutesReportUAS_Object = MibScalar
cdx6500T1E1VGStatCurrent15MinutesReportUAS = _Cdx6500T1E1VGStatCurrent15MinutesReportUAS_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 2, 15, 3, 1, 11),
    _Cdx6500T1E1VGStatCurrent15MinutesReportUAS_Type()
)
cdx6500T1E1VGStatCurrent15MinutesReportUAS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500T1E1VGStatCurrent15MinutesReportUAS.setStatus("mandatory")
_Cdx6500T1E1VGStatT1ChannelStateTable_Object = MibTable
cdx6500T1E1VGStatT1ChannelStateTable = _Cdx6500T1E1VGStatT1ChannelStateTable_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 2, 15, 4)
)
if mibBuilder.loadTexts:
    cdx6500T1E1VGStatT1ChannelStateTable.setStatus("mandatory")
_Cdx6500T1E1VGStatT1ChannelStateEntry_Object = MibTableRow
cdx6500T1E1VGStatT1ChannelStateEntry = _Cdx6500T1E1VGStatT1ChannelStateEntry_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 2, 15, 4, 1)
)
cdx6500T1E1VGStatT1ChannelStateEntry.setIndexNames(
    (0, "T1E1VG-OPT-MIB", "cdx6500T1E1VGStatT1ChannelStateIfNumber"),
    (0, "T1E1VG-OPT-MIB", "cdx6500T1E1VGStatT1ChannelStateABCDNumber"),
)
if mibBuilder.loadTexts:
    cdx6500T1E1VGStatT1ChannelStateEntry.setStatus("mandatory")
_Cdx6500T1E1VGStatT1ChannelStateIfNumber_Type = Integer32
_Cdx6500T1E1VGStatT1ChannelStateIfNumber_Object = MibTableColumn
cdx6500T1E1VGStatT1ChannelStateIfNumber = _Cdx6500T1E1VGStatT1ChannelStateIfNumber_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 2, 15, 4, 1, 1),
    _Cdx6500T1E1VGStatT1ChannelStateIfNumber_Type()
)
cdx6500T1E1VGStatT1ChannelStateIfNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500T1E1VGStatT1ChannelStateIfNumber.setStatus("mandatory")


class _Cdx6500T1E1VGStatT1ChannelStateABCDNumber_Type(Integer32):
    """Custom type cdx6500T1E1VGStatT1ChannelStateABCDNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 24),
    )


_Cdx6500T1E1VGStatT1ChannelStateABCDNumber_Type.__name__ = "Integer32"
_Cdx6500T1E1VGStatT1ChannelStateABCDNumber_Object = MibTableColumn
cdx6500T1E1VGStatT1ChannelStateABCDNumber = _Cdx6500T1E1VGStatT1ChannelStateABCDNumber_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 2, 15, 4, 1, 2),
    _Cdx6500T1E1VGStatT1ChannelStateABCDNumber_Type()
)
cdx6500T1E1VGStatT1ChannelStateABCDNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500T1E1VGStatT1ChannelStateABCDNumber.setStatus("mandatory")
_Cdx6500T1E1VGStatT1ChannelStateCurrentRxState_Type = DisplayString
_Cdx6500T1E1VGStatT1ChannelStateCurrentRxState_Object = MibTableColumn
cdx6500T1E1VGStatT1ChannelStateCurrentRxState = _Cdx6500T1E1VGStatT1ChannelStateCurrentRxState_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 2, 15, 4, 1, 3),
    _Cdx6500T1E1VGStatT1ChannelStateCurrentRxState_Type()
)
cdx6500T1E1VGStatT1ChannelStateCurrentRxState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500T1E1VGStatT1ChannelStateCurrentRxState.setStatus("mandatory")
_Cdx6500T1E1VGStatE1ABCDStateTable_Object = MibTable
cdx6500T1E1VGStatE1ABCDStateTable = _Cdx6500T1E1VGStatE1ABCDStateTable_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 2, 15, 5)
)
if mibBuilder.loadTexts:
    cdx6500T1E1VGStatE1ABCDStateTable.setStatus("mandatory")
_Cdx6500T1E1VGStatE1ABCDStateEntry_Object = MibTableRow
cdx6500T1E1VGStatE1ABCDStateEntry = _Cdx6500T1E1VGStatE1ABCDStateEntry_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 2, 15, 5, 1)
)
cdx6500T1E1VGStatE1ABCDStateEntry.setIndexNames(
    (0, "T1E1VG-OPT-MIB", "cdx6500T1E1VGStatE1ABCDStateIfNumber"),
    (0, "T1E1VG-OPT-MIB", "cdx6500T1E1VGStatE1ABCDStateChannelNumber"),
)
if mibBuilder.loadTexts:
    cdx6500T1E1VGStatE1ABCDStateEntry.setStatus("mandatory")
_Cdx6500T1E1VGStatE1ABCDStateIfNumber_Type = Integer32
_Cdx6500T1E1VGStatE1ABCDStateIfNumber_Object = MibTableColumn
cdx6500T1E1VGStatE1ABCDStateIfNumber = _Cdx6500T1E1VGStatE1ABCDStateIfNumber_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 2, 15, 5, 1, 1),
    _Cdx6500T1E1VGStatE1ABCDStateIfNumber_Type()
)
cdx6500T1E1VGStatE1ABCDStateIfNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500T1E1VGStatE1ABCDStateIfNumber.setStatus("mandatory")


class _Cdx6500T1E1VGStatE1ABCDStateChannelNumber_Type(Integer32):
    """Custom type cdx6500T1E1VGStatE1ABCDStateChannelNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 30),
    )


_Cdx6500T1E1VGStatE1ABCDStateChannelNumber_Type.__name__ = "Integer32"
_Cdx6500T1E1VGStatE1ABCDStateChannelNumber_Object = MibTableColumn
cdx6500T1E1VGStatE1ABCDStateChannelNumber = _Cdx6500T1E1VGStatE1ABCDStateChannelNumber_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 2, 15, 5, 1, 2),
    _Cdx6500T1E1VGStatE1ABCDStateChannelNumber_Type()
)
cdx6500T1E1VGStatE1ABCDStateChannelNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500T1E1VGStatE1ABCDStateChannelNumber.setStatus("mandatory")
_Cdx6500T1E1VGStatE1ABCDStateCurrentRxState_Type = DisplayString
_Cdx6500T1E1VGStatE1ABCDStateCurrentRxState_Object = MibTableColumn
cdx6500T1E1VGStatE1ABCDStateCurrentRxState = _Cdx6500T1E1VGStatE1ABCDStateCurrentRxState_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 2, 15, 5, 1, 3),
    _Cdx6500T1E1VGStatE1ABCDStateCurrentRxState_Type()
)
cdx6500T1E1VGStatE1ABCDStateCurrentRxState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500T1E1VGStatE1ABCDStateCurrentRxState.setStatus("mandatory")
_Cdx6500Controls_ObjectIdentity = ObjectIdentity
cdx6500Controls = _Cdx6500Controls_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 4)
)
_Cdx6500ContT1E1VGTable_ObjectIdentity = ObjectIdentity
cdx6500ContT1E1VGTable = _Cdx6500ContT1E1VGTable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 4, 19)
)
_Cdx6500T1E1VGContEntry_Object = MibTableRow
cdx6500T1E1VGContEntry = _Cdx6500T1E1VGContEntry_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 4, 19, 1)
)
cdx6500T1E1VGContEntry.setIndexNames(
    (0, "T1E1VG-OPT-MIB", "t1e1vgContIfNumber"),
)
if mibBuilder.loadTexts:
    cdx6500T1E1VGContEntry.setStatus("mandatory")
_T1e1vgContIfNumber_Type = Integer32
_T1e1vgContIfNumber_Object = MibTableColumn
t1e1vgContIfNumber = _T1e1vgContIfNumber_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 4, 19, 1, 1),
    _T1e1vgContIfNumber_Type()
)
t1e1vgContIfNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    t1e1vgContIfNumber.setStatus("mandatory")


class _T1e1vgContIfBoot_Type(Integer32):
    """Custom type t1e1vgContIfBoot based on Integer32"""
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


_T1e1vgContIfBoot_Type.__name__ = "Integer32"
_T1e1vgContIfBoot_Object = MibTableColumn
t1e1vgContIfBoot = _T1e1vgContIfBoot_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 4, 19, 1, 2),
    _T1e1vgContIfBoot_Type()
)
t1e1vgContIfBoot.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    t1e1vgContIfBoot.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "T1E1VG-OPT-MIB",
    **{"DisplayString": DisplayString,
       "codex": codex,
       "cdxProductSpecific": cdxProductSpecific,
       "cdx6500": cdx6500,
       "cdx6500Configuration": cdx6500Configuration,
       "cdx6500CfgGeneralGroup": cdx6500CfgGeneralGroup,
       "cdx6500T1E1VGTable": cdx6500T1E1VGTable,
       "cdx6500T1E1VGEntry": cdx6500T1E1VGEntry,
       "cdx6500T1E1VGCfgEntryNumber": cdx6500T1E1VGCfgEntryNumber,
       "cdx6500T1E1VGCfgInterfaceType": cdx6500T1E1VGCfgInterfaceType,
       "cdx6500T1E1VGCfgFormat": cdx6500T1E1VGCfgFormat,
       "cdx6500T1E1VGCfgSwitchType": cdx6500T1E1VGCfgSwitchType,
       "cdx6500T1E1VGCfgUserNetworkSide": cdx6500T1E1VGCfgUserNetworkSide,
       "cdx6500T1E1VGCfgDirectBchannel": cdx6500T1E1VGCfgDirectBchannel,
       "cdx6500T1E1VGCfgBchRange": cdx6500T1E1VGCfgBchRange,
       "cdx6500T1E1VGCfgCallAddrReplace": cdx6500T1E1VGCfgCallAddrReplace,
       "cdx6500T1E1VGCfgIsdnQsigOpt": cdx6500T1E1VGCfgIsdnQsigOpt,
       "cdx6500T1E1VGCfgFilteredIE": cdx6500T1E1VGCfgFilteredIE,
       "cdx6500T1E1VGCfgReplIsdnQsig": cdx6500T1E1VGCfgReplIsdnQsig,
       "cdx6500T1E1VGCfgCallPartyNumType": cdx6500T1E1VGCfgCallPartyNumType,
       "cdx6500T1E1VGCfgCallPartyNumPlan": cdx6500T1E1VGCfgCallPartyNumPlan,
       "cdx6500T1E1VGCfg1stChanPort": cdx6500T1E1VGCfg1stChanPort,
       "cdx6500T1E1VGCfg1stChanSlot": cdx6500T1E1VGCfg1stChanSlot,
       "cdx6500T1E1VGCfg1stChanDS0Rate": cdx6500T1E1VGCfg1stChanDS0Rate,
       "cdx6500T1E1VGCfg2ndChanPort": cdx6500T1E1VGCfg2ndChanPort,
       "cdx6500T1E1VGCfg2ndChanSlot": cdx6500T1E1VGCfg2ndChanSlot,
       "cdx6500T1E1VGCfg2ndChanDS0Rate": cdx6500T1E1VGCfg2ndChanDS0Rate,
       "cdx6500T1E1VGCfg3rdChanPort": cdx6500T1E1VGCfg3rdChanPort,
       "cdx6500T1E1VGCfg3rdChanSlot": cdx6500T1E1VGCfg3rdChanSlot,
       "cdx6500T1E1VGCfg3rdChanDS0Rate": cdx6500T1E1VGCfg3rdChanDS0Rate,
       "cdx6500T1E1VGCfgLineFramingType": cdx6500T1E1VGCfgLineFramingType,
       "cdx6500T1E1VGCfgLineCoding": cdx6500T1E1VGCfgLineCoding,
       "cdx6500T1E1VGCfgTransmitClock": cdx6500T1E1VGCfgTransmitClock,
       "cdx6500T1E1VGCfgLineImpedance": cdx6500T1E1VGCfgLineImpedance,
       "cdx6500T1E1VGCfgLineBuildOut": cdx6500T1E1VGCfgLineBuildOut,
       "cdx6500T1E1VGCfgRecvSense": cdx6500T1E1VGCfgRecvSense,
       "cdx6500T1E1VGCfgFacilityDataLink": cdx6500T1E1VGCfgFacilityDataLink,
       "cdx6500T1E1VGCfgV54RecvRLBK": cdx6500T1E1VGCfgV54RecvRLBK,
       "cdx6500T1E1VGCfgThresholdValueLES": cdx6500T1E1VGCfgThresholdValueLES,
       "cdx6500T1E1VGCfgThresholdValueLCV": cdx6500T1E1VGCfgThresholdValueLCV,
       "cdx6500T1E1VGCfgThresholdValuePCV": cdx6500T1E1VGCfgThresholdValuePCV,
       "cdx6500T1E1VGCfgThresholdValueCSS": cdx6500T1E1VGCfgThresholdValueCSS,
       "cdx6500T1E1VGCfgThresholdValueES": cdx6500T1E1VGCfgThresholdValueES,
       "cdx6500T1E1VGCfgThresholdValueBES": cdx6500T1E1VGCfgThresholdValueBES,
       "cdx6500T1E1VGCfgThresholdValueSES": cdx6500T1E1VGCfgThresholdValueSES,
       "cdx6500T1E1VGCfgThresholdValueSEFS": cdx6500T1E1VGCfgThresholdValueSEFS,
       "cdx6500T1E1VGCfgThresholdValueUAS": cdx6500T1E1VGCfgThresholdValueUAS,
       "cdx6500T1E1VGCfgBchNumScheme": cdx6500T1E1VGCfgBchNumScheme,
       "cdx6500Statistics": cdx6500Statistics,
       "cdx6500StatOtherStatsGroup": cdx6500StatOtherStatsGroup,
       "cdx6500STT1E1VGGroup": cdx6500STT1E1VGGroup,
       "cdx6500STT1E1VGTable": cdx6500STT1E1VGTable,
       "cdx6500STT1E1VGEntry": cdx6500STT1E1VGEntry,
       "cdx6500T1E1VGStatIfNumber": cdx6500T1E1VGStatIfNumber,
       "cdx6500T1E1VGStatInterfaceType": cdx6500T1E1VGStatInterfaceType,
       "cdx6500T1E1VGStatTimeSinceLastReset": cdx6500T1E1VGStatTimeSinceLastReset,
       "cdx6500T1E1VGStatAlarmState": cdx6500T1E1VGStatAlarmState,
       "cdx6500T1E1VGStatChannelState": cdx6500T1E1VGStatChannelState,
       "cdx6500T1E1VGStatTotal24HoursReportTable": cdx6500T1E1VGStatTotal24HoursReportTable,
       "cdx6500T1E1VGStatTotal24HoursReportEntry": cdx6500T1E1VGStatTotal24HoursReportEntry,
       "cdx6500T1E1VGStatTotal24HoursReportIfNumber": cdx6500T1E1VGStatTotal24HoursReportIfNumber,
       "cdx6500T1E1VGStatTotal24HoursReportLES": cdx6500T1E1VGStatTotal24HoursReportLES,
       "cdx6500T1E1VGStatTotal24HoursReportLCV": cdx6500T1E1VGStatTotal24HoursReportLCV,
       "cdx6500T1E1VGStatTotal24HoursReportPCV": cdx6500T1E1VGStatTotal24HoursReportPCV,
       "cdx6500T1E1VGStatTotal24HoursReportCSS": cdx6500T1E1VGStatTotal24HoursReportCSS,
       "cdx6500T1E1VGStatTotal24HoursReportES": cdx6500T1E1VGStatTotal24HoursReportES,
       "cdx6500T1E1VGStatTotal24HoursReportBES": cdx6500T1E1VGStatTotal24HoursReportBES,
       "cdx6500T1E1VGStatTotal24HoursReportSES": cdx6500T1E1VGStatTotal24HoursReportSES,
       "cdx6500T1E1VGStatTotal24HoursReportSEFS": cdx6500T1E1VGStatTotal24HoursReportSEFS,
       "cdx6500T1E1VGStatTotal24HoursReportUAS": cdx6500T1E1VGStatTotal24HoursReportUAS,
       "cdx6500T1E1VGStatCurrent15MinutesReportTable": cdx6500T1E1VGStatCurrent15MinutesReportTable,
       "cdx6500T1E1VGStatCurrent15MinutesReportEntry": cdx6500T1E1VGStatCurrent15MinutesReportEntry,
       "cdx6500T1E1VGStatCurrent15MinutesReportIfNumber": cdx6500T1E1VGStatCurrent15MinutesReportIfNumber,
       "cdx6500T1E1VGStatCurrent15MinutesReportTimeElapsed": cdx6500T1E1VGStatCurrent15MinutesReportTimeElapsed,
       "cdx6500T1E1VGStatCurrent15MinutesReportLES": cdx6500T1E1VGStatCurrent15MinutesReportLES,
       "cdx6500T1E1VGStatCurrent15MinutesReportLCV": cdx6500T1E1VGStatCurrent15MinutesReportLCV,
       "cdx6500T1E1VGStatCurrent15MinutesReportPCV": cdx6500T1E1VGStatCurrent15MinutesReportPCV,
       "cdx6500T1E1VGStatCurrent15MinutesReportCSS": cdx6500T1E1VGStatCurrent15MinutesReportCSS,
       "cdx6500T1E1VGStatCurrent15MinutesReportES": cdx6500T1E1VGStatCurrent15MinutesReportES,
       "cdx6500T1E1VGStatCurrent15MinutesReportBES": cdx6500T1E1VGStatCurrent15MinutesReportBES,
       "cdx6500T1E1VGStatCurrent15MinutesReportSES": cdx6500T1E1VGStatCurrent15MinutesReportSES,
       "cdx6500T1E1VGStatCurrent15MinutesReportSEFS": cdx6500T1E1VGStatCurrent15MinutesReportSEFS,
       "cdx6500T1E1VGStatCurrent15MinutesReportUAS": cdx6500T1E1VGStatCurrent15MinutesReportUAS,
       "cdx6500T1E1VGStatT1ChannelStateTable": cdx6500T1E1VGStatT1ChannelStateTable,
       "cdx6500T1E1VGStatT1ChannelStateEntry": cdx6500T1E1VGStatT1ChannelStateEntry,
       "cdx6500T1E1VGStatT1ChannelStateIfNumber": cdx6500T1E1VGStatT1ChannelStateIfNumber,
       "cdx6500T1E1VGStatT1ChannelStateABCDNumber": cdx6500T1E1VGStatT1ChannelStateABCDNumber,
       "cdx6500T1E1VGStatT1ChannelStateCurrentRxState": cdx6500T1E1VGStatT1ChannelStateCurrentRxState,
       "cdx6500T1E1VGStatE1ABCDStateTable": cdx6500T1E1VGStatE1ABCDStateTable,
       "cdx6500T1E1VGStatE1ABCDStateEntry": cdx6500T1E1VGStatE1ABCDStateEntry,
       "cdx6500T1E1VGStatE1ABCDStateIfNumber": cdx6500T1E1VGStatE1ABCDStateIfNumber,
       "cdx6500T1E1VGStatE1ABCDStateChannelNumber": cdx6500T1E1VGStatE1ABCDStateChannelNumber,
       "cdx6500T1E1VGStatE1ABCDStateCurrentRxState": cdx6500T1E1VGStatE1ABCDStateCurrentRxState,
       "cdx6500Controls": cdx6500Controls,
       "cdx6500ContT1E1VGTable": cdx6500ContT1E1VGTable,
       "cdx6500T1E1VGContEntry": cdx6500T1E1VGContEntry,
       "t1e1vgContIfNumber": t1e1vgContIfNumber,
       "t1e1vgContIfBoot": t1e1vgContIfBoot}
)
