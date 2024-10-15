# SNMP MIB module (VERILINK-ENTERPRISE-CSUNCM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/VERILINK-ENTERPRISE-CSUNCM-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:12:10 2024
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

(ncm_csu,) = mibBuilder.importSymbols(
    "VERILINK-ENTERPRISE-NCMALARM-MIB",
    "ncm-csu")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_NcmcsuMainConfigTable_Object = MibTable
ncmcsuMainConfigTable = _NcmcsuMainConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3025, 6000)
)
if mibBuilder.loadTexts:
    ncmcsuMainConfigTable.setStatus("mandatory")
_NcmcsuMainConfigEntry_Object = MibTableRow
ncmcsuMainConfigEntry = _NcmcsuMainConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3025, 6000, 1)
)
ncmcsuMainConfigEntry.setIndexNames(
    (0, "VERILINK-ENTERPRISE-CSUNCM-MIB", "ncmcsuNIDMainConfigIndex"),
    (0, "VERILINK-ENTERPRISE-CSUNCM-MIB", "ncmcsuMainLineIndex"),
)
if mibBuilder.loadTexts:
    ncmcsuMainConfigEntry.setStatus("mandatory")
_NcmcsuNIDMainConfigIndex_Type = Integer32
_NcmcsuNIDMainConfigIndex_Object = MibTableColumn
ncmcsuNIDMainConfigIndex = _NcmcsuNIDMainConfigIndex_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3025, 6000, 1, 1),
    _NcmcsuNIDMainConfigIndex_Type()
)
ncmcsuNIDMainConfigIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmcsuNIDMainConfigIndex.setStatus("mandatory")
_NcmcsuMainLineIndex_Type = Integer32
_NcmcsuMainLineIndex_Object = MibTableColumn
ncmcsuMainLineIndex = _NcmcsuMainLineIndex_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3025, 6000, 1, 2),
    _NcmcsuMainLineIndex_Type()
)
ncmcsuMainLineIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmcsuMainLineIndex.setStatus("mandatory")


class _NcmcsuFormat_Type(Integer32):
    """Custom type ncmcsuFormat based on Integer32"""
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
        *(("esf", 3),
          ("sf", 2),
          ("unframed", 1),
          ("zbtsi", 4))
    )


_NcmcsuFormat_Type.__name__ = "Integer32"
_NcmcsuFormat_Object = MibTableColumn
ncmcsuFormat = _NcmcsuFormat_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3025, 6000, 1, 3),
    _NcmcsuFormat_Type()
)
ncmcsuFormat.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ncmcsuFormat.setStatus("mandatory")


class _NcmcsuLineCode_Type(Integer32):
    """Custom type ncmcsuLineCode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ami", 1),
          ("b8zs", 2))
    )


_NcmcsuLineCode_Type.__name__ = "Integer32"
_NcmcsuLineCode_Object = MibTableColumn
ncmcsuLineCode = _NcmcsuLineCode_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3025, 6000, 1, 4),
    _NcmcsuLineCode_Type()
)
ncmcsuLineCode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ncmcsuLineCode.setStatus("mandatory")


class _NcmcsuEQCableLength_Type(Integer32):
    """Custom type ncmcsuEQCableLength based on Integer32"""
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
        *(("fT-133-266", 2),
          ("fT-266-399", 3),
          ("fT-399-533", 4),
          ("fT-533-655", 5),
          ("ft-0-133", 1))
    )


_NcmcsuEQCableLength_Type.__name__ = "Integer32"
_NcmcsuEQCableLength_Object = MibTableColumn
ncmcsuEQCableLength = _NcmcsuEQCableLength_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3025, 6000, 1, 5),
    _NcmcsuEQCableLength_Type()
)
ncmcsuEQCableLength.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ncmcsuEQCableLength.setStatus("mandatory")


class _NcmcsuTiming_Type(Integer32):
    """Custom type ncmcsuTiming based on Integer32"""
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
        *(("dsu", 8),
          ("eq", 6),
          ("ext-ttl", 4),
          ("external-422", 3),
          ("internal", 2),
          ("net", 5),
          ("through", 1),
          ("tiu", 7))
    )


_NcmcsuTiming_Type.__name__ = "Integer32"
_NcmcsuTiming_Object = MibTableColumn
ncmcsuTiming = _NcmcsuTiming_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3025, 6000, 1, 6),
    _NcmcsuTiming_Type()
)
ncmcsuTiming.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ncmcsuTiming.setStatus("mandatory")


class _Ncmdsudatabus_Type(Integer32):
    """Custom type ncmdsudatabus based on Integer32"""
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
        *(("bus-a", 2),
          ("bus-b", 3),
          ("bus-c", 4),
          ("drop-uses-bus-b", 5),
          ("insert-uses-bus-a", 6),
          ("none", 1))
    )


_Ncmdsudatabus_Type.__name__ = "Integer32"
_Ncmdsudatabus_Object = MibTableColumn
ncmdsudatabus = _Ncmdsudatabus_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3025, 6000, 1, 7),
    _Ncmdsudatabus_Type()
)
ncmdsudatabus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ncmdsudatabus.setStatus("mandatory")


class _NcmcsuNetLineBuildOut_Type(Integer32):
    """Custom type ncmcsuNetLineBuildOut based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("db-Fifteen", 3),
          ("db-Seven-point-five", 2),
          ("db-Zero", 1))
    )


_NcmcsuNetLineBuildOut_Type.__name__ = "Integer32"
_NcmcsuNetLineBuildOut_Object = MibTableColumn
ncmcsuNetLineBuildOut = _NcmcsuNetLineBuildOut_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3025, 6000, 1, 8),
    _NcmcsuNetLineBuildOut_Type()
)
ncmcsuNetLineBuildOut.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ncmcsuNetLineBuildOut.setStatus("mandatory")
_NcmcsuValidIntervals_Type = Integer32
_NcmcsuValidIntervals_Object = MibTableColumn
ncmcsuValidIntervals = _NcmcsuValidIntervals_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3025, 6000, 1, 9),
    _NcmcsuValidIntervals_Type()
)
ncmcsuValidIntervals.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmcsuValidIntervals.setStatus("mandatory")
_NcmcsuCurrentIntervalSec_Type = Integer32
_NcmcsuCurrentIntervalSec_Object = MibTableColumn
ncmcsuCurrentIntervalSec = _NcmcsuCurrentIntervalSec_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3025, 6000, 1, 10),
    _NcmcsuCurrentIntervalSec_Type()
)
ncmcsuCurrentIntervalSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmcsuCurrentIntervalSec.setStatus("mandatory")


class _NcmcsuJitterBuf_Type(Integer32):
    """Custom type ncmcsuJitterBuf based on Integer32"""
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
        *(("eq-Net-16-16", 1),
          ("eq-Net-16-40", 3),
          ("eq-Net-40-16", 2),
          ("eq-Net-40-40", 4))
    )


_NcmcsuJitterBuf_Type.__name__ = "Integer32"
_NcmcsuJitterBuf_Object = MibTableColumn
ncmcsuJitterBuf = _NcmcsuJitterBuf_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3025, 6000, 1, 11),
    _NcmcsuJitterBuf_Type()
)
ncmcsuJitterBuf.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ncmcsuJitterBuf.setStatus("mandatory")


class _NcmcsuTestSigCfgEnable_Type(Integer32):
    """Custom type ncmcsuTestSigCfgEnable based on Integer32"""
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


_NcmcsuTestSigCfgEnable_Type.__name__ = "Integer32"
_NcmcsuTestSigCfgEnable_Object = MibTableColumn
ncmcsuTestSigCfgEnable = _NcmcsuTestSigCfgEnable_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3025, 6000, 1, 12),
    _NcmcsuTestSigCfgEnable_Type()
)
ncmcsuTestSigCfgEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ncmcsuTestSigCfgEnable.setStatus("mandatory")


class _NcmcsuTestSigCfgFrameSignal_Type(Integer32):
    """Custom type ncmcsuTestSigCfgFrameSignal based on Integer32"""
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


_NcmcsuTestSigCfgFrameSignal_Type.__name__ = "Integer32"
_NcmcsuTestSigCfgFrameSignal_Object = MibTableColumn
ncmcsuTestSigCfgFrameSignal = _NcmcsuTestSigCfgFrameSignal_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3025, 6000, 1, 13),
    _NcmcsuTestSigCfgFrameSignal_Type()
)
ncmcsuTestSigCfgFrameSignal.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ncmcsuTestSigCfgFrameSignal.setStatus("mandatory")
_NcmcsuRLBTimeoutIndex_Type = Integer32
_NcmcsuRLBTimeoutIndex_Object = MibTableColumn
ncmcsuRLBTimeoutIndex = _NcmcsuRLBTimeoutIndex_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3025, 6000, 1, 14),
    _NcmcsuRLBTimeoutIndex_Type()
)
ncmcsuRLBTimeoutIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ncmcsuRLBTimeoutIndex.setStatus("mandatory")


class _NcmcsuCfgRptSendPRM_Type(Integer32):
    """Custom type ncmcsuCfgRptSendPRM based on Integer32"""
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


_NcmcsuCfgRptSendPRM_Type.__name__ = "Integer32"
_NcmcsuCfgRptSendPRM_Object = MibTableColumn
ncmcsuCfgRptSendPRM = _NcmcsuCfgRptSendPRM_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3025, 6000, 1, 15),
    _NcmcsuCfgRptSendPRM_Type()
)
ncmcsuCfgRptSendPRM.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ncmcsuCfgRptSendPRM.setStatus("mandatory")


class _NcmcsuCfgRptPollFarEnd_Type(Integer32):
    """Custom type ncmcsuCfgRptPollFarEnd based on Integer32"""
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


_NcmcsuCfgRptPollFarEnd_Type.__name__ = "Integer32"
_NcmcsuCfgRptPollFarEnd_Object = MibTableColumn
ncmcsuCfgRptPollFarEnd = _NcmcsuCfgRptPollFarEnd_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3025, 6000, 1, 16),
    _NcmcsuCfgRptPollFarEnd_Type()
)
ncmcsuCfgRptPollFarEnd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ncmcsuCfgRptPollFarEnd.setStatus("mandatory")


class _NcmcsuCfgRptDataLinkUnsolicit_Type(Integer32):
    """Custom type ncmcsuCfgRptDataLinkUnsolicit based on Integer32"""
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


_NcmcsuCfgRptDataLinkUnsolicit_Type.__name__ = "Integer32"
_NcmcsuCfgRptDataLinkUnsolicit_Object = MibTableColumn
ncmcsuCfgRptDataLinkUnsolicit = _NcmcsuCfgRptDataLinkUnsolicit_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3025, 6000, 1, 17),
    _NcmcsuCfgRptDataLinkUnsolicit_Type()
)
ncmcsuCfgRptDataLinkUnsolicit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ncmcsuCfgRptDataLinkUnsolicit.setStatus("mandatory")


class _NcmcsuCfgRptAlmReporting_Type(Integer32):
    """Custom type ncmcsuCfgRptAlmReporting based on Integer32"""
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


_NcmcsuCfgRptAlmReporting_Type.__name__ = "Integer32"
_NcmcsuCfgRptAlmReporting_Object = MibTableColumn
ncmcsuCfgRptAlmReporting = _NcmcsuCfgRptAlmReporting_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3025, 6000, 1, 18),
    _NcmcsuCfgRptAlmReporting_Type()
)
ncmcsuCfgRptAlmReporting.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ncmcsuCfgRptAlmReporting.setStatus("mandatory")


class _NcmcsuCfgRptPRMType_Type(Integer32):
    """Custom type ncmcsuCfgRptPRMType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("nO-PRM", 1),
          ("uSER", 2))
    )


_NcmcsuCfgRptPRMType_Type.__name__ = "Integer32"
_NcmcsuCfgRptPRMType_Object = MibTableColumn
ncmcsuCfgRptPRMType = _NcmcsuCfgRptPRMType_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3025, 6000, 1, 19),
    _NcmcsuCfgRptPRMType_Type()
)
ncmcsuCfgRptPRMType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ncmcsuCfgRptPRMType.setStatus("mandatory")


class _NcmcsuCfgCodeRegenCRC_Type(Integer32):
    """Custom type ncmcsuCfgCodeRegenCRC based on Integer32"""
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
        *(("both", 4),
          ("eq-to-Net", 3),
          ("net-to-Eq", 2),
          ("pass", 1))
    )


_NcmcsuCfgCodeRegenCRC_Type.__name__ = "Integer32"
_NcmcsuCfgCodeRegenCRC_Object = MibTableColumn
ncmcsuCfgCodeRegenCRC = _NcmcsuCfgCodeRegenCRC_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3025, 6000, 1, 20),
    _NcmcsuCfgCodeRegenCRC_Type()
)
ncmcsuCfgCodeRegenCRC.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ncmcsuCfgCodeRegenCRC.setStatus("mandatory")


class _NcmcsuCfgCodeXYellowAlarm_Type(Integer32):
    """Custom type ncmcsuCfgCodeXYellowAlarm based on Integer32"""
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
        *(("both", 4),
          ("eq-to-Net", 3),
          ("net-to-Eq", 2),
          ("off", 1))
    )


_NcmcsuCfgCodeXYellowAlarm_Type.__name__ = "Integer32"
_NcmcsuCfgCodeXYellowAlarm_Object = MibTableColumn
ncmcsuCfgCodeXYellowAlarm = _NcmcsuCfgCodeXYellowAlarm_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3025, 6000, 1, 21),
    _NcmcsuCfgCodeXYellowAlarm_Type()
)
ncmcsuCfgCodeXYellowAlarm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ncmcsuCfgCodeXYellowAlarm.setStatus("mandatory")


class _NcmcsuCfgCodeEQFIFO_Type(Integer32):
    """Custom type ncmcsuCfgCodeEQFIFO based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("fifteen-bits", 1),
          ("forty-bits", 2))
    )


_NcmcsuCfgCodeEQFIFO_Type.__name__ = "Integer32"
_NcmcsuCfgCodeEQFIFO_Object = MibTableColumn
ncmcsuCfgCodeEQFIFO = _NcmcsuCfgCodeEQFIFO_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3025, 6000, 1, 22),
    _NcmcsuCfgCodeEQFIFO_Type()
)
ncmcsuCfgCodeEQFIFO.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ncmcsuCfgCodeEQFIFO.setStatus("mandatory")


