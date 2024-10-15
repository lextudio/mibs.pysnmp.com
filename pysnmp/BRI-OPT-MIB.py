# SNMP MIB module (BRI-OPT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/BRI-OPT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:49:13 2024
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
_Cdx6500PPCTISDN_ObjectIdentity = ObjectIdentity
cdx6500PPCTISDN = _Cdx6500PPCTISDN_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 26)
)
_Cdx6500PPCTBRIConfig_ObjectIdentity = ObjectIdentity
cdx6500PPCTBRIConfig = _Cdx6500PPCTBRIConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 26, 1)
)
_Cdx6500PPCTBRIPortTable_Object = MibTable
cdx6500PPCTBRIPortTable = _Cdx6500PPCTBRIPortTable_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 26, 1, 1)
)
if mibBuilder.loadTexts:
    cdx6500PPCTBRIPortTable.setStatus("mandatory")
_Cdx6500PPCTBRIPortEntry_Object = MibTableRow
cdx6500PPCTBRIPortEntry = _Cdx6500PPCTBRIPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 26, 1, 1, 1)
)
cdx6500PPCTBRIPortEntry.setIndexNames(
    (0, "BRI-OPT-MIB", "cdx6500BRICfgPortNumber"),
)
if mibBuilder.loadTexts:
    cdx6500PPCTBRIPortEntry.setStatus("mandatory")
_Cdx6500BRICfgPortNumber_Type = Integer32
_Cdx6500BRICfgPortNumber_Object = MibTableColumn
cdx6500BRICfgPortNumber = _Cdx6500BRICfgPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 26, 1, 1, 1, 1),
    _Cdx6500BRICfgPortNumber_Type()
)
cdx6500BRICfgPortNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500BRICfgPortNumber.setStatus("mandatory")


class _Cdx6500BRICfgPortType_Type(Integer32):
    """Custom type cdx6500BRICfgPortType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            40
        )
    )
    namedValues = NamedValues(
        ("bri", 40)
    )


_Cdx6500BRICfgPortType_Type.__name__ = "Integer32"
_Cdx6500BRICfgPortType_Object = MibTableColumn
cdx6500BRICfgPortType = _Cdx6500BRICfgPortType_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 26, 1, 1, 1, 2),
    _Cdx6500BRICfgPortType_Type()
)
cdx6500BRICfgPortType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500BRICfgPortType.setStatus("mandatory")


class _Cdx6500BRICfgSwitchType_Type(DisplayString):
    """Custom type cdx6500BRICfgSwitchType based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 24),
    )


_Cdx6500BRICfgSwitchType_Type.__name__ = "DisplayString"
_Cdx6500BRICfgSwitchType_Object = MibTableColumn
cdx6500BRICfgSwitchType = _Cdx6500BRICfgSwitchType_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 26, 1, 1, 1, 3),
    _Cdx6500BRICfgSwitchType_Type()
)
cdx6500BRICfgSwitchType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500BRICfgSwitchType.setStatus("mandatory")


class _Cdx6500BRICfgVmebug_Type(Integer32):
    """Custom type cdx6500BRICfgVmebug based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_Cdx6500BRICfgVmebug_Type.__name__ = "Integer32"
_Cdx6500BRICfgVmebug_Object = MibTableColumn
cdx6500BRICfgVmebug = _Cdx6500BRICfgVmebug_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 26, 1, 1, 1, 4),
    _Cdx6500BRICfgVmebug_Type()
)
cdx6500BRICfgVmebug.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500BRICfgVmebug.setStatus("mandatory")
_Cdx6500BRICfgTEI_Type = Integer32
_Cdx6500BRICfgTEI_Object = MibTableColumn
cdx6500BRICfgTEI = _Cdx6500BRICfgTEI_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 26, 1, 1, 1, 5),
    _Cdx6500BRICfgTEI_Type()
)
cdx6500BRICfgTEI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500BRICfgTEI.setStatus("mandatory")
_Cdx6500PPCTBRIChan_ObjectIdentity = ObjectIdentity
cdx6500PPCTBRIChan = _Cdx6500PPCTBRIChan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 26, 1, 2)
)
_Cdx6500PPCTBRIX25ChanTable_Object = MibTable
cdx6500PPCTBRIX25ChanTable = _Cdx6500PPCTBRIX25ChanTable_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 26, 1, 2, 1)
)
if mibBuilder.loadTexts:
    cdx6500PPCTBRIX25ChanTable.setStatus("mandatory")
_Cdx6500PPCTBRIX25ChanEntry_Object = MibTableRow
cdx6500PPCTBRIX25ChanEntry = _Cdx6500PPCTBRIX25ChanEntry_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 26, 1, 2, 1, 1)
)
cdx6500PPCTBRIX25ChanEntry.setIndexNames(
    (0, "BRI-OPT-MIB", "cdx6500BRIX25ChanCfgPortNumber"),
    (0, "BRI-OPT-MIB", "cdx6500BRIX25ChanCfgChannelNum"),
)
if mibBuilder.loadTexts:
    cdx6500PPCTBRIX25ChanEntry.setStatus("mandatory")
_Cdx6500BRIX25ChanCfgPortNumber_Type = Integer32
_Cdx6500BRIX25ChanCfgPortNumber_Object = MibTableColumn
cdx6500BRIX25ChanCfgPortNumber = _Cdx6500BRIX25ChanCfgPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 26, 1, 2, 1, 1, 1),
    _Cdx6500BRIX25ChanCfgPortNumber_Type()
)
cdx6500BRIX25ChanCfgPortNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500BRIX25ChanCfgPortNumber.setStatus("mandatory")


class _Cdx6500BRIX25ChanCfgChannelNum_Type(Integer32):
    """Custom type cdx6500BRIX25ChanCfgChannelNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3),
    )


_Cdx6500BRIX25ChanCfgChannelNum_Type.__name__ = "Integer32"
_Cdx6500BRIX25ChanCfgChannelNum_Object = MibTableColumn
cdx6500BRIX25ChanCfgChannelNum = _Cdx6500BRIX25ChanCfgChannelNum_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 26, 1, 2, 1, 1, 2),
    _Cdx6500BRIX25ChanCfgChannelNum_Type()
)
cdx6500BRIX25ChanCfgChannelNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500BRIX25ChanCfgChannelNum.setStatus("mandatory")


class _Cdx6500BRIX25ChanCfgChannelType_Type(Integer32):
    """Custom type cdx6500BRIX25ChanCfgChannelType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("bChannel", 3),
          ("dChannel", 4))
    )


_Cdx6500BRIX25ChanCfgChannelType_Type.__name__ = "Integer32"
_Cdx6500BRIX25ChanCfgChannelType_Object = MibTableColumn
cdx6500BRIX25ChanCfgChannelType = _Cdx6500BRIX25ChanCfgChannelType_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 26, 1, 2, 1, 1, 3),
    _Cdx6500BRIX25ChanCfgChannelType_Type()
)
cdx6500BRIX25ChanCfgChannelType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500BRIX25ChanCfgChannelType.setStatus("mandatory")


class _Cdx6500BRIX25ChanCfgAccessType_Type(Integer32):
    """Custom type cdx6500BRIX25ChanCfgAccessType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("permanent", 1),
          ("switched", 2))
    )


_Cdx6500BRIX25ChanCfgAccessType_Type.__name__ = "Integer32"
_Cdx6500BRIX25ChanCfgAccessType_Object = MibTableColumn
cdx6500BRIX25ChanCfgAccessType = _Cdx6500BRIX25ChanCfgAccessType_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 26, 1, 2, 1, 1, 4),
    _Cdx6500BRIX25ChanCfgAccessType_Type()
)
cdx6500BRIX25ChanCfgAccessType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500BRIX25ChanCfgAccessType.setStatus("mandatory")
_Cdx6500BRIX25ChanCfgTimeslot_Type = Integer32
_Cdx6500BRIX25ChanCfgTimeslot_Object = MibTableColumn
cdx6500BRIX25ChanCfgTimeslot = _Cdx6500BRIX25ChanCfgTimeslot_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 26, 1, 2, 1, 1, 5),
    _Cdx6500BRIX25ChanCfgTimeslot_Type()
)
cdx6500BRIX25ChanCfgTimeslot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500BRIX25ChanCfgTimeslot.setStatus("mandatory")


class _Cdx6500BRIX25ChanCfgSPID_Type(DisplayString):
    """Custom type cdx6500BRIX25ChanCfgSPID based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 21),
    )


_Cdx6500BRIX25ChanCfgSPID_Type.__name__ = "DisplayString"
_Cdx6500BRIX25ChanCfgSPID_Object = MibTableColumn
cdx6500BRIX25ChanCfgSPID = _Cdx6500BRIX25ChanCfgSPID_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 26, 1, 2, 1, 1, 6),
    _Cdx6500BRIX25ChanCfgSPID_Type()
)
cdx6500BRIX25ChanCfgSPID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500BRIX25ChanCfgSPID.setStatus("mandatory")


class _Cdx6500BRIX25ChanCfgISDNCallAcc_Type(Integer32):
    """Custom type cdx6500BRIX25ChanCfgISDNCallAcc based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3,
              5)
        )
    )
    namedValues = NamedValues(
        *(("addressOnly", 3),
          ("addressSubaddress", 5),
          ("allCalls", 2))
    )


_Cdx6500BRIX25ChanCfgISDNCallAcc_Type.__name__ = "Integer32"
_Cdx6500BRIX25ChanCfgISDNCallAcc_Object = MibTableColumn
cdx6500BRIX25ChanCfgISDNCallAcc = _Cdx6500BRIX25ChanCfgISDNCallAcc_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 26, 1, 2, 1, 1, 7),
    _Cdx6500BRIX25ChanCfgISDNCallAcc_Type()
)
cdx6500BRIX25ChanCfgISDNCallAcc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500BRIX25ChanCfgISDNCallAcc.setStatus("mandatory")


class _Cdx6500BRIX25ChanCfgLocalSubsAddr_Type(DisplayString):
    """Custom type cdx6500BRIX25ChanCfgLocalSubsAddr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 36),
    )


_Cdx6500BRIX25ChanCfgLocalSubsAddr_Type.__name__ = "DisplayString"
_Cdx6500BRIX25ChanCfgLocalSubsAddr_Object = MibTableColumn
cdx6500BRIX25ChanCfgLocalSubsAddr = _Cdx6500BRIX25ChanCfgLocalSubsAddr_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 26, 1, 2, 1, 1, 8),
    _Cdx6500BRIX25ChanCfgLocalSubsAddr_Type()
)
cdx6500BRIX25ChanCfgLocalSubsAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500BRIX25ChanCfgLocalSubsAddr.setStatus("mandatory")


class _Cdx6500BRIX25ChanCfgLocalSubsSubAddr_Type(DisplayString):
    """Custom type cdx6500BRIX25ChanCfgLocalSubsSubAddr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_Cdx6500BRIX25ChanCfgLocalSubsSubAddr_Type.__name__ = "DisplayString"
_Cdx6500BRIX25ChanCfgLocalSubsSubAddr_Object = MibTableColumn
cdx6500BRIX25ChanCfgLocalSubsSubAddr = _Cdx6500BRIX25ChanCfgLocalSubsSubAddr_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 26, 1, 2, 1, 1, 9),
    _Cdx6500BRIX25ChanCfgLocalSubsSubAddr_Type()
)
cdx6500BRIX25ChanCfgLocalSubsSubAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500BRIX25ChanCfgLocalSubsSubAddr.setStatus("mandatory")


class _Cdx6500BRIX25ChanCfgRateAdaption_Type(Integer32):
    """Custom type cdx6500BRIX25ChanCfgRateAdaption based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("rate56k", 1),
          ("rate64k", 2))
    )


_Cdx6500BRIX25ChanCfgRateAdaption_Type.__name__ = "Integer32"
_Cdx6500BRIX25ChanCfgRateAdaption_Object = MibTableColumn
cdx6500BRIX25ChanCfgRateAdaption = _Cdx6500BRIX25ChanCfgRateAdaption_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 26, 1, 2, 1, 1, 10),
    _Cdx6500BRIX25ChanCfgRateAdaption_Type()
)
cdx6500BRIX25ChanCfgRateAdaption.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500BRIX25ChanCfgRateAdaption.setStatus("mandatory")


class _Cdx6500BRIX25ChanCfgProtocolType_Type(Integer32):
    """Custom type cdx6500BRIX25ChanCfgProtocolType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("fri", 3),
          ("x25", 2))
    )


_Cdx6500BRIX25ChanCfgProtocolType_Type.__name__ = "Integer32"
_Cdx6500BRIX25ChanCfgProtocolType_Object = MibTableColumn
cdx6500BRIX25ChanCfgProtocolType = _Cdx6500BRIX25ChanCfgProtocolType_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 26, 1, 2, 1, 1, 11),
    _Cdx6500BRIX25ChanCfgProtocolType_Type()
)
cdx6500BRIX25ChanCfgProtocolType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500BRIX25ChanCfgProtocolType.setStatus("mandatory")


class _Cdx6500BRIX25ChanCfgLinkAddr_Type(Integer32):
    """Custom type cdx6500BRIX25ChanCfgLinkAddr based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dce", 2),
          ("dte", 1))
    )


_Cdx6500BRIX25ChanCfgLinkAddr_Type.__name__ = "Integer32"
_Cdx6500BRIX25ChanCfgLinkAddr_Object = MibTableColumn
cdx6500BRIX25ChanCfgLinkAddr = _Cdx6500BRIX25ChanCfgLinkAddr_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 26, 1, 2, 1, 1, 12),
    _Cdx6500BRIX25ChanCfgLinkAddr_Type()
)
cdx6500BRIX25ChanCfgLinkAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500BRIX25ChanCfgLinkAddr.setStatus("mandatory")


class _Cdx6500BRIX25ChanCfgNumPVCChannels_Type(Integer32):
    """Custom type cdx6500BRIX25ChanCfgNumPVCChannels based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Cdx6500BRIX25ChanCfgNumPVCChannels_Type.__name__ = "Integer32"
_Cdx6500BRIX25ChanCfgNumPVCChannels_Object = MibTableColumn
cdx6500BRIX25ChanCfgNumPVCChannels = _Cdx6500BRIX25ChanCfgNumPVCChannels_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 26, 1, 2, 1, 1, 13),
    _Cdx6500BRIX25ChanCfgNumPVCChannels_Type()
)
cdx6500BRIX25ChanCfgNumPVCChannels.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500BRIX25ChanCfgNumPVCChannels.setStatus("mandatory")


class _Cdx6500BRIX25ChanCfgStartPVCChanNum_Type(Integer32):
    """Custom type cdx6500BRIX25ChanCfgStartPVCChanNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_Cdx6500BRIX25ChanCfgStartPVCChanNum_Type.__name__ = "Integer32"
_Cdx6500BRIX25ChanCfgStartPVCChanNum_Object = MibTableColumn
cdx6500BRIX25ChanCfgStartPVCChanNum = _Cdx6500BRIX25ChanCfgStartPVCChanNum_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 26, 1, 2, 1, 1, 14),
    _Cdx6500BRIX25ChanCfgStartPVCChanNum_Type()
)
cdx6500BRIX25ChanCfgStartPVCChanNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500BRIX25ChanCfgStartPVCChanNum.setStatus("mandatory")


class _Cdx6500BRIX25ChanCfgBNumSVCChannels_Type(Integer32):
    """Custom type cdx6500BRIX25ChanCfgBNumSVCChannels based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 512),
    )


_Cdx6500BRIX25ChanCfgBNumSVCChannels_Type.__name__ = "Integer32"
_Cdx6500BRIX25ChanCfgBNumSVCChannels_Object = MibTableColumn
cdx6500BRIX25ChanCfgBNumSVCChannels = _Cdx6500BRIX25ChanCfgBNumSVCChannels_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 26, 1, 2, 1, 1, 15),
    _Cdx6500BRIX25ChanCfgBNumSVCChannels_Type()
)
cdx6500BRIX25ChanCfgBNumSVCChannels.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500BRIX25ChanCfgBNumSVCChannels.setStatus("mandatory")


