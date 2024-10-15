# SNMP MIB module (NCRBSC-OPT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/NCRBSC-OPT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:25:15 2024
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
_Cdx6500PPCTNCRBisyncTable_Object = MibTable
cdx6500PPCTNCRBisyncTable = _Cdx6500PPCTNCRBisyncTable_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 17)
)
if mibBuilder.loadTexts:
    cdx6500PPCTNCRBisyncTable.setStatus("mandatory")
_Cdx6500PPCTNCRBisyncEntry_Object = MibTableRow
cdx6500PPCTNCRBisyncEntry = _Cdx6500PPCTNCRBisyncEntry_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 17, 1)
)
cdx6500PPCTNCRBisyncEntry.setIndexNames(
    (0, "NCRBSC-OPT-MIB", "cdx6500NCRBSCCfgPortNumber"),
)
if mibBuilder.loadTexts:
    cdx6500PPCTNCRBisyncEntry.setStatus("mandatory")


class _Cdx6500NCRBSCCfgPortNumber_Type(Integer32):
    """Custom type cdx6500NCRBSCCfgPortNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 54),
    )


_Cdx6500NCRBSCCfgPortNumber_Type.__name__ = "Integer32"
_Cdx6500NCRBSCCfgPortNumber_Object = MibTableColumn
cdx6500NCRBSCCfgPortNumber = _Cdx6500NCRBSCCfgPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 17, 1, 1),
    _Cdx6500NCRBSCCfgPortNumber_Type()
)
cdx6500NCRBSCCfgPortNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500NCRBSCCfgPortNumber.setStatus("mandatory")


class _Cdx6500NCRBSCCfgPADType_Type(Integer32):
    """Custom type cdx6500NCRBSCCfgPADType based on Integer32"""
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


_Cdx6500NCRBSCCfgPADType_Type.__name__ = "Integer32"
_Cdx6500NCRBSCCfgPADType_Object = MibTableColumn
cdx6500NCRBSCCfgPADType = _Cdx6500NCRBSCCfgPADType_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 17, 1, 2),
    _Cdx6500NCRBSCCfgPADType_Type()
)
cdx6500NCRBSCCfgPADType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500NCRBSCCfgPADType.setStatus("mandatory")


class _Cdx6500NCRBSCCfgClockSource_Type(Integer32):
    """Custom type cdx6500NCRBSCCfgClockSource based on Integer32"""
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


_Cdx6500NCRBSCCfgClockSource_Type.__name__ = "Integer32"
_Cdx6500NCRBSCCfgClockSource_Object = MibTableColumn
cdx6500NCRBSCCfgClockSource = _Cdx6500NCRBSCCfgClockSource_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 17, 1, 3),
    _Cdx6500NCRBSCCfgClockSource_Type()
)
cdx6500NCRBSCCfgClockSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500NCRBSCCfgClockSource.setStatus("mandatory")


class _Cdx6500NCRBSCCfgClockSpeed_Type(Integer32):
    """Custom type cdx6500NCRBSCCfgClockSpeed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1200, 19200),
    )


_Cdx6500NCRBSCCfgClockSpeed_Type.__name__ = "Integer32"
_Cdx6500NCRBSCCfgClockSpeed_Object = MibTableColumn
cdx6500NCRBSCCfgClockSpeed = _Cdx6500NCRBSCCfgClockSpeed_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 17, 1, 4),
    _Cdx6500NCRBSCCfgClockSpeed_Type()
)
cdx6500NCRBSCCfgClockSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500NCRBSCCfgClockSpeed.setStatus("mandatory")


class _Cdx6500NCRBSCCfgContention_Type(Integer32):
    """Custom type cdx6500NCRBSCCfgContention based on Integer32"""
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


_Cdx6500NCRBSCCfgContention_Type.__name__ = "Integer32"
_Cdx6500NCRBSCCfgContention_Object = MibTableColumn
cdx6500NCRBSCCfgContention = _Cdx6500NCRBSCCfgContention_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 17, 1, 5),
    _Cdx6500NCRBSCCfgContention_Type()
)
cdx6500NCRBSCCfgContention.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500NCRBSCCfgContention.setStatus("mandatory")