class _NcmcsuCfgCodeNETFIFO_Type(Integer32):
    """Custom type ncmcsuCfgCodeNETFIFO based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("fifteen-bits", 1),
          ("forty-bits", 2))
    )


_NcmcsuCfgCodeNETFIFO_Type.__name__ = "Integer32"
_NcmcsuCfgCodeNETFIFO_Object = MibTableColumn
ncmcsuCfgCodeNETFIFO = _NcmcsuCfgCodeNETFIFO_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3025, 6000, 1, 23),
    _NcmcsuCfgCodeNETFIFO_Type()
)
ncmcsuCfgCodeNETFIFO.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ncmcsuCfgCodeNETFIFO.setStatus("mandatory")


class _NcmcsuCfgCodeTranMode_Type(Integer32):
    """Custom type ncmcsuCfgCodeTranMode based on Integer32"""
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


_NcmcsuCfgCodeTranMode_Type.__name__ = "Integer32"
_NcmcsuCfgCodeTranMode_Object = MibTableColumn
ncmcsuCfgCodeTranMode = _NcmcsuCfgCodeTranMode_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3025, 6000, 1, 24),
    _NcmcsuCfgCodeTranMode_Type()
)
ncmcsuCfgCodeTranMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ncmcsuCfgCodeTranMode.setStatus("mandatory")


class _NcmcsuCfgCodeSend1sLnkIdle_Type(Integer32):
    """Custom type ncmcsuCfgCodeSend1sLnkIdle based on Integer32"""
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


_NcmcsuCfgCodeSend1sLnkIdle_Type.__name__ = "Integer32"
_NcmcsuCfgCodeSend1sLnkIdle_Object = MibTableColumn
ncmcsuCfgCodeSend1sLnkIdle = _NcmcsuCfgCodeSend1sLnkIdle_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3025, 6000, 1, 25),
    _NcmcsuCfgCodeSend1sLnkIdle_Type()
)
ncmcsuCfgCodeSend1sLnkIdle.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ncmcsuCfgCodeSend1sLnkIdle.setStatus("mandatory")


class _NcmcsuCfgAlmSelfTest_Type(Integer32):
    """Custom type ncmcsuCfgAlmSelfTest based on Integer32"""
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


_NcmcsuCfgAlmSelfTest_Type.__name__ = "Integer32"
_NcmcsuCfgAlmSelfTest_Object = MibTableColumn
ncmcsuCfgAlmSelfTest = _NcmcsuCfgAlmSelfTest_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3025, 6000, 1, 26),
    _NcmcsuCfgAlmSelfTest_Type()
)
ncmcsuCfgAlmSelfTest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ncmcsuCfgAlmSelfTest.setStatus("mandatory")


class _NcmcsuCfgAlmEnableTestState_Type(Integer32):
    """Custom type ncmcsuCfgAlmEnableTestState based on Integer32"""
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


_NcmcsuCfgAlmEnableTestState_Type.__name__ = "Integer32"
_NcmcsuCfgAlmEnableTestState_Object = MibTableColumn
ncmcsuCfgAlmEnableTestState = _NcmcsuCfgAlmEnableTestState_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3025, 6000, 1, 27),
    _NcmcsuCfgAlmEnableTestState_Type()
)
ncmcsuCfgAlmEnableTestState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ncmcsuCfgAlmEnableTestState.setStatus("mandatory")


class _NcmcsuCfgAlmUnframedMode_Type(Integer32):
    """Custom type ncmcsuCfgAlmUnframedMode based on Integer32"""
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


_NcmcsuCfgAlmUnframedMode_Type.__name__ = "Integer32"
_NcmcsuCfgAlmUnframedMode_Object = MibTableColumn
ncmcsuCfgAlmUnframedMode = _NcmcsuCfgAlmUnframedMode_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3025, 6000, 1, 28),
    _NcmcsuCfgAlmUnframedMode_Type()
)
ncmcsuCfgAlmUnframedMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ncmcsuCfgAlmUnframedMode.setStatus("mandatory")


class _NcmcsuCfgAlmOnEqLoop_Type(Integer32):
    """Custom type ncmcsuCfgAlmOnEqLoop based on Integer32"""
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


_NcmcsuCfgAlmOnEqLoop_Type.__name__ = "Integer32"
_NcmcsuCfgAlmOnEqLoop_Object = MibTableColumn
ncmcsuCfgAlmOnEqLoop = _NcmcsuCfgAlmOnEqLoop_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3025, 6000, 1, 29),
    _NcmcsuCfgAlmOnEqLoop_Type()
)
ncmcsuCfgAlmOnEqLoop.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ncmcsuCfgAlmOnEqLoop.setStatus("mandatory")


class _NcmcsuCfgAlmOnNetLoop_Type(Integer32):
    """Custom type ncmcsuCfgAlmOnNetLoop based on Integer32"""
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


_NcmcsuCfgAlmOnNetLoop_Type.__name__ = "Integer32"
_NcmcsuCfgAlmOnNetLoop_Object = MibTableColumn
ncmcsuCfgAlmOnNetLoop = _NcmcsuCfgAlmOnNetLoop_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3025, 6000, 1, 30),
    _NcmcsuCfgAlmOnNetLoop_Type()
)
ncmcsuCfgAlmOnNetLoop.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ncmcsuCfgAlmOnNetLoop.setStatus("mandatory")


class _NcmcsuCfgAlmOnPowerUpLoop_Type(Integer32):
    """Custom type ncmcsuCfgAlmOnPowerUpLoop based on Integer32"""
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


_NcmcsuCfgAlmOnPowerUpLoop_Type.__name__ = "Integer32"
_NcmcsuCfgAlmOnPowerUpLoop_Object = MibTableColumn
ncmcsuCfgAlmOnPowerUpLoop = _NcmcsuCfgAlmOnPowerUpLoop_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3025, 6000, 1, 31),
    _NcmcsuCfgAlmOnPowerUpLoop_Type()
)
ncmcsuCfgAlmOnPowerUpLoop.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ncmcsuCfgAlmOnPowerUpLoop.setStatus("mandatory")


class _NcmcsuCfgLoopRespLLB_Type(Integer32):
    """Custom type ncmcsuCfgLoopRespLLB based on Integer32"""
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


_NcmcsuCfgLoopRespLLB_Type.__name__ = "Integer32"
_NcmcsuCfgLoopRespLLB_Object = MibTableColumn
ncmcsuCfgLoopRespLLB = _NcmcsuCfgLoopRespLLB_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3025, 6000, 1, 32),
    _NcmcsuCfgLoopRespLLB_Type()
)
ncmcsuCfgLoopRespLLB.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ncmcsuCfgLoopRespLLB.setStatus("mandatory")


class _NcmcsuCfgLoopRespPLB_Type(Integer32):
    """Custom type ncmcsuCfgLoopRespPLB based on Integer32"""
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


_NcmcsuCfgLoopRespPLB_Type.__name__ = "Integer32"
_NcmcsuCfgLoopRespPLB_Object = MibTableColumn
ncmcsuCfgLoopRespPLB = _NcmcsuCfgLoopRespPLB_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3025, 6000, 1, 33),
    _NcmcsuCfgLoopRespPLB_Type()
)
ncmcsuCfgLoopRespPLB.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ncmcsuCfgLoopRespPLB.setStatus("mandatory")


class _NcmcsuCfgLoopRespELB_Type(Integer32):
    """Custom type ncmcsuCfgLoopRespELB based on Integer32"""
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


_NcmcsuCfgLoopRespELB_Type.__name__ = "Integer32"
_NcmcsuCfgLoopRespELB_Object = MibTableColumn
ncmcsuCfgLoopRespELB = _NcmcsuCfgLoopRespELB_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3025, 6000, 1, 34),
    _NcmcsuCfgLoopRespELB_Type()
)
ncmcsuCfgLoopRespELB.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ncmcsuCfgLoopRespELB.setStatus("mandatory")


class _NcmcsuCfgLoopRespRLB_Type(Integer32):
    """Custom type ncmcsuCfgLoopRespRLB based on Integer32"""
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


_NcmcsuCfgLoopRespRLB_Type.__name__ = "Integer32"
_NcmcsuCfgLoopRespRLB_Object = MibTableColumn
ncmcsuCfgLoopRespRLB = _NcmcsuCfgLoopRespRLB_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3025, 6000, 1, 35),
    _NcmcsuCfgLoopRespRLB_Type()
)
ncmcsuCfgLoopRespRLB.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ncmcsuCfgLoopRespRLB.setStatus("mandatory")


class _NcmcsuCfgLoopRespLLBTONE_Type(Integer32):
    """Custom type ncmcsuCfgLoopRespLLBTONE based on Integer32"""
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


_NcmcsuCfgLoopRespLLBTONE_Type.__name__ = "Integer32"
_NcmcsuCfgLoopRespLLBTONE_Object = MibTableColumn
ncmcsuCfgLoopRespLLBTONE = _NcmcsuCfgLoopRespLLBTONE_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3025, 6000, 1, 36),
    _NcmcsuCfgLoopRespLLBTONE_Type()
)
ncmcsuCfgLoopRespLLBTONE.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ncmcsuCfgLoopRespLLBTONE.setStatus("mandatory")


class _NcmcsuCfgLoopRespPLBTONE_Type(Integer32):
    """Custom type ncmcsuCfgLoopRespPLBTONE based on Integer32"""
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


_NcmcsuCfgLoopRespPLBTONE_Type.__name__ = "Integer32"
_NcmcsuCfgLoopRespPLBTONE_Object = MibTableColumn
ncmcsuCfgLoopRespPLBTONE = _NcmcsuCfgLoopRespPLBTONE_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3025, 6000, 1, 37),
    _NcmcsuCfgLoopRespPLBTONE_Type()
)
ncmcsuCfgLoopRespPLBTONE.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ncmcsuCfgLoopRespPLBTONE.setStatus("mandatory")


class _NcmcsuCfgSendReceiveInBandCode_Type(Integer32):
    """Custom type ncmcsuCfgSendReceiveInBandCode based on Integer32"""
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


_NcmcsuCfgSendReceiveInBandCode_Type.__name__ = "Integer32"
_NcmcsuCfgSendReceiveInBandCode_Object = MibTableColumn
ncmcsuCfgSendReceiveInBandCode = _NcmcsuCfgSendReceiveInBandCode_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3025, 6000, 1, 38),
    _NcmcsuCfgSendReceiveInBandCode_Type()
)
ncmcsuCfgSendReceiveInBandCode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ncmcsuCfgSendReceiveInBandCode.setStatus("mandatory")
_NcmcsuEnhanceConfigTable_Object = MibTable
ncmcsuEnhanceConfigTable = _NcmcsuEnhanceConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3025, 6001)
)
if mibBuilder.loadTexts:
    ncmcsuEnhanceConfigTable.setStatus("mandatory")
_NcmcsuEnhanceConfigEntry_Object = MibTableRow
ncmcsuEnhanceConfigEntry = _NcmcsuEnhanceConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3025, 6001, 1)
)
ncmcsuEnhanceConfigEntry.setIndexNames(
    (0, "VERILINK-ENTERPRISE-CSUNCM-MIB", "ncmcsuNIDEnhanceIndex"),
    (0, "VERILINK-ENTERPRISE-CSUNCM-MIB", "ncmcsuEnhanceLineIndex"),
)
if mibBuilder.loadTexts:
    ncmcsuEnhanceConfigEntry.setStatus("mandatory")
_NcmcsuNIDEnhanceIndex_Type = Integer32
_NcmcsuNIDEnhanceIndex_Object = MibTableColumn
ncmcsuNIDEnhanceIndex = _NcmcsuNIDEnhanceIndex_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3025, 6001, 1, 1),
    _NcmcsuNIDEnhanceIndex_Type()
)
ncmcsuNIDEnhanceIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmcsuNIDEnhanceIndex.setStatus("mandatory")
_NcmcsuEnhanceLineIndex_Type = Integer32
_NcmcsuEnhanceLineIndex_Object = MibTableColumn
ncmcsuEnhanceLineIndex = _NcmcsuEnhanceLineIndex_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3025, 6001, 1, 2),
    _NcmcsuEnhanceLineIndex_Type()
)
ncmcsuEnhanceLineIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmcsuEnhanceLineIndex.setStatus("mandatory")


class _NcmcsuNetworkKeepAlive_Type(Integer32):
    """Custom type ncmcsuNetworkKeepAlive based on Integer32"""
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
        *(("aIS", 3),
          ("framed-all-ones", 4),
          ("loop", 2),
          ("none", 1))
    )


_NcmcsuNetworkKeepAlive_Type.__name__ = "Integer32"
_NcmcsuNetworkKeepAlive_Object = MibTableColumn
ncmcsuNetworkKeepAlive = _NcmcsuNetworkKeepAlive_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3025, 6001, 1, 3),
    _NcmcsuNetworkKeepAlive_Type()
)
ncmcsuNetworkKeepAlive.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ncmcsuNetworkKeepAlive.setStatus("mandatory")
_NcmcsuAlarmSetDelay_Type = Integer32
_NcmcsuAlarmSetDelay_Object = MibTableColumn
ncmcsuAlarmSetDelay = _NcmcsuAlarmSetDelay_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3025, 6001, 1, 4),
    _NcmcsuAlarmSetDelay_Type()
)
ncmcsuAlarmSetDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ncmcsuAlarmSetDelay.setStatus("mandatory")
_NcmcsuAlarmClearDelay_Type = Integer32
_NcmcsuAlarmClearDelay_Object = MibTableColumn
ncmcsuAlarmClearDelay = _NcmcsuAlarmClearDelay_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3025, 6001, 1, 5),
    _NcmcsuAlarmClearDelay_Type()
)
ncmcsuAlarmClearDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ncmcsuAlarmClearDelay.setStatus("mandatory")


class _NcmcsuAlarmEnable_Type(Integer32):
    """Custom type ncmcsuAlarmEnable based on Integer32"""
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


_NcmcsuAlarmEnable_Type.__name__ = "Integer32"
_NcmcsuAlarmEnable_Object = MibTableColumn
ncmcsuAlarmEnable = _NcmcsuAlarmEnable_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3025, 6001, 1, 6),
    _NcmcsuAlarmEnable_Type()
)
ncmcsuAlarmEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ncmcsuAlarmEnable.setStatus("mandatory")


class _NcmcsuNetDensityEnforcement_Type(Integer32):
    """Custom type ncmcsuNetDensityEnforcement based on Integer32"""
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
        *(("eighty-zeroes", 4),
          ("fcc-part-68", 2),
          ("fifteen-zeroes", 5),
          ("none", 1),
          ("pub-62411", 3))
    )


_NcmcsuNetDensityEnforcement_Type.__name__ = "Integer32"
_NcmcsuNetDensityEnforcement_Object = MibTableColumn
ncmcsuNetDensityEnforcement = _NcmcsuNetDensityEnforcement_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3025, 6001, 1, 7),
    _NcmcsuNetDensityEnforcement_Type()
)
ncmcsuNetDensityEnforcement.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ncmcsuNetDensityEnforcement.setStatus("mandatory")


class _NcmcsuLoopback_Type(Integer32):
    """Custom type ncmcsuLoopback based on Integer32"""
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
              9,
              10)
        )
    )
    namedValues = NamedValues(
        *(("csu-Equip-Loop-Back", 4),
          ("csu-Line-Loop-Back", 2),
          ("csu-No-Loop-Back", 5),
          ("csu-Payload-Loop-Back", 1),
          ("deactivate-ELB-and-RLB", 7),
          ("deactivate-LLB-and-PLB", 6),
          ("repeater-Loop-Back", 3),
          ("send-Inband-Loop-Down", 10),
          ("send-Inband-Loop-Up", 9))
    )


_NcmcsuLoopback_Type.__name__ = "Integer32"
_NcmcsuLoopback_Object = MibTableColumn
ncmcsuLoopback = _NcmcsuLoopback_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3025, 6001, 1, 8),
    _NcmcsuLoopback_Type()
)
ncmcsuLoopback.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ncmcsuLoopback.setStatus("mandatory")


class _NcmcsuTestPattern_Type(Integer32):
    """Custom type ncmcsuTestPattern based on Integer32"""
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
        *(("all-ones-to-eq", 9),
          ("all-ones-to-net", 5),
          ("no-test", 1),
          ("one-in-eight-to-eq", 7),
          ("one-in-eight-to-net", 3),
          ("qrss-to-eq", 6),
          ("qrss-to-net", 2),
          ("three-in-twenty-four-to-eq", 8),
          ("three-in-twenty-four-to-net", 4))
    )


_NcmcsuTestPattern_Type.__name__ = "Integer32"
_NcmcsuTestPattern_Object = MibTableColumn
ncmcsuTestPattern = _NcmcsuTestPattern_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3025, 6001, 1, 9),
    _NcmcsuTestPattern_Type()
)
ncmcsuTestPattern.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ncmcsuTestPattern.setStatus("mandatory")


class _NcmcsuResetPerfReg_Type(Integer32):
    """Custom type ncmcsuResetPerfReg based on Integer32"""
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


_NcmcsuResetPerfReg_Type.__name__ = "Integer32"
_NcmcsuResetPerfReg_Object = MibTableColumn
ncmcsuResetPerfReg = _NcmcsuResetPerfReg_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3025, 6001, 1, 10),
    _NcmcsuResetPerfReg_Type()
)
ncmcsuResetPerfReg.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ncmcsuResetPerfReg.setStatus("mandatory")
_NcmcsuTestErrorCounter_Type = Gauge32
_NcmcsuTestErrorCounter_Object = MibTableColumn
ncmcsuTestErrorCounter = _NcmcsuTestErrorCounter_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3025, 6001, 1, 11),
    _NcmcsuTestErrorCounter_Type()
)
ncmcsuTestErrorCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmcsuTestErrorCounter.setStatus("mandatory")
_NcmcsuTestSecondsRemain_Type = Gauge32
_NcmcsuTestSecondsRemain_Object = MibTableColumn
ncmcsuTestSecondsRemain = _NcmcsuTestSecondsRemain_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3025, 6001, 1, 12),
    _NcmcsuTestSecondsRemain_Type()
)
ncmcsuTestSecondsRemain.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmcsuTestSecondsRemain.setStatus("mandatory")
_NcmcsuTestTimeSeconds_Type = Integer32
_NcmcsuTestTimeSeconds_Object = MibTableColumn
ncmcsuTestTimeSeconds = _NcmcsuTestTimeSeconds_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3025, 6001, 1, 13),
    _NcmcsuTestTimeSeconds_Type()
)
ncmcsuTestTimeSeconds.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ncmcsuTestTimeSeconds.setStatus("mandatory")
_NcmcsuNetLOFCIndexTime_Type = Integer32
_NcmcsuNetLOFCIndexTime_Object = MibTableColumn
ncmcsuNetLOFCIndexTime = _NcmcsuNetLOFCIndexTime_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3025, 6001, 1, 14),
    _NcmcsuNetLOFCIndexTime_Type()
)
ncmcsuNetLOFCIndexTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ncmcsuNetLOFCIndexTime.setStatus("mandatory")


class _NcmcsuChannelMask_Type(DisplayString):
    """Custom type ncmcsuChannelMask based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_NcmcsuChannelMask_Type.__name__ = "DisplayString"
_NcmcsuChannelMask_Object = MibTableColumn
ncmcsuChannelMask = _NcmcsuChannelMask_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3025, 6001, 1, 15),
    _NcmcsuChannelMask_Type()
)
ncmcsuChannelMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ncmcsuChannelMask.setStatus("mandatory")


class _NcmcsuApplication_Type(Integer32):
    """Custom type ncmcsuApplication based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("csu", 2),
          ("none", 1),
          ("smds", 3))
    )


_NcmcsuApplication_Type.__name__ = "Integer32"
_NcmcsuApplication_Object = MibTableColumn
ncmcsuApplication = _NcmcsuApplication_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3025, 6001, 1, 16),
    _NcmcsuApplication_Type()
)
ncmcsuApplication.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ncmcsuApplication.setStatus("mandatory")
_NcmcsuTestIntervalIndex_Type = Integer32
_NcmcsuTestIntervalIndex_Object = MibTableColumn
ncmcsuTestIntervalIndex = _NcmcsuTestIntervalIndex_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3025, 6001, 1, 17),
    _NcmcsuTestIntervalIndex_Type()
)
ncmcsuTestIntervalIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ncmcsuTestIntervalIndex.setStatus("mandatory")
_NcmcsuElementStatusOneTable_Object = MibTable
ncmcsuElementStatusOneTable = _NcmcsuElementStatusOneTable_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3025, 6002)
)
if mibBuilder.loadTexts:
    ncmcsuElementStatusOneTable.setStatus("mandatory")
_NcmcsuElementStatusOneEntry_Object = MibTableRow
ncmcsuElementStatusOneEntry = _NcmcsuElementStatusOneEntry_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3025, 6002, 1)
)
ncmcsuElementStatusOneEntry.setIndexNames(
    (0, "VERILINK-ENTERPRISE-CSUNCM-MIB", "ncmcsuNIDElementStatusIndex1"),
    (0, "VERILINK-ENTERPRISE-CSUNCM-MIB", "ncmcsuElementStatusIndex1"),
)
if mibBuilder.loadTexts:
    ncmcsuElementStatusOneEntry.setStatus("mandatory")
_NcmcsuNIDElementStatusIndex1_Type = Integer32
_NcmcsuNIDElementStatusIndex1_Object = MibTableColumn
ncmcsuNIDElementStatusIndex1 = _NcmcsuNIDElementStatusIndex1_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3025, 6002, 1, 1),
    _NcmcsuNIDElementStatusIndex1_Type()
)
ncmcsuNIDElementStatusIndex1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmcsuNIDElementStatusIndex1.setStatus("mandatory")
_NcmcsuElementStatusIndex1_Type = Integer32
_NcmcsuElementStatusIndex1_Object = MibTableColumn
ncmcsuElementStatusIndex1 = _NcmcsuElementStatusIndex1_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3025, 6002, 1, 2),
    _NcmcsuElementStatusIndex1_Type()
)
ncmcsuElementStatusIndex1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmcsuElementStatusIndex1.setStatus("mandatory")


class _NcmcsuExcessiveError_Type(Integer32):
    """Custom type ncmcsuExcessiveError based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ais", 2),
          ("signal", 1))
    )


_NcmcsuExcessiveError_Type.__name__ = "Integer32"
_NcmcsuExcessiveError_Object = MibTableColumn
ncmcsuExcessiveError = _NcmcsuExcessiveError_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3025, 6002, 1, 3),
    _NcmcsuExcessiveError_Type()
)
ncmcsuExcessiveError.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ncmcsuExcessiveError.setStatus("mandatory")


class _NcmcsuOutOfFrame_Type(Integer32):
    """Custom type ncmcsuOutOfFrame based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ais", 2),
          ("signal", 1))
    )


_NcmcsuOutOfFrame_Type.__name__ = "Integer32"
_NcmcsuOutOfFrame_Object = MibTableColumn
ncmcsuOutOfFrame = _NcmcsuOutOfFrame_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3025, 6002, 1, 4),
    _NcmcsuOutOfFrame_Type()
)
ncmcsuOutOfFrame.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ncmcsuOutOfFrame.setStatus("mandatory")


class _NcmcsuNetLossOfSignal_Type(Integer32):
    """Custom type ncmcsuNetLossOfSignal based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ais", 2),
          ("signal", 1))
    )


_NcmcsuNetLossOfSignal_Type.__name__ = "Integer32"
_NcmcsuNetLossOfSignal_Object = MibTableColumn
ncmcsuNetLossOfSignal = _NcmcsuNetLossOfSignal_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3025, 6002, 1, 5),
    _NcmcsuNetLossOfSignal_Type()
)
ncmcsuNetLossOfSignal.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ncmcsuNetLossOfSignal.setStatus("mandatory")
_NcmcsuElementStatusTwoTable_Object = MibTable
ncmcsuElementStatusTwoTable = _NcmcsuElementStatusTwoTable_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3025, 6003)
)
if mibBuilder.loadTexts:
    ncmcsuElementStatusTwoTable.setStatus("mandatory")
_NcmcsuElementStatusTwoEntry_Object = MibTableRow
ncmcsuElementStatusTwoEntry = _NcmcsuElementStatusTwoEntry_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3025, 6003, 1)
)
ncmcsuElementStatusTwoEntry.setIndexNames(
    (0, "VERILINK-ENTERPRISE-CSUNCM-MIB", "ncmcsuNIDElementStatusIndex2"),
    (0, "VERILINK-ENTERPRISE-CSUNCM-MIB", "ncmcsuElementStatusIndex2"),
)
if mibBuilder.loadTexts:
    ncmcsuElementStatusTwoEntry.setStatus("mandatory")
_NcmcsuNIDElementStatusIndex2_Type = Integer32
_NcmcsuNIDElementStatusIndex2_Object = MibTableColumn
ncmcsuNIDElementStatusIndex2 = _NcmcsuNIDElementStatusIndex2_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3025, 6003, 1, 1),
    _NcmcsuNIDElementStatusIndex2_Type()
)
ncmcsuNIDElementStatusIndex2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmcsuNIDElementStatusIndex2.setStatus("mandatory")
_NcmcsuElementStatusIndex2_Type = Integer32
_NcmcsuElementStatusIndex2_Object = MibTableColumn
ncmcsuElementStatusIndex2 = _NcmcsuElementStatusIndex2_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3025, 6003, 1, 2),
    _NcmcsuElementStatusIndex2_Type()
)
ncmcsuElementStatusIndex2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmcsuElementStatusIndex2.setStatus("mandatory")
_NcmcsuStatus_Type = Integer32
_NcmcsuStatus_Object = MibTableColumn
ncmcsuStatus = _NcmcsuStatus_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3025, 6003, 1, 3),
    _NcmcsuStatus_Type()
)
ncmcsuStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmcsuStatus.setStatus("mandatory")
_NcmcsuAddress1_Type = Integer32
_NcmcsuAddress1_Object = MibTableColumn
ncmcsuAddress1 = _NcmcsuAddress1_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3025, 6003, 1, 4),
    _NcmcsuAddress1_Type()
)
ncmcsuAddress1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ncmcsuAddress1.setStatus("mandatory")
_NcmcsuAddress2_Type = Integer32
_NcmcsuAddress2_Object = MibTableColumn
ncmcsuAddress2 = _NcmcsuAddress2_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3025, 6003, 1, 5),
    _NcmcsuAddress2_Type()
)
ncmcsuAddress2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ncmcsuAddress2.setStatus("mandatory")


