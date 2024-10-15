# SNMP MIB module (ISDN-OPT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ISDN-OPT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:11:45 2024
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
_IsgIsdnCfgGroup_ObjectIdentity = ObjectIdentity
isgIsdnCfgGroup = _IsgIsdnCfgGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 2, 19)
)
_IsgVGIsdnCfgChanTable_Object = MibTable
isgVGIsdnCfgChanTable = _IsgVGIsdnCfgChanTable_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 2, 19, 1)
)
if mibBuilder.loadTexts:
    isgVGIsdnCfgChanTable.setStatus("mandatory")
_IsgVGIsdnCfgChanTableEntry_Object = MibTable
isgVGIsdnCfgChanTableEntry = _IsgVGIsdnCfgChanTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 2, 19, 1, 1)
)
if mibBuilder.loadTexts:
    isgVGIsdnCfgChanTableEntry.setStatus("mandatory")
_IsgVGIsdnCfgEntryNum_Type = Integer32
_IsgVGIsdnCfgEntryNum_Object = MibTableColumn
isgVGIsdnCfgEntryNum = _IsgVGIsdnCfgEntryNum_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 2, 19, 1, 1, 1),
    _IsgVGIsdnCfgEntryNum_Type()
)
isgVGIsdnCfgEntryNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isgVGIsdnCfgEntryNum.setStatus("mandatory")


class _IsgVGIsdnCfgChanType_Type(Integer32):
    """Custom type isgVGIsdnCfgChanType based on Integer32"""
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
        *(("isdn2B", 5),
          ("isdnB", 6),
          ("isdnB1", 3),
          ("isdnB2", 4),
          ("isdnD", 2),
          ("isdnNone", 1))
    )


_IsgVGIsdnCfgChanType_Type.__name__ = "Integer32"
_IsgVGIsdnCfgChanType_Object = MibTableColumn
isgVGIsdnCfgChanType = _IsgVGIsdnCfgChanType_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 2, 19, 1, 1, 2),
    _IsgVGIsdnCfgChanType_Type()
)
isgVGIsdnCfgChanType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isgVGIsdnCfgChanType.setStatus("mandatory")


class _IsgVGIsdnCfgDChanPort_Type(Integer32):
    """Custom type isgVGIsdnCfgDChanPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              5,
              100)
        )
    )
    namedValues = NamedValues(
        *(("dchanfour", 5),
          ("dchanone", 2),
          ("dchanzero", 1),
          ("nc", 100))
    )


_IsgVGIsdnCfgDChanPort_Type.__name__ = "Integer32"
_IsgVGIsdnCfgDChanPort_Object = MibTableColumn
isgVGIsdnCfgDChanPort = _IsgVGIsdnCfgDChanPort_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 2, 19, 1, 1, 3),
    _IsgVGIsdnCfgDChanPort_Type()
)
isgVGIsdnCfgDChanPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    isgVGIsdnCfgDChanPort.setStatus("mandatory")


class _IsgVGIsdnCfgSwitchType_Type(Integer32):
    """Custom type isgVGIsdnCfgSwitchType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3,
              6,
              8,
              9,
              11,
              13,
              14,
              15)
        )
    )
    namedValues = NamedValues(
        *(("bri1tr6Stype", 2),
          ("bri5essStype", 3),
          ("briDms100Stype", 6),
          ("briEtsiStype", 9),
          ("briKddStype", 8),
          ("briNi1Stype", 11),
          ("briNttStype", 13),
          ("briTs013Stype", 14),
          ("briVnStype", 15))
    )


_IsgVGIsdnCfgSwitchType_Type.__name__ = "Integer32"
_IsgVGIsdnCfgSwitchType_Object = MibTableColumn
isgVGIsdnCfgSwitchType = _IsgVGIsdnCfgSwitchType_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 2, 19, 1, 1, 4),
    _IsgVGIsdnCfgSwitchType_Type()
)
isgVGIsdnCfgSwitchType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    isgVGIsdnCfgSwitchType.setStatus("mandatory")
_IsgVGIsdnCfgDChanTEI_Type = Integer32
_IsgVGIsdnCfgDChanTEI_Object = MibTableColumn
isgVGIsdnCfgDChanTEI = _IsgVGIsdnCfgDChanTEI_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 2, 19, 1, 1, 5),
    _IsgVGIsdnCfgDChanTEI_Type()
)
isgVGIsdnCfgDChanTEI.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    isgVGIsdnCfgDChanTEI.setStatus("mandatory")


class _IsgVGIsdnCfgDPckTraffic_Type(Integer32):
    """Custom type isgVGIsdnCfgDPckTraffic based on Integer32"""
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


_IsgVGIsdnCfgDPckTraffic_Type.__name__ = "Integer32"
_IsgVGIsdnCfgDPckTraffic_Object = MibTableColumn
isgVGIsdnCfgDPckTraffic = _IsgVGIsdnCfgDPckTraffic_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 2, 19, 1, 1, 6),
    _IsgVGIsdnCfgDPckTraffic_Type()
)
isgVGIsdnCfgDPckTraffic.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    isgVGIsdnCfgDPckTraffic.setStatus("mandatory")


class _IsgVGIsdnCfgDChanDN_Type(DisplayString):
    """Custom type isgVGIsdnCfgDChanDN based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 17),
    )


_IsgVGIsdnCfgDChanDN_Type.__name__ = "DisplayString"
_IsgVGIsdnCfgDChanDN_Object = MibTableColumn
isgVGIsdnCfgDChanDN = _IsgVGIsdnCfgDChanDN_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 2, 19, 1, 1, 7),
    _IsgVGIsdnCfgDChanDN_Type()
)
isgVGIsdnCfgDChanDN.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    isgVGIsdnCfgDChanDN.setStatus("mandatory")


class _IsgVGIsdnCfgDSPID_Type(DisplayString):
    """Custom type isgVGIsdnCfgDSPID based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 21),
    )


_IsgVGIsdnCfgDSPID_Type.__name__ = "DisplayString"
_IsgVGIsdnCfgDSPID_Object = MibTableColumn
isgVGIsdnCfgDSPID = _IsgVGIsdnCfgDSPID_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 2, 19, 1, 1, 8),
    _IsgVGIsdnCfgDSPID_Type()
)
isgVGIsdnCfgDSPID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    isgVGIsdnCfgDSPID.setStatus("mandatory")


class _IsgVGIsdnCfgFirstBChanPort_Type(Integer32):
    """Custom type isgVGIsdnCfgFirstBChanPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_IsgVGIsdnCfgFirstBChanPort_Type.__name__ = "Integer32"
_IsgVGIsdnCfgFirstBChanPort_Object = MibTableColumn
isgVGIsdnCfgFirstBChanPort = _IsgVGIsdnCfgFirstBChanPort_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 2, 19, 1, 1, 9),
    _IsgVGIsdnCfgFirstBChanPort_Type()
)
isgVGIsdnCfgFirstBChanPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    isgVGIsdnCfgFirstBChanPort.setStatus("mandatory")


class _IsgVGIsdnCfgFirstAccType_Type(Integer32):
    """Custom type isgVGIsdnCfgFirstAccType based on Integer32"""
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
        *(("cmd", 2),
          ("cvl", 4),
          ("dov", 5),
          ("perm", 1),
          ("pmd", 3))
    )


_IsgVGIsdnCfgFirstAccType_Type.__name__ = "Integer32"
_IsgVGIsdnCfgFirstAccType_Object = MibTableColumn
isgVGIsdnCfgFirstAccType = _IsgVGIsdnCfgFirstAccType_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 2, 19, 1, 1, 10),
    _IsgVGIsdnCfgFirstAccType_Type()
)
isgVGIsdnCfgFirstAccType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    isgVGIsdnCfgFirstAccType.setStatus("mandatory")


class _IsgVGIsdnCfgFirstCallDisablSTm_Type(DisplayString):
    """Custom type isgVGIsdnCfgFirstCallDisablSTm based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 5),
    )


_IsgVGIsdnCfgFirstCallDisablSTm_Type.__name__ = "DisplayString"
_IsgVGIsdnCfgFirstCallDisablSTm_Object = MibTableColumn
isgVGIsdnCfgFirstCallDisablSTm = _IsgVGIsdnCfgFirstCallDisablSTm_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 2, 19, 1, 1, 11),
    _IsgVGIsdnCfgFirstCallDisablSTm_Type()
)
isgVGIsdnCfgFirstCallDisablSTm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isgVGIsdnCfgFirstCallDisablSTm.setStatus("mandatory")


