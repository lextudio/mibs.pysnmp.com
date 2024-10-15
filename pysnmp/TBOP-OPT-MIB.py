# SNMP MIB module (TBOP-OPT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/TBOP-OPT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:00:55 2024
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



class Counter16(Integer32):
    """Custom type Counter16 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )





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
_Cdx6500PPCTTBOPPortTable_Object = MibTable
cdx6500PPCTTBOPPortTable = _Cdx6500PPCTTBOPPortTable_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 7)
)
if mibBuilder.loadTexts:
    cdx6500PPCTTBOPPortTable.setStatus("mandatory")
_Cdx6500PPCTTBOPPortEntry_Object = MibTableRow
cdx6500PPCTTBOPPortEntry = _Cdx6500PPCTTBOPPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 7, 1)
)
cdx6500PPCTTBOPPortEntry.setIndexNames(
    (0, "TBOP-OPT-MIB", "cdx6500TBOPCfgPortNumber"),
)
if mibBuilder.loadTexts:
    cdx6500PPCTTBOPPortEntry.setStatus("mandatory")


class _Cdx6500TBOPCfgPortNumber_Type(Integer32):
    """Custom type cdx6500TBOPCfgPortNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 54),
    )


_Cdx6500TBOPCfgPortNumber_Type.__name__ = "Integer32"
_Cdx6500TBOPCfgPortNumber_Object = MibTableColumn
cdx6500TBOPCfgPortNumber = _Cdx6500TBOPCfgPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 7, 1, 1),
    _Cdx6500TBOPCfgPortNumber_Type()
)
cdx6500TBOPCfgPortNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500TBOPCfgPortNumber.setStatus("mandatory")


class _Cdx6500TBOPCfgPortEIAOpt_Type(Integer32):
    """Custom type cdx6500TBOPCfgPortEIAOpt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              8,
              50,
              100)
        )
    )
    namedValues = NamedValues(
        *(("dtr", 1),
          ("dtrd", 2),
          ("dtrp", 8),
          ("nc", 100),
          ("newvalSimp", 50),
          ("simp", 0))
    )


_Cdx6500TBOPCfgPortEIAOpt_Type.__name__ = "Integer32"
_Cdx6500TBOPCfgPortEIAOpt_Object = MibTableColumn
cdx6500TBOPCfgPortEIAOpt = _Cdx6500TBOPCfgPortEIAOpt_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 7, 1, 2),
    _Cdx6500TBOPCfgPortEIAOpt_Type()
)
cdx6500TBOPCfgPortEIAOpt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500TBOPCfgPortEIAOpt.setStatus("mandatory")


class _Cdx6500TBOPCfgPortClockType_Type(Integer32):
    """Custom type cdx6500TBOPCfgPortClockType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              50,
              100)
        )
    )
    namedValues = NamedValues(
        *(("ext", 1),
          ("int", 0),
          ("nc", 100),
          ("newvalInt", 50))
    )


_Cdx6500TBOPCfgPortClockType_Type.__name__ = "Integer32"
_Cdx6500TBOPCfgPortClockType_Object = MibTableColumn
cdx6500TBOPCfgPortClockType = _Cdx6500TBOPCfgPortClockType_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 7, 1, 3),
    _Cdx6500TBOPCfgPortClockType_Type()
)
cdx6500TBOPCfgPortClockType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500TBOPCfgPortClockType.setStatus("mandatory")


class _Cdx6500TBOPCfgPortClockSpeed_Type(Integer32):
    """Custom type cdx6500TBOPCfgPortClockSpeed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 384000),
    )


_Cdx6500TBOPCfgPortClockSpeed_Type.__name__ = "Integer32"
_Cdx6500TBOPCfgPortClockSpeed_Object = MibTableColumn
cdx6500TBOPCfgPortClockSpeed = _Cdx6500TBOPCfgPortClockSpeed_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 7, 1, 4),
    _Cdx6500TBOPCfgPortClockSpeed_Type()
)
cdx6500TBOPCfgPortClockSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500TBOPCfgPortClockSpeed.setStatus("mandatory")


class _Cdx6500TBOPCfgPortTxCoding_Type(Integer32):
    """Custom type cdx6500TBOPCfgPortTxCoding based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              50,
              100)
        )
    )
    namedValues = NamedValues(
        *(("nc", 100),
          ("newvalNrz", 50),
          ("nrz", 0),
          ("nrzi", 1))
    )


