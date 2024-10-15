# SNMP MIB module (CTRON-DLSW-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CTRON-DLSW-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:18:44 2024
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

(MacAddress,) = mibBuilder.importSymbols(
    "BRIDGE-MIB",
    "MacAddress")

(ctDLSW,) = mibBuilder.importSymbols(
    "CTRON-MIB-NAMES",
    "ctDLSW")

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


# MODULE-IDENTITY


# Types definitions



class NBName(DisplayString):
    """Custom type NBName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )




# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CtdlswNode_ObjectIdentity = ObjectIdentity
ctdlswNode = _CtdlswNode_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 8, 1)
)
_CtdlswNodeConfig_ObjectIdentity = ObjectIdentity
ctdlswNodeConfig = _CtdlswNodeConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 8, 1, 1)
)
_CtdlswVersion_Type = DisplayString
_CtdlswVersion_Object = MibScalar
ctdlswVersion = _CtdlswVersion_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 8, 1, 1, 1),
    _CtdlswVersion_Type()
)
ctdlswVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctdlswVersion.setStatus("mandatory")


class _CtdlswAdminStatus_Type(Integer32):
    """Custom type ctdlswAdminStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 3),
          ("other", 1))
    )


_CtdlswAdminStatus_Type.__name__ = "Integer32"
_CtdlswAdminStatus_Object = MibScalar
ctdlswAdminStatus = _CtdlswAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 8, 1, 1, 2),
    _CtdlswAdminStatus_Type()
)
ctdlswAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctdlswAdminStatus.setStatus("mandatory")


class _CtdlswOperStatus_Type(Integer32):
    """Custom type ctdlswOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 3),
          ("other", 1))
    )


_CtdlswOperStatus_Type.__name__ = "Integer32"
_CtdlswOperStatus_Object = MibScalar
ctdlswOperStatus = _CtdlswOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 8, 1, 1, 3),
    _CtdlswOperStatus_Type()
)
ctdlswOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctdlswOperStatus.setStatus("mandatory")
_CtdlswUpTime_Type = TimeTicks
_CtdlswUpTime_Object = MibScalar
ctdlswUpTime = _CtdlswUpTime_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 8, 1, 1, 4),
    _CtdlswUpTime_Type()
)
ctdlswUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctdlswUpTime.setStatus("mandatory")


class _CtdlswOperVirtualRingNumber_Type(Integer32):
    """Custom type ctdlswOperVirtualRingNumber based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_CtdlswOperVirtualRingNumber_Type.__name__ = "Integer32"
_CtdlswOperVirtualRingNumber_Object = MibScalar
ctdlswOperVirtualRingNumber = _CtdlswOperVirtualRingNumber_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 8, 1, 1, 5),
    _CtdlswOperVirtualRingNumber_Type()
)
ctdlswOperVirtualRingNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctdlswOperVirtualRingNumber.setStatus("mandatory")


class _CtdlswNBLocalFilterType_Type(Integer32):
    """Custom type ctdlswNBLocalFilterType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("block", 1),
          ("pass", 2))
    )


_CtdlswNBLocalFilterType_Type.__name__ = "Integer32"
_CtdlswNBLocalFilterType_Object = MibScalar
ctdlswNBLocalFilterType = _CtdlswNBLocalFilterType_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 8, 1, 1, 6),
    _CtdlswNBLocalFilterType_Type()
)
ctdlswNBLocalFilterType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctdlswNBLocalFilterType.setStatus("mandatory")


class _CtdlswNBRemoteFilterType_Type(Integer32):
    """Custom type ctdlswNBRemoteFilterType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("block", 1),
          ("pass", 2))
    )


_CtdlswNBRemoteFilterType_Type.__name__ = "Integer32"
_CtdlswNBRemoteFilterType_Object = MibScalar
ctdlswNBRemoteFilterType = _CtdlswNBRemoteFilterType_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 8, 1, 1, 7),
    _CtdlswNBRemoteFilterType_Type()
)
ctdlswNBRemoteFilterType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctdlswNBRemoteFilterType.setStatus("mandatory")


class _CtdlswMacLocalFilterType_Type(Integer32):
    """Custom type ctdlswMacLocalFilterType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("block", 1),
          ("pass", 2))
    )


_CtdlswMacLocalFilterType_Type.__name__ = "Integer32"
_CtdlswMacLocalFilterType_Object = MibScalar
ctdlswMacLocalFilterType = _CtdlswMacLocalFilterType_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 8, 1, 1, 8),
    _CtdlswMacLocalFilterType_Type()
)
ctdlswMacLocalFilterType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctdlswMacLocalFilterType.setStatus("mandatory")


class _CtdlswMacRemoteFilterType_Type(Integer32):
    """Custom type ctdlswMacRemoteFilterType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("block", 1),
          ("pass", 2))
    )


_CtdlswMacRemoteFilterType_Type.__name__ = "Integer32"
_CtdlswMacRemoteFilterType_Object = MibScalar
ctdlswMacRemoteFilterType = _CtdlswMacRemoteFilterType_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 8, 1, 1, 9),
    _CtdlswMacRemoteFilterType_Type()
)
ctdlswMacRemoteFilterType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctdlswMacRemoteFilterType.setStatus("mandatory")


