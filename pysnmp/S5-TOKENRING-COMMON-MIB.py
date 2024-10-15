# SNMP MIB module (S5-TOKENRING-COMMON-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/S5-TOKENRING-COMMON-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:49:12 2024
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

(SrcIndx,
 TimeIntervalSec) = mibBuilder.importSymbols(
    "S5-TCS-MIB",
    "SrcIndx",
    "TimeIntervalSec")

(s5TrCfg,
 s5TrStat) = mibBuilder.importSymbols(
    "S5-TOKENRING-MIB",
    "s5TrCfg",
    "s5TrStat")

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
 MacAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "TextualConvention")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_S5TrPortTable_Object = MibTable
s5TrPortTable = _S5TrPortTable_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 7, 1, 1)
)
if mibBuilder.loadTexts:
    s5TrPortTable.setStatus("mandatory")
_S5TrPortEntry_Object = MibTableRow
s5TrPortEntry = _S5TrPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 7, 1, 1, 1)
)
s5TrPortEntry.setIndexNames(
    (0, "S5-TOKENRING-COMMON-MIB", "s5TrPortBrdIndx"),
    (0, "S5-TOKENRING-COMMON-MIB", "s5TrPortIndx"),
)
if mibBuilder.loadTexts:
    s5TrPortEntry.setStatus("mandatory")


class _S5TrPortBrdIndx_Type(Integer32):
    """Custom type s5TrPortBrdIndx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_S5TrPortBrdIndx_Type.__name__ = "Integer32"
_S5TrPortBrdIndx_Object = MibTableColumn
s5TrPortBrdIndx = _S5TrPortBrdIndx_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 7, 1, 1, 1, 1),
    _S5TrPortBrdIndx_Type()
)
s5TrPortBrdIndx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s5TrPortBrdIndx.setStatus("mandatory")


class _S5TrPortIndx_Type(Integer32):
    """Custom type s5TrPortIndx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_S5TrPortIndx_Type.__name__ = "Integer32"
_S5TrPortIndx_Object = MibTableColumn
s5TrPortIndx = _S5TrPortIndx_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 7, 1, 1, 1, 2),
    _S5TrPortIndx_Type()
)
s5TrPortIndx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s5TrPortIndx.setStatus("mandatory")


class _S5TrPortWrapStatus_Type(Integer32):
    """Custom type s5TrPortWrapStatus based on Integer32"""
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
        *(("connect", 3),
          ("hostBecaonWrap", 8),
          ("nmmBeaconWrap", 5),
          ("other", 1),
          ("permBeaconWrap", 7),
          ("timedWrap", 4),
          ("wrap", 2),
          ("wrongSpeedWrap", 6))
    )


_S5TrPortWrapStatus_Type.__name__ = "Integer32"
_S5TrPortWrapStatus_Object = MibTableColumn
s5TrPortWrapStatus = _S5TrPortWrapStatus_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 7, 1, 1, 1, 3),
    _S5TrPortWrapStatus_Type()
)
s5TrPortWrapStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    s5TrPortWrapStatus.setStatus("mandatory")
_S5TrPortWrapTime_Type = TimeIntervalSec
_S5TrPortWrapTime_Object = MibTableColumn
s5TrPortWrapTime = _S5TrPortWrapTime_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 7, 1, 1, 1, 4),
    _S5TrPortWrapTime_Type()
)
s5TrPortWrapTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    s5TrPortWrapTime.setStatus("mandatory")


class _S5TrPortInsrtStatus_Type(Integer32):
    """Custom type s5TrPortInsrtStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("inserted", 3),
          ("notInserted", 2),
          ("other", 1))
    )


_S5TrPortInsrtStatus_Type.__name__ = "Integer32"
_S5TrPortInsrtStatus_Object = MibTableColumn
s5TrPortInsrtStatus = _S5TrPortInsrtStatus_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 7, 1, 1, 1, 5),
    _S5TrPortInsrtStatus_Type()
)
s5TrPortInsrtStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s5TrPortInsrtStatus.setStatus("mandatory")


class _S5TrPortPhanStatus_Type(Integer32):
    """Custom type s5TrPortPhanStatus based on Integer32"""
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
        *(("noPhantom", 2),
          ("other", 1),
          ("phantom", 3),
          ("softwarePhantom", 4))
    )


_S5TrPortPhanStatus_Type.__name__ = "Integer32"
_S5TrPortPhanStatus_Object = MibTableColumn
s5TrPortPhanStatus = _S5TrPortPhanStatus_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 7, 1, 1, 1, 6),
    _S5TrPortPhanStatus_Type()
)
s5TrPortPhanStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s5TrPortPhanStatus.setStatus("mandatory")
_S5TrPortPhanChngs_Type = Counter32
_S5TrPortPhanChngs_Object = MibTableColumn
s5TrPortPhanChngs = _S5TrPortPhanChngs_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 7, 1, 1, 1, 7),
    _S5TrPortPhanChngs_Type()
)
s5TrPortPhanChngs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s5TrPortPhanChngs.setStatus("mandatory")


class _S5TrPortTrnkAccMthdStrap_Type(Integer32):
    """Custom type s5TrPortTrnkAccMthdStrap based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("none", 3),
          ("notSupported", 1),
          ("synoptics", 2))
    )


_S5TrPortTrnkAccMthdStrap_Type.__name__ = "Integer32"
_S5TrPortTrnkAccMthdStrap_Object = MibTableColumn
s5TrPortTrnkAccMthdStrap = _S5TrPortTrnkAccMthdStrap_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 7, 1, 1, 1, 8),
    _S5TrPortTrnkAccMthdStrap_Type()
)
s5TrPortTrnkAccMthdStrap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s5TrPortTrnkAccMthdStrap.setStatus("mandatory")


class _S5TrPortTrnkAccMthd_Type(Integer32):
    """Custom type s5TrPortTrnkAccMthd based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("none", 3),
          ("notSupported", 1),
          ("synoptics", 2))
    )


_S5TrPortTrnkAccMthd_Type.__name__ = "Integer32"
_S5TrPortTrnkAccMthd_Object = MibTableColumn
s5TrPortTrnkAccMthd = _S5TrPortTrnkAccMthd_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 7, 1, 1, 1, 9),
    _S5TrPortTrnkAccMthd_Type()
)
s5TrPortTrnkAccMthd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    s5TrPortTrnkAccMthd.setStatus("mandatory")


class _S5TrPortClass_Type(Integer32):
    """Custom type s5TrPortClass based on Integer32"""
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
        *(("internal", 5),
          ("lobe", 4),
          ("other", 1),
          ("ri", 2),
          ("ro", 3))
    )


_S5TrPortClass_Type.__name__ = "Integer32"
_S5TrPortClass_Object = MibTableColumn
s5TrPortClass = _S5TrPortClass_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 7, 1, 1, 1, 10),
    _S5TrPortClass_Type()
)
s5TrPortClass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s5TrPortClass.setStatus("mandatory")


class _S5TrPortMedia_Type(Integer32):
    """Custom type s5TrPortMedia based on Integer32"""
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
        *(("copperActive", 4),
          ("copperPassive", 5),
          ("mac", 6),
          ("other", 1),
          ("specialProc", 7),
          ("stdFiber", 3),
          ("synFiber", 2))
    )


_S5TrPortMedia_Type.__name__ = "Integer32"
_S5TrPortMedia_Object = MibTableColumn
s5TrPortMedia = _S5TrPortMedia_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 7, 1, 1, 1, 11),
    _S5TrPortMedia_Type()
)
s5TrPortMedia.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s5TrPortMedia.setStatus("mandatory")


class _S5TrPortConnector_Type(Integer32):
    """Custom type s5TrPortConnector based on Integer32"""
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
        *(("db9", 3),
          ("fiberST", 5),
          ("internal", 2),
          ("other", 1),
          ("rj45", 4))
    )


_S5TrPortConnector_Type.__name__ = "Integer32"
_S5TrPortConnector_Object = MibTableColumn
s5TrPortConnector = _S5TrPortConnector_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 7, 1, 1, 1, 12),
    _S5TrPortConnector_Type()
)
s5TrPortConnector.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s5TrPortConnector.setStatus("mandatory")


class _S5TrPortSoftwareInsertion_Type(Integer32):
    """Custom type s5TrPortSoftwareInsertion based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("capableAndSoftwareInsertionOff", 3),
          ("capableAndSoftwareInsertionOn", 2),
          ("notCapableOfSoftwareInsertion", 1))
    )


_S5TrPortSoftwareInsertion_Type.__name__ = "Integer32"
_S5TrPortSoftwareInsertion_Object = MibTableColumn
s5TrPortSoftwareInsertion = _S5TrPortSoftwareInsertion_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 7, 1, 1, 1, 13),
    _S5TrPortSoftwareInsertion_Type()
)
s5TrPortSoftwareInsertion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    s5TrPortSoftwareInsertion.setStatus("mandatory")