class _NcmcsuLLBELBPLB_Type(Integer32):
    """Custom type ncmcsuLLBELBPLB based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ais", 2),
          ("signal", 1))
    )


_NcmcsuLLBELBPLB_Type.__name__ = "Integer32"
_NcmcsuLLBELBPLB_Object = MibTableColumn
ncmcsuLLBELBPLB = _NcmcsuLLBELBPLB_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3025, 6003, 1, 6),
    _NcmcsuLLBELBPLB_Type()
)
ncmcsuLLBELBPLB.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ncmcsuLLBELBPLB.setStatus("mandatory")
_NcmcsuThresholdIntervalTable_Object = MibTable
ncmcsuThresholdIntervalTable = _NcmcsuThresholdIntervalTable_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3025, 6004)
)
if mibBuilder.loadTexts:
    ncmcsuThresholdIntervalTable.setStatus("mandatory")
_NcmcsuThresholdIntervalEntry_Object = MibTableRow
ncmcsuThresholdIntervalEntry = _NcmcsuThresholdIntervalEntry_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3025, 6004, 1)
)
ncmcsuThresholdIntervalEntry.setIndexNames(
    (0, "VERILINK-ENTERPRISE-CSUNCM-MIB", "ncmcsuNIDThresholdIntervalIndex"),
    (0, "VERILINK-ENTERPRISE-CSUNCM-MIB", "ncmcsuThresholdIntervalIndex"),
)
if mibBuilder.loadTexts:
    ncmcsuThresholdIntervalEntry.setStatus("mandatory")
_NcmcsuNIDThresholdIntervalIndex_Type = Integer32
_NcmcsuNIDThresholdIntervalIndex_Object = MibTableColumn
ncmcsuNIDThresholdIntervalIndex = _NcmcsuNIDThresholdIntervalIndex_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3025, 6004, 1, 1),
    _NcmcsuNIDThresholdIntervalIndex_Type()
)
ncmcsuNIDThresholdIntervalIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmcsuNIDThresholdIntervalIndex.setStatus("mandatory")
_NcmcsuThresholdIntervalIndex_Type = Integer32
_NcmcsuThresholdIntervalIndex_Object = MibTableColumn
ncmcsuThresholdIntervalIndex = _NcmcsuThresholdIntervalIndex_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3025, 6004, 1, 2),
    _NcmcsuThresholdIntervalIndex_Type()
)
ncmcsuThresholdIntervalIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmcsuThresholdIntervalIndex.setStatus("mandatory")


class _NcmcsuBERThreshold_Type(Integer32):
    """Custom type ncmcsuBERThreshold based on Integer32"""
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
        *(("disable", 1),
          ("ten-to-Eight", 6),
          ("ten-to-Five", 3),
          ("ten-to-Four", 2),
          ("ten-to-Nine", 7),
          ("ten-to-Seven", 5),
          ("ten-to-Six", 4))
    )


_NcmcsuBERThreshold_Type.__name__ = "Integer32"
_NcmcsuBERThreshold_Object = MibTableColumn
ncmcsuBERThreshold = _NcmcsuBERThreshold_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3025, 6004, 1, 3),
    _NcmcsuBERThreshold_Type()
)
ncmcsuBERThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ncmcsuBERThreshold.setStatus("mandatory")
_NcmcsubpvSecThreshold_Type = Integer32
_NcmcsubpvSecThreshold_Object = MibTableColumn
ncmcsubpvSecThreshold = _NcmcsubpvSecThreshold_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3025, 6004, 1, 4),
    _NcmcsubpvSecThreshold_Type()
)
ncmcsubpvSecThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ncmcsubpvSecThreshold.setStatus("mandatory")
_NcmcsubpvSecInterval_Type = Integer32
_NcmcsubpvSecInterval_Object = MibTableColumn
ncmcsubpvSecInterval = _NcmcsubpvSecInterval_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3025, 6004, 1, 5),
    _NcmcsubpvSecInterval_Type()
)
ncmcsubpvSecInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ncmcsubpvSecInterval.setStatus("mandatory")
_NcmcsuESThreshold_Type = Integer32
_NcmcsuESThreshold_Object = MibTableColumn
ncmcsuESThreshold = _NcmcsuESThreshold_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3025, 6004, 1, 6),
    _NcmcsuESThreshold_Type()
)
ncmcsuESThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ncmcsuESThreshold.setStatus("mandatory")
_NcmcsuESInterval_Type = Integer32
_NcmcsuESInterval_Object = MibTableColumn
ncmcsuESInterval = _NcmcsuESInterval_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3025, 6004, 1, 7),
    _NcmcsuESInterval_Type()
)
ncmcsuESInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ncmcsuESInterval.setStatus("mandatory")
_NcmcsuUASThreshold_Type = Integer32
_NcmcsuUASThreshold_Object = MibTableColumn
ncmcsuUASThreshold = _NcmcsuUASThreshold_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3025, 6004, 1, 8),
    _NcmcsuUASThreshold_Type()
)
ncmcsuUASThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ncmcsuUASThreshold.setStatus("mandatory")
_NcmcsuUASInterval_Type = Integer32
_NcmcsuUASInterval_Object = MibTableColumn
ncmcsuUASInterval = _NcmcsuUASInterval_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3025, 6004, 1, 9),
    _NcmcsuUASInterval_Type()
)
ncmcsuUASInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ncmcsuUASInterval.setStatus("mandatory")
_NcmcsuCurrentOneTable_Object = MibTable
ncmcsuCurrentOneTable = _NcmcsuCurrentOneTable_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3025, 6005)
)
if mibBuilder.loadTexts:
    ncmcsuCurrentOneTable.setStatus("mandatory")
_NcmcsuCurrentOneEntry_Object = MibTableRow
ncmcsuCurrentOneEntry = _NcmcsuCurrentOneEntry_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3025, 6005, 1)
)
ncmcsuCurrentOneEntry.setIndexNames(
    (0, "VERILINK-ENTERPRISE-CSUNCM-MIB", "ncmcsuNIDCurrentIndex1"),
    (0, "VERILINK-ENTERPRISE-CSUNCM-MIB", "ncmcsuCurrentIndex1"),
    (0, "VERILINK-ENTERPRISE-CSUNCM-MIB", "ncmcsuCurrentEndType1"),
)
if mibBuilder.loadTexts:
    ncmcsuCurrentOneEntry.setStatus("mandatory")


class _NcmcsuNIDCurrentIndex1_Type(Integer32):
    """Custom type ncmcsuNIDCurrentIndex1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_NcmcsuNIDCurrentIndex1_Type.__name__ = "Integer32"
_NcmcsuNIDCurrentIndex1_Object = MibTableColumn
ncmcsuNIDCurrentIndex1 = _NcmcsuNIDCurrentIndex1_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3025, 6005, 1, 1),
    _NcmcsuNIDCurrentIndex1_Type()
)
ncmcsuNIDCurrentIndex1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmcsuNIDCurrentIndex1.setStatus("mandatory")


class _NcmcsuCurrentIndex1_Type(Integer32):
    """Custom type ncmcsuCurrentIndex1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_NcmcsuCurrentIndex1_Type.__name__ = "Integer32"
_NcmcsuCurrentIndex1_Object = MibTableColumn
ncmcsuCurrentIndex1 = _NcmcsuCurrentIndex1_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3025, 6005, 1, 2),
    _NcmcsuCurrentIndex1_Type()
)
ncmcsuCurrentIndex1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmcsuCurrentIndex1.setStatus("mandatory")


class _NcmcsuCurrentEndType1_Type(Integer32):
    """Custom type ncmcsuCurrentEndType1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("far-End", 2),
          ("near-End", 1))
    )


_NcmcsuCurrentEndType1_Type.__name__ = "Integer32"
_NcmcsuCurrentEndType1_Object = MibTableColumn
ncmcsuCurrentEndType1 = _NcmcsuCurrentEndType1_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3025, 6005, 1, 3),
    _NcmcsuCurrentEndType1_Type()
)
ncmcsuCurrentEndType1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmcsuCurrentEndType1.setStatus("mandatory")
_NcmcsuCurrentESs_Type = Gauge32
_NcmcsuCurrentESs_Object = MibTableColumn
ncmcsuCurrentESs = _NcmcsuCurrentESs_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3025, 6005, 1, 4),
    _NcmcsuCurrentESs_Type()
)
ncmcsuCurrentESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmcsuCurrentESs.setStatus("mandatory")
_NcmcsuCurrentSESs_Type = Gauge32
_NcmcsuCurrentSESs_Object = MibTableColumn
ncmcsuCurrentSESs = _NcmcsuCurrentSESs_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3025, 6005, 1, 5),
    _NcmcsuCurrentSESs_Type()
)
ncmcsuCurrentSESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmcsuCurrentSESs.setStatus("mandatory")
_NcmcsuCurrentSEFSs_Type = Gauge32
_NcmcsuCurrentSEFSs_Object = MibTableColumn
ncmcsuCurrentSEFSs = _NcmcsuCurrentSEFSs_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3025, 6005, 1, 6),
    _NcmcsuCurrentSEFSs_Type()
)
ncmcsuCurrentSEFSs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmcsuCurrentSEFSs.setStatus("mandatory")
_NcmcsuCurrentUASs_Type = Gauge32
_NcmcsuCurrentUASs_Object = MibTableColumn
ncmcsuCurrentUASs = _NcmcsuCurrentUASs_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3025, 6005, 1, 7),
    _NcmcsuCurrentUASs_Type()
)
ncmcsuCurrentUASs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmcsuCurrentUASs.setStatus("mandatory")
_NcmcsuCurrentCSSs_Type = Gauge32
_NcmcsuCurrentCSSs_Object = MibTableColumn
ncmcsuCurrentCSSs = _NcmcsuCurrentCSSs_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3025, 6005, 1, 8),
    _NcmcsuCurrentCSSs_Type()
)
ncmcsuCurrentCSSs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmcsuCurrentCSSs.setStatus("mandatory")
_NcmcsuCurrentPCVs_Type = Gauge32
_NcmcsuCurrentPCVs_Object = MibTableColumn
ncmcsuCurrentPCVs = _NcmcsuCurrentPCVs_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3025, 6005, 1, 9),
    _NcmcsuCurrentPCVs_Type()
)
ncmcsuCurrentPCVs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmcsuCurrentPCVs.setStatus("mandatory")
_NcmcsuCurrentLESs_Type = Gauge32
_NcmcsuCurrentLESs_Object = MibTableColumn
ncmcsuCurrentLESs = _NcmcsuCurrentLESs_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3025, 6005, 1, 10),
    _NcmcsuCurrentLESs_Type()
)
ncmcsuCurrentLESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmcsuCurrentLESs.setStatus("mandatory")
_NcmcsuCurrentBESs_Type = Gauge32
_NcmcsuCurrentBESs_Object = MibTableColumn
ncmcsuCurrentBESs = _NcmcsuCurrentBESs_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3025, 6005, 1, 11),
    _NcmcsuCurrentBESs_Type()
)
ncmcsuCurrentBESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmcsuCurrentBESs.setStatus("mandatory")
_NcmcsuCurrentDMs_Type = Gauge32
_NcmcsuCurrentDMs_Object = MibTableColumn
ncmcsuCurrentDMs = _NcmcsuCurrentDMs_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3025, 6005, 1, 12),
    _NcmcsuCurrentDMs_Type()
)
ncmcsuCurrentDMs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmcsuCurrentDMs.setStatus("mandatory")
_NcmcsuCurrentLCVs_Type = Gauge32
_NcmcsuCurrentLCVs_Object = MibTableColumn
ncmcsuCurrentLCVs = _NcmcsuCurrentLCVs_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3025, 6005, 1, 13),
    _NcmcsuCurrentLCVs_Type()
)
ncmcsuCurrentLCVs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmcsuCurrentLCVs.setStatus("mandatory")
_NcmcsuIntervalOneTable_Object = MibTable
ncmcsuIntervalOneTable = _NcmcsuIntervalOneTable_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3025, 6006)
)
if mibBuilder.loadTexts:
    ncmcsuIntervalOneTable.setStatus("mandatory")
_NcmcsuIntervalOneEntry_Object = MibTableRow
ncmcsuIntervalOneEntry = _NcmcsuIntervalOneEntry_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3025, 6006, 1)
)
ncmcsuIntervalOneEntry.setIndexNames(
    (0, "VERILINK-ENTERPRISE-CSUNCM-MIB", "ncmcsuNIDIntervalIndex1"),
    (0, "VERILINK-ENTERPRISE-CSUNCM-MIB", "ncmcsuIntervalIndex1"),
    (0, "VERILINK-ENTERPRISE-CSUNCM-MIB", "ncmcsuIntervalEndType1"),
    (0, "VERILINK-ENTERPRISE-CSUNCM-MIB", "ncmcsuIntervalNumber1"),
)
if mibBuilder.loadTexts:
    ncmcsuIntervalOneEntry.setStatus("mandatory")


class _NcmcsuNIDIntervalIndex1_Type(Integer32):
    """Custom type ncmcsuNIDIntervalIndex1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_NcmcsuNIDIntervalIndex1_Type.__name__ = "Integer32"
_NcmcsuNIDIntervalIndex1_Object = MibTableColumn
ncmcsuNIDIntervalIndex1 = _NcmcsuNIDIntervalIndex1_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3025, 6006, 1, 1),
    _NcmcsuNIDIntervalIndex1_Type()
)
ncmcsuNIDIntervalIndex1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmcsuNIDIntervalIndex1.setStatus("mandatory")


class _NcmcsuIntervalIndex1_Type(Integer32):
    """Custom type ncmcsuIntervalIndex1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_NcmcsuIntervalIndex1_Type.__name__ = "Integer32"
_NcmcsuIntervalIndex1_Object = MibTableColumn
ncmcsuIntervalIndex1 = _NcmcsuIntervalIndex1_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3025, 6006, 1, 2),
    _NcmcsuIntervalIndex1_Type()
)
ncmcsuIntervalIndex1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmcsuIntervalIndex1.setStatus("mandatory")


class _NcmcsuIntervalEndType1_Type(Integer32):
    """Custom type ncmcsuIntervalEndType1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("far-End", 2),
          ("near-End", 1))
    )


_NcmcsuIntervalEndType1_Type.__name__ = "Integer32"
_NcmcsuIntervalEndType1_Object = MibTableColumn
ncmcsuIntervalEndType1 = _NcmcsuIntervalEndType1_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3025, 6006, 1, 3),
    _NcmcsuIntervalEndType1_Type()
)
ncmcsuIntervalEndType1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmcsuIntervalEndType1.setStatus("mandatory")


class _NcmcsuIntervalNumber1_Type(Integer32):
    """Custom type ncmcsuIntervalNumber1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 96),
    )


_NcmcsuIntervalNumber1_Type.__name__ = "Integer32"
_NcmcsuIntervalNumber1_Object = MibTableColumn
ncmcsuIntervalNumber1 = _NcmcsuIntervalNumber1_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3025, 6006, 1, 4),
    _NcmcsuIntervalNumber1_Type()
)
ncmcsuIntervalNumber1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmcsuIntervalNumber1.setStatus("mandatory")
_NcmcsuIntervalESs_Type = Gauge32
_NcmcsuIntervalESs_Object = MibTableColumn
ncmcsuIntervalESs = _NcmcsuIntervalESs_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3025, 6006, 1, 5),
    _NcmcsuIntervalESs_Type()
)
ncmcsuIntervalESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmcsuIntervalESs.setStatus("mandatory")
_NcmcsuIntervalSESs_Type = Gauge32
_NcmcsuIntervalSESs_Object = MibTableColumn
ncmcsuIntervalSESs = _NcmcsuIntervalSESs_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3025, 6006, 1, 6),
    _NcmcsuIntervalSESs_Type()
)
ncmcsuIntervalSESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmcsuIntervalSESs.setStatus("mandatory")
_NcmcsuIntervalSEFSs_Type = Gauge32
_NcmcsuIntervalSEFSs_Object = MibTableColumn
ncmcsuIntervalSEFSs = _NcmcsuIntervalSEFSs_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3025, 6006, 1, 7),
    _NcmcsuIntervalSEFSs_Type()
)
ncmcsuIntervalSEFSs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmcsuIntervalSEFSs.setStatus("mandatory")
_NcmcsuIntervalUASs_Type = Gauge32
_NcmcsuIntervalUASs_Object = MibTableColumn
ncmcsuIntervalUASs = _NcmcsuIntervalUASs_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3025, 6006, 1, 8),
    _NcmcsuIntervalUASs_Type()
)
ncmcsuIntervalUASs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmcsuIntervalUASs.setStatus("mandatory")
_NcmcsuIntervalCSSs_Type = Gauge32
_NcmcsuIntervalCSSs_Object = MibTableColumn
ncmcsuIntervalCSSs = _NcmcsuIntervalCSSs_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3025, 6006, 1, 9),
    _NcmcsuIntervalCSSs_Type()
)
ncmcsuIntervalCSSs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmcsuIntervalCSSs.setStatus("mandatory")
_NcmcsuIntervalPCVs_Type = Gauge32
_NcmcsuIntervalPCVs_Object = MibTableColumn
ncmcsuIntervalPCVs = _NcmcsuIntervalPCVs_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3025, 6006, 1, 10),
    _NcmcsuIntervalPCVs_Type()
)
ncmcsuIntervalPCVs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmcsuIntervalPCVs.setStatus("mandatory")
_NcmcsuIntervalLESs_Type = Gauge32
_NcmcsuIntervalLESs_Object = MibTableColumn
ncmcsuIntervalLESs = _NcmcsuIntervalLESs_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3025, 6006, 1, 11),
    _NcmcsuIntervalLESs_Type()
)
ncmcsuIntervalLESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmcsuIntervalLESs.setStatus("mandatory")
_NcmcsuIntervalBESs_Type = Gauge32
_NcmcsuIntervalBESs_Object = MibTableColumn
ncmcsuIntervalBESs = _NcmcsuIntervalBESs_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3025, 6006, 1, 12),
    _NcmcsuIntervalBESs_Type()
)
ncmcsuIntervalBESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmcsuIntervalBESs.setStatus("mandatory")
_NcmcsuIntervalDMs_Type = Gauge32
_NcmcsuIntervalDMs_Object = MibTableColumn
ncmcsuIntervalDMs = _NcmcsuIntervalDMs_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3025, 6006, 1, 13),
    _NcmcsuIntervalDMs_Type()
)
ncmcsuIntervalDMs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmcsuIntervalDMs.setStatus("mandatory")
_NcmcsuIntervalLCVs_Type = Gauge32
_NcmcsuIntervalLCVs_Object = MibTableColumn
ncmcsuIntervalLCVs = _NcmcsuIntervalLCVs_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3025, 6006, 1, 14),
    _NcmcsuIntervalLCVs_Type()
)
ncmcsuIntervalLCVs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmcsuIntervalLCVs.setStatus("mandatory")
_NcmcsuTotalOneTable_Object = MibTable
ncmcsuTotalOneTable = _NcmcsuTotalOneTable_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3025, 6007)
)
if mibBuilder.loadTexts:
    ncmcsuTotalOneTable.setStatus("mandatory")
_NcmcsuTotalOneEntry_Object = MibTableRow
ncmcsuTotalOneEntry = _NcmcsuTotalOneEntry_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3025, 6007, 1)
)
ncmcsuTotalOneEntry.setIndexNames(
    (0, "VERILINK-ENTERPRISE-CSUNCM-MIB", "ncmcsuNIDTotalIndex1"),
    (0, "VERILINK-ENTERPRISE-CSUNCM-MIB", "ncmcsuTotalIndex1"),
    (0, "VERILINK-ENTERPRISE-CSUNCM-MIB", "ncmcsuTotalEndType1"),
)
if mibBuilder.loadTexts:
    ncmcsuTotalOneEntry.setStatus("mandatory")


class _NcmcsuNIDTotalIndex1_Type(Integer32):
    """Custom type ncmcsuNIDTotalIndex1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_NcmcsuNIDTotalIndex1_Type.__name__ = "Integer32"
_NcmcsuNIDTotalIndex1_Object = MibTableColumn
ncmcsuNIDTotalIndex1 = _NcmcsuNIDTotalIndex1_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3025, 6007, 1, 1),
    _NcmcsuNIDTotalIndex1_Type()
)
ncmcsuNIDTotalIndex1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmcsuNIDTotalIndex1.setStatus("mandatory")


class _NcmcsuTotalIndex1_Type(Integer32):
    """Custom type ncmcsuTotalIndex1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_NcmcsuTotalIndex1_Type.__name__ = "Integer32"
_NcmcsuTotalIndex1_Object = MibTableColumn
ncmcsuTotalIndex1 = _NcmcsuTotalIndex1_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3025, 6007, 1, 2),
    _NcmcsuTotalIndex1_Type()
)
ncmcsuTotalIndex1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmcsuTotalIndex1.setStatus("mandatory")