class _CtdlswAcceptDynamicTConn_Type(Integer32):
    """Custom type ctdlswAcceptDynamicTConn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_CtdlswAcceptDynamicTConn_Type.__name__ = "Integer32"
_CtdlswAcceptDynamicTConn_Object = MibScalar
ctdlswAcceptDynamicTConn = _CtdlswAcceptDynamicTConn_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 8, 1, 1, 10),
    _CtdlswAcceptDynamicTConn_Type()
)
ctdlswAcceptDynamicTConn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctdlswAcceptDynamicTConn.setStatus("mandatory")
_CtdlswDefaultPortNumber_Type = Integer32
_CtdlswDefaultPortNumber_Object = MibScalar
ctdlswDefaultPortNumber = _CtdlswDefaultPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 8, 1, 1, 11),
    _CtdlswDefaultPortNumber_Type()
)
ctdlswDefaultPortNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctdlswDefaultPortNumber.setStatus("mandatory")
_CtdlswPort_ObjectIdentity = ObjectIdentity
ctdlswPort = _CtdlswPort_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 8, 2)
)
_CtdlswPortTable_Object = MibTable
ctdlswPortTable = _CtdlswPortTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 8, 2, 1)
)
if mibBuilder.loadTexts:
    ctdlswPortTable.setStatus("mandatory")
_CtdlswPortEntry_Object = MibTableRow
ctdlswPortEntry = _CtdlswPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 8, 2, 1, 1)
)
ctdlswPortEntry.setIndexNames(
    (0, "CTRON-DLSW-MIB", "ctdlswPortName"),
)
if mibBuilder.loadTexts:
    ctdlswPortEntry.setStatus("mandatory")
_CtdlswPortIndex_Type = Integer32
_CtdlswPortIndex_Object = MibTableColumn
ctdlswPortIndex = _CtdlswPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 8, 2, 1, 1, 1),
    _CtdlswPortIndex_Type()
)
ctdlswPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctdlswPortIndex.setStatus("mandatory")


class _CtdlswPortName_Type(DisplayString):
    """Custom type ctdlswPortName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 8),
    )


_CtdlswPortName_Type.__name__ = "DisplayString"
_CtdlswPortName_Object = MibTableColumn
ctdlswPortName = _CtdlswPortName_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 8, 2, 1, 1, 2),
    _CtdlswPortName_Type()
)
ctdlswPortName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctdlswPortName.setStatus("mandatory")
_CtdlswPortAddress_Type = MacAddress
_CtdlswPortAddress_Object = MibTableColumn
ctdlswPortAddress = _CtdlswPortAddress_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 8, 2, 1, 1, 3),
    _CtdlswPortAddress_Type()
)
ctdlswPortAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctdlswPortAddress.setStatus("mandatory")


class _CtdlswPortAdminStatus_Type(Integer32):
    """Custom type ctdlswPortAdminStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 3),
          ("other", 1))
    )


_CtdlswPortAdminStatus_Type.__name__ = "Integer32"
_CtdlswPortAdminStatus_Object = MibTableColumn
ctdlswPortAdminStatus = _CtdlswPortAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 8, 2, 1, 1, 4),
    _CtdlswPortAdminStatus_Type()
)
ctdlswPortAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctdlswPortAdminStatus.setStatus("mandatory")


class _CtdlswPortOperStatus_Type(Integer32):
    """Custom type ctdlswPortOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 3),
          ("other", 1))
    )


_CtdlswPortOperStatus_Type.__name__ = "Integer32"
_CtdlswPortOperStatus_Object = MibTableColumn
ctdlswPortOperStatus = _CtdlswPortOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 8, 2, 1, 1, 5),
    _CtdlswPortOperStatus_Type()
)
ctdlswPortOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctdlswPortOperStatus.setStatus("mandatory")
_CtdlswPortUpTime_Type = TimeTicks
_CtdlswPortUpTime_Object = MibTableColumn
ctdlswPortUpTime = _CtdlswPortUpTime_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 8, 2, 1, 1, 6),
    _CtdlswPortUpTime_Type()
)
ctdlswPortUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctdlswPortUpTime.setStatus("mandatory")
_CtdlswFilter_ObjectIdentity = ObjectIdentity
ctdlswFilter = _CtdlswFilter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 8, 3)
)
_CtdlswLocalNBFilterTable_Object = MibTable
ctdlswLocalNBFilterTable = _CtdlswLocalNBFilterTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 8, 3, 1)
)
if mibBuilder.loadTexts:
    ctdlswLocalNBFilterTable.setStatus("mandatory")
_CtdlswLocalNBFilterEntry_Object = MibTableRow
ctdlswLocalNBFilterEntry = _CtdlswLocalNBFilterEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 8, 3, 1, 1)
)
ctdlswLocalNBFilterEntry.setIndexNames(
    (0, "CTRON-DLSW-MIB", "ctdlswLocalNBFilterSrcName"),
    (0, "CTRON-DLSW-MIB", "ctdlswLocalNBFilterDestName"),
)
if mibBuilder.loadTexts:
    ctdlswLocalNBFilterEntry.setStatus("mandatory")