class _Cdx6500BRIX25ChanCfgStartSVCChanNum_Type(Integer32):
    """Custom type cdx6500BRIX25ChanCfgStartSVCChanNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_Cdx6500BRIX25ChanCfgStartSVCChanNum_Type.__name__ = "Integer32"
_Cdx6500BRIX25ChanCfgStartSVCChanNum_Object = MibTableColumn
cdx6500BRIX25ChanCfgStartSVCChanNum = _Cdx6500BRIX25ChanCfgStartSVCChanNum_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 26, 1, 2, 1, 1, 16),
    _Cdx6500BRIX25ChanCfgStartSVCChanNum_Type()
)
cdx6500BRIX25ChanCfgStartSVCChanNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500BRIX25ChanCfgStartSVCChanNum.setStatus("mandatory")


class _Cdx6500BRIX25ChanCfgInitialFrame_Type(Integer32):
    """Custom type cdx6500BRIX25ChanCfgInitialFrame based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disc", 2),
          ("none", 3),
          ("sabm", 1))
    )


_Cdx6500BRIX25ChanCfgInitialFrame_Type.__name__ = "Integer32"
_Cdx6500BRIX25ChanCfgInitialFrame_Object = MibTableColumn
cdx6500BRIX25ChanCfgInitialFrame = _Cdx6500BRIX25ChanCfgInitialFrame_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 26, 1, 2, 1, 1, 17),
    _Cdx6500BRIX25ChanCfgInitialFrame_Type()
)
cdx6500BRIX25ChanCfgInitialFrame.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500BRIX25ChanCfgInitialFrame.setStatus("mandatory")


class _Cdx6500BRIX25ChanCfgT1TransRetryTimer_Type(Integer32):
    """Custom type cdx6500BRIX25ChanCfgT1TransRetryTimer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 254),
    )


_Cdx6500BRIX25ChanCfgT1TransRetryTimer_Type.__name__ = "Integer32"
_Cdx6500BRIX25ChanCfgT1TransRetryTimer_Object = MibTableColumn
cdx6500BRIX25ChanCfgT1TransRetryTimer = _Cdx6500BRIX25ChanCfgT1TransRetryTimer_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 26, 1, 2, 1, 1, 18),
    _Cdx6500BRIX25ChanCfgT1TransRetryTimer_Type()
)
cdx6500BRIX25ChanCfgT1TransRetryTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500BRIX25ChanCfgT1TransRetryTimer.setStatus("mandatory")
_Cdx6500BRIX25ChanCfgT4PollTimer_Type = Integer32
_Cdx6500BRIX25ChanCfgT4PollTimer_Object = MibTableColumn
cdx6500BRIX25ChanCfgT4PollTimer = _Cdx6500BRIX25ChanCfgT4PollTimer_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 26, 1, 2, 1, 1, 19),
    _Cdx6500BRIX25ChanCfgT4PollTimer_Type()
)
cdx6500BRIX25ChanCfgT4PollTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500BRIX25ChanCfgT4PollTimer.setStatus("mandatory")


class _Cdx6500BRIX25ChanCfgBN2TransTries_Type(Integer32):
    """Custom type cdx6500BRIX25ChanCfgBN2TransTries based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 20),
    )


_Cdx6500BRIX25ChanCfgBN2TransTries_Type.__name__ = "Integer32"
_Cdx6500BRIX25ChanCfgBN2TransTries_Object = MibTableColumn
cdx6500BRIX25ChanCfgBN2TransTries = _Cdx6500BRIX25ChanCfgBN2TransTries_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 26, 1, 2, 1, 1, 20),
    _Cdx6500BRIX25ChanCfgBN2TransTries_Type()
)
cdx6500BRIX25ChanCfgBN2TransTries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500BRIX25ChanCfgBN2TransTries.setStatus("mandatory")


class _Cdx6500BRIX25ChanCfgFrameSeqCount_Type(Integer32):
    """Custom type cdx6500BRIX25ChanCfgFrameSeqCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ext", 2),
          ("norm", 1))
    )


_Cdx6500BRIX25ChanCfgFrameSeqCount_Type.__name__ = "Integer32"
_Cdx6500BRIX25ChanCfgFrameSeqCount_Object = MibTableColumn
cdx6500BRIX25ChanCfgFrameSeqCount = _Cdx6500BRIX25ChanCfgFrameSeqCount_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 26, 1, 2, 1, 1, 21),
    _Cdx6500BRIX25ChanCfgFrameSeqCount_Type()
)
cdx6500BRIX25ChanCfgFrameSeqCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500BRIX25ChanCfgFrameSeqCount.setStatus("mandatory")


class _Cdx6500BRIX25ChanCfgBKFrameWindow_Type(Integer32):
    """Custom type cdx6500BRIX25ChanCfgBKFrameWindow based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_Cdx6500BRIX25ChanCfgBKFrameWindow_Type.__name__ = "Integer32"
_Cdx6500BRIX25ChanCfgBKFrameWindow_Object = MibTableColumn
cdx6500BRIX25ChanCfgBKFrameWindow = _Cdx6500BRIX25ChanCfgBKFrameWindow_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 26, 1, 2, 1, 1, 22),
    _Cdx6500BRIX25ChanCfgBKFrameWindow_Type()
)
cdx6500BRIX25ChanCfgBKFrameWindow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500BRIX25ChanCfgBKFrameWindow.setStatus("mandatory")


class _Cdx6500BRIX25ChanCfgPktSeqCount_Type(Integer32):
    """Custom type cdx6500BRIX25ChanCfgPktSeqCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ext", 2),
          ("norm", 1))
    )


_Cdx6500BRIX25ChanCfgPktSeqCount_Type.__name__ = "Integer32"
_Cdx6500BRIX25ChanCfgPktSeqCount_Object = MibTableColumn
cdx6500BRIX25ChanCfgPktSeqCount = _Cdx6500BRIX25ChanCfgPktSeqCount_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 26, 1, 2, 1, 1, 23),
    _Cdx6500BRIX25ChanCfgPktSeqCount_Type()
)
cdx6500BRIX25ChanCfgPktSeqCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500BRIX25ChanCfgPktSeqCount.setStatus("mandatory")


class _Cdx6500BRIX25ChanCfgBWPktWindow_Type(Integer32):
    """Custom type cdx6500BRIX25ChanCfgBWPktWindow based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_Cdx6500BRIX25ChanCfgBWPktWindow_Type.__name__ = "Integer32"
_Cdx6500BRIX25ChanCfgBWPktWindow_Object = MibTableColumn
cdx6500BRIX25ChanCfgBWPktWindow = _Cdx6500BRIX25ChanCfgBWPktWindow_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 26, 1, 2, 1, 1, 24),
    _Cdx6500BRIX25ChanCfgBWPktWindow_Type()
)
cdx6500BRIX25ChanCfgBWPktWindow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500BRIX25ChanCfgBWPktWindow.setStatus("mandatory")


class _Cdx6500BRIX25ChanCfgBPPktSize_Type(Integer32):
    """Custom type cdx6500BRIX25ChanCfgBPPktSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(8,
              9,
              10,
              11)
        )
    )
    namedValues = NamedValues(
        *(("s1024", 11),
          ("s128", 8),
          ("s256", 9),
          ("s512", 10))
    )


_Cdx6500BRIX25ChanCfgBPPktSize_Type.__name__ = "Integer32"
_Cdx6500BRIX25ChanCfgBPPktSize_Object = MibTableColumn
cdx6500BRIX25ChanCfgBPPktSize = _Cdx6500BRIX25ChanCfgBPPktSize_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 26, 1, 2, 1, 1, 25),
    _Cdx6500BRIX25ChanCfgBPPktSize_Type()
)
cdx6500BRIX25ChanCfgBPPktSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500BRIX25ChanCfgBPPktSize.setStatus("mandatory")


class _Cdx6500BRIX25ChanCfgMaxNegoPktSize_Type(Integer32):
    """Custom type cdx6500BRIX25ChanCfgMaxNegoPktSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(8,
              9,
              10,
              11)
        )
    )
    namedValues = NamedValues(
        *(("s1024", 11),
          ("s128", 8),
          ("s256", 9),
          ("s512", 10))
    )


_Cdx6500BRIX25ChanCfgMaxNegoPktSize_Type.__name__ = "Integer32"
_Cdx6500BRIX25ChanCfgMaxNegoPktSize_Object = MibTableColumn
cdx6500BRIX25ChanCfgMaxNegoPktSize = _Cdx6500BRIX25ChanCfgMaxNegoPktSize_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 26, 1, 2, 1, 1, 26),
    _Cdx6500BRIX25ChanCfgMaxNegoPktSize_Type()
)
cdx6500BRIX25ChanCfgMaxNegoPktSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500BRIX25ChanCfgMaxNegoPktSize.setStatus("mandatory")


class _Cdx6500BRIX25ChanCfgDataQUpperThres_Type(Integer32):
    """Custom type cdx6500BRIX25ChanCfgDataQUpperThres based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 15),
    )


_Cdx6500BRIX25ChanCfgDataQUpperThres_Type.__name__ = "Integer32"
_Cdx6500BRIX25ChanCfgDataQUpperThres_Object = MibTableColumn
cdx6500BRIX25ChanCfgDataQUpperThres = _Cdx6500BRIX25ChanCfgDataQUpperThres_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 26, 1, 2, 1, 1, 27),
    _Cdx6500BRIX25ChanCfgDataQUpperThres_Type()
)
cdx6500BRIX25ChanCfgDataQUpperThres.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500BRIX25ChanCfgDataQUpperThres.setStatus("mandatory")


class _Cdx6500BRIX25ChanCfgDataQLowerThres_Type(Integer32):
    """Custom type cdx6500BRIX25ChanCfgDataQLowerThres based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4),
    )


_Cdx6500BRIX25ChanCfgDataQLowerThres_Type.__name__ = "Integer32"
_Cdx6500BRIX25ChanCfgDataQLowerThres_Object = MibTableColumn
cdx6500BRIX25ChanCfgDataQLowerThres = _Cdx6500BRIX25ChanCfgDataQLowerThres_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 26, 1, 2, 1, 1, 28),
    _Cdx6500BRIX25ChanCfgDataQLowerThres_Type()
)
cdx6500BRIX25ChanCfgDataQLowerThres.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500BRIX25ChanCfgDataQLowerThres.setStatus("mandatory")


class _Cdx6500BRIX25ChanCfgRestartTimer_Type(Integer32):
    """Custom type cdx6500BRIX25ChanCfgRestartTimer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 255),
    )


_Cdx6500BRIX25ChanCfgRestartTimer_Type.__name__ = "Integer32"
_Cdx6500BRIX25ChanCfgRestartTimer_Object = MibTableColumn
cdx6500BRIX25ChanCfgRestartTimer = _Cdx6500BRIX25ChanCfgRestartTimer_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 26, 1, 2, 1, 1, 29),
    _Cdx6500BRIX25ChanCfgRestartTimer_Type()
)
cdx6500BRIX25ChanCfgRestartTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500BRIX25ChanCfgRestartTimer.setStatus("mandatory")


class _Cdx6500BRIX25ChanCfgResetTimer_Type(Integer32):
    """Custom type cdx6500BRIX25ChanCfgResetTimer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 255),
    )


_Cdx6500BRIX25ChanCfgResetTimer_Type.__name__ = "Integer32"
_Cdx6500BRIX25ChanCfgResetTimer_Object = MibTableColumn
cdx6500BRIX25ChanCfgResetTimer = _Cdx6500BRIX25ChanCfgResetTimer_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 26, 1, 2, 1, 1, 30),
    _Cdx6500BRIX25ChanCfgResetTimer_Type()
)
cdx6500BRIX25ChanCfgResetTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500BRIX25ChanCfgResetTimer.setStatus("mandatory")


class _Cdx6500BRIX25ChanCfgCallTimer_Type(Integer32):
    """Custom type cdx6500BRIX25ChanCfgCallTimer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 255),
    )


_Cdx6500BRIX25ChanCfgCallTimer_Type.__name__ = "Integer32"
_Cdx6500BRIX25ChanCfgCallTimer_Object = MibTableColumn
cdx6500BRIX25ChanCfgCallTimer = _Cdx6500BRIX25ChanCfgCallTimer_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 26, 1, 2, 1, 1, 31),
    _Cdx6500BRIX25ChanCfgCallTimer_Type()
)
cdx6500BRIX25ChanCfgCallTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500BRIX25ChanCfgCallTimer.setStatus("mandatory")


class _Cdx6500BRIX25ChanCfgClearTimer_Type(Integer32):
    """Custom type cdx6500BRIX25ChanCfgClearTimer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 255),
    )


_Cdx6500BRIX25ChanCfgClearTimer_Type.__name__ = "Integer32"
_Cdx6500BRIX25ChanCfgClearTimer_Object = MibTableColumn
cdx6500BRIX25ChanCfgClearTimer = _Cdx6500BRIX25ChanCfgClearTimer_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 26, 1, 2, 1, 1, 32),
    _Cdx6500BRIX25ChanCfgClearTimer_Type()
)
cdx6500BRIX25ChanCfgClearTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500BRIX25ChanCfgClearTimer.setStatus("mandatory")


class _Cdx6500BRIX25ChanCfgFacToDelFromOutbCalls_Type(DisplayString):
    """Custom type cdx6500BRIX25ChanCfgFacToDelFromOutbCalls based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(3, 17),
    )


_Cdx6500BRIX25ChanCfgFacToDelFromOutbCalls_Type.__name__ = "DisplayString"
_Cdx6500BRIX25ChanCfgFacToDelFromOutbCalls_Object = MibTableColumn
cdx6500BRIX25ChanCfgFacToDelFromOutbCalls = _Cdx6500BRIX25ChanCfgFacToDelFromOutbCalls_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 26, 1, 2, 1, 1, 33),
    _Cdx6500BRIX25ChanCfgFacToDelFromOutbCalls_Type()
)
cdx6500BRIX25ChanCfgFacToDelFromOutbCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500BRIX25ChanCfgFacToDelFromOutbCalls.setStatus("mandatory")


class _Cdx6500BRIX25ChanCfgFacToAddToOutbCalls_Type(DisplayString):
    """Custom type cdx6500BRIX25ChanCfgFacToAddToOutbCalls based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(3, 18),
    )


_Cdx6500BRIX25ChanCfgFacToAddToOutbCalls_Type.__name__ = "DisplayString"
_Cdx6500BRIX25ChanCfgFacToAddToOutbCalls_Object = MibTableColumn
cdx6500BRIX25ChanCfgFacToAddToOutbCalls = _Cdx6500BRIX25ChanCfgFacToAddToOutbCalls_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 26, 1, 2, 1, 1, 34),
    _Cdx6500BRIX25ChanCfgFacToAddToOutbCalls_Type()
)
cdx6500BRIX25ChanCfgFacToAddToOutbCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500BRIX25ChanCfgFacToAddToOutbCalls.setStatus("mandatory")


class _Cdx6500BRIX25ChanCfgFacToBarInOutbCalls_Type(DisplayString):
    """Custom type cdx6500BRIX25ChanCfgFacToBarInOutbCalls based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(3, 24),
    )


_Cdx6500BRIX25ChanCfgFacToBarInOutbCalls_Type.__name__ = "DisplayString"
_Cdx6500BRIX25ChanCfgFacToBarInOutbCalls_Object = MibTableColumn
cdx6500BRIX25ChanCfgFacToBarInOutbCalls = _Cdx6500BRIX25ChanCfgFacToBarInOutbCalls_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 26, 1, 2, 1, 1, 35),
    _Cdx6500BRIX25ChanCfgFacToBarInOutbCalls_Type()
)
cdx6500BRIX25ChanCfgFacToBarInOutbCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500BRIX25ChanCfgFacToBarInOutbCalls.setStatus("mandatory")


class _Cdx6500BRIX25ChanCfgFacToBarInInbCalls_Type(DisplayString):
    """Custom type cdx6500BRIX25ChanCfgFacToBarInInbCalls based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(3, 19),
    )


