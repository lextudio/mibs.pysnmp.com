# SNMP MIB module (VERILINK-ENTERPRISE-NCMIDCSU-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/VERILINK-ENTERPRISE-NCMIDCSU-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:12:15 2024
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

(ncm_idcsu,) = mibBuilder.importSymbols(
    "VERILINK-ENTERPRISE-NCMALARM-MIB",
    "ncm-idcsu")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_NcmidcsuConfigTable_Object = MibTable
ncmidcsuConfigTable = _NcmidcsuConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3027, 10000)
)
if mibBuilder.loadTexts:
    ncmidcsuConfigTable.setStatus("mandatory")
_NcmidcsuConfigEntry_Object = MibTableRow
ncmidcsuConfigEntry = _NcmidcsuConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3027, 10000, 1)
)
ncmidcsuConfigEntry.setIndexNames(
    (0, "VERILINK-ENTERPRISE-NCMIDCSU-MIB", "ncmidcsucfgNIDIndex"),
    (0, "VERILINK-ENTERPRISE-NCMIDCSU-MIB", "ncmidcsuLineIndex"),
)
if mibBuilder.loadTexts:
    ncmidcsuConfigEntry.setStatus("mandatory")


class _NcmidcsucfgNIDIndex_Type(Integer32):
    """Custom type ncmidcsucfgNIDIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_NcmidcsucfgNIDIndex_Type.__name__ = "Integer32"
_NcmidcsucfgNIDIndex_Object = MibTableColumn
ncmidcsucfgNIDIndex = _NcmidcsucfgNIDIndex_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3027, 10000, 1, 1),
    _NcmidcsucfgNIDIndex_Type()
)
ncmidcsucfgNIDIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmidcsucfgNIDIndex.setStatus("mandatory")
_NcmidcsuLineIndex_Type = Integer32
_NcmidcsuLineIndex_Object = MibTableColumn
ncmidcsuLineIndex = _NcmidcsuLineIndex_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3027, 10000, 1, 2),
    _NcmidcsuLineIndex_Type()
)
ncmidcsuLineIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmidcsuLineIndex.setStatus("mandatory")


class _NcmidcsuNetLineBuildOut_Type(Integer32):
    """Custom type ncmidcsuNetLineBuildOut based on Integer32"""
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


_NcmidcsuNetLineBuildOut_Type.__name__ = "Integer32"
_NcmidcsuNetLineBuildOut_Object = MibTableColumn
ncmidcsuNetLineBuildOut = _NcmidcsuNetLineBuildOut_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3027, 10000, 1, 3),
    _NcmidcsuNetLineBuildOut_Type()
)
ncmidcsuNetLineBuildOut.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ncmidcsuNetLineBuildOut.setStatus("mandatory")


class _NcmidcsuNetworkKeepAlive_Type(Integer32):
    """Custom type ncmidcsuNetworkKeepAlive based on Integer32"""
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
        *(("ais", 3),
          ("framed-all-ones", 4),
          ("loop", 2),
          ("none", 1))
    )


_NcmidcsuNetworkKeepAlive_Type.__name__ = "Integer32"
_NcmidcsuNetworkKeepAlive_Object = MibTableColumn
ncmidcsuNetworkKeepAlive = _NcmidcsuNetworkKeepAlive_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3027, 10000, 1, 4),
    _NcmidcsuNetworkKeepAlive_Type()
)
ncmidcsuNetworkKeepAlive.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ncmidcsuNetworkKeepAlive.setStatus("mandatory")


class _NcmidcsuExcessiveError_Type(Integer32):
    """Custom type ncmidcsuExcessiveError based on Integer32"""
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


_NcmidcsuExcessiveError_Type.__name__ = "Integer32"
_NcmidcsuExcessiveError_Object = MibTableColumn
ncmidcsuExcessiveError = _NcmidcsuExcessiveError_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3027, 10000, 1, 5),
    _NcmidcsuExcessiveError_Type()
)
ncmidcsuExcessiveError.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ncmidcsuExcessiveError.setStatus("mandatory")


class _NcmidcsuOutOfFrame_Type(Integer32):
    """Custom type ncmidcsuOutOfFrame based on Integer32"""
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


_NcmidcsuOutOfFrame_Type.__name__ = "Integer32"
_NcmidcsuOutOfFrame_Object = MibTableColumn
ncmidcsuOutOfFrame = _NcmidcsuOutOfFrame_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3027, 10000, 1, 6),
    _NcmidcsuOutOfFrame_Type()
)
ncmidcsuOutOfFrame.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ncmidcsuOutOfFrame.setStatus("mandatory")


class _NcmidcsuFormat_Type(Integer32):
    """Custom type ncmidcsuFormat based on Integer32"""
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


_NcmidcsuFormat_Type.__name__ = "Integer32"
_NcmidcsuFormat_Object = MibTableColumn
ncmidcsuFormat = _NcmidcsuFormat_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3027, 10000, 1, 7),
    _NcmidcsuFormat_Type()
)
ncmidcsuFormat.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ncmidcsuFormat.setStatus("mandatory")


class _NcmidcsuNetDensityEnforcement_Type(Integer32):
    """Custom type ncmidcsuNetDensityEnforcement based on Integer32"""
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


_NcmidcsuNetDensityEnforcement_Type.__name__ = "Integer32"
_NcmidcsuNetDensityEnforcement_Object = MibTableColumn
ncmidcsuNetDensityEnforcement = _NcmidcsuNetDensityEnforcement_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3027, 10000, 1, 8),
    _NcmidcsuNetDensityEnforcement_Type()
)
ncmidcsuNetDensityEnforcement.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ncmidcsuNetDensityEnforcement.setStatus("mandatory")
_NcmidcsuNetLossOfSignal_Type = Integer32
_NcmidcsuNetLossOfSignal_Object = MibTableColumn
ncmidcsuNetLossOfSignal = _NcmidcsuNetLossOfSignal_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3027, 10000, 1, 9),
    _NcmidcsuNetLossOfSignal_Type()
)
ncmidcsuNetLossOfSignal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmidcsuNetLossOfSignal.setStatus("mandatory")


class _NcmidcsuJitterBuf_Type(Integer32):
    """Custom type ncmidcsuJitterBuf based on Integer32"""
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


_NcmidcsuJitterBuf_Type.__name__ = "Integer32"
_NcmidcsuJitterBuf_Object = MibTableColumn
ncmidcsuJitterBuf = _NcmidcsuJitterBuf_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3027, 10000, 1, 10),
    _NcmidcsuJitterBuf_Type()
)
ncmidcsuJitterBuf.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ncmidcsuJitterBuf.setStatus("mandatory")


class _NcmidcsuTestSigCfgEnable_Type(Integer32):
    """Custom type ncmidcsuTestSigCfgEnable based on Integer32"""
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


_NcmidcsuTestSigCfgEnable_Type.__name__ = "Integer32"
_NcmidcsuTestSigCfgEnable_Object = MibTableColumn
ncmidcsuTestSigCfgEnable = _NcmidcsuTestSigCfgEnable_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3027, 10000, 1, 11),
    _NcmidcsuTestSigCfgEnable_Type()
)
ncmidcsuTestSigCfgEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ncmidcsuTestSigCfgEnable.setStatus("mandatory")


class _NcmidcsuTestSigCfgFrameSignal_Type(Integer32):
    """Custom type ncmidcsuTestSigCfgFrameSignal based on Integer32"""
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


_NcmidcsuTestSigCfgFrameSignal_Type.__name__ = "Integer32"
_NcmidcsuTestSigCfgFrameSignal_Object = MibTableColumn
ncmidcsuTestSigCfgFrameSignal = _NcmidcsuTestSigCfgFrameSignal_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3027, 10000, 1, 12),
    _NcmidcsuTestSigCfgFrameSignal_Type()
)
ncmidcsuTestSigCfgFrameSignal.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ncmidcsuTestSigCfgFrameSignal.setStatus("mandatory")


class _NcmidcsuCfgRptSendPRM_Type(Integer32):
    """Custom type ncmidcsuCfgRptSendPRM based on Integer32"""
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


_NcmidcsuCfgRptSendPRM_Type.__name__ = "Integer32"
_NcmidcsuCfgRptSendPRM_Object = MibTableColumn
ncmidcsuCfgRptSendPRM = _NcmidcsuCfgRptSendPRM_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3027, 10000, 1, 13),
    _NcmidcsuCfgRptSendPRM_Type()
)
ncmidcsuCfgRptSendPRM.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ncmidcsuCfgRptSendPRM.setStatus("mandatory")


class _NcmidcsuCfgRptPollFarEnd_Type(Integer32):
    """Custom type ncmidcsuCfgRptPollFarEnd based on Integer32"""
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


_NcmidcsuCfgRptPollFarEnd_Type.__name__ = "Integer32"
_NcmidcsuCfgRptPollFarEnd_Object = MibTableColumn
ncmidcsuCfgRptPollFarEnd = _NcmidcsuCfgRptPollFarEnd_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3027, 10000, 1, 14),
    _NcmidcsuCfgRptPollFarEnd_Type()
)
ncmidcsuCfgRptPollFarEnd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ncmidcsuCfgRptPollFarEnd.setStatus("mandatory")


class _NcmidcsuCfgRptDataLinkUnsolicit_Type(Integer32):
    """Custom type ncmidcsuCfgRptDataLinkUnsolicit based on Integer32"""
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


_NcmidcsuCfgRptDataLinkUnsolicit_Type.__name__ = "Integer32"
_NcmidcsuCfgRptDataLinkUnsolicit_Object = MibTableColumn
ncmidcsuCfgRptDataLinkUnsolicit = _NcmidcsuCfgRptDataLinkUnsolicit_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3027, 10000, 1, 15),
    _NcmidcsuCfgRptDataLinkUnsolicit_Type()
)
ncmidcsuCfgRptDataLinkUnsolicit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ncmidcsuCfgRptDataLinkUnsolicit.setStatus("mandatory")


class _NcmidcsuCfgRptAlmReporting_Type(Integer32):
    """Custom type ncmidcsuCfgRptAlmReporting based on Integer32"""
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


_NcmidcsuCfgRptAlmReporting_Type.__name__ = "Integer32"
_NcmidcsuCfgRptAlmReporting_Object = MibTableColumn
ncmidcsuCfgRptAlmReporting = _NcmidcsuCfgRptAlmReporting_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3027, 10000, 1, 16),
    _NcmidcsuCfgRptAlmReporting_Type()
)
ncmidcsuCfgRptAlmReporting.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ncmidcsuCfgRptAlmReporting.setStatus("mandatory")


class _NcmidcsuCfgRptPRMType_Type(Integer32):
    """Custom type ncmidcsuCfgRptPRMType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("tELCO", 1),
          ("uSER", 2))
    )