class _IsgVGIsdnCfgFirstCallEnablSTm_Type(DisplayString):
    """Custom type isgVGIsdnCfgFirstCallEnablSTm based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 5),
    )


_IsgVGIsdnCfgFirstCallEnablSTm_Type.__name__ = "DisplayString"
_IsgVGIsdnCfgFirstCallEnablSTm_Object = MibTableColumn
isgVGIsdnCfgFirstCallEnablSTm = _IsgVGIsdnCfgFirstCallEnablSTm_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 2, 19, 1, 1, 12),
    _IsgVGIsdnCfgFirstCallEnablSTm_Type()
)
isgVGIsdnCfgFirstCallEnablSTm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isgVGIsdnCfgFirstCallEnablSTm.setStatus("mandatory")


class _IsgVGIsdnCfgFirstSPBU_Type(Integer32):
    """Custom type isgVGIsdnCfgFirstSPBU based on Integer32"""
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


_IsgVGIsdnCfgFirstSPBU_Type.__name__ = "Integer32"
_IsgVGIsdnCfgFirstSPBU_Object = MibTableColumn
isgVGIsdnCfgFirstSPBU = _IsgVGIsdnCfgFirstSPBU_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 2, 19, 1, 1, 13),
    _IsgVGIsdnCfgFirstSPBU_Type()
)
isgVGIsdnCfgFirstSPBU.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    isgVGIsdnCfgFirstSPBU.setStatus("mandatory")


class _IsgVGIsdnCfgFirstSPBUOpt_Type(DisplayString):
    """Custom type isgVGIsdnCfgFirstSPBUOpt based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(3, 18),
    )


_IsgVGIsdnCfgFirstSPBUOpt_Type.__name__ = "DisplayString"
_IsgVGIsdnCfgFirstSPBUOpt_Object = MibTableColumn
isgVGIsdnCfgFirstSPBUOpt = _IsgVGIsdnCfgFirstSPBUOpt_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 2, 19, 1, 1, 14),
    _IsgVGIsdnCfgFirstSPBUOpt_Type()
)
isgVGIsdnCfgFirstSPBUOpt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    isgVGIsdnCfgFirstSPBUOpt.setStatus("mandatory")


class _IsgVGIsdnCfgFirstSPBUTmOut_Type(Integer32):
    """Custom type isgVGIsdnCfgFirstSPBUTmOut based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 240),
    )


_IsgVGIsdnCfgFirstSPBUTmOut_Type.__name__ = "Integer32"
_IsgVGIsdnCfgFirstSPBUTmOut_Object = MibTableColumn
isgVGIsdnCfgFirstSPBUTmOut = _IsgVGIsdnCfgFirstSPBUTmOut_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 2, 19, 1, 1, 15),
    _IsgVGIsdnCfgFirstSPBUTmOut_Type()
)
isgVGIsdnCfgFirstSPBUTmOut.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    isgVGIsdnCfgFirstSPBUTmOut.setStatus("mandatory")


class _IsgVGIsdnCfgFirstRate_Type(Integer32):
    """Custom type isgVGIsdnCfgFirstRate based on Integer32"""
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
        *(("rate112k", 4),
          ("rate128k", 2),
          ("rate56k", 3),
          ("rate64k", 1))
    )


_IsgVGIsdnCfgFirstRate_Type.__name__ = "Integer32"
_IsgVGIsdnCfgFirstRate_Object = MibTableColumn
isgVGIsdnCfgFirstRate = _IsgVGIsdnCfgFirstRate_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 2, 19, 1, 1, 16),
    _IsgVGIsdnCfgFirstRate_Type()
)
isgVGIsdnCfgFirstRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    isgVGIsdnCfgFirstRate.setStatus("mandatory")
_IsgVGIsdnCfgFirstTEI_Type = Integer32
_IsgVGIsdnCfgFirstTEI_Object = MibTableColumn
isgVGIsdnCfgFirstTEI = _IsgVGIsdnCfgFirstTEI_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 2, 19, 1, 1, 17),
    _IsgVGIsdnCfgFirstTEI_Type()
)
isgVGIsdnCfgFirstTEI.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    isgVGIsdnCfgFirstTEI.setStatus("mandatory")


class _IsgVGIsdnCfgFirstSPID_Type(DisplayString):
    """Custom type isgVGIsdnCfgFirstSPID based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 21),
    )


_IsgVGIsdnCfgFirstSPID_Type.__name__ = "DisplayString"
_IsgVGIsdnCfgFirstSPID_Object = MibTableColumn
isgVGIsdnCfgFirstSPID = _IsgVGIsdnCfgFirstSPID_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 2, 19, 1, 1, 18),
    _IsgVGIsdnCfgFirstSPID_Type()
)
isgVGIsdnCfgFirstSPID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    isgVGIsdnCfgFirstSPID.setStatus("mandatory")


class _IsgVGIsdnCfgFirstDN_Type(DisplayString):
    """Custom type isgVGIsdnCfgFirstDN based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 17),
    )


_IsgVGIsdnCfgFirstDN_Type.__name__ = "DisplayString"
_IsgVGIsdnCfgFirstDN_Object = MibTableColumn
isgVGIsdnCfgFirstDN = _IsgVGIsdnCfgFirstDN_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 2, 19, 1, 1, 19),
    _IsgVGIsdnCfgFirstDN_Type()
)
isgVGIsdnCfgFirstDN.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    isgVGIsdnCfgFirstDN.setStatus("mandatory")


class _IsgVGIsdnCfgFirstSubAddr_Type(DisplayString):
    """Custom type isgVGIsdnCfgFirstSubAddr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 21),
    )


_IsgVGIsdnCfgFirstSubAddr_Type.__name__ = "DisplayString"
_IsgVGIsdnCfgFirstSubAddr_Object = MibTableColumn
isgVGIsdnCfgFirstSubAddr = _IsgVGIsdnCfgFirstSubAddr_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 2, 19, 1, 1, 20),
    _IsgVGIsdnCfgFirstSubAddr_Type()
)
isgVGIsdnCfgFirstSubAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    isgVGIsdnCfgFirstSubAddr.setStatus("mandatory")


class _IsgVGIsdnCfgFirstOutDialNum1_Type(DisplayString):
    """Custom type isgVGIsdnCfgFirstOutDialNum1 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 17),
    )


_IsgVGIsdnCfgFirstOutDialNum1_Type.__name__ = "DisplayString"
_IsgVGIsdnCfgFirstOutDialNum1_Object = MibTableColumn
isgVGIsdnCfgFirstOutDialNum1 = _IsgVGIsdnCfgFirstOutDialNum1_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 2, 19, 1, 1, 21),
    _IsgVGIsdnCfgFirstOutDialNum1_Type()
)
isgVGIsdnCfgFirstOutDialNum1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    isgVGIsdnCfgFirstOutDialNum1.setStatus("mandatory")


class _IsgVGIsdnCfgFirstOutDialNum2_Type(DisplayString):
    """Custom type isgVGIsdnCfgFirstOutDialNum2 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 17),
    )


_IsgVGIsdnCfgFirstOutDialNum2_Type.__name__ = "DisplayString"
_IsgVGIsdnCfgFirstOutDialNum2_Object = MibTableColumn
isgVGIsdnCfgFirstOutDialNum2 = _IsgVGIsdnCfgFirstOutDialNum2_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 2, 19, 1, 1, 22),
    _IsgVGIsdnCfgFirstOutDialNum2_Type()
)
isgVGIsdnCfgFirstOutDialNum2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    isgVGIsdnCfgFirstOutDialNum2.setStatus("mandatory")
_IsgVGIsdnCfgFirstDialRetryIntrvl_Type = Integer32
_IsgVGIsdnCfgFirstDialRetryIntrvl_Object = MibTableColumn
isgVGIsdnCfgFirstDialRetryIntrvl = _IsgVGIsdnCfgFirstDialRetryIntrvl_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 2, 19, 1, 1, 23),
    _IsgVGIsdnCfgFirstDialRetryIntrvl_Type()
)
isgVGIsdnCfgFirstDialRetryIntrvl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    isgVGIsdnCfgFirstDialRetryIntrvl.setStatus("mandatory")