_Cdx6500BRIX25ChanCfgFacToBarInInbCalls_Type.__name__ = "DisplayString"
_Cdx6500BRIX25ChanCfgFacToBarInInbCalls_Object = MibTableColumn
cdx6500BRIX25ChanCfgFacToBarInInbCalls = _Cdx6500BRIX25ChanCfgFacToBarInInbCalls_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 26, 1, 2, 1, 1, 36),
    _Cdx6500BRIX25ChanCfgFacToBarInInbCalls_Type()
)
cdx6500BRIX25ChanCfgFacToBarInInbCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500BRIX25ChanCfgFacToBarInInbCalls.setStatus("mandatory")


class _Cdx6500BRIX25ChanCfgX25Options_Type(DisplayString):
    """Custom type cdx6500BRIX25ChanCfgX25Options based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(3, 107),
    )


_Cdx6500BRIX25ChanCfgX25Options_Type.__name__ = "DisplayString"
_Cdx6500BRIX25ChanCfgX25Options_Object = MibTableColumn
cdx6500BRIX25ChanCfgX25Options = _Cdx6500BRIX25ChanCfgX25Options_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 26, 1, 2, 1, 1, 37),
    _Cdx6500BRIX25ChanCfgX25Options_Type()
)
cdx6500BRIX25ChanCfgX25Options.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500BRIX25ChanCfgX25Options.setStatus("mandatory")


class _Cdx6500BRIX25ChanCfgNumRoutDgtInCallUsrData_Type(Integer32):
    """Custom type cdx6500BRIX25ChanCfgNumRoutDgtInCallUsrData based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 12),
    )


_Cdx6500BRIX25ChanCfgNumRoutDgtInCallUsrData_Type.__name__ = "Integer32"
_Cdx6500BRIX25ChanCfgNumRoutDgtInCallUsrData_Object = MibTableColumn
cdx6500BRIX25ChanCfgNumRoutDgtInCallUsrData = _Cdx6500BRIX25ChanCfgNumRoutDgtInCallUsrData_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 26, 1, 2, 1, 1, 38),
    _Cdx6500BRIX25ChanCfgNumRoutDgtInCallUsrData_Type()
)
cdx6500BRIX25ChanCfgNumRoutDgtInCallUsrData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500BRIX25ChanCfgNumRoutDgtInCallUsrData.setStatus("mandatory")


class _Cdx6500BRIX25ChanCfgNumPreAddrDgstrpOutgCalls_Type(Integer32):
    """Custom type cdx6500BRIX25ChanCfgNumPreAddrDgstrpOutgCalls based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 14),
    )


_Cdx6500BRIX25ChanCfgNumPreAddrDgstrpOutgCalls_Type.__name__ = "Integer32"
_Cdx6500BRIX25ChanCfgNumPreAddrDgstrpOutgCalls_Object = MibTableColumn
cdx6500BRIX25ChanCfgNumPreAddrDgstrpOutgCalls = _Cdx6500BRIX25ChanCfgNumPreAddrDgstrpOutgCalls_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 26, 1, 2, 1, 1, 39),
    _Cdx6500BRIX25ChanCfgNumPreAddrDgstrpOutgCalls_Type()
)
cdx6500BRIX25ChanCfgNumPreAddrDgstrpOutgCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500BRIX25ChanCfgNumPreAddrDgstrpOutgCalls.setStatus("mandatory")


class _Cdx6500BRIX25ChanCfgInDigitsToStrip_Type(Integer32):
    """Custom type cdx6500BRIX25ChanCfgInDigitsToStrip based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_Cdx6500BRIX25ChanCfgInDigitsToStrip_Type.__name__ = "Integer32"
_Cdx6500BRIX25ChanCfgInDigitsToStrip_Object = MibTableColumn
cdx6500BRIX25ChanCfgInDigitsToStrip = _Cdx6500BRIX25ChanCfgInDigitsToStrip_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 26, 1, 2, 1, 1, 40),
    _Cdx6500BRIX25ChanCfgInDigitsToStrip_Type()
)
cdx6500BRIX25ChanCfgInDigitsToStrip.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500BRIX25ChanCfgInDigitsToStrip.setStatus("mandatory")


class _Cdx6500BRIX25ChanCfgRestrictedConnDest_Type(DisplayString):
    """Custom type cdx6500BRIX25ChanCfgRestrictedConnDest based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Cdx6500BRIX25ChanCfgRestrictedConnDest_Type.__name__ = "DisplayString"
_Cdx6500BRIX25ChanCfgRestrictedConnDest_Object = MibTableColumn
cdx6500BRIX25ChanCfgRestrictedConnDest = _Cdx6500BRIX25ChanCfgRestrictedConnDest_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 26, 1, 2, 1, 1, 41),
    _Cdx6500BRIX25ChanCfgRestrictedConnDest_Type()
)
cdx6500BRIX25ChanCfgRestrictedConnDest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500BRIX25ChanCfgRestrictedConnDest.setStatus("mandatory")


class _Cdx6500BRIX25ChanCfgPortAddress_Type(DisplayString):
    """Custom type cdx6500BRIX25ChanCfgPortAddress based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_Cdx6500BRIX25ChanCfgPortAddress_Type.__name__ = "DisplayString"
_Cdx6500BRIX25ChanCfgPortAddress_Object = MibTableColumn
cdx6500BRIX25ChanCfgPortAddress = _Cdx6500BRIX25ChanCfgPortAddress_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 26, 1, 2, 1, 1, 42),
    _Cdx6500BRIX25ChanCfgPortAddress_Type()
)
cdx6500BRIX25ChanCfgPortAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500BRIX25ChanCfgPortAddress.setStatus("mandatory")


class _Cdx6500BRIX25ChanCfgCUGMembership_Type(DisplayString):
    """Custom type cdx6500BRIX25ChanCfgCUGMembership based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 23),
    )


_Cdx6500BRIX25ChanCfgCUGMembership_Type.__name__ = "DisplayString"
_Cdx6500BRIX25ChanCfgCUGMembership_Object = MibTableColumn
cdx6500BRIX25ChanCfgCUGMembership = _Cdx6500BRIX25ChanCfgCUGMembership_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 26, 1, 2, 1, 1, 43),
    _Cdx6500BRIX25ChanCfgCUGMembership_Type()
)
cdx6500BRIX25ChanCfgCUGMembership.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500BRIX25ChanCfgCUGMembership.setStatus("mandatory")


class _Cdx6500BRIX25ChanCfgBillingRecords_Type(Integer32):
    """Custom type cdx6500BRIX25ChanCfgBillingRecords based on Integer32"""
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


_Cdx6500BRIX25ChanCfgBillingRecords_Type.__name__ = "Integer32"
_Cdx6500BRIX25ChanCfgBillingRecords_Object = MibTableColumn
cdx6500BRIX25ChanCfgBillingRecords = _Cdx6500BRIX25ChanCfgBillingRecords_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 26, 1, 2, 1, 1, 44),
    _Cdx6500BRIX25ChanCfgBillingRecords_Type()
)
cdx6500BRIX25ChanCfgBillingRecords.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500BRIX25ChanCfgBillingRecords.setStatus("mandatory")


class _Cdx6500BRIX25ChanCfgSubAddrSize_Type(Integer32):
    """Custom type cdx6500BRIX25ChanCfgSubAddrSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_Cdx6500BRIX25ChanCfgSubAddrSize_Type.__name__ = "Integer32"
_Cdx6500BRIX25ChanCfgSubAddrSize_Object = MibTableColumn
cdx6500BRIX25ChanCfgSubAddrSize = _Cdx6500BRIX25ChanCfgSubAddrSize_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 26, 1, 2, 1, 1, 45),
    _Cdx6500BRIX25ChanCfgSubAddrSize_Type()
)
cdx6500BRIX25ChanCfgSubAddrSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500BRIX25ChanCfgSubAddrSize.setStatus("mandatory")


class _Cdx6500BRIX25ChanCfgCallSecurity_Type(Integer32):
    """Custom type cdx6500BRIX25ChanCfgCallSecurity based on Integer32"""
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


_Cdx6500BRIX25ChanCfgCallSecurity_Type.__name__ = "Integer32"
_Cdx6500BRIX25ChanCfgCallSecurity_Object = MibTableColumn
cdx6500BRIX25ChanCfgCallSecurity = _Cdx6500BRIX25ChanCfgCallSecurity_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 26, 1, 2, 1, 1, 46),
    _Cdx6500BRIX25ChanCfgCallSecurity_Type()
)
cdx6500BRIX25ChanCfgCallSecurity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500BRIX25ChanCfgCallSecurity.setStatus("mandatory")


class _Cdx6500BRIX25ChanCfgProtectionLevel_Type(Integer32):
    """Custom type cdx6500BRIX25ChanCfgProtectionLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("cpOnly", 2),
          ("fullDcp", 3),
          ("none", 1))
    )


_Cdx6500BRIX25ChanCfgProtectionLevel_Type.__name__ = "Integer32"
_Cdx6500BRIX25ChanCfgProtectionLevel_Object = MibTableColumn
cdx6500BRIX25ChanCfgProtectionLevel = _Cdx6500BRIX25ChanCfgProtectionLevel_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 26, 1, 2, 1, 1, 47),
    _Cdx6500BRIX25ChanCfgProtectionLevel_Type()
)
cdx6500BRIX25ChanCfgProtectionLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500BRIX25ChanCfgProtectionLevel.setStatus("mandatory")


class _Cdx6500BRIX25ChanCfgReconnTimeout_Type(Integer32):
    """Custom type cdx6500BRIX25ChanCfgReconnTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 128),
    )


_Cdx6500BRIX25ChanCfgReconnTimeout_Type.__name__ = "Integer32"
_Cdx6500BRIX25ChanCfgReconnTimeout_Object = MibTableColumn
cdx6500BRIX25ChanCfgReconnTimeout = _Cdx6500BRIX25ChanCfgReconnTimeout_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 26, 1, 2, 1, 1, 48),
    _Cdx6500BRIX25ChanCfgReconnTimeout_Type()
)
cdx6500BRIX25ChanCfgReconnTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500BRIX25ChanCfgReconnTimeout.setStatus("mandatory")


class _Cdx6500BRIX25ChanCfgReconnTriesLt_Type(Integer32):
    """Custom type cdx6500BRIX25ChanCfgReconnTriesLt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 127),
    )


_Cdx6500BRIX25ChanCfgReconnTriesLt_Type.__name__ = "Integer32"
_Cdx6500BRIX25ChanCfgReconnTriesLt_Object = MibTableColumn
cdx6500BRIX25ChanCfgReconnTriesLt = _Cdx6500BRIX25ChanCfgReconnTriesLt_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 26, 1, 2, 1, 1, 49),
    _Cdx6500BRIX25ChanCfgReconnTriesLt_Type()
)
cdx6500BRIX25ChanCfgReconnTriesLt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500BRIX25ChanCfgReconnTriesLt.setStatus("mandatory")
_Cdx6500BRIX25ChanCfgFacSubsCtl_Type = DisplayString
_Cdx6500BRIX25ChanCfgFacSubsCtl_Object = MibTableColumn
cdx6500BRIX25ChanCfgFacSubsCtl = _Cdx6500BRIX25ChanCfgFacSubsCtl_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 26, 1, 2, 1, 1, 50),
    _Cdx6500BRIX25ChanCfgFacSubsCtl_Type()
)
cdx6500BRIX25ChanCfgFacSubsCtl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500BRIX25ChanCfgFacSubsCtl.setStatus("mandatory")


class _Cdx6500BRIX25ChanCfgAlarmPriority_Type(Integer32):
    """Custom type cdx6500BRIX25ChanCfgAlarmPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("access", 2),
          ("network", 1))
    )


_Cdx6500BRIX25ChanCfgAlarmPriority_Type.__name__ = "Integer32"
_Cdx6500BRIX25ChanCfgAlarmPriority_Object = MibTableColumn
cdx6500BRIX25ChanCfgAlarmPriority = _Cdx6500BRIX25ChanCfgAlarmPriority_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 26, 1, 2, 1, 1, 51),
    _Cdx6500BRIX25ChanCfgAlarmPriority_Type()
)
cdx6500BRIX25ChanCfgAlarmPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500BRIX25ChanCfgAlarmPriority.setStatus("mandatory")


class _Cdx6500BRIX25ChanCfgChanTEI_Type(Integer32):
    """Custom type cdx6500BRIX25ChanCfgChanTEI based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 63),
    )


_Cdx6500BRIX25ChanCfgChanTEI_Type.__name__ = "Integer32"
_Cdx6500BRIX25ChanCfgChanTEI_Object = MibTableColumn
cdx6500BRIX25ChanCfgChanTEI = _Cdx6500BRIX25ChanCfgChanTEI_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 26, 1, 2, 1, 1, 52),
    _Cdx6500BRIX25ChanCfgChanTEI_Type()
)
cdx6500BRIX25ChanCfgChanTEI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500BRIX25ChanCfgChanTEI.setStatus("mandatory")


class _Cdx6500BRIX25ChanCfgX25NetworkType_Type(Integer32):
    """Custom type cdx6500BRIX25ChanCfgX25NetworkType based on Integer32"""
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
        *(("datanet", 4),
          ("pss", 3),
          ("telenet", 2),
          ("transpac", 1))
    )


_Cdx6500BRIX25ChanCfgX25NetworkType_Type.__name__ = "Integer32"
_Cdx6500BRIX25ChanCfgX25NetworkType_Object = MibTableColumn
cdx6500BRIX25ChanCfgX25NetworkType = _Cdx6500BRIX25ChanCfgX25NetworkType_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 26, 1, 2, 1, 1, 53),
    _Cdx6500BRIX25ChanCfgX25NetworkType_Type()
)
cdx6500BRIX25ChanCfgX25NetworkType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500BRIX25ChanCfgX25NetworkType.setStatus("mandatory")


class _Cdx6500BRIX25ChanCfgDNumSVCChannels_Type(Integer32):
    """Custom type cdx6500BRIX25ChanCfgDNumSVCChannels based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_Cdx6500BRIX25ChanCfgDNumSVCChannels_Type.__name__ = "Integer32"
_Cdx6500BRIX25ChanCfgDNumSVCChannels_Object = MibTableColumn
cdx6500BRIX25ChanCfgDNumSVCChannels = _Cdx6500BRIX25ChanCfgDNumSVCChannels_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 26, 1, 2, 1, 1, 54),
    _Cdx6500BRIX25ChanCfgDNumSVCChannels_Type()
)
cdx6500BRIX25ChanCfgDNumSVCChannels.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500BRIX25ChanCfgDNumSVCChannels.setStatus("mandatory")


class _Cdx6500BRIX25ChanCfgDWPktWindow_Type(Integer32):
    """Custom type cdx6500BRIX25ChanCfgDWPktWindow based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 7),
    )


_Cdx6500BRIX25ChanCfgDWPktWindow_Type.__name__ = "Integer32"
_Cdx6500BRIX25ChanCfgDWPktWindow_Object = MibTableColumn
cdx6500BRIX25ChanCfgDWPktWindow = _Cdx6500BRIX25ChanCfgDWPktWindow_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 26, 1, 2, 1, 1, 55),
    _Cdx6500BRIX25ChanCfgDWPktWindow_Type()
)
cdx6500BRIX25ChanCfgDWPktWindow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500BRIX25ChanCfgDWPktWindow.setStatus("mandatory")


class _Cdx6500BRIX25ChanCfgDPPktSize_Type(Integer32):
    """Custom type cdx6500BRIX25ChanCfgDPPktSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(6,
              7,
              8,
              9)
        )
    )
    namedValues = NamedValues(
        *(("psize128", 8),
          ("psize256", 9),
          ("psize32", 6),
          ("psize64", 7))
    )


_Cdx6500BRIX25ChanCfgDPPktSize_Type.__name__ = "Integer32"
_Cdx6500BRIX25ChanCfgDPPktSize_Object = MibTableColumn
cdx6500BRIX25ChanCfgDPPktSize = _Cdx6500BRIX25ChanCfgDPPktSize_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 26, 1, 2, 1, 1, 56),
    _Cdx6500BRIX25ChanCfgDPPktSize_Type()
)
cdx6500BRIX25ChanCfgDPPktSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500BRIX25ChanCfgDPPktSize.setStatus("mandatory")