_Cdx6500TBOPCfgPortTxCoding_Type.__name__ = "Integer32"
_Cdx6500TBOPCfgPortTxCoding_Object = MibTableColumn
cdx6500TBOPCfgPortTxCoding = _Cdx6500TBOPCfgPortTxCoding_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 7, 1, 5),
    _Cdx6500TBOPCfgPortTxCoding_Type()
)
cdx6500TBOPCfgPortTxCoding.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500TBOPCfgPortTxCoding.setStatus("mandatory")


class _Cdx6500TBOPCfgPortByteCount_Type(Integer32):
    """Custom type cdx6500TBOPCfgPortByteCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1045),
    )


_Cdx6500TBOPCfgPortByteCount_Type.__name__ = "Integer32"
_Cdx6500TBOPCfgPortByteCount_Object = MibTableColumn
cdx6500TBOPCfgPortByteCount = _Cdx6500TBOPCfgPortByteCount_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 7, 1, 6),
    _Cdx6500TBOPCfgPortByteCount_Type()
)
cdx6500TBOPCfgPortByteCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500TBOPCfgPortByteCount.setStatus("mandatory")


class _Cdx6500TBOPCfgPortEIASigAction_Type(DisplayString):
    """Custom type cdx6500TBOPCfgPortEIASigAction based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(3, 15),
    )


_Cdx6500TBOPCfgPortEIASigAction_Type.__name__ = "DisplayString"
_Cdx6500TBOPCfgPortEIASigAction_Object = MibTableColumn
cdx6500TBOPCfgPortEIASigAction = _Cdx6500TBOPCfgPortEIASigAction_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 7, 1, 7),
    _Cdx6500TBOPCfgPortEIASigAction_Type()
)
cdx6500TBOPCfgPortEIASigAction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500TBOPCfgPortEIASigAction.setStatus("mandatory")


class _Cdx6500TBOPCfgPortOptions_Type(Integer32):
    """Custom type cdx6500TBOPCfgPortOptions based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              50,
              100)
        )
    )
    namedValues = NamedValues(
        *(("cbr", 2),
          ("marki", 1),
          ("nc", 100),
          ("newvalNone", 50),
          ("none", 0))
    )


_Cdx6500TBOPCfgPortOptions_Type.__name__ = "Integer32"
_Cdx6500TBOPCfgPortOptions_Object = MibTableColumn
cdx6500TBOPCfgPortOptions = _Cdx6500TBOPCfgPortOptions_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 7, 1, 8),
    _Cdx6500TBOPCfgPortOptions_Type()
)
cdx6500TBOPCfgPortOptions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500TBOPCfgPortOptions.setStatus("mandatory")


class _Cdx6500TBOPCfgPortRTSCTSDelay_Type(Integer32):
    """Custom type cdx6500TBOPCfgPortRTSCTSDelay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 200),
    )


_Cdx6500TBOPCfgPortRTSCTSDelay_Type.__name__ = "Integer32"
_Cdx6500TBOPCfgPortRTSCTSDelay_Object = MibTableColumn
cdx6500TBOPCfgPortRTSCTSDelay = _Cdx6500TBOPCfgPortRTSCTSDelay_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 7, 1, 9),
    _Cdx6500TBOPCfgPortRTSCTSDelay_Type()
)
cdx6500TBOPCfgPortRTSCTSDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500TBOPCfgPortRTSCTSDelay.setStatus("mandatory")


class _Cdx6500TBOPCfgPortDcdOnDelay_Type(Integer32):
    """Custom type cdx6500TBOPCfgPortDcdOnDelay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_Cdx6500TBOPCfgPortDcdOnDelay_Type.__name__ = "Integer32"
_Cdx6500TBOPCfgPortDcdOnDelay_Object = MibTableColumn
cdx6500TBOPCfgPortDcdOnDelay = _Cdx6500TBOPCfgPortDcdOnDelay_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 7, 1, 10),
    _Cdx6500TBOPCfgPortDcdOnDelay_Type()
)
cdx6500TBOPCfgPortDcdOnDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500TBOPCfgPortDcdOnDelay.setStatus("mandatory")


class _Cdx6500TBOPCfgPortAutoCallMnem_Type(DisplayString):
    """Custom type cdx6500TBOPCfgPortAutoCallMnem based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_Cdx6500TBOPCfgPortAutoCallMnem_Type.__name__ = "DisplayString"