_CtdlswLocalNBFilterSrcName_Type = NBName
_CtdlswLocalNBFilterSrcName_Object = MibTableColumn
ctdlswLocalNBFilterSrcName = _CtdlswLocalNBFilterSrcName_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 8, 3, 1, 1, 1),
    _CtdlswLocalNBFilterSrcName_Type()
)
ctdlswLocalNBFilterSrcName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctdlswLocalNBFilterSrcName.setStatus("mandatory")
_CtdlswLocalNBFilterDestName_Type = NBName
_CtdlswLocalNBFilterDestName_Object = MibTableColumn
ctdlswLocalNBFilterDestName = _CtdlswLocalNBFilterDestName_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 8, 3, 1, 1, 2),
    _CtdlswLocalNBFilterDestName_Type()
)
ctdlswLocalNBFilterDestName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctdlswLocalNBFilterDestName.setStatus("mandatory")


class _CtdlswLocalNBFilterControl_Type(Integer32):
    """Custom type ctdlswLocalNBFilterControl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("create", 2),
          ("delete", 3),
          ("other", 1))
    )


_CtdlswLocalNBFilterControl_Type.__name__ = "Integer32"
_CtdlswLocalNBFilterControl_Object = MibTableColumn
ctdlswLocalNBFilterControl = _CtdlswLocalNBFilterControl_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 8, 3, 1, 1, 3),
    _CtdlswLocalNBFilterControl_Type()
)
ctdlswLocalNBFilterControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctdlswLocalNBFilterControl.setStatus("mandatory")
_CtdlswRemoteNBFilterTable_Object = MibTable
ctdlswRemoteNBFilterTable = _CtdlswRemoteNBFilterTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 8, 3, 2)
)
if mibBuilder.loadTexts:
    ctdlswRemoteNBFilterTable.setStatus("mandatory")
_CtdlswRemoteNBFilterEntry_Object = MibTableRow
ctdlswRemoteNBFilterEntry = _CtdlswRemoteNBFilterEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 8, 3, 2, 1)
)
ctdlswRemoteNBFilterEntry.setIndexNames(
    (0, "CTRON-DLSW-MIB", "ctdlswRemoteNBFilterSrcName"),
    (0, "CTRON-DLSW-MIB", "ctdlswRemoteNBFilterDestName"),
)
if mibBuilder.loadTexts:
    ctdlswRemoteNBFilterEntry.setStatus("mandatory")
_CtdlswRemoteNBFilterSrcName_Type = NBName
_CtdlswRemoteNBFilterSrcName_Object = MibTableColumn
ctdlswRemoteNBFilterSrcName = _CtdlswRemoteNBFilterSrcName_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 8, 3, 2, 1, 1),
    _CtdlswRemoteNBFilterSrcName_Type()
)
ctdlswRemoteNBFilterSrcName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctdlswRemoteNBFilterSrcName.setStatus("mandatory")
_CtdlswRemoteNBFilterDestName_Type = NBName
_CtdlswRemoteNBFilterDestName_Object = MibTableColumn
ctdlswRemoteNBFilterDestName = _CtdlswRemoteNBFilterDestName_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 8, 3, 2, 1, 2),
    _CtdlswRemoteNBFilterDestName_Type()
)
ctdlswRemoteNBFilterDestName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctdlswRemoteNBFilterDestName.setStatus("mandatory")


class _CtdlswRemoteNBFilterControl_Type(Integer32):
    """Custom type ctdlswRemoteNBFilterControl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("create", 2),
          ("delete", 3),
          ("other", 1))
    )


_CtdlswRemoteNBFilterControl_Type.__name__ = "Integer32"
_CtdlswRemoteNBFilterControl_Object = MibTableColumn
ctdlswRemoteNBFilterControl = _CtdlswRemoteNBFilterControl_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 8, 3, 2, 1, 3),
    _CtdlswRemoteNBFilterControl_Type()
)
ctdlswRemoteNBFilterControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctdlswRemoteNBFilterControl.setStatus("mandatory")
_CtdlswLocalMacFilterTable_Object = MibTable
ctdlswLocalMacFilterTable = _CtdlswLocalMacFilterTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 8, 3, 3)
)
if mibBuilder.loadTexts:
    ctdlswLocalMacFilterTable.setStatus("mandatory")
_CtdlswLocalMacFilterEntry_Object = MibTableRow
ctdlswLocalMacFilterEntry = _CtdlswLocalMacFilterEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 8, 3, 3, 1)
)
ctdlswLocalMacFilterEntry.setIndexNames(
    (0, "CTRON-DLSW-MIB", "ctdlswLocalMacFilterSrcAddr"),
    (0, "CTRON-DLSW-MIB", "ctdlswLocalMacFilterSrcMask"),
    (0, "CTRON-DLSW-MIB", "ctdlswLocalMacFilterDestAddr"),
    (0, "CTRON-DLSW-MIB", "ctdlswLocalMacFilterDestMask"),
)
if mibBuilder.loadTexts:
    ctdlswLocalMacFilterEntry.setStatus("mandatory")
