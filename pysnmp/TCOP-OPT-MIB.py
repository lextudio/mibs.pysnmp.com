# SNMP MIB module (TCOP-OPT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/TCOP-OPT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:00:58 2024
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
_Cdx6500PPCTTCOPPortTable_Object = MibTable
cdx6500PPCTTCOPPortTable = _Cdx6500PPCTTCOPPortTable_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 23)
)
if mibBuilder.loadTexts:
    cdx6500PPCTTCOPPortTable.setStatus("mandatory")
_Cdx6500PPCTTCOPPortEntry_Object = MibTableRow
cdx6500PPCTTCOPPortEntry = _Cdx6500PPCTTCOPPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 23, 1)
)
cdx6500PPCTTCOPPortEntry.setIndexNames(
    (0, "TCOP-OPT-MIB", "cdx6500TCOPCfgPortNumber"),
)
if mibBuilder.loadTexts:
    cdx6500PPCTTCOPPortEntry.setStatus("mandatory")


class _Cdx6500TCOPCfgPortNumber_Type(Integer32):
    """Custom type cdx6500TCOPCfgPortNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 54),
    )


_Cdx6500TCOPCfgPortNumber_Type.__name__ = "Integer32"
_Cdx6500TCOPCfgPortNumber_Object = MibTableColumn
cdx6500TCOPCfgPortNumber = _Cdx6500TCOPCfgPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 23, 1, 1),
    _Cdx6500TCOPCfgPortNumber_Type()
)
cdx6500TCOPCfgPortNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500TCOPCfgPortNumber.setStatus("mandatory")


class _Cdx6500TCOPCfgSubtype_Type(Integer32):
    """Custom type cdx6500TCOPCfgSubtype based on Integer32"""
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
        *(("ac100", 5),
          ("gnet", 2),
          ("hsc3", 1),
          ("slc", 4),
          ("uts", 3))
    )


_Cdx6500TCOPCfgSubtype_Type.__name__ = "Integer32"
_Cdx6500TCOPCfgSubtype_Object = MibTableColumn
cdx6500TCOPCfgSubtype = _Cdx6500TCOPCfgSubtype_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 23, 1, 2),
    _Cdx6500TCOPCfgSubtype_Type()
)
cdx6500TCOPCfgSubtype.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500TCOPCfgSubtype.setStatus("mandatory")


class _Cdx6500TCOPCfgClockSource_Type(Integer32):
    """Custom type cdx6500TCOPCfgClockSource based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ext", 2),
          ("int", 1))
    )


_Cdx6500TCOPCfgClockSource_Type.__name__ = "Integer32"
_Cdx6500TCOPCfgClockSource_Object = MibTableColumn
cdx6500TCOPCfgClockSource = _Cdx6500TCOPCfgClockSource_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 23, 1, 3),
    _Cdx6500TCOPCfgClockSource_Type()
)
cdx6500TCOPCfgClockSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500TCOPCfgClockSource.setStatus("mandatory")


class _Cdx6500TCOPCfgClockSpeed_Type(Integer32):
    """Custom type cdx6500TCOPCfgClockSpeed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1200, 80000),
    )


_Cdx6500TCOPCfgClockSpeed_Type.__name__ = "Integer32"
_Cdx6500TCOPCfgClockSpeed_Object = MibTableColumn
cdx6500TCOPCfgClockSpeed = _Cdx6500TCOPCfgClockSpeed_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 23, 1, 4),
    _Cdx6500TCOPCfgClockSpeed_Type()
)
cdx6500TCOPCfgClockSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500TCOPCfgClockSpeed.setStatus("mandatory")


class _Cdx6500TCOPCfgContention_Type(Integer32):
    """Custom type cdx6500TCOPCfgContention based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("fdx", 2),
          ("hdx", 1))
    )


_Cdx6500TCOPCfgContention_Type.__name__ = "Integer32"
_Cdx6500TCOPCfgContention_Object = MibTableColumn
cdx6500TCOPCfgContention = _Cdx6500TCOPCfgContention_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 23, 1, 5),
    _Cdx6500TCOPCfgContention_Type()
)
cdx6500TCOPCfgContention.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500TCOPCfgContention.setStatus("mandatory")


class _Cdx6500TCOPCfgCodeType_Type(Integer32):
    """Custom type cdx6500TCOPCfgCodeType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ascii", 1),
          ("ebcdic", 2))
    )


_Cdx6500TCOPCfgCodeType_Type.__name__ = "Integer32"
_Cdx6500TCOPCfgCodeType_Object = MibTableColumn
cdx6500TCOPCfgCodeType = _Cdx6500TCOPCfgCodeType_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 23, 1, 6),
    _Cdx6500TCOPCfgCodeType_Type()
)
cdx6500TCOPCfgCodeType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500TCOPCfgCodeType.setStatus("mandatory")


class _Cdx6500TCOPCfgReceiveByteCount_Type(Integer32):
    """Custom type cdx6500TCOPCfgReceiveByteCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(8, 127),
    )


_Cdx6500TCOPCfgReceiveByteCount_Type.__name__ = "Integer32"
_Cdx6500TCOPCfgReceiveByteCount_Object = MibTableColumn
cdx6500TCOPCfgReceiveByteCount = _Cdx6500TCOPCfgReceiveByteCount_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 23, 1, 7),
    _Cdx6500TCOPCfgReceiveByteCount_Type()
)
cdx6500TCOPCfgReceiveByteCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500TCOPCfgReceiveByteCount.setStatus("mandatory")


class _Cdx6500TCOPCfgCallControl_Type(Integer32):
    """Custom type cdx6500TCOPCfgCallControl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("auto", 2),
          ("none", 1))
    )


_Cdx6500TCOPCfgCallControl_Type.__name__ = "Integer32"
_Cdx6500TCOPCfgCallControl_Object = MibTableColumn
cdx6500TCOPCfgCallControl = _Cdx6500TCOPCfgCallControl_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 23, 1, 8),
    _Cdx6500TCOPCfgCallControl_Type()
)
cdx6500TCOPCfgCallControl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500TCOPCfgCallControl.setStatus("mandatory")


class _Cdx6500TCOPCfgAutoCallMnem_Type(DisplayString):
    """Custom type cdx6500TCOPCfgAutoCallMnem based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_Cdx6500TCOPCfgAutoCallMnem_Type.__name__ = "DisplayString"