class _IsgVGIsdnCfgFirstNumCallRetries_Type(Integer32):
    """Custom type isgVGIsdnCfgFirstNumCallRetries based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_IsgVGIsdnCfgFirstNumCallRetries_Type.__name__ = "Integer32"
_IsgVGIsdnCfgFirstNumCallRetries_Object = MibTableColumn
isgVGIsdnCfgFirstNumCallRetries = _IsgVGIsdnCfgFirstNumCallRetries_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 2, 19, 1, 1, 24),
    _IsgVGIsdnCfgFirstNumCallRetries_Type()
)
isgVGIsdnCfgFirstNumCallRetries.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    isgVGIsdnCfgFirstNumCallRetries.setStatus("mandatory")


class _IsgVGIsdnCfgSecondChanPort_Type(Integer32):
    """Custom type isgVGIsdnCfgSecondChanPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_IsgVGIsdnCfgSecondChanPort_Type.__name__ = "Integer32"
_IsgVGIsdnCfgSecondChanPort_Object = MibTableColumn
isgVGIsdnCfgSecondChanPort = _IsgVGIsdnCfgSecondChanPort_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 2, 19, 1, 1, 25),
    _IsgVGIsdnCfgSecondChanPort_Type()
)
isgVGIsdnCfgSecondChanPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    isgVGIsdnCfgSecondChanPort.setStatus("mandatory")


class _IsgVGIsdnCfgSecondAccType_Type(Integer32):
    """Custom type isgVGIsdnCfgSecondAccType based on Integer32"""
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
        *(("cmd", 2),
          ("cvl", 4),
          ("dov", 5),
          ("perm", 1),
          ("pmd", 3))
    )


_IsgVGIsdnCfgSecondAccType_Type.__name__ = "Integer32"
_IsgVGIsdnCfgSecondAccType_Object = MibTableColumn
isgVGIsdnCfgSecondAccType = _IsgVGIsdnCfgSecondAccType_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 2, 19, 1, 1, 26),
    _IsgVGIsdnCfgSecondAccType_Type()
)
isgVGIsdnCfgSecondAccType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    isgVGIsdnCfgSecondAccType.setStatus("mandatory")


class _IsgVGIsdnCfgSecondCallDisablSTm_Type(DisplayString):
    """Custom type isgVGIsdnCfgSecondCallDisablSTm based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 5),
    )


_IsgVGIsdnCfgSecondCallDisablSTm_Type.__name__ = "DisplayString"
_IsgVGIsdnCfgSecondCallDisablSTm_Object = MibTableColumn
isgVGIsdnCfgSecondCallDisablSTm = _IsgVGIsdnCfgSecondCallDisablSTm_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 2, 19, 1, 1, 27),
    _IsgVGIsdnCfgSecondCallDisablSTm_Type()
)
isgVGIsdnCfgSecondCallDisablSTm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isgVGIsdnCfgSecondCallDisablSTm.setStatus("mandatory")


class _IsgVGIsdnCfgSecondCallEnablSTm_Type(DisplayString):
    """Custom type isgVGIsdnCfgSecondCallEnablSTm based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 5),
    )


_IsgVGIsdnCfgSecondCallEnablSTm_Type.__name__ = "DisplayString"
_IsgVGIsdnCfgSecondCallEnablSTm_Object = MibTableColumn
isgVGIsdnCfgSecondCallEnablSTm = _IsgVGIsdnCfgSecondCallEnablSTm_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 2, 19, 1, 1, 28),
    _IsgVGIsdnCfgSecondCallEnablSTm_Type()
)
isgVGIsdnCfgSecondCallEnablSTm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isgVGIsdnCfgSecondCallEnablSTm.setStatus("mandatory")


class _IsgVGIsdnCfgSecondSPBU_Type(Integer32):
    """Custom type isgVGIsdnCfgSecondSPBU based on Integer32"""
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


_IsgVGIsdnCfgSecondSPBU_Type.__name__ = "Integer32"
_IsgVGIsdnCfgSecondSPBU_Object = MibTableColumn
isgVGIsdnCfgSecondSPBU = _IsgVGIsdnCfgSecondSPBU_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 2, 19, 1, 1, 29),
    _IsgVGIsdnCfgSecondSPBU_Type()
)
isgVGIsdnCfgSecondSPBU.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    isgVGIsdnCfgSecondSPBU.setStatus("mandatory")


class _IsgVGIsdnCfgSecondSPBUOpt_Type(DisplayString):
    """Custom type isgVGIsdnCfgSecondSPBUOpt based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(3, 18),
    )


_IsgVGIsdnCfgSecondSPBUOpt_Type.__name__ = "DisplayString"
_IsgVGIsdnCfgSecondSPBUOpt_Object = MibTableColumn
isgVGIsdnCfgSecondSPBUOpt = _IsgVGIsdnCfgSecondSPBUOpt_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 2, 19, 1, 1, 30),
    _IsgVGIsdnCfgSecondSPBUOpt_Type()
)
isgVGIsdnCfgSecondSPBUOpt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    isgVGIsdnCfgSecondSPBUOpt.setStatus("mandatory")


class _IsgVGIsdnCfgSecondSPBUTmOut_Type(Integer32):
    """Custom type isgVGIsdnCfgSecondSPBUTmOut based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 240),
    )


_IsgVGIsdnCfgSecondSPBUTmOut_Type.__name__ = "Integer32"
_IsgVGIsdnCfgSecondSPBUTmOut_Object = MibTableColumn
isgVGIsdnCfgSecondSPBUTmOut = _IsgVGIsdnCfgSecondSPBUTmOut_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 2, 19, 1, 1, 31),
    _IsgVGIsdnCfgSecondSPBUTmOut_Type()
)
isgVGIsdnCfgSecondSPBUTmOut.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    isgVGIsdnCfgSecondSPBUTmOut.setStatus("mandatory")


class _IsgVGIsdnCfgSecondRate_Type(Integer32):
    """Custom type isgVGIsdnCfgSecondRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              3)
        )
    )
    namedValues = NamedValues(
        *(("rate56k", 3),
          ("rate64k", 1))
    )


_IsgVGIsdnCfgSecondRate_Type.__name__ = "Integer32"
_IsgVGIsdnCfgSecondRate_Object = MibTableColumn
isgVGIsdnCfgSecondRate = _IsgVGIsdnCfgSecondRate_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 2, 19, 1, 1, 32),
    _IsgVGIsdnCfgSecondRate_Type()
)
isgVGIsdnCfgSecondRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    isgVGIsdnCfgSecondRate.setStatus("mandatory")
_IsgVGIsdnCfgSecondTEI_Type = Integer32
_IsgVGIsdnCfgSecondTEI_Object = MibTableColumn
isgVGIsdnCfgSecondTEI = _IsgVGIsdnCfgSecondTEI_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 2, 19, 1, 1, 33),
    _IsgVGIsdnCfgSecondTEI_Type()
)
isgVGIsdnCfgSecondTEI.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    isgVGIsdnCfgSecondTEI.setStatus("mandatory")


class _IsgVGIsdnCfgSecondSPID_Type(DisplayString):
    """Custom type isgVGIsdnCfgSecondSPID based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 21),
    )


_IsgVGIsdnCfgSecondSPID_Type.__name__ = "DisplayString"
_IsgVGIsdnCfgSecondSPID_Object = MibTableColumn
isgVGIsdnCfgSecondSPID = _IsgVGIsdnCfgSecondSPID_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 2, 19, 1, 1, 34),
    _IsgVGIsdnCfgSecondSPID_Type()
)
isgVGIsdnCfgSecondSPID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    isgVGIsdnCfgSecondSPID.setStatus("mandatory")


class _IsgVGIsdnCfgSecondDN_Type(DisplayString):
    """Custom type isgVGIsdnCfgSecondDN based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 17),
    )


_IsgVGIsdnCfgSecondDN_Type.__name__ = "DisplayString"
_IsgVGIsdnCfgSecondDN_Object = MibTableColumn
isgVGIsdnCfgSecondDN = _IsgVGIsdnCfgSecondDN_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 2, 19, 1, 1, 35),
    _IsgVGIsdnCfgSecondDN_Type()
)
isgVGIsdnCfgSecondDN.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    isgVGIsdnCfgSecondDN.setStatus("mandatory")


class _IsgVGIsdnCfgSecondSubAddr_Type(DisplayString):
    """Custom type isgVGIsdnCfgSecondSubAddr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 21),
    )