_CtdlswLocalMacFilterSrcAddr_Type = MacAddress
_CtdlswLocalMacFilterSrcAddr_Object = MibTableColumn
ctdlswLocalMacFilterSrcAddr = _CtdlswLocalMacFilterSrcAddr_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 8, 3, 3, 1, 1),
    _CtdlswLocalMacFilterSrcAddr_Type()
)
ctdlswLocalMacFilterSrcAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctdlswLocalMacFilterSrcAddr.setStatus("mandatory")
_CtdlswLocalMacFilterSrcMask_Type = MacAddress
_CtdlswLocalMacFilterSrcMask_Object = MibTableColumn
ctdlswLocalMacFilterSrcMask = _CtdlswLocalMacFilterSrcMask_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 8, 3, 3, 1, 2),
    _CtdlswLocalMacFilterSrcMask_Type()
)
ctdlswLocalMacFilterSrcMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctdlswLocalMacFilterSrcMask.setStatus("mandatory")
_CtdlswLocalMacFilterDestAddr_Type = MacAddress
_CtdlswLocalMacFilterDestAddr_Object = MibTableColumn
ctdlswLocalMacFilterDestAddr = _CtdlswLocalMacFilterDestAddr_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 8, 3, 3, 1, 3),
    _CtdlswLocalMacFilterDestAddr_Type()
)
ctdlswLocalMacFilterDestAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctdlswLocalMacFilterDestAddr.setStatus("mandatory")
_CtdlswLocalMacFilterDestMask_Type = MacAddress
_CtdlswLocalMacFilterDestMask_Object = MibTableColumn
ctdlswLocalMacFilterDestMask = _CtdlswLocalMacFilterDestMask_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 8, 3, 3, 1, 4),
    _CtdlswLocalMacFilterDestMask_Type()
)
ctdlswLocalMacFilterDestMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctdlswLocalMacFilterDestMask.setStatus("mandatory")


class _CtdlswLocalMacFilterControl_Type(Integer32):
    """Custom type ctdlswLocalMacFilterControl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("create", 2),
          ("delete", 3),
          ("other", 1))
    )


_CtdlswLocalMacFilterControl_Type.__name__ = "Integer32"
_CtdlswLocalMacFilterControl_Object = MibTableColumn
ctdlswLocalMacFilterControl = _CtdlswLocalMacFilterControl_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 8, 3, 3, 1, 5),
    _CtdlswLocalMacFilterControl_Type()
)
ctdlswLocalMacFilterControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctdlswLocalMacFilterControl.setStatus("mandatory")
_CtdlswRemoteMacFilterTable_Object = MibTable
ctdlswRemoteMacFilterTable = _CtdlswRemoteMacFilterTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 8, 3, 4)
)
if mibBuilder.loadTexts:
    ctdlswRemoteMacFilterTable.setStatus("mandatory")
_CtdlswRemoteMacFilterEntry_Object = MibTableRow
ctdlswRemoteMacFilterEntry = _CtdlswRemoteMacFilterEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 8, 3, 4, 1)
)
ctdlswRemoteMacFilterEntry.setIndexNames(
    (0, "CTRON-DLSW-MIB", "ctdlswRemoteMacFilterSrcAddr"),
    (0, "CTRON-DLSW-MIB", "ctdlswRemoteMacFilterSrcMask"),
    (0, "CTRON-DLSW-MIB", "ctdlswRemoteMacFilterDestAddr"),
    (0, "CTRON-DLSW-MIB", "ctdlswRemoteMacFilterDestMask"),
)
if mibBuilder.loadTexts:
    ctdlswRemoteMacFilterEntry.setStatus("mandatory")
_CtdlswRemoteMacFilterSrcAddr_Type = MacAddress
_CtdlswRemoteMacFilterSrcAddr_Object = MibTableColumn
ctdlswRemoteMacFilterSrcAddr = _CtdlswRemoteMacFilterSrcAddr_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 8, 3, 4, 1, 1),
    _CtdlswRemoteMacFilterSrcAddr_Type()
)
ctdlswRemoteMacFilterSrcAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctdlswRemoteMacFilterSrcAddr.setStatus("mandatory")
_CtdlswRemoteMacFilterSrcMask_Type = MacAddress
_CtdlswRemoteMacFilterSrcMask_Object = MibTableColumn
ctdlswRemoteMacFilterSrcMask = _CtdlswRemoteMacFilterSrcMask_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 8, 3, 4, 1, 2),
    _CtdlswRemoteMacFilterSrcMask_Type()
)
ctdlswRemoteMacFilterSrcMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctdlswRemoteMacFilterSrcMask.setStatus("mandatory")
_CtdlswRemoteMacFilterDestAddr_Type = MacAddress
_CtdlswRemoteMacFilterDestAddr_Object = MibTableColumn
ctdlswRemoteMacFilterDestAddr = _CtdlswRemoteMacFilterDestAddr_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 8, 3, 4, 1, 3),
    _CtdlswRemoteMacFilterDestAddr_Type()
)
ctdlswRemoteMacFilterDestAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctdlswRemoteMacFilterDestAddr.setStatus("mandatory")
_CtdlswRemoteMacFilterDestMask_Type = MacAddress
_CtdlswRemoteMacFilterDestMask_Object = MibTableColumn
ctdlswRemoteMacFilterDestMask = _CtdlswRemoteMacFilterDestMask_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 8, 3, 4, 1, 4),
    _CtdlswRemoteMacFilterDestMask_Type()
)
ctdlswRemoteMacFilterDestMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctdlswRemoteMacFilterDestMask.setStatus("mandatory")


class _CtdlswRemoteMacFilterControl_Type(Integer32):
    """Custom type ctdlswRemoteMacFilterControl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("create", 2),
          ("delete", 3),
          ("other", 1))
    )


