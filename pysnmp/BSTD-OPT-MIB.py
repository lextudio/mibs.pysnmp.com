# SNMP MIB module (BSTD-OPT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/BSTD-OPT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:49:42 2024
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
_Cdx6500PPCTBSTDPortTable_Object = MibTable
cdx6500PPCTBSTDPortTable = _Cdx6500PPCTBSTDPortTable_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 14)
)
if mibBuilder.loadTexts:
    cdx6500PPCTBSTDPortTable.setStatus("mandatory")
_Cdx6500PPCTBSTDPortEntry_Object = MibTableRow
cdx6500PPCTBSTDPortEntry = _Cdx6500PPCTBSTDPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 14, 1)
)
cdx6500PPCTBSTDPortEntry.setIndexNames(
    (0, "BSTD-OPT-MIB", "cdx6500BSTDCfgPortNumber"),
)
if mibBuilder.loadTexts:
    cdx6500PPCTBSTDPortEntry.setStatus("mandatory")


class _Cdx6500BSTDCfgPortNumber_Type(Integer32):
    """Custom type cdx6500BSTDCfgPortNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 54),
    )


_Cdx6500BSTDCfgPortNumber_Type.__name__ = "Integer32"
_Cdx6500BSTDCfgPortNumber_Object = MibTableColumn
cdx6500BSTDCfgPortNumber = _Cdx6500BSTDCfgPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 14, 1, 1),
    _Cdx6500BSTDCfgPortNumber_Type()
)
cdx6500BSTDCfgPortNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500BSTDCfgPortNumber.setStatus("mandatory")


class _Cdx6500BSTDCfgPADType_Type(Integer32):
    """Custom type cdx6500BSTDCfgPADType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              50)
        )
    )
    namedValues = NamedValues(
        *(("hpad", 1),
          ("newvalTpad", 50),
          ("tpad", 0))
    )


_Cdx6500BSTDCfgPADType_Type.__name__ = "Integer32"
_Cdx6500BSTDCfgPADType_Object = MibTableColumn
cdx6500BSTDCfgPADType = _Cdx6500BSTDCfgPADType_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 14, 1, 2),
    _Cdx6500BSTDCfgPADType_Type()
)
cdx6500BSTDCfgPADType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500BSTDCfgPADType.setStatus("mandatory")


class _Cdx6500BSTDCfgLineInterface_Type(Integer32):
    """Custom type cdx6500BSTDCfgLineInterface based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              50)
        )
    )
    namedValues = NamedValues(
        *(("async", 1),
          ("newvalSync", 50),
          ("sync", 0))
    )


_Cdx6500BSTDCfgLineInterface_Type.__name__ = "Integer32"
_Cdx6500BSTDCfgLineInterface_Object = MibTableColumn
cdx6500BSTDCfgLineInterface = _Cdx6500BSTDCfgLineInterface_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 14, 1, 3),
    _Cdx6500BSTDCfgLineInterface_Type()
)
cdx6500BSTDCfgLineInterface.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500BSTDCfgLineInterface.setStatus("mandatory")


class _Cdx6500BSTDCfgClockSource_Type(Integer32):
    """Custom type cdx6500BSTDCfgClockSource based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              50)
        )
    )
    namedValues = NamedValues(
        *(("ext", 1),
          ("int", 0),
          ("newvalInt", 50))
    )


_Cdx6500BSTDCfgClockSource_Type.__name__ = "Integer32"
_Cdx6500BSTDCfgClockSource_Object = MibTableColumn
cdx6500BSTDCfgClockSource = _Cdx6500BSTDCfgClockSource_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 14, 1, 4),
    _Cdx6500BSTDCfgClockSource_Type()
)
cdx6500BSTDCfgClockSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500BSTDCfgClockSource.setStatus("mandatory")


class _Cdx6500BSTDCfgClockSpeed_Type(Integer32):
    """Custom type cdx6500BSTDCfgClockSpeed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1200, 192000),
    )


_Cdx6500BSTDCfgClockSpeed_Type.__name__ = "Integer32"
_Cdx6500BSTDCfgClockSpeed_Object = MibTableColumn
cdx6500BSTDCfgClockSpeed = _Cdx6500BSTDCfgClockSpeed_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 14, 1, 5),
    _Cdx6500BSTDCfgClockSpeed_Type()
)
cdx6500BSTDCfgClockSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500BSTDCfgClockSpeed.setStatus("mandatory")


class _Cdx6500BSTDCfgSyncContention_Type(Integer32):
    """Custom type cdx6500BSTDCfgSyncContention based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              50)
        )
    )
    namedValues = NamedValues(
        *(("fdx", 1),
          ("hdx", 0),
          ("newvalHdx", 50))
    )