class _Cdx6500BRIX25ChanCfgDKFrameWindow_Type(Integer32):
    """Custom type cdx6500BRIX25ChanCfgDKFrameWindow based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 7),
    )


_Cdx6500BRIX25ChanCfgDKFrameWindow_Type.__name__ = "Integer32"
_Cdx6500BRIX25ChanCfgDKFrameWindow_Object = MibTableColumn
cdx6500BRIX25ChanCfgDKFrameWindow = _Cdx6500BRIX25ChanCfgDKFrameWindow_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 26, 1, 2, 1, 1, 57),
    _Cdx6500BRIX25ChanCfgDKFrameWindow_Type()
)
cdx6500BRIX25ChanCfgDKFrameWindow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500BRIX25ChanCfgDKFrameWindow.setStatus("mandatory")


class _Cdx6500BRIX25ChanCfgDN2TransTries_Type(Integer32):
    """Custom type cdx6500BRIX25ChanCfgDN2TransTries based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 254),
    )


_Cdx6500BRIX25ChanCfgDN2TransTries_Type.__name__ = "Integer32"
_Cdx6500BRIX25ChanCfgDN2TransTries_Object = MibTableColumn
cdx6500BRIX25ChanCfgDN2TransTries = _Cdx6500BRIX25ChanCfgDN2TransTries_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 26, 1, 2, 1, 1, 58),
    _Cdx6500BRIX25ChanCfgDN2TransTries_Type()
)
cdx6500BRIX25ChanCfgDN2TransTries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500BRIX25ChanCfgDN2TransTries.setStatus("mandatory")


class _Cdx6500BRIX25ChanCfgT1Timer_Type(Integer32):
    """Custom type cdx6500BRIX25ChanCfgT1Timer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16383),
    )


_Cdx6500BRIX25ChanCfgT1Timer_Type.__name__ = "Integer32"
_Cdx6500BRIX25ChanCfgT1Timer_Object = MibTableColumn
cdx6500BRIX25ChanCfgT1Timer = _Cdx6500BRIX25ChanCfgT1Timer_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 26, 1, 2, 1, 1, 59),
    _Cdx6500BRIX25ChanCfgT1Timer_Type()
)
cdx6500BRIX25ChanCfgT1Timer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500BRIX25ChanCfgT1Timer.setStatus("mandatory")


class _Cdx6500BRIX25ChanCfgT2Timer_Type(Integer32):
    """Custom type cdx6500BRIX25ChanCfgT2Timer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16383),
    )


_Cdx6500BRIX25ChanCfgT2Timer_Type.__name__ = "Integer32"
_Cdx6500BRIX25ChanCfgT2Timer_Object = MibTableColumn
cdx6500BRIX25ChanCfgT2Timer = _Cdx6500BRIX25ChanCfgT2Timer_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 26, 1, 2, 1, 1, 60),
    _Cdx6500BRIX25ChanCfgT2Timer_Type()
)
cdx6500BRIX25ChanCfgT2Timer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500BRIX25ChanCfgT2Timer.setStatus("mandatory")


class _Cdx6500BRIX25ChanCfgLinkType_Type(Integer32):
    """Custom type cdx6500BRIX25ChanCfgLinkType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("dChannel", 1),
          ("v24Dce", 3),
          ("v24Dte", 2))
    )


_Cdx6500BRIX25ChanCfgLinkType_Type.__name__ = "Integer32"
_Cdx6500BRIX25ChanCfgLinkType_Object = MibTableColumn
cdx6500BRIX25ChanCfgLinkType = _Cdx6500BRIX25ChanCfgLinkType_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 26, 1, 2, 1, 1, 61),
    _Cdx6500BRIX25ChanCfgLinkType_Type()
)
cdx6500BRIX25ChanCfgLinkType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500BRIX25ChanCfgLinkType.setStatus("mandatory")


class _Cdx6500BRIX25ChanCfgAddrTrans_Type(DisplayString):
    """Custom type cdx6500BRIX25ChanCfgAddrTrans based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(3, 107),
    )


_Cdx6500BRIX25ChanCfgAddrTrans_Type.__name__ = "DisplayString"
_Cdx6500BRIX25ChanCfgAddrTrans_Object = MibTableColumn
cdx6500BRIX25ChanCfgAddrTrans = _Cdx6500BRIX25ChanCfgAddrTrans_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 26, 1, 2, 1, 1, 62),
    _Cdx6500BRIX25ChanCfgAddrTrans_Type()
)
cdx6500BRIX25ChanCfgAddrTrans.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500BRIX25ChanCfgAddrTrans.setStatus("mandatory")
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
_Cdx6500BRIStats_ObjectIdentity = ObjectIdentity
cdx6500BRIStats = _Cdx6500BRIStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 27)
)
_Cdx6500BRIPStatsTable_Object = MibTable
cdx6500BRIPStatsTable = _Cdx6500BRIPStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 27, 1)
)
if mibBuilder.loadTexts:
    cdx6500BRIPStatsTable.setStatus("mandatory")
_Cdx6500BRIPStatsTableEntry_Object = MibTableRow
cdx6500BRIPStatsTableEntry = _Cdx6500BRIPStatsTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 27, 1, 1)
)
cdx6500BRIPStatsTableEntry.setIndexNames(
    (0, "BRI-OPT-MIB", "cdx6500BRIPStatPortNumber"),
)
if mibBuilder.loadTexts:
    cdx6500BRIPStatsTableEntry.setStatus("mandatory")
_Cdx6500BRIPStatPortNumber_Type = Integer32
_Cdx6500BRIPStatPortNumber_Object = MibTableColumn
cdx6500BRIPStatPortNumber = _Cdx6500BRIPStatPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 27, 1, 1, 1),
    _Cdx6500BRIPStatPortNumber_Type()
)
cdx6500BRIPStatPortNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500BRIPStatPortNumber.setStatus("mandatory")


class _Cdx6500BRIPStatPortType_Type(Integer32):
    """Custom type cdx6500BRIPStatPortType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            40
        )
    )
    namedValues = NamedValues(
        ("bri", 40)
    )


_Cdx6500BRIPStatPortType_Type.__name__ = "Integer32"
_Cdx6500BRIPStatPortType_Object = MibTableColumn
cdx6500BRIPStatPortType = _Cdx6500BRIPStatPortType_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 27, 1, 1, 2),
    _Cdx6500BRIPStatPortType_Type()
)
cdx6500BRIPStatPortType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500BRIPStatPortType.setStatus("mandatory")


class _Cdx6500BRIPStatPortStatus_Type(DisplayString):
    """Custom type cdx6500BRIPStatPortStatus based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 8),
    )


_Cdx6500BRIPStatPortStatus_Type.__name__ = "DisplayString"
_Cdx6500BRIPStatPortStatus_Object = MibTableColumn
cdx6500BRIPStatPortStatus = _Cdx6500BRIPStatPortStatus_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 27, 1, 1, 3),
    _Cdx6500BRIPStatPortStatus_Type()
)
cdx6500BRIPStatPortStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500BRIPStatPortStatus.setStatus("mandatory")


class _Cdx6500BRIPStatNumConfigChannels_Type(Integer32):
    """Custom type cdx6500BRIPStatNumConfigChannels based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_Cdx6500BRIPStatNumConfigChannels_Type.__name__ = "Integer32"
_Cdx6500BRIPStatNumConfigChannels_Object = MibTableColumn
cdx6500BRIPStatNumConfigChannels = _Cdx6500BRIPStatNumConfigChannels_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 27, 1, 1, 4),
    _Cdx6500BRIPStatNumConfigChannels_Type()
)
cdx6500BRIPStatNumConfigChannels.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500BRIPStatNumConfigChannels.setStatus("mandatory")


class _Cdx6500BRIPStatSwitchType_Type(DisplayString):
    """Custom type cdx6500BRIPStatSwitchType based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 23),
    )


_Cdx6500BRIPStatSwitchType_Type.__name__ = "DisplayString"
_Cdx6500BRIPStatSwitchType_Object = MibTableColumn
cdx6500BRIPStatSwitchType = _Cdx6500BRIPStatSwitchType_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 27, 1, 1, 5),
    _Cdx6500BRIPStatSwitchType_Type()
)
cdx6500BRIPStatSwitchType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500BRIPStatSwitchType.setStatus("mandatory")
_Cdx6500BRIPStatTEI_Type = Integer32
_Cdx6500BRIPStatTEI_Object = MibTableColumn
cdx6500BRIPStatTEI = _Cdx6500BRIPStatTEI_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 27, 1, 1, 6),
    _Cdx6500BRIPStatTEI_Type()
)
cdx6500BRIPStatTEI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500BRIPStatTEI.setStatus("mandatory")
_Cdx6500BRIPStatLastStatsReset_Type = DisplayString
_Cdx6500BRIPStatLastStatsReset_Object = MibTableColumn
cdx6500BRIPStatLastStatsReset = _Cdx6500BRIPStatLastStatsReset_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 27, 1, 1, 7),
    _Cdx6500BRIPStatLastStatsReset_Type()
)
cdx6500BRIPStatLastStatsReset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500BRIPStatLastStatsReset.setStatus("mandatory")
_Cdx6500BRIPStatCharsInTot_Type = Counter32
_Cdx6500BRIPStatCharsInTot_Object = MibTableColumn
cdx6500BRIPStatCharsInTot = _Cdx6500BRIPStatCharsInTot_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 27, 1, 1, 8),
    _Cdx6500BRIPStatCharsInTot_Type()
)
cdx6500BRIPStatCharsInTot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500BRIPStatCharsInTot.setStatus("mandatory")
_Cdx6500BRIPStatCharsInPerSec_Type = Integer32
_Cdx6500BRIPStatCharsInPerSec_Object = MibTableColumn
cdx6500BRIPStatCharsInPerSec = _Cdx6500BRIPStatCharsInPerSec_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 27, 1, 1, 9),
    _Cdx6500BRIPStatCharsInPerSec_Type()
)
cdx6500BRIPStatCharsInPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500BRIPStatCharsInPerSec.setStatus("mandatory")
_Cdx6500BRIPStatCharsOutTot_Type = Counter32
_Cdx6500BRIPStatCharsOutTot_Object = MibTableColumn
cdx6500BRIPStatCharsOutTot = _Cdx6500BRIPStatCharsOutTot_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 27, 1, 1, 10),
    _Cdx6500BRIPStatCharsOutTot_Type()
)
cdx6500BRIPStatCharsOutTot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500BRIPStatCharsOutTot.setStatus("mandatory")
_Cdx6500BRIPStatCharsOutPerSec_Type = Integer32
_Cdx6500BRIPStatCharsOutPerSec_Object = MibTableColumn
cdx6500BRIPStatCharsOutPerSec = _Cdx6500BRIPStatCharsOutPerSec_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 27, 1, 1, 11),
    _Cdx6500BRIPStatCharsOutPerSec_Type()
)
cdx6500BRIPStatCharsOutPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500BRIPStatCharsOutPerSec.setStatus("mandatory")
_Cdx6500BRIPStatFramesInTot_Type = Counter32
_Cdx6500BRIPStatFramesInTot_Object = MibTableColumn
cdx6500BRIPStatFramesInTot = _Cdx6500BRIPStatFramesInTot_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 27, 1, 1, 12),
    _Cdx6500BRIPStatFramesInTot_Type()
)
cdx6500BRIPStatFramesInTot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500BRIPStatFramesInTot.setStatus("mandatory")
_Cdx6500BRIPStatFramesInPerSec_Type = Integer32
_Cdx6500BRIPStatFramesInPerSec_Object = MibTableColumn
cdx6500BRIPStatFramesInPerSec = _Cdx6500BRIPStatFramesInPerSec_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 27, 1, 1, 13),
    _Cdx6500BRIPStatFramesInPerSec_Type()
)
cdx6500BRIPStatFramesInPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500BRIPStatFramesInPerSec.setStatus("mandatory")
_Cdx6500BRIPStatFrameOutTot_Type = Counter32
_Cdx6500BRIPStatFrameOutTot_Object = MibTableColumn
cdx6500BRIPStatFrameOutTot = _Cdx6500BRIPStatFrameOutTot_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 27, 1, 1, 14),
    _Cdx6500BRIPStatFrameOutTot_Type()
)
cdx6500BRIPStatFrameOutTot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500BRIPStatFrameOutTot.setStatus("mandatory")
_Cdx6500BRIPStatFrameOutPerSec_Type = Integer32
_Cdx6500BRIPStatFrameOutPerSec_Object = MibTableColumn
cdx6500BRIPStatFrameOutPerSec = _Cdx6500BRIPStatFrameOutPerSec_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 27, 1, 1, 15),
    _Cdx6500BRIPStatFrameOutPerSec_Type()
)
cdx6500BRIPStatFrameOutPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500BRIPStatFrameOutPerSec.setStatus("mandatory")
_Cdx6500BRIPStatAvFrameSzIn_Type = Integer32
_Cdx6500BRIPStatAvFrameSzIn_Object = MibTableColumn
cdx6500BRIPStatAvFrameSzIn = _Cdx6500BRIPStatAvFrameSzIn_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 27, 1, 1, 16),
    _Cdx6500BRIPStatAvFrameSzIn_Type()
)
cdx6500BRIPStatAvFrameSzIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500BRIPStatAvFrameSzIn.setStatus("mandatory")
_Cdx6500BRIPStatAvFrameSzOut_Type = Integer32
_Cdx6500BRIPStatAvFrameSzOut_Object = MibTableColumn
cdx6500BRIPStatAvFrameSzOut = _Cdx6500BRIPStatAvFrameSzOut_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 27, 1, 1, 17),
    _Cdx6500BRIPStatAvFrameSzOut_Type()
)
cdx6500BRIPStatAvFrameSzOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500BRIPStatAvFrameSzOut.setStatus("mandatory")
_Cdx6500BRIPStatPortUtilIn_Type = Integer32
_Cdx6500BRIPStatPortUtilIn_Object = MibTableColumn
cdx6500BRIPStatPortUtilIn = _Cdx6500BRIPStatPortUtilIn_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 27, 1, 1, 18),
    _Cdx6500BRIPStatPortUtilIn_Type()
)
cdx6500BRIPStatPortUtilIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500BRIPStatPortUtilIn.setStatus("mandatory")
_Cdx6500BRIPStatPortUtilOut_Type = Integer32
_Cdx6500BRIPStatPortUtilOut_Object = MibTableColumn
cdx6500BRIPStatPortUtilOut = _Cdx6500BRIPStatPortUtilOut_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 27, 1, 1, 19),
    _Cdx6500BRIPStatPortUtilOut_Type()
)
cdx6500BRIPStatPortUtilOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500BRIPStatPortUtilOut.setStatus("mandatory")
_Cdx6500BRIPStatPortUtilInMax_Type = Integer32
_Cdx6500BRIPStatPortUtilInMax_Object = MibTableColumn
cdx6500BRIPStatPortUtilInMax = _Cdx6500BRIPStatPortUtilInMax_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 27, 1, 1, 20),
    _Cdx6500BRIPStatPortUtilInMax_Type()
)
cdx6500BRIPStatPortUtilInMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500BRIPStatPortUtilInMax.setStatus("mandatory")
_Cdx6500BRIPStatPortUtilOutMax_Type = Integer32
_Cdx6500BRIPStatPortUtilOutMax_Object = MibTableColumn
cdx6500BRIPStatPortUtilOutMax = _Cdx6500BRIPStatPortUtilOutMax_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 27, 1, 1, 21),
    _Cdx6500BRIPStatPortUtilOutMax_Type()
)
cdx6500BRIPStatPortUtilOutMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500BRIPStatPortUtilOutMax.setStatus("mandatory")
_Cdx6500BRIChanStatsTable_Object = MibTable
cdx6500BRIChanStatsTable = _Cdx6500BRIChanStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 27, 2)
)
if mibBuilder.loadTexts:
    cdx6500BRIChanStatsTable.setStatus("mandatory")