_CtdlswRemoteMacFilterControl_Type.__name__ = "Integer32"
_CtdlswRemoteMacFilterControl_Object = MibTableColumn
ctdlswRemoteMacFilterControl = _CtdlswRemoteMacFilterControl_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 8, 3, 4, 1, 5),
    _CtdlswRemoteMacFilterControl_Type()
)
ctdlswRemoteMacFilterControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctdlswRemoteMacFilterControl.setStatus("mandatory")
_CtdlswTConn_ObjectIdentity = ObjectIdentity
ctdlswTConn = _CtdlswTConn_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 8, 4)
)
_CtdlswTConnTable_Object = MibTable
ctdlswTConnTable = _CtdlswTConnTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 8, 4, 1)
)
if mibBuilder.loadTexts:
    ctdlswTConnTable.setStatus("mandatory")
_CtdlswTConnEntry_Object = MibTableRow
ctdlswTConnEntry = _CtdlswTConnEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 8, 4, 1, 1)
)
ctdlswTConnEntry.setIndexNames(
    (0, "CTRON-DLSW-MIB", "ctdlswTConnRemoteTAddr"),
)
if mibBuilder.loadTexts:
    ctdlswTConnEntry.setStatus("mandatory")
_CtdlswTConnRemoteTAddr_Type = IpAddress
_CtdlswTConnRemoteTAddr_Object = MibTableColumn
ctdlswTConnRemoteTAddr = _CtdlswTConnRemoteTAddr_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 8, 4, 1, 1, 1),
    _CtdlswTConnRemoteTAddr_Type()
)
ctdlswTConnRemoteTAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctdlswTConnRemoteTAddr.setStatus("mandatory")


class _CtdlswTConnControl_Type(Integer32):
    """Custom type ctdlswTConnControl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("create", 2),
          ("delete", 3),
          ("other", 1))
    )


_CtdlswTConnControl_Type.__name__ = "Integer32"
_CtdlswTConnControl_Object = MibTableColumn
ctdlswTConnControl = _CtdlswTConnControl_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 8, 4, 1, 1, 2),
    _CtdlswTConnControl_Type()
)
ctdlswTConnControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctdlswTConnControl.setStatus("mandatory")
_CtdlswTConnUpTime_Type = TimeTicks
_CtdlswTConnUpTime_Object = MibTableColumn
ctdlswTConnUpTime = _CtdlswTConnUpTime_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 8, 4, 1, 1, 3),
    _CtdlswTConnUpTime_Type()
)
ctdlswTConnUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctdlswTConnUpTime.setStatus("mandatory")


class _CtdlswTConnOperStatus_Type(Integer32):
    """Custom type ctdlswTConnOperStatus based on Integer32"""
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
        *(("disabled", 2),
          ("enabled", 3),
          ("other", 1),
          ("pendingDisable", 4),
          ("pendingEnable", 5))
    )


_CtdlswTConnOperStatus_Type.__name__ = "Integer32"
_CtdlswTConnOperStatus_Object = MibTableColumn
ctdlswTConnOperStatus = _CtdlswTConnOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 8, 4, 1, 1, 4),
    _CtdlswTConnOperStatus_Type()
)
ctdlswTConnOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctdlswTConnOperStatus.setStatus("mandatory")


class _CtdlswTConnType_Type(Integer32):
    """Custom type ctdlswTConnType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("configured", 1),
          ("dynamic", 2))
    )


_CtdlswTConnType_Type.__name__ = "Integer32"
_CtdlswTConnType_Object = MibTableColumn
ctdlswTConnType = _CtdlswTConnType_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 8, 4, 1, 1, 5),
    _CtdlswTConnType_Type()
)
ctdlswTConnType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctdlswTConnType.setStatus("mandatory")
_CtdlswTrap_ObjectIdentity = ObjectIdentity
ctdlswTrap = _CtdlswTrap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 8, 5)
)
_CtdlswEvent_ObjectIdentity = ObjectIdentity
ctdlswEvent = _CtdlswEvent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 8, 6)
)
_CtdlswEventLogConfig_ObjectIdentity = ObjectIdentity
ctdlswEventLogConfig = _CtdlswEventLogConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 8, 6, 1)
)