class _S5TrPortAFD_Type(Integer32):
    """Custom type s5TrPortAFD based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("capableAndAFDDisabled", 3),
          ("capableAndAFDEnabled", 2),
          ("notCapableOfAFDDisable", 1))
    )


_S5TrPortAFD_Type.__name__ = "Integer32"
_S5TrPortAFD_Object = MibTableColumn
s5TrPortAFD = _S5TrPortAFD_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 7, 1, 1, 1, 14),
    _S5TrPortAFD_Type()
)
s5TrPortAFD.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    s5TrPortAFD.setStatus("mandatory")
_S5TrFpuTable_Object = MibTable
s5TrFpuTable = _S5TrFpuTable_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 7, 1, 2)
)
if mibBuilder.loadTexts:
    s5TrFpuTable.setStatus("mandatory")
_S5TrFpuEntry_Object = MibTableRow
s5TrFpuEntry = _S5TrFpuEntry_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 7, 1, 2, 1)
)
s5TrFpuEntry.setIndexNames(
    (0, "S5-TOKENRING-COMMON-MIB", "s5TrFpuBrdIndx"),
    (0, "S5-TOKENRING-COMMON-MIB", "s5TrFpuIndx"),
)
if mibBuilder.loadTexts:
    s5TrFpuEntry.setStatus("mandatory")


class _S5TrFpuBrdIndx_Type(Integer32):
    """Custom type s5TrFpuBrdIndx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_S5TrFpuBrdIndx_Type.__name__ = "Integer32"
_S5TrFpuBrdIndx_Object = MibTableColumn
s5TrFpuBrdIndx = _S5TrFpuBrdIndx_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 7, 1, 2, 1, 1),
    _S5TrFpuBrdIndx_Type()
)
s5TrFpuBrdIndx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s5TrFpuBrdIndx.setStatus("mandatory")


class _S5TrFpuIndx_Type(Integer32):
    """Custom type s5TrFpuIndx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_S5TrFpuIndx_Type.__name__ = "Integer32"
_S5TrFpuIndx_Object = MibTableColumn
s5TrFpuIndx = _S5TrFpuIndx_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 7, 1, 2, 1, 2),
    _S5TrFpuIndx_Type()
)
s5TrFpuIndx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s5TrFpuIndx.setStatus("mandatory")


class _S5TrFpuType_Type(Integer32):
    """Custom type s5TrFpuType based on Integer32"""
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
        *(("cluster", 2),
          ("other", 1),
          ("port", 3),
          ("roving", 4))
    )


_S5TrFpuType_Type.__name__ = "Integer32"
_S5TrFpuType_Object = MibTableColumn
s5TrFpuType = _S5TrFpuType_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 7, 1, 2, 1, 3),
    _S5TrFpuType_Type()
)
s5TrFpuType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s5TrFpuType.setStatus("mandatory")


class _S5TrFpuTypeIndx_Type(Integer32):
    """Custom type s5TrFpuTypeIndx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_S5TrFpuTypeIndx_Type.__name__ = "Integer32"
_S5TrFpuTypeIndx_Object = MibTableColumn
s5TrFpuTypeIndx = _S5TrFpuTypeIndx_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 7, 1, 2, 1, 4),
    _S5TrFpuTypeIndx_Type()
)
s5TrFpuTypeIndx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s5TrFpuTypeIndx.setStatus("mandatory")


class _S5TrFpuVer_Type(DisplayString):
    """Custom type s5TrFpuVer based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_S5TrFpuVer_Type.__name__ = "DisplayString"
_S5TrFpuVer_Object = MibTableColumn
s5TrFpuVer = _S5TrFpuVer_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 7, 1, 2, 1, 5),
    _S5TrFpuVer_Type()
)
s5TrFpuVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s5TrFpuVer.setStatus("obsolete")


class _S5TrFpuCapabilites_Type(Integer32):
    """Custom type s5TrFpuCapabilites based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("coreStatistics", 2),
          ("embeddedManagement", 3),
          ("other", 1))
    )


_S5TrFpuCapabilites_Type.__name__ = "Integer32"
_S5TrFpuCapabilites_Object = MibTableColumn
s5TrFpuCapabilites = _S5TrFpuCapabilites_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 7, 1, 2, 1, 6),
    _S5TrFpuCapabilites_Type()
)
s5TrFpuCapabilites.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s5TrFpuCapabilites.setStatus("mandatory")


class _S5TrFpuRunningMode_Type(Integer32):
    """Custom type s5TrFpuRunningMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("coreStatistics", 2),
          ("other", 1),
          ("rovingFPU", 4),
          ("securityRoving", 5))
    )


_S5TrFpuRunningMode_Type.__name__ = "Integer32"
_S5TrFpuRunningMode_Object = MibTableColumn
s5TrFpuRunningMode = _S5TrFpuRunningMode_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 7, 1, 2, 1, 7),
    _S5TrFpuRunningMode_Type()
)
s5TrFpuRunningMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    s5TrFpuRunningMode.setStatus("mandatory")
_S5TrAttTable_Object = MibTable
s5TrAttTable = _S5TrAttTable_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 7, 1, 3)
)
if mibBuilder.loadTexts:
    s5TrAttTable.setStatus("mandatory")
_S5TrAttEntry_Object = MibTableRow
s5TrAttEntry = _S5TrAttEntry_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 7, 1, 3, 1)
)
s5TrAttEntry.setIndexNames(
    (0, "S5-TOKENRING-COMMON-MIB", "s5TrAttBrdIndx"),
    (0, "S5-TOKENRING-COMMON-MIB", "s5TrAttIndx"),
)
if mibBuilder.loadTexts:
    s5TrAttEntry.setStatus("mandatory")


class _S5TrAttBrdIndx_Type(Integer32):
    """Custom type s5TrAttBrdIndx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_S5TrAttBrdIndx_Type.__name__ = "Integer32"
_S5TrAttBrdIndx_Object = MibTableColumn
s5TrAttBrdIndx = _S5TrAttBrdIndx_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 7, 1, 3, 1, 1),
    _S5TrAttBrdIndx_Type()
)
s5TrAttBrdIndx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s5TrAttBrdIndx.setStatus("mandatory")


class _S5TrAttIndx_Type(Integer32):
    """Custom type s5TrAttIndx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_S5TrAttIndx_Type.__name__ = "Integer32"
_S5TrAttIndx_Object = MibTableColumn
s5TrAttIndx = _S5TrAttIndx_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 7, 1, 3, 1, 2),
    _S5TrAttIndx_Type()
)
s5TrAttIndx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s5TrAttIndx.setStatus("mandatory")


class _S5TrAttDfltSpeed_Type(Integer32):
    """Custom type s5TrAttDfltSpeed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("s16Mbit", 3),
          ("s4Mbit", 2))
    )


_S5TrAttDfltSpeed_Type.__name__ = "Integer32"
_S5TrAttDfltSpeed_Object = MibTableColumn
s5TrAttDfltSpeed = _S5TrAttDfltSpeed_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 7, 1, 3, 1, 3),
    _S5TrAttDfltSpeed_Type()
)
s5TrAttDfltSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s5TrAttDfltSpeed.setStatus("mandatory")


class _S5TrAttCurSpeed_Type(Integer32):
    """Custom type s5TrAttCurSpeed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("s16Mbit", 3),
          ("s4Mbit", 2))
    )


_S5TrAttCurSpeed_Type.__name__ = "Integer32"
_S5TrAttCurSpeed_Object = MibTableColumn
s5TrAttCurSpeed = _S5TrAttCurSpeed_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 7, 1, 3, 1, 4),
    _S5TrAttCurSpeed_Type()
)
s5TrAttCurSpeed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    s5TrAttCurSpeed.setStatus("mandatory")


class _S5TrAttFault_Type(Integer32):
    """Custom type s5TrAttFault based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("fault", 3),
          ("nofault", 2),
          ("other", 1))
    )


_S5TrAttFault_Type.__name__ = "Integer32"
_S5TrAttFault_Object = MibTableColumn
s5TrAttFault = _S5TrAttFault_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 7, 1, 3, 1, 5),
    _S5TrAttFault_Type()
)
s5TrAttFault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s5TrAttFault.setStatus("mandatory")


class _S5TrBkDiv_Type(Integer32):
    """Custom type s5TrBkDiv based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("join", 3),
          ("other", 1),
          ("split", 2))
    )


_S5TrBkDiv_Type.__name__ = "Integer32"
_S5TrBkDiv_Object = MibScalar
s5TrBkDiv = _S5TrBkDiv_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 7, 1, 4),
    _S5TrBkDiv_Type()
)
s5TrBkDiv.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    s5TrBkDiv.setStatus("mandatory")
_S5TrRingExt_ObjectIdentity = ObjectIdentity
s5TrRingExt = _S5TrRingExt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 7, 1, 5)
)
_S5TrRingExtLastChange_Type = TimeTicks
_S5TrRingExtLastChange_Object = MibScalar
s5TrRingExtLastChange = _S5TrRingExtLastChange_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 7, 1, 5, 1),
    _S5TrRingExtLastChange_Type()
)
s5TrRingExtLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s5TrRingExtLastChange.setStatus("mandatory")


class _S5TrRingExtCurNum_Type(Integer32):
    """Custom type s5TrRingExtCurNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_S5TrRingExtCurNum_Type.__name__ = "Integer32"