_IsgVGIsdnCfgSecondSubAddr_Type.__name__ = "DisplayString"
_IsgVGIsdnCfgSecondSubAddr_Object = MibTableColumn
isgVGIsdnCfgSecondSubAddr = _IsgVGIsdnCfgSecondSubAddr_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 2, 19, 1, 1, 36),
    _IsgVGIsdnCfgSecondSubAddr_Type()
)
isgVGIsdnCfgSecondSubAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    isgVGIsdnCfgSecondSubAddr.setStatus("mandatory")


class _IsgVGIsdnCfgSecondOutDialNum1_Type(DisplayString):
    """Custom type isgVGIsdnCfgSecondOutDialNum1 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 17),
    )


_IsgVGIsdnCfgSecondOutDialNum1_Type.__name__ = "DisplayString"
_IsgVGIsdnCfgSecondOutDialNum1_Object = MibTableColumn
isgVGIsdnCfgSecondOutDialNum1 = _IsgVGIsdnCfgSecondOutDialNum1_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 2, 19, 1, 1, 37),
    _IsgVGIsdnCfgSecondOutDialNum1_Type()
)
isgVGIsdnCfgSecondOutDialNum1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    isgVGIsdnCfgSecondOutDialNum1.setStatus("mandatory")


class _IsgVGIsdnCfgSecondOutDialNum2_Type(DisplayString):
    """Custom type isgVGIsdnCfgSecondOutDialNum2 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 17),
    )


_IsgVGIsdnCfgSecondOutDialNum2_Type.__name__ = "DisplayString"
_IsgVGIsdnCfgSecondOutDialNum2_Object = MibTableColumn
isgVGIsdnCfgSecondOutDialNum2 = _IsgVGIsdnCfgSecondOutDialNum2_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 2, 19, 1, 1, 38),
    _IsgVGIsdnCfgSecondOutDialNum2_Type()
)
isgVGIsdnCfgSecondOutDialNum2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    isgVGIsdnCfgSecondOutDialNum2.setStatus("mandatory")
_IsgVGIsdnCfgSecondDialRetryIntrvl_Type = Integer32
_IsgVGIsdnCfgSecondDialRetryIntrvl_Object = MibTableColumn
isgVGIsdnCfgSecondDialRetryIntrvl = _IsgVGIsdnCfgSecondDialRetryIntrvl_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 2, 19, 1, 1, 39),
    _IsgVGIsdnCfgSecondDialRetryIntrvl_Type()
)
isgVGIsdnCfgSecondDialRetryIntrvl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    isgVGIsdnCfgSecondDialRetryIntrvl.setStatus("mandatory")


class _IsgVGIsdnCfgSecondNumCallRetries_Type(Integer32):
    """Custom type isgVGIsdnCfgSecondNumCallRetries based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_IsgVGIsdnCfgSecondNumCallRetries_Type.__name__ = "Integer32"
_IsgVGIsdnCfgSecondNumCallRetries_Object = MibTableColumn
isgVGIsdnCfgSecondNumCallRetries = _IsgVGIsdnCfgSecondNumCallRetries_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 2, 19, 1, 1, 40),
    _IsgVGIsdnCfgSecondNumCallRetries_Type()
)
isgVGIsdnCfgSecondNumCallRetries.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    isgVGIsdnCfgSecondNumCallRetries.setStatus("mandatory")
_IsgVGIsdnCfgFirstPlainOldTelSet_Type = DisplayString
_IsgVGIsdnCfgFirstPlainOldTelSet_Object = MibTableColumn
isgVGIsdnCfgFirstPlainOldTelSet = _IsgVGIsdnCfgFirstPlainOldTelSet_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 2, 19, 1, 1, 41),
    _IsgVGIsdnCfgFirstPlainOldTelSet_Type()
)
isgVGIsdnCfgFirstPlainOldTelSet.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    isgVGIsdnCfgFirstPlainOldTelSet.setStatus("mandatory")
_IsgVGIsdnCfgFirstCallPerm_Type = DisplayString
_IsgVGIsdnCfgFirstCallPerm_Object = MibTableColumn
isgVGIsdnCfgFirstCallPerm = _IsgVGIsdnCfgFirstCallPerm_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 2, 19, 1, 1, 42),
    _IsgVGIsdnCfgFirstCallPerm_Type()
)
isgVGIsdnCfgFirstCallPerm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    isgVGIsdnCfgFirstCallPerm.setStatus("mandatory")


class _IsgVGIsdnCfgFirstChSelect_Type(Integer32):
    """Custom type isgVGIsdnCfgFirstChSelect based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              3)
        )
    )
    namedValues = NamedValues(
        *(("exclusive", 3),
          ("preferred", 1))
    )


_IsgVGIsdnCfgFirstChSelect_Type.__name__ = "Integer32"
_IsgVGIsdnCfgFirstChSelect_Object = MibTableColumn
isgVGIsdnCfgFirstChSelect = _IsgVGIsdnCfgFirstChSelect_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 2, 19, 1, 1, 43),
    _IsgVGIsdnCfgFirstChSelect_Type()
)
isgVGIsdnCfgFirstChSelect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    isgVGIsdnCfgFirstChSelect.setStatus("mandatory")
_IsgVGIsdnCfgSecondPlainOldTelSet_Type = DisplayString
_IsgVGIsdnCfgSecondPlainOldTelSet_Object = MibTableColumn
isgVGIsdnCfgSecondPlainOldTelSet = _IsgVGIsdnCfgSecondPlainOldTelSet_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 2, 19, 1, 1, 44),
    _IsgVGIsdnCfgSecondPlainOldTelSet_Type()
)
isgVGIsdnCfgSecondPlainOldTelSet.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    isgVGIsdnCfgSecondPlainOldTelSet.setStatus("mandatory")
_IsgVGIsdnCfgSecondCallPerm_Type = DisplayString
_IsgVGIsdnCfgSecondCallPerm_Object = MibTableColumn
isgVGIsdnCfgSecondCallPerm = _IsgVGIsdnCfgSecondCallPerm_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 2, 19, 1, 1, 45),
    _IsgVGIsdnCfgSecondCallPerm_Type()
)
isgVGIsdnCfgSecondCallPerm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    isgVGIsdnCfgSecondCallPerm.setStatus("mandatory")


class _IsgVGIsdnCfgSecondChSelect_Type(Integer32):
    """Custom type isgVGIsdnCfgSecondChSelect based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              3)
        )
    )
    namedValues = NamedValues(
        *(("exclusive", 3),
          ("preferred", 1))
    )


_IsgVGIsdnCfgSecondChSelect_Type.__name__ = "Integer32"
_IsgVGIsdnCfgSecondChSelect_Object = MibTableColumn
isgVGIsdnCfgSecondChSelect = _IsgVGIsdnCfgSecondChSelect_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 2, 19, 1, 1, 46),
    _IsgVGIsdnCfgSecondChSelect_Type()
)
isgVGIsdnCfgSecondChSelect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    isgVGIsdnCfgSecondChSelect.setStatus("mandatory")
_Cdx6500Statistics_ObjectIdentity = ObjectIdentity
cdx6500Statistics = _Cdx6500Statistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3)
)
_Cdx6500StatOtherStatsGroup_ObjectIdentity = ObjectIdentity
cdx6500StatOtherStatsGroup = _Cdx6500StatOtherStatsGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 2)
)
_IsgIsdnStatsGroup_ObjectIdentity = ObjectIdentity
isgIsdnStatsGroup = _IsgIsdnStatsGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 2, 9)
)
_IsgVGIsdnStats_ObjectIdentity = ObjectIdentity
isgVGIsdnStats = _IsgVGIsdnStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 2, 9, 1)
)
_IsgVGIsdnCCStatsTbl_Object = MibTable
isgVGIsdnCCStatsTbl = _IsgVGIsdnCCStatsTbl_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 2, 9, 1, 1)
)
if mibBuilder.loadTexts:
    isgVGIsdnCCStatsTbl.setStatus("mandatory")
_IsgVGIsdnCCStatsTblEntry_Object = MibTableRow
isgVGIsdnCCStatsTblEntry = _IsgVGIsdnCCStatsTblEntry_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 2, 9, 1, 1, 1)
)
isgVGIsdnCCStatsTblEntry.setIndexNames(
    (0, "ISDN-OPT-MIB", "isgVGIsdnCCStatsDSLNum"),
    (0, "ISDN-OPT-MIB", "isgVGIsdnCCStatsChType"),
)
if mibBuilder.loadTexts:
    isgVGIsdnCCStatsTblEntry.setStatus("mandatory")
_IsgVGIsdnCCStatsDSLNum_Type = Integer32
_IsgVGIsdnCCStatsDSLNum_Object = MibTableColumn
isgVGIsdnCCStatsDSLNum = _IsgVGIsdnCCStatsDSLNum_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 2, 9, 1, 1, 1, 1),
    _IsgVGIsdnCCStatsDSLNum_Type()
)
isgVGIsdnCCStatsDSLNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isgVGIsdnCCStatsDSLNum.setStatus("mandatory")


class _IsgVGIsdnCCStatsChType_Type(Integer32):
    """Custom type isgVGIsdnCCStatsChType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("b1Channel", 2),
          ("b2Channel", 3),
          ("dChannel", 1))
    )