class _CtdlswEventAdminStatus_Type(Integer32):
    """Custom type ctdlswEventAdminStatus based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 3),
          ("other", 1))
    )


_CtdlswEventAdminStatus_Type.__name__ = "Integer32"
_CtdlswEventAdminStatus_Object = MibScalar
ctdlswEventAdminStatus = _CtdlswEventAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 8, 6, 1, 1),
    _CtdlswEventAdminStatus_Type()
)
ctdlswEventAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctdlswEventAdminStatus.setStatus("mandatory")


class _CtdlswEventMaxEntries_Type(Integer32):
    """Custom type ctdlswEventMaxEntries based on Integer32"""
    defaultValue = 100


_CtdlswEventMaxEntries_Object = MibScalar
ctdlswEventMaxEntries = _CtdlswEventMaxEntries_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 8, 6, 1, 2),
    _CtdlswEventMaxEntries_Type()
)
ctdlswEventMaxEntries.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctdlswEventMaxEntries.setStatus("mandatory")


class _CtdlswEventTraceAll_Type(Integer32):
    """Custom type ctdlswEventTraceAll based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 3),
          ("other", 1))
    )


_CtdlswEventTraceAll_Type.__name__ = "Integer32"
_CtdlswEventTraceAll_Object = MibScalar
ctdlswEventTraceAll = _CtdlswEventTraceAll_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 8, 6, 1, 3),
    _CtdlswEventTraceAll_Type()
)
ctdlswEventTraceAll.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctdlswEventTraceAll.setStatus("mandatory")
_CtdlswEventLogFilterTable_ObjectIdentity = ObjectIdentity
ctdlswEventLogFilterTable = _CtdlswEventLogFilterTable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 8, 6, 2)
)
_CtdlswEventFilterTable_Object = MibTable
ctdlswEventFilterTable = _CtdlswEventFilterTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 8, 6, 2, 1)
)
if mibBuilder.loadTexts:
    ctdlswEventFilterTable.setStatus("mandatory")
_CtdlswEventFilterEntry_Object = MibTableRow
ctdlswEventFilterEntry = _CtdlswEventFilterEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 8, 6, 2, 1, 1)
)
ctdlswEventFilterEntry.setIndexNames(
    (0, "CTRON-DLSW-MIB", "ctdlswEventFltrProtocol"),
    (0, "CTRON-DLSW-MIB", "ctdlswEventFltrIfNum"),
)
if mibBuilder.loadTexts:
    ctdlswEventFilterEntry.setStatus("mandatory")
_CtdlswEventFltrProtocol_Type = Integer32
_CtdlswEventFltrProtocol_Object = MibTableColumn
ctdlswEventFltrProtocol = _CtdlswEventFltrProtocol_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 8, 6, 2, 1, 1, 1),
    _CtdlswEventFltrProtocol_Type()
)
ctdlswEventFltrProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctdlswEventFltrProtocol.setStatus("mandatory")
_CtdlswEventFltrIfNum_Type = Integer32
_CtdlswEventFltrIfNum_Object = MibTableColumn
ctdlswEventFltrIfNum = _CtdlswEventFltrIfNum_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 8, 6, 2, 1, 1, 2),
    _CtdlswEventFltrIfNum_Type()
)
ctdlswEventFltrIfNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctdlswEventFltrIfNum.setStatus("mandatory")


class _CtdlswEventFltrControl_Type(Integer32):
    """Custom type ctdlswEventFltrControl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("add", 3),
          ("delete", 2),
          ("other", 1))
    )


_CtdlswEventFltrControl_Type.__name__ = "Integer32"
_CtdlswEventFltrControl_Object = MibTableColumn
ctdlswEventFltrControl = _CtdlswEventFltrControl_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 8, 6, 2, 1, 1, 3),
    _CtdlswEventFltrControl_Type()
)
ctdlswEventFltrControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctdlswEventFltrControl.setStatus("mandatory")


class _CtdlswEventFltrType_Type(Integer32):
    """Custom type ctdlswEventFltrType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4,
              8,
              16,
              32)
        )
    )
    namedValues = NamedValues(
        *(("error", 32),
          ("event", 16),
          ("misc", 1),
          ("rcv", 4),
          ("timer", 2),
          ("xmit", 8))
    )


_CtdlswEventFltrType_Type.__name__ = "Integer32"
_CtdlswEventFltrType_Object = MibTableColumn
ctdlswEventFltrType = _CtdlswEventFltrType_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 8, 6, 2, 1, 1, 4),
    _CtdlswEventFltrType_Type()
)
ctdlswEventFltrType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctdlswEventFltrType.setStatus("mandatory")


class _CtdlswEventFltrSeverity_Type(Integer32):
    """Custom type ctdlswEventFltrSeverity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("highest", 1),
          ("highlow", 3),
          ("highmed", 2))
    )


_CtdlswEventFltrSeverity_Type.__name__ = "Integer32"
_CtdlswEventFltrSeverity_Object = MibTableColumn
ctdlswEventFltrSeverity = _CtdlswEventFltrSeverity_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 8, 6, 2, 1, 1, 5),
    _CtdlswEventFltrSeverity_Type()
)
ctdlswEventFltrSeverity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctdlswEventFltrSeverity.setStatus("mandatory")


class _CtdlswEventFltrAction_Type(Integer32):
    """Custom type ctdlswEventFltrAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("log", 1),
          ("logTrap", 3),
          ("trap", 2))
    )