_Cdx6500BRIChanStatsTableEntry_Object = MibTableRow
cdx6500BRIChanStatsTableEntry = _Cdx6500BRIChanStatsTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 27, 2, 1)
)
cdx6500BRIChanStatsTableEntry.setIndexNames(
    (0, "BRI-OPT-MIB", "cdx6500BRICStatsPortNumber"),
    (0, "BRI-OPT-MIB", "cdx6500BRICStatsChannelNum"),
)
if mibBuilder.loadTexts:
    cdx6500BRIChanStatsTableEntry.setStatus("mandatory")
_Cdx6500BRICStatsPortNumber_Type = Integer32
_Cdx6500BRICStatsPortNumber_Object = MibTableColumn
cdx6500BRICStatsPortNumber = _Cdx6500BRICStatsPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 27, 2, 1, 1),
    _Cdx6500BRICStatsPortNumber_Type()
)
cdx6500BRICStatsPortNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500BRICStatsPortNumber.setStatus("mandatory")


class _Cdx6500BRICStatsChannelNum_Type(Integer32):
    """Custom type cdx6500BRICStatsChannelNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3),
    )


_Cdx6500BRICStatsChannelNum_Type.__name__ = "Integer32"
_Cdx6500BRICStatsChannelNum_Object = MibTableColumn
cdx6500BRICStatsChannelNum = _Cdx6500BRICStatsChannelNum_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 27, 2, 1, 2),
    _Cdx6500BRICStatsChannelNum_Type()
)
cdx6500BRICStatsChannelNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500BRICStatsChannelNum.setStatus("mandatory")
_Cdx6500BRICStatsChannelType_Type = DisplayString
_Cdx6500BRICStatsChannelType_Object = MibTableColumn
cdx6500BRICStatsChannelType = _Cdx6500BRICStatsChannelType_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 27, 2, 1, 3),
    _Cdx6500BRICStatsChannelType_Type()
)
cdx6500BRICStatsChannelType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500BRICStatsChannelType.setStatus("mandatory")
_Cdx6500BRICStatsAccessType_Type = DisplayString
_Cdx6500BRICStatsAccessType_Object = MibTableColumn
cdx6500BRICStatsAccessType = _Cdx6500BRICStatsAccessType_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 27, 2, 1, 4),
    _Cdx6500BRICStatsAccessType_Type()
)
cdx6500BRICStatsAccessType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500BRICStatsAccessType.setStatus("mandatory")
_Cdx6500BRICStatsProtocolType_Type = DisplayString
_Cdx6500BRICStatsProtocolType_Object = MibTableColumn
cdx6500BRICStatsProtocolType = _Cdx6500BRICStatsProtocolType_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 27, 2, 1, 5),
    _Cdx6500BRICStatsProtocolType_Type()
)
cdx6500BRICStatsProtocolType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500BRICStatsProtocolType.setStatus("mandatory")
_Cdx6500BRICStatsCallState_Type = DisplayString
_Cdx6500BRICStatsCallState_Object = MibTableColumn
cdx6500BRICStatsCallState = _Cdx6500BRICStatsCallState_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 27, 2, 1, 6),
    _Cdx6500BRICStatsCallState_Type()
)
cdx6500BRICStatsCallState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500BRICStatsCallState.setStatus("mandatory")
_Cdx6500BRICStatsChannelStatus_Type = DisplayString
_Cdx6500BRICStatsChannelStatus_Object = MibTableColumn
cdx6500BRICStatsChannelStatus = _Cdx6500BRICStatsChannelStatus_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 27, 2, 1, 7),
    _Cdx6500BRICStatsChannelStatus_Type()
)
cdx6500BRICStatsChannelStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500BRICStatsChannelStatus.setStatus("mandatory")
_Cdx6500BRICStatsInCurCallAddr_Type = DisplayString
_Cdx6500BRICStatsInCurCallAddr_Object = MibTableColumn
cdx6500BRICStatsInCurCallAddr = _Cdx6500BRICStatsInCurCallAddr_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 27, 2, 1, 8),
    _Cdx6500BRICStatsInCurCallAddr_Type()
)
cdx6500BRICStatsInCurCallAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500BRICStatsInCurCallAddr.setStatus("mandatory")
_Cdx6500BRICStatsInCurCallSubAddr_Type = DisplayString
_Cdx6500BRICStatsInCurCallSubAddr_Object = MibTableColumn
cdx6500BRICStatsInCurCallSubAddr = _Cdx6500BRICStatsInCurCallSubAddr_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 27, 2, 1, 9),
    _Cdx6500BRICStatsInCurCallSubAddr_Type()
)
cdx6500BRICStatsInCurCallSubAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500BRICStatsInCurCallSubAddr.setStatus("mandatory")
_Cdx6500BRICStatsInAvConnTm_Type = DisplayString
_Cdx6500BRICStatsInAvConnTm_Object = MibTableColumn
cdx6500BRICStatsInAvConnTm = _Cdx6500BRICStatsInAvConnTm_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 27, 2, 1, 10),
    _Cdx6500BRICStatsInAvConnTm_Type()
)
cdx6500BRICStatsInAvConnTm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500BRICStatsInAvConnTm.setStatus("mandatory")
_Cdx6500BRICStatsInCurConnTm_Type = DisplayString
_Cdx6500BRICStatsInCurConnTm_Object = MibTableColumn
cdx6500BRICStatsInCurConnTm = _Cdx6500BRICStatsInCurConnTm_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 27, 2, 1, 11),
    _Cdx6500BRICStatsInCurConnTm_Type()
)
cdx6500BRICStatsInCurConnTm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500BRICStatsInCurConnTm.setStatus("mandatory")
_Cdx6500BRICStatsInMinConnTm_Type = DisplayString
_Cdx6500BRICStatsInMinConnTm_Object = MibTableColumn
cdx6500BRICStatsInMinConnTm = _Cdx6500BRICStatsInMinConnTm_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 27, 2, 1, 12),
    _Cdx6500BRICStatsInMinConnTm_Type()
)
cdx6500BRICStatsInMinConnTm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500BRICStatsInMinConnTm.setStatus("mandatory")
_Cdx6500BRICStatsInMaxConnTm_Type = DisplayString
_Cdx6500BRICStatsInMaxConnTm_Object = MibTableColumn
cdx6500BRICStatsInMaxConnTm = _Cdx6500BRICStatsInMaxConnTm_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 27, 2, 1, 13),
    _Cdx6500BRICStatsInMaxConnTm_Type()
)
cdx6500BRICStatsInMaxConnTm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500BRICStatsInMaxConnTm.setStatus("mandatory")
_Cdx6500BRICStatsInNumSuccCalls_Type = Integer32
_Cdx6500BRICStatsInNumSuccCalls_Object = MibTableColumn
cdx6500BRICStatsInNumSuccCalls = _Cdx6500BRICStatsInNumSuccCalls_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 27, 2, 1, 14),
    _Cdx6500BRICStatsInNumSuccCalls_Type()
)
cdx6500BRICStatsInNumSuccCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500BRICStatsInNumSuccCalls.setStatus("mandatory")
_Cdx6500BRICStatsInNumFailCalls_Type = Integer32
_Cdx6500BRICStatsInNumFailCalls_Object = MibTableColumn
cdx6500BRICStatsInNumFailCalls = _Cdx6500BRICStatsInNumFailCalls_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 27, 2, 1, 15),
    _Cdx6500BRICStatsInNumFailCalls_Type()
)
cdx6500BRICStatsInNumFailCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500BRICStatsInNumFailCalls.setStatus("mandatory")
_Cdx6500BRICStatsOutCurCallAddr_Type = DisplayString
_Cdx6500BRICStatsOutCurCallAddr_Object = MibTableColumn
cdx6500BRICStatsOutCurCallAddr = _Cdx6500BRICStatsOutCurCallAddr_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 27, 2, 1, 16),
    _Cdx6500BRICStatsOutCurCallAddr_Type()
)
cdx6500BRICStatsOutCurCallAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500BRICStatsOutCurCallAddr.setStatus("mandatory")
_Cdx6500BRICStatsOutCurCallSubAddr_Type = DisplayString
_Cdx6500BRICStatsOutCurCallSubAddr_Object = MibTableColumn
cdx6500BRICStatsOutCurCallSubAddr = _Cdx6500BRICStatsOutCurCallSubAddr_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 27, 2, 1, 17),
    _Cdx6500BRICStatsOutCurCallSubAddr_Type()
)
cdx6500BRICStatsOutCurCallSubAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500BRICStatsOutCurCallSubAddr.setStatus("mandatory")
_Cdx6500BRICStatsOutAvConnTm_Type = DisplayString
_Cdx6500BRICStatsOutAvConnTm_Object = MibTableColumn
cdx6500BRICStatsOutAvConnTm = _Cdx6500BRICStatsOutAvConnTm_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 27, 2, 1, 18),
    _Cdx6500BRICStatsOutAvConnTm_Type()
)
cdx6500BRICStatsOutAvConnTm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500BRICStatsOutAvConnTm.setStatus("mandatory")
_Cdx6500BRICStatsOutCurConnTm_Type = DisplayString
_Cdx6500BRICStatsOutCurConnTm_Object = MibTableColumn
cdx6500BRICStatsOutCurConnTm = _Cdx6500BRICStatsOutCurConnTm_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 27, 2, 1, 19),
    _Cdx6500BRICStatsOutCurConnTm_Type()
)
cdx6500BRICStatsOutCurConnTm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500BRICStatsOutCurConnTm.setStatus("mandatory")
_Cdx6500BRICStatsOutMinConnTm_Type = DisplayString
_Cdx6500BRICStatsOutMinConnTm_Object = MibTableColumn
cdx6500BRICStatsOutMinConnTm = _Cdx6500BRICStatsOutMinConnTm_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 27, 2, 1, 20),
    _Cdx6500BRICStatsOutMinConnTm_Type()
)
cdx6500BRICStatsOutMinConnTm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500BRICStatsOutMinConnTm.setStatus("mandatory")
_Cdx6500BRICStatsOutMaxConnTm_Type = DisplayString
_Cdx6500BRICStatsOutMaxConnTm_Object = MibTableColumn
cdx6500BRICStatsOutMaxConnTm = _Cdx6500BRICStatsOutMaxConnTm_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 27, 2, 1, 21),
    _Cdx6500BRICStatsOutMaxConnTm_Type()
)
cdx6500BRICStatsOutMaxConnTm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500BRICStatsOutMaxConnTm.setStatus("mandatory")
_Cdx6500BRICStatsOutNumSuccCalls_Type = Integer32
_Cdx6500BRICStatsOutNumSuccCalls_Object = MibTableColumn
cdx6500BRICStatsOutNumSuccCalls = _Cdx6500BRICStatsOutNumSuccCalls_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 27, 2, 1, 22),
    _Cdx6500BRICStatsOutNumSuccCalls_Type()
)
cdx6500BRICStatsOutNumSuccCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500BRICStatsOutNumSuccCalls.setStatus("mandatory")
_Cdx6500BRICStatsOutNumFailCalls_Type = Integer32
_Cdx6500BRICStatsOutNumFailCalls_Object = MibTableColumn
cdx6500BRICStatsOutNumFailCalls = _Cdx6500BRICStatsOutNumFailCalls_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 27, 2, 1, 23),
    _Cdx6500BRICStatsOutNumFailCalls_Type()
)
cdx6500BRICStatsOutNumFailCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500BRICStatsOutNumFailCalls.setStatus("mandatory")
_Cdx6500BRICStatsMaxSVC_Type = Integer32
_Cdx6500BRICStatsMaxSVC_Object = MibTableColumn
cdx6500BRICStatsMaxSVC = _Cdx6500BRICStatsMaxSVC_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 27, 2, 1, 24),
    _Cdx6500BRICStatsMaxSVC_Type()
)
cdx6500BRICStatsMaxSVC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500BRICStatsMaxSVC.setStatus("mandatory")
_Cdx6500BRICStatsMaxPVC_Type = Integer32
_Cdx6500BRICStatsMaxPVC_Object = MibTableColumn
cdx6500BRICStatsMaxPVC = _Cdx6500BRICStatsMaxPVC_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 27, 2, 1, 25),
    _Cdx6500BRICStatsMaxPVC_Type()
)
cdx6500BRICStatsMaxPVC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500BRICStatsMaxPVC.setStatus("mandatory")
_Cdx6500BRICStatsCurSVC_Type = Integer32
_Cdx6500BRICStatsCurSVC_Object = MibTableColumn
cdx6500BRICStatsCurSVC = _Cdx6500BRICStatsCurSVC_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 27, 2, 1, 26),
    _Cdx6500BRICStatsCurSVC_Type()
)
cdx6500BRICStatsCurSVC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500BRICStatsCurSVC.setStatus("mandatory")
_Cdx6500BRICStatsCurPVC_Type = Integer32
_Cdx6500BRICStatsCurPVC_Object = MibTableColumn
cdx6500BRICStatsCurPVC = _Cdx6500BRICStatsCurPVC_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 27, 2, 1, 27),
    _Cdx6500BRICStatsCurPVC_Type()
)
cdx6500BRICStatsCurPVC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500BRICStatsCurPVC.setStatus("mandatory")
_Cdx6500BRICStatsLastRepReasonCodes_Type = DisplayString
_Cdx6500BRICStatsLastRepReasonCodes_Object = MibTableColumn
cdx6500BRICStatsLastRepReasonCodes = _Cdx6500BRICStatsLastRepReasonCodes_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 27, 2, 1, 28),
    _Cdx6500BRICStatsLastRepReasonCodes_Type()
)
cdx6500BRICStatsLastRepReasonCodes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500BRICStatsLastRepReasonCodes.setStatus("mandatory")
_Cdx6500BRICStatsLastStatsReset_Type = DisplayString
_Cdx6500BRICStatsLastStatsReset_Object = MibTableColumn
cdx6500BRICStatsLastStatsReset = _Cdx6500BRICStatsLastStatsReset_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 27, 2, 1, 29),
    _Cdx6500BRICStatsLastStatsReset_Type()
)
cdx6500BRICStatsLastStatsReset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500BRICStatsLastStatsReset.setStatus("mandatory")
_Cdx6500BRICStatsCharsInTot_Type = Counter32
_Cdx6500BRICStatsCharsInTot_Object = MibTableColumn
cdx6500BRICStatsCharsInTot = _Cdx6500BRICStatsCharsInTot_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 27, 2, 1, 30),
    _Cdx6500BRICStatsCharsInTot_Type()
)
cdx6500BRICStatsCharsInTot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500BRICStatsCharsInTot.setStatus("mandatory")
_Cdx6500BRICStatsCharsOutTot_Type = Counter32
_Cdx6500BRICStatsCharsOutTot_Object = MibTableColumn
cdx6500BRICStatsCharsOutTot = _Cdx6500BRICStatsCharsOutTot_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 27, 2, 1, 31),
    _Cdx6500BRICStatsCharsOutTot_Type()
)
cdx6500BRICStatsCharsOutTot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500BRICStatsCharsOutTot.setStatus("mandatory")
_Cdx6500BRICStatsCharsInPerSec_Type = Integer32
_Cdx6500BRICStatsCharsInPerSec_Object = MibTableColumn
cdx6500BRICStatsCharsInPerSec = _Cdx6500BRICStatsCharsInPerSec_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 27, 2, 1, 32),
    _Cdx6500BRICStatsCharsInPerSec_Type()
)
cdx6500BRICStatsCharsInPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500BRICStatsCharsInPerSec.setStatus("mandatory")
_Cdx6500BRICStatsCharsOutPerSec_Type = Integer32
_Cdx6500BRICStatsCharsOutPerSec_Object = MibTableColumn
cdx6500BRICStatsCharsOutPerSec = _Cdx6500BRICStatsCharsOutPerSec_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 27, 2, 1, 33),
    _Cdx6500BRICStatsCharsOutPerSec_Type()
)
cdx6500BRICStatsCharsOutPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500BRICStatsCharsOutPerSec.setStatus("mandatory")
_Cdx6500BRICStatsPktsInTot_Type = Counter32
_Cdx6500BRICStatsPktsInTot_Object = MibTableColumn
cdx6500BRICStatsPktsInTot = _Cdx6500BRICStatsPktsInTot_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 27, 2, 1, 34),
    _Cdx6500BRICStatsPktsInTot_Type()
)
cdx6500BRICStatsPktsInTot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500BRICStatsPktsInTot.setStatus("mandatory")
_Cdx6500BRICStatsPktsOutTot_Type = Counter32
_Cdx6500BRICStatsPktsOutTot_Object = MibTableColumn
cdx6500BRICStatsPktsOutTot = _Cdx6500BRICStatsPktsOutTot_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 27, 2, 1, 35),
    _Cdx6500BRICStatsPktsOutTot_Type()
)
cdx6500BRICStatsPktsOutTot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500BRICStatsPktsOutTot.setStatus("mandatory")
_Cdx6500BRICStatsPktsInPerSec_Type = Integer32
_Cdx6500BRICStatsPktsInPerSec_Object = MibTableColumn
cdx6500BRICStatsPktsInPerSec = _Cdx6500BRICStatsPktsInPerSec_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 27, 2, 1, 36),
    _Cdx6500BRICStatsPktsInPerSec_Type()
)
cdx6500BRICStatsPktsInPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500BRICStatsPktsInPerSec.setStatus("mandatory")
_Cdx6500BRICStatsPktsOutPerSec_Type = Integer32
_Cdx6500BRICStatsPktsOutPerSec_Object = MibTableColumn
cdx6500BRICStatsPktsOutPerSec = _Cdx6500BRICStatsPktsOutPerSec_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 27, 2, 1, 37),
    _Cdx6500BRICStatsPktsOutPerSec_Type()
)
cdx6500BRICStatsPktsOutPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500BRICStatsPktsOutPerSec.setStatus("mandatory")
_Cdx6500BRICStatsFramesInTot_Type = Counter32
_Cdx6500BRICStatsFramesInTot_Object = MibTableColumn
cdx6500BRICStatsFramesInTot = _Cdx6500BRICStatsFramesInTot_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 27, 2, 1, 38),
    _Cdx6500BRICStatsFramesInTot_Type()
)
cdx6500BRICStatsFramesInTot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500BRICStatsFramesInTot.setStatus("mandatory")
_Cdx6500BRICStatsFramesOutTot_Type = Counter32
_Cdx6500BRICStatsFramesOutTot_Object = MibTableColumn
cdx6500BRICStatsFramesOutTot = _Cdx6500BRICStatsFramesOutTot_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 27, 2, 1, 39),
    _Cdx6500BRICStatsFramesOutTot_Type()
)
cdx6500BRICStatsFramesOutTot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500BRICStatsFramesOutTot.setStatus("mandatory")
_Cdx6500BRICStatsFramesInPerSec_Type = Integer32
_Cdx6500BRICStatsFramesInPerSec_Object = MibTableColumn
cdx6500BRICStatsFramesInPerSec = _Cdx6500BRICStatsFramesInPerSec_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 27, 2, 1, 40),
    _Cdx6500BRICStatsFramesInPerSec_Type()
)
cdx6500BRICStatsFramesInPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500BRICStatsFramesInPerSec.setStatus("mandatory")
_Cdx6500BRICStatsFramesOutPerSec_Type = Integer32
_Cdx6500BRICStatsFramesOutPerSec_Object = MibTableColumn
cdx6500BRICStatsFramesOutPerSec = _Cdx6500BRICStatsFramesOutPerSec_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 27, 2, 1, 41),
    _Cdx6500BRICStatsFramesOutPerSec_Type()
)
cdx6500BRICStatsFramesOutPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500BRICStatsFramesOutPerSec.setStatus("mandatory")
_Cdx6500BRICStatsInfoFramesIn_Type = Counter32
_Cdx6500BRICStatsInfoFramesIn_Object = MibTableColumn
cdx6500BRICStatsInfoFramesIn = _Cdx6500BRICStatsInfoFramesIn_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 27, 2, 1, 42),
    _Cdx6500BRICStatsInfoFramesIn_Type()
)
cdx6500BRICStatsInfoFramesIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500BRICStatsInfoFramesIn.setStatus("mandatory")
_Cdx6500BRICStatsInfoFramesOut_Type = Counter32
_Cdx6500BRICStatsInfoFramesOut_Object = MibTableColumn
cdx6500BRICStatsInfoFramesOut = _Cdx6500BRICStatsInfoFramesOut_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 27, 2, 1, 43),
    _Cdx6500BRICStatsInfoFramesOut_Type()
)
cdx6500BRICStatsInfoFramesOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500BRICStatsInfoFramesOut.setStatus("mandatory")
_Cdx6500BRICStatsRNRFramesIn_Type = Counter32
_Cdx6500BRICStatsRNRFramesIn_Object = MibTableColumn
cdx6500BRICStatsRNRFramesIn = _Cdx6500BRICStatsRNRFramesIn_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 27, 2, 1, 44),
    _Cdx6500BRICStatsRNRFramesIn_Type()
)
cdx6500BRICStatsRNRFramesIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500BRICStatsRNRFramesIn.setStatus("mandatory")
_Cdx6500BRICStatsRNRFramesOut_Type = Counter32
_Cdx6500BRICStatsRNRFramesOut_Object = MibTableColumn
cdx6500BRICStatsRNRFramesOut = _Cdx6500BRICStatsRNRFramesOut_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 27, 2, 1, 45),
    _Cdx6500BRICStatsRNRFramesOut_Type()
)
cdx6500BRICStatsRNRFramesOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500BRICStatsRNRFramesOut.setStatus("mandatory")
_Cdx6500BRICStatsSABMFramesIn_Type = Counter32
_Cdx6500BRICStatsSABMFramesIn_Object = MibTableColumn
cdx6500BRICStatsSABMFramesIn = _Cdx6500BRICStatsSABMFramesIn_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 27, 2, 1, 46),
    _Cdx6500BRICStatsSABMFramesIn_Type()
)
cdx6500BRICStatsSABMFramesIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500BRICStatsSABMFramesIn.setStatus("mandatory")
_Cdx6500BRICStatsSABMFramesOut_Type = Counter32
_Cdx6500BRICStatsSABMFramesOut_Object = MibTableColumn
cdx6500BRICStatsSABMFramesOut = _Cdx6500BRICStatsSABMFramesOut_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 27, 2, 1, 47),
    _Cdx6500BRICStatsSABMFramesOut_Type()
)
cdx6500BRICStatsSABMFramesOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500BRICStatsSABMFramesOut.setStatus("mandatory")
_Cdx6500BRICStatsDMFramesIn_Type = Counter32
_Cdx6500BRICStatsDMFramesIn_Object = MibTableColumn
cdx6500BRICStatsDMFramesIn = _Cdx6500BRICStatsDMFramesIn_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 27, 2, 1, 48),
    _Cdx6500BRICStatsDMFramesIn_Type()
)
cdx6500BRICStatsDMFramesIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500BRICStatsDMFramesIn.setStatus("mandatory")
_Cdx6500BRICStatsDMFramesOut_Type = Counter32
_Cdx6500BRICStatsDMFramesOut_Object = MibTableColumn
cdx6500BRICStatsDMFramesOut = _Cdx6500BRICStatsDMFramesOut_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 27, 2, 1, 49),
    _Cdx6500BRICStatsDMFramesOut_Type()
)
cdx6500BRICStatsDMFramesOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500BRICStatsDMFramesOut.setStatus("mandatory")
_Cdx6500BRICStatsRRFramesIn_Type = Counter32
_Cdx6500BRICStatsRRFramesIn_Object = MibTableColumn
cdx6500BRICStatsRRFramesIn = _Cdx6500BRICStatsRRFramesIn_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 27, 2, 1, 50),
    _Cdx6500BRICStatsRRFramesIn_Type()
)
cdx6500BRICStatsRRFramesIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500BRICStatsRRFramesIn.setStatus("mandatory")
_Cdx6500BRICStatsRRFramesOut_Type = Counter32
_Cdx6500BRICStatsRRFramesOut_Object = MibTableColumn
cdx6500BRICStatsRRFramesOut = _Cdx6500BRICStatsRRFramesOut_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 27, 2, 1, 51),
    _Cdx6500BRICStatsRRFramesOut_Type()
)
cdx6500BRICStatsRRFramesOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500BRICStatsRRFramesOut.setStatus("mandatory")
_Cdx6500BRICStatsREJFramesIn_Type = Counter32
_Cdx6500BRICStatsREJFramesIn_Object = MibTableColumn
cdx6500BRICStatsREJFramesIn = _Cdx6500BRICStatsREJFramesIn_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 27, 2, 1, 52),
    _Cdx6500BRICStatsREJFramesIn_Type()
)
cdx6500BRICStatsREJFramesIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500BRICStatsREJFramesIn.setStatus("mandatory")
_Cdx6500BRICStatsREJFramesOut_Type = Counter32
_Cdx6500BRICStatsREJFramesOut_Object = MibTableColumn
cdx6500BRICStatsREJFramesOut = _Cdx6500BRICStatsREJFramesOut_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 27, 2, 1, 53),
    _Cdx6500BRICStatsREJFramesOut_Type()
)
cdx6500BRICStatsREJFramesOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500BRICStatsREJFramesOut.setStatus("mandatory")
_Cdx6500BRICStatsDISCFramesIn_Type = Counter32
_Cdx6500BRICStatsDISCFramesIn_Object = MibTableColumn
cdx6500BRICStatsDISCFramesIn = _Cdx6500BRICStatsDISCFramesIn_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 27, 2, 1, 54),
    _Cdx6500BRICStatsDISCFramesIn_Type()
)
cdx6500BRICStatsDISCFramesIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500BRICStatsDISCFramesIn.setStatus("mandatory")
_Cdx6500BRICStatsDISCFramesOut_Type = Counter32
_Cdx6500BRICStatsDISCFramesOut_Object = MibTableColumn
cdx6500BRICStatsDISCFramesOut = _Cdx6500BRICStatsDISCFramesOut_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 27, 2, 1, 55),
    _Cdx6500BRICStatsDISCFramesOut_Type()
)
cdx6500BRICStatsDISCFramesOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500BRICStatsDISCFramesOut.setStatus("mandatory")
_Cdx6500BRICStatsUAFramesIn_Type = Counter32
_Cdx6500BRICStatsUAFramesIn_Object = MibTableColumn
cdx6500BRICStatsUAFramesIn = _Cdx6500BRICStatsUAFramesIn_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 27, 2, 1, 56),
    _Cdx6500BRICStatsUAFramesIn_Type()
)
cdx6500BRICStatsUAFramesIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500BRICStatsUAFramesIn.setStatus("mandatory")
_Cdx6500BRICStatsUAFramesOut_Type = Counter32
_Cdx6500BRICStatsUAFramesOut_Object = MibTableColumn
cdx6500BRICStatsUAFramesOut = _Cdx6500BRICStatsUAFramesOut_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 27, 2, 1, 57),
    _Cdx6500BRICStatsUAFramesOut_Type()
)
cdx6500BRICStatsUAFramesOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500BRICStatsUAFramesOut.setStatus("mandatory")
_Cdx6500BRICStatsFRMRFramesIn_Type = Counter32
_Cdx6500BRICStatsFRMRFramesIn_Object = MibTableColumn
cdx6500BRICStatsFRMRFramesIn = _Cdx6500BRICStatsFRMRFramesIn_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 27, 2, 1, 58),
    _Cdx6500BRICStatsFRMRFramesIn_Type()
)
cdx6500BRICStatsFRMRFramesIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500BRICStatsFRMRFramesIn.setStatus("mandatory")
_Cdx6500BRICStatsFRMRFramesOut_Type = Counter32
_Cdx6500BRICStatsFRMRFramesOut_Object = MibTableColumn
cdx6500BRICStatsFRMRFramesOut = _Cdx6500BRICStatsFRMRFramesOut_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 27, 2, 1, 59),
    _Cdx6500BRICStatsFRMRFramesOut_Type()
)
cdx6500BRICStatsFRMRFramesOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500BRICStatsFRMRFramesOut.setStatus("mandatory")
_Cdx6500BRICStatsDataPktsIn_Type = Counter32
_Cdx6500BRICStatsDataPktsIn_Object = MibTableColumn
cdx6500BRICStatsDataPktsIn = _Cdx6500BRICStatsDataPktsIn_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 27, 2, 1, 60),
    _Cdx6500BRICStatsDataPktsIn_Type()
)
cdx6500BRICStatsDataPktsIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500BRICStatsDataPktsIn.setStatus("mandatory")
_Cdx6500BRICStatsDataPktsOut_Type = Counter32
_Cdx6500BRICStatsDataPktsOut_Object = MibTableColumn
cdx6500BRICStatsDataPktsOut = _Cdx6500BRICStatsDataPktsOut_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 27, 2, 1, 61),
    _Cdx6500BRICStatsDataPktsOut_Type()
)
cdx6500BRICStatsDataPktsOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500BRICStatsDataPktsOut.setStatus("mandatory")
_Cdx6500BRICStatsRRPktsIn_Type = Counter32
_Cdx6500BRICStatsRRPktsIn_Object = MibTableColumn
cdx6500BRICStatsRRPktsIn = _Cdx6500BRICStatsRRPktsIn_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 27, 2, 1, 62),
    _Cdx6500BRICStatsRRPktsIn_Type()
)
cdx6500BRICStatsRRPktsIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500BRICStatsRRPktsIn.setStatus("mandatory")
_Cdx6500BRICStatsRRPktsOut_Type = Counter32
_Cdx6500BRICStatsRRPktsOut_Object = MibTableColumn
cdx6500BRICStatsRRPktsOut = _Cdx6500BRICStatsRRPktsOut_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 27, 2, 1, 63),
    _Cdx6500BRICStatsRRPktsOut_Type()
)
cdx6500BRICStatsRRPktsOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500BRICStatsRRPktsOut.setStatus("mandatory")
_Cdx6500BRICStatsRNRPktsIn_Type = Counter32
_Cdx6500BRICStatsRNRPktsIn_Object = MibTableColumn
cdx6500BRICStatsRNRPktsIn = _Cdx6500BRICStatsRNRPktsIn_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 27, 2, 1, 64),
    _Cdx6500BRICStatsRNRPktsIn_Type()
)
cdx6500BRICStatsRNRPktsIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500BRICStatsRNRPktsIn.setStatus("mandatory")
_Cdx6500BRICStatsRNRPktsOut_Type = Counter32
_Cdx6500BRICStatsRNRPktsOut_Object = MibTableColumn
cdx6500BRICStatsRNRPktsOut = _Cdx6500BRICStatsRNRPktsOut_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 27, 2, 1, 65),
    _Cdx6500BRICStatsRNRPktsOut_Type()
)
cdx6500BRICStatsRNRPktsOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500BRICStatsRNRPktsOut.setStatus("mandatory")
_Cdx6500BRICStatsRejPktsIn_Type = Counter32
_Cdx6500BRICStatsRejPktsIn_Object = MibTableColumn
cdx6500BRICStatsRejPktsIn = _Cdx6500BRICStatsRejPktsIn_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 27, 2, 1, 66),
    _Cdx6500BRICStatsRejPktsIn_Type()
)
cdx6500BRICStatsRejPktsIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500BRICStatsRejPktsIn.setStatus("mandatory")
_Cdx6500BRICStatsRejPktsOut_Type = Counter32
_Cdx6500BRICStatsRejPktsOut_Object = MibTableColumn
cdx6500BRICStatsRejPktsOut = _Cdx6500BRICStatsRejPktsOut_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 27, 2, 1, 67),
    _Cdx6500BRICStatsRejPktsOut_Type()
)
cdx6500BRICStatsRejPktsOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500BRICStatsRejPktsOut.setStatus("mandatory")
_Cdx6500BRICStatsCallReqPktsIn_Type = Counter32
_Cdx6500BRICStatsCallReqPktsIn_Object = MibTableColumn
cdx6500BRICStatsCallReqPktsIn = _Cdx6500BRICStatsCallReqPktsIn_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 27, 2, 1, 68),
    _Cdx6500BRICStatsCallReqPktsIn_Type()
)
cdx6500BRICStatsCallReqPktsIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500BRICStatsCallReqPktsIn.setStatus("mandatory")
_Cdx6500BRICStatsCallReqPktsOut_Type = Counter32
_Cdx6500BRICStatsCallReqPktsOut_Object = MibTableColumn
cdx6500BRICStatsCallReqPktsOut = _Cdx6500BRICStatsCallReqPktsOut_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 27, 2, 1, 69),
    _Cdx6500BRICStatsCallReqPktsOut_Type()
)
cdx6500BRICStatsCallReqPktsOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500BRICStatsCallReqPktsOut.setStatus("mandatory")
_Cdx6500BRICStatsCallAccPktsIn_Type = Counter32
_Cdx6500BRICStatsCallAccPktsIn_Object = MibTableColumn
cdx6500BRICStatsCallAccPktsIn = _Cdx6500BRICStatsCallAccPktsIn_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 27, 2, 1, 70),
    _Cdx6500BRICStatsCallAccPktsIn_Type()
)
cdx6500BRICStatsCallAccPktsIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500BRICStatsCallAccPktsIn.setStatus("mandatory")
_Cdx6500BRICStatsCallAccPktsOut_Type = Counter32
_Cdx6500BRICStatsCallAccPktsOut_Object = MibTableColumn
cdx6500BRICStatsCallAccPktsOut = _Cdx6500BRICStatsCallAccPktsOut_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 27, 2, 1, 71),
    _Cdx6500BRICStatsCallAccPktsOut_Type()
)
cdx6500BRICStatsCallAccPktsOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500BRICStatsCallAccPktsOut.setStatus("mandatory")
_Cdx6500BRICStatsClrReqPktsIn_Type = Counter32
_Cdx6500BRICStatsClrReqPktsIn_Object = MibTableColumn
cdx6500BRICStatsClrReqPktsIn = _Cdx6500BRICStatsClrReqPktsIn_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 27, 2, 1, 72),
    _Cdx6500BRICStatsClrReqPktsIn_Type()
)
cdx6500BRICStatsClrReqPktsIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500BRICStatsClrReqPktsIn.setStatus("mandatory")
_Cdx6500BRICStatsClrReqPktsOut_Type = Counter32
_Cdx6500BRICStatsClrReqPktsOut_Object = MibTableColumn
cdx6500BRICStatsClrReqPktsOut = _Cdx6500BRICStatsClrReqPktsOut_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 27, 2, 1, 73),
    _Cdx6500BRICStatsClrReqPktsOut_Type()
)
cdx6500BRICStatsClrReqPktsOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500BRICStatsClrReqPktsOut.setStatus("mandatory")
_Cdx6500BRICStatsClrConfPktsIn_Type = Counter32
_Cdx6500BRICStatsClrConfPktsIn_Object = MibTableColumn
cdx6500BRICStatsClrConfPktsIn = _Cdx6500BRICStatsClrConfPktsIn_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 27, 2, 1, 74),
    _Cdx6500BRICStatsClrConfPktsIn_Type()
)
cdx6500BRICStatsClrConfPktsIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500BRICStatsClrConfPktsIn.setStatus("mandatory")
_Cdx6500BRICStatsClrConfPktsOut_Type = Counter32
_Cdx6500BRICStatsClrConfPktsOut_Object = MibTableColumn
cdx6500BRICStatsClrConfPktsOut = _Cdx6500BRICStatsClrConfPktsOut_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 27, 2, 1, 75),
    _Cdx6500BRICStatsClrConfPktsOut_Type()
)
cdx6500BRICStatsClrConfPktsOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500BRICStatsClrConfPktsOut.setStatus("mandatory")
_Cdx6500BRICStatsIntReqPktsIn_Type = Counter32
_Cdx6500BRICStatsIntReqPktsIn_Object = MibTableColumn
cdx6500BRICStatsIntReqPktsIn = _Cdx6500BRICStatsIntReqPktsIn_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 27, 2, 1, 76),
    _Cdx6500BRICStatsIntReqPktsIn_Type()
)
cdx6500BRICStatsIntReqPktsIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500BRICStatsIntReqPktsIn.setStatus("mandatory")
_Cdx6500BRICStatsIntReqPktsOut_Type = Counter32
_Cdx6500BRICStatsIntReqPktsOut_Object = MibTableColumn
cdx6500BRICStatsIntReqPktsOut = _Cdx6500BRICStatsIntReqPktsOut_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 27, 2, 1, 77),
    _Cdx6500BRICStatsIntReqPktsOut_Type()
)
cdx6500BRICStatsIntReqPktsOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500BRICStatsIntReqPktsOut.setStatus("mandatory")
_Cdx6500BRICStatsIntConfPktsIn_Type = Counter32
_Cdx6500BRICStatsIntConfPktsIn_Object = MibTableColumn
cdx6500BRICStatsIntConfPktsIn = _Cdx6500BRICStatsIntConfPktsIn_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 27, 2, 1, 78),
    _Cdx6500BRICStatsIntConfPktsIn_Type()
)
cdx6500BRICStatsIntConfPktsIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500BRICStatsIntConfPktsIn.setStatus("mandatory")
_Cdx6500BRICStatsIntConfPktsOut_Type = Counter32
_Cdx6500BRICStatsIntConfPktsOut_Object = MibTableColumn
cdx6500BRICStatsIntConfPktsOut = _Cdx6500BRICStatsIntConfPktsOut_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 27, 2, 1, 79),
    _Cdx6500BRICStatsIntConfPktsOut_Type()
)
cdx6500BRICStatsIntConfPktsOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500BRICStatsIntConfPktsOut.setStatus("mandatory")
_Cdx6500BRICStatsRstReqPktsIn_Type = Counter32
_Cdx6500BRICStatsRstReqPktsIn_Object = MibTableColumn
cdx6500BRICStatsRstReqPktsIn = _Cdx6500BRICStatsRstReqPktsIn_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 27, 2, 1, 80),
    _Cdx6500BRICStatsRstReqPktsIn_Type()
)
cdx6500BRICStatsRstReqPktsIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500BRICStatsRstReqPktsIn.setStatus("mandatory")
_Cdx6500BRICStatsRstReqPktsOut_Type = Counter32
_Cdx6500BRICStatsRstReqPktsOut_Object = MibTableColumn
cdx6500BRICStatsRstReqPktsOut = _Cdx6500BRICStatsRstReqPktsOut_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 27, 2, 1, 81),
    _Cdx6500BRICStatsRstReqPktsOut_Type()
)
cdx6500BRICStatsRstReqPktsOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500BRICStatsRstReqPktsOut.setStatus("mandatory")
_Cdx6500BRICStatsRstConfPktsIn_Type = Counter32
_Cdx6500BRICStatsRstConfPktsIn_Object = MibTableColumn
cdx6500BRICStatsRstConfPktsIn = _Cdx6500BRICStatsRstConfPktsIn_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 27, 2, 1, 82),
    _Cdx6500BRICStatsRstConfPktsIn_Type()
)
cdx6500BRICStatsRstConfPktsIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500BRICStatsRstConfPktsIn.setStatus("mandatory")
_Cdx6500BRICStatsRstConfPktsOut_Type = Counter32
_Cdx6500BRICStatsRstConfPktsOut_Object = MibTableColumn
cdx6500BRICStatsRstConfPktsOut = _Cdx6500BRICStatsRstConfPktsOut_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 27, 2, 1, 83),
    _Cdx6500BRICStatsRstConfPktsOut_Type()
)
cdx6500BRICStatsRstConfPktsOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500BRICStatsRstConfPktsOut.setStatus("mandatory")
_Cdx6500BRICStatsRestartReqPktsIn_Type = Counter32
_Cdx6500BRICStatsRestartReqPktsIn_Object = MibTableColumn
cdx6500BRICStatsRestartReqPktsIn = _Cdx6500BRICStatsRestartReqPktsIn_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 27, 2, 1, 84),
    _Cdx6500BRICStatsRestartReqPktsIn_Type()
)
cdx6500BRICStatsRestartReqPktsIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500BRICStatsRestartReqPktsIn.setStatus("mandatory")
_Cdx6500BRICStatsRestartReqPktsOut_Type = Counter32
_Cdx6500BRICStatsRestartReqPktsOut_Object = MibTableColumn
cdx6500BRICStatsRestartReqPktsOut = _Cdx6500BRICStatsRestartReqPktsOut_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 27, 2, 1, 85),
    _Cdx6500BRICStatsRestartReqPktsOut_Type()
)
cdx6500BRICStatsRestartReqPktsOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500BRICStatsRestartReqPktsOut.setStatus("mandatory")
_Cdx6500BRICStatsRestartConfPktsIn_Type = Counter32
_Cdx6500BRICStatsRestartConfPktsIn_Object = MibTableColumn
cdx6500BRICStatsRestartConfPktsIn = _Cdx6500BRICStatsRestartConfPktsIn_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 27, 2, 1, 86),
    _Cdx6500BRICStatsRestartConfPktsIn_Type()
)
cdx6500BRICStatsRestartConfPktsIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500BRICStatsRestartConfPktsIn.setStatus("mandatory")
_Cdx6500BRICStatsRestartConfPktsOut_Type = Counter32
_Cdx6500BRICStatsRestartConfPktsOut_Object = MibTableColumn
cdx6500BRICStatsRestartConfPktsOut = _Cdx6500BRICStatsRestartConfPktsOut_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 27, 2, 1, 87),
    _Cdx6500BRICStatsRestartConfPktsOut_Type()
)
cdx6500BRICStatsRestartConfPktsOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500BRICStatsRestartConfPktsOut.setStatus("mandatory")
_Cdx6500BRICStatsTEI_Type = Integer32
_Cdx6500BRICStatsTEI_Object = MibTableColumn
cdx6500BRICStatsTEI = _Cdx6500BRICStatsTEI_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 27, 2, 1, 88),
    _Cdx6500BRICStatsTEI_Type()
)
cdx6500BRICStatsTEI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500BRICStatsTEI.setStatus("mandatory")
_Cdx6500BRICStatsSAPI_Type = Integer32
_Cdx6500BRICStatsSAPI_Object = MibTableColumn
cdx6500BRICStatsSAPI = _Cdx6500BRICStatsSAPI_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 27, 2, 1, 89),
    _Cdx6500BRICStatsSAPI_Type()
)
cdx6500BRICStatsSAPI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500BRICStatsSAPI.setStatus("mandatory")
_Cdx6500BRICStatsNetworkType_Type = DisplayString
_Cdx6500BRICStatsNetworkType_Object = MibTableColumn
cdx6500BRICStatsNetworkType = _Cdx6500BRICStatsNetworkType_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 27, 2, 1, 90),
    _Cdx6500BRICStatsNetworkType_Type()
)
cdx6500BRICStatsNetworkType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500BRICStatsNetworkType.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "BRI-OPT-MIB",
    **{"DisplayString": DisplayString,
       "codex": codex,
       "cdxProductSpecific": cdxProductSpecific,
       "cdx6500": cdx6500,
       "cdx6500Configuration": cdx6500Configuration,
       "cdx6500CfgProtocolGroup": cdx6500CfgProtocolGroup,
       "cdx6500PCTPortProtocolGroup": cdx6500PCTPortProtocolGroup,
       "cdx6500PPCTISDN": cdx6500PPCTISDN,
       "cdx6500PPCTBRIConfig": cdx6500PPCTBRIConfig,
       "cdx6500PPCTBRIPortTable": cdx6500PPCTBRIPortTable,
       "cdx6500PPCTBRIPortEntry": cdx6500PPCTBRIPortEntry,
       "cdx6500BRICfgPortNumber": cdx6500BRICfgPortNumber,
       "cdx6500BRICfgPortType": cdx6500BRICfgPortType,
       "cdx6500BRICfgSwitchType": cdx6500BRICfgSwitchType,
       "cdx6500BRICfgVmebug": cdx6500BRICfgVmebug,
       "cdx6500BRICfgTEI": cdx6500BRICfgTEI,
       "cdx6500PPCTBRIChan": cdx6500PPCTBRIChan,
       "cdx6500PPCTBRIX25ChanTable": cdx6500PPCTBRIX25ChanTable,
       "cdx6500PPCTBRIX25ChanEntry": cdx6500PPCTBRIX25ChanEntry,
       "cdx6500BRIX25ChanCfgPortNumber": cdx6500BRIX25ChanCfgPortNumber,
       "cdx6500BRIX25ChanCfgChannelNum": cdx6500BRIX25ChanCfgChannelNum,
       "cdx6500BRIX25ChanCfgChannelType": cdx6500BRIX25ChanCfgChannelType,
       "cdx6500BRIX25ChanCfgAccessType": cdx6500BRIX25ChanCfgAccessType,
       "cdx6500BRIX25ChanCfgTimeslot": cdx6500BRIX25ChanCfgTimeslot,
       "cdx6500BRIX25ChanCfgSPID": cdx6500BRIX25ChanCfgSPID,
       "cdx6500BRIX25ChanCfgISDNCallAcc": cdx6500BRIX25ChanCfgISDNCallAcc,
       "cdx6500BRIX25ChanCfgLocalSubsAddr": cdx6500BRIX25ChanCfgLocalSubsAddr,
       "cdx6500BRIX25ChanCfgLocalSubsSubAddr": cdx6500BRIX25ChanCfgLocalSubsSubAddr,
       "cdx6500BRIX25ChanCfgRateAdaption": cdx6500BRIX25ChanCfgRateAdaption,
       "cdx6500BRIX25ChanCfgProtocolType": cdx6500BRIX25ChanCfgProtocolType,
       "cdx6500BRIX25ChanCfgLinkAddr": cdx6500BRIX25ChanCfgLinkAddr,
       "cdx6500BRIX25ChanCfgNumPVCChannels": cdx6500BRIX25ChanCfgNumPVCChannels,
       "cdx6500BRIX25ChanCfgStartPVCChanNum": cdx6500BRIX25ChanCfgStartPVCChanNum,
       "cdx6500BRIX25ChanCfgBNumSVCChannels": cdx6500BRIX25ChanCfgBNumSVCChannels,
       "cdx6500BRIX25ChanCfgStartSVCChanNum": cdx6500BRIX25ChanCfgStartSVCChanNum,
       "cdx6500BRIX25ChanCfgInitialFrame": cdx6500BRIX25ChanCfgInitialFrame,
       "cdx6500BRIX25ChanCfgT1TransRetryTimer": cdx6500BRIX25ChanCfgT1TransRetryTimer,
       "cdx6500BRIX25ChanCfgT4PollTimer": cdx6500BRIX25ChanCfgT4PollTimer,
       "cdx6500BRIX25ChanCfgBN2TransTries": cdx6500BRIX25ChanCfgBN2TransTries,
       "cdx6500BRIX25ChanCfgFrameSeqCount": cdx6500BRIX25ChanCfgFrameSeqCount,
       "cdx6500BRIX25ChanCfgBKFrameWindow": cdx6500BRIX25ChanCfgBKFrameWindow,
       "cdx6500BRIX25ChanCfgPktSeqCount": cdx6500BRIX25ChanCfgPktSeqCount,
       "cdx6500BRIX25ChanCfgBWPktWindow": cdx6500BRIX25ChanCfgBWPktWindow,
       "cdx6500BRIX25ChanCfgBPPktSize": cdx6500BRIX25ChanCfgBPPktSize,
       "cdx6500BRIX25ChanCfgMaxNegoPktSize": cdx6500BRIX25ChanCfgMaxNegoPktSize,
       "cdx6500BRIX25ChanCfgDataQUpperThres": cdx6500BRIX25ChanCfgDataQUpperThres,
       "cdx6500BRIX25ChanCfgDataQLowerThres": cdx6500BRIX25ChanCfgDataQLowerThres,
       "cdx6500BRIX25ChanCfgRestartTimer": cdx6500BRIX25ChanCfgRestartTimer,
       "cdx6500BRIX25ChanCfgResetTimer": cdx6500BRIX25ChanCfgResetTimer,
       "cdx6500BRIX25ChanCfgCallTimer": cdx6500BRIX25ChanCfgCallTimer,
       "cdx6500BRIX25ChanCfgClearTimer": cdx6500BRIX25ChanCfgClearTimer,
       "cdx6500BRIX25ChanCfgFacToDelFromOutbCalls": cdx6500BRIX25ChanCfgFacToDelFromOutbCalls,
       "cdx6500BRIX25ChanCfgFacToAddToOutbCalls": cdx6500BRIX25ChanCfgFacToAddToOutbCalls,
       "cdx6500BRIX25ChanCfgFacToBarInOutbCalls": cdx6500BRIX25ChanCfgFacToBarInOutbCalls,
       "cdx6500BRIX25ChanCfgFacToBarInInbCalls": cdx6500BRIX25ChanCfgFacToBarInInbCalls,
       "cdx6500BRIX25ChanCfgX25Options": cdx6500BRIX25ChanCfgX25Options,
       "cdx6500BRIX25ChanCfgNumRoutDgtInCallUsrData": cdx6500BRIX25ChanCfgNumRoutDgtInCallUsrData,
       "cdx6500BRIX25ChanCfgNumPreAddrDgstrpOutgCalls": cdx6500BRIX25ChanCfgNumPreAddrDgstrpOutgCalls,
       "cdx6500BRIX25ChanCfgInDigitsToStrip": cdx6500BRIX25ChanCfgInDigitsToStrip,
       "cdx6500BRIX25ChanCfgRestrictedConnDest": cdx6500BRIX25ChanCfgRestrictedConnDest,
       "cdx6500BRIX25ChanCfgPortAddress": cdx6500BRIX25ChanCfgPortAddress,
       "cdx6500BRIX25ChanCfgCUGMembership": cdx6500BRIX25ChanCfgCUGMembership,
       "cdx6500BRIX25ChanCfgBillingRecords": cdx6500BRIX25ChanCfgBillingRecords,
       "cdx6500BRIX25ChanCfgSubAddrSize": cdx6500BRIX25ChanCfgSubAddrSize,
       "cdx6500BRIX25ChanCfgCallSecurity": cdx6500BRIX25ChanCfgCallSecurity,
       "cdx6500BRIX25ChanCfgProtectionLevel": cdx6500BRIX25ChanCfgProtectionLevel,
       "cdx6500BRIX25ChanCfgReconnTimeout": cdx6500BRIX25ChanCfgReconnTimeout,
       "cdx6500BRIX25ChanCfgReconnTriesLt": cdx6500BRIX25ChanCfgReconnTriesLt,
       "cdx6500BRIX25ChanCfgFacSubsCtl": cdx6500BRIX25ChanCfgFacSubsCtl,
       "cdx6500BRIX25ChanCfgAlarmPriority": cdx6500BRIX25ChanCfgAlarmPriority,
       "cdx6500BRIX25ChanCfgChanTEI": cdx6500BRIX25ChanCfgChanTEI,
       "cdx6500BRIX25ChanCfgX25NetworkType": cdx6500BRIX25ChanCfgX25NetworkType,
       "cdx6500BRIX25ChanCfgDNumSVCChannels": cdx6500BRIX25ChanCfgDNumSVCChannels,
       "cdx6500BRIX25ChanCfgDWPktWindow": cdx6500BRIX25ChanCfgDWPktWindow,
       "cdx6500BRIX25ChanCfgDPPktSize": cdx6500BRIX25ChanCfgDPPktSize,
       "cdx6500BRIX25ChanCfgDKFrameWindow": cdx6500BRIX25ChanCfgDKFrameWindow,
       "cdx6500BRIX25ChanCfgDN2TransTries": cdx6500BRIX25ChanCfgDN2TransTries,
       "cdx6500BRIX25ChanCfgT1Timer": cdx6500BRIX25ChanCfgT1Timer,
       "cdx6500BRIX25ChanCfgT2Timer": cdx6500BRIX25ChanCfgT2Timer,
       "cdx6500BRIX25ChanCfgLinkType": cdx6500BRIX25ChanCfgLinkType,
       "cdx6500BRIX25ChanCfgAddrTrans": cdx6500BRIX25ChanCfgAddrTrans,
       "cdx6500Statistics": cdx6500Statistics,
       "cdx6500StatProtocolGroup": cdx6500StatProtocolGroup,
       "cdx6500PSTPortProtocolGroup": cdx6500PSTPortProtocolGroup,
       "cdx6500BRIStats": cdx6500BRIStats,
       "cdx6500BRIPStatsTable": cdx6500BRIPStatsTable,
       "cdx6500BRIPStatsTableEntry": cdx6500BRIPStatsTableEntry,
       "cdx6500BRIPStatPortNumber": cdx6500BRIPStatPortNumber,
       "cdx6500BRIPStatPortType": cdx6500BRIPStatPortType,
       "cdx6500BRIPStatPortStatus": cdx6500BRIPStatPortStatus,
       "cdx6500BRIPStatNumConfigChannels": cdx6500BRIPStatNumConfigChannels,
       "cdx6500BRIPStatSwitchType": cdx6500BRIPStatSwitchType,
       "cdx6500BRIPStatTEI": cdx6500BRIPStatTEI,
       "cdx6500BRIPStatLastStatsReset": cdx6500BRIPStatLastStatsReset,
       "cdx6500BRIPStatCharsInTot": cdx6500BRIPStatCharsInTot,
       "cdx6500BRIPStatCharsInPerSec": cdx6500BRIPStatCharsInPerSec,
       "cdx6500BRIPStatCharsOutTot": cdx6500BRIPStatCharsOutTot,
       "cdx6500BRIPStatCharsOutPerSec": cdx6500BRIPStatCharsOutPerSec,
       "cdx6500BRIPStatFramesInTot": cdx6500BRIPStatFramesInTot,
       "cdx6500BRIPStatFramesInPerSec": cdx6500BRIPStatFramesInPerSec,
       "cdx6500BRIPStatFrameOutTot": cdx6500BRIPStatFrameOutTot,
       "cdx6500BRIPStatFrameOutPerSec": cdx6500BRIPStatFrameOutPerSec,
       "cdx6500BRIPStatAvFrameSzIn": cdx6500BRIPStatAvFrameSzIn,
       "cdx6500BRIPStatAvFrameSzOut": cdx6500BRIPStatAvFrameSzOut,
       "cdx6500BRIPStatPortUtilIn": cdx6500BRIPStatPortUtilIn,
       "cdx6500BRIPStatPortUtilOut": cdx6500BRIPStatPortUtilOut,
       "cdx6500BRIPStatPortUtilInMax": cdx6500BRIPStatPortUtilInMax,
       "cdx6500BRIPStatPortUtilOutMax": cdx6500BRIPStatPortUtilOutMax,
       "cdx6500BRIChanStatsTable": cdx6500BRIChanStatsTable,
       "cdx6500BRIChanStatsTableEntry": cdx6500BRIChanStatsTableEntry,
       "cdx6500BRICStatsPortNumber": cdx6500BRICStatsPortNumber,
       "cdx6500BRICStatsChannelNum": cdx6500BRICStatsChannelNum,
       "cdx6500BRICStatsChannelType": cdx6500BRICStatsChannelType,
       "cdx6500BRICStatsAccessType": cdx6500BRICStatsAccessType,
       "cdx6500BRICStatsProtocolType": cdx6500BRICStatsProtocolType,
       "cdx6500BRICStatsCallState": cdx6500BRICStatsCallState,
       "cdx6500BRICStatsChannelStatus": cdx6500BRICStatsChannelStatus,
       "cdx6500BRICStatsInCurCallAddr": cdx6500BRICStatsInCurCallAddr,
       "cdx6500BRICStatsInCurCallSubAddr": cdx6500BRICStatsInCurCallSubAddr,
       "cdx6500BRICStatsInAvConnTm": cdx6500BRICStatsInAvConnTm,
       "cdx6500BRICStatsInCurConnTm": cdx6500BRICStatsInCurConnTm,
       "cdx6500BRICStatsInMinConnTm": cdx6500BRICStatsInMinConnTm,
       "cdx6500BRICStatsInMaxConnTm": cdx6500BRICStatsInMaxConnTm,
       "cdx6500BRICStatsInNumSuccCalls": cdx6500BRICStatsInNumSuccCalls,
       "cdx6500BRICStatsInNumFailCalls": cdx6500BRICStatsInNumFailCalls,
       "cdx6500BRICStatsOutCurCallAddr": cdx6500BRICStatsOutCurCallAddr,
       "cdx6500BRICStatsOutCurCallSubAddr": cdx6500BRICStatsOutCurCallSubAddr,
       "cdx6500BRICStatsOutAvConnTm": cdx6500BRICStatsOutAvConnTm,
       "cdx6500BRICStatsOutCurConnTm": cdx6500BRICStatsOutCurConnTm,
       "cdx6500BRICStatsOutMinConnTm": cdx6500BRICStatsOutMinConnTm,
       "cdx6500BRICStatsOutMaxConnTm": cdx6500BRICStatsOutMaxConnTm,
       "cdx6500BRICStatsOutNumSuccCalls": cdx6500BRICStatsOutNumSuccCalls,
       "cdx6500BRICStatsOutNumFailCalls": cdx6500BRICStatsOutNumFailCalls,
       "cdx6500BRICStatsMaxSVC": cdx6500BRICStatsMaxSVC,
       "cdx6500BRICStatsMaxPVC": cdx6500BRICStatsMaxPVC,
       "cdx6500BRICStatsCurSVC": cdx6500BRICStatsCurSVC,
       "cdx6500BRICStatsCurPVC": cdx6500BRICStatsCurPVC,
       "cdx6500BRICStatsLastRepReasonCodes": cdx6500BRICStatsLastRepReasonCodes,
       "cdx6500BRICStatsLastStatsReset": cdx6500BRICStatsLastStatsReset,
       "cdx6500BRICStatsCharsInTot": cdx6500BRICStatsCharsInTot,
       "cdx6500BRICStatsCharsOutTot": cdx6500BRICStatsCharsOutTot,
       "cdx6500BRICStatsCharsInPerSec": cdx6500BRICStatsCharsInPerSec,
       "cdx6500BRICStatsCharsOutPerSec": cdx6500BRICStatsCharsOutPerSec,
       "cdx6500BRICStatsPktsInTot": cdx6500BRICStatsPktsInTot,
       "cdx6500BRICStatsPktsOutTot": cdx6500BRICStatsPktsOutTot,
       "cdx6500BRICStatsPktsInPerSec": cdx6500BRICStatsPktsInPerSec,
       "cdx6500BRICStatsPktsOutPerSec": cdx6500BRICStatsPktsOutPerSec,
       "cdx6500BRICStatsFramesInTot": cdx6500BRICStatsFramesInTot,
       "cdx6500BRICStatsFramesOutTot": cdx6500BRICStatsFramesOutTot,
       "cdx6500BRICStatsFramesInPerSec": cdx6500BRICStatsFramesInPerSec,
       "cdx6500BRICStatsFramesOutPerSec": cdx6500BRICStatsFramesOutPerSec,
       "cdx6500BRICStatsInfoFramesIn": cdx6500BRICStatsInfoFramesIn,
       "cdx6500BRICStatsInfoFramesOut": cdx6500BRICStatsInfoFramesOut,
       "cdx6500BRICStatsRNRFramesIn": cdx6500BRICStatsRNRFramesIn,
       "cdx6500BRICStatsRNRFramesOut": cdx6500BRICStatsRNRFramesOut,
       "cdx6500BRICStatsSABMFramesIn": cdx6500BRICStatsSABMFramesIn,
       "cdx6500BRICStatsSABMFramesOut": cdx6500BRICStatsSABMFramesOut,
       "cdx6500BRICStatsDMFramesIn": cdx6500BRICStatsDMFramesIn,
       "cdx6500BRICStatsDMFramesOut": cdx6500BRICStatsDMFramesOut,
       "cdx6500BRICStatsRRFramesIn": cdx6500BRICStatsRRFramesIn,
       "cdx6500BRICStatsRRFramesOut": cdx6500BRICStatsRRFramesOut,
       "cdx6500BRICStatsREJFramesIn": cdx6500BRICStatsREJFramesIn,
       "cdx6500BRICStatsREJFramesOut": cdx6500BRICStatsREJFramesOut,
       "cdx6500BRICStatsDISCFramesIn": cdx6500BRICStatsDISCFramesIn,
       "cdx6500BRICStatsDISCFramesOut": cdx6500BRICStatsDISCFramesOut,
       "cdx6500BRICStatsUAFramesIn": cdx6500BRICStatsUAFramesIn,
       "cdx6500BRICStatsUAFramesOut": cdx6500BRICStatsUAFramesOut,
       "cdx6500BRICStatsFRMRFramesIn": cdx6500BRICStatsFRMRFramesIn,
       "cdx6500BRICStatsFRMRFramesOut": cdx6500BRICStatsFRMRFramesOut,
       "cdx6500BRICStatsDataPktsIn": cdx6500BRICStatsDataPktsIn,
       "cdx6500BRICStatsDataPktsOut": cdx6500BRICStatsDataPktsOut,
       "cdx6500BRICStatsRRPktsIn": cdx6500BRICStatsRRPktsIn,
       "cdx6500BRICStatsRRPktsOut": cdx6500BRICStatsRRPktsOut,
       "cdx6500BRICStatsRNRPktsIn": cdx6500BRICStatsRNRPktsIn,
       "cdx6500BRICStatsRNRPktsOut": cdx6500BRICStatsRNRPktsOut,
       "cdx6500BRICStatsRejPktsIn": cdx6500BRICStatsRejPktsIn,
       "cdx6500BRICStatsRejPktsOut": cdx6500BRICStatsRejPktsOut,
       "cdx6500BRICStatsCallReqPktsIn": cdx6500BRICStatsCallReqPktsIn,
       "cdx6500BRICStatsCallReqPktsOut": cdx6500BRICStatsCallReqPktsOut,
       "cdx6500BRICStatsCallAccPktsIn": cdx6500BRICStatsCallAccPktsIn,
       "cdx6500BRICStatsCallAccPktsOut": cdx6500BRICStatsCallAccPktsOut,
       "cdx6500BRICStatsClrReqPktsIn": cdx6500BRICStatsClrReqPktsIn,
       "cdx6500BRICStatsClrReqPktsOut": cdx6500BRICStatsClrReqPktsOut,
       "cdx6500BRICStatsClrConfPktsIn": cdx6500BRICStatsClrConfPktsIn,
       "cdx6500BRICStatsClrConfPktsOut": cdx6500BRICStatsClrConfPktsOut,
       "cdx6500BRICStatsIntReqPktsIn": cdx6500BRICStatsIntReqPktsIn,
       "cdx6500BRICStatsIntReqPktsOut": cdx6500BRICStatsIntReqPktsOut,
       "cdx6500BRICStatsIntConfPktsIn": cdx6500BRICStatsIntConfPktsIn,
       "cdx6500BRICStatsIntConfPktsOut": cdx6500BRICStatsIntConfPktsOut,
       "cdx6500BRICStatsRstReqPktsIn": cdx6500BRICStatsRstReqPktsIn,
       "cdx6500BRICStatsRstReqPktsOut": cdx6500BRICStatsRstReqPktsOut,
       "cdx6500BRICStatsRstConfPktsIn": cdx6500BRICStatsRstConfPktsIn,
       "cdx6500BRICStatsRstConfPktsOut": cdx6500BRICStatsRstConfPktsOut,
       "cdx6500BRICStatsRestartReqPktsIn": cdx6500BRICStatsRestartReqPktsIn,
       "cdx6500BRICStatsRestartReqPktsOut": cdx6500BRICStatsRestartReqPktsOut,
       "cdx6500BRICStatsRestartConfPktsIn": cdx6500BRICStatsRestartConfPktsIn,
       "cdx6500BRICStatsRestartConfPktsOut": cdx6500BRICStatsRestartConfPktsOut,
       "cdx6500BRICStatsTEI": cdx6500BRICStatsTEI,
       "cdx6500BRICStatsSAPI": cdx6500BRICStatsSAPI,
       "cdx6500BRICStatsNetworkType": cdx6500BRICStatsNetworkType}
)