class _Cdx6500NCRBSCCfgNumDevices_Type(Integer32):
    """Custom type cdx6500NCRBSCCfgNumDevices based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_Cdx6500NCRBSCCfgNumDevices_Type.__name__ = "Integer32"
_Cdx6500NCRBSCCfgNumDevices_Object = MibTableColumn
cdx6500NCRBSCCfgNumDevices = _Cdx6500NCRBSCCfgNumDevices_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 17, 1, 6),
    _Cdx6500NCRBSCCfgNumDevices_Type()
)
cdx6500NCRBSCCfgNumDevices.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500NCRBSCCfgNumDevices.setStatus("mandatory")


class _Cdx6500NCRBSCCfgServTimer_Type(Integer32):
    """Custom type cdx6500NCRBSCCfgServTimer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 60),
    )


_Cdx6500NCRBSCCfgServTimer_Type.__name__ = "Integer32"
_Cdx6500NCRBSCCfgServTimer_Object = MibTableColumn
cdx6500NCRBSCCfgServTimer = _Cdx6500NCRBSCCfgServTimer_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 17, 1, 7),
    _Cdx6500NCRBSCCfgServTimer_Type()
)
cdx6500NCRBSCCfgServTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500NCRBSCCfgServTimer.setStatus("mandatory")


class _Cdx6500NCRBSCCfgErrThreshCount_Type(Integer32):
    """Custom type cdx6500NCRBSCCfgErrThreshCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_Cdx6500NCRBSCCfgErrThreshCount_Type.__name__ = "Integer32"
_Cdx6500NCRBSCCfgErrThreshCount_Object = MibTableColumn
cdx6500NCRBSCCfgErrThreshCount = _Cdx6500NCRBSCCfgErrThreshCount_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 17, 1, 8),
    _Cdx6500NCRBSCCfgErrThreshCount_Type()
)
cdx6500NCRBSCCfgErrThreshCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500NCRBSCCfgErrThreshCount.setStatus("mandatory")


class _Cdx6500NCRBSCCfgRetranTimeout_Type(Integer32):
    """Custom type cdx6500NCRBSCCfgRetranTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_Cdx6500NCRBSCCfgRetranTimeout_Type.__name__ = "Integer32"
_Cdx6500NCRBSCCfgRetranTimeout_Object = MibTableColumn
cdx6500NCRBSCCfgRetranTimeout = _Cdx6500NCRBSCCfgRetranTimeout_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 17, 1, 10),
    _Cdx6500NCRBSCCfgRetranTimeout_Type()
)
cdx6500NCRBSCCfgRetranTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500NCRBSCCfgRetranTimeout.setStatus("mandatory")


class _Cdx6500NCRBSCCfgInterBuffTimeout_Type(Integer32):
    """Custom type cdx6500NCRBSCCfgInterBuffTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_Cdx6500NCRBSCCfgInterBuffTimeout_Type.__name__ = "Integer32"
_Cdx6500NCRBSCCfgInterBuffTimeout_Object = MibTableColumn
cdx6500NCRBSCCfgInterBuffTimeout = _Cdx6500NCRBSCCfgInterBuffTimeout_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 17, 1, 11),
    _Cdx6500NCRBSCCfgInterBuffTimeout_Type()
)
cdx6500NCRBSCCfgInterBuffTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500NCRBSCCfgInterBuffTimeout.setStatus("mandatory")


class _Cdx6500NCRBSCCfgPortSubAddr_Type(DisplayString):
    """Custom type cdx6500NCRBSCCfgPortSubAddr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 3),
    )


_Cdx6500NCRBSCCfgPortSubAddr_Type.__name__ = "DisplayString"
_Cdx6500NCRBSCCfgPortSubAddr_Object = MibTableColumn
cdx6500NCRBSCCfgPortSubAddr = _Cdx6500NCRBSCCfgPortSubAddr_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 17, 1, 12),
    _Cdx6500NCRBSCCfgPortSubAddr_Type()
)
cdx6500NCRBSCCfgPortSubAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500NCRBSCCfgPortSubAddr.setStatus("mandatory")
_Cdx6500NCRBSCCfgPortOptions_Type = DisplayString
_Cdx6500NCRBSCCfgPortOptions_Object = MibTableColumn
cdx6500NCRBSCCfgPortOptions = _Cdx6500NCRBSCCfgPortOptions_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 17, 1, 13),
    _Cdx6500NCRBSCCfgPortOptions_Type()
)
cdx6500NCRBSCCfgPortOptions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500NCRBSCCfgPortOptions.setStatus("mandatory")