_Cdx6500TBOPCfgPortAutoCallMnem_Object = MibTableColumn
cdx6500TBOPCfgPortAutoCallMnem = _Cdx6500TBOPCfgPortAutoCallMnem_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 7, 1, 11),
    _Cdx6500TBOPCfgPortAutoCallMnem_Type()
)
cdx6500TBOPCfgPortAutoCallMnem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500TBOPCfgPortAutoCallMnem.setStatus("mandatory")


class _Cdx6500TBOPCfgPortAutoCallTO_Type(Integer32):
    """Custom type cdx6500TBOPCfgPortAutoCallTO based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 255),
    )


_Cdx6500TBOPCfgPortAutoCallTO_Type.__name__ = "Integer32"
_Cdx6500TBOPCfgPortAutoCallTO_Object = MibTableColumn
cdx6500TBOPCfgPortAutoCallTO = _Cdx6500TBOPCfgPortAutoCallTO_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 7, 1, 12),
    _Cdx6500TBOPCfgPortAutoCallTO_Type()
)
cdx6500TBOPCfgPortAutoCallTO.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500TBOPCfgPortAutoCallTO.setStatus("mandatory")


class _Cdx6500TBOPCfgPortMaxAutoTries_Type(Integer32):
    """Custom type cdx6500TBOPCfgPortMaxAutoTries based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_Cdx6500TBOPCfgPortMaxAutoTries_Type.__name__ = "Integer32"
_Cdx6500TBOPCfgPortMaxAutoTries_Object = MibTableColumn
cdx6500TBOPCfgPortMaxAutoTries = _Cdx6500TBOPCfgPortMaxAutoTries_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 7, 1, 13),
    _Cdx6500TBOPCfgPortMaxAutoTries_Type()
)
cdx6500TBOPCfgPortMaxAutoTries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500TBOPCfgPortMaxAutoTries.setStatus("mandatory")


class _Cdx6500TBOPCfgPortSubAddress_Type(DisplayString):
    """Custom type cdx6500TBOPCfgPortSubAddress based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 3),
    )


_Cdx6500TBOPCfgPortSubAddress_Type.__name__ = "DisplayString"
_Cdx6500TBOPCfgPortSubAddress_Object = MibTableColumn
cdx6500TBOPCfgPortSubAddress = _Cdx6500TBOPCfgPortSubAddress_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 7, 1, 14),
    _Cdx6500TBOPCfgPortSubAddress_Type()
)
cdx6500TBOPCfgPortSubAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500TBOPCfgPortSubAddress.setStatus("mandatory")


class _Cdx6500TBOPCfgPortCUG_Type(DisplayString):
    """Custom type cdx6500TBOPCfgPortCUG based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 23),
    )


_Cdx6500TBOPCfgPortCUG_Type.__name__ = "DisplayString"
_Cdx6500TBOPCfgPortCUG_Object = MibTableColumn
cdx6500TBOPCfgPortCUG = _Cdx6500TBOPCfgPortCUG_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 7, 1, 15),
    _Cdx6500TBOPCfgPortCUG_Type()
)
cdx6500TBOPCfgPortCUG.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500TBOPCfgPortCUG.setStatus("mandatory")


class _Cdx6500TBOPCfgPortEnableBill_Type(Integer32):
    """Custom type cdx6500TBOPCfgPortEnableBill based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              50)
        )
    )
    namedValues = NamedValues(
        *(("newvalOff", 50),
          ("off", 0),
          ("on", 1))
    )


_Cdx6500TBOPCfgPortEnableBill_Type.__name__ = "Integer32"
_Cdx6500TBOPCfgPortEnableBill_Object = MibTableColumn
cdx6500TBOPCfgPortEnableBill = _Cdx6500TBOPCfgPortEnableBill_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 7, 1, 16),
    _Cdx6500TBOPCfgPortEnableBill_Type()
)
cdx6500TBOPCfgPortEnableBill.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500TBOPCfgPortEnableBill.setStatus("mandatory")


class _Cdx6500TBOPCfgDimType_Type(Integer32):
    """Custom type cdx6500TBOPCfgDimType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              50)
        )
    )
    namedValues = NamedValues(
        *(("newvalOff", 50),
          ("off", 0),
          ("on", 1))
    )


_Cdx6500TBOPCfgDimType_Type.__name__ = "Integer32"
_Cdx6500TBOPCfgDimType_Object = MibTableColumn
cdx6500TBOPCfgDimType = _Cdx6500TBOPCfgDimType_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 7, 1, 17),
    _Cdx6500TBOPCfgDimType_Type()
)
cdx6500TBOPCfgDimType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500TBOPCfgDimType.setStatus("mandatory")