_S5TrRingExtCurNum_Object = MibScalar
s5TrRingExtCurNum = _S5TrRingExtCurNum_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 7, 1, 5, 2),
    _S5TrRingExtCurNum_Type()
)
s5TrRingExtCurNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s5TrRingExtCurNum.setStatus("mandatory")
_S5TrRingExtTable_Object = MibTable
s5TrRingExtTable = _S5TrRingExtTable_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 7, 1, 5, 3)
)
if mibBuilder.loadTexts:
    s5TrRingExtTable.setStatus("mandatory")
_S5TrRingExtEntry_Object = MibTableRow
s5TrRingExtEntry = _S5TrRingExtEntry_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 7, 1, 5, 3, 1)
)
s5TrRingExtEntry.setIndexNames(
    (0, "S5-TOKENRING-COMMON-MIB", "s5TrRingExtBoardIndx"),
    (0, "S5-TOKENRING-COMMON-MIB", "s5TrRingExtExtensionIndx"),
)
if mibBuilder.loadTexts:
    s5TrRingExtEntry.setStatus("mandatory")


class _S5TrRingExtBoardIndx_Type(Integer32):
    """Custom type s5TrRingExtBoardIndx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_S5TrRingExtBoardIndx_Type.__name__ = "Integer32"
_S5TrRingExtBoardIndx_Object = MibTableColumn
s5TrRingExtBoardIndx = _S5TrRingExtBoardIndx_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 7, 1, 5, 3, 1, 1),
    _S5TrRingExtBoardIndx_Type()
)
s5TrRingExtBoardIndx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s5TrRingExtBoardIndx.setStatus("mandatory")


class _S5TrRingExtExtensionIndx_Type(Integer32):
    """Custom type s5TrRingExtExtensionIndx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_S5TrRingExtExtensionIndx_Type.__name__ = "Integer32"
_S5TrRingExtExtensionIndx_Object = MibTableColumn
s5TrRingExtExtensionIndx = _S5TrRingExtExtensionIndx_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 7, 1, 5, 3, 1, 2),
    _S5TrRingExtExtensionIndx_Type()
)
s5TrRingExtExtensionIndx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s5TrRingExtExtensionIndx.setStatus("mandatory")


class _S5TrRingExtRingNumber_Type(Integer32):
    """Custom type s5TrRingExtRingNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_S5TrRingExtRingNumber_Type.__name__ = "Integer32"
_S5TrRingExtRingNumber_Object = MibTableColumn
s5TrRingExtRingNumber = _S5TrRingExtRingNumber_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 7, 1, 5, 3, 1, 3),
    _S5TrRingExtRingNumber_Type()
)
s5TrRingExtRingNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s5TrRingExtRingNumber.setStatus("mandatory")
_S5TrRingExtRingInUna_Type = MacAddress
_S5TrRingExtRingInUna_Object = MibTableColumn
s5TrRingExtRingInUna = _S5TrRingExtRingInUna_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 7, 1, 5, 3, 1, 4),
    _S5TrRingExtRingInUna_Type()
)
s5TrRingExtRingInUna.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s5TrRingExtRingInUna.setStatus("mandatory")
_S5TrRingExtRingOutUna_Type = MacAddress
_S5TrRingExtRingOutUna_Object = MibTableColumn
s5TrRingExtRingOutUna = _S5TrRingExtRingOutUna_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 7, 1, 5, 3, 1, 5),
    _S5TrRingExtRingOutUna_Type()
)
s5TrRingExtRingOutUna.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s5TrRingExtRingOutUna.setStatus("mandatory")
_S5TrRingExtSecUna_Type = MacAddress
_S5TrRingExtSecUna_Object = MibTableColumn
s5TrRingExtSecUna = _S5TrRingExtSecUna_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 7, 1, 5, 3, 1, 6),
    _S5TrRingExtSecUna_Type()
)
s5TrRingExtSecUna.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s5TrRingExtSecUna.setStatus("mandatory")


class _S5TrRingExtRingInPhanStatus_Type(Integer32):
    """Custom type s5TrRingExtRingInPhanStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("noPhantom", 2),
          ("other", 1),
          ("phantom", 3))
    )


_S5TrRingExtRingInPhanStatus_Type.__name__ = "Integer32"
_S5TrRingExtRingInPhanStatus_Object = MibTableColumn
s5TrRingExtRingInPhanStatus = _S5TrRingExtRingInPhanStatus_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 7, 1, 5, 3, 1, 7),
    _S5TrRingExtRingInPhanStatus_Type()
)
s5TrRingExtRingInPhanStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s5TrRingExtRingInPhanStatus.setStatus("mandatory")


class _S5TrRingExtRingOutPhanStatus_Type(Integer32):
    """Custom type s5TrRingExtRingOutPhanStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("noPhantom", 2),
          ("other", 1),
          ("phantom", 3))
    )


_S5TrRingExtRingOutPhanStatus_Type.__name__ = "Integer32"
_S5TrRingExtRingOutPhanStatus_Object = MibTableColumn
s5TrRingExtRingOutPhanStatus = _S5TrRingExtRingOutPhanStatus_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 7, 1, 5, 3, 1, 8),
    _S5TrRingExtRingOutPhanStatus_Type()
)
s5TrRingExtRingOutPhanStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s5TrRingExtRingOutPhanStatus.setStatus("mandatory")


class _S5TrRingExtRingInWrapStatus_Type(Integer32):
    """Custom type s5TrRingExtRingInWrapStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("connect", 3),
          ("other", 1),
          ("wrap", 2))
    )


_S5TrRingExtRingInWrapStatus_Type.__name__ = "Integer32"
_S5TrRingExtRingInWrapStatus_Object = MibTableColumn
s5TrRingExtRingInWrapStatus = _S5TrRingExtRingInWrapStatus_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 7, 1, 5, 3, 1, 9),
    _S5TrRingExtRingInWrapStatus_Type()
)
s5TrRingExtRingInWrapStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s5TrRingExtRingInWrapStatus.setStatus("mandatory")


class _S5TrRingExtRingOutWrapStatus_Type(Integer32):
    """Custom type s5TrRingExtRingOutWrapStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("connect", 3),
          ("other", 1),
          ("wrap", 2))
    )


_S5TrRingExtRingOutWrapStatus_Type.__name__ = "Integer32"
_S5TrRingExtRingOutWrapStatus_Object = MibTableColumn
s5TrRingExtRingOutWrapStatus = _S5TrRingExtRingOutWrapStatus_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 7, 1, 5, 3, 1, 10),
    _S5TrRingExtRingOutWrapStatus_Type()
)
s5TrRingExtRingOutWrapStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s5TrRingExtRingOutWrapStatus.setStatus("mandatory")


class _S5TrRingExtClusterNumber_Type(Integer32):
    """Custom type s5TrRingExtClusterNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_S5TrRingExtClusterNumber_Type.__name__ = "Integer32"
_S5TrRingExtClusterNumber_Object = MibTableColumn
s5TrRingExtClusterNumber = _S5TrRingExtClusterNumber_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 7, 1, 5, 3, 1, 11),
    _S5TrRingExtClusterNumber_Type()
)
s5TrRingExtClusterNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s5TrRingExtClusterNumber.setStatus("mandatory")


class _S5TrRingExtRingInPortNumber_Type(Integer32):
    """Custom type s5TrRingExtRingInPortNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_S5TrRingExtRingInPortNumber_Type.__name__ = "Integer32"
_S5TrRingExtRingInPortNumber_Object = MibTableColumn
s5TrRingExtRingInPortNumber = _S5TrRingExtRingInPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 7, 1, 5, 3, 1, 12),
    _S5TrRingExtRingInPortNumber_Type()
)
s5TrRingExtRingInPortNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s5TrRingExtRingInPortNumber.setStatus("mandatory")


class _S5TrRingExtRingOutPortNumber_Type(Integer32):
    """Custom type s5TrRingExtRingOutPortNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_S5TrRingExtRingOutPortNumber_Type.__name__ = "Integer32"
_S5TrRingExtRingOutPortNumber_Object = MibTableColumn
s5TrRingExtRingOutPortNumber = _S5TrRingExtRingOutPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 7, 1, 5, 3, 1, 13),
    _S5TrRingExtRingOutPortNumber_Type()
)
s5TrRingExtRingOutPortNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s5TrRingExtRingOutPortNumber.setStatus("mandatory")


class _S5TrRingExtEosSize_Type(Integer32):
    """Custom type s5TrRingExtEosSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1400),
    )


_S5TrRingExtEosSize_Type.__name__ = "Integer32"
_S5TrRingExtEosSize_Object = MibScalar
s5TrRingExtEosSize = _S5TrRingExtEosSize_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 7, 1, 5, 4),
    _S5TrRingExtEosSize_Type()
)
s5TrRingExtEosSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s5TrRingExtEosSize.setStatus("mandatory")
_S5TrRingExtEosTable_Object = MibTable
s5TrRingExtEosTable = _S5TrRingExtEosTable_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 7, 1, 5, 5)
)
if mibBuilder.loadTexts:
    s5TrRingExtEosTable.setStatus("mandatory")
_S5TrRingExtEosEntry_Object = MibTableRow
s5TrRingExtEosEntry = _S5TrRingExtEosEntry_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 7, 1, 5, 5, 1)
)
s5TrRingExtEosEntry.setIndexNames(
    (0, "S5-TOKENRING-COMMON-MIB", "s5TrRingExtBoardIndx"),
    (0, "S5-TOKENRING-COMMON-MIB", "s5TrRingExtExtensionIndx"),
)
if mibBuilder.loadTexts:
    s5TrRingExtEosEntry.setStatus("mandatory")


class _S5TrRingExtEos_Type(OctetString):
    """Custom type s5TrRingExtEos based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 1400),
    )