_Cdx6500BSTDCfgSyncContention_Type.__name__ = "Integer32"
_Cdx6500BSTDCfgSyncContention_Object = MibTableColumn
cdx6500BSTDCfgSyncContention = _Cdx6500BSTDCfgSyncContention_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 14, 1, 6),
    _Cdx6500BSTDCfgSyncContention_Type()
)
cdx6500BSTDCfgSyncContention.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500BSTDCfgSyncContention.setStatus("mandatory")


class _Cdx6500BSTDCfgAsyncConnType_Type(Integer32):
    """Custom type cdx6500BSTDCfgAsyncConnType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              15,
              50)
        )
    )
    namedValues = NamedValues(
        *(("newvalSimp", 50),
          ("simp", 0),
          ("simpa", 15))
    )


_Cdx6500BSTDCfgAsyncConnType_Type.__name__ = "Integer32"
_Cdx6500BSTDCfgAsyncConnType_Object = MibTableColumn
cdx6500BSTDCfgAsyncConnType = _Cdx6500BSTDCfgAsyncConnType_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 14, 1, 7),
    _Cdx6500BSTDCfgAsyncConnType_Type()
)
cdx6500BSTDCfgAsyncConnType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500BSTDCfgAsyncConnType.setStatus("mandatory")


class _Cdx6500BSTDCfgNumDevices_Type(Integer32):
    """Custom type cdx6500BSTDCfgNumDevices based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_Cdx6500BSTDCfgNumDevices_Type.__name__ = "Integer32"
_Cdx6500BSTDCfgNumDevices_Object = MibTableColumn
cdx6500BSTDCfgNumDevices = _Cdx6500BSTDCfgNumDevices_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 14, 1, 8),
    _Cdx6500BSTDCfgNumDevices_Type()
)
cdx6500BSTDCfgNumDevices.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500BSTDCfgNumDevices.setStatus("mandatory")


class _Cdx6500BSTDCfgServTimer_Type(Integer32):
    """Custom type cdx6500BSTDCfgServTimer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 60),
    )


_Cdx6500BSTDCfgServTimer_Type.__name__ = "Integer32"
_Cdx6500BSTDCfgServTimer_Object = MibTableColumn
cdx6500BSTDCfgServTimer = _Cdx6500BSTDCfgServTimer_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 14, 1, 9),
    _Cdx6500BSTDCfgServTimer_Type()
)
cdx6500BSTDCfgServTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500BSTDCfgServTimer.setStatus("mandatory")


class _Cdx6500BSTDCfgErrThreshCount_Type(Integer32):
    """Custom type cdx6500BSTDCfgErrThreshCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_Cdx6500BSTDCfgErrThreshCount_Type.__name__ = "Integer32"
_Cdx6500BSTDCfgErrThreshCount_Object = MibTableColumn
cdx6500BSTDCfgErrThreshCount = _Cdx6500BSTDCfgErrThreshCount_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 14, 1, 10),
    _Cdx6500BSTDCfgErrThreshCount_Type()
)
cdx6500BSTDCfgErrThreshCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500BSTDCfgErrThreshCount.setStatus("mandatory")


class _Cdx6500BSTDCfgResponseTimeout_Type(Integer32):
    """Custom type cdx6500BSTDCfgResponseTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(400, 5000),
    )


_Cdx6500BSTDCfgResponseTimeout_Type.__name__ = "Integer32"
_Cdx6500BSTDCfgResponseTimeout_Object = MibTableColumn
cdx6500BSTDCfgResponseTimeout = _Cdx6500BSTDCfgResponseTimeout_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 14, 1, 11),
    _Cdx6500BSTDCfgResponseTimeout_Type()
)
cdx6500BSTDCfgResponseTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500BSTDCfgResponseTimeout.setStatus("mandatory")


class _Cdx6500BSTDCfgPadProtTimeout_Type(Integer32):
    """Custom type cdx6500BSTDCfgPadProtTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 60),
    )


_Cdx6500BSTDCfgPadProtTimeout_Type.__name__ = "Integer32"
_Cdx6500BSTDCfgPadProtTimeout_Object = MibTableColumn
cdx6500BSTDCfgPadProtTimeout = _Cdx6500BSTDCfgPadProtTimeout_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 14, 1, 12),
    _Cdx6500BSTDCfgPadProtTimeout_Type()
)
cdx6500BSTDCfgPadProtTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500BSTDCfgPadProtTimeout.setStatus("mandatory")