_Cdx6500TCOPCfgAutoCallMnem_Object = MibTableColumn
cdx6500TCOPCfgAutoCallMnem = _Cdx6500TCOPCfgAutoCallMnem_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 23, 1, 9),
    _Cdx6500TCOPCfgAutoCallMnem_Type()
)
cdx6500TCOPCfgAutoCallMnem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500TCOPCfgAutoCallMnem.setStatus("mandatory")


class _Cdx6500TCOPCfgAutoCallTO_Type(Integer32):
    """Custom type cdx6500TCOPCfgAutoCallTO based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 255),
    )


_Cdx6500TCOPCfgAutoCallTO_Type.__name__ = "Integer32"
_Cdx6500TCOPCfgAutoCallTO_Object = MibTableColumn
cdx6500TCOPCfgAutoCallTO = _Cdx6500TCOPCfgAutoCallTO_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 23, 1, 10),
    _Cdx6500TCOPCfgAutoCallTO_Type()
)
cdx6500TCOPCfgAutoCallTO.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500TCOPCfgAutoCallTO.setStatus("mandatory")


class _Cdx6500TCOPCfgMaxAutoCallTries_Type(Integer32):
    """Custom type cdx6500TCOPCfgMaxAutoCallTries based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_Cdx6500TCOPCfgMaxAutoCallTries_Type.__name__ = "Integer32"
_Cdx6500TCOPCfgMaxAutoCallTries_Object = MibTableColumn
cdx6500TCOPCfgMaxAutoCallTries = _Cdx6500TCOPCfgMaxAutoCallTries_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 23, 1, 11),
    _Cdx6500TCOPCfgMaxAutoCallTries_Type()
)
cdx6500TCOPCfgMaxAutoCallTries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500TCOPCfgMaxAutoCallTries.setStatus("mandatory")


class _Cdx6500TCOPCfgPortAddress_Type(DisplayString):
    """Custom type cdx6500TCOPCfgPortAddress based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_Cdx6500TCOPCfgPortAddress_Type.__name__ = "DisplayString"
_Cdx6500TCOPCfgPortAddress_Object = MibTableColumn
cdx6500TCOPCfgPortAddress = _Cdx6500TCOPCfgPortAddress_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 23, 1, 12),
    _Cdx6500TCOPCfgPortAddress_Type()
)
cdx6500TCOPCfgPortAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500TCOPCfgPortAddress.setStatus("mandatory")


class _Cdx6500TCOPCfgProtocolID_Type(DisplayString):
    """Custom type cdx6500TCOPCfgProtocolID based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_Cdx6500TCOPCfgProtocolID_Type.__name__ = "DisplayString"
_Cdx6500TCOPCfgProtocolID_Object = MibTableColumn
cdx6500TCOPCfgProtocolID = _Cdx6500TCOPCfgProtocolID_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 23, 1, 13),
    _Cdx6500TCOPCfgProtocolID_Type()
)
cdx6500TCOPCfgProtocolID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500TCOPCfgProtocolID.setStatus("mandatory")


class _Cdx6500TCOPCfgEnableBill_Type(Integer32):
    """Custom type cdx6500TCOPCfgEnableBill based on Integer32"""
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


_Cdx6500TCOPCfgEnableBill_Type.__name__ = "Integer32"
_Cdx6500TCOPCfgEnableBill_Object = MibTableColumn
cdx6500TCOPCfgEnableBill = _Cdx6500TCOPCfgEnableBill_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 23, 1, 14),
    _Cdx6500TCOPCfgEnableBill_Type()
)
cdx6500TCOPCfgEnableBill.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500TCOPCfgEnableBill.setStatus("mandatory")


class _Cdx6500TCOPCfgRestrictConn_Type(DisplayString):
    """Custom type cdx6500TCOPCfgRestrictConn based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Cdx6500TCOPCfgRestrictConn_Type.__name__ = "DisplayString"
_Cdx6500TCOPCfgRestrictConn_Object = MibTableColumn
cdx6500TCOPCfgRestrictConn = _Cdx6500TCOPCfgRestrictConn_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 23, 1, 15),
    _Cdx6500TCOPCfgRestrictConn_Type()
)
cdx6500TCOPCfgRestrictConn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500TCOPCfgRestrictConn.setStatus("mandatory")


class _Cdx6500TCOPCfgRXQueue_Type(Integer32):
    """Custom type cdx6500TCOPCfgRXQueue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 500),
    )


_Cdx6500TCOPCfgRXQueue_Type.__name__ = "Integer32"
_Cdx6500TCOPCfgRXQueue_Object = MibTableColumn
cdx6500TCOPCfgRXQueue = _Cdx6500TCOPCfgRXQueue_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 23, 1, 16),
    _Cdx6500TCOPCfgRXQueue_Type()
)
cdx6500TCOPCfgRXQueue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500TCOPCfgRXQueue.setStatus("mandatory")


class _Cdx6500TCOPCfgTXQueue_Type(Integer32):
    """Custom type cdx6500TCOPCfgTXQueue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 500),
    )


_Cdx6500TCOPCfgTXQueue_Type.__name__ = "Integer32"
_Cdx6500TCOPCfgTXQueue_Object = MibTableColumn
cdx6500TCOPCfgTXQueue = _Cdx6500TCOPCfgTXQueue_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 23, 1, 17),
    _Cdx6500TCOPCfgTXQueue_Type()
)
cdx6500TCOPCfgTXQueue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500TCOPCfgTXQueue.setStatus("mandatory")


class _Cdx6500TCOPCfgQueueOverflow_Type(Integer32):
    """Custom type cdx6500TCOPCfgQueueOverflow based on Integer32"""
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
        *(("dropMessage", 2),
          ("eotMessage", 4),
          ("flushQueue", 3),
          ("resetConnection", 1))
    )


_Cdx6500TCOPCfgQueueOverflow_Type.__name__ = "Integer32"
_Cdx6500TCOPCfgQueueOverflow_Object = MibTableColumn
cdx6500TCOPCfgQueueOverflow = _Cdx6500TCOPCfgQueueOverflow_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 23, 1, 18),
    _Cdx6500TCOPCfgQueueOverflow_Type()
)
cdx6500TCOPCfgQueueOverflow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500TCOPCfgQueueOverflow.setStatus("mandatory")


class _Cdx6500TCOPCfgPortType_Type(Integer32):
    """Custom type cdx6500TCOPCfgPortType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            27
        )
    )
    namedValues = NamedValues(
        ("tcop", 27)
    )