class _NcmcsuTotalEndType1_Type(Integer32):
    """Custom type ncmcsuTotalEndType1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("far-End", 2),
          ("near-End", 1))
    )


_NcmcsuTotalEndType1_Type.__name__ = "Integer32"
_NcmcsuTotalEndType1_Object = MibTableColumn
ncmcsuTotalEndType1 = _NcmcsuTotalEndType1_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3025, 6007, 1, 3),
    _NcmcsuTotalEndType1_Type()
)
ncmcsuTotalEndType1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmcsuTotalEndType1.setStatus("mandatory")
_NcmcsuTotalESs_Type = Gauge32
_NcmcsuTotalESs_Object = MibTableColumn
ncmcsuTotalESs = _NcmcsuTotalESs_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3025, 6007, 1, 4),
    _NcmcsuTotalESs_Type()
)
ncmcsuTotalESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmcsuTotalESs.setStatus("mandatory")
_NcmcsuTotalSESs_Type = Gauge32
_NcmcsuTotalSESs_Object = MibTableColumn
ncmcsuTotalSESs = _NcmcsuTotalSESs_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3025, 6007, 1, 5),
    _NcmcsuTotalSESs_Type()
)
ncmcsuTotalSESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmcsuTotalSESs.setStatus("mandatory")
_NcmcsuTotalSEFSs_Type = Gauge32
_NcmcsuTotalSEFSs_Object = MibTableColumn
ncmcsuTotalSEFSs = _NcmcsuTotalSEFSs_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3025, 6007, 1, 6),
    _NcmcsuTotalSEFSs_Type()
)
ncmcsuTotalSEFSs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmcsuTotalSEFSs.setStatus("mandatory")
_NcmcsuTotalUASs_Type = Gauge32
_NcmcsuTotalUASs_Object = MibTableColumn
ncmcsuTotalUASs = _NcmcsuTotalUASs_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3025, 6007, 1, 7),
    _NcmcsuTotalUASs_Type()
)
ncmcsuTotalUASs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmcsuTotalUASs.setStatus("mandatory")
_NcmcsuTotalCSSs_Type = Gauge32
_NcmcsuTotalCSSs_Object = MibTableColumn
ncmcsuTotalCSSs = _NcmcsuTotalCSSs_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3025, 6007, 1, 8),
    _NcmcsuTotalCSSs_Type()
)
ncmcsuTotalCSSs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmcsuTotalCSSs.setStatus("mandatory")
_NcmcsuTotalPCVs_Type = Gauge32
_NcmcsuTotalPCVs_Object = MibTableColumn
ncmcsuTotalPCVs = _NcmcsuTotalPCVs_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3025, 6007, 1, 9),
    _NcmcsuTotalPCVs_Type()
)
ncmcsuTotalPCVs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmcsuTotalPCVs.setStatus("mandatory")
_NcmcsuTotalLESs_Type = Gauge32
_NcmcsuTotalLESs_Object = MibTableColumn
ncmcsuTotalLESs = _NcmcsuTotalLESs_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3025, 6007, 1, 10),
    _NcmcsuTotalLESs_Type()
)
ncmcsuTotalLESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmcsuTotalLESs.setStatus("mandatory")
_NcmcsuTotalBESs_Type = Gauge32
_NcmcsuTotalBESs_Object = MibTableColumn
ncmcsuTotalBESs = _NcmcsuTotalBESs_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3025, 6007, 1, 11),
    _NcmcsuTotalBESs_Type()
)
ncmcsuTotalBESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmcsuTotalBESs.setStatus("mandatory")
_NcmcsuTotalDMs_Type = Gauge32
_NcmcsuTotalDMs_Object = MibTableColumn
ncmcsuTotalDMs = _NcmcsuTotalDMs_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3025, 6007, 1, 12),
    _NcmcsuTotalDMs_Type()
)
ncmcsuTotalDMs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmcsuTotalDMs.setStatus("mandatory")
_NcmcsuTotalLCVs_Type = Gauge32
_NcmcsuTotalLCVs_Object = MibTableColumn
ncmcsuTotalLCVs = _NcmcsuTotalLCVs_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3025, 6007, 1, 13),
    _NcmcsuTotalLCVs_Type()
)
ncmcsuTotalLCVs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmcsuTotalLCVs.setStatus("mandatory")
_NcmcsuEnhancedCurrentTable_Object = MibTable
ncmcsuEnhancedCurrentTable = _NcmcsuEnhancedCurrentTable_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3025, 6008)
)
if mibBuilder.loadTexts:
    ncmcsuEnhancedCurrentTable.setStatus("mandatory")
_NcmcsuEnhancedCurrentEntry_Object = MibTableRow
ncmcsuEnhancedCurrentEntry = _NcmcsuEnhancedCurrentEntry_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3025, 6008, 1)
)
ncmcsuEnhancedCurrentEntry.setIndexNames(
    (0, "VERILINK-ENTERPRISE-CSUNCM-MIB", "ncmcsuNIDEnhancedCurrentIndex"),
    (0, "VERILINK-ENTERPRISE-CSUNCM-MIB", "ncmcsuEnhancedCurrentIndex"),
    (0, "VERILINK-ENTERPRISE-CSUNCM-MIB", "ncmcsuEnhancedCurrentEndType"),
)
if mibBuilder.loadTexts:
    ncmcsuEnhancedCurrentEntry.setStatus("mandatory")


class _NcmcsuNIDEnhancedCurrentIndex_Type(Integer32):
    """Custom type ncmcsuNIDEnhancedCurrentIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_NcmcsuNIDEnhancedCurrentIndex_Type.__name__ = "Integer32"
_NcmcsuNIDEnhancedCurrentIndex_Object = MibTableColumn
ncmcsuNIDEnhancedCurrentIndex = _NcmcsuNIDEnhancedCurrentIndex_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3025, 6008, 1, 1),
    _NcmcsuNIDEnhancedCurrentIndex_Type()
)
ncmcsuNIDEnhancedCurrentIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmcsuNIDEnhancedCurrentIndex.setStatus("mandatory")


class _NcmcsuEnhancedCurrentIndex_Type(Integer32):
    """Custom type ncmcsuEnhancedCurrentIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_NcmcsuEnhancedCurrentIndex_Type.__name__ = "Integer32"
_NcmcsuEnhancedCurrentIndex_Object = MibTableColumn
ncmcsuEnhancedCurrentIndex = _NcmcsuEnhancedCurrentIndex_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3025, 6008, 1, 2),
    _NcmcsuEnhancedCurrentIndex_Type()
)
ncmcsuEnhancedCurrentIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmcsuEnhancedCurrentIndex.setStatus("mandatory")


class _NcmcsuEnhancedCurrentEndType_Type(Integer32):
    """Custom type ncmcsuEnhancedCurrentEndType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("far-End", 2),
          ("near-End", 1))
    )


_NcmcsuEnhancedCurrentEndType_Type.__name__ = "Integer32"
_NcmcsuEnhancedCurrentEndType_Object = MibTableColumn
ncmcsuEnhancedCurrentEndType = _NcmcsuEnhancedCurrentEndType_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3025, 6008, 1, 3),
    _NcmcsuEnhancedCurrentEndType_Type()
)
ncmcsuEnhancedCurrentEndType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmcsuEnhancedCurrentEndType.setStatus("mandatory")
_NcmcsuEnhancedCurrentESs_Type = Gauge32
_NcmcsuEnhancedCurrentESs_Object = MibTableColumn
ncmcsuEnhancedCurrentESs = _NcmcsuEnhancedCurrentESs_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3025, 6008, 1, 4),
    _NcmcsuEnhancedCurrentESs_Type()
)
ncmcsuEnhancedCurrentESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmcsuEnhancedCurrentESs.setStatus("mandatory")
_NcmcsuEnhancedCurrentSESs_Type = Gauge32
_NcmcsuEnhancedCurrentSESs_Object = MibTableColumn
ncmcsuEnhancedCurrentSESs = _NcmcsuEnhancedCurrentSESs_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3025, 6008, 1, 5),
    _NcmcsuEnhancedCurrentSESs_Type()
)
ncmcsuEnhancedCurrentSESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmcsuEnhancedCurrentSESs.setStatus("mandatory")
_NcmcsuEnhancedCurrentUASs_Type = Gauge32
_NcmcsuEnhancedCurrentUASs_Object = MibTableColumn
ncmcsuEnhancedCurrentUASs = _NcmcsuEnhancedCurrentUASs_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3025, 6008, 1, 6),
    _NcmcsuEnhancedCurrentUASs_Type()
)
ncmcsuEnhancedCurrentUASs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmcsuEnhancedCurrentUASs.setStatus("mandatory")
_NcmcsuEnhancedCurrentCSSs_Type = Gauge32
_NcmcsuEnhancedCurrentCSSs_Object = MibTableColumn
ncmcsuEnhancedCurrentCSSs = _NcmcsuEnhancedCurrentCSSs_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3025, 6008, 1, 7),
    _NcmcsuEnhancedCurrentCSSs_Type()
)
ncmcsuEnhancedCurrentCSSs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmcsuEnhancedCurrentCSSs.setStatus("mandatory")
_NcmcsuEnhancedCurrentBESs_Type = Gauge32
_NcmcsuEnhancedCurrentBESs_Object = MibTableColumn
ncmcsuEnhancedCurrentBESs = _NcmcsuEnhancedCurrentBESs_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3025, 6008, 1, 8),
    _NcmcsuEnhancedCurrentBESs_Type()
)
ncmcsuEnhancedCurrentBESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmcsuEnhancedCurrentBESs.setStatus("mandatory")
_NcmcsuEnhancedCurrentLOFC_Type = Gauge32
_NcmcsuEnhancedCurrentLOFC_Object = MibTableColumn
ncmcsuEnhancedCurrentLOFC = _NcmcsuEnhancedCurrentLOFC_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3025, 6008, 1, 9),
    _NcmcsuEnhancedCurrentLOFC_Type()
)
ncmcsuEnhancedCurrentLOFC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmcsuEnhancedCurrentLOFC.setStatus("mandatory")
_NcmcsuEnhancedIntervalTable_Object = MibTable
ncmcsuEnhancedIntervalTable = _NcmcsuEnhancedIntervalTable_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3025, 6009)
)
if mibBuilder.loadTexts:
    ncmcsuEnhancedIntervalTable.setStatus("mandatory")
_NcmcsuEnhancedIntervalEntry_Object = MibTableRow
ncmcsuEnhancedIntervalEntry = _NcmcsuEnhancedIntervalEntry_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3025, 6009, 1)
)
ncmcsuEnhancedIntervalEntry.setIndexNames(
    (0, "VERILINK-ENTERPRISE-CSUNCM-MIB", "ncmcsuNIDEnhancedIntervalIndex"),
    (0, "VERILINK-ENTERPRISE-CSUNCM-MIB", "ncmcsuEnhancedIntervalIndex"),
    (0, "VERILINK-ENTERPRISE-CSUNCM-MIB", "ncmcsuEnhancedIntervalEndType"),
    (0, "VERILINK-ENTERPRISE-CSUNCM-MIB", "ncmcsuEnhancedIntervalNumber"),
)
if mibBuilder.loadTexts:
    ncmcsuEnhancedIntervalEntry.setStatus("mandatory")


class _NcmcsuNIDEnhancedIntervalIndex_Type(Integer32):
    """Custom type ncmcsuNIDEnhancedIntervalIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_NcmcsuNIDEnhancedIntervalIndex_Type.__name__ = "Integer32"
_NcmcsuNIDEnhancedIntervalIndex_Object = MibTableColumn
ncmcsuNIDEnhancedIntervalIndex = _NcmcsuNIDEnhancedIntervalIndex_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3025, 6009, 1, 1),
    _NcmcsuNIDEnhancedIntervalIndex_Type()
)
ncmcsuNIDEnhancedIntervalIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmcsuNIDEnhancedIntervalIndex.setStatus("mandatory")


class _NcmcsuEnhancedIntervalIndex_Type(Integer32):
    """Custom type ncmcsuEnhancedIntervalIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_NcmcsuEnhancedIntervalIndex_Type.__name__ = "Integer32"
_NcmcsuEnhancedIntervalIndex_Object = MibTableColumn
ncmcsuEnhancedIntervalIndex = _NcmcsuEnhancedIntervalIndex_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3025, 6009, 1, 2),
    _NcmcsuEnhancedIntervalIndex_Type()
)
ncmcsuEnhancedIntervalIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmcsuEnhancedIntervalIndex.setStatus("mandatory")


class _NcmcsuEnhancedIntervalEndType_Type(Integer32):
    """Custom type ncmcsuEnhancedIntervalEndType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("far-End", 2),
          ("near-End", 1))
    )


_NcmcsuEnhancedIntervalEndType_Type.__name__ = "Integer32"
_NcmcsuEnhancedIntervalEndType_Object = MibTableColumn
ncmcsuEnhancedIntervalEndType = _NcmcsuEnhancedIntervalEndType_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3025, 6009, 1, 3),
    _NcmcsuEnhancedIntervalEndType_Type()
)
ncmcsuEnhancedIntervalEndType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmcsuEnhancedIntervalEndType.setStatus("mandatory")


class _NcmcsuEnhancedIntervalNumber_Type(Integer32):
    """Custom type ncmcsuEnhancedIntervalNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 96),
    )


_NcmcsuEnhancedIntervalNumber_Type.__name__ = "Integer32"
_NcmcsuEnhancedIntervalNumber_Object = MibTableColumn
ncmcsuEnhancedIntervalNumber = _NcmcsuEnhancedIntervalNumber_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3025, 6009, 1, 4),
    _NcmcsuEnhancedIntervalNumber_Type()
)
ncmcsuEnhancedIntervalNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmcsuEnhancedIntervalNumber.setStatus("mandatory")
_NcmcsuEnhancedIntervalESs_Type = Gauge32
_NcmcsuEnhancedIntervalESs_Object = MibTableColumn
ncmcsuEnhancedIntervalESs = _NcmcsuEnhancedIntervalESs_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3025, 6009, 1, 5),
    _NcmcsuEnhancedIntervalESs_Type()
)
ncmcsuEnhancedIntervalESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmcsuEnhancedIntervalESs.setStatus("mandatory")
_NcmcsuEnhancedIntervalSESs_Type = Gauge32
_NcmcsuEnhancedIntervalSESs_Object = MibTableColumn
ncmcsuEnhancedIntervalSESs = _NcmcsuEnhancedIntervalSESs_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3025, 6009, 1, 6),
    _NcmcsuEnhancedIntervalSESs_Type()
)
ncmcsuEnhancedIntervalSESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmcsuEnhancedIntervalSESs.setStatus("mandatory")
_NcmcsuEnhancedIntervalUASs_Type = Gauge32
_NcmcsuEnhancedIntervalUASs_Object = MibTableColumn
ncmcsuEnhancedIntervalUASs = _NcmcsuEnhancedIntervalUASs_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3025, 6009, 1, 7),
    _NcmcsuEnhancedIntervalUASs_Type()
)
ncmcsuEnhancedIntervalUASs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmcsuEnhancedIntervalUASs.setStatus("mandatory")
_NcmcsuEnhancedIntervalCSSs_Type = Gauge32
_NcmcsuEnhancedIntervalCSSs_Object = MibTableColumn
ncmcsuEnhancedIntervalCSSs = _NcmcsuEnhancedIntervalCSSs_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3025, 6009, 1, 8),
    _NcmcsuEnhancedIntervalCSSs_Type()
)
ncmcsuEnhancedIntervalCSSs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmcsuEnhancedIntervalCSSs.setStatus("mandatory")
_NcmcsuEnhancedIntervalBESs_Type = Gauge32
_NcmcsuEnhancedIntervalBESs_Object = MibTableColumn
ncmcsuEnhancedIntervalBESs = _NcmcsuEnhancedIntervalBESs_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3025, 6009, 1, 9),
    _NcmcsuEnhancedIntervalBESs_Type()
)
ncmcsuEnhancedIntervalBESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmcsuEnhancedIntervalBESs.setStatus("mandatory")
_NcmcsuEnhancedIntervalLOFC_Type = Gauge32
_NcmcsuEnhancedIntervalLOFC_Object = MibTableColumn
ncmcsuEnhancedIntervalLOFC = _NcmcsuEnhancedIntervalLOFC_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3025, 6009, 1, 10),
    _NcmcsuEnhancedIntervalLOFC_Type()
)
ncmcsuEnhancedIntervalLOFC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmcsuEnhancedIntervalLOFC.setStatus("mandatory")
_NcmcsuEnhancedTotalTable_Object = MibTable
ncmcsuEnhancedTotalTable = _NcmcsuEnhancedTotalTable_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3025, 6010)
)
if mibBuilder.loadTexts:
    ncmcsuEnhancedTotalTable.setStatus("mandatory")
_NcmcsuEnhancedTotalEntry_Object = MibTableRow
ncmcsuEnhancedTotalEntry = _NcmcsuEnhancedTotalEntry_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3025, 6010, 1)
)
ncmcsuEnhancedTotalEntry.setIndexNames(
    (0, "VERILINK-ENTERPRISE-CSUNCM-MIB", "ncmcsuNIDEnhancedTotalIndex"),
    (0, "VERILINK-ENTERPRISE-CSUNCM-MIB", "ncmcsuEnhancedTotalIndex"),
    (0, "VERILINK-ENTERPRISE-CSUNCM-MIB", "ncmcsuEnhancedTotalEndType"),
)
if mibBuilder.loadTexts:
    ncmcsuEnhancedTotalEntry.setStatus("mandatory")


class _NcmcsuNIDEnhancedTotalIndex_Type(Integer32):
    """Custom type ncmcsuNIDEnhancedTotalIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_NcmcsuNIDEnhancedTotalIndex_Type.__name__ = "Integer32"
_NcmcsuNIDEnhancedTotalIndex_Object = MibTableColumn
ncmcsuNIDEnhancedTotalIndex = _NcmcsuNIDEnhancedTotalIndex_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3025, 6010, 1, 1),
    _NcmcsuNIDEnhancedTotalIndex_Type()
)
ncmcsuNIDEnhancedTotalIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmcsuNIDEnhancedTotalIndex.setStatus("mandatory")


class _NcmcsuEnhancedTotalIndex_Type(Integer32):
    """Custom type ncmcsuEnhancedTotalIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_NcmcsuEnhancedTotalIndex_Type.__name__ = "Integer32"
_NcmcsuEnhancedTotalIndex_Object = MibTableColumn
ncmcsuEnhancedTotalIndex = _NcmcsuEnhancedTotalIndex_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3025, 6010, 1, 2),
    _NcmcsuEnhancedTotalIndex_Type()
)
ncmcsuEnhancedTotalIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmcsuEnhancedTotalIndex.setStatus("mandatory")


class _NcmcsuEnhancedTotalEndType_Type(Integer32):
    """Custom type ncmcsuEnhancedTotalEndType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("far-End", 2),
          ("near-End", 1))
    )


_NcmcsuEnhancedTotalEndType_Type.__name__ = "Integer32"
_NcmcsuEnhancedTotalEndType_Object = MibTableColumn
ncmcsuEnhancedTotalEndType = _NcmcsuEnhancedTotalEndType_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3025, 6010, 1, 3),
    _NcmcsuEnhancedTotalEndType_Type()
)
ncmcsuEnhancedTotalEndType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmcsuEnhancedTotalEndType.setStatus("mandatory")
_NcmcsuEnhancedTotalESs_Type = Gauge32
_NcmcsuEnhancedTotalESs_Object = MibTableColumn
ncmcsuEnhancedTotalESs = _NcmcsuEnhancedTotalESs_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3025, 6010, 1, 4),
    _NcmcsuEnhancedTotalESs_Type()
)
ncmcsuEnhancedTotalESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmcsuEnhancedTotalESs.setStatus("mandatory")
_NcmcsuEnhancedTotalSESs_Type = Gauge32
_NcmcsuEnhancedTotalSESs_Object = MibTableColumn
ncmcsuEnhancedTotalSESs = _NcmcsuEnhancedTotalSESs_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3025, 6010, 1, 5),
    _NcmcsuEnhancedTotalSESs_Type()
)
ncmcsuEnhancedTotalSESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmcsuEnhancedTotalSESs.setStatus("mandatory")
_NcmcsuEnhancedTotalUASs_Type = Gauge32
_NcmcsuEnhancedTotalUASs_Object = MibTableColumn
ncmcsuEnhancedTotalUASs = _NcmcsuEnhancedTotalUASs_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3025, 6010, 1, 6),
    _NcmcsuEnhancedTotalUASs_Type()
)
ncmcsuEnhancedTotalUASs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmcsuEnhancedTotalUASs.setStatus("mandatory")
_NcmcsuEnhancedTotalCSSs_Type = Gauge32
_NcmcsuEnhancedTotalCSSs_Object = MibTableColumn
ncmcsuEnhancedTotalCSSs = _NcmcsuEnhancedTotalCSSs_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3025, 6010, 1, 7),
    _NcmcsuEnhancedTotalCSSs_Type()
)
ncmcsuEnhancedTotalCSSs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmcsuEnhancedTotalCSSs.setStatus("mandatory")
_NcmcsuEnhancedTotalBESs_Type = Gauge32
_NcmcsuEnhancedTotalBESs_Object = MibTableColumn
ncmcsuEnhancedTotalBESs = _NcmcsuEnhancedTotalBESs_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3025, 6010, 1, 8),
    _NcmcsuEnhancedTotalBESs_Type()
)
ncmcsuEnhancedTotalBESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmcsuEnhancedTotalBESs.setStatus("mandatory")
_NcmcsuEnhancedTotalLOFC_Type = Gauge32
_NcmcsuEnhancedTotalLOFC_Object = MibTableColumn
ncmcsuEnhancedTotalLOFC = _NcmcsuEnhancedTotalLOFC_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3025, 6010, 1, 9),
    _NcmcsuEnhancedTotalLOFC_Type()
)
ncmcsuEnhancedTotalLOFC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmcsuEnhancedTotalLOFC.setStatus("mandatory")
_NcmcsuCurrentTable_Object = MibTable
ncmcsuCurrentTable = _NcmcsuCurrentTable_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3025, 6011)
)
if mibBuilder.loadTexts:
    ncmcsuCurrentTable.setStatus("mandatory")
_NcmcsuCurrentEntry_Object = MibTableRow
ncmcsuCurrentEntry = _NcmcsuCurrentEntry_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3025, 6011, 1)
)
ncmcsuCurrentEntry.setIndexNames(
    (0, "VERILINK-ENTERPRISE-CSUNCM-MIB", "ncmcsuNIDCurrentIndex"),
    (0, "VERILINK-ENTERPRISE-CSUNCM-MIB", "ncmcsuCurrentIndex"),
    (0, "VERILINK-ENTERPRISE-CSUNCM-MIB", "ncmcsuCurrentEndType"),
)
if mibBuilder.loadTexts:
    ncmcsuCurrentEntry.setStatus("mandatory")


class _NcmcsuNIDCurrentIndex_Type(Integer32):
    """Custom type ncmcsuNIDCurrentIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_NcmcsuNIDCurrentIndex_Type.__name__ = "Integer32"
_NcmcsuNIDCurrentIndex_Object = MibTableColumn
ncmcsuNIDCurrentIndex = _NcmcsuNIDCurrentIndex_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3025, 6011, 1, 1),
    _NcmcsuNIDCurrentIndex_Type()
)
ncmcsuNIDCurrentIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmcsuNIDCurrentIndex.setStatus("mandatory")


class _NcmcsuCurrentIndex_Type(Integer32):
    """Custom type ncmcsuCurrentIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_NcmcsuCurrentIndex_Type.__name__ = "Integer32"
_NcmcsuCurrentIndex_Object = MibTableColumn
ncmcsuCurrentIndex = _NcmcsuCurrentIndex_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3025, 6011, 1, 2),
    _NcmcsuCurrentIndex_Type()
)
ncmcsuCurrentIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmcsuCurrentIndex.setStatus("mandatory")


class _NcmcsuCurrentEndType_Type(Integer32):
    """Custom type ncmcsuCurrentEndType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("far-End", 2),
          ("near-End", 1))
    )