class _Cdx6500TBOPCfgPortMaxRxQSize_Type(Integer32):
    """Custom type cdx6500TBOPCfgPortMaxRxQSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 501),
    )


_Cdx6500TBOPCfgPortMaxRxQSize_Type.__name__ = "Integer32"
_Cdx6500TBOPCfgPortMaxRxQSize_Object = MibTableColumn
cdx6500TBOPCfgPortMaxRxQSize = _Cdx6500TBOPCfgPortMaxRxQSize_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 7, 1, 18),
    _Cdx6500TBOPCfgPortMaxRxQSize_Type()
)
cdx6500TBOPCfgPortMaxRxQSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500TBOPCfgPortMaxRxQSize.setStatus("mandatory")


class _Cdx6500TBOPCfgPortMaxTxQSize_Type(Integer32):
    """Custom type cdx6500TBOPCfgPortMaxTxQSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(16, 800),
    )


_Cdx6500TBOPCfgPortMaxTxQSize_Type.__name__ = "Integer32"
_Cdx6500TBOPCfgPortMaxTxQSize_Object = MibTableColumn
cdx6500TBOPCfgPortMaxTxQSize = _Cdx6500TBOPCfgPortMaxTxQSize_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 7, 1, 19),
    _Cdx6500TBOPCfgPortMaxTxQSize_Type()
)
cdx6500TBOPCfgPortMaxTxQSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500TBOPCfgPortMaxTxQSize.setStatus("mandatory")


class _Cdx6500TBOPCfgPortChanT1E1_Conn_Type(Integer32):
    """Custom type cdx6500TBOPCfgPortChanT1E1_Conn based on Integer32"""
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
          ("no", 1),
          ("yes", 2))
    )


_Cdx6500TBOPCfgPortChanT1E1_Conn_Type.__name__ = "Integer32"
_Cdx6500TBOPCfgPortChanT1E1_Conn_Object = MibScalar
cdx6500TBOPCfgPortChanT1E1_Conn = _Cdx6500TBOPCfgPortChanT1E1_Conn_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 7, 1, 20),
    _Cdx6500TBOPCfgPortChanT1E1_Conn_Type()
)
cdx6500TBOPCfgPortChanT1E1_Conn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500TBOPCfgPortChanT1E1_Conn.setStatus("mandatory")


class _Cdx6500TBOPCfgPortIdleFlagCount_Type(Integer32):
    """Custom type cdx6500TBOPCfgPortIdleFlagCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_Cdx6500TBOPCfgPortIdleFlagCount_Type.__name__ = "Integer32"
_Cdx6500TBOPCfgPortIdleFlagCount_Object = MibTableColumn
cdx6500TBOPCfgPortIdleFlagCount = _Cdx6500TBOPCfgPortIdleFlagCount_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 7, 1, 21),
    _Cdx6500TBOPCfgPortIdleFlagCount_Type()
)
cdx6500TBOPCfgPortIdleFlagCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500TBOPCfgPortIdleFlagCount.setStatus("mandatory")


class _Cdx6500TBOPCfgPortElectricalInterfaceType_Type(Integer32):
    """Custom type cdx6500TBOPCfgPortElectricalInterfaceType based on Integer32"""
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
        *(("none", 5),
          ("v24", 1),
          ("v35", 2),
          ("v36", 3),
          ("x21", 4))
    )


_Cdx6500TBOPCfgPortElectricalInterfaceType_Type.__name__ = "Integer32"
_Cdx6500TBOPCfgPortElectricalInterfaceType_Object = MibTableColumn
cdx6500TBOPCfgPortElectricalInterfaceType = _Cdx6500TBOPCfgPortElectricalInterfaceType_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 7, 1, 22),
    _Cdx6500TBOPCfgPortElectricalInterfaceType_Type()
)
cdx6500TBOPCfgPortElectricalInterfaceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500TBOPCfgPortElectricalInterfaceType.setStatus("mandatory")


class _Cdx6500TBOPCfgPortV24ElectricalInterfaceOption_Type(Integer32):
    """Custom type cdx6500TBOPCfgPortV24ElectricalInterfaceOption based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ri", 1),
          ("tm", 2))
    )