class _Cdx6500NCRBSCCfgRestrictConnDest_Type(DisplayString):
    """Custom type cdx6500NCRBSCCfgRestrictConnDest based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_Cdx6500NCRBSCCfgRestrictConnDest_Type.__name__ = "DisplayString"
_Cdx6500NCRBSCCfgRestrictConnDest_Object = MibTableColumn
cdx6500NCRBSCCfgRestrictConnDest = _Cdx6500NCRBSCCfgRestrictConnDest_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 17, 1, 14),
    _Cdx6500NCRBSCCfgRestrictConnDest_Type()
)
cdx6500NCRBSCCfgRestrictConnDest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500NCRBSCCfgRestrictConnDest.setStatus("mandatory")


class _Cdx6500NCRBSCCfgBillRec_Type(Integer32):
    """Custom type cdx6500NCRBSCCfgBillRec based on Integer32"""
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


_Cdx6500NCRBSCCfgBillRec_Type.__name__ = "Integer32"
_Cdx6500NCRBSCCfgBillRec_Object = MibTableColumn
cdx6500NCRBSCCfgBillRec = _Cdx6500NCRBSCCfgBillRec_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 17, 1, 15),
    _Cdx6500NCRBSCCfgBillRec_Type()
)
cdx6500NCRBSCCfgBillRec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500NCRBSCCfgBillRec.setStatus("mandatory")


class _Cdx6500NCRBSCCfgElectricalInterfaceType_Type(Integer32):
    """Custom type cdx6500NCRBSCCfgElectricalInterfaceType based on Integer32"""
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


_Cdx6500NCRBSCCfgElectricalInterfaceType_Type.__name__ = "Integer32"
_Cdx6500NCRBSCCfgElectricalInterfaceType_Object = MibTableColumn
cdx6500NCRBSCCfgElectricalInterfaceType = _Cdx6500NCRBSCCfgElectricalInterfaceType_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 17, 1, 16),
    _Cdx6500NCRBSCCfgElectricalInterfaceType_Type()
)
cdx6500NCRBSCCfgElectricalInterfaceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500NCRBSCCfgElectricalInterfaceType.setStatus("mandatory")


class _Cdx6500NCRBSCCfgV24ElectricalInterfaceOption_Type(Integer32):
    """Custom type cdx6500NCRBSCCfgV24ElectricalInterfaceOption based on Integer32"""
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


_Cdx6500NCRBSCCfgV24ElectricalInterfaceOption_Type.__name__ = "Integer32"
_Cdx6500NCRBSCCfgV24ElectricalInterfaceOption_Object = MibTableColumn
cdx6500NCRBSCCfgV24ElectricalInterfaceOption = _Cdx6500NCRBSCCfgV24ElectricalInterfaceOption_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 17, 1, 17),
    _Cdx6500NCRBSCCfgV24ElectricalInterfaceOption_Type()
)
cdx6500NCRBSCCfgV24ElectricalInterfaceOption.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500NCRBSCCfgV24ElectricalInterfaceOption.setStatus("mandatory")


class _Cdx6500NCRBSCCfgHighSpeedElectricalInterfaceOption_Type(Integer32):
    """Custom type cdx6500NCRBSCCfgHighSpeedElectricalInterfaceOption based on Integer32"""
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


_Cdx6500NCRBSCCfgHighSpeedElectricalInterfaceOption_Type.__name__ = "Integer32"
_Cdx6500NCRBSCCfgHighSpeedElectricalInterfaceOption_Object = MibTableColumn
cdx6500NCRBSCCfgHighSpeedElectricalInterfaceOption = _Cdx6500NCRBSCCfgHighSpeedElectricalInterfaceOption_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 17, 1, 18),
    _Cdx6500NCRBSCCfgHighSpeedElectricalInterfaceOption_Type()
)
cdx6500NCRBSCCfgHighSpeedElectricalInterfaceOption.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500NCRBSCCfgHighSpeedElectricalInterfaceOption.setStatus("mandatory")
_Cdx6500PCTNCRBSCDeviceGroup_ObjectIdentity = ObjectIdentity
cdx6500PCTNCRBSCDeviceGroup = _Cdx6500PCTNCRBSCDeviceGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 7)
)
_Cdx6500PBCTNCRBSCDeviceTable_Object = MibTable
cdx6500PBCTNCRBSCDeviceTable = _Cdx6500PBCTNCRBSCDeviceTable_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 7, 1)
)
if mibBuilder.loadTexts:
    cdx6500PBCTNCRBSCDeviceTable.setStatus("mandatory")
_Cdx6500PBCTNCRBSCDeviceEntry_Object = MibTableRow
cdx6500PBCTNCRBSCDeviceEntry = _Cdx6500PBCTNCRBSCDeviceEntry_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 7, 1, 1)
)
cdx6500PBCTNCRBSCDeviceEntry.setIndexNames(
    (0, "NCRBSC-OPT-MIB", "cdx6500ncrbscDevPortNumber"),
    (0, "NCRBSC-OPT-MIB", "cdx6500ncrbscDevEntry"),
)
if mibBuilder.loadTexts:
    cdx6500PBCTNCRBSCDeviceEntry.setStatus("mandatory")


class _Cdx6500ncrbscDevPortNumber_Type(Integer32):
    """Custom type cdx6500ncrbscDevPortNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 54),
    )