class _Cdx6500BSTDCfgTranNumbers_Type(Integer32):
    """Custom type cdx6500BSTDCfgTranNumbers based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              50)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("modulo2", 1),
          ("newvalDisable", 50))
    )


_Cdx6500BSTDCfgTranNumbers_Type.__name__ = "Integer32"
_Cdx6500BSTDCfgTranNumbers_Object = MibTableColumn
cdx6500BSTDCfgTranNumbers = _Cdx6500BSTDCfgTranNumbers_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 14, 1, 13),
    _Cdx6500BSTDCfgTranNumbers_Type()
)
cdx6500BSTDCfgTranNumbers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500BSTDCfgTranNumbers.setStatus("mandatory")


class _Cdx6500BSTDCfgContentionMode_Type(Integer32):
    """Custom type cdx6500BSTDCfgContentionMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              50)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1),
          ("newvalDisable", 50))
    )


_Cdx6500BSTDCfgContentionMode_Type.__name__ = "Integer32"
_Cdx6500BSTDCfgContentionMode_Object = MibTableColumn
cdx6500BSTDCfgContentionMode = _Cdx6500BSTDCfgContentionMode_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 14, 1, 14),
    _Cdx6500BSTDCfgContentionMode_Type()
)
cdx6500BSTDCfgContentionMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500BSTDCfgContentionMode.setStatus("mandatory")


class _Cdx6500BSTDCfgPortSubAddr_Type(DisplayString):
    """Custom type cdx6500BSTDCfgPortSubAddr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 3),
    )


_Cdx6500BSTDCfgPortSubAddr_Type.__name__ = "DisplayString"
_Cdx6500BSTDCfgPortSubAddr_Object = MibTableColumn
cdx6500BSTDCfgPortSubAddr = _Cdx6500BSTDCfgPortSubAddr_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 14, 1, 15),
    _Cdx6500BSTDCfgPortSubAddr_Type()
)
cdx6500BSTDCfgPortSubAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500BSTDCfgPortSubAddr.setStatus("mandatory")


class _Cdx6500BSTDCfgPortOptions_Type(Integer32):
    """Custom type cdx6500BSTDCfgPortOptions based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("deprecatedObj", 1)
    )


_Cdx6500BSTDCfgPortOptions_Type.__name__ = "Integer32"
_Cdx6500BSTDCfgPortOptions_Object = MibTableColumn
cdx6500BSTDCfgPortOptions = _Cdx6500BSTDCfgPortOptions_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 14, 1, 16),
    _Cdx6500BSTDCfgPortOptions_Type()
)
cdx6500BSTDCfgPortOptions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500BSTDCfgPortOptions.setStatus("deprecated")


class _Cdx6500BSTDCfgRestrictConnDest_Type(DisplayString):
    """Custom type cdx6500BSTDCfgRestrictConnDest based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 3),
    )


_Cdx6500BSTDCfgRestrictConnDest_Type.__name__ = "DisplayString"
_Cdx6500BSTDCfgRestrictConnDest_Object = MibTableColumn
cdx6500BSTDCfgRestrictConnDest = _Cdx6500BSTDCfgRestrictConnDest_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 14, 1, 17),
    _Cdx6500BSTDCfgRestrictConnDest_Type()
)
cdx6500BSTDCfgRestrictConnDest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500BSTDCfgRestrictConnDest.setStatus("mandatory")


class _Cdx6500BSTDCfgBillRec_Type(Integer32):
    """Custom type cdx6500BSTDCfgBillRec based on Integer32"""
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


_Cdx6500BSTDCfgBillRec_Type.__name__ = "Integer32"
_Cdx6500BSTDCfgBillRec_Object = MibTableColumn
cdx6500BSTDCfgBillRec = _Cdx6500BSTDCfgBillRec_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 14, 1, 18),
    _Cdx6500BSTDCfgBillRec_Type()
)
cdx6500BSTDCfgBillRec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500BSTDCfgBillRec.setStatus("mandatory")


class _Cdx6500BSTDPortOptString_Type(DisplayString):
    """Custom type cdx6500BSTDPortOptString based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(3, 16),
    )


_Cdx6500BSTDPortOptString_Type.__name__ = "DisplayString"
_Cdx6500BSTDPortOptString_Object = MibTableColumn
cdx6500BSTDPortOptString = _Cdx6500BSTDPortOptString_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 14, 1, 19),
    _Cdx6500BSTDPortOptString_Type()
)
cdx6500BSTDPortOptString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500BSTDPortOptString.setStatus("mandatory")