_Cdx6500TCOPCfgPortType_Type.__name__ = "Integer32"
_Cdx6500TCOPCfgPortType_Object = MibTableColumn
cdx6500TCOPCfgPortType = _Cdx6500TCOPCfgPortType_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 23, 1, 19),
    _Cdx6500TCOPCfgPortType_Type()
)
cdx6500TCOPCfgPortType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500TCOPCfgPortType.setStatus("mandatory")


class _Cdx6500TCOPCfgDataTransmission_Type(Integer32):
    """Custom type cdx6500TCOPCfgDataTransmission based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("fdx", 2),
          ("hdx", 1))
    )


_Cdx6500TCOPCfgDataTransmission_Type.__name__ = "Integer32"
_Cdx6500TCOPCfgDataTransmission_Object = MibTableColumn
cdx6500TCOPCfgDataTransmission = _Cdx6500TCOPCfgDataTransmission_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 23, 1, 20),
    _Cdx6500TCOPCfgDataTransmission_Type()
)
cdx6500TCOPCfgDataTransmission.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500TCOPCfgDataTransmission.setStatus("mandatory")


class _Cdx6500TCOPCfgElectricalInterfaceType_Type(Integer32):
    """Custom type cdx6500TCOPCfgElectricalInterfaceType based on Integer32"""
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


_Cdx6500TCOPCfgElectricalInterfaceType_Type.__name__ = "Integer32"
_Cdx6500TCOPCfgElectricalInterfaceType_Object = MibTableColumn
cdx6500TCOPCfgElectricalInterfaceType = _Cdx6500TCOPCfgElectricalInterfaceType_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 23, 1, 21),
    _Cdx6500TCOPCfgElectricalInterfaceType_Type()
)
cdx6500TCOPCfgElectricalInterfaceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500TCOPCfgElectricalInterfaceType.setStatus("mandatory")


class _Cdx6500TCOPCfgV24ElectricalInterfaceOption_Type(Integer32):
    """Custom type cdx6500TCOPCfgV24ElectricalInterfaceOption based on Integer32"""
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


_Cdx6500TCOPCfgV24ElectricalInterfaceOption_Type.__name__ = "Integer32"
_Cdx6500TCOPCfgV24ElectricalInterfaceOption_Object = MibTableColumn
cdx6500TCOPCfgV24ElectricalInterfaceOption = _Cdx6500TCOPCfgV24ElectricalInterfaceOption_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 23, 1, 22),
    _Cdx6500TCOPCfgV24ElectricalInterfaceOption_Type()
)
cdx6500TCOPCfgV24ElectricalInterfaceOption.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500TCOPCfgV24ElectricalInterfaceOption.setStatus("mandatory")


class _Cdx6500TCOPCfgHighSpeedElectricalInterfaceOption_Type(Integer32):
    """Custom type cdx6500TCOPCfgHighSpeedElectricalInterfaceOption based on Integer32"""
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


_Cdx6500TCOPCfgHighSpeedElectricalInterfaceOption_Type.__name__ = "Integer32"
_Cdx6500TCOPCfgHighSpeedElectricalInterfaceOption_Object = MibTableColumn
cdx6500TCOPCfgHighSpeedElectricalInterfaceOption = _Cdx6500TCOPCfgHighSpeedElectricalInterfaceOption_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 23, 1, 23),
    _Cdx6500TCOPCfgHighSpeedElectricalInterfaceOption_Type()
)
cdx6500TCOPCfgHighSpeedElectricalInterfaceOption.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500TCOPCfgHighSpeedElectricalInterfaceOption.setStatus("mandatory")
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
_Cdx6500PPSTTCOPPortTable_Object = MibTable
cdx6500PPSTTCOPPortTable = _Cdx6500PPSTTCOPPortTable_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 24)
)
if mibBuilder.loadTexts:
    cdx6500PPSTTCOPPortTable.setStatus("mandatory")
_Cdx6500PPSTTCOPPortEntry_Object = MibTableRow
cdx6500PPSTTCOPPortEntry = _Cdx6500PPSTTCOPPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 24, 1)
)
cdx6500PPSTTCOPPortEntry.setIndexNames(
    (0, "TCOP-OPT-MIB", "cdx6500TCOPStatPortNumber"),
)
if mibBuilder.loadTexts:
    cdx6500PPSTTCOPPortEntry.setStatus("mandatory")


class _Cdx6500TCOPStatPortNumber_Type(Integer32):
    """Custom type cdx6500TCOPStatPortNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 54),
    )


_Cdx6500TCOPStatPortNumber_Type.__name__ = "Integer32"
_Cdx6500TCOPStatPortNumber_Object = MibTableColumn
cdx6500TCOPStatPortNumber = _Cdx6500TCOPStatPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 24, 1, 1),
    _Cdx6500TCOPStatPortNumber_Type()
)
cdx6500TCOPStatPortNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500TCOPStatPortNumber.setStatus("mandatory")