_NcmidcsuCfgRptPRMType_Type.__name__ = "Integer32"
_NcmidcsuCfgRptPRMType_Object = MibTableColumn
ncmidcsuCfgRptPRMType = _NcmidcsuCfgRptPRMType_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3027, 10000, 1, 17),
    _NcmidcsuCfgRptPRMType_Type()
)
ncmidcsuCfgRptPRMType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ncmidcsuCfgRptPRMType.setStatus("mandatory")


class _NcmidcsuCfgCodeRegenCRC_Type(Integer32):
    """Custom type ncmidcsuCfgCodeRegenCRC based on Integer32"""
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


_NcmidcsuCfgCodeRegenCRC_Type.__name__ = "Integer32"
_NcmidcsuCfgCodeRegenCRC_Object = MibTableColumn
ncmidcsuCfgCodeRegenCRC = _NcmidcsuCfgCodeRegenCRC_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3027, 10000, 1, 18),
    _NcmidcsuCfgCodeRegenCRC_Type()
)
ncmidcsuCfgCodeRegenCRC.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ncmidcsuCfgCodeRegenCRC.setStatus("mandatory")


class _NcmidcsuCfgCodeXYellowAlarm_Type(Integer32):
    """Custom type ncmidcsuCfgCodeXYellowAlarm based on Integer32"""
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


_NcmidcsuCfgCodeXYellowAlarm_Type.__name__ = "Integer32"
_NcmidcsuCfgCodeXYellowAlarm_Object = MibTableColumn
ncmidcsuCfgCodeXYellowAlarm = _NcmidcsuCfgCodeXYellowAlarm_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3027, 10000, 1, 19),
    _NcmidcsuCfgCodeXYellowAlarm_Type()
)
ncmidcsuCfgCodeXYellowAlarm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ncmidcsuCfgCodeXYellowAlarm.setStatus("mandatory")


class _NcmidcsuCfgCodeEQFIFO_Type(Integer32):
    """Custom type ncmidcsuCfgCodeEQFIFO based on Integer32"""
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


_NcmidcsuCfgCodeEQFIFO_Type.__name__ = "Integer32"
_NcmidcsuCfgCodeEQFIFO_Object = MibTableColumn
ncmidcsuCfgCodeEQFIFO = _NcmidcsuCfgCodeEQFIFO_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3027, 10000, 1, 20),
    _NcmidcsuCfgCodeEQFIFO_Type()
)
ncmidcsuCfgCodeEQFIFO.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ncmidcsuCfgCodeEQFIFO.setStatus("mandatory")


class _NcmidcsuCfgCodeNETFIFO_Type(Integer32):
    """Custom type ncmidcsuCfgCodeNETFIFO based on Integer32"""
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