_NcmcsuCurrentEndType_Type.__name__ = "Integer32"
_NcmcsuCurrentEndType_Object = MibTableColumn
ncmcsuCurrentEndType = _NcmcsuCurrentEndType_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3025, 6011, 1, 3),
    _NcmcsuCurrentEndType_Type()
)
ncmcsuCurrentEndType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmcsuCurrentEndType.setStatus("mandatory")
_NcmcsuCurrentNETOOFS_Type = Gauge32
_NcmcsuCurrentNETOOFS_Object = MibTableColumn
ncmcsuCurrentNETOOFS = _NcmcsuCurrentNETOOFS_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3025, 6011, 1, 4),
    _NcmcsuCurrentNETOOFS_Type()
)
ncmcsuCurrentNETOOFS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmcsuCurrentNETOOFS.setStatus("mandatory")
_NcmcsuCurrentNETLOSS_Type = Gauge32
_NcmcsuCurrentNETLOSS_Object = MibTableColumn
ncmcsuCurrentNETLOSS = _NcmcsuCurrentNETLOSS_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3025, 6011, 1, 5),
    _NcmcsuCurrentNETLOSS_Type()
)
ncmcsuCurrentNETLOSS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmcsuCurrentNETLOSS.setStatus("mandatory")
_NcmcsuCurrentNETAISS_Type = Gauge32
_NcmcsuCurrentNETAISS_Object = MibTableColumn
ncmcsuCurrentNETAISS = _NcmcsuCurrentNETAISS_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3025, 6011, 1, 6),
    _NcmcsuCurrentNETAISS_Type()
)
ncmcsuCurrentNETAISS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmcsuCurrentNETAISS.setStatus("mandatory")
_NcmcsuCurrentNETBERS_Type = Gauge32
_NcmcsuCurrentNETBERS_Object = MibTableColumn
ncmcsuCurrentNETBERS = _NcmcsuCurrentNETBERS_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3025, 6011, 1, 7),
    _NcmcsuCurrentNETBERS_Type()
)
ncmcsuCurrentNETBERS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmcsuCurrentNETBERS.setStatus("mandatory")
_NcmcsuCurrentNETYELS_Type = Gauge32
_NcmcsuCurrentNETYELS_Object = MibTableColumn
ncmcsuCurrentNETYELS = _NcmcsuCurrentNETYELS_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3025, 6011, 1, 8),
    _NcmcsuCurrentNETYELS_Type()
)
ncmcsuCurrentNETYELS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmcsuCurrentNETYELS.setStatus("mandatory")
_NcmcsuCurrentNETLOFS_Type = Gauge32
_NcmcsuCurrentNETLOFS_Object = MibTableColumn
ncmcsuCurrentNETLOFS = _NcmcsuCurrentNETLOFS_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3025, 6011, 1, 9),
    _NcmcsuCurrentNETLOFS_Type()
)
ncmcsuCurrentNETLOFS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmcsuCurrentNETLOFS.setStatus("mandatory")
_NcmcsuCurrentNETESL_Type = Gauge32
_NcmcsuCurrentNETESL_Object = MibTableColumn
ncmcsuCurrentNETESL = _NcmcsuCurrentNETESL_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3025, 6011, 1, 10),
    _NcmcsuCurrentNETESL_Type()
)
ncmcsuCurrentNETESL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmcsuCurrentNETESL.setStatus("mandatory")
_NcmcsuCurrentNETSEFS_Type = Gauge32
_NcmcsuCurrentNETSEFS_Object = MibTableColumn
ncmcsuCurrentNETSEFS = _NcmcsuCurrentNETSEFS_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3025, 6011, 1, 11),
    _NcmcsuCurrentNETSEFS_Type()
)
ncmcsuCurrentNETSEFS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmcsuCurrentNETSEFS.setStatus("mandatory")
_NcmcsuCurrentEQOOFS_Type = Gauge32
_NcmcsuCurrentEQOOFS_Object = MibTableColumn
ncmcsuCurrentEQOOFS = _NcmcsuCurrentEQOOFS_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3025, 6011, 1, 12),
    _NcmcsuCurrentEQOOFS_Type()
)
ncmcsuCurrentEQOOFS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmcsuCurrentEQOOFS.setStatus("mandatory")
_NcmcsuCurrentEQDTED_Type = Gauge32
_NcmcsuCurrentEQDTED_Object = MibTableColumn
ncmcsuCurrentEQDTED = _NcmcsuCurrentEQDTED_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3025, 6011, 1, 13),
    _NcmcsuCurrentEQDTED_Type()
)
ncmcsuCurrentEQDTED.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmcsuCurrentEQDTED.setStatus("mandatory")
_NcmcsuCurrentEQDBER_Type = Gauge32
_NcmcsuCurrentEQDBER_Object = MibTableColumn
ncmcsuCurrentEQDBER = _NcmcsuCurrentEQDBER_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3025, 6011, 1, 14),
    _NcmcsuCurrentEQDBER_Type()
)
ncmcsuCurrentEQDBER.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmcsuCurrentEQDBER.setStatus("mandatory")
_NcmcsuCurrentEQES_Type = Gauge32
_NcmcsuCurrentEQES_Object = MibTableColumn
ncmcsuCurrentEQES = _NcmcsuCurrentEQES_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3025, 6011, 1, 15),
    _NcmcsuCurrentEQES_Type()
)
ncmcsuCurrentEQES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmcsuCurrentEQES.setStatus("mandatory")
_NcmcsuCurrentEQUAS_Type = Gauge32
_NcmcsuCurrentEQUAS_Object = MibTableColumn
ncmcsuCurrentEQUAS = _NcmcsuCurrentEQUAS_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3025, 6011, 1, 16),
    _NcmcsuCurrentEQUAS_Type()
)
ncmcsuCurrentEQUAS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmcsuCurrentEQUAS.setStatus("mandatory")
_NcmcsuCurrentEQESL_Type = Gauge32
_NcmcsuCurrentEQESL_Object = MibTableColumn
ncmcsuCurrentEQESL = _NcmcsuCurrentEQESL_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3025, 6011, 1, 17),
    _NcmcsuCurrentEQESL_Type()
)
ncmcsuCurrentEQESL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmcsuCurrentEQESL.setStatus("mandatory")
_NcmcsuTotalTable_Object = MibTable
ncmcsuTotalTable = _NcmcsuTotalTable_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3025, 6012)
)
if mibBuilder.loadTexts:
    ncmcsuTotalTable.setStatus("mandatory")
_NcmcsuTotalEntry_Object = MibTableRow
ncmcsuTotalEntry = _NcmcsuTotalEntry_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3025, 6012, 1)
)
ncmcsuTotalEntry.setIndexNames(
    (0, "VERILINK-ENTERPRISE-CSUNCM-MIB", "ncmcsuNIDTotalIndex"),
    (0, "VERILINK-ENTERPRISE-CSUNCM-MIB", "ncmcsuTotalIndex"),
    (0, "VERILINK-ENTERPRISE-CSUNCM-MIB", "ncmcsuTotalEndType"),
)
if mibBuilder.loadTexts:
    ncmcsuTotalEntry.setStatus("mandatory")


class _NcmcsuNIDTotalIndex_Type(Integer32):
    """Custom type ncmcsuNIDTotalIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_NcmcsuNIDTotalIndex_Type.__name__ = "Integer32"
_NcmcsuNIDTotalIndex_Object = MibTableColumn
ncmcsuNIDTotalIndex = _NcmcsuNIDTotalIndex_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3025, 6012, 1, 1),
    _NcmcsuNIDTotalIndex_Type()
)
ncmcsuNIDTotalIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmcsuNIDTotalIndex.setStatus("mandatory")


class _NcmcsuTotalIndex_Type(Integer32):
    """Custom type ncmcsuTotalIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_NcmcsuTotalIndex_Type.__name__ = "Integer32"
_NcmcsuTotalIndex_Object = MibTableColumn
ncmcsuTotalIndex = _NcmcsuTotalIndex_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3025, 6012, 1, 2),
    _NcmcsuTotalIndex_Type()
)
ncmcsuTotalIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmcsuTotalIndex.setStatus("mandatory")


class _NcmcsuTotalEndType_Type(Integer32):
    """Custom type ncmcsuTotalEndType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("far-End", 2),
          ("near-End", 1))
    )


_NcmcsuTotalEndType_Type.__name__ = "Integer32"
_NcmcsuTotalEndType_Object = MibTableColumn
ncmcsuTotalEndType = _NcmcsuTotalEndType_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3025, 6012, 1, 3),
    _NcmcsuTotalEndType_Type()
)
ncmcsuTotalEndType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmcsuTotalEndType.setStatus("mandatory")
_NcmcsuTotalNETOOFS_Type = Gauge32
_NcmcsuTotalNETOOFS_Object = MibTableColumn
ncmcsuTotalNETOOFS = _NcmcsuTotalNETOOFS_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3025, 6012, 1, 4),
    _NcmcsuTotalNETOOFS_Type()
)
ncmcsuTotalNETOOFS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmcsuTotalNETOOFS.setStatus("mandatory")
_NcmcsuTotalNETLOSS_Type = Gauge32
_NcmcsuTotalNETLOSS_Object = MibTableColumn
ncmcsuTotalNETLOSS = _NcmcsuTotalNETLOSS_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3025, 6012, 1, 5),
    _NcmcsuTotalNETLOSS_Type()
)
ncmcsuTotalNETLOSS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmcsuTotalNETLOSS.setStatus("mandatory")
_NcmcsuTotalNETAISS_Type = Gauge32
_NcmcsuTotalNETAISS_Object = MibTableColumn
ncmcsuTotalNETAISS = _NcmcsuTotalNETAISS_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3025, 6012, 1, 6),
    _NcmcsuTotalNETAISS_Type()
)
ncmcsuTotalNETAISS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmcsuTotalNETAISS.setStatus("mandatory")
_NcmcsuTotalNETBERS_Type = Gauge32
_NcmcsuTotalNETBERS_Object = MibTableColumn
ncmcsuTotalNETBERS = _NcmcsuTotalNETBERS_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3025, 6012, 1, 7),
    _NcmcsuTotalNETBERS_Type()
)
ncmcsuTotalNETBERS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmcsuTotalNETBERS.setStatus("mandatory")
_NcmcsuTotalNETYELS_Type = Gauge32
_NcmcsuTotalNETYELS_Object = MibTableColumn
ncmcsuTotalNETYELS = _NcmcsuTotalNETYELS_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3025, 6012, 1, 8),
    _NcmcsuTotalNETYELS_Type()
)
ncmcsuTotalNETYELS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmcsuTotalNETYELS.setStatus("mandatory")
_NcmcsuTotalNETLOFS_Type = Gauge32
_NcmcsuTotalNETLOFS_Object = MibTableColumn
ncmcsuTotalNETLOFS = _NcmcsuTotalNETLOFS_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3025, 6012, 1, 9),
    _NcmcsuTotalNETLOFS_Type()
)
ncmcsuTotalNETLOFS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmcsuTotalNETLOFS.setStatus("mandatory")
_NcmcsuTotalNETESL_Type = Gauge32
_NcmcsuTotalNETESL_Object = MibTableColumn
ncmcsuTotalNETESL = _NcmcsuTotalNETESL_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3025, 6012, 1, 10),
    _NcmcsuTotalNETESL_Type()
)
ncmcsuTotalNETESL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmcsuTotalNETESL.setStatus("mandatory")
_NcmcsuTotalNETSEFS_Type = Gauge32
_NcmcsuTotalNETSEFS_Object = MibTableColumn
ncmcsuTotalNETSEFS = _NcmcsuTotalNETSEFS_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3025, 6012, 1, 11),
    _NcmcsuTotalNETSEFS_Type()
)
ncmcsuTotalNETSEFS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmcsuTotalNETSEFS.setStatus("mandatory")
_NcmcsuTotalEQOOFS_Type = Gauge32
_NcmcsuTotalEQOOFS_Object = MibTableColumn
ncmcsuTotalEQOOFS = _NcmcsuTotalEQOOFS_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3025, 6012, 1, 12),
    _NcmcsuTotalEQOOFS_Type()
)
ncmcsuTotalEQOOFS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmcsuTotalEQOOFS.setStatus("mandatory")
_NcmcsuTotalEQDTED_Type = Gauge32
_NcmcsuTotalEQDTED_Object = MibTableColumn
ncmcsuTotalEQDTED = _NcmcsuTotalEQDTED_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3025, 6012, 1, 13),
    _NcmcsuTotalEQDTED_Type()
)
ncmcsuTotalEQDTED.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmcsuTotalEQDTED.setStatus("mandatory")
_NcmcsuTotalEQDBER_Type = Gauge32
_NcmcsuTotalEQDBER_Object = MibTableColumn
ncmcsuTotalEQDBER = _NcmcsuTotalEQDBER_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3025, 6012, 1, 14),
    _NcmcsuTotalEQDBER_Type()
)
ncmcsuTotalEQDBER.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmcsuTotalEQDBER.setStatus("mandatory")
_NcmcsuTotalEQES_Type = Gauge32
_NcmcsuTotalEQES_Object = MibTableColumn
ncmcsuTotalEQES = _NcmcsuTotalEQES_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3025, 6012, 1, 15),
    _NcmcsuTotalEQES_Type()
)
ncmcsuTotalEQES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmcsuTotalEQES.setStatus("mandatory")
_NcmcsuTotalEQUAS_Type = Gauge32
_NcmcsuTotalEQUAS_Object = MibTableColumn
ncmcsuTotalEQUAS = _NcmcsuTotalEQUAS_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3025, 6012, 1, 16),
    _NcmcsuTotalEQUAS_Type()
)
ncmcsuTotalEQUAS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmcsuTotalEQUAS.setStatus("mandatory")
_NcmcsuTotalEQESL_Type = Gauge32
_NcmcsuTotalEQESL_Object = MibTableColumn
ncmcsuTotalEQESL = _NcmcsuTotalEQESL_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3025, 6012, 1, 17),
    _NcmcsuTotalEQESL_Type()
)
ncmcsuTotalEQESL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmcsuTotalEQESL.setStatus("mandatory")
_NcmcsuIntervalTable_Object = MibTable
ncmcsuIntervalTable = _NcmcsuIntervalTable_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3025, 6013)
)
if mibBuilder.loadTexts:
    ncmcsuIntervalTable.setStatus("mandatory")
_NcmcsuIntervalEntry_Object = MibTableRow
ncmcsuIntervalEntry = _NcmcsuIntervalEntry_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3025, 6013, 1)
)
ncmcsuIntervalEntry.setIndexNames(
    (0, "VERILINK-ENTERPRISE-CSUNCM-MIB", "ncmcsuNIDIntervalIndex"),
    (0, "VERILINK-ENTERPRISE-CSUNCM-MIB", "ncmcsuIntervalIndex"),
    (0, "VERILINK-ENTERPRISE-CSUNCM-MIB", "ncmcsuIntervalEndType"),
    (0, "VERILINK-ENTERPRISE-CSUNCM-MIB", "ncmcsuIntervalNumber"),
)
if mibBuilder.loadTexts:
    ncmcsuIntervalEntry.setStatus("mandatory")
_NcmcsuNIDIntervalIndex_Type = Integer32
_NcmcsuNIDIntervalIndex_Object = MibTableColumn
ncmcsuNIDIntervalIndex = _NcmcsuNIDIntervalIndex_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3025, 6013, 1, 1),
    _NcmcsuNIDIntervalIndex_Type()
)
ncmcsuNIDIntervalIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmcsuNIDIntervalIndex.setStatus("mandatory")


class _NcmcsuIntervalIndex_Type(Integer32):
    """Custom type ncmcsuIntervalIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_NcmcsuIntervalIndex_Type.__name__ = "Integer32"
_NcmcsuIntervalIndex_Object = MibTableColumn
ncmcsuIntervalIndex = _NcmcsuIntervalIndex_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3025, 6013, 1, 2),
    _NcmcsuIntervalIndex_Type()
)
ncmcsuIntervalIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmcsuIntervalIndex.setStatus("mandatory")


class _NcmcsuIntervalEndType_Type(Integer32):
    """Custom type ncmcsuIntervalEndType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("far-End", 2),
          ("near-End", 1))
    )


_NcmcsuIntervalEndType_Type.__name__ = "Integer32"
_NcmcsuIntervalEndType_Object = MibTableColumn
ncmcsuIntervalEndType = _NcmcsuIntervalEndType_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3025, 6013, 1, 3),
    _NcmcsuIntervalEndType_Type()
)
ncmcsuIntervalEndType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmcsuIntervalEndType.setStatus("mandatory")


class _NcmcsuIntervalNumber_Type(Integer32):
    """Custom type ncmcsuIntervalNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 96),
    )


_NcmcsuIntervalNumber_Type.__name__ = "Integer32"
_NcmcsuIntervalNumber_Object = MibTableColumn
ncmcsuIntervalNumber = _NcmcsuIntervalNumber_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3025, 6013, 1, 4),
    _NcmcsuIntervalNumber_Type()
)
ncmcsuIntervalNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmcsuIntervalNumber.setStatus("mandatory")
_NcmcsuIntervalNETOOFS_Type = Gauge32
_NcmcsuIntervalNETOOFS_Object = MibTableColumn
ncmcsuIntervalNETOOFS = _NcmcsuIntervalNETOOFS_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3025, 6013, 1, 5),
    _NcmcsuIntervalNETOOFS_Type()
)
ncmcsuIntervalNETOOFS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmcsuIntervalNETOOFS.setStatus("mandatory")
_NcmcsuIntervalNETLOSS_Type = Gauge32
_NcmcsuIntervalNETLOSS_Object = MibTableColumn
ncmcsuIntervalNETLOSS = _NcmcsuIntervalNETLOSS_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3025, 6013, 1, 6),
    _NcmcsuIntervalNETLOSS_Type()
)
ncmcsuIntervalNETLOSS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmcsuIntervalNETLOSS.setStatus("mandatory")
_NcmcsuIntervalNETAISS_Type = Gauge32
_NcmcsuIntervalNETAISS_Object = MibTableColumn
ncmcsuIntervalNETAISS = _NcmcsuIntervalNETAISS_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3025, 6013, 1, 7),
    _NcmcsuIntervalNETAISS_Type()
)
ncmcsuIntervalNETAISS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmcsuIntervalNETAISS.setStatus("mandatory")
_NcmcsuIntervalNETBERS_Type = Gauge32
_NcmcsuIntervalNETBERS_Object = MibTableColumn
ncmcsuIntervalNETBERS = _NcmcsuIntervalNETBERS_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3025, 6013, 1, 8),
    _NcmcsuIntervalNETBERS_Type()
)
ncmcsuIntervalNETBERS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmcsuIntervalNETBERS.setStatus("mandatory")
_NcmcsuIntervalNETYELS_Type = Gauge32
_NcmcsuIntervalNETYELS_Object = MibTableColumn
ncmcsuIntervalNETYELS = _NcmcsuIntervalNETYELS_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3025, 6013, 1, 9),
    _NcmcsuIntervalNETYELS_Type()
)
ncmcsuIntervalNETYELS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmcsuIntervalNETYELS.setStatus("mandatory")
_NcmcsuIntervalNETLOFS_Type = Gauge32
_NcmcsuIntervalNETLOFS_Object = MibTableColumn
ncmcsuIntervalNETLOFS = _NcmcsuIntervalNETLOFS_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3025, 6013, 1, 10),
    _NcmcsuIntervalNETLOFS_Type()
)
ncmcsuIntervalNETLOFS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmcsuIntervalNETLOFS.setStatus("mandatory")
_NcmcsuIntervalNETESL_Type = Gauge32
_NcmcsuIntervalNETESL_Object = MibTableColumn
ncmcsuIntervalNETESL = _NcmcsuIntervalNETESL_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3025, 6013, 1, 11),
    _NcmcsuIntervalNETESL_Type()
)
ncmcsuIntervalNETESL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmcsuIntervalNETESL.setStatus("mandatory")
_NcmcsuIntervalNETSEFS_Type = Gauge32
_NcmcsuIntervalNETSEFS_Object = MibTableColumn
ncmcsuIntervalNETSEFS = _NcmcsuIntervalNETSEFS_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3025, 6013, 1, 12),
    _NcmcsuIntervalNETSEFS_Type()
)
ncmcsuIntervalNETSEFS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmcsuIntervalNETSEFS.setStatus("mandatory")
_NcmcsuIntervalEQOOFS_Type = Gauge32
_NcmcsuIntervalEQOOFS_Object = MibTableColumn
ncmcsuIntervalEQOOFS = _NcmcsuIntervalEQOOFS_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3025, 6013, 1, 13),
    _NcmcsuIntervalEQOOFS_Type()
)
ncmcsuIntervalEQOOFS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmcsuIntervalEQOOFS.setStatus("mandatory")
_NcmcsuIntervalEQDTED_Type = Gauge32
_NcmcsuIntervalEQDTED_Object = MibTableColumn
ncmcsuIntervalEQDTED = _NcmcsuIntervalEQDTED_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3025, 6013, 1, 14),
    _NcmcsuIntervalEQDTED_Type()
)
ncmcsuIntervalEQDTED.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmcsuIntervalEQDTED.setStatus("mandatory")
_NcmcsuIntervalEQDBER_Type = Gauge32
_NcmcsuIntervalEQDBER_Object = MibTableColumn
ncmcsuIntervalEQDBER = _NcmcsuIntervalEQDBER_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3025, 6013, 1, 15),
    _NcmcsuIntervalEQDBER_Type()
)
ncmcsuIntervalEQDBER.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmcsuIntervalEQDBER.setStatus("mandatory")
_NcmcsuIntervalEQES_Type = Gauge32
_NcmcsuIntervalEQES_Object = MibTableColumn
ncmcsuIntervalEQES = _NcmcsuIntervalEQES_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3025, 6013, 1, 16),
    _NcmcsuIntervalEQES_Type()
)
ncmcsuIntervalEQES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmcsuIntervalEQES.setStatus("mandatory")
_NcmcsuIntervalEQUAS_Type = Gauge32
_NcmcsuIntervalEQUAS_Object = MibTableColumn
ncmcsuIntervalEQUAS = _NcmcsuIntervalEQUAS_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3025, 6013, 1, 17),
    _NcmcsuIntervalEQUAS_Type()
)
ncmcsuIntervalEQUAS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmcsuIntervalEQUAS.setStatus("mandatory")
_NcmcsuIntervalEQESL_Type = Gauge32
_NcmcsuIntervalEQESL_Object = MibTableColumn
ncmcsuIntervalEQESL = _NcmcsuIntervalEQESL_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3025, 6013, 1, 18),
    _NcmcsuIntervalEQESL_Type()
)
ncmcsuIntervalEQESL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmcsuIntervalEQESL.setStatus("mandatory")
_NcmcsucommonTable_Object = MibTable
ncmcsucommonTable = _NcmcsucommonTable_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3025, 6014)
)
if mibBuilder.loadTexts:
    ncmcsucommonTable.setStatus("mandatory")