_Cdx6500ncrbscDevPortNumber_Type.__name__ = "Integer32"
_Cdx6500ncrbscDevPortNumber_Object = MibTableColumn
cdx6500ncrbscDevPortNumber = _Cdx6500ncrbscDevPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 7, 1, 1, 1),
    _Cdx6500ncrbscDevPortNumber_Type()
)
cdx6500ncrbscDevPortNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500ncrbscDevPortNumber.setStatus("mandatory")


class _Cdx6500ncrbscDevEntry_Type(Integer32):
    """Custom type cdx6500ncrbscDevEntry based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_Cdx6500ncrbscDevEntry_Type.__name__ = "Integer32"
_Cdx6500ncrbscDevEntry_Object = MibTableColumn
cdx6500ncrbscDevEntry = _Cdx6500ncrbscDevEntry_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 7, 1, 1, 2),
    _Cdx6500ncrbscDevEntry_Type()
)
cdx6500ncrbscDevEntry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500ncrbscDevEntry.setStatus("mandatory")


class _Cdx6500ncrbscBSCControlUnitAddr_Type(DisplayString):
    """Custom type cdx6500ncrbscBSCControlUnitAddr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 3),
    )


_Cdx6500ncrbscBSCControlUnitAddr_Type.__name__ = "DisplayString"
_Cdx6500ncrbscBSCControlUnitAddr_Object = MibTableColumn
cdx6500ncrbscBSCControlUnitAddr = _Cdx6500ncrbscBSCControlUnitAddr_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 7, 1, 1, 3),
    _Cdx6500ncrbscBSCControlUnitAddr_Type()
)
cdx6500ncrbscBSCControlUnitAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500ncrbscBSCControlUnitAddr.setStatus("mandatory")


class _Cdx6500ncrbscDestControlUnitAddr_Type(DisplayString):
    """Custom type cdx6500ncrbscDestControlUnitAddr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 3),
    )


_Cdx6500ncrbscDestControlUnitAddr_Type.__name__ = "DisplayString"
_Cdx6500ncrbscDestControlUnitAddr_Object = MibTableColumn
cdx6500ncrbscDestControlUnitAddr = _Cdx6500ncrbscDestControlUnitAddr_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 7, 1, 1, 4),
    _Cdx6500ncrbscDestControlUnitAddr_Type()
)
cdx6500ncrbscDestControlUnitAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500ncrbscDestControlUnitAddr.setStatus("mandatory")


class _Cdx6500ncrbscAutocallMnemonic_Type(DisplayString):
    """Custom type cdx6500ncrbscAutocallMnemonic based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_Cdx6500ncrbscAutocallMnemonic_Type.__name__ = "DisplayString"
_Cdx6500ncrbscAutocallMnemonic_Object = MibTableColumn
cdx6500ncrbscAutocallMnemonic = _Cdx6500ncrbscAutocallMnemonic_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 7, 1, 1, 5),
    _Cdx6500ncrbscAutocallMnemonic_Type()
)
cdx6500ncrbscAutocallMnemonic.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500ncrbscAutocallMnemonic.setStatus("mandatory")


class _Cdx6500ncrbscDeviceEnabled_Type(Integer32):
    """Custom type cdx6500ncrbscDeviceEnabled based on Integer32"""
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


_Cdx6500ncrbscDeviceEnabled_Type.__name__ = "Integer32"
_Cdx6500ncrbscDeviceEnabled_Object = MibTableColumn
cdx6500ncrbscDeviceEnabled = _Cdx6500ncrbscDeviceEnabled_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 7, 1, 1, 6),
    _Cdx6500ncrbscDeviceEnabled_Type()
)
cdx6500ncrbscDeviceEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500ncrbscDeviceEnabled.setStatus("mandatory")
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
_Cdx6500PPSTNCRBisyncTable_Object = MibTable
cdx6500PPSTNCRBisyncTable = _Cdx6500PPSTNCRBisyncTable_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 17)
)
if mibBuilder.loadTexts:
    cdx6500PPSTNCRBisyncTable.setStatus("mandatory")