_NcmidcsuCfgCodeNETFIFO_Type.__name__ = "Integer32"
_NcmidcsuCfgCodeNETFIFO_Object = MibTableColumn
ncmidcsuCfgCodeNETFIFO = _NcmidcsuCfgCodeNETFIFO_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3027, 10000, 1, 21),
    _NcmidcsuCfgCodeNETFIFO_Type()
)
ncmidcsuCfgCodeNETFIFO.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ncmidcsuCfgCodeNETFIFO.setStatus("mandatory")


class _NcmidcsuCfgCodeTranMode_Type(Integer32):
    """Custom type ncmidcsuCfgCodeTranMode based on Integer32"""
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


_NcmidcsuCfgCodeTranMode_Type.__name__ = "Integer32"
_NcmidcsuCfgCodeTranMode_Object = MibTableColumn
ncmidcsuCfgCodeTranMode = _NcmidcsuCfgCodeTranMode_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3027, 10000, 1, 22),
    _NcmidcsuCfgCodeTranMode_Type()
)
ncmidcsuCfgCodeTranMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ncmidcsuCfgCodeTranMode.setStatus("mandatory")


class _NcmidcsuCfgCodeSend1sLnkIdle_Type(Integer32):
    """Custom type ncmidcsuCfgCodeSend1sLnkIdle based on Integer32"""
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


_NcmidcsuCfgCodeSend1sLnkIdle_Type.__name__ = "Integer32"
_NcmidcsuCfgCodeSend1sLnkIdle_Object = MibTableColumn
ncmidcsuCfgCodeSend1sLnkIdle = _NcmidcsuCfgCodeSend1sLnkIdle_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3027, 10000, 1, 23),
    _NcmidcsuCfgCodeSend1sLnkIdle_Type()
)
ncmidcsuCfgCodeSend1sLnkIdle.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ncmidcsuCfgCodeSend1sLnkIdle.setStatus("mandatory")


class _NcmidcsuCfgAlmSelfTest_Type(Integer32):
    """Custom type ncmidcsuCfgAlmSelfTest based on Integer32"""
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


_NcmidcsuCfgAlmSelfTest_Type.__name__ = "Integer32"
_NcmidcsuCfgAlmSelfTest_Object = MibTableColumn
ncmidcsuCfgAlmSelfTest = _NcmidcsuCfgAlmSelfTest_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3027, 10000, 1, 24),
    _NcmidcsuCfgAlmSelfTest_Type()
)
ncmidcsuCfgAlmSelfTest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ncmidcsuCfgAlmSelfTest.setStatus("mandatory")


class _NcmidcsuCfgAlmEnableTestState_Type(Integer32):
    """Custom type ncmidcsuCfgAlmEnableTestState based on Integer32"""
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


_NcmidcsuCfgAlmEnableTestState_Type.__name__ = "Integer32"
_NcmidcsuCfgAlmEnableTestState_Object = MibTableColumn
ncmidcsuCfgAlmEnableTestState = _NcmidcsuCfgAlmEnableTestState_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3027, 10000, 1, 25),
    _NcmidcsuCfgAlmEnableTestState_Type()
)
ncmidcsuCfgAlmEnableTestState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ncmidcsuCfgAlmEnableTestState.setStatus("mandatory")


class _NcmidcsuCfgAlmUnframedMode_Type(Integer32):
    """Custom type ncmidcsuCfgAlmUnframedMode based on Integer32"""
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


_NcmidcsuCfgAlmUnframedMode_Type.__name__ = "Integer32"
_NcmidcsuCfgAlmUnframedMode_Object = MibTableColumn
ncmidcsuCfgAlmUnframedMode = _NcmidcsuCfgAlmUnframedMode_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3027, 10000, 1, 26),
    _NcmidcsuCfgAlmUnframedMode_Type()
)
ncmidcsuCfgAlmUnframedMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ncmidcsuCfgAlmUnframedMode.setStatus("mandatory")


class _NcmidcsuCfgAlmOnEqLoop_Type(Integer32):
    """Custom type ncmidcsuCfgAlmOnEqLoop based on Integer32"""
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


_NcmidcsuCfgAlmOnEqLoop_Type.__name__ = "Integer32"
_NcmidcsuCfgAlmOnEqLoop_Object = MibTableColumn
ncmidcsuCfgAlmOnEqLoop = _NcmidcsuCfgAlmOnEqLoop_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3027, 10000, 1, 27),
    _NcmidcsuCfgAlmOnEqLoop_Type()
)
ncmidcsuCfgAlmOnEqLoop.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ncmidcsuCfgAlmOnEqLoop.setStatus("mandatory")


class _NcmidcsuCfgAlmOnNetLoop_Type(Integer32):
    """Custom type ncmidcsuCfgAlmOnNetLoop based on Integer32"""
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


_NcmidcsuCfgAlmOnNetLoop_Type.__name__ = "Integer32"
_NcmidcsuCfgAlmOnNetLoop_Object = MibTableColumn
ncmidcsuCfgAlmOnNetLoop = _NcmidcsuCfgAlmOnNetLoop_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3027, 10000, 1, 28),
    _NcmidcsuCfgAlmOnNetLoop_Type()
)
ncmidcsuCfgAlmOnNetLoop.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ncmidcsuCfgAlmOnNetLoop.setStatus("mandatory")


class _NcmidcsuCfgAlmOnPowerUpLoop_Type(Integer32):
    """Custom type ncmidcsuCfgAlmOnPowerUpLoop based on Integer32"""
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


_NcmidcsuCfgAlmOnPowerUpLoop_Type.__name__ = "Integer32"
_NcmidcsuCfgAlmOnPowerUpLoop_Object = MibTableColumn
ncmidcsuCfgAlmOnPowerUpLoop = _NcmidcsuCfgAlmOnPowerUpLoop_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3027, 10000, 1, 29),
    _NcmidcsuCfgAlmOnPowerUpLoop_Type()
)
ncmidcsuCfgAlmOnPowerUpLoop.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ncmidcsuCfgAlmOnPowerUpLoop.setStatus("mandatory")


class _NcmidcsuCfgLoopRespLLB_Type(Integer32):
    """Custom type ncmidcsuCfgLoopRespLLB based on Integer32"""
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


_NcmidcsuCfgLoopRespLLB_Type.__name__ = "Integer32"
_NcmidcsuCfgLoopRespLLB_Object = MibTableColumn
ncmidcsuCfgLoopRespLLB = _NcmidcsuCfgLoopRespLLB_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3027, 10000, 1, 30),
    _NcmidcsuCfgLoopRespLLB_Type()
)
ncmidcsuCfgLoopRespLLB.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ncmidcsuCfgLoopRespLLB.setStatus("mandatory")


class _NcmidcsuCfgLoopRespPLB_Type(Integer32):
    """Custom type ncmidcsuCfgLoopRespPLB based on Integer32"""
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