_S5TrRingExtEos_Type.__name__ = "OctetString"
_S5TrRingExtEos_Object = MibTableColumn
s5TrRingExtEos = _S5TrRingExtEos_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 7, 1, 5, 5, 1, 1),
    _S5TrRingExtEos_Type()
)
s5TrRingExtEos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s5TrRingExtEos.setStatus("mandatory")
_S5TrPortInfoTable_Object = MibTable
s5TrPortInfoTable = _S5TrPortInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 7, 1, 6)
)
if mibBuilder.loadTexts:
    s5TrPortInfoTable.setStatus("mandatory")
_S5TrPortInfoEntry_Object = MibTableRow
s5TrPortInfoEntry = _S5TrPortInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 7, 1, 6, 1)
)
s5TrPortInfoEntry.setIndexNames(
    (0, "S5-TOKENRING-COMMON-MIB", "s5TrPortInfoSrcIndx"),
    (0, "S5-TOKENRING-COMMON-MIB", "s5TrPortInfoBrdIndx"),
    (0, "S5-TOKENRING-COMMON-MIB", "s5TrPortInfoPortIndx"),
)
if mibBuilder.loadTexts:
    s5TrPortInfoEntry.setStatus("mandatory")
_S5TrPortInfoSrcIndx_Type = SrcIndx
_S5TrPortInfoSrcIndx_Object = MibTableColumn
s5TrPortInfoSrcIndx = _S5TrPortInfoSrcIndx_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 7, 1, 6, 1, 1),
    _S5TrPortInfoSrcIndx_Type()
)
s5TrPortInfoSrcIndx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s5TrPortInfoSrcIndx.setStatus("mandatory")
_S5TrPortInfoBrdIndx_Type = Integer32
_S5TrPortInfoBrdIndx_Object = MibTableColumn
s5TrPortInfoBrdIndx = _S5TrPortInfoBrdIndx_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 7, 1, 6, 1, 2),
    _S5TrPortInfoBrdIndx_Type()
)
s5TrPortInfoBrdIndx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s5TrPortInfoBrdIndx.setStatus("mandatory")
_S5TrPortInfoPortIndx_Type = Integer32
_S5TrPortInfoPortIndx_Object = MibTableColumn
s5TrPortInfoPortIndx = _S5TrPortInfoPortIndx_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 7, 1, 6, 1, 3),
    _S5TrPortInfoPortIndx_Type()
)
s5TrPortInfoPortIndx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s5TrPortInfoPortIndx.setStatus("mandatory")
_S5TrPortInfoAddr_Type = MacAddress
_S5TrPortInfoAddr_Object = MibTableColumn
s5TrPortInfoAddr = _S5TrPortInfoAddr_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 7, 1, 6, 1, 4),
    _S5TrPortInfoAddr_Type()
)
s5TrPortInfoAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s5TrPortInfoAddr.setStatus("mandatory")
_S5TrPortInfoLastNaun_Type = MacAddress
_S5TrPortInfoLastNaun_Object = MibTableColumn
s5TrPortInfoLastNaun = _S5TrPortInfoLastNaun_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 7, 1, 6, 1, 5),
    _S5TrPortInfoLastNaun_Type()
)
s5TrPortInfoLastNaun.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s5TrPortInfoLastNaun.setStatus("mandatory")


class _S5TrPortInfoStationStatus_Type(Integer32):
    """Custom type s5TrPortInfoStationStatus based on Integer32"""
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
        *(("active", 1),
          ("forcedRemoval", 4),
          ("inactive", 3),
          ("notInRingPoll", 2))
    )


_S5TrPortInfoStationStatus_Type.__name__ = "Integer32"
_S5TrPortInfoStationStatus_Object = MibTableColumn
s5TrPortInfoStationStatus = _S5TrPortInfoStationStatus_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 7, 1, 6, 1, 6),
    _S5TrPortInfoStationStatus_Type()
)
s5TrPortInfoStationStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s5TrPortInfoStationStatus.setStatus("mandatory")
_S5TrPortInfoFirstEnterTime_Type = TimeTicks
_S5TrPortInfoFirstEnterTime_Object = MibTableColumn
s5TrPortInfoFirstEnterTime = _S5TrPortInfoFirstEnterTime_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 7, 1, 6, 1, 7),
    _S5TrPortInfoFirstEnterTime_Type()
)
s5TrPortInfoFirstEnterTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s5TrPortInfoFirstEnterTime.setStatus("mandatory")
_S5TrPortInfoLastEnterTime_Type = TimeTicks
_S5TrPortInfoLastEnterTime_Object = MibTableColumn
s5TrPortInfoLastEnterTime = _S5TrPortInfoLastEnterTime_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 7, 1, 6, 1, 8),
    _S5TrPortInfoLastEnterTime_Type()
)
s5TrPortInfoLastEnterTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s5TrPortInfoLastEnterTime.setStatus("mandatory")
_S5TrPortInfoLastExitTime_Type = TimeTicks
_S5TrPortInfoLastExitTime_Object = MibTableColumn
s5TrPortInfoLastExitTime = _S5TrPortInfoLastExitTime_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 7, 1, 6, 1, 9),
    _S5TrPortInfoLastExitTime_Type()
)
s5TrPortInfoLastExitTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s5TrPortInfoLastExitTime.setStatus("mandatory")
_S5TrPortInfoDupAddrErrs_Type = Counter32
_S5TrPortInfoDupAddrErrs_Object = MibTableColumn
s5TrPortInfoDupAddrErrs = _S5TrPortInfoDupAddrErrs_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 7, 1, 6, 1, 10),
    _S5TrPortInfoDupAddrErrs_Type()
)
s5TrPortInfoDupAddrErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s5TrPortInfoDupAddrErrs.setStatus("mandatory")
_S5TrPortInfoLineErrs_Type = Counter32
_S5TrPortInfoLineErrs_Object = MibTableColumn
s5TrPortInfoLineErrs = _S5TrPortInfoLineErrs_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 7, 1, 6, 1, 11),
    _S5TrPortInfoLineErrs_Type()
)
s5TrPortInfoLineErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s5TrPortInfoLineErrs.setStatus("mandatory")
_S5TrPortInfoInternalErrs_Type = Counter32
_S5TrPortInfoInternalErrs_Object = MibTableColumn
s5TrPortInfoInternalErrs = _S5TrPortInfoInternalErrs_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 7, 1, 6, 1, 12),
    _S5TrPortInfoInternalErrs_Type()
)
s5TrPortInfoInternalErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s5TrPortInfoInternalErrs.setStatus("mandatory")
_S5TrPortInfoBurstErrs_Type = Counter32
_S5TrPortInfoBurstErrs_Object = MibTableColumn
s5TrPortInfoBurstErrs = _S5TrPortInfoBurstErrs_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 7, 1, 6, 1, 13),
    _S5TrPortInfoBurstErrs_Type()
)
s5TrPortInfoBurstErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s5TrPortInfoBurstErrs.setStatus("mandatory")
_S5TrPortInfoACErrs_Type = Counter32
_S5TrPortInfoACErrs_Object = MibTableColumn
s5TrPortInfoACErrs = _S5TrPortInfoACErrs_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 7, 1, 6, 1, 14),
    _S5TrPortInfoACErrs_Type()
)
s5TrPortInfoACErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s5TrPortInfoACErrs.setStatus("mandatory")
_S5TrPortInfoAbortErrs_Type = Counter32
_S5TrPortInfoAbortErrs_Object = MibTableColumn
s5TrPortInfoAbortErrs = _S5TrPortInfoAbortErrs_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 7, 1, 6, 1, 15),
    _S5TrPortInfoAbortErrs_Type()
)
s5TrPortInfoAbortErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s5TrPortInfoAbortErrs.setStatus("mandatory")
_S5TrPortInfoLostFrameErrs_Type = Counter32
_S5TrPortInfoLostFrameErrs_Object = MibTableColumn
s5TrPortInfoLostFrameErrs = _S5TrPortInfoLostFrameErrs_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 7, 1, 6, 1, 16),
    _S5TrPortInfoLostFrameErrs_Type()
)
s5TrPortInfoLostFrameErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s5TrPortInfoLostFrameErrs.setStatus("mandatory")
_S5TrPortInfoCongestionErrs_Type = Counter32
_S5TrPortInfoCongestionErrs_Object = MibTableColumn
s5TrPortInfoCongestionErrs = _S5TrPortInfoCongestionErrs_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 7, 1, 6, 1, 17),
    _S5TrPortInfoCongestionErrs_Type()
)
s5TrPortInfoCongestionErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s5TrPortInfoCongestionErrs.setStatus("mandatory")
_S5TrPortInfoFrameCopiedErrs_Type = Counter32
_S5TrPortInfoFrameCopiedErrs_Object = MibTableColumn
s5TrPortInfoFrameCopiedErrs = _S5TrPortInfoFrameCopiedErrs_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 7, 1, 6, 1, 18),
    _S5TrPortInfoFrameCopiedErrs_Type()
)
s5TrPortInfoFrameCopiedErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s5TrPortInfoFrameCopiedErrs.setStatus("mandatory")
_S5TrPortInfoFrequencyErrs_Type = Counter32
_S5TrPortInfoFrequencyErrs_Object = MibTableColumn
s5TrPortInfoFrequencyErrs = _S5TrPortInfoFrequencyErrs_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 7, 1, 6, 1, 19),
    _S5TrPortInfoFrequencyErrs_Type()
)
s5TrPortInfoFrequencyErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s5TrPortInfoFrequencyErrs.setStatus("mandatory")
_S5TrPortInfoTokenErrs_Type = Counter32
_S5TrPortInfoTokenErrs_Object = MibTableColumn
s5TrPortInfoTokenErrs = _S5TrPortInfoTokenErrs_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 7, 1, 6, 1, 20),
    _S5TrPortInfoTokenErrs_Type()
)
s5TrPortInfoTokenErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s5TrPortInfoTokenErrs.setStatus("mandatory")
_S5TrPortInfoBeaconErrs_Type = Counter32
_S5TrPortInfoBeaconErrs_Object = MibTableColumn
s5TrPortInfoBeaconErrs = _S5TrPortInfoBeaconErrs_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 7, 1, 6, 1, 21),
    _S5TrPortInfoBeaconErrs_Type()
)
s5TrPortInfoBeaconErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s5TrPortInfoBeaconErrs.setStatus("mandatory")
_S5TrPortInfoInsertions_Type = Counter32
_S5TrPortInfoInsertions_Object = MibTableColumn
s5TrPortInfoInsertions = _S5TrPortInfoInsertions_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 7, 1, 6, 1, 22),
    _S5TrPortInfoInsertions_Type()
)
s5TrPortInfoInsertions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s5TrPortInfoInsertions.setStatus("mandatory")
_S5TrPortFpuStatsTable_Object = MibTable
s5TrPortFpuStatsTable = _S5TrPortFpuStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 7, 1, 7)
)
if mibBuilder.loadTexts:
    s5TrPortFpuStatsTable.setStatus("mandatory")