class _Cdx6500BSTDCfgElectricalInterfaceType_Type(Integer32):
    """Custom type cdx6500BSTDCfgElectricalInterfaceType based on Integer32"""
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


_Cdx6500BSTDCfgElectricalInterfaceType_Type.__name__ = "Integer32"
_Cdx6500BSTDCfgElectricalInterfaceType_Object = MibTableColumn
cdx6500BSTDCfgElectricalInterfaceType = _Cdx6500BSTDCfgElectricalInterfaceType_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 14, 1, 20),
    _Cdx6500BSTDCfgElectricalInterfaceType_Type()
)
cdx6500BSTDCfgElectricalInterfaceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500BSTDCfgElectricalInterfaceType.setStatus("mandatory")


class _Cdx6500BSTDCfgV24ElectricalInterfaceOption_Type(Integer32):
    """Custom type cdx6500BSTDCfgV24ElectricalInterfaceOption based on Integer32"""
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


_Cdx6500BSTDCfgV24ElectricalInterfaceOption_Type.__name__ = "Integer32"
_Cdx6500BSTDCfgV24ElectricalInterfaceOption_Object = MibTableColumn
cdx6500BSTDCfgV24ElectricalInterfaceOption = _Cdx6500BSTDCfgV24ElectricalInterfaceOption_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 14, 1, 21),
    _Cdx6500BSTDCfgV24ElectricalInterfaceOption_Type()
)
cdx6500BSTDCfgV24ElectricalInterfaceOption.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500BSTDCfgV24ElectricalInterfaceOption.setStatus("mandatory")


class _Cdx6500BSTDCfgHighSpeedElectricalInterfaceOption_Type(Integer32):
    """Custom type cdx6500BSTDCfgHighSpeedElectricalInterfaceOption based on Integer32"""
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


_Cdx6500BSTDCfgHighSpeedElectricalInterfaceOption_Type.__name__ = "Integer32"
_Cdx6500BSTDCfgHighSpeedElectricalInterfaceOption_Object = MibTableColumn
cdx6500BSTDCfgHighSpeedElectricalInterfaceOption = _Cdx6500BSTDCfgHighSpeedElectricalInterfaceOption_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 14, 1, 22),
    _Cdx6500BSTDCfgHighSpeedElectricalInterfaceOption_Type()
)
cdx6500BSTDCfgHighSpeedElectricalInterfaceOption.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500BSTDCfgHighSpeedElectricalInterfaceOption.setStatus("mandatory")
_Cdx6500PCTBSTDDeviceGroup_ObjectIdentity = ObjectIdentity
cdx6500PCTBSTDDeviceGroup = _Cdx6500PCTBSTDDeviceGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 8)
)
_Cdx6500PBCTBSTDDeviceTable_Object = MibTable
cdx6500PBCTBSTDDeviceTable = _Cdx6500PBCTBSTDDeviceTable_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 8, 1)
)
if mibBuilder.loadTexts:
    cdx6500PBCTBSTDDeviceTable.setStatus("mandatory")
_Cdx6500PBCTBSTDDeviceEntry_Object = MibTableRow
cdx6500PBCTBSTDDeviceEntry = _Cdx6500PBCTBSTDDeviceEntry_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 8, 1, 1)
)
cdx6500PBCTBSTDDeviceEntry.setIndexNames(
    (0, "BSTD-OPT-MIB", "cdx6500BSTDDevPortNumber"),
    (0, "BSTD-OPT-MIB", "cdx6500BSTDDevEntry"),
)
if mibBuilder.loadTexts:
    cdx6500PBCTBSTDDeviceEntry.setStatus("mandatory")


class _Cdx6500BSTDDevPortNumber_Type(Integer32):
    """Custom type cdx6500BSTDDevPortNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 54),
    )


_Cdx6500BSTDDevPortNumber_Type.__name__ = "Integer32"
_Cdx6500BSTDDevPortNumber_Object = MibTableColumn
cdx6500BSTDDevPortNumber = _Cdx6500BSTDDevPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 8, 1, 1, 1),
    _Cdx6500BSTDDevPortNumber_Type()
)
cdx6500BSTDDevPortNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500BSTDDevPortNumber.setStatus("mandatory")


class _Cdx6500BSTDDevEntry_Type(Integer32):
    """Custom type cdx6500BSTDDevEntry based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_Cdx6500BSTDDevEntry_Type.__name__ = "Integer32"