_Cdx6500ncrbscPortStatEntry_Object = MibTableRow
cdx6500ncrbscPortStatEntry = _Cdx6500ncrbscPortStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 17, 1)
)
cdx6500ncrbscPortStatEntry.setIndexNames(
    (0, "NCRBSC-OPT-MIB", "cdx6500ncrbscStatPortNumber"),
)
if mibBuilder.loadTexts:
    cdx6500ncrbscPortStatEntry.setStatus("mandatory")


class _Cdx6500ncrbscStatPortNumber_Type(Integer32):
    """Custom type cdx6500ncrbscStatPortNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 54),
    )


_Cdx6500ncrbscStatPortNumber_Type.__name__ = "Integer32"
_Cdx6500ncrbscStatPortNumber_Object = MibTableColumn
cdx6500ncrbscStatPortNumber = _Cdx6500ncrbscStatPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 17, 1, 1),
    _Cdx6500ncrbscStatPortNumber_Type()
)
cdx6500ncrbscStatPortNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500ncrbscStatPortNumber.setStatus("mandatory")


class _Cdx6500ncrbscPortStatus_Type(Integer32):
    """Custom type cdx6500ncrbscPortStatus based on Integer32"""
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


_Cdx6500ncrbscPortStatus_Type.__name__ = "Integer32"
_Cdx6500ncrbscPortStatus_Object = MibTableColumn
cdx6500ncrbscPortStatus = _Cdx6500ncrbscPortStatus_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 17, 1, 2),
    _Cdx6500ncrbscPortStatus_Type()
)
cdx6500ncrbscPortStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500ncrbscPortStatus.setStatus("mandatory")


class _Cdx6500ncrbscPortState_Type(DisplayString):
    """Custom type cdx6500ncrbscPortState based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 10),
    )


_Cdx6500ncrbscPortState_Type.__name__ = "DisplayString"
_Cdx6500ncrbscPortState_Object = MibTableColumn
cdx6500ncrbscPortState = _Cdx6500ncrbscPortState_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 17, 1, 3),
    _Cdx6500ncrbscPortState_Type()
)
cdx6500ncrbscPortState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500ncrbscPortState.setStatus("mandatory")
_Cdx6500ncrbscPortSpeed_Type = Integer32
_Cdx6500ncrbscPortSpeed_Object = MibTableColumn
cdx6500ncrbscPortSpeed = _Cdx6500ncrbscPortSpeed_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 17, 1, 4),
    _Cdx6500ncrbscPortSpeed_Type()
)
cdx6500ncrbscPortSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500ncrbscPortSpeed.setStatus("mandatory")


class _Cdx6500ncrbscPortUtilIn_Type(Integer32):
    """Custom type cdx6500ncrbscPortUtilIn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_Cdx6500ncrbscPortUtilIn_Type.__name__ = "Integer32"
_Cdx6500ncrbscPortUtilIn_Object = MibTableColumn
cdx6500ncrbscPortUtilIn = _Cdx6500ncrbscPortUtilIn_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 17, 1, 5),
    _Cdx6500ncrbscPortUtilIn_Type()
)
cdx6500ncrbscPortUtilIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500ncrbscPortUtilIn.setStatus("mandatory")


class _Cdx6500ncrbscPortUtilOut_Type(Integer32):
    """Custom type cdx6500ncrbscPortUtilOut based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_Cdx6500ncrbscPortUtilOut_Type.__name__ = "Integer32"