class _Cdx6500TCOPStatPortType_Type(Integer32):
    """Custom type cdx6500TCOPStatPortType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            27
        )
    )
    namedValues = NamedValues(
        ("tcop", 27)
    )


_Cdx6500TCOPStatPortType_Type.__name__ = "Integer32"
_Cdx6500TCOPStatPortType_Object = MibTableColumn
cdx6500TCOPStatPortType = _Cdx6500TCOPStatPortType_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 24, 1, 2),
    _Cdx6500TCOPStatPortType_Type()
)
cdx6500TCOPStatPortType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500TCOPStatPortType.setStatus("mandatory")


class _Cdx6500TCOPStatPortSubtype_Type(Integer32):
    """Custom type cdx6500TCOPStatPortSubtype based on Integer32"""
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
        *(("alc", 5),
          ("gnet", 2),
          ("hsc3", 1),
          ("slc", 4),
          ("uts", 3))
    )


_Cdx6500TCOPStatPortSubtype_Type.__name__ = "Integer32"
_Cdx6500TCOPStatPortSubtype_Object = MibTableColumn
cdx6500TCOPStatPortSubtype = _Cdx6500TCOPStatPortSubtype_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 24, 1, 3),
    _Cdx6500TCOPStatPortSubtype_Type()
)
cdx6500TCOPStatPortSubtype.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500TCOPStatPortSubtype.setStatus("mandatory")


class _Cdx6500TCOPStatPortStatus_Type(DisplayString):
    """Custom type cdx6500TCOPStatPortStatus based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 8),
    )


_Cdx6500TCOPStatPortStatus_Type.__name__ = "DisplayString"
_Cdx6500TCOPStatPortStatus_Object = MibTableColumn
cdx6500TCOPStatPortStatus = _Cdx6500TCOPStatPortStatus_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 24, 1, 4),
    _Cdx6500TCOPStatPortStatus_Type()
)
cdx6500TCOPStatPortStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500TCOPStatPortStatus.setStatus("mandatory")


class _Cdx6500TCOPStatPortState_Type(Integer32):
    """Custom type cdx6500TCOPStatPortState based on Integer32"""
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
        *(("calledPhase", 3),
          ("callingPhase", 2),
          ("connected", 4),
          ("discPhase", 1))
    )


_Cdx6500TCOPStatPortState_Type.__name__ = "Integer32"
_Cdx6500TCOPStatPortState_Object = MibTableColumn
cdx6500TCOPStatPortState = _Cdx6500TCOPStatPortState_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 24, 1, 5),
    _Cdx6500TCOPStatPortState_Type()
)
cdx6500TCOPStatPortState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500TCOPStatPortState.setStatus("mandatory")
_Cdx6500TCOPStatPortSpeed_Type = Integer32
_Cdx6500TCOPStatPortSpeed_Object = MibTableColumn
cdx6500TCOPStatPortSpeed = _Cdx6500TCOPStatPortSpeed_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 24, 1, 6),
    _Cdx6500TCOPStatPortSpeed_Type()
)
cdx6500TCOPStatPortSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500TCOPStatPortSpeed.setStatus("mandatory")


class _Cdx6500TCOPStatPortUtilIn_Type(Integer32):
    """Custom type cdx6500TCOPStatPortUtilIn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_Cdx6500TCOPStatPortUtilIn_Type.__name__ = "Integer32"
_Cdx6500TCOPStatPortUtilIn_Object = MibTableColumn
cdx6500TCOPStatPortUtilIn = _Cdx6500TCOPStatPortUtilIn_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 24, 1, 7),
    _Cdx6500TCOPStatPortUtilIn_Type()
)
cdx6500TCOPStatPortUtilIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500TCOPStatPortUtilIn.setStatus("mandatory")


class _Cdx6500TCOPStatPortUtilOut_Type(Integer32):
    """Custom type cdx6500TCOPStatPortUtilOut based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_Cdx6500TCOPStatPortUtilOut_Type.__name__ = "Integer32"