_Cdx6500BSTDDevEntry_Object = MibTableColumn
cdx6500BSTDDevEntry = _Cdx6500BSTDDevEntry_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 8, 1, 1, 2),
    _Cdx6500BSTDDevEntry_Type()
)
cdx6500BSTDDevEntry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500BSTDDevEntry.setStatus("mandatory")


class _Cdx6500BSTDStationAddr1_Type(DisplayString):
    """Custom type cdx6500BSTDStationAddr1 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_Cdx6500BSTDStationAddr1_Type.__name__ = "DisplayString"
_Cdx6500BSTDStationAddr1_Object = MibTableColumn
cdx6500BSTDStationAddr1 = _Cdx6500BSTDStationAddr1_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 8, 1, 1, 3),
    _Cdx6500BSTDStationAddr1_Type()
)
cdx6500BSTDStationAddr1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500BSTDStationAddr1.setStatus("mandatory")


class _Cdx6500BSTDStationAddr2_Type(DisplayString):
    """Custom type cdx6500BSTDStationAddr2 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_Cdx6500BSTDStationAddr2_Type.__name__ = "DisplayString"
_Cdx6500BSTDStationAddr2_Object = MibTableColumn
cdx6500BSTDStationAddr2 = _Cdx6500BSTDStationAddr2_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 8, 1, 1, 4),
    _Cdx6500BSTDStationAddr2_Type()
)
cdx6500BSTDStationAddr2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500BSTDStationAddr2.setStatus("mandatory")


class _Cdx6500BSTDDestStationAddr1_Type(DisplayString):
    """Custom type cdx6500BSTDDestStationAddr1 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_Cdx6500BSTDDestStationAddr1_Type.__name__ = "DisplayString"
_Cdx6500BSTDDestStationAddr1_Object = MibTableColumn
cdx6500BSTDDestStationAddr1 = _Cdx6500BSTDDestStationAddr1_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 8, 1, 1, 5),
    _Cdx6500BSTDDestStationAddr1_Type()
)
cdx6500BSTDDestStationAddr1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500BSTDDestStationAddr1.setStatus("mandatory")


class _Cdx6500BSTDDesstStationAddr2_Type(DisplayString):
    """Custom type cdx6500BSTDDesstStationAddr2 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_Cdx6500BSTDDesstStationAddr2_Type.__name__ = "DisplayString"
_Cdx6500BSTDDesstStationAddr2_Object = MibTableColumn
cdx6500BSTDDesstStationAddr2 = _Cdx6500BSTDDesstStationAddr2_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 8, 1, 1, 6),
    _Cdx6500BSTDDesstStationAddr2_Type()
)
cdx6500BSTDDesstStationAddr2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500BSTDDesstStationAddr2.setStatus("mandatory")


class _Cdx6500BSTDGroupAddr1_Type(DisplayString):
    """Custom type cdx6500BSTDGroupAddr1 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_Cdx6500BSTDGroupAddr1_Type.__name__ = "DisplayString"
_Cdx6500BSTDGroupAddr1_Object = MibTableColumn
cdx6500BSTDGroupAddr1 = _Cdx6500BSTDGroupAddr1_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 8, 1, 1, 7),
    _Cdx6500BSTDGroupAddr1_Type()
)
cdx6500BSTDGroupAddr1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500BSTDGroupAddr1.setStatus("mandatory")


class _Cdx6500BSTDGroupAddr2_Type(DisplayString):
    """Custom type cdx6500BSTDGroupAddr2 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_Cdx6500BSTDGroupAddr2_Type.__name__ = "DisplayString"
_Cdx6500BSTDGroupAddr2_Object = MibTableColumn
cdx6500BSTDGroupAddr2 = _Cdx6500BSTDGroupAddr2_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 8, 1, 1, 8),
    _Cdx6500BSTDGroupAddr2_Type()
)
cdx6500BSTDGroupAddr2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500BSTDGroupAddr2.setStatus("mandatory")


class _Cdx6500BSTDCallMnemonic_Type(DisplayString):
    """Custom type cdx6500BSTDCallMnemonic based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_Cdx6500BSTDCallMnemonic_Type.__name__ = "DisplayString"
_Cdx6500BSTDCallMnemonic_Object = MibTableColumn
cdx6500BSTDCallMnemonic = _Cdx6500BSTDCallMnemonic_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 8, 1, 1, 9),
    _Cdx6500BSTDCallMnemonic_Type()
)
cdx6500BSTDCallMnemonic.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500BSTDCallMnemonic.setStatus("mandatory")


class _Cdx6500BSTDStationEnabled_Type(Integer32):
    """Custom type cdx6500BSTDStationEnabled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              50)
        )
    )
    namedValues = NamedValues(
        *(("newvalNo", 50),
          ("no", 0),
          ("yes", 1))
    )