_NcmidcsuCfgLoopRespPLB_Type.__name__ = "Integer32"
_NcmidcsuCfgLoopRespPLB_Object = MibTableColumn
ncmidcsuCfgLoopRespPLB = _NcmidcsuCfgLoopRespPLB_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3027, 10000, 1, 31),
    _NcmidcsuCfgLoopRespPLB_Type()
)
ncmidcsuCfgLoopRespPLB.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ncmidcsuCfgLoopRespPLB.setStatus("mandatory")


class _NcmidcsuCfgLoopRespELB_Type(Integer32):
    """Custom type ncmidcsuCfgLoopRespELB based on Integer32"""
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


_NcmidcsuCfgLoopRespELB_Type.__name__ = "Integer32"
_NcmidcsuCfgLoopRespELB_Object = MibTableColumn
ncmidcsuCfgLoopRespELB = _NcmidcsuCfgLoopRespELB_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3027, 10000, 1, 32),
    _NcmidcsuCfgLoopRespELB_Type()
)
ncmidcsuCfgLoopRespELB.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ncmidcsuCfgLoopRespELB.setStatus("mandatory")


class _NcmidcsuCfgLoopRespRLB_Type(Integer32):
    """Custom type ncmidcsuCfgLoopRespRLB based on Integer32"""
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


_NcmidcsuCfgLoopRespRLB_Type.__name__ = "Integer32"
_NcmidcsuCfgLoopRespRLB_Object = MibTableColumn
ncmidcsuCfgLoopRespRLB = _NcmidcsuCfgLoopRespRLB_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3027, 10000, 1, 33),
    _NcmidcsuCfgLoopRespRLB_Type()
)
ncmidcsuCfgLoopRespRLB.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ncmidcsuCfgLoopRespRLB.setStatus("mandatory")


class _NcmidcsuCfgLoopRespLLBTONE_Type(Integer32):
    """Custom type ncmidcsuCfgLoopRespLLBTONE based on Integer32"""
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


_NcmidcsuCfgLoopRespLLBTONE_Type.__name__ = "Integer32"
_NcmidcsuCfgLoopRespLLBTONE_Object = MibTableColumn
ncmidcsuCfgLoopRespLLBTONE = _NcmidcsuCfgLoopRespLLBTONE_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3027, 10000, 1, 34),
    _NcmidcsuCfgLoopRespLLBTONE_Type()
)
ncmidcsuCfgLoopRespLLBTONE.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ncmidcsuCfgLoopRespLLBTONE.setStatus("mandatory")


class _NcmidcsuCfgLoopRespPLBTONE_Type(Integer32):
    """Custom type ncmidcsuCfgLoopRespPLBTONE based on Integer32"""
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


_NcmidcsuCfgLoopRespPLBTONE_Type.__name__ = "Integer32"
_NcmidcsuCfgLoopRespPLBTONE_Object = MibTableColumn
ncmidcsuCfgLoopRespPLBTONE = _NcmidcsuCfgLoopRespPLBTONE_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3027, 10000, 1, 35),
    _NcmidcsuCfgLoopRespPLBTONE_Type()
)
ncmidcsuCfgLoopRespPLBTONE.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ncmidcsuCfgLoopRespPLBTONE.setStatus("mandatory")


class _NcmidcsuCfgSendReceiveInBandCode_Type(Integer32):
    """Custom type ncmidcsuCfgSendReceiveInBandCode based on Integer32"""
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


_NcmidcsuCfgSendReceiveInBandCode_Type.__name__ = "Integer32"
_NcmidcsuCfgSendReceiveInBandCode_Object = MibTableColumn
ncmidcsuCfgSendReceiveInBandCode = _NcmidcsuCfgSendReceiveInBandCode_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3027, 10000, 1, 36),
    _NcmidcsuCfgSendReceiveInBandCode_Type()
)
ncmidcsuCfgSendReceiveInBandCode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ncmidcsuCfgSendReceiveInBandCode.setStatus("mandatory")
_NcmidcsuThresholdIntervalTable_Object = MibTable
ncmidcsuThresholdIntervalTable = _NcmidcsuThresholdIntervalTable_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3027, 10001)
)
if mibBuilder.loadTexts:
    ncmidcsuThresholdIntervalTable.setStatus("mandatory")
_NcmidcsuThresholdIntervalEntry_Object = MibTableRow
ncmidcsuThresholdIntervalEntry = _NcmidcsuThresholdIntervalEntry_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3027, 10001, 1)
)
ncmidcsuThresholdIntervalEntry.setIndexNames(
    (0, "VERILINK-ENTERPRISE-NCMIDCSU-MIB", "ncmidcsuThresholdNIDIndex"),
    (0, "VERILINK-ENTERPRISE-NCMIDCSU-MIB", "ncmidcsuThresholdIntervalIndex"),
)
if mibBuilder.loadTexts:
    ncmidcsuThresholdIntervalEntry.setStatus("mandatory")