_NcmcsucommonEntry_Object = MibTableRow
ncmcsucommonEntry = _NcmcsucommonEntry_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3025, 6014, 1)
)
ncmcsucommonEntry.setIndexNames(
    (0, "VERILINK-ENTERPRISE-CSUNCM-MIB", "ncmcsuNIDcommonIndex"),
    (0, "VERILINK-ENTERPRISE-CSUNCM-MIB", "ncmcsucommonIndex"),
    (0, "VERILINK-ENTERPRISE-CSUNCM-MIB", "ncmcsucommonEndType"),
)
if mibBuilder.loadTexts:
    ncmcsucommonEntry.setStatus("mandatory")
_NcmcsuNIDcommonIndex_Type = Integer32
_NcmcsuNIDcommonIndex_Object = MibTableColumn
ncmcsuNIDcommonIndex = _NcmcsuNIDcommonIndex_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3025, 6014, 1, 1),
    _NcmcsuNIDcommonIndex_Type()
)
ncmcsuNIDcommonIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmcsuNIDcommonIndex.setStatus("mandatory")
_NcmcsucommonIndex_Type = Integer32
_NcmcsucommonIndex_Object = MibTableColumn
ncmcsucommonIndex = _NcmcsucommonIndex_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3025, 6014, 1, 2),
    _NcmcsucommonIndex_Type()
)
ncmcsucommonIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmcsucommonIndex.setStatus("mandatory")


class _NcmcsucommonEndType_Type(Integer32):
    """Custom type ncmcsucommonEndType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("far-End", 2),
          ("near-End", 1))
    )


_NcmcsucommonEndType_Type.__name__ = "Integer32"
_NcmcsucommonEndType_Object = MibTableColumn
ncmcsucommonEndType = _NcmcsucommonEndType_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3025, 6014, 1, 3),
    _NcmcsucommonEndType_Type()
)
ncmcsucommonEndType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmcsucommonEndType.setStatus("mandatory")
_NcmValidInterval_Type = Integer32
_NcmValidInterval_Object = MibTableColumn
ncmValidInterval = _NcmValidInterval_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3025, 6014, 1, 4),
    _NcmValidInterval_Type()
)
ncmValidInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmValidInterval.setStatus("mandatory")
_NcmCurrentIntervalSeconds_Type = Integer32
_NcmCurrentIntervalSeconds_Object = MibTableColumn
ncmCurrentIntervalSeconds = _NcmCurrentIntervalSeconds_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3025, 6014, 1, 5),
    _NcmCurrentIntervalSeconds_Type()
)
ncmCurrentIntervalSeconds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmCurrentIntervalSeconds.setStatus("mandatory")


class _NcmResetPerformanceReg_Type(Integer32):
    """Custom type ncmResetPerformanceReg based on Integer32"""
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


_NcmResetPerformanceReg_Type.__name__ = "Integer32"
_NcmResetPerformanceReg_Object = MibTableColumn
ncmResetPerformanceReg = _NcmResetPerformanceReg_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3025, 6014, 1, 6),
    _NcmResetPerformanceReg_Type()
)
ncmResetPerformanceReg.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ncmResetPerformanceReg.setStatus("mandatory")
_NcmcsuRetrievalStatusOneTable_Object = MibTable
ncmcsuRetrievalStatusOneTable = _NcmcsuRetrievalStatusOneTable_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3025, 6015)
)
if mibBuilder.loadTexts:
    ncmcsuRetrievalStatusOneTable.setStatus("mandatory")
_NcmcsuRetrievalStatusOneEntry_Object = MibTableRow
ncmcsuRetrievalStatusOneEntry = _NcmcsuRetrievalStatusOneEntry_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3025, 6015, 1)
)
ncmcsuRetrievalStatusOneEntry.setIndexNames(
    (0, "VERILINK-ENTERPRISE-CSUNCM-MIB", "ncmcsuNIDRetrievalStatusIndex1"),
    (0, "VERILINK-ENTERPRISE-CSUNCM-MIB", "ncmcsuRetrievalStatusIndex1"),
)
if mibBuilder.loadTexts:
    ncmcsuRetrievalStatusOneEntry.setStatus("mandatory")
_NcmcsuNIDRetrievalStatusIndex1_Type = Integer32
_NcmcsuNIDRetrievalStatusIndex1_Object = MibTableColumn
ncmcsuNIDRetrievalStatusIndex1 = _NcmcsuNIDRetrievalStatusIndex1_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3025, 6015, 1, 1),
    _NcmcsuNIDRetrievalStatusIndex1_Type()
)
ncmcsuNIDRetrievalStatusIndex1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmcsuNIDRetrievalStatusIndex1.setStatus("mandatory")
_NcmcsuRetrievalStatusIndex1_Type = Integer32
_NcmcsuRetrievalStatusIndex1_Object = MibTableColumn
ncmcsuRetrievalStatusIndex1 = _NcmcsuRetrievalStatusIndex1_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3025, 6015, 1, 2),
    _NcmcsuRetrievalStatusIndex1_Type()
)
ncmcsuRetrievalStatusIndex1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmcsuRetrievalStatusIndex1.setStatus("mandatory")


class _NcmcsuNearAlmBERthresexcd_Type(Integer32):
    """Custom type ncmcsuNearAlmBERthresexcd based on Integer32"""
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


_NcmcsuNearAlmBERthresexcd_Type.__name__ = "Integer32"
_NcmcsuNearAlmBERthresexcd_Object = MibTableColumn
ncmcsuNearAlmBERthresexcd = _NcmcsuNearAlmBERthresexcd_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3025, 6015, 1, 3),
    _NcmcsuNearAlmBERthresexcd_Type()
)
ncmcsuNearAlmBERthresexcd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmcsuNearAlmBERthresexcd.setStatus("mandatory")


class _NcmcsuNearAlmESthresexcd_Type(Integer32):
    """Custom type ncmcsuNearAlmESthresexcd based on Integer32"""
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


_NcmcsuNearAlmESthresexcd_Type.__name__ = "Integer32"
_NcmcsuNearAlmESthresexcd_Object = MibTableColumn
ncmcsuNearAlmESthresexcd = _NcmcsuNearAlmESthresexcd_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3025, 6015, 1, 4),
    _NcmcsuNearAlmESthresexcd_Type()
)
ncmcsuNearAlmESthresexcd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmcsuNearAlmESthresexcd.setStatus("mandatory")


class _NcmcsuNearAlmUASthresexcd_Type(Integer32):
    """Custom type ncmcsuNearAlmUASthresexcd based on Integer32"""
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


_NcmcsuNearAlmUASthresexcd_Type.__name__ = "Integer32"
_NcmcsuNearAlmUASthresexcd_Object = MibTableColumn
ncmcsuNearAlmUASthresexcd = _NcmcsuNearAlmUASthresexcd_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3025, 6015, 1, 5),
    _NcmcsuNearAlmUASthresexcd_Type()
)
ncmcsuNearAlmUASthresexcd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmcsuNearAlmUASthresexcd.setStatus("mandatory")


class _NcmcsuNearAlmLLBPLB_Type(Integer32):
    """Custom type ncmcsuNearAlmLLBPLB based on Integer32"""
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


_NcmcsuNearAlmLLBPLB_Type.__name__ = "Integer32"
_NcmcsuNearAlmLLBPLB_Object = MibTableColumn
ncmcsuNearAlmLLBPLB = _NcmcsuNearAlmLLBPLB_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3025, 6015, 1, 6),
    _NcmcsuNearAlmLLBPLB_Type()
)
ncmcsuNearAlmLLBPLB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmcsuNearAlmLLBPLB.setStatus("mandatory")


class _NcmcsuFarAlmBERthresexcd_Type(Integer32):
    """Custom type ncmcsuFarAlmBERthresexcd based on Integer32"""
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


_NcmcsuFarAlmBERthresexcd_Type.__name__ = "Integer32"
_NcmcsuFarAlmBERthresexcd_Object = MibTableColumn
ncmcsuFarAlmBERthresexcd = _NcmcsuFarAlmBERthresexcd_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3025, 6015, 1, 7),
    _NcmcsuFarAlmBERthresexcd_Type()
)
ncmcsuFarAlmBERthresexcd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmcsuFarAlmBERthresexcd.setStatus("mandatory")


class _NcmcsuFarAlmESthresexcd_Type(Integer32):
    """Custom type ncmcsuFarAlmESthresexcd based on Integer32"""
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


_NcmcsuFarAlmESthresexcd_Type.__name__ = "Integer32"
_NcmcsuFarAlmESthresexcd_Object = MibTableColumn
ncmcsuFarAlmESthresexcd = _NcmcsuFarAlmESthresexcd_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3025, 6015, 1, 8),
    _NcmcsuFarAlmESthresexcd_Type()
)
ncmcsuFarAlmESthresexcd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmcsuFarAlmESthresexcd.setStatus("mandatory")


class _NcmcsuFarAlmUASthresexcd_Type(Integer32):
    """Custom type ncmcsuFarAlmUASthresexcd based on Integer32"""
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


_NcmcsuFarAlmUASthresexcd_Type.__name__ = "Integer32"
_NcmcsuFarAlmUASthresexcd_Object = MibTableColumn
ncmcsuFarAlmUASthresexcd = _NcmcsuFarAlmUASthresexcd_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3025, 6015, 1, 9),
    _NcmcsuFarAlmUASthresexcd_Type()
)
ncmcsuFarAlmUASthresexcd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmcsuFarAlmUASthresexcd.setStatus("mandatory")


class _NcmcsuFarAlmLLBDLB_Type(Integer32):
    """Custom type ncmcsuFarAlmLLBDLB based on Integer32"""
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


_NcmcsuFarAlmLLBDLB_Type.__name__ = "Integer32"
_NcmcsuFarAlmLLBDLB_Object = MibTableColumn
ncmcsuFarAlmLLBDLB = _NcmcsuFarAlmLLBDLB_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3025, 6015, 1, 10),
    _NcmcsuFarAlmLLBDLB_Type()
)
ncmcsuFarAlmLLBDLB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmcsuFarAlmLLBDLB.setStatus("mandatory")


class _NcmcsuFarCsuAbsent_Type(Integer32):
    """Custom type ncmcsuFarCsuAbsent based on Integer32"""
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


_NcmcsuFarCsuAbsent_Type.__name__ = "Integer32"
_NcmcsuFarCsuAbsent_Object = MibTableColumn
ncmcsuFarCsuAbsent = _NcmcsuFarCsuAbsent_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3025, 6015, 1, 11),
    _NcmcsuFarCsuAbsent_Type()
)
ncmcsuFarCsuAbsent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmcsuFarCsuAbsent.setStatus("mandatory")


class _NcmcsuEqStatusLowDensity_Type(Integer32):
    """Custom type ncmcsuEqStatusLowDensity based on Integer32"""
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


_NcmcsuEqStatusLowDensity_Type.__name__ = "Integer32"
_NcmcsuEqStatusLowDensity_Object = MibTableColumn
ncmcsuEqStatusLowDensity = _NcmcsuEqStatusLowDensity_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3025, 6015, 1, 12),
    _NcmcsuEqStatusLowDensity_Type()
)
ncmcsuEqStatusLowDensity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmcsuEqStatusLowDensity.setStatus("mandatory")


class _NcmcsuEqStatusOOF_Type(Integer32):
    """Custom type ncmcsuEqStatusOOF based on Integer32"""
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


_NcmcsuEqStatusOOF_Type.__name__ = "Integer32"
_NcmcsuEqStatusOOF_Object = MibTableColumn
ncmcsuEqStatusOOF = _NcmcsuEqStatusOOF_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3025, 6015, 1, 13),
    _NcmcsuEqStatusOOF_Type()
)
ncmcsuEqStatusOOF.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmcsuEqStatusOOF.setStatus("mandatory")


class _NcmcsuEqStatusCRCError_Type(Integer32):
    """Custom type ncmcsuEqStatusCRCError based on Integer32"""
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


_NcmcsuEqStatusCRCError_Type.__name__ = "Integer32"
_NcmcsuEqStatusCRCError_Object = MibTableColumn
ncmcsuEqStatusCRCError = _NcmcsuEqStatusCRCError_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3025, 6015, 1, 14),
    _NcmcsuEqStatusCRCError_Type()
)
ncmcsuEqStatusCRCError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmcsuEqStatusCRCError.setStatus("mandatory")


class _NcmcsuEqStatusBPV_Type(Integer32):
    """Custom type ncmcsuEqStatusBPV based on Integer32"""
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


_NcmcsuEqStatusBPV_Type.__name__ = "Integer32"
_NcmcsuEqStatusBPV_Object = MibTableColumn
ncmcsuEqStatusBPV = _NcmcsuEqStatusBPV_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3025, 6015, 1, 15),
    _NcmcsuEqStatusBPV_Type()
)
ncmcsuEqStatusBPV.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmcsuEqStatusBPV.setStatus("mandatory")


class _NcmcsuEqStatusPLB_Type(Integer32):
    """Custom type ncmcsuEqStatusPLB based on Integer32"""
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


_NcmcsuEqStatusPLB_Type.__name__ = "Integer32"
_NcmcsuEqStatusPLB_Object = MibTableColumn
ncmcsuEqStatusPLB = _NcmcsuEqStatusPLB_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3025, 6015, 1, 16),
    _NcmcsuEqStatusPLB_Type()
)
ncmcsuEqStatusPLB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmcsuEqStatusPLB.setStatus("mandatory")


class _NcmcsuEqStatusELBRLB_Type(Integer32):
    """Custom type ncmcsuEqStatusELBRLB based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("elb", 2),
          ("no-Loop", 1),
          ("rlb", 3))
    )


_NcmcsuEqStatusELBRLB_Type.__name__ = "Integer32"
_NcmcsuEqStatusELBRLB_Object = MibTableColumn
ncmcsuEqStatusELBRLB = _NcmcsuEqStatusELBRLB_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3025, 6015, 1, 17),
    _NcmcsuEqStatusELBRLB_Type()
)
ncmcsuEqStatusELBRLB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmcsuEqStatusELBRLB.setStatus("mandatory")


class _NcmcsuNetStatusPulses_Type(Integer32):
    """Custom type ncmcsuNetStatusPulses based on Integer32"""
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


_NcmcsuNetStatusPulses_Type.__name__ = "Integer32"
_NcmcsuNetStatusPulses_Object = MibTableColumn
ncmcsuNetStatusPulses = _NcmcsuNetStatusPulses_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3025, 6015, 1, 18),
    _NcmcsuNetStatusPulses_Type()
)
ncmcsuNetStatusPulses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmcsuNetStatusPulses.setStatus("mandatory")


class _NcmcsuNetStatusOOF_Type(Integer32):
    """Custom type ncmcsuNetStatusOOF based on Integer32"""
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


_NcmcsuNetStatusOOF_Type.__name__ = "Integer32"
_NcmcsuNetStatusOOF_Object = MibTableColumn
ncmcsuNetStatusOOF = _NcmcsuNetStatusOOF_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3025, 6015, 1, 19),
    _NcmcsuNetStatusOOF_Type()
)
ncmcsuNetStatusOOF.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmcsuNetStatusOOF.setStatus("mandatory")


class _NcmcsuNetStatusCRCError_Type(Integer32):
    """Custom type ncmcsuNetStatusCRCError based on Integer32"""
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


_NcmcsuNetStatusCRCError_Type.__name__ = "Integer32"
_NcmcsuNetStatusCRCError_Object = MibTableColumn
ncmcsuNetStatusCRCError = _NcmcsuNetStatusCRCError_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3025, 6015, 1, 20),
    _NcmcsuNetStatusCRCError_Type()
)
ncmcsuNetStatusCRCError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmcsuNetStatusCRCError.setStatus("mandatory")


class _NcmcsuNetStatusBPV_Type(Integer32):
    """Custom type ncmcsuNetStatusBPV based on Integer32"""
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


_NcmcsuNetStatusBPV_Type.__name__ = "Integer32"
_NcmcsuNetStatusBPV_Object = MibTableColumn
ncmcsuNetStatusBPV = _NcmcsuNetStatusBPV_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3025, 6015, 1, 21),
    _NcmcsuNetStatusBPV_Type()
)
ncmcsuNetStatusBPV.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmcsuNetStatusBPV.setStatus("mandatory")


class _NcmcsuNetStatusLLB_Type(Integer32):
    """Custom type ncmcsuNetStatusLLB based on Integer32"""
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


_NcmcsuNetStatusLLB_Type.__name__ = "Integer32"
_NcmcsuNetStatusLLB_Object = MibTableColumn
ncmcsuNetStatusLLB = _NcmcsuNetStatusLLB_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3025, 6015, 1, 22),
    _NcmcsuNetStatusLLB_Type()
)
ncmcsuNetStatusLLB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmcsuNetStatusLLB.setStatus("mandatory")


class _NcmcsuXNetStatus1BERthresexcd_Type(Integer32):
    """Custom type ncmcsuXNetStatus1BERthresexcd based on Integer32"""
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


_NcmcsuXNetStatus1BERthresexcd_Type.__name__ = "Integer32"
_NcmcsuXNetStatus1BERthresexcd_Object = MibTableColumn
ncmcsuXNetStatus1BERthresexcd = _NcmcsuXNetStatus1BERthresexcd_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3025, 6015, 1, 23),
    _NcmcsuXNetStatus1BERthresexcd_Type()
)
ncmcsuXNetStatus1BERthresexcd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmcsuXNetStatus1BERthresexcd.setStatus("mandatory")


class _NcmcsuXNetStatus1ES1thresexcd_Type(Integer32):
    """Custom type ncmcsuXNetStatus1ES1thresexcd based on Integer32"""
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


_NcmcsuXNetStatus1ES1thresexcd_Type.__name__ = "Integer32"
_NcmcsuXNetStatus1ES1thresexcd_Object = MibTableColumn
ncmcsuXNetStatus1ES1thresexcd = _NcmcsuXNetStatus1ES1thresexcd_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3025, 6015, 1, 24),
    _NcmcsuXNetStatus1ES1thresexcd_Type()
)
ncmcsuXNetStatus1ES1thresexcd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmcsuXNetStatus1ES1thresexcd.setStatus("mandatory")


class _NcmcsuXNetStatus1ESthresexcd_Type(Integer32):
    """Custom type ncmcsuXNetStatus1ESthresexcd based on Integer32"""
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


_NcmcsuXNetStatus1ESthresexcd_Type.__name__ = "Integer32"
_NcmcsuXNetStatus1ESthresexcd_Object = MibTableColumn
ncmcsuXNetStatus1ESthresexcd = _NcmcsuXNetStatus1ESthresexcd_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3025, 6015, 1, 25),
    _NcmcsuXNetStatus1ESthresexcd_Type()
)
ncmcsuXNetStatus1ESthresexcd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmcsuXNetStatus1ESthresexcd.setStatus("mandatory")


class _NcmcsuXNetStatus1UASthresexcd_Type(Integer32):
    """Custom type ncmcsuXNetStatus1UASthresexcd based on Integer32"""
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


_NcmcsuXNetStatus1UASthresexcd_Type.__name__ = "Integer32"
_NcmcsuXNetStatus1UASthresexcd_Object = MibTableColumn
ncmcsuXNetStatus1UASthresexcd = _NcmcsuXNetStatus1UASthresexcd_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3025, 6015, 1, 26),
    _NcmcsuXNetStatus1UASthresexcd_Type()
)
ncmcsuXNetStatus1UASthresexcd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmcsuXNetStatus1UASthresexcd.setStatus("mandatory")


class _NcmcsuXNetStatus1LLB_Type(Integer32):
    """Custom type ncmcsuXNetStatus1LLB based on Integer32"""
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


_NcmcsuXNetStatus1LLB_Type.__name__ = "Integer32"
_NcmcsuXNetStatus1LLB_Object = MibTableColumn
ncmcsuXNetStatus1LLB = _NcmcsuXNetStatus1LLB_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3025, 6015, 1, 27),
    _NcmcsuXNetStatus1LLB_Type()
)
ncmcsuXNetStatus1LLB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmcsuXNetStatus1LLB.setStatus("mandatory")