_CtdlswEventFltrAction_Type.__name__ = "Integer32"
_CtdlswEventFltrAction_Object = MibTableColumn
ctdlswEventFltrAction = _CtdlswEventFltrAction_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 8, 6, 2, 1, 1, 6),
    _CtdlswEventFltrAction_Type()
)
ctdlswEventFltrAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctdlswEventFltrAction.setStatus("mandatory")
_CtdlswEventLogTable_ObjectIdentity = ObjectIdentity
ctdlswEventLogTable = _CtdlswEventLogTable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 8, 6, 3)
)
_CtdlswEventTable_Object = MibTable
ctdlswEventTable = _CtdlswEventTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 8, 6, 3, 1)
)
if mibBuilder.loadTexts:
    ctdlswEventTable.setStatus("mandatory")
_CtdlswEventEntry_Object = MibTableRow
ctdlswEventEntry = _CtdlswEventEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 8, 6, 3, 1, 1)
)
ctdlswEventEntry.setIndexNames(
    (0, "CTRON-DLSW-MIB", "ctdlswEventNumber"),
)
if mibBuilder.loadTexts:
    ctdlswEventEntry.setStatus("mandatory")
_CtdlswEventNumber_Type = Integer32
_CtdlswEventNumber_Object = MibTableColumn
ctdlswEventNumber = _CtdlswEventNumber_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 8, 6, 3, 1, 1, 1),
    _CtdlswEventNumber_Type()
)
ctdlswEventNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctdlswEventNumber.setStatus("mandatory")
_CtdlswEventTime_Type = TimeTicks
_CtdlswEventTime_Object = MibTableColumn
ctdlswEventTime = _CtdlswEventTime_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 8, 6, 3, 1, 1, 2),
    _CtdlswEventTime_Type()
)
ctdlswEventTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctdlswEventTime.setStatus("mandatory")


class _CtdlswEventType_Type(Integer32):
    """Custom type ctdlswEventType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4,
              8,
              16,
              32)
        )
    )
    namedValues = NamedValues(
        *(("error", 32),
          ("event", 16),
          ("misc", 1),
          ("rcv", 4),
          ("timer", 2),
          ("xmit", 8))
    )


_CtdlswEventType_Type.__name__ = "Integer32"
_CtdlswEventType_Object = MibTableColumn
ctdlswEventType = _CtdlswEventType_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 8, 6, 3, 1, 1, 3),
    _CtdlswEventType_Type()
)
ctdlswEventType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctdlswEventType.setStatus("mandatory")


class _CtdlswEventSeverity_Type(Integer32):
    """Custom type ctdlswEventSeverity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("highest", 1),
          ("highlow", 3),
          ("highmed", 2))
    )