class _NcmidcsuThresholdNIDIndex_Type(Integer32):
    """Custom type ncmidcsuThresholdNIDIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_NcmidcsuThresholdNIDIndex_Type.__name__ = "Integer32"
_NcmidcsuThresholdNIDIndex_Object = MibTableColumn
ncmidcsuThresholdNIDIndex = _NcmidcsuThresholdNIDIndex_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3027, 10001, 1, 1),
    _NcmidcsuThresholdNIDIndex_Type()
)
ncmidcsuThresholdNIDIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmidcsuThresholdNIDIndex.setStatus("mandatory")
_NcmidcsuThresholdIntervalIndex_Type = Integer32
_NcmidcsuThresholdIntervalIndex_Object = MibTableColumn
ncmidcsuThresholdIntervalIndex = _NcmidcsuThresholdIntervalIndex_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3027, 10001, 1, 2),
    _NcmidcsuThresholdIntervalIndex_Type()
)
ncmidcsuThresholdIntervalIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmidcsuThresholdIntervalIndex.setStatus("mandatory")


class _NcmidcsuBERThreshold_Type(Integer32):
    """Custom type ncmidcsuBERThreshold based on Integer32"""
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


_NcmidcsuBERThreshold_Type.__name__ = "Integer32"
_NcmidcsuBERThreshold_Object = MibTableColumn
ncmidcsuBERThreshold = _NcmidcsuBERThreshold_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3027, 10001, 1, 3),
    _NcmidcsuBERThreshold_Type()
)
ncmidcsuBERThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ncmidcsuBERThreshold.setStatus("mandatory")
_NcmidcsubpvSecThreshold_Type = Integer32
_NcmidcsubpvSecThreshold_Object = MibTableColumn
ncmidcsubpvSecThreshold = _NcmidcsubpvSecThreshold_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3027, 10001, 1, 4),
    _NcmidcsubpvSecThreshold_Type()
)
ncmidcsubpvSecThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ncmidcsubpvSecThreshold.setStatus("mandatory")
_NcmidcsubpvSecInterval_Type = Integer32
_NcmidcsubpvSecInterval_Object = MibTableColumn
ncmidcsubpvSecInterval = _NcmidcsubpvSecInterval_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3027, 10001, 1, 5),
    _NcmidcsubpvSecInterval_Type()
)
ncmidcsubpvSecInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ncmidcsubpvSecInterval.setStatus("mandatory")
_NcmidcsuESThreshold_Type = Integer32
_NcmidcsuESThreshold_Object = MibTableColumn
ncmidcsuESThreshold = _NcmidcsuESThreshold_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3027, 10001, 1, 6),
    _NcmidcsuESThreshold_Type()
)
ncmidcsuESThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ncmidcsuESThreshold.setStatus("mandatory")
_NcmidcsuESInterval_Type = Integer32
_NcmidcsuESInterval_Object = MibTableColumn
ncmidcsuESInterval = _NcmidcsuESInterval_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3027, 10001, 1, 7),
    _NcmidcsuESInterval_Type()
)
ncmidcsuESInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ncmidcsuESInterval.setStatus("mandatory")
_NcmidcsuUASThreshold_Type = Integer32
_NcmidcsuUASThreshold_Object = MibTableColumn
ncmidcsuUASThreshold = _NcmidcsuUASThreshold_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3027, 10001, 1, 8),
    _NcmidcsuUASThreshold_Type()
)
ncmidcsuUASThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ncmidcsuUASThreshold.setStatus("mandatory")
_NcmidcsuUASInterval_Type = Integer32
_NcmidcsuUASInterval_Object = MibTableColumn
ncmidcsuUASInterval = _NcmidcsuUASInterval_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3027, 10001, 1, 9),
    _NcmidcsuUASInterval_Type()
)
ncmidcsuUASInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ncmidcsuUASInterval.setStatus("mandatory")
_NcmidcsuConfigOneTable_Object = MibTable
ncmidcsuConfigOneTable = _NcmidcsuConfigOneTable_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3027, 10002)
)
if mibBuilder.loadTexts:
    ncmidcsuConfigOneTable.setStatus("mandatory")
_NcmidcsuConfigOneEntry_Object = MibTableRow
ncmidcsuConfigOneEntry = _NcmidcsuConfigOneEntry_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3027, 10002, 1)
)
ncmidcsuConfigOneEntry.setIndexNames(
    (0, "VERILINK-ENTERPRISE-NCMIDCSU-MIB", "ncmidcsucfg1NIDIndex"),
    (0, "VERILINK-ENTERPRISE-NCMIDCSU-MIB", "ncmidcsuLineIndex1"),
)
if mibBuilder.loadTexts:
    ncmidcsuConfigOneEntry.setStatus("mandatory")


class _Ncmidcsucfg1NIDIndex_Type(Integer32):
    """Custom type ncmidcsucfg1NIDIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_Ncmidcsucfg1NIDIndex_Type.__name__ = "Integer32"
_Ncmidcsucfg1NIDIndex_Object = MibTableColumn
ncmidcsucfg1NIDIndex = _Ncmidcsucfg1NIDIndex_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3027, 10002, 1, 1),
    _Ncmidcsucfg1NIDIndex_Type()
)
ncmidcsucfg1NIDIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmidcsucfg1NIDIndex.setStatus("mandatory")
_NcmidcsuLineIndex1_Type = Integer32
_NcmidcsuLineIndex1_Object = MibTableColumn
ncmidcsuLineIndex1 = _NcmidcsuLineIndex1_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3027, 10002, 1, 2),
    _NcmidcsuLineIndex1_Type()
)
ncmidcsuLineIndex1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmidcsuLineIndex1.setStatus("mandatory")


class _NcmidcsuDS0Channel_Type(DisplayString):
    """Custom type ncmidcsuDS0Channel based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_NcmidcsuDS0Channel_Type.__name__ = "DisplayString"
_NcmidcsuDS0Channel_Object = MibTableColumn
ncmidcsuDS0Channel = _NcmidcsuDS0Channel_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3027, 10002, 1, 3),
    _NcmidcsuDS0Channel_Type()
)
ncmidcsuDS0Channel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ncmidcsuDS0Channel.setStatus("mandatory")
_NcmidcsuRLBTimeoutIndex_Type = Integer32
_NcmidcsuRLBTimeoutIndex_Object = MibTableColumn
ncmidcsuRLBTimeoutIndex = _NcmidcsuRLBTimeoutIndex_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3027, 10002, 1, 4),
    _NcmidcsuRLBTimeoutIndex_Type()
)
ncmidcsuRLBTimeoutIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ncmidcsuRLBTimeoutIndex.setStatus("mandatory")
_NcmidcsuNetLofcIndexTime_Type = Integer32
_NcmidcsuNetLofcIndexTime_Object = MibTableColumn
ncmidcsuNetLofcIndexTime = _NcmidcsuNetLofcIndexTime_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3027, 10002, 1, 5),
    _NcmidcsuNetLofcIndexTime_Type()
)
ncmidcsuNetLofcIndexTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ncmidcsuNetLofcIndexTime.setStatus("mandatory")


class _NcmidcsuTiming_Type(Integer32):
    """Custom type ncmidcsuTiming based on Integer32"""
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
          ("external-422", 3),
          ("internal", 2),
          ("net", 5),
          ("reserved", 4),
          ("reserved-two", 7),
          ("timing", 1))
    )


_NcmidcsuTiming_Type.__name__ = "Integer32"
_NcmidcsuTiming_Object = MibTableColumn
ncmidcsuTiming = _NcmidcsuTiming_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3027, 10002, 1, 6),
    _NcmidcsuTiming_Type()
)
ncmidcsuTiming.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ncmidcsuTiming.setStatus("mandatory")


class _NcmidcsuLineCode_Type(Integer32):
    """Custom type ncmidcsuLineCode based on Integer32"""
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


_NcmidcsuLineCode_Type.__name__ = "Integer32"
_NcmidcsuLineCode_Object = MibTableColumn
ncmidcsuLineCode = _NcmidcsuLineCode_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3027, 10002, 1, 7),
    _NcmidcsuLineCode_Type()
)
ncmidcsuLineCode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ncmidcsuLineCode.setStatus("mandatory")


class _NcmidcsuMode_Type(Integer32):
    """Custom type ncmidcsuMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("mode-56k", 1),
          ("mode-64k", 2))
    )


_NcmidcsuMode_Type.__name__ = "Integer32"
_NcmidcsuMode_Object = MibTableColumn
ncmidcsuMode = _NcmidcsuMode_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3027, 10002, 1, 8),
    _NcmidcsuMode_Type()
)
ncmidcsuMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ncmidcsuMode.setStatus("mandatory")