_Cdx6500TCOPStatPortUtilOut_Object = MibTableColumn
cdx6500TCOPStatPortUtilOut = _Cdx6500TCOPStatPortUtilOut_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 24, 1, 8),
    _Cdx6500TCOPStatPortUtilOut_Type()
)
cdx6500TCOPStatPortUtilOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500TCOPStatPortUtilOut.setStatus("mandatory")
_Cdx6500TCOPStatPortOverrunErrs_Type = Counter16
_Cdx6500TCOPStatPortOverrunErrs_Object = MibTableColumn
cdx6500TCOPStatPortOverrunErrs = _Cdx6500TCOPStatPortOverrunErrs_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 24, 1, 9),
    _Cdx6500TCOPStatPortOverrunErrs_Type()
)
cdx6500TCOPStatPortOverrunErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500TCOPStatPortOverrunErrs.setStatus("mandatory")
_Cdx6500TCOPStatPortUnderrunErrs_Type = Counter16
_Cdx6500TCOPStatPortUnderrunErrs_Object = MibTableColumn
cdx6500TCOPStatPortUnderrunErrs = _Cdx6500TCOPStatPortUnderrunErrs_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 24, 1, 10),
    _Cdx6500TCOPStatPortUnderrunErrs_Type()
)
cdx6500TCOPStatPortUnderrunErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500TCOPStatPortUnderrunErrs.setStatus("mandatory")
_Cdx6500TCOPStatPortBCCErrs_Type = Counter16
_Cdx6500TCOPStatPortBCCErrs_Object = MibTableColumn
cdx6500TCOPStatPortBCCErrs = _Cdx6500TCOPStatPortBCCErrs_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 24, 1, 11),
    _Cdx6500TCOPStatPortBCCErrs_Type()
)
cdx6500TCOPStatPortBCCErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500TCOPStatPortBCCErrs.setStatus("mandatory")
_Cdx6500TCOPStatPortParityErrs_Type = Counter16
_Cdx6500TCOPStatPortParityErrs_Object = MibTableColumn
cdx6500TCOPStatPortParityErrs = _Cdx6500TCOPStatPortParityErrs_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 24, 1, 12),
    _Cdx6500TCOPStatPortParityErrs_Type()
)
cdx6500TCOPStatPortParityErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500TCOPStatPortParityErrs.setStatus("mandatory")
_Cdx6500TCOPStatPortInChars_Type = Counter32
_Cdx6500TCOPStatPortInChars_Object = MibTableColumn
cdx6500TCOPStatPortInChars = _Cdx6500TCOPStatPortInChars_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 24, 1, 13),
    _Cdx6500TCOPStatPortInChars_Type()
)
cdx6500TCOPStatPortInChars.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500TCOPStatPortInChars.setStatus("mandatory")
_Cdx6500TCOPStatPortOutChars_Type = Counter32
_Cdx6500TCOPStatPortOutChars_Object = MibTableColumn
cdx6500TCOPStatPortOutChars = _Cdx6500TCOPStatPortOutChars_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 24, 1, 14),
    _Cdx6500TCOPStatPortOutChars_Type()
)
cdx6500TCOPStatPortOutChars.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500TCOPStatPortOutChars.setStatus("mandatory")
_Cdx6500TCOPStatPortInCharsRate_Type = Integer32
_Cdx6500TCOPStatPortInCharsRate_Object = MibTableColumn
cdx6500TCOPStatPortInCharsRate = _Cdx6500TCOPStatPortInCharsRate_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 24, 1, 15),
    _Cdx6500TCOPStatPortInCharsRate_Type()
)
cdx6500TCOPStatPortInCharsRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500TCOPStatPortInCharsRate.setStatus("mandatory")
_Cdx6500TCOPStatPortOutCharsRate_Type = Integer32
_Cdx6500TCOPStatPortOutCharsRate_Object = MibTableColumn
cdx6500TCOPStatPortOutCharsRate = _Cdx6500TCOPStatPortOutCharsRate_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 24, 1, 16),
    _Cdx6500TCOPStatPortOutCharsRate_Type()
)
cdx6500TCOPStatPortOutCharsRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500TCOPStatPortOutCharsRate.setStatus("mandatory")
_Cdx6500TCOPStatPortInMessages_Type = Counter32
_Cdx6500TCOPStatPortInMessages_Object = MibTableColumn
cdx6500TCOPStatPortInMessages = _Cdx6500TCOPStatPortInMessages_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 24, 1, 17),
    _Cdx6500TCOPStatPortInMessages_Type()
)
cdx6500TCOPStatPortInMessages.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500TCOPStatPortInMessages.setStatus("mandatory")
_Cdx6500TCOPStatPortOutMessages_Type = Counter32
_Cdx6500TCOPStatPortOutMessages_Object = MibTableColumn
cdx6500TCOPStatPortOutMessages = _Cdx6500TCOPStatPortOutMessages_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 24, 1, 18),
    _Cdx6500TCOPStatPortOutMessages_Type()
)
cdx6500TCOPStatPortOutMessages.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500TCOPStatPortOutMessages.setStatus("mandatory")
_Cdx6500TCOPStatPortInMessagesRate_Type = Integer32
_Cdx6500TCOPStatPortInMessagesRate_Object = MibTableColumn
cdx6500TCOPStatPortInMessagesRate = _Cdx6500TCOPStatPortInMessagesRate_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 24, 1, 19),
    _Cdx6500TCOPStatPortInMessagesRate_Type()
)
cdx6500TCOPStatPortInMessagesRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500TCOPStatPortInMessagesRate.setStatus("mandatory")
_Cdx6500TCOPStatPortOutMessagesRate_Type = Integer32
_Cdx6500TCOPStatPortOutMessagesRate_Object = MibTableColumn
cdx6500TCOPStatPortOutMessagesRate = _Cdx6500TCOPStatPortOutMessagesRate_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 24, 1, 20),
    _Cdx6500TCOPStatPortOutMessagesRate_Type()
)
cdx6500TCOPStatPortOutMessagesRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500TCOPStatPortOutMessagesRate.setStatus("mandatory")
_Cdx6500TCOPStatPortInPktsQueued_Type = Integer32
_Cdx6500TCOPStatPortInPktsQueued_Object = MibTableColumn
cdx6500TCOPStatPortInPktsQueued = _Cdx6500TCOPStatPortInPktsQueued_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 24, 1, 21),
    _Cdx6500TCOPStatPortInPktsQueued_Type()
)
cdx6500TCOPStatPortInPktsQueued.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500TCOPStatPortInPktsQueued.setStatus("mandatory")
_Cdx6500TCOPStatPortOutPktsQueued_Type = Integer32
_Cdx6500TCOPStatPortOutPktsQueued_Object = MibTableColumn
cdx6500TCOPStatPortOutPktsQueued = _Cdx6500TCOPStatPortOutPktsQueued_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 24, 1, 22),
    _Cdx6500TCOPStatPortOutPktsQueued_Type()
)
cdx6500TCOPStatPortOutPktsQueued.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500TCOPStatPortOutPktsQueued.setStatus("mandatory")
_Cdx6500TCOPStatPortMaxInQueueLength_Type = Gauge32
_Cdx6500TCOPStatPortMaxInQueueLength_Object = MibTableColumn
cdx6500TCOPStatPortMaxInQueueLength = _Cdx6500TCOPStatPortMaxInQueueLength_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 24, 1, 23),
    _Cdx6500TCOPStatPortMaxInQueueLength_Type()
)
cdx6500TCOPStatPortMaxInQueueLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500TCOPStatPortMaxInQueueLength.setStatus("mandatory")
_Cdx6500TCOPStatPortMaxOutQueueLength_Type = Gauge32
_Cdx6500TCOPStatPortMaxOutQueueLength_Object = MibTableColumn
cdx6500TCOPStatPortMaxOutQueueLength = _Cdx6500TCOPStatPortMaxOutQueueLength_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 24, 1, 24),
    _Cdx6500TCOPStatPortMaxOutQueueLength_Type()
)
cdx6500TCOPStatPortMaxOutQueueLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500TCOPStatPortMaxOutQueueLength.setStatus("mandatory")
_Cdx6500TCOPStatPortPktQueueFlushCount_Type = Integer32
_Cdx6500TCOPStatPortPktQueueFlushCount_Object = MibTableColumn
cdx6500TCOPStatPortPktQueueFlushCount = _Cdx6500TCOPStatPortPktQueueFlushCount_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 24, 1, 25),
    _Cdx6500TCOPStatPortPktQueueFlushCount_Type()
)
cdx6500TCOPStatPortPktQueueFlushCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500TCOPStatPortPktQueueFlushCount.setStatus("mandatory")
_Cdx6500TCOPStatAutoCallStatus_Type = DisplayString
_Cdx6500TCOPStatAutoCallStatus_Object = MibTableColumn
cdx6500TCOPStatAutoCallStatus = _Cdx6500TCOPStatAutoCallStatus_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 24, 1, 26),
    _Cdx6500TCOPStatAutoCallStatus_Type()
)
cdx6500TCOPStatAutoCallStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500TCOPStatAutoCallStatus.setStatus("mandatory")
_Cdx6500TCOPStatAutoCallNextAttempt_Type = Integer32
_Cdx6500TCOPStatAutoCallNextAttempt_Object = MibTableColumn
cdx6500TCOPStatAutoCallNextAttempt = _Cdx6500TCOPStatAutoCallNextAttempt_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 24, 1, 27),
    _Cdx6500TCOPStatAutoCallNextAttempt_Type()
)
cdx6500TCOPStatAutoCallNextAttempt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500TCOPStatAutoCallNextAttempt.setStatus("mandatory")
_Cdx6500TCOPStatAutoCallAttemptCount_Type = Counter32
_Cdx6500TCOPStatAutoCallAttemptCount_Object = MibTableColumn
cdx6500TCOPStatAutoCallAttemptCount = _Cdx6500TCOPStatAutoCallAttemptCount_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 24, 1, 28),
    _Cdx6500TCOPStatAutoCallAttemptCount_Type()
)
cdx6500TCOPStatAutoCallAttemptCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500TCOPStatAutoCallAttemptCount.setStatus("mandatory")