_Cdx6500ncrbscPortUtilOut_Object = MibTableColumn
cdx6500ncrbscPortUtilOut = _Cdx6500ncrbscPortUtilOut_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 17, 1, 6),
    _Cdx6500ncrbscPortUtilOut_Type()
)
cdx6500ncrbscPortUtilOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500ncrbscPortUtilOut.setStatus("mandatory")
_Cdx6500ncrbscInMsgs_Type = Counter32
_Cdx6500ncrbscInMsgs_Object = MibTableColumn
cdx6500ncrbscInMsgs = _Cdx6500ncrbscInMsgs_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 17, 1, 7),
    _Cdx6500ncrbscInMsgs_Type()
)
cdx6500ncrbscInMsgs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500ncrbscInMsgs.setStatus("mandatory")
_Cdx6500ncrbscOutMsgs_Type = Counter32
_Cdx6500ncrbscOutMsgs_Object = MibTableColumn
cdx6500ncrbscOutMsgs = _Cdx6500ncrbscOutMsgs_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 17, 1, 8),
    _Cdx6500ncrbscOutMsgs_Type()
)
cdx6500ncrbscOutMsgs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500ncrbscOutMsgs.setStatus("mandatory")
_Cdx6500ncrbscInChars_Type = Counter32
_Cdx6500ncrbscInChars_Object = MibTableColumn
cdx6500ncrbscInChars = _Cdx6500ncrbscInChars_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 17, 1, 9),
    _Cdx6500ncrbscInChars_Type()
)
cdx6500ncrbscInChars.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500ncrbscInChars.setStatus("mandatory")
_Cdx6500ncrbscOutChars_Type = Counter32
_Cdx6500ncrbscOutChars_Object = MibTableColumn
cdx6500ncrbscOutChars = _Cdx6500ncrbscOutChars_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 17, 1, 10),
    _Cdx6500ncrbscOutChars_Type()
)
cdx6500ncrbscOutChars.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500ncrbscOutChars.setStatus("mandatory")


class _Cdx6500ncrbscCharRateIn_Type(Integer32):
    """Custom type cdx6500ncrbscCharRateIn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Cdx6500ncrbscCharRateIn_Type.__name__ = "Integer32"
_Cdx6500ncrbscCharRateIn_Object = MibTableColumn
cdx6500ncrbscCharRateIn = _Cdx6500ncrbscCharRateIn_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 17, 1, 11),
    _Cdx6500ncrbscCharRateIn_Type()
)
cdx6500ncrbscCharRateIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500ncrbscCharRateIn.setStatus("mandatory")


class _Cdx6500ncrbscCharRateOut_Type(Integer32):
    """Custom type cdx6500ncrbscCharRateOut based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Cdx6500ncrbscCharRateOut_Type.__name__ = "Integer32"