_IsgVGIsdnCCStatsChType_Type.__name__ = "Integer32"
_IsgVGIsdnCCStatsChType_Object = MibTableColumn
isgVGIsdnCCStatsChType = _IsgVGIsdnCCStatsChType_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 2, 9, 1, 1, 1, 2),
    _IsgVGIsdnCCStatsChType_Type()
)
isgVGIsdnCCStatsChType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isgVGIsdnCCStatsChType.setStatus("mandatory")


class _IsgVGIsdnCCStatsSwtchType_Type(Integer32):
    """Custom type isgVGIsdnCCStatsSwtchType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3,
              6,
              8,
              9,
              11,
              13,
              14,
              15,
              16)
        )
    )
    namedValues = NamedValues(
        *(("bri1tr6Stype", 2),
          ("bri5essStype", 3),
          ("briDms100Stype", 6),
          ("briEtsiStype", 9),
          ("briKddStype", 8),
          ("briNi1Stype", 11),
          ("briNttStype", 13),
          ("briTs013Stype", 14),
          ("briVnStype", 15),
          ("unsupported", 16))
    )


_IsgVGIsdnCCStatsSwtchType_Type.__name__ = "Integer32"
_IsgVGIsdnCCStatsSwtchType_Object = MibTableColumn
isgVGIsdnCCStatsSwtchType = _IsgVGIsdnCCStatsSwtchType_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 2, 9, 1, 1, 1, 3),
    _IsgVGIsdnCCStatsSwtchType_Type()
)
isgVGIsdnCCStatsSwtchType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isgVGIsdnCCStatsSwtchType.setStatus("mandatory")


class _IsgVGIsdnCCStatsL1State_Type(Integer32):
    """Custom type isgVGIsdnCCStatsL1State based on Integer32"""
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
        *(("l12BDLoop", 7),
          ("l1Active", 2),
          ("l1B1B2Loop", 6),
          ("l1B1Loop", 4),
          ("l1B2Loop", 5),
          ("l1Deactive", 3),
          ("l1Setup", 1),
          ("unknown", 8))
    )


_IsgVGIsdnCCStatsL1State_Type.__name__ = "Integer32"
_IsgVGIsdnCCStatsL1State_Object = MibTableColumn
isgVGIsdnCCStatsL1State = _IsgVGIsdnCCStatsL1State_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 2, 9, 1, 1, 1, 4),
    _IsgVGIsdnCCStatsL1State_Type()
)
isgVGIsdnCCStatsL1State.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isgVGIsdnCCStatsL1State.setStatus("mandatory")
_IsgVGIsdnCCStatsTEI_Type = Integer32
_IsgVGIsdnCCStatsTEI_Object = MibTableColumn
isgVGIsdnCCStatsTEI = _IsgVGIsdnCCStatsTEI_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 2, 9, 1, 1, 1, 5),
    _IsgVGIsdnCCStatsTEI_Type()
)
isgVGIsdnCCStatsTEI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isgVGIsdnCCStatsTEI.setStatus("mandatory")


class _IsgVGIsdnCCStatsCallgAddr_Type(DisplayString):
    """Custom type isgVGIsdnCCStatsCallgAddr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 21),
    )


_IsgVGIsdnCCStatsCallgAddr_Type.__name__ = "DisplayString"
_IsgVGIsdnCCStatsCallgAddr_Object = MibTableColumn
isgVGIsdnCCStatsCallgAddr = _IsgVGIsdnCCStatsCallgAddr_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 2, 9, 1, 1, 1, 6),
    _IsgVGIsdnCCStatsCallgAddr_Type()
)
isgVGIsdnCCStatsCallgAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isgVGIsdnCCStatsCallgAddr.setStatus("mandatory")


class _IsgVGIsdnCCStatsCalldAddr_Type(DisplayString):
    """Custom type isgVGIsdnCCStatsCalldAddr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 21),
    )


_IsgVGIsdnCCStatsCalldAddr_Type.__name__ = "DisplayString"
_IsgVGIsdnCCStatsCalldAddr_Object = MibTableColumn
isgVGIsdnCCStatsCalldAddr = _IsgVGIsdnCCStatsCalldAddr_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 2, 9, 1, 1, 1, 7),
    _IsgVGIsdnCCStatsCalldAddr_Type()
)
isgVGIsdnCCStatsCalldAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isgVGIsdnCCStatsCalldAddr.setStatus("mandatory")


class _IsgVGIsdnCCStatsSubaddr_Type(DisplayString):
    """Custom type isgVGIsdnCCStatsSubaddr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 21),
    )


_IsgVGIsdnCCStatsSubaddr_Type.__name__ = "DisplayString"
_IsgVGIsdnCCStatsSubaddr_Object = MibTableColumn
isgVGIsdnCCStatsSubaddr = _IsgVGIsdnCCStatsSubaddr_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 2, 9, 1, 1, 1, 8),
    _IsgVGIsdnCCStatsSubaddr_Type()
)
isgVGIsdnCCStatsSubaddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isgVGIsdnCCStatsSubaddr.setStatus("mandatory")


class _IsgVGIsdnCCStatsDirection_Type(Integer32):
    """Custom type isgVGIsdnCCStatsDirection based on Integer32"""
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
        *(("collision", 4),
          ("incoming", 3),
          ("noCall", 1),
          ("outgoing", 2))
    )


_IsgVGIsdnCCStatsDirection_Type.__name__ = "Integer32"
_IsgVGIsdnCCStatsDirection_Object = MibTableColumn
isgVGIsdnCCStatsDirection = _IsgVGIsdnCCStatsDirection_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 2, 9, 1, 1, 1, 9),
    _IsgVGIsdnCCStatsDirection_Type()
)
isgVGIsdnCCStatsDirection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isgVGIsdnCCStatsDirection.setStatus("mandatory")


class _IsgVGIsdnCCStatsAccType_Type(Integer32):
    """Custom type isgVGIsdnCCStatsAccType based on Integer32"""
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
        *(("cktMode", 2),
          ("cvl", 4),
          ("notApplicable", 5),
          ("permanent", 1),
          ("pktMode", 3))
    )


_IsgVGIsdnCCStatsAccType_Type.__name__ = "Integer32"
_IsgVGIsdnCCStatsAccType_Object = MibTableColumn
isgVGIsdnCCStatsAccType = _IsgVGIsdnCCStatsAccType_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 2, 9, 1, 1, 1, 10),
    _IsgVGIsdnCCStatsAccType_Type()
)
isgVGIsdnCCStatsAccType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isgVGIsdnCCStatsAccType.setStatus("mandatory")


class _IsgVGIsdnCCStatsCallStatus_Type(Integer32):
    """Custom type isgVGIsdnCCStatsCallStatus based on Integer32"""
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
        *(("callConn", 7),
          ("callInit", 4),
          ("discSent", 5),
          ("hostProc", 6),
          ("initFail", 2),
          ("notApplicable", 8),
          ("termIdle", 3),
          ("waitInit", 1))
    )


_IsgVGIsdnCCStatsCallStatus_Type.__name__ = "Integer32"
_IsgVGIsdnCCStatsCallStatus_Object = MibTableColumn
isgVGIsdnCCStatsCallStatus = _IsgVGIsdnCCStatsCallStatus_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 2, 9, 1, 1, 1, 11),
    _IsgVGIsdnCCStatsCallStatus_Type()
)
isgVGIsdnCCStatsCallStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isgVGIsdnCCStatsCallStatus.setStatus("mandatory")