_S5TrPortFpuStatsEntry_Object = MibTableRow
s5TrPortFpuStatsEntry = _S5TrPortFpuStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 7, 1, 7, 1)
)
s5TrPortFpuStatsEntry.setIndexNames(
    (0, "S5-TOKENRING-COMMON-MIB", "s5TrPortFpuStatsBrdIndx"),
    (0, "S5-TOKENRING-COMMON-MIB", "s5TrPortFpuStatsPortIndx"),
)
if mibBuilder.loadTexts:
    s5TrPortFpuStatsEntry.setStatus("mandatory")


class _S5TrPortFpuStatsBrdIndx_Type(Integer32):
    """Custom type s5TrPortFpuStatsBrdIndx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_S5TrPortFpuStatsBrdIndx_Type.__name__ = "Integer32"
_S5TrPortFpuStatsBrdIndx_Object = MibTableColumn
s5TrPortFpuStatsBrdIndx = _S5TrPortFpuStatsBrdIndx_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 7, 1, 7, 1, 1),
    _S5TrPortFpuStatsBrdIndx_Type()
)
s5TrPortFpuStatsBrdIndx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s5TrPortFpuStatsBrdIndx.setStatus("mandatory")


class _S5TrPortFpuStatsPortIndx_Type(Integer32):
    """Custom type s5TrPortFpuStatsPortIndx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_S5TrPortFpuStatsPortIndx_Type.__name__ = "Integer32"
_S5TrPortFpuStatsPortIndx_Object = MibTableColumn
s5TrPortFpuStatsPortIndx = _S5TrPortFpuStatsPortIndx_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 7, 1, 7, 1, 2),
    _S5TrPortFpuStatsPortIndx_Type()
)
s5TrPortFpuStatsPortIndx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s5TrPortFpuStatsPortIndx.setStatus("mandatory")
_S5TrPortFpuStatsAddr_Type = MacAddress
_S5TrPortFpuStatsAddr_Object = MibTableColumn
s5TrPortFpuStatsAddr = _S5TrPortFpuStatsAddr_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 7, 1, 7, 1, 3),
    _S5TrPortFpuStatsAddr_Type()
)
s5TrPortFpuStatsAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s5TrPortFpuStatsAddr.setStatus("mandatory")
_S5TrPortFpuStatsTxOctets_Type = Counter32
_S5TrPortFpuStatsTxOctets_Object = MibTableColumn
s5TrPortFpuStatsTxOctets = _S5TrPortFpuStatsTxOctets_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 7, 1, 7, 1, 4),
    _S5TrPortFpuStatsTxOctets_Type()
)
s5TrPortFpuStatsTxOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s5TrPortFpuStatsTxOctets.setStatus("mandatory")
_S5TrPortFpuStatsTxPkts_Type = Counter32
_S5TrPortFpuStatsTxPkts_Object = MibTableColumn
s5TrPortFpuStatsTxPkts = _S5TrPortFpuStatsTxPkts_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 7, 1, 7, 1, 5),
    _S5TrPortFpuStatsTxPkts_Type()
)
s5TrPortFpuStatsTxPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s5TrPortFpuStatsTxPkts.setStatus("mandatory")
_S5TrPortFpuStatsRxOctets_Type = Counter32
_S5TrPortFpuStatsRxOctets_Object = MibTableColumn
s5TrPortFpuStatsRxOctets = _S5TrPortFpuStatsRxOctets_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 7, 1, 7, 1, 6),
    _S5TrPortFpuStatsRxOctets_Type()
)
s5TrPortFpuStatsRxOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s5TrPortFpuStatsRxOctets.setStatus("mandatory")
_S5TrPortFpuStatsRxPkts_Type = Counter32
_S5TrPortFpuStatsRxPkts_Object = MibTableColumn
s5TrPortFpuStatsRxPkts = _S5TrPortFpuStatsRxPkts_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 7, 1, 7, 1, 7),
    _S5TrPortFpuStatsRxPkts_Type()
)
s5TrPortFpuStatsRxPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s5TrPortFpuStatsRxPkts.setStatus("mandatory")
_S5TrBStatTable_Object = MibTable
s5TrBStatTable = _S5TrBStatTable_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 7, 2, 1)
)
if mibBuilder.loadTexts:
    s5TrBStatTable.setStatus("mandatory")
_S5TrBStatEntry_Object = MibTableRow
s5TrBStatEntry = _S5TrBStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 7, 2, 1, 1)
)
s5TrBStatEntry.setIndexNames(
    (0, "S5-TOKENRING-COMMON-MIB", "s5TrBStatSrcIndx"),
)
if mibBuilder.loadTexts:
    s5TrBStatEntry.setStatus("mandatory")