_Cdx6500BSTDStationEnabled_Type.__name__ = "Integer32"
_Cdx6500BSTDStationEnabled_Object = MibTableColumn
cdx6500BSTDStationEnabled = _Cdx6500BSTDStationEnabled_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 8, 1, 1, 10),
    _Cdx6500BSTDStationEnabled_Type()
)
cdx6500BSTDStationEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500BSTDStationEnabled.setStatus("mandatory")
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
_Cdx6500PPSTBSTDPortStatTable_Object = MibTable
cdx6500PPSTBSTDPortStatTable = _Cdx6500PPSTBSTDPortStatTable_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 14)
)
if mibBuilder.loadTexts:
    cdx6500PPSTBSTDPortStatTable.setStatus("mandatory")
_Cdx6500BSTDPortStatEntry_Object = MibTableRow
cdx6500BSTDPortStatEntry = _Cdx6500BSTDPortStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 14, 1)
)
cdx6500BSTDPortStatEntry.setIndexNames(
    (0, "BSTD-OPT-MIB", "cdx6500BSTDStatPortNumber"),
)
if mibBuilder.loadTexts:
    cdx6500BSTDPortStatEntry.setStatus("mandatory")


class _Cdx6500BSTDStatPortNumber_Type(Integer32):
    """Custom type cdx6500BSTDStatPortNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 54),
    )


_Cdx6500BSTDStatPortNumber_Type.__name__ = "Integer32"
_Cdx6500BSTDStatPortNumber_Object = MibTableColumn
cdx6500BSTDStatPortNumber = _Cdx6500BSTDStatPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 14, 1, 1),
    _Cdx6500BSTDStatPortNumber_Type()
)
cdx6500BSTDStatPortNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500BSTDStatPortNumber.setStatus("mandatory")


class _Cdx6500BSTDPortStatus_Type(Integer32):
    """Custom type cdx6500BSTDPortStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              50)
        )
    )
    namedValues = NamedValues(
        *(("busyOut", 2),
          ("disabled", 0),
          ("down", 4),
          ("enabled", 1),
          ("newvalDisabled", 50),
          ("up", 3))
    )


_Cdx6500BSTDPortStatus_Type.__name__ = "Integer32"
_Cdx6500BSTDPortStatus_Object = MibTableColumn
cdx6500BSTDPortStatus = _Cdx6500BSTDPortStatus_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 14, 1, 2),
    _Cdx6500BSTDPortStatus_Type()
)
cdx6500BSTDPortStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500BSTDPortStatus.setStatus("mandatory")


class _Cdx6500BSTDPortState_Type(DisplayString):
    """Custom type cdx6500BSTDPortState based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 10),
    )


_Cdx6500BSTDPortState_Type.__name__ = "DisplayString"
_Cdx6500BSTDPortState_Object = MibTableColumn
cdx6500BSTDPortState = _Cdx6500BSTDPortState_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 14, 1, 3),
    _Cdx6500BSTDPortState_Type()
)
cdx6500BSTDPortState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500BSTDPortState.setStatus("mandatory")
_Cdx6500BSTDPortSpeed_Type = Integer32
_Cdx6500BSTDPortSpeed_Object = MibTableColumn
cdx6500BSTDPortSpeed = _Cdx6500BSTDPortSpeed_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 14, 1, 4),
    _Cdx6500BSTDPortSpeed_Type()
)
cdx6500BSTDPortSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500BSTDPortSpeed.setStatus("mandatory")


class _Cdx6500BSTDPortUtilIn_Type(Integer32):
    """Custom type cdx6500BSTDPortUtilIn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_Cdx6500BSTDPortUtilIn_Type.__name__ = "Integer32"
_Cdx6500BSTDPortUtilIn_Object = MibTableColumn
cdx6500BSTDPortUtilIn = _Cdx6500BSTDPortUtilIn_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 14, 1, 5),
    _Cdx6500BSTDPortUtilIn_Type()
)
cdx6500BSTDPortUtilIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500BSTDPortUtilIn.setStatus("mandatory")