class _NcmidcsuClock_Type(Integer32):
    """Custom type ncmidcsuClock based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("iNVST", 2),
          ("sT", 1),
          ("tT", 3))
    )


_NcmidcsuClock_Type.__name__ = "Integer32"
_NcmidcsuClock_Object = MibTableColumn
ncmidcsuClock = _NcmidcsuClock_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3027, 10002, 1, 9),
    _NcmidcsuClock_Type()
)
ncmidcsuClock.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ncmidcsuClock.setStatus("mandatory")


class _NcmidcsuScramble_Type(Integer32):
    """Custom type ncmidcsuScramble based on Integer32"""
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


_NcmidcsuScramble_Type.__name__ = "Integer32"
_NcmidcsuScramble_Object = MibTableColumn
ncmidcsuScramble = _NcmidcsuScramble_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3027, 10002, 1, 10),
    _NcmidcsuScramble_Type()
)
ncmidcsuScramble.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ncmidcsuScramble.setStatus("mandatory")
_NcmidcsuLosLead_Type = Integer32
_NcmidcsuLosLead_Object = MibTableColumn
ncmidcsuLosLead = _NcmidcsuLosLead_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3027, 10002, 1, 11),
    _NcmidcsuLosLead_Type()
)
ncmidcsuLosLead.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ncmidcsuLosLead.setStatus("mandatory")


class _NcmidcsuPortLoopEnable_Type(Integer32):
    """Custom type ncmidcsuPortLoopEnable based on Integer32"""
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


_NcmidcsuPortLoopEnable_Type.__name__ = "Integer32"
_NcmidcsuPortLoopEnable_Object = MibTableColumn
ncmidcsuPortLoopEnable = _NcmidcsuPortLoopEnable_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3027, 10002, 1, 12),
    _NcmidcsuPortLoopEnable_Type()
)
ncmidcsuPortLoopEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ncmidcsuPortLoopEnable.setStatus("mandatory")


class _NcmidcsuDataInvert_Type(Integer32):
    """Custom type ncmidcsuDataInvert based on Integer32"""
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


_NcmidcsuDataInvert_Type.__name__ = "Integer32"
_NcmidcsuDataInvert_Object = MibTableColumn
ncmidcsuDataInvert = _NcmidcsuDataInvert_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3027, 10002, 1, 13),
    _NcmidcsuDataInvert_Type()
)
ncmidcsuDataInvert.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ncmidcsuDataInvert.setStatus("mandatory")


class _NcmidcsuTimingUnit_Type(Integer32):
    """Custom type ncmidcsuTimingUnit based on Integer32"""
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


_NcmidcsuTimingUnit_Type.__name__ = "Integer32"
_NcmidcsuTimingUnit_Object = MibTableColumn
ncmidcsuTimingUnit = _NcmidcsuTimingUnit_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3027, 10002, 1, 14),
    _NcmidcsuTimingUnit_Type()
)
ncmidcsuTimingUnit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ncmidcsuTimingUnit.setStatus("mandatory")


class _NcmidcsuAlarmReporting_Type(Integer32):
    """Custom type ncmidcsuAlarmReporting based on Integer32"""
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


_NcmidcsuAlarmReporting_Type.__name__ = "Integer32"
_NcmidcsuAlarmReporting_Object = MibTableColumn
ncmidcsuAlarmReporting = _NcmidcsuAlarmReporting_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3027, 10002, 1, 15),
    _NcmidcsuAlarmReporting_Type()
)
ncmidcsuAlarmReporting.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ncmidcsuAlarmReporting.setStatus("mandatory")
_NcmidcsuDiagnosticTable_Object = MibTable
ncmidcsuDiagnosticTable = _NcmidcsuDiagnosticTable_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3027, 10003)
)
if mibBuilder.loadTexts:
    ncmidcsuDiagnosticTable.setStatus("mandatory")
_NcmidcsuDiagnosticEntry_Object = MibTableRow
ncmidcsuDiagnosticEntry = _NcmidcsuDiagnosticEntry_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3027, 10003, 1)
)
ncmidcsuDiagnosticEntry.setIndexNames(
    (0, "VERILINK-ENTERPRISE-NCMIDCSU-MIB", "ncmidcsuDiagNIDIndex"),
    (0, "VERILINK-ENTERPRISE-NCMIDCSU-MIB", "ncmidcsuDiagnosticIndex"),
)
if mibBuilder.loadTexts:
    ncmidcsuDiagnosticEntry.setStatus("mandatory")


class _NcmidcsuDiagNIDIndex_Type(Integer32):
    """Custom type ncmidcsuDiagNIDIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_NcmidcsuDiagNIDIndex_Type.__name__ = "Integer32"
_NcmidcsuDiagNIDIndex_Object = MibTableColumn
ncmidcsuDiagNIDIndex = _NcmidcsuDiagNIDIndex_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3027, 10003, 1, 1),
    _NcmidcsuDiagNIDIndex_Type()
)
ncmidcsuDiagNIDIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmidcsuDiagNIDIndex.setStatus("mandatory")
_NcmidcsuDiagnosticIndex_Type = Integer32
_NcmidcsuDiagnosticIndex_Object = MibTableColumn
ncmidcsuDiagnosticIndex = _NcmidcsuDiagnosticIndex_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3027, 10003, 1, 2),
    _NcmidcsuDiagnosticIndex_Type()
)
ncmidcsuDiagnosticIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmidcsuDiagnosticIndex.setStatus("mandatory")
_NcmidcsuAlarmSetDelay_Type = Integer32
_NcmidcsuAlarmSetDelay_Object = MibTableColumn
ncmidcsuAlarmSetDelay = _NcmidcsuAlarmSetDelay_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3027, 10003, 1, 3),
    _NcmidcsuAlarmSetDelay_Type()
)
ncmidcsuAlarmSetDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ncmidcsuAlarmSetDelay.setStatus("mandatory")
_NcmidcsuAlarmClearDelay_Type = Integer32
_NcmidcsuAlarmClearDelay_Object = MibTableColumn
ncmidcsuAlarmClearDelay = _NcmidcsuAlarmClearDelay_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3027, 10003, 1, 4),
    _NcmidcsuAlarmClearDelay_Type()
)
ncmidcsuAlarmClearDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ncmidcsuAlarmClearDelay.setStatus("mandatory")


class _NcmidcsuAlarmEnable_Type(Integer32):
    """Custom type ncmidcsuAlarmEnable based on Integer32"""
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


_NcmidcsuAlarmEnable_Type.__name__ = "Integer32"
_NcmidcsuAlarmEnable_Object = MibTableColumn
ncmidcsuAlarmEnable = _NcmidcsuAlarmEnable_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3027, 10003, 1, 5),
    _NcmidcsuAlarmEnable_Type()
)
ncmidcsuAlarmEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ncmidcsuAlarmEnable.setStatus("mandatory")