_Cdx6500ncrbscCharRateOut_Object = MibTableColumn
cdx6500ncrbscCharRateOut = _Cdx6500ncrbscCharRateOut_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 17, 1, 12),
    _Cdx6500ncrbscCharRateOut_Type()
)
cdx6500ncrbscCharRateOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500ncrbscCharRateOut.setStatus("mandatory")
_Cdx6500ncrbscCrcBccErrs_Type = Counter32
_Cdx6500ncrbscCrcBccErrs_Object = MibTableColumn
cdx6500ncrbscCrcBccErrs = _Cdx6500ncrbscCrcBccErrs_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 17, 1, 13),
    _Cdx6500ncrbscCrcBccErrs_Type()
)
cdx6500ncrbscCrcBccErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500ncrbscCrcBccErrs.setStatus("mandatory")
_Cdx6500ncrbscRviRx_Type = Integer32
_Cdx6500ncrbscRviRx_Object = MibTableColumn
cdx6500ncrbscRviRx = _Cdx6500ncrbscRviRx_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 17, 1, 14),
    _Cdx6500ncrbscRviRx_Type()
)
cdx6500ncrbscRviRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500ncrbscRviRx.setStatus("mandatory")
_Cdx6500ncrbscRviTx_Type = Integer32
_Cdx6500ncrbscRviTx_Object = MibTableColumn
cdx6500ncrbscRviTx = _Cdx6500ncrbscRviTx_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 17, 1, 15),
    _Cdx6500ncrbscRviTx_Type()
)
cdx6500ncrbscRviTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500ncrbscRviTx.setStatus("mandatory")
_Cdx6500ncrbscWackRx_Type = Integer32
_Cdx6500ncrbscWackRx_Object = MibTableColumn
cdx6500ncrbscWackRx = _Cdx6500ncrbscWackRx_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 17, 1, 16),
    _Cdx6500ncrbscWackRx_Type()
)
cdx6500ncrbscWackRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500ncrbscWackRx.setStatus("mandatory")
_Cdx6500ncrbscNconvRxMax_Type = Integer32
_Cdx6500ncrbscNconvRxMax_Object = MibTableColumn
cdx6500ncrbscNconvRxMax = _Cdx6500ncrbscNconvRxMax_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 17, 1, 17),
    _Cdx6500ncrbscNconvRxMax_Type()
)
cdx6500ncrbscNconvRxMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500ncrbscNconvRxMax.setStatus("mandatory")
_Cdx6500ncrbscNconvTxMax_Type = Integer32
_Cdx6500ncrbscNconvTxMax_Object = MibTableColumn
cdx6500ncrbscNconvTxMax = _Cdx6500ncrbscNconvTxMax_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 17, 1, 18),
    _Cdx6500ncrbscNconvTxMax_Type()
)
cdx6500ncrbscNconvTxMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500ncrbscNconvTxMax.setStatus("mandatory")
_Cdx6500ncrbscNgroupRxMax_Type = Integer32
_Cdx6500ncrbscNgroupRxMax_Object = MibTableColumn
cdx6500ncrbscNgroupRxMax = _Cdx6500ncrbscNgroupRxMax_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 17, 1, 19),
    _Cdx6500ncrbscNgroupRxMax_Type()
)
cdx6500ncrbscNgroupRxMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500ncrbscNgroupRxMax.setStatus("mandatory")
_Cdx6500ncrbscNgroupTxMax_Type = Integer32
_Cdx6500ncrbscNgroupTxMax_Object = MibTableColumn
cdx6500ncrbscNgroupTxMax = _Cdx6500ncrbscNgroupTxMax_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 17, 1, 20),
    _Cdx6500ncrbscNgroupTxMax_Type()
)
cdx6500ncrbscNgroupTxMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500ncrbscNgroupTxMax.setStatus("mandatory")
_Cdx6500ncrbscLongRespTime_Type = Integer32
_Cdx6500ncrbscLongRespTime_Object = MibTableColumn
cdx6500ncrbscLongRespTime = _Cdx6500ncrbscLongRespTime_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 17, 1, 21),
    _Cdx6500ncrbscLongRespTime_Type()
)
cdx6500ncrbscLongRespTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500ncrbscLongRespTime.setStatus("mandatory")
_Cdx6500ncrbscAverageRespTime_Type = Integer32
_Cdx6500ncrbscAverageRespTime_Object = MibTableColumn
cdx6500ncrbscAverageRespTime = _Cdx6500ncrbscAverageRespTime_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 17, 1, 22),
    _Cdx6500ncrbscAverageRespTime_Type()
)
cdx6500ncrbscAverageRespTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500ncrbscAverageRespTime.setStatus("mandatory")
_Cdx6500ncrbscRviForce_Type = Integer32
_Cdx6500ncrbscRviForce_Object = MibTableColumn
cdx6500ncrbscRviForce = _Cdx6500ncrbscRviForce_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 17, 1, 23),
    _Cdx6500ncrbscRviForce_Type()
)
cdx6500ncrbscRviForce.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500ncrbscRviForce.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "NCRBSC-OPT-MIB",
    **{"DisplayString": DisplayString,
       "codex": codex,
       "cdxProductSpecific": cdxProductSpecific,
       "cdx6500": cdx6500,
       "cdx6500Configuration": cdx6500Configuration,
       "cdx6500CfgProtocolGroup": cdx6500CfgProtocolGroup,
       "cdx6500PCTPortProtocolGroup": cdx6500PCTPortProtocolGroup,
       "cdx6500PPCTNCRBisyncTable": cdx6500PPCTNCRBisyncTable,
       "cdx6500PPCTNCRBisyncEntry": cdx6500PPCTNCRBisyncEntry,
       "cdx6500NCRBSCCfgPortNumber": cdx6500NCRBSCCfgPortNumber,
       "cdx6500NCRBSCCfgPADType": cdx6500NCRBSCCfgPADType,
       "cdx6500NCRBSCCfgClockSource": cdx6500NCRBSCCfgClockSource,
       "cdx6500NCRBSCCfgClockSpeed": cdx6500NCRBSCCfgClockSpeed,
       "cdx6500NCRBSCCfgContention": cdx6500NCRBSCCfgContention,
       "cdx6500NCRBSCCfgNumDevices": cdx6500NCRBSCCfgNumDevices,
       "cdx6500NCRBSCCfgServTimer": cdx6500NCRBSCCfgServTimer,
       "cdx6500NCRBSCCfgErrThreshCount": cdx6500NCRBSCCfgErrThreshCount,
       "cdx6500NCRBSCCfgRetranTimeout": cdx6500NCRBSCCfgRetranTimeout,
       "cdx6500NCRBSCCfgInterBuffTimeout": cdx6500NCRBSCCfgInterBuffTimeout,
       "cdx6500NCRBSCCfgPortSubAddr": cdx6500NCRBSCCfgPortSubAddr,
       "cdx6500NCRBSCCfgPortOptions": cdx6500NCRBSCCfgPortOptions,
       "cdx6500NCRBSCCfgRestrictConnDest": cdx6500NCRBSCCfgRestrictConnDest,
       "cdx6500NCRBSCCfgBillRec": cdx6500NCRBSCCfgBillRec,
       "cdx6500NCRBSCCfgElectricalInterfaceType": cdx6500NCRBSCCfgElectricalInterfaceType,
       "cdx6500NCRBSCCfgV24ElectricalInterfaceOption": cdx6500NCRBSCCfgV24ElectricalInterfaceOption,
       "cdx6500NCRBSCCfgHighSpeedElectricalInterfaceOption": cdx6500NCRBSCCfgHighSpeedElectricalInterfaceOption,
       "cdx6500PCTNCRBSCDeviceGroup": cdx6500PCTNCRBSCDeviceGroup,
       "cdx6500PBCTNCRBSCDeviceTable": cdx6500PBCTNCRBSCDeviceTable,
       "cdx6500PBCTNCRBSCDeviceEntry": cdx6500PBCTNCRBSCDeviceEntry,
       "cdx6500ncrbscDevPortNumber": cdx6500ncrbscDevPortNumber,
       "cdx6500ncrbscDevEntry": cdx6500ncrbscDevEntry,
       "cdx6500ncrbscBSCControlUnitAddr": cdx6500ncrbscBSCControlUnitAddr,
       "cdx6500ncrbscDestControlUnitAddr": cdx6500ncrbscDestControlUnitAddr,
       "cdx6500ncrbscAutocallMnemonic": cdx6500ncrbscAutocallMnemonic,
       "cdx6500ncrbscDeviceEnabled": cdx6500ncrbscDeviceEnabled,
       "cdx6500Statistics": cdx6500Statistics,
       "cdx6500StatProtocolGroup": cdx6500StatProtocolGroup,
       "cdx6500PSTPortProtocolGroup": cdx6500PSTPortProtocolGroup,
       "cdx6500PPSTNCRBisyncTable": cdx6500PPSTNCRBisyncTable,
       "cdx6500ncrbscPortStatEntry": cdx6500ncrbscPortStatEntry,
       "cdx6500ncrbscStatPortNumber": cdx6500ncrbscStatPortNumber,
       "cdx6500ncrbscPortStatus": cdx6500ncrbscPortStatus,
       "cdx6500ncrbscPortState": cdx6500ncrbscPortState,
       "cdx6500ncrbscPortSpeed": cdx6500ncrbscPortSpeed,
       "cdx6500ncrbscPortUtilIn": cdx6500ncrbscPortUtilIn,
       "cdx6500ncrbscPortUtilOut": cdx6500ncrbscPortUtilOut,
       "cdx6500ncrbscInMsgs": cdx6500ncrbscInMsgs,
       "cdx6500ncrbscOutMsgs": cdx6500ncrbscOutMsgs,
       "cdx6500ncrbscInChars": cdx6500ncrbscInChars,
       "cdx6500ncrbscOutChars": cdx6500ncrbscOutChars,
       "cdx6500ncrbscCharRateIn": cdx6500ncrbscCharRateIn,
       "cdx6500ncrbscCharRateOut": cdx6500ncrbscCharRateOut,
       "cdx6500ncrbscCrcBccErrs": cdx6500ncrbscCrcBccErrs,
       "cdx6500ncrbscRviRx": cdx6500ncrbscRviRx,
       "cdx6500ncrbscRviTx": cdx6500ncrbscRviTx,
       "cdx6500ncrbscWackRx": cdx6500ncrbscWackRx,
       "cdx6500ncrbscNconvRxMax": cdx6500ncrbscNconvRxMax,
       "cdx6500ncrbscNconvTxMax": cdx6500ncrbscNconvTxMax,
       "cdx6500ncrbscNgroupRxMax": cdx6500ncrbscNgroupRxMax,
       "cdx6500ncrbscNgroupTxMax": cdx6500ncrbscNgroupTxMax,
       "cdx6500ncrbscLongRespTime": cdx6500ncrbscLongRespTime,
       "cdx6500ncrbscAverageRespTime": cdx6500ncrbscAverageRespTime,
       "cdx6500ncrbscRviForce": cdx6500ncrbscRviForce}
)