class _Cdx6500BSTDPortUtilOut_Type(Integer32):
    """Custom type cdx6500BSTDPortUtilOut based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_Cdx6500BSTDPortUtilOut_Type.__name__ = "Integer32"
_Cdx6500BSTDPortUtilOut_Object = MibTableColumn
cdx6500BSTDPortUtilOut = _Cdx6500BSTDPortUtilOut_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 14, 1, 6),
    _Cdx6500BSTDPortUtilOut_Type()
)
cdx6500BSTDPortUtilOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500BSTDPortUtilOut.setStatus("mandatory")
_Cdx6500BSTDInMsgs_Type = Counter32
_Cdx6500BSTDInMsgs_Object = MibTableColumn
cdx6500BSTDInMsgs = _Cdx6500BSTDInMsgs_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 14, 1, 7),
    _Cdx6500BSTDInMsgs_Type()
)
cdx6500BSTDInMsgs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500BSTDInMsgs.setStatus("mandatory")
_Cdx6500BSTDOutMsgs_Type = Counter32
_Cdx6500BSTDOutMsgs_Object = MibTableColumn
cdx6500BSTDOutMsgs = _Cdx6500BSTDOutMsgs_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 14, 1, 8),
    _Cdx6500BSTDOutMsgs_Type()
)
cdx6500BSTDOutMsgs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500BSTDOutMsgs.setStatus("mandatory")
_Cdx6500BSTDInChars_Type = Counter32
_Cdx6500BSTDInChars_Object = MibTableColumn
cdx6500BSTDInChars = _Cdx6500BSTDInChars_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 14, 1, 9),
    _Cdx6500BSTDInChars_Type()
)
cdx6500BSTDInChars.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500BSTDInChars.setStatus("mandatory")
_Cdx6500BSTDOutChars_Type = Counter32
_Cdx6500BSTDOutChars_Object = MibTableColumn
cdx6500BSTDOutChars = _Cdx6500BSTDOutChars_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 14, 1, 10),
    _Cdx6500BSTDOutChars_Type()
)
cdx6500BSTDOutChars.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500BSTDOutChars.setStatus("mandatory")


class _Cdx6500BSTDCharRateIn_Type(Integer32):
    """Custom type cdx6500BSTDCharRateIn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Cdx6500BSTDCharRateIn_Type.__name__ = "Integer32"
_Cdx6500BSTDCharRateIn_Object = MibTableColumn
cdx6500BSTDCharRateIn = _Cdx6500BSTDCharRateIn_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 14, 1, 11),
    _Cdx6500BSTDCharRateIn_Type()
)
cdx6500BSTDCharRateIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500BSTDCharRateIn.setStatus("mandatory")