_CtdlswEventSeverity_Type.__name__ = "Integer32"
_CtdlswEventSeverity_Object = MibTableColumn
ctdlswEventSeverity = _CtdlswEventSeverity_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 8, 6, 3, 1, 1, 4),
    _CtdlswEventSeverity_Type()
)
ctdlswEventSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctdlswEventSeverity.setStatus("mandatory")
_CtdlswEventProtocol_Type = Integer32
_CtdlswEventProtocol_Object = MibTableColumn
ctdlswEventProtocol = _CtdlswEventProtocol_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 8, 6, 3, 1, 1, 5),
    _CtdlswEventProtocol_Type()
)
ctdlswEventProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctdlswEventProtocol.setStatus("mandatory")
_CtdlswEventIfNum_Type = Integer32
_CtdlswEventIfNum_Object = MibTableColumn
ctdlswEventIfNum = _CtdlswEventIfNum_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 8, 6, 3, 1, 1, 6),
    _CtdlswEventIfNum_Type()
)
ctdlswEventIfNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctdlswEventIfNum.setStatus("mandatory")
_CtdlswEventTextString_Type = OctetString
_CtdlswEventTextString_Object = MibTableColumn
ctdlswEventTextString = _CtdlswEventTextString_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 8, 6, 3, 1, 1, 7),
    _CtdlswEventTextString_Type()
)
ctdlswEventTextString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctdlswEventTextString.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CTRON-DLSW-MIB",
    **{"NBName": NBName,
       "ctdlswNode": ctdlswNode,
       "ctdlswNodeConfig": ctdlswNodeConfig,
       "ctdlswVersion": ctdlswVersion,
       "ctdlswAdminStatus": ctdlswAdminStatus,
       "ctdlswOperStatus": ctdlswOperStatus,
       "ctdlswUpTime": ctdlswUpTime,
       "ctdlswOperVirtualRingNumber": ctdlswOperVirtualRingNumber,
       "ctdlswNBLocalFilterType": ctdlswNBLocalFilterType,
       "ctdlswNBRemoteFilterType": ctdlswNBRemoteFilterType,
       "ctdlswMacLocalFilterType": ctdlswMacLocalFilterType,
       "ctdlswMacRemoteFilterType": ctdlswMacRemoteFilterType,
       "ctdlswAcceptDynamicTConn": ctdlswAcceptDynamicTConn,
       "ctdlswDefaultPortNumber": ctdlswDefaultPortNumber,
       "ctdlswPort": ctdlswPort,
       "ctdlswPortTable": ctdlswPortTable,
       "ctdlswPortEntry": ctdlswPortEntry,
       "ctdlswPortIndex": ctdlswPortIndex,
       "ctdlswPortName": ctdlswPortName,
       "ctdlswPortAddress": ctdlswPortAddress,
       "ctdlswPortAdminStatus": ctdlswPortAdminStatus,
       "ctdlswPortOperStatus": ctdlswPortOperStatus,
       "ctdlswPortUpTime": ctdlswPortUpTime,
       "ctdlswFilter": ctdlswFilter,
       "ctdlswLocalNBFilterTable": ctdlswLocalNBFilterTable,
       "ctdlswLocalNBFilterEntry": ctdlswLocalNBFilterEntry,
       "ctdlswLocalNBFilterSrcName": ctdlswLocalNBFilterSrcName,
       "ctdlswLocalNBFilterDestName": ctdlswLocalNBFilterDestName,
       "ctdlswLocalNBFilterControl": ctdlswLocalNBFilterControl,
       "ctdlswRemoteNBFilterTable": ctdlswRemoteNBFilterTable,
       "ctdlswRemoteNBFilterEntry": ctdlswRemoteNBFilterEntry,
       "ctdlswRemoteNBFilterSrcName": ctdlswRemoteNBFilterSrcName,
       "ctdlswRemoteNBFilterDestName": ctdlswRemoteNBFilterDestName,
       "ctdlswRemoteNBFilterControl": ctdlswRemoteNBFilterControl,
       "ctdlswLocalMacFilterTable": ctdlswLocalMacFilterTable,
       "ctdlswLocalMacFilterEntry": ctdlswLocalMacFilterEntry,
       "ctdlswLocalMacFilterSrcAddr": ctdlswLocalMacFilterSrcAddr,
       "ctdlswLocalMacFilterSrcMask": ctdlswLocalMacFilterSrcMask,
       "ctdlswLocalMacFilterDestAddr": ctdlswLocalMacFilterDestAddr,
       "ctdlswLocalMacFilterDestMask": ctdlswLocalMacFilterDestMask,
       "ctdlswLocalMacFilterControl": ctdlswLocalMacFilterControl,
       "ctdlswRemoteMacFilterTable": ctdlswRemoteMacFilterTable,
       "ctdlswRemoteMacFilterEntry": ctdlswRemoteMacFilterEntry,
       "ctdlswRemoteMacFilterSrcAddr": ctdlswRemoteMacFilterSrcAddr,
       "ctdlswRemoteMacFilterSrcMask": ctdlswRemoteMacFilterSrcMask,
       "ctdlswRemoteMacFilterDestAddr": ctdlswRemoteMacFilterDestAddr,
       "ctdlswRemoteMacFilterDestMask": ctdlswRemoteMacFilterDestMask,
       "ctdlswRemoteMacFilterControl": ctdlswRemoteMacFilterControl,
       "ctdlswTConn": ctdlswTConn,
       "ctdlswTConnTable": ctdlswTConnTable,
       "ctdlswTConnEntry": ctdlswTConnEntry,
       "ctdlswTConnRemoteTAddr": ctdlswTConnRemoteTAddr,
       "ctdlswTConnControl": ctdlswTConnControl,
       "ctdlswTConnUpTime": ctdlswTConnUpTime,
       "ctdlswTConnOperStatus": ctdlswTConnOperStatus,
       "ctdlswTConnType": ctdlswTConnType,
       "ctdlswTrap": ctdlswTrap,
       "ctdlswEvent": ctdlswEvent,
       "ctdlswEventLogConfig": ctdlswEventLogConfig,
       "ctdlswEventAdminStatus": ctdlswEventAdminStatus,
       "ctdlswEventMaxEntries": ctdlswEventMaxEntries,
       "ctdlswEventTraceAll": ctdlswEventTraceAll,
       "ctdlswEventLogFilterTable": ctdlswEventLogFilterTable,
       "ctdlswEventFilterTable": ctdlswEventFilterTable,
       "ctdlswEventFilterEntry": ctdlswEventFilterEntry,
       "ctdlswEventFltrProtocol": ctdlswEventFltrProtocol,
       "ctdlswEventFltrIfNum": ctdlswEventFltrIfNum,
       "ctdlswEventFltrControl": ctdlswEventFltrControl,
       "ctdlswEventFltrType": ctdlswEventFltrType,
       "ctdlswEventFltrSeverity": ctdlswEventFltrSeverity,
       "ctdlswEventFltrAction": ctdlswEventFltrAction,
       "ctdlswEventLogTable": ctdlswEventLogTable,
       "ctdlswEventTable": ctdlswEventTable,
       "ctdlswEventEntry": ctdlswEventEntry,
       "ctdlswEventNumber": ctdlswEventNumber,
       "ctdlswEventTime": ctdlswEventTime,
       "ctdlswEventType": ctdlswEventType,
       "ctdlswEventSeverity": ctdlswEventSeverity,
       "ctdlswEventProtocol": ctdlswEventProtocol,
       "ctdlswEventIfNum": ctdlswEventIfNum,
       "ctdlswEventTextString": ctdlswEventTextString}
)