class _Cdx6500TCOPStatAutoCallLastClearCause_Type(Integer32):
    """Custom type cdx6500TCOPStatAutoCallLastClearCause based on Integer32"""
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
              12,
              13,
              14,
              15)
        )
    )
    namedValues = NamedValues(
        *(("ctp", 14),
          ("der", 9),
          ("dte", 1),
          ("err", 7),
          ("fsn", 13),
          ("icd", 12),
          ("inv", 5),
          ("na", 6),
          ("nc", 4),
          ("np", 2),
          ("occ", 3),
          ("rna", 10),
          ("roo", 11),
          ("rpe", 8),
          ("sha", 15))
    )


_Cdx6500TCOPStatAutoCallLastClearCause_Type.__name__ = "Integer32"
_Cdx6500TCOPStatAutoCallLastClearCause_Object = MibTableColumn
cdx6500TCOPStatAutoCallLastClearCause = _Cdx6500TCOPStatAutoCallLastClearCause_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 24, 1, 29),
    _Cdx6500TCOPStatAutoCallLastClearCause_Type()
)
cdx6500TCOPStatAutoCallLastClearCause.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500TCOPStatAutoCallLastClearCause.setStatus("mandatory")


class _Cdx6500TCOPStatAutoCallLastClearDiagnosis_Type(Integer32):
    """Custom type cdx6500TCOPStatAutoCallLastClearDiagnosis based on Integer32"""
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
              12,
              13,
              14,
              15,
              16,
              17,
              18,
              19,
              20,
              21,
              22,
              23,
              24,
              25,
              26,
              27,
              28,
              29,
              30,
              31,
              32,
              33,
              34,
              35,
              36,
              37,
              38,
              39,
              40,
              41,
              42,
              43,
              44,
              45,
              46)
        )
    )
    namedValues = NamedValues(
        *(("aderr", 43),
          ("bpr", 3),
          ("bps", 2),
          ("cald", 13),
          ("cali", 14),
          ("cco", 18),
          ("ccpo", 27),
          ("cldn", 25),
          ("clin", 24),
          ("cshe", 29),
          ("csld", 28),
          ("disc", 32),
          ("dm", 33),
          ("dpbo", 45),
          ("dupl", 19),
          ("finl", 30),
          ("frlen", 42),
          ("frmr", 35),
          ("gtcap", 40),
          ("icb", 16),
          ("invfl", 15),
          ("invnr", 36),
          ("nadl", 20),
          ("ncil", 26),
          ("nfce", 22),
          ("nfcl", 21),
          ("nocs", 10),
          ("nofc", 11),
          ("nofp", 12),
          ("nolcn", 17),
          ("none", 1),
          ("pln", 7),
          ("pna", 5),
          ("psh", 6),
          ("ptinv", 4),
          ("rin3", 31),
          ("sabm", 34),
          ("spbo", 44),
          ("srr", 46),
          ("t1to", 41),
          ("tcli", 9),
          ("tout", 8),
          ("trp", 23),
          ("ucmd", 38),
          ("unsf", 37),
          ("uresp", 39))
    )


_Cdx6500TCOPStatAutoCallLastClearDiagnosis_Type.__name__ = "Integer32"
_Cdx6500TCOPStatAutoCallLastClearDiagnosis_Object = MibTableColumn
cdx6500TCOPStatAutoCallLastClearDiagnosis = _Cdx6500TCOPStatAutoCallLastClearDiagnosis_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 24, 1, 30),
    _Cdx6500TCOPStatAutoCallLastClearDiagnosis_Type()
)
cdx6500TCOPStatAutoCallLastClearDiagnosis.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500TCOPStatAutoCallLastClearDiagnosis.setStatus("mandatory")


class _Cdx6500TCOPStatAutoCallLastInCalledAddress_Type(DisplayString):
    """Custom type cdx6500TCOPStatAutoCallLastInCalledAddress based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_Cdx6500TCOPStatAutoCallLastInCalledAddress_Type.__name__ = "DisplayString"
_Cdx6500TCOPStatAutoCallLastInCalledAddress_Object = MibTableColumn
cdx6500TCOPStatAutoCallLastInCalledAddress = _Cdx6500TCOPStatAutoCallLastInCalledAddress_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 24, 1, 31),
    _Cdx6500TCOPStatAutoCallLastInCalledAddress_Type()
)
cdx6500TCOPStatAutoCallLastInCalledAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500TCOPStatAutoCallLastInCalledAddress.setStatus("mandatory")


class _Cdx6500TCOPStatAutoCallLastInCallingAddress_Type(DisplayString):
    """Custom type cdx6500TCOPStatAutoCallLastInCallingAddress based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_Cdx6500TCOPStatAutoCallLastInCallingAddress_Type.__name__ = "DisplayString"