_Cdx6500TBOPCfgPortV24ElectricalInterfaceOption_Type.__name__ = "Integer32"
_Cdx6500TBOPCfgPortV24ElectricalInterfaceOption_Object = MibTableColumn
cdx6500TBOPCfgPortV24ElectricalInterfaceOption = _Cdx6500TBOPCfgPortV24ElectricalInterfaceOption_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 7, 1, 23),
    _Cdx6500TBOPCfgPortV24ElectricalInterfaceOption_Type()
)
cdx6500TBOPCfgPortV24ElectricalInterfaceOption.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500TBOPCfgPortV24ElectricalInterfaceOption.setStatus("mandatory")


class _Cdx6500TBOPCfgPortHighSpeedElectricalInterfaceOption_Type(Integer32):
    """Custom type cdx6500TBOPCfgPortHighSpeedElectricalInterfaceOption based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("xover", 2))
    )


_Cdx6500TBOPCfgPortHighSpeedElectricalInterfaceOption_Type.__name__ = "Integer32"
_Cdx6500TBOPCfgPortHighSpeedElectricalInterfaceOption_Object = MibTableColumn
cdx6500TBOPCfgPortHighSpeedElectricalInterfaceOption = _Cdx6500TBOPCfgPortHighSpeedElectricalInterfaceOption_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 7, 1, 24),
    _Cdx6500TBOPCfgPortHighSpeedElectricalInterfaceOption_Type()
)
cdx6500TBOPCfgPortHighSpeedElectricalInterfaceOption.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500TBOPCfgPortHighSpeedElectricalInterfaceOption.setStatus("mandatory")


class _Cdx6500TBOPCfgPortMaxFrameSize_Type(Integer32):
    """Custom type cdx6500TBOPCfgPortMaxFrameSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16384),
    )


_Cdx6500TBOPCfgPortMaxFrameSize_Type.__name__ = "Integer32"
_Cdx6500TBOPCfgPortMaxFrameSize_Object = MibTableColumn
cdx6500TBOPCfgPortMaxFrameSize = _Cdx6500TBOPCfgPortMaxFrameSize_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 7, 1, 25),
    _Cdx6500TBOPCfgPortMaxFrameSize_Type()
)
cdx6500TBOPCfgPortMaxFrameSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500TBOPCfgPortMaxFrameSize.setStatus("mandatory")
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
_Cdx6500PPSTTBOPPortTable_Object = MibTable
cdx6500PPSTTBOPPortTable = _Cdx6500PPSTTBOPPortTable_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 7)
)
if mibBuilder.loadTexts:
    cdx6500PPSTTBOPPortTable.setStatus("mandatory")
_Cdx6500PPSTTBOPPortEntry_Object = MibTableRow
cdx6500PPSTTBOPPortEntry = _Cdx6500PPSTTBOPPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 7, 1)
)
cdx6500PPSTTBOPPortEntry.setIndexNames(
    (0, "TBOP-OPT-MIB", "cdx6500TBOPStPortNumber"),
)
if mibBuilder.loadTexts:
    cdx6500PPSTTBOPPortEntry.setStatus("mandatory")


class _Cdx6500TBOPStPortNumber_Type(Integer32):
    """Custom type cdx6500TBOPStPortNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 54),
    )


_Cdx6500TBOPStPortNumber_Type.__name__ = "Integer32"
_Cdx6500TBOPStPortNumber_Object = MibTableColumn
cdx6500TBOPStPortNumber = _Cdx6500TBOPStPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 7, 1, 1),
    _Cdx6500TBOPStPortNumber_Type()
)
cdx6500TBOPStPortNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500TBOPStPortNumber.setStatus("mandatory")


class _Cdx6500TBOPStPortStatus_Type(DisplayString):
    """Custom type cdx6500TBOPStPortStatus based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 8),
    )


_Cdx6500TBOPStPortStatus_Type.__name__ = "DisplayString"
_Cdx6500TBOPStPortStatus_Object = MibTableColumn
cdx6500TBOPStPortStatus = _Cdx6500TBOPStPortStatus_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 7, 1, 2),
    _Cdx6500TBOPStPortStatus_Type()
)
cdx6500TBOPStPortStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500TBOPStPortStatus.setStatus("mandatory")