class _Cdx6500BSTDCharRateOut_Type(Integer32):
    """Custom type cdx6500BSTDCharRateOut based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Cdx6500BSTDCharRateOut_Type.__name__ = "Integer32"
_Cdx6500BSTDCharRateOut_Object = MibTableColumn
cdx6500BSTDCharRateOut = _Cdx6500BSTDCharRateOut_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 14, 1, 12),
    _Cdx6500BSTDCharRateOut_Type()
)
cdx6500BSTDCharRateOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500BSTDCharRateOut.setStatus("mandatory")
_Cdx6500BSTDCrcBccErrs_Type = Counter32
_Cdx6500BSTDCrcBccErrs_Object = MibTableColumn
cdx6500BSTDCrcBccErrs = _Cdx6500BSTDCrcBccErrs_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 14, 1, 13),
    _Cdx6500BSTDCrcBccErrs_Type()
)
cdx6500BSTDCrcBccErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500BSTDCrcBccErrs.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "BSTD-OPT-MIB",
    **{"DisplayString": DisplayString,
       "codex": codex,
       "cdxProductSpecific": cdxProductSpecific,
       "cdx6500": cdx6500,
       "cdx6500Configuration": cdx6500Configuration,
       "cdx6500CfgProtocolGroup": cdx6500CfgProtocolGroup,
       "cdx6500PCTPortProtocolGroup": cdx6500PCTPortProtocolGroup,
       "cdx6500PPCTBSTDPortTable": cdx6500PPCTBSTDPortTable,
       "cdx6500PPCTBSTDPortEntry": cdx6500PPCTBSTDPortEntry,
       "cdx6500BSTDCfgPortNumber": cdx6500BSTDCfgPortNumber,
       "cdx6500BSTDCfgPADType": cdx6500BSTDCfgPADType,
       "cdx6500BSTDCfgLineInterface": cdx6500BSTDCfgLineInterface,
       "cdx6500BSTDCfgClockSource": cdx6500BSTDCfgClockSource,
       "cdx6500BSTDCfgClockSpeed": cdx6500BSTDCfgClockSpeed,
       "cdx6500BSTDCfgSyncContention": cdx6500BSTDCfgSyncContention,
       "cdx6500BSTDCfgAsyncConnType": cdx6500BSTDCfgAsyncConnType,
       "cdx6500BSTDCfgNumDevices": cdx6500BSTDCfgNumDevices,
       "cdx6500BSTDCfgServTimer": cdx6500BSTDCfgServTimer,
       "cdx6500BSTDCfgErrThreshCount": cdx6500BSTDCfgErrThreshCount,
       "cdx6500BSTDCfgResponseTimeout": cdx6500BSTDCfgResponseTimeout,
       "cdx6500BSTDCfgPadProtTimeout": cdx6500BSTDCfgPadProtTimeout,
       "cdx6500BSTDCfgTranNumbers": cdx6500BSTDCfgTranNumbers,
       "cdx6500BSTDCfgContentionMode": cdx6500BSTDCfgContentionMode,
       "cdx6500BSTDCfgPortSubAddr": cdx6500BSTDCfgPortSubAddr,
       "cdx6500BSTDCfgPortOptions": cdx6500BSTDCfgPortOptions,
       "cdx6500BSTDCfgRestrictConnDest": cdx6500BSTDCfgRestrictConnDest,
       "cdx6500BSTDCfgBillRec": cdx6500BSTDCfgBillRec,
       "cdx6500BSTDPortOptString": cdx6500BSTDPortOptString,
       "cdx6500BSTDCfgElectricalInterfaceType": cdx6500BSTDCfgElectricalInterfaceType,
       "cdx6500BSTDCfgV24ElectricalInterfaceOption": cdx6500BSTDCfgV24ElectricalInterfaceOption,
       "cdx6500BSTDCfgHighSpeedElectricalInterfaceOption": cdx6500BSTDCfgHighSpeedElectricalInterfaceOption,
       "cdx6500PCTBSTDDeviceGroup": cdx6500PCTBSTDDeviceGroup,
       "cdx6500PBCTBSTDDeviceTable": cdx6500PBCTBSTDDeviceTable,
       "cdx6500PBCTBSTDDeviceEntry": cdx6500PBCTBSTDDeviceEntry,
       "cdx6500BSTDDevPortNumber": cdx6500BSTDDevPortNumber,
       "cdx6500BSTDDevEntry": cdx6500BSTDDevEntry,
       "cdx6500BSTDStationAddr1": cdx6500BSTDStationAddr1,
       "cdx6500BSTDStationAddr2": cdx6500BSTDStationAddr2,
       "cdx6500BSTDDestStationAddr1": cdx6500BSTDDestStationAddr1,
       "cdx6500BSTDDesstStationAddr2": cdx6500BSTDDesstStationAddr2,
       "cdx6500BSTDGroupAddr1": cdx6500BSTDGroupAddr1,
       "cdx6500BSTDGroupAddr2": cdx6500BSTDGroupAddr2,
       "cdx6500BSTDCallMnemonic": cdx6500BSTDCallMnemonic,
       "cdx6500BSTDStationEnabled": cdx6500BSTDStationEnabled,
       "cdx6500Statistics": cdx6500Statistics,
       "cdx6500StatProtocolGroup": cdx6500StatProtocolGroup,
       "cdx6500PSTPortProtocolGroup": cdx6500PSTPortProtocolGroup,
       "cdx6500PPSTBSTDPortStatTable": cdx6500PPSTBSTDPortStatTable,
       "cdx6500BSTDPortStatEntry": cdx6500BSTDPortStatEntry,
       "cdx6500BSTDStatPortNumber": cdx6500BSTDStatPortNumber,
       "cdx6500BSTDPortStatus": cdx6500BSTDPortStatus,
       "cdx6500BSTDPortState": cdx6500BSTDPortState,
       "cdx6500BSTDPortSpeed": cdx6500BSTDPortSpeed,
       "cdx6500BSTDPortUtilIn": cdx6500BSTDPortUtilIn,
       "cdx6500BSTDPortUtilOut": cdx6500BSTDPortUtilOut,
       "cdx6500BSTDInMsgs": cdx6500BSTDInMsgs,
       "cdx6500BSTDOutMsgs": cdx6500BSTDOutMsgs,
       "cdx6500BSTDInChars": cdx6500BSTDInChars,
       "cdx6500BSTDOutChars": cdx6500BSTDOutChars,
       "cdx6500BSTDCharRateIn": cdx6500BSTDCharRateIn,
       "cdx6500BSTDCharRateOut": cdx6500BSTDCharRateOut,
       "cdx6500BSTDCrcBccErrs": cdx6500BSTDCrcBccErrs}
)