class _NcmidcsuLoopback_Type(Integer32):
    """Custom type ncmidcsuLoopback based on Integer32"""
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
              10)
        )
    )
    namedValues = NamedValues(
        *(("csu-Equip-Loop-Back", 4),
          ("csu-No-Loop-Back", 5),
          ("csu-Payload-Loop-Back", 1),
          ("deactivate-ELB-and-RLB", 7),
          ("deactivate-LLB-and-PLB", 6),
          ("deactivate-Payload-Loop-Back", 8),
          ("line-Loop-Back", 2),
          ("repeater-Loop-Back", 3),
          ("send-Inband-Loop-Down", 10),
          ("send-Inband-Loop-Up", 9))
    )


_NcmidcsuLoopback_Type.__name__ = "Integer32"
_NcmidcsuLoopback_Object = MibTableColumn
ncmidcsuLoopback = _NcmidcsuLoopback_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3027, 10003, 1, 6),
    _NcmidcsuLoopback_Type()
)
ncmidcsuLoopback.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ncmidcsuLoopback.setStatus("mandatory")


class _Ncmdteloops_Type(Integer32):
    """Custom type ncmdteloops based on Integer32"""
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
        *(("far-off", 5),
          ("far-on", 4),
          ("near-off", 3),
          ("near-on", 2),
          ("no-loop", 1),
          ("repeater-loopback", 6))
    )


_Ncmdteloops_Type.__name__ = "Integer32"
_Ncmdteloops_Object = MibTableColumn
ncmdteloops = _Ncmdteloops_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3027, 10003, 1, 7),
    _Ncmdteloops_Type()
)
ncmdteloops.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ncmdteloops.setStatus("mandatory")


class _NcmidcsuTestPattern_Type(Integer32):
    """Custom type ncmidcsuTestPattern based on Integer32"""
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
        *(("all-ones", 5),
          ("no-test", 1),
          ("one-in-eight", 3),
          ("qrss", 2),
          ("three-in-twenty-four", 4))
    )


_NcmidcsuTestPattern_Type.__name__ = "Integer32"
_NcmidcsuTestPattern_Object = MibTableColumn
ncmidcsuTestPattern = _NcmidcsuTestPattern_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3027, 10003, 1, 8),
    _NcmidcsuTestPattern_Type()
)
ncmidcsuTestPattern.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ncmidcsuTestPattern.setStatus("mandatory")


class _NcmidcsuResetPerfReg_Type(Integer32):
    """Custom type ncmidcsuResetPerfReg based on Integer32"""
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


_NcmidcsuResetPerfReg_Type.__name__ = "Integer32"
_NcmidcsuResetPerfReg_Object = MibTableColumn
ncmidcsuResetPerfReg = _NcmidcsuResetPerfReg_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3027, 10003, 1, 9),
    _NcmidcsuResetPerfReg_Type()
)
ncmidcsuResetPerfReg.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ncmidcsuResetPerfReg.setStatus("mandatory")
_NcmidcsuTestErrorCounter_Type = Gauge32
_NcmidcsuTestErrorCounter_Object = MibTableColumn
ncmidcsuTestErrorCounter = _NcmidcsuTestErrorCounter_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3027, 10003, 1, 10),
    _NcmidcsuTestErrorCounter_Type()
)
ncmidcsuTestErrorCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmidcsuTestErrorCounter.setStatus("mandatory")
_NcmidcsuTestSecondsRemain_Type = Gauge32
_NcmidcsuTestSecondsRemain_Object = MibTableColumn
ncmidcsuTestSecondsRemain = _NcmidcsuTestSecondsRemain_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3027, 10003, 1, 11),
    _NcmidcsuTestSecondsRemain_Type()
)
ncmidcsuTestSecondsRemain.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmidcsuTestSecondsRemain.setStatus("mandatory")
_NcmidcsuTestTimeSeconds_Type = Integer32
_NcmidcsuTestTimeSeconds_Object = MibTableColumn
ncmidcsuTestTimeSeconds = _NcmidcsuTestTimeSeconds_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3027, 10003, 1, 12),
    _NcmidcsuTestTimeSeconds_Type()
)
ncmidcsuTestTimeSeconds.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ncmidcsuTestTimeSeconds.setStatus("mandatory")
_NcmidcsuNetLOFCIndexTime_Type = Integer32
_NcmidcsuNetLOFCIndexTime_Object = MibTableColumn
ncmidcsuNetLOFCIndexTime = _NcmidcsuNetLOFCIndexTime_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3027, 10003, 1, 13),
    _NcmidcsuNetLOFCIndexTime_Type()
)
ncmidcsuNetLOFCIndexTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ncmidcsuNetLOFCIndexTime.setStatus("mandatory")