class _Cdx6500TBOPStPortState_Type(DisplayString):
    """Custom type cdx6500TBOPStPortState based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 30),
    )


_Cdx6500TBOPStPortState_Type.__name__ = "DisplayString"
_Cdx6500TBOPStPortState_Object = MibTableColumn
cdx6500TBOPStPortState = _Cdx6500TBOPStPortState_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 7, 1, 3),
    _Cdx6500TBOPStPortState_Type()
)
cdx6500TBOPStPortState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500TBOPStPortState.setStatus("mandatory")
_Cdx6500TBOPStPortSpeed_Type = Integer32
_Cdx6500TBOPStPortSpeed_Object = MibTableColumn
cdx6500TBOPStPortSpeed = _Cdx6500TBOPStPortSpeed_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 7, 1, 4),
    _Cdx6500TBOPStPortSpeed_Type()
)
cdx6500TBOPStPortSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500TBOPStPortSpeed.setStatus("mandatory")
_Cdx6500TBOPStOverrunErrors_Type = Counter16
_Cdx6500TBOPStOverrunErrors_Object = MibTableColumn
cdx6500TBOPStOverrunErrors = _Cdx6500TBOPStOverrunErrors_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 7, 1, 5),
    _Cdx6500TBOPStOverrunErrors_Type()
)
cdx6500TBOPStOverrunErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500TBOPStOverrunErrors.setStatus("mandatory")
_Cdx6500TBOPStUnderrunErrors_Type = Counter16
_Cdx6500TBOPStUnderrunErrors_Object = MibTableColumn
cdx6500TBOPStUnderrunErrors = _Cdx6500TBOPStUnderrunErrors_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 7, 1, 6),
    _Cdx6500TBOPStUnderrunErrors_Type()
)
cdx6500TBOPStUnderrunErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500TBOPStUnderrunErrors.setStatus("mandatory")
_Cdx6500TBOPStCRCErrors_Type = Counter16
_Cdx6500TBOPStCRCErrors_Object = MibTableColumn
cdx6500TBOPStCRCErrors = _Cdx6500TBOPStCRCErrors_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 7, 1, 7),
    _Cdx6500TBOPStCRCErrors_Type()
)
cdx6500TBOPStCRCErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500TBOPStCRCErrors.setStatus("mandatory")
_Cdx6500TBOPStPortRxChars_Type = Counter32
_Cdx6500TBOPStPortRxChars_Object = MibTableColumn
cdx6500TBOPStPortRxChars = _Cdx6500TBOPStPortRxChars_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 7, 1, 8),
    _Cdx6500TBOPStPortRxChars_Type()
)
cdx6500TBOPStPortRxChars.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500TBOPStPortRxChars.setStatus("mandatory")
_Cdx6500TBOPStPortRxCharsSec_Type = Integer32
_Cdx6500TBOPStPortRxCharsSec_Object = MibTableColumn
cdx6500TBOPStPortRxCharsSec = _Cdx6500TBOPStPortRxCharsSec_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 7, 1, 9),
    _Cdx6500TBOPStPortRxCharsSec_Type()
)
cdx6500TBOPStPortRxCharsSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500TBOPStPortRxCharsSec.setStatus("mandatory")
_Cdx6500TBOPStPortRxFrames_Type = Counter32
_Cdx6500TBOPStPortRxFrames_Object = MibTableColumn
cdx6500TBOPStPortRxFrames = _Cdx6500TBOPStPortRxFrames_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 7, 1, 10),
    _Cdx6500TBOPStPortRxFrames_Type()
)
cdx6500TBOPStPortRxFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500TBOPStPortRxFrames.setStatus("mandatory")
_Cdx6500TBOPStPortRxFramesSec_Type = Integer32
_Cdx6500TBOPStPortRxFramesSec_Object = MibTableColumn
cdx6500TBOPStPortRxFramesSec = _Cdx6500TBOPStPortRxFramesSec_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 7, 1, 11),
    _Cdx6500TBOPStPortRxFramesSec_Type()
)
cdx6500TBOPStPortRxFramesSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500TBOPStPortRxFramesSec.setStatus("mandatory")
_Cdx6500TBOPStPortTxChars_Type = Counter32
_Cdx6500TBOPStPortTxChars_Object = MibTableColumn
cdx6500TBOPStPortTxChars = _Cdx6500TBOPStPortTxChars_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 7, 1, 12),
    _Cdx6500TBOPStPortTxChars_Type()
)
cdx6500TBOPStPortTxChars.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500TBOPStPortTxChars.setStatus("mandatory")
_Cdx6500TBOPStPortTxCharsSec_Type = Integer32
_Cdx6500TBOPStPortTxCharsSec_Object = MibTableColumn
cdx6500TBOPStPortTxCharsSec = _Cdx6500TBOPStPortTxCharsSec_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 7, 1, 13),
    _Cdx6500TBOPStPortTxCharsSec_Type()
)
cdx6500TBOPStPortTxCharsSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500TBOPStPortTxCharsSec.setStatus("mandatory")
_Cdx6500TBOPStPortTxFrames_Type = Counter32
_Cdx6500TBOPStPortTxFrames_Object = MibTableColumn
cdx6500TBOPStPortTxFrames = _Cdx6500TBOPStPortTxFrames_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 7, 1, 14),
    _Cdx6500TBOPStPortTxFrames_Type()
)
cdx6500TBOPStPortTxFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500TBOPStPortTxFrames.setStatus("mandatory")
_Cdx6500TBOPStPortTxFramesSec_Type = Integer32
_Cdx6500TBOPStPortTxFramesSec_Object = MibTableColumn
cdx6500TBOPStPortTxFramesSec = _Cdx6500TBOPStPortTxFramesSec_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 7, 1, 15),
    _Cdx6500TBOPStPortTxFramesSec_Type()
)
cdx6500TBOPStPortTxFramesSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500TBOPStPortTxFramesSec.setStatus("mandatory")


class _Cdx6500TBOPStPortRxUtil_Type(Integer32):
    """Custom type cdx6500TBOPStPortRxUtil based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_Cdx6500TBOPStPortRxUtil_Type.__name__ = "Integer32"