class _NcmcsuXNetStatus1PLB_Type(Integer32):
    """Custom type ncmcsuXNetStatus1PLB based on Integer32"""
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


_NcmcsuXNetStatus1PLB_Type.__name__ = "Integer32"
_NcmcsuXNetStatus1PLB_Object = MibTableColumn
ncmcsuXNetStatus1PLB = _NcmcsuXNetStatus1PLB_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3025, 6015, 1, 28),
    _NcmcsuXNetStatus1PLB_Type()
)
ncmcsuXNetStatus1PLB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmcsuXNetStatus1PLB.setStatus("mandatory")


class _NcmcsuXNetStatus1LOS_Type(Integer32):
    """Custom type ncmcsuXNetStatus1LOS based on Integer32"""
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


_NcmcsuXNetStatus1LOS_Type.__name__ = "Integer32"
_NcmcsuXNetStatus1LOS_Object = MibTableColumn
ncmcsuXNetStatus1LOS = _NcmcsuXNetStatus1LOS_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3025, 6015, 1, 29),
    _NcmcsuXNetStatus1LOS_Type()
)
ncmcsuXNetStatus1LOS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmcsuXNetStatus1LOS.setStatus("mandatory")


class _NcmcsuXNetStatus1YEL_Type(Integer32):
    """Custom type ncmcsuXNetStatus1YEL based on Integer32"""
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


_NcmcsuXNetStatus1YEL_Type.__name__ = "Integer32"
_NcmcsuXNetStatus1YEL_Object = MibTableColumn
ncmcsuXNetStatus1YEL = _NcmcsuXNetStatus1YEL_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3025, 6015, 1, 30),
    _NcmcsuXNetStatus1YEL_Type()
)
ncmcsuXNetStatus1YEL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmcsuXNetStatus1YEL.setStatus("mandatory")


class _NcmcsuXNetStatus2LOF_Type(Integer32):
    """Custom type ncmcsuXNetStatus2LOF based on Integer32"""
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


_NcmcsuXNetStatus2LOF_Type.__name__ = "Integer32"
_NcmcsuXNetStatus2LOF_Object = MibTableColumn
ncmcsuXNetStatus2LOF = _NcmcsuXNetStatus2LOF_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3025, 6015, 1, 31),
    _NcmcsuXNetStatus2LOF_Type()
)
ncmcsuXNetStatus2LOF.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmcsuXNetStatus2LOF.setStatus("mandatory")


class _NcmcsuXNetStatus2AIS_Type(Integer32):
    """Custom type ncmcsuXNetStatus2AIS based on Integer32"""
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


_NcmcsuXNetStatus2AIS_Type.__name__ = "Integer32"
_NcmcsuXNetStatus2AIS_Object = MibTableColumn
ncmcsuXNetStatus2AIS = _NcmcsuXNetStatus2AIS_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3025, 6015, 1, 32),
    _NcmcsuXNetStatus2AIS_Type()
)
ncmcsuXNetStatus2AIS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmcsuXNetStatus2AIS.setStatus("mandatory")


class _NcmcsuXNetStatus2TSTProgress_Type(Integer32):
    """Custom type ncmcsuXNetStatus2TSTProgress based on Integer32"""
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


_NcmcsuXNetStatus2TSTProgress_Type.__name__ = "Integer32"
_NcmcsuXNetStatus2TSTProgress_Object = MibTableColumn
ncmcsuXNetStatus2TSTProgress = _NcmcsuXNetStatus2TSTProgress_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3025, 6015, 1, 33),
    _NcmcsuXNetStatus2TSTProgress_Type()
)
ncmcsuXNetStatus2TSTProgress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmcsuXNetStatus2TSTProgress.setStatus("mandatory")


class _NcmcsuXNetStatus2PowerAFail_Type(Integer32):
    """Custom type ncmcsuXNetStatus2PowerAFail based on Integer32"""
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


_NcmcsuXNetStatus2PowerAFail_Type.__name__ = "Integer32"
_NcmcsuXNetStatus2PowerAFail_Object = MibTableColumn
ncmcsuXNetStatus2PowerAFail = _NcmcsuXNetStatus2PowerAFail_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3025, 6015, 1, 34),
    _NcmcsuXNetStatus2PowerAFail_Type()
)
ncmcsuXNetStatus2PowerAFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmcsuXNetStatus2PowerAFail.setStatus("mandatory")


class _NcmcsuXNetStatus2PowerBFail_Type(Integer32):
    """Custom type ncmcsuXNetStatus2PowerBFail based on Integer32"""
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


_NcmcsuXNetStatus2PowerBFail_Type.__name__ = "Integer32"
_NcmcsuXNetStatus2PowerBFail_Object = MibTableColumn
ncmcsuXNetStatus2PowerBFail = _NcmcsuXNetStatus2PowerBFail_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3025, 6015, 1, 35),
    _NcmcsuXNetStatus2PowerBFail_Type()
)
ncmcsuXNetStatus2PowerBFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmcsuXNetStatus2PowerBFail.setStatus("mandatory")


class _NcmcsuXEqStatus1BERthresexcd_Type(Integer32):
    """Custom type ncmcsuXEqStatus1BERthresexcd based on Integer32"""
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


_NcmcsuXEqStatus1BERthresexcd_Type.__name__ = "Integer32"
_NcmcsuXEqStatus1BERthresexcd_Object = MibTableColumn
ncmcsuXEqStatus1BERthresexcd = _NcmcsuXEqStatus1BERthresexcd_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3025, 6015, 1, 36),
    _NcmcsuXEqStatus1BERthresexcd_Type()
)
ncmcsuXEqStatus1BERthresexcd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmcsuXEqStatus1BERthresexcd.setStatus("mandatory")


class _NcmcsuXEqStatus1ES1thresexcd_Type(Integer32):
    """Custom type ncmcsuXEqStatus1ES1thresexcd based on Integer32"""
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


_NcmcsuXEqStatus1ES1thresexcd_Type.__name__ = "Integer32"
_NcmcsuXEqStatus1ES1thresexcd_Object = MibTableColumn
ncmcsuXEqStatus1ES1thresexcd = _NcmcsuXEqStatus1ES1thresexcd_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3025, 6015, 1, 37),
    _NcmcsuXEqStatus1ES1thresexcd_Type()
)
ncmcsuXEqStatus1ES1thresexcd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmcsuXEqStatus1ES1thresexcd.setStatus("mandatory")


class _NcmcsuXEqStatus1ESthresexcd_Type(Integer32):
    """Custom type ncmcsuXEqStatus1ESthresexcd based on Integer32"""
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


_NcmcsuXEqStatus1ESthresexcd_Type.__name__ = "Integer32"
_NcmcsuXEqStatus1ESthresexcd_Object = MibTableColumn
ncmcsuXEqStatus1ESthresexcd = _NcmcsuXEqStatus1ESthresexcd_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3025, 6015, 1, 38),
    _NcmcsuXEqStatus1ESthresexcd_Type()
)
ncmcsuXEqStatus1ESthresexcd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmcsuXEqStatus1ESthresexcd.setStatus("mandatory")


class _NcmcsuXEqStatus1UASthresexcd_Type(Integer32):
    """Custom type ncmcsuXEqStatus1UASthresexcd based on Integer32"""
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


_NcmcsuXEqStatus1UASthresexcd_Type.__name__ = "Integer32"
_NcmcsuXEqStatus1UASthresexcd_Object = MibTableColumn
ncmcsuXEqStatus1UASthresexcd = _NcmcsuXEqStatus1UASthresexcd_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3025, 6015, 1, 39),
    _NcmcsuXEqStatus1UASthresexcd_Type()
)
ncmcsuXEqStatus1UASthresexcd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmcsuXEqStatus1UASthresexcd.setStatus("mandatory")


class _NcmcsuXEqStatus1ELB_Type(Integer32):
    """Custom type ncmcsuXEqStatus1ELB based on Integer32"""
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


_NcmcsuXEqStatus1ELB_Type.__name__ = "Integer32"
_NcmcsuXEqStatus1ELB_Object = MibTableColumn
ncmcsuXEqStatus1ELB = _NcmcsuXEqStatus1ELB_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3025, 6015, 1, 40),
    _NcmcsuXEqStatus1ELB_Type()
)
ncmcsuXEqStatus1ELB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmcsuXEqStatus1ELB.setStatus("mandatory")


class _NcmcsuXEqStatus1RLB_Type(Integer32):
    """Custom type ncmcsuXEqStatus1RLB based on Integer32"""
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


_NcmcsuXEqStatus1RLB_Type.__name__ = "Integer32"
_NcmcsuXEqStatus1RLB_Object = MibTableColumn
ncmcsuXEqStatus1RLB = _NcmcsuXEqStatus1RLB_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3025, 6015, 1, 41),
    _NcmcsuXEqStatus1RLB_Type()
)
ncmcsuXEqStatus1RLB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmcsuXEqStatus1RLB.setStatus("mandatory")


class _NcmcsuXEqStatus1LOS_Type(Integer32):
    """Custom type ncmcsuXEqStatus1LOS based on Integer32"""
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


_NcmcsuXEqStatus1LOS_Type.__name__ = "Integer32"
_NcmcsuXEqStatus1LOS_Object = MibTableColumn
ncmcsuXEqStatus1LOS = _NcmcsuXEqStatus1LOS_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3025, 6015, 1, 42),
    _NcmcsuXEqStatus1LOS_Type()
)
ncmcsuXEqStatus1LOS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmcsuXEqStatus1LOS.setStatus("mandatory")


class _NcmcsuXEqStatus1YEL_Type(Integer32):
    """Custom type ncmcsuXEqStatus1YEL based on Integer32"""
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


_NcmcsuXEqStatus1YEL_Type.__name__ = "Integer32"
_NcmcsuXEqStatus1YEL_Object = MibTableColumn
ncmcsuXEqStatus1YEL = _NcmcsuXEqStatus1YEL_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3025, 6015, 1, 43),
    _NcmcsuXEqStatus1YEL_Type()
)
ncmcsuXEqStatus1YEL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmcsuXEqStatus1YEL.setStatus("mandatory")


class _NcmcsuXEqStatus2LOF_Type(Integer32):
    """Custom type ncmcsuXEqStatus2LOF based on Integer32"""
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


_NcmcsuXEqStatus2LOF_Type.__name__ = "Integer32"
_NcmcsuXEqStatus2LOF_Object = MibTableColumn
ncmcsuXEqStatus2LOF = _NcmcsuXEqStatus2LOF_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3025, 6015, 1, 44),
    _NcmcsuXEqStatus2LOF_Type()
)
ncmcsuXEqStatus2LOF.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmcsuXEqStatus2LOF.setStatus("mandatory")


class _NcmcsuXEqStatus2AIS_Type(Integer32):
    """Custom type ncmcsuXEqStatus2AIS based on Integer32"""
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


_NcmcsuXEqStatus2AIS_Type.__name__ = "Integer32"
_NcmcsuXEqStatus2AIS_Object = MibTableColumn
ncmcsuXEqStatus2AIS = _NcmcsuXEqStatus2AIS_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3025, 6015, 1, 45),
    _NcmcsuXEqStatus2AIS_Type()
)
ncmcsuXEqStatus2AIS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmcsuXEqStatus2AIS.setStatus("mandatory")


class _NcmcsuXEqStatus2TSTSignal_Type(Integer32):
    """Custom type ncmcsuXEqStatus2TSTSignal based on Integer32"""
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


_NcmcsuXEqStatus2TSTSignal_Type.__name__ = "Integer32"
_NcmcsuXEqStatus2TSTSignal_Object = MibTableColumn
ncmcsuXEqStatus2TSTSignal = _NcmcsuXEqStatus2TSTSignal_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3025, 6015, 1, 46),
    _NcmcsuXEqStatus2TSTSignal_Type()
)
ncmcsuXEqStatus2TSTSignal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmcsuXEqStatus2TSTSignal.setStatus("mandatory")


class _NcmcsuTstRstNearRLBTstFail_Type(Integer32):
    """Custom type ncmcsuTstRstNearRLBTstFail based on Integer32"""
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


_NcmcsuTstRstNearRLBTstFail_Type.__name__ = "Integer32"
_NcmcsuTstRstNearRLBTstFail_Object = MibTableColumn
ncmcsuTstRstNearRLBTstFail = _NcmcsuTstRstNearRLBTstFail_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3025, 6015, 1, 47),
    _NcmcsuTstRstNearRLBTstFail_Type()
)
ncmcsuTstRstNearRLBTstFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmcsuTstRstNearRLBTstFail.setStatus("mandatory")


class _NcmcsuTstRstNearPLBTstFail_Type(Integer32):
    """Custom type ncmcsuTstRstNearPLBTstFail based on Integer32"""
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


_NcmcsuTstRstNearPLBTstFail_Type.__name__ = "Integer32"
_NcmcsuTstRstNearPLBTstFail_Object = MibTableColumn
ncmcsuTstRstNearPLBTstFail = _NcmcsuTstRstNearPLBTstFail_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3025, 6015, 1, 48),
    _NcmcsuTstRstNearPLBTstFail_Type()
)
ncmcsuTstRstNearPLBTstFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmcsuTstRstNearPLBTstFail.setStatus("mandatory")
_NcmcsuMiscellaneousTable_Object = MibTable
ncmcsuMiscellaneousTable = _NcmcsuMiscellaneousTable_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3025, 6016)
)
if mibBuilder.loadTexts:
    ncmcsuMiscellaneousTable.setStatus("mandatory")
_NcmcsuMiscellaneousEntry_Object = MibTableRow
ncmcsuMiscellaneousEntry = _NcmcsuMiscellaneousEntry_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3025, 6016, 1)
)
ncmcsuMiscellaneousEntry.setIndexNames(
    (0, "VERILINK-ENTERPRISE-CSUNCM-MIB", "ncmcsuNIDMiscellaneousIndex"),
    (0, "VERILINK-ENTERPRISE-CSUNCM-MIB", "ncmcsuMiscellaneousIndex"),
)
if mibBuilder.loadTexts:
    ncmcsuMiscellaneousEntry.setStatus("mandatory")
_NcmcsuNIDMiscellaneousIndex_Type = Integer32
_NcmcsuNIDMiscellaneousIndex_Object = MibTableColumn
ncmcsuNIDMiscellaneousIndex = _NcmcsuNIDMiscellaneousIndex_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3025, 6016, 1, 1),
    _NcmcsuNIDMiscellaneousIndex_Type()
)
ncmcsuNIDMiscellaneousIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmcsuNIDMiscellaneousIndex.setStatus("mandatory")
_NcmcsuMiscellaneousIndex_Type = Integer32
_NcmcsuMiscellaneousIndex_Object = MibTableColumn
ncmcsuMiscellaneousIndex = _NcmcsuMiscellaneousIndex_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3025, 6016, 1, 2),
    _NcmcsuMiscellaneousIndex_Type()
)
ncmcsuMiscellaneousIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmcsuMiscellaneousIndex.setStatus("mandatory")
_NcmcsuResetESFErrCounter_Type = Integer32
_NcmcsuResetESFErrCounter_Object = MibTableColumn
ncmcsuResetESFErrCounter = _NcmcsuResetESFErrCounter_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3025, 6016, 1, 3),
    _NcmcsuResetESFErrCounter_Type()
)
ncmcsuResetESFErrCounter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ncmcsuResetESFErrCounter.setStatus("mandatory")
_NcmcsuRetrieveNetESFErrCounter_Type = Integer32
_NcmcsuRetrieveNetESFErrCounter_Object = MibTableColumn
ncmcsuRetrieveNetESFErrCounter = _NcmcsuRetrieveNetESFErrCounter_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3025, 6016, 1, 4),
    _NcmcsuRetrieveNetESFErrCounter_Type()
)
ncmcsuRetrieveNetESFErrCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmcsuRetrieveNetESFErrCounter.setStatus("mandatory")
_NcmcsuRetrieveEqESFErrCounter_Type = Integer32
_NcmcsuRetrieveEqESFErrCounter_Object = MibTableColumn
ncmcsuRetrieveEqESFErrCounter = _NcmcsuRetrieveEqESFErrCounter_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3025, 6016, 1, 5),
    _NcmcsuRetrieveEqESFErrCounter_Type()
)
ncmcsuRetrieveEqESFErrCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmcsuRetrieveEqESFErrCounter.setStatus("mandatory")


class _NcmcsuSendBOPmessage_Type(Integer32):
    """Custom type ncmcsuSendBOPmessage based on Integer32"""
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
        *(("llb-activate", 3),
          ("llb-deactivate", 4),
          ("plb-activate", 1),
          ("plb-deactivate", 2))
    )