class _IsgVGIsdnCCStatsLineSpeed_Type(Integer32):
    """Custom type isgVGIsdnCCStatsLineSpeed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("rate0k", 3),
          ("rate56k", 2),
          ("rate64k", 1))
    )


_IsgVGIsdnCCStatsLineSpeed_Type.__name__ = "Integer32"
_IsgVGIsdnCCStatsLineSpeed_Object = MibTableColumn
isgVGIsdnCCStatsLineSpeed = _IsgVGIsdnCCStatsLineSpeed_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 2, 9, 1, 1, 1, 12),
    _IsgVGIsdnCCStatsLineSpeed_Type()
)
isgVGIsdnCCStatsLineSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isgVGIsdnCCStatsLineSpeed.setStatus("mandatory")
_IsgVGIsdnCCStatsPortConn_Type = Integer32
_IsgVGIsdnCCStatsPortConn_Object = MibTableColumn
isgVGIsdnCCStatsPortConn = _IsgVGIsdnCCStatsPortConn_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 2, 9, 1, 1, 1, 13),
    _IsgVGIsdnCCStatsPortConn_Type()
)
isgVGIsdnCCStatsPortConn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isgVGIsdnCCStatsPortConn.setStatus("mandatory")
_IsgVGIsdnCCStatsCauseCode_Type = Integer32
_IsgVGIsdnCCStatsCauseCode_Object = MibTableColumn
isgVGIsdnCCStatsCauseCode = _IsgVGIsdnCCStatsCauseCode_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 2, 9, 1, 1, 1, 14),
    _IsgVGIsdnCCStatsCauseCode_Type()
)
isgVGIsdnCCStatsCauseCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isgVGIsdnCCStatsCauseCode.setStatus("mandatory")


class _IsgVGIsdnCCStatsCallStarted_Type(DisplayString):
    """Custom type isgVGIsdnCCStatsCallStarted based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 18),
    )


_IsgVGIsdnCCStatsCallStarted_Type.__name__ = "DisplayString"
_IsgVGIsdnCCStatsCallStarted_Object = MibTableColumn
isgVGIsdnCCStatsCallStarted = _IsgVGIsdnCCStatsCallStarted_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 2, 9, 1, 1, 1, 15),
    _IsgVGIsdnCCStatsCallStarted_Type()
)
isgVGIsdnCCStatsCallStarted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isgVGIsdnCCStatsCallStarted.setStatus("mandatory")


class _IsgVGIsdnCCStatsDChanStatus_Type(Integer32):
    """Custom type isgVGIsdnCCStatsDChanStatus based on Integer32"""
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


_IsgVGIsdnCCStatsDChanStatus_Type.__name__ = "Integer32"
_IsgVGIsdnCCStatsDChanStatus_Object = MibTableColumn
isgVGIsdnCCStatsDChanStatus = _IsgVGIsdnCCStatsDChanStatus_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 2, 9, 1, 1, 1, 16),
    _IsgVGIsdnCCStatsDChanStatus_Type()
)
isgVGIsdnCCStatsDChanStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isgVGIsdnCCStatsDChanStatus.setStatus("mandatory")


class _IsgVGIsdnCCStatsTrmStatus_Type(Integer32):
    """Custom type isgVGIsdnCCStatsTrmStatus based on Integer32"""
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
        *(("fitFailed", 2),
          ("fitTimeout", 3),
          ("fitWaitInit", 1),
          ("networkTimeout", 4),
          ("online", 6),
          ("spiDerror", 5))
    )


_IsgVGIsdnCCStatsTrmStatus_Type.__name__ = "Integer32"
_IsgVGIsdnCCStatsTrmStatus_Object = MibTableColumn
isgVGIsdnCCStatsTrmStatus = _IsgVGIsdnCCStatsTrmStatus_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 2, 9, 1, 1, 1, 17),
    _IsgVGIsdnCCStatsTrmStatus_Type()
)
isgVGIsdnCCStatsTrmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isgVGIsdnCCStatsTrmStatus.setStatus("mandatory")
_IsgVGIsdnCCStatsTrmTei_Type = Integer32
_IsgVGIsdnCCStatsTrmTei_Object = MibTableColumn
isgVGIsdnCCStatsTrmTei = _IsgVGIsdnCCStatsTrmTei_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 2, 9, 1, 1, 1, 18),
    _IsgVGIsdnCCStatsTrmTei_Type()
)
isgVGIsdnCCStatsTrmTei.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isgVGIsdnCCStatsTrmTei.setStatus("mandatory")
_IsgVGIsdnCHStatsTbl_Object = MibTable
isgVGIsdnCHStatsTbl = _IsgVGIsdnCHStatsTbl_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 2, 9, 1, 2)
)
if mibBuilder.loadTexts:
    isgVGIsdnCHStatsTbl.setStatus("mandatory")
_IsgVGIsdnCHStatsTblEntry_Object = MibTableRow
isgVGIsdnCHStatsTblEntry = _IsgVGIsdnCHStatsTblEntry_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 2, 9, 1, 2, 1)
)
isgVGIsdnCHStatsTblEntry.setIndexNames(
    (0, "ISDN-OPT-MIB", "isgVGIsdnCHStatsDSLNum"),
    (0, "ISDN-OPT-MIB", "isgVGIsdnCHStatsChType"),
    (0, "ISDN-OPT-MIB", "isgVGIsdnCHStatsSession"),
)
if mibBuilder.loadTexts:
    isgVGIsdnCHStatsTblEntry.setStatus("mandatory")
_IsgVGIsdnCHStatsDSLNum_Type = Integer32
_IsgVGIsdnCHStatsDSLNum_Object = MibTableColumn
isgVGIsdnCHStatsDSLNum = _IsgVGIsdnCHStatsDSLNum_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 2, 9, 1, 2, 1, 1),
    _IsgVGIsdnCHStatsDSLNum_Type()
)
isgVGIsdnCHStatsDSLNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isgVGIsdnCHStatsDSLNum.setStatus("mandatory")


class _IsgVGIsdnCHStatsChType_Type(Integer32):
    """Custom type isgVGIsdnCHStatsChType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("b1Channel", 1),
          ("b2Channel", 2))
    )


_IsgVGIsdnCHStatsChType_Type.__name__ = "Integer32"
_IsgVGIsdnCHStatsChType_Object = MibTableColumn
isgVGIsdnCHStatsChType = _IsgVGIsdnCHStatsChType_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 2, 9, 1, 2, 1, 2),
    _IsgVGIsdnCHStatsChType_Type()
)
isgVGIsdnCHStatsChType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isgVGIsdnCHStatsChType.setStatus("mandatory")


class _IsgVGIsdnCHStatsSession_Type(Integer32):
    """Custom type isgVGIsdnCHStatsSession based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_IsgVGIsdnCHStatsSession_Type.__name__ = "Integer32"
_IsgVGIsdnCHStatsSession_Object = MibTableColumn
isgVGIsdnCHStatsSession = _IsgVGIsdnCHStatsSession_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 2, 9, 1, 2, 1, 3),
    _IsgVGIsdnCHStatsSession_Type()
)
isgVGIsdnCHStatsSession.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isgVGIsdnCHStatsSession.setStatus("mandatory")


class _IsgVGIsdnCHStatsNumCalld_Type(DisplayString):
    """Custom type isgVGIsdnCHStatsNumCalld based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_IsgVGIsdnCHStatsNumCalld_Type.__name__ = "DisplayString"
_IsgVGIsdnCHStatsNumCalld_Object = MibTableColumn
isgVGIsdnCHStatsNumCalld = _IsgVGIsdnCHStatsNumCalld_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 2, 9, 1, 2, 1, 4),
    _IsgVGIsdnCHStatsNumCalld_Type()
)
isgVGIsdnCHStatsNumCalld.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isgVGIsdnCHStatsNumCalld.setStatus("mandatory")


class _IsgVGIsdnCHStatsDirection_Type(Integer32):
    """Custom type isgVGIsdnCHStatsDirection based on Integer32"""
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
        *(("collision", 4),
          ("incoming", 3),
          ("noCall", 1),
          ("outgoing", 2))
    )


_IsgVGIsdnCHStatsDirection_Type.__name__ = "Integer32"
_IsgVGIsdnCHStatsDirection_Object = MibTableColumn
isgVGIsdnCHStatsDirection = _IsgVGIsdnCHStatsDirection_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 2, 9, 1, 2, 1, 5),
    _IsgVGIsdnCHStatsDirection_Type()
)
isgVGIsdnCHStatsDirection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isgVGIsdnCHStatsDirection.setStatus("mandatory")
_IsgVGIsdnCHStatsCauseCode_Type = Integer32
_IsgVGIsdnCHStatsCauseCode_Object = MibTableColumn
isgVGIsdnCHStatsCauseCode = _IsgVGIsdnCHStatsCauseCode_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 2, 9, 1, 2, 1, 6),
    _IsgVGIsdnCHStatsCauseCode_Type()
)
isgVGIsdnCHStatsCauseCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isgVGIsdnCHStatsCauseCode.setStatus("mandatory")


class _IsgVGIsdnCHStatsLineSpeed_Type(Integer32):
    """Custom type isgVGIsdnCHStatsLineSpeed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("rate0k", 3),
          ("rate56k", 2),
          ("rate64k", 1))
    )