_Cdx6500TBOPStPortRxUtil_Object = MibTableColumn
cdx6500TBOPStPortRxUtil = _Cdx6500TBOPStPortRxUtil_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 7, 1, 16),
    _Cdx6500TBOPStPortRxUtil_Type()
)
cdx6500TBOPStPortRxUtil.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500TBOPStPortRxUtil.setStatus("mandatory")


class _Cdx6500TBOPStPortTxUtil_Type(Integer32):
    """Custom type cdx6500TBOPStPortTxUtil based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_Cdx6500TBOPStPortTxUtil_Type.__name__ = "Integer32"
_Cdx6500TBOPStPortTxUtil_Object = MibTableColumn
cdx6500TBOPStPortTxUtil = _Cdx6500TBOPStPortTxUtil_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 7, 1, 17),
    _Cdx6500TBOPStPortTxUtil_Type()
)
cdx6500TBOPStPortTxUtil.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500TBOPStPortTxUtil.setStatus("mandatory")
_Cdx6500TBOPStPortFramesQueued_Type = Counter32
_Cdx6500TBOPStPortFramesQueued_Object = MibTableColumn
cdx6500TBOPStPortFramesQueued = _Cdx6500TBOPStPortFramesQueued_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 7, 1, 18),
    _Cdx6500TBOPStPortFramesQueued_Type()
)
cdx6500TBOPStPortFramesQueued.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500TBOPStPortFramesQueued.setStatus("mandatory")
_Cdx6500Controls_ObjectIdentity = ObjectIdentity
cdx6500Controls = _Cdx6500Controls_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 4)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TBOP-OPT-MIB",
    **{"Counter16": Counter16,
       "DisplayString": DisplayString,
       "codex": codex,
       "cdxProductSpecific": cdxProductSpecific,
       "cdx6500": cdx6500,
       "cdx6500Configuration": cdx6500Configuration,
       "cdx6500CfgProtocolGroup": cdx6500CfgProtocolGroup,
       "cdx6500PCTPortProtocolGroup": cdx6500PCTPortProtocolGroup,
       "cdx6500PPCTTBOPPortTable": cdx6500PPCTTBOPPortTable,
       "cdx6500PPCTTBOPPortEntry": cdx6500PPCTTBOPPortEntry,
       "cdx6500TBOPCfgPortNumber": cdx6500TBOPCfgPortNumber,
       "cdx6500TBOPCfgPortEIAOpt": cdx6500TBOPCfgPortEIAOpt,
       "cdx6500TBOPCfgPortClockType": cdx6500TBOPCfgPortClockType,
       "cdx6500TBOPCfgPortClockSpeed": cdx6500TBOPCfgPortClockSpeed,
       "cdx6500TBOPCfgPortTxCoding": cdx6500TBOPCfgPortTxCoding,
       "cdx6500TBOPCfgPortByteCount": cdx6500TBOPCfgPortByteCount,
       "cdx6500TBOPCfgPortEIASigAction": cdx6500TBOPCfgPortEIASigAction,
       "cdx6500TBOPCfgPortOptions": cdx6500TBOPCfgPortOptions,
       "cdx6500TBOPCfgPortRTSCTSDelay": cdx6500TBOPCfgPortRTSCTSDelay,
       "cdx6500TBOPCfgPortDcdOnDelay": cdx6500TBOPCfgPortDcdOnDelay,
       "cdx6500TBOPCfgPortAutoCallMnem": cdx6500TBOPCfgPortAutoCallMnem,
       "cdx6500TBOPCfgPortAutoCallTO": cdx6500TBOPCfgPortAutoCallTO,
       "cdx6500TBOPCfgPortMaxAutoTries": cdx6500TBOPCfgPortMaxAutoTries,
       "cdx6500TBOPCfgPortSubAddress": cdx6500TBOPCfgPortSubAddress,
       "cdx6500TBOPCfgPortCUG": cdx6500TBOPCfgPortCUG,
       "cdx6500TBOPCfgPortEnableBill": cdx6500TBOPCfgPortEnableBill,
       "cdx6500TBOPCfgDimType": cdx6500TBOPCfgDimType,
       "cdx6500TBOPCfgPortMaxRxQSize": cdx6500TBOPCfgPortMaxRxQSize,
       "cdx6500TBOPCfgPortMaxTxQSize": cdx6500TBOPCfgPortMaxTxQSize,
       "cdx6500TBOPCfgPortChanT1E1-Conn": cdx6500TBOPCfgPortChanT1E1_Conn,
       "cdx6500TBOPCfgPortIdleFlagCount": cdx6500TBOPCfgPortIdleFlagCount,
       "cdx6500TBOPCfgPortElectricalInterfaceType": cdx6500TBOPCfgPortElectricalInterfaceType,
       "cdx6500TBOPCfgPortV24ElectricalInterfaceOption": cdx6500TBOPCfgPortV24ElectricalInterfaceOption,
       "cdx6500TBOPCfgPortHighSpeedElectricalInterfaceOption": cdx6500TBOPCfgPortHighSpeedElectricalInterfaceOption,
       "cdx6500TBOPCfgPortMaxFrameSize": cdx6500TBOPCfgPortMaxFrameSize,
       "cdx6500Statistics": cdx6500Statistics,
       "cdx6500StatProtocolGroup": cdx6500StatProtocolGroup,
       "cdx6500PSTPortProtocolGroup": cdx6500PSTPortProtocolGroup,
       "cdx6500PPSTTBOPPortTable": cdx6500PPSTTBOPPortTable,
       "cdx6500PPSTTBOPPortEntry": cdx6500PPSTTBOPPortEntry,
       "cdx6500TBOPStPortNumber": cdx6500TBOPStPortNumber,
       "cdx6500TBOPStPortStatus": cdx6500TBOPStPortStatus,
       "cdx6500TBOPStPortState": cdx6500TBOPStPortState,
       "cdx6500TBOPStPortSpeed": cdx6500TBOPStPortSpeed,
       "cdx6500TBOPStOverrunErrors": cdx6500TBOPStOverrunErrors,
       "cdx6500TBOPStUnderrunErrors": cdx6500TBOPStUnderrunErrors,
       "cdx6500TBOPStCRCErrors": cdx6500TBOPStCRCErrors,
       "cdx6500TBOPStPortRxChars": cdx6500TBOPStPortRxChars,
       "cdx6500TBOPStPortRxCharsSec": cdx6500TBOPStPortRxCharsSec,
       "cdx6500TBOPStPortRxFrames": cdx6500TBOPStPortRxFrames,
       "cdx6500TBOPStPortRxFramesSec": cdx6500TBOPStPortRxFramesSec,
       "cdx6500TBOPStPortTxChars": cdx6500TBOPStPortTxChars,
       "cdx6500TBOPStPortTxCharsSec": cdx6500TBOPStPortTxCharsSec,
       "cdx6500TBOPStPortTxFrames": cdx6500TBOPStPortTxFrames,
       "cdx6500TBOPStPortTxFramesSec": cdx6500TBOPStPortTxFramesSec,
       "cdx6500TBOPStPortRxUtil": cdx6500TBOPStPortRxUtil,
       "cdx6500TBOPStPortTxUtil": cdx6500TBOPStPortTxUtil,
       "cdx6500TBOPStPortFramesQueued": cdx6500TBOPStPortFramesQueued,
       "cdx6500Controls": cdx6500Controls}
)