_NcmcsuSendBOPmessage_Type.__name__ = "Integer32"
_NcmcsuSendBOPmessage_Object = MibTableColumn
ncmcsuSendBOPmessage = _NcmcsuSendBOPmessage_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3025, 6016, 1, 6),
    _NcmcsuSendBOPmessage_Type()
)
ncmcsuSendBOPmessage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ncmcsuSendBOPmessage.setStatus("mandatory")
_NcmcsuResetNetEqBERAlarm_Type = Integer32
_NcmcsuResetNetEqBERAlarm_Object = MibTableColumn
ncmcsuResetNetEqBERAlarm = _NcmcsuResetNetEqBERAlarm_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3025, 6016, 1, 7),
    _NcmcsuResetNetEqBERAlarm_Type()
)
ncmcsuResetNetEqBERAlarm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ncmcsuResetNetEqBERAlarm.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "VERILINK-ENTERPRISE-CSUNCM-MIB",
    **{"ncmcsuMainConfigTable": ncmcsuMainConfigTable,
       "ncmcsuMainConfigEntry": ncmcsuMainConfigEntry,
       "ncmcsuNIDMainConfigIndex": ncmcsuNIDMainConfigIndex,
       "ncmcsuMainLineIndex": ncmcsuMainLineIndex,
       "ncmcsuFormat": ncmcsuFormat,
       "ncmcsuLineCode": ncmcsuLineCode,
       "ncmcsuEQCableLength": ncmcsuEQCableLength,
       "ncmcsuTiming": ncmcsuTiming,
       "ncmdsudatabus": ncmdsudatabus,
       "ncmcsuNetLineBuildOut": ncmcsuNetLineBuildOut,
       "ncmcsuValidIntervals": ncmcsuValidIntervals,
       "ncmcsuCurrentIntervalSec": ncmcsuCurrentIntervalSec,
       "ncmcsuJitterBuf": ncmcsuJitterBuf,
       "ncmcsuTestSigCfgEnable": ncmcsuTestSigCfgEnable,
       "ncmcsuTestSigCfgFrameSignal": ncmcsuTestSigCfgFrameSignal,
       "ncmcsuRLBTimeoutIndex": ncmcsuRLBTimeoutIndex,
       "ncmcsuCfgRptSendPRM": ncmcsuCfgRptSendPRM,
       "ncmcsuCfgRptPollFarEnd": ncmcsuCfgRptPollFarEnd,
       "ncmcsuCfgRptDataLinkUnsolicit": ncmcsuCfgRptDataLinkUnsolicit,
       "ncmcsuCfgRptAlmReporting": ncmcsuCfgRptAlmReporting,
       "ncmcsuCfgRptPRMType": ncmcsuCfgRptPRMType,
       "ncmcsuCfgCodeRegenCRC": ncmcsuCfgCodeRegenCRC,
       "ncmcsuCfgCodeXYellowAlarm": ncmcsuCfgCodeXYellowAlarm,
       "ncmcsuCfgCodeEQFIFO": ncmcsuCfgCodeEQFIFO,
       "ncmcsuCfgCodeNETFIFO": ncmcsuCfgCodeNETFIFO,
       "ncmcsuCfgCodeTranMode": ncmcsuCfgCodeTranMode,
       "ncmcsuCfgCodeSend1sLnkIdle": ncmcsuCfgCodeSend1sLnkIdle,
       "ncmcsuCfgAlmSelfTest": ncmcsuCfgAlmSelfTest,
       "ncmcsuCfgAlmEnableTestState": ncmcsuCfgAlmEnableTestState,
       "ncmcsuCfgAlmUnframedMode": ncmcsuCfgAlmUnframedMode,
       "ncmcsuCfgAlmOnEqLoop": ncmcsuCfgAlmOnEqLoop,
       "ncmcsuCfgAlmOnNetLoop": ncmcsuCfgAlmOnNetLoop,
       "ncmcsuCfgAlmOnPowerUpLoop": ncmcsuCfgAlmOnPowerUpLoop,
       "ncmcsuCfgLoopRespLLB": ncmcsuCfgLoopRespLLB,
       "ncmcsuCfgLoopRespPLB": ncmcsuCfgLoopRespPLB,
       "ncmcsuCfgLoopRespELB": ncmcsuCfgLoopRespELB,
       "ncmcsuCfgLoopRespRLB": ncmcsuCfgLoopRespRLB,
       "ncmcsuCfgLoopRespLLBTONE": ncmcsuCfgLoopRespLLBTONE,
       "ncmcsuCfgLoopRespPLBTONE": ncmcsuCfgLoopRespPLBTONE,
       "ncmcsuCfgSendReceiveInBandCode": ncmcsuCfgSendReceiveInBandCode,
       "ncmcsuEnhanceConfigTable": ncmcsuEnhanceConfigTable,
       "ncmcsuEnhanceConfigEntry": ncmcsuEnhanceConfigEntry,
       "ncmcsuNIDEnhanceIndex": ncmcsuNIDEnhanceIndex,
       "ncmcsuEnhanceLineIndex": ncmcsuEnhanceLineIndex,
       "ncmcsuNetworkKeepAlive": ncmcsuNetworkKeepAlive,
       "ncmcsuAlarmSetDelay": ncmcsuAlarmSetDelay,
       "ncmcsuAlarmClearDelay": ncmcsuAlarmClearDelay,
       "ncmcsuAlarmEnable": ncmcsuAlarmEnable,
       "ncmcsuNetDensityEnforcement": ncmcsuNetDensityEnforcement,
       "ncmcsuLoopback": ncmcsuLoopback,
       "ncmcsuTestPattern": ncmcsuTestPattern,
       "ncmcsuResetPerfReg": ncmcsuResetPerfReg,
       "ncmcsuTestErrorCounter": ncmcsuTestErrorCounter,
       "ncmcsuTestSecondsRemain": ncmcsuTestSecondsRemain,
       "ncmcsuTestTimeSeconds": ncmcsuTestTimeSeconds,
       "ncmcsuNetLOFCIndexTime": ncmcsuNetLOFCIndexTime,
       "ncmcsuChannelMask": ncmcsuChannelMask,
       "ncmcsuApplication": ncmcsuApplication,
       "ncmcsuTestIntervalIndex": ncmcsuTestIntervalIndex,
       "ncmcsuElementStatusOneTable": ncmcsuElementStatusOneTable,
       "ncmcsuElementStatusOneEntry": ncmcsuElementStatusOneEntry,
       "ncmcsuNIDElementStatusIndex1": ncmcsuNIDElementStatusIndex1,
       "ncmcsuElementStatusIndex1": ncmcsuElementStatusIndex1,
       "ncmcsuExcessiveError": ncmcsuExcessiveError,
       "ncmcsuOutOfFrame": ncmcsuOutOfFrame,
       "ncmcsuNetLossOfSignal": ncmcsuNetLossOfSignal,
       "ncmcsuElementStatusTwoTable": ncmcsuElementStatusTwoTable,
       "ncmcsuElementStatusTwoEntry": ncmcsuElementStatusTwoEntry,
       "ncmcsuNIDElementStatusIndex2": ncmcsuNIDElementStatusIndex2,
       "ncmcsuElementStatusIndex2": ncmcsuElementStatusIndex2,
       "ncmcsuStatus": ncmcsuStatus,
       "ncmcsuAddress1": ncmcsuAddress1,
       "ncmcsuAddress2": ncmcsuAddress2,
       "ncmcsuLLBELBPLB": ncmcsuLLBELBPLB,
       "ncmcsuThresholdIntervalTable": ncmcsuThresholdIntervalTable,
       "ncmcsuThresholdIntervalEntry": ncmcsuThresholdIntervalEntry,
       "ncmcsuNIDThresholdIntervalIndex": ncmcsuNIDThresholdIntervalIndex,
       "ncmcsuThresholdIntervalIndex": ncmcsuThresholdIntervalIndex,
       "ncmcsuBERThreshold": ncmcsuBERThreshold,
       "ncmcsubpvSecThreshold": ncmcsubpvSecThreshold,
       "ncmcsubpvSecInterval": ncmcsubpvSecInterval,
       "ncmcsuESThreshold": ncmcsuESThreshold,
       "ncmcsuESInterval": ncmcsuESInterval,
       "ncmcsuUASThreshold": ncmcsuUASThreshold,
       "ncmcsuUASInterval": ncmcsuUASInterval,
       "ncmcsuCurrentOneTable": ncmcsuCurrentOneTable,
       "ncmcsuCurrentOneEntry": ncmcsuCurrentOneEntry,
       "ncmcsuNIDCurrentIndex1": ncmcsuNIDCurrentIndex1,
       "ncmcsuCurrentIndex1": ncmcsuCurrentIndex1,
       "ncmcsuCurrentEndType1": ncmcsuCurrentEndType1,
       "ncmcsuCurrentESs": ncmcsuCurrentESs,
       "ncmcsuCurrentSESs": ncmcsuCurrentSESs,
       "ncmcsuCurrentSEFSs": ncmcsuCurrentSEFSs,
       "ncmcsuCurrentUASs": ncmcsuCurrentUASs,
       "ncmcsuCurrentCSSs": ncmcsuCurrentCSSs,
       "ncmcsuCurrentPCVs": ncmcsuCurrentPCVs,
       "ncmcsuCurrentLESs": ncmcsuCurrentLESs,
       "ncmcsuCurrentBESs": ncmcsuCurrentBESs,
       "ncmcsuCurrentDMs": ncmcsuCurrentDMs,
       "ncmcsuCurrentLCVs": ncmcsuCurrentLCVs,
       "ncmcsuIntervalOneTable": ncmcsuIntervalOneTable,
       "ncmcsuIntervalOneEntry": ncmcsuIntervalOneEntry,
       "ncmcsuNIDIntervalIndex1": ncmcsuNIDIntervalIndex1,
       "ncmcsuIntervalIndex1": ncmcsuIntervalIndex1,
       "ncmcsuIntervalEndType1": ncmcsuIntervalEndType1,
       "ncmcsuIntervalNumber1": ncmcsuIntervalNumber1,
       "ncmcsuIntervalESs": ncmcsuIntervalESs,
       "ncmcsuIntervalSESs": ncmcsuIntervalSESs,
       "ncmcsuIntervalSEFSs": ncmcsuIntervalSEFSs,
       "ncmcsuIntervalUASs": ncmcsuIntervalUASs,
       "ncmcsuIntervalCSSs": ncmcsuIntervalCSSs,
       "ncmcsuIntervalPCVs": ncmcsuIntervalPCVs,
       "ncmcsuIntervalLESs": ncmcsuIntervalLESs,
       "ncmcsuIntervalBESs": ncmcsuIntervalBESs,
       "ncmcsuIntervalDMs": ncmcsuIntervalDMs,
       "ncmcsuIntervalLCVs": ncmcsuIntervalLCVs,
       "ncmcsuTotalOneTable": ncmcsuTotalOneTable,
       "ncmcsuTotalOneEntry": ncmcsuTotalOneEntry,
       "ncmcsuNIDTotalIndex1": ncmcsuNIDTotalIndex1,
       "ncmcsuTotalIndex1": ncmcsuTotalIndex1,
       "ncmcsuTotalEndType1": ncmcsuTotalEndType1,
       "ncmcsuTotalESs": ncmcsuTotalESs,
       "ncmcsuTotalSESs": ncmcsuTotalSESs,
       "ncmcsuTotalSEFSs": ncmcsuTotalSEFSs,
       "ncmcsuTotalUASs": ncmcsuTotalUASs,
       "ncmcsuTotalCSSs": ncmcsuTotalCSSs,
       "ncmcsuTotalPCVs": ncmcsuTotalPCVs,
       "ncmcsuTotalLESs": ncmcsuTotalLESs,
       "ncmcsuTotalBESs": ncmcsuTotalBESs,
       "ncmcsuTotalDMs": ncmcsuTotalDMs,
       "ncmcsuTotalLCVs": ncmcsuTotalLCVs,
       "ncmcsuEnhancedCurrentTable": ncmcsuEnhancedCurrentTable,
       "ncmcsuEnhancedCurrentEntry": ncmcsuEnhancedCurrentEntry,
       "ncmcsuNIDEnhancedCurrentIndex": ncmcsuNIDEnhancedCurrentIndex,
       "ncmcsuEnhancedCurrentIndex": ncmcsuEnhancedCurrentIndex,
       "ncmcsuEnhancedCurrentEndType": ncmcsuEnhancedCurrentEndType,
       "ncmcsuEnhancedCurrentESs": ncmcsuEnhancedCurrentESs,
       "ncmcsuEnhancedCurrentSESs": ncmcsuEnhancedCurrentSESs,
       "ncmcsuEnhancedCurrentUASs": ncmcsuEnhancedCurrentUASs,
       "ncmcsuEnhancedCurrentCSSs": ncmcsuEnhancedCurrentCSSs,
       "ncmcsuEnhancedCurrentBESs": ncmcsuEnhancedCurrentBESs,
       "ncmcsuEnhancedCurrentLOFC": ncmcsuEnhancedCurrentLOFC,
       "ncmcsuEnhancedIntervalTable": ncmcsuEnhancedIntervalTable,
       "ncmcsuEnhancedIntervalEntry": ncmcsuEnhancedIntervalEntry,
       "ncmcsuNIDEnhancedIntervalIndex": ncmcsuNIDEnhancedIntervalIndex,
       "ncmcsuEnhancedIntervalIndex": ncmcsuEnhancedIntervalIndex,
       "ncmcsuEnhancedIntervalEndType": ncmcsuEnhancedIntervalEndType,
       "ncmcsuEnhancedIntervalNumber": ncmcsuEnhancedIntervalNumber,
       "ncmcsuEnhancedIntervalESs": ncmcsuEnhancedIntervalESs,
       "ncmcsuEnhancedIntervalSESs": ncmcsuEnhancedIntervalSESs,
       "ncmcsuEnhancedIntervalUASs": ncmcsuEnhancedIntervalUASs,
       "ncmcsuEnhancedIntervalCSSs": ncmcsuEnhancedIntervalCSSs,
       "ncmcsuEnhancedIntervalBESs": ncmcsuEnhancedIntervalBESs,
       "ncmcsuEnhancedIntervalLOFC": ncmcsuEnhancedIntervalLOFC,
       "ncmcsuEnhancedTotalTable": ncmcsuEnhancedTotalTable,
       "ncmcsuEnhancedTotalEntry": ncmcsuEnhancedTotalEntry,
       "ncmcsuNIDEnhancedTotalIndex": ncmcsuNIDEnhancedTotalIndex,
       "ncmcsuEnhancedTotalIndex": ncmcsuEnhancedTotalIndex,
       "ncmcsuEnhancedTotalEndType": ncmcsuEnhancedTotalEndType,
       "ncmcsuEnhancedTotalESs": ncmcsuEnhancedTotalESs,
       "ncmcsuEnhancedTotalSESs": ncmcsuEnhancedTotalSESs,
       "ncmcsuEnhancedTotalUASs": ncmcsuEnhancedTotalUASs,
       "ncmcsuEnhancedTotalCSSs": ncmcsuEnhancedTotalCSSs,
       "ncmcsuEnhancedTotalBESs": ncmcsuEnhancedTotalBESs,
       "ncmcsuEnhancedTotalLOFC": ncmcsuEnhancedTotalLOFC,
       "ncmcsuCurrentTable": ncmcsuCurrentTable,
       "ncmcsuCurrentEntry": ncmcsuCurrentEntry,
       "ncmcsuNIDCurrentIndex": ncmcsuNIDCurrentIndex,
       "ncmcsuCurrentIndex": ncmcsuCurrentIndex,
       "ncmcsuCurrentEndType": ncmcsuCurrentEndType,
       "ncmcsuCurrentNETOOFS": ncmcsuCurrentNETOOFS,
       "ncmcsuCurrentNETLOSS": ncmcsuCurrentNETLOSS,
       "ncmcsuCurrentNETAISS": ncmcsuCurrentNETAISS,
       "ncmcsuCurrentNETBERS": ncmcsuCurrentNETBERS,
       "ncmcsuCurrentNETYELS": ncmcsuCurrentNETYELS,
       "ncmcsuCurrentNETLOFS": ncmcsuCurrentNETLOFS,
       "ncmcsuCurrentNETESL": ncmcsuCurrentNETESL,
       "ncmcsuCurrentNETSEFS": ncmcsuCurrentNETSEFS,
       "ncmcsuCurrentEQOOFS": ncmcsuCurrentEQOOFS,
       "ncmcsuCurrentEQDTED": ncmcsuCurrentEQDTED,
       "ncmcsuCurrentEQDBER": ncmcsuCurrentEQDBER,
       "ncmcsuCurrentEQES": ncmcsuCurrentEQES,
       "ncmcsuCurrentEQUAS": ncmcsuCurrentEQUAS,
       "ncmcsuCurrentEQESL": ncmcsuCurrentEQESL,
       "ncmcsuTotalTable": ncmcsuTotalTable,
       "ncmcsuTotalEntry": ncmcsuTotalEntry,
       "ncmcsuNIDTotalIndex": ncmcsuNIDTotalIndex,
       "ncmcsuTotalIndex": ncmcsuTotalIndex,
       "ncmcsuTotalEndType": ncmcsuTotalEndType,
       "ncmcsuTotalNETOOFS": ncmcsuTotalNETOOFS,
       "ncmcsuTotalNETLOSS": ncmcsuTotalNETLOSS,
       "ncmcsuTotalNETAISS": ncmcsuTotalNETAISS,
       "ncmcsuTotalNETBERS": ncmcsuTotalNETBERS,
       "ncmcsuTotalNETYELS": ncmcsuTotalNETYELS,
       "ncmcsuTotalNETLOFS": ncmcsuTotalNETLOFS,
       "ncmcsuTotalNETESL": ncmcsuTotalNETESL,
       "ncmcsuTotalNETSEFS": ncmcsuTotalNETSEFS,
       "ncmcsuTotalEQOOFS": ncmcsuTotalEQOOFS,
       "ncmcsuTotalEQDTED": ncmcsuTotalEQDTED,
       "ncmcsuTotalEQDBER": ncmcsuTotalEQDBER,
       "ncmcsuTotalEQES": ncmcsuTotalEQES,
       "ncmcsuTotalEQUAS": ncmcsuTotalEQUAS,
       "ncmcsuTotalEQESL": ncmcsuTotalEQESL,
       "ncmcsuIntervalTable": ncmcsuIntervalTable,
       "ncmcsuIntervalEntry": ncmcsuIntervalEntry,
       "ncmcsuNIDIntervalIndex": ncmcsuNIDIntervalIndex,
       "ncmcsuIntervalIndex": ncmcsuIntervalIndex,
       "ncmcsuIntervalEndType": ncmcsuIntervalEndType,
       "ncmcsuIntervalNumber": ncmcsuIntervalNumber,
       "ncmcsuIntervalNETOOFS": ncmcsuIntervalNETOOFS,
       "ncmcsuIntervalNETLOSS": ncmcsuIntervalNETLOSS,
       "ncmcsuIntervalNETAISS": ncmcsuIntervalNETAISS,
       "ncmcsuIntervalNETBERS": ncmcsuIntervalNETBERS,
       "ncmcsuIntervalNETYELS": ncmcsuIntervalNETYELS,
       "ncmcsuIntervalNETLOFS": ncmcsuIntervalNETLOFS,
       "ncmcsuIntervalNETESL": ncmcsuIntervalNETESL,
       "ncmcsuIntervalNETSEFS": ncmcsuIntervalNETSEFS,
       "ncmcsuIntervalEQOOFS": ncmcsuIntervalEQOOFS,
       "ncmcsuIntervalEQDTED": ncmcsuIntervalEQDTED,
       "ncmcsuIntervalEQDBER": ncmcsuIntervalEQDBER,
       "ncmcsuIntervalEQES": ncmcsuIntervalEQES,
       "ncmcsuIntervalEQUAS": ncmcsuIntervalEQUAS,
       "ncmcsuIntervalEQESL": ncmcsuIntervalEQESL,
       "ncmcsucommonTable": ncmcsucommonTable,
       "ncmcsucommonEntry": ncmcsucommonEntry,
       "ncmcsuNIDcommonIndex": ncmcsuNIDcommonIndex,
       "ncmcsucommonIndex": ncmcsucommonIndex,
       "ncmcsucommonEndType": ncmcsucommonEndType,
       "ncmValidInterval": ncmValidInterval,
       "ncmCurrentIntervalSeconds": ncmCurrentIntervalSeconds,
       "ncmResetPerformanceReg": ncmResetPerformanceReg,
       "ncmcsuRetrievalStatusOneTable": ncmcsuRetrievalStatusOneTable,
       "ncmcsuRetrievalStatusOneEntry": ncmcsuRetrievalStatusOneEntry,
       "ncmcsuNIDRetrievalStatusIndex1": ncmcsuNIDRetrievalStatusIndex1,
       "ncmcsuRetrievalStatusIndex1": ncmcsuRetrievalStatusIndex1,
       "ncmcsuNearAlmBERthresexcd": ncmcsuNearAlmBERthresexcd,
       "ncmcsuNearAlmESthresexcd": ncmcsuNearAlmESthresexcd,
       "ncmcsuNearAlmUASthresexcd": ncmcsuNearAlmUASthresexcd,
       "ncmcsuNearAlmLLBPLB": ncmcsuNearAlmLLBPLB,
       "ncmcsuFarAlmBERthresexcd": ncmcsuFarAlmBERthresexcd,
       "ncmcsuFarAlmESthresexcd": ncmcsuFarAlmESthresexcd,
       "ncmcsuFarAlmUASthresexcd": ncmcsuFarAlmUASthresexcd,
       "ncmcsuFarAlmLLBDLB": ncmcsuFarAlmLLBDLB,
       "ncmcsuFarCsuAbsent": ncmcsuFarCsuAbsent,
       "ncmcsuEqStatusLowDensity": ncmcsuEqStatusLowDensity,
       "ncmcsuEqStatusOOF": ncmcsuEqStatusOOF,
       "ncmcsuEqStatusCRCError": ncmcsuEqStatusCRCError,
       "ncmcsuEqStatusBPV": ncmcsuEqStatusBPV,
       "ncmcsuEqStatusPLB": ncmcsuEqStatusPLB,
       "ncmcsuEqStatusELBRLB": ncmcsuEqStatusELBRLB,
       "ncmcsuNetStatusPulses": ncmcsuNetStatusPulses,
       "ncmcsuNetStatusOOF": ncmcsuNetStatusOOF,
       "ncmcsuNetStatusCRCError": ncmcsuNetStatusCRCError,
       "ncmcsuNetStatusBPV": ncmcsuNetStatusBPV,
       "ncmcsuNetStatusLLB": ncmcsuNetStatusLLB,
       "ncmcsuXNetStatus1BERthresexcd": ncmcsuXNetStatus1BERthresexcd,
       "ncmcsuXNetStatus1ES1thresexcd": ncmcsuXNetStatus1ES1thresexcd,
       "ncmcsuXNetStatus1ESthresexcd": ncmcsuXNetStatus1ESthresexcd,
       "ncmcsuXNetStatus1UASthresexcd": ncmcsuXNetStatus1UASthresexcd,
       "ncmcsuXNetStatus1LLB": ncmcsuXNetStatus1LLB,
       "ncmcsuXNetStatus1PLB": ncmcsuXNetStatus1PLB,
       "ncmcsuXNetStatus1LOS": ncmcsuXNetStatus1LOS,
       "ncmcsuXNetStatus1YEL": ncmcsuXNetStatus1YEL,
       "ncmcsuXNetStatus2LOF": ncmcsuXNetStatus2LOF,
       "ncmcsuXNetStatus2AIS": ncmcsuXNetStatus2AIS,
       "ncmcsuXNetStatus2TSTProgress": ncmcsuXNetStatus2TSTProgress,
       "ncmcsuXNetStatus2PowerAFail": ncmcsuXNetStatus2PowerAFail,
       "ncmcsuXNetStatus2PowerBFail": ncmcsuXNetStatus2PowerBFail,
       "ncmcsuXEqStatus1BERthresexcd": ncmcsuXEqStatus1BERthresexcd,
       "ncmcsuXEqStatus1ES1thresexcd": ncmcsuXEqStatus1ES1thresexcd,
       "ncmcsuXEqStatus1ESthresexcd": ncmcsuXEqStatus1ESthresexcd,
       "ncmcsuXEqStatus1UASthresexcd": ncmcsuXEqStatus1UASthresexcd,
       "ncmcsuXEqStatus1ELB": ncmcsuXEqStatus1ELB,
       "ncmcsuXEqStatus1RLB": ncmcsuXEqStatus1RLB,
       "ncmcsuXEqStatus1LOS": ncmcsuXEqStatus1LOS,
       "ncmcsuXEqStatus1YEL": ncmcsuXEqStatus1YEL,
       "ncmcsuXEqStatus2LOF": ncmcsuXEqStatus2LOF,
       "ncmcsuXEqStatus2AIS": ncmcsuXEqStatus2AIS,
       "ncmcsuXEqStatus2TSTSignal": ncmcsuXEqStatus2TSTSignal,
       "ncmcsuTstRstNearRLBTstFail": ncmcsuTstRstNearRLBTstFail,
       "ncmcsuTstRstNearPLBTstFail": ncmcsuTstRstNearPLBTstFail,
       "ncmcsuMiscellaneousTable": ncmcsuMiscellaneousTable,
       "ncmcsuMiscellaneousEntry": ncmcsuMiscellaneousEntry,
       "ncmcsuNIDMiscellaneousIndex": ncmcsuNIDMiscellaneousIndex,
       "ncmcsuMiscellaneousIndex": ncmcsuMiscellaneousIndex,
       "ncmcsuResetESFErrCounter": ncmcsuResetESFErrCounter,
       "ncmcsuRetrieveNetESFErrCounter": ncmcsuRetrieveNetESFErrCounter,
       "ncmcsuRetrieveEqESFErrCounter": ncmcsuRetrieveEqESFErrCounter,
       "ncmcsuSendBOPmessage": ncmcsuSendBOPmessage,
       "ncmcsuResetNetEqBERAlarm": ncmcsuResetNetEqBERAlarm}
)