_IsgVGIsdnCHStatsLineSpeed_Type.__name__ = "Integer32"
_IsgVGIsdnCHStatsLineSpeed_Object = MibTableColumn
isgVGIsdnCHStatsLineSpeed = _IsgVGIsdnCHStatsLineSpeed_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 2, 9, 1, 2, 1, 7),
    _IsgVGIsdnCHStatsLineSpeed_Type()
)
isgVGIsdnCHStatsLineSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isgVGIsdnCHStatsLineSpeed.setStatus("mandatory")
_IsgVGIsdnCHStatsAsscPort_Type = Integer32
_IsgVGIsdnCHStatsAsscPort_Object = MibTableColumn
isgVGIsdnCHStatsAsscPort = _IsgVGIsdnCHStatsAsscPort_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 2, 9, 1, 2, 1, 8),
    _IsgVGIsdnCHStatsAsscPort_Type()
)
isgVGIsdnCHStatsAsscPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isgVGIsdnCHStatsAsscPort.setStatus("mandatory")


class _IsgVGIsdnCHStatsStrtTm_Type(DisplayString):
    """Custom type isgVGIsdnCHStatsStrtTm based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 18),
    )


_IsgVGIsdnCHStatsStrtTm_Type.__name__ = "DisplayString"
_IsgVGIsdnCHStatsStrtTm_Object = MibTableColumn
isgVGIsdnCHStatsStrtTm = _IsgVGIsdnCHStatsStrtTm_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 2, 9, 1, 2, 1, 9),
    _IsgVGIsdnCHStatsStrtTm_Type()
)
isgVGIsdnCHStatsStrtTm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isgVGIsdnCHStatsStrtTm.setStatus("mandatory")


class _IsgVGIsdnCHStatsEndTm_Type(DisplayString):
    """Custom type isgVGIsdnCHStatsEndTm based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 13),
    )


_IsgVGIsdnCHStatsEndTm_Type.__name__ = "DisplayString"
_IsgVGIsdnCHStatsEndTm_Object = MibTableColumn
isgVGIsdnCHStatsEndTm = _IsgVGIsdnCHStatsEndTm_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 2, 9, 1, 2, 1, 10),
    _IsgVGIsdnCHStatsEndTm_Type()
)
isgVGIsdnCHStatsEndTm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isgVGIsdnCHStatsEndTm.setStatus("mandatory")
_IsgVGIsdnPRICCStatsTbl_Object = MibTable
isgVGIsdnPRICCStatsTbl = _IsgVGIsdnPRICCStatsTbl_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 2, 9, 1, 3)
)
if mibBuilder.loadTexts:
    isgVGIsdnPRICCStatsTbl.setStatus("mandatory")
_IsgVGIsdnPRICCStatsTblEntry_Object = MibTableRow
isgVGIsdnPRICCStatsTblEntry = _IsgVGIsdnPRICCStatsTblEntry_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 2, 9, 1, 3, 1)
)
isgVGIsdnPRICCStatsTblEntry.setIndexNames(
    (0, "ISDN-OPT-MIB", "isgVGIsdnPRICCStatsDSLNum"),
)
if mibBuilder.loadTexts:
    isgVGIsdnPRICCStatsTblEntry.setStatus("mandatory")
_IsgVGIsdnPRICCStatsDSLNum_Type = Integer32
_IsgVGIsdnPRICCStatsDSLNum_Object = MibTableColumn
isgVGIsdnPRICCStatsDSLNum = _IsgVGIsdnPRICCStatsDSLNum_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 2, 9, 1, 3, 1, 1),
    _IsgVGIsdnPRICCStatsDSLNum_Type()
)
isgVGIsdnPRICCStatsDSLNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isgVGIsdnPRICCStatsDSLNum.setStatus("mandatory")


class _IsgVGIsdnPRICCStatsSwtchType_Type(Integer32):
    """Custom type isgVGIsdnPRICCStatsSwtchType based on Integer32"""
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
        *(("pri5essStype", 3),
          ("priDms100Stype", 4),
          ("priEtsiStype", 7),
          ("priNi2Stype", 2),
          ("priNttStype", 5),
          ("priQsigMStype", 8),
          ("priQsigSStype", 9),
          ("priT1QsigMStype", 10),
          ("priT1QsigSStype", 11),
          ("priTs014Stype", 6),
          ("priUnspecifiedStype", 1),
          ("unsupported", 12))
    )


_IsgVGIsdnPRICCStatsSwtchType_Type.__name__ = "Integer32"
_IsgVGIsdnPRICCStatsSwtchType_Object = MibTableColumn
isgVGIsdnPRICCStatsSwtchType = _IsgVGIsdnPRICCStatsSwtchType_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 2, 9, 1, 3, 1, 2),
    _IsgVGIsdnPRICCStatsSwtchType_Type()
)
isgVGIsdnPRICCStatsSwtchType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isgVGIsdnPRICCStatsSwtchType.setStatus("mandatory")