_Cdx6500TCOPStatAutoCallLastInCallingAddress_Object = MibTableColumn
cdx6500TCOPStatAutoCallLastInCallingAddress = _Cdx6500TCOPStatAutoCallLastInCallingAddress_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 24, 1, 32),
    _Cdx6500TCOPStatAutoCallLastInCallingAddress_Type()
)
cdx6500TCOPStatAutoCallLastInCallingAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500TCOPStatAutoCallLastInCallingAddress.setStatus("mandatory")
_Cdx6500TCOPStatAutoCallLastInCallFacilities_Type = DisplayString
_Cdx6500TCOPStatAutoCallLastInCallFacilities_Object = MibTableColumn
cdx6500TCOPStatAutoCallLastInCallFacilities = _Cdx6500TCOPStatAutoCallLastInCallFacilities_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 24, 1, 33),
    _Cdx6500TCOPStatAutoCallLastInCallFacilities_Type()
)
cdx6500TCOPStatAutoCallLastInCallFacilities.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500TCOPStatAutoCallLastInCallFacilities.setStatus("mandatory")
_Cdx6500TCOPStatAutoCallLastInCallCUD_Type = DisplayString
_Cdx6500TCOPStatAutoCallLastInCallCUD_Object = MibTableColumn
cdx6500TCOPStatAutoCallLastInCallCUD = _Cdx6500TCOPStatAutoCallLastInCallCUD_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 24, 1, 34),
    _Cdx6500TCOPStatAutoCallLastInCallCUD_Type()
)
cdx6500TCOPStatAutoCallLastInCallCUD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500TCOPStatAutoCallLastInCallCUD.setStatus("mandatory")
_Cdx6500TCOPStatAutoCallLastOutCalledAddress_Type = DisplayString
_Cdx6500TCOPStatAutoCallLastOutCalledAddress_Object = MibTableColumn
cdx6500TCOPStatAutoCallLastOutCalledAddress = _Cdx6500TCOPStatAutoCallLastOutCalledAddress_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 24, 1, 35),
    _Cdx6500TCOPStatAutoCallLastOutCalledAddress_Type()
)
cdx6500TCOPStatAutoCallLastOutCalledAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500TCOPStatAutoCallLastOutCalledAddress.setStatus("mandatory")
_Cdx6500TCOPStatAutoCallLastOutCallingAddress_Type = DisplayString
_Cdx6500TCOPStatAutoCallLastOutCallingAddress_Object = MibTableColumn
cdx6500TCOPStatAutoCallLastOutCallingAddress = _Cdx6500TCOPStatAutoCallLastOutCallingAddress_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 24, 1, 36),
    _Cdx6500TCOPStatAutoCallLastOutCallingAddress_Type()
)
cdx6500TCOPStatAutoCallLastOutCallingAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500TCOPStatAutoCallLastOutCallingAddress.setStatus("mandatory")
_Cdx6500TCOPStatAutoCallLastOutCallFacilities_Type = DisplayString
_Cdx6500TCOPStatAutoCallLastOutCallFacilities_Object = MibTableColumn
cdx6500TCOPStatAutoCallLastOutCallFacilities = _Cdx6500TCOPStatAutoCallLastOutCallFacilities_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 24, 1, 37),
    _Cdx6500TCOPStatAutoCallLastOutCallFacilities_Type()
)
cdx6500TCOPStatAutoCallLastOutCallFacilities.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500TCOPStatAutoCallLastOutCallFacilities.setStatus("mandatory")
_Cdx6500TCOPStatAutoCallLastOutCallCUD_Type = DisplayString
_Cdx6500TCOPStatAutoCallLastOutCallCUD_Object = MibTableColumn
cdx6500TCOPStatAutoCallLastOutCallCUD = _Cdx6500TCOPStatAutoCallLastOutCallCUD_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 24, 1, 38),
    _Cdx6500TCOPStatAutoCallLastOutCallCUD_Type()
)
cdx6500TCOPStatAutoCallLastOutCallCUD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500TCOPStatAutoCallLastOutCallCUD.setStatus("mandatory")
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
    "TCOP-OPT-MIB",
    **{"Counter16": Counter16,
       "DisplayString": DisplayString,
       "codex": codex,
       "cdxProductSpecific": cdxProductSpecific,
       "cdx6500": cdx6500,
       "cdx6500Configuration": cdx6500Configuration,
       "cdx6500CfgProtocolGroup": cdx6500CfgProtocolGroup,
       "cdx6500PCTPortProtocolGroup": cdx6500PCTPortProtocolGroup,
       "cdx6500PPCTTCOPPortTable": cdx6500PPCTTCOPPortTable,
       "cdx6500PPCTTCOPPortEntry": cdx6500PPCTTCOPPortEntry,
       "cdx6500TCOPCfgPortNumber": cdx6500TCOPCfgPortNumber,
       "cdx6500TCOPCfgSubtype": cdx6500TCOPCfgSubtype,
       "cdx6500TCOPCfgClockSource": cdx6500TCOPCfgClockSource,
       "cdx6500TCOPCfgClockSpeed": cdx6500TCOPCfgClockSpeed,
       "cdx6500TCOPCfgContention": cdx6500TCOPCfgContention,
       "cdx6500TCOPCfgCodeType": cdx6500TCOPCfgCodeType,
       "cdx6500TCOPCfgReceiveByteCount": cdx6500TCOPCfgReceiveByteCount,
       "cdx6500TCOPCfgCallControl": cdx6500TCOPCfgCallControl,
       "cdx6500TCOPCfgAutoCallMnem": cdx6500TCOPCfgAutoCallMnem,
       "cdx6500TCOPCfgAutoCallTO": cdx6500TCOPCfgAutoCallTO,
       "cdx6500TCOPCfgMaxAutoCallTries": cdx6500TCOPCfgMaxAutoCallTries,
       "cdx6500TCOPCfgPortAddress": cdx6500TCOPCfgPortAddress,
       "cdx6500TCOPCfgProtocolID": cdx6500TCOPCfgProtocolID,
       "cdx6500TCOPCfgEnableBill": cdx6500TCOPCfgEnableBill,
       "cdx6500TCOPCfgRestrictConn": cdx6500TCOPCfgRestrictConn,
       "cdx6500TCOPCfgRXQueue": cdx6500TCOPCfgRXQueue,
       "cdx6500TCOPCfgTXQueue": cdx6500TCOPCfgTXQueue,
       "cdx6500TCOPCfgQueueOverflow": cdx6500TCOPCfgQueueOverflow,
       "cdx6500TCOPCfgPortType": cdx6500TCOPCfgPortType,
       "cdx6500TCOPCfgDataTransmission": cdx6500TCOPCfgDataTransmission,
       "cdx6500TCOPCfgElectricalInterfaceType": cdx6500TCOPCfgElectricalInterfaceType,
       "cdx6500TCOPCfgV24ElectricalInterfaceOption": cdx6500TCOPCfgV24ElectricalInterfaceOption,
       "cdx6500TCOPCfgHighSpeedElectricalInterfaceOption": cdx6500TCOPCfgHighSpeedElectricalInterfaceOption,
       "cdx6500Statistics": cdx6500Statistics,
       "cdx6500StatProtocolGroup": cdx6500StatProtocolGroup,
       "cdx6500PSTPortProtocolGroup": cdx6500PSTPortProtocolGroup,
       "cdx6500PPSTTCOPPortTable": cdx6500PPSTTCOPPortTable,
       "cdx6500PPSTTCOPPortEntry": cdx6500PPSTTCOPPortEntry,
       "cdx6500TCOPStatPortNumber": cdx6500TCOPStatPortNumber,
       "cdx6500TCOPStatPortType": cdx6500TCOPStatPortType,
       "cdx6500TCOPStatPortSubtype": cdx6500TCOPStatPortSubtype,
       "cdx6500TCOPStatPortStatus": cdx6500TCOPStatPortStatus,
       "cdx6500TCOPStatPortState": cdx6500TCOPStatPortState,
       "cdx6500TCOPStatPortSpeed": cdx6500TCOPStatPortSpeed,
       "cdx6500TCOPStatPortUtilIn": cdx6500TCOPStatPortUtilIn,
       "cdx6500TCOPStatPortUtilOut": cdx6500TCOPStatPortUtilOut,
       "cdx6500TCOPStatPortOverrunErrs": cdx6500TCOPStatPortOverrunErrs,
       "cdx6500TCOPStatPortUnderrunErrs": cdx6500TCOPStatPortUnderrunErrs,
       "cdx6500TCOPStatPortBCCErrs": cdx6500TCOPStatPortBCCErrs,
       "cdx6500TCOPStatPortParityErrs": cdx6500TCOPStatPortParityErrs,
       "cdx6500TCOPStatPortInChars": cdx6500TCOPStatPortInChars,
       "cdx6500TCOPStatPortOutChars": cdx6500TCOPStatPortOutChars,
       "cdx6500TCOPStatPortInCharsRate": cdx6500TCOPStatPortInCharsRate,
       "cdx6500TCOPStatPortOutCharsRate": cdx6500TCOPStatPortOutCharsRate,
       "cdx6500TCOPStatPortInMessages": cdx6500TCOPStatPortInMessages,
       "cdx6500TCOPStatPortOutMessages": cdx6500TCOPStatPortOutMessages,
       "cdx6500TCOPStatPortInMessagesRate": cdx6500TCOPStatPortInMessagesRate,
       "cdx6500TCOPStatPortOutMessagesRate": cdx6500TCOPStatPortOutMessagesRate,
       "cdx6500TCOPStatPortInPktsQueued": cdx6500TCOPStatPortInPktsQueued,
       "cdx6500TCOPStatPortOutPktsQueued": cdx6500TCOPStatPortOutPktsQueued,
       "cdx6500TCOPStatPortMaxInQueueLength": cdx6500TCOPStatPortMaxInQueueLength,
       "cdx6500TCOPStatPortMaxOutQueueLength": cdx6500TCOPStatPortMaxOutQueueLength,
       "cdx6500TCOPStatPortPktQueueFlushCount": cdx6500TCOPStatPortPktQueueFlushCount,
       "cdx6500TCOPStatAutoCallStatus": cdx6500TCOPStatAutoCallStatus,
       "cdx6500TCOPStatAutoCallNextAttempt": cdx6500TCOPStatAutoCallNextAttempt,
       "cdx6500TCOPStatAutoCallAttemptCount": cdx6500TCOPStatAutoCallAttemptCount,
       "cdx6500TCOPStatAutoCallLastClearCause": cdx6500TCOPStatAutoCallLastClearCause,
       "cdx6500TCOPStatAutoCallLastClearDiagnosis": cdx6500TCOPStatAutoCallLastClearDiagnosis,
       "cdx6500TCOPStatAutoCallLastInCalledAddress": cdx6500TCOPStatAutoCallLastInCalledAddress,
       "cdx6500TCOPStatAutoCallLastInCallingAddress": cdx6500TCOPStatAutoCallLastInCallingAddress,
       "cdx6500TCOPStatAutoCallLastInCallFacilities": cdx6500TCOPStatAutoCallLastInCallFacilities,
       "cdx6500TCOPStatAutoCallLastInCallCUD": cdx6500TCOPStatAutoCallLastInCallCUD,
       "cdx6500TCOPStatAutoCallLastOutCalledAddress": cdx6500TCOPStatAutoCallLastOutCalledAddress,
       "cdx6500TCOPStatAutoCallLastOutCallingAddress": cdx6500TCOPStatAutoCallLastOutCallingAddress,
       "cdx6500TCOPStatAutoCallLastOutCallFacilities": cdx6500TCOPStatAutoCallLastOutCallFacilities,
       "cdx6500TCOPStatAutoCallLastOutCallCUD": cdx6500TCOPStatAutoCallLastOutCallCUD,
       "cdx6500Controls": cdx6500Controls}
)