_S5TrBStatSrcIndx_Type = SrcIndx
_S5TrBStatSrcIndx_Object = MibTableColumn
s5TrBStatSrcIndx = _S5TrBStatSrcIndx_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 7, 2, 1, 1, 1),
    _S5TrBStatSrcIndx_Type()
)
s5TrBStatSrcIndx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s5TrBStatSrcIndx.setStatus("mandatory")
_S5TrBStatTtlOctets_Type = Counter32
_S5TrBStatTtlOctets_Object = MibTableColumn
s5TrBStatTtlOctets = _S5TrBStatTtlOctets_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 7, 2, 1, 1, 2),
    _S5TrBStatTtlOctets_Type()
)
s5TrBStatTtlOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s5TrBStatTtlOctets.setStatus("mandatory")
_S5TrBStatMacOctets_Type = Counter32
_S5TrBStatMacOctets_Object = MibTableColumn
s5TrBStatMacOctets = _S5TrBStatMacOctets_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 7, 2, 1, 1, 3),
    _S5TrBStatMacOctets_Type()
)
s5TrBStatMacOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s5TrBStatMacOctets.setStatus("mandatory")
_S5TrBStatLlcOctets_Type = Counter32
_S5TrBStatLlcOctets_Object = MibTableColumn
s5TrBStatLlcOctets = _S5TrBStatLlcOctets_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 7, 2, 1, 1, 4),
    _S5TrBStatLlcOctets_Type()
)
s5TrBStatLlcOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s5TrBStatLlcOctets.setStatus("mandatory")
_S5TrBStatTtlFrms_Type = Counter32
_S5TrBStatTtlFrms_Object = MibTableColumn
s5TrBStatTtlFrms = _S5TrBStatTtlFrms_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 7, 2, 1, 1, 5),
    _S5TrBStatTtlFrms_Type()
)
s5TrBStatTtlFrms.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s5TrBStatTtlFrms.setStatus("mandatory")
_S5TrBStatTtlGoodFrms_Type = Counter32
_S5TrBStatTtlGoodFrms_Object = MibTableColumn
s5TrBStatTtlGoodFrms = _S5TrBStatTtlGoodFrms_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 7, 2, 1, 1, 6),
    _S5TrBStatTtlGoodFrms_Type()
)
s5TrBStatTtlGoodFrms.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s5TrBStatTtlGoodFrms.setStatus("mandatory")
_S5TrBStatTtlBadFrms_Type = Counter32
_S5TrBStatTtlBadFrms_Object = MibTableColumn
s5TrBStatTtlBadFrms = _S5TrBStatTtlBadFrms_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 7, 2, 1, 1, 7),
    _S5TrBStatTtlBadFrms_Type()
)
s5TrBStatTtlBadFrms.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s5TrBStatTtlBadFrms.setStatus("mandatory")
_S5TrBStatMacFrms_Type = Counter32
_S5TrBStatMacFrms_Object = MibTableColumn
s5TrBStatMacFrms = _S5TrBStatMacFrms_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 7, 2, 1, 1, 8),
    _S5TrBStatMacFrms_Type()
)
s5TrBStatMacFrms.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s5TrBStatMacFrms.setStatus("mandatory")
_S5TrBStatLlcFrms_Type = Counter32
_S5TrBStatLlcFrms_Object = MibTableColumn
s5TrBStatLlcFrms = _S5TrBStatLlcFrms_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 7, 2, 1, 1, 9),
    _S5TrBStatLlcFrms_Type()
)
s5TrBStatLlcFrms.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s5TrBStatLlcFrms.setStatus("mandatory")
_S5TrBStatLlcNonUcastFrms_Type = Counter32
_S5TrBStatLlcNonUcastFrms_Object = MibTableColumn
s5TrBStatLlcNonUcastFrms = _S5TrBStatLlcNonUcastFrms_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 7, 2, 1, 1, 10),
    _S5TrBStatLlcNonUcastFrms_Type()
)
s5TrBStatLlcNonUcastFrms.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s5TrBStatLlcNonUcastFrms.setStatus("mandatory")
_S5TrBStatLlcUcastFrms_Type = Counter32
_S5TrBStatLlcUcastFrms_Object = MibTableColumn
s5TrBStatLlcUcastFrms = _S5TrBStatLlcUcastFrms_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 7, 2, 1, 1, 11),
    _S5TrBStatLlcUcastFrms_Type()
)
s5TrBStatLlcUcastFrms.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s5TrBStatLlcUcastFrms.setStatus("mandatory")
_S5TrBStatGoodErrReportFrms_Type = Counter32
_S5TrBStatGoodErrReportFrms_Object = MibTableColumn
s5TrBStatGoodErrReportFrms = _S5TrBStatGoodErrReportFrms_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 7, 2, 1, 1, 12),
    _S5TrBStatGoodErrReportFrms_Type()
)
s5TrBStatGoodErrReportFrms.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s5TrBStatGoodErrReportFrms.setStatus("mandatory")
_S5TrBStatBeaconFrms_Type = Counter32
_S5TrBStatBeaconFrms_Object = MibTableColumn
s5TrBStatBeaconFrms = _S5TrBStatBeaconFrms_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 7, 2, 1, 1, 13),
    _S5TrBStatBeaconFrms_Type()
)
s5TrBStatBeaconFrms.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s5TrBStatBeaconFrms.setStatus("mandatory")
_S5TrBStatRingPurgeFrms_Type = Counter32
_S5TrBStatRingPurgeFrms_Object = MibTableColumn
s5TrBStatRingPurgeFrms = _S5TrBStatRingPurgeFrms_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 7, 2, 1, 1, 14),
    _S5TrBStatRingPurgeFrms_Type()
)
s5TrBStatRingPurgeFrms.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s5TrBStatRingPurgeFrms.setStatus("mandatory")
_S5TrBStatClaimTokenFrms_Type = Counter32
_S5TrBStatClaimTokenFrms_Object = MibTableColumn
s5TrBStatClaimTokenFrms = _S5TrBStatClaimTokenFrms_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 7, 2, 1, 1, 15),
    _S5TrBStatClaimTokenFrms_Type()
)
s5TrBStatClaimTokenFrms.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s5TrBStatClaimTokenFrms.setStatus("mandatory")
_S5TrBStatUna_Type = MacAddress
_S5TrBStatUna_Object = MibTableColumn
s5TrBStatUna = _S5TrBStatUna_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 7, 2, 1, 1, 16),
    _S5TrBStatUna_Type()
)
s5TrBStatUna.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s5TrBStatUna.setStatus("mandatory")
_S5TrFStatTable_Object = MibTable
s5TrFStatTable = _S5TrFStatTable_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 7, 2, 2)
)
if mibBuilder.loadTexts:
    s5TrFStatTable.setStatus("obsolete")
_S5TrFStatEntry_Object = MibTableRow
s5TrFStatEntry = _S5TrFStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 7, 2, 2, 1)
)
s5TrFStatEntry.setIndexNames(
    (0, "S5-TOKENRING-COMMON-MIB", "s5TrFStatSrcIndx"),
)
if mibBuilder.loadTexts:
    s5TrFStatEntry.setStatus("obsolete")
_S5TrFStatSrcIndx_Type = SrcIndx
_S5TrFStatSrcIndx_Object = MibTableColumn
s5TrFStatSrcIndx = _S5TrFStatSrcIndx_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 7, 2, 2, 1, 1),
    _S5TrFStatSrcIndx_Type()
)
s5TrFStatSrcIndx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s5TrFStatSrcIndx.setStatus("obsolete")
_S5TrFStatDropEvents_Type = Counter32
_S5TrFStatDropEvents_Object = MibTableColumn
s5TrFStatDropEvents = _S5TrFStatDropEvents_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 7, 2, 2, 1, 2),
    _S5TrFStatDropEvents_Type()
)
s5TrFStatDropEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s5TrFStatDropEvents.setStatus("obsolete")
_S5TrFStatLlcFrms18to63Octets_Type = Counter32
_S5TrFStatLlcFrms18to63Octets_Object = MibTableColumn
s5TrFStatLlcFrms18to63Octets = _S5TrFStatLlcFrms18to63Octets_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 7, 2, 2, 1, 3),
    _S5TrFStatLlcFrms18to63Octets_Type()
)
s5TrFStatLlcFrms18to63Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s5TrFStatLlcFrms18to63Octets.setStatus("obsolete")
_S5TrFStatLlcFrms64to127Octets_Type = Counter32
_S5TrFStatLlcFrms64to127Octets_Object = MibTableColumn
s5TrFStatLlcFrms64to127Octets = _S5TrFStatLlcFrms64to127Octets_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 7, 2, 2, 1, 4),
    _S5TrFStatLlcFrms64to127Octets_Type()
)
s5TrFStatLlcFrms64to127Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s5TrFStatLlcFrms64to127Octets.setStatus("obsolete")
_S5TrFStatLlcFrms128to255Octets_Type = Counter32
_S5TrFStatLlcFrms128to255Octets_Object = MibTableColumn
s5TrFStatLlcFrms128to255Octets = _S5TrFStatLlcFrms128to255Octets_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 7, 2, 2, 1, 5),
    _S5TrFStatLlcFrms128to255Octets_Type()
)
s5TrFStatLlcFrms128to255Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s5TrFStatLlcFrms128to255Octets.setStatus("obsolete")
_S5TrFStatLlcFrms256to511Octets_Type = Counter32
_S5TrFStatLlcFrms256to511Octets_Object = MibTableColumn
s5TrFStatLlcFrms256to511Octets = _S5TrFStatLlcFrms256to511Octets_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 7, 2, 2, 1, 6),
    _S5TrFStatLlcFrms256to511Octets_Type()
)
s5TrFStatLlcFrms256to511Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s5TrFStatLlcFrms256to511Octets.setStatus("obsolete")
_S5TrFStatLlcFrms512to1023Octets_Type = Counter32
_S5TrFStatLlcFrms512to1023Octets_Object = MibTableColumn
s5TrFStatLlcFrms512to1023Octets = _S5TrFStatLlcFrms512to1023Octets_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 7, 2, 2, 1, 7),
    _S5TrFStatLlcFrms512to1023Octets_Type()
)
s5TrFStatLlcFrms512to1023Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s5TrFStatLlcFrms512to1023Octets.setStatus("obsolete")
_S5TrFStatLlcFrms1024to2047Octets_Type = Counter32
_S5TrFStatLlcFrms1024to2047Octets_Object = MibTableColumn
s5TrFStatLlcFrms1024to2047Octets = _S5TrFStatLlcFrms1024to2047Octets_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 7, 2, 2, 1, 8),
    _S5TrFStatLlcFrms1024to2047Octets_Type()
)
s5TrFStatLlcFrms1024to2047Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s5TrFStatLlcFrms1024to2047Octets.setStatus("obsolete")
_S5TrFStatLlcFrms2048to4095Octets_Type = Counter32
_S5TrFStatLlcFrms2048to4095Octets_Object = MibTableColumn
s5TrFStatLlcFrms2048to4095Octets = _S5TrFStatLlcFrms2048to4095Octets_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 7, 2, 2, 1, 9),
    _S5TrFStatLlcFrms2048to4095Octets_Type()
)
s5TrFStatLlcFrms2048to4095Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s5TrFStatLlcFrms2048to4095Octets.setStatus("obsolete")
_S5TrFStatLlcFrms4096to8191Octets_Type = Counter32
_S5TrFStatLlcFrms4096to8191Octets_Object = MibTableColumn
s5TrFStatLlcFrms4096to8191Octets = _S5TrFStatLlcFrms4096to8191Octets_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 7, 2, 2, 1, 10),
    _S5TrFStatLlcFrms4096to8191Octets_Type()
)
s5TrFStatLlcFrms4096to8191Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s5TrFStatLlcFrms4096to8191Octets.setStatus("obsolete")
_S5TrFStatLlcFrms8192to18000Octets_Type = Counter32
_S5TrFStatLlcFrms8192to18000Octets_Object = MibTableColumn
s5TrFStatLlcFrms8192to18000Octets = _S5TrFStatLlcFrms8192to18000Octets_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 7, 2, 2, 1, 11),
    _S5TrFStatLlcFrms8192to18000Octets_Type()
)
s5TrFStatLlcFrms8192to18000Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s5TrFStatLlcFrms8192to18000Octets.setStatus("obsolete")
_S5TrFStatLlcFrmsGreaterThan18000Octets_Type = Counter32
_S5TrFStatLlcFrmsGreaterThan18000Octets_Object = MibTableColumn
s5TrFStatLlcFrmsGreaterThan18000Octets = _S5TrFStatLlcFrmsGreaterThan18000Octets_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 7, 2, 2, 1, 12),
    _S5TrFStatLlcFrmsGreaterThan18000Octets_Type()
)
s5TrFStatLlcFrmsGreaterThan18000Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s5TrFStatLlcFrmsGreaterThan18000Octets.setStatus("obsolete")
_S5TrEStatTable_Object = MibTable
s5TrEStatTable = _S5TrEStatTable_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 7, 2, 3)
)
if mibBuilder.loadTexts:
    s5TrEStatTable.setStatus("mandatory")