class _IsgVGIsdnPRICCStatsDChannelState_Type(Integer32):
    """Custom type isgVGIsdnPRICCStatsDChannelState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("dChannelDown", 2),
          ("dChannelUp", 1),
          ("unknown", 3))
    )


_IsgVGIsdnPRICCStatsDChannelState_Type.__name__ = "Integer32"
_IsgVGIsdnPRICCStatsDChannelState_Object = MibTableColumn
isgVGIsdnPRICCStatsDChannelState = _IsgVGIsdnPRICCStatsDChannelState_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 2, 9, 1, 3, 1, 3),
    _IsgVGIsdnPRICCStatsDChannelState_Type()
)
isgVGIsdnPRICCStatsDChannelState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isgVGIsdnPRICCStatsDChannelState.setStatus("mandatory")
_Cdx6500Controls_ObjectIdentity = ObjectIdentity
cdx6500Controls = _Cdx6500Controls_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 4)
)
_IsgIsdnCtrlGroup_ObjectIdentity = ObjectIdentity
isgIsdnCtrlGroup = _IsgIsdnCtrlGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 4, 8)
)


class _IsgVGIsdnBootChannel_Type(Integer32):
    """Custom type isgVGIsdnBootChannel based on Integer32"""
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


_IsgVGIsdnBootChannel_Type.__name__ = "Integer32"
_IsgVGIsdnBootChannel_Object = MibScalar
isgVGIsdnBootChannel = _IsgVGIsdnBootChannel_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 4, 8, 1),
    _IsgVGIsdnBootChannel_Type()
)
isgVGIsdnBootChannel.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    isgVGIsdnBootChannel.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ISDN-OPT-MIB",
    **{"DisplayString": DisplayString,
       "codex": codex,
       "cdxProductSpecific": cdxProductSpecific,
       "cdx6500": cdx6500,
       "cdx6500Configuration": cdx6500Configuration,
       "cdx6500CfgGeneralGroup": cdx6500CfgGeneralGroup,
       "isgIsdnCfgGroup": isgIsdnCfgGroup,
       "isgVGIsdnCfgChanTable": isgVGIsdnCfgChanTable,
       "isgVGIsdnCfgChanTableEntry": isgVGIsdnCfgChanTableEntry,
       "isgVGIsdnCfgEntryNum": isgVGIsdnCfgEntryNum,
       "isgVGIsdnCfgChanType": isgVGIsdnCfgChanType,
       "isgVGIsdnCfgDChanPort": isgVGIsdnCfgDChanPort,
       "isgVGIsdnCfgSwitchType": isgVGIsdnCfgSwitchType,
       "isgVGIsdnCfgDChanTEI": isgVGIsdnCfgDChanTEI,
       "isgVGIsdnCfgDPckTraffic": isgVGIsdnCfgDPckTraffic,
       "isgVGIsdnCfgDChanDN": isgVGIsdnCfgDChanDN,
       "isgVGIsdnCfgDSPID": isgVGIsdnCfgDSPID,
       "isgVGIsdnCfgFirstBChanPort": isgVGIsdnCfgFirstBChanPort,
       "isgVGIsdnCfgFirstAccType": isgVGIsdnCfgFirstAccType,
       "isgVGIsdnCfgFirstCallDisablSTm": isgVGIsdnCfgFirstCallDisablSTm,
       "isgVGIsdnCfgFirstCallEnablSTm": isgVGIsdnCfgFirstCallEnablSTm,
       "isgVGIsdnCfgFirstSPBU": isgVGIsdnCfgFirstSPBU,
       "isgVGIsdnCfgFirstSPBUOpt": isgVGIsdnCfgFirstSPBUOpt,
       "isgVGIsdnCfgFirstSPBUTmOut": isgVGIsdnCfgFirstSPBUTmOut,
       "isgVGIsdnCfgFirstRate": isgVGIsdnCfgFirstRate,
       "isgVGIsdnCfgFirstTEI": isgVGIsdnCfgFirstTEI,
       "isgVGIsdnCfgFirstSPID": isgVGIsdnCfgFirstSPID,
       "isgVGIsdnCfgFirstDN": isgVGIsdnCfgFirstDN,
       "isgVGIsdnCfgFirstSubAddr": isgVGIsdnCfgFirstSubAddr,
       "isgVGIsdnCfgFirstOutDialNum1": isgVGIsdnCfgFirstOutDialNum1,
       "isgVGIsdnCfgFirstOutDialNum2": isgVGIsdnCfgFirstOutDialNum2,
       "isgVGIsdnCfgFirstDialRetryIntrvl": isgVGIsdnCfgFirstDialRetryIntrvl,
       "isgVGIsdnCfgFirstNumCallRetries": isgVGIsdnCfgFirstNumCallRetries,
       "isgVGIsdnCfgSecondChanPort": isgVGIsdnCfgSecondChanPort,
       "isgVGIsdnCfgSecondAccType": isgVGIsdnCfgSecondAccType,
       "isgVGIsdnCfgSecondCallDisablSTm": isgVGIsdnCfgSecondCallDisablSTm,
       "isgVGIsdnCfgSecondCallEnablSTm": isgVGIsdnCfgSecondCallEnablSTm,
       "isgVGIsdnCfgSecondSPBU": isgVGIsdnCfgSecondSPBU,
       "isgVGIsdnCfgSecondSPBUOpt": isgVGIsdnCfgSecondSPBUOpt,
       "isgVGIsdnCfgSecondSPBUTmOut": isgVGIsdnCfgSecondSPBUTmOut,
       "isgVGIsdnCfgSecondRate": isgVGIsdnCfgSecondRate,
       "isgVGIsdnCfgSecondTEI": isgVGIsdnCfgSecondTEI,
       "isgVGIsdnCfgSecondSPID": isgVGIsdnCfgSecondSPID,
       "isgVGIsdnCfgSecondDN": isgVGIsdnCfgSecondDN,
       "isgVGIsdnCfgSecondSubAddr": isgVGIsdnCfgSecondSubAddr,
       "isgVGIsdnCfgSecondOutDialNum1": isgVGIsdnCfgSecondOutDialNum1,
       "isgVGIsdnCfgSecondOutDialNum2": isgVGIsdnCfgSecondOutDialNum2,
       "isgVGIsdnCfgSecondDialRetryIntrvl": isgVGIsdnCfgSecondDialRetryIntrvl,
       "isgVGIsdnCfgSecondNumCallRetries": isgVGIsdnCfgSecondNumCallRetries,
       "isgVGIsdnCfgFirstPlainOldTelSet": isgVGIsdnCfgFirstPlainOldTelSet,
       "isgVGIsdnCfgFirstCallPerm": isgVGIsdnCfgFirstCallPerm,
       "isgVGIsdnCfgFirstChSelect": isgVGIsdnCfgFirstChSelect,
       "isgVGIsdnCfgSecondPlainOldTelSet": isgVGIsdnCfgSecondPlainOldTelSet,
       "isgVGIsdnCfgSecondCallPerm": isgVGIsdnCfgSecondCallPerm,
       "isgVGIsdnCfgSecondChSelect": isgVGIsdnCfgSecondChSelect,
       "cdx6500Statistics": cdx6500Statistics,
       "cdx6500StatOtherStatsGroup": cdx6500StatOtherStatsGroup,
       "isgIsdnStatsGroup": isgIsdnStatsGroup,
       "isgVGIsdnStats": isgVGIsdnStats,
       "isgVGIsdnCCStatsTbl": isgVGIsdnCCStatsTbl,
       "isgVGIsdnCCStatsTblEntry": isgVGIsdnCCStatsTblEntry,
       "isgVGIsdnCCStatsDSLNum": isgVGIsdnCCStatsDSLNum,
       "isgVGIsdnCCStatsChType": isgVGIsdnCCStatsChType,
       "isgVGIsdnCCStatsSwtchType": isgVGIsdnCCStatsSwtchType,
       "isgVGIsdnCCStatsL1State": isgVGIsdnCCStatsL1State,
       "isgVGIsdnCCStatsTEI": isgVGIsdnCCStatsTEI,
       "isgVGIsdnCCStatsCallgAddr": isgVGIsdnCCStatsCallgAddr,
       "isgVGIsdnCCStatsCalldAddr": isgVGIsdnCCStatsCalldAddr,
       "isgVGIsdnCCStatsSubaddr": isgVGIsdnCCStatsSubaddr,
       "isgVGIsdnCCStatsDirection": isgVGIsdnCCStatsDirection,
       "isgVGIsdnCCStatsAccType": isgVGIsdnCCStatsAccType,
       "isgVGIsdnCCStatsCallStatus": isgVGIsdnCCStatsCallStatus,
       "isgVGIsdnCCStatsLineSpeed": isgVGIsdnCCStatsLineSpeed,
       "isgVGIsdnCCStatsPortConn": isgVGIsdnCCStatsPortConn,
       "isgVGIsdnCCStatsCauseCode": isgVGIsdnCCStatsCauseCode,
       "isgVGIsdnCCStatsCallStarted": isgVGIsdnCCStatsCallStarted,
       "isgVGIsdnCCStatsDChanStatus": isgVGIsdnCCStatsDChanStatus,
       "isgVGIsdnCCStatsTrmStatus": isgVGIsdnCCStatsTrmStatus,
       "isgVGIsdnCCStatsTrmTei": isgVGIsdnCCStatsTrmTei,
       "isgVGIsdnCHStatsTbl": isgVGIsdnCHStatsTbl,
       "isgVGIsdnCHStatsTblEntry": isgVGIsdnCHStatsTblEntry,
       "isgVGIsdnCHStatsDSLNum": isgVGIsdnCHStatsDSLNum,
       "isgVGIsdnCHStatsChType": isgVGIsdnCHStatsChType,
       "isgVGIsdnCHStatsSession": isgVGIsdnCHStatsSession,
       "isgVGIsdnCHStatsNumCalld": isgVGIsdnCHStatsNumCalld,
       "isgVGIsdnCHStatsDirection": isgVGIsdnCHStatsDirection,
       "isgVGIsdnCHStatsCauseCode": isgVGIsdnCHStatsCauseCode,
       "isgVGIsdnCHStatsLineSpeed": isgVGIsdnCHStatsLineSpeed,
       "isgVGIsdnCHStatsAsscPort": isgVGIsdnCHStatsAsscPort,
       "isgVGIsdnCHStatsStrtTm": isgVGIsdnCHStatsStrtTm,
       "isgVGIsdnCHStatsEndTm": isgVGIsdnCHStatsEndTm,
       "isgVGIsdnPRICCStatsTbl": isgVGIsdnPRICCStatsTbl,
       "isgVGIsdnPRICCStatsTblEntry": isgVGIsdnPRICCStatsTblEntry,
       "isgVGIsdnPRICCStatsDSLNum": isgVGIsdnPRICCStatsDSLNum,
       "isgVGIsdnPRICCStatsSwtchType": isgVGIsdnPRICCStatsSwtchType,
       "isgVGIsdnPRICCStatsDChannelState": isgVGIsdnPRICCStatsDChannelState,
       "cdx6500Controls": cdx6500Controls,
       "isgIsdnCtrlGroup": isgIsdnCtrlGroup,
       "isgVGIsdnBootChannel": isgVGIsdnBootChannel}
)