class _NcmidcsuChannelMask_Type(DisplayString):
    """Custom type ncmidcsuChannelMask based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_NcmidcsuChannelMask_Type.__name__ = "DisplayString"
_NcmidcsuChannelMask_Object = MibTableColumn
ncmidcsuChannelMask = _NcmidcsuChannelMask_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3027, 10003, 1, 14),
    _NcmidcsuChannelMask_Type()
)
ncmidcsuChannelMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ncmidcsuChannelMask.setStatus("mandatory")


class _NcmidcsuApplication_Type(Integer32):
    """Custom type ncmidcsuApplication based on Integer32"""
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


_NcmidcsuApplication_Type.__name__ = "Integer32"
_NcmidcsuApplication_Object = MibTableColumn
ncmidcsuApplication = _NcmidcsuApplication_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3027, 10003, 1, 15),
    _NcmidcsuApplication_Type()
)
ncmidcsuApplication.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ncmidcsuApplication.setStatus("mandatory")
_NcmidcsuTestIntervalIndex_Type = Integer32
_NcmidcsuTestIntervalIndex_Object = MibTableColumn
ncmidcsuTestIntervalIndex = _NcmidcsuTestIntervalIndex_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3027, 10003, 1, 16),
    _NcmidcsuTestIntervalIndex_Type()
)
ncmidcsuTestIntervalIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ncmidcsuTestIntervalIndex.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "VERILINK-ENTERPRISE-NCMIDCSU-MIB",
    **{"ncmidcsuConfigTable": ncmidcsuConfigTable,
       "ncmidcsuConfigEntry": ncmidcsuConfigEntry,
       "ncmidcsucfgNIDIndex": ncmidcsucfgNIDIndex,
       "ncmidcsuLineIndex": ncmidcsuLineIndex,
       "ncmidcsuNetLineBuildOut": ncmidcsuNetLineBuildOut,
       "ncmidcsuNetworkKeepAlive": ncmidcsuNetworkKeepAlive,
       "ncmidcsuExcessiveError": ncmidcsuExcessiveError,
       "ncmidcsuOutOfFrame": ncmidcsuOutOfFrame,
       "ncmidcsuFormat": ncmidcsuFormat,
       "ncmidcsuNetDensityEnforcement": ncmidcsuNetDensityEnforcement,
       "ncmidcsuNetLossOfSignal": ncmidcsuNetLossOfSignal,
       "ncmidcsuJitterBuf": ncmidcsuJitterBuf,
       "ncmidcsuTestSigCfgEnable": ncmidcsuTestSigCfgEnable,
       "ncmidcsuTestSigCfgFrameSignal": ncmidcsuTestSigCfgFrameSignal,
       "ncmidcsuCfgRptSendPRM": ncmidcsuCfgRptSendPRM,
       "ncmidcsuCfgRptPollFarEnd": ncmidcsuCfgRptPollFarEnd,
       "ncmidcsuCfgRptDataLinkUnsolicit": ncmidcsuCfgRptDataLinkUnsolicit,
       "ncmidcsuCfgRptAlmReporting": ncmidcsuCfgRptAlmReporting,
       "ncmidcsuCfgRptPRMType": ncmidcsuCfgRptPRMType,
       "ncmidcsuCfgCodeRegenCRC": ncmidcsuCfgCodeRegenCRC,
       "ncmidcsuCfgCodeXYellowAlarm": ncmidcsuCfgCodeXYellowAlarm,
       "ncmidcsuCfgCodeEQFIFO": ncmidcsuCfgCodeEQFIFO,
       "ncmidcsuCfgCodeNETFIFO": ncmidcsuCfgCodeNETFIFO,
       "ncmidcsuCfgCodeTranMode": ncmidcsuCfgCodeTranMode,
       "ncmidcsuCfgCodeSend1sLnkIdle": ncmidcsuCfgCodeSend1sLnkIdle,
       "ncmidcsuCfgAlmSelfTest": ncmidcsuCfgAlmSelfTest,
       "ncmidcsuCfgAlmEnableTestState": ncmidcsuCfgAlmEnableTestState,
       "ncmidcsuCfgAlmUnframedMode": ncmidcsuCfgAlmUnframedMode,
       "ncmidcsuCfgAlmOnEqLoop": ncmidcsuCfgAlmOnEqLoop,
       "ncmidcsuCfgAlmOnNetLoop": ncmidcsuCfgAlmOnNetLoop,
       "ncmidcsuCfgAlmOnPowerUpLoop": ncmidcsuCfgAlmOnPowerUpLoop,
       "ncmidcsuCfgLoopRespLLB": ncmidcsuCfgLoopRespLLB,
       "ncmidcsuCfgLoopRespPLB": ncmidcsuCfgLoopRespPLB,
       "ncmidcsuCfgLoopRespELB": ncmidcsuCfgLoopRespELB,
       "ncmidcsuCfgLoopRespRLB": ncmidcsuCfgLoopRespRLB,
       "ncmidcsuCfgLoopRespLLBTONE": ncmidcsuCfgLoopRespLLBTONE,
       "ncmidcsuCfgLoopRespPLBTONE": ncmidcsuCfgLoopRespPLBTONE,
       "ncmidcsuCfgSendReceiveInBandCode": ncmidcsuCfgSendReceiveInBandCode,
       "ncmidcsuThresholdIntervalTable": ncmidcsuThresholdIntervalTable,
       "ncmidcsuThresholdIntervalEntry": ncmidcsuThresholdIntervalEntry,
       "ncmidcsuThresholdNIDIndex": ncmidcsuThresholdNIDIndex,
       "ncmidcsuThresholdIntervalIndex": ncmidcsuThresholdIntervalIndex,
       "ncmidcsuBERThreshold": ncmidcsuBERThreshold,
       "ncmidcsubpvSecThreshold": ncmidcsubpvSecThreshold,
       "ncmidcsubpvSecInterval": ncmidcsubpvSecInterval,
       "ncmidcsuESThreshold": ncmidcsuESThreshold,
       "ncmidcsuESInterval": ncmidcsuESInterval,
       "ncmidcsuUASThreshold": ncmidcsuUASThreshold,
       "ncmidcsuUASInterval": ncmidcsuUASInterval,
       "ncmidcsuConfigOneTable": ncmidcsuConfigOneTable,
       "ncmidcsuConfigOneEntry": ncmidcsuConfigOneEntry,
       "ncmidcsucfg1NIDIndex": ncmidcsucfg1NIDIndex,
       "ncmidcsuLineIndex1": ncmidcsuLineIndex1,
       "ncmidcsuDS0Channel": ncmidcsuDS0Channel,
       "ncmidcsuRLBTimeoutIndex": ncmidcsuRLBTimeoutIndex,
       "ncmidcsuNetLofcIndexTime": ncmidcsuNetLofcIndexTime,
       "ncmidcsuTiming": ncmidcsuTiming,
       "ncmidcsuLineCode": ncmidcsuLineCode,
       "ncmidcsuMode": ncmidcsuMode,
       "ncmidcsuClock": ncmidcsuClock,
       "ncmidcsuScramble": ncmidcsuScramble,
       "ncmidcsuLosLead": ncmidcsuLosLead,
       "ncmidcsuPortLoopEnable": ncmidcsuPortLoopEnable,
       "ncmidcsuDataInvert": ncmidcsuDataInvert,
       "ncmidcsuTimingUnit": ncmidcsuTimingUnit,
       "ncmidcsuAlarmReporting": ncmidcsuAlarmReporting,
       "ncmidcsuDiagnosticTable": ncmidcsuDiagnosticTable,
       "ncmidcsuDiagnosticEntry": ncmidcsuDiagnosticEntry,
       "ncmidcsuDiagNIDIndex": ncmidcsuDiagNIDIndex,
       "ncmidcsuDiagnosticIndex": ncmidcsuDiagnosticIndex,
       "ncmidcsuAlarmSetDelay": ncmidcsuAlarmSetDelay,
       "ncmidcsuAlarmClearDelay": ncmidcsuAlarmClearDelay,
       "ncmidcsuAlarmEnable": ncmidcsuAlarmEnable,
       "ncmidcsuLoopback": ncmidcsuLoopback,
       "ncmdteloops": ncmdteloops,
       "ncmidcsuTestPattern": ncmidcsuTestPattern,
       "ncmidcsuResetPerfReg": ncmidcsuResetPerfReg,
       "ncmidcsuTestErrorCounter": ncmidcsuTestErrorCounter,
       "ncmidcsuTestSecondsRemain": ncmidcsuTestSecondsRemain,
       "ncmidcsuTestTimeSeconds": ncmidcsuTestTimeSeconds,
       "ncmidcsuNetLOFCIndexTime": ncmidcsuNetLOFCIndexTime,
       "ncmidcsuChannelMask": ncmidcsuChannelMask,
       "ncmidcsuApplication": ncmidcsuApplication,
       "ncmidcsuTestIntervalIndex": ncmidcsuTestIntervalIndex}
)