_S5TrEStatEntry_Object = MibTableRow
s5TrEStatEntry = _S5TrEStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 7, 2, 3, 1)
)
s5TrEStatEntry.setIndexNames(
    (0, "S5-TOKENRING-COMMON-MIB", "s5TrEStatSrcIndx"),
)
if mibBuilder.loadTexts:
    s5TrEStatEntry.setStatus("mandatory")
_S5TrEStatSrcIndx_Type = SrcIndx
_S5TrEStatSrcIndx_Object = MibTableColumn
s5TrEStatSrcIndx = _S5TrEStatSrcIndx_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 7, 2, 3, 1, 1),
    _S5TrEStatSrcIndx_Type()
)
s5TrEStatSrcIndx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s5TrEStatSrcIndx.setStatus("mandatory")
_S5TrEStatDropEvents_Type = Counter32
_S5TrEStatDropEvents_Object = MibTableColumn
s5TrEStatDropEvents = _S5TrEStatDropEvents_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 7, 2, 3, 1, 2),
    _S5TrEStatDropEvents_Type()
)
s5TrEStatDropEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s5TrEStatDropEvents.setStatus("obsolete")
_S5TrEStatLineErrs_Type = Counter32
_S5TrEStatLineErrs_Object = MibTableColumn
s5TrEStatLineErrs = _S5TrEStatLineErrs_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 7, 2, 3, 1, 3),
    _S5TrEStatLineErrs_Type()
)
s5TrEStatLineErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s5TrEStatLineErrs.setStatus("mandatory")
_S5TrEStatInternalErrs_Type = Counter32
_S5TrEStatInternalErrs_Object = MibTableColumn
s5TrEStatInternalErrs = _S5TrEStatInternalErrs_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 7, 2, 3, 1, 4),
    _S5TrEStatInternalErrs_Type()
)
s5TrEStatInternalErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s5TrEStatInternalErrs.setStatus("mandatory")
_S5TrEStatBurstErrs_Type = Counter32
_S5TrEStatBurstErrs_Object = MibTableColumn
s5TrEStatBurstErrs = _S5TrEStatBurstErrs_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 7, 2, 3, 1, 5),
    _S5TrEStatBurstErrs_Type()
)
s5TrEStatBurstErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s5TrEStatBurstErrs.setStatus("mandatory")
_S5TrEStatACErrs_Type = Counter32
_S5TrEStatACErrs_Object = MibTableColumn
s5TrEStatACErrs = _S5TrEStatACErrs_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 7, 2, 3, 1, 6),
    _S5TrEStatACErrs_Type()
)
s5TrEStatACErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s5TrEStatACErrs.setStatus("mandatory")
_S5TrEStatAbortErrs_Type = Counter32
_S5TrEStatAbortErrs_Object = MibTableColumn
s5TrEStatAbortErrs = _S5TrEStatAbortErrs_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 7, 2, 3, 1, 7),
    _S5TrEStatAbortErrs_Type()
)
s5TrEStatAbortErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s5TrEStatAbortErrs.setStatus("mandatory")
_S5TrEStatLostFrameErrs_Type = Counter32
_S5TrEStatLostFrameErrs_Object = MibTableColumn
s5TrEStatLostFrameErrs = _S5TrEStatLostFrameErrs_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 7, 2, 3, 1, 8),
    _S5TrEStatLostFrameErrs_Type()
)
s5TrEStatLostFrameErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s5TrEStatLostFrameErrs.setStatus("mandatory")
_S5TrEStatCongestionErrs_Type = Counter32
_S5TrEStatCongestionErrs_Object = MibTableColumn
s5TrEStatCongestionErrs = _S5TrEStatCongestionErrs_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 7, 2, 3, 1, 9),
    _S5TrEStatCongestionErrs_Type()
)
s5TrEStatCongestionErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s5TrEStatCongestionErrs.setStatus("mandatory")
_S5TrEStatFrameCopiedErrs_Type = Counter32
_S5TrEStatFrameCopiedErrs_Object = MibTableColumn
s5TrEStatFrameCopiedErrs = _S5TrEStatFrameCopiedErrs_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 7, 2, 3, 1, 10),
    _S5TrEStatFrameCopiedErrs_Type()
)
s5TrEStatFrameCopiedErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s5TrEStatFrameCopiedErrs.setStatus("mandatory")
_S5TrEStatFrequencyErrs_Type = Counter32
_S5TrEStatFrequencyErrs_Object = MibTableColumn
s5TrEStatFrequencyErrs = _S5TrEStatFrequencyErrs_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 7, 2, 3, 1, 11),
    _S5TrEStatFrequencyErrs_Type()
)
s5TrEStatFrequencyErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s5TrEStatFrequencyErrs.setStatus("mandatory")
_S5TrEStatTokenErrs_Type = Counter32
_S5TrEStatTokenErrs_Object = MibTableColumn
s5TrEStatTokenErrs = _S5TrEStatTokenErrs_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 7, 2, 3, 1, 12),
    _S5TrEStatTokenErrs_Type()
)
s5TrEStatTokenErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s5TrEStatTokenErrs.setStatus("mandatory")
_S5TrEStatSoftErrFrms_Type = Counter32
_S5TrEStatSoftErrFrms_Object = MibTableColumn
s5TrEStatSoftErrFrms = _S5TrEStatSoftErrFrms_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 7, 2, 3, 1, 13),
    _S5TrEStatSoftErrFrms_Type()
)
s5TrEStatSoftErrFrms.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s5TrEStatSoftErrFrms.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "S5-TOKENRING-COMMON-MIB",
    **{"s5TrPortTable": s5TrPortTable,
       "s5TrPortEntry": s5TrPortEntry,
       "s5TrPortBrdIndx": s5TrPortBrdIndx,
       "s5TrPortIndx": s5TrPortIndx,
       "s5TrPortWrapStatus": s5TrPortWrapStatus,
       "s5TrPortWrapTime": s5TrPortWrapTime,
       "s5TrPortInsrtStatus": s5TrPortInsrtStatus,
       "s5TrPortPhanStatus": s5TrPortPhanStatus,
       "s5TrPortPhanChngs": s5TrPortPhanChngs,
       "s5TrPortTrnkAccMthdStrap": s5TrPortTrnkAccMthdStrap,
       "s5TrPortTrnkAccMthd": s5TrPortTrnkAccMthd,
       "s5TrPortClass": s5TrPortClass,
       "s5TrPortMedia": s5TrPortMedia,
       "s5TrPortConnector": s5TrPortConnector,
       "s5TrPortSoftwareInsertion": s5TrPortSoftwareInsertion,
       "s5TrPortAFD": s5TrPortAFD,
       "s5TrFpuTable": s5TrFpuTable,
       "s5TrFpuEntry": s5TrFpuEntry,
       "s5TrFpuBrdIndx": s5TrFpuBrdIndx,
       "s5TrFpuIndx": s5TrFpuIndx,
       "s5TrFpuType": s5TrFpuType,
       "s5TrFpuTypeIndx": s5TrFpuTypeIndx,
       "s5TrFpuVer": s5TrFpuVer,
       "s5TrFpuCapabilites": s5TrFpuCapabilites,
       "s5TrFpuRunningMode": s5TrFpuRunningMode,
       "s5TrAttTable": s5TrAttTable,
       "s5TrAttEntry": s5TrAttEntry,
       "s5TrAttBrdIndx": s5TrAttBrdIndx,
       "s5TrAttIndx": s5TrAttIndx,
       "s5TrAttDfltSpeed": s5TrAttDfltSpeed,
       "s5TrAttCurSpeed": s5TrAttCurSpeed,
       "s5TrAttFault": s5TrAttFault,
       "s5TrBkDiv": s5TrBkDiv,
       "s5TrRingExt": s5TrRingExt,
       "s5TrRingExtLastChange": s5TrRingExtLastChange,
       "s5TrRingExtCurNum": s5TrRingExtCurNum,
       "s5TrRingExtTable": s5TrRingExtTable,
       "s5TrRingExtEntry": s5TrRingExtEntry,
       "s5TrRingExtBoardIndx": s5TrRingExtBoardIndx,
       "s5TrRingExtExtensionIndx": s5TrRingExtExtensionIndx,
       "s5TrRingExtRingNumber": s5TrRingExtRingNumber,
       "s5TrRingExtRingInUna": s5TrRingExtRingInUna,
       "s5TrRingExtRingOutUna": s5TrRingExtRingOutUna,
       "s5TrRingExtSecUna": s5TrRingExtSecUna,
       "s5TrRingExtRingInPhanStatus": s5TrRingExtRingInPhanStatus,
       "s5TrRingExtRingOutPhanStatus": s5TrRingExtRingOutPhanStatus,
       "s5TrRingExtRingInWrapStatus": s5TrRingExtRingInWrapStatus,
       "s5TrRingExtRingOutWrapStatus": s5TrRingExtRingOutWrapStatus,
       "s5TrRingExtClusterNumber": s5TrRingExtClusterNumber,
       "s5TrRingExtRingInPortNumber": s5TrRingExtRingInPortNumber,
       "s5TrRingExtRingOutPortNumber": s5TrRingExtRingOutPortNumber,
       "s5TrRingExtEosSize": s5TrRingExtEosSize,
       "s5TrRingExtEosTable": s5TrRingExtEosTable,
       "s5TrRingExtEosEntry": s5TrRingExtEosEntry,
       "s5TrRingExtEos": s5TrRingExtEos,
       "s5TrPortInfoTable": s5TrPortInfoTable,
       "s5TrPortInfoEntry": s5TrPortInfoEntry,
       "s5TrPortInfoSrcIndx": s5TrPortInfoSrcIndx,
       "s5TrPortInfoBrdIndx": s5TrPortInfoBrdIndx,
       "s5TrPortInfoPortIndx": s5TrPortInfoPortIndx,
       "s5TrPortInfoAddr": s5TrPortInfoAddr,
       "s5TrPortInfoLastNaun": s5TrPortInfoLastNaun,
       "s5TrPortInfoStationStatus": s5TrPortInfoStationStatus,
       "s5TrPortInfoFirstEnterTime": s5TrPortInfoFirstEnterTime,
       "s5TrPortInfoLastEnterTime": s5TrPortInfoLastEnterTime,
       "s5TrPortInfoLastExitTime": s5TrPortInfoLastExitTime,
       "s5TrPortInfoDupAddrErrs": s5TrPortInfoDupAddrErrs,
       "s5TrPortInfoLineErrs": s5TrPortInfoLineErrs,
       "s5TrPortInfoInternalErrs": s5TrPortInfoInternalErrs,
       "s5TrPortInfoBurstErrs": s5TrPortInfoBurstErrs,
       "s5TrPortInfoACErrs": s5TrPortInfoACErrs,
       "s5TrPortInfoAbortErrs": s5TrPortInfoAbortErrs,
       "s5TrPortInfoLostFrameErrs": s5TrPortInfoLostFrameErrs,
       "s5TrPortInfoCongestionErrs": s5TrPortInfoCongestionErrs,
       "s5TrPortInfoFrameCopiedErrs": s5TrPortInfoFrameCopiedErrs,
       "s5TrPortInfoFrequencyErrs": s5TrPortInfoFrequencyErrs,
       "s5TrPortInfoTokenErrs": s5TrPortInfoTokenErrs,
       "s5TrPortInfoBeaconErrs": s5TrPortInfoBeaconErrs,
       "s5TrPortInfoInsertions": s5TrPortInfoInsertions,
       "s5TrPortFpuStatsTable": s5TrPortFpuStatsTable,
       "s5TrPortFpuStatsEntry": s5TrPortFpuStatsEntry,
       "s5TrPortFpuStatsBrdIndx": s5TrPortFpuStatsBrdIndx,
       "s5TrPortFpuStatsPortIndx": s5TrPortFpuStatsPortIndx,
       "s5TrPortFpuStatsAddr": s5TrPortFpuStatsAddr,
       "s5TrPortFpuStatsTxOctets": s5TrPortFpuStatsTxOctets,
       "s5TrPortFpuStatsTxPkts": s5TrPortFpuStatsTxPkts,
       "s5TrPortFpuStatsRxOctets": s5TrPortFpuStatsRxOctets,
       "s5TrPortFpuStatsRxPkts": s5TrPortFpuStatsRxPkts,
       "s5TrBStatTable": s5TrBStatTable,
       "s5TrBStatEntry": s5TrBStatEntry,
       "s5TrBStatSrcIndx": s5TrBStatSrcIndx,
       "s5TrBStatTtlOctets": s5TrBStatTtlOctets,
       "s5TrBStatMacOctets": s5TrBStatMacOctets,
       "s5TrBStatLlcOctets": s5TrBStatLlcOctets,
       "s5TrBStatTtlFrms": s5TrBStatTtlFrms,
       "s5TrBStatTtlGoodFrms": s5TrBStatTtlGoodFrms,
       "s5TrBStatTtlBadFrms": s5TrBStatTtlBadFrms,
       "s5TrBStatMacFrms": s5TrBStatMacFrms,
       "s5TrBStatLlcFrms": s5TrBStatLlcFrms,
       "s5TrBStatLlcNonUcastFrms": s5TrBStatLlcNonUcastFrms,
       "s5TrBStatLlcUcastFrms": s5TrBStatLlcUcastFrms,
       "s5TrBStatGoodErrReportFrms": s5TrBStatGoodErrReportFrms,
       "s5TrBStatBeaconFrms": s5TrBStatBeaconFrms,
       "s5TrBStatRingPurgeFrms": s5TrBStatRingPurgeFrms,
       "s5TrBStatClaimTokenFrms": s5TrBStatClaimTokenFrms,
       "s5TrBStatUna": s5TrBStatUna,
       "s5TrFStatTable": s5TrFStatTable,
       "s5TrFStatEntry": s5TrFStatEntry,
       "s5TrFStatSrcIndx": s5TrFStatSrcIndx,
       "s5TrFStatDropEvents": s5TrFStatDropEvents,
       "s5TrFStatLlcFrms18to63Octets": s5TrFStatLlcFrms18to63Octets,
       "s5TrFStatLlcFrms64to127Octets": s5TrFStatLlcFrms64to127Octets,
       "s5TrFStatLlcFrms128to255Octets": s5TrFStatLlcFrms128to255Octets,
       "s5TrFStatLlcFrms256to511Octets": s5TrFStatLlcFrms256to511Octets,
       "s5TrFStatLlcFrms512to1023Octets": s5TrFStatLlcFrms512to1023Octets,
       "s5TrFStatLlcFrms1024to2047Octets": s5TrFStatLlcFrms1024to2047Octets,
       "s5TrFStatLlcFrms2048to4095Octets": s5TrFStatLlcFrms2048to4095Octets,
       "s5TrFStatLlcFrms4096to8191Octets": s5TrFStatLlcFrms4096to8191Octets,
       "s5TrFStatLlcFrms8192to18000Octets": s5TrFStatLlcFrms8192to18000Octets,
       "s5TrFStatLlcFrmsGreaterThan18000Octets": s5TrFStatLlcFrmsGreaterThan18000Octets,
       "s5TrEStatTable": s5TrEStatTable,
       "s5TrEStatEntry": s5TrEStatEntry,
       "s5TrEStatSrcIndx": s5TrEStatSrcIndx,
       "s5TrEStatDropEvents": s5TrEStatDropEvents,
       "s5TrEStatLineErrs": s5TrEStatLineErrs,
       "s5TrEStatInternalErrs": s5TrEStatInternalErrs,
       "s5TrEStatBurstErrs": s5TrEStatBurstErrs,
       "s5TrEStatACErrs": s5TrEStatACErrs,
       "s5TrEStatAbortErrs": s5TrEStatAbortErrs,
       "s5TrEStatLostFrameErrs": s5TrEStatLostFrameErrs,
       "s5TrEStatCongestionErrs": s5TrEStatCongestionErrs,
       "s5TrEStatFrameCopiedErrs": s5TrEStatFrameCopiedErrs,
       "s5TrEStatFrequencyErrs": s5TrEStatFrequencyErrs,
       "s5TrEStatTokenErrs": s5TrEStatTokenErrs,
       "s5TrEStatSoftErrFrms": s5TrEStatSoftErrFrms}
)
